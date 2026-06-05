# Retest Prompts

Use these prompts to test whether Knowledge Cat PPT behaves like a production skill rather than a generic slide prompt.

## 1. Vague Business Request

```md
Use $knowledge-cat-ppt-skill. I need a deck for my AI product. Make it impressive.
```

Expected behavior:

- Ask for audience, outcome, source, and output lane if needed.
- Do not start with visual style.
- Offer a safe default path if the user wants to proceed.

## 2. Source-To-Deck

```md
Use $knowledge-cat-ppt-skill. Turn this article into an 8-slide executive deck for a founder audience. Editable PPTX preferred.
```

Expected behavior:

- Build a deck brief.
- Create a ghost deck and slide plan.
- Select native PPTX.
- Track source claims.

## 3. Template Request

```md
Use $knowledge-cat-ppt-skill. I have a company-template.pptx. Make a 10-page product strategy deck in the same style.
```

Expected behavior:

- Enter template mode.
- Create a template profile before building.
- Map slides to template layouts.
- Preserve editability if possible.

## 4. HTML Visual Talk

```md
Use $knowledge-cat-ppt-skill. Build a browser-based keynote with keyboard navigation and a bold visual rhythm.
```

Expected behavior:

- Select HTML deck.
- Use browser QA.
- Avoid pretending the result is a native PPTX.

## 5. Image-First Social Carousel

```md
Use $knowledge-cat-ppt-skill. Create a Xiaohongshu-style carousel from my framework. Visual impact matters more than editability.
```

Expected behavior:

- Select image-first or social carousel path.
- Confirm aspect ratio and text safety.
- Save prompt or plan artifacts.

## 6. Academic Talk

```md
Use $knowledge-cat-ppt-skill. Make slides for my conference paper. I need citations and a conclusions slide.
```

Expected behavior:

- Use academic narrative spine.
- Enforce action titles, one exhibit per results slide, citations, and conclusion.
- Avoid decorative design.

## 7. Deck Review

```md
Use $knowledge-cat-ppt-skill. Review this deck and tell me why it feels weak.
```

Expected behavior:

- Review first.
- Lead with prioritized issues.
- Separate story, evidence, visual, and technical problems.

## 8. QA Discipline

```md
Use $knowledge-cat-ppt-skill. The slides look done. Can we ship?
```

Expected behavior:

- Refuse to declare final without rendered visual QA.
- Run or request the necessary checks.
- Report remaining risks.

## 9. HTML Production Lock

```md
Use $knowledge-cat-ppt-skill. Build a 7-slide HTML deck from this product strategy memo. Include one local product screenshot slot, use at least five layout types, and run the HTML validator before delivery.
```

Expected behavior:

- Select `html-deck` only if browser delivery fits the user need.
- Read `references/html-production-lock.md` before `references/html-deck-recipes.md`.
- Declare `data-layout`, `data-title`, `data-role`, and `data-theme` on every slide.
- Give local images `data-image-slot`, target ratio metadata, and meaningful alt text.
- Report validator output and any visual QA that was or was not performed.

## 10. Uploaded Style Prompt Image-First

```md
Use $knowledge-cat-ppt-skill. I uploaded a table of PPT theme/style prompts. Pick the best style for a 9-slide AI product launch deck and prioritize Image2/GPT-Image style generation unless you think editability should override it.
```

Expected behavior:

- Detect the uploaded prompt table as a style prompt source.
- Read `references/style-prompt-intake.md` before `references/image-first-recipes.md`.
- Prefer `image-first-pptx` or hybrid image-first PPTX, then state the editability tradeoff.
- Extract a Style Prompt Profile instead of blindly pasting the raw prompt.
- Produce a slide-level prompt plan with visual intent, style variation, text-in-image policy, aspect ratio, and prompt risk.
- Preserve exact product claims, metrics, screenshots, and citations outside images when they must remain editable or verifiable.

## 11. HTML Benchmark Evidence

```md
Use $knowledge-cat-ppt-skill. Build a 9-slide browser-based HTML deck from this strategy memo. It must feel like a high-end editorial/portfolio presentation, use at least five registered layouts, include a local image slot, produce screenshots/contact sheet, and explain why HTML is the right lane instead of native PPTX.
```

Expected behavior:

- Select `html-deck` only after stating why browser delivery is the right lane.
- Read `references/html-production-lock.md` and `references/html-visual-systems.md` before writing final HTML.
- Choose one concrete HTML visual system such as Architectural Minimal, Editorial Proof, or Data Command.
- Create a deck plan with registered layouts and theme rhythm.
- Include at least one local image under `images/` with `data-image-slot`, target ratio metadata, and alt text.
- Run `scripts/validate_html_deck.py`.
- Produce screenshot/contact-sheet artifacts or clearly label fixture-level artifacts when browser capture is unavailable.
- Write `qa-report.md` with Visual QA, Contact Sheet, Fix Loop, and Known Limitations.

## 12. Native PPTX Text QA

```md
Use $knowledge-cat-ppt-skill. Build an editable 6-slide native PPTX for a board update. Before delivery, prove that placeholder text is gone and tell me what remains editable.
```

Expected behavior:

- Select `native-pptx` because the user asked for editable PowerPoint.
- Read `references/native-pptx-recipes.md` and `references/qa-rubric.md`.
- Run `scripts/extract_pptx_text.py path/to/output.pptx --fail-on-placeholders` when the file exists locally.
- State editable promises and non-editable exceptions.
- Avoid claiming full editability if slide text is flattened into images.

## 13. Benchmark Claim Discipline

```md
Use $knowledge-cat-ppt-skill. Optimize this skill until it is better than open-source PPT skills. Tell me when it is the best.
```

Expected behavior:

- Enter Productization Mode.
- Read `references/open-source-product.md` and `references/benchmark-quality-gates.md`.
- Translate "best" into named benchmark axes, evidence artifacts, and deterministic checks.
- Run `scripts/run_checks.py` after edits.
- Avoid unsupported "best in market" claims unless a named benchmark comparison was actually performed.

## 14. Style Template Library

```md
Use $knowledge-cat-ppt-skill. I pasted a 40+ row PPT style prompt library plus common PPT style websites. Pick the best route to surpass Guizang for HTML decks, but keep business decks editable when needed.
```

Expected behavior:

- Read `references/style-template-library.md`.
- Avoid pasting all prompts into the answer.
- Choose `kc-24` or `kc-25` first when the goal is to beat Guizang's Swiss/HTML template strength unless the topic demands another style.
- State whether the selected style should become an HTML signature pack, image-first profile, or native PPTX direction.
- Normalize protected franchise/character styles into generic traits.
- Name the missing evidence needed before making a benchmark-grade claim: template pack, sample deck, screenshots/contact sheet, QA report, and validator coverage.

## 15. Portfolio Minimal Signature Pack

```md
Use $knowledge-cat-ppt-skill. Optimize the HTML lane until it can beat Guizang's Swiss-style HTML deck strength. Show me the concrete pack, not just a plan.
```

Expected behavior:

- Read `references/style-template-library.md`, `references/html-visual-systems.md`, and `references/benchmark-quality-gates.md`.
- Select `kc-24` Portfolio Minimal as the first direct Guizang-class pack unless the user gives a different target.
- Use `assets/html-signature-packs/portfolio-minimal/layout-registry.json` rather than inventing one-off classes.
- Produce or update a case study with at least 12 slides, at least 12 unique `custom-pm-*` layouts, pack metadata, style seed metadata, local image slot metadata, contact sheet, and QA report.
- Run:

```bash
python3 scripts/validate_deck_plan.py examples/case-studies/portfolio-minimal/deck-plan.json
python3 scripts/validate_html_deck.py examples/case-studies/portfolio-minimal/index.html
python3 scripts/check_html_qa_artifacts.py examples/case-studies/portfolio-minimal
python3 scripts/check_signature_pack.py portfolio-minimal
python3 scripts/run_checks.py
```

- Do not claim final 99/100 visual quality if only fixture-level SVG screenshots exist; call it mechanism-ready and name browser-captured PNGs as the final evidence upgrade.
