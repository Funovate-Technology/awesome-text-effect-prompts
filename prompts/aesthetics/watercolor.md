---
id: watercolor
slug: watercolor
category: aesthetics
tags: ["transparent", "paint", "handmade", "dreamy", "watercolor", "delicate"]
names:
  en: "Watercolor"
  ja: "水彩"
  zh: "水彩"
  es: "Acuarela"
  pt: "Aquarela"
  de: "Aquarell"
description:
  en: "Serif capitals filled with transparent watercolor washes and small floral sprigs, white paper glowing through, on deckled cold-press paper beside a paint palette."
  ja: "透明な水彩のにじみと小さな草花で満たしたセリフ体大文字。白い紙が光のように透け、耳付きのコールドプレス紙に、横にはパレット。"
  zh: "衬线大写字母填满透明水彩晕染和小花枝，白纸透出光亮，写在毛边冷压水彩纸上，旁边是调色盘。"
  es: "Mayúsculas con serifa rellenas de aguadas transparentes de acuarela y pequeñas ramitas florales, con el papel blanco brillando a través, sobre papel prensado en frío de borde irregular junto a una paleta."
  pt: "Maiúsculas serifadas preenchidas com aguadas transparentes de aquarela e pequenos raminhos florais, com o papel branco brilhando através, sobre papel prensado a frio de borda irregular ao lado de uma paleta."
  de: "Serifenversalien gefüllt mit transparenten Aquarelllasuren und kleinen Blütenzweigen, das weiße Papier scheint durch, auf büttenrandigem Kaltpresspapier neben einem Farbkasten."
fontvibe_url: https://fontvibe.ai/styles/watercolor
preview_image: https://cos.fontvibe.ai/generations/user/17/555e7b6d-6f08-46cf-83dc-7740d16ef242.jpeg
examples:
  - url: https://fontvibe.ai/gallery/17669
    image: https://cos.fontvibe.ai/generations/user/17/77733674-447e-4fd6-8ab9-a9f0f5df6d96.jpeg
  - url: https://fontvibe.ai/gallery/1510
    image: https://cos.fontvibe.ai/generations/user/17/7b637b8b252b427e8fb3d8c9c36a6677.jpeg
  - url: https://fontvibe.ai/gallery/231
    image: https://cos.fontvibe.ai/generations/user/17/8d601f7a-3b77-430a-ad12-685b8abb1346.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "Hello Spring"
  image: ""
  passed: true
  note: "Watercolour letters on paper; two words, spelled right."
license: CC-BY-4.0
---

# Watercolor

> Serif capitals filled with transparent watercolor washes and small floral sprigs, white paper glowing through, on deckled cold-press paper beside a paint palette.

[![Watercolor on FontVibe](https://cos.fontvibe.ai/generations/user/17/555e7b6d-6f08-46cf-83dc-7740d16ef242.jpeg)](https://fontvibe.ai/styles/watercolor)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/watercolor](https://fontvibe.ai/styles/watercolor)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. The letters of {{TEXT}} are painted as luminous, transparent wet-on-wet watercolor washes directly onto bright cold-press watercolor paper. The pigment disperses unevenly across each character, pooling darker along the outer edges while centers stay pale, with soft cauliflower blooms where wet paint meets wet and crisp hard edges where paint dried on dry paper. Granulating pigment settles into the textured paper tooth, revealing tiny flecks of bare paper that act as the lightest values in the composition. The lettering is rendered in a fine-art aquarelle palette featuring layered washes of sap and olive green, rose madder, blush, cobalt, cerulean blue, indigo, and raw sienna, remaining completely transparent and luminous without opacity. The text sits large and centered with generous negative space across the paper sheet, bordered by faint deckled torn edges and grounded by a gentle, cool shadow under soft, even north-light, accompanied only by a few loose botanical sprigs and subtle drifting pigment specks.
```

Tested on `gemini-2.5-flash-image` with the text "Hello Spring" on 2026-10-30 — passed (legible, correctly spelled, recognisably this style).

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/77733674-447e-4fd6-8ab9-a9f0f5df6d96.jpeg)](https://fontvibe.ai/gallery/17669) [![example](https://cos.fontvibe.ai/generations/user/17/7b637b8b252b427e8fb3d8c9c36a6677.jpeg)](https://fontvibe.ai/gallery/1510) [![example](https://cos.fontvibe.ai/generations/user/17/8d601f7a-3b77-430a-ad12-685b8abb1346.jpeg)](https://fontvibe.ai/gallery/231)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
a luminous transparent watercolor world painted on paper. LIGHT & GROUND: soft even north-light falls on cold-press watercolor paper whose bright unpainted white is the lightest value in the frame — highlights are the bare paper itself, never painted white. SURFACE: transparent washes let the paper glow through; pigment disperses unevenly, pooling darker along edges while centers stay pale, with soft wet-on-wet cauliflower blooms where wet meets wet and crisp hard edges where paint dried on dry paper — the signature soft/hard tension. TEXTURE: cold-press paper tooth flecks the washes with tiny bare-white gaps and heavier pigment granulates into the grain. PALETTE: a transparent fine-art aquarelle palette — sap and olive green, rose madder and blush, cobalt and cerulean blue, indigo, raw sienna — always luminous and layered, never opaque. LETTERFORM PRIORITY: when the chosen font carries its own material or color (botanical floral sprigs, ink-in-water diffusion, expressive splatter, line-and-wash ink, etc.), that font treatment takes absolute priority and owns the letter surface; this style then governs only the paper, light and surrounding color atmosphere. FALLBACK MATERIAL: if the font carries no material of its own, paint the letters as transparent wet-on-wet watercolor washes — pale luminous centers, pigment pooling and blooming at the edges, the white paper breathing through — so the watercolor identity always reads.
```

**Scene**

```text
The text sits large and centered on a sheet of fine cold-press watercolor paper, the bright paper breathing around it as generous negative space, a faint deckled torn edge and a soft cool shadow grounding the sheet. A few loose botanical sprigs and drifting pigment specks rest softly nearby. Calm, luminous, gallery-quality fine-art painting composition with plenty of white paper.
```

## Tips

- Short, evocative nature words, names, or poetic terms harmonize best with the delicate, organic watercolor bleed.
- To shift the mood, narrow the color palette to specific combinations like deep indigo and raw sienna or soft rose madder and olive green.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/watercolor](https://fontvibe.ai/styles/watercolor) — see [Attribution](../../README.md#attribution).
