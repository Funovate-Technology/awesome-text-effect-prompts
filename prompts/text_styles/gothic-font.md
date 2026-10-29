---
id: gothic_font
slug: gothic-font
category: text_styles
tags: ["blackletter", "formal", "condensed", "gold", "ink", "medieval", "gothic", "regal", "high contrast"]
names:
  en: "Gothic Font"
  ja: "ゴシックフォント"
  zh: "哥特字体"
  es: "Letras Góticas"
  pt: "Fonte Gótica"
  de: "Gotische Schrift"
description:
  en: "Precise Textura blackletter: narrow broken strokes, diamond terminals and strong thick-thin contrast, in black ink with gold-touched edges on dark aged parchment."
  ja: "端正なテクストゥーラのブラックレター。細く折れる線、菱形の筆端、強い太細の差を、金でふちどった黒インクで暗い古い羊皮紙に。"
  zh: "严谨的 Textura 哥特黑体：窄长的折笔、菱形笔端和强烈粗细对比，黑墨带金色描边，写在深色旧羊皮纸上。"
  es: "Blackletter Textura precisa: trazos estrechos y quebrados, remates en rombo y fuerte contraste grueso-fino, en tinta negra con toques dorados sobre pergamino oscuro y envejecido."
  pt: "Blackletter Textura precisa: traços estreitos e quebrados, terminais em losango e forte contraste grosso-fino, em tinta preta com toques dourados sobre pergaminho escuro e envelhecido."
  de: "Präzise Textura-Fraktur: schmale, gebrochene Striche, rautenförmige Enden und starker Kontrast von dick und dünn, in schwarzer Tinte mit Goldakzenten auf dunklem, altem Pergament."
fontvibe_url: https://fontvibe.ai/styles/gothic-font
preview_image: https://cos.fontvibe.ai/generations/user/17/26ed817a-5f55-43cc-ab2d-869e9e5a18ed.jpeg
examples:
  - url: https://fontvibe.ai/gallery/3905
    image: https://cos.fontvibe.ai/generations/user/17/e7bc42f9-51ed-4c95-bde0-f3e7c7780664.jpeg
  - url: https://fontvibe.ai/gallery/3909
    image: https://cos.fontvibe.ai/generations/user/17/fbd7ffa0-3454-4922-b9d1-403372d87e31.jpeg
  - url: https://fontvibe.ai/gallery/3910
    image: https://cos.fontvibe.ai/generations/user/17/55871572-2118-4aa5-b3d2-6bc74f846d04.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "Gothic"
  image: "https://cos.fontvibe.ai/opensource/text-effect-prompts/gothic_font.jpg"
  passed: true
  note: "Gilded blackletter on a parchment scroll; spelled right."
license: CC-BY-4.0
---

# Gothic Font

> Precise Textura blackletter: narrow broken strokes, diamond terminals and strong thick-thin contrast, in black ink with gold-touched edges on dark aged parchment.

[![Gothic Font on FontVibe](https://cos.fontvibe.ai/generations/user/17/26ed817a-5f55-43cc-ab2d-869e9e5a18ed.jpeg)](https://fontvibe.ai/styles/gothic-font)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/gothic-font](https://fontvibe.ai/styles/gothic-font)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character, ensuring it is the only legible text in the image. The letters are crafted in precise gothic blackletter calligraphy, characterized by diamond-shaped stroke terminals, dramatic thick-thin contrast, and pointed arch counters. Each glyph demonstrates medieval scribal precision, executed in rich black ink with warm undertones and refined gold ink highlights accenting the serifs and capitals. The lettering stands clean and unweathered, focused entirely on pure typographic craft without cobwebs or rust. In the background, dark parchment merges into a medieval cathedral interior lined with soaring stone arches that gently fade into distant fog. Warm candlelight flickers across nearby stone surfaces, curling ribbons of incense smoke drift through the air, and a solitary shaft of pale moonlight filters through a broken stained glass window, subtly illuminating the dark, solemn environment around the text.
```

Generic-model test (`gemini-2.5-flash-image`, text "Gothic", 2026-10-30):

![test render](https://cos.fontvibe.ai/opensource/text-effect-prompts/gothic_font.jpg)

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/e7bc42f9-51ed-4c95-bde0-f3e7c7780664.jpeg)](https://fontvibe.ai/gallery/3905) [![example](https://cos.fontvibe.ai/generations/user/17/fbd7ffa0-3454-4922-b9d1-403372d87e31.jpeg)](https://fontvibe.ai/gallery/3909) [![example](https://cos.fontvibe.ai/generations/user/17/55871572-2118-4aa5-b3d2-6bc74f846d04.jpeg)](https://fontvibe.ai/gallery/3910)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
rendered in precise gothic blackletter letterforms with authentic calligraphic construction — diamond-shaped stroke terminals, strong thick-thin contrast, pointed arch counters. Rich black ink with warm depth on dark parchment or deep charcoal background. Subtle gold ink highlights on serifs and capitals. Medieval scribal precision. No cobwebs, no rust, no atmospheric fog — pure typographic craft. LETTERFORM PRIORITY: when the chosen font carries its own treatment, that font's letterform shapes take priority and own the letters; this style governs the rich ink, the parchment ground and the subtle gold highlights. FALLBACK MATERIAL: if the font carries no material of its own, render the letters as precise gothic blackletter in rich black ink with subtle gold highlights on dark parchment — pure typographic craft, no cobwebs, rust or fog. COLOR PRIORITY: keep the font's own colors if specified; otherwise black ink with warm gold accents.
```

**Scene**

```text
Medieval cathedral interior with stone arches fading into fog, candlelight flickering on nearby surfaces, shaft of pale moonlight from broken stained glass window, incense smoke curling through the air.
```

## Tips

- Short Latin phrases, solemn titles, or single words in Title Case showcase the ornate blackletter capitals and rhythmic vertical strokes best.
- Adjust the lighting balance between the warm flickering candlelight and the pale shaft of moonlight to make the mood feel either intimate or cold and haunting.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/gothic-font](https://fontvibe.ai/styles/gothic-font) — see [Attribution](../../README.md#attribution).
