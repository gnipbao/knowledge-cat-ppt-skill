# Changelog

## 0.6.0 - Uploaded Style Prompt Image-First

- Added `references/style-prompt-intake.md` for user-uploaded theme/style prompts, prompt tables, visual DNA blocks, and Image2/GPT-Image-driven PPT styling.
- Updated routing so uploaded visual style prompts prefer `image-first-pptx` or hybrid image-first PPTX unless editability, charts, citations, or collaboration should override it.
- Expanded `references/image-first-recipes.md` with Style Prompt Profile, prompt-table handling, text-in-image policy, prompt structure, and representative-slide smoke testing.
- Added deck-plan schema fields for style prompt source, style prompt profile, image generation strategy, prompt log path, and slide-level prompt metadata.
- Added a retest prompt for uploaded style prompt image-first generation.

## 0.5.0 - HTML Production Lock

- Added `references/html-production-lock.md` for style package selection, layout registration, theme rhythm, local image slots, screenshot handling, static validation, and rendered QA.
- Updated `SKILL.md`, engine routing, and HTML recipes to load the production lock before building final browser decks.
- Strengthened `validate_html_deck.py` with `data-layout`, theme rhythm, local image slot, target ratio, alt text, and SVG text checks.
- Updated the HTML deck initializer and sample deck to emit `data-layout` metadata.
- Refreshed the Guizang PPT Skill benchmark synthesis with portable mechanisms rather than template imitation.

## 0.4.0 - Chinese Docs And Mode Previews

- Added Chinese documentation in `README_CN.md`.
- Added bilingual documentation in `README_BILINGUAL.md`.
- Added three local PNG mode preview images for native PPTX, HTML deck, and image-first PPTX.
- Kept editable SVG preview sources under `docs/images/`.
- Updated the main README with language links and visual mode previews.

## 0.3.0 - Repo-Ready Open Source Package

- Added standalone repository packaging.
- Added GitHub Actions validation workflow.
- Added bug, feature, and deck-quality issue templates.
- Added pull request template.
- Added `.gitignore`, `.gitattributes`, and `VERSION`.
- Added repository hygiene checker.
- Added publishing guide and roadmap.

## 0.2.0 - Productization Pass

- Added an HTML deck starter template.
- Added HTML deck initialization and static validation scripts.
- Added bundled check runner.
- Added open-source README, contributing guide, security notes, and MIT license.
- Added lane-specific production recipes for HTML, native PPTX, and image-first decks.
- Expanded product readiness and release guidance.

## 0.1.0 - Initial Skill

- Added story-first `SKILL.md`.
- Added engine routing, story architecture, design systems, template replication, QA rubric, benchmark synthesis, retest prompts, deck-plan schema, and deck-plan validator.
