---
id: drip_font_melting
slug: drip-font-melting
category: effects
parent: drip_font
tags: ["liquid", "drip", "glossy", "lava", "intense", "surreal"]
names:
  en: "Melting Font"
  ja: "溶けるフォント"
  zh: "融化字体"
  es: "Letras Derretidas"
  pt: "Fonte Derretida"
  de: "Schmelzschrift"
description:
  en: "Glossy orange-red letters liquefying from the base down, with molten drips, warped lower edges and a glowing puddle on a dark charcoal floor."
  ja: "下から液化していく艶のあるオレンジレッドの文字。溶けた滴、ゆがんだ下端、暗いチャコールの床に光る水たまり。"
  zh: "亮面橙红字母从底部开始液化，熔融滴落、下缘变形，深炭色地面上一滩发光的液体。"
  es: "Letras rojo anaranjado brillantes que se licúan desde la base, con goteos fundidos, bordes inferiores deformados y un charco luminoso sobre un suelo carbón oscuro."
  pt: "Letras laranja-avermelhadas brilhantes se liquefazendo a partir da base, com escorridos derretidos, bordas inferiores deformadas e uma poça luminosa num chão carvão escuro."
  de: "Glänzende orangerote Buchstaben, die von unten her flüssig werden, mit geschmolzenen Tropfen, verzogenen Unterkanten und einer leuchtenden Pfütze auf dunklem anthrazitfarbenem Boden."
fontvibe_url: https://fontvibe.ai/styles/drip-font-melting
preview_image: https://cos.fontvibe.ai/generations/user/17/51f51094-2675-49e7-93fb-b5dbebf9cc2e.jpeg
examples:
  - url: https://fontvibe.ai/gallery/11604
    image: https://cos.fontvibe.ai/generations/user/17/f49148a1-d8b2-491f-a3a5-b1a6a0b24a05.jpeg
  - url: https://fontvibe.ai/gallery/2394
    image: https://cos.fontvibe.ai/generations/user/17/95ef81a1-1f89-4bbc-abca-10068cbb83d9.jpeg
  - url: https://fontvibe.ai/gallery/2393
    image: https://cos.fontvibe.ai/generations/user/17/a9d44475-c8eb-4d4d-b5f6-053809453fff.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "MELT"
  image: ""
  passed: true
  note: "Glowing molten dripping letters; spelled right."
license: CC-BY-4.0
---

# Melting Font

> Glossy orange-red letters liquefying from the base down, with molten drips, warped lower edges and a glowing puddle on a dark charcoal floor.

[![Melting Font on FontVibe](https://cos.fontvibe.ai/generations/user/17/51f51094-2675-49e7-93fb-b5dbebf9cc2e.jpeg)](https://fontvibe.ai/styles/drip-font-melting)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/drip-font-melting](https://fontvibe.ai/styles/drip-font-melting)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. The letterforms are sculpted from a warm amber-to-deep-orange heated translucent material, actively liquefying and flowing downward under intense heat. The lower portions of {{TEXT}} lose structural integrity, their edges softening and rounding outward as gravity draws down the molten mass. Drips of varying thickness descend from the forms, featuring one to two thick primary flows with bulged origins and teardrop ends, several medium streams, and fine capillary trails showing surface tension at the drip necks. Viscous molten material pools at the letter bases with a glossy, wet sheen. An intense overhead key light bleaches the upper contours, tracing specular highlight arcs along the crest of each character. Narrow bright streaks gleam across the accumulated liquid below. An ambient heat glow radiates outward against a deep, dark background imbued with faint warm undertones, where a soft heat haze gently blurs the distant edges while maintaining razor-sharp clarity on the dripping letter surfaces.
```

Tested on `gemini-2.5-flash-image` with the text "MELT" on 2026-10-30 — passed (legible, correctly spelled, recognisably this style).

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/f49148a1-d8b2-491f-a3a5-b1a6a0b24a05.jpeg)](https://fontvibe.ai/gallery/11604) [![example](https://cos.fontvibe.ai/generations/user/17/95ef81a1-1f89-4bbc-abca-10068cbb83d9.jpeg)](https://fontvibe.ai/gallery/2394) [![example](https://cos.fontvibe.ai/generations/user/17/a9d44475-c8eb-4d4d-b5f6-053809453fff.jpeg)](https://fontvibe.ai/gallery/2393)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
letter material liquefying and flowing downward under heat — lower portions lose structural integrity, edges softening and rounding outward as gravity pulls the molten mass down. Multiple drips of varying thickness: one to two thick primary flows with slight bulge at origin and teardrop termination, two to three medium streams, fine capillary trails between them. Surface tension visible at drip necks. Viscous pooling accumulates at the letter base with a faint wet-surface sheen. When no specific material is defined, the default melt color is warm amber-to-deep-orange — the natural thermal color of heated translucent material.
```

**Scene**

```text
Intense overhead key light bleaches the top surface of the melting material, specular highlight arc running along the highest point of each character. Ambient heat glow radiates outward from the letterforms against a deep dark background with faint warm undertone — not pure black, the surrounding air carries residual heat. Glossy accumulated liquid at letter bases catches the overhead light as a narrow bright streak. Fine depth gradation: melting surface sharp, drip extremities crisp, heat haze softens at background edges.
```

## Tips

- Short words or terms related to heat, wax, or temperature naturally complement the melting effect.
- Change the warm amber tone to deep crimson, toxic green, or metallic silver to shift the style from melting resin to wax, slime, or molten metal.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/drip-font-melting](https://fontvibe.ai/styles/drip-font-melting) — see [Attribution](../../README.md#attribution).
