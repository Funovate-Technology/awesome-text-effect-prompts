---
id: vaporwave
slug: vaporwave
category: aesthetics
tags: ["90s", "vaporwave", "dreamy", "nostalgic", "retro internet", "chrome", "gradient", "surreal"]
names:
  en: "Vaporwave"
  ja: "ヴェイパーウェイブ"
  zh: "Vaporwave 蒸汽波"
  es: "Vaporwave"
  pt: "Vaporwave"
  de: "Vaporwave"
description:
  en: "Chrome block capitals in pastel pink and cyan, floating over a checkerboard floor beside a marble bust, palms and small katakana text."
  ja: "パステルピンクとシアンのクロームのブロック体大文字。市松模様の床の上に浮かび、大理石の胸像、ヤシ、小さなカタカナが添えられます。"
  zh: "粉彩粉与青色的铬金属方块大写字母，悬浮在棋盘格地面上方，旁边是大理石胸像、棕榈和小号片假名。"
  es: "Mayúsculas de bloque cromadas en rosa pastel y cian, flotando sobre un suelo de damero junto a un busto de mármol, palmeras y pequeño texto en katakana."
  pt: "Maiúsculas em bloco cromadas em rosa pastel e ciano, flutuando sobre um piso xadrez ao lado de um busto de mármore, palmeiras e pequeno texto em katakana."
  de: "Chrom-Blockversalien in Pastellrosa und Cyan, schwebend über einem Schachbrettboden neben einer Marmorbüste, Palmen und kleinem Katakana-Text."
fontvibe_url: https://fontvibe.ai/styles/vaporwave
preview_image: https://cos.fontvibe.ai/generations/user/17/a6067e8d-612c-4ae3-8b31-e3e4fd69cac9.jpeg
examples:
  - url: https://fontvibe.ai/gallery/481
    image: https://cos.fontvibe.ai/generations/user/17/de5a303f-8e65-4dea-a3a3-67816087640c.jpeg
  - url: https://fontvibe.ai/gallery/483
    image: https://cos.fontvibe.ai/generations/user/17/70ca5b11-f6d7-424b-ab80-ce3f2e8a2964.jpeg
  - url: https://fontvibe.ai/gallery/1500
    image: https://cos.fontvibe.ai/generations/user/17/ae485f54c1c84af2ac619469ef496f97.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "WAVE"
  image: ""
  passed: true
  note: "Pastel vaporwave scene with bust, palms and checkerboard; spelled right."
license: CC-BY-4.0
---

# Vaporwave

> Chrome block capitals in pastel pink and cyan, floating over a checkerboard floor beside a marble bust, palms and small katakana text.

[![Vaporwave on FontVibe](https://cos.fontvibe.ai/generations/user/17/a6067e8d-612c-4ae3-8b31-e3e4fd69cac9.jpeg)](https://fontvibe.ai/styles/vaporwave)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/vaporwave](https://fontvibe.ai/styles/vaporwave)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. The text sits large and dominant in the center, rendered in a soft pink-to-cyan vaporwave gradient with a gentle luminous bloom and faint drifting scanlines across its surface. Make {{TEXT}} the only legible text in the entire image. The lettering is placed within a nostalgic 1990s dreamscape illuminated by the soft glow of an early CRT screen. An early-3D perspective checkerboard grid recedes toward a gentle pastel horizon beneath a serene sunset sky. A classical marble bust rests quietly to one side, complemented by dark palm silhouettes along the edges. The entire composition is bathed in a dreamy, low-saturation pastel palette of cotton-candy pink, soft cyan-teal, and lilac-purple. A subtle analog VHS texture blankets the scene, complete with horizontal scanlines, delicate tracking lines, hazy diffusion, and magenta-cyan chromatic aberration edge bleed, evoking a calm, atmospheric retro aesthetic.
```

Tested on `gemini-2.5-flash-image` with the text "WAVE" on 2026-10-30 — passed (legible, correctly spelled, recognisably this style).

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/de5a303f-8e65-4dea-a3a3-67816087640c.jpeg)](https://fontvibe.ai/gallery/481) [![example](https://cos.fontvibe.ai/generations/user/17/70ca5b11-f6d7-424b-ab80-ce3f2e8a2964.jpeg)](https://fontvibe.ai/gallery/483) [![example](https://cos.fontvibe.ai/generations/user/17/ae485f54c1c84af2ac619469ef496f97.jpeg)](https://fontvibe.ai/gallery/1500)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
a 1990s vaporwave dreamscape — the glow of an early consumer CRT. LIGHT & COLOR: a soft low-saturation pastel palette of cotton-candy pink, soft cyan-teal and lilac-purple, lit like a 1990s desktop-wallpaper sunset, gentle and dreamy rather than high-contrast neon. SCENE ATMOSPHERE: a classical marble Roman bust, an early-3D perspective checkerboard grid receding to a pastel horizon, palm silhouettes, and decorative fullwidth letters and Japanese katakana floating as accents. TEXTURE: a soft VHS layer over everything — horizontal scanlines, gentle tracking lines, magenta-cyan chromatic-aberration bleed and analog haze. LETTERFORM PRIORITY: when the chosen font carries its own material (pastel chrome, fullwidth gradient, VHS glitch, Y2K silver), that font treatment takes absolute priority and owns the letters; this style governs the pastel light, the marble-and-grid scene and the VHS texture. FALLBACK MATERIAL: if the font carries no material of its own, render the letters in a soft pink-to-cyan vaporwave gradient with a gentle bloom and a drifting VHS scanline, so the vaporwave aesthetic always reads.
```

**Scene**

```text
The text sits large and dominant in the center of a 1990s vaporwave dreamscape — a soft pink-and-cyan pastel gradient sky over an early-3D checkerboard grid receding to the horizon, a classical marble bust to one side, palm silhouettes and a katakana accent drifting in a corner, soft VHS scanlines and tracking lines across everything. Dreamy, nostalgic, lo-fi 90s aesthetic.
```

## Tips

- Short, evocative words like 'DREAM', 'NOSTALGIA', or 'HORIZON' in uppercase complement the retro digital atmosphere especially well.
- To shift the mood from peaceful pastel to late-night broadcast, emphasize heavy VHS tracking lines and stronger chromatic aberration.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/vaporwave](https://fontvibe.ai/styles/vaporwave) — see [Attribution](../../README.md#attribution).
