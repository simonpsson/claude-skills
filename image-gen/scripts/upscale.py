#!/usr/bin/env python
"""
upscale.py — enlarge / sharpen finished images for printing.

Methods:
  lanczos   (default, FREE, no GPU)  - high-quality Lanczos resize + mild sharpen.
                                       Best for PAINTINGS: enlarges without hallucinating
                                       new facial detail. Works even when ZeroGPU is out.
  pasd      (GPU, ZeroGPU)           - fffiloni/PASD diffusion super-resolution (adds detail;
                                       can alter faces - use on scenery, not portraits).
  superface (GPU, ZeroGPU)           - leonelhs/superface face restoration (sharpen real faces).

Examples:
  python upscale.py --image painting.webp --scale 3
  python upscale.py --dir "...\\stylized" --scale 2            # batch a whole folder
  python upscale.py --image p.webp --method superface          # GPU face restore
"""
import argparse
import os
import sys
import time

_IMG_EXTS = (".png", ".jpg", ".jpeg", ".webp")


def _resolve_token(t):
    return t or os.environ.get("HF_TOKEN") or os.environ.get("HUGGING_FACE_HUB_TOKEN")


def _outfile(src, outarg, suffix):
    base = os.path.splitext(os.path.basename(src))[0]
    fname = f"{base}-{suffix}.png"
    if outarg:
        if os.path.isdir(outarg) or outarg.endswith(("\\", "/")):
            os.makedirs(outarg, exist_ok=True)
            return os.path.join(outarg, fname)
        os.makedirs(os.path.dirname(os.path.abspath(outarg)), exist_ok=True)
        return outarg
    d = os.path.join(os.path.dirname(os.path.abspath(src)), "upscaled")
    os.makedirs(d, exist_ok=True)
    return os.path.join(d, fname)


def _lanczos(src, dst, scale):
    from PIL import Image, ImageFilter
    im = Image.open(src).convert("RGB")
    w, h = im.size
    big = im.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
    big = big.filter(ImageFilter.UnsharpMask(radius=2, percent=80, threshold=2))
    big.save(dst, "PNG")
    return big.size


def _find_image(result):
    stack = [result]
    while stack:
        it = stack.pop(0)
        if isinstance(it, str) and it.lower().endswith(_IMG_EXTS) and os.path.exists(it):
            return it
        if isinstance(it, dict):
            for k in ("path", "name", "url"):
                if it.get(k):
                    stack.append(it[k])
        elif isinstance(it, (list, tuple)):
            stack.extend(it)
    return None


def _gpu_upscale(src, dst, method, token, scale):
    from gradio_client import Client, handle_file
    if method == "pasd":
        space, api = "fffiloni/PASD", "/super_resolve_image"
        args = (handle_file(src), "", "clean, high-resolution, 8k, best quality, masterpiece",
                "blur, lowres, oversmooth, bad anatomy, worst quality, low quality",
                20, float(scale), 1.1, 7.5, 1435536528)
    else:  # superface
        space, api = "leonelhs/superface", "/predict"
        args = (handle_file(src),)
    client = Client(space, token=token)
    for attempt in range(1, 4):
        try:
            res = client.predict(*args, api_name=api)
            break
        except Exception as e:
            low = str(e).lower()
            if ("no gpu" in low or "queue" in low or "503" in low) and attempt < 3:
                print(f"[*] GPU busy ({attempt}/3) - retrying in 10s..."); time.sleep(10); continue
            sys.exit(f"[!] Upscale failed: {type(e).__name__}: {e}")
    img = _find_image(res)
    if not img:
        sys.exit(f"[!] No image in result: {res!r}")
    import shutil
    shutil.copyfile(img, dst)


def process(src, args, token):
    dst = _outfile(src, args.out, args.method if args.method != "lanczos" else f"x{args.scale}")
    if args.method == "lanczos":
        size = _lanczos(src, dst, args.scale)
        print(f"[OK] {os.path.basename(src)} -> {dst}  ({size[0]}x{size[1]})")
    else:
        _gpu_upscale(src, dst, args.method, token, args.scale)
        print(f"[OK] {os.path.basename(src)} -> {dst}  ({args.method})")


def main():
    p = argparse.ArgumentParser(description="Upscale/sharpen images for print.")
    p.add_argument("--image", help="single image path")
    p.add_argument("--dir", help="folder of images to batch-upscale")
    p.add_argument("--method", choices=["lanczos", "pasd", "superface"], default="lanczos")
    p.add_argument("--scale", type=float, default=2.0, help="enlargement factor (lanczos/pasd)")
    p.add_argument("--out", help="output file or directory")
    p.add_argument("--token", help="HF token (GPU methods)")
    args = p.parse_args()

    if not args.image and not args.dir:
        p.error("provide --image or --dir")
    token = _resolve_token(args.token)
    targets = []
    if args.image:
        targets.append(args.image)
    if args.dir:
        for f in sorted(os.listdir(args.dir)):
            if f.lower().endswith(_IMG_EXTS):
                targets.append(os.path.join(args.dir, f))
    if not targets:
        sys.exit("[!] No images found.")
    print(f"[*] Upscaling {len(targets)} image(s) via {args.method} (scale {args.scale})")
    for t in targets:
        process(t, args, token)


if __name__ == "__main__":
    main()
