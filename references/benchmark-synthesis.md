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

Last benchmark refresh: 2026-05-24.

Current market signals:

- PPT Master is the strongest native-editable PPTX benchmark: document-to-PPTX, real PowerPoint shapes, template replication, animation, narration/video, live preview, public examples, and release packaging.
- Guizang PPT Skill is the strongest HTML-deck skill benchmark: single-file horizontal deck, opinionated aesthetics, reusable templates, layout locks, checklist discipline, and static validation.
- gpt-image2-ppt-skills is a strong image-first benchmark: bundled visual styles, template clone mode, prompt-backed image generation, HTML viewer, PPTX packaging, and installer scripts.

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

### HTML Is An Excellent Agent Surface

Guizang and Frontend Slides show why HTML decks are strong for agent workflows: text files are easy to edit, preview, diff, and visually test. HTML is best when interaction, animation, single-file portability, or rapid visual iteration matters more than PowerPoint editability.

Knowledge Cat rule: HTML is a first-class lane, not a fallback, but it must be chosen intentionally.

### Image-First Decks Are A Separate Product

gpt-image2-ppt-skills shows the value of image-first generation for dramatic visual style, template mimicry, and social sharing. The tradeoff is that slide content often becomes less editable.

Knowledge Cat rule: image-first decks are for visual impact, not routine business collaboration.

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
- `html-deck-recipes.md`: browser deck starter and layout recipes.
- `image-first-recipes.md`: visual deck prompt plan and editability contract.
- `template-replication.md`: template extraction and reuse.
- `qa-rubric.md`: final verification loop.
- `validate_deck_plan.py`: deterministic guardrail for JSON plans.
- `validate_html_deck.py`: deterministic guardrail for HTML deck structure.
- `init_deck_project.py`: runnable starter path for the HTML lane.
- `open-source-product.md`: repository-readiness contract.

## Failure Modes To Avoid

- A pretty prompt with no build pathway.
- A native PPTX workflow that ignores visual QA.
- An HTML workflow that pretends to satisfy PowerPoint collaboration needs.
- An image-first workflow that hides lack of editability.
- Template mimicry without permission or layout analysis.
- A giant monolithic SKILL.md that loads everything for every request.
- Quality claims based on code inspection instead of rendered slides.
