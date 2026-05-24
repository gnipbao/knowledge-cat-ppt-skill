#!/usr/bin/env python3
"""Run bundled Knowledge Cat PPT checks."""

from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run(cmd: list[str]) -> int:
    print("$ " + " ".join(cmd))
    completed = subprocess.run(cmd, cwd=ROOT)
    return completed.returncode


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Knowledge Cat PPT validation checks.")
    parser.add_argument(
        "--skip-sample-html",
        action="store_true",
        help="Do not initialize and validate the temporary sample HTML deck.",
    )
    args = parser.parse_args()

    checks = [
        [sys.executable, "scripts/validate_deck_plan.py", "examples/sample-deck-plan.json"],
    ]

    if not args.skip_sample_html:
        temp = Path(tempfile.mkdtemp(prefix="knowledge-cat-html-"))
        checks.append([sys.executable, "scripts/init_deck_project.py", str(temp), "--title", "Knowledge Cat Sample"])
        checks.append([sys.executable, "scripts/validate_html_deck.py", str(temp / "index.html")])

    checks.append([sys.executable, "scripts/check_repo.py"])

    for cmd in checks:
        code = run(cmd)
        if code:
            return code

    print("All Knowledge Cat PPT checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
