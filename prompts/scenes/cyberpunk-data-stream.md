---
id: cyberpunk_data_stream
slug: cyberpunk-data-stream
category: scenes
parent: cyberpunk
tags: ["mysterious", "cold", "monospace", "digital", "glow", "scanlines"]
names:
  en: "Data Stream"
  ja: "データストリーム"
  zh: "数据流"
  es: "Data Stream"
  pt: "Data Stream"
  de: "Datenstrom"
description:
  en: "Cascading data stream text with digital rain and terminal green glow. Hacker and code aesthetic."
  ja: "ハッカーとコードの美学です。"
  zh: "黑客与代码美学。"
  es: "Estética hacker y de código."
  pt: "Estética hacker e de código."
  de: "Diese hacker schrift bringt Hacker- und Code-Ästhetik auf den Punkt."
fontvibe_url: https://fontvibe.ai/styles/cyberpunk-data-stream
preview_image: https://cos.fontvibe.ai/generations/user/17/a1fff21e-79fa-49b9-8eb4-9a9b038fec0a.jpeg
examples:
  - url: https://fontvibe.ai/gallery/1677
    image: https://cos.fontvibe.ai/styles/cyberpunk_data_stream/cyberpunk_data_stream_hacker-text-effect-png.jpg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "DATA"
  image: ""
  passed: true
  note: "Terminal-green letters inside cascading code rain; spelled right."
license: CC-BY-4.0
---

# Data Stream

> Cascading data stream text with digital rain and terminal green glow. Hacker and code aesthetic.

[![Data Stream on FontVibe](https://cos.fontvibe.ai/generations/user/17/a1fff21e-79fa-49b9-8eb4-9a9b038fec0a.jpeg)](https://fontvibe.ai/styles/cyberpunk-data-stream)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/cyberpunk-data-stream](https://fontvibe.ai/styles/cyberpunk-data-stream)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. The primary letters of {{TEXT}} are formed from vibrant terminal-green (#00FF41) monospace characters emitting an intense phosphor-screen glow. A secondary layer of cascading smaller digital code characters flows through and around the main letterforms like falling rain. The density of these tiny digital characters is highest along the outer edges of the letters, producing a dissolving effect where the glyphs transition into the surrounding darkness. The entire image features vintage CRT monitor horizontal scanlines and a subtle screen-door pixel grid texture with deep, punchy contrast. The environment is a pure black void evoking a dark computer terminal. In the deep background, vertical streams of green code characters fall at varying speeds and opacities, while a subtle green ambient glow casts across the ground plane beneath the glowing typography.
```

Tested on `gemini-2.5-flash-image` with the text "DATA" on 2026-10-30 — passed (legible, correctly spelled, recognisably this style).

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/styles/cyberpunk_data_stream/cyberpunk_data_stream_hacker-text-effect-png.jpg)](https://fontvibe.ai/gallery/1677)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
rendered in digital data stream style. Primary letters formed from bright terminal-green (#00FF41) monospace characters with strong phosphor-screen glow, secondary layer of cascading smaller code characters flowing through and around the letterforms like falling rain, character density highest at letter edges creating a dissolving effect, old CRT monitor scanlines and subtle screen-door pixel grid texture, deep contrast. LETTERFORM PRIORITY: when the chosen font carries its own treatment, that font's letterform shapes take priority and own the letters; this style governs the terminal-green phosphor code rain, the cascading characters and the CRT scanlines. FALLBACK MATERIAL: if the font carries no material of its own, render the letters as bright terminal-green monospace letters with cascading digital-rain characters, phosphor glow and CRT scanlines. COLOR PRIORITY: keep the font's own colors if specified; otherwise terminal green (#00FF41) on a near-black screen.
```

**Scene**

```text
Pure black void environment evoking a dark terminal screen. Vertical streams of cascading green code characters falling at different speeds and opacities in the deep background, subtle green ambient glow on ground plane.
```

## Tips

- Short, tech-oriented words, commands, or acronyms work best with this computer terminal look.
- Swap the terminal-green hex code for amber (#FFB000) or monochrome cyan to simulate other vintage phosphor monitor styles.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/cyberpunk-data-stream](https://fontvibe.ai/styles/cyberpunk-data-stream) — see [Attribution](../../README.md#attribution).
