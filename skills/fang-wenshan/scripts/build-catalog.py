#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""扫描 lyrics/**/*.md 的 frontmatter，汇总生成 catalog.md 全集索引。

用法: python3 skills/fang-wenshan/scripts/build-catalog.py
"""
import re
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent  # skills/fang-wenshan
LYRICS_DIR = SKILL_DIR / "lyrics"
OUT_FILE = SKILL_DIR / "catalog.md"


def parse_frontmatter(text):
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
    if not m:
        return None
    data = {}
    for line in m.group(1).splitlines():
        kv = re.match(r"^(\w+):\s*(.*)$", line.strip())
        if kv:
            data[kv.group(1)] = kv.group(2).strip()
    return data


def main():
    if not LYRICS_DIR.is_dir():
        print("未找到 lyrics/ 目录", file=sys.stderr)
        return 1
    songs = []
    for f in sorted(LYRICS_DIR.rglob("*.md")):
        text = f.read_text(encoding="utf-8")
        d = parse_frontmatter(text)
        if d is None:
            print(f"跳过（无 frontmatter）: {f}", file=sys.stderr)
            continue
        d["_path"] = f.relative_to(SKILL_DIR).as_posix()
        songs.append(d)

    by_artist = {}
    for s in songs:
        by_artist.setdefault(s.get("artist", "未知歌手"), []).append(s)

    lines = [
        "# 方文山歌词全集索引",
        "",
        f"共收录 {len(songs)} 首。本索引由 `scripts/build-catalog.py` 自动生成，勿手改。",
        "",
        "字段：年份 / 歌名 / 专辑 / 主题 / 风格 / 名句 / verified / 路径（相对本目录）",
        "",
    ]
    for artist in sorted(by_artist):
        ss = sorted(
            by_artist[artist],
            key=lambda x: (str(x.get("year", "")), x.get("album", ""), x.get("title", "")),
        )
        lines.append(f"## {artist}（{len(ss)} 首）")
        for s in ss:
            lines.append(
                f"- {s.get('year', '?')} 《{s.get('title', '?')}》 "
                f"专辑《{s.get('album', '?')}》 主题[{s.get('themes', '')}] "
                f"风格[{s.get('style', '')}] 名句「{s.get('famous', '')}」 "
                f"verified={s.get('verified', '?')} → `{s['_path']}`"
            )
        lines.append("")
    OUT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"catalog.md 已生成: {OUT_FILE}（{len(songs)} 首）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
