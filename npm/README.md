# text-effect-prompts

AI text-effect prompts — neon, chrome, liquid glass, ink brush, pixel art, pop art and more — each
with a `{{TEXT}}` placeholder, each **tested on a general image model before inclusion**, with style
names and descriptions in English, Japanese, Chinese, Spanish, Portuguese and German.
From [FontVibe](https://fontvibe.ai/styles). Zero dependencies.

```bash
npm i text-effect-prompts
npx text-effect-prompts neon-glow "OPEN LATE"     # prints the filled-in prompt
npx text-effect-prompts --search ネオン
```

```js
const tep = require('text-effect-prompts')       // or: import tep from 'text-effect-prompts'

tep.prompt('neon-glow', 'OPEN LATE')    // standalone prompt with {{TEXT}} filled in
tep.get('neon_glow')                    // full entry (id or slug)
tep.search('ink', { lang: 'en', limit: 5 })
tep.search('霓虹')                       // searches names/descriptions in all six languages
tep.list({ category: 'effects' })       // effects · aesthetics · text_styles · scenes · occasions
tep.list({ tag: 'neon' })
tep.name('neon-glow', 'ja')             // localised name, English fallback
tep.attribution('neon-glow', 'html')    // credit line linking the style's FontVibe page
tep.stats                               // counts, missing translations, test model
```

Each entry: `id`, `slug`, `category`, `tags`, `names{en,ja,zh,es,pt,de}`,
`description{…}`, `prompt`, `style_layer{core,scene}` (FontVibe's original layer — not a complete
prompt on its own), `fontvibe_url`, `preview_image`, `examples[]`, `test{model,date,text,passed}`.
Types are in `index.d.ts`.

**Results are best on FontVibe.** These prompts carry a style's material, colour, lighting and
scene; on [fontvibe.ai](https://fontvibe.ai/styles) the same style is also paired with a real font,
a font reference image and the model it was tuned on. Keep `{{TEXT}}` short (1–3 words) on general
models.

## License and attribution

- Prompts and data (`data/index.json`): **CC BY 4.0**. Please credit with a link to the style's page,
  e.g. `https://fontvibe.ai/styles/neon-glow` (or `https://fontvibe.ai/styles` for the collection) —
  `rel="nofollow"` is fine. `attribution()` returns a ready-made line.
- Code: **MIT**.

Source, test records and the trademark-screening log:
[github.com/Funovate-Technology/awesome-text-effect-prompts](https://github.com/Funovate-Technology/awesome-text-effect-prompts).
