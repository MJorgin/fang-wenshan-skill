#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""押韵检查：读取歌词 md 文件，输出每行末字、韵母（需 pypinyin）与韵脚分组。

用法:
  python3 scripts/rhyme-check.py <歌词文件.md>
完整韵母分析需先安装: pip3 install pypinyin
未安装时退化为内置常见末字简表（覆盖不全会标 ?）。
"""
import re
import sys
from pathlib import Path

# 常见歌词末字 -> 韵母（无音调）简表，作为 pypinyin 缺失时的降级方案。
# 韵母与 pypinyin Style.FINALS_TONE3 去声调后一致（如 光->uang、黄->uang）。
FALLBACK_FINALS = {
    # i / u / ü
    "你": "i", "一": "i", "里": "i", "地": "i", "起": "i", "意": "i",
    "记": "i", "气": "i", "题": "i", "细": "i", "雨": "v", "句": "v",
    "路": "u", "书": "u", "福": "u", "苦": "u", "诉": "u", "处": "u",
    "不": "u", "步": "u", "哭": "u", "度": "u", "初": "u", "露": "u",
    "的": "e", "了": "e", "呢": "e", "歌": "e", "车": "e", "河": "e",
    "和": "e", "合": "e", "热": "e", "夜": "ie", "月": "ve", "雪": "ve",
    "界": "ie", "借": "ie", "别": "ie", "节": "ie", "灭": "ie", "约": "ve",
    # a / ia / ua
    "花": "a", "画": "ua", "话": "ua", "沙": "a", "发": "a", "家": "ia",
    "下": "ia", "涯": "ia", "假": "ia", "夏": "ia", "妈": "a", "爸": "a",
    "抓": "ua", "卦": "ua", "华": "ua", "差": "a", "怕": "a", "茶": "a",
    # ang / iang / uang
    "光": "uang", "凉": "iang", "裳": "ang", "章": "ang", "墙": "iang",
    "僵": "iang", "谎": "uang", "黄": "uang", "桨": "iang", "妆": "uang",
    "样": "iang", "长": "ang", "香": "iang", "想": "iang", "上": "ang",
    "方": "ang", "场": "ang", "伤": "ang", "郎": "ang", "娘": "iang",
    "央": "ang", "霜": "uang", "窗": "uang", "忘": "ang", "忙": "ang",
    "洋": "iang", "响": "iang", "江": "iang", "巷": "iang", "唱": "ang",
    "浪": "ang", "烫": "ang", "糖": "ang", "汤": "ang", "双": "uang",
    "装": "uang", "床": "uang", "网": "ang", "放": "ang", "望": "ang",
    "荒": "uang", "狂": "uang", "仗": "ang", "账": "ang", "腔": "iang",
    # an / ian / uan
    "晚": "an", "半": "an", "满": "an", "山": "an", "蓝": "an", "难": "an",
    "看": "an", "岸": "an", "散": "an", "寒": "an", "天": "ian", "年": "ian",
    "间": "ian", "远": "uan", "边": "ian", "言": "ian", "前": "ian",
    "见": "ian", "恋": "ian", "念": "ian", "烟": "ian", "缘": "uan",
    "愿": "uan", "圆": "uan", "全": "uan", "欢": "uan", "断": "uan",
    "乱": "uan", "弯": "uan", "转": "uan", "缠": "an",
    # en / in / un
    "人": "en", "门": "en", "真": "en", "尘": "en", "分": "en", "问": "en",
    "狠": "en", "吻": "en", "痕": "en", "心": "in", "音": "in", "阴": "in",
    "今": "in", "金": "in", "林": "in", "春": "un", "存": "un", "魂": "un",
    "温": "un", "顺": "un", "困": "un", "文": "en", "深": "en", "身": "en",
    # ing / eng / ong
    "情": "ing", "听": "ing", "星": "ing", "明": "ing", "命": "ing",
    "名": "ing", "平": "ing", "轻": "ing", "停": "ing", "行": "ang", "声": "eng",
    "城": "eng", "等": "eng", "风": "eng", "梦": "eng", "生": "eng",
    "灯": "eng", "争": "eng", "成": "eng", "程": "eng", "冷": "eng",
    "疼": "eng", "空": "ong", "中": "ong", "东": "ong", "冬": "ong",
    "钟": "ong", "终": "ong", "红": "ong", "痛": "ong", "浓": "ong",
    "种": "ong", "懂": "ong", "同": "ong", "重": "ong", "动": "ong",
    # ou / iu
    "旧": "iu", "酒": "iu", "留": "iu", "走": "ou", "手": "ou", "首": "ou",
    "头": "ou", "口": "ou", "后": "ou", "愁": "ou", "楼": "ou", "秋": "iu",
    "休": "iu", "流": "iu", "久": "iu", "有": "ou", "够": "ou", "候": "ou",
    "幼": "iu", "柔": "ou", "奏": "ou", "收": "ou", "皱": "ou", "丢": "iu",
    "舟": "ou", "洲": "ou", "州": "ou", "咒": "ou", "昼": "ou", "油": "ou",
    # ai / ei / ui / ao / uo
    "海": "ai", "爱": "ai", "来": "ai", "在": "ai", "开": "ai", "白": "ai",
    "台": "ai", "孩": "ai", "外": "ai", "回": "ui", "会": "ui", "水": "ui",
    "罪": "ui", "睡": "ui", "飞": "ei", "美": "ei", "泪": "ei", "黑": "ei",
    "岛": "ao", "到": "ao", "道": "ao", "老": "ao", "笑": "iao", "要": "iao",
    "调": "iao", "骄": "iao", "桥": "iao", "秒": "iao", "漂": "iao", "草": "ao",
    "好": "ao", "逃": "ao", "包": "ao", "抱": "ao", "恼": "ao", "早": "ao",
    "摇": "iao", "朝": "ao", "庙": "iao", "嚣": "iao", "标": "iao", "跳": "iao",
    "扫": "ao", "号": "ao", "消": "iao", "烧": "ao", "宵": "iao", "晓": "iao",
    "道": "ao", "刀": "ao", "霄": "iao", "老": "ao", "梢": "ao", "招": "ao",
    "傲": "ao", "遥": "iao", "聊": "iao", "料": "iao", "笑": "iao", "嚎": "ao",
    "我": "uo", "错": "uo", "过": "uo", "落": "uo", "火": "uo", "活": "uo",
}


def make_final_fn():
    try:
        from pypinyin import lazy_pinyin, Style  # noqa: PLC0415

        def fn(ch):
            res = lazy_pinyin(ch, style=Style.FINALS_TONE3, errors=lambda _: [""])
            return res[0].rstrip("012345") if res and res[0] else "?"

        print("（使用 pypinyin 完整韵母分析）")
        return fn
    except ImportError:
        print("（未安装 pypinyin，使用内置简表，覆盖不全标 ?；建议 pip3 install pypinyin）")

        def fn(ch):
            return FALLBACK_FINALS.get(ch, "?")

        return fn


PUNCT = set("，。！？、；：""''（）《》【】…—·,.'\"()[]!?;: ")


def tail_char(line):
    for ch in reversed(line):
        if ch not in PUNCT:
            return ch
    return ""


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8")
    in_front = False
    section = ""
    seen_section = False
    runs = []  # (section, final, [末字...])
    final_of = make_final_fn()

    def flush():
        nonlocal runs
        for sec, fin, chars in runs:
            if len(chars) >= 2:
                print(f"  ↳ {sec} 韵母 {fin} ×{len(chars)}: {'、'.join(chars)}")
        runs = []

    def push(sec, fin, ch):
        if runs and runs[-1][0] == sec and runs[-1][1] == fin:
            runs[-1][2].append(ch)
        else:
            runs.append([sec, fin, [ch]])

    print(f"== {path.name} ==")
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("---"):
            in_front = not in_front
            continue
        if in_front or not line:
            continue
        if line.startswith("##"):
            if seen_section:  # 歌词正文之后的拆解/说明部分，停止分析
                break
            continue  # 正文之前的小标题（如「## 歌词正文」）跳过
        if line.startswith("#") or line.startswith("- "):
            continue
        if line.startswith("（") and line.endswith("）"):  # 阶段标注如（副歌重复）
            continue
        if re.match(r"^[【\[][^】\]]+[】\]]", line):
            flush()
            section = line
            seen_section = True
            print(f"\n{line}")
            continue
        ch = tail_char(line)
        fin = final_of(ch) if ch else "?"
        push(section, fin, ch)
        print(f"  {line}   [{ch}] {fin}")
    flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())
