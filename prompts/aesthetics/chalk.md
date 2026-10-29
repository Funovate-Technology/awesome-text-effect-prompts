---
id: chalk
slug: chalk
category: aesthetics
tags: ["handwritten", "rustic", "chalk", "handmade", "warm", "cozy"]
names:
  en: "Chalk"
  ja: "チョーク"
  zh: "粉笔"
  es: "Tiza"
  pt: "Giz"
  de: "Kreide"
description:
  en: "Hand-lettered cream chalk on a dark slate board: mixed script and serif lines, flourishes and small doodles, soft chalk-dust edges under warm café lighting."
  ja: "暗いスレート板に描いたクリーム色のチョーク手描き文字。筆記体とセリフ体の組み合わせに飾り線と小さな落書き、粉っぽい柔らかな輪郭、温かなカフェの照明。"
  zh: "深色石板上的奶油色粉笔手写字：手写体与衬线混排，配花饰和小涂鸦，粉笔边缘柔和带粉尘，暖调咖啡馆灯光。"
  es: "Rotulación a mano con tiza crema sobre una pizarra oscura: líneas en script y serifa mezcladas, adornos y pequeños dibujos, bordes suaves con polvo de tiza bajo una cálida luz de cafetería."
  pt: "Letreiramento à mão em giz creme numa lousa escura: linhas em script e serifa misturadas, floreios e pequenos desenhos, bordas suaves com pó de giz sob a luz quente de um café."
  de: "Handgeschriebene cremefarbene Kreideschrift auf dunkler Schiefertafel: Schreibschrift und Serifen gemischt, Schnörkel und kleine Zeichnungen, weiche Kreidestaubkanten im warmen Café-Licht."
fontvibe_url: https://fontvibe.ai/styles/chalk
preview_image: https://cos.fontvibe.ai/generations/user/17/91803a7c-c779-40e4-b937-b492139cbf8a.jpeg
examples:
  - url: https://fontvibe.ai/gallery/13518
    image: https://cos.fontvibe.ai/generations/user/17/67fa7fb9-797b-4743-a1fe-15d09b4c0da5.jpeg
  - url: https://fontvibe.ai/gallery/13487
    image: https://cos.fontvibe.ai/generations/user/17/38ebdafd-8cdd-4051-97df-627ee47468eb.jpeg
  - url: https://fontvibe.ai/gallery/13482
    image: https://cos.fontvibe.ai/generations/user/17/4b7a1b00-d02d-424a-86a3-f2e2924a0a25.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "SPECIAL"
  image: "https://cos.fontvibe.ai/opensource/text-effect-prompts/chalk.jpg"
  passed: true
  note: "Chalk lettering with flourishes on a framed blackboard; spelled right."
license: CC-BY-4.0
---

# Chalk

> Hand-lettered cream chalk on a dark slate board: mixed script and serif lines, flourishes and small doodles, soft chalk-dust edges under warm café lighting.

[![Chalk on FontVibe](https://cos.fontvibe.ai/generations/user/17/91803a7c-c779-40e4-b937-b492139cbf8a.jpeg)](https://fontvibe.ai/styles/chalk)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/chalk](https://fontvibe.ai/styles/chalk)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. The letters are artisan hand-drawn in textured chalk with cream-white to warm ivory tones, exhibiting a soft, matte, powdery quality. Delicate dusty pastel accents in soft coral, sage, lavender, and warm mustard appear alongside simple hand-drawn chalk embellishments such as borders of dots, dashes, or small decorative leaves and stars. The letters are set against an authentic deep chalkboard green-black or charcoal slate surface, which functions as an active dark ground showing subtle texture within a wooden frame. {{TEXT}} fills the frame, positioned large and centered, ensuring it remains the only legible text in the composition. Overhead warm ambient lighting illuminates the scene from above at a low angle, evoking the cozy glow of morning light through a cafe window or a vintage filament bulb over a specials board. This gentle directional light reveals powdery chalk marks and surface depth without harsh contrast, accompanied by a faint hint of a warm interior at the outer frame edges.
```

Generic-model test (`gemini-2.5-flash-image`, text "SPECIAL", 2026-10-30):

![test render](https://cos.fontvibe.ai/opensource/text-effect-prompts/chalk.jpg)

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/67fa7fb9-797b-4743-a1fe-15d09b4c0da5.jpeg)](https://fontvibe.ai/gallery/13518) [![example](https://cos.fontvibe.ai/generations/user/17/38ebdafd-8cdd-4051-97df-627ee47468eb.jpeg)](https://fontvibe.ai/gallery/13487) [![example](https://cos.fontvibe.ai/generations/user/17/4b7a1b00-d02d-424a-86a3-f2e2924a0a25.jpeg)](https://fontvibe.ai/gallery/13482)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
Chalkboard aesthetic — the visual language of artisan hand-lettering on dark board surfaces.

COLOR CLIMATE: high-contrast warmth defines the palette. Foreground marks: cream-white to warm ivory as the primary tone, with dusty pastel accents — soft coral, sage, lavender, warm mustard — for secondary decorative elements. Background ground: deep chalkboard green-black or charcoal slate. The dark ground is an active compositional element, not neutral filler.

LIGHT ATMOSPHERE: warm overhead ambient at cafe or classroom intensity — the quality of morning light through a cafe window or an evening vintage filament bulb above a pub specials board. Soft directional quality, revealing surface and dimension without creating harsh contrast. Warm, inviting, crafted.

DECORATIVE REGISTER: simple hand-drawn borders of dots, dashes, or double-ruled lines; small illustrative accents (arrows, stars, leaves, dividers); mixed-weight lettering styles on the same surface — all belong to the chalk aesthetic vocabulary and may appear in compositions.

When no specific material is defined by the font: default lighting environment — warm overhead ambient, cream-white chalk tones against deep chalkboard green-black board ground, soft and matte in quality.
```

**Scene**

```text
Text fills the frame, large and centered against a dark slate chalkboard surface within a wooden frame. Overhead light from above at a low angle. A hint of warm interior visible at the very edges of frame.
```

## Tips

- Short phrases, culinary words, cafe specials, or warm artisanal slogans naturally fit this chalkboard look.
- Swap the background between classic deep chalkboard green and dark charcoal slate to instantly change the atmosphere.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/chalk](https://fontvibe.ai/styles/chalk) — see [Attribution](../../README.md#attribution).
