---
id: ice_crystal
slug: ice-crystal
category: effects
tags: ["ice", "spiky", "crystal", "glow", "cold", "magical"]
names:
  en: "Ice Crystal"
  ja: "アイスクリスタル"
  zh: "冰晶"
  es: "Cristal de Hielo"
  pt: "Cristal de Gelo"
  de: "Eiskristall"
description:
  en: "Translucent ice-crystal capitals with spiky frost feathering along every edge, glowing under icy blue backlight with drifting snow dust."
  ja: "すべての縁にとげのような霜の羽が伸びる半透明の氷の結晶の大文字。氷のような青い逆光で輝き、雪の粉が舞います。"
  zh: "半透明的冰晶大写字母，每道边缘都长着尖刺状霜花，冰蓝色逆光下发光，四周飘着雪尘。"
  es: "Mayúsculas translúcidas de cristal de hielo con plumas de escarcha puntiagudas en cada borde, brillando bajo una contraluz azul helada con polvo de nieve."
  pt: "Maiúsculas translúcidas de cristal de gelo com plumas de geada pontiagudas em cada borda, brilhando sob uma contraluz azul gelada com pó de neve."
  de: "Durchscheinende Eiskristall-Versalien mit stacheligen Raureiffedern an jeder Kante, leuchtend im eisblauen Gegenlicht mit treibendem Schneestaub."
fontvibe_url: https://fontvibe.ai/styles/ice-crystal
preview_image: https://cos.fontvibe.ai/generations/user/17/0b3bf19f-6d6d-44a0-93b7-addb831e20ac.jpeg
examples:
  - url: https://fontvibe.ai/gallery/263
    image: https://cos.fontvibe.ai/generations/user/17/266697e3-bc9f-492e-9496-b938c7bcfecf.jpeg
  - url: https://fontvibe.ai/gallery/262
    image: https://cos.fontvibe.ai/generations/user/17/8d293fce-4d3f-4251-a4dd-835a900030ae.jpeg
  - url: https://fontvibe.ai/gallery/261
    image: https://cos.fontvibe.ai/generations/user/17/faacefcd-0250-4d96-abfc-82d1aef8558a.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "FROZEN"
  image: "https://cos.fontvibe.ai/opensource/text-effect-prompts/ice_crystal.jpg"
  passed: true
  note: "Spiky ice-crystal letters; spelled right."
license: CC-BY-4.0
---

# Ice Crystal

> Translucent ice-crystal capitals with spiky frost feathering along every edge, glowing under icy blue backlight with drifting snow dust.

[![Ice Crystal on FontVibe](https://cos.fontvibe.ai/generations/user/17/0b3bf19f-6d6d-44a0-93b7-addb831e20ac.jpeg)](https://fontvibe.ai/styles/ice-crystal)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/ice-crystal](https://fontvibe.ai/styles/ice-crystal)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. The lettering is formed entirely from clear crystalline ice with delicate frost feathering like frozen fern leaves spreading outward from the edges. The letters have a glassy frozen surface that is transparent and naturally refracts light, embedded with tiny suspended ice particles. Set the piece in a cold winter atmosphere filled with drifting frost and fine snow dust. Illuminate the text with a dramatic icy blue backlight and crisp rim lighting that catches and defines the sharp crystal facets. The color palette is strictly cool, luminous, and never warm, dominated by ice blue, cyan, frost white, and pale teal with bright, gleaming highlights.
```

Generic-model test (`gemini-2.5-flash-image`, text "FROZEN", 2026-10-30):

![test render](https://cos.fontvibe.ai/opensource/text-effect-prompts/ice_crystal.jpg)

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/266697e3-bc9f-492e-9496-b938c7bcfecf.jpeg)](https://fontvibe.ai/gallery/263) [![example](https://cos.fontvibe.ai/generations/user/17/8d293fce-4d3f-4251-a4dd-835a900030ae.jpeg)](https://fontvibe.ai/gallery/262) [![example](https://cos.fontvibe.ai/generations/user/17/faacefcd-0250-4d96-abfc-82d1aef8558a.jpeg)](https://fontvibe.ai/gallery/261)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
a frozen ice-crystal piece — cold, crystalline and luminous. SURFACE / STYLE: the lettering is formed from clear crystalline ice with frost feathering like frozen fern leaves spreading from the edges, transparent ice refracting light, tiny suspended ice particles and a glassy frozen surface. SCENE ATMOSPHERE: a cold winter setting — icy blue backlight, drifting frost and snow dust, dramatic rim light catching the crystal edges. PALETTE: cool blue-white — ice blue, cyan, frost white and pale teal with crisp highlights — cold and luminous, never warm. LETTERFORM PRIORITY: when the chosen font carries its own treatment (ice crystal, ice shard, 3D ice, frost display, ice drip, clear glass), that font's letterform takes priority and owns the letters; this style governs the crystalline ice material, the frost feathering, the cool backlight and the blue-white palette. FALLBACK MATERIAL: if the font carries no material of its own, render the letters as clear crystalline ice with frost feathering at the edges, refraction and a cold blue rim light, so the frozen ice feel always reads.
```

**Scene**

```text
The text sits clear and crystalline as frozen ice, frost feathering like fern leaves spreading from the edges, suspended ice particles in cold air, dramatic icy blue backlight catching the crystal edges. Cold, luminous, frozen winter mood.
```

## Tips

- Short, punchy words related to winter, cold, or clarity emphasize the sharp crystalline facets best.
- Adjust the amount of drifting frost and snow dust in the background to make the scene feel either like a calm deep freeze or a dynamic blizzard.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/ice-crystal](https://fontvibe.ai/styles/ice-crystal) — see [Attribution](../../README.md#attribution).
