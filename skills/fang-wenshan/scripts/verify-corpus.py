#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""语料校验：检查 lyrics/ 全库 frontmatter 完整性、重复歌名、verified 统计、
段落标记、来源域名分布。无参数运行，输出报告，发现问题以非零退出。

用法: python3 skills/fang-wenshan/scripts/verify-corpus.py
"""
import re
import sys
from collections import Counter
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
LYRICS_DIR = SKILL_DIR / "lyrics"

REQUIRED_KEYS = ["title", "artist", "album", "year", "themes", "style", "source", "verified"]
SECTION_RE = re.compile(r"【[^】]+】")


def main():
    if not LYRICS_DIR.is_dir():
        print("错误: 未找到 lyrics/ 目录", file=sys.stderr)
        return 1

    files = sorted(LYRICS_DIR.rglob("*.md"))
    problems = []
    titles = Counter()
    verified = Counter()
    sources = Counter()
    no_section = 0

    for f in files:
        text = f.read_text(encoding="utf-8")
        rel = f.relative_to(SKILL_DIR).as_posix()
        m = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
        if not m:
            problems.append(f"{rel}: 无 frontmatter")
            continue
        fm = m.group(1)
        for key in REQUIRED_KEYS:
            if not re.search(rf"^{key}:", fm, re.M):
                problems.append(f"{rel}: 缺少字段 {key}")
        mt = re.search(r"^title:\s*(.+)$", fm, re.M)
        if mt:
            titles[mt.group(1).strip()] += 1
        mv = re.search(r"^verified:\s*(\w+)", fm, re.M)
        verified[mv.group(1) if mv else "?"] += 1
        ms = re.search(r"^source:\s*(.+)$", fm, re.M)
        if ms:
            url = ms.group(1).strip()
            src = url.split("/")[2] if url.startswith("http") else url
            sources[src] += 1
        if not SECTION_RE.search(text):
            no_section += 1
            problems.append(f"{rel}: 正文无段落标记")

    dups = {t: c for t, c in titles.items() if c > 1}

    print(f"文件总数: {len(files)}")
    print(f"verified 分布: {dict(verified)}")
    print(f"歌手分布: {dict(Counter() | {})}")
    by_artist = Counter()
    for f in files:
        text = f.read_text(encoding="utf-8")
        m = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
        if m:
            a = re.search(r"^artist:\s*(.+)$", m.group(1), re.M)
            if a:
                by_artist[a.group(1).strip()] += 1
    for artist, n in by_artist.most_common():
        print(f"  {artist}: {n} 首")
    print(f"来源域名: {dict(sources.most_common(8))}")
    print(f"无段落标记文件: {no_section}")
    print(f"重复歌名: {dups if dups else '无'}")
    if problems:
        print("\n== 问题清单 ==")
        for p in problems:
            print(" -", p)
        return 1
    print("\n校验通过: 全部合格 ✅")
    return 0


if __name__ == "__main__":
    sys.exit(main())
