---
id: drip_font
slug: drip-font
category: effects
tags: ["liquid", "drip", "urban", "raw", "heavy", "glossy", "street art", "aggressive"]
names:
  en: "Drip Font"
  ja: "ドリップフォント"
  zh: "滴落字体"
  es: "Letras Chorreantes"
  pt: "Fonte Pingando"
  de: "Drip Font"
description:
  en: "Heavy glossy red block letters with thick paint drips hanging from every base, teardrop ends and pooled paint on the floor, against a dark concrete wall."
  ja: "艶のある極太の赤いブロック体。すべての文字の下から太い塗料が垂れ、先端は涙形、床には塗料だまり。背景は暗いコンクリートの壁。"
  zh: "粗重亮面的红色方块字，每个字底都挂着浓稠颜料滴，末端成泪滴状，地面积着颜料，背景是深色水泥墙。"
  es: "Letras de bloque rojas, gruesas y brillantes con espesos chorreones de pintura colgando de cada base, puntas en forma de lágrima y pintura acumulada en el suelo, frente a un muro de hormigón oscuro."
  pt: "Letras em bloco vermelhas, grossas e brilhantes com escorridos espessos de tinta pendendo de cada base, pontas em gota e tinta empoçada no chão, diante de uma parede de concreto escura."
  de: "Dicke, glänzende rote Blockbuchstaben, an jeder Grundlinie hängen zähe Farbtropfen mit tropfenförmigen Enden, Farbpfützen auf dem Boden, vor einer dunklen Betonwand."
fontvibe_url: https://fontvibe.ai/styles/drip-font
preview_image: https://cos.fontvibe.ai/generations/user/17/b97be45e-e274-46f2-883e-56455388d608.jpeg
examples:
  - url: https://fontvibe.ai/gallery/9359
    image: https://cos.fontvibe.ai/generations/user/17/5c7494e6-ae08-49a8-82e1-15298875b568.jpeg
  - url: https://fontvibe.ai/gallery/9379
    image: https://cos.fontvibe.ai/generations/user/17/7ba65c94-5233-4999-b25d-181ba27aea1c.jpeg
  - url: https://fontvibe.ai/gallery/9372
    image: https://cos.fontvibe.ai/generations/user/17/2ee30a6f-b534-476e-9ae1-c0c94d072106.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "DRIP"
  image: "https://cos.fontvibe.ai/opensource/text-effect-prompts/drip_font.jpg"
  passed: true
  note: "Glossy paint-drip letters on a graffiti wall; spelled right (blue rather than the preview's red)."
license: CC-BY-4.0
---

# Drip Font

> Heavy glossy red block letters with thick paint drips hanging from every base, teardrop ends and pooled paint on the floor, against a dark concrete wall.

[![Drip Font on FontVibe](https://cos.fontvibe.ai/generations/user/17/b97be45e-e274-46f2-883e-56455388d608.jpeg)](https://fontvibe.ai/styles/drip-font)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/drip-font](https://fontvibe.ai/styles/drip-font)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. The bold letterforms are constructed entirely from thick, glossy liquid paint, reading as three-dimensional liquid-material objects built from saturated, vivid electric blue pigment. Smooth high-gloss surfaces catch bright specular highlights across the curved tops and letter edges. Heavy tear-shaped drip extensions hang from the bases of the letters with realistic fluid physics and surface tension, showing viscous trails of varying lengths that thin before breaking into rounded points. Tangible paint depth is visible at every contour, casting distinct drip shadows underneath. The text is set against an urban street art wall of dark concrete or brick, where thick, cascading paint trails gather and pool along the ground line. The drips catch ambient light from below, creating deep shadows between the drops and bright glints at the curved top of each falling bead of paint.
```

Generic-model test (`gemini-2.5-flash-image`, text "DRIP", 2026-10-30):

![test render](https://cos.fontvibe.ai/opensource/text-effect-prompts/drip_font.jpg)

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/5c7494e6-ae08-49a8-82e1-15298875b568.jpeg)](https://fontvibe.ai/gallery/9359) [![example](https://cos.fontvibe.ai/generations/user/17/7ba65c94-5233-4999-b25d-181ba27aea1c.jpeg)](https://fontvibe.ai/gallery/9379) [![example](https://cos.fontvibe.ai/generations/user/17/2ee30a6f-b534-476e-9ae1-c0c94d072106.jpeg)](https://fontvibe.ai/gallery/9372)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
Bold letterforms constructed from thick glossy liquid paint — letter bodies appear built from saturated pigment material with smooth high-gloss surface catching specular highlights. Heavy tear-shaped drip extensions hang from letter bases with realistic surface tension, viscous fluid trails of varying lengths, pigment pooling at the base. Each letterform reads as a 3D liquid-material object: glossy top surface, drip shadows underneath, paint depth visible at letter edges. Realistic liquid physics: drops taper to rounded points, trails thin before breaking.

Color direction: choose paint color based on text meaning and mood — FIRE / RAGE / HEAT → vivid red-orange; TOXIC / ALIEN / ACID → neon yellow-green; OCEAN / FROST / ICE → electric cyan-blue; GOLD / ROYAL / CROWN → rich metallic gold; SHADOW / VOID / DARK → deep violet-black; CANDY / SWEET / POP → hot pink; default → vivid electric blue with high saturation.
```

**Scene**

```text
Urban street art wall — dark concrete or brick surface, paint drips catching ambient light from below, raw graffiti energy. Thick glossy paint trails cascade from letter bases with surface tension visible at each drip head. Deep shadow between drips, bright specular glint at the curved top of each drop. Paint pooling at the ground line.
```

## Tips

- Short, punchy words work best to give the heavy dripping trails enough vertical space to stretch and pool without overlapping neighboring letters.
- Change the paint color to match the tone of your word, such as neon yellow-green for acidic themes, fiery red-orange for heat, or metallic gold for a luxurious look.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/drip-font](https://fontvibe.ai/styles/drip-font) — see [Attribution](../../README.md#attribution).
