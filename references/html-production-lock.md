# HTML Production Lock

Use this reference when the selected output lane is `html-deck`, especially for client-ready decks, web presentations, public talks, visual prototypes, or HTML decks that will later be captured as images/PDF.

This file turns the HTML lane into an executable production system. It is inspired by the strongest open-source HTML deck skills, especially Guizang PPT Skill, but it does not copy their templates, visual systems, or wording. Knowledge Cat keeps its broader multi-lane role: HTML is a first-class lane, not the only lane.

## Root Rule

Do not treat HTML as "free layout." A browser deck is reliable only when style, layout, image slots, validation, and visual QA are locked before final slide writing.

## Source Boundary

Mechanisms absorbed:

- choose a style system before writing slides
- copy from a known template rather than inventing markup from scratch
- require every slide to declare a registered layout
- plan theme rhythm across the deck
- bind images to named slots and target ratios
- run static checks before visual inspection
- inspect rendered output before final delivery

Mechanisms not absorbed:

- Guizang's specific visual identities
- Guizang's exact templates, class names, sponsors, or private golden-source paths
- the assumption that every presentation should be a single-file HTML deck

## HTML Deck Contract

Every production HTML deck must have:

- `index.html`
- `deck-plan.json` when the deck has more than three slides or uses source evidence
- `images/` for local image assets, even if empty at first
- `<title>` replaced with the real deck title
- no unresolved `SLIDES_HERE`, `{{DECK_TITLE}}`, `TODO`, placeholder copy, or "replace with" text
- one selected design posture from `references/design-systems.md`
- a declared layout on every slide
- a theme rhythm plan
- a static validation run
- a rendered visual QA pass for final delivery

## Style Package Selection

Before writing slide markup, choose one primary style package:

| Style package | Best for | Use with |
|---|---|---|
| Strategic Minimal | executive, consulting, investor, board, product strategy | `hero`, `statement`, `two-col`, `evidence`, `comparison` |
| Editorial Proof | essays, talks, thought leadership, human stories | `hero`, `quote`, `image-annotation`, `two-col`, `closing-decision` |
| Data Command | market maps, dashboards, analytical reports | `evidence`, `data-dashboard`, `comparison`, `timeline` |
| Product Lab | SaaS, AI tools, product demos, workflow explanation | `image-annotation`, `system-map`, `process`, `evidence` |
| Teaching Board | workshops, courses, explainers | `process`, `timeline`, `two-col`, `closing-decision` |
| Social Carousel | Xiaohongshu, LinkedIn, WeChat, saveable frameworks | `hero`, `statement`, `comparison`, `quote` |
| Vision Keynote | launch, culture, public keynote | `hero`, `statement`, `image-annotation`, `closing-decision` |

Rules:

- Pick one primary style package and keep it stable.
- If a custom visual direction is needed, name it and map it to the closest package.
- Do not mix multiple visual languages in one deck unless the story explicitly needs a section break.
- Do not accept arbitrary decoration as a style system. A style package must define typography, palette, layout families, image treatment, chart treatment, and density.

## Layout Registry

Every slide section must declare `data-layout`:

```html
<section class="slide hero" data-layout="hero" data-title="The audience shift is visible in the first minute" data-role="Hook" data-theme="light">
  ...
</section>
```

Built-in layout names:

- `hero`
- `statement`
- `two-col`
- `evidence`
- `image-annotation`
- `closing-decision`
- `comparison`
- `timeline`
- `process`
- `system-map`
- `data-dashboard`
- `quote`

Custom layout rules:

- Use `data-layout="custom-short-name"` only when a built-in layout cannot express the slide job.
- Add or verify the CSS for the custom structure in the deck stylesheet before using it.
- Explain the custom layout in `deck-plan.json` under `visual` or `asset_needs`.
- Do not create more than two custom layouts in a production deck unless the task is explicitly a visual-system prototype.

## Class Source Rule

Use classes already defined in `assets/html-template/index.html` or classes you intentionally add to the deck stylesheet.

Before writing a custom class:

1. Search the template stylesheet.
2. Prefer an existing layout or utility.
3. If a new class is needed, define it once in the stylesheet.
4. Do not rely on class names that exist only in another skill, another template, or an imagined design system.

## Theme Rhythm

Plan the `data-theme` sequence before final slide writing.

Rules:

- Every slide must use `data-theme="light"` or `data-theme="dark"`.
- Avoid three consecutive slides with the same theme in decks of five or more slides.
- Decks of eight or more slides should include at least two dark slides and at least two light slides.
- Use spacious reset slides every three to five slides.
- The theme rhythm must serve the story, not merely alternate colors.

Example rhythm:

```txt
01 light hero
02 dark statement
03 light evidence
04 light image-annotation
05 dark statement
06 light comparison
07 light process
08 dark closing-decision
```

## Image Slot Contract

Local images must be stored in `images/` and named with slide number plus semantic purpose:

```txt
images/04-product-surface.png
images/06-workflow-map.jpg
images/08-closing-visual.png
```

Every local image must declare a slot:

```html
<img src="images/04-product-surface.png" alt="Annotated product workflow" data-image-slot="04-main-16x10" data-slot-ratio="16:10">
```

Rules:

- `data-image-slot` must connect the image to the slide number, role, or layout slot.
- Include the target ratio in `data-image-slot` or `data-slot-ratio`.
- Use `alt` text for meaningful images.
- Match image generation or cropping to the final slot before insertion.
- Do not place slide titles, page numbers, footers, logos, or page chrome inside generated images unless the image is being shown as a screenshot of an existing artifact.
- Use screenshots as evidence. Preserve exact UI, labels, metrics, and sensitive-data redactions unless the user asks for a redesign.

Common ratios:

| Use | Ratio |
|---|---|
| full-width hero strip | `21:9` |
| product screenshot or UI scene | `16:10` |
| standard exhibit | `16:9` |
| square social proof card | `1:1` |
| vertical carousel image | `3:4` |
| compact photo grid | `3:2` |

## Screenshot Handling

If the user provides product screenshots, dashboards, webpages, code screenshots, Figma frames, or old deck screenshots:

1. Ask or infer whether the goal is faithful presentation, beautified framing, or redesign.
2. Preserve exact content when the screenshot is evidence.
3. Use a calm background canvas or crop wrapper before redesigning the screenshot itself.
4. Redesign only when the screenshot is too long, too narrow, too cluttered, or meant to become a conceptual visual.
5. Keep the output ratio bound to the slide slot.

## Static Validation

Run:

```bash
python3 scripts/validate_html_deck.py path/to/project/index.html
```

Treat errors as blockers. Treat warnings as work queue items unless the user explicitly asked for a rough prototype.

The validator checks:

- required slide attributes
- weak action titles
- unresolved placeholders
- slide count vs `deck-plan.json`
- repeated titles
- theme rhythm
- layout registration
- local image slot declarations
- risky SVG text labels

## Rendered QA

Static validation is not enough. For final HTML decks:

1. Open the deck in a browser.
2. Verify keyboard navigation.
3. Inspect representative slides at desktop size.
4. Check mobile or print/PDF output when promised.
5. Look for text overflow, image crop errors, footer collisions, contrast problems, and repeated layout fatigue.
6. Fix affected slides and re-run validation.

Do not claim client-ready quality from code inspection alone.

## Failure Modes

- HTML deck selected when the user needed editable PowerPoint.
- Layouts look nice individually but the story has no rhythm.
- A slide uses a class that is not defined in the active template.
- Images are inserted without target ratio or slot ownership.
- Screenshots are redesigned when the user needed faithful evidence.
- Dark/light themes alternate mechanically without narrative reason.
- SVG diagrams contain text labels that become hard to edit, translate, or inspect.
- The final response says the deck is ready without browser QA.

## Retest Prompts

Use these after changing this skill or the HTML lane:

```md
Use $knowledge-cat-ppt-skill to create a 7-slide HTML deck from a product strategy memo. The deck must declare data-layout on every slide, use at least five layout types, include one local screenshot slot, and pass validate_html_deck.py.
```

```md
Use $knowledge-cat-ppt-skill to review this HTML deck. Focus only on layout registration, theme rhythm, image slots, placeholder leakage, and whether the deck was visually QA'd.
```

