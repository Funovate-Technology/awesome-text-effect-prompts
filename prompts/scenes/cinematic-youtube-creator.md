---
id: cinematic_youtube_creator
slug: cinematic-youtube-creator
category: scenes
parent: cinematic
tags: ["outline", "energetic", "striking", "chunky", "cinematic", "bold", "glow", "condensed"]
names:
  en: "Video Creator"
  ja: ""
  zh: ""
  es: ""
  pt: ""
  de: ""
description:
  en: "Tall condensed sans capitals in warm yellow with a dark outline and glow, a small episode line above, over a golden-hour city rooftop."
  ja: "暖かな黄色に濃いフチと光彩をつけた縦長サンセリフの大文字。上に小さなエピソード表記、背景はゴールデンアワーの街の屋上。"
  zh: "高窄无衬线大写字母，暖黄色配深色描边与辉光，上方一行小字集数，背景是黄金时刻的城市楼顶。"
  es: "Mayúsculas sans serif altas y condensadas en amarillo cálido con contorno oscuro y resplandor, una pequeña línea de episodio encima, sobre una azotea urbana en la hora dorada."
  pt: "Maiúsculas sans serif altas e condensadas em amarelo quente com contorno escuro e brilho, uma pequena linha de episódio acima, sobre um terraço urbano na hora dourada."
  de: "Hohe, schmale serifenlose Versalien in warmem Gelb mit dunkler Kontur und Glow, darüber eine kleine Episodenzeile, vor einer Stadtdachterrasse zur goldenen Stunde."
fontvibe_url: https://fontvibe.ai/styles/cinematic-youtube-creator
preview_image: https://cos.fontvibe.ai/generations/user/17/f62eb4f9-659f-4d5a-a2ea-41f10582dba8.jpeg
examples:
  - url: https://fontvibe.ai/gallery/7012
    image: https://cos.fontvibe.ai/generations/user/17/1b202fd6-0dae-496a-b9c0-e5e2d6d4c253.jpeg
  - url: https://fontvibe.ai/gallery/7013
    image: https://cos.fontvibe.ai/generations/user/17/33623642-815f-4760-b8fc-8bde6dda9662.jpeg
  - url: https://fontvibe.ai/gallery/7018
    image: https://cos.fontvibe.ai/generations/user/17/b2fc7367-3094-4d1f-ae1c-8cb2a2e50c38.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "CREATOR"
  image: "https://cos.fontvibe.ai/opensource/text-effect-prompts/cinematic_youtube_creator.jpg"
  passed: true
  note: "Attempt 1: legible, but silver letters rather than the style's warm yellow with dark outline — not recognisably this style. Attempt 2: warm glowing letters over a golden-hour city rooftop; spelled right (lighter than the preview's yellow)."
license: CC-BY-4.0
---

# Video Creator

> Tall condensed sans capitals in warm yellow with a dark outline and glow, a small episode line above, over a golden-hour city rooftop.

[![Video Creator on FontVibe](https://cos.fontvibe.ai/generations/user/17/f62eb4f9-659f-4d5a-a2ea-41f10582dba8.jpeg)](https://fontvibe.ai/styles/cinematic-youtube-creator)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/cinematic-youtube-creator](https://fontvibe.ai/styles/cinematic-youtube-creator)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. Modern, energetic, and high-visibility letterforms are designed with a confident, bold presence suited for digital screens. The letters are finished in a vibrant palette of bold white and warm amber with luminous, glowing backlit edges. Position the text prominently in the center with strong directional lighting that creates clear visual hierarchy and sharp depth. The scene takes place on an urban rooftop during golden hour, with warm amber sunlight flooding the environment while a dusky, deep-toned city skyline rests softly blurred in the background. Rich shadows in the cityscape contrast dramatically with the illuminated lettering. A faint touch of cinematic film grain textures the atmosphere, enhancing the contemporary video creator aesthetic while ensuring {{TEXT}} remains the only legible text in the entire image.
```

Generic-model test (`gemini-2.5-flash-image`, text "CREATOR", 2026-10-30):

![test render](https://cos.fontvibe.ai/opensource/text-effect-prompts/cinematic_youtube_creator.jpg)

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/1b202fd6-0dae-496a-b9c0-e5e2d6d4c253.jpeg)](https://fontvibe.ai/gallery/7012) [![example](https://cos.fontvibe.ai/generations/user/17/33623642-815f-4760-b8fc-8bde6dda9662.jpeg)](https://fontvibe.ai/gallery/7013) [![example](https://cos.fontvibe.ai/generations/user/17/b2fc7367-3094-4d1f-ae1c-8cb2a2e50c38.jpeg)](https://fontvibe.ai/gallery/7018)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
video creator title typography. Modern, energetic, high-visibility letterforms designed for digital screens and video thumbnails. Vibrant yet controlled color palette — warm amber, bright cyan, electric yellow or bold white against rich dark backgrounds. Dynamic scene backgrounds: urban streets, rooftops at golden hour, neon-lit city nights, or cinematic outdoor vistas. Strong directional lighting with clear focal hierarchy. Clean typographic structure supporting multi-line titles: channel name / episode title / series indicator. Film grain optional. Contemporary video creator aesthetic — confident, bold, watchable.
```

**Scene**

```text
Urban rooftop at golden hour, warm amber light flooding the scene, city skyline blurred behind. The letters glow with warm backlight against the dusky cityscape. Three-layer typography structure: dominant channel name, secondary subtitle, minimal series indicator.
```

## Tips

- Short, punchy words or single-title phrases in all caps best capture the high-impact thumbnail look.
- Change the golden hour rooftop setting to a neon-lit city street with bright cyan and electric yellow accents for a cool-toned nighttime variation.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/cinematic-youtube-creator](https://fontvibe.ai/styles/cinematic-youtube-creator) — see [Attribution](../../README.md#attribution).
