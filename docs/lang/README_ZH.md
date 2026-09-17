<div align="center">

<img src="../social-preview.png" alt="fang-wenshan-skill — 学习方文山的歌词艺术，写你自己的歌" width="100%">

<br>

# 🏮 fang-wenshan-skill

### *学方文山的词，写你自己的歌。*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../LICENSE)
[![语料](https://img.shields.io/badge/corpus-111%20songs%20(local)-2EA44F)](../README.md#-版权与隐私)
[![手法卡](https://img.shields.io/badge/techniques-5%20cards-4D6BFE)](../techniques/)
[![评价库](https://img.shields.io/badge/criticism-5%20files-4D6BFE)](../criticism/)
[![跨工具](https://img.shields.io/badge/cross--tool-Claude%20Code%20%2F%20Codex-8B5CF6)](../README.md#-快速开始)
[![歌词私有](https://img.shields.io/badge/lyrics-private%2C%20stay%20local-8B5CF6)](../README.md#-版权与隐私)

[**English**](../README.md) · [**简体中文**](README_ZH.md) · [**繁體中文**](README_ZH_TW.md)

<br>

方文山（Vincent Fang）歌词学习与创作 skill：不是一段「写歌词提示词」，而是一套结构化的创作方法论体系——**语料库 + 手法知识库 + 外界评价库 + 双模式工作流**：

- 📚 **111 首歌词语料（本地私有）** — 周杰伦 93 首（2000–2022 全部专辑逐曲核实词作者）+ 其他歌手精选 18 首（蔡依林、温岚、S.H.E、江蕙、容祖儿、袁咏琳、南拳妈妈、李玟、张韶涵、阿桑、潘玮柏、陈奕迅、梁静茹），每首带元数据与来源 URL。
- 🎓 **5 张手法卡** — 韵脚体系（含素颜韵脚诗）、中国风意象系统、修辞与用典（注明化用出处）、结构与画面感、词曲咬合与可唱性，全部带来源与「可操作的创作清单」。
- 🏆 **5 份评价库** — 获奖记录（对一手来源逐条核实）、乐评与业界评价、学术研究提炼、批评与争议、大众口碑与名句。
- ✍️ **双模式工作流** — 分析模式（拆解任意歌曲手法）+ 创作模式（检索参考 → 定韵 → 搭骨架 → 起草 → 评分卡自查 → 查重），内置风格评分卡与 **4 字查重红线**。
- 🔧 **三件脚本** — 押韵检查、语料校验、索引重建。
- ✍️ **原创仿写示例** — 3 首完整原创歌词，带逐行手法拆解与评分卡。

[为什么](#-为什么) · [快速开始](#-快速开始) · [使用方式](#-使用方式) · [版权与隐私](#-版权与隐私) · [常见问题](#-常见问题) · [目录结构](#-目录结构)

</div>

---

## 🤔 为什么

市面上「AI 写歌词」大多只有一段提示词，或只有一个歌词收集站。本 skill 的做法不同——**把创作方法论结构化，让模型真的「学会」再创作**：

| | 本 skill | 通用「写歌词提示词」 | 纯歌词收集库 |
|---|---|---|---|
| 歌词全文语料（元数据/来源） | ✅ 111 首（本地私有） | ❌ | ✅ 但无分析 |
| 手法知识库（韵脚/意象/修辞/结构/咬合） | ✅ 5 卡全带来源 | ❌ 靠模型记忆 | ❌ |
| 外界评价库（获奖/乐评/论文/批评） | ✅ 5 文件 | ❌ | ❌ |
| 创作工作流 + 风格评分卡 | ✅ 可复现流程 | ❌ 单次生成 | ❌ |
| 查重护栏（与原词 4 字红线） | ✅ 硬性规则 | ❌ 易抄袭 | ❌ |
| 押韵/语料校验脚本 | ✅ 可自动化 | ❌ | ❌ |
| 版权合规可公开分发 | ✅ 公开版不含歌词 | ✅ | ⚠️ 通常有风险 |

## ⚡ 快速开始

skill 本体在 `skills/fang-wenshan/` 下，**目录自包含**、遵循通用 SKILL.md 规范：

```sh
# Claude Code
mkdir -p ~/.claude/skills
cp -r skills/fang-wenshan ~/.claude/skills/

# Codex / 任何支持 skills 的 agent
cp -r skills/fang-wenshan ~/.codex/skills/
```

> 仓库内附 DeepSeek Harness 适配层（`index.js` + `cordis.patch.yml`），DSH 用户可选安装；skill 本体无运行时依赖。

**本地完整版（含 111 首歌词语料）**：歌词全文受版权保护，仅本地个人学习使用，不随公开仓库分发。私有部署方式见 [docs/PUBLISHING.md](../PUBLISHING.md)。

## 🚀 使用方式

直接说人话即可：

- 📖 **分析模式**：「分析我贴给你的这段歌词的韵脚与意象手法」「这段词用了哪些修辞？化用了什么？」
- ✍️ **创作模式**：「写一首中国风歌词，主题离乡，主韵 -ang，副歌要有金句」
- 🏆 **评价库**：「这位词人拿过几次金曲奖最佳作词人？」「对"中国风"潮流的批评有哪些？」
- 🔍 **检索**：「找所有 -ang 韵的副歌」「语料库里的台语歌词」
- 🔧 **脚本**：

```sh
python3 skills/fang-wenshan/scripts/rhyme-check.py <歌词文件.md>   # 押韵检查（完整韵母建议 pip3 install pypinyin）
python3 skills/fang-wenshan/scripts/verify-corpus.py               # 语料完整性校验
python3 skills/fang-wenshan/scripts/build-catalog.py               # 重建全集索引
```

## 🔒 版权与隐私

- **歌词全文受版权保护，绝不进公开仓库**。`.gitignore` 已排除 `lyrics/` 与 `catalog.md`（含名句摘录）；推送前跑 `bash scripts/check-public.sh` 把关（版权排除 / 路径隐私 / 密钥 / 品牌与歌手名 / 垃圾产物五查）。
- **查重红线**：生成歌词与原词连续 4 字及以上相同即按抄袭处理，必须改写。
- **署名规则**：生成作品不得署原作者之名、不得声称是其未发表作品；公开发布前自行评估版权与署名。
- **密钥**：仓库不含任何 API key（已扫描验证）；密钥一律在 `~/.dsh/secrets/`，永不入库。
- **公开版降级说明**：无歌词库时分析模式照常（靠手法卡/评价库），创作模式明确告知语料缺失并降级检索。

## ❓ 常见问题

**为什么公开版没有歌词全文？**
歌词是受版权保护的作品，公开分发有侵权风险。公开版提供全部方法论（手法卡/评价卡/示例/脚本），语料由本地私有部署补齐——见 [docs/PUBLISHING.md](../PUBLISHING.md)。

**生成的歌词能商用吗？**
可以，注意三条：① 不得署原作者之名；② 若配曲，旋律需原创（原曲旋律版权归曲作者/版权方）；③ 自行确认歌词与任何既有作品无 4 字以上连续重合（skill 内置查重步骤）。

**为什么有的热门歌不在语料里？**
只收「作词」署名确认的作品——多首常被误传的歌曲（如《枫》《夜的第七章》《牛仔很忙》《花海》）经官方 credit 核实后排除，而常被漏掉的（如《甜甜的》）已收录；每首均按官方署名逐曲核实。

## 🗺️ 目录结构

```
fang-wenshan-skill/
├── package.json           # dsh.bundle manifest（private，禁止 npm 发布）
├── cordis.patch.yml       # DeepSeek Harness 适配层
├── index.js               # DSH 适配层：注册 skill provider
├── skills/fang-wenshan/   # ★ skill 本体（跨工具通用，目录自包含）
│   ├── SKILL.md           # 双模式、工作流、评分卡、查重与版权规则
│   ├── catalog.md         # 全集索引（本地生成，公开版不含）
│   ├── lyrics/            # 歌词全文 111 首（本地私有，公开版不含）
│   ├── techniques/        # 手法卡 ×5
│   ├── criticism/         # 评价库 ×5
│   ├── examples/          # 原创仿写示例 ×3
│   └── scripts/           # rhyme-check / verify-corpus / build-catalog
├── scripts/check-public.sh # 推送前安全把关（版权/路径/密钥/名字/垃圾）
├── docs/                  # 简介 banner、验收清单、发布指南、多语言 README
└── LICENSE                # MIT（仅覆盖原创内容，不含歌词）
```

## 🤝 相关仓库

- [dsh-media-skills](https://github.com/MJorgin/dsh-media-skills) — 同作者的免费读图/生图技能包
- [dsh-agent-conductor](https://github.com/MJorgin/dsh-agent-conductor) — 同作者的指挥家

> PR、issue、翻译均欢迎——**但请勿在 PR 中加入任何受版权保护的歌词全文**。

## 📄 License

[MIT](../LICENSE)（仅覆盖本仓库原创内容：SKILL.md、手法卡、评价卡、示例、脚本、文档；歌词全文版权归原作者与版权方，不随本仓库分发）
