# Native PPTX Recipes

Use this reference when the selected output lane is `native-pptx`.

## Principle

Native PPTX means the deck should be editable in PowerPoint or Keynote where promised. Prefer real text boxes, shapes, charts, tables, notes, and images over flattened slide screenshots.

## When To Use

Use `native-pptx` for:

- Board decks
- Investor or sales decks
- Consulting and strategy decks
- Academic talks with citations
- Training and internal enablement decks
- Any workflow that needs team editing
- Any deck where charts or text may change later

## Production Contract

Before building, state:

```md
Output lane: native-pptx
Editable promises:
Non-editable exceptions:
Source of truth:
Render/QA method:
```

Editable promises may include:

- Text boxes remain editable.
- Charts remain editable.
- Tables remain editable.
- Speaker notes are included.
- Theme colors or master layouts are used.

Non-editable exceptions may include:

- Decorative generated images.
- Complex screenshots.
- Logo or brand assets.
- Pixel-perfect hero backgrounds.

## Recommended Build Paths

Choose what is available in the current environment:

1. Dedicated presentation/PPTX skill or plugin.
2. PPT Master or another native-PPTX harness.
3. PptxGenJS for programmable PowerPoint generation.
4. python-pptx for simpler documents or repairs.
5. Existing `.pptx` template plus direct OOXML editing when needed.

Do not hand-roll fragile `.pptx` XML unless the change is narrow and testable.

## Bundled Deck-Plan Builder

Knowledge Cat includes `scripts/build_native_pptx.mjs`, a deterministic path from a validated JSON deck plan to native PowerPoint objects. It supports these `slides[].native_content.kind` values:

- `cover`
- `statement`
- `chart` with native categories and series
- `table` with native headers and rows
- `process`
- `closing`
- `default` or no `native_content` for a safe text-and-evidence layout

The builder requires Node.js and `@oai/artifact-tool` in a prepared workspace. In Codex, use the active Presentations skill's workspace setup helper. In another runtime, install or provide the same package before running the builder. Do not silently fall back to slide screenshots.

```bash
python3 scripts/validate_deck_plan.py path/to/deck-plan.json

node scripts/build_native_pptx.mjs \
  --plan path/to/deck-plan.json \
  --output path/to/output.pptx \
  --workspace path/to/prepared-artifact-workspace \
  --preview-dir path/to/screenshots \
  --inspection path/to/inspection.ndjson
```

The generated evidence includes:

- editable `.pptx`
- one PNG per final slide, rendered only after PPTX re-import
- one layout JSON per slide
- `contact-sheet.png`
- object inspection NDJSON

Use `examples/case-studies/native-editable/deck-plan.json` as the executable reference. The case deliberately uses no slide-sized images, so a passing result proves native text, shapes, chart, table, and notes rather than image packaging.

## Slide Object Rules

- Use real text for titles, body, labels, and citations.
- Use real shapes for cards, lines, arrows, dividers, and callouts.
- Use native charts for normal bar, line, pie, scatter, and area charts when possible.
- Use images for photos, screenshots, complex illustrations, and decorative backgrounds.
- Use speaker notes for detail removed from slides.

## Template Use

When a user provides a template:

- Extract or respect slide size, theme colors, fonts, master layouts, and reusable placeholders.
- Map slide plan roles to existing layouts before inventing new ones.
- Preserve footers, source labels, confidentiality marks, and page numbering when appropriate.
- Do not copy proprietary visuals unless the user has permission.

## QA

Minimum checks:

```md
- File opens.
- Slide count matches plan.
- Text is selectable where promised.
- Speaker notes exist if requested.
- Placeholder text is gone.
- Rendered output has no overflow or collisions.
- Charts/tables are editable if promised.
- Sources/citations are present where needed.
```

Extract text from the finished PPTX when possible. This catches placeholder text and gives a weak but useful signal that key slide copy is not fully flattened into images:

```bash
python3 scripts/extract_pptx_text.py path/to/output.pptx --fail-on-placeholders
```

Text extraction alone is insufficient. Inspect native object counts and reject image-only slides:

```bash
python3 scripts/check_pptx_editability.py path/to/output.pptx \
  --min-text-shapes-per-slide 1 \
  --fail-on-image-only-slides
```

When the delivery promises native charts, tables, or notes, add the relevant gates:

```bash
python3 scripts/check_pptx_editability.py path/to/output.pptx \
  --require-native-chart \
  --require-native-table \
  --require-notes \
  --fail-on-image-only-slides
```

Run the reversible text-object probe. It modifies only a temporary copy and confirms that a native DrawingML text object can be changed and reopened while the delivered file remains unchanged:

```bash
python3 scripts/probe_pptx_editability.py path/to/output.pptx \
  --search "Exact existing slide text" \
  --replacement "Exact temporary probe text"
```

For the bundled benchmark case, run:

```bash
python3 scripts/check_native_pptx_case.py
```

If a renderer is available, render to images or PDF and inspect. If not, say the file-open/render QA was not completed.

## Common Failures

- Flattening every slide into a full-page image.
- Overpromising chart editability.
- Using tiny text to preserve a dense plan.
- Breaking a template's footer or master logic.
- Skipping speaker notes for a presentation-heavy deck.
- Shipping without opening or rendering the file.
- Treating text extraction as complete editability proof without object inspection.
- Letting a builder dependency fail and quietly replacing native objects with full-slide images.
