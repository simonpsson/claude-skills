#!/usr/bin/env python
"""
sv3d.py — Stable Video 3D: orbital video from a single image, via the cloud.

This is the NON-LOCAL path for stabilityai/sv3d. The model is gated + GPU-heavy and
this machine has no CUDA GPU, so we call a hosted Space that already has the weights:
    gubernac/sv3d-space  ->  endpoint /run_sv3d
which takes one image and returns an orbital novel-view VIDEO (mp4).

Input image: works best on a SINGLE centered object; use --remove-bg to cut the
background first. Square images are ideal (SV3D renders a 360° orbit).

Auth: set HF_TOKEN (Read token) in the environment, or pass --token.

Examples:
  python sv3d.py --image C:\\path\\object.png --remove-bg
  python sv3d.py --image https://example.com/chair.png --version sv3d_p --elevation 0
  python sv3d.py --list-api          # show the Space's endpoint signature
"""
import argparse
import datetime as _dt
import os
import re
import shutil
import sys
import time

SPACE = "gubernac/sv3d-space"
API_NAME = "/run_sv3d"
_VID_EXTS = (".mp4", ".webm", ".gif", ".mov", ".mkv")


def _slug(text, n=40):
    s = re.sub(r"[^a-zA-Z0-9]+", "-", (text or "sv3d").strip().lower()).strip("-")
    return (s[:n] or "sv3d").rstrip("-")


def _resolve_token(cli_token):
    return cli_token or os.environ.get("HF_TOKEN") or os.environ.get("HUGGING_FACE_HUB_TOKEN")


def _find_media(result, exts):
    """Walk an arbitrary gradio result and return the first local file with a wanted ext."""
    stack = [result]
    while stack:
        item = stack.pop(0)
        if isinstance(item, str):
            if item.lower().endswith(exts) and os.path.exists(item):
                return item
        elif isinstance(item, dict):
            for key in ("video", "path", "name", "url"):
                if key in item and item[key]:
                    stack.append(item[key])
        elif isinstance(item, (list, tuple)):
            stack.extend(item)
    return None


def main():
    p = argparse.ArgumentParser(description="SV3D orbital video from a single image (cloud).")
    p.add_argument("--image", help="input image: local path or URL (single centered object works best)")
    p.add_argument("--version", choices=["sv3d_u", "sv3d_p"], default="sv3d_u",
                   help="sv3d_u = fixed orbit; sv3d_p = elevation-conditioned orbit")
    p.add_argument("--elevation", type=float, default=10.0, help="elevation_deg (sv3d_p)")
    p.add_argument("--steps", type=int, default=30, help="num diffusion steps")
    p.add_argument("--seed", type=int, default=23)
    p.add_argument("--remove-bg", action="store_true", help="strip the background before orbiting")
    p.add_argument("--out", help="output file or dir (default: Claude\\generated-videos\\)")
    p.add_argument("--space", default=SPACE, help=f"Space id to call (default {SPACE}; use your GPU-backed copy)")
    p.add_argument("--token", help="HF token (else uses HF_TOKEN env var)")
    p.add_argument("--list-api", action="store_true", help="print the Space's API and exit")
    args = p.parse_args()

    try:
        from gradio_client import Client, handle_file
    except ImportError:
        sys.exit("gradio_client not installed. Run: pip install gradio_client")

    token = _resolve_token(args.token)
    print(f"[*] Connecting to Space: {args.space}" + ("  (with HF token)" if token else "  (anonymous)"))
    try:
        client = Client(args.space, token=token)
    except Exception as e:
        sys.exit(f"[!] Could not connect to {args.space}: {e}")

    if args.list_api:
        client.view_api()
        return
    if not args.image:
        p.error("--image is required (unless --list-api)")

    # gradio_client.handle_file wraps a local path OR a URL into the expected FileData.
    image_arg = handle_file(args.image)
    print(f"[*] Image: {args.image}")
    print(f"[*] version={args.version} elevation={args.elevation} steps={args.steps} "
          f"seed={args.seed} remove_bg={args.remove_bg}")
    print("[*] SV3D renders a full orbit — this is slow; be patient.")

    attempts = 4
    result = None
    for attempt in range(1, attempts + 1):
        try:
            result = client.predict(
                image_arg, args.version, args.elevation, args.steps,
                args.seed, args.remove_bg, api_name=API_NAME,
            )
            break
        except Exception as e:
            msg = str(e); etype = type(e).__name__; low = msg.lower()
            transient = ("no gpu" in low or "gpu was available" in low
                         or "gpu is currently" in low or "queue" in low or "503" in low)
            if transient and attempt < attempts:
                print(f"[*] GPU busy (attempt {attempt}/{attempts}) - retrying in 12s...")
                time.sleep(12)
                continue
            hint = ""
            if "requires gpu" in low or "assign a gpu" in low or "gpu hardware" in low:
                hint = ("\n    -> The Space has NO GPU assigned (it's on CPU), so SV3D can't run there. "
                        "Duplicate it to your account and assign a paid GPU (Space Settings -> Hardware), "
                        "then re-run with --space <your-copy>. Free ZeroGPU does not apply.")
            elif "no gpu" in low or "quota" in low or "zerogpu" in low or "queue" in low:
                hint = "\n    -> ZeroGPU availability: couldn't get a GPU in time. Retry, or HF PRO for priority."
            elif etype == "AppError":
                hint = "\n    -> SERVER-SIDE error inside the Space (not your input). Retry later."
            sys.exit(f"[!] SV3D failed: {etype}: {e}{hint}")

    vid = _find_media(result, _VID_EXTS)
    if not vid:
        sys.exit(f"[!] No video found in result. Raw result was:\n{result!r}")

    default_dir = os.path.join(os.path.expanduser("~"), "Claude", "generated-videos")
    ext = os.path.splitext(vid)[1] or ".mp4"
    stamp = _dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    fname = f"{stamp}-{_slug(os.path.basename(args.image))}-sv3d{ext}"
    if args.out:
        out = args.out
        if os.path.isdir(out) or out.endswith(("\\", "/")):
            os.makedirs(out, exist_ok=True); out = os.path.join(out, fname)
        else:
            os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    else:
        os.makedirs(default_dir, exist_ok=True); out = os.path.join(default_dir, fname)

    shutil.copyfile(vid, out)
    print(f"[OK] Saved: {out}")


if __name__ == "__main__":
    main()
