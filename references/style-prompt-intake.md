# Style Prompt Intake

Use this reference when the user uploads, pastes, or references a theme/style prompt, a prompt table, a visual style library, a brand style DNA block, or says they want GPT-Image / image generation to drive the PPT look.

The goal is to turn user-provided style prompts into a controlled image-first production contract. Do not merely paste the style prompt into every slide. Extract the portable visual system, normalize unsafe or over-specific references, then combine it with each slide's story job.

## When This Changes Routing

Prefer `image-first-pptx` when:

- the user uploads a theme/style prompt and asks to use it as the deck's look
- the uploaded prompt describes image style, texture, lighting, composition, poster style, illustration style, cinematic style, or full-slide visual surfaces
- the user says Image2, image generation, GPT-Image, visual PPT, style prompt, theme prompt, template prompt, image-first, or "按这个风格生成 PPT"
- the output is a social carousel, keynote, campaign deck, visual talk, cover-heavy deck, or style exploration

Do not automatically choose image-first when:

- the user needs editable text, charts, tables, speaker notes, or many stakeholder edits
- the uploaded prompt is only a brand palette or typography guide for an otherwise editable PPTX
- exact citations, metrics, legal wording, or academic formatting are central

Mixed mode is allowed:

- full-slide images for cover, section openers, visual summaries, and social cards
- editable text/charts for dense evidence slides
- generated image assets inserted into native PPTX layouts when editability still matters

## Intake Workflow

### 1. Identify The Prompt Shape

Classify the user input:

| Shape | Signal | Action |
|---|---|---|
| Single style prompt | one paragraph or one named style | build one Style Prompt Profile |
| Prompt table | rows with style name, use case, keywords, copyable prompt | ask which row to use, or choose the best row if the user gave a topic |
| Large style library | many rows, style websites, or 20+ prompt presets | read `references/style-template-library.md`, shortlist 2-3 styles by deck job, then build one Style Prompt Profile |
| Brand DNA | palette, fonts, layout rules, image treatment | preserve constraints and use image-first only if surfaces should be generated |
| Screenshot/reference deck | visual sample rather than prompt text | route through template/profile extraction first |
| Mixed style dump | many prompts with no selection | shortlist 2-3 styles by deck goal and ask once if needed |

If the user says "直接按最合适的来", choose one style and state the assumption.

When the user says the target is to surpass Guizang or another HTML-deck benchmark, do not merely choose a pretty image style. Use `references/style-template-library.md` to identify whether the chosen style should become an HTML signature pack, image-first profile, or native editable PPTX direction.

### 2. Extract A Style Prompt Profile

Create this profile before generating slide prompts:

```md
Style Prompt Profile
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

Guidelines:

- `Selected prompt` can quote or summarize the user's prompt, but keep it concise.
- `Visual DNA` should be reusable across every slide.
- `Text-in-image policy` must decide whether slide text is editable outside images or baked into images.
- `Must preserve` includes brand colors, product screenshots, exact data, language, or audience tone.
- `Must avoid` includes watermarks, fake logos, page chrome, slide numbers, footers, unreadable small text, and style drift.

### 3. Normalize The Prompt

Protect the user's intent while removing brittle or unsafe details:

- Convert protected character/franchise/style references into generic visual traits unless the user has rights and the use is allowed.
- Do not imitate a living artist's exact style. Extract medium, composition, palette, and mood instead.
- Remove instructions that ask the image model to invent citations, logos, UI metrics, or exact long text.
- Preserve language requirements: Chinese decks should use Chinese labels if text appears inside generated images; English decks should use English.
- Add "no title bar, no footer, no page number, no watermark, no logo unless user provides it" for slide-surface images.

### 4. Choose Image-First Strategy

Choose one:

| Strategy | Use when | Output |
|---|---|---|
| Full image-first deck | every slide is a generated surface | PPTX with full-slide images plus prompt log |
| Hybrid image-first PPTX | selected slides are images, dense slides remain editable | native PPTX with generated image assets |
| Image-first HTML prototype | user wants browser preview before packaging | HTML deck with generated images and visual QA |
| Social carousel | square or vertical image cards | 1:1, 3:4, 4:5 image set and optional PPTX wrapper |

Default for uploaded visual prompt tables: `Full image-first deck` for carousels/keynotes; `Hybrid image-first PPTX` for business/report decks.

### 5. Build Slide-Level Prompts

Every slide prompt should combine:

```txt
GLOBAL STYLE DNA:
{normalized style profile}

SLIDE JOB:
Slide {number}: {role}
Action title: {action title}
Visual intent: {visual job}
Required content: {short labels only}
Aspect ratio: {ratio}
Safe area: keep important subjects and labels inside center 80%
Forbidden: no watermark, no fake logo, no page number, no footer, no long paragraphs
```

Rules:

- Generate one representative slide first when quality matters.
- Keep slide prompts consistent; vary composition by slide role, not by random style changes.
- Do not bake long paragraphs into images.
- If exact words matter, place them as editable PPTX text over or beside the image.
- Save a prompt log for every generated slide.

## Output Protocol

When using uploaded style prompts, include this in the deck brief:

```md
Style prompt source:
Selected style:
Why this style fits:
Output lane:
Editability tradeoff:
Image generation strategy:
Text-in-image policy:
Prompt log path:
QA method:
```

Slide plan table:

```md
| # | Role | Action title | Visual intent | Style variation | Text in image | Ratio | Prompt risk |
|---|---|---|---|---|---|---|---|
```

## QA Checklist

Before delivery:

- User-provided style prompt was parsed into a profile.
- Output lane and editability tradeoff were stated.
- One representative slide was generated or planned before full production when stakes are high.
- Prompt log exists.
- Style is consistent across slides.
- Text inside images is short, readable, and visually checked.
- No unwanted watermark, fake logo, page chrome, footer, or slide number appears inside generated images.
- Exact data, citations, product screenshots, and sensitive details were not hallucinated or redesigned without permission.

## Failure Modes

- Treating a style prompt as a magic suffix and losing slide-level story intent.
- Choosing image-first even though the user needed editable charts or legal/academic precision.
- Baking too much text into images.
- Mixing several uploaded styles in one deck without a section-level reason.
- Copying protected characters, brands, or living-artist style labels instead of extracting visual traits.
- Generating beautiful slide surfaces that no longer match the deck's audience shift.
