#!/usr/bin/env python
"""
generate_image.py — generate images from the official Hugging Face Spaces via gradio_client.

This is the NON-MCP path: it talks directly to the official Gradio Spaces, so it can
reach Spaces that are not MCP-enabled (e.g. black-forest-labs/FLUX.1-Krea-dev, Qwen/Qwen-Image).

Engines:
  krea-official  -> black-forest-labs/FLUX.1-Krea-dev   (the real FLUX.1-Krea-dev)
  qwen-image     -> Qwen/Qwen-Image                      (the official Qwen-Image)

Auth: official Spaces run on ZeroGPU and need a Hugging Face token for reliable quota.
  Set HF_TOKEN in the environment (a "Read" token from https://huggingface.co/settings/tokens)
  or pass --token. Without a token the call may be rate-limited or rejected.

Examples:
  python generate_image.py --engine krea-official --prompt "a vibrant garden with a Victorian house"
  python generate_image.py --engine qwen-image --prompt "a neon cyberpunk alley" --out C:\\tmp\\qwen.png
  python generate_image.py --engine krea-official --list-api      # inspect the Space's endpoints
"""
import argparse
import datetime as _dt
import os
import re
import shutil
import sys

# Engine -> official Space id. Override per-call with --space.
ENGINES = {
    "krea-official": "black-forest-labs/FLUX.1-Krea-dev",
    "qwen-image": "Qwen/Qwen-Image",
}

# api_name candidates preferred in this order when none is given via --api-name.
_API_PREFERENCE = ["/infer", "/run", "/generate", "/predict", "/process"]

# file extensions we treat as the generated image.
_IMG_EXTS = (".png", ".jpg", ".jpeg", ".webp")


def _slug(text, n=40):
    s = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower()).strip("-")
    return (s[:n] or "image").rstrip("-")


def _resolve_token(cli_token):
    return cli_token or os.environ.get("HF_TOKEN") or os.environ.get("HUGGING_FACE_HUB_TOKEN")


def _pick_api_name(client, override):
    """Choose the inference endpoint: explicit override, else a sensible default."""
    if override:
        return override
    try:
        api = client.view_api(return_format="dict") or {}
        named = list((api.get("named_endpoints") or {}).keys())
    except Exception:
        named = []
    for pref in _API_PREFERENCE:
        if pref in named:
            return pref
    return named[0] if named else "/infer"


def _find_image(result):
    """Walk an arbitrary gradio result and return the first local image file path."""
    stack = [result]
    while stack:
        item = stack.pop(0)
        if isinstance(item, str):
            if item.lower().endswith(_IMG_EXTS) and os.path.exists(item):
                return item
        elif isinstance(item, dict):
            # gradio FileData dicts: {'path': ..., 'url': ...}
            for key in ("path", "name", "image", "url"):
                if key in item and item[key]:
                    stack.append(item[key])
        elif isinstance(item, (list, tuple)):
            stack.extend(item)
    return None


def main():
    p = argparse.ArgumentParser(description="Generate images from official HF Spaces via gradio_client.")
    p.add_argument("--engine", choices=sorted(ENGINES), help="which official Space to use")
    p.add_argument("--space", help="override: explicit Space id (author/name), ignores --engine mapping")
    p.add_argument("--prompt", help="text prompt")
    p.add_argument("--out", help="output file or directory (default: Claude\\generated-images\\)")
    p.add_argument("--api-name", help="override the Gradio endpoint name (e.g. /infer)")
    p.add_argument("--token", help="HF token (else uses HF_TOKEN env var)")
    p.add_argument("--list-api", action="store_true", help="print the Space's API endpoints and exit")
    args = p.parse_args()

    space = args.space or (ENGINES.get(args.engine) if args.engine else None)
    if not space:
        p.error("provide --engine {%s} or --space <id>" % ",".join(sorted(ENGINES)))

    try:
        from gradio_client import Client
    except ImportError:
        sys.exit("gradio_client not installed. Run: pip install gradio_client")

    token = _resolve_token(args.token)
    print(f"[*] Connecting to Space: {space}" + ("  (with HF token)" if token else "  (anonymous)"))
    try:
        client = Client(space, token=token)
    except Exception as e:
        sys.exit(f"[!] Could not connect to {space}: {e}")

    if args.list_api:
        client.view_api()  # prints a human-readable endpoint listing
        return

    if not args.prompt:
        p.error("--prompt is required (unless --list-api)")

    api_name = _pick_api_name(client, args.api_name)
    print(f"[*] Endpoint: {api_name}")
    print(f"[*] Prompt: {args.prompt}")
    try:
        # Pass only the prompt; gradio_client fills remaining inputs with the Space's
        # own component defaults. This is the version-robust minimal call.
        result = client.predict(args.prompt, api_name=api_name)
    except Exception as e:
        msg = str(e)
        hint = ""
        if "gpu" in msg.lower() or "quota" in msg.lower() or "zerogpu" in msg.lower():
            hint = "\n    -> Looks like a ZeroGPU quota/availability issue. Add/refresh HF_TOKEN, or retry later."
        elif "api_name" in msg.lower() or "endpoint" in msg.lower():
            hint = f"\n    -> Endpoint '{api_name}' may be wrong. Run with --list-api to see the real names, then pass --api-name."
        sys.exit(f"[!] Generation failed: {e}{hint}")

    img = _find_image(result)
    if not img:
        sys.exit(f"[!] No image found in result. Raw result was:\n{result!r}")

    # Resolve output path.
    default_dir = os.path.join(os.path.expanduser("~"), "Claude", "generated-images")
    ext = os.path.splitext(img)[1] or ".png"
    stamp = _dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    fname = f"{stamp}-{_slug(args.prompt)}-{args.engine or 'space'}{ext}"
    if args.out:
        out = args.out
        if os.path.isdir(out) or out.endswith(("\\", "/")):
            os.makedirs(out, exist_ok=True)
            out = os.path.join(out, fname)
        else:
            os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    else:
        os.makedirs(default_dir, exist_ok=True)
        out = os.path.join(default_dir, fname)

    shutil.copyfile(img, out)
    print(f"[OK] Saved: {out}")


if __name__ == "__main__":
    main()
