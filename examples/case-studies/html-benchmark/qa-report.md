# HTML Benchmark QA Report

## Visual QA

- Selected visual system: Architectural Minimal.
- Registered layouts used: hero, statement, two-col, image-annotation, comparison, process, system-map, data-dashboard, closing-decision.
- Theme rhythm: light, dark, light, light, dark, light, dark, light, light.
- Local image slot: `images/04-product-surface.svg` with `data-image-slot="04-main-16x10"` and `data-slot-ratio="16:10"`.
- Contact sheet artifact: `screenshots/contact-sheet.svg`.
- Slide screenshot artifact: `screenshots/slide-01.svg`.

## Contact Sheet

The included contact sheet is a repository fixture that verifies the benchmark case has a screenshot-level QA artifact. It is intentionally SVG so the open-source skill can keep deterministic checks in the Python standard library.

## Fix Loop

- First pass risk: the HTML lane previously had only static validation and no durable visual-evidence artifact.
- P0 fix: this case study adds a contact sheet, a slide screenshot artifact, an image-slot asset, and a QA artifact checker wired into `scripts/run_checks.py`.

## Known Limitations

- The screenshot artifacts are fixture-level SVGs, not browser-captured PNGs.
- A future browser/Playwright integration should replace or supplement these fixtures with generated viewport screenshots.
