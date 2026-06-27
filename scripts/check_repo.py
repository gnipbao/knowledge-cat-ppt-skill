#!/usr/bin/env python3
"""Repository hygiene checks for Knowledge Cat PPT."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "README_CN.md",
    "README_BILINGUAL.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CHANGELOG.md",
    "VERSION",
    ".gitignore",
    ".gitattributes",
    ".github/workflows/validate.yml",
    ".github/pull_request_template.md",
    ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/feature_request.yml",
    ".github/ISSUE_TEMPLATE/deck_quality_report.yml",
    "agents/openai.yaml",
    "assets/deck-plan.schema.json",
    "assets/html-template/index.html",
    "assets/html-signature-packs/portfolio-minimal/README.md",
    "assets/html-signature-packs/portfolio-minimal/template.html",
    "assets/html-signature-packs/portfolio-minimal/layout-registry.json",
    "examples/retest-prompts.md",
    "examples/sample-deck-plan.json",
    "examples/sample-html-deck/index.html",
    "examples/case-studies/html-benchmark/deck-plan.json",
    "examples/case-studies/html-benchmark/index.html",
    "examples/case-studies/html-benchmark/images/04-product-surface.svg",
    "examples/case-studies/html-benchmark/screenshots/slide-01.svg",
    "examples/case-studies/html-benchmark/screenshots/contact-sheet.svg",
    "examples/case-studies/html-benchmark/qa-report.md",
    "examples/case-studies/portfolio-minimal/deck-plan.json",
    "examples/case-studies/portfolio-minimal/index.html",
    "examples/case-studies/portfolio-minimal/images/04-pack-surface.svg",
    "examples/case-studies/portfolio-minimal/screenshots/slide-01.svg",
    "examples/case-studies/portfolio-minimal/screenshots/slide-01.png",
    "examples/case-studies/portfolio-minimal/screenshots/contact-sheet.svg",
    "examples/case-studies/portfolio-minimal/screenshots/contact-sheet.png",
    "examples/case-studies/portfolio-minimal/screenshots/contact-sheet.html",
    "examples/case-studies/portfolio-minimal/qa-report.md",
    "examples/case-studies/native-editable/deck-brief.md",
    "examples/case-studies/native-editable/deck-plan.json",
    "examples/case-studies/native-editable/knowledge-cat-native-editable.pptx",
    "examples/case-studies/native-editable/inspection.ndjson",
    "examples/case-studies/native-editable/editability-report.json",
    "examples/case-studies/native-editable/edit-probe.json",
    "examples/case-studies/native-editable/qa-report.md",
    "examples/case-studies/native-editable/screenshots/contact-sheet.png",
    "examples/case-studies/native-editable/screenshots/slide-01.png",
    "examples/case-studies/native-editable/screenshots/slide-01.layout.json",
    "examples/case-studies/native-editable/screenshots/slide-02.png",
    "examples/case-studies/native-editable/screenshots/slide-02.layout.json",
    "examples/case-studies/native-editable/screenshots/slide-03.png",
    "examples/case-studies/native-editable/screenshots/slide-03.layout.json",
    "examples/case-studies/native-editable/screenshots/slide-04.png",
    "examples/case-studies/native-editable/screenshots/slide-04.layout.json",
    "examples/case-studies/native-editable/screenshots/slide-05.png",
    "examples/case-studies/native-editable/screenshots/slide-05.layout.json",
    "examples/case-studies/native-editable/screenshots/slide-06.png",
    "examples/case-studies/native-editable/screenshots/slide-06.layout.json",
    "examples/failure-fixtures/html/missing-layout/index.html",
    "examples/failure-fixtures/html/missing-image-slot/index.html",
    "examples/failure-fixtures/html/unresolved-marker/index.html",
    "examples/failure-fixtures/html/slide-count-mismatch/deck-plan.json",
    "examples/failure-fixtures/html/slide-count-mismatch/index.html",
    "docs/images/mode-native-pptx.svg",
    "docs/images/mode-native-pptx.png",
    "docs/images/mode-html-deck.svg",
    "docs/images/mode-html-deck.png",
    "docs/images/mode-image-first.svg",
    "docs/images/mode-image-first.png",
    "references/benchmark-synthesis.md",
    "references/benchmark-quality-gates.md",
    "references/engine-routing.md",
    "references/story-architecture.md",
    "references/design-systems.md",
    "references/template-replication.md",
    "references/style-template-library.md",
    "references/html-visual-systems.md",
    "references/html-production-lock.md",
    "references/style-prompt-intake.md",
    "references/native-pptx-recipes.md",
    "references/html-deck-recipes.md",
    "references/image-first-recipes.md",
    "references/qa-rubric.md",
    "references/open-source-product.md",
    "scripts/check_failure_fixtures.py",
    "scripts/build_native_pptx.mjs",
    "scripts/check_pptx_editability.py",
    "scripts/probe_pptx_editability.py",
    "scripts/check_native_pptx_case.py",
    "scripts/extract_pptx_text.py",
    "scripts/init_deck_project.py",
    "scripts/install_skill.py",
    "scripts/run_checks.py",
    "scripts/check_html_qa_artifacts.py",
    "scripts/check_signature_pack.py",
    "scripts/validate_deck_plan.py",
    "scripts/validate_html_deck.py",
]

BANNED_DIR_NAMES = {
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "node_modules",
}

BANNED_FILE_PATTERNS = [
    re.compile(r".*\.pyc$"),
    re.compile(r".*\.log$"),
    re.compile(r".*\.tmp$"),
    re.compile(r".*\.bak$"),
    re.compile(r".*\.DS_Store$"),
    re.compile(r".*\.pptx\.inspect\.ndjson$"),
]


def is_text_file(path: Path) -> bool:
    return path.suffix.lower() in {
        ".md",
        ".py",
        ".yml",
        ".yaml",
        ".json",
        ".html",
        ".svg",
        ".mjs",
        ".ndjson",
        ".txt",
        ".cff",
        "",
    }


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            errors.append(f"Missing required file: {rel}")

    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip() if (ROOT / "VERSION").exists() else ""
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8") if (ROOT / "CHANGELOG.md").exists() else ""
    if version and f"## {version}" not in changelog:
        errors.append(f"CHANGELOG.md does not contain a section for VERSION {version}")

    for path in ROOT.rglob("*"):
        rel = path.relative_to(ROOT)
        if ".git" in rel.parts:
            continue
        if any(part in BANNED_DIR_NAMES for part in rel.parts):
            errors.append(f"Banned generated directory or cache path: {rel}")
        if path.is_file():
            rel_s = str(rel)
            if any(pattern.match(rel_s) for pattern in BANNED_FILE_PATTERNS):
                errors.append(f"Banned generated file: {rel}")
            if is_text_file(path):
                data = path.read_bytes()
                try:
                    text = data.decode("utf-8")
                except UnicodeDecodeError:
                    errors.append(f"Text file is not valid UTF-8: {rel}")
                    continue
                if "\r\n" in text:
                    errors.append(f"CRLF line endings found: {rel}")
                if rel_s not in {"README.md", "docs/PUBLISHING.md", "scripts/check_repo.py"} and "REPO_URL" in text:
                    warnings.append(f"REPO_URL placeholder found outside README: {rel}")

    readme = ROOT / "README.md"
    if readme.exists() and "REPO_URL" in readme.read_text(encoding="utf-8"):
        warnings.append("README.md still contains REPO_URL placeholder; replace it before first public push.")

    for warning in warnings:
        print(f"WARNING: {warning}")

    if errors:
        print("Repository check failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Repository check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
