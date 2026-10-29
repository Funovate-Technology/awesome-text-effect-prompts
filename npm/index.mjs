import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const m = require('./index.js');
export const { LANGS, PLACEHOLDER, all, get, list, search, prompt, name, categories, tags, attribution } = m;
export const stats = m.stats;
export default m;
