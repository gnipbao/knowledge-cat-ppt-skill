#!/usr/bin/env python3
"""Extract slide text from a PPTX file for placeholder and editability QA."""

from __future__ import annotations

import argparse
import json
import re
import sys
import tempfile
import zipfile
from pathlib import Path
from xml.etree import ElementTree


A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"
A_P = f"{{{A_NS}}}p"
A_T = f"{{{A_NS}}}t"

SLIDE_XML_RE = re.compile(r"ppt/slides/slide(\d+)\.xml$")
PLACEHOLDER_RE = re.compile(
    r"\b(?:x{3,}|lorem|ipsum|placeholder|todo)\b|"
    r"replace\s+with|"
    r"this\s+(?:page|slide)\s+layout",
    re.IGNORECASE,
)


def slide_number(name: str) -> int:
    match = SLIDE_XML_RE.match(name)
    if not match:
        raise ValueError(f"Not a slide XML path: {name}")
    return int(match.group(1))


def normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def extract_lines(xml_bytes: bytes) -> list[str]:
    try:
        root = ElementTree.fromstring(xml_bytes)
    except ElementTree.ParseError as exc:
        raise ValueError(f"Invalid slide XML: {exc}") from exc

    lines: list[str] = []
    for paragraph in root.iter(A_P):
        parts = [node.text or "" for node in paragraph.iter(A_T)]
        line = normalize_text("".join(parts))
        if line:
            lines.append(line)
    return lines


def extract_pptx_text(path: Path) -> list[dict[str, object]]:
    if not path.exists():
        raise FileNotFoundError(f"PPTX not found: {path}")
    if path.suffix.lower() != ".pptx":
        raise ValueError(f"Expected a .pptx file: {path}")

    try:
        with zipfile.ZipFile(path) as archive:
            slide_names = sorted(
                (name for name in archive.namelist() if SLIDE_XML_RE.match(name)),
                key=slide_number,
            )
            if not slide_names:
                raise ValueError("No ppt/slides/slide*.xml files found.")

            slides: list[dict[str, object]] = []
            for name in slide_names:
                number = slide_number(name)
                lines = extract_lines(archive.read(name))
                slides.append({"slide": number, "text": lines})
            return slides
    except zipfile.BadZipFile as exc:
        raise ValueError(f"Not a valid PPTX zip package: {path}") from exc


def find_placeholder_hits(slides: list[dict[str, object]]) -> list[str]:
    hits: list[str] = []
    for slide in slides:
        number = slide["slide"]
        for line in slide["text"]:
            if isinstance(line, str) and PLACEHOLDER_RE.search(line):
                hits.append(f"Slide {number}: {line}")
    return hits


def write_self_test_pptx(path: Path) -> None:
    slide_xml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="{A_NS}" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:cSld>
    <p:spTree>
      <p:sp>
        <p:txBody>
          <a:p><a:r><a:t>Launch evidence wins</a:t></a:r></a:p>
          <a:p><a:r><a:t>TODO remove marker</a:t></a:r></a:p>
        </p:txBody>
      </p:sp>
    </p:spTree>
  </p:cSld>
</p:sld>
"""
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("ppt/slides/slide1.xml", slide_xml)


def run_self_test() -> int:
    with tempfile.TemporaryDirectory(prefix="knowledge-cat-pptx-") as temp_dir:
        pptx_path = Path(temp_dir) / "fixture.pptx"
        write_self_test_pptx(pptx_path)
        slides = extract_pptx_text(pptx_path)

    lines = slides[0]["text"] if slides else []
    if lines != ["Launch evidence wins", "TODO remove marker"]:
        print(f"Unexpected self-test extraction: {lines!r}", file=sys.stderr)
        return 1
    hits = find_placeholder_hits(slides)
    if not hits or "TODO remove marker" not in hits[0]:
        print(f"Self-test did not detect placeholder text: {hits!r}", file=sys.stderr)
        return 1
    print("PPTX text extraction self-test passed.")
    return 0


def print_text(slides: list[dict[str, object]]) -> None:
    for slide in slides:
        print(f"Slide {int(slide['slide']):02d}")
        lines = slide["text"]
        if not lines:
            print("- [no extracted text]")
        else:
            for line in lines:
                print(f"- {line}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract editable text from a PPTX deck.")
    parser.add_argument("pptx", nargs="?", help="Path to the .pptx file")
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="Run a tiny in-memory PPTX extraction test and exit.",
    )
    parser.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        help="Output format. Defaults to text.",
    )
    parser.add_argument(
        "--fail-on-placeholders",
        action="store_true",
        help="Return a non-zero exit code if placeholder-like text is found.",
    )
    args = parser.parse_args()

    if args.self_test:
        return run_self_test()
    if not args.pptx:
        parser.error("pptx is required unless --self-test is used")

    try:
        slides = extract_pptx_text(Path(args.pptx))
    except (FileNotFoundError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1

    if args.format == "json":
        print(json.dumps({"slides": slides}, ensure_ascii=False, indent=2))
    else:
        print_text(slides)

    hits = find_placeholder_hits(slides)
    if hits:
        print("Placeholder-like text found:", file=sys.stderr)
        for hit in hits:
            print(f"- {hit}", file=sys.stderr)
        if args.fail_on_placeholders:
            return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
