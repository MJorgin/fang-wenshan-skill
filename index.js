/**
 * DSH 适配层：把通用 skill `fang-wenshan` 注册进 DeepSeek Harness。
 *
 * 这是本仓库唯一的 DSH 专有代码。skill 本体位于 `skills/fang-wenshan/`，
 * 遵循通用 SKILL.md 规范，可被 Claude Code / Codex / 其他 agent 直接挂载，
 * 无需本适配层。
 *
 * IMPORTANT: the lyrics under `skills/fang-wenshan/lyrics/` are copyrighted
 * material collected for private, local study only. This package is marked
 * `private` and must never be published to a public registry or repository.
 *
 * @module fang-wenshan-skill
 */

import { readFile } from 'node:fs/promises'
import { fileURLToPath } from 'node:url'

const PROVIDER_NAME = 'fang-wenshan-skill'

const SKILLS = [
  {
    name: 'fang-wenshan',
    description:
      '方文山歌词学习与创作。当用户要分析方文山（周杰伦等）歌词的写作手法、学习其创作风格，或按主题/情感/韵脚/风格创作歌词时使用。内置歌词库（私有）、手法卡、评价库、押韵检查脚本。',
    body: new URL('./skills/fang-wenshan/SKILL.md', import.meta.url),
    resourceDir: './skills/fang-wenshan/',
  },
].map((skill) => ({
  ...skill,
  invocation: { modelInvocable: true, userInvocable: true },
  provider: PROVIDER_NAME,
  source: 'bundled',
  resourceBase: {
    kind: 'directory',
    path: fileURLToPath(new URL(skill.resourceDir, import.meta.url)),
  },
  rank: 600,
  locator: skill.body,
}))

const provider = {
  name: PROVIDER_NAME,
  list: () => Promise.resolve(SKILLS),
  async get(candidate) {
    const raw = await readFile(candidate.locator, 'utf8')
    // Strip the YAML frontmatter so the loaded body is clean instructions.
    const content = raw.replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n?/, '')
    return {
      name: candidate.name,
      description: candidate.description,
      invocation: candidate.invocation,
      provider: candidate.provider,
      source: candidate.source,
      resourceBase: candidate.resourceBase,
      content,
    }
  },
}

/** Cordis plugin name. */
export const name = 'fang-wenshan-skill'
/** Service required by the bundled provider. */
export const inject = ['skills']

/** Register the bundled skill provider. */
export function apply(ctx) {
  ctx.skills.registerProvider(() => provider)
}
