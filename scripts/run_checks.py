#!/usr/bin/env python3
"""Run bundled Knowledge Cat PPT checks."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HTML_BENCHMARK = Path("examples/case-studies/html-benchmark")


def run(cmd: list[str]) -> int:
    print("$ " + " ".join(cmd))
    completed = subprocess.run(cmd, cwd=ROOT)
    return completed.returncode


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Knowledge Cat PPT validation checks.")
    parser.add_argument(
        "--skip-sample-html",
        action="store_true",
        help="Do not initialize and validate the temporary sample HTML deck.",
    )
    args = parser.parse_args()

    checks = [
        [sys.executable, "scripts/validate_deck_plan.py", "examples/sample-deck-plan.json"],
    ]

    node = shutil.which("node")
    if node:
        checks.append([node, "--check", "scripts/build_native_pptx.mjs"])
    else:
        print("WARNING: node not found; skipped native builder syntax check.")

    if not args.skip_sample_html:
        temp = Path(tempfile.mkdtemp(prefix="knowledge-cat-html-"))
        checks.append([sys.executable, "scripts/init_deck_project.py", str(temp), "--title", "Knowledge Cat Sample"])
        checks.append([sys.executable, "scripts/validate_html_deck.py", str(temp / "index.html")])

    checks.append([sys.executable, "scripts/validate_deck_plan.py", str(HTML_BENCHMARK / "deck-plan.json")])
    checks.append([sys.executable, "scripts/validate_html_deck.py", str(HTML_BENCHMARK / "index.html")])
    checks.append([sys.executable, "scripts/check_html_qa_artifacts.py", str(HTML_BENCHMARK)])
    checks.append([sys.executable, "scripts/validate_deck_plan.py", "examples/case-studies/portfolio-minimal/deck-plan.json"])
    checks.append([sys.executable, "scripts/validate_html_deck.py", "examples/case-studies/portfolio-minimal/index.html"])
    checks.append([sys.executable, "scripts/check_html_qa_artifacts.py", "examples/case-studies/portfolio-minimal"])
    checks.append([sys.executable, "scripts/check_signature_pack.py", "portfolio-minimal"])
    checks.append([sys.executable, "scripts/check_failure_fixtures.py"])
    checks.append([sys.executable, "scripts/extract_pptx_text.py", "--self-test"])
    checks.append([sys.executable, "scripts/check_pptx_editability.py", "--self-test"])
    checks.append([sys.executable, "scripts/probe_pptx_editability.py", "--self-test"])
    checks.append([sys.executable, "scripts/check_native_pptx_case.py"])
    checks.append([sys.executable, "scripts/check_repo.py"])

    for cmd in checks:
        code = run(cmd)
        if code:
            return code

    print("All Knowledge Cat PPT checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
