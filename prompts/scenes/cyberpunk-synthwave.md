---
id: cyberpunk_synthwave
slug: cyberpunk-synthwave
category: scenes
parent: cyberpunk
tags: ["gradient", "synthwave", "nostalgic", "80s", "neon", "3d"]
names:
  en: "Synthwave"
  ja: "シンセウェイブ"
  zh: "Synthwave"
  es: "Synthwave"
  pt: "Synthwave"
  de: "Synthwave"
description:
  en: "Retro 80s synthwave aesthetic with neon pink-purple gradient text and iconic grid floor. Vaporwave nostalgia meets cyberpunk."
  ja: "ネオンのピンク・パープルのグラデーション文字と象徴的なグリッドの床が特徴の、レトロな80年代シンセウェイブ美学。ヴェイパーウェイブの郷愁とサイバーパンクが融合します。"
  zh: "复古80年代 Synthwave 风格，霓虹粉紫渐变文字配上标志性的网格地面。Vaporwave 的怀旧撞上 Cyberpunk。"
  es: "Estética synthwave retro de los 80 con texto en degradado rosa-morado neón y el icónico suelo de rejilla. La nostalgia Vaporwave se cruza con el Cyberpunk."
  pt: "Estética synthwave retrô dos anos 80 com texto em degradê rosa-roxo neon e o icônico chão de grade. A nostalgia Vaporwave encontra o Cyberpunk."
  de: "Retro-80er-Synthwave-Ästhetik mit neonpink-violettem Verlaufstext und ikonischem Gitterboden. Vaporwave-Nostalgie trifft auf Cyberpunk."
fontvibe_url: https://fontvibe.ai/styles/cyberpunk-synthwave
preview_image: https://cos.fontvibe.ai/generations/user/17/f92a2299-8811-4ee2-8256-1f0e9a832e35.jpeg
examples:
  - url: https://fontvibe.ai/gallery/1673
    image: https://cos.fontvibe.ai/styles/cyberpunk_synthwave/cyberpunk_synthwave_retrowave-text-effect-png.jpg
  - url: https://fontvibe.ai/gallery/1672
    image: https://cos.fontvibe.ai/styles/cyberpunk_synthwave/cyberpunk_synthwave_synthwave-text-generator-png.jpg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "SYNTH"
  image: "https://cos.fontvibe.ai/opensource/text-effect-prompts/cyberpunk_synthwave.jpg"
  passed: true
  note: "Chrome 80s letters over sunset and neon grid; spelled right."
license: CC-BY-4.0
---

# Synthwave

> Retro 80s synthwave aesthetic with neon pink-purple gradient text and iconic grid floor. Vaporwave nostalgia meets cyberpunk.

[![Synthwave on FontVibe](https://cos.fontvibe.ai/generations/user/17/f92a2299-8811-4ee2-8256-1f0e9a832e35.jpeg)](https://fontvibe.ai/styles/cyberpunk-synthwave)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/cyberpunk-synthwave](https://fontvibe.ai/styles/cyberpunk-synthwave)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. The letters are rendered in a synthwave retro-futuristic style with bold, geometric letterforms. Each letter features a beveled 3D extrusion giving it solid depth, filled with a deep magenta-to-violet gradient. A vibrant neon pink electric glow outlines the exterior of every letter, complemented by a polished chrome-like inner highlight strip running along the top edge. Subtle lens flares accent the sharp corners of the typography. The text floats above an iconic scene where an infinite perspective grid floor in glowing neon pink lines converges toward the horizon. Centered on the horizon sits an oversized sun segmented by horizontal gradient stripes transitioning through magenta, coral, and yellow. In the background, the sky fades from deep purple to dark black and is speckled with sparse, pink-tinted stars. {{TEXT}} must be the only legible text in the image.
```

Generic-model test (`gemini-2.5-flash-image`, text "SYNTH", 2026-10-30):

![test render](https://cos.fontvibe.ai/opensource/text-effect-prompts/cyberpunk_synthwave.jpg)

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/styles/cyberpunk_synthwave/cyberpunk_synthwave_retrowave-text-effect-png.jpg)](https://fontvibe.ai/gallery/1673) [![example](https://cos.fontvibe.ai/styles/cyberpunk_synthwave/cyberpunk_synthwave_synthwave-text-generator-png.jpg)](https://fontvibe.ai/gallery/1672)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
rendered in synthwave retro-futuristic style. Letters in deep magenta-to-violet gradient (#FF006E to #8B00FF), outlined with bright neon pink electric glow, beveled 3D extrusion giving depth, chrome-like inner highlight strip along top edge of each letter, slight lens flare on sharp corners, bold and geometric letterforms. LETTERFORM PRIORITY: when the chosen font carries its own treatment, that font's letterform shapes take priority and own the letters; this style governs the synthwave gradient, the neon-pink glow outline and the 3D extrusion. FALLBACK MATERIAL: if the font carries no material of its own, render the letters as magenta-to-violet gradient letters outlined with bright neon-pink glow, beveled 3D extrusion and a chrome top-edge highlight. COLOR PRIORITY: keep the font's own colors if specified; otherwise deep magenta (#FF006E) to violet (#8B00FF).
```

**Scene**

```text
Iconic 80s synthwave scene: infinite perspective grid floor in neon pink lines converging to horizon, oversized sun with horizontal stripe gradient (magenta, coral, yellow) sitting on the horizon, deep purple-to-black sky with sparse pink-tinted stars.
```

## Tips

- Short, punchy words or short titles in all-capital letters complement the bold geometric 3D perspective best.
- You can easily shift the mood by changing the neon grid and outline colors from pink to cyan or electric blue.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/cyberpunk-synthwave](https://fontvibe.ai/styles/cyberpunk-synthwave) — see [Attribution](../../README.md#attribution).
