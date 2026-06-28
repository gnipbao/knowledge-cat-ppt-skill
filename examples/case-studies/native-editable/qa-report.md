# Native Editable PPTX QA Report

## Scope

- Case: `examples/case-studies/native-editable`
- Output lane: `native-pptx`
- Final deck: `knowledge-cat-native-editable.pptx`
- Slide count: 6
- Build source: `deck-plan.json` through `scripts/build_native_pptx.mjs`
- Renderer: `@oai/artifact-tool`, followed by PPTX re-import before previews were rendered

## Editable promises

- Slide titles, body copy, labels, and page chrome are native text shapes.
- The chart on slide 3 is a native chart object with editable categories and series values.
- The evidence matrix on slide 4 is a native table.
- Process nodes and rules are native PowerPoint shapes.
- Every slide contains a speaker-note part.
- No full-slide picture or flattened slide surface is present.

Non-editable exceptions: none in this fixture. The deck intentionally contains no photos, screenshots, logos, or decorative bitmap backgrounds.

## Content QA

- `deck.slide_count` matches six generated slides.
- Action titles form a complete claim-to-proof-to-gate story.
- `scripts/extract_pptx_text.py --fail-on-placeholders` found no placeholder markers.
- All values on the chart are explicitly labeled as illustrative benchmark fixtures.
- No external factual claims or unsourced market data are used.

## Rendered QA

- The exported PPTX was re-imported before rendering.
- Six final-slide PNG previews were rendered at 1280 × 720.
- `screenshots/contact-sheet.png` contains all six final slides in a 3 × 2 review grid.
- Full-size review covered title wrapping, chart labels, table legibility, process spacing, contrast, and slide-to-slide rhythm.
- The Presentations overflow test returned `Test passed. No overflow detected.`
- No unintended collision, clipping, broken connector, or missing glyph was observed.

## Object and editability QA

- `inspection.ndjson` records 42 text shapes, one native chart, one native table, and six notes objects after PPTX re-import.
- `editability-report.json` records 53 native shapes, no pictures, one chart, one table, and six note parts.
- `edit-probe.json` proves a named native `a:t` text object can be changed in a temporary copy, reopened, and verified while the final deck remains unchanged.
- The negative self-test in `scripts/check_pptx_editability.py` rejects an image-only slide.

## Fix loop

First pass findings and repairs:

1. The artifact-tool montage export returned only the first slide. Replaced it with an artifact-tool contact-sheet composition built from all six re-imported PNG previews.
2. Chart axis labels and table body copy were below the 16 px production floor. Increased both to 16 px and regenerated the deck.
3. The chart part was emitted under `ppt/slides/charts/` rather than the conventional `ppt/charts/`. Expanded the package checker to recognize both valid emitted locations while still requiring a native `c:chart` graphic frame.
4. An artifact-tool import/edit/re-export experiment changed text in memory but did not persist it after export. Replaced that unreliable probe with a reversible OOXML text-object mutation test and documented the imported-deck repair limitation below.

The final deck and every preview were regenerated after these fixes.

## Known limitations

- The bundled builder requires Node.js plus `@oai/artifact-tool` in a prepared workspace. Python validators remain standard-library only.
- This case proves net-new native generation. It does not certify arbitrary edits to imported third-party templates.
- The current artifact-tool import/edit/re-export path did not persist the probe text change in this environment. Existing-deck repairs should continue to route through the active Presentations skill, PPT Master, or another verified native editor until that path is retested.
- The deterministic edit probe operates on a temporary OOXML copy; a final manual edit in desktop PowerPoint or Keynote remains recommended for high-stakes delivery.
- The fixture contains no image crops, external fonts, equations, or complex diagrams, so those capabilities are outside this case's evidence boundary.

## Commands

```bash
python3 scripts/validate_deck_plan.py examples/case-studies/native-editable/deck-plan.json
python3 scripts/extract_pptx_text.py examples/case-studies/native-editable/knowledge-cat-native-editable.pptx --fail-on-placeholders
python3 scripts/check_pptx_editability.py examples/case-studies/native-editable/knowledge-cat-native-editable.pptx --expected-slides 6 --min-text-shapes-per-slide 2 --require-native-chart --require-native-table --require-notes --fail-on-image-only-slides
python3 scripts/probe_pptx_editability.py examples/case-studies/native-editable/knowledge-cat-native-editable.pptx
python3 scripts/check_native_pptx_case.py
```
