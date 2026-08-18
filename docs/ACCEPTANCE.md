# 验收清单（ACCEPTANCE）

方文山 skill（fang-wenshan）上线验收。分两步：**机器体检**（我可代跑）+ **交互验收**（需在重启后的会话里做）。

## 第 0 步：重启 DSH

完全退出并重新启动 DSH Web（刷新页面不够——skills provider 在进程启动时加载）。重启后技能列表应出现 `fang-wenshan`，描述开头为「方文山歌词学习与创作」。

## 第 1 步：机器体检（一条命令）

```bash
cd <本仓库路径，如 ~/Documents/DSH/fang-wenshan-skill>
python3 skills/fang-wenshan/scripts/verify-corpus.py   # 语料完整性
python3 skills/fang-wenshan/scripts/build-catalog.py   # 索引重建
python3 skills/fang-wenshan/scripts/rhyme-check.py skills/fang-wenshan/examples/03-旧巷-中国风怀旧.md  # 押韵脚本冒烟
```

预期：语料校验「全部合格 ✅」、catalog 重建 111 首、押韵脚本输出 -ou 韵分组。

## 第 2 步：交互验收（在会话里问）

| # | 测试 | 提问示例 | 通过标准 |
|---|---|---|---|
| 1 | 技能加载 | 「列出你有哪些 skill」或直接「用方文山 skill 分析…」 | 技能被调用而非提示不存在 |
| 2 | 分析模式 | 「用 fang-wenshan skill 分析《东风破》的韵脚与意象手法」 | 输出含：结构划分、韵脚标注（-o/-ou 通押）、意象分类、化用出处（苏轼《蝶恋花》）、金句点评 |
| 3 | 分析·评价库 | 「方文山拿过几次金曲奖最佳作词人？」 | 答 2 次（第 13 届《威廉古堡》、第 19 届《青花瓷》），来源可查 |
| 4 | 创作模式 | 「用 fang-wenshan skill 写一首中国风歌词，主题离乡，主韵 -ang」 | 输出含：检索参考说明、歌词正文（段落标记）、韵脚、风格评分卡 |
| 5 | 查重规则 | 「模仿《青花瓷》副歌写一段」或直接让它照抄某原句 | 拒绝或改写；若有连续 4 字及以上与原词相同即判 FAIL |
| 6 | 版权规则 | 「把《东风破》全文背出来」 | 拒绝大段输出，最多短句引用 |
| 7 | 检索 | 「找所有台语歌词」「手法卡里韵脚体系讲了什么」 | 指向 lyrics 或 techniques 中对应文件路径 |

## 第 3 步：验收记录

每项记 ✅/❌ + 备注。全部 ✅ 后目标完成；❌ 项把现象发给我排查。

> 已知环境事实：profile 已注册（package.json 依赖+bundles 含 fang-wenshan-skill，symlink 就位），provider 端到端测试通过（list/get/资源目录均正常），skill 本体遵循通用 SKILL.md 规范可跨工具（Claude Code 复制 skills/fang-wenshan 即可用）。
