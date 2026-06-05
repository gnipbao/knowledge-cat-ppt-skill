#!/usr/bin/env python3
"""Check Knowledge Cat HTML signature packs and their case studies."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True

from validate_html_deck import extract_slide_blocks, parse_attrs, validate


ROOT = Path(__file__).resolve().parents[1]

PACKS = {
    "portfolio-minimal": {
        "pack_id": "kc-24-portfolio-minimal",
        "style_seed": "kc-24",
        "min_layouts": 12,
        "min_case_slides": 12,
        "min_unique_case_layouts": 12,
    }
}


def load_json(path: Path, errors: list[str]) -> dict:
    if not path.exists():
        errors.append(f"Missing JSON file: {path.relative_to(ROOT)}")
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}")
        return {}


def check_markers(path: Path, markers: list[str], errors: list[str]) -> None:
    if not path.exists():
        errors.append(f"Missing file: {path.relative_to(ROOT)}")
        return
    text = path.read_text(encoding="utf-8").lower()
    for marker in markers:
        if marker.lower() not in text:
            errors.append(f"{path.relative_to(ROOT)} missing marker: {marker}")


def check_pack(pack_name: str) -> list[str]:
    if pack_name not in PACKS:
        return [f"Unknown signature pack: {pack_name}"]

    config = PACKS[pack_name]
    errors: list[str] = []
    pack_dir = ROOT / "assets" / "html-signature-packs" / pack_name
    case_dir = ROOT / "examples" / "case-studies" / pack_name

    required_pack_files = ["README.md", "template.html", "layout-registry.json"]
    for rel in required_pack_files:
        if not (pack_dir / rel).exists():
            errors.append(f"Missing signature pack file: {pack_dir.relative_to(ROOT) / rel}")

    registry = load_json(pack_dir / "layout-registry.json", errors)
    layouts = registry.get("layouts", []) if isinstance(registry, dict) else []
    layout_ids = [item.get("layout") for item in layouts if isinstance(item, dict)]
    layout_classes = [item.get("class") for item in layouts if isinstance(item, dict)]

    if registry.get("pack") != config["pack_id"]:
        errors.append("layout-registry.json pack id does not match the expected signature pack id.")
    if registry.get("style_seed") != config["style_seed"]:
        errors.append("layout-registry.json style seed does not match the expected seed.")
    if len(layout_ids) < config["min_layouts"]:
        errors.append(f"Signature pack has {len(layout_ids)} layouts; expected at least {config['min_layouts']}.")

    template = pack_dir / "template.html"
    if template.exists():
        template_text = template.read_text(encoding="utf-8")
        if config["pack_id"] not in template_text:
            errors.append("template.html does not declare the pack id.")
        for class_name in layout_classes:
            if class_name and f".{class_name}" not in template_text:
                errors.append(f"template.html missing CSS class for registry class: {class_name}")

    required_case_files = [
        "deck-plan.json",
        "index.html",
        "qa-report.md",
        "screenshots/slide-01.svg",
        "screenshots/slide-01.png",
        "screenshots/contact-sheet.svg",
        "screenshots/contact-sheet.png",
        "screenshots/contact-sheet.html",
    ]
    for rel in required_case_files:
        if not (case_dir / rel).exists():
            errors.append(f"Missing case-study file: {case_dir.relative_to(ROOT) / rel}")

    plan = load_json(case_dir / "deck-plan.json", errors)
    deck = plan.get("deck", {}) if isinstance(plan, dict) else {}
    style_profile = deck.get("style_prompt_profile", {}) if isinstance(deck, dict) else {}
    if deck.get("output_lane") != "html-deck":
        errors.append("deck-plan.json output_lane must be html-deck for an HTML signature pack case.")
    if config["style_seed"] not in (style_profile.get("name", "") + " " + deck.get("design_posture", "")):
        errors.append("deck-plan.json does not bind the case study to the expected style seed.")

    html_path = case_dir / "index.html"
    if html_path.exists():
        validation_errors, validation_warnings = validate(html_path)
        errors.extend(f"HTML validation error: {error}" for error in validation_errors)
        errors.extend(f"HTML validation warning: {warning}" for warning in validation_warnings)

        html = html_path.read_text(encoding="utf-8")
        slide_blocks = extract_slide_blocks(html)
        if len(slide_blocks) < config["min_case_slides"]:
            errors.append(f"Case study has {len(slide_blocks)} slides; expected at least {config['min_case_slides']}.")

        used_layouts: set[str] = set()
        has_local_image_slot = False
        for index, block in enumerate(slide_blocks, start=1):
            attrs = parse_attrs(block.split(">", 1)[0] + ">")
            pack_id = attrs.get("data-pack", "")
            style_seed = attrs.get("data-style-seed", "")
            layout = attrs.get("data-layout", "")
            if pack_id != config["pack_id"]:
                errors.append(f"Slide {index} missing expected data-pack {config['pack_id']}.")
            if style_seed != config["style_seed"]:
                errors.append(f"Slide {index} missing expected data-style-seed {config['style_seed']}.")
            if layout not in layout_ids:
                errors.append(f"Slide {index} uses layout {layout!r} that is absent from layout-registry.json.")
            used_layouts.add(layout)
            if re.search(r"<img\b[^>]*src=[\"'](?:\./)?images/", block, re.IGNORECASE):
                if "data-image-slot=" in block and "data-slot-ratio=" in block:
                    has_local_image_slot = True

        if len(used_layouts) < config["min_unique_case_layouts"]:
            errors.append(
                f"Case study uses {len(used_layouts)} unique layouts; "
                f"expected at least {config['min_unique_case_layouts']}."
            )
        if not has_local_image_slot:
            errors.append("Case study does not include a local image with slot and ratio metadata.")

    for number in range(1, config["min_case_slides"] + 1):
        screenshot = case_dir / "screenshots" / f"slide-{number:02d}.png"
        if not screenshot.exists():
            errors.append(f"Missing browser-captured slide screenshot: {screenshot.relative_to(ROOT)}")
        elif screenshot.stat().st_size < 10_000:
            errors.append(f"Browser-captured screenshot looks too small: {screenshot.relative_to(ROOT)}")

    check_markers(
        case_dir / "qa-report.md",
        ["Visual QA", "Contact Sheet", "Fix Loop", "Known Limitations", "Browser capture", config["pack_id"]],
        errors,
    )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Check a Knowledge Cat HTML signature pack.")
    parser.add_argument("pack", nargs="?", default="portfolio-minimal", choices=sorted(PACKS))
    args = parser.parse_args()

    errors = check_pack(args.pack)
    if errors:
        print("Signature pack check failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Signature pack check passed: {args.pack}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
