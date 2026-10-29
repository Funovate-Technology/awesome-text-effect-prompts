---
id: cyberpunk
slug: cyberpunk
category: scenes
tags: ["neon", "cyberpunk", "dark", "glitch", "chromatic aberration", "scanlines", "intense"]
names:
  en: "Cyberpunk"
  ja: "サイバーパンク"
  zh: "赛博朋克 Cyberpunk"
  es: "Cyberpunk"
  pt: "Cyberpunk"
  de: "Cyberpunk"
description:
  en: "Chrome block capitals with magenta and cyan color fringing, horizontal glitch slices and scanlines, glowing over a rainy neon megacity at night."
  ja: "マゼンタとシアンの色ずれ、水平のグリッチスライスと走査線が入ったクロームのブロック体大文字。雨の夜のネオン巨大都市の上で光ります。"
  zh: "铬金属方块大写字母带品红与青色色边，横向故障切片和扫描线，在雨夜霓虹巨型都市上空发光。"
  es: "Mayúsculas de bloque cromadas con franjas de color magenta y cian, cortes glitch horizontales y líneas de escaneo, brillando sobre una megaciudad de neón lluviosa por la noche."
  pt: "Maiúsculas em bloco cromadas com franjas de cor magenta e ciano, cortes glitch horizontais e linhas de varredura, brilhando sobre uma megacidade de neon chuvosa à noite."
  de: "Chrom-Blockversalien mit magenta- und cyanfarbenen Farbsäumen, horizontalen Glitch-Schnitten und Scanlines, leuchtend über einer verregneten Neon-Megastadt bei Nacht."
fontvibe_url: https://fontvibe.ai/styles/cyberpunk
preview_image: https://cos.fontvibe.ai/generations/user/17/dea1ad21-e39b-4b88-8056-e3415c72fdd6.jpeg
examples:
  - url: https://fontvibe.ai/gallery/12039
    image: https://cos.fontvibe.ai/generations/user/17/368db224-fb0a-43c7-a6ec-4f25c780bd25.jpeg
  - url: https://fontvibe.ai/gallery/12048
    image: https://cos.fontvibe.ai/generations/user/17/b4a490b9-d28f-4740-b6b8-8500a5fb1e08.jpeg
  - url: https://fontvibe.ai/gallery/12030
    image: https://cos.fontvibe.ai/generations/user/17/9ab4b113-8864-4600-80c0-8508653f835d.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "CYBER"
  image: ""
  passed: true
  note: "Neon chrome letters with electric glitch in a dark street; spelled right."
license: CC-BY-4.0
---

# Cyberpunk

> Chrome block capitals with magenta and cyan color fringing, horizontal glitch slices and scanlines, glowing over a rainy neon megacity at night.

[![Cyberpunk on FontVibe](https://cos.fontvibe.ai/generations/user/17/dea1ad21-e39b-4b88-8056-e3415c72fdd6.jpeg)](https://fontvibe.ai/styles/cyberpunk)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/cyberpunk](https://fontvibe.ai/styles/cyberpunk)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. The letters are formed from cold chrome, illuminated by a stark blue-white overhead arc light with intense electric cyan and hot magenta neon fill striking from both flanks. Electric cyan-white plasma threads crackle and arc along the outer perimeters of the letterforms. The entire graphic displays heavy digital distortion: pronounced RGB chromatic aberration with cyan shifted left and magenta shifted right, fine horizontal scan-line cuts across all surfaces, and digital glitch slice displacements where horizontal bands are shifted rightward to simulate CRT signal failure. All non-illuminated areas drop into cold blue-tinted shadows, strictly avoiding warm tones. The composition is set in a rain-soaked, tech-noir back alley at night amidst dense atmospheric fog and steam rising from street grates. The wet asphalt below mirrors fractured puddles of cyan and magenta light against a near-black background, with distant, unrecognizable neon blurs kept softly out of focus, ensuring {{TEXT}} remains the only legible text.
```

Tested on `gemini-2.5-flash-image` with the text "CYBER" on 2026-10-30 — passed (legible, correctly spelled, recognisably this style).

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/368db224-fb0a-43c7-a6ec-4f25c780bd25.jpeg)](https://fontvibe.ai/gallery/12039) [![example](https://cos.fontvibe.ai/generations/user/17/b4a490b9-d28f-4740-b6b8-8500a5fb1e08.jpeg)](https://fontvibe.ai/gallery/12048) [![example](https://cos.fontvibe.ai/generations/user/17/9ab4b113-8864-4600-80c0-8508653f835d.jpeg)](https://fontvibe.ai/gallery/12030)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
RGB chromatic aberration: cyan channel offset 4px left, magenta channel offset 4px right, vivid color fringing on all hard edges. Fine horizontal scan-line cuts at 15-20px intervals at 25% opacity crossing all surfaces. Digital glitch slice displacement: 2-3 horizontal bands shifted rightward 6-8px, simulating CRT signal failure. Electric cyan-white plasma threads arcing along character perimeters. Cold ambient fill: blue-tinted shadow zones on all non-illuminated surfaces. Color palette restricted to: electric cyan (#00E5FF), hot magenta (#FF00FF), cold chrome (#C0C0C0), near-black background — no warm tones, no unmotivated gradients. When no specific material is defined by the font: default lighting environment — cold blue-white overhead arc light, cyan and magenta neon fill from both sides, near-black background with subtle atmospheric fog.
```

**Scene**

```text
Set in a rain-soaked neon-lit back alley at night — wet asphalt reflecting fractured cyan and magenta light below, steam venting from grates, blurred neon signs in the extreme background out of focus. Dense atmospheric fog, oppressive tech-noir mood.
```

## Tips

- Short, punchy words or acronyms work best, as they provide broad surfaces for the horizontal glitch bands and scan lines to show through clearly.
- You can vary the mood by adjusting the level of digital corruption, dialing between subtle scan lines or heavily shattered CRT displacement slices.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/cyberpunk](https://fontvibe.ai/styles/cyberpunk) — see [Attribution](../../README.md#attribution).
