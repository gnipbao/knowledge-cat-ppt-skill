#!/usr/bin/env python3
"""Run negative fixtures that should fail with specific validation errors."""

from __future__ import annotations

import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Fixture:
    name: str
    command: list[str]
    expected: tuple[str, ...]


FIXTURES = [
    Fixture(
        name="html missing layout metadata",
        command=[
            sys.executable,
            "scripts/validate_html_deck.py",
            "examples/failure-fixtures/html/missing-layout/index.html",
        ],
        expected=("Slide 1 missing data-layout.",),
    ),
    Fixture(
        name="html missing local image slot",
        command=[
            sys.executable,
            "scripts/validate_html_deck.py",
            "examples/failure-fixtures/html/missing-image-slot/index.html",
        ],
        expected=("Slide 1 local image 1 missing data-image-slot.",),
    ),
    Fixture(
        name="html unresolved placeholder marker",
        command=[
            sys.executable,
            "scripts/validate_html_deck.py",
            "examples/failure-fixtures/html/unresolved-marker/index.html",
        ],
        expected=("Unresolved placeholder marker: todo",),
    ),
    Fixture(
        name="html slide count mismatch",
        command=[
            sys.executable,
            "scripts/validate_html_deck.py",
            "examples/failure-fixtures/html/slide-count-mismatch/index.html",
        ],
        expected=("deck-plan.json slide_count is 2, but HTML has 1 slides.",),
    ),
]


def run_fixture(fixture: Fixture) -> list[str]:
    completed = subprocess.run(
        fixture.command,
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    output = f"{completed.stdout}\n{completed.stderr}"
    lowered = output.lower()

    errors: list[str] = []
    if completed.returncode == 0:
        errors.append(f"{fixture.name}: command unexpectedly passed")
    for phrase in fixture.expected:
        if phrase.lower() not in lowered:
            errors.append(f"{fixture.name}: missing expected error {phrase!r}")

    if errors:
        print(f"\n--- {fixture.name} output ---")
        print(output.rstrip())
    else:
        print(f"Negative fixture passed: {fixture.name}")
    return errors


def main() -> int:
    errors: list[str] = []
    for fixture in FIXTURES:
        errors.extend(run_fixture(fixture))

    if errors:
        print("Failure fixture check failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("All failure fixtures behaved as expected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
