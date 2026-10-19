import { describe, expect, test } from 'bun:test';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

const outdir = process.env.CLARITY_PLUGIN_BUILD || resolve(import.meta.dir, '../dist');
const { default: clarity } = await import(pathToFileURL(resolve(outdir, 'omp.js')).href);

// Substitute only hook registration; invoke the bundled adapter with native string[] policy.
function createPreparation() {
  let handler;
  clarity({ on(event, callback) { if (event === 'before_agent_start') handler = callback; } });
  return async systemPrompt => {
    const event = Object.freeze({
      type: 'before_agent_start',
      prompt: 'Hello',
      images: Object.freeze([]),
      systemPrompt,
    });
    const result = await handler(event, {});
    return result?.systemPrompt ?? systemPrompt;
  };
}

describe('OMP communication guidance', () => {
  test('preserves native policy blocks despite a skill listing', async () => {
    const prepare = createPreparation();
    const base = Object.freeze([
      'Base policy. Available skill: communication-style.',
      '<project-context>Repository policy and workstation data.</project-context>',
    ]);
    const first = await prepare(base);
    expect(first.slice(0, base.length)).toEqual(base);
    expect(first).toHaveLength(base.length + 1);
    expect(first.join('\n').match(/<clarity-communication-style(?:\s|>)/g)).toHaveLength(1);
    expect(await prepare(first)).toBe(first);
    expect(await prepare(base)).toEqual(first);
  });

  test('the same registration guides a rebuilt base without retaining stale policy', async () => {
    const prepare = createPreparation();
    await prepare(['Old policy', '<project-context>Old directory</project-context>']);
    const base = Object.freeze(['New policy', '<project-context>New directory</project-context>']);
    const next = await prepare(base);
    expect(next.slice(0, base.length)).toEqual(base);
    expect(next.join('\n')).not.toContain('Old policy');
    expect(next.join('\n')).not.toContain('Old directory');
    expect(next.join('\n').match(/<clarity-communication-style(?:\s|>)/g)).toHaveLength(1);
    expect(await prepare(next)).toBe(next);
  });

  test('a fresh child registration preserves inherited guidance and assignment blocks', async () => {
    const parentPolicy = await createPreparation()(['Parent policy']);
    const inherited = Object.freeze([...parentPolicy, 'Child role and assignment']);
    const childPolicy = await createPreparation()(inherited);
    expect(childPolicy).toBe(inherited);
    expect(childPolicy.at(-1)).toBe('Child role and assignment');
    expect(childPolicy.join('\n').match(/<clarity-communication-style(?:\s|>)/g)).toHaveLength(1);
  });

  test('inherited guidance embedded in a combined policy block remains unchanged', async () => {
    const guided = await createPreparation()(['Base policy']);
    const inherited = Object.freeze([guided.join('\n\n') + '\n\nChild policy']);
    expect(await createPreparation()(inherited)).toBe(inherited);
  });

  test('inherited bootstrap survives whitespace normalization without reinsertion', async () => {
    const parent = await createPreparation()(['Parent policy']);
    const inherited = Object.freeze(parent.map(block => block.replace(/\n/g, '\r\n')));
    expect(await createPreparation()(inherited)).toBe(inherited);
  });

});
