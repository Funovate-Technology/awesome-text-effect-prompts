'use strict';
/*!
 * text-effect-prompts — AI text-effect prompts from FontVibe.
 * Code: MIT. Prompts and data: CC BY 4.0 — please credit with a link to the
 * style's FontVibe page (see attribution()). https://fontvibe.ai/styles
 */
const path = require('path');

const LANGS = ['en', 'ja', 'zh', 'es', 'pt', 'de'];
const PLACEHOLDER = '{{TEXT}}';

let _index = null;
function index() {
  if (!_index) _index = require(path.join(__dirname, 'data', 'index.json'));
  return _index;
}

function norm(s) {
  return String(s == null ? '' : s).trim().toLowerCase();
}

/* -1 / undefined mean "no limit"; never slice(0, -n). */
function take(arr, limit) {
  if (limit == null || limit < 0) return arr;
  return arr.slice(0, limit);
}

/** Every published style. */
function all() {
  return index().styles;
}

/** Look a style up by id ("neon_glow") or slug ("neon-glow"). */
function get(idOrSlug) {
  const q = norm(idOrSlug);
  return all().find((s) => s.id === q || s.slug === q);
}

/** Category ids that have at least one style, in index order. */
function categories() {
  const seen = [];
  for (const s of all()) if (!seen.includes(s.category)) seen.push(s.category);
  return seen;
}

/** All tags with how many styles carry them, most common first. */
function tags() {
  const m = new Map();
  for (const s of all()) for (const t of s.tags) m.set(t, (m.get(t) || 0) + 1);
  return [...m.entries()].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0])).map(([tag, count]) => ({ tag, count }));
}

/**
 * Filter by category and/or tag.
 * @param {{category?: string, tag?: string, limit?: number}} [opts]
 */
function list(opts) {
  const o = opts || {};
  const cat = o.category ? norm(o.category) : '';
  const tag = o.tag ? norm(o.tag) : '';
  return take(all().filter((s) => (!cat || s.category === cat) && (!tag || s.tags.includes(tag))), o.limit);
}

/**
 * Case-insensitive substring search over id, tags, and names and descriptions
 * in all six languages (or only `lang`). Name and id matches rank first.
 * @param {string} query
 * @param {{lang?: string, category?: string, limit?: number}} [opts]
 */
function search(query, opts) {
  const o = opts || {};
  const q = norm(query);
  if (!q) return [];
  if (o.lang && !LANGS.includes(o.lang)) throw new Error('text-effect-prompts: unknown lang "' + o.lang + '" (use one of ' + LANGS.join(', ') + ')');
  const langs = o.lang ? [o.lang] : LANGS;
  const scored = [];
  for (const s of list({ category: o.category })) {
    let score = 0;
    if (s.id.includes(q) || s.slug.includes(q) || langs.some((l) => norm(s.names[l]).includes(q))) score = 3;
    else if (s.tags.some((t) => t.includes(q))) score = 2;
    else if (langs.some((l) => norm(s.description[l]).includes(q))) score = 1;
    if (score) scored.push([score, s]);
  }
  scored.sort((a, b) => b[0] - a[0]);
  return take(scored.map((x) => x[1]), o.limit);
}

/**
 * The standalone prompt for a style with {{TEXT}} replaced by your words.
 * Throws if the style is unknown or the text is empty.
 */
function prompt(idOrSlug, text) {
  const s = get(idOrSlug);
  if (!s) throw new Error('text-effect-prompts: unknown style "' + idOrSlug + '"');
  const t = String(text == null ? '' : text);
  if (!t.trim()) throw new Error('text-effect-prompts: text must not be empty');
  return s.prompt.split(PLACEHOLDER).join(t);
}

/** Localised name, falling back to English when a translation is missing. */
function name(idOrSlug, lang) {
  const s = get(idOrSlug);
  if (!s) return undefined;
  return (lang && s.names[lang]) || s.names.en;
}

/**
 * A credit line for a style (or the whole collection when id is omitted).
 * @param {string} [idOrSlug]
 * @param {'markdown'|'html'|'text'} [format]
 */
function attribution(idOrSlug, format) {
  const s = idOrSlug ? get(idOrSlug) : null;
  if (idOrSlug && !s) throw new Error('text-effect-prompts: unknown style "' + idOrSlug + '"');
  const url = s ? s.fontvibe_url : 'https://fontvibe.ai/styles';
  const label = s ? s.names.en + ' prompt from FontVibe' : 'Text-effect prompts from FontVibe';
  const lic = 'https://creativecommons.org/licenses/by/4.0/';
  switch (format || 'markdown') {
    case 'html':
      return label.replace('FontVibe', '<a href="' + url + '">FontVibe</a>') + ' · <a href="' + lic + '">CC BY 4.0</a>';
    case 'text':
      return label + ' — ' + url + ' — CC BY 4.0';
    case 'markdown':
      return label.replace('FontVibe', '[FontVibe](' + url + ')') + ' · [CC BY 4.0](' + lic + ')';
    default:
      throw new Error('text-effect-prompts: format must be markdown, html or text');
  }
}

module.exports = {
  LANGS,
  PLACEHOLDER,
  get stats() { return index().stats; },
  all,
  get,
  list,
  search,
  prompt,
  name,
  categories,
  tags,
  attribution,
};
