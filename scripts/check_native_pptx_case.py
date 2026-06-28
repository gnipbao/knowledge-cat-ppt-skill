#!/usr/bin/env python3
"""Validate the bundled native PPTX benchmark case and evidence package."""

from __future__ import annotations

import argparse
import json
import struct
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_QA_SECTIONS = (
    "## Editable promises",
    "## Rendered QA",
    "## Fix loop",
    "## Known limitations",
)


def png_dimensions(path: Path) -> tuple[int, int]:
    data = path.read_bytes()[:24]
    if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"Not a valid PNG: {path}")
    return struct.unpack(">II", data[16:24])


def run(cmd: list[str]) -> int:
    print("$ " + " ".join(cmd))
    return subprocess.run(cmd, cwd=ROOT).returncode


def main() -> int:
    parser = argparse.ArgumentParser(description="Check a native PPTX case-study evidence package.")
    parser.add_argument(
        "case_dir",
        nargs="?",
        default="examples/case-studies/native-editable",
    )
    args = parser.parse_args()
    case = (ROOT / args.case_dir).resolve()
    plan_path = case / "deck-plan.json"
    pptx_path = case / "knowledge-cat-native-editable.pptx"
    inspection_path = case / "inspection.ndjson"
    editability_path = case / "editability-report.json"
    edit_probe_path = case / "edit-probe.json"
    qa_path = case / "qa-report.md"
    brief_path = case / "deck-brief.md"
    screenshot_dir = case / "screenshots"

    required = [
        plan_path,
        pptx_path,
        inspection_path,
        editability_path,
        edit_probe_path,
        qa_path,
        brief_path,
        screenshot_dir / "contact-sheet.png",
    ]
    errors = [f"Missing native case artifact: {path.relative_to(ROOT)}" for path in required if not path.exists()]
    if errors:
        print("Native PPTX case check failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    slide_count = plan.get("deck", {}).get("slide_count")
    if not isinstance(slide_count, int) or slide_count < 1:
        print("Native PPTX case has invalid slide_count", file=sys.stderr)
        return 1

    for number in range(1, slide_count + 1):
        preview = screenshot_dir / f"slide-{number:02d}.png"
        layout = screenshot_dir / f"slide-{number:02d}.layout.json"
        if not preview.exists():
            errors.append(f"Missing rendered preview: {preview.relative_to(ROOT)}")
        else:
            try:
                width, height = png_dimensions(preview)
                if width != 1280 or height != 720:
                    errors.append(f"Preview {preview.name} is {width}x{height}, expected 1280x720")
            except ValueError as exc:
                errors.append(str(exc))
        if not layout.exists():
            errors.append(f"Missing layout evidence: {layout.relative_to(ROOT)}")

    qa = qa_path.read_text(encoding="utf-8")
    for section in REQUIRED_QA_SECTIONS:
        if section not in qa:
            errors.append(f"qa-report.md missing section: {section}")
    inspection = inspection_path.read_text(encoding="utf-8").strip()
    if "chart" not in inspection or "table" not in inspection:
        errors.append("inspection.ndjson does not show both chart and table objects")
    editability = json.loads(editability_path.read_text(encoding="utf-8"))
    if editability.get("passed") is not True:
        errors.append("editability-report.json is not passing")
    edit_probe = json.loads(edit_probe_path.read_text(encoding="utf-8"))
    if edit_probe.get("passed") is not True or "mutate one native" not in edit_probe.get("method", ""):
        errors.append("edit-probe.json does not prove a reversible native-text object mutation")

    if errors:
        print("Native PPTX case check failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    checks = [
        [sys.executable, "scripts/validate_deck_plan.py", str(plan_path.relative_to(ROOT))],
        [sys.executable, "scripts/extract_pptx_text.py", str(pptx_path.relative_to(ROOT)), "--fail-on-placeholders"],
        [
            sys.executable,
            "scripts/check_pptx_editability.py",
            str(pptx_path.relative_to(ROOT)),
            "--expected-slides",
            str(slide_count),
            "--min-text-shapes-per-slide",
            "2",
            "--require-native-chart",
            "--require-native-table",
            "--require-notes",
            "--fail-on-image-only-slides",
        ],
        [
            sys.executable,
            "scripts/probe_pptx_editability.py",
            str(pptx_path.relative_to(ROOT)),
        ],
    ]
    for cmd in checks:
        if run(cmd):
            return 1

    print("Native PPTX case-study check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
