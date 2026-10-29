---
id: glass_morphism
slug: glass-morphism
category: effects
parent: glass
tags: ["minimal", "transparent", "blur", "airy", "modern", "sleek", "frosted glass"]
names:
  en: "Frosted Glass"
  ja: "フロストガラス"
  zh: "磨砂玻璃"
  es: "Vidrio Esmerilado"
  pt: "Vidro Fosco"
  de: "Milchglas"
description:
  en: "Milky semi-transparent frosted glass panels with soft blur and glassmorphism aesthetic — thin glass border, blurred colorful background visible through surface. Modern UI quality."
  ja: "乳白色の半透明フロストガラスパネルに、柔らかなブラーとグラスモーフィズムの質感を組み合わせたスタイルです。薄いガラスの縁取りと、表面を通して透ける色鮮やかでぼかされた背景が特徴です。モダンなUIならではの完成度を実現します。"
  zh: "乳白半透明的磨砂玻璃面板，柔和模糊，玻璃拟态质感——细细的玻璃边框，透过表面能看到背后模糊的彩色背景。现代 UI 级别的品质。"
  es: "Paneles de vidrio esmerilado semitransparentes y lechosos, con desenfoque suave y estética glassmorphism: borde fino de vidrio y un fondo colorido y difuminado que se ve a través de la superficie. Calidad de UI moderna."
  pt: "Painéis de vidro fosco leitosos e semitransparentes, com desfoque suave e estética glassmorphism: borda fina de vidro e um fundo colorido e desfocado visível através da superfície. Qualidade de UI moderna."
  de: "Milchig-halbtransparente Milchglas-Paneele mit sanftem Weichzeichner und Glasmorphismus-Ästhetik — dünner Glasrand, verschwommener, farbiger Hintergrund durch die Oberfläche sichtbar. Moderne UI-Qualität."
fontvibe_url: https://fontvibe.ai/styles/glass-morphism
preview_image: https://cos.fontvibe.ai/generations/user/17/985d9f4a-3047-44d8-ab14-37662e36bb9a.jpeg
examples:
  - url: https://fontvibe.ai/gallery/11149
    image: https://cos.fontvibe.ai/generations/user/17/c4c0518e-aee6-4b51-a889-6ef9ec185da6.jpeg
  - url: https://fontvibe.ai/gallery/11162
    image: https://cos.fontvibe.ai/generations/user/17/ec9befff-737c-4026-b2eb-60fad3b260b9.jpeg
  - url: https://fontvibe.ai/gallery/11170
    image: https://cos.fontvibe.ai/generations/user/17/9e9fe60f-94ad-4cc7-a518-3c35537fa022.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "BLUR"
  image: "https://cos.fontvibe.ai/opensource/text-effect-prompts/glass_morphism.jpg"
  passed: true
  note: "Frosted glass letters over coloured bokeh; spelled right."
license: CC-BY-4.0
---

# Frosted Glass

> Milky semi-transparent frosted glass panels with soft blur and glassmorphism aesthetic — thin glass border, blurred colorful background visible through surface. Modern UI quality.

[![Frosted Glass on FontVibe](https://cos.fontvibe.ai/generations/user/17/985d9f4a-3047-44d8-ab14-37662e36bb9a.jpeg)](https://fontvibe.ai/styles/glass-morphism)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/glass-morphism](https://fontvibe.ai/styles/glass-morphism)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. Each letter appears as a translucent frosted glassmorphism slab suspended in space with multi-layered optical depth. The material features three distinct optical zones: a razor-thin, bright white specular highlight tracing the perimeter, an interior surface of semi-transparent milky frosted glass with a subtle blur revealing the background at low opacity, and a soft internal glow concentrated at the center of each letterform. Soft dark inner shadows run along the glass edges to create physical thickness, while the frosted texture scatters illumination into a faint diffuse halo around the perimeter. The letters float before a deep midnight-blue background illuminated by vibrant, out-of-focus bokeh orbs in glowing shades of coral-orange, electric violet, cyan-teal, and emerald green. These colorful light spheres subtly bleed and refract through the semi-transparent glass bodies, making the letters act as frosted windows onto the luminous backdrop, with high contrast ensuring edge highlights stay razor-sharp.
```

Generic-model test (`gemini-2.5-flash-image`, text "BLUR", 2026-10-30):

![test render](https://cos.fontvibe.ai/opensource/text-effect-prompts/glass_morphism.jpg)

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/c4c0518e-aee6-4b51-a889-6ef9ec185da6.jpeg)](https://fontvibe.ai/gallery/11149) [![example](https://cos.fontvibe.ai/generations/user/17/ec9befff-737c-4026-b2eb-60fad3b260b9.jpeg)](https://fontvibe.ai/gallery/11162) [![example](https://cos.fontvibe.ai/generations/user/17/9e9fe60f-94ad-4cc7-a518-3c35537fa022.jpeg)](https://fontvibe.ai/gallery/11170)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
rendered as frosted glassmorphism panel letterforms — each letter a translucent frosted glass slab suspended in space with multi-layer depth. The glass material has three distinct optical zones: outer edge — a razor-thin bright white specular highlight line tracing the full letter perimeter; interior surface — semi-transparent milky frosted glass with subtle gaussian blur revealing the colorful background through it with 15-20% opacity; inner highlight — a soft internal glow where light concentrates at letter center. The frosted surface scatters light into a soft diffuse halo around each letter. Letter faces show characteristic glassmorphism: white inner border, background color bleeding through with subtle color shift, soft dark inner shadow at letter edges creating tactile depth. The typographic language of modern mobile-OS frosted panels, desktop glassmorphism UI, modern SaaS dashboard design — contemporary, airy, premium digital.
```

**Scene**

```text
Rich bokeh background with vivid floating color orbs — deep midnight blue base with luminous colored light spheres: coral-orange, electric violet, cyan-teal, emerald green circles softly out of focus behind the frosted glass letters. The frosted letters sit in front of this colorful depth, their semi-transparent surfaces showing the blurred color orbs through them — each letter a window onto the colorful bokeh world behind. Background dark enough that frosted glass edge highlights read clearly. Overall aesthetic: modern premium app UI, floating glass cards over a vibrant abstract background — airy, layered, depth-rich.
```

## Tips

- Short, clean words work best, as the complex frosted reflections and background blur can become cluttered on lengthy phrases.
- Change the palette of the floating background bokeh orbs to alter the overall color mood reflected through the frosted panels.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/glass-morphism](https://fontvibe.ai/styles/glass-morphism) — see [Attribution](../../README.md#attribution).
