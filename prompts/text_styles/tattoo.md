---
id: tattoo
slug: tattoo
category: text_styles
tags: ["ink", "classic", "blackletter", "script", "proud", "expressive", "high contrast"]
names:
  en: "Tattoo Font"
  ja: "タトゥーフォント"
  zh: "纹身字体"
  es: "Letras de Tatuaje"
  pt: "Letras de Tatuagem"
  de: "Tattoo-Schrift"
description:
  en: "Old English tattoo lettering inked in black with a slight blue-black cast and fine shading, healed into real skin on a forearm or wrist."
  ja: "わずかに青みがかった黒で細かな陰影をつけたオールドイングリッシュのタトゥー文字。前腕や手首の実際の肌に定着しています。"
  zh: "黑色 Old English 纹身字，墨色略带蓝黑并有细腻阴影，已愈合在前臂或手腕的真实皮肤上。"
  es: "Rotulación de tatuaje Old English en tinta negra con un ligero matiz negro azulado y sombreado fino, ya curada sobre piel real de antebrazo o muñeca."
  pt: "Letreiramento de tatuagem Old English em tinta preta com leve tom preto-azulado e sombreado fino, já cicatrizado em pele real de antebraço ou pulso."
  de: "Old-English-Tattoo-Schrift in schwarzer Tinte mit leichtem Blauschwarz und feiner Schattierung, verheilt auf echter Haut an Unterarm oder Handgelenk."
fontvibe_url: https://fontvibe.ai/styles/tattoo
preview_image: https://cos.fontvibe.ai/generations/user/17/a6fde25d-8269-49db-9404-b1d70f1761bd.jpeg
examples:
  - url: https://fontvibe.ai/gallery/7706
    image: https://cos.fontvibe.ai/generations/user/17/102085bb-e49b-4dd0-8bc6-f3306ea3aaac.jpeg
  - url: https://fontvibe.ai/gallery/5727
    image: https://cos.fontvibe.ai/generations/user/17/2046e8a4-4da6-413b-a232-232843d7d5ef.jpeg
  - url: https://fontvibe.ai/gallery/5725
    image: https://cos.fontvibe.ai/generations/user/17/baa829fa-0a30-427b-ab5f-3f77cf009900.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "Forever"
  image: "https://cos.fontvibe.ai/opensource/text-effect-prompts/tattoo.jpg"
  passed: true
  note: "Fresh black tattoo lettering on an arm; spelled right (plainer script than the preview)."
license: CC-BY-4.0
---

# Tattoo Font

> Old English tattoo lettering inked in black with a slight blue-black cast and fine shading, healed into real skin on a forearm or wrist.

[![Tattoo Font on FontVibe](https://cos.fontvibe.ai/generations/user/17/a6fde25d-8269-49db-9404-b1d70f1761bd.jpeg)](https://fontvibe.ai/styles/tattoo)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/tattoo](https://fontvibe.ai/styles/tattoo)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. The letterforms appear as authentic fresh tattoo ink applied directly onto skin, centered in a close-up composition on an inner forearm. The ink is a rich, saturated, velvety matte deep black with a subtle blue-black undertone characteristic of needle-applied work. Each stroke exhibits an organic hand-applied quality, featuring crisp edges with minimal feathering, slight ink spread at junctions, and saturation that is heaviest at stroke centers with natural density variations. Subtle, precise imperfections reflect intentional needlework rather than mechanical perfection. The skin has a realistic medium tone, with fine pore texture showing through the ink and a very slight raise along the stroke edges. Diffused studio lighting from above-left casts soft shadows that reveal the delicate skin texture around the ink. The background is a soft, blurred neutral studio environment, framing the shot in a documentary tattoo photography style with focus strictly held on the tattooed lettering.
```

Generic-model test (`gemini-2.5-flash-image`, text "Forever", 2026-10-30):

![test render](https://cos.fontvibe.ai/opensource/text-effect-prompts/tattoo.jpg)

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/102085bb-e49b-4dd0-8bc6-f3306ea3aaac.jpeg)](https://fontvibe.ai/gallery/7706) [![example](https://cos.fontvibe.ai/generations/user/17/2046e8a4-4da6-413b-a232-232843d7d5ef.jpeg)](https://fontvibe.ai/gallery/5727) [![example](https://cos.fontvibe.ai/generations/user/17/baa829fa-0a30-427b-ab5f-3f77cf009900.jpeg)](https://fontvibe.ai/gallery/5725)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
rendered as authentic tattoo ink letterforms — deep black ink with slight blue-black undertone characteristic of fresh needle-applied tattoo. Each stroke shows organic hand-applied quality: slight ink spread at junctions, crisp line edges with minimal feathering, ink saturation heaviest at stroke centers with natural density variation. Letterforms carry the subtle imperfection of real tattooing — not mechanically perfect, but precise and intentional. Ink depth: rich, saturated, velvety matte black.
```

**Scene**

```text
Close-up of inner forearm skin with tattoo lettering centered in frame. The letterforms appear as fresh black tattoo ink on skin — authentic needle-applied quality with slight skin raise at ink edges, pore texture visible through ink, natural skin tone showing between strokes. Natural diffused studio lighting from above-left — soft shadows reveal skin texture around ink. Skin tone: medium, realistic. No full face visible, focus entirely on the tattooed text area. Background: blurred neutral studio environment. Photorealistic skin texture. Documentary tattoo photography style.
```

## Tips

- Short, punchy words, names, or single-word mantras work best to maintain the authentic look of a forearm tattoo.
- To vary the atmosphere, you can change the placement location on the body or specify healed, softened ink rather than fresh needlework.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/tattoo](https://fontvibe.ai/styles/tattoo) — see [Attribution](../../README.md#attribution).
