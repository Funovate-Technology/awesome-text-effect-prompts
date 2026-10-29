'use strict';
// Plain-node test. No framework, no dev dependency.
const assert = require('assert');
const p = require('./index.js');

let n = 0;
const t = (name, fn) => { fn(); n++; console.log('  ok  ' + name); };

t('all() matches stats.published', () => {
  assert.ok(p.all().length > 0);
  assert.strictEqual(p.all().length, p.stats.published);
});

t('every style has the documented shape', () => {
  for (const s of p.all()) {
    assert.ok(/^[a-z0-9_]+$/.test(s.id), s.id);
    assert.strictEqual(s.slug, s.id.replace(/_/g, '-'));
    assert.strictEqual(s.fontvibe_url, 'https://fontvibe.ai/styles/' + s.slug);
    assert.ok(s.prompt.includes(p.PLACEHOLDER), s.id + ' prompt has no placeholder');
    assert.ok(s.names.en, s.id + ' has no English name');
    for (const l of p.LANGS) assert.strictEqual(typeof s.names[l], 'string');
    assert.strictEqual(s.test.passed, true);
    assert.ok(s.test.model);
  }
});

t('ids are unique', () => {
  assert.strictEqual(new Set(p.all().map((s) => s.id)).size, p.all().length);
});

t('get() accepts id and slug', () => {
  const s = p.all()[0];
  assert.strictEqual(p.get(s.id), s);
  assert.strictEqual(p.get(s.slug), s);
  assert.strictEqual(p.get(s.slug.toUpperCase()), s);
  assert.strictEqual(p.get('no-such-style'), undefined);
});

t('prompt() fills every placeholder', () => {
  const s = p.all()[0];
  const out = p.prompt(s.slug, 'HELLO $& WORLD');
  assert.ok(!out.includes('{{TEXT}}'));
  assert.ok(out.includes('"HELLO $& WORLD"'), 'special replacement patterns must be literal');
});

t('prompt() rejects unknown style and empty text', () => {
  assert.throws(() => p.prompt('no-such-style', 'x'), /unknown style/);
  assert.throws(() => p.prompt(p.all()[0].id, '  '), /empty/);
});

t('list() filters by category', () => {
  for (const c of p.categories()) {
    const l = p.list({ category: c });
    assert.ok(l.length > 0);
    assert.ok(l.every((s) => s.category === c));
    assert.strictEqual(l.length, p.stats.by_category[c]);
  }
  assert.strictEqual(p.list({ category: 'nope' }).length, 0);
});

t('list() filters by tag and honours limit', () => {
  const top = p.tags()[0];
  assert.strictEqual(p.list({ tag: top.tag }).length, top.count);
  assert.strictEqual(p.list({ limit: 2 }).length, 2);
  assert.strictEqual(p.list({ limit: -1 }).length, p.all().length);
});

t('search() finds English names', () => {
  const s = p.all()[0];
  assert.ok(p.search(s.names.en).includes(s));
});

t('search() finds names in every language that has them', () => {
  for (const l of p.LANGS) {
    const s = p.all().find((x) => x.names[l]);
    if (!s) continue;
    assert.ok(p.search(s.names[l], { lang: l }).includes(s), l);
  }
});

t('search() ranks name matches first and honours limit and category', () => {
  const r = p.search('neon');
  assert.ok(r.length > 0);
  assert.ok(/neon/i.test(r[0].names.en) || r[0].id.includes('neon'));
  assert.strictEqual(p.search('neon', { limit: 1 }).length, 1);
  const cat = r[0].category;
  assert.ok(p.search('neon', { category: cat }).every((s) => s.category === cat));
  assert.deepStrictEqual(p.search(''), []);
  assert.throws(() => p.search('x', { lang: 'fr' }), /unknown lang/);
});

t('name() falls back to English', () => {
  const s = p.all().find((x) => p.LANGS.some((l) => !x.names[l])) || p.all()[0];
  const missing = p.LANGS.find((l) => !s.names[l]);
  if (missing) assert.strictEqual(p.name(s.id, missing), s.names.en);
  assert.strictEqual(p.name(s.id), s.names.en);
});

t('attribution() links the website, not the repo', () => {
  const s = p.all()[0];
  for (const f of ['markdown', 'html', 'text']) {
    const a = p.attribution(s.id, f);
    assert.ok(a.includes(s.fontvibe_url), f);
    assert.ok(!a.includes('github.com'), f);
  }
  assert.ok(p.attribution().includes('https://fontvibe.ai/styles'));
  assert.throws(() => p.attribution(s.id, 'pdf'), /format/);
});

t('ESM entry exposes the same API', () => {
  const src = require('fs').readFileSync(require('path').join(__dirname, 'index.mjs'), 'utf8');
  for (const k of ['all', 'get', 'list', 'search', 'prompt', 'attribution']) assert.ok(src.includes(k), k);
});

console.log('\n' + n + ' tests passed');
