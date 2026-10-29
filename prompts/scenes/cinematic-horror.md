---
id: cinematic_horror
slug: cinematic-horror
category: scenes
parent: cinematic
tags: ["cracked", "scary", "eerie", "macabre", "cinematic", "drip"]
names:
  en: "Horror Movie"
  ja: "ホラー映画"
  zh: "恐怖电影"
  es: "Película de Terror"
  pt: "Filme de Terror"
  de: "Horrorfilm"
description:
  en: "Horror movie title lettering with cracked, blood-stained surfaces and dim sickly lighting. Perfect for Halloween designs, thriller posters, and dark atmospheric visuals."
  ja: "ひび割れて血に染まった表面と、薄暗く不気味な照明で表現するホラー映画タイトル風のレタリングです。ハロウィンのデザインやスリラーのポスター、闇の雰囲気を漂わせるビジュアルにぴったりです。"
  zh: "恐怖电影片名字体，带裂纹、血渍表面和昏暗病态的光线。特别适合 Halloween 设计、惊悚片海报和阴森氛围的画面。"
  es: "Letras de título de película de terror con superficies agrietadas y manchadas de sangre, y una iluminación tenue y enfermiza. Ideal para diseños de Halloween, pósters de suspenso y visuales oscuros llenos de atmósfera."
  pt: "Letras de título de filme de terror com superfícies rachadas e manchadas de sangue e uma iluminação fraca e doentia. Perfeito para designs de Halloween, pôsteres de suspense e visuais escuros cheios de atmosfera."
  de: "Horrorfilm-Titelschrift mit rissigen, blutverschmierten Oberflächen und trübem, kränklichem Licht — die Horror-Schrift für Halloween-Designs, Thriller-Poster und dunkle, atmosphärische Visuals."
fontvibe_url: https://fontvibe.ai/styles/cinematic-horror
preview_image: https://cos.fontvibe.ai/generations/user/17/370cce37-5784-475a-a78d-d5d9b45ed65d.jpeg
examples:
  - url: https://fontvibe.ai/gallery/12917
    image: https://cos.fontvibe.ai/generations/user/17/67760eb2-b3fd-49ea-a54a-b943d0147e0f.jpeg
  - url: https://fontvibe.ai/gallery/12915
    image: https://cos.fontvibe.ai/generations/user/17/59aafda5-fdbc-4b50-b112-d61b6e7e896f.jpeg
  - url: https://fontvibe.ai/gallery/12929
    image: https://cos.fontvibe.ai/generations/user/17/55ecd3cc-c437-4da8-9c0b-23ba06783728.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "DREAD"
  image: "https://cos.fontvibe.ai/opensource/text-effect-prompts/cinematic_horror.jpg"
  passed: true
  note: "Weathered, dripping title in a cold dark scene; spelled right."
license: CC-BY-4.0
---

# Horror Movie

> Horror movie title lettering with cracked, blood-stained surfaces and dim sickly lighting. Perfect for Halloween designs, thriller posters, and dark atmospheric visuals.

[![Horror Movie on FontVibe](https://cos.fontvibe.ai/generations/user/17/370cce37-5784-475a-a78d-d5d9b45ed65d.jpeg)](https://fontvibe.ai/styles/cinematic-horror)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/cinematic-horror](https://fontvibe.ai/styles/cinematic-horror)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. The title typography exists completely inside a desolate cinematic horror environment, centered in a wide cinematic frame and filling sixty-five to eighty percent of the frame width. The distressed surfaces of the letters bear physical evidence of horror, marked with dried blood seepage along crack lines, heavy rust oxidation staining, deep decay, and weathered age damage. Illumination comes entirely from a single, psychologically unsettling light source: a cold blue-green underlight positioned at ground level, casting long, hard-edged vertical shadows that rise upward into absolute darkness. Extreme tonal contrast dominates the composition, with oppressive black shadows occupying at least sixty percent of the frame. Dense, heavy fog pools around the base of the letters while disturbed dust hangs suspended in the air. The camera angle is slightly too low and canted to create unease, utilizing vast, active negative space where darkness conceals an unspoken threat.
```

Generic-model test (`gemini-2.5-flash-image`, text "DREAD", 2026-10-30):

![test render](https://cos.fontvibe.ai/opensource/text-effect-prompts/cinematic_horror.jpg)

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/67760eb2-b3fd-49ea-a54a-b943d0147e0f.jpeg)](https://fontvibe.ai/gallery/12917) [![example](https://cos.fontvibe.ai/generations/user/17/59aafda5-fdbc-4b50-b112-d61b6e7e896f.jpeg)](https://fontvibe.ai/gallery/12915) [![example](https://cos.fontvibe.ai/generations/user/17/55ecd3cc-c437-4da8-9c0b-23ba06783728.jpeg)](https://fontvibe.ai/gallery/12929)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
Cinematic horror movie title typography. The scene dominates -- letterforms exist inside a complete horror world, not placed in front of a background.

CINEMATIC HORROR RULES (apply to every shot):
- Single light source. Psychologically wrong origin: a bulb too dim, daylight too harsh, a glow with no identifiable source. One light. Hard edges.
- Extreme tonal contrast: deep shadow occupies at least 60% of the frame. The darkness is not empty -- it contains the threat.
- Negative space is active: what is NOT shown is more frightening than what is shown. Leave room for the unseen.
- The camera angle is wrong: slightly too low, too close, or canted in a way that creates unease.
- NOT balanced composition. NOT safe. NOT studio light. NOT neutral background.

ATMOSPHERE: physical presence, not decorative effect. Fog has weight and source. Dust is disturbed by something. The air itself carries wrong information.

LETTER SURFACE FALLBACK (when font defines no specific material):
Letters carry the evidence of horror -- surfaces show dried blood seepage along crack lines, rust oxidation staining, decay marks, or age damage. NOT clean. NOT neutral. The letters have been through something.
```

**Scene**

```text
Wide cinematic frame. Title text centered, filling 65-80% of frame width. Cold blue-green underlight source at ground level casting long vertical shadows rising above letters into absolute darkness above. Dense fog layer pooling at letter bases. Desolate horror atmosphere.
```

## Tips

- Short, punchy words or single-word titles maximize the active negative space and amplify the sense of isolation.
- Change the cold blue-green underlight to a sickly pale yellow or dim crimson to alter the psychological tone of the scene.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/cinematic-horror](https://fontvibe.ai/styles/cinematic-horror) — see [Attribution](../../README.md#attribution).
