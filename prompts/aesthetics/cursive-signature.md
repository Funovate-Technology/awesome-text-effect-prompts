---
id: cursive_signature
slug: cursive-signature
category: aesthetics
parent: cursive
tags: ["handwritten", "ink", "refined", "confident", "intimate", "flowing", "minimal", "connected"]
names:
  en: "Signature Script"
  ja: "サインスクリプト"
  zh: "签名手写体"
  es: "Firma Manuscrita"
  pt: "Assinatura Manuscrita"
  de: "Unterschrift-Schreibschrift"
description:
  en: "A hand-signed autograph: one fluid pen line with a dominant capital, small connected letters and a long underline swash, in flat blue-black ink on white paper."
  ja: "手書きのサイン。一本の流れる線で、目立つ頭文字に小さくつながる文字、最後に長いアンダーラインのスワッシュ。白い紙に青黒いインク。"
  zh: "亲笔签名：一笔流畅连成，首字母突出、后续小写相连，末尾一道长下划线花饰，蓝黑墨水写在白纸上。"
  es: "Una firma autógrafa: una sola línea fluida con una inicial dominante, minúsculas pequeñas enlazadas y un largo subrayado ornamental, en tinta negro azulada sobre papel blanco."
  pt: "Um autógrafo assinado à mão: uma única linha fluida com uma inicial dominante, minúsculas pequenas ligadas e um longo sublinhado ornamental, em tinta preto-azulada sobre papel branco."
  de: "Eine handschriftliche Unterschrift: eine einzige fließende Linie mit markantem Anfangsbuchstaben, kleinen verbundenen Buchstaben und einem langen Unterstreichungsschwung, in blauschwarzer Tinte auf weißem Papier."
fontvibe_url: https://fontvibe.ai/styles/cursive-signature
preview_image: https://cos.fontvibe.ai/generations/user/17/bceb5c8b-153d-4eea-8f3a-b71bd5928453.jpeg
examples:
  - url: https://fontvibe.ai/gallery/29716
    image: https://cos.fontvibe.ai/generations/user/17/28f0dd20-dfdb-4bc0-b4b5-f4fb5fef1acf.jpeg
  - url: https://fontvibe.ai/gallery/29717
    image: https://cos.fontvibe.ai/generations/user/17/116f85c0-0f7a-4b6c-88e4-f351f0dc535c.jpeg
  - url: https://fontvibe.ai/gallery/29781
    image: https://cos.fontvibe.ai/generations/user/17/bc0e17b5-3747-4c07-9e48-7ccb26139ff7.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "Signature"
  image: "https://cos.fontvibe.ai/opensource/text-effect-prompts/cursive_signature.jpg"
  passed: true
  note: "Signature-style ink script on white; spelled right."
license: CC-BY-4.0
---

# Signature Script

> A hand-signed autograph: one fluid pen line with a dominant capital, small connected letters and a long underline swash, in flat blue-black ink on white paper.

[![Signature Script on FontVibe](https://cos.fontvibe.ai/generations/user/17/bceb5c8b-153d-4eea-8f3a-b71bd5928453.jpeg)](https://fontvibe.ai/styles/cursive-signature)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/cursive-signature](https://fontvibe.ai/styles/cursive-signature)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. The lettering is captured as an authentic hand-signed autograph, laid down in one confident pass as a real pen signature. The line work displays a fine matte pen-ink line with natural fountain-pen texture in a rich, dark blue-black ink. The stroke shows subtle ink pooling where curves turn and faint, natural pen-skips where the nib momentarily lifts from the surface, completely free of gloss, metallic reflections, or artificial embellishments. The name sits large and centered with generous negative space across a plain, crisp white document card stock with an understated, tactile paper surface. The scene is illuminated by soft, even daylight resembling gentle desk light, casting no dramatic shadows and keeping the writing flat, crisp, and fully legible. The overall atmosphere feels personal, confident, and genuine, capturing the authentic mark of an everyday handwritten signature.
```

Generic-model test (`gemini-2.5-flash-image`, text "Signature", 2026-10-30):

![test render](https://cos.fontvibe.ai/opensource/text-effect-prompts/cursive_signature.jpg)

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/28f0dd20-dfdb-4bc0-b4b5-f4fb5fef1acf.jpeg)](https://fontvibe.ai/gallery/29716) [![example](https://cos.fontvibe.ai/generations/user/17/116f85c0-0f7a-4b6c-88e4-f351f0dc535c.jpeg)](https://fontvibe.ai/gallery/29717) [![example](https://cos.fontvibe.ai/generations/user/17/bc0e17b5-3747-4c07-9e48-7ccb26139ff7.jpeg)](https://fontvibe.ai/gallery/29781)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
captured as an authentic hand-signed autograph. SURFACE / INK: the name is laid down in one confident pass as a real pen signature — a fine ballpoint or fountain-pen line in flat matte ink, with natural pen texture: subtle ink pooling where strokes turn, faint pen-skips where the nib lifts, no gloss, no metallic, no decorative shine. GROUND: a plain, real signing surface — crisp white document or card stock, a signed letter or contract, a clean notebook page or a soft neutral paper — understated and everyday, with generous space so the name reads. LIGHT: even, natural, document-like — soft flat daylight or a gentle desk light, minimal drama, the signature reading clear and legible the way a real autograph does. ATMOSPHERE: personal, confident and authentic — the feel of a genuine hand-signed name or personal-brand mark, dashed off yet unmistakably distinctive. LETTERFORM PRIORITY: when the chosen font carries its own treatment, that font's letterform shapes and personal flourishes take priority and own the letters; this style governs only the ink surface, ground and light, never the letter shapes. When no specific material is defined by the font: a fine matte pen-ink line with natural ballpoint or fountain-pen texture in a single flat ink color, on the clean paper ground. COLOR: if the font declares its own color keep it; otherwise the ink reads as a deep classic signing tone — near-black or a dark blue-black — on the light paper ground.
```

**Scene**

```text
The name sits large and centered with generous negative space on a plain, real signing surface — crisp white document or card stock, a signed letter or a clean notebook page. Even soft daylight reads the signature flat and clear, the way a real autograph does. Personal, confident, authentic hand-signed feel.
```

## Tips

- Personal names, single titles, or short words work best to capture the natural rhythm and confident flow of a genuine signature.
- Change the ink tone to near-black or place the writing on an aged notebook page to vary the type of stationery.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/cursive-signature](https://fontvibe.ai/styles/cursive-signature) — see [Attribution](../../README.md#attribution).
