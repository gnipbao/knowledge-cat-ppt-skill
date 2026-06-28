# Changelog

## 0.10.0 - Native Editable PPTX Evidence Loop

- Added `scripts/build_native_pptx.mjs`, a deck-plan-to-PPTX generator that creates native text, shapes, charts, tables, and speaker notes with `@oai/artifact-tool`.
- Added a six-slide native PPTX case study with the real `.pptx`, re-imported slide renders, contact sheet, layout JSON, object inspection, editability report, reversible text-object probe, and QA report.
- Added `scripts/check_pptx_editability.py` with native-object counts, chart/table/notes gates, and a negative image-only fixture.
- Added `scripts/probe_pptx_editability.py` to perform a reversible native DrawingML text-object mutation on a temporary PPTX copy.
- Added `scripts/check_native_pptx_case.py` and wired all native case gates into `scripts/run_checks.py`.
- Extended the deck-plan schema and validator with structured `native_content` payloads for cover, statement, chart, table, process, and closing slides.
- Updated runtime instructions, benchmark contracts, public docs, roadmap, and repository hygiene requirements for the native lane.
- Recorded the current imported-deck limitation: artifact-tool re-import inspection works, but the import/edit/re-export probe did not persist the changed text in this environment, so arbitrary imported-deck repairs remain delegated to a verified native editor.

## 0.9.0 - Portfolio Minimal Signature Pack

- Added the `kc-24` Portfolio Minimal HTML signature pack with a reusable template, 14-layout registry, and pack contract.
- Added a 12-slide `examples/case-studies/portfolio-minimal` case study with deck plan, local image slot, fixture-level screenshot, contact sheet, and QA report.
- Added `scripts/check_signature_pack.py` to enforce pack metadata, style seed binding, layout coverage, image slot ownership, and clean HTML validation.
- Wired the Portfolio Minimal case study and signature-pack check into `scripts/run_checks.py`.
- Updated repository hygiene requirements, retest prompts, and docs so the HTML lane has a concrete Guizang-class pack path instead of only a style roadmap.
- Added `docs/TEMPLATE_LIBRARY_PROMPTS.md` and expanded GitHub README guidance for the 44-style template library, Portfolio Minimal, and 99-point HTML evidence gate.

## 0.8.0 - Style Template Library

- Added `references/style-template-library.md` with 44 routed PPT style seeds, external style-site radar, protected-style normalization, and Guizang-surpass signature-pack targets.
- Updated runtime routing so large style tables and "surpass Guizang" requests load the style-template library before image-first or HTML production recipes.
- Expanded HTML visual-system guidance with a signature-pack roadmap for Portfolio Minimal, Minimal Data Story, Editorial Magazine, Dark SaaS Product, and Technical Blueprint packs.
- Added benchmark and QA guidance for style-template claims, plus a retest prompt for large style libraries.
- Updated README version metadata and repository checks for the new reference.

## 0.7.0 - Benchmark QA Hardening

- Added `references/benchmark-quality-gates.md` with 95+ scoring gates, case-study artifact contracts, and competitive claim rules.
- Added negative HTML failure fixtures plus `scripts/check_failure_fixtures.py` so validators prove known bad decks fail for the right reasons.
- Added `scripts/extract_pptx_text.py` with placeholder detection and a self-test for native PPTX text QA.
- Wired failure fixtures and PPTX text extraction self-test into `scripts/run_checks.py`.
- Updated QA, native PPTX, product-readiness, roadmap, and retest guidance around benchmark-grade evidence.

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
