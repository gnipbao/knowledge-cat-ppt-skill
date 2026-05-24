#!/usr/bin/env python3
"""Install Knowledge Cat PPT into a local agent skill directory."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "knowledge-cat-ppt-skill"


def default_target(agent: str) -> Path:
    home = Path.home()
    if agent == "codex":
        return home / ".codex" / "skills" / SKILL_NAME
    if agent == "claude":
        return home / ".claude" / "skills" / SKILL_NAME
    raise ValueError(f"Unknown agent: {agent}")


def ignore(dirpath: str, names: list[str]) -> set[str]:
    ignored = {
        ".git",
        ".DS_Store",
        "__pycache__",
        ".pytest_cache",
    }
    return {name for name in names if name in ignored or name.endswith(".pyc")}


def main() -> int:
    parser = argparse.ArgumentParser(description="Install Knowledge Cat PPT as a local skill.")
    parser.add_argument("--agent", choices=["codex", "claude"], default="codex")
    parser.add_argument("--target", help="Override install target folder")
    parser.add_argument("--force", action="store_true", help="Overwrite an existing install")
    args = parser.parse_args()

    target = Path(args.target).expanduser().resolve() if args.target else default_target(args.agent)
    if target.exists():
        if not args.force:
            print(f"Target already exists: {target}", file=sys.stderr)
            print("Use --force to replace it.", file=sys.stderr)
            return 1
        shutil.rmtree(target)

    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(ROOT, target, ignore=ignore)
    print(f"Installed {SKILL_NAME} to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
