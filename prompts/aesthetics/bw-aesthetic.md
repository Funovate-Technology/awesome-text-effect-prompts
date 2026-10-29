---
id: bw_aesthetic
slug: bw-aesthetic
category: aesthetics
tags: ["noir", "cinematic", "anime", "analog", "dark", "melancholic", "mysterious", "intimate"]
names:
  en: "Black & White Aesthetic"
  ja: "モノクロ・エステティック"
  zh: "黑白氛围"
  es: "Estética Blanco y Negro"
  pt: "Estética Preto e Branco"
  de: "Schwarz-Weiß-Ästhetik"
description:
  en: "Moody black-and-white portraits cropped close in deep shadow, with hard side light, rain and smoke, heavy film grain, a soft vignette and at most one small red accent."
  ja: "深い影の中に寄ったモノクロの人物、硬いサイド光、雨と煙、強いフィルムグレイン、やわらかな周辺減光、赤は最大でひとつだけ。"
  zh: "深阴影里的近景黑白人像，硬侧光、雨和烟雾、浓重的胶片颗粒、柔和暗角，最多一处小小的红色点缀。"
  es: "Retratos en blanco y negro muy cerca y en sombra profunda, con luz lateral dura, lluvia y humo, grano de película intenso, viñeta suave y como mucho un detalle rojo."
  pt: "Retratos em preto e branco bem de perto e em sombra profunda, com luz lateral dura, chuva e fumaça, granulação forte de filme, vinheta suave e no máximo um detalhe vermelho."
  de: "Stimmungsvolle Schwarz-Weiß-Porträts nah und im tiefen Schatten, mit hartem Seitenlicht, Regen und Rauch, starkem Filmkorn, weicher Vignette und höchstens einem kleinen roten Akzent."
fontvibe_url: https://fontvibe.ai/styles/bw-aesthetic
preview_image: https://cos.fontvibe.ai/generations/user/17/7eece551-0b15-4fe1-abab-f0d51b9657a2.jpeg
examples:
  - url: https://fontvibe.ai/gallery/87775
    image: https://cos.fontvibe.ai/generations/user/17/b4e5c924-82f0-44e4-a280-2f04d5b4d883.jpeg
  - url: https://fontvibe.ai/gallery/87824
    image: https://cos.fontvibe.ai/generations/user/17/71566b76-cc0e-4d9a-b136-a7e6de2d1bf4.jpeg
  - url: https://fontvibe.ai/gallery/87850
    image: https://cos.fontvibe.ai/generations/user/17/0bdb0c13-1ca4-46e2-931d-040668c08a9c.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "MOOD"
  image: "https://cos.fontvibe.ai/opensource/text-effect-prompts/bw_aesthetic.jpg"
  passed: true
  note: "Moody black-and-white rain portrait with the word legible; spelled right."
license: CC-BY-4.0
---

# Black & White Aesthetic

> Moody black-and-white portraits cropped close in deep shadow, with hard side light, rain and smoke, heavy film grain, a soft vignette and at most one small red accent.

[![Black & White Aesthetic on FontVibe](https://cos.fontvibe.ai/generations/user/17/7eece551-0b15-4fe1-abab-f0d51b9657a2.jpeg)](https://fontvibe.ai/styles/bw-aesthetic)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/bw-aesthetic](https://fontvibe.ai/styles/bw-aesthetic)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. The scene is a moody, high-contrast black-and-white portrait featuring a single figure cropped close in three-quarter view, surrounded by deep negative black space. Hard, single-source side lighting carves out the form from the darkness, producing crushed blacks alongside bright, sharp highlights across wet skin, hair, and falling rain streaks. The surrounding atmosphere contains drifting smoke, reflections on wet pavement, and softly blurred nocturnal streetlights. The entire composition is captured in monochrome tones of black, white, and greys, textured with prominent film grain, shallow depth of field, and a soft dark vignette at the corners. The letters of {{TEXT}} sit quietly and subtly positioned within the dark negative space beside the subject, illuminated by the same directional side light in matte white and pale grey tones, remaining the sole legible writing in the image.
```

Generic-model test (`gemini-2.5-flash-image`, text "MOOD", 2026-10-30):

![test render](https://cos.fontvibe.ai/opensource/text-effect-prompts/bw_aesthetic.jpg)

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/b4e5c924-82f0-44e4-a280-2f04d5b4d883.jpeg)](https://fontvibe.ai/gallery/87775) [![example](https://cos.fontvibe.ai/generations/user/17/71566b76-cc0e-4d9a-b136-a7e6de2d1bf4.jpeg)](https://fontvibe.ai/gallery/87824) [![example](https://cos.fontvibe.ai/generations/user/17/0bdb0c13-1ca4-46e2-931d-040668c08a9c.jpeg)](https://fontvibe.ai/gallery/87850)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
the kind of moody black-and-white picture people set as a profile picture, split into a matching pair for two accounts, use as a phone wallpaper or put on a poster or album cover. GRAPHIC LANGUAGE: one subject large and close, usually a face or figure in three-quarter view or seen from behind, cropped tight with deep black space around it; rain streaks, drifting smoke, wet city-night reflections, blurred street lights or a lone window as the setting. For a matching pair the canvas splits into two equal halves, each half a complete square portrait with its face centred in that half, the two figures turned toward each other or sharing one continuous background (one umbrella, one street, one moon). LIGHT: hard single-source side light carving half the face out of darkness, crushed blacks, bright highlights on wet hair, rain and skin. COLOUR: pure black, white and greys only; optionally ONE small deep red accent (a rose, lips, a scarf, a red thread) in one place per picture, one per half in a pair. TEXTURE: visible film grain over the whole image and a soft dark vignette at the corners. TIERS: the ink illustration tier is a manga-style inked portrait with solid brush-black hair, fine hatching and dot screentone shading on white paper; the film photo tier looks like grainy black-and-white photography, shallow depth of field, slight motion blur, pushed high-ISO grain. No real people, celebrities or brand logos. LETTERFORM COLOR PRIORITY: if the selected font defines its own letterform colour or material, that takes absolute priority; the black, white and grey palette colours the letters only when the font does not specify. ATMOSPHERE: the black-and-white image, the film grain, the dark vignette and the hard side light always fill the picture around the words regardless of letterform colour. When no specific material is defined by the font: default lighting - the words sit small and quiet in the dark negative space beside the subject, under the same hard side light.
```

## Tips

- Short, single-word texts or understated titles work best, allowing the deep negative space and moody lighting to dominate the frame.
- Introduce a single subtle deep red accent, such as a rose or a thread, to create a dramatic selective-color contrast against the monochrome scene.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/bw-aesthetic](https://fontvibe.ai/styles/bw-aesthetic) — see [Attribution](../../README.md#attribution).
