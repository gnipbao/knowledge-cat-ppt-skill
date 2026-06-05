# Roadmap

## 0.4.x - Public Repository Hardening

- Add final repository URL.
- Add public mode preview images for native PPTX, HTML deck, and image-first PPTX.
- Add CI status badge after the repository is live.

## 0.5.x - Output Examples

- Editable PPTX case study.
- HTML keynote case study.
- Image-first social carousel case study.
- QA report for each case study.
- HTML benchmark case study with local image slot and screenshot/contact-sheet artifacts.

## 0.6.x - Stronger Validators

- HTML viewport screenshot checks.
- Deck-plan to HTML slide-count and title matching.
- HTML benchmark QA artifact check for contact sheets, screenshots, and fix-loop reports.
- Optional schema validation with `jsonschema` when installed.

## 0.7.x - Benchmark QA Hardening

- Add failure fixtures for missing layout metadata, missing image slots, unresolved markers, and plan/HTML slide-count mismatch.
- Add native PPTX text extraction with placeholder detection and a self-test.
- Add benchmark quality gates and case-study artifact contracts.

## 0.8.x - Style Template Library

- Add 44 routed PPT style seeds.
- Add common style-site radar.
- Add Guizang-surpass signature-pack priority.
- Add template-library retest prompts.

## 0.9.x - Portfolio Minimal Signature Pack

- Add `kc-24` Portfolio Minimal HTML signature pack.
- Add 14-layout registry and reusable template.
- Add 12-slide case study with local image slot.
- Add browser-captured PNG screenshots and contact sheet.
- Add `scripts/check_signature_pack.py`.
- Wire signature-pack checks into `scripts/run_checks.py`.

## 0.10.x - Multi-Lane Case Studies

- Promote `references/html-visual-systems.md` into the default HTML production path.
- Add browser-captured PNG screenshots for all benchmark HTML cases.
- Add a contact-sheet review rubric that scores visual rhythm separately from static validation.
- Add a minimal native PPTX example when a stable renderer is selected.

## 1.0.0 - Stable Skill Contract

- Stable SKILL.md workflow contract.
- Stable deck-plan JSON schema.
- Public examples across all output lanes.
- Release notes with migration guidance.
- HTML lane can demonstrate benchmark-grade output with plan, deck, screenshots, contact sheet, QA report, and validation logs.
- HTML lane has at least three implemented signature packs: Portfolio Minimal, Minimal Data Story, and Editorial Magazine.
- Native PPTX lane can demonstrate editability with text extraction, render QA, and a documented exception list.
