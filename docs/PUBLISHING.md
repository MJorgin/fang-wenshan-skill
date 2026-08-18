# 发布指南（公开 GitHub 仓库）

本仓库采用「一库两用」：同一目录下，git 只跟踪公开内容，`lyrics/` 与 `catalog.md` 被 `.gitignore` 排除，**永不入库**。

## 可公开 / 不可公开

| 内容 | 状态 | 许可 |
|---|---|---|
| SKILL.md、techniques/、criticism/、examples/01-03（原创仿写）、scripts/、docs/、README、index.js、cordis.patch.yml | ✅ 公开 | MIT（原创内容） |
| skills/fang-wenshan/lyrics/（歌词全文 111 首） | ❌ 排除 | 受版权保护，仅本地个人学习 |
| skills/fang-wenshan/catalog.md（含名句摘录） | ❌ 排除 | 稳妥起见一并排除 |
| skills/fang-wenshan/examples/04-06（音乐生成工具配置，含商业产品名与歌手声线描述） | ❌ 排除 | 品牌/名字风险，仅本地使用 |

短句引用说明：techniques/criticism/examples 中对原词的单句引用（每处 ≤1 句、注明出处）属合理引用范畴，公开前已控制在最小范围。

## 发布前检查（每次推送前必跑）

```bash
bash scripts/check-public.sh
```

脚本会验证：① lyrics/ 与 catalog.md 及 examples/04-06 是否被 git 忽略；② 已跟踪文件里有无本机用户目录绝对路径（形如 Users 目录下的真实路径，会泄露用户名）；③ 有无密钥模式（api key / token / secret）；④ 有无品牌/歌手名痕迹（音乐生成工具名、声线模仿对象名）；⑤ 有无意外产物（pycache、DS_Store、日志）。全部通过才允许 push。

## 发布步骤（首次）

```bash
cd <本仓库路径>
git init
git add -A
git status          # 确认 lyrics/ 与 catalog.md 不在待提交列表（check-public.sh 也会把关）
git commit -m "feat: 方文山歌词 skill 公开版（不含歌词库，版权内容本地私有）"
git branch -M main
git remote add origin https://github.com/<你的账号>/fang-wenshan-skill.git
git push -u origin main
```

## 日常维护

- 语料更新：照常往 `lyrics/` 加文件，git 自动忽略，不影响本地使用与 catalog 重建（catalog.md 重建后依然被忽略）。
- 推送前：先跑 `bash scripts/check-public.sh`。
- 想彻底上锁：在 GitHub 仓库 Settings → 分支保护，禁止 `git add -f` 强推（可选）。

## 安全提醒

- 本仓库不含任何密钥（已扫描验证）；API key 一律在 `~/.dsh/secrets/`，永不入库。
- 仓库路径中的绝对路径已清洗为占位符；README 使用 `~` 相对写法。
- 若将来公开版被他人 fork，歌词库仍不会流出（本来就不在 git 历史里）。
