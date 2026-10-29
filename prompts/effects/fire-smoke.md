---
id: fire_smoke
slug: fire-smoke
category: effects
tags: ["fire", "smoke", "burnt", "energetic", "aggressive", "intense"]
names:
  en: "Fire & Smoke"
  ja: "炎と煙"
  zh: "火焰与烟雾"
  es: "Fuego y Humo"
  pt: "Fogo e Fumaça"
  de: "Feuer & Rauch"
description:
  en: "Blazing fire and smoke effects, dramatic heat waves and ember glow."
  ja: "燃え盛る炎と煙のエフェクト、劇的な熱波と燃え残りの輝きを表現します。"
  zh: "熊熊燃烧的火焰与烟雾特效，戏剧化的热浪和余烬光芒。"
  es: "Efectos ardientes de fuego y humo, ondas de calor dramáticas y el brillo de las brasas."
  pt: "Efeitos ardentes de fogo e fumaça, ondas de calor dramáticas e o brilho das brasas."
  de: "Lodernde Feuer- und Raucheffekte, dramatische Hitzewellen und Glutschein – eine Feuer Schrift, die wirklich brennt."
fontvibe_url: https://fontvibe.ai/styles/fire-smoke
preview_image: https://cos.fontvibe.ai/generations/user/17/d83cc3c9-414b-4dc6-b720-1f7cddfebb68.jpeg
examples:
  - url: https://fontvibe.ai/gallery/9829
    image: https://cos.fontvibe.ai/generations/user/17/b9848548-5aaf-41e0-8b74-8fa8dc5dd408.jpeg
  - url: https://fontvibe.ai/gallery/9849
    image: https://cos.fontvibe.ai/generations/user/17/e0c0de36-fa6c-4224-854d-fd284107b485.jpeg
  - url: https://fontvibe.ai/gallery/9845
    image: https://cos.fontvibe.ai/generations/user/17/e49eacd0-3efc-41b8-8f7f-5c2d3a8f8615.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "BLAZE"
  image: "https://cos.fontvibe.ai/opensource/text-effect-prompts/fire_smoke.jpg"
  passed: true
  note: "Letters made of flame with smoke; spelled right."
license: CC-BY-4.0
---

# Fire & Smoke

> Blazing fire and smoke effects, dramatic heat waves and ember glow.

[![Fire & Smoke on FontVibe](https://cos.fontvibe.ai/generations/user/17/d83cc3c9-414b-4dc6-b720-1f7cddfebb68.jpeg)](https://fontvibe.ai/styles/fire-smoke)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/fire-smoke](https://fontvibe.ai/styles/fire-smoke)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. The letters are sculpted from active combustion, appearing fully ablaze with a brilliant white-yellow inner core that transitions outward through radiant orange and deep fiery red into turbulent flame tongues surging upward with natural random motion. Faint wispy blue-grey tips lick at the outer edges of the flames. Dense, dark smoke billows from the letters in heavy rolling columns, curling upward in charcoal and near-black volumes with faint translucency along the borders. Intense firelight self-illuminates from below with a warm amber-orange cast, creating a dramatic upward rim along the heat source underneath. Glowing embers drift upward through the surrounding space. The background consists of a deep charcoal haze with a faint ember glow, producing dramatic contrast between the combustion glow and the surrounding darkness as heavy smoke curls into the black above.
```

Generic-model test (`gemini-2.5-flash-image`, text "BLAZE", 2026-10-30):

![test render](https://cos.fontvibe.ai/opensource/text-effect-prompts/fire_smoke.jpg)

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/b9848548-5aaf-41e0-8b74-8fa8dc5dd408.jpeg)](https://fontvibe.ai/gallery/9829) [![example](https://cos.fontvibe.ai/generations/user/17/e0c0de36-fa6c-4224-854d-fd284107b485.jpeg)](https://fontvibe.ai/gallery/9849) [![example](https://cos.fontvibe.ai/generations/user/17/e49eacd0-3efc-41b8-8f7f-5c2d3a8f8615.jpeg)](https://fontvibe.ai/gallery/9845)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
Real combustion physics: white-yellow inner core transitioning through orange and deep red to wispy blue-grey outer tips. Turbulent flame tongues surge upward with natural random motion. Dense dark smoke billows in heavy rolling columns, curling upward — charcoal and near-black with faint translucency at edges. Firelight self-illuminates from below with warm amber-orange cast. Dramatic upward rim from intense heat source underneath. Background: deep charcoal haze with faint ember glow — not pure black. Cinematic fire photography quality. LETTERFORM PRIORITY: when the chosen font carries its own treatment, that font's letterform shapes take priority and own the letters; this style governs the flame-and-smoke material, the combustion glow and the cast light. FALLBACK MATERIAL: if the font carries no material of its own, render the letters ablaze — a white-yellow core through orange to deep red flame tongues with dark rolling smoke and warm self-illumination from below. COLOR PRIORITY: keep the font's own colors if specified; otherwise the natural fire spectrum of amber, orange and deep red.
```

**Scene**

```text
Deep black background with dramatic contrast between the fire glow and the surrounding darkness, glowing embers drifting upward, a warm amber cast lighting the haze, heavy smoke curling into the black above.
```

## Tips

- Short, punchy words work best, as rising flame tongues and thick rolling smoke can obscure dense or lengthy text.
- To vary the mood, adjust the balance between the billowing dark smoke and the brilliant white-yellow flame core to suggest either a smoldering burn or an intense inferno.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/fire-smoke](https://fontvibe.ai/styles/fire-smoke) — see [Attribution](../../README.md#attribution).
