import { describe, expect, test } from 'bun:test';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

const outdir = process.env.CLARITY_PLUGIN_BUILD || resolve(import.meta.dir, '../dist');
const { ClarityPlugin } = await import(pathToFileURL(resolve(outdir, 'opencode.js')).href);

async function transform(system, hooks, input = { sessionID: 'test-session', model: {} }) {
  hooks ??= await ClarityPlugin({});
  const output = { system };
  await hooks['experimental.chat.system.transform'](input, output);
  return output.system;
}

describe('OpenCode communication guidance', () => {
  test('preserves all system blocks and does not duplicate guidance on repeated transforms', async () => {
    const hooks = await ClarityPlugin({});
    const system = ['Base policy', '', 'Available skill: communication-style.'];
    await transform(system, hooks);
    expect(system.slice(0, 3)).toEqual(['Base policy', '', 'Available skill: communication-style.']);
    expect(system).toHaveLength(4);
    expect(system.filter(part => part.includes('<clarity-communication-style '))).toHaveLength(1);
    const once = [...system];
    await transform(system, hooks);
    expect(system).toEqual(once);
  });

  test('reconstructed context is guided independently and input text is retained', async () => {
    const hooks = await ClarityPlugin({});
    const oldSystem = await transform(['Old policy'], hooks);
    const previous = [...oldSystem];
    const next = await transform(['New policy'], hooks);
    expect(oldSystem).toEqual(previous);
    expect(next[0]).toBe('New policy');
    expect(next).not.toContain('Old policy');
    expect(next.filter(part => part.includes('<clarity-communication-style '))).toHaveLength(1);
    const again = [...next];
    await transform(again);
    expect(again).toEqual(next);
  });

  test('inherited guidance remains unchanged inside a merged system block', async () => {
    const original = await transform(['Parent policy']);
    const inherited = [`Child prefix\n${original.join('\n')}\nChild suffix`, 'Final policy'];
    const before = [...inherited];
    await transform(inherited);
    expect(inherited).toEqual(before);
  });

  test('inherited bootstrap survives whitespace normalization without reinsertion', async () => {
    const parent = await transform(['Parent policy']);
    const inherited = parent.map(block => block.replace(/\n/g, '\r\n'));
    const before = [...inherited];
    await transform(inherited);
    expect(inherited).toEqual(before);
  });

});
