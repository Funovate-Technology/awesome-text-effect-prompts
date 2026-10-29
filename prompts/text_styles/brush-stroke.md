---
id: brush_stroke
slug: brush-stroke
category: text_styles
tags: ["ink", "expressive", "flowing", "brush", "script", "handmade", "elegant", "high contrast"]
names:
  en: "Brush Script"
  ja: "ブラッシュスクリプト"
  zh: "毛笔书法"
  es: "Letras de Pincel"
  pt: "Letras de Pincel"
  de: "Pinselschrift"
description:
  en: "Western brush script with connected letters: thick pressure downstrokes, hairline upstrokes, visible bristle streaks and dry-brush trails in warm off-black ink on textured paper."
  ja: "文字がつながる西洋の筆記体。筆圧の強い太い下ろし、髪の毛ほど細い上げ、筆の毛の筋とかすれを、温かみのある黒インクで質感のある紙に。"
  zh: "西式毛笔连写体：下笔重压粗、上挑细如发丝，可见笔毛纹理和枯笔拖尾，暖黑墨色落在纹理纸上。"
  es: "Script de pincel occidental con letras enlazadas: trazos descendentes gruesos por presión, ascendentes finísimos, vetas visibles de las cerdas y rastros de pincel seco en tinta negra cálida sobre papel texturizado."
  pt: "Script de pincel ocidental com letras ligadas: traços descendentes grossos pela pressão, ascendentes finíssimos, marcas visíveis das cerdas e rastros de pincel seco em tinta preta quente sobre papel texturizado."
  de: "Westliche Pinselschrift mit verbundenen Buchstaben: kräftige Abstriche durch Druck, haarfeine Aufstriche, sichtbare Borstenspuren und Trockenpinsel-Ausläufe in warmer schwarzer Tinte auf strukturiertem Papier."
fontvibe_url: https://fontvibe.ai/styles/brush-stroke
preview_image: https://cos.fontvibe.ai/generations/user/17/f5d3a32a-fad6-4e40-bba3-fbf9b2decd9a.jpeg
examples:
  - url: https://fontvibe.ai/gallery/9056
    image: https://cos.fontvibe.ai/generations/user/17/178926dc-7288-4562-8dbe-a3880e47fa0f.jpeg
  - url: https://fontvibe.ai/gallery/9079
    image: https://cos.fontvibe.ai/generations/user/17/c3d4495f-beab-4585-828e-d820d099c000.jpeg
  - url: https://fontvibe.ai/gallery/9068
    image: https://cos.fontvibe.ai/generations/user/17/84eff457-46e1-4628-a1ca-6597eca892ef.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "Script"
  image: "https://cos.fontvibe.ai/opensource/text-effect-prompts/brush_stroke.jpg"
  passed: true
  note: "Brush script on warm paper; spelled right."
license: CC-BY-4.0
---

# Brush Script

> Western brush script with connected letters: thick pressure downstrokes, hairline upstrokes, visible bristle streaks and dry-brush trails in warm off-black ink on textured paper.

[![Brush Script on FontVibe](https://cos.fontvibe.ai/generations/user/17/f5d3a32a-fad6-4e40-bba3-fbf9b2decd9a.jpeg)](https://fontvibe.ai/styles/brush-stroke)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/brush-stroke](https://fontvibe.ai/styles/brush-stroke)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. The letters are rendered as expressive Western brush script lettering with fluid connected strokes, showing visible bristle texture and authentic thick-to-thin pressure variation, with thick downstrokes and thin upstrokes reminiscent of a loaded calligraphy brush. The warm off-black ink appears slightly wet and glistening, featuring natural ink pooling at stroke beginnings and feathered dry-brush trails at stroke ends, capturing a hand-crafted artisan energy with realistic brush imperfections. The words {{TEXT}} are the only legible text in the image. The lettering is set against warm cream textured paper under soft diffused natural studio light coming from the upper left. Subtle paper grain is visible throughout the background, and the ink strokes cast light, soft warm shadows onto the surface, creating an intimate artisan letterpress atmosphere.
```

Generic-model test (`gemini-2.5-flash-image`, text "Script", 2026-10-30):

![test render](https://cos.fontvibe.ai/opensource/text-effect-prompts/brush_stroke.jpg)

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/178926dc-7288-4562-8dbe-a3880e47fa0f.jpeg)](https://fontvibe.ai/gallery/9056) [![example](https://cos.fontvibe.ai/generations/user/17/c3d4495f-beab-4585-828e-d820d099c000.jpeg)](https://fontvibe.ai/gallery/9079) [![example](https://cos.fontvibe.ai/generations/user/17/84eff457-46e1-4628-a1ca-6597eca892ef.jpeg)](https://fontvibe.ai/gallery/9068)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
rendered as expressive Western brush script lettering with fluid connected strokes. Visible bristle texture with authentic thick-to-thin pressure variation — thick downstrokes, thin upstrokes, just like a loaded calligraphy brush. Ink slightly wet and glistening. Natural ink pooling at stroke starts, feathered dry-brush ending trails. Warm off-black ink on visible surface texture. Hand-crafted artisan energy with real brush imperfection. LETTERFORM PRIORITY: when the chosen font carries its own treatment, that font's letterform shapes take priority and own the letters; this style governs the brush-script medium, the thick-to-thin pressure variation and the ink wetness. FALLBACK MATERIAL: if the font carries no material of its own, render the letters as fluid connected brush-script strokes with thick downstrokes, thin upstrokes, wet pooling at starts and feathered dry-brush trails in warm off-black ink. COLOR PRIORITY: keep the font's own colors if specified; otherwise warm off-black ink on a textured surface.
```

**Scene**

```text
On warm cream textured paper under soft diffused natural studio light from upper left. Subtle paper grain visible. Light warm shadow cast by letters. Artisan letterpress atmosphere.
```

## Tips

- Short words or names in title case work best, allowing the fluid swashes and thick-to-thin stroke transitions to shine without crowding.
- You can change the ink color to rich sepia, deep indigo, or forest green while keeping the wet bristle and dry-brush effects intact.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/brush-stroke](https://fontvibe.ai/styles/brush-stroke) — see [Attribution](../../README.md#attribution).
