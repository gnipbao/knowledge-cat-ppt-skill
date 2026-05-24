# Open Source Product Readiness

Use this file when preparing Knowledge Cat PPT or a deck-output workflow for public release.

## Product Bar

An open-source Agent Skill is product-grade only when a new user can answer:

- What does this skill do?
- When should I use it?
- What should I not expect it to do?
- How do I install it?
- How do I run a smoke test?
- How do I know the output is good?
- How do I contribute without breaking the workflow?

## Required Repository Surfaces

For this project:

- `SKILL.md`: concise runtime instructions for the agent.
- `README.md`: human-facing install, purpose, usage, and validation.
- `agents/openai.yaml`: product UI metadata.
- `references/`: detailed workflows loaded only when needed.
- `assets/`: templates, schemas, and reusable output resources.
- `scripts/`: deterministic checks and setup helpers.
- `examples/`: retest prompts and sample artifacts.
- `scripts/install_skill.py`: local install helper for Codex or Claude Code.
- `CONTRIBUTING.md`: contribution rules.
- `SECURITY.md`: handling untrusted inputs and templates.
- `LICENSE`: explicit open-source license.
- `CHANGELOG.md`: release history.
- `.github/`: CI workflow plus issue and pull request templates.
- `docs/`: publishing and roadmap docs.

## Release Checklist

Before publishing:

```md
Skill metadata:
- [ ] name is lowercase hyphen-case.
- [ ] description includes concrete trigger phrases.
- [ ] frontmatter is valid.

Runtime:
- [ ] SKILL.md references every bundled reference it expects the agent to load.
- [ ] workflow names output lane, source-of-truth artifact, and QA signal.
- [ ] boundaries mention editability, HTML, image-first, evidence, and template permissions.

Scripts:
- [ ] all scripts run with standard Python where possible.
- [ ] scripts fail clearly on missing files or invalid input.
- [ ] validators have at least one bundled passing sample.
- [ ] install script has overwrite protection and ignores caches.

Examples:
- [ ] retest prompts cover vague request, source-to-deck, template, HTML, image-first, academic, review, and QA.
- [ ] sample plan passes validation.
- [ ] sample HTML can be generated and validates.

Docs:
- [ ] README includes install, usage, layout, validation, and license.
- [ ] CONTRIBUTING tells people how to avoid breaking the skill.
- [ ] SECURITY covers untrusted user inputs.

Packaging:
- [ ] no cache files, secrets, private decks, or local absolute paths.
- [ ] file tree is small enough to install as a skill.
- [ ] license is present.
- [ ] `python3 scripts/check_repo.py` passes.
```

## Versioning

Use semantic versioning:

- Patch: documentation fixes, small validator improvements, typo fixes.
- Minor: new recipe, new validator, new template, new lane capability.
- Major: changed workflow contract, renamed required fields, incompatible script behavior.

## Benchmark Positioning

Do not claim "best" without naming the axis. Better language:

- "Story-first router and QA system for presentation-producing agents."
- "Designed to compose with native PPTX, HTML, and image-first presentation workflows."
- "Not a replacement for format-specific renderers; it gives agents the control system around them."

## Product Failure Modes

- Strong README but weak runtime `SKILL.md`.
- Beautiful templates but no story or evidence discipline.
- Scripts that work only on the maintainer's machine.
- Claims of editable PPTX while producing flattened images.
- Validators that only check syntax, not deck-specific quality markers.
- Examples that are too easy and never catch workflow drift.
