# Benchmark Quality Gates

Use this reference when a deck, example, or skill release is expected to be benchmark-grade, public-facing, or compared with other PPT skills.

## Principle

Benchmark-grade quality is not a claim. It is an evidence package:

- A strong story spine.
- A deliberate output lane.
- A reusable visual system.
- A rendered or inspected artifact.
- A QA report with fixes and residual risk.
- Deterministic checks that catch both passing and failing examples.

Do not say "best", "beyond all open-source PPT skills", or "benchmark-grade" unless the artifact has been compared against named alternatives or has passed the gates below.

## Scorecard

Score out of 100:

| Area | Points | Gate |
|---|---:|---|
| Audience shift and story spine | 18 | Action titles tell a complete argument for a specific audience. |
| Output-lane fit | 14 | Native PPTX, HTML, or image-first is chosen for the real job, with tradeoffs stated. |
| Visual system | 18 | Layout rhythm, type, color, imagery, chart rules, and negative space form a coherent system. |
| Evidence discipline | 12 | Claims, numbers, screenshots, and citations are sourced or labeled as assumptions. |
| Rendered QA artifacts | 16 | Screenshots, contact sheet, PPTX render, PDF export, or equivalent visual proof exists. |
| Reproducibility | 12 | Source plan, assets, validation logs, and negative fixtures are present where applicable. |
| Handoff quality | 10 | Output paths, assumptions, editability promises, and next iteration point are clear. |

For style-template claims, the visual-system score requires a named style seed or signature pack from `references/style-template-library.md`, plus a reason that the lane matches the user's editability and story needs.

95+ requires all of these:

- No P0 issue from `references/qa-rubric.md`.
- At least one fix-and-recheck loop or a clear note that the first pass was intentionally draft-only.
- The chosen lane has its required case-study artifacts.
- The artifact can be reopened, rendered, or statically validated with local tools.
- Any "editable" promise has been checked by text extraction, object inspection, or target-app review.
- Any local images have visible provenance or placeholder status.

## Case Study Artifact Contract

### Native PPTX

Required for a publishable native PPTX case study:

- `deck-brief.md`
- `deck-plan.json` or `deck-plan.md`
- `.pptx` source output
- rendered preview images and a contact sheet produced from the reopened final PPTX
- object inspection log
- PPTX text extraction result from `scripts/extract_pptx_text.py`
- editability report from `scripts/check_pptx_editability.py`
- reversible object edit probe from `scripts/probe_pptx_editability.py`
- `qa-report.md` with editability promises and exceptions

Minimum command:

```bash
python3 scripts/extract_pptx_text.py path/to/output.pptx --fail-on-placeholders
python3 scripts/check_pptx_editability.py path/to/output.pptx --fail-on-image-only-slides
python3 scripts/probe_pptx_editability.py path/to/output.pptx
```

Bundled reference case:

```bash
python3 scripts/check_native_pptx_case.py
```

### HTML Deck

Required for a publishable HTML case study:

- `deck-plan.json`
- `index.html`
- local `images/` assets where used
- `screenshots/` with representative slides and a contact sheet
- static validation log from `scripts/validate_html_deck.py`
- `qa-report.md` with Visual QA, Contact Sheet, Fix Loop, and Known Limitations sections
- when using a named style seed, the chosen `kc-XX` style or signature pack is recorded in the deck plan or QA report

Minimum commands:

```bash
python3 scripts/validate_deck_plan.py path/to/deck-plan.json
python3 scripts/validate_html_deck.py path/to/index.html
python3 scripts/check_html_qa_artifacts.py path/to/case-study
python3 scripts/check_signature_pack.py portfolio-minimal  # when the case uses a signature pack
```

### Image-First PPTX

Required for a publishable image-first case study:

- `deck-brief.md`
- `style-prompt-profile.md` or equivalent prompt source summary
- slide-level prompt log
- generated image outputs or source images
- `.pptx` or PDF assembly
- representative rendered QA images
- `qa-report.md` with editability tradeoff, text-in-image check, and iteration notes

## Competitive Claim Rules

Use precise claims:

- "benchmark-oriented"
- "95+ gate ready"
- "story-first multi-lane PPT production system"
- "stronger QA contract than template-only slide generators"

Avoid unsupported claims:

- "best PPT skill"
- "surpasses every open-source skill"
- "guaranteed client-ready"
- "fully editable" when slides include flattened screenshots or generated images

If the user asks for "the best version", translate that into:

1. A named benchmark axis.
2. Required evidence artifacts.
3. Deterministic checks.
4. A retest prompt that would have failed the previous version.

## Release Gates

Before public release or a major internal claim:

```bash
python3 scripts/run_checks.py
```

The bundled check runner must include:

- passing deck-plan validation
- passing HTML sample validation
- benchmark HTML case validation
- HTML QA artifact check
- negative failure fixtures
- PPTX text extraction self-test
- PPTX native-object checker and negative image-only fixture
- reversible PPTX text-object edit probe
- bundled native PPTX case-study check
- repository hygiene check

Any skipped rendered QA must be named as a limitation, not hidden behind a quality score.
