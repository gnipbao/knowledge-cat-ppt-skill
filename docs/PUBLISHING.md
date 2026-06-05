# Publishing Guide

Use this guide when publishing Knowledge Cat PPT as a public repository.

## Before First Push

1. Pick the GitHub owner and final URL.
2. Confirm `README.md` uses the final clone URL.
3. Run:

```bash
python3 scripts/run_checks.py
python3 scripts/check_repo.py
```

4. Confirm no generated outputs, private templates, source decks, secrets, or local-only files are included.
5. Create the repository and push:

```bash
git init
git add .
git commit -m "Initial open-source release"
git branch -M main
git remote add origin git@github.com:gnipbao/knowledge-cat-ppt-skill.git
git push -u origin main
```

## Suggested Repository Description

Story-first Agent Skill for creating, routing, and QA-checking PPT, HTML, and image-first decks, with a 44-style template library and HTML signature packs.

## Suggested Topics

```txt
agent-skill
codex-skill
claude-code-skill
ai-presentation
ppt
pptx
slides
html-deck
presentation-generator
deck-qa
template-library
html-slides
presentation-design
```

## GitHub README Checklist

- [ ] README states the current version.
- [ ] README explains the three output lanes.
- [ ] README links the 44-style template library.
- [ ] README explains Portfolio Minimal as the first HTML signature pack.
- [ ] README shows `python3 scripts/check_signature_pack.py portfolio-minimal`.
- [ ] README names the evidence artifacts: deck plan, sample HTML, browser screenshots, contact sheet, QA report, and deterministic checks.

## Release Checklist

- [ ] `VERSION` matches `CHANGELOG.md`.
- [ ] `README.md` install commands use the final repository URL.
- [ ] GitHub Actions passes on `main`.
- [ ] At least one sample deck plan validates.
- [ ] At least one sample HTML deck opens in a browser.
- [ ] Security and contribution docs are present.
- [ ] No private files or generated caches are committed.
