---
id: drip_font_ice
slug: drip-font-ice
category: effects
parent: drip_font
tags: ["drip", "kawaii", "cute", "sweet", "ice cream", "appetizing"]
names:
  en: "Ice Cream Drip Font"
  ja: "アイスクリームドリップフォント"
  zh: "冰淇淋滴落字体"
  es: "Letras de Helado Derretido"
  pt: "Fonte de Sorvete Derretido"
  de: "Eis-Tropf-Schrift"
description:
  en: "Chunky letters swirled with pink and cream soft-serve, melting into thick rounded drips over a pastel pink background."
  ja: "ピンクとクリームのソフトクリームが渦巻く厚い文字。丸く太いしずくとなって溶け落ち、背景はパステルピンク。"
  zh: "厚实字母上盘旋着粉色与奶油色软冰淇淋，融化成浓稠的圆润滴落，背景是粉彩粉色。"
  es: "Letras gruesas cubiertas de helado suave rosa y crema en espiral, derritiéndose en gotas espesas y redondeadas sobre un fondo rosa pastel."
  pt: "Letras grossas envoltas em sorvete cremoso rosa e creme em espiral, derretendo em gotas espessas e arredondadas sobre um fundo rosa pastel."
  de: "Dicke Buchstaben, umwunden von rosa und cremefarbenem Softeis, das in dicken, runden Tropfen auf einem pastellrosa Hintergrund schmilzt."
fontvibe_url: https://fontvibe.ai/styles/drip-font-ice
preview_image: https://cos.fontvibe.ai/generations/user/17/481a9fca-4c50-4152-9490-bc0429ed9e4a.jpeg
examples:
  - url: https://fontvibe.ai/gallery/2388
    image: https://cos.fontvibe.ai/generations/user/17/505fc983-37b1-4ecc-b9fd-c61d63962f2c.jpeg
  - url: https://fontvibe.ai/gallery/2387
    image: https://cos.fontvibe.ai/generations/user/17/3b6c1866-4c7d-492d-bb81-b6894679773d.jpeg
  - url: https://fontvibe.ai/gallery/2381
    image: https://cos.fontvibe.ai/generations/user/17/fd11e239-5ad3-4964-97c4-a55c0787986d.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "SWEET"
  image: "https://cos.fontvibe.ai/opensource/text-effect-prompts/drip_font_ice.jpg"
  passed: true
  note: "Pastel ice-cream drip letters; spelled right."
license: CC-BY-4.0
---

# Ice Cream Drip Font

> Chunky letters swirled with pink and cream soft-serve, melting into thick rounded drips over a pastel pink background.

[![Ice Cream Drip Font on FontVibe](https://cos.fontvibe.ai/generations/user/17/481a9fca-4c50-4152-9490-bc0429ed9e4a.jpeg)](https://fontvibe.ai/styles/drip-font-ice)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/drip-font-ice](https://fontvibe.ai/styles/drip-font-ice)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. The letters are bold block letterforms formed from melting soft-serve ice cream, capturing a sweet summer aesthetic. Thick, creamy fluid flows from the bottom of every letter, featuring large rounded cream drops hanging with soft surface tension and slow, viscous trails running downward. The ice cream material exhibits a photorealistic, smooth creamy surface with a delicate, subtle gloss that catches the illumination. A warm pastel color palette defines the letters, presenting a visually delicious look influenced naturally by gravity. The scene features a clean, warm soft pastel background illuminated by gentle, inviting overhead light that highlights the realistic dripping details of each letterform. The text "{{TEXT}}" is the sole legible text in the entire image.
```

Generic-model test (`gemini-2.5-flash-image`, text "SWEET", 2026-10-30):

![test render](https://cos.fontvibe.ai/opensource/text-effect-prompts/drip_font_ice.jpg)

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/505fc983-37b1-4ecc-b9fd-c61d63962f2c.jpeg)](https://fontvibe.ai/gallery/2388) [![example](https://cos.fontvibe.ai/generations/user/17/3b6c1866-4c7d-492d-bb81-b6894679773d.jpeg)](https://fontvibe.ai/gallery/2387) [![example](https://cos.fontvibe.ai/generations/user/17/fd11e239-5ad3-4964-97c4-a55c0787986d.jpeg)](https://fontvibe.ai/gallery/2381)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
rendered in ice cream drip font style. Bold block letterforms dripping with melting soft-serve ice cream — thick creamy fluid flowing from every letter bottom, large rounded cream drops hanging with soft surface tension, slow viscous trails running down each letterform. Photorealistic ice cream texture: smooth creamy surface with subtle gloss, warm pastel color palette. Sweet summer aesthetic, gravity-pulled soft serve, visually delicious. LETTERFORM PRIORITY: when the chosen font carries its own treatment, that font's letterform shapes take priority and own the letters; this style governs the melting soft-serve ice-cream fluid, the creamy drips and the gloss. FALLBACK MATERIAL: if the font carries no material of its own, render the letters as bold block letters dripping melting soft-serve ice cream with large rounded cream drops and slow viscous trails. COLOR PRIORITY: keep the font's own colors if specified; otherwise a warm pastel ice-cream palette.
```

**Scene**

```text
Warm soft pastel background. Gentle overhead light — warm and inviting. Each letter dripping realistically with soft-serve ice cream.
```

## Tips

- Short, punchy words with playful or summer themes work best to allow room for the heavy, dripping fluid effects.
- Specify distinct pastel flavor shades, such as strawberry pink, pistachio green, or vanilla cream, to adjust the color theme.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/drip-font-ice](https://fontvibe.ai/styles/drip-font-ice) — see [Attribution](../../README.md#attribution).
