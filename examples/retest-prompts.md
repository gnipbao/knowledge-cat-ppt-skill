# Retest Prompts

Use these prompts to test whether Knowledge Cat PPT behaves like a production skill rather than a generic slide prompt.

## 1. Vague Business Request

```md
Use $knowledge-cat-ppt-skill. I need a deck for my AI product. Make it impressive.
```

Expected behavior:

- Ask for audience, outcome, source, and output lane if needed.
- Do not start with visual style.
- Offer a safe default path if the user wants to proceed.

## 2. Source-To-Deck

```md
Use $knowledge-cat-ppt-skill. Turn this article into an 8-slide executive deck for a founder audience. Editable PPTX preferred.
```

Expected behavior:

- Build a deck brief.
- Create a ghost deck and slide plan.
- Select native PPTX.
- Track source claims.

## 3. Template Request

```md
Use $knowledge-cat-ppt-skill. I have a company-template.pptx. Make a 10-page product strategy deck in the same style.
```

Expected behavior:

- Enter template mode.
- Create a template profile before building.
- Map slides to template layouts.
- Preserve editability if possible.

## 4. HTML Visual Talk

```md
Use $knowledge-cat-ppt-skill. Build a browser-based keynote with keyboard navigation and a bold visual rhythm.
```

Expected behavior:

- Select HTML deck.
- Use browser QA.
- Avoid pretending the result is a native PPTX.

## 5. Image-First Social Carousel

```md
Use $knowledge-cat-ppt-skill. Create a Xiaohongshu-style carousel from my framework. Visual impact matters more than editability.
```

Expected behavior:

- Select image-first or social carousel path.
- Confirm aspect ratio and text safety.
- Save prompt or plan artifacts.

## 6. Academic Talk

```md
Use $knowledge-cat-ppt-skill. Make slides for my conference paper. I need citations and a conclusions slide.
```

Expected behavior:

- Use academic narrative spine.
- Enforce action titles, one exhibit per results slide, citations, and conclusion.
- Avoid decorative design.

## 7. Deck Review

```md
Use $knowledge-cat-ppt-skill. Review this deck and tell me why it feels weak.
```

Expected behavior:

- Review first.
- Lead with prioritized issues.
- Separate story, evidence, visual, and technical problems.

## 8. QA Discipline

```md
Use $knowledge-cat-ppt-skill. The slides look done. Can we ship?
```

Expected behavior:

- Refuse to declare final without rendered visual QA.
- Run or request the necessary checks.
- Report remaining risks.

## 9. HTML Production Lock

```md
Use $knowledge-cat-ppt-skill. Build a 7-slide HTML deck from this product strategy memo. Include one local product screenshot slot, use at least five layout types, and run the HTML validator before delivery.
```

Expected behavior:

- Select `html-deck` only if browser delivery fits the user need.
- Read `references/html-production-lock.md` before `references/html-deck-recipes.md`.
- Declare `data-layout`, `data-title`, `data-role`, and `data-theme` on every slide.
- Give local images `data-image-slot`, target ratio metadata, and meaningful alt text.
- Report validator output and any visual QA that was or was not performed.

## 10. Uploaded Style Prompt Image-First

```md
Use $knowledge-cat-ppt-skill. I uploaded a table of PPT theme/style prompts. Pick the best style for a 9-slide AI product launch deck and prioritize Image2/GPT-Image style generation unless you think editability should override it.
```

Expected behavior:

- Detect the uploaded prompt table as a style prompt source.
- Read `references/style-prompt-intake.md` before `references/image-first-recipes.md`.
- Prefer `image-first-pptx` or hybrid image-first PPTX, then state the editability tradeoff.
- Extract a Style Prompt Profile instead of blindly pasting the raw prompt.
- Produce a slide-level prompt plan with visual intent, style variation, text-in-image policy, aspect ratio, and prompt risk.
- Preserve exact product claims, metrics, screenshots, and citations outside images when they must remain editable or verifiable.
