---
id: neon_outline
slug: neon-outline
category: effects
parent: neon_glow
tags: ["minimal", "outline", "modern", "thin", "neon", "glow", "sleek", "cold"]
names:
  en: "Neon Outline"
  ja: "ネオンアウトライン"
  zh: "霓虹描边"
  es: "Contorno Neón"
  pt: "Contorno Neon"
  de: "Neon-Umriss"
description:
  en: "Hollow outline capitals traced by a single glowing blue-violet neon line, dark inside, with a soft halo and a glossy floor reflection."
  ja: "一本の青紫に光るネオン線だけで描いた中空のアウトライン大文字。内側は暗く、柔らかな光の輪と艶のある床への映り込み。"
  zh: "空心描边大写字母，只由一条发光的蓝紫霓虹线勾出，内部漆黑，外有柔和光晕和亮面地面倒影。"
  es: "Mayúsculas huecas trazadas por una sola línea de neón azul violeta luminosa, oscuras por dentro, con un halo suave y reflejo en un suelo brillante."
  pt: "Maiúsculas vazadas traçadas por uma única linha de neon azul-violeta luminosa, escuras por dentro, com halo suave e reflexo num piso brilhante."
  de: "Hohle Konturversalien aus einer einzigen leuchtenden blauvioletten Neonlinie, innen dunkel, mit weichem Halo und Spiegelung auf glänzendem Boden."
fontvibe_url: https://fontvibe.ai/styles/neon-outline
preview_image: https://cos.fontvibe.ai/generations/user/17/3c61c9b4-3d1c-4541-9fdf-a7a8f8dddce5.jpeg
examples:
  - url: https://fontvibe.ai/gallery/8682
    image: https://cos.fontvibe.ai/generations/user/17/f94dd368-1932-4470-b32b-bb201fa66d4d.jpeg
  - url: https://fontvibe.ai/gallery/8665
    image: https://cos.fontvibe.ai/generations/user/17/9d0b493e-75ee-4864-904d-710673e79e5b.jpeg
  - url: https://fontvibe.ai/gallery/8677
    image: https://cos.fontvibe.ai/generations/user/17/381deb4d-ed5a-41bd-99d0-4409bac50b3f.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "OUTLINE"
  image: ""
  passed: true
  note: "Thin neon outline letters with reflection; spelled right."
license: CC-BY-4.0
---

# Neon Outline

> Hollow outline capitals traced by a single glowing blue-violet neon line, dark inside, with a soft halo and a glossy floor reflection.

[![Neon Outline on FontVibe](https://cos.fontvibe.ai/generations/user/17/3c61c9b4-3d1c-4541-9fdf-a7a8f8dddce5.jpeg)](https://fontvibe.ai/styles/neon-outline)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/neon-outline](https://fontvibe.ai/styles/neon-outline)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. Render the letters as pure hollow neon outline letterforms, defined strictly by their glowing stroke borders with interiors remaining completely hollow and deep dark voids. The outline strokes emit electric blue and deep violet neon tube light, featuring an intense white-hot center core along the stroke path, a vivid colored glow zone expanding outward, and a soft wide halo. Following real gas-tube physics, the glow bleeds wider on the outside edge of each stroke than on the inside, with no light bleeding into the dark void centers. The strokes maintain crisp geometric precision with subtle organic brightness variations along the paths. The text is centered against a deep midnight blue-black atmospheric gradient, transitioning from indigo-black above to dark navy below with subtle electric blue ambient light scatter. Fine atmospheric haze and barely visible floating micro-particles catch the neon radiance. Below the text, a smooth obsidian floor with a faint wet sheen reflects elongated mirror columns of the glowing outlines, creating a cold, electric, and pristine minimalist setting.
```

Tested on `gemini-2.5-flash-image` with the text "OUTLINE" on 2026-10-30 — passed (legible, correctly spelled, recognisably this style).

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/f94dd368-1932-4470-b32b-bb201fa66d4d.jpeg)](https://fontvibe.ai/gallery/8682) [![example](https://cos.fontvibe.ai/generations/user/17/9d0b493e-75ee-4864-904d-710673e79e5b.jpeg)](https://fontvibe.ai/gallery/8665) [![example](https://cos.fontvibe.ai/generations/user/17/381deb4d-ed5a-41bd-99d0-4409bac50b3f.jpeg)](https://fontvibe.ai/gallery/8677)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
Pure neon outline letterforms — each letter defined only by its glowing stroke border, interior completely hollow and dark. The outline stroke glows with a continuous tube-light energy: bright white-hot center line along the stroke path, vivid neon glow zone expanding outward, soft wide halo bleeding into surrounding darkness. Glow is wider on the outside edge of the stroke than the inside, following real gas-tube light physics. Interior of each letter reads as deep void — no fill, no ambient light bleed inward. Stroke width is crisp and consistent, geometric precision. Slightly uneven brightness variation along the stroke path for organic gas-tube character. Choose neon color based on text meaning and mood: electric blue + deep violet for tech/cyber/cold words, neon pink + magenta for vibrant/pop/fun words, lime green + cyan for acid/gaming/hacker words, warm amber + orange for retro/diner/warm words, or multi-color with each letter a different hue for festive/creative content. LETTERFORM PRIORITY: when the chosen font carries its own treatment, that font's letterform shapes take priority and own the letters, rendered as their glowing hollow outline; this style governs the gas-tube glow physics and the color. FALLBACK MATERIAL: if the font carries no material of its own, render each letter as a pure hollow glowing neon outline with a white-hot center line, outward glow and a dark void interior. COLOR PRIORITY: keep the font's own colors if specified; otherwise choose the neon hue by the word's mood (electric blue/violet for tech, pink/magenta for fun, lime/cyan for gaming, amber for retro).
```

**Scene**

```text
Wide 16:9. APEX as neon outline letters, centered at 72% of frame width. Each letter is pure hollow, only the glowing stroke outline exists, interior is deep dark void. The outline strokes emit electric blue and deep violet neon light: bright white-hot center line, vivid colored glow zone expanding outward asymmetrically, wider halo on the outside edge of each stroke than the inside, exactly as real gas-tube physics dictates. Background: deep midnight blue-black — NOT pure black. A rich, dark atmospheric gradient: upper zone is deep indigo-black, lower zone shifts to dark navy with the faintest electric blue ambient scatter from the letters illuminating the space around them. Subtle depth and air. Very fine atmospheric haze in the glow field — barely visible floating micro-particles catching the neon light, adding spatial depth. Lower third: perfectly smooth dark floor — obsidian-toned but with a faint wet sheen. The neon outline letters reflect downward as elongated color columns, precise mirror image softening and fading toward the viewer. No warm tones anywhere. The atmosphere is cold, electric, deep. High-end minimal cyberpunk — the darkness has depth, not flatness.
```

## Tips

- Short words, technical terms, or punchy acronyms work best with hollow outline letterforms because they keep the negative space uncluttered.
- Change the electric blue and violet glow to hot pink and magenta or warm amber to shift the scene from a cold, sleek mood to a vibrant pop or retro setting.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/neon-outline](https://fontvibe.ai/styles/neon-outline) — see [Attribution](../../README.md#attribution).
