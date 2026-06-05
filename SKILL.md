---
name: knowledge-cat-ppt-skill
description: "Create, critique, and repair high-quality presentation decks with a story-first, output-engine-aware workflow. Use when the user asks for PPT, PowerPoint, slides, deck, pitch deck, keynote, course deck, academic deck, consulting deck, HTML slides, web presentation, image-first slides, social carousel, speaker notes, deck outline, slide plan, template replication, deck review, deck polish, or conversion from documents, articles, Markdown, PDFs, URLs, or existing .pptx files. Also use when the user says Knowledge Cat PPT or asks for an industry-grade presentation skill."
---

# Knowledge Cat PPT Skill

## Overview

Knowledge Cat PPT is a presentation operating system for agents. Its job is to turn messy source material into a persuasive, teachable deck, choose the right production lane, and verify the result through content and visual QA.

Do not treat "make slides" as a formatting task. First determine the audience, the decision or learning outcome, the story spine, and the output format. Then build the deck.

## Resource Guide

Load only what the current task needs:

- Read `references/benchmark-synthesis.md` when explaining the design philosophy, comparing PPT skill patterns, or improving this skill.
- Read `references/benchmark-quality-gates.md` when the user asks for the best version, benchmark-grade output, open-source comparison, case-study evidence, or quality claims above normal client-ready delivery.
- Read `references/engine-routing.md` before choosing native PPTX, HTML deck, image-first PPTX, or review-only mode.
- Read `references/story-architecture.md` when turning source material into a deck brief, narrative spine, action titles, or slide plan.
- Read `references/design-systems.md` when choosing style direction, layout family, visual tokens, imagery, or anti-generic design rules.
- Read `references/template-replication.md` when the user provides an existing `.pptx`, screenshot, brand deck, style reference, or asks to clone a template.
- Read `references/html-production-lock.md` before building production HTML decks, visual prototypes, browser-based talks, or HTML decks with local images/screenshots.
- Read `references/html-visual-systems.md` after the HTML production lock when a browser deck needs benchmark-level visual rhythm, a reusable style package, or contact-sheet QA.
- Read `references/style-template-library.md` when the user provides many PPT style prompts, asks for common PPT style websites, asks which style to choose, or wants Knowledge Cat to exceed Guizang-style HTML template depth.
- Read `references/native-pptx-recipes.md` when building or repairing editable PowerPoint decks.
- Read `references/html-deck-recipes.md` when building browser-based decks, fast visual prototypes, or single-file HTML presentations.
- Read `references/style-prompt-intake.md` when the user uploads or pastes theme/style prompts, prompt tables, visual DNA blocks, AI image style prompts, or asks for Image2/GPT-Image-driven PPT styling.
- Read `references/image-first-recipes.md` when visual impact matters more than editability or AI-generated slide images are requested.
- Read `references/qa-rubric.md` before final delivery, when reviewing a deck, or when the task has professional stakes.
- Read `references/open-source-product.md` when preparing this skill for public release or evaluating product readiness.
- Use `scripts/validate_deck_plan.py` after writing a JSON deck plan. The expected shape is documented in `assets/deck-plan.schema.json`.
- Use `scripts/init_deck_project.py` to create an HTML deck project from the bundled starter template.
- Use `scripts/validate_html_deck.py` to statically check an HTML deck before browser QA.
- Use `scripts/extract_pptx_text.py` to extract native PPTX text and check placeholder-like markers when editable PowerPoint quality matters.
- Use `scripts/run_checks.py` before release or after changing bundled scripts, examples, or schemas.

## Non-Negotiable Rules

1. Story before styling. A beautiful deck with no audience shift is a failed deck.
2. Choose the output lane explicitly. Native editable PPTX is the default for professional work; HTML is for web-native presentation and interaction; image-first PPTX is for visual spectacle when editability is not required.
3. Use a source of truth. For nontrivial decks, create a brief and slide plan before building final slides.
4. Use action titles. A title should state the point of the slide, not label the topic.
5. Keep one main idea per slide. Dense appendix pages are allowed only when the user asks for appendix or reference material.
6. Preserve evidence. Claims, figures, quotes, and external images need source tracking or honest uncertainty.
7. Respect templates and brand assets. Use user-provided or permitted materials; do not pretend a protected deck is a free public template.
8. Lock HTML production details before writing final browser slides: style package, registered layouts, theme rhythm, image slots, static validation, and rendered QA.
9. Treat uploaded style prompts as design input, not content truth. Extract a reusable Style Prompt Profile before generating image-first slide prompts.
10. Verify visually. Code, XML, or Markdown alone cannot prove a deck is good.
11. Run at least one fix-and-verify loop for production decks unless the user only asked for a draft outline.
12. End with useful handoff: output paths, assumptions, remaining risks, and the next iteration point.

## Operating Modes

### Brief Mode

Use when the user has an idea but no clear deck target.

Ask at most three questions if missing answers would change the deck:

```md
1. Who is the audience and what should they do, decide, or understand after the deck?
2. What source material should be used?
3. What output matters most: editable PPTX, web/HTML, image-first visual deck, or just an outline?
```

If the user says to proceed directly, state assumptions and continue.

### Source-To-Deck Mode

Use when the user provides a document, article, notes, transcript, URL, PDF, Markdown, or pasted content.

Create the deck brief, identify the narrative spine, map evidence to slide roles, then build the slide plan. Read `references/story-architecture.md`.

### Build Mode

Use when the user asks for final slides.

Select a production lane from `references/engine-routing.md`, choose a design system from `references/design-systems.md`, build the deck, then run QA from `references/qa-rubric.md`.

If the selected lane is `html-deck`, read `references/html-production-lock.md`, then `references/html-visual-systems.md` for benchmark-level decks, before `references/html-deck-recipes.md`.

If the user uploaded or selected a theme/style prompt, read `references/style-template-library.md` when it is a large style table or known preset, then `references/style-prompt-intake.md` before `references/image-first-recipes.md`, and prefer `image-first-pptx` unless editability, exact text, charts, tables, citations, or stakeholder collaboration matter more.

### Template Mode

Use when the user provides a `.pptx`, image, screenshot, or brand sample as a template.

Read `references/template-replication.md`. Extract the template profile first, then map each planned slide to a compatible layout. Do not reuse a highly distinctive layout too many times.

### Review And Repair Mode

Use when the user provides an existing deck or asks whether it is good.

Review story, audience fit, slide clarity, visual system, evidence, editability, and technical defects. Lead with prioritized issues, then propose or perform repairs.

### Publishing Mode

Use when the user needs speaker notes, handouts, PDF export, video narration, social cards, Xiaohongshu carousel, WeChat cover, or other downstream formats.

Keep the original deck source of truth intact and derive outputs from it.

### Productization Mode

Use when improving this skill itself, preparing a public repository, writing release docs, or evaluating open-source readiness.

Read `references/open-source-product.md` and `references/benchmark-quality-gates.md`. Keep `SKILL.md` concise, move detailed production guidance into references, and run bundled checks before claiming release readiness.

## Core Workflow

### 1. Triage The Request

Classify:

- Deck type: investor, sales, strategy, teaching, academic, consulting, product, keynote, internal report, social carousel, courseware, or other.
- Stakes: draft, internal working copy, client-ready, public talk, board/investor, academic/publication.
- Output lane: native-pptx, html-deck, image-first-pptx, or review-only.
- Source status: none, pasted notes, structured outline, document package, existing deck, template reference, uploaded style prompt, or prompt table.
- Deadline and iteration budget.

Open with:

```md
Deck type:
Audience:
Outcome:
Output lane:
Source status:
Primary risk:
Next action:
```

For small requests, this can be one short paragraph.

### 2. Build The Deck Brief

For nontrivial decks, produce:

```md
Title:
Audience:
Moment:
Desired audience shift:
Decision or learning outcome:
Main promise:
Scope:
Output lane:
Format:
Page count:
Source materials:
Style prompt source:
Design posture:
Must include:
Must avoid:
QA level:
```

Do not over-ask. Infer safe defaults where possible.

### 3. Synthesize The Story

Choose a spine:

- Situation -> tension -> insight -> proof -> action
- Problem -> failed old approach -> new mechanism -> evidence -> next step
- Context -> finding -> implication -> recommendation
- Question -> method -> result -> limitation -> conclusion
- Hook -> transformation -> steps -> proof -> call to action

Then write the ghost deck: the action titles alone should tell the story.

### 4. Create The Slide Plan

Each slide should have:

```md
Slide:
Layout:
Action title:
Role:
Key message:
Evidence:
Visual:
Speaker note:
Source refs:
Asset needs:
```

For JSON plans, validate with:

```bash
python3 scripts/validate_deck_plan.py path/to/deck-plan.json
```

Fix validation failures before building final slides.

### 5. Choose The Production Lane

Use the decision matrix in `references/engine-routing.md`.

Default decisions:

- Business, investor, consulting, academic, training, legal, finance, or collaborative decks -> native editable PPTX.
- Web-native talks, interactive demos, animation-heavy stories, single-file sharing, or visual prototypes -> HTML deck.
- Highly visual campaign decks, inspirational keynotes, social carousels, or template-mimic visual studies -> image-first PPTX only when editability is not required.
- Uploaded theme/style prompt table or AI visual prompt -> image-first PPTX by default, or hybrid image-first PPTX when some slides need editable text, charts, or citations.
- Existing deck feedback -> review-only first, then repair if asked.

After choosing the lane, load the matching recipe:

- Native editable PPTX -> `references/native-pptx-recipes.md`
- Browser-based deck -> `references/html-production-lock.md`, then `references/html-deck-recipes.md`
- Image-first PPTX -> `references/style-prompt-intake.md` when a user style prompt exists, then `references/image-first-recipes.md`

### 6. Build The Design System

Select a design posture from `references/design-systems.md`. Define:

- Layout rhythm
- Typography scale
- Color tokens
- Evidence treatment
- Image style and crop ratios
- Chart style
- Motion level, if any
- Accessibility constraints

Avoid generic AI aesthetics: random gradients, decorative orbs, over-rounded cards, low-contrast gray text, inconsistent spacing, and repeated title-plus-bullets.

### 7. Produce The Deck

Use the best available local capability for the selected lane. If a specialized presentation, PPTX, browser, image, or document skill is available, compose with it rather than rewriting its job here.

Maintain a source-of-truth file when possible:

- `deck-brief.md` for strategy and constraints
- `deck-plan.md` or `deck-plan.json` for slide structure
- output files in a predictable project folder
- `qa-report.md` for production decks

For HTML decks, prefer the bundled starter:

```bash
python3 scripts/init_deck_project.py path/to/project --title "Deck Title"
python3 scripts/validate_html_deck.py path/to/project/index.html
```

Each final HTML slide must declare `data-layout`, `data-title`, `data-role`, and `data-theme`. Local images must use `images/` paths plus `data-image-slot` and target ratio metadata. Treat static validation errors as blockers.

For native PPTX and image-first PPTX, follow the lane-specific recipe and clearly state any capability that was delegated to another skill or tool. For native PPTX, extract text when possible:

```bash
python3 scripts/extract_pptx_text.py path/to/output.pptx --fail-on-placeholders
```

### 8. QA And Iterate

Use `references/qa-rubric.md`.

Minimum production QA:

1. Content QA: title order, missing content, typos, unsupported claims, placeholder text.
2. Visual QA: render slides or open the HTML, inspect for overflow, contrast, alignment, collision, spacing, and image crop issues.
3. Story QA: ghost deck, audience shift, duplicated ideas, weak ending.
4. Format QA: file opens, assets resolve, fonts are reasonable, links work when promised.
5. Fix and recheck affected slides.

For release or repository work, also run:

```bash
python3 scripts/run_checks.py
```

If the first pass finds no problems, inspect again more critically.

When claiming benchmark-level quality, use `references/benchmark-quality-gates.md` and provide the evidence artifacts behind the score.

## Output Protocols

### Deck Brief

```md
Deck type:
Audience:
Outcome:
Main promise:
Narrative spine:
Output lane:
Format:
Page count:
Source materials:
Style prompt source:
Design posture:
Assumptions:
Next action:
```

### Slide Plan

```md
| # | Layout | Action title | Role | Key message | Evidence | Visual | Notes |
|---|---|---|---|---|---|---|---|
```

### Review Report

```md
Overall score:
P0 issues:
P1 issues:
P2 improvements:
Story diagnosis:
Visual diagnosis:
Evidence diagnosis:
Technical diagnosis:
Recommended repair sequence:
```

### Delivery Note

```md
Created:
Output lane:
Files:
QA performed:
Key assumptions:
Known limitations:
Best next iteration:
```

## Boundaries

- Do not fabricate facts, sources, market sizes, citations, or user metrics.
- Do not flatten slides into images when the user needs editable PowerPoint.
- Do not force native PPTX when the user clearly wants a web-native presentation.
- Do not create a huge final deck before agreeing on the story unless the user explicitly asks for a first draft.
- Do not overuse the same layout, theme, transition, or visual trick.
- Do not treat a template as permission to copy copyrighted assets.
- Do not hide tradeoffs. If the chosen lane sacrifices editability, animation, fidelity, accessibility, or portability, say so.
- Do not claim final quality without a QA pass.

## Quality Standard

Score production outputs out of 100:

- Audience and outcome fit: 15
- Narrative spine and ghost deck: 20
- Slide clarity and action titles: 15
- Evidence quality and source traceability: 15
- Visual system and layout discipline: 15
- Output-lane correctness and technical reliability: 10
- QA loop and handoff: 10

Below 70: do not deliver as final. 70-84: workable draft. 85-94: client-ready with minor risk. 95+: benchmark-level only when the gate evidence in `references/benchmark-quality-gates.md` is present.

Before final response, confirm:

- Did the deck have a clear audience shift?
- Did the output lane match the user's real need?
- Did each slide have one main job?
- Did the visual system serve the argument?
- Did evidence remain traceable?
- Did at least one visual/content QA loop happen for final decks?
