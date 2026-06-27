# Knowledge Cat PPT Skill / 知识猫 PPT Skill

Story-first presentation production for AI agents.  
面向 AI Agent 的故事优先型 PPT 生产系统。

[English](README.md) | [简体中文](README_CN.md) | [Bilingual](README_BILINGUAL.md)

Knowledge Cat PPT is an open-source Agent Skill for creating, reviewing, and repairing presentation decks. It is designed for Codex, Claude Code, and other skill-aware coding agents.  
知识猫 PPT 是一个开源 Agent Skill，用来创建、审阅和修复高质量演示文稿，兼容 Codex、Claude Code 和其他能读取 `SKILL.md` 的 Agent。

Current version / 当前版本：`0.10.0`

## Highlights / 亮点

| English | 中文 |
|---|---|
| Story-first deck planning with audience, outcome, narrative spine, and action titles. | 以故事和受众转变为核心，先定义听众、目标、叙事主线和 action title。 |
| Output-lane routing for native editable PPTX, HTML decks, image-first PPTX, and review-only workflows. | 支持原生可编辑 PPTX、HTML 演示、图像优先 PPTX 和 review-only 诊断模式。 |
| Evidence tracking for claims, quotes, data, assumptions, screenshots, and source materials. | 对数字、引用、假设、截图和外部资料进行证据追踪。 |
| HTML deck starter with keyboard navigation, print CSS, light/dark themes, and no external dependencies. | 内置 HTML deck 模板，支持键盘导航、打印 CSS、明暗主题且无外部依赖。 |
| Curated 44-style template library with PPT style-site radar and Guizang-surpass signature-pack targets. | 内置 44 个 PPT 风格种子、常见风格网站雷达，以及用于超越 Guizang 的 signature pack 路线。 |
| Portfolio Minimal HTML signature pack with 14 layouts, a 12-slide case study, QA artifacts, and a dedicated checker. | 已落地 Portfolio Minimal HTML signature pack：14 个版式、12 页案例、QA artifact 和专用校验器。 |
| Native deck-plan-to-PPTX builder with editable text, shapes, charts, tables, and notes. | 新增 deck plan → 原生 PPTX 构建器，可生成可编辑文字、形状、图表、表格和备注。 |
| Real native PPTX case with re-imported renders, contact sheet, object inspection, editability report, and reversible edit probe. | 新增真实原生 PPTX 案例，包含重导入渲染、联系表、对象检查、编辑性报告和可逆编辑探针。 |
| JSON deck-plan validator, HTML validator, repository checks, GitHub Actions, and open-source release docs. | 内置 deck plan 校验、HTML 校验、仓库检查、GitHub Actions 和开源发布文档。 |

## Three Production Modes / 三种生产模式

| Native PPTX / 原生 PPTX | HTML Deck / HTML 演示 | Image-First PPTX / 图像优先 PPTX |
|---|---|---|
| ![Native PPTX mode preview](docs/images/mode-native-pptx.png) | ![HTML deck mode preview](docs/images/mode-html-deck.png) | ![Image-first PPTX mode preview](docs/images/mode-image-first.png) |
| Editable PowerPoint work for real teams, client handoffs, charts, tables, and speaker notes. | Browser-native decks with keyboard navigation, print CSS, fast iteration, and visual QA. | High-impact visual decks for social carousels, campaigns, and keynote-style moments. |
| 适合真实团队协作、客户交付、图表、表格和讲稿备注。 | 适合浏览器原生演示、快速视觉迭代、打印和可视化 QA。 | 适合社交轮播、营销活动和视觉 keynote，代价是可编辑性更低。 |

## Compatibility / 兼容性

| Agent environment | Status | Install path |
|---|---|---|
| Codex | Supported / 支持 | `~/.codex/skills/knowledge-cat-ppt-skill` |
| Claude Code | Supported / 支持 | `~/.claude/skills/knowledge-cat-ppt-skill` |
| Other skill-aware agents | Should work if they read `SKILL.md` and bundled resources / 理论支持 | Agent-specific / 取决于具体 Agent |

The skill itself is plain Markdown, Python, JavaScript, JSON, and HTML. Validators use only the Python standard library; the optional native builder needs Node.js plus a prepared `@oai/artifact-tool` workspace.

Skill 本体由 Markdown、Python、JavaScript、JSON 和 HTML 组成；校验器只使用 Python 标准库，可选原生构建器需要 Node.js 和准备好的 `@oai/artifact-tool` workspace。

## Install / 安装

Repository URL / 仓库地址：

```txt
https://github.com/gnipbao/knowledge-cat-ppt-skill.git
```

Codex:

```bash
git clone https://github.com/gnipbao/knowledge-cat-ppt-skill.git ~/.codex/skills/knowledge-cat-ppt-skill
```

Claude Code:

```bash
git clone https://github.com/gnipbao/knowledge-cat-ppt-skill.git ~/.claude/skills/knowledge-cat-ppt-skill
```

From a cloned repository / 如果已经 clone 到本地仓库：

```bash
python3 scripts/install_skill.py --agent codex --force
python3 scripts/install_skill.py --agent claude --force
```

Restart or refresh your agent after installation.  
安装后请重启或刷新 Agent 的 skills。

## Quick Start / 快速使用

Client-ready editable deck / 生成客户可交付可编辑 PPT：

```md
Use $knowledge-cat-ppt-skill to turn my notes into an 8-slide client-ready deck. I need editable PPTX unless you think another output lane is better.
```

Deck review / 审阅已有 deck：

```md
Use $knowledge-cat-ppt-skill to review this deck. Focus on story, evidence, visual clarity, and whether it is actually ready to send.
```

HTML deck / 生成 HTML 演示：

```md
Use $knowledge-cat-ppt-skill to build a browser-based HTML deck from this outline. Make it keyboard navigable and run the bundled HTML validator.
```

Image-first deck / 生成图像优先 deck：

```md
Use $knowledge-cat-ppt-skill to create a visual-first social carousel deck. Keep the text editable unless the image-first tradeoff is necessary.
```

Template library / 模板库：

```md
Use $knowledge-cat-ppt-skill. Choose the best style from the template library for my topic, explain the lane tradeoff, then create a deck brief and slide plan.
```

Portfolio Minimal signature pack / Portfolio Minimal 模板包：

```md
Use $knowledge-cat-ppt-skill. Build a browser-based HTML deck using the kc-24 Portfolio Minimal signature pack, produce screenshots/contact sheet, and run signature-pack checks.
```

## Output Lanes / 输出模式

| Lane / 模式 | Use when / 适用场景 | Main tradeoff / 主要取舍 |
|---|---|---|
| `native-pptx` | PowerPoint editability, team collaboration, charts, tables, notes, client decks / 需要 PowerPoint 可编辑性、团队协作、图表、表格、备注和客户交付 | Bundled builder needs a prepared artifact-tool workspace; imported-deck repairs still need a verified native editor / 内置构建器需要准备好的 artifact-tool workspace，旧 deck 修复仍需经验证的原生编辑器 |
| `html-deck` | Web-native presentation, rapid visual iteration, browser preview, single-folder sharing / Web 演示、快速视觉迭代、浏览器预览、单文件夹分享 | Not a true editable PowerPoint file / 不是原生可编辑 PowerPoint 文件 |
| `image-first-pptx` | Social carousel, campaign deck, visual keynote, AI-generated slide surfaces / 社交轮播、营销活动、视觉 keynote、AI 生成页面 | Lower editability / 可编辑性较弱 |
| `review-only` | Existing deck critique, repair planning, story and evidence diagnosis / 已有 deck 诊断、修复计划、叙事和证据审阅 | Does not create a final deck until repair is requested / 不直接生成最终 deck |

Native case / 原生案例：

```bash
python3 scripts/check_native_pptx_case.py
```

The case contains a real editable PPTX, six re-imported renders, a contact sheet, object inspection, an editability report, and a reversible text-object probe.

案例包含真实可编辑 PPTX、6 张重导入渲染图、联系表、对象检查、编辑性报告和可逆文字对象探针。

## Validation / 验证

Create and validate a sample HTML deck / 创建并校验示例 HTML deck：

```bash
python3 scripts/init_deck_project.py /tmp/kc-demo-deck --title "Knowledge Cat Demo"
python3 scripts/validate_html_deck.py /tmp/kc-demo-deck/index.html
```

Validate a deck plan / 校验 deck plan：

```bash
python3 scripts/validate_deck_plan.py examples/sample-deck-plan.json
```

Run all bundled checks / 运行全部检查：

```bash
python3 scripts/run_checks.py
```

## Template Library / 模板库

The 44-style template library lives in `references/style-template-library.md`; copy-ready prompts live in `docs/TEMPLATE_LIBRARY_PROMPTS.md`.  
44 个风格种子库位于 `references/style-template-library.md`；可直接复制的提示词位于 `docs/TEMPLATE_LIBRARY_PROMPTS.md`。

The first implemented HTML signature pack is `kc-24` Portfolio Minimal, with a 14-layout registry, 12-slide case study, browser screenshots, contact sheet, QA report, and `scripts/check_signature_pack.py`.  
第一个已落地的 HTML signature pack 是 `kc-24` Portfolio Minimal，包含 14 个版式、12 页案例、浏览器截图、contact sheet、QA 报告和 `scripts/check_signature_pack.py`。

## How The Skill Works / 工作方式

The main runtime file is `SKILL.md`. It keeps the agent workflow concise: triage the request, build a brief, synthesize the story, create a slide plan, choose a production lane, build the design system, produce the deck, then QA and iterate.  
主运行文件是 `SKILL.md`。它让 Agent 按顺序完成：判断请求、建立 brief、综合叙事、创建 slide plan、选择生产模式、建立视觉系统、生产 deck、QA 和迭代。

Detailed instructions live in `references/` and are loaded only when needed.  
细节说明放在 `references/` 中，只在需要时加载。

## Design Philosophy / 设计哲学

Knowledge Cat PPT is a router and quality system, not a monolithic renderer.  
知识猫 PPT 是一个路由器和质量系统，而不是单体渲染器。

- Use native editable PPTX when collaboration and PowerPoint editing matter. / 协作和 PowerPoint 编辑重要时，用原生可编辑 PPTX。
- Use HTML when web-native presentation, animation, preview, or browser QA matters. / Web 演示、动画、预览或浏览器 QA 重要时，用 HTML。
- Use image-first PPTX when visual spectacle matters more than editability. / 视觉冲击比可编辑性更重要时，用图像优先 PPTX。
- Use review-only mode when the deck's story or evidence may be the real failure. / 根本问题在叙事或证据时，用 review-only。

## Contributing / 贡献

Read `CONTRIBUTING.md` first. Good contributions usually add clearer routing rules, reusable recipes, deterministic checks, realistic retest prompts, sample artifacts, or better QA and release documentation.  
请先阅读 `CONTRIBUTING.md`。好的贡献通常会增加更清晰的模式选择规则、可复用 recipe、确定性校验、真实 retest prompt、sample artifact，或更完整的 QA 与发布文档。

Before opening a pull request / 提交 PR 前：

```bash
python3 scripts/run_checks.py
```

## Security / 安全

Treat user-provided decks, HTML, PDFs, documents, templates, and archives as untrusted input. Do not execute scripts from user-provided archives. See `SECURITY.md`.  
用户上传的 PPT、HTML、PDF、文档、模板和压缩包都应视为不可信输入。不要执行用户压缩包中的脚本。详见 `SECURITY.md`。

## License / 许可证

MIT. See `LICENSE`.  
MIT。详见 `LICENSE`。
