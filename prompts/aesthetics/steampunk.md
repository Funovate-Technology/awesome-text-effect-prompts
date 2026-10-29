---
id: steampunk
slug: steampunk
category: aesthetics
tags: ["brass", "steampunk", "victorian", "copper", "patina", "adventurous", "nostalgic"]
names:
  en: "Steampunk"
  ja: "スチームパンク"
  zh: "Steampunk"
  es: "Steampunk"
  pt: "Steampunk"
  de: "Steampunk"
description:
  en: "Victorian steampunk typography with brass gear mechanisms, copper pipe frameworks, steam-powered industrial textures and clockwork ornamental details."
  ja: "真鍮の歯車機構、銅パイプのフレーム、蒸気機関を思わせる工業的なテクスチャ、時計仕掛けの装飾ディテールを備えたヴィクトリア朝スチームパンクのタイポグラフィです。"
  zh: "维多利亚风格的 Steampunk 字体排印，黄铜齿轮机构、紫铜管道框架、蒸汽驱动的工业质感，还有钟表机械般的华丽装饰细节。"
  es: "Tipografía Steampunk victoriana con mecanismos de engranajes de latón, estructuras de tuberías de cobre, texturas industriales a vapor y detalles ornamentales de relojería."
  pt: "Tipografia Steampunk vitoriana com mecanismos de engrenagens de latão, estruturas de tubos de cobre, texturas industriais a vapor e detalhes ornamentais de relojoaria."
  de: "Viktorianische Steampunk Schrift mit Messing-Zahnradmechanismen, Kupferrohr-Gerüsten, dampfbetriebenen Industrietexturen und ornamentalen Uhrwerk-Details."
fontvibe_url: https://fontvibe.ai/styles/steampunk
preview_image: https://cos.fontvibe.ai/generations/user/17/b63b87f1-24ed-4b79-af15-545a87c7eb1a.jpeg
examples:
  - url: https://fontvibe.ai/gallery/12145
    image: https://cos.fontvibe.ai/generations/user/17/34f60eb6-2804-4d98-b922-42e0b7bbc5e2.jpeg
  - url: https://fontvibe.ai/gallery/12122
    image: https://cos.fontvibe.ai/generations/user/17/4dcf640f-e386-4611-99ce-72b48136917a.jpeg
  - url: https://fontvibe.ai/gallery/12136
    image: https://cos.fontvibe.ai/generations/user/17/ce73464c-2d57-492a-a88b-30903d656d5a.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "STEAM"
  image: "https://cos.fontvibe.ai/opensource/text-effect-prompts/steampunk.jpg"
  passed: true
  note: "Brass-and-pipe letters in a workshop with filament bulbs; spelled right."
license: CC-BY-4.0
---

# Steampunk

> Victorian steampunk typography with brass gear mechanisms, copper pipe frameworks, steam-powered industrial textures and clockwork ornamental details.

[![Steampunk on FontVibe](https://cos.fontvibe.ai/generations/user/17/b63b87f1-24ed-4b79-af15-545a87c7eb1a.jpeg)](https://fontvibe.ai/styles/steampunk)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/steampunk](https://fontvibe.ai/styles/steampunk)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. The text {{TEXT}} is centered in the frame, filling most of the width, and serves as the sole legible subject. The letters are crafted with metallic steampunk materials featuring polished brass highlights, dark patina bronze, aged verdigris copper-green accents, and deep cast iron shadows. The scene is illuminated by dual-light thermal contrast: a warm amber vintage filament bulb from the upper-right at 45 degrees casting bright directional specular highlights with deep warm shadows at the letter bases, countered by a cool blue-grey secondary fill from the upper-left. The letters rest on a dark mahogany workbench inside a Victorian inventor's workshop, with small brass gears, calipers, coiled copper wire, and clockwork components scattered in soft focus around the base. Soft steam vents from distant pipe joints into the warm amber haze, with a receding brick wall and hanging filament bulbs blurred in the background. The camera views the scene from a slight low angle, keeping the letters sharp while foreground props and background elements softly blur.
```

Generic-model test (`gemini-2.5-flash-image`, text "STEAM", 2026-10-30):

![test render](https://cos.fontvibe.ai/opensource/text-effect-prompts/steampunk.jpg)

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/34f60eb6-2804-4d98-b922-42e0b7bbc5e2.jpeg)](https://fontvibe.ai/gallery/12145) [![example](https://cos.fontvibe.ai/generations/user/17/4dcf640f-e386-4611-99ce-72b48136917a.jpeg)](https://fontvibe.ai/gallery/12122) [![example](https://cos.fontvibe.ai/generations/user/17/ce73464c-2d57-492a-a88b-30903d656d5a.jpeg)](https://fontvibe.ai/gallery/12136)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
steampunk material environment — warm amber vintage filament light (2700K) as primary source from upper-right at 45 degrees, creating hot directional specular highlights on brass and copper surfaces with deep warm shadows at letter bases. Cool blue-grey secondary fill from upper-left: the cold-warm dual-light thermal contrast is the defining lighting signature of this style. Background atmosphere: Victorian inventor's workshop — dark mahogany workbench surface with scattered brass calipers, unrolled mechanical blueprints, and small clockwork components barely visible in warm shadow depth. Steam venting from pipe joints in background, diffusing into warm amber air. Visible gear assemblies and pressure gauges as environmental props in mid-ground shadow — mechanical elements present but never competing with the text subject. Ambient material palette: polished brass highlights (#D4A017), aged verdigris copper-green (#4A7B5A), dark patina bronze (#7D6608), cast iron shadow (#2C2420). When no specific material is defined by the font: default lighting environment — warm amber vintage filament bulb from upper-right at 45 degrees, cool blue-grey window fill from upper-left, dark mahogany workshop background with brass and clockwork props barely visible in warm shadow, gentle steam haze in the air.
```

**Scene**

```text
Text centered in frame, filling 78-85% of frame width. Background: Victorian workshop interior — dark wooden workbench surface in lower foreground, brick wall with mounted gas pipe sconces receding into warm amber background darkness. Small brass gears, calipers, and coiled copper wire scattered at letter bases as physical props. Overhead vintage filament bulbs hanging in background casting warm amber pools on the workbench surface. Camera at slight low angle looking up at the text subject, giving the letters presence and weight against the workshop ceiling. Depth of field: letter subject sharp, workshop props in soft foreground blur, background brick wall in atmospheric warm haze.
```

## Tips

- Words related to machinery, exploration, invention, or industrial themes feel most natural in this aesthetic.
- To adjust the mood, alter the balance between the warm filament amber light and the cool blue fill light to make the scene feel either cozier or more industrial.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/steampunk](https://fontvibe.ai/styles/steampunk) — see [Attribution](../../README.md#attribution).
