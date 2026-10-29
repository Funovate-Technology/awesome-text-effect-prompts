---
id: typewriter
slug: typewriter
category: text_styles
tags: ["ink", "vintage", "analog", "monospace", "typewriter", "letterpress", "nostalgic", "serious"]
names:
  en: "Typewriter"
  ja: "タイプライター"
  zh: "打字机"
  es: "Máquina de Escribir"
  pt: "Máquina de Escrever"
  de: "Schreibmaschine"
description:
  en: "Monospaced slab-serif type struck into cream paper, with uneven ink density, ribbon texture, faint letter misalignment and soft paper fibers."
  ja: "クリーム色の紙に打ち込まれた等幅スラブセリフ。インクの濃淡のむら、リボンの質感、わずかな文字のずれ、柔らかな紙の繊維。"
  zh: "等宽板衬线字敲印在米色纸上，墨色深浅不均，可见色带纹理和轻微错位，纸纤维柔和。"
  es: "Tipos slab monoespaciados golpeados sobre papel crema, con densidad de tinta irregular, textura de cinta, leve desalineación y suaves fibras de papel."
  pt: "Tipos slab monoespaçados batidos em papel creme, com densidade de tinta irregular, textura de fita, leve desalinhamento e fibras de papel suaves."
  de: "Nichtproportionale Slab-Schrift, in cremefarbenes Papier getippt, mit ungleichmäßiger Tintendichte, Farbbandstruktur, leichtem Versatz und weichen Papierfasern."
fontvibe_url: https://fontvibe.ai/styles/typewriter
preview_image: https://cos.fontvibe.ai/generations/user/17/c50d58c0-8dd4-4974-9998-13f7022cf670.jpeg
examples:
  - url: https://fontvibe.ai/gallery/3703
    image: https://cos.fontvibe.ai/generations/user/17/210aeeed-6026-4467-a80e-d9831e8502bf.jpeg
  - url: https://fontvibe.ai/gallery/3707
    image: https://cos.fontvibe.ai/generations/user/17/0c94f877-6e5b-47c7-8681-bab80166d140.jpeg
  - url: https://fontvibe.ai/gallery/3704
    image: https://cos.fontvibe.ai/generations/user/17/7ef8fe24-ac59-4a47-84ae-925d42c730e4.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "DISPATCH"
  image: "https://cos.fontvibe.ai/opensource/text-effect-prompts/typewriter.jpg"
  passed: true
  note: "Typewriter-struck letters on aged paper; spelled right."
license: CC-BY-4.0
---

# Typewriter

> Monospaced slab-serif type struck into cream paper, with uneven ink density, ribbon texture, faint letter misalignment and soft paper fibers.

[![Typewriter on FontVibe](https://cos.fontvibe.ai/generations/user/17/c50d58c0-8dd4-4974-9998-13f7022cf670.jpeg)](https://fontvibe.ai/styles/typewriter)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/typewriter](https://fontvibe.ai/styles/typewriter)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. Present {{TEXT}} in monospaced mechanical typewriter letterforms featuring authentic key-strike impressions. The ink application displays realistic uneven distribution across the letters, with certain strokes darker and others lighter, and thicker ink pooling at the stroke terminals. A distinct woven ribbon texture is visible throughout the letterforms, complemented by slightly irregular baseline alignments and natural letter spacing imperfections. Rendered in a warm sepia-tinted black ink, each character presses subtly into an aged cream bond paper surface that showcases a delicate fiber texture and fine paper grain. Soft directional side lighting casts gentle, subtle micro-shadows from the stamped letterforms onto the textured paper beneath them. The composition is completely minimalist and clean, containing no props, extra graphics, or decorative elements, keeping {{TEXT}} as the sole legible focus on the warm paper background.
```

Generic-model test (`gemini-2.5-flash-image`, text "DISPATCH", 2026-10-30):

![test render](https://cos.fontvibe.ai/opensource/text-effect-prompts/typewriter.jpg)

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/210aeeed-6026-4467-a80e-d9831e8502bf.jpeg)](https://fontvibe.ai/gallery/3703) [![example](https://cos.fontvibe.ai/generations/user/17/0c94f877-6e5b-47c7-8681-bab80166d140.jpeg)](https://fontvibe.ai/gallery/3707) [![example](https://cos.fontvibe.ai/generations/user/17/7ef8fe24-ac59-4a47-84ae-925d42c730e4.jpeg)](https://fontvibe.ai/gallery/3704)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
Monospaced typewriter letterforms with authentic mechanical key-strike impressions. Uneven ink distribution — some strokes darker, some lighter, ink thicker at stroke terminals. Aged cream bond paper surface with subtle fiber texture. Vintage manual-typewriter aesthetic. Warm sepia-tinted black ink. Slightly irregular baseline alignment, individual letter spacing imperfections. Visible ribbon texture on letterforms. Clean vintage typewriter quality.
```

**Scene**

```text
Clean warm cream paper texture background, subtle paper grain visible. Soft side lighting casting gentle shadow from letterforms onto paper surface. No scene elements, no props, no decorations. Pure typography showcase.
```

## Tips

- Short poetic phrases, single words, or manuscript-style excerpts suit this mechanical printing aesthetic best.
- Try shifting the ink color description to a dual-color red and black ribbon style to create a classic editorial revision look.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/typewriter](https://fontvibe.ai/styles/typewriter) — see [Attribution](../../README.md#attribution).
