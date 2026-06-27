#!/usr/bin/env python3
"""Inspect a PPTX package for native editable slide objects."""

from __future__ import annotations

import argparse
import json
import re
import sys
import tempfile
import zipfile
from pathlib import Path
from xml.etree import ElementTree


P_NS = "http://schemas.openxmlformats.org/presentationml/2006/main"
A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"
C_NS = "http://schemas.openxmlformats.org/drawingml/2006/chart"
P_SP = f"{{{P_NS}}}sp"
P_PIC = f"{{{P_NS}}}pic"
P_GRAPHIC_FRAME = f"{{{P_NS}}}graphicFrame"
A_T = f"{{{A_NS}}}t"
A_GRAPHIC_DATA = f"{{{A_NS}}}graphicData"
C_CHART = f"{{{C_NS}}}chart"
TABLE_URI = "http://schemas.openxmlformats.org/drawingml/2006/table"
CHART_URI = "http://schemas.openxmlformats.org/drawingml/2006/chart"
SLIDE_RE = re.compile(r"ppt/slides/slide(\d+)\.xml$")


def slide_number(name: str) -> int:
    match = SLIDE_RE.match(name)
    if not match:
        raise ValueError(name)
    return int(match.group(1))


def inspect_slide(xml_bytes: bytes, number: int) -> dict[str, object]:
    root = ElementTree.fromstring(xml_bytes)
    text_shapes = 0
    shapes = 0
    pictures = 0
    charts = 0
    tables = 0
    text_runs = 0

    for shape in root.iter(P_SP):
        shapes += 1
        runs = [node.text or "" for node in shape.iter(A_T) if (node.text or "").strip()]
        if runs:
            text_shapes += 1
            text_runs += len(runs)
    pictures = sum(1 for _ in root.iter(P_PIC))
    for frame in root.iter(P_GRAPHIC_FRAME):
        for graphic_data in frame.iter(A_GRAPHIC_DATA):
            uri = graphic_data.attrib.get("uri", "")
            if uri == TABLE_URI:
                tables += 1
            if uri == CHART_URI or any(True for _ in graphic_data.iter(C_CHART)):
                charts += 1

    return {
        "slide": number,
        "text_shapes": text_shapes,
        "text_runs": text_runs,
        "shapes": shapes,
        "pictures": pictures,
        "charts": charts,
        "tables": tables,
    }


def inspect_pptx(path: Path) -> dict[str, object]:
    if not path.exists():
        raise FileNotFoundError(f"PPTX not found: {path}")
    try:
        with zipfile.ZipFile(path) as archive:
            names = archive.namelist()
            slide_names = sorted((name for name in names if SLIDE_RE.match(name)), key=slide_number)
            if not slide_names:
                raise ValueError("No slide XML files found in PPTX package.")
            slides = [inspect_slide(archive.read(name), slide_number(name)) for name in slide_names]
            notes = sum(1 for name in names if re.match(r"ppt/notesSlides/notesSlide\d+\.xml$", name))
            chart_parts = sum(
                1
                for name in names
                if re.match(r"ppt/(?:charts|slides/charts)/chart\d+\.xml$", name)
            )
            media_parts = sum(1 for name in names if name.startswith("ppt/media/") and not name.endswith("/"))
    except zipfile.BadZipFile as exc:
        raise ValueError(f"Not a valid PPTX zip package: {path}") from exc

    totals = {
        key: sum(int(slide[key]) for slide in slides)
        for key in ("text_shapes", "text_runs", "shapes", "pictures", "charts", "tables")
    }
    return {
        "path": str(path),
        "slide_count": len(slides),
        "notes_count": notes,
        "chart_parts": chart_parts,
        "media_parts": media_parts,
        "totals": totals,
        "slides": slides,
    }


def evaluate(report: dict[str, object], args: argparse.Namespace) -> list[str]:
    errors: list[str] = []
    slides = report["slides"]
    assert isinstance(slides, list)
    totals = report["totals"]
    assert isinstance(totals, dict)

    if args.expected_slides and report["slide_count"] != args.expected_slides:
        errors.append(f"Expected {args.expected_slides} slides, found {report['slide_count']}")
    for slide in slides:
        if slide["text_shapes"] < args.min_text_shapes_per_slide:
            errors.append(
                f"Slide {slide['slide']} has {slide['text_shapes']} editable text shapes; "
                f"minimum is {args.min_text_shapes_per_slide}"
            )
        if args.fail_on_image_only_slides and slide["pictures"] > 0 and slide["text_shapes"] == 0:
            errors.append(f"Slide {slide['slide']} is image-only and does not prove native editability")
    if args.require_native_chart and totals["charts"] < 1:
        errors.append("No native chart object found")
    if args.require_native_table and totals["tables"] < 1:
        errors.append("No native table object found")
    if args.require_notes and report["notes_count"] < report["slide_count"]:
        errors.append(
            f"Expected notes for every slide; found {report['notes_count']} note parts for {report['slide_count']} slides"
        )
    return errors


def write_fixture(path: Path, *, image_only: bool) -> None:
    if image_only:
        body = "<p:pic/>"
    else:
        body = f"""
<p:sp><p:txBody><a:p><a:r><a:t>Editable title</a:t></a:r></a:p></p:txBody></p:sp>
<p:graphicFrame><a:graphic><a:graphicData uri="{TABLE_URI}"/></a:graphic></p:graphicFrame>
<p:graphicFrame><a:graphic><a:graphicData uri="{CHART_URI}"><c:chart/></a:graphicData></a:graphic></p:graphicFrame>
"""
    slide_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<p:sld xmlns:p="{P_NS}" xmlns:a="{A_NS}" xmlns:c="{C_NS}">
  <p:cSld><p:spTree>{body}</p:spTree></p:cSld>
</p:sld>
"""
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("ppt/slides/slide1.xml", slide_xml)
        if not image_only:
            archive.writestr("ppt/charts/chart1.xml", "<c:chartSpace xmlns:c=\"%s\"/>" % C_NS)
            archive.writestr("ppt/notesSlides/notesSlide1.xml", "<p:notes xmlns:p=\"%s\"/>" % P_NS)


def self_test() -> int:
    with tempfile.TemporaryDirectory(prefix="kc-editability-") as temp:
        positive = Path(temp) / "positive.pptx"
        negative = Path(temp) / "negative.pptx"
        write_fixture(positive, image_only=False)
        write_fixture(negative, image_only=True)
        positive_report = inspect_pptx(positive)
        negative_report = inspect_pptx(negative)

    positive_args = argparse.Namespace(
        expected_slides=1,
        min_text_shapes_per_slide=1,
        fail_on_image_only_slides=True,
        require_native_chart=True,
        require_native_table=True,
        require_notes=True,
    )
    negative_args = argparse.Namespace(
        expected_slides=1,
        min_text_shapes_per_slide=1,
        fail_on_image_only_slides=True,
        require_native_chart=False,
        require_native_table=False,
        require_notes=False,
    )
    if evaluate(positive_report, positive_args):
        print("Positive editability fixture failed", file=sys.stderr)
        return 1
    if not evaluate(negative_report, negative_args):
        print("Negative image-only fixture unexpectedly passed", file=sys.stderr)
        return 1
    print("PPTX editability checker self-test passed.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Check a PPTX for native editable objects.")
    parser.add_argument("pptx", nargs="?", help="Path to .pptx")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--expected-slides", type=int)
    parser.add_argument("--min-text-shapes-per-slide", type=int, default=1)
    parser.add_argument("--require-native-chart", action="store_true")
    parser.add_argument("--require-native-table", action="store_true")
    parser.add_argument("--require-notes", action="store_true")
    parser.add_argument("--fail-on-image-only-slides", action="store_true")
    parser.add_argument("--json-output", help="Write report JSON to this path")
    args = parser.parse_args()

    if args.self_test:
        return self_test()
    if not args.pptx:
        parser.error("pptx is required unless --self-test is used")
    try:
        report = inspect_pptx(Path(args.pptx))
    except (FileNotFoundError, ValueError, ElementTree.ParseError) as exc:
        print(str(exc), file=sys.stderr)
        return 1

    errors = evaluate(report, args)
    report["passed"] = not errors
    report["errors"] = errors
    rendered = json.dumps(report, ensure_ascii=False, indent=2)
    print(rendered)
    if args.json_output:
        output = Path(args.json_output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered + "\n", encoding="utf-8")
    if errors:
        return 1
    print("PPTX editability check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
