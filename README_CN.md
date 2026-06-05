# 知识猫 PPT Skill

面向 AI Agent 的故事优先型 PPT 生产系统。

[English](README.md) | [简体中文](README_CN.md) | [Bilingual](README_BILINGUAL.md)

知识猫 PPT 是一个开源 Agent Skill，用来创建、审阅和修复高质量演示文稿。它兼容 Codex、Claude Code，以及其他能够读取 `SKILL.md` 的 Agent。它不是一句“帮我做得好看点”的提示词，而是一套完整生产流程：先明确受众变化，再选择输出模式，规划叙事和页面，生成交付物，最后做质量验证。

当前版本：`0.9.0`

## 亮点

- 以故事和受众转变为核心：先定义听众、目标、叙事主线和 action title。
- 支持三种生产模式：原生可编辑 PPTX、HTML 演示文稿、图像优先 PPTX。
- 支持 review-only 诊断模式，用来审阅已有 deck 的叙事、证据、视觉和可交付风险。
- 建立证据追踪：数字、引用、截图、假设、外部资料都要有来源或明确不确定性。
- 内置 HTML deck 模板：键盘导航、打印 CSS、明暗主题、无外部依赖。
- 内置 JSON deck plan 校验、HTML deck 校验和仓库健康检查。
- 内置 44 个 PPT 风格种子、常见 PPT 风格网站雷达，以及用于超越 Guizang 的 HTML signature pack 路线。
- 已落地 Portfolio Minimal HTML signature pack：14 个版式、12 页案例、QA artifact 和专用 pack 校验器。
- 面向开源发布：GitHub Actions、Issue 模板、PR 模板、发布清单、路线图和安全说明。
- 同时兼容 Codex local skills 与 Claude Code 风格的 skills。

## 三种生产模式

| 原生 PPTX | HTML Deck | 图像优先 PPTX |
|---|---|---|
| ![Native PPTX mode preview](docs/images/mode-native-pptx.png) | ![HTML deck mode preview](docs/images/mode-html-deck.png) | ![Image-first PPTX mode preview](docs/images/mode-image-first.png) |
| 适合真实团队协作、客户交付、图表、表格、讲稿备注和模板继承。 | 适合浏览器原生演示、快速视觉迭代、键盘导航、打印和可视化 QA。 | 适合社交轮播、营销活动、视觉 keynote 和风格探索，代价是可编辑性更低。 |

## 兼容性

| Agent 环境 | 状态 | 安装目录 |
|---|---|---|
| Codex | 支持 | `~/.codex/skills/knowledge-cat-ppt-skill` |
| Claude Code | 支持 | `~/.claude/skills/knowledge-cat-ppt-skill` |
| 其他 Skill-aware Agent | 理论支持，只要能读取 `SKILL.md` 和资源文件 | 取决于具体 Agent |

Skill 本体由 Markdown、Python、JSON 和 HTML 组成。内置 Python 脚本只使用标准库；真正生成 PPTX、渲染 HTML 或生成图像时，会根据用户环境组合可用的专业工具或其他 skill。

## 它能做什么

知识猫 PPT 可以帮助 Agent：

- 把粗略想法、笔记、文档、访谈稿、URL、PDF、调研资料转成 deck brief。
- 生成 slide plan：包含 action title、页面角色、证据、视觉建议、讲稿备注和来源。
- 在生产前选择正确输出模式，避免“用户要可编辑 PPT，结果交付一堆图片”的问题。
- 生成或指导生成 HTML deck、可编辑 PowerPoint、图像优先视觉 deck。
- 审阅已有 PPT，检查叙事、证据、视觉系统、可编辑性和技术风险。
- 在交付前执行校验，不把“代码看起来没报错”误当成“deck 已经可交付”。

## 安装

仓库地址：

```txt
https://github.com/gnipbao/knowledge-cat-ppt-skill.git
```

### Codex

```bash
git clone https://github.com/gnipbao/knowledge-cat-ppt-skill.git ~/.codex/skills/knowledge-cat-ppt-skill
```

然后重启 Codex，或刷新本地 skills。

如果已经 clone 到本地仓库：

```bash
python3 scripts/install_skill.py --agent codex --force
```

### Claude Code

```bash
git clone https://github.com/gnipbao/knowledge-cat-ppt-skill.git ~/.claude/skills/knowledge-cat-ppt-skill
```

然后重启 Claude Code，或刷新本地 skills。

如果已经 clone 到本地仓库：

```bash
python3 scripts/install_skill.py --agent claude --force
```

### 手动安装

把整个目录复制到对应 Agent 的 skills 目录：

```bash
cp -R knowledge-cat-ppt-skill ~/.codex/skills/
```

或：

```bash
cp -R knowledge-cat-ppt-skill ~/.claude/skills/
```

## 快速使用

生成客户可交付 PPT：

```md
Use $knowledge-cat-ppt-skill to turn my notes into an 8-slide client-ready deck. I need editable PPTX unless you think another output lane is better.
```

审阅已有 deck：

```md
Use $knowledge-cat-ppt-skill to review this deck. Focus on story, evidence, visual clarity, and whether it is actually ready to send.
```

生成 HTML 演示：

```md
Use $knowledge-cat-ppt-skill to build a browser-based HTML deck from this outline. Make it keyboard navigable and run the bundled HTML validator.
```

生成图像优先 deck：

```md
Use $knowledge-cat-ppt-skill to create a visual-first social carousel deck. Keep the text editable unless the image-first tradeoff is necessary.
```

使用 44 个风格种子库：

```md
Use $knowledge-cat-ppt-skill. 从模板库里为我的主题选择最合适的风格，说明输出模式取舍，然后先生成 deck brief 和 slide plan。
```

使用 Portfolio Minimal signature pack：

```md
Use $knowledge-cat-ppt-skill. 使用 kc-24 Portfolio Minimal signature pack 生成 HTML deck，使用 pack layout registry，包含本地图片槽位，产出 screenshots/contact sheet，并运行 signature-pack checks。
```

## 输出模式

| 模式 | 适用场景 | 主要取舍 |
|---|---|---|
| `native-pptx` | PowerPoint 可编辑性、团队协作、图表、表格、备注、客户交付 | 需要可生成 PPTX 的渲染器或配套 skill |
| `html-deck` | Web 演示、快速视觉迭代、浏览器预览、单文件夹分享 | 不是原生可编辑 PowerPoint 文件 |
| `image-first-pptx` | 社交轮播、营销活动、视觉 keynote、AI 生成页面 | 可编辑性较弱 |
| `review-only` | 已有 deck 诊断、修复计划、叙事和证据审阅 | 不直接生成最终 deck，除非用户继续要求修复 |

## HTML Deck 模板

创建一个示例 HTML deck：

```bash
python3 scripts/init_deck_project.py /tmp/kc-demo-deck --title "Knowledge Cat Demo"
python3 scripts/validate_html_deck.py /tmp/kc-demo-deck/index.html
```

打开：

```txt
/tmp/kc-demo-deck/index.html
```

模板包含 16:9 桌面画布、移动端堆叠布局、键盘导航、打印 CSS、明暗主题、action title 页面结构和无外部依赖实现。

## 风格模板库

知识猫 PPT 内置 44 个风格种子，文件是：

```txt
references/style-template-library.md
```

它不是简单堆 prompt，而是把风格变成路由系统：适用场景、默认输出模式、受保护风格的泛化规则，以及优先落地的 signature pack 路线。

可直接复制的测试提示词在：

```txt
docs/TEMPLATE_LIBRARY_PROMPTS.md
```

## Portfolio Minimal Signature Pack

第一个已落地的 HTML signature pack 是 `kc-24` Portfolio Minimal：

```txt
assets/html-signature-packs/portfolio-minimal/
+-- README.md
+-- layout-registry.json
+-- template.html
```

它包含 14 个 `custom-pm-*` 版式和 12 页案例：

```txt
examples/case-studies/portfolio-minimal/
```

运行专用校验：

```bash
python3 scripts/check_signature_pack.py portfolio-minimal
```

该案例已经包含浏览器捕获的 PNG 截图和 contact sheet，因此 HTML 质量声明不是只基于代码检查。

## Deck Plan 校验

校验 JSON deck plan：

```bash
python3 scripts/validate_deck_plan.py examples/sample-deck-plan.json
```

结构定义在：

```txt
assets/deck-plan.schema.json
```

## 完整验证

运行全部检查：

```bash
python3 scripts/run_checks.py
```

运行仓库健康检查：

```bash
python3 scripts/check_repo.py
```

检查范围包括 sample deck plan、HTML 示例、HTML 结构、必要仓库文件、版本与 changelog 一致性、缓存和生成文件卫生。

## 工作方式

主运行文件是 `SKILL.md`。它让 Agent 按以下顺序工作：

1. 判断请求类型。
2. 建立 deck brief。
3. 综合叙事。
4. 创建 slide plan。
5. 选择生产模式。
6. 建立视觉系统。
7. 生产 deck。
8. QA、修复和交付。

细节说明放在 `references/` 中，Agent 只在需要时加载对应参考文件。

## 设计哲学

知识猫 PPT 是一个路由器和质量系统，而不是一个单体渲染器。

- 协作和 PowerPoint 编辑重要时，用原生可编辑 PPTX。
- Web 演示、动画、预览或浏览器 QA 重要时，用 HTML。
- 视觉冲击比可编辑性更重要时，用图像优先 PPTX。
- 已有 deck 的根本问题在叙事或证据时，用 review-only。

## 贡献

请先阅读 `CONTRIBUTING.md`。

好的贡献通常会增加以下之一：

- 更清晰的模式选择规则
- 可复用生产 recipe
- 确定性校验脚本
- 真实 retest prompt
- 能暴露质量问题的 sample artifact
- 更完整的发布或 QA 文档

提交 PR 前请运行：

```bash
python3 scripts/run_checks.py
```

## 安全

用户上传的 PPT、HTML、PDF、文档、模板和压缩包都应视为不可信输入。不要执行用户压缩包中的脚本。详见 `SECURITY.md`。

## 路线图

详见 `docs/ROADMAP.md`。

近期方向：

- editable PPTX case study
- HTML keynote case study
- image-first carousel case study
- 更强的视觉 QA 自动化

## 许可证

MIT。详见 `LICENSE`。
