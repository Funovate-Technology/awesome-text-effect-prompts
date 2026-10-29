---
id: stencil
slug: stencil
category: aesthetics
tags: ["stencil", "distressed", "spray paint", "industrial", "chunky", "raw", "rugged", "military"]
names:
  en: "Stencil"
  ja: "ステンシル"
  zh: "镂空喷绘"
  es: "Stencil"
  pt: "Stencil"
  de: "Schablone"
description:
  en: "Olive-green military stencil capitals with bridged gaps and soft overspray, sprayed onto weathered wooden crate boards with metal corner plates."
  ja: "ブリッジの切れ目と柔らかな吹き付けのにじみがあるオリーブグリーンの軍用ステンシル大文字。金属の角当てのある古い木箱の板にスプレー。"
  zh: "橄榄绿军用镂空模板大写字母，带连接桥断口和柔和喷溅边，喷在钉有金属护角的旧木箱板上。"
  es: "Mayúsculas de plantilla militar verde oliva con puentes y un suave rociado, pintadas con espray sobre tablas de cajón de madera envejecida con esquinas metálicas."
  pt: "Maiúsculas de estêncil militar verde-oliva com pontes e um spray suave, pintadas sobre tábuas de caixote de madeira envelhecida com cantoneiras de metal."
  de: "Olivgrüne Militär-Schablonenversalien mit Stegen und weichem Sprühnebel, gesprüht auf verwitterte Holzkistenbretter mit Metallecken."
fontvibe_url: https://fontvibe.ai/styles/stencil
preview_image: https://cos.fontvibe.ai/generations/user/17/3c53fc61-1f2d-4377-99cb-a3babbd68230.jpeg
examples:
  - url: https://fontvibe.ai/gallery/13557
    image: https://cos.fontvibe.ai/generations/user/17/4ef77a7c-c233-4a0b-91c8-a2c54d2571be.jpeg
  - url: https://fontvibe.ai/gallery/13558
    image: https://cos.fontvibe.ai/generations/user/17/e90acc03-d1b4-43e8-b27a-0c12b8af71c8.jpeg
  - url: https://fontvibe.ai/gallery/13560
    image: https://cos.fontvibe.ai/generations/user/17/c045fe8c-481e-4d08-bb3c-3c2564e13438.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "CARGO"
  image: "https://cos.fontvibe.ai/opensource/text-effect-prompts/stencil.jpg"
  passed: true
  note: "Spray-stencilled letters on concrete; spelled right."
license: CC-BY-4.0
---

# Stencil

> Olive-green military stencil capitals with bridged gaps and soft overspray, sprayed onto weathered wooden crate boards with metal corner plates.

[![Stencil on FontVibe](https://cos.fontvibe.ai/generations/user/17/3c53fc61-1f2d-4377-99cb-a3babbd68230.jpeg)](https://fontvibe.ai/styles/stencil)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/stencil](https://fontvibe.ai/styles/stencil)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. The lettering is applied in a stencil spray application aesthetic, rendered in matte black spray paint onto an aged, rough concrete grey wall. Paint deposited through a physical cut template forms the letters, featuring crisp inner boundaries contrasted with subtle, soft outer halos where overspray has bled beyond the masking edges. Stroke centers have the highest pigment density, thinning out toward the peripheries, with a few occasional drip runs descending from areas of heavy paint buildup. The rugged texture and aggregate of the concrete substrate show visibly through the thinner coverage of the matte paint. Harsh directional light strikes from directly above at a low raking angle, casting deep micro-shadows across the pitted surface imperfections of the concrete and accentuating the binary, industrial contrast. The text {{TEXT}} is large and centered, dominating the frame as the sole legible wording, with the weathered industrial concrete surface extending continuously to all edges.
```

Generic-model test (`gemini-2.5-flash-image`, text "CARGO", 2026-10-30):

![test render](https://cos.fontvibe.ai/opensource/text-effect-prompts/stencil.jpg)

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/4ef77a7c-c233-4a0b-91c8-a2c54d2571be.jpeg)](https://fontvibe.ai/gallery/13557) [![example](https://cos.fontvibe.ai/generations/user/17/e90acc03-d1b4-43e8-b27a-0c12b8af71c8.jpeg)](https://fontvibe.ai/gallery/13558) [![example](https://cos.fontvibe.ai/generations/user/17/c045fe8c-481e-4d08-bb3c-3c2564e13438.jpeg)](https://fontvibe.ai/gallery/13560)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
Stencil spray application aesthetic — the visual language of pigment applied through a physical template onto an industrial surface.

SPRAY MEDIUM: paint deposited through a cut template creates the defining edge characteristics — hard inner boundary where stencil material masked the surface, soft outer halo where overspray bled beyond the template edge. Paint density peaks at the center of strokes, thins toward periphery. Drip runs descend from areas of heavy paint application. The spray medium is matte and pigment-dense, completely unlike liquid or digital media.

COLOR REGIME: maximum contrast two-tone palette — the stencil process is inherently binary. Primary combinations: black on concrete grey, military olive on weathered wood, white on rusted metal, warning red on industrial steel. The surface beneath always participates: substrate texture shows through thinner paint coverage, grounding the mark in physical space.

SURFACE CONTEXT: stencil typography implies a physical surface — concrete wall, wooden crate, corrugated metal, canvas fabric. The substrate texture is visible through and around the paint layer, never a neutral void. Surface imperfections coexist naturally with the spray marks.

When no specific material is defined by the font: default spray environment — matte black spray paint on rough concrete grey surface, visible overspray halo at letter edges, slight texture of concrete aggregate showing through paint.
```

**Scene**

```text
Text fills the frame, large and centered on an aged concrete wall surface. Harsh directional light from directly above at a low raking angle, illuminating the surface sharply. Industrial environment — wall texture extends to all frame edges, no soft elements.
```

## Tips

- Short, punchy words, warnings, or utilitarian codes work best to match the functional industrial aesthetic.
- To create a different setting, swap the concrete wall and black paint for warning red spray paint on industrial steel or military olive on weathered wood crates.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/stencil](https://fontvibe.ai/styles/stencil) — see [Attribution](../../README.md#attribution).
