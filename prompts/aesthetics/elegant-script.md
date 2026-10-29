---
id: elegant_script
slug: elegant-script
category: aesthetics
parent: cursive
tags: ["calligraphy", "swash", "thin", "script", "gold", "luxury", "elegant", "refined"]
names:
  en: "Elegant Script"
  ja: "エレガントスクリプト"
  zh: "优雅手写体"
  es: "Letras Elegantes"
  pt: "Fonte Elegante"
  de: "Elegante Schreibschrift"
description:
  en: "Fine gold script with long hairline swashes and a looping capital, laid on matte black or ivory card beside luxury props under soft grazing light."
  ja: "髪の毛のように細い長いスワッシュとループする頭文字を持つ繊細な金の筆記体。マットな黒やアイボリーのカードに高級な小物を添え、柔らかな斜光で。"
  zh: "精致的金色手写体，发丝般的长花饰与回环大写，置于哑光黑或象牙白卡纸上，旁有奢华道具，柔和掠射光。"
  es: "Script dorado y fino con largos remates finísimos y una mayúscula en bucle, sobre cartulina negra mate o marfil junto a objetos de lujo bajo una luz rasante suave."
  pt: "Script dourado e fino com longos floreios finíssimos e uma maiúscula em laço, sobre cartão preto fosco ou marfim ao lado de objetos de luxo sob luz rasante suave."
  de: "Feine goldene Schreibschrift mit langen haarfeinen Schwüngen und geschlungener Initiale, auf mattschwarzem oder elfenbeinfarbenem Karton neben Luxusobjekten im sanften Streiflicht."
fontvibe_url: https://fontvibe.ai/styles/elegant-script
preview_image: https://cos.fontvibe.ai/generations/user/17/f545b0c8-7c3f-4b86-b0ea-6581060af8f4.jpeg
examples:
  - url: https://fontvibe.ai/gallery/17840
    image: https://cos.fontvibe.ai/generations/user/17/c9e40fd0-2679-40c7-b35d-ae10f4539411.jpeg
  - url: https://fontvibe.ai/gallery/307
    image: https://cos.fontvibe.ai/generations/user/17/5ce9c75a-4ee8-4c29-a879-06be65761db6.jpeg
  - url: https://fontvibe.ai/gallery/309
    image: https://cos.fontvibe.ai/generations/user/17/8478f30d-0018-468b-8aed-4c5387277934.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "Elegant"
  image: "https://cos.fontvibe.ai/opensource/text-effect-prompts/elegant_script.jpg"
  passed: true
  note: "Gold foil script on black; spelled right."
license: CC-BY-4.0
---

# Elegant Script

> Fine gold script with long hairline swashes and a looping capital, laid on matte black or ivory card beside luxury props under soft grazing light.

[![Elegant Script on FontVibe](https://cos.fontvibe.ai/generations/user/17/f545b0c8-7c3f-4b86-b0ea-6581060af8f4.jpeg)](https://fontvibe.ai/styles/elegant-script)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/elegant-script](https://fontvibe.ai/styles/elegant-script)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. The lettering embodies the hushed luxury of an intimate, hand-signed brand mark, crafted in fine warm gold metallic ink that appears restrained, expensive, and never flashy. The strokes are pressed into the surface with the subtle crispness of an engraving, catching a single soft directional light that grazes across the letters to reveal their delicate metallic sheen and dimensional edges. The word {{TEXT}} sits large and centered against a premium, deep matte black luxury ground, framed by generous negative space that enhances its refined, high-end editorial atmosphere. The entire scene captures the quiet sophistication of a couture label, a boutique logo, or a perfume-bottle signature, with pure focus resting on the gleaming golden strokes and the tactile texture of the dark backdrop. Ensure {{TEXT}} is the only legible text in the image.
```

Generic-model test (`gemini-2.5-flash-image`, text "Elegant", 2026-10-30):

![test render](https://cos.fontvibe.ai/opensource/text-effect-prompts/elegant_script.jpg)

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/c9e40fd0-2679-40c7-b35d-ae10f4539411.jpeg)](https://fontvibe.ai/gallery/17840) [![example](https://cos.fontvibe.ai/generations/user/17/5ce9c75a-4ee8-4c29-a879-06be65761db6.jpeg)](https://fontvibe.ai/gallery/307) [![example](https://cos.fontvibe.ai/generations/user/17/8478f30d-0018-468b-8aed-4c5387277934.jpeg)](https://fontvibe.ai/gallery/309)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
the hushed luxury of a hand-signed brand mark. SURFACE / FINISH: where the lettering catches light it reads as fine metallic ink — warm gold, champagne or a soft rose-gold — or as a crisp blind-emboss / engraving pressed into the surface; restrained and expensive, never flashy. GROUND: a premium luxury surface — deep matte black, ivory or champagne card, soft marble, blush, or a dark editorial backdrop — with generous negative space and a single soft directional light that grazes the strokes. ATMOSPHERE: the elegant, intimate feel of a perfume-bottle signature, a couture label, a boutique logo or an engraved monogram — luxury branding, not a wedding scene. LETTERFORM PRIORITY: when the chosen font carries its own material or color, that font treatment takes absolute priority and owns the letters; this style governs the finish, the luxury ground, the light and the negative space. FALLBACK MATERIAL: if the font carries no material of its own, render the letters in fine warm gold metallic ink on a premium ground (deep black, ivory or marble) with a single soft grazing light, so the luxury-signature feel always reads.
```

**Scene**

```text
The signature sits large and centered with elegant negative space on a premium luxury surface — deep matte black, an ivory card, soft marble or a blush editorial backdrop. A single soft directional light grazes the strokes to catch the metallic finish, with at most a whisper of an accent (a thin rule or a small sprig). Refined, intimate, expensive — a luxury brand signature, perfume label or boutique mark.
```

## Tips

- Short single words, monograms, or brief luxury names work best, allowing the generous negative space to maintain an uncluttered, premium feel.
- To adjust the palette, change the deep matte black backdrop to textured ivory card or soft pale marble, paired with champagne or rose-gold metallic ink.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/elegant-script](https://fontvibe.ai/styles/elegant-script) — see [Attribution](../../README.md#attribution).
