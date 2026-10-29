---
id: neon_glow
slug: neon-glow
category: effects
tags: ["glow", "dreamy", "neon", "tubular", "retro", "energetic"]
names:
  en: "Neon Glow"
  ja: "ネオングロー"
  zh: "霓虹光效"
  es: "Resplandor Neón"
  pt: "Brilho Neon"
  de: "Neon-Leuchtschrift"
description:
  en: "Rounded neon-tube capitals alternating cyan and magenta, with bright tube cores, soft bloom and colored reflections on wet ground in the dark."
  ja: "シアンとマゼンタを交互にした丸いネオン管の大文字。明るい管の芯と柔らかなにじみ、暗がりの濡れた地面に色の映り込み。"
  zh: "青色与品红交替的圆润霓虹灯管大写字母，灯管芯明亮、光晕柔和，在黑暗中把彩色倒影投在湿地面上。"
  es: "Mayúsculas redondeadas de tubo de neón alternando cian y magenta, con núcleos brillantes, halo suave y reflejos de color en el suelo mojado en la oscuridad."
  pt: "Maiúsculas arredondadas de tubo de neon alternando ciano e magenta, com núcleos brilhantes, halo suave e reflexos coloridos no chão molhado no escuro."
  de: "Runde Neonröhren-Versalien abwechselnd in Cyan und Magenta, mit hellen Röhrenkernen, weichem Schein und farbigen Spiegelungen auf nassem Boden im Dunkeln."
fontvibe_url: https://fontvibe.ai/styles/neon-glow
preview_image: https://cos.fontvibe.ai/generations/user/17/801e9efa-8206-4c03-bfa4-8f7f716650a9.jpeg
examples:
  - url: https://fontvibe.ai/gallery/7592
    image: https://cos.fontvibe.ai/generations/user/17/ac0e315f-70fe-4cf8-84d7-f477294b5e11.jpeg
  - url: https://fontvibe.ai/gallery/7594
    image: https://cos.fontvibe.ai/generations/user/17/6993a336-2279-40e9-a088-71a902929c89.jpeg
  - url: https://fontvibe.ai/gallery/7588
    image: https://cos.fontvibe.ai/generations/user/17/344a1e9f-023e-41b4-ab65-cc31a5d1519d.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "NEON"
  image: "https://cos.fontvibe.ai/opensource/text-effect-prompts/neon_glow.jpg"
  passed: true
  note: "Bent glass neon tubes on concrete with brackets; spelled right."
license: CC-BY-4.0
---

# Neon Glow

> Rounded neon-tube capitals alternating cyan and magenta, with bright tube cores, soft bloom and colored reflections on wet ground in the dark.

[![Neon Glow on FontVibe](https://cos.fontvibe.ai/generations/user/17/801e9efa-8206-4c03-bfa4-8f7f716650a9.jpeg)](https://fontvibe.ai/styles/neon-glow)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/neon-glow](https://fontvibe.ai/styles/neon-glow)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. The letters are formed from real bent glass neon tubes complete with visible tube brackets, mounting hardware, and subtle glass tube refraction. The glow shines in bright cyan and magenta neon light, displaying sharp glowing edges enveloped by a soft light bloom, featuring slightly uneven brightness between individual letters for realism. Mounted on a dark concrete wall, each letter's colored illumination pools softly onto the floor beneath it. Tiny dust particles drift and catch the glow in the illuminated air, alongside faint reflections cast across the slightly damp ground while deep shadow gathers around the edges of the frame.
```

Generic-model test (`gemini-2.5-flash-image`, text "NEON", 2026-10-30):

![test render](https://cos.fontvibe.ai/opensource/text-effect-prompts/neon_glow.jpg)

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/ac0e315f-70fe-4cf8-84d7-f477294b5e11.jpeg)](https://fontvibe.ai/gallery/7592) [![example](https://cos.fontvibe.ai/generations/user/17/6993a336-2279-40e9-a088-71a902929c89.jpeg)](https://fontvibe.ai/gallery/7594) [![example](https://cos.fontvibe.ai/generations/user/17/344a1e9f-023e-41b4-ab65-cc31a5d1519d.jpeg)](https://fontvibe.ai/gallery/7588)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
rendered as real bent glass neon tubes with visible tube brackets and mounting hardware. Bright cyan and magenta neon light, sharp glowing edges with soft light bloom, visible glass tube refraction. Slightly uneven brightness between letters for realism. LETTERFORM PRIORITY: when the chosen font carries its own treatment, that font's letterform shapes take priority and own the letters; this style governs the glass-tube neon material, the glow bloom and the color. FALLBACK MATERIAL: if the font carries no material of its own, render the letters as real bent glass neon tubes with visible brackets, glowing with sharp edges and soft bloom. COLOR PRIORITY: keep the font's own colors if specified; otherwise bright cyan and magenta neon.
```

**Scene**

```text
Mounted on a dark concrete wall, each letter's colored light pooling softly on the floor beneath it, tiny dust particles caught in the glow, faint reflections on the slightly damp ground, deep shadow gathering around the edges of the frame.
```

## Tips

- Short, punchy words or single-word phrases work best to replicate the look of a real bent-glass sign without overcrowding.
- Swap cyan and magenta for warm amber or ruby red in the prompt to shift the mood from a cool night scene to vintage roadside signage.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/neon-glow](https://fontvibe.ai/styles/neon-glow) — see [Attribution](../../README.md#attribution).
