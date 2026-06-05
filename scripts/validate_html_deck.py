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

REGISTERED_LAYOUTS = {
    "hero",
    "statement",
    "two-col",
    "evidence",
    "image-annotation",
    "closing-decision",
    "comparison",
    "timeline",
    "process",
    "system-map",
    "data-dashboard",
    "quote",
}

BUILT_IN_CLASS_LAYOUTS = {"hero", "statement", "two-col", "evidence"}

RATIO_RE = re.compile(
    r"(^|[-_])(?:21x9|16x10|16x9|4x3|1x1|3x4|3x2)($|[-_])|"
    r"(?:21:9|16:10|16:9|4:3|1:1|3:4|3:2)",
    re.IGNORECASE,
)

SLIDE_RE = re.compile(
    r"<section\b[^>]*class=[\"'][^\"']*\bslide\b[^\"']*[\"'][^>]*>[\s\S]*?</section>",
    re.IGNORECASE,
)

IMG_RE = re.compile(r"<img\b[^>]*>", re.IGNORECASE)

ATTR_RE = re.compile(r"([\w:-]+)\s*=\s*([\"'])(.*?)\2", re.DOTALL)

CJK_RE = re.compile(r"[\u4e00-\u9fff]")


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
    if CJK_RE.search(cleaned):
        return len(CJK_RE.findall(cleaned)) < 6
    return len(cleaned.split()) < 4


def parse_attrs(tag: str) -> dict[str, str]:
    return {match.group(1).lower(): match.group(3) for match in ATTR_RE.finditer(tag)}


def extract_slide_blocks(text: str) -> list[str]:
    text_without_comments = re.sub(r"<!--[\s\S]*?-->", "", text)
    return [match.group(0) for match in SLIDE_RE.finditer(text_without_comments)]


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
    slide_blocks = extract_slide_blocks(text)

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
        layout = slide.get("data-layout", "").strip()
        classes = set(slide.get("class", "").split())
        slide_html = slide_blocks[index - 1] if index - 1 < len(slide_blocks) else ""

        if not layout:
            errors.append(f"Slide {index} missing data-layout.")
        elif layout not in REGISTERED_LAYOUTS and not layout.startswith("custom-"):
            warnings.append(
                f"Slide {index} data-layout {layout!r} is not registered. "
                "Use a built-in layout or a custom-* name with explicit CSS."
            )
        elif layout in BUILT_IN_CLASS_LAYOUTS and layout not in classes:
            warnings.append(
                f"Slide {index} data-layout {layout!r} is not present in the slide class list."
            )

        if not title:
            errors.append(f"Slide {index} missing data-title.")
        elif weak_action_title(title):
            warnings.append(f"Slide {index} data-title may be too weak: {title!r}")
        if not role:
            errors.append(f"Slide {index} missing data-role.")
        if not theme:
            errors.append(f"Slide {index} missing data-theme.")
        elif theme not in {"light", "dark"}:
            errors.append(f"Slide {index} data-theme must be light or dark.")

        for img_index, img_tag in enumerate(IMG_RE.findall(slide_html), start=1):
            attrs = parse_attrs(img_tag)
            src = attrs.get("src", "")
            if not src.startswith(("images/", "./images/")):
                continue
            slot = attrs.get("data-image-slot", "").strip()
            slot_ratio = attrs.get("data-slot-ratio", "").strip()
            if not attrs.get("alt", "").strip():
                warnings.append(f"Slide {index} local image {img_index} is missing alt text.")
            if not slot:
                errors.append(f"Slide {index} local image {img_index} missing data-image-slot.")
            elif not RATIO_RE.search(slot) and not RATIO_RE.search(slot_ratio):
                warnings.append(
                    f"Slide {index} local image {img_index} slot {slot!r} does not declare a target ratio."
                )
            if re.search(r"border-radius\s*:|box-shadow\s*:", img_tag, re.IGNORECASE):
                warnings.append(
                    f"Slide {index} local image {img_index} has inline radius or shadow; confirm it matches the style package."
                )

        if re.search(r"<svg\b[\s\S]*?<text\b", slide_html, re.IGNORECASE):
            warnings.append(
                f"Slide {index} SVG contains <text>; HTML labels are usually easier to inspect and revise."
            )

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

    themes = [slide.get("data-theme", "").strip() for slide in parser.slides]
    valid_themes = [theme for theme in themes if theme in {"light", "dark"}]
    if len(valid_themes) >= 5:
        streak_theme = valid_themes[0]
        streak_start = 1
        streak_count = 1
        for offset, theme in enumerate(valid_themes[1:], start=2):
            if theme == streak_theme:
                streak_count += 1
                if streak_count == 3:
                    warnings.append(
                        f"Slides {streak_start}-{offset} use three consecutive {theme} themes."
                    )
            else:
                streak_theme = theme
                streak_start = offset
                streak_count = 1
    if len(valid_themes) >= 8:
        for theme in ("light", "dark"):
            if valid_themes.count(theme) < 2:
                warnings.append(f"Decks of 8+ slides should include at least two {theme} slides.")

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
