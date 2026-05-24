#!/usr/bin/env python3
"""Validate a Knowledge Cat deck-plan JSON file without third-party deps."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


REQUIRED_DECK_FIELDS = {
    "title",
    "audience",
    "outcome",
    "output_lane",
    "format",
    "slide_count",
}

REQUIRED_SLIDE_FIELDS = {
    "number",
    "action_title",
    "role",
    "key_message",
    "visual",
}

VALID_LANES = {
    "native-pptx",
    "html-deck",
    "image-first-pptx",
    "review-only",
}

WEAK_TOPIC_TITLES = {
    "agenda",
    "appendix",
    "background",
    "conclusion",
    "features",
    "introduction",
    "market overview",
    "overview",
    "problem",
    "results",
    "roadmap",
    "solution",
    "summary",
    "thank you",
}


def is_nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def has_action_language(title: str) -> bool:
    """Heuristic only: action titles should usually contain a claim."""

    stripped = title.strip()
    if len(stripped.split()) < 4:
        return False
    if stripped.lower() in WEAK_TOPIC_TITLES:
        return False
    return bool(re.search(r"[a-zA-Z0-9]", stripped))


def validate_plan(plan: Any) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not isinstance(plan, dict):
        return ["Plan must be a JSON object."], warnings

    deck = plan.get("deck")
    slides = plan.get("slides")

    if not isinstance(deck, dict):
        errors.append("Missing object: deck")
        deck = {}
    if not isinstance(slides, list):
        errors.append("Missing array: slides")
        slides = []

    missing_deck = sorted(REQUIRED_DECK_FIELDS - set(deck))
    if missing_deck:
        errors.append(f"deck missing required fields: {', '.join(missing_deck)}")

    for field in REQUIRED_DECK_FIELDS - {"slide_count"}:
        if field in deck and not is_nonempty_string(deck[field]):
            errors.append(f"deck.{field} must be a nonempty string")

    if deck.get("output_lane") and deck.get("output_lane") not in VALID_LANES:
        errors.append(
            "deck.output_lane must be one of: "
            + ", ".join(sorted(VALID_LANES))
        )

    if "slide_count" in deck:
        if not isinstance(deck["slide_count"], int) or deck["slide_count"] < 1:
            errors.append("deck.slide_count must be a positive integer")
        elif slides and deck["slide_count"] != len(slides):
            errors.append(
                f"deck.slide_count is {deck['slide_count']} but slides has {len(slides)} items"
            )

    seen_numbers: set[int] = set()
    previous_title = ""

    for index, slide in enumerate(slides, start=1):
        prefix = f"slides[{index}]"
        if not isinstance(slide, dict):
            errors.append(f"{prefix} must be an object")
            continue

        missing_slide = sorted(REQUIRED_SLIDE_FIELDS - set(slide))
        if missing_slide:
            errors.append(
                f"{prefix} missing required fields: {', '.join(missing_slide)}"
            )

        number = slide.get("number")
        if not isinstance(number, int) or number < 1:
            errors.append(f"{prefix}.number must be a positive integer")
        elif number in seen_numbers:
            errors.append(f"{prefix}.number duplicates slide {number}")
        else:
            seen_numbers.add(number)

        for field in REQUIRED_SLIDE_FIELDS - {"number"}:
            if field in slide and not is_nonempty_string(slide[field]):
                errors.append(f"{prefix}.{field} must be a nonempty string")

        title = str(slide.get("action_title", "")).strip()
        if title:
            if not has_action_language(title):
                warnings.append(
                    f"{prefix}.action_title may be a topic label, not an action title: {title!r}"
                )
            if title == previous_title:
                warnings.append(f"{prefix}.action_title repeats the previous slide title")
            previous_title = title

        evidence = slide.get("evidence")
        source_refs = slide.get("source_refs")
        if evidence is not None and not isinstance(evidence, list):
            errors.append(f"{prefix}.evidence must be an array when present")
        if source_refs is not None and not isinstance(source_refs, list):
            errors.append(f"{prefix}.source_refs must be an array when present")
        if evidence == [] and source_refs == []:
            warnings.append(f"{prefix} has no evidence or source references")

    if slides:
        expected = list(range(1, len(slides) + 1))
        actual = [slide.get("number") for slide in slides if isinstance(slide, dict)]
        if actual != expected:
            warnings.append(
                "Slide numbers are not sequential from 1 to N; confirm this is intentional"
            )

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Knowledge Cat deck-plan JSON.")
    parser.add_argument("plan", help="Path to deck-plan JSON")
    args = parser.parse_args()

    path = Path(args.plan)
    try:
        plan = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"Deck plan not found: {path}", file=sys.stderr)
        return 1
    except json.JSONDecodeError as exc:
        print(f"Invalid JSON: {exc}", file=sys.stderr)
        return 1

    errors, warnings = validate_plan(plan)
    for warning in warnings:
        print(f"WARNING: {warning}")
    if errors:
        print("Deck plan validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Deck plan validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
