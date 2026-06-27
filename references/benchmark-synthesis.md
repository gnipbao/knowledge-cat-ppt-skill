# Benchmark Synthesis

Use this file when improving the skill, explaining its architecture, or comparing presentation production patterns.

## Sources Reviewed

- PPT Master: https://github.com/hugohe3/ppt-master
- Guizang PPT Skill: https://github.com/op7418/guizang-ppt-skill
- gpt-image2-ppt-skills: https://github.com/JuneYaooo/gpt-image2-ppt-skills
- Frontend Slides: https://github.com/zarazhangrui/frontend-slides
- Anthropic PPTX Skill: https://github.com/anthropics/skills/tree/main/skills/pptx
- Academic PPTX Skill: https://github.com/Gabberflast/academic-pptx-skill
- Claude Office Skills presentation patterns: https://github.com/claude-office-skills/skills

Last benchmark refresh: 2026-06-04.

Current market signals:

- PPT Master is the strongest native-editable PPTX benchmark: document-to-PPTX, real PowerPoint shapes, template replication, animation, narration/video, live preview, public examples, and release packaging.
- Guizang PPT Skill is the strongest HTML-deck skill benchmark: single-file horizontal deck, opinionated aesthetics, reusable templates, layout locks, checklist discipline, image slot rules, screenshot handling, and static validation.
- gpt-image2-ppt-skills is a strong image-first benchmark: bundled visual styles, template clone mode, prompt-backed image generation, HTML viewer, PPTX packaging, and installer scripts.
- User-uploaded prompt libraries are a strong image-first signal: the portable mechanism is style DNA extraction, prompt normalization, slide-level prompt planning, and editability-aware routing.
- User-provided 40+ style libraries are a template-depth signal: the portable mechanism is not copying long prompts, but turning style rows into a routed style-template library, signature HTML packs, image-first profiles, and retest prompts.

## What The Strongest Skills Have In Common

They are not single prompts. They are production systems with:

- A clear trigger description
- A source-of-truth plan before final output
- Progressive disclosure through references
- A small number of explicit output lanes
- Template or layout constraints
- A quality loop that renders and inspects slides
- A path for user feedback after the first pass
- Honest boundaries around editability, fidelity, collaboration, and source evidence

## Lessons To Keep

### Native Editability Matters

PPT Master's strongest principle is that professional decks should remain editable. When the user expects a PowerPoint deliverable, the output should use real text, shapes, charts, and notes when practical.

Knowledge Cat default: professional decks start in native editable PPTX unless the user asks for HTML or visual-first output.

Knowledge Cat implementation: `scripts/build_native_pptx.mjs` now turns a structured deck plan into native text, shapes, chart, table, and notes when an artifact-tool workspace is available. The bundled `native-editable` case proves the net-new path with PPTX re-import, six rendered previews, object inspection, a negative image-only fixture, and a reversible text-object mutation. Imported-deck repairs remain outside this case's proof boundary.

### HTML Is An Excellent Agent Surface

Guizang and Frontend Slides show why HTML decks are strong for agent workflows: text files are easy to edit, preview, diff, and visually test. HTML is best when interaction, animation, single-file portability, or rapid visual iteration matters more than PowerPoint editability.

Knowledge Cat rule: HTML is a first-class lane, not a fallback, but it must be chosen intentionally.

### HTML Needs A Production Lock

Guizang's strongest transferable mechanism is not a visual style; it is a lock system. A browser deck becomes stable when the agent must choose a style package, copy from a known template, declare a layout on every slide, plan theme rhythm, bind local images to named slots and target ratios, run static validation, and visually inspect the rendered deck.

Knowledge Cat rule: production HTML decks load `references/html-production-lock.md` before `references/html-deck-recipes.md`. Every final slide declares `data-layout`, `data-title`, `data-role`, and `data-theme`; local images declare `data-image-slot` and target ratio metadata; static validation errors block delivery.

### Image-First Decks Are A Separate Product

gpt-image2-ppt-skills shows the value of image-first generation for dramatic visual style, template mimicry, and social sharing. The tradeoff is that slide content often becomes less editable.

Knowledge Cat rule: image-first decks are for visual impact, not routine business collaboration.

### Uploaded Style Prompts Should Drive Image-First Routing

Prompt tables and theme/style prompt libraries are not just inspiration lists. When a user uploads them and asks to use that visual language, they are providing art direction for generated slide surfaces.

Knowledge Cat rule: parse uploaded style prompts with `references/style-prompt-intake.md`, extract a Style Prompt Profile, and prefer `image-first-pptx` or hybrid image-first PPTX unless editability, charts, citations, or collaboration override the visual-first goal.

### Style Libraries Should Become Template Packs

Large style dumps are valuable only when they become a decision system. A 40+ style list should be compressed into style seeds, default output lanes, protected-style normalization, and a small set of signature packs.

Knowledge Cat rule: use `references/style-template-library.md` when the user asks for common PPT styles, style websites, or "surpass Guizang". Build the first benchmark HTML packs from `kc-24` Polished Minimal Portfolio, `kc-25` Minimal Data Story, `kc-28` Bold Editorial Magazine, `kc-26` Dark SaaS Product, and `kc-11` Architectural Blueprint.

### Template Replication Needs Structure

The best template workflows extract a reusable profile: canvas, colors, typography, layout archetypes, image crops, spacing, and reusable assets. They do not merely "make it look like this."

Knowledge Cat rule: template mode creates a template profile before building content.

### QA Must Be A Bug Hunt

Anthropic's PPTX workflow treats first render as suspect. Good deck generation requires content extraction, visual rendering, placeholder checks, and at least one fix loop for serious deliverables.

Knowledge Cat rule: no production deck is final until QA has inspected actual rendered output.

### Action Titles Are A Quality Multiplier

Academic-pptx-skill emphasizes the ghost deck test: action titles alone should tell the argument. This is one of the fastest ways to distinguish professional decks from topic lists.

Knowledge Cat rule: topic labels are draft scaffolding, not final slide titles.

## Architecture Implication

Knowledge Cat PPT should be a methodology toolbox:

- Main `SKILL.md`: route, workflow, and quality gates.
- `story-architecture.md`: content and narrative discipline.
- `engine-routing.md`: output lane selection and tradeoffs.
- `design-systems.md`: visual system and layout rules.
- `native-pptx-recipes.md`: editable PowerPoint production contract.
- `build_native_pptx.mjs`: executable plan-to-native-PPTX reference builder.
- `check_pptx_editability.py`, `probe_pptx_editability.py`, and `check_native_pptx_case.py`: deterministic native-object and case-study gates.
- `html-deck-recipes.md`: browser deck starter and layout recipes.
- `html-production-lock.md`: HTML layout registration, theme rhythm, local image slot contract, screenshot handling, and validation rules.
- `image-first-recipes.md`: visual deck prompt plan and editability contract.
- `style-prompt-intake.md`: user-uploaded theme/style prompt parsing, Style Prompt Profile, prompt normalization, and image-first routing.
- `style-template-library.md`: 44 style seeds, website radar, Guizang-surpass priority, and signature-pack contract.
- `template-replication.md`: template extraction and reuse.
- `qa-rubric.md`: final verification loop.
- `validate_deck_plan.py`: deterministic guardrail for JSON plans.
- `validate_html_deck.py`: deterministic guardrail for HTML deck structure.
- `init_deck_project.py`: runnable starter path for the HTML lane.
- `open-source-product.md`: repository-readiness contract.

## Failure Modes To Avoid

- A pretty prompt with no build pathway.
- A native PPTX workflow that ignores visual QA.
- A native PPTX claim supported only by text extraction instead of object inspection and edit probing.
- An HTML workflow that pretends to satisfy PowerPoint collaboration needs.
- An image-first workflow that hides lack of editability.
- Template mimicry without permission or layout analysis.
- A giant monolithic SKILL.md that loads everything for every request.
- Quality claims based on code inspection instead of rendered slides.
- A style library that remains a long prompt dump instead of becoming routed templates, examples, and validators.
