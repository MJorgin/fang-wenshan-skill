#!/usr/bin/env bash
# 公开仓库发布前检查：版权排除 / 路径清洗 / 密钥 / 品牌与歌手名 / 产物垃圾
# 用法: bash scripts/check-public.sh   （在仓库根目录执行）
set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
FAIL=0

# 依赖 git；未初始化时自动初始化（不提交）
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "[init] 未发现 git 仓库，自动 git init（不创建提交）"
  git init -q
fi

echo "== 1/5 版权排除检查 =="
for p in "skills/fang-wenshan/lyrics" "skills/fang-wenshan/catalog.md" \
         "skills/fang-wenshan/examples/04-旧巷-Suno配置.md" \
         "skills/fang-wenshan/examples/05-剑挂柳梢-武侠中国风.md" \
         "skills/fang-wenshan/examples/06-Suno试听方法与矩阵.md"; do
  if git check-ignore -q "$p"; then
    echo "  ✅ 已忽略: $p"
  else
    echo "  ❌ 未被忽略: $p —— 禁止推送，检查 .gitignore"
    FAIL=1
  fi
done
# 双保险：即使被忽略也扫描暂存区/已跟踪文件里有无歌词
STAGED_LYRICS=$(git ls-files | grep -c "^skills/fang-wenshan/lyrics/" || true)
if [ "$STAGED_LYRICS" -gt 0 ]; then
  echo "  ❌ 暂存区/已跟踪文件出现歌词文件 —— git rm --cached 清理"
  FAIL=1
fi

echo "== 2/5 绝对路径检查（隐私）=="
HITS=$(grep -rnE "/Users/|/home/" --include="*.md" --include="*.json" --include="*.js" --include="*.yml" --include="*.py" . 2>/dev/null | grep -v "^\./\.git/" || true)
if [ -n "$HITS" ]; then
  echo "  ❌ 发现绝对路径（泄露用户名/机器路径）:"
  echo "$HITS"
  FAIL=1
else
  echo "  ✅ 无绝对路径"
fi

echo "== 3/5 密钥检查 =="
KEYS=$(grep -rniE "sk-[a-z0-9]{20,}|api[_-]?key[[:space:]]*[:=]|secret[[:space:]]*[:=]|Bearer [A-Za-z0-9]" --include="*.md" --include="*.json" --include="*.js" --include="*.yml" --include="*.py" --include="*.sh" . 2>/dev/null | grep -v "^\./\.git/" | grep -viE "check-public|tokenizer|check_public" || true)
if [ -n "$KEYS" ]; then
  echo "  ❌ 疑似密钥/凭证痕迹:"
  echo "$KEYS"
  FAIL=1
else
  echo "  ✅ 无密钥痕迹"
fi

echo "== 4/5 品牌与歌手名检查 =="
# 公开版不出现：商业音乐生成工具名、以及用于描述声线的歌手名。
# 注意：被忽略的文件（examples/04-06）不在扫描范围，本检查针对已跟踪文件；
# .gitignore 与 check-public.sh 自身因需要书写忽略规则/匹配模式而豁免。
NAMES=$(git ls-files | grep -vE "^\.gitignore$|^scripts/check-public\.sh$" | while read -r f; do grep -liE "suno|孙燕姿|adele|stefanie" "$f" 2>/dev/null; done | head -20)
if [ -n "$NAMES" ]; then
  echo "  ❌ 已跟踪文件出现品牌/歌手名（公开版应不含）:"
  echo "$NAMES"
  FAIL=1
else
  echo "  ✅ 无品牌/歌手名痕迹"
fi

echo "== 5/5 产物垃圾检查 =="
JUNK=$(git status --porcelain 2>/dev/null | grep -iE "\.DS_Store|__pycache__|\.pyc|\.log$" || true)
if [ -n "$JUNK" ]; then
  echo "  ⚠️ 发现垃圾产物（.gitignore 已覆盖则无碍）:"
  echo "$JUNK"
else
  echo "  ✅ 无垃圾产物"
fi

echo
if [ "$FAIL" -eq 0 ]; then
  echo "🎉 检查通过，可以推送公开仓库。"
  exit 0
else
  echo "⛔ 存在阻断问题，先修复再推送。"
  exit 1
fi
