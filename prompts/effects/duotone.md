---
id: duotone
slug: duotone
category: effects
tags: ["modern", "heavy", "halftone", "shadow", "bold", "striking"]
names:
  en: "Duotone"
  ja: "デュオトーン"
  zh: "Duotone 双色调"
  es: "Duotone"
  pt: "Duotone"
  de: "Duotone"
description:
  en: "Bold condensed slab capitals in one bright color with a halftone dot texture and a solid offset shadow in a second color, on a flat contrasting ground."
  ja: "太く縦長のスラブセリフ大文字。片方の明るい色にハーフトーンの網点、もう一色でずらしたベタの影。対照的な色のフラットな地に。"
  zh: "粗壮窄长的板衬线大写字母，一种亮色带半调网点纹理，另一种颜色做实心错位阴影，置于对比色平涂底上。"
  es: "Mayúsculas slab condensadas y gruesas en un color vivo con textura de semitono y una sombra sólida desplazada en un segundo color, sobre un fondo plano de contraste."
  pt: "Maiúsculas slab condensadas e grossas numa cor viva com textura de meio-tom e uma sombra sólida deslocada numa segunda cor, sobre um fundo chapado contrastante."
  de: "Kräftige, schmale Slab-Versalien in einer leuchtenden Farbe mit Rasterpunkt-Textur und einem versetzten Vollschatten in einer zweiten Farbe, auf einem flachen Kontrastgrund."
fontvibe_url: https://fontvibe.ai/styles/duotone
preview_image: https://cos.fontvibe.ai/generations/user/17/9b28045c-3443-42f8-b84c-9c5eb03f95d2.jpeg
examples:
  - url: https://fontvibe.ai/gallery/372
    image: https://cos.fontvibe.ai/generations/user/17/79e5e517-58d3-4d9b-a18f-a1c356a83555.jpeg
  - url: https://fontvibe.ai/gallery/1503
    image: https://cos.fontvibe.ai/generations/user/17/df528ea08f7548fe87354e89ccb31b95.jpeg
  - url: https://fontvibe.ai/gallery/1020
    image: https://cos.fontvibe.ai/generations/user/17/3ae7d2d9-421e-4f5a-9414-444be0b4b332.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "DUOTONE"
  image: ""
  passed: true
  note: "Two-colour red/navy halftone letters; spelled right."
license: CC-BY-4.0
---

# Duotone

> Bold condensed slab capitals in one bright color with a halftone dot texture and a solid offset shadow in a second color, on a flat contrasting ground.

[![Duotone on FontVibe](https://cos.fontvibe.ai/generations/user/17/9b28045c-3443-42f8-b84c-9c5eb03f95d2.jpeg)](https://fontvibe.ai/styles/duotone)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/duotone](https://fontvibe.ai/styles/duotone)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. The lettering is rendered in a striking, punchy duotone treatment with a graphic print aesthetic. A dominant, flat bright color covers the face of the letters, while a deep contrasting tone fills a crisp, hard-edged offset drop shadow. A visible halftone screen-dot pattern overlays the dominant color, lending texture and depth without sacrificing sharp outlines. The palette consists strictly of a high-contrast two-color pair, such as vibrant vermillion red paired with deep midnight navy, remaining completely flat, saturated, and bold with no soft gradients or muddy transitions. The text is set against a clean, flat two-tone poster ground complemented by subtle geometric or halftone accents that reinforce the high-contrast graphic energy. Ensure {{TEXT}} is the only legible text in the entire image, commanding the composition with crisp print-like impact.
```

Tested on `gemini-2.5-flash-image` with the text "DUOTONE" on 2026-10-30 — passed (legible, correctly spelled, recognisably this style).

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/79e5e517-58d3-4d9b-a18f-a1c356a83555.jpeg)](https://fontvibe.ai/gallery/372) [![example](https://cos.fontvibe.ai/generations/user/17/df528ea08f7548fe87354e89ccb31b95.jpeg)](https://fontvibe.ai/gallery/1503) [![example](https://cos.fontvibe.ai/generations/user/17/3ae7d2d9-421e-4f5a-9414-444be0b4b332.jpeg)](https://fontvibe.ai/gallery/1020)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
a bold duotone piece — graphic, punchy and print-like. SURFACE / STYLE: the lettering is rendered in a striking two-color treatment — one bright color dominating the letter face, a second deep contrasting color filling the drop shadow, bevel inset or offset layer — with a visible halftone screen-dot pattern in the dominant color and a crisp hard-edged graphic finish. SCENE ATMOSPHERE: a flat bold poster setting — clean two-tone ground, simple geometric or halftone accents, high-contrast graphic energy. PALETTE: any high-contrast two-color pair — vermillion red + midnight navy, electric blue + hot pink, black + bright accent — flat, saturated and bold, never gradient-soft or muddy. LETTERFORM PRIORITY: when the chosen font carries its own treatment (retro or Clarendon slab, condensed or geo sans, halftone comic, 3D shadow, sticker outline), that font's letterform takes priority and owns the letters; this style governs the two-color split, the halftone dots and the graphic poster finish. FALLBACK MATERIAL: if the font carries no material of its own, render the letters in a bold duotone — bright face with a deep contrasting offset shadow and a halftone dot pattern — so the punchy two-color graphic always reads.
```

**Scene**

```text
The text sits bold and graphic in a two-color duotone — a bright face with a deep contrasting offset shadow and a visible halftone dot pattern — on a clean flat two-tone ground with high-contrast poster energy. Punchy, graphic, print-style mood.
```

## Tips

- Short, punchy words or acronyms work best with this style to maximize the bold, poster-like graphic impact.
- You can easily change the entire mood by swapping the two-color pair, such as using electric blue and hot pink instead of red and navy.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/duotone](https://fontvibe.ai/styles/duotone) — see [Attribution](../../README.md#attribution).
