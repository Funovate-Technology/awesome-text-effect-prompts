---
id: glass_color
slug: glass-color
category: effects
parent: glass
tags: ["transparent", "glass", "modern", "cheerful", "dazzling"]
names:
  en: "Color Glass"
  ja: "カラーガラス"
  zh: "彩色玻璃"
  es: "Vidrio de Color"
  pt: "Vidro Colorido"
  de: "Farbglas"
description:
  en: "Thick solid glass letters, each a different jewel tone, casting colored light pools and caustic fans across a bright white studio floor."
  ja: "一文字ずつ違う宝石色の、厚く中身の詰まったガラス文字。明るい白いスタジオの床に色の光だまりとコースティクスの扇を落とします。"
  zh: "厚实的实心玻璃字母，每个字母一种宝石色，在明亮的白色影棚地面上投出彩色光斑和焦散光扇。"
  es: "Letras gruesas de vidrio macizo, cada una en un tono joya distinto, que proyectan charcos de luz de color y abanicos cáusticos sobre un suelo de estudio blanco y luminoso."
  pt: "Letras grossas de vidro maciço, cada uma num tom de joia diferente, projetando poças de luz colorida e leques cáusticos sobre um piso de estúdio branco e luminoso."
  de: "Dicke Buchstaben aus massivem Glas, jeder in einem anderen Edelsteinton, die farbige Lichtflecken und Kaustikfächer auf einen hellen weißen Studioboden werfen."
fontvibe_url: https://fontvibe.ai/styles/glass-color
preview_image: https://cos.fontvibe.ai/generations/user/17/5e5f1724-6c89-4796-a202-42e41f614506.jpeg
examples:
  - url: https://fontvibe.ai/gallery/10925
    image: https://cos.fontvibe.ai/generations/user/17/0dcc96d4-3e8b-4a52-8a98-eabdbe340e3e.jpeg
  - url: https://fontvibe.ai/gallery/10944
    image: https://cos.fontvibe.ai/generations/user/17/a5aa522f-0bb8-4208-baef-a70e57071df7.jpeg
  - url: https://fontvibe.ai/gallery/10933
    image: https://cos.fontvibe.ai/generations/user/17/c828009c-4461-488a-ae35-ce98d16e3eee.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "CYAN"
  image: "https://cos.fontvibe.ai/opensource/text-effect-prompts/glass_color.jpg"
  passed: true
  note: "Coloured stained-glass letters with reflections; spelled right."
license: CC-BY-4.0
---

# Color Glass

> Thick solid glass letters, each a different jewel tone, casting colored light pools and caustic fans across a bright white studio floor.

[![Color Glass on FontVibe](https://cos.fontvibe.ai/generations/user/17/5e5f1724-6c89-4796-a202-42e41f614506.jpeg)](https://fontvibe.ai/styles/glass-color)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/glass-color](https://fontvibe.ai/styles/glass-color)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. The words are sculpted as thick, solid colored glass letterforms with visible material weight and depth, crafted from deep-saturated jewel-tone glass. Each letter holds intense color throughout its transparent body—featuring vivid ruby, sapphire, emerald, or amber tones—with internal light scattering that produces a luminous glow at the core and rich saturation at the edges. Top surfaces carry sharp, mirror-bright specular highlights, while the sides reveal the full glass thickness and crisp refraction lines in the style of precision-cut optical glass sculpture. The letters rest on a dark, polished charcoal lacquer surface that produces clear mirror reflections directly beneath them. A single strong spotlight shining from the upper-left casts brilliant, rainbow-edged caustic light patterns and refraction fans across the ground plane. The background fades cleanly to near-black with a faint complementary gradient haze, keeping the composition uncluttered so the glowing, light-transmitting glass letters remain the primary, vibrant visual focus.
```

Generic-model test (`gemini-2.5-flash-image`, text "CYAN", 2026-10-30):

![test render](https://cos.fontvibe.ai/opensource/text-effect-prompts/glass_color.jpg)

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/0dcc96d4-3e8b-4a52-8a98-eabdbe340e3e.jpeg)](https://fontvibe.ai/gallery/10925) [![example](https://cos.fontvibe.ai/generations/user/17/a5aa522f-0bb8-4208-baef-a70e57071df7.jpeg)](https://fontvibe.ai/gallery/10944) [![example](https://cos.fontvibe.ai/generations/user/17/c828009c-4461-488a-ae35-ce98d16e3eee.jpeg)](https://fontvibe.ai/gallery/10933)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
sculpted as thick solid colored glass letterforms — each letter formed from deep-saturated jewel-tone glass with visible material weight and depth. The glass holds intense color throughout its body: ruby red, sapphire blue, emerald green, amber gold, cyan, or violet — color set by scene context. Top surfaces carry sharp mirror-bright specular highlights; side edges reveal full glass thickness with bright refracted light lines. Internal light scatters creating subsurface color gradients — luminous at the core, deeply saturated at edges. Caustic light patterns (rainbow-edged refraction fans) radiate from letter bases onto surrounding surfaces. Style may range from smooth precision-cut optical glass sculpture (modern) to segmented cathedral stained glass (traditional lead-came divided jewel panes) — determined by font choice. The defining quality: saturated transparent color glowing with transmitted light, like jewels held to sunlight.
```

**Scene**

```text
Dark polished surface — black marble or deep charcoal lacquer — reflecting the colored glass letters from below with mirror clarity. A single strong spotlight from above-left generates brilliant caustic light fans spreading across the dark surface in the letter's dominant hue. Background fades to near-black with a faint complementary-color gradient haze. No clutter — the glass letters are the only light source, their refracted color the most saturated element in the frame.
```

## Tips

- Short words with thick, bold structures highlight the internal light scattering, glass thickness, and caustic reflections best.
- Specify a single jewel tone like ruby red, sapphire blue, or emerald green in the prompt if you prefer a unified color theme instead of multicolored letters.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/glass-color](https://fontvibe.ai/styles/glass-color) — see [Attribution](../../README.md#attribution).
