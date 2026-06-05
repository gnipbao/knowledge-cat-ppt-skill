# Portfolio Minimal Signature Pack

Style seed: `kc-24` from `references/style-template-library.md`.

Use this pack when the user asks for a polished minimal portfolio, architecture-style company profile, consulting proposal, executive HTML deck, or a Guizang/Sistema-like Swiss portfolio feel without copying another skill's templates.

## Root Contract

The pack is designed to beat generic HTML slides by making style executable:

- every slide uses `data-pack="kc-24-portfolio-minimal"`
- every slide uses `data-style-seed="kc-24"`
- every slide declares one `custom-pm-*` layout from `layout-registry.json`
- decks of 10+ slides should use at least 10 unique pack layouts
- local images must live under `images/` with `data-image-slot` and `data-slot-ratio`
- final case studies must include a deck plan, validation run, screenshots/contact sheet, and QA report

## Visual DNA

- canvas: white, light gray, or hard black reset slides
- type: Inter/Helvetica-like sans, huge numbers, compact metadata
- structure: strict grid, top-left navigation, thin rules, high negative space
- imagery: low-saturation office, product, architecture, UI, or abstract proof images
- forbidden moves: gradient blobs, decorative cards, fake laptop frames, crowded bullets, generic icons, unsupported logos

## Layout Registry

The pack currently defines 14 layouts:

1. `custom-pm-hero-index`
2. `custom-pm-stamp-field`
3. `custom-pm-number-split`
4. `custom-pm-image-grid`
5. `custom-pm-photo-list`
6. `custom-pm-minimal-map`
7. `custom-pm-vertical-timeline`
8. `custom-pm-dark-network`
9. `custom-pm-three-steps`
10. `custom-pm-logo-grid`
11. `custom-pm-problem-solution`
12. `custom-pm-equation`
13. `custom-pm-arrow-process`
14. `custom-pm-closing-decision`

## 99-Point HTML Gate

To claim this pack is benchmark-grade, run:

```bash
python3 scripts/validate_deck_plan.py examples/case-studies/portfolio-minimal/deck-plan.json
python3 scripts/validate_html_deck.py examples/case-studies/portfolio-minimal/index.html
python3 scripts/check_html_qa_artifacts.py examples/case-studies/portfolio-minimal
python3 scripts/check_signature_pack.py portfolio-minimal
```

The pack is not benchmark-grade if the example only has a template but no rendered or fixture-labeled visual proof.
