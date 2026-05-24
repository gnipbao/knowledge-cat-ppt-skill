# Image-First Recipes

Use this reference when the selected output lane is `image-first-pptx` or when the user explicitly prioritizes visual impact over editability.

## Principle

Image-first decks are visual artifacts. They can be excellent for keynotes, campaigns, social carousels, and style exploration, but they are the wrong default for collaborative business decks.

## When To Use

Use `image-first-pptx` when:

- Visual spectacle matters more than editability.
- The user asks for AI-generated slide surfaces.
- The output is a social carousel, launch visual, concept deck, or poster-like talk.
- The user wants a template-inspired visual study.

Do not use when:

- The user needs editable text, charts, or tables.
- The deck will go through many stakeholder edits.
- Exact citation formatting or numbers are central.

## Production Contract

Before building, state:

```md
Output lane: image-first-pptx
Editability tradeoff:
Image model or generation path:
Prompt log path:
Text safety rule:
QA method:
```

## Prompt Plan

Create a prompt table before generation:

```md
| Slide | Role | Visual intent | Text inside image? | Aspect ratio | Prompt seed | QA risk |
|---|---|---|---|---|---|---|
```

Rules:

- Keep text outside images when exact wording matters.
- If text must be inside images, keep it short and verify it visually.
- Generate one representative slide before the full set.
- Keep prompt language consistent across the deck.
- Store prompt logs for iteration.

## Aspect Ratios

- 16:9 for normal slides.
- 4:5 or 3:4 for social cards when requested.
- 1:1 for square carousel variants.
- 21:9 for cinematic hero imagery only when the slide layout has a matching slot.

## QA

Check:

- User accepted editability limitations.
- Images are high enough resolution.
- Text inside images is correct and readable.
- No unwanted watermarks, UI artifacts, fake logos, or accidental text.
- Visual style is consistent across slides.
- Crops preserve the subject and slide safe areas.
- PPTX packaging preserves image quality.

## Common Failures

- A deck that looks dramatic but cannot be edited.
- Long text baked into images with spelling errors.
- Mixed styles across slides.
- Aspect ratios that do not fit the final slide slots.
- Treating template mimicry as permission to copy protected assets.
