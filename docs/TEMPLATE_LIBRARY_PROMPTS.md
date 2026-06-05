# Template Library Prompts

Use these prompts to test or demonstrate the 44-style template library and the Portfolio Minimal HTML signature pack.

## 1. Pick A Style From The Library

```md
Use $knowledge-cat-ppt-skill. I need a 10-slide deck for this topic:

Topic:
Audience:
Outcome:
Source material:

Choose the best style from the 44-style template library. Explain why the style fits, choose the output lane, and create a deck brief plus slide plan before building.
```

Expected behavior:

- Read `references/style-template-library.md`.
- Choose one style seed such as `kc-24`, `kc-25`, `kc-28`, `kc-26`, or another better fit.
- State the lane: `native-pptx`, `html-deck`, `image-first-pptx`, or hybrid.
- Do not paste every style prompt into the answer.

## 2. Build With Portfolio Minimal

```md
Use $knowledge-cat-ppt-skill. Build a browser-based HTML deck using the `kc-24` Portfolio Minimal signature pack.

Topic:
Audience:
Outcome:
Slide count:
Source material:

Use the pack layout registry, include at least one local image slot, produce screenshots/contact sheet, and run the signature-pack checks before delivery.
```

Expected behavior:

- Use `assets/html-signature-packs/portfolio-minimal/layout-registry.json`.
- Use `data-pack="kc-24-portfolio-minimal"` and `data-style-seed="kc-24"` on every slide.
- Use at least 12 unique `custom-pm-*` layouts for a benchmark case.
- Run `scripts/check_signature_pack.py portfolio-minimal` when updating the bundled case study.

## 3. Surpass Guizang-Style HTML Depth

```md
Use $knowledge-cat-ppt-skill. Optimize this HTML deck path to beat Guizang's Swiss-style HTML deck strength. I want a concrete production pack, not just a plan.

Benchmark axis:
- template depth
- layout reuse
- image-slot discipline
- browser screenshots
- contact sheet
- QA report
- deterministic checks
```

Expected behavior:

- Treat `kc-24` Portfolio Minimal as the first direct benchmark lane.
- Produce or update a reusable signature pack and a case study.
- Run:

```bash
python3 scripts/validate_deck_plan.py examples/case-studies/portfolio-minimal/deck-plan.json
python3 scripts/validate_html_deck.py examples/case-studies/portfolio-minimal/index.html
python3 scripts/check_html_qa_artifacts.py examples/case-studies/portfolio-minimal
python3 scripts/check_signature_pack.py portfolio-minimal
python3 scripts/run_checks.py
```

- Only claim 99/100 for the HTML lane when browser-captured PNGs, contact sheet, QA report, and pack checks are present.

## 4. Convert A Pasted Style Table

```md
Use $knowledge-cat-ppt-skill. I pasted a large PPT style prompt table. Convert it into a reusable style-template library:

1. Deduplicate and name style seeds.
2. Map each style to best use cases.
3. Choose default output lanes.
4. Normalize protected brands, characters, franchises, and living-artist references.
5. Pick the first 3 signature packs worth implementing.
6. Write retest prompts and validation gates.
```

Expected behavior:

- Extract mechanisms, not raw prompt bulk.
- Prefer small signature-pack implementation steps over a giant style dump.
- Keep exact data, citations, and business copy editable unless the user chooses image-first.

## 5. Business Deck With Style Discipline

```md
Use $knowledge-cat-ppt-skill. Create a client-ready strategy deck from this material. Use the template library only if it improves the deck; editability and evidence matter more than visual spectacle.

Audience:
Decision:
Source material:
Must include:
Must avoid:
```

Expected behavior:

- Default toward `native-pptx` or hybrid if collaboration/editability matters.
- Use `kc-01`, `kc-24`, or `kc-25` only when they serve the audience and outcome.
- Keep evidence traceable and avoid flattened text-heavy images.

