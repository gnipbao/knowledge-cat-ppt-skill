# Image-First Recipes

Use this reference when the selected output lane is `image-first-pptx` or when the user explicitly prioritizes visual impact over editability.

If the user uploaded or pasted a theme/style prompt, prompt table, or visual DNA block, read `references/style-prompt-intake.md` first.

## Principle

Image-first decks are visual artifacts. They can be excellent for keynotes, campaigns, social carousels, and style exploration, but they are the wrong default for collaborative business decks.

## When To Use

Use `image-first-pptx` when:

- Visual spectacle matters more than editability.
- The user asks for AI-generated slide surfaces.
- The user uploads a theme/style prompt and wants the PPT to follow it.
- The user says Image2, GPT-Image, AI image style, style prompt, visual prompt, theme prompt, or "按这个风格生成 PPT".
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
Style prompt source:
Style Prompt Profile path:
Image model or generation path:
Prompt log path:
Text safety rule:
QA method:
```

## User-Uploaded Style Prompts

When the user provides a style prompt or prompt table:

1. Parse the prompt source with `references/style-prompt-intake.md`.
2. If multiple styles are present, choose the best fit from the deck goal or ask one short selection question.
3. Create a Style Prompt Profile before slide-level prompts.
4. Normalize protected brand, character, franchise, or living-artist references into generic visual traits unless the user has rights and the use is allowed.
5. Use the profile as the global style DNA for every generated slide.
6. Keep long or exact text outside images whenever possible.

Style Prompt Profile:

```md
Name:
Source:
Selected prompt:
Use case fit:
Visual DNA:
Palette:
Typography:
Texture/material:
Composition:
Imagery:
Diagram/chart treatment:
Text-in-image policy:
Aspect ratios:
Must preserve:
Must avoid:
Safety normalization:
Output lane:
```

Default routing:

- Keynote, campaign, social carousel, cover-heavy deck -> full image-first PPTX.
- Business report, investor, academic, training, data-heavy deck -> hybrid image-first PPTX unless the user accepts flattened slides.
- Brand palette or typography prompt only -> native PPTX can still be better if editability matters.

## Prompt Plan

Create a prompt table before generation:

```md
| Slide | Role | Visual intent | Style variation | Text inside image? | Aspect ratio | Prompt seed | QA risk |
|---|---|---|---|---|---|---|---|
```

Rules:

- Keep text outside images when exact wording matters.
- If text must be inside images, keep it short and verify it visually.
- Generate one representative slide before the full set.
- Keep prompt language consistent across the deck.
- Store prompt logs for iteration.
- Add a negative clause for full-slide images: no watermark, no fake logo, no page number, no footer, no title bar, no long paragraphs.
- Use the user's style prompt as global DNA, then add slide-specific intent; do not paste the same generic prompt with no slide job.

Prompt structure:

```txt
GLOBAL STYLE DNA:
{normalized style prompt profile}

SLIDE JOB:
Slide {number}: {role}
Action title: {action_title}
Visual intent: {visual_intent}
Required visible labels: {short_labels_or_none}
Aspect ratio: {ratio}
Safe area: keep important subjects and labels inside center 80%
Forbidden: no watermark, no fake logo, no page number, no footer, no long paragraphs
```

## Aspect Ratios

- 16:9 for normal slides.
- 4:5 or 3:4 for social cards when requested.
- 1:1 for square carousel variants.
- 21:9 for cinematic hero imagery only when the slide layout has a matching slot.

## QA

Check:

- User accepted editability limitations.
- Uploaded style prompt was parsed into a Style Prompt Profile when present.
- A representative slide was smoke-tested before full generation when stakes are high.
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
- Treating a user style prompt as a magic suffix while ignoring the slide's story role.
