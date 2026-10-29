---
id: glitch
slug: glitch
category: effects
tags: ["glitch", "scanlines", "digital", "chromatic aberration", "cyberpunk", "intense", "chaotic"]
names:
  en: "Glitch"
  ja: "グリッチ"
  zh: "故障 Glitch"
  es: "Glitch"
  pt: "Glitch"
  de: "Glitch"
description:
  en: "White sans capitals split by red and cyan channel offsets, sliced by horizontal displacement bands and scanlines, reflected on a wet neon street at night."
  ja: "赤とシアンのチャンネルずれで裂けた白いサンセリフ大文字。水平の変位スライスと走査線が走り、夜の濡れたネオン街に映ります。"
  zh: "白色无衬线大写字母被红青通道错位撕开，横向位移切片和扫描线贯穿，倒映在夜里湿漉漉的霓虹街道上。"
  es: "Mayúsculas sans serif blancas partidas por desplazamientos de canal rojo y cian, cortadas por franjas horizontales y líneas de escaneo, reflejadas en una calle de neón mojada de noche."
  pt: "Maiúsculas sans serif brancas partidas por deslocamentos de canal vermelho e ciano, cortadas por faixas horizontais e linhas de varredura, refletidas numa rua de neon molhada à noite."
  de: "Weiße serifenlose Versalien, aufgerissen durch rote und cyanfarbene Kanalversätze, durchschnitten von horizontalen Verschiebungen und Scanlines, gespiegelt auf nasser Neonstraße bei Nacht."
fontvibe_url: https://fontvibe.ai/styles/glitch
preview_image: https://cos.fontvibe.ai/generations/user/17/eb45177c-8ee4-4334-a8c4-4be1d4161a28.jpeg
examples:
  - url: https://fontvibe.ai/gallery/13324
    image: https://cos.fontvibe.ai/generations/user/17/a878fef9-05b9-49f8-b39d-a0832167c292.jpeg
  - url: https://fontvibe.ai/gallery/13247
    image: https://cos.fontvibe.ai/generations/user/17/d1da9b55-657c-43e2-8f83-9a60469667c2.jpeg
  - url: https://fontvibe.ai/gallery/13310
    image: https://cos.fontvibe.ai/generations/user/17/0e6d61e2-8ab2-48f6-a0e7-02ca011b1e44.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "GLITCH"
  image: ""
  passed: true
  note: "Scanline RGB glitch letters; spelled right."
license: CC-BY-4.0
---

# Glitch

> White sans capitals split by red and cyan channel offsets, sliced by horizontal displacement bands and scanlines, reflected on a wet neon street at night.

[![Glitch on FontVibe](https://cos.fontvibe.ai/generations/user/17/eb45177c-8ee4-4334-a8c4-4be1d4161a28.jpeg)](https://fontvibe.ai/styles/glitch)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/glitch](https://fontvibe.ai/styles/glitch)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. The lettering is large, dominant, and fills the frame with a controlled digital corruption aesthetic. Authentic RGB chromatic aberration splits every letter edge, shifting the red channel cleanly to the left and the cyan channel to the right to produce a distinctive double-vision split. Dense, rhythmic, semi-transparent horizontal CRT scan lines cover the entire text surface, simulating a glowing phosphor monitor screen. At random vertical positions along the letters, several sharp-edged rectangular pixel blocks displace horizontally while keeping the text completely readable. A subtle cyan-white phosphor bloom glows along the outer contours of the characters. The entire composition is set against an empty, dark digital void accented by faint horizontal VHS tracking error bands and small clusters of corrupted pixel artifacts scattered throughout the atmosphere.
```

Tested on `gemini-2.5-flash-image` with the text "GLITCH" on 2026-10-30 — passed (legible, correctly spelled, recognisably this style).

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/a878fef9-05b9-49f8-b39d-a0832167c292.jpeg)](https://fontvibe.ai/gallery/13324) [![example](https://cos.fontvibe.ai/generations/user/17/d1da9b55-657c-43e2-8f83-9a60469667c2.jpeg)](https://fontvibe.ai/gallery/13247) [![example](https://cos.fontvibe.ai/generations/user/17/0e6d61e2-8ab2-48f6-a0e7-02ca011b1e44.jpeg)](https://fontvibe.ai/gallery/13310)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
Core glitch effect: authentic RGB chromatic aberration — red channel shifted 5–8px to the left, cyan channel shifted 5–8px to the right, creating the classic double-vision color split on every letter edge. CRT scan lines: dense horizontal parallel lines across the entire text surface, spacing 3–4px, semi-transparent, rhythmic — simulating a real CRT phosphor screen. Pixel block artifacts: 3–5 sharp-edged rectangular chunks of letter pixels displaced horizontally by 10–25px at random vertical positions along the text. Edge glow: subtle cyan-white phosphor bloom emanating from letter boundaries. The glitch distortion is controlled and deliberate — text remains clearly readable. No random noise flood. No cartoon effects. Professional digital corruption aesthetic. LETTERFORM PRIORITY: when the chosen font carries its own treatment, that font's letterform shapes take priority and own the letters; this style governs the RGB chromatic aberration, the scan lines and the pixel-displacement corruption. FALLBACK MATERIAL: if the font carries no material of its own, render the letters with a red/cyan channel split, dense CRT scan lines and displaced pixel blocks, kept clearly readable. COLOR PRIORITY: keep the font's own colors if specified; otherwise the red-and-cyan split with cyan-white phosphor glow on a dark digital void.
```

**Scene**

```text
Text fills the frame with maximum visual presence — large and dominant. VHS tracking error bands across the frame, dark digital void background with scattered corrupted pixel clusters.
```

## Tips

- Short, punchy words or technical terminology in all capital letters work best to showcase the horizontal slice displacements.
- To shift the mood, swap the red and cyan color channels for a magenta and green split, or adjust the intensity of the VHS tracking bands across the background.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/glitch](https://fontvibe.ai/styles/glitch) — see [Attribution](../../README.md#attribution).
