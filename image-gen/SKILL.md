---
name: image-gen
description: Generate images from a text prompt via Hugging Face. Use WHENEVER the user asks to create/generate/make/render an image, picture, illustration, artwork, logo, or visual from a description (e.g. "generate an image of...", "make a picture of...", "render...", "/image-gen"), AND whenever you yourself decide an image would help. ALWAYS asks which engine to use (flux.1-krea-dev, z-image-turbo, krea-official, qwen-image) before generating. Requires the Hugging Face MCP server (authenticated) for the MCP engines and HF_TOKEN for the official gradio_client engines.
---

# image-gen

Generate images from text prompts using Hugging Face. Works both when the user explicitly asks and when you decide an image would help.

## HARD RULE — always ask the engine first

**Before generating anything, you MUST ask the user which engine to use via `AskUserQuestion`.** This applies on EVERY invocation — including when you triggered the skill yourself, autonomously. Never silently pick an engine. The only exception: the user named a specific engine in their request (then use that one and skip the question).

Present these four options every time:

| Engine | Route | Token? | Notes |
|--------|-------|--------|-------|
| `flux.1-krea-dev` | MCP `dynamic_space` → `prithivMLmods/FLUX-REALISM` | none | Krea-dev via the authenticated MCP session. Solid default. |
| `z-image-turbo` | MCP pinned tool `gr1_z_image_turbo_generate` | none | Fastest (8 steps). Good for drafts. |
| `krea-official` | `generate_image.py` (gradio_client) → `black-forest-labs/FLUX.1-Krea-dev` | **HF_TOKEN** | The literal official Krea Space. |
| `qwen-image` | `generate_image.py` (gradio_client) → `Qwen/Qwen-Image` | **HF_TOKEN** | The official Qwen-Image Space. Strong at text-in-image. |

If you want, also ask for a resolution/aspect ratio in the same `AskUserQuestion` call (optional — default 1024×1024).

## Quota flag (state it before the first generation of a session)

All engines run on Hugging Face **ZeroGPU**, which is quota-metered, not money-billed. Free tier = small daily allowance; PRO ≈ 25× more. When quota is spent you get a "quota exceeded / GPU busy" error — not a charge. The two MCP engines spend the authenticated session's quota; the two official engines spend the `HF_TOKEN` owner's quota.

## Procedure

### 1. Ask the engine (HARD RULE above). Then generate by route:

**MCP route — `flux.1-krea-dev`:** call `mcp__plugin_huggingface-skills_huggingface-skills__dynamic_space` with:
```json
{"operation":"invoke","space_name":"prithivMLmods/FLUX-REALISM",
 "parameters":"{\"prompt\":\"<PROMPT>\",\"model_choice\":\"flux.1-krea-dev\",\"use_negative_prompt\":false,\"negative_prompt\":\"\",\"num_images\":1,\"num_inference_steps\":28,\"guidance_scale\":4.5,\"width\":1024,\"height\":1024,\"randomize_seed\":true,\"style_name\":\"Style Zero\",\"zip_images\":false}"}
```
> `negative_prompt` MUST be present even though it's marked optional, or the call errors.

**MCP route — `z-image-turbo`:** call `mcp__plugin_huggingface-skills_huggingface-skills__gr1_z_image_turbo_generate` with `{"prompt":"<PROMPT>","resolution":"1024x1024 ( 1:1 )"}`.

Both MCP routes return a Gradio file **URL** that is **ephemeral** (lives on the Space replica's `/tmp/gradio/`). You MUST download it immediately — see step 2.

**gradio_client route — `krea-official` / `qwen-image`:** run the script with the venv Python (PowerShell):
```powershell
& "C:\Users\simon.pettersson\Claude\tools\image-gen\.venv\Scripts\python.exe" `
  "C:\Users\simon.pettersson\.claude\skills\image-gen\scripts\generate_image.py" `
  --engine <krea-official|qwen-image> --prompt "<PROMPT>"
```
The script reads `HF_TOKEN` from the environment, downloads the result, and prints `[OK] Saved: <path>`. If it reports a missing/expired token or ZeroGPU error, tell the user to set/refresh `HF_TOKEN` (a Read token from https://huggingface.co/settings/tokens). Add `--list-api` to debug a changed endpoint, `--out <path>` to choose the destination.

### 2. Save locally (MCP routes only)

The gradio_client script already saves. For the MCP routes, download the returned URL to `C:\Users\simon.pettersson\Claude\generated-images\` with a `YYYYMMDD-HHMMSS-<slug>-<engine>.png` name (PowerShell `Invoke-WebRequest -Uri <url> -OutFile <path>`). Create the folder if needed.

### 3. View and describe

`Read` the saved PNG so you can actually see it, then give the user the local path (as a clickable link) and a 1–2 sentence description of what was produced. Note the seed if returned (useful for reproducing).

## Setup (one-time per machine — only needed for the gradio_client engines)
The script lives in this skill at `scripts\generate_image.py` (so it travels via the claude-skills repo). The venv lives OUTSIDE the skill folder so `sync-skills.ps1` doesn't delete it. To (re)create it on a fresh machine:
```powershell
py -3.12 -m venv "C:\Users\simon.pettersson\Claude\tools\image-gen\.venv"
& "C:\Users\simon.pettersson\Claude\tools\image-gen\.venv\Scripts\python.exe" -m pip install -r `
  "C:\Users\simon.pettersson\.claude\skills\image-gen\scripts\requirements.txt"
```
Then set a Read token: `setx HF_TOKEN "hf_..."` and restart the app so child processes inherit it.

## Notes
- MCP engines require the `huggingface-skills` MCP server to be authenticated (OAuth as the HF user). If its tools aren't loaded, the user must authenticate it first. MCP engines do NOT use HF_TOKEN — they ride the authenticated session.
- The official Space ids can change ownership; `generate_image.py` accepts `--space <author/name>` to override, and `--list-api` to discover the current endpoint signature.
- Canonical script: `~\.claude\skills\image-gen\scripts\generate_image.py`. Venv: `~\Claude\tools\image-gen\.venv`. Output: `~\Claude\generated-images\`.
