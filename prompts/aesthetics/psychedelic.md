---
id: psychedelic
slug: psychedelic
category: aesthetics
tags: ["psychedelic", "1960s", "groovy", "drip", "glossy", "surreal", "funky"]
names:
  en: "Psychedelic"
  ja: "サイケデリック"
  zh: "迷幻"
  es: "Psicodélico"
  pt: "Psicodélico"
  de: "Psychedelisch"
description:
  en: "Melting glossy bubble letters in hot pink, orange and yellow, set against vibrating concentric rainbow waves with daisies and swirls."
  ja: "ホットピンク、オレンジ、黄色の溶けかけた艶のあるバブル文字。震えるような同心円の虹の波にデイジーと渦巻き。"
  zh: "融化中的亮面泡泡字，热粉、橙、黄三色，衬在振动的同心彩虹波纹上，点缀雏菊与漩涡。"
  es: "Letras burbuja brillantes que se derriten en rosa intenso, naranja y amarillo, frente a ondas de arcoíris concéntricas que vibran, con margaritas y remolinos."
  pt: "Letras bolha brilhantes derretendo em rosa-choque, laranja e amarelo, contra ondas de arco-íris concêntricas e vibrantes, com margaridas e espirais."
  de: "Schmelzende, glänzende Bubble-Buchstaben in Pink, Orange und Gelb vor vibrierenden konzentrischen Regenbogenwellen mit Gänseblümchen und Spiralen."
fontvibe_url: https://fontvibe.ai/styles/psychedelic
preview_image: https://cos.fontvibe.ai/generations/user/17/ca3f4d4d-5c4d-43e3-9115-58ed1e6a4d37.jpeg
examples:
  - url: https://fontvibe.ai/gallery/300
    image: https://cos.fontvibe.ai/generations/user/17/48e3f851-4f95-4401-bf21-573124480cf0.jpeg
  - url: https://fontvibe.ai/gallery/299
    image: https://cos.fontvibe.ai/generations/user/17/6b21005e-8289-4c1a-bb49-b5948613117f.jpeg
  - url: https://fontvibe.ai/gallery/301
    image: https://cos.fontvibe.ai/generations/user/17/4cc431ca-c83e-45bd-9b8f-e2c6d4d3819f.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "PSYCH"
  image: "https://cos.fontvibe.ai/opensource/text-effect-prompts/psychedelic.jpg"
  passed: true
  note: "Attempt 1: letters dissolve into the background pattern; hard to read. Attempt 2: melting rainbow letters on concentric op-art waves; legible, spelled right."
license: CC-BY-4.0
---

# Psychedelic

> Melting glossy bubble letters in hot pink, orange and yellow, set against vibrating concentric rainbow waves with daisies and swirls.

[![Psychedelic on FontVibe](https://cos.fontvibe.ai/generations/user/17/ca3f4d4d-5c4d-43e3-9115-58ed1e6a4d37.jpeg)](https://fontvibe.ai/styles/psychedelic)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/psychedelic](https://fontvibe.ai/styles/psychedelic)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. The text sits large and dominant in the center of the frame, rendered in glossy candy-gloss with a soft wet melting quality, drips sliding from its lower edges, and surfaces filled with vibrating rainbow color. The composition captures the aesthetic of a 1960s psychedelic concert poster under flat, even, high-key illumination that hums like a backlit print. Maximum-saturation complementary color pairs clash edge to edge—hot magenta against acid green, electric orange against cobalt blue, and cadmium yellow against violet—creating a buzzing simultaneous-contrast vibration along every flat, hard-edged, screenprint-clean boundary. Radiating outward from behind the letters to every edge is a symmetrical, hypnotic, kaleidoscopic field of concentric rainbow waves, spirals, and op-art ripples. Groovy flower-power daisies and paisley accents drift in the corners, completing an immersive visual field where {{TEXT}} is the only legible text.
```

Generic-model test (`gemini-2.5-flash-image`, text "PSYCH", 2026-10-30):

![test render](https://cos.fontvibe.ai/opensource/text-effect-prompts/psychedelic.jpg)

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/48e3f851-4f95-4401-bf21-573124480cf0.jpeg)](https://fontvibe.ai/gallery/300) [![example](https://cos.fontvibe.ai/generations/user/17/6b21005e-8289-4c1a-bb49-b5948613117f.jpeg)](https://fontvibe.ai/gallery/299) [![example](https://cos.fontvibe.ai/generations/user/17/4cc431ca-c83e-45bd-9b8f-e2c6d4d3819f.jpeg)](https://fontvibe.ai/gallery/301)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
a 1960s psychedelic poster world where saturated color is set vibrating. OPTICS / COLOR: maximum-saturation complementary pairs are placed edge to edge — hot magenta against acid green, electric orange against cobalt blue, cadmium yellow against violet — every boundary buzzing with simultaneous-contrast vibration, the defining 1960s concert-poster optical effect; color stays flat, hard-edged and screenprint-clean, never muddy or desaturated. LIGHT: flat, even, high-key illumination with no single hard source, so the whole frame hums at once like a backlit poster. FIELD: a kaleidoscopic field of concentric radiating rainbow waves, spirals and op-art ripples expands outward to every edge, framing the text. PALETTE: hot magenta, acid green, electric orange, cobalt blue, cadmium yellow, violet — full spectrum at peak saturation. LETTERFORM PRIORITY: when the chosen font defines its own surface (op-art contour bands, fluorescent blacklight glow, tie-dye fabric dye, melting drips, etc.), that font treatment takes absolute priority and owns the glyph surface — this style then governs only the surrounding color atmosphere and the vibrating field. FALLBACK MATERIAL: if the chosen font carries no material of its own, render the letters in glossy candy-gloss with a soft wet melting quality, drips sliding from their lower edges and the surfaces filled with vibrating rainbow color, so the psychedelic identity always reads.
```

**Scene**

```text
The text sits large and dominant in the center, owning the frame, wrapped in a kaleidoscopic burst of concentric rainbow waves and spirals that radiate outward from behind the letters to every edge. A few groovy flower-power daisies and paisley accents drift at the corners. Symmetrical, hypnotic, immersive — a full 1960s psychedelic concert-poster composition, the kind pasted on a ballroom wall during the Summer of Love.
```

## Tips

- Short, punchy single words or brief phrases work best, giving the heavy melting drips and radiating background waves ample space to breathe.
- Swap the corner daisies and paisley accents for geometric op-art checkerboards to give the piece a sharper, more optical-art direction.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/psychedelic](https://fontvibe.ai/styles/psychedelic) — see [Attribution](../../README.md#attribution).
