---
id: drip_font_blood
slug: drip-font-blood
category: effects
parent: drip_font
tags: ["drip", "wet", "scary", "macabre", "gothic"]
names:
  en: "Blood Drip Font"
  ja: "血のしたたるフォント"
  zh: "血滴字体"
  es: "Letras de Sangre"
  pt: "Fonte de Sangue"
  de: "Bluttropfen-Schrift"
description:
  en: "Bold crimson letters with a wet, dark-red surface and long blood drips ending in round drops, isolated on pure black under side light."
  ja: "濡れた暗赤色の表面を持つ太い深紅の文字。長い血の滴は丸い粒で終わり、横からの光を受けて真っ黒な背景に浮かびます。"
  zh: "粗体深红字母，表面湿润暗红，长长的血滴末端凝成圆珠，在侧光下孤立于纯黑背景。"
  es: "Letras carmesí gruesas con una superficie roja oscura y húmeda y largos goteos de sangre que terminan en gotas redondas, aisladas sobre negro puro con luz lateral."
  pt: "Letras carmesim grossas com superfície vermelho-escura e molhada e longos escorridos de sangue terminando em gotas redondas, isoladas sobre preto puro com luz lateral."
  de: "Kräftige karminrote Buchstaben mit nasser, dunkelroter Oberfläche und langen Blutläufen, die in runden Tropfen enden, freigestellt auf reinem Schwarz im Seitenlicht."
fontvibe_url: https://fontvibe.ai/styles/drip-font-blood
preview_image: https://cos.fontvibe.ai/generations/user/17/f38864d6-1b55-4b4a-a49b-73adaf3989f6.jpeg
examples:
  - url: https://fontvibe.ai/gallery/10257
    image: https://cos.fontvibe.ai/generations/user/17/cfea9c42-dace-4577-b8ae-907dc5cf1866.jpeg
  - url: https://fontvibe.ai/gallery/10259
    image: https://cos.fontvibe.ai/generations/user/17/018d67f8-b9c1-4a38-a9b2-ac36c204264a.jpeg
  - url: https://fontvibe.ai/gallery/10258
    image: https://cos.fontvibe.ai/generations/user/17/4e78d8c6-dd7a-4383-9020-b3940c6bd858.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "BLOOD"
  image: ""
  passed: true
  note: "Glossy red dripping letters on black; spelled right."
license: CC-BY-4.0
---

# Blood Drip Font

> Bold crimson letters with a wet, dark-red surface and long blood drips ending in round drops, isolated on pure black under side light.

[![Blood Drip Font on FontVibe](https://cos.fontvibe.ai/generations/user/17/f38864d6-1b55-4b4a-a49b-73adaf3989f6.jpeg)](https://fontvibe.ai/styles/drip-font-blood)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/drip-font-blood](https://fontvibe.ai/styles/drip-font-blood)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. The letters are rendered as thick, viscous crimson blood fluid exhibiting authentic gravity-driven fluid behavior. Large tear-shaped drops hang suspended with visible surface tension at each drip terminus, while connecting streams thin as they descend past the letter baselines toward the lower third. The fluid displays a color gradient transitioning from bright arterial red on active drip paths to deep, near-black clot tones where the blood accumulates and pools. Material properties include subsurface scattering that imparts a deep red inner glow, high specular gloss across wet convex drip heads, and matte-dark textures in dense clotted sections. The text is positioned in the center frame with generous breathing room against a pure black void background devoid of any ambient fill or decoration. A single cold key light positioned at a forty-five-degree angle from the upper-left strikes the wet surfaces, creating intense specular peaks while casting deep, sharp shadows toward the lower-right.
```

Tested on `gemini-2.5-flash-image` with the text "BLOOD" on 2026-10-30 — passed (legible, correctly spelled, recognisably this style).

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/cfea9c42-dace-4577-b8ae-907dc5cf1866.jpeg)](https://fontvibe.ai/gallery/10257) [![example](https://cos.fontvibe.ai/generations/user/17/018d67f8-b9c1-4a38-a9b2-ac36c204264a.jpeg)](https://fontvibe.ai/gallery/10259) [![example](https://cos.fontvibe.ai/generations/user/17/4e78d8c6-dd7a-4383-9020-b3940c6bd858.jpeg)](https://fontvibe.ai/gallery/10258)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
Thick crimson blood saturating every surface — viscous, high-density fluid with authentic physical behavior: large tear-shaped drops suspended at each drip terminus with surface tension visible at the meniscus, connecting streams thinning as they extend downward, deep near-black pooling where blood accumulates. Material properties: subsurface scattering gives deep red glow when backlit, specular gloss on convex drip surfaces catching directional light, matte-dark at clotted pooling zones. Blood color gradient from bright arterial red (#CC0000) at active drip streams to near-black clot (#3D0000) at base pools. Gravity-driven physics — every drip pulled downward with anatomically accurate tension. Horror film practical effects quality — not painted, not stylized, photorealistic blood. LETTERFORM PRIORITY: when the chosen font carries its own treatment, that font's letterform shapes take priority and own the letters; this style governs the viscous blood fluid physics, the suspended drips and the pooling. FALLBACK MATERIAL: if the font carries no material of its own, render the letters as viscous crimson blood letters with tear-shaped drops held by surface tension, thinning connecting streams and near-black pooling. COLOR PRIORITY: keep the font's own colors if specified; otherwise arterial red (#CC0000) grading to near-black clot (#3D0000).
```

**Scene**

```text
Pure black void background — zero ambient fill, maximum contrast for crimson blood reads. Single cold key light from upper-left at 45° strikes letterform surfaces and ignites specular peaks on wet blood drip heads; cast shadows fall lower-right, deep and sharp. Letters occupy center frame with generous breathing room. Blood drips descend past the baseline toward lower-third, heaviest drip formations on letters with large surface area. No background decoration — only letters, blood, and darkness.
```

## Tips

- Short words with broad, solid letter shapes give the fluid physics more surface area to generate heavy, dramatic drips and clots.
- To modify the mood, adjust the single key light from cold white to a warm amber or sickly pale green tone.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/drip-font-blood](https://fontvibe.ai/styles/drip-font-blood) — see [Attribution](../../README.md#attribution).
