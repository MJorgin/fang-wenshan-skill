<div align="center">

<img src="../social-preview.png" alt="fang-wenshan-skill — 學習方文山的歌詞藝術，寫你自己的歌" width="100%">

<br>

# 🏮 fang-wenshan-skill

### *學方文山的詞，寫你自己的歌。*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../LICENSE)
[![語料](https://img.shields.io/badge/corpus-111%20songs%20(local)-2EA44F)](../README.md#-版權與隱私)
[![手法卡](https://img.shields.io/badge/techniques-5%20cards-4D6BFE)](../techniques/)
[![評價庫](https://img.shields.io/badge/criticism-5%20files-4D6BFE)](../criticism/)
[![跨工具](https://img.shields.io/badge/cross--tool-Claude%20Code%20%2F%20Codex-8B5CF6)](../README.md#-快速開始)
[![歌詞私有](https://img.shields.io/badge/lyrics-private%2C%20stay%20local-8B5CF6)](../README.md#-版權與隱私)

[**English**](../README.md) · [**简体中文**](README_ZH.md) · [**繁體中文**](README_ZH_TW.md)

<br>

方文山（Vincent Fang）歌詞學習與創作 skill：不是一段「寫歌詞提示詞」，而是一套結構化的創作方法論體系——**語料庫 + 手法知識庫 + 外界評價庫 + 雙模式工作流**：

- 📚 **111 首歌詞語料（本地私有）** — 周杰倫 93 首（2000–2022 全部專輯逐曲核實詞作者）+ 其他歌手精選 18 首（蔡依林、溫嵐、S.H.E、江蕙、容祖兒、袁詠琳、南拳媽媽、李玟、張韶涵、阿桑、潘瑋柏、陳奕迅、梁靜茹），每首帶元數據與來源 URL。
- 🎓 **5 張手法卡** — 韻腳體系（含素顏韻腳詩）、中國風意象系統、修辭與用典（註明化用出處）、結構與畫面感、詞曲咬合與可唱性，全部帶來源與「可操作的創作清單」。
- 🏆 **5 份評價庫** — 獲獎記錄（對一手來源逐條核實）、樂評與業界評價、學術研究提煉、批評與爭議、大眾口碑與名句。
- ✍️ **雙模式工作流** — 分析模式（拆解任意歌曲手法）+ 創作模式（檢索參考 → 定韻 → 搭骨架 → 起草 → 評分卡自查 → 查重），內建風格評分卡與 **4 字查重紅線**。
- 🔧 **三件腳本** — 押韻檢查、語料校驗、索引重建。
- ✍️ **原創仿寫示例** — 3 首完整原創歌詞，帶逐行手法拆解與評分卡。

[為什麼](#-為什麼) · [快速開始](#-快速開始) · [使用方式](#-使用方式) · [版權與隱私](#-版權與隱私) · [常見問題](#-常見問題) · [目錄結構](#-目錄結構)

</div>

---

## 🤔 為什麼

市面上「AI 寫歌詞」大多只有一段提示詞，或只有一個歌詞收集站。本 skill 的做法不同——**把創作方法論結構化，讓模型真的「學會」再創作**：

| | 本 skill | 通用「寫歌詞提示詞」 | 純歌詞收集庫 |
|---|---|---|---|
| 歌詞全文語料（元數據/來源） | ✅ 111 首（本地私有） | ❌ | ✅ 但無分析 |
| 手法知識庫（韻腳/意象/修辭/結構/咬合） | ✅ 5 卡全帶來源 | ❌ 靠模型記憶 | ❌ |
| 外界評價庫（獲獎/樂評/論文/批評） | ✅ 5 文件 | ❌ | ❌ |
| 創作工作流 + 風格評分卡 | ✅ 可重現流程 | ❌ 單次生成 | ❌ |
| 查重護欄（與原詞 4 字紅線） | ✅ 硬性規則 | ❌ 易抄襲 | ❌ |
| 押韻/語料校驗腳本 | ✅ 可自動化 | ❌ | ❌ |
| 版權合規可公開分發 | ✅ 公開版不含歌詞 | ✅ | ⚠️ 通常有風險 |

## ⚡ 快速開始

skill 本體在 `skills/fang-wenshan/` 下，**目錄自包含**、遵循通用 SKILL.md 規範：

```sh
# Claude Code
mkdir -p ~/.claude/skills
cp -r skills/fang-wenshan ~/.claude/skills/

# Codex / 任何支援 skills 的 agent
cp -r skills/fang-wenshan ~/.codex/skills/
```

> 倉庫內附 DeepSeek Harness 適配層（`index.js` + `cordis.patch.yml`），DSH 用戶可選安裝；skill 本體無執行期依賴。

**本地完整版（含 111 首歌詞語料）**：歌詞全文受版權保護，僅本地個人學習使用，不隨公開倉庫分發。私有部署方式見 [docs/PUBLISHING.md](../PUBLISHING.md)。

## 🚀 使用方式

直接說人話即可：

- 📖 **分析模式**：「分析我貼給你的這段歌詞的韻腳與意象手法」「這段詞用了哪些修辭？化用了什麼？」
- ✍️ **創作模式**：「寫一首中國風歌詞，主題離鄉，主韻 -ang，副歌要有金句」
- 🏆 **評價庫**：「這位詞人拿過幾次金曲獎最佳作詞人？」「對"中國風"潮流的批評有哪些？」
- 🔍 **檢索**：「找所有 -ang 韻的副歌」「語料庫裡的台語歌詞」
- 🔧 **腳本**：

```sh
python3 skills/fang-wenshan/scripts/rhyme-check.py <歌詞文件.md>   # 押韻檢查（完整韻母建議 pip3 install pypinyin）
python3 skills/fang-wenshan/scripts/verify-corpus.py               # 語料完整性校驗
python3 skills/fang-wenshan/scripts/build-catalog.py               # 重建全集索引
```

## 🔒 版權與隱私

- **歌詞全文受版權保護，絕不進公開倉庫**。`.gitignore` 已排除 `lyrics/` 與 `catalog.md`（含名句摘錄）；推送前跑 `bash scripts/check-public.sh` 把關（版權排除 / 路徑隱私 / 金鑰 / 品牌與歌手名 / 垃圾產物五查）。
- **查重紅線**：生成歌詞與原詞連續 4 字及以上相同即按抄襲處理，必須改寫。
- **署名規則**：生成作品不得署原作者之名、不得聲稱是其未發表作品；公開發佈前自行評估版權與署名。
- **金鑰**：倉庫不含任何 API key（已掃描驗證）；金鑰一律在 `~/.dsh/secrets/`，永不入庫。
- **公開版降級說明**：無歌詞庫時分析模式照常（靠手法卡/評價庫），創作模式明確告知語料缺失並降級檢索。

## ❓ 常見問題

**為什麼公開版沒有歌詞全文？**
歌詞是受版權保護的作品，公開分發有侵權風險。公開版提供全部方法論（手法卡/評價卡/示例/腳本），語料由本地私有部署補齊——見 [docs/PUBLISHING.md](../PUBLISHING.md)。

**生成的歌詞能商用嗎？**
可以，注意三條：① 不得署原作者之名；② 若配曲，旋律需原創（原曲旋律版權歸曲作者/版權方）；③ 自行確認歌詞與任何既有作品無 4 字以上連續重合（skill 內建查重步驟）。

**為什麼有的熱門歌不在語料裡？**
只收「作詞」署名確認的作品——多首常被誤傳的歌曲（如《楓》《夜的第七章》《牛仔很忙》《花海》）經官方 credit 核實後排除，而常被漏掉的（如《甜甜的》）已收錄；每首均按官方署名逐曲核實。

## 🗺️ 目錄結構

```
fang-wenshan-skill/
├── package.json           # dsh.bundle manifest（private，禁止 npm 發佈）
├── cordis.patch.yml       # DeepSeek Harness 適配層
├── index.js               # DSH 適配層：註冊 skill provider
├── skills/fang-wenshan/   # ★ skill 本體（跨工具通用，目錄自包含）
│   ├── SKILL.md           # 雙模式、工作流、評分卡、查重與版權規則
│   ├── catalog.md         # 全集索引（本地生成，公開版不含）
│   ├── lyrics/            # 歌詞全文 111 首（本地私有，公開版不含）
│   ├── techniques/        # 手法卡 ×5
│   ├── criticism/         # 評價庫 ×5
│   ├── examples/          # 原創仿寫示例 ×3
│   └── scripts/           # rhyme-check / verify-corpus / build-catalog
├── scripts/check-public.sh # 推送前安全把關（版權/路徑/金鑰/名字/垃圾）
├── docs/                  # 簡介 banner、驗收清單、發佈指南、多語言 README
└── LICENSE                # MIT（僅覆蓋原創內容，不含歌詞）
```

## 🤝 相關倉庫

- [dsh-media-skills](https://github.com/MJorgin/dsh-media-skills) — 同作者的免費讀圖/生圖技能包
- [dsh-agent-conductor](https://github.com/MJorgin/dsh-agent-conductor) — 同作者的指揮家

> PR、issue、翻譯均歡迎——**但請勿在 PR 中加入任何受版權保護的歌詞全文**。

## 📄 License

[MIT](../LICENSE)（僅覆蓋本倉庫原創內容：SKILL.md、手法卡、評價卡、示例、腳本、文檔；歌詞全文版權歸原作者與版權方，不隨本倉庫分發）
