---
id: sand_stone
slug: sand-stone
category: aesthetics
tags: ["stone", "textured", "carved", "ancient", "epic", "earthy", "roman capitals"]
names:
  en: "Sand & Stone"
  ja: "砂と石"
  zh: "沙石"
  es: "Arena y Piedra"
  pt: "Areia e Pedra"
  de: "Sand & Stein"
description:
  en: "Roman-style serif capitals carved deep into warm sandstone, V-cut grooves catching amber raking light, with sedimentary grain lines across the rock."
  ja: "暖かな砂岩に深く彫ったローマン風セリフ体大文字。V字の彫り溝が琥珀色の斜光をとらえ、岩肌には堆積層の筋。"
  zh: "罗马式衬线大写字母深刻在暖色砂岩上，V 形刻槽接住琥珀色斜光，岩面带沉积层纹理。"
  es: "Mayúsculas romanas con serifa talladas a fondo en arenisca cálida, con surcos en V que captan la luz ámbar rasante y vetas sedimentarias en la roca."
  pt: "Maiúsculas romanas serifadas entalhadas fundo em arenito quente, com sulcos em V captando a luz âmbar rasante e veios sedimentares na rocha."
  de: "Römische Serifenversalien tief in warmen Sandstein gemeißelt, die V-Kerben fangen bernsteinfarbenes Streiflicht, mit Sedimentschichten im Gestein."
fontvibe_url: https://fontvibe.ai/styles/sand-stone
preview_image: https://cos.fontvibe.ai/generations/user/17/8791f87d-c0ad-4798-a85c-c059d086c2cc.jpeg
examples:
  - url: https://fontvibe.ai/gallery/14449
    image: https://cos.fontvibe.ai/generations/user/17/e72011da-878d-4542-b43d-116ff2a808e1.jpeg
  - url: https://fontvibe.ai/gallery/14433
    image: https://cos.fontvibe.ai/generations/user/17/29687f14-da62-4893-8c96-8dba676bc9f7.jpeg
  - url: https://fontvibe.ai/gallery/14442
    image: https://cos.fontvibe.ai/generations/user/17/a2ae3c51-443a-4434-9f13-8f6ed88f11fb.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "ANCIENT"
  image: "https://cos.fontvibe.ai/opensource/text-effect-prompts/sand_stone.jpg"
  passed: true
  note: "Letters carved into a sandstone cliff; spelled right."
license: CC-BY-4.0
---

# Sand & Stone

> Roman-style serif capitals carved deep into warm sandstone, V-cut grooves catching amber raking light, with sedimentary grain lines across the rock.

[![Sand & Stone on FontVibe](https://cos.fontvibe.ai/generations/user/17/8791f87d-c0ad-4798-a85c-c059d086c2cc.jpeg)](https://fontvibe.ai/styles/sand-stone)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/sand-stone](https://fontvibe.ai/styles/sand-stone)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. The letters appear as deep, irreversible physical carvings in an ancient desert stone face. Chiseled in sharp V-cut bas-relief grooves, the freshly cut interior sections expose pale cream-beige rock that contrasts boldly with the weathered, amber-ochre and warm sienna exterior. Horizontal sedimentary grain lines, mineral oxidation staining, and fine micro-pitting from wind erosion run across the letters, with specks of loose quartz sand settled into their bases. A low-angle raking sidelight from the lower-left at a shallow twenty-degree angle sweeps across the rock, casting deep amber-brown shadow pools into the carved grooves and accentuating every textural ridge, patina unevenness, and incised edge. The scene is set against a dark desert earth ground under a warm golden-hour haze with fine airborne dust. The entire composition strictly adheres to a warm geological palette of cream, terracotta red, and burnt umber without cool tones or modern polished surfaces, making {{TEXT}} the sole legible text in the image.
```

Generic-model test (`gemini-2.5-flash-image`, text "ANCIENT", 2026-10-30):

![test render](https://cos.fontvibe.ai/opensource/text-effect-prompts/sand_stone.jpg)

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/e72011da-878d-4542-b43d-116ff2a808e1.jpeg)](https://fontvibe.ai/gallery/14449) [![example](https://cos.fontvibe.ai/generations/user/17/29687f14-da62-4893-8c96-8dba676bc9f7.jpeg)](https://fontvibe.ai/gallery/14433) [![example](https://cos.fontvibe.ai/generations/user/17/a2ae3c51-443a-4434-9f13-8f6ed88f11fb.jpeg)](https://fontvibe.ai/gallery/14442)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
Text exists as an irreversible physical mark in ancient earth material — carved stone, incised desert varnish, or painted adobe plaster. Not digitally rendered.

MATERIAL TRACKS:
— Classic Stone / Bas-Relief: warm stone face; iron oxide banding shifts from cream-beige at fresh chisel cuts to amber-ochre across weathered exterior; V-cut groove interiors filled with warm amber shadow; fresh-cut sections reveal lighter stone against darker aged surface — color contrast defines dimensional depth.
— Desert Sandstone: amber-ochre to rose-red stone body; horizontal sedimentary grain lines; micro-pitting from wind erosion; fine quartz sand at letter bases.
— Petroglyph / Varnish Stone: near-black desert varnish patina on rock; scratch channels cut through to pale tan unweathered stone — high contrast between pale interior and dark patina.
— Adobe / Painted Earth: sun-baked buff terracotta plaster; warm red-ochre to burnt sienna pigment; sand aggregate and trowel marks visible through thin paint; hairline drying cracks at pigment edges.

STONE LAWS (all tracks):
— Low-angle raking sidelight from left at 15–25° grazes every surface — reveals grain, carving depth, micro-texture, patina unevenness.
— Geological color palette: cream-beige / amber-ochre / warm sienna / burnt umber / terracotta red / iron brown. No cool tones.
— All surfaces carry age: patina, oxidation staining, erosion pitting, mineral banding.
— Cut and incised sections always expose lighter, fresher material against dark weathered exterior.

FORBIDDEN: neon, digital glow, chrome, smooth modern surfaces, gradient fills, drop shadows, cool tones.

When no specific material is defined by the font: default environment — warm amber raking sidelight from lower-left at 20° angle, deep amber-brown shadow pools in surface recesses, dark desert earth background.
```

**Scene**

```text
Ancient stone or desert rock face as the material ground. Warm raking sidelight from lower-left at a shallow 20° angle — light grazes every carved groove, incised channel, and surface grain; amber-shadow pools fill all recesses, making depth and texture fully legible. Background: near-black or deep warm-brown desert earth, dry dust atmosphere with golden-hour haze. Close examination viewpoint — camera close enough to reveal sedimentary grain lines, micro-pitting, and patina unevenness. Warm ochre-amber-sienna color throughout. No cool tones.
```

## Tips

- Short, punchy words, monumental titles, or ancient place names look especially natural carved into heavy geological stone.
- To shift the variant, swap the carved stone description for incised petroglyph scratches revealing pale rock through a dark desert varnish, or painted red-ochre on sun-baked adobe plaster.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/sand-stone](https://fontvibe.ai/styles/sand-stone) — see [Attribution](../../README.md#attribution).
