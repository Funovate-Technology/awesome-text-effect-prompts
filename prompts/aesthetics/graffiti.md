---
id: graffiti
slug: graffiti
category: aesthetics
tags: ["graffiti", "spray paint", "hip-hop", "drip", "outline", "street art", "rebellious", "energetic"]
names:
  en: "Graffiti"
  ja: "グラフィティ"
  zh: "涂鸦"
  es: "Grafiti"
  pt: "Grafite"
  de: "Graffiti"
description:
  en: "Wildstyle spray-paint letters with sharp arrows and overlapping shapes, filled in bright layered colors, locked in a thick black outline with drips on a red brick wall."
  ja: "鋭い矢印と重なり合う形のワイルドスタイルのスプレー文字。鮮やかな色を重ねて塗り、太い黒フチで締め、赤レンガの壁に塗料の垂れ。"
  zh: "狂野风格的喷漆字母，带尖锐箭头和重叠造型，填满层叠的鲜艳色彩，粗黑描边锁边，红砖墙上还有颜料滴痕。"
  es: "Letras wildstyle de espray con flechas afiladas y formas superpuestas, rellenas de colores vivos en capas, encerradas en un grueso contorno negro con chorreones sobre un muro de ladrillo rojo."
  pt: "Letras wildstyle de spray com setas afiadas e formas sobrepostas, preenchidas com cores vivas em camadas, presas num contorno preto grosso com escorridos sobre uma parede de tijolos vermelhos."
  de: "Wildstyle-Sprühbuchstaben mit scharfen Pfeilen und überlappenden Formen, in leuchtenden Farbschichten gefüllt, von dicker schwarzer Kontur gehalten, mit Farbläufen auf roter Backsteinwand."
fontvibe_url: https://fontvibe.ai/styles/graffiti
preview_image: https://cos.fontvibe.ai/generations/user/17/b944c4f9-3742-44c3-9b06-a977c7f2a6ee.jpeg
examples:
  - url: https://fontvibe.ai/gallery/17753
    image: https://cos.fontvibe.ai/generations/user/17/3b537b71-dfb5-4f44-b2fd-a3a5f112446d.jpeg
  - url: https://fontvibe.ai/gallery/17749
    image: https://cos.fontvibe.ai/generations/user/17/2a710d56-7008-44d1-a526-56319f05e399.jpeg
  - url: https://fontvibe.ai/gallery/17756
    image: https://cos.fontvibe.ai/generations/user/17/f6d26f3d-3d68-4497-82ef-2764e9b268b0.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "STREET"
  image: "https://cos.fontvibe.ai/opensource/text-effect-prompts/graffiti.jpg"
  passed: true
  note: "Wildstyle-adjacent spray graffiti with drips; spelled right."
license: CC-BY-4.0
---

# Graffiti

> Wildstyle spray-paint letters with sharp arrows and overlapping shapes, filled in bright layered colors, locked in a thick black outline with drips on a red brick wall.

[![Graffiti on FontVibe](https://cos.fontvibe.ai/generations/user/17/b944c4f9-3742-44c3-9b06-a977c7f2a6ee.jpeg)](https://fontvibe.ai/styles/graffiti)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/graffiti](https://fontvibe.ai/styles/graffiti)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. The words "{{TEXT}}" appear as the only legible text, rendered as a massive graffiti piece dominating a gritty urban wall of weathered red brick and textured concrete. The letters are built up in physical layers of aerosol spray paint, featuring a high-impact multi-color fade fill transitioning between hot magenta, electric blue, and vivid lime green, accented with bright white highlights. A thick, load-bearing black outline cleanly defines the letter shapes, complemented by an angled 3D block shadow that creates dramatic depth against the wall. Fine overspray mist haloes the perimeter of the piece, accompanied by spray-can mottling and scattered paint droplets. Heavy wet paint drips run naturally downward from saturated edges, pooling on the pavement below. The entire scene is illuminated by raw, natural street daylight, highlighting the authentic surface texture of the brick mortar and the vivid chromatic vibration of the fresh aerosol lacquer.
```

Generic-model test (`gemini-2.5-flash-image`, text "STREET", 2026-10-30):

![test render](https://cos.fontvibe.ai/opensource/text-effect-prompts/graffiti.jpg)

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/3b537b71-dfb5-4f44-b2fd-a3a5f112446d.jpeg)](https://fontvibe.ai/gallery/17753) [![example](https://cos.fontvibe.ai/generations/user/17/2a710d56-7008-44d1-a526-56319f05e399.jpeg)](https://fontvibe.ai/gallery/17749) [![example](https://cos.fontvibe.ai/generations/user/17/f6d26f3d-3d68-4497-82ef-2764e9b268b0.jpeg)](https://fontvibe.ai/gallery/17756)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
a wall coming alive with spray paint. PAINT: bold letters built up in physical layers of aerosol — a base fill, a thick load-bearing black outline holding the shapes, bright highlights and a 3D block shadow; paint drips run from the heavy spots, overspray mist haloes the edges, spray-can mottling and splatter droplets on the surface. COLOR: a full high-impact spray-can palette chosen for chromatic vibration — classic chrome-silver-and-black, electric blue, hot magenta, lime, orange, or multi-color fades — saturated for maximum punch at distance. GROUND: a real urban surface — red brick, grey concrete, a metal roller shutter or subway car — paint drips pooling below. LETTERFORM PRIORITY: when the chosen font carries its own treatment (wildstyle arrows, stencil bridges, marker handstyle, bubble, blockbuster, drips), that font treatment takes absolute priority and owns the letters; this style governs the spray layering, outline, drips, palette and the wall behind. FALLBACK MATERIAL: if the font carries no material of its own, spray the letters in layered aerosol with a thick black outline, bright fill, drips and overspray on a brick or concrete wall, so the graffiti energy always reads.
```

**Scene**

```text
The text dominates a real urban wall — red brick, grey concrete or a metal roller shutter — sprayed large and bold with paint drips running down to the pavement below, overspray haze around it and a couple of splatter marks. Gritty street daylight. Raw graffiti-piece energy with attitude — streetwear, hip-hop and skate culture.
```

## Tips

- Short, punchy words, street tags, or single words between three to seven letters work best with the bold, heavy geometry of aerosol graffiti.
- Change the background surface to a corrugated metal roller shutter or switch the fill to classic polished chrome with black outlines to create a distinct street aesthetic.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/graffiti](https://fontvibe.ai/styles/graffiti) — see [Attribution](../../README.md#attribution).
