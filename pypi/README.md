# text-effect-prompts

**AI text-effect prompts with a `{{TEXT}}` placeholder** — neon, chrome, graffiti, calligraphy,
3D and more — each tested on a general image model, with style names and descriptions in
English, Japanese, Chinese, Spanish, Portuguese and German.

Every prompt comes from a style on **[FontVibe](https://fontvibe.ai/styles)**, where you can try
it on your own words with no prompt writing at all. Results are best there: FontVibe adds font
references and layout on top of the prompt. The full collection, with example images for every
style, lives at **[github.com/Funovate-Technology/awesome-text-effect-prompts](https://github.com/Funovate-Technology/awesome-text-effect-prompts)**.

```bash
pip install text-effect-prompts
text-effect-prompts neon-glow "OPEN 24/7"     # print the prompt with your text filled in
text-effect-prompts --search graffiti         # search names in any of the six languages
text-effect-prompts --list effects            # list a category
```

```python
import text_effect_prompts as tep

tep.prompt("neon-glow", "OPEN 24/7")          # str, ready for your image model
tep.search("书法")                             # names/descriptions in en ja zh es pt de
tep.list_styles(category="effects", limit=5)
tep.attribution("neon-glow")                  # credit line with a link to the style page
```

Same API and data as the npm package [`text-effect-prompts`](https://www.npmjs.com/package/text-effect-prompts).

## Licence and attribution

Code is MIT. Prompts and data are **CC BY 4.0**: if you use them, please credit FontVibe with a
link to the style's page — `attribution(id)` gives you a ready-made line in Markdown, HTML or
plain text. Please link the site, not just the repo; adding `rel="nofollow"` is fine.
