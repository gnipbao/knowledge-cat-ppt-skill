# Style Template Library

Use this reference when the user provides a large PPT style list, asks for common PPT style websites, asks which style to choose, or wants Knowledge Cat PPT to exceed an HTML-deck benchmark such as Guizang.

## Source Boundary

This library is distilled from a user-provided prompt table containing 44 PPT style seeds plus common style websites. It is not a license to copy protected characters, brand assets, paid templates, or another skill's templates. Treat every row as reusable visual DNA: palette, typography, texture, composition, and deck-use fit.

When a style mentions a protected franchise, character, living artist, or brand-owned look, normalize it into generic traits before production.

## Surpass-Guizang Target

Guizang's HTML strength is not that it has more style words. Its strength is that it converts a narrow style set into executable templates, locked layouts, image slots, and validation.

Knowledge Cat should exceed it on three axes:

1. Breadth: route across native PPTX, HTML, and image-first PPTX instead of only HTML.
2. Depth: convert selected styles into reusable template packs with registered layouts and QA evidence.
3. Judgment: choose styles by audience, evidence, editability, and story job instead of visual taste alone.

Priority to beat Guizang in HTML:

| Priority | Build first | Why |
|---|---|---|
| P0 | `kc-24` Polished Minimal Portfolio | Closest to Guizang's Swiss/portfolio lane and strongest for professional HTML decks. |
| P0 | `kc-25` Minimal Data Story | Turns the Swiss look into decision and evidence decks, where Cat's story system can win. |
| P1 | `kc-28` Bold Editorial Magazine | Gives Cat a premium public-talk and thought-leadership lane beyond strict minimalism. |
| P1 | `kc-26` Dark SaaS Product | Strong for AI/product launch decks with screenshots and product surfaces. |
| P1 | `kc-11` Architectural Blueprint | Gives Cat a technical-diagram lane Guizang does not own by default. |
| P2 | `kc-09` Riso Decision Tree and `kc-17` Lo-fi Riso UI | Strong for education and social explainers, but lower priority for client-ready decks. |

Do not try to turn all 44 styles into full HTML templates at once. First create 3-5 signature packs with real screenshots, contact sheets, and validator coverage.

Current implementation status:

- `kc-24` Portfolio Minimal: implemented as `assets/html-signature-packs/portfolio-minimal` with a 14-layout registry, reusable template, 12-slide case study, QA artifacts, and `scripts/check_signature_pack.py`.
- `kc-25` Minimal Data Story: next P0 pack.
- `kc-28`, `kc-26`, `kc-11`: queued P1 packs.

## Style Selection Rule

Choose the style by deck job:

| Deck job | Prefer | Default lane |
|---|---|---|
| Client, investor, board, consulting | `kc-01`, `kc-24`, `kc-25` | native-pptx or html-deck |
| AI/SaaS/product launch | `kc-02`, `kc-08`, `kc-26`, `kc-36` | html-deck or hybrid image-first |
| Data, research, operating review | `kc-04`, `kc-25`, `kc-32` | native-pptx or html-deck |
| Technical process, SOP, architecture | `kc-11`, `kc-15`, `kc-30`, `kc-32` | native-pptx or html-deck |
| Public talk, keynote, founder story | `kc-27`, `kc-28`, `kc-34` | html-deck or image-first |
| Social carousel, Xiaohongshu, course notes | `kc-10`, `kc-17`, `kc-31`, `kc-35`, `kc-43` | image-first or html-deck |
| Kids, healing, warm education | `kc-12`, `kc-29`, `kc-38`, `kc-40`, `kc-44` | image-first or native-pptx |
| Brand/campaign/visual cover | `kc-18` to `kc-23`, `kc-34`, `kc-41` | image-first |

If the user says "the goal is to surpass Guizang", prefer `kc-24` or `kc-25` first unless their topic clearly needs another style.

## 44 Style Seeds

| ID | Style | Best for | Visual DNA | Default lane | Notes |
|---|---|---|---|---|---|
| kc-01 | Minimal Business | business reports, investor decks, company profiles | white canvas, charcoal text, navy accent, 60% whitespace, modern sans | native-pptx | Safe professional default. |
| kc-02 | Futuristic Tech | AI, tech companies, launches, data platforms | deep navy/black, blue-purple neon, grids, nodes, data glow | html-deck | Avoid generic purple gradients; use product evidence. |
| kc-03 | Vibrant Creative | marketing, campaigns, youth content | saturated colors, doodles, irregular shapes, playful type | image-first | Keep hierarchy readable. |
| kc-04 | Infographic Story | analysis, courseware, complex concepts | icons, flowcharts, timelines, comparison visuals | native-pptx | Preserve editability for labels and charts. |
| kc-05 | Cinematic Anthropomorphic 3D | culture, light team sharing | warm 3D animated characters in professional settings | image-first | Normalize protected franchise references into generic cinematic 3D traits. |
| kc-06 | Rounded Japanese Toy-Anime Explainer | education, imagination, tech for beginners | blue-white, rounded shapes, friendly toy-like forms | image-first | Normalize protected character references. |
| kc-07 | Neo-Constructivist Collage Archive | history, culture, ideas, education | grayscale cutouts, geometric color blocks, Swiss grid, retro modern | html-deck | Strong editorial HTML candidate. |
| kc-08 | Thermal Industrial HUD | hardware, surveillance, AI recognition | dark blue, thermal gradients, HUD frames, wireframes, product center | html-deck | Best with real product screenshots. |
| kc-09 | Riso Decision Tree | methods, process choices, course steps | paper grain, purple-orange, thick arrows, branching logic | image-first | Good for social explainers. |
| kc-10 | Retro-Pop Halftone Infographic | education, tutorials, concepts | duotone, misregistration, numbered modules, halftone | image-first | Keep text outside images if exact wording matters. |
| kc-11 | Architectural Blueprint | SOP, systems, engineering, spatial logic | line art, dimensions, isometric diagrams, thin strokes | html-deck | Strong Cat differentiator. |
| kc-12 | Retro Black-Line Vector | education, kids, brand warmth | cream background, black outlines, soft vintage palette | image-first | Good for approachable explainers. |
| kc-13 | Bauhaus Riso Geometry | design proposals, process diagrams | primitives, multiply overlays, diagonal motion, Bauhaus | image-first | Works well for visual method cards. |
| kc-14 | Constructivist Industrial Poster | strategy manifesto, organization mobilization | red-black-cream, heavy diagonals, industrial icons | image-first | Use carefully; can overpower business content. |
| kc-15 | Textbook Isometric Technical | technical lessons, product modules, data systems | isometric blocks, node trees, dashed flows, textbook paper | native-pptx | Hybrid option when diagrams must be editable. |
| kc-16 | Vintage Comic Panels | brand story, user journey, conflict narrative | panels, speech bubbles, bold black lines, newsprint | image-first | Avoid long body copy. |
| kc-17 | Lo-fi Riso UI Infographic | complex logic, notes, knowledge cards | hand-drawn UI, speech bubbles, offset print, brain icons | image-first | Strong for creator education. |
| kc-18 | Prism Fashion Magazine | fashion, people, event covers | pale white, prism gradient, large photos, dynamic Latin type | image-first | Requires high-quality imagery. |
| kc-19 | Black Premium Photography | luxury brand, launch, profile | black background, premium photography, dynamic type | image-first | Use for covers and section openers. |
| kc-20 | Blood-Orange Agency | creative agency, brand proposal | white, black type, blood-orange accent, stylish photos | html-deck | Good editorial-business bridge. |
| kc-21 | Red High-End Portrait | founder/person story, fashion, portfolio | white canvas, red accent, sans type, premium portraits | image-first | Portrait asset quality is decisive. |
| kc-22 | Navy Fashion Portrait | premium brand, founder culture, reports | navy, white type, brown-orange accent, italic emphasis | image-first | Best for narrative and identity decks. |
| kc-23 | Yellow Bold Serif Magazine | trends, events, creative covers | yellow background, black text, big serif, stickers | image-first | Great hook; risky for dense decks. |
| kc-24 | Polished Minimal Portfolio | portfolios, company profiles, consulting, architecture | strict grid, top-left nav, huge numbers, black/gray, negative space | html-deck | P0 HTML signature pack target. |
| kc-25 | Minimal Data Story | finance, operating reviews, monthly reports | Swiss grid, one insight, simple charts, restrained palette | native-pptx | P0 data/story pack target. |
| kc-26 | Dark SaaS Product | SaaS sites, feature launches, demos | dark UI, high contrast, screenshot cards, modules, subtle glow | html-deck | Pair with product screenshots. |
| kc-27 | TED Stage Keynote | talks, public lessons, point-of-view decks | one idea per slide, bold headline, emotional metaphor | html-deck | Story pacing matters more than visual density. |
| kc-28 | Bold Editorial Magazine | trend reports, people, brand opinion | oversized headlines, photo journalism, asymmetry, pull quotes | html-deck | P1 signature pack target. |
| kc-29 | Soft Pastel Education | courseware, parenting, beginner lessons | warm off-white, pastel blocks, rounded containers, gentle icons | native-pptx | Keep it calm, not childish by default. |
| kc-30 | Instruction Manual | SOP, product tutorials, training | black line drawings, steps, callouts, exploded diagrams | native-pptx | Excellent for repairable process decks. |
| kc-31 | Sketchnote | brainstorming, knowledge notes, summaries | paper texture, marker strokes, arrows, sticky notes | image-first | Use for informal learning, not board decks. |
| kc-32 | Engineering Blueprint Flow | business process, system architecture | blueprint grid, nodes, flow arrows, technical labels | html-deck | Strong for architecture explainers. |
| kc-33 | Startup Whiteboard Workshop | strategy sessions, retrospectives, co-creation | whiteboard, markers, sticky notes, rough charts | native-pptx | Good for workshop artifacts. |
| kc-34 | Cinematic Poster Story | launches, brand stories, event openings | dramatic lighting, hero subject, bold title, trailer pacing | image-first | Good for title/section slides. |
| kc-35 | Bento Grid Cards | features, knowledge modules, tools, social posts | modular cards, balanced grid, icons, modern product UI | html-deck | Watch card fatigue. |
| kc-36 | Glassmorphism Tech | app demos, future brand, launches | frosted glass, blur, layered depth, dark/gradient background | html-deck | Avoid generic shiny surfaces without content. |
| kc-37 | Chalkboard Teaching | lessons, review, exam prep | blackboard, colored chalk, arrows, hand-drawn icons | image-first | Avoid realistic photos. |
| kc-38 | Watercolor Gentle Illustration | public good, healing, travel, education | soft washes, pencil lines, paper texture, airy composition | image-first | Keep labels readable. |
| kc-39 | Isometric 3D Product Diagram | product structure, platform capability, architecture | polished isometric blocks, modules, soft shadow, clean labels | image-first | Hybrid with editable labels can work well. |
| kc-40 | Claymation | kids education, warm brands, light science | plasticine texture, rounded handmade forms, studio lighting | image-first | Good for social or friendly topics. |
| kc-41 | Vintage Travel Poster | city, routes, spaces, events | Art Deco, scenic forms, retro palette, poster composition | image-first | Use as campaign/key visual. |
| kc-42 | Esports Game UI | gamified courses, communities, youth reports | dark UI, metallic frames, task panels, energy bars, badges | html-deck | Keep text editable; do not flatten everything. |
| kc-43 | Xiaohongshu Cute Doodle | social posts, course notes, knowledge cards | cream base, macaron colors, stickers, bubbles, stars | image-first | Optimize for screenshot sharing. |
| kc-44 | Monoline Doodle | light tutorials, process notes, minimal brand | simple vector lines, warm neutral background, minimal accents | native-pptx | Good low-risk explainer style. |

## External Style Website Radar

Use these as inspiration and category language, not as proof that a specific template is licensed for reuse.

| Source | Use it for | URL or lookup |
|---|---|---|
| DrawPPT Style Templates | AI PPT style categories such as data story, SaaS, TED, editorial, pastel, sketchnote, cinematic, comic, claymation, neon | https://www.drawppt.com/styles |
| Beautiful.ai Image Styles | Image style vocabulary: minimalist, warm, claymation, isometric, watercolor, monoline/doodle | Search: `Beautiful.ai Image Styles` |
| Gamma Prompting Tips | Prompting frameworks for style, perspective, lighting, identity, context, and expression | Search: `Gamma prompting tips SPLICE` |
| Tome Help | AI presentation controls: theme, image style, charts, diagrams, text format, page count | Search: `Tome help AI presentation prompt` |
| Canva AI Presentation Maker | Brand consistency, presentation generation, styles, color/font matching | https://www.canva.com/presentations/ |
| Slidesgo | Common template categories: minimalist, simple, aesthetic, cute, professional, vintage | https://slidesgo.com |
| PixPs PPT prompt pages | Chinese AI PPT prompt patterns such as cyber hand-drawn, bento, game UI, minimal, board writing | Search: `PixPs PPT prompt` |

Before citing a website in user-facing research, verify the exact URL and current page content. The library can still use the site names as style-source signals when the user provided them.

## Style Prompt Profile Shortcut

When a user chooses one of these styles, create:

```md
Style Prompt Profile
Name: kc-XX - style name
Source: Knowledge Cat style-template-library.md, derived from user-provided style table
Use case fit:
Visual DNA:
Palette:
Typography:
Texture/material:
Composition:
Imagery:
Diagram/chart treatment:
Text-in-image policy:
Aspect ratios:
Must preserve:
Must avoid:
Safety normalization:
Output lane:
```

## HTML Signature Pack Contract

To turn a style seed into a Guizang-class HTML pack, create:

- one template file or starter variant
- at least 12 registered section skeletons
- a layout registry table
- one sample deck plan
- one sample HTML deck
- real or clearly labeled fixture screenshots
- contact sheet
- QA report
- static validator coverage for the style-specific contract
- retest prompt that would fail if the pack drifts

Minimum P0 pack sequence:

1. `kc-24` Polished Minimal Portfolio
2. `kc-25` Minimal Data Story
3. `kc-28` Bold Editorial Magazine
4. `kc-26` Dark SaaS Product
5. `kc-11` Architectural Blueprint
