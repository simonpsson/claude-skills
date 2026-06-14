---
name: sv3d
description: Stable Video 3D (SV3D) — turn a SINGLE image of an object into an orbital novel-view VIDEO (image→video/3D). Use when the user wants to "orbit", "spin", "rotate", "see all sides of", or make a 360°/turntable video from an object image, or mentions SV3D / Stable Video 3D / stabilityai/sv3d. This is image→video, NOT text→image (for text→image use the image-gen skill). Runs in the cloud via a hosted Space and needs HF_TOKEN. NOTE: requires a GPU-backed SV3D Space — see the blocker below.
---

# sv3d

Stable Video 3D: input one image of a single object, output an orbital video showing it from many angles. The `stabilityai/sv3d` model is gated + GPU-heavy; this machine has no CUDA GPU, so we call a hosted Space rather than run it locally.

## ⚠️ Current blocker (state this before attempting)
The model's public demo Spaces are **not runnable** as of 2026-06-14:
- `gubernac/sv3d-space` — API is live (`/run_sv3d`) but the Space has **no GPU assigned** → fails with *"This Space requires GPU hardware."*
- `chenwang/physctrl` — in BUILD_ERROR.

So SV3D **cannot execute right now** on free infra. To actually run it, do ONE of:
1. **Duplicate `gubernac/sv3d-space` to your account and assign a paid GPU** (Space → Settings → Hardware, e.g. T4/L4/A10 ~ $0.40–1+/hr), then call with `--space <your-username>/sv3d-space`.
2. Point `--space` at any other GPU-backed SV3D Space.
3. Run the real `Stability-AI/generative-models` SV3D pipeline on a rented cloud GPU box.

The caller below is correct and ready — it just needs a GPU-backed Space behind it.

## How to run (once a GPU-backed Space exists)
```powershell
& "C:\Users\simon.pettersson\Claude\tools\image-gen\.venv\Scripts\python.exe" `
  "C:\Users\simon.pettersson\.claude\skills\sv3d\scripts\sv3d.py" `
  --image "<PATH-OR-URL>" --remove-bg [--space <gpu-backed-space>] [--version sv3d_u|sv3d_p] [--steps 30]
```
- **Input**: one image of a single, centered object. `--remove-bg` strips the background first (recommended). Square images orbit best.
- `--version`: `sv3d_u` (fixed orbit) or `sv3d_p` (elevation-conditioned; use `--elevation`).
- Reuses the **image-gen venv** (`Claude\tools\image-gen\.venv`, has `gradio_client`). Needs `HF_TOKEN`.
- Output: an `.mp4` saved to `C:\Users\simon.pettersson\Claude\generated-videos\`.
- The script auto-retries transient ZeroGPU queue errors and gives a clear hint for the "no GPU hardware" case.

## Notes
- SV3D is slow (renders a full 21-frame orbit) — expect minutes per run, and possible ZeroGPU time limits on shared hardware.
- If a frame source image isn't an object on a clean background, results degrade — generate/prepare a centered-object image first (e.g. via the `image-gen` skill, plain background).
- `--list-api` prints the Space's endpoint signature for debugging.
