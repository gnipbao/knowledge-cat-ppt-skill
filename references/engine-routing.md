# Engine Routing

Use this file before choosing the production lane for a nontrivial deck.

## Decision Matrix

| User Need | Best Lane | Why | Main Tradeoff |
|---|---|---|---|
| Client-ready PowerPoint, board deck, finance, legal, sales, training, academic, internal collaboration | Native editable PPTX | PowerPoint users can edit text, charts, shapes, notes, and templates | Harder to reach extreme visual fidelity without careful QA |
| Web presentation, interactive story, animation-heavy keynote, design prototype, single-file sharing | HTML deck | Easy for agents to edit, preview, animate, and test in a browser | Not a true PowerPoint file unless exported as static images/PDF |
| Visual campaign, dramatic keynote, social carousel, cover-heavy deck, template-mimic visual study | Image-first PPTX | Highest visual style ceiling and fast image iteration | Slides may be flattened images and less editable |
| User-uploaded theme/style prompt, AI image prompt table, visual DNA block, Image2/GPT-Image style request | Image-first PPTX or hybrid image-first PPTX | The user is giving art direction for generated slide surfaces | Exact text, charts, and later edits may need editable overlays or native slides |
| Existing deck critique or rescue | Review-only first | Prevents premature rewriting and surfaces root defects | User may still need a second repair pass |

## Default Routing Rules

Choose native editable PPTX when:

- The user says PPT, PowerPoint, pitch deck, consulting deck, board deck, training, investor deck, academic presentation, or editable deck.
- The deck will be reviewed or edited by multiple people.
- Charts, tables, citations, speaker notes, or appendices matter.
- The user needs a deliverable that opens cleanly in PowerPoint or Keynote.

Choose HTML deck when:

- The user asks for web slides, interactive slides, browser presentation, animation, single-file deck, or visual prototype.
- The user values rapid visual iteration over PowerPoint editability.
- The deck needs custom interactions, keyboard navigation, scroll/swipe behavior, or responsive export.
- The user needs a quick open-source-demo artifact that can be inspected without PowerPoint.

Choose image-first PPTX when:

- The user explicitly prioritizes visual impact over editability.
- The output is a visual talk, launch deck, social carousel, or art-directed narrative.
- The user asks to use AI image generation for most slide surfaces.
- The user uploads or pastes a theme/style prompt, prompt table, style DNA block, or says to use Image2/GPT-Image as the primary PPT visual engine.
- Template mimicry is primarily about visual feel rather than editable structures.

Choose hybrid image-first PPTX when:

- The uploaded style prompt should drive covers, section openers, summaries, or social cards, but evidence slides need editable text, charts, tables, citations, or product screenshots.
- The user wants the uploaded style but will still revise the deck with teammates.

Choose review-only when:

- The user asks "is this good", "polish this", "why does this deck feel weak", or "review my PPT".
- The deck may have strategic issues that design changes cannot fix.

## Output Lane Contract

State the lane before building:

```md
Selected lane:
Reason:
Tradeoff:
Validation method:
Source of truth:
```

Example:

```md
Selected lane: native editable PPTX
Reason: investor deck that needs later team edits and charts
Tradeoff: extreme visual textures will be simplified into editable shapes or images
Validation method: render to images, inspect visuals, extract text for content QA
Source of truth: deck-plan.json
```

## Production Pathways

### Native Editable PPTX

Use when PowerPoint editability matters.

Before building, read `references/native-pptx-recipes.md`.

Preferred tools, depending on what is available:

- The bundled `scripts/build_native_pptx.mjs` deck-plan builder when an `@oai/artifact-tool` workspace is available.
- A dedicated presentation/PPTX skill or plugin.
- PPT Master if installed and the user accepts its workflow.
- PptxGenJS for programmable layouts and charts.
- python-pptx for simple generation or repair.
- LibreOffice or PowerPoint for rendering and export checks.

Required checks:

- File opens.
- Text is selectable where editability is promised.
- Charts/tables are editable when promised.
- Speaker notes are present if requested.
- Placeholder text is gone.
- Native object inspection passes and image-only slides are rejected.
- A reversible object edit probe or target-app edit test passes when editability is promised.
- Rendered slides do not overflow.

### HTML Deck

Use when web-native quality matters.

Before building, read `references/html-production-lock.md`, then `references/html-deck-recipes.md`.

Recommended properties:

- Single HTML file or a small predictable folder.
- 16:9 slide canvas unless user specifies otherwise.
- Keyboard navigation.
- Stable dimensions for fixed UI elements.
- Clear print/PDF export route if needed.
- Local assets with predictable paths.
- Registered slide layouts through `data-layout`.
- Image slots with target ratios for local assets.

Bundled starter path:

```bash
python3 scripts/init_deck_project.py path/to/project --title "Deck Title"
python3 scripts/validate_html_deck.py path/to/project/index.html
```

Required checks:

- Open in browser.
- Inspect desktop and mobile or at least target presentation viewport.
- Check text overflow, image loading, keyboard navigation, and contrast.
- If canvas/WebGL is used, verify it is nonblank and does not cover content.

### Image-First PPTX

Use when art direction is more important than editability.

Before building, read `references/style-prompt-intake.md` if the user provided a style prompt, then `references/image-first-recipes.md`.

Recommended properties:

- Markdown plan first.
- Style Prompt Profile when user art direction exists.
- Prompt log for each slide.
- One-slide smoke test before full generation.
- Consistent image aspect ratio and safe areas.
- PPTX package with one full-slide image per page only when user accepts that tradeoff.

Required checks:

- User understands editability limits.
- Uploaded style prompt was parsed and normalized.
- Images match slide slots and language.
- No AI-generated footer, page number, title bar, or unwanted text inside images unless intended.
- Prompt log is saved for iteration.

## Escalation And Composition

When another skill is better for the concrete production task, compose with it:

- Use a PPTX or Presentations skill for PowerPoint file creation and editing.
- Use a browser skill for visual inspection of HTML slides.
- Use an image generation skill for image-first slides or visual assets.
- Use a documents or spreadsheets skill when the source material requires extraction or chart-ready data.

Knowledge Cat owns the deck strategy, routing, story, and QA contract. Specialized tools own their file-format mechanics.
