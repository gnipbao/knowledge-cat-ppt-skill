# Template Replication

Use this file when the user provides a `.pptx`, screenshot, PDF, HTML deck, brand guide, or reference slide deck.

## Permission First

Ask or infer whether the user has the right to use the template. If the template is public inspiration, replicate the structure and design language, not protected logos, proprietary illustrations, confidential charts, or exact copyrighted content.

## Template Profile

Before generating new slides, create a template profile:

```md
Template source:
Permission status:
Canvas:
Primary use case:
Slide archetypes:
Color tokens:
Typography:
Grid and margins:
Image ratios:
Chart style:
Icon or illustration style:
Motion or transition pattern:
Reusable assets:
Non-reusable distinctive assets:
Risks:
```

## Extraction Checklist

Inspect:

- Canvas size and safe margins.
- Master/layout structure if a PPTX is available.
- Fonts and fallback fonts.
- Theme colors and accent semantics.
- Reusable layouts.
- Unique hero pages that should not be repeated.
- Crop behavior and image focal points.
- Chart styles, table styles, callout styles.
- Footers, page numbers, source lines, confidentiality labels.
- Animation or transition rules if the output lane supports them.

## Layout Mapping

For each planned slide:

```md
Slide:
Content shape:
Recommended template layout:
Why it fits:
Image slots:
Data slots:
Reuse risk:
Required adaptation:
```

Rules:

- Prefer one planned slide to one template layout.
- Do not reuse distinctive hero or illustration pages repeatedly.
- Use generic text, comparison, or grid layouts for repeated concepts.
- If the content does not fit any layout, adapt the content shape before inventing a new layout.
- Keep section dividers, proof pages, and closing pages visually distinct.

## Fidelity Levels

### Standard

Use when the user wants a deck in the same style.

- Preserve palette, hierarchy, rhythm, and layout families.
- Allow new content-specific layouts when needed.
- Avoid exact asset copying unless provided and permitted.

### High Fidelity

Use when the user wants strict template adherence.

- Preserve layout geometry and major style tokens.
- Map each slide to a known template layout.
- Avoid unregistered layout inventions.
- Run extra visual comparison against reference slides.

### Inspired

Use when the reference is only a mood board.

- Extract mood, contrast, pacing, and visual grammar.
- Create a new design system that does not look like a direct clone.

## Smoke Test

Before a full deck, build or render one representative slide:

- Cover or strongest hero slide.
- One dense evidence slide.
- One image-heavy or chart-heavy slide.

Check:

- Does the layout hold the new content?
- Are text sizes and line lengths acceptable?
- Does the visual style survive without the original assets?
- Are images cropped correctly?
- Does the selected output lane preserve the desired fidelity?

## Common Failures

- Copying colors but missing spacing, typography, or hierarchy.
- Reusing a distinctive layout until the deck feels repetitive.
- Replacing a chart layout with paragraphs.
- Using image-first methods when editable template components were required.
- Treating a PPTX as a screenshot instead of extracting editable layout logic.
- Ignoring brand footers, source lines, or confidentiality labels.
- Overfitting to the reference and weakening the new story.
