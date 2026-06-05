#!/usr/bin/env python3
"""Check that a production HTML case study includes QA artifacts."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


REQUIRED_FILES = [
    "index.html",
    "deck-plan.json",
    "qa-report.md",
    "screenshots/contact-sheet.svg",
]


def has_slide_screenshot(screenshots: Path) -> bool:
    if not screenshots.exists():
        return False
    for path in screenshots.iterdir():
        if path.name.startswith("slide-") and path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".svg"}:
            return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Check HTML benchmark QA artifacts.")
    parser.add_argument("case_dir", help="Path to an HTML case-study directory.")
    args = parser.parse_args()

    case_dir = Path(args.case_dir)
    errors: list[str] = []

    for rel in REQUIRED_FILES:
        if not (case_dir / rel).exists():
            errors.append(f"Missing required HTML QA artifact: {rel}")

    if not has_slide_screenshot(case_dir / "screenshots"):
        errors.append("Missing at least one slide screenshot artifact in screenshots/.")

    qa_report = case_dir / "qa-report.md"
    if qa_report.exists():
        text = qa_report.read_text(encoding="utf-8").lower()
        for marker in ["visual qa", "contact sheet", "fix loop", "known limitations"]:
            if marker not in text:
                errors.append(f"qa-report.md missing section marker: {marker}")

    if errors:
        print("HTML QA artifact check failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("HTML QA artifacts check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
