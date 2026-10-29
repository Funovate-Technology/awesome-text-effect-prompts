---
id: metallic
slug: metallic
category: effects
tags: ["chrome", "metallic", "industrial", "cold", "gold", "3d", "powerful"]
names:
  en: "Metallic"
  ja: "メタリック"
  zh: "金属"
  es: "Metálico"
  pt: "Metálico"
  de: "Metallic"
description:
  en: "Beveled 3D capitals mixing polished gold and brushed steel, with sharp highlight lines and a cool reflective floor under directional studio light."
  ja: "磨いた金とヘアラインのスチールを組み合わせた面取りの3D大文字。鋭いハイライトの線、方向性のあるスタジオ光の下で冷たい反射床に映ります。"
  zh: "斜面 3D 大写字母混合抛光金与拉丝钢，高光线条锐利，在定向影棚光下倒映在冷色反光地面上。"
  es: "Mayúsculas 3D biseladas que combinan oro pulido y acero cepillado, con líneas de brillo nítidas y un suelo reflectante frío bajo luz direccional de estudio."
  pt: "Maiúsculas 3D chanfradas combinando ouro polido e aço escovado, com linhas de brilho nítidas e um piso refletor frio sob luz direcional de estúdio."
  de: "Abgeschrägte 3D-Versalien aus poliertem Gold und gebürstetem Stahl, mit scharfen Glanzlinien auf einem kühlen, spiegelnden Boden im gerichteten Studiolicht."
fontvibe_url: https://fontvibe.ai/styles/metallic
preview_image: https://cos.fontvibe.ai/generations/user/17/b16e73f6-131b-449e-acbb-4a5846cf122f.jpeg
examples:
  - url: https://fontvibe.ai/gallery/10617
    image: https://cos.fontvibe.ai/generations/user/17/cfd02d85-be34-4fce-ba0e-f27f5dc27827.jpeg
  - url: https://fontvibe.ai/gallery/10631
    image: https://cos.fontvibe.ai/generations/user/17/8d10f859-4e25-4d08-b9a0-219baa487a1c.jpeg
  - url: https://fontvibe.ai/gallery/10644
    image: https://cos.fontvibe.ai/generations/user/17/bfe5b6da-c06d-4d94-adf5-4befad707cb1.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "METAL"
  image: ""
  passed: true
  note: "Brushed-steel 3D letters with reflection; spelled right."
license: CC-BY-4.0
---

# Metallic

> Beveled 3D capitals mixing polished gold and brushed steel, with sharp highlight lines and a cool reflective floor under directional studio light.

[![Metallic on FontVibe](https://cos.fontvibe.ai/generations/user/17/b16e73f6-131b-449e-acbb-4a5846cf122f.jpeg)](https://fontvibe.ai/styles/metallic)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/metallic](https://fontvibe.ai/styles/metallic)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. The letters appear as bold, 3D extruded forms crafted from solid brushed steel with a tactile matte-satin finish and subtle horizontal grain texture. The metallic surfaces interact dynamically with light, displaying realistic directional anisotropic highlight streaks and razor-sharp edge highlight compression along the beveled planes. Colored in cool industrial grey with soft steel undertones, the letters exhibit wide specular highlight gradients transitioning smoothly into rich shadow zones that subtly catch ambient environmental reflections. The scene is illuminated by a focused studio key light from the upper-left at a forty-five-degree angle, casting crisp, defined shadows, while a subtle secondary fill light from the lower-right ensures distinct edge separation. The composition is set against an atmospheric deep charcoal-to-steel-blue gradient backdrop, with the typography resting on a dark reflective ground plane that mirrors the metallic forms with precision clarity.
```

Tested on `gemini-2.5-flash-image` with the text "METAL" on 2026-10-30 — passed (legible, correctly spelled, recognisably this style).

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/cfd02d85-be34-4fce-ba0e-f27f5dc27827.jpeg)](https://fontvibe.ai/gallery/10617) [![example](https://cos.fontvibe.ai/generations/user/17/8d10f859-4e25-4d08-b9a0-219baa487a1c.jpeg)](https://fontvibe.ai/gallery/10631) [![example](https://cos.fontvibe.ai/generations/user/17/bfe5b6da-c06d-4d94-adf5-4befad707cb1.jpeg)](https://fontvibe.ai/gallery/10644)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
Rendered as bold 3D extruded letters with realistic metal surface physics — two signature material tracks: brushed steel with directional anisotropic highlight streaks across the surface, matte-satin finish, subtle horizontal grain texture, industrial grey with cool undertones; and gold/trophy with warm amber-yellow color temperature, wide smooth specular gradient from bright highlight to deep shadow, achievement trophy polish and weight. Supporting track: chrome/mirror for high-contrast metallic accent work. Core optical behavior rules across all tracks: wide specular highlight gradient (not a point highlight), ambient reflection in shadow zones capturing environmental color, material-specific color temperature held consistently, edge highlight compression where bevel planes meet. Never flat grey paint — always show the metal's interaction with light. Dark industrial background to maximize material contrast. LETTERFORM PRIORITY: when the chosen font carries its own treatment, that font's letterform shapes take priority and own the letters; this style governs the metal-surface physics, the specular lighting and the finish. FALLBACK MATERIAL: if the font carries no material of its own, render the letters as bold 3D-extruded metal — brushed steel or polished gold/trophy with a wide specular gradient and compressed edge highlights. COLOR PRIORITY: keep the font's own colors if specified; otherwise hold the chosen metal's color temperature — cool steel grey or warm trophy gold.
```

**Scene**

```text
Deep charcoal-to-steel-blue gradient background — industrial atmosphere with subtle environmental depth, not pure black. Studio key light from upper-left at 45 degrees, creating strong directional specular highlights and crisp cast shadows. Warm secondary fill light from lower-right adding separation. Letter surfaces show brushed grain texture or warm gold gradient depending on material. Dark reflective platform below with subtle material reflection. Ultra-clean precision manufacturing atmosphere.
```

## Tips

- Short words or single titles in capital letters work best to showcase the heavy beveling and metallic reflections.
- Change the cool steel grey and anisotropic grain to warm amber-gold with a smooth trophy polish to shift the atmosphere from industrial to celebratory.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/metallic](https://fontvibe.ai/styles/metallic) — see [Attribution](../../README.md#attribution).
