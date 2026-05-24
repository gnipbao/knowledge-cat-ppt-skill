#!/usr/bin/env python3
"""Static checks for Knowledge Cat HTML decks."""

from __future__ import annotations

import argparse
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from typing import Any


PLACEHOLDERS = [
    "{{DECK_TITLE}}",
    "SLIDES_HERE",
    "lorem ipsum",
    "[placeholder]",
    "placeholder copy",
    "replace with",
    "todo",
]

WEAK_TITLES = {
    "agenda",
    "background",
    "conclusion",
    "introduction",
    "overview",
    "problem",
    "results",
    "roadmap",
    "solution",
    "summary",
    "thank you",
}


class SlideParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self.slides: list[dict[str, str]] = []
        self._in_title = False
        self._title_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_map = {key: value or "" for key, value in attrs}
        if tag == "title":
            self._in_title = True
        if tag == "section":
            classes = attrs_map.get("class", "")
            if "slide" in classes.split():
                self.slides.append(attrs_map)

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False
            self.title = "".join(self._title_parts).strip()

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self._title_parts.append(data)


def weak_action_title(title: str) -> bool:
    cleaned = re.sub(r"\s+", " ", title.strip().lower())
    if cleaned in WEAK_TITLES:
        return True
    return len(cleaned.split()) < 4


def load_plan_count(html_path: Path) -> int | None:
    plan_path = html_path.with_name("deck-plan.json")
    if not plan_path.exists():
        return None
    try:
        plan: Any = json.loads(plan_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None
    deck = plan.get("deck", {}) if isinstance(plan, dict) else {}
    count = deck.get("slide_count")
    return count if isinstance(count, int) else None


def validate(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    text = path.read_text(encoding="utf-8")

    parser = SlideParser()
    parser.feed(text)

    if not parser.title:
        errors.append("Missing <title>.")
    if parser.title in {"{{DECK_TITLE}}", "[Deck Title]", "Deck Title"}:
        errors.append("Deck title was not replaced.")

    lowered = text.lower()
    for marker in PLACEHOLDERS:
        if marker.lower() in lowered:
            errors.append(f"Unresolved placeholder marker: {marker}")

    if not parser.slides:
        errors.append("No <section class=\"slide\"> elements found.")

    for index, slide in enumerate(parser.slides, start=1):
        title = slide.get("data-title", "").strip()
        role = slide.get("data-role", "").strip()
        theme = slide.get("data-theme", "").strip()
        if not title:
            errors.append(f"Slide {index} missing data-title.")
        elif weak_action_title(title):
            warnings.append(f"Slide {index} data-title may be too weak: {title!r}")
        if not role:
            errors.append(f"Slide {index} missing data-role.")
        if theme and theme not in {"light", "dark"}:
            errors.append(f"Slide {index} data-theme must be light or dark.")

    plan_count = load_plan_count(path)
    if plan_count is not None and plan_count != len(parser.slides):
        errors.append(
            f"deck-plan.json slide_count is {plan_count}, but HTML has {len(parser.slides)} slides."
        )

    if len(parser.slides) > 1:
        titles = [slide.get("data-title", "").strip() for slide in parser.slides]
        for index in range(1, len(titles)):
            if titles[index] and titles[index] == titles[index - 1]:
                warnings.append(f"Slides {index} and {index + 1} repeat the same title.")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Knowledge Cat HTML deck.")
    parser.add_argument("html", help="Path to index.html")
    args = parser.parse_args()

    path = Path(args.html)
    if not path.exists():
        print(f"HTML deck not found: {path}", file=sys.stderr)
        return 1

    errors, warnings = validate(path)
    for warning in warnings:
        print(f"WARNING: {warning}")
    if errors:
        print("HTML deck validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("HTML deck validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
