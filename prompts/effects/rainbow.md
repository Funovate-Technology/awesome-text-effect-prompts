---
id: rainbow
slug: rainbow
category: effects
tags: ["gradient", "fun", "balloon", "glossy", "bold", "cheerful"]
names:
  en: "Rainbow"
  ja: "レインボー"
  zh: "彩虹"
  es: "Arcoíris"
  pt: "Arco-íris"
  de: "Regenbogen"
description:
  en: "Vibrant multi-color rainbow gradient text effects with smooth color transitions, prismatic light and joyful chromatic typography."
  ja: "鮮やかな多色レインボーグラデーションの文字エフェクトです。滑らかな色の移り変わり、プリズムのような光、そして陽気で色彩豊かなタイポグラフィが特徴です。"
  zh: "绚丽的多彩虹色渐变文字特效，色彩过渡顺滑，棱镜般的光泽与欢快的多彩排版。"
  es: "Efectos de texto con degradado arcoíris multicolor y vibrante, con transiciones de color suaves, luz prismática y tipografía cromática llena de alegría."
  pt: "Efeitos de texto com degradê arco-íris multicolorido e vibrante, transições de cor suaves, luz prismática e tipografia cromática cheia de alegria."
  de: "Lebhafte, mehrfarbige Regenbogen-Farbverlaufs-Texteffekte mit sanften Farbübergängen und prismatischem Licht – eine bunte Schrift voller Freude und chromatischer Tiefe."
fontvibe_url: https://fontvibe.ai/styles/rainbow
preview_image: https://cos.fontvibe.ai/generations/user/17/04c70c44-8999-4337-8eea-f2de3c3da070.jpeg
examples:
  - url: https://fontvibe.ai/gallery/11375
    image: https://cos.fontvibe.ai/generations/user/17/d4c25f1e-d5a2-422e-8193-032277a895de.jpeg
  - url: https://fontvibe.ai/gallery/11381
    image: https://cos.fontvibe.ai/generations/user/17/74956f5b-9f32-4de1-b048-a4beb0f8734b.jpeg
  - url: https://fontvibe.ai/gallery/11377
    image: https://cos.fontvibe.ai/generations/user/17/15be1424-d15e-43b9-ba9a-217054050575.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "COLOR"
  image: ""
  passed: true
  note: "Rainbow-striped letters with confetti; spelled right."
license: CC-BY-4.0
---

# Rainbow

> Vibrant multi-color rainbow gradient text effects with smooth color transitions, prismatic light and joyful chromatic typography.

[![Rainbow on FontVibe](https://cos.fontvibe.ai/generations/user/17/04c70c44-8999-4337-8eea-f2de3c3da070.jpeg)](https://fontvibe.ai/styles/rainbow)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/rainbow](https://fontvibe.ai/styles/rainbow)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. Clean, bold letters form {{TEXT}}, which is the only legible text in the image. Each individual letter contains a complete top-to-bottom ROYGBIV rainbow gradient entirely within itself: vibrant red at the top, orange in the upper section, yellow-green in the middle, blue-indigo across the lower portion, and deep violet at the bottom. The colors are rendered at full chroma Pride-flag saturation, vivid and unmuted, ensuring every letter independently showcases its own complete vertical spectrum rather than spreading across the entire word. Strong directional sunlight strikes the letters from the upper-right, producing sharp specular highlights across their smooth surfaces. The background depicts a vibrant outdoor festival scene beneath a deep sky gradient shifting from warm amber-orange at the horizon to rich cobalt blue overhead. Soft bokeh orbs of floating festival lights in pink, yellow, cyan, and violet drift through the mid-air, complemented by a faint scatter of colorful confetti drifting below the letters.
```

Tested on `gemini-2.5-flash-image` with the text "COLOR" on 2026-10-30 — passed (legible, correctly spelled, recognisably this style).

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/d4c25f1e-d5a2-422e-8193-032277a895de.jpeg)](https://fontvibe.ai/gallery/11375) [![example](https://cos.fontvibe.ai/generations/user/17/74956f5b-9f32-4de1-b048-a4beb0f8734b.jpeg)](https://fontvibe.ai/gallery/11381) [![example](https://cos.fontvibe.ai/generations/user/17/15be1424-d15e-43b9-ba9a-217054050575.jpeg)](https://fontvibe.ai/gallery/11377)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
rendered as rainbow text effect — COLOR (mandatory): each individual letter must contain a complete ROYGBIV rainbow gradient top-to-bottom within itself — top=red, upper=orange, mid=yellow-green, lower=blue-indigo, bottom=violet. NOT one color per letter. NOT a gradient across the whole word. Every letter is its own complete rainbow. Full chroma Pride flag saturation — not pastel, not muted, not shifted to any single hue. LETTERFORM PRIORITY: when the chosen font carries its own treatment, that font's letterform shapes take priority and own the letters; this style always governs the color — every letter still carries its own complete top-to-bottom ROYGBIV rainbow gradient. FALLBACK MATERIAL: if the font carries no material of its own, render clean bold letters each filled with a full vertical ROYGBIV rainbow. COLOR PRIORITY: the rainbow gradient is mandatory and overrides any single font color — each individual letter is its own complete rainbow at full Pride-flag saturation.
```

**Scene**

```text
Background: vibrant outdoor festival scene — deep gradient sky from warm amber-orange at horizon to rich cobalt blue at top, soft bokeh of colorful light orbs (pink, yellow, cyan, violet) floating in mid-air suggesting festival lights or confetti. Strong directional sunlight from upper-right creating sharp specular highlights on letter surfaces. Faint colorful confetti scatter below the letters. The overall scene feels like a summer Pride festival or birthday celebration — never a plain white or studio background.
```

## Tips

- Short, uplifting words or celebratory greetings work best to allow each letter's full vertical rainbow gradient to remain clear and readable.
- To shift the mood, try altering the time of day in the festival scene, such as twilight or night, to make the bokeh orbs and specular highlights pop even more.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/rainbow](https://fontvibe.ai/styles/rainbow) — see [Attribution](../../README.md#attribution).
