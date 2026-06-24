#!/usr/bin/env python3
"""Regenerate README.md from the actual skill folders.

Run after adding/removing/renaming a skill so the README never goes stale:

    python scripts/gen_readme.py

It scans every top-level folder containing a SKILL.md, reads each skill's
`name` and `description` from the YAML frontmatter (handling block scalars),
groups them by area, and writes a clean table to README.md. No template
placeholders, no hand-maintained counts.

Pure standard library — no dependencies.
"""
import re
import pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent

# A skill is grouped as "Full-stack development" if its frontmatter credits the
# upstream author (Jeffallan/claude-skills, MIT). Detected by marker, not a
# hardcoded list, so the grouping stays correct as skills come and go.
FULLSTACK_MARKER = "github.com/jeffallan"


def parse_frontmatter(text):
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
    if not m:
        return {}, ""
    block = m.group(1)
    lines = block.split("\n")
    data, i = {}, 0
    while i < len(lines):
        km = re.match(r"^([A-Za-z0-9_-]+):\s?(.*)$", lines[i])
        if km:
            key, val = km.group(1), km.group(2).strip()
            if val in (">", "|", ">-", "|-", ">+", "|+"):  # YAML block scalar
                collected, i = [], i + 1
                while i < len(lines) and (lines[i].strip() == "" or lines[i][:1] in (" ", "\t")):
                    collected.append(lines[i].strip())
                    i += 1
                data[key] = " ".join(x for x in collected if x).strip()
                continue
            data[key] = val.strip('"').strip("'")
        i += 1
    return data, block


def short(desc):
    desc = re.sub(r"\s+", " ", desc).strip()
    m = re.search(r"(.+?[.!?])(\s|$)", desc)
    s = m.group(1) if m else desc
    if len(s) > 220:
        s = s[:217].rstrip() + "..."
    return s.replace("|", "\\|")


def classify(folder, frontmatter_text):
    if FULLSTACK_MARKER in frontmatter_text.lower():
        return "Full-stack development"
    if folder.startswith("pbi") or "pbip" in folder:
        return "Power BI"
    if folder.startswith("gsd"):
        return "GSD project workflow"
    return "Analysis, BI & general"


def main():
    groups = {
        "Analysis, BI & general": [],
        "Power BI": [],
        "Full-stack development": [],
        "GSD project workflow": [],
    }
    total = 0
    for d in sorted(REPO.iterdir()):
        f = d / "SKILL.md"
        if not f.exists():
            continue
        text = f.read_text(encoding="utf-8", errors="replace")
        fm, fm_text = parse_frontmatter(text)
        name = fm.get("name", d.name)
        desc = short(fm.get("description", ""))
        groups[classify(d.name, fm_text)].append((d.name, name, desc))
        total += 1

    out = [
        "# claude-skills",
        "",
        f"A curated collection of **{total} [Claude Agent Skills](https://agentskills.io)**. "
        "Each skill is a folder with a `SKILL.md` plus any supporting `references/`, `scripts/`, or `assets/`.",
        "",
        "## Install",
        "",
        "**Claude Code** — copy a skill folder into your skills directory, then restart Claude Code:",
        "",
        "```bash",
        "git clone https://github.com/simonpsson/claude-skills.git",
        "cp -r claude-skills/<skill-name> ~/.claude/skills/",
        "```",
        "",
        "**Claude chat / Cowork** — zip a skill folder and upload it at "
        "claude.ai → Settings → Capabilities → Skills:",
        "",
        "```bash",
        "cd claude-skills && zip -r <skill-name>.zip <skill-name>",
        "```",
        "",
        "## Skills",
        "",
        f"{total} skills, grouped by area. Click a name for its `SKILL.md`. "
        "Regenerate this list with `python scripts/gen_readme.py`.",
    ]
    for title, items in groups.items():
        if not items:
            continue
        out += ["", f"### {title} ({len(items)})"]
        if title == "Full-stack development":
            out += [
                "",
                "> Added from [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) "
                "(MIT). See [ATTRIBUTION.md](ATTRIBUTION.md).",
            ]
        out += ["", "| Skill | Description |", "| --- | --- |"]
        for folder, name, desc in sorted(items):
            out.append(f"| [{name}]({folder}/SKILL.md) | {desc} |")

    out += [
        "",
        "## Attribution & license",
        "",
        "Skills retain their original `license` and `author` frontmatter. The full-stack "
        "development skills come from [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) "
        "(MIT) — full text in [`LICENSE-fullstack-dev-skills`](LICENSE-fullstack-dev-skills) and "
        "[`ATTRIBUTION.md`](ATTRIBUTION.md).",
        "",
    ]

    (REPO / "README.md").write_text("\n".join(out), encoding="utf-8")
    print(f"README regenerated: {total} skills")
    for title, items in groups.items():
        print(f"  {title}: {len(items)}")


if __name__ == "__main__":
    main()
