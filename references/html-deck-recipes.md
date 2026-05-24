# HTML Deck Recipes

Use this reference when the selected output lane is `html-deck` or when a fast visual prototype is needed before converting to another format.

## Source Template

Use `assets/html-template/index.html` as the starter. It is intentionally lightweight:

- 16:9 desktop slide canvas
- Mobile fallback that stacks slides vertically
- Keyboard navigation
- Print-friendly CSS
- Light/dark theme switching through `data-theme`
- Action-title aware slide structure
- No external dependencies

Create a project with:

```bash
python3 scripts/init_deck_project.py path/to/project --title "Deck Title"
```

Then replace `<!-- SLIDES_HERE -->` with real slide sections.

## Required Section Contract

Every slide must be a `<section>` with:

```html
<section class="slide layout-name" data-title="Action title" data-role="Hook" data-theme="light">
  ...
</section>
```

Required attributes:

- `data-title`: the action title of the slide.
- `data-role`: the story role, such as Hook, Context, Proof, Mechanism, Comparison, Decision, or Closing.
- `data-theme`: `light` or `dark`.

Rules:

- Do not leave `{{DECK_TITLE}}`, `SLIDES_HERE`, or placeholder copy in the final deck.
- Prefer complete-sentence action titles.
- Keep one primary visual job per slide.
- Use `source refs` in speaker notes or visible footnotes when claims matter.
- Keep bottom navigation clear; do not place important content below 92vh.

## Layout Recipes

### 1. Hero

Use for covers, section openers, or major pivots.

```html
<section class="slide hero" data-title="The title states the deck's promise" data-role="Hook" data-theme="light">
  <div>
    <p class="kicker">Knowledge Cat PPT</p>
    <h1 class="hero-title">The title states the deck's promise</h1>
  </div>
  <p class="lead">One sentence that names the audience, stakes, or transformation.</p>
  <div class="footnote"><span>Source: user brief</span><span>01</span></div>
</section>
```

### 2. Statement

Use for a sharp insight with a short supporting note.

```html
<section class="slide statement" data-title="One claim changes how the audience reads the rest" data-role="Insight" data-theme="dark">
  <div>
    <p class="kicker">Insight</p>
    <h2 class="action-title">One claim changes how the audience reads the rest</h2>
  </div>
  <p class="lead">Support the claim with a concise explanation, not a paragraph pile.</p>
</section>
```

### 3. Two Column

Use for before/after, old/new, or problem/solution.

```html
<section class="slide two-col" data-title="The old workflow loses trust before the demo" data-role="Comparison" data-theme="light">
  <div>
    <p class="kicker">Before / After</p>
    <h2 class="action-title">The old workflow loses trust before the demo</h2>
  </div>
  <div class="grid-3">
    <article class="card"><strong>Slow handoff</strong><p class="body">Context is rewritten at every stage.</p></article>
    <article class="card"><strong>Weak proof</strong><p class="body">Claims arrive before evidence.</p></article>
    <article class="card"><strong>Late QA</strong><p class="body">Quality is checked only after production.</p></article>
  </div>
</section>
```

### 4. Evidence Exhibit

Use for data, research, screenshots, or an annotated diagram.

```html
<section class="slide evidence" data-title="Three signals show the category is ready" data-role="Proof" data-theme="light">
  <div>
    <p class="kicker">Evidence</p>
    <h2 class="action-title">Three signals show the category is ready</h2>
  </div>
  <div class="exhibit">
    <div class="bar-list">
      <div class="bar-row"><span>Search demand</span><span class="bar-track"><span class="bar-fill" style="--value:82%"></span></span><strong>82</strong></div>
      <div class="bar-row"><span>Paid urgency</span><span class="bar-track"><span class="bar-fill" style="--value:68%"></span></span><strong>68</strong></div>
      <div class="bar-row"><span>Tool maturity</span><span class="bar-track"><span class="bar-fill" style="--value:76%"></span></span><strong>76</strong></div>
    </div>
    <p class="meta">Source: user-provided research sample</p>
  </div>
</section>
```

### 5. Image Plus Annotation

Use when a screenshot, product surface, or generated visual is the main evidence.

```html
<section class="slide two-col" data-title="The product surface proves the workflow is inspectable" data-role="Case" data-theme="light">
  <div class="image-slot">
    <span class="placeholder">Replace with images/04-product.png</span>
  </div>
  <div>
    <p class="kicker">Case</p>
    <h2 class="action-title">The product surface proves the workflow is inspectable</h2>
    <p class="lead">Use annotations to explain what the audience should notice.</p>
  </div>
</section>
```

### 6. Closing Decision

Use for a clear next step.

```html
<section class="slide statement" data-title="The next move is to test one deck through the full QA loop" data-role="Decision" data-theme="dark">
  <div>
    <p class="kicker">Decision</p>
    <h2 class="action-title">The next move is to test one deck through the full QA loop</h2>
  </div>
  <p class="lead">Name the owner, artifact, deadline, and pass/fail signal.</p>
</section>
```

## Validation

Run:

```bash
python3 scripts/validate_html_deck.py path/to/project/index.html
```

Minimum pass:

- No unreplaced template markers.
- At least one slide exists.
- Every slide has `data-title` and `data-role`.
- No weak placeholder text.
- Slide count matches `deck-plan.json` when a plan is provided.

For production delivery, static validation is not enough. Open the HTML deck in a browser and visually inspect representative slides.
