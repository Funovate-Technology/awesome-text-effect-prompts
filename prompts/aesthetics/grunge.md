---
id: grunge
slug: grunge
category: aesthetics
tags: ["torn", "raw", "punk", "ransom note", "collage", "photocopy", "rebellious"]
names:
  en: "Grunge"
  ja: "グランジ"
  zh: "Grunge 垃圾摇滚"
  es: "Grunge"
  pt: "Grunge"
  de: "Grunge"
description:
  en: "Ransom-note letters cut from mixed newspaper type, taped onto raw photocopied paper with halftone speckle, torn edges and a single punk-red accent."
  ja: "さまざまな新聞の活字を切り抜いた脅迫状風の文字。コピーした粗い紙にテープで貼り、ハーフトーンの粒、破れた縁、パンクな赤をひとさし。"
  zh: "从各式报纸字剪下拼成的勒索信字母，用胶带贴在影印粗纸上，带半调噪点、撕边和一抹朋克红。"
  es: "Letras de nota de rescate recortadas de distintos periódicos, pegadas con cinta sobre papel fotocopiado tosco con moteado de semitono, bordes rasgados y un único acento rojo punk."
  pt: "Letras de bilhete de resgate recortadas de vários jornais, coladas com fita sobre papel fotocopiado áspero com pontilhado de meio-tom, bordas rasgadas e um único toque vermelho punk."
  de: "Erpresserbrief-Buchstaben aus verschiedenen Zeitungen geschnitten, mit Klebeband auf rauem Kopierpapier mit Rasterkörnung, eingerissenen Kanten und einem einzigen Punk-Rot-Akzent."
fontvibe_url: https://fontvibe.ai/styles/grunge
preview_image: https://cos.fontvibe.ai/generations/user/17/12f78b1e-bb3c-495e-bf77-349fe35da045.jpeg
examples:
  - url: https://fontvibe.ai/gallery/311
    image: https://cos.fontvibe.ai/generations/user/17/91d0a9fb-d18c-48a2-961b-b4dc0245997a.jpeg
  - url: https://fontvibe.ai/gallery/314
    image: https://cos.fontvibe.ai/generations/user/17/6fe2af72-e2df-41f4-98cf-6405d58773b5.jpeg
  - url: https://fontvibe.ai/gallery/4964
    image: https://cos.fontvibe.ai/generations/user/17/e15eff65-d2a1-4858-a536-dd71cf1ab81c.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "GRUNGE"
  image: "https://cos.fontvibe.ai/opensource/text-effect-prompts/grunge.jpg"
  passed: true
  note: "Attempt 1: main word correct, but the collage adds gibberish pseudo-text. Attempt 2: torn photocopy collage with the word clean and legible; no stray text."
license: CC-BY-4.0
---

# Grunge

> Ransom-note letters cut from mixed newspaper type, taped onto raw photocopied paper with halftone speckle, torn edges and a single punk-red accent.

[![Grunge on FontVibe](https://cos.fontvibe.ai/generations/user/17/12f78b1e-bb3c-495e-bf77-349fe35da045.jpeg)](https://fontvibe.ai/styles/grunge)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/grunge](https://fontvibe.ai/styles/grunge)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. The letters of {{TEXT}} are rendered in heavy, high-contrast black ink, featuring coarse halftone dot screens, ink bleed, low-ink roller streaks, and clogged edges on raw off-white newsprint paper. The letters appear cut out and pasted by hand, accented with torn paper borders, scissor-cut edges, lifted paper corners, and strips of tape. The surrounding scene functions as a photocopied punk-zine cover, featuring a layered cut-and-paste collage aesthetic with subtle spray-paint overspray, photocopy speckles, scratches, and nth-generation blurring. The color palette relies on high-contrast black ink against gritty off-white paper, disrupted by a single punchy accent slash of punk red that prints slightly off-register. The composition is raw and asymmetric, full of DIY collage energy, ensuring that {{TEXT}} remains the only legible text in the entire image.
```

Generic-model test (`gemini-2.5-flash-image`, text "GRUNGE", 2026-10-30):

![test render](https://cos.fontvibe.ai/opensource/text-effect-prompts/grunge.jpg)

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/91d0a9fb-d18c-48a2-961b-b4dc0245997a.jpeg)](https://fontvibe.ai/gallery/311) [![example](https://cos.fontvibe.ai/generations/user/17/6fe2af72-e2df-41f4-98cf-6405d58773b5.jpeg)](https://fontvibe.ai/gallery/314) [![example](https://cos.fontvibe.ai/generations/user/17/e15eff65-d2a1-4858-a536-dd71cf1ab81c.jpeg)](https://fontvibe.ai/gallery/4964)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
a photocopied punk-zine world. PRINT: everything looks run through a cheap copier and pasted up by hand — coarse halftone dot screens, heavy black ink that bleeds and clogs, low-ink dropout and roller streaks, photocopy speckle and nth-generation blur on raw off-white newsprint and photocopy paper. TEXTURE: torn and scissor-cut paper edges, strips of tape, lifted corners, creases, scratches, smears and spray-paint overspray — the evidence of a hand working under pressure. LIMITED PALETTE: the cheap two-color reproduction palette — high-contrast black ink and raw off-white paper, with one punchy punk RED as the accent (occasionally a hit of acid yellow), printed slightly off-register. ENERGY: a layered cut-and-paste collage grammar, asymmetric and disrupted like a stapled zine. LETTERFORM PRIORITY: when the chosen font carries its own material or treatment (ransom-note collage, riso halftone, distressed, spray, stamp, ink-bleed), that font treatment takes absolute priority and owns the letters; this style governs the paper, print degradation, palette and surrounding collage. FALLBACK MATERIAL: if the font carries no material of its own, print the letters in heavy high-contrast black ink on raw off-white paper with photocopy grain, ink bleed and torn edges, so the grunge zine feel always reads.
```

**Scene**

```text
The text sits bold and dominant, pasted up like the cover of a photocopied punk zine on raw off-white paper, surrounded by torn paper scraps, strips of tape, ink splatter and a slash of red. Halftone grain, photocopy speckle and a faint off-register print shift run across everything. Raw, asymmetric, cut-and-paste DIY energy — punk poster, streetwear and album-cover attitude.
```

## Tips

- Short, punchy words in all-caps work best to match the harsh, cut-and-paste aesthetic of underground zines.
- Try swapping the red accent color for an acid yellow to change the visual tone while keeping the cheap two-color print look.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/grunge](https://fontvibe.ai/styles/grunge) — see [Attribution](../../README.md#attribution).
