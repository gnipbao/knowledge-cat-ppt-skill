# Contributing

Thanks for improving Knowledge Cat PPT.

## What Good Contributions Look Like

The project values production reliability over prompt cleverness. A good contribution usually adds one of:

- A clearer routing rule.
- A reusable layout or recipe.
- A deterministic validation check.
- A realistic retest prompt.
- A small example that exposes a real failure mode.
- Better documentation for installation, QA, or handoff.

## Development Loop

1. Change the smallest useful surface.
2. Run:

```bash
python3 scripts/run_checks.py
```

3. If you changed `SKILL.md`, confirm every referenced file exists.
4. If you changed an output lane, add or update a retest prompt.
5. If you changed a validator, include a sample that should pass and a failure case if practical.

## Style

- Keep `SKILL.md` concise. Move detailed instructions to `references/`.
- Prefer ASCII in repository files unless a file has a clear reason to include other characters.
- Do not add claims about external tools without a source or a test.
- Do not add vendor-specific lock-in unless the workflow explicitly requires it.
- Do not weaken the editability tradeoff language.

## Quality Bar

Before opening a pull request, check:

- The skill still starts with audience, outcome, and output lane.
- New workflows have pass/fail signals.
- Validators fail loudly on placeholder or incomplete output.
- Examples are realistic enough to catch regressions.
- Documentation tells users what the tool does not do.
