import { readFile, mkdir } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { resolve } from 'node:path';
import { createHash } from 'node:crypto';

const root = new URL('./', import.meta.url);
const skill = await readFile(new URL('../communication-style/SKILL.md', root), 'utf8');
const body = skill.replace(/^---\r?\n[\s\S]*?\r?\n---(?:\r?\n|$)/, '').trim();
const digest = createHash('sha256').update(body).digest('hex');
const tag = '<clarity-communication-style source="' + digest + '">';
const prompt = [
  tag,
  'The communication-style skill is already loaded below. Apply it when communicating with the human.',
  'This block does not start any other Clarity workflow.',
  '',
  body,
  '</clarity-communication-style>',
].join('\n');
const outdir = process.argv[2] ? resolve(process.argv[2]) : fileURLToPath(new URL('dist/', root));
await mkdir(outdir, { recursive: true });

for (const platform of ['omp', 'opencode']) {
  const result = await Bun.build({
    entrypoints: [fileURLToPath(new URL(platform + '/index.js', root))],
    outdir,
    naming: platform + '.js',
    target: 'bun',
    format: 'esm',
    define: {
      __CLARITY_COMMUNICATION_STYLE__: JSON.stringify(prompt),
      __CLARITY_COMMUNICATION_STYLE_TAG__: JSON.stringify(tag),
    },
  });
  if (!result.success) throw new AggregateError(result.logs, 'Failed to build ' + platform + ' plugin');
}
