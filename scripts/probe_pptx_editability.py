#!/usr/bin/env python3
"""Prove that a native PPTX text object can be changed without flattening slides."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import sys
import tempfile
import zipfile
from pathlib import Path
from xml.etree import ElementTree


A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"
A_T = f"{{{A_NS}}}t"


def checksum(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def slide_text(xml_bytes: bytes) -> list[str]:
    root = ElementTree.fromstring(xml_bytes)
    return [(node.text or "") for node in root.iter(A_T)]


def mutate_package(source: Path, target: Path, search: str, replacement: str) -> tuple[str, int]:
    search_bytes = html.escape(search, quote=False).encode("utf-8")
    replacement_bytes = html.escape(replacement, quote=False).encode("utf-8")
    changed_slide = ""
    replacements = 0
    with zipfile.ZipFile(source) as src, zipfile.ZipFile(target, "w") as dst:
        for info in src.infolist():
            data = src.read(info.filename)
            if not changed_slide and info.filename.startswith("ppt/slides/slide") and info.filename.endswith(".xml"):
                count = data.count(search_bytes)
                if count:
                    data = data.replace(search_bytes, replacement_bytes, 1)
                    changed_slide = info.filename
                    replacements = 1
            dst.writestr(info, data)
    return changed_slide, replacements


def verify_mutation(path: Path, replacement: str) -> bool:
    with zipfile.ZipFile(path) as archive:
        if archive.testzip() is not None:
            return False
        for name in archive.namelist():
            if name.startswith("ppt/slides/slide") and name.endswith(".xml"):
                if replacement in slide_text(archive.read(name)):
                    return True
    return False


def run_probe(source: Path, search: str, replacement: str) -> dict[str, object]:
    if not source.exists():
        raise FileNotFoundError(f"PPTX not found: {source}")
    original_checksum = checksum(source)
    with tempfile.TemporaryDirectory(prefix="kc-pptx-edit-probe-") as temp:
        probe = Path(temp) / "probe.pptx"
        changed_slide, replacements = mutate_package(source, probe, search, replacement)
        passed = bool(changed_slide) and replacements == 1 and verify_mutation(probe, replacement)
        probe_checksum = checksum(probe)
    original_unchanged = checksum(source) == original_checksum
    return {
        "passed": passed and original_unchanged,
        "method": "copy PPTX -> mutate one native a:t text object -> reopen ZIP/XML -> verify replacement",
        "search": search,
        "replacement": replacement,
        "changed_slide_part": changed_slide,
        "replacement_count": replacements,
        "probe_package_valid": passed,
        "probe_file_retained": False,
        "original_unchanged": original_unchanged,
        "original_sha256": original_checksum,
        "probe_sha256": probe_checksum,
    }


def write_fixture(path: Path) -> None:
    slide = f"""<?xml version="1.0" encoding="UTF-8"?>
<p:sld xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:a="{A_NS}">
  <p:cSld><p:spTree><p:sp><p:txBody><a:p><a:r><a:t>Editable title</a:t></a:r></a:p></p:txBody></p:sp></p:spTree></p:cSld>
</p:sld>
"""
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("ppt/slides/slide1.xml", slide)


def self_test() -> int:
    with tempfile.TemporaryDirectory(prefix="kc-probe-test-") as temp:
        fixture = Path(temp) / "fixture.pptx"
        write_fixture(fixture)
        report = run_probe(fixture, "Editable title", "Edited title")
    if report["passed"] is not True:
        print(f"PPTX edit probe self-test failed: {report}", file=sys.stderr)
        return 1
    print("PPTX edit probe self-test passed.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a reversible text-object edit probe on a PPTX.")
    parser.add_argument("pptx", nargs="?", help="Path to .pptx")
    parser.add_argument("--search", default="Native objects survive the handoff")
    parser.add_argument("--replacement", default="Native objects survive the handoff · EDIT PROBE")
    parser.add_argument("--json-output")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    if not args.pptx:
        parser.error("pptx is required unless --self-test is used")
    try:
        report = run_probe(Path(args.pptx), args.search, args.replacement)
    except (FileNotFoundError, zipfile.BadZipFile, ElementTree.ParseError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    rendered = json.dumps(report, ensure_ascii=False, indent=2)
    print(rendered)
    if args.json_output:
        output = Path(args.json_output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered + "\n", encoding="utf-8")
    if report["passed"] is not True:
        return 1
    print("PPTX edit probe passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
