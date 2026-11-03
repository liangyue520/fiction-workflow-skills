# Fiction Workflow Skills · 中文小说协作技能包

**从人物为什么行动，到这一章究竟推进了什么，让 AI 写作与审稿有据可查。**

19 个可独立使用的技能，覆盖参考研读、现实研究、人物与场景设计、正文修订、读者体验和版本交付。适合已有故事、正在写长篇，或需要认真检查一份 AI 稿件的作者。

**版本：v0.1.0 首个维护版本** · 中文 · 按需组合 · 当前以本地技能目录方式使用

**项目整理、改编与维护：[梁养浩](AUTHORS.md)** · [GitHub 公开仓库](https://github.com/liangyue520/fiction-workflow-skills)

[快速开始](#快速开始) · [使用示例](#使用示例) · [全部技能](#全部技能) · [协作规则](#协作规则) · [验证记录](VALIDATION.md) · [维护与贡献](#维护与贡献)

## 能帮你解决什么

| 写作中的问题 | 从哪里入手 | 你会得到什么 |
|---|---|---|
| 主角为什么非要冒这个险？ | 人物动机设计 | 触发、所知、选择、代价，以及更自然的替代选择 |
| 场景很吓人，却不影响人物做事 | 空间设计 + 恐怖设计 | 可走的路线、视线限制、行动障碍和应对代价 |
| 连续几章都有新线索，读起来却没进展 | 流水账检测 | 跨章功能对照，定位重复、有效变化与可合并部分 |
| 审稿一直高分，具体问题还在 | 逻辑审查 + 读者审查 | 绑定正文版本的证据、问题等级和修改方向 |
| 文件越来越多，不知道该读哪一版 | 交付核对 | 当前候选稿、真实审查状态和明确的阅读入口 |

这套方法来自小说协作中的实际问题与纠错，尤其关注第一人称、悬疑和探险场景。人物、节奏、版本等通用方法可按题材选用；恐怖和第一人称要求只在相应场景适用。九类历史工作如何转成技能，见 [经验与技能对照](docs/work-experience.md)。

## 快速开始

### 1. 先选一个技能

已有正文时，可以先用 `novel-boring-detect` 检查连续章节。你只需准备待检稿，以及理解重复问题所需的相关前文，不必一开始就搭建完整工作流。

下载并解压技能包，或取得本仓库的本地副本。每个 `skills/<技能名>/` 都是独立技能文件夹；复制时连同其中的 `references/`、`agents/` 等已有内容一起保留。

### 2. 放到宿主能够发现的位置

Codex 的当前官方文档支持项目内 `.agents/skills/` 和个人目录 `~/.agents/skills/`。以项目内安装为例，将 `skills/novel-boring-detect/` 复制到你的小说项目，形成以下结构。目录与发现方式详见 [Codex 技能文档](https://developers.openai.com/codex/skills)。

```text
你的小说项目/
├── .agents/
│   └── skills/
│       └── novel-boring-detect/
│           └── SKILL.md
└── 正文/
    ├── 第01章_v1.md
    └── 第02章_v2.md
```

若目标已有同名技能，先备份，再更新所选文件夹，避免新旧副本同时被发现。使用已有自定义技能路径的环境，沿用宿主实际配置。其他宿主按其本地技能导入方式操作；本包尚未完成跨宿主运行验证。

安装后在技能列表中确认能够找到它；若未出现，按宿主要求重新加载或重启。复制成功不等于运行中的旧聊天已读到新规则。使用这些 Markdown 技能本身无需安装 Python 或 Node.js；验证脚本的依赖另见下文。

### 3. 发出第一次请求

```text
使用 novel-boring-detect。
请读取正文/第01章_v1.md 和正文/第02章_v2.md，
比较两章的目标、行动、所得、人物关系和局部答案。
指出哪些段落有新作用，哪些只是换说法或推迟同一个问题，
并给出最小修改方向。先检查，不改正文。
如果文件读不到，请说明缺口。
```

先把示例路径换成自己的真实文件，或提供清楚标记版本的正文。报告应交代实际读了哪一版、问题出现在哪里、为什么影响阅读，以及哪些内容值得保留。无需为了使用一个技能而运行全部 19 项。

## 使用示例

以下都是可改写后直接发送的请求。先安装所提及的技能，并提供对应材料。

### 人物的选择缺乏说服力

```text
使用 novel-character-design。
主角原本只是替朋友送回一件借物，却发现朋友隐瞒了一段经历。
请根据我提供的前文，设计他继续追问的动机。
比较追问、离开、求助三种选择，写清触发、误判和代价。
新设定只作为候选，不替我决定朋友的身份或结局。
```

### 同一地点再次出现，是否算重复

```text
使用 novel-boring-detect，比较我提供的两次重访场景。
这次人物知道了什么、关系改变了什么、付出了什么？
如果只是重复上次行动，请指出可合并之处；
如果重复承担了新的情感或伏笔作用，也请说明证据。
```

### 整理真正可以阅读的版本

```text
使用 novel-delivery-check。
核对我指定的正文版本与现有审查返回，列出当前候选稿、
实际审查状态和供阅读的文件路径，作者认可单独标注。
不要把旧版报告套给新稿；缺报告就标未完成，不补写通过结论。
```

## 全部技能

技能按任务组合，不是一条必须逐项执行的流水线。点击名称可直接阅读对应 `SKILL.md`。

| 阶段 | 技能 | 主要用途 |
|---|---|---|
| 研究 | [novel-reference-study](skills/novel-reference-study/SKILL.md) | 研读参考作品，提炼可原创迁移的机制 |
| 研究 | [novel-setting-research](skills/novel-setting-research/SKILL.md) | 查证年代、地域、职业、器物与现实流程 |
| 设计 | [novel-concept-check](skills/novel-concept-check/SKILL.md) | 检查选题、简介与核心阅读承诺 |
| 设计 | [novel-character-design](skills/novel-character-design/SKILL.md) | 设计动机、伙伴介入和关系变化 |
| 设计 | [novel-character-voice](skills/novel-character-voice/SKILL.md) | 区分对话关注点、语气和潜台词 |
| 设计 | [novel-spatial-design](skills/novel-spatial-design/SKILL.md) | 理清方位、连通、视线与行动路线 |
| 设计 | [novel-horror-design](skills/novel-horror-design/SKILL.md) | 设计恐怖征兆、行动障碍与应对代价 |
| 写作与修订 | [novel-scene-director](skills/novel-scene-director/SKILL.md) | 组织场景目标、动作、情绪与后果 |
| 写作与修订 | [novel-reveal-control](skills/novel-reveal-control/SKILL.md) | 安排秘密揭示、信息负担与承诺兑现 |
| 写作与修订 | [author-first-person-fiction](skills/author-first-person-fiction/SKILL.md) | 检查第一人称信息边界、空间与动作因果 |
| 写作与修订 | [r01-author-feedback](skills/r01-author-feedback/SKILL.md) | 将作者已明确的反馈用于相应修订 |
| 审查 | [novel-logic-review](skills/novel-logic-review/SKILL.md) | 检查线索、动机、道具及跨章因果 |
| 审查 | [novel-reader-review](skills/novel-reader-review/SKILL.md) | 检查冷读体验并提出反方质疑 |
| 审查 | [novel-quality-check](skills/novel-quality-check/SKILL.md) | 依据正文评估冲突、情绪、期待和节奏 |
| 审查 | [novel-boring-detect](skills/novel-boring-detect/SKILL.md) | 识别流水账、功能重复与连续拖延 |
| 审查 | [novel-character-check](skills/novel-character-check/SKILL.md) | 检查行为一致性、关系与工具人化 |
| 审查 | [novel-opening-check](skills/novel-opening-check/SKILL.md) | 检查开篇进入感、处境与题材承诺 |
| 状态与交付 | [novel-chapter-state](skills/novel-chapter-state/SKILL.md) | 提取事件、人物章末状态和未兑现承诺 |
| 状态与交付 | [novel-delivery-check](skills/novel-delivery-check/SKILL.md) | 核对指定版本、审查证据与阅读入口 |

`r01-author-feedback` 保留旧名称以兼容既有调用，内容不依赖某部私人小说。

## 协作规则

单次检查可以直接使用一个技能。长期写作或多人协作时，将 [AGENTS.md](AGENTS.md) 中适用的规则合并进自己的项目；[AGENTS.example.md](AGENTS.example.md) 提供简版。保留原项目的事实与作者决定，不直接覆盖已有文件。

规则重点是：

- **比较正文中的变化。** 新章对照相关前文，修订对照上一稿。人物处境、认知、关系、选择或行动后果是否改变，比日期、地点和分数更有意义。
- **有改善就继续，重复空转就调整。** 不设默认三章或两轮配额；持续推进以作者授权为准。反复改同一问题却无改善时，停止原路径，保存问题并提出不同处理方向。已明确约定的投入边界仍有效。
- **真正执行独立审查。** 主笔可以自检，独立结论要来自实际审查返回；冷读只拿指定正文，逻辑审查按需获得设定。
- **每个结论绑定版本。** 草稿、自检、独立审查、可交付和作者认可分别记录；新稿不能继承旧稿的通过状态。

具体调度与交接见 [协作说明](docs/collaboration.md)。本包提供工作指引，自动派发、权限隔离、计费控制及发布由宿主和项目负责。

## 已验证到哪里

当前完成 19 项技能格式检查、包内引用与版本检查，以及有限的独立使用验证：首轮四个案例，补充六组请求。这两次验证覆盖不同的技能子集，并不代表所有技能在所有场景均已验证。

实际观察包括：识别连续章节的功能重复；保留有效的安静情感戏；缺正文时不强行评分；拒绝以旧版报告验收新稿。完整输入、实际输出、后续澄清和未测范围见 [VALIDATION.md](VALIDATION.md) 与 [行为验证说明](evals/README.md)。

尚未完成跨宿主、多模型或真实长篇自动化的端到端验证；没有费用节省比例或固定质量分数承诺。v0.1.0 是第一份可持续维护的版本，仓库已公开；后续改动按版本记录维护，整体许可另行确定。

## 常见问题

**需要每章把 19 个技能都跑一遍吗？** 选择当前问题需要的技能即可。只查对白时无需先做地域研究，已有有效审查也无需反复全量重跑。

**已经有起草或大纲工具，还能用吗？** 可以先接入一个审查或设计技能。它们接收你实际提供的文本和资料；是否能够读取文件、联网查证或独立委派，取决于宿主能力与授权。

**能安装成一键自动写书插件吗？** 当前交付的是技能目录和协作规则，尚未提供插件清单或自动调度程序。现阶段按上面的本地方式使用。

**新技能没有出现怎么办？** 检查是否复制了完整文件夹、其中是否有 `SKILL.md`、宿主是否扫描该位置，以及是否存在同名旧副本。必要时重新加载；再让执行者确认实际使用的技能文件。

## 维护与贡献

欢迎提供一个具体问题和最小脱敏样例：使用的技能/版本、输入、实际结果、你认为哪里有问题，以及应当保留的正常行为。不要提交未公开正文、人物谜底、私人路径或原始聊天。可以通过 Issue 或 PR 反馈，也可随本地修订附上同样的信息。

`skills/` 是维护源，安装目录是副本。改进按“复现问题 → 最小修改 → 验证受影响行为与正常对照 → 记录版本 → 同步安装”推进，细则见 [MAINTAINING.md](MAINTAINING.md) 和 [CHANGELOG.md](CHANGELOG.md)。

维护者在 Python 3.10+ 环境准备好 [验证依赖](requirements-dev.txt) 后，可在包根目录运行：

```sh
python3 scripts/validate_package.py
```

脚本不会自动安装依赖；只检查结构、版本、引用和部分明显私人标识，不能替代行为验证或人工来源核对。

## 来源与许可

项目署名为 **梁养浩**。他人分发或公开改编本技能包时保留项目、作者和第三方来源的要求，已记录于 [署名声明](NOTICE.md)，将随首次公开时确定的许可落实。此声明不单独授予使用许可；上游材料的既有权利与许可继续有效。

本包是在既有小说技能基础上的整理与改进，并补入实际协作经验。感谢 [snowflake-fiction](https://github.com/hestudy/snowflake-fiction)、[chinese-novelist-skill](https://github.com/PenglongHuang/chinese-novelist-skill) 及本地归档的 dreampowers；具体涉及内容与已知来源见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

**整体许可仍待确认。** 已保留可核对的 MIT 与 GPL-3.0 上游文本，当前没有统一根目录 `LICENSE`。首次公开前须完成整体许可方案与来源版本补齐；不能将本包标为已采用 MIT 或已完成开源许可核定。

README 的信息组织参考了 [Anthropic Skills](https://github.com/anthropics/skills) 的技能说明与使用入口、[Superpowers](https://github.com/obra/superpowers) 的工作流与安装组织，以及 [chinese-novelist-skill](https://github.com/PenglongHuang/chinese-novelist-skill) 的快速开始。此处仅借鉴文档结构；能力、示例和验证范围均以本包实际内容为准。
