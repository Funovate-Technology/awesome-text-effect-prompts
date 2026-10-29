---
id: emboss
slug: emboss
category: effects
tags: ["emboss", "paper", "letterpress", "classic", "minimal", "refined", "elegant"]
names:
  en: "Embossed"
  ja: "エンボス"
  zh: "浮雕压印"
  es: "Relieve"
  pt: "Relevo"
  de: "Geprägt"
description:
  en: "Serif capitals blind-embossed into ivory cotton paper: no ink, only a raised relief with a crisp highlight ridge and soft shadow from low raking light."
  ja: "アイボリーのコットン紙に空押ししたセリフ体大文字。インクはなく、低い斜光が浮き上がった凹凸のくっきりした稜線と柔らかな影だけを描きます。"
  zh: "衬线大写字母盲压在象牙白棉纸上：不着墨，只有凸起的浮雕，低角度斜光勾出清晰的高光脊与柔和阴影。"
  es: "Mayúsculas con serifa estampadas en seco sobre papel de algodón marfil: sin tinta, solo un relieve con una arista de luz nítida y una sombra suave bajo luz rasante."
  pt: "Maiúsculas serifadas gravadas em relevo seco sobre papel de algodão marfim: sem tinta, apenas um relevo com aresta de luz nítida e sombra suave sob luz rasante baixa."
  de: "Serifenversalien blind in elfenbeinfarbenes Baumwollpapier geprägt: keine Tinte, nur ein Relief mit klarer Lichtkante und weichem Schatten im flachen Streiflicht."
fontvibe_url: https://fontvibe.ai/styles/emboss
preview_image: https://cos.fontvibe.ai/generations/user/17/4cfa112b-122d-448e-a3b5-6cf953ff9763.jpeg
examples:
  - url: https://fontvibe.ai/gallery/12419
    image: https://cos.fontvibe.ai/generations/user/17/f98d8970-83c2-478e-b2a7-51363a905e05.jpeg
  - url: https://fontvibe.ai/gallery/12416
    image: https://cos.fontvibe.ai/generations/user/17/19c37cfb-5e09-4de1-8a47-84ca1f1fb6ec.jpeg
  - url: https://fontvibe.ai/gallery/12432
    image: https://cos.fontvibe.ai/generations/user/17/7794ca82-a0bb-4236-8b03-72c521451b0e.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "PRESS"
  image: ""
  passed: true
  note: "Blind-embossed letters on paper; spelled right."
license: CC-BY-4.0
---

# Embossed

> Serif capitals blind-embossed into ivory cotton paper: no ink, only a raised relief with a crisp highlight ridge and soft shadow from low raking light.

[![Embossed on FontVibe](https://cos.fontvibe.ai/generations/user/17/4cfa112b-122d-448e-a3b5-6cf953ff9763.jpeg)](https://fontvibe.ai/styles/emboss)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/emboss](https://fontvibe.ai/styles/emboss)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. The letters are rendered as a clean, dimensional blind-embossed relief raised directly from a surface of premium paper or card stock. Fine paper fibers are subtly visible around the letter edges where the raised topology meets the flat surrounding surface. Warm raking light shines from the upper-left at a low angle across the composition to emphasize the relief, creating a crisp highlight ridge along the top edge of each letter and a soft shadow on the opposite, lee side. No color is added; tonal contrast and dimensional depth serve as the primary visual language, preserving a uniform natural paper tone across the entire piece. There are no gradients on the letter faces, no glowing effects, and no outline strokes, creating a minimal, elegant stationery aesthetic defined by tactile paper texture catching the side lighting.
```

Tested on `gemini-2.5-flash-image` with the text "PRESS" on 2026-10-30 — passed (legible, correctly spelled, recognisably this style).

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/f98d8970-83c2-478e-b2a7-51363a905e05.jpeg)](https://fontvibe.ai/gallery/12419) [![example](https://cos.fontvibe.ai/generations/user/17/19c37cfb-5e09-4de1-8a47-84ca1f1fb6ec.jpeg)](https://fontvibe.ai/gallery/12416) [![example](https://cos.fontvibe.ai/generations/user/17/7794ca82-a0bb-4236-8b03-72c521451b0e.jpeg)](https://fontvibe.ai/gallery/12432)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
Fine paper fibers visible around letter edges where the relief meets the flat surface. Raking light from upper-left at a low angle reveals the raised topology: crisp highlight ridge along the top edge of each letter, soft shadow on the opposite side. No color added — tonal contrast is the only visual language. No gradients on letter faces, no glow, no outline strokes. LETTERFORM PRIORITY: when the chosen font carries its own treatment, that font's letterform shapes take priority and own the letters, rendered as raised relief; this style governs the embossed topology and the raking light. FALLBACK MATERIAL: if the font carries no material of its own, render the letters as a clean blind-embossed relief raised from premium paper, read only through raking-light highlight and shadow. COLOR PRIORITY: emboss adds no color of its own — keep the surface tonal; if the font specifies a color render it as a subtle tinted relief, otherwise natural paper tone.
```

**Scene**

```text
Warm side lighting raking across a premium paper or card surface to emphasize the dimensional relief, fine paper-fiber texture catching the light, a soft shadow on the lee side of each letter. Minimal, elegant stationery aesthetic.
```

## Tips

- Short words, single names, or minimalist monograms work best, giving the delicate highlights and shadows enough space to stand out.
- To subtly alter the mood, specify a particular paper tone such as warm ivory, soft cream, or pure white cotton cardstock.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/emboss](https://fontvibe.ai/styles/emboss) — see [Attribution](../../README.md#attribution).
