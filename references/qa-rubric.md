# QA Rubric

Use this file before final delivery, when reviewing an existing deck, or when repairing a production deck.

## Scoring

Score out of 100:

| Area | Points | Questions |
|---|---:|---|
| Audience and outcome fit | 15 | Is the deck built for a specific audience and decision or learning outcome? |
| Narrative spine and ghost deck | 20 | Do the action titles tell a complete argument? |
| Slide clarity | 15 | Does each slide have one main job and an understandable hierarchy? |
| Evidence quality | 15 | Are claims supported, sourced, or labeled as assumptions? |
| Visual system | 15 | Are layouts, type, color, imagery, and charts disciplined and readable? |
| Output-lane correctness | 10 | Does the file format match the user's actual need? |
| QA loop and handoff | 10 | Was rendered output inspected, fixed, and clearly handed off? |

## Priority Levels

### P0 - Must Fix Before Delivery

- File does not open.
- Output lane contradicts the user's requirement.
- Important text is cut off, unreadable, or overlapping.
- Missing required slide, data, source, or citation.
- Placeholder text remains.
- Fabricated or unsupported factual claim is presented as fact.
- Template or brand asset is used without permission.
- Speaker notes, appendix, or export requested by the user is absent.

### P1 - Should Fix Before Client-Ready Delivery

- Ghost deck is weak or repetitive.
- Slide has more than one main point.
- Layout repeats too often.
- Chart lacks direct takeaway or source.
- Low contrast or inconsistent spacing reduces readability.
- Image crop damages the subject or evidence.
- Ending does not create a conclusion, decision, or action.

### P2 - Improve If Time Allows

- Title could be sharper.
- Visual rhythm could be more varied.
- Notes could be more speaker-friendly.
- Appendix could make the main deck lighter.
- Export package could be easier to navigate.

## Content QA

Check:

- Slide order matches the story.
- Titles are action titles.
- Required content is present.
- No duplicated arguments.
- Numbers and labels are consistent.
- Sources are visible or tracked.
- Assumptions are labeled.
- Speaker notes match slide content.

For PPTX files, extract text when possible and search for placeholder patterns:

```bash
python3 scripts/extract_pptx_text.py output.pptx --fail-on-placeholders
```

Use equivalent extraction tools such as `markitdown` only when the bundled helper is unavailable.

## Visual QA

Inspect actual rendered slides, not only code.

Look for:

- Text overflow or clipping.
- Overlapping shapes, charts, icons, captions, or footers.
- Inconsistent margins.
- Weak contrast.
- Images that fail to load.
- Crops that hide key subject matter.
- Charts too small to read.
- Lines or dividers colliding with wrapped text.
- Crowded footnotes.
- Repeated layouts that make the deck feel mechanical.

For PPTX, render to images or PDF if possible. For HTML, open in browser and capture representative screenshots.

## Story QA

Run the ghost deck test:

```md
Read only the action titles.
Does the sequence explain the whole story?
Where does the story jump?
Which slide is redundant?
Which claim lacks proof?
What should the audience do next?
```

## Output-Lane QA

Native PPTX:

- Text is selectable where promised.
- Charts and shapes are editable where promised.
- Fonts are available or have sane fallbacks.
- Notes are present if requested.
- File opens in PowerPoint or Keynote target.

HTML deck:

- Keyboard navigation works.
- Assets load from relative paths.
- Slide canvas is stable at target viewport.
- Print/PDF/export route works if promised.
- Animations do not block readability.
- Static validation passes:

```bash
python3 scripts/validate_html_deck.py path/to/index.html
```

Image-first PPTX:

- User accepted editability tradeoff.
- Images are high enough resolution.
- Text inside images is correct and readable.
- Prompt log or source images are saved for iteration.

## Final Handoff Checklist

Before final response:

- State files created or reviewed.
- State output lane and tradeoff.
- State QA performed.
- State any known limitations.
- Give the most useful next iteration point.

Do not say "final" if a required render, file-open check, or user confirmation was skipped.

## Repository Release QA

When changing the skill repository itself, run:

```bash
python3 scripts/run_checks.py
```

Also check:

- No generated cache files are included.
- `README.md` matches actual commands.
- `SKILL.md` links every reference it expects.
- Sample deck plan passes validation.
- Sample HTML deck can be initialized and statically validated.
- Negative fixtures prove validators fail on known bad artifacts.
- PPTX text extraction self-test passes.
- Benchmark-quality claims follow `references/benchmark-quality-gates.md`.
