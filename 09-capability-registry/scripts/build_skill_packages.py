#!/usr/bin/env python3
"""Build host-specific skill directories from the portable canonical source."""

from __future__ import annotations

import argparse
import json
import shutil
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
CLAUDE_OVERLAYS = ROOT / "adapters" / "claude" / "overlays.json"
CHATGPT_INTERFACES = ROOT / "adapters" / "chatgpt" / "interfaces.json"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def frontmatter_value(skill_md: Path, key: str) -> str:
    lines = skill_md.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        raise ValueError(f"Missing frontmatter: {skill_md}")
    for line in lines[1:]:
        if line == "---":
            break
        if line.startswith(f"{key}:"):
            raw = line.split(":", 1)[1].strip()
            if raw.startswith('"'):
                return json.loads(raw)
            return raw.strip("'")
    raise ValueError(f"Missing {key}: {skill_md}")


def add_claude_overlay(skill_md: Path, overlay: dict) -> None:
    if not overlay:
        return
    lines = skill_md.read_text(encoding="utf-8").splitlines()
    closing = lines[1:].index("---") + 1
    additions = []
    for key, value in overlay.items():
        rendered = "true" if value is True else "false" if value is False else json.dumps(value)
        additions.append(f"{key}: {rendered}")
    lines[closing:closing] = additions
    skill_md.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_chatgpt_interface(skill_dir: Path, interface: dict) -> None:
    agents = skill_dir / "agents"
    agents.mkdir(exist_ok=True)
    lines = ["interface:"]
    for key in ("display_name", "short_description", "default_prompt"):
        lines.append(f"  {key}: {json.dumps(interface[key], ensure_ascii=False)}")
    lines.extend([
        "policy:",
        f"  allow_implicit_invocation: {'true' if interface['allow_implicit_invocation'] else 'false'}",
    ])
    (agents / "openai.yaml").write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_target(target: str, output_root: Path, make_zip: bool) -> None:
    overlays = load_json(CLAUDE_OVERLAYS)
    interfaces = load_json(CHATGPT_INTERFACES)
    target_root = output_root / target
    target_root.mkdir(parents=True, exist_ok=True)

    for source in sorted(path for path in SKILLS_ROOT.iterdir() if path.is_dir()):
        skill_md = source / "SKILL.md"
        name = frontmatter_value(skill_md, "name")
        description = frontmatter_value(skill_md, "description")
        if name != source.name:
            raise ValueError(f"Folder/name mismatch: {source.name} != {name}")
        if target == "claude" and len(name) > 64:
            raise ValueError(f"Claude skill name exceeds 64 characters: {name}")
        if target == "claude" and len(description) > 200:
            raise ValueError(
                f"Claude skill description exceeds 200 characters ({len(description)}): {name}"
            )
        destination = target_root / name
        if destination.exists():
            shutil.rmtree(destination)
        shutil.copytree(source, destination)

        if target == "claude":
            add_claude_overlay(destination / "SKILL.md", overlays.get(name, {}))
        elif target == "chatgpt":
            write_chatgpt_interface(destination, interfaces[name])
        else:
            raise ValueError(f"Unsupported target: {target}")

        if make_zip:
            archive = target_root / f"{name}.zip"
            if archive.exists():
                archive.unlink()
            with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as bundle:
                for file_path in sorted(destination.rglob("*")):
                    if file_path.is_file():
                        bundle.write(file_path, file_path.relative_to(target_root))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", choices=("claude", "chatgpt", "all"), default="all")
    parser.add_argument("--output", type=Path, default=ROOT / "dist")
    parser.add_argument("--zip", action="store_true", help="Also create one ZIP per skill")
    args = parser.parse_args()

    targets = ("claude", "chatgpt") if args.target == "all" else (args.target,)
    for target in targets:
        build_target(target, args.output.resolve(), args.zip)

    print(f"Built {', '.join(targets)} packages in {args.output.resolve()}")


if __name__ == "__main__":
    main()
