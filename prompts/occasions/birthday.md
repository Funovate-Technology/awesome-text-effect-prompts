---
id: birthday
slug: birthday
category: occasions
tags: ["energetic", "cheerful", "festive", "outline", "bold"]
names:
  en: "Birthday"
  ja: "バースデー"
  zh: "生日"
  es: "Cumpleaños"
  pt: "Aniversário"
  de: "Geburtstag"
description:
  en: "Rainbow-striped bubbly capitals with a crisp white outline, surrounded by confetti bursts and balloon clusters on a saturated pink-to-turquoise party background."
  ja: "白フチのくっきりした虹色ストライプの丸い大文字。紙吹雪と風船の束に囲まれ、ピンクからターコイズへの鮮やかなパーティー背景。"
  zh: "彩虹条纹的圆胖大写字母带清晰白描边，四周是彩纸屑和气球簇，背景是饱和的粉色到青绿派对渐变。"
  es: "Mayúsculas abombadas con rayas de arcoíris y un nítido contorno blanco, rodeadas de confeti y racimos de globos sobre un fondo festivo saturado de rosa a turquesa."
  pt: "Maiúsculas arredondadas com listras de arco-íris e contorno branco nítido, cercadas por confete e cachos de balões num fundo de festa saturado do rosa ao turquesa."
  de: "Runde Versalien mit Regenbogenstreifen und klarer weißer Kontur, umgeben von Konfetti und Luftballontrauben vor einem satten Partyhintergrund von Pink bis Türkis."
fontvibe_url: https://fontvibe.ai/styles/birthday
preview_image: https://cos.fontvibe.ai/generations/user/17/be25ff51-8983-4ddb-90f5-d4da8d5faddb.jpeg
examples:
  - url: https://fontvibe.ai/gallery/34672
    image: https://cos.fontvibe.ai/generations/user/17/85564306-d646-468c-a1c0-17f163ae46ee.jpeg
  - url: https://fontvibe.ai/gallery/34674
    image: https://cos.fontvibe.ai/generations/user/17/5275a368-9de0-4b02-b7c1-6b8fd5cc43b0.jpeg
  - url: https://fontvibe.ai/gallery/34675
    image: https://cos.fontvibe.ai/generations/user/17/4241ba7b-c3e8-4f10-bf46-fdebec87ec62.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "HAPPY BD"
  image: "https://cos.fontvibe.ai/opensource/text-effect-prompts/birthday.jpg"
  passed: true
  note: "Balloon letters with confetti and balloons; spelled right."
license: CC-BY-4.0
---

# Birthday

> Rainbow-striped bubbly capitals with a crisp white outline, surrounded by confetti bursts and balloon clusters on a saturated pink-to-turquoise party background.

[![Birthday on FontVibe](https://cos.fontvibe.ai/generations/user/17/be25ff51-8983-4ddb-90f5-d4da8d5faddb.jpeg)](https://fontvibe.ai/styles/birthday)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/birthday](https://fontvibe.ai/styles/birthday)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. Ensure {{TEXT}} is the only legible text in the image. The letters are styled as bold, glossy party lettering featuring a crisp white outline and gleaming surface highlights, with each letter rendered in a different vivid, punchy saturated party color. A soft drop shadow separates the letters cleanly from the setting. The background is a bright, high-energy celebration scene featuring a rich, saturated gradient shifting smoothly from hot-pink into vibrant tangerine. A dense, dynamic burst of multicolor confetti scatters through the air around the words, complemented by luminous sparkles and bright light streaks. Generous clusters of colorful party balloons frame the outer edges of the composition. The entire space is bathed in bright, festive party light with sparkling glints, creating vibrant color contrast that keeps the scene joyful and high-energy.
```

Generic-model test (`gemini-2.5-flash-image`, text "HAPPY BD", 2026-10-30):

![test render](https://cos.fontvibe.ai/opensource/text-effect-prompts/birthday.jpg)

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/85564306-d646-468c-a1c0-17f163ae46ee.jpeg)](https://fontvibe.ai/gallery/34672) [![example](https://cos.fontvibe.ai/generations/user/17/5275a368-9de0-4b02-b7c1-6b8fd5cc43b0.jpeg)](https://fontvibe.ai/gallery/34674) [![example](https://cos.fontvibe.ai/generations/user/17/4241ba7b-c3e8-4f10-bf46-fdebec87ec62.jpeg)](https://fontvibe.ai/gallery/34675)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
a bright, high-energy birthday celebration scene — vivid, saturated and punchy. BACKGROUND: bright and celebratory but with REAL color saturation — a bold party backdrop such as a vivid candy-color field, a rich saturated gradient (e.g. hot-pink into tangerine, or turquoise into violet), or a confetti-packed party sky; luminous and cheerful, never muddy or grey, but NOT a washed-out pale pastel wash and NOT a flat near-white ground — enough color and contrast for the text to pop off the background. Bright lively party light with sparkling glints. ATMOSPHERE: a dense energetic burst of multicolor confetti and generous clustered balloons framing the composition, sparkles and light streaks — festive and high-energy, keeping the text clearly legible. LETTERFORM COLOR: when the chosen font defines its own color (rainbow, foil, candy, neon, holographic) keep it fully — bold multi-color and per-letter rainbow are welcome and encouraged; otherwise render the letters in vivid saturated party colors, either bright multi-color (each letter or word a different punchy hue) or one or two bold dominant hues, always with strong contrast and a crisp white outline or soft drop shadow so the letters pop. Never dull, washed-out or muddy. LETTERFORM PRIORITY: when the chosen font carries its own treatment (balloon, bubble, foil, script, sticker, rainbow, neon, drip, candy), that treatment takes absolute priority and owns the letters; this style governs only the bright saturated party light, confetti, balloons and palette — never the letter shapes. FALLBACK: if the font carries no material of its own, render bold glossy party lettering with a crisp outline and bright highlight in vivid saturated colors, so the birthday energy reads strong. GROUND: keep the space bright (not a dark night stage) but rich with saturated color, never pale or empty. Render the exact text provided, with no extra or altered words.
```

**Scene**

```text
A bright, high-energy birthday scene on a vivid saturated party background — bold candy color or a rich party gradient (not a pale pastel wash, not near-white), with dense multicolor confetti bursting through the air and generous balloon clusters framing the edges, sparkles and light streaks. Strong color and contrast so the text pops. Festive, punchy, joyful party energy.
```

## Tips

- Short names, celebratory exclamations, or birthday milestones work best to give the confetti and balloons plenty of room to frame the words.
- To shift the mood, change the hot-pink and tangerine backdrop gradient to turquoise and violet while keeping the multicolor confetti.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/birthday](https://fontvibe.ai/styles/birthday) — see [Attribution](../../README.md#attribution).
