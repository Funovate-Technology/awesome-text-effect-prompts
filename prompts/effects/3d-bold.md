---
id: 3d_bold
slug: 3d-bold
category: effects
tags: ["3d", "striking", "heavy", "chunky", "glossy", "bold", "playful"]
names:
  en: "3D Bold"
  ja: "3D 太字"
  zh: "3D 立体粗体"
  es: "3D Negrita"
  pt: "3D Negrito"
  de: "3D Fett"
description:
  en: "Chunky block capitals with deep extrusions, each letter a different glossy candy color, lit from above so highlights roll over rounded edges and colored reflections pool on the floor."
  ja: "深く押し出された極太のブロック体大文字。一文字ずつ艶のあるキャンディカラーで、上からの光がハイライトを丸い角に走らせ、床に色の映り込みが広がります。"
  zh: "厚重的方块大写字母带深度挤出，每个字母一种亮面糖果色，顶光让高光滚过圆润边角，彩色倒影落在地面上。"
  es: "Mayúsculas de bloque gruesas con extrusión profunda, cada letra en un color caramelo brillante, iluminadas desde arriba para que los brillos recorran los bordes redondeados y los reflejos de color se acumulen en el suelo."
  pt: "Maiúsculas em bloco robustas com extrusão profunda, cada letra numa cor de bala brilhante, iluminadas de cima para que os brilhos percorram as bordas arredondadas e os reflexos coloridos se espalhem pelo chão."
  de: "Wuchtige Blockversalien mit tiefer Extrusion, jeder Buchstabe in einer anderen glänzenden Bonbonfarbe, von oben beleuchtet, sodass Glanzlichter über die runden Kanten laufen und farbige Spiegelungen auf dem Boden liegen."
fontvibe_url: https://fontvibe.ai/styles/3d-bold
preview_image: https://cos.fontvibe.ai/generations/user/17/e557d84c-6e8b-4bca-bf27-ef76ea5e3d38.jpeg
examples:
  - url: https://fontvibe.ai/gallery/10695
    image: https://cos.fontvibe.ai/generations/user/17/c306e5e5-1e54-4397-b69c-405360935733.jpeg
  - url: https://fontvibe.ai/gallery/10701
    image: https://cos.fontvibe.ai/generations/user/17/8b43e1df-1a60-4220-af17-f53099f647b9.jpeg
  - url: https://fontvibe.ai/gallery/10689
    image: https://cos.fontvibe.ai/generations/user/17/3f2af287-d4f4-4fa0-af48-6ba60474d962.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "3D"
  image: ""
  passed: true
  note: "3D glossy chunky letters, spelled right."
license: CC-BY-4.0
---

# 3D Bold

> Chunky block capitals with deep extrusions, each letter a different glossy candy color, lit from above so highlights roll over rounded edges and colored reflections pool on the floor.

[![3D Bold on FontVibe](https://cos.fontvibe.ai/generations/user/17/e557d84c-6e8b-4bca-bf27-ef76ea5e3d38.jpeg)](https://fontvibe.ai/styles/3d-bold)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/3d-bold](https://fontvibe.ai/styles/3d-bold)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. The words appear as massive, chunky 3D block letters with a heavyweight extruded depth measuring around half their height. The front faces are finished in an ultra-glossy lacquer resembling a hard candy coating or high-gloss toy paint, catching bright directional key light from the upper left with natural specular highlights. Each adjacent letter features a completely different, vivid, saturated hue to maximize chromatic contrast, while their side extrusion planes appear in noticeably darker tones of the same hue with sharp, unbeveled edges. Centered prominently in the frame from a frontal view with a slight low elevation, the letters cast long, parallel 45-degree shadows across a polished dark floor that catches clean mirror reflections. The background is a deep, dark studio environment with rich atmospheric depth, subtle warm amber to cool blue gradients, faint volumetric haze, and gentle environmental color bleed from the vibrant letters.
```

Tested on `gemini-2.5-flash-image` with the text "3D" on 2026-10-30 — passed (legible, correctly spelled, recognisably this style).

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/c306e5e5-1e54-4397-b69c-405360935733.jpeg)](https://fontvibe.ai/gallery/10695) [![example](https://cos.fontvibe.ai/generations/user/17/8b43e1df-1a60-4220-af17-f53099f647b9.jpeg)](https://fontvibe.ai/gallery/10701) [![example](https://cos.fontvibe.ai/generations/user/17/3f2af287-d4f4-4fa0-af48-6ba60474d962.jpeg)](https://fontvibe.ai/gallery/10689)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
Massive chunky 3D block letters with heavyweight extruded presence — thick uniform extrusion depth of 50-60% of letter height. Front face finished in ultra-glossy lacquer, catching directional key light with natural specular reflections that graduate from bright highlight to deep saturated color — the surface quality of hard candy coating or high-gloss toy paint. Side extrusion planes in a noticeably darker shade of the same hue, creating crisp face-to-depth contrast that reads immediately as three-dimensional volume. Adjacent letters each carry a different vivid saturated color, maximizing chromatic contrast across the word — no two adjacent letters share the same hue family. Hard sharp corner edges where face meets extrusion, no beveling. Long dramatic cast shadows at consistent 45-degree angle, shadow depth approximately 40-50% of letter height. Strong directional key light from upper left. Bold, high-contrast, maximum visual impact. LETTERFORM PRIORITY: when the chosen font carries its own treatment, that font's letterform shapes take priority and own the letters; this style governs the glossy 3D extrusion, the directional lighting and the multi-color scheme. FALLBACK MATERIAL: if the font carries no material of its own, render the letters as thick glossy extruded 3D blocks with hard candy-lacquer faces and darker extrusion sides. COLOR PRIORITY: if the font specifies its own colors, keep them; otherwise give each adjacent letter a different vivid saturated hue.
```

**Scene**

```text
Massive colorful 3D block letters centered in frame, filling 75-80% of width. Each letter in a different vivid saturated color — ultra-glossy candy lacquer surface with bright circular specular highlight at center, darker extrusion sides clearly visible. Long parallel cast shadows at 45 degrees. Strong key light from upper left. Background: deep dark studio with rich atmospheric depth — subtle color gradients from warm amber to cool blue, faint volumetric haze, hints of environmental color bleed from the letters. Polished dark floor below letters showing clean mirror reflections of each letter's color. Camera: frontal view, slight low elevation. Letters fill the frame with commanding presence.
```

## Tips

- Short words or punchy acronyms with four to seven characters work best to let the heavy extrusion and distinct colors fill the frame without overcrowding.
- You can change the multi-color treatment to a tight monochromatic spectrum, like shifting shades of hot pink or electric blue, for a more unified appearance.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/3d-bold](https://fontvibe.ai/styles/3d-bold) — see [Attribution](../../README.md#attribution).
