---
id: cyberpunk_bio_mech
slug: cyberpunk-bio-mech
category: scenes
parent: cyberpunk
tags: ["metallic", "industrial", "biomechanical", "dark", "grotesque", "bone"]
names:
  en: "Bio Mech"
  ja: "バイオメカ"
  zh: "生物机械"
  es: "Bio Mech"
  pt: "Bio Mech"
  de: "Bio Mech"
description:
  en: "Biomechanical fusion of organic tissue and metal machinery. H.R. Giger-inspired dark industrial aesthetic."
  ja: "有機的な組織と金属機械が融合したバイオメカニカル。H.R. Gigerにインスパイアされたダークでインダストリアルな美学です。"
  zh: "有机组织与金属机械的生物机械融合。灵感源自 H.R. Giger 的暗黑工业美学。"
  es: "Fusión biomecánica de tejido orgánico y maquinaria de metal. Estética industrial oscura inspirada en H.R. Giger."
  pt: "Fusão biomecânica de tecido orgânico e maquinário de metal. Estética industrial sombria inspirada em H.R. Giger."
  de: "Biomechanische Verschmelzung von organischem Gewebe und Metallmaschinerie. Dunkle, industrielle Ästhetik im Stil von H.R. Giger."
fontvibe_url: https://fontvibe.ai/styles/cyberpunk-bio-mech
preview_image: https://cos.fontvibe.ai/generations/user/17/3d3053cb-aaad-4152-96e8-91338671b2b7.jpeg
examples:
  - url: https://fontvibe.ai/gallery/12097
    image: https://cos.fontvibe.ai/generations/user/17/73619750-36fd-48d9-af1d-ce22818bf73b.jpeg
  - url: https://fontvibe.ai/gallery/12096
    image: https://cos.fontvibe.ai/generations/user/17/c1fbcbd3-f08c-4053-99ef-784c07bbad7f.jpeg
  - url: https://fontvibe.ai/gallery/12094
    image: https://cos.fontvibe.ai/generations/user/17/3050cde6-7aee-4665-9025-1f2f41e789aa.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "MECH"
  image: "https://cos.fontvibe.ai/opensource/text-effect-prompts/cyberpunk_bio_mech.jpg"
  passed: true
  note: "Biomechanical bone-and-metal letters in a dark hall; spelled right."
license: CC-BY-4.0
---

# Bio Mech

> Biomechanical fusion of organic tissue and metal machinery. H.R. Giger-inspired dark industrial aesthetic.

[![Bio Mech on FontVibe](https://cos.fontvibe.ai/generations/user/17/3d3053cb-aaad-4152-96e8-91338671b2b7.jpeg)](https://fontvibe.ai/styles/cyberpunk-bio-mech)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/cyberpunk-bio-mech](https://fontvibe.ai/styles/cyberpunk-bio-mech)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. The letters are sculpted in a biomechanical style, fusing oil-stained forged steel with calcium-white bone matter erupting through stressed joint seams. Gear teeth, piston housings corroded with machine oil, and welded seams with mineral calcium deposits cover the letterforms along stress fractures, balancing a cold dark metal exoskeleton with warm ivory organic bone. Centered in the frame and filling 75 to 85 percent of the frame width, the text is viewed from a slight low angle. The setting is a dark industrial chamber featuring corrugated metal walls with exposed pipe bundles and cable conduits receding into darkness. A single cold blue-white industrial arc overhead serves as the primary key light, creating a tight oval pool on the oil-stained concrete floor beneath the text, while a deep amber-orange fill light from the lower-left simulates a distant machinery furnace glow. Deep shadows envelop the outer edges, leaving {{TEXT}} as the sole legible focus.
```

Generic-model test (`gemini-2.5-flash-image`, text "MECH", 2026-10-30):

![test render](https://cos.fontvibe.ai/opensource/text-effect-prompts/cyberpunk_bio_mech.jpg)

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/73619750-36fd-48d9-af1d-ce22818bf73b.jpeg)](https://fontvibe.ai/gallery/12097) [![example](https://cos.fontvibe.ai/generations/user/17/c1fbcbd3-f08c-4053-99ef-784c07bbad7f.jpeg)](https://fontvibe.ai/gallery/12096) [![example](https://cos.fontvibe.ai/generations/user/17/3050cde6-7aee-4665-9025-1f2f41e789aa.jpeg)](https://fontvibe.ai/gallery/12094)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
biomechanical style — the visual world is dark industrial: oil-stained forged steel (#1A1A1E), calcium-white bone matter (#F5EFE0) erupting through stressed joint seams, gear teeth and piston housings corroded with machine oil, welded seams with mineral calcium deposits along stress fractures. Material contrast: cold dark metal exoskeleton vs warm ivory organic bone — both present simultaneously in the same space. Lighting environment: single cold blue-white industrial arc overhead as primary; deep amber-orange fill from lower-left simulating background furnace or machinery glow. Atmosphere: interior of a decommissioned bio-mechanical industrial facility — corrugated dark metal ribbed walls recede into shadow, faint amber workshop glow from deep background machinery, oil-stained concrete floor below. When no specific material is defined by the font: default lighting environment — cold blue-white overhead arc from directly above, amber-orange warm fill from lower-left, near-black background with faint corroded dark metal wall texture, ground plane shows faint oil-stained concrete reflection.
```

**Scene**

```text
Text centered in frame, filling 75-85% of frame width. Background: dark bio-mechanical industrial chamber — corrugated dark metal walls with exposed pipe bundles and cable conduits, biomechanical machinery silhouettes barely visible in deep background darkness, single cold industrial overhead arc light creating a tight oval pool on the oil-slick dark floor below the letters. Dim amber workshop glow from deep background machinery warming the lower atmosphere. Deep shadows at frame edges. Camera at eye level, slight low angle looking up at the letterforms.
```

## Tips

- Short, aggressive words related to industry, technology, or anatomy work best with this aesthetic.
- Shift the ratio between calcium bone matter and forged steel pistons to make the structure appear either more organic or more mechanical.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/cyberpunk-bio-mech](https://fontvibe.ai/styles/cyberpunk-bio-mech) — see [Attribution](../../README.md#attribution).
