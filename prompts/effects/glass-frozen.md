---
id: glass_frozen
slug: glass-frozen
category: effects
parent: glass
tags: ["ice", "crystal", "transparent", "cold", "photorealistic"]
names:
  en: "Frozen Ice"
  ja: "凍った氷"
  zh: "寒冰冻结"
  es: "Hielo Congelado"
  pt: "Gelo Congelado"
  de: "Gefrorenes Eis"
description:
  en: "Encased in solid ice — thick frozen block with sharp edge facets, deep internal frost cracks, and icicle drips. Photorealistic frozen water quality."
  ja: "分厚い氷の塊に閉じ込められた文字。鋭くカットされた氷のファセット、内部まで深く走る霜のひび割れ、そして垂れ下がるつらら。実写のようにリアルな氷結の質感です。"
  zh: "封进厚实的坚冰里——冰块棱角锋利，内部布满深层霜裂纹，还挂着垂落的冰锥。写实的冻水质感。"
  es: "Encerrado en hielo macizo: un bloque grueso y congelado con facetas de bordes filosos, grietas internas de escarcha y goteos de carámbanos. Calidad fotorrealista de agua congelada."
  pt: "Preso em gelo maciço: um bloco espesso e congelado com facetas de bordas afiadas, rachaduras internas de geada e pingos de estalactites de gelo. Qualidade fotorrealista de água congelada."
  de: "In festem Eis eingeschlossen — dicker gefrorener Block mit scharfen Kantenfacetten, tiefen inneren Frostrissen und Eiszapfen-Tropfen. Diese Eis-Schrift hat fotorealistische Gefrierwasser-Qualität."
fontvibe_url: https://fontvibe.ai/styles/glass-frozen
preview_image: https://cos.fontvibe.ai/generations/user/17/0f7ebd64-c757-4472-be6f-07358821cae4.jpeg
examples:
  - url: https://fontvibe.ai/gallery/11194
    image: https://cos.fontvibe.ai/generations/user/17/c74ae387-bed0-4dbd-ab6f-a9d747800298.jpeg
  - url: https://fontvibe.ai/gallery/11213
    image: https://cos.fontvibe.ai/generations/user/17/6bdf013a-2909-4f4a-bdfc-c9e7211fa16c.jpeg
  - url: https://fontvibe.ai/gallery/11223
    image: https://cos.fontvibe.ai/generations/user/17/f4621d35-00a3-488d-85cf-d0587a8f7bfa.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "FROST"
  image: "https://cos.fontvibe.ai/opensource/text-effect-prompts/glass_frozen.jpg"
  passed: true
  note: "Ice-encased letters with icicles under an aurora; spelled right."
license: CC-BY-4.0
---

# Frozen Ice

> Encased in solid ice — thick frozen block with sharp edge facets, deep internal frost cracks, and icicle drips. Photorealistic frozen water quality.

[![Frozen Ice on FontVibe](https://cos.fontvibe.ai/generations/user/17/0f7ebd64-c757-4472-be6f-07358821cae4.jpeg)](https://fontvibe.ai/styles/glass-frozen)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/glass-frozen](https://fontvibe.ai/styles/glass-frozen)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. The text is formed from massive, deep-frozen solid glacial ice blocks. Each letter features a smooth-polished outer surface rimmed with faint frost micro-crystal bloom and delicate edge frost textures. The body is thick, translucent ice with a pale blue-white tint, filled with suspended internal air bubble inclusions and fine crack networks branching inward from surface stress points. A deep, cold cyan-blue glow emanates from within the core of each letter via subsurface scattering, fading toward the crisp perimeters. Sharp icicle extensions hang from the letter bases, casting bright caustic refractions below, while polished edges catch incoming light in bright rim caustics and subtle cold-spectral micro-prisms. The letters rest against a deep arctic midnight backdrop of near-black darkness, accented by a faint cold blue-teal atmospheric aurora glow spreading across the upper frame. Fine airborne ice crystal particles drift through the air, catching the light as glittering specks. The glowing ice letters serve as the primary illumination in the scene, maintaining a palette of pure icy blues, cyans, and crisp whites with zero warm tones.
```

Generic-model test (`gemini-2.5-flash-image`, text "FROST", 2026-10-30):

![test render](https://cos.fontvibe.ai/opensource/text-effect-prompts/glass_frozen.jpg)

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/c74ae387-bed0-4dbd-ab6f-a9d747800298.jpeg)](https://fontvibe.ai/gallery/11194) [![example](https://cos.fontvibe.ai/generations/user/17/6bdf013a-2909-4f4a-bdfc-c9e7211fa16c.jpeg)](https://fontvibe.ai/gallery/11213) [![example](https://cos.fontvibe.ai/generations/user/17/f4621d35-00a3-488d-85cf-d0587a8f7bfa.jpeg)](https://fontvibe.ai/gallery/11223)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
rendered in deep-frozen solid ice letterforms — each letter a massive glacial ice block. Surface: smooth-polished outer ice face with faint frost micro-crystal bloom at letter edges and surface rim frost texture. Body: thick translucent ice with pale blue-white tint, internal air bubble inclusions caught as bright white spherical highlights, faint crack networks branching inward from surface stress points. Internal: deep cold glow emanating from letter center — subsurface scattering of cold light through the ice mass, brighter at core, fading toward edges. Optical behavior: incoming light refracts at the polished ice surface creating bright rim caustic lines at letter edges; internal ice density variation bends light into cold blue-white spectral micro-prisms; icicle extensions at letter bases show pure refraction clarity — crisp cold caustic light fans below. Peak visual moment: cold internal glow + surface frost bloom + refracted rim light + hanging icicle drips = letters physically frozen in time. Reference: blue glacier ice cave walls / Arctic sea ice block at dawn / Jökulsárlón glacial lagoon ice / professional ice sculptor competition piece under cold spotlight.
```

**Scene**

```text
Deep arctic midnight background — near-black with a wide cold blue-teal atmospheric aurora glow spreading across the upper frame, subtly illuminating the frozen letters from behind. Fine airborne ice crystal particles catch the cold light as bright specks. The frozen letters are the sole light source in the dark composition — their internal cold glow and refracted rim light are the brightest elements in the frame. Zero warm tones. Maximum cold drama.
```

## Tips

- Short words with thick, bold letter shapes work best because they provide enough internal volume to display the cracks, trapped bubbles, and subsurface light glow.
- To adjust the mood, you can emphasize heavier falling snow and blizzard drifts, or reduce the icicle drips for a cleaner carved-ice look.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/glass-frozen](https://fontvibe.ai/styles/glass-frozen) — see [Attribution](../../README.md#attribution).
