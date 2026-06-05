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

If a renderer is available, render to images or PDF and inspect. If not, say the file-open/render QA was not completed.

## Common Failures

- Flattening every slide into a full-page image.
- Overpromising chart editability.
- Using tiny text to preserve a dense plan.
- Breaking a template's footer or master logic.
- Skipping speaker notes for a presentation-heavy deck.
- Shipping without opening or rendering the file.
