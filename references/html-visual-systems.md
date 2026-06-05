# HTML Visual Systems

Use this file when building a production `html-deck`, before writing final slide markup. It defines reusable visual systems that are strong enough to survive a contact-sheet review.

## Root Rule

A visual system is not a mood board. It is a production contract for typography, palette, density, layout rhythm, image treatment, and forbidden moves.

Choose one system, then vary only by slide role.

When the user provides a large style table or asks to surpass Guizang, read `references/style-template-library.md` before finalizing the visual system. Treat the 44 style seeds as a routing library, not as a reason to mix multiple looks in one deck.

## System 1: Architectural Minimal

Best for:

- strategy memos
- portfolio-style thought leadership
- operating-model decks
- executive narratives that need restraint and edge

Visual DNA:

- off-white or light-gray canvas
- black type, black rules, hairline grids
- small top-left navigation
- large negative space
- asymmetric split pages
- occasional black slide as a visual reset

Tokens:

```txt
bg: #f2f2f0 / #ffffff
ink: #050505
muted: #6d6d68
line: #cfcfca
dark: #050505
dark-ink: #f7f7f3
accent: #050505
font: Inter or system sans
mono: SFMono-Regular or ui-monospace
radius: 0-4px
```

Layout rhythm:

- open with a sparse hero or statement
- follow with a split diagnosis slide
- use one dark system-map or network slide by slide 3-5
- alternate data/list pages with visual reset pages
- end with a restrained decision or operating-system recap

Image treatment:

- use monochrome or low-saturation screenshots
- crop images to strict slots
- no decorative stock atmosphere
- diagrams should use thin lines and real HTML labels

Must avoid:

- rounded card stacks
- gradient backgrounds
- decorative blobs
- icon-heavy explanation
- centered paragraphs longer than one line

## System 2: Editorial Proof

Best for:

- essay-to-deck transformations
- keynote narratives
- public talks
- creator or founder lessons

Visual DNA:

- magazine-like rhythm
- large pull statements
- narrow evidence columns
- strong typographic contrast
- one visual proof object per evidence slide

Tokens:

```txt
bg: #fbfaf7
ink: #151515
muted: #67645e
line: #ddd6ca
accent: #d44b2a
panel: #ffffff
font: Inter or system sans
serif optional for short quote display only
radius: 4-8px
```

Layout rhythm:

- hook with a sharp claim
- alternate quote/implication pages with proof pages
- use image-annotation for concrete evidence
- end with a concise memory structure

Image treatment:

- images carry context or evidence
- captions are short and quiet
- screenshots keep exact content when used as proof

Must avoid:

- generic article summary pages
- decorative quote pages with no implication
- long body copy under large display text

## System 3: Data Command

Best for:

- analytics and market maps
- investor or operating reviews
- decision decks with measurable evidence
- product or GTM performance narratives

Visual DNA:

- white or near-black command surfaces
- one chart or metric exhibit per slide
- direct annotation on the exhibit
- compact labels, clear hierarchy
- strong source footers

Tokens:

```txt
bg: #ffffff
ink: #101010
muted: #5a5f63
line: #d8dde1
accent: #0057ff
warning: #d64545
positive: #16875a
dark: #0b0f14
font: Inter or system sans
mono: SFMono-Regular or ui-monospace
radius: 4px
```

Layout rhythm:

- start with the decision or implication
- place one large exhibit at the center
- annotate the point directly
- use comparison or dashboard layouts only when they answer a decision question
- end with a recommendation or operating cadence

Image treatment:

- charts, tables, screenshots, and diagrams are evidence
- never redesign evidence screenshots without saying so
- source labels must remain visible or tracked in notes

Must avoid:

- dashboard wallpaper
- unlabeled axes
- legends that make the reader hunt for the point
- unsupported benchmark numbers

## Selection Checklist

Before final HTML production, write this in the deck brief or plan:

```md
HTML visual system:
Why it fits:
Theme rhythm:
Registered layouts:
Image slot policy:
Screenshot/contact-sheet QA plan:
Forbidden moves:
```

## Contact-Sheet Gate

A production HTML deck should pass this thumbnail test:

- each slide has a distinct job
- the visual system is recognizable across slides
- at least five registered layouts appear in decks of seven or more slides
- dark slides are intentional resets, not decoration
- image slots are visible and bound to a target ratio
- no slide looks like an unstyled article page

## Signature Pack Roadmap

To compete with style-locked HTML skills, the HTML lane should grow from three visual systems into named template packs. Build these first:

| Pack | Seed | Registered layout target |
|---|---|---|
| Portfolio Minimal | `kc-24` Polished Minimal Portfolio | 12-18 strict-grid sections with top navigation, huge numbers, image/list splits, timelines, logo grids, and dark network resets. |
| Minimal Data Story | `kc-25` Minimal Data Story | 12-16 evidence sections with one-insight charts, source footers, annotation layers, metric comparisons, and decision endings. |
| Editorial Magazine | `kc-28` Bold Editorial Magazine | 12-16 keynote/editorial sections with oversized headlines, pull quotes, proof objects, image essays, and closing memory structures. |
| Dark SaaS Product | `kc-26` Dark SaaS Product | 12-16 product sections with screenshot slots, feature cards, workflow maps, dashboards, and demo-to-value transitions. |
| Technical Blueprint | `kc-11` Architectural Blueprint | 12-16 system sections with line diagrams, dimensions, process flows, exploded views, and implementation notes. |

Each pack needs a sample deck, screenshot/contact sheet, QA report, and validator coverage before it can be called benchmark-grade.
