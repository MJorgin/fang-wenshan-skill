<div align="center">

<img src="docs/social-preview.png" alt="fang-wenshan-skill — study Vincent Fang's lyric craft and write your own songs" width="100%">

<br>

# 🏮 fang-wenshan-skill

### *Study Vincent Fang's lyric craft. Write your own songs.*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Corpus](https://img.shields.io/badge/corpus-111%20songs%20(local)-2EA44F)](README.md#-copyright--privacy)
[![Techniques](https://img.shields.io/badge/techniques-5%20cards-4D6BFE)](skills/fang-wenshan/techniques/)
[![Criticism](https://img.shields.io/badge/criticism-5%20files-4D6BFE)](skills/fang-wenshan/criticism/)
[![Cross-tool](https://img.shields.io/badge/cross--tool-Claude%20Code%20%2F%20Codex-8B5CF6)](README.md#-quick-start)
[![Lyrics stay local](https://img.shields.io/badge/lyrics-private%2C%20stay%20local-8B5CF6)](README.md#-copyright--privacy)

[**English**](README.md) · [**简体中文**](docs/lang/README_ZH.md) · [**繁體中文**](docs/lang/README_ZH_TW.md)

<br>

A complete lyric-study system for Vincent Fang (方文山), one of the most awarded Chinese lyricists — not a generic "write lyrics" prompt, but a structured craft library:

- 📚 **111-song lyric corpus (local, private)** — 93 Jay Chou songs (2000–2022, lyricist credits verified track by track) + 18 curated songs by other artists (Jolin Tsai, Landy Wen, S.H.E, Jody Chiang, Joey Yung, Cindy Yen, Nan Quan Mama, Coco Lee, Angela Chang, A-Sun, Will Pan, Eason Chan, Fish Leong) — each with metadata and source URL.
- 🎓 **5 technique cards** — rhyme systems, Chinese-style imagery, rhetoric & allusions (with sources traced), structure & visual storytelling, lyric-melody fit — every card with citations and an actionable checklist.
- 🏆 **5 criticism files** — award records (verified against primary sources), critics & industry reviews, academic research distilled, controversies, and public reception.
- ✍️ **Two working modes** — *analysis* (dissect any song's craft) and *creation* (retrieve references → pick a rhyme → build the skeleton → draft → scorecard self-check → plagiarism check), with a built-in style scorecard and a **4-character plagiarism red line**.
- 🔧 **Three scripts** — rhyme checker, corpus validator, catalog builder.
- ✍️ **Original lyric examples** — three fully-written original songs with line-by-line craft breakdowns and scorecards.

[Why](#-why) · [Quick start](#-quick-start) · [Usage](#-usage) · [Copyright & privacy](#-copyright--privacy) · [FAQ](#-faq) · [Layout](#-layout)

</div>

---

## 🤔 Why

Most "AI lyric writing" is a paragraph of prompt, or a lyrics dump site. `fang-wenshan-skill` goes the other way: **structure the craft methodology so the model actually learns it, then writes**:

| | This skill | Generic lyric prompt | Lyrics dump site |
|---|---|---|---|
| Full lyric corpus (metadata + sources) | ✅ 111 songs (local, private) | ❌ | ✅ but zero analysis |
| Craft library (rhyme / imagery / rhetoric / structure / melody fit) | ✅ 5 cited cards | ❌ relies on model memory | ❌ |
| Critical reception (awards / reviews / papers / disputes) | ✅ 5 files | ❌ | ❌ |
| Repeatable creation workflow + scorecard | ✅ | ❌ one-shot | ❌ |
| Plagiarism guard (4-char red line vs originals) | ✅ hard rule | ❌ | ❌ |
| Rhyme / corpus validation scripts | ✅ automatable | ❌ | ❌ |
| Legally distributable | ✅ public shell ships no lyrics | ✅ | ⚠️ usually risky |

## ⚡ Quick start

The skill body is **self-contained** under `skills/fang-wenshan/` and follows the universal SKILL.md convention:

```sh
# Claude Code
mkdir -p ~/.claude/skills
cp -r skills/fang-wenshan ~/.claude/skills/

# Codex / any agent that supports skills
cp -r skills/fang-wenshan ~/.codex/skills/
```

> A DeepSeek Harness adapter (`index.js` + `cordis.patch.yml`) is included for DSH users — see [Layout](#-layout). The skill itself has no runtime dependencies.

**Local full version (with the 111-song corpus)**: lyric texts are copyrighted and stay local — never distributed with this repo. See [docs/PUBLISHING.md](docs/PUBLISHING.md) for the private-deployment notes.

## 🚀 Usage

Just say it in plain language:

- 📖 **Analysis mode** — "Analyze the rhyme scheme and imagery of a Chinese-style lyric I'll paste." / "What rhetorical devices and allusions appear in this lyric?"
- ✍️ **Creation mode** — "Write a Chinese-style lyric about leaving home, main rhyme -ang, with a hook in the chorus."
- 🏆 **Reception** — "How many Golden Melody Awards for Best Lyricist has this lyricist won?" / "What are the criticisms of the 'Chinese style' wave?"
- 🔍 **Search** — "Find all choruses in -ang rhyme." / "Which Taiwanese-language lyrics are in the corpus?"
- 🔧 **Scripts**:

```sh
python3 skills/fang-wenshan/scripts/rhyme-check.py <lyric.md>   # rhyme analysis (pip3 install pypinyin for full finals)
python3 skills/fang-wenshan/scripts/verify-corpus.py            # corpus integrity check
python3 skills/fang-wenshan/scripts/build-catalog.py            # rebuild the catalog index
```

## 🔒 Copyright & privacy

- **Lyric texts are copyrighted and never enter this repo.** `.gitignore` excludes `lyrics/` and `catalog.md` (which contains famous-line excerpts). Run `bash scripts/check-public.sh` before pushing — it gates on copyright exclusions, absolute paths, secrets, brand/artist-name mentions, and junk artifacts.
- **4-character red line**: any generated lyric sharing 4+ consecutive characters with an original must be rewritten.
- **Attribution**: generated works must not be signed with the original lyricist's name or presented as their unreleased works; review rights before publishing.
- **No keys in the repo** (scanned & verified); credentials live only in `~/.dsh/secrets/`.
- **Public-version behavior**: without the corpus, analysis mode still works fully (technique cards + criticism files); creation mode states the corpus is missing and degrades its retrieval step gracefully.

## ❓ FAQ

**Why is there no lyric full text in the public repo?**
Lyrics are copyrighted works; redistributing them publicly is infringement. The public repo ships the full methodology (technique cards, criticism, examples, scripts); the corpus is completed in private local deployment — see [docs/PUBLISHING.md](docs/PUBLISHING.md).

**Can I use generated lyrics commercially?**
Yes, with three conditions: ① never sign them with the original lyricist's name; ② if set to music, the melody must be original (original melodies belong to their composers/rightsholders); ③ confirm no 4+ consecutive characters shared with any existing lyric (the skill's built-in plagiarism step).

**Why are some famous songs missing from the corpus?**
Only works actually credited to the lyricist are included. Several widely-misattributed songs were excluded after credit verification, while songs commonly missed were included — every track was checked against official credits.

## 🗺️ Layout

```
fang-wenshan-skill/
├── package.json           # dsh.bundle manifest (private — never published to npm)
├── cordis.patch.yml       # DeepSeek Harness adapter layer
├── index.js               # DSH adapter: registers the skill provider
├── skills/fang-wenshan/   # ★ the skill itself (cross-tool, self-contained)
│   ├── SKILL.md           # two modes, workflow, scorecard, plagiarism & copyright rules
│   ├── catalog.md         # full index (generated locally; excluded from public)
│   ├── lyrics/            # 111 lyric texts (local private; excluded from public)
│   ├── techniques/        # 5 technique cards (cited)
│   ├── criticism/         # 5 criticism files (cited)
│   ├── examples/          # 3 original example lyrics with craft breakdowns
│   └── scripts/           # rhyme-check / verify-corpus / build-catalog
├── scripts/check-public.sh # pre-push safety gate (copyright / paths / secrets / names / junk)
├── docs/                  # social preview, acceptance checklist, publishing guide, language READMEs
└── LICENSE                # MIT (covers original content only, not the lyrics)
```

## 🤝 Related

- [dsh-media-skills](https://github.com/MJorgin/dsh-media-skills) — free image reading & generation skill pack, same author
- [dsh-agent-conductor](https://github.com/MJorgin/dsh-agent-conductor) — orchestrate external agent CLIs, same author

> PRs, issues and translations are welcome — **but never include copyrighted lyric full text in a PR**.

## 📄 License

[MIT](LICENSE) — covers the original content of this repo only (SKILL.md, technique cards, criticism files, examples, scripts, docs). Lyric texts belong to their authors and rightsholders and are not distributed with this repo.
