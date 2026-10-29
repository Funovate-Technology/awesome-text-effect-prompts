---
id: horror
slug: horror
category: effects
tags: ["scary", "eerie", "macabre", "drip", "glow", "gothic"]
names:
  en: "Horror"
  ja: "ホラー"
  zh: "恐怖"
  es: "Terror"
  pt: "Terror"
  de: "Horror"
description:
  en: "Thin jagged red letters dripping blood, lit by a single bare bulb in a flooded tunnel, reflected in dark still water."
  ja: "血が滴る細くぎざぎざした赤い文字。水没したトンネルのただ一つの裸電球に照らされ、暗く静かな水面に映ります。"
  zh: "细瘦参差的红色字母不断滴血，被积水隧道里唯一一盏裸灯照亮，倒映在漆黑静止的水面上。"
  es: "Letras rojas finas y dentadas que gotean sangre, iluminadas por una sola bombilla desnuda en un túnel inundado y reflejadas en agua oscura y quieta."
  pt: "Letras vermelhas finas e serrilhadas pingando sangue, iluminadas por uma única lâmpada nua num túnel alagado e refletidas em água escura e parada."
  de: "Dünne, gezackte rote Buchstaben, von denen Blut tropft, beleuchtet von einer einzigen nackten Glühbirne in einem gefluteten Tunnel und gespiegelt im dunklen, stillen Wasser."
fontvibe_url: https://fontvibe.ai/styles/horror
preview_image: https://cos.fontvibe.ai/generations/user/17/f68ab0eb-1d5f-4218-b76f-2366bdbecb9c.jpeg
examples:
  - url: https://fontvibe.ai/gallery/4950
    image: https://cos.fontvibe.ai/generations/user/17/cd0b7682-59cf-4ed6-9137-a6aabc4f3315.jpeg
  - url: https://fontvibe.ai/gallery/13140
    image: https://cos.fontvibe.ai/generations/user/17/d592cfc0-45f6-4380-b638-8cbb1a50359a.jpeg
  - url: https://fontvibe.ai/gallery/13141
    image: https://cos.fontvibe.ai/generations/user/17/dd66a0db-3fc2-4c3e-ba5f-ed6f5663d958.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "WICKED"
  image: ""
  passed: true
  note: "Rotting letters with glowing lower edges; spelled right."
license: CC-BY-4.0
---

# Horror

> Thin jagged red letters dripping blood, lit by a single bare bulb in a flooded tunnel, reflected in dark still water.

[![Horror on FontVibe](https://cos.fontvibe.ai/generations/user/17/f68ab0eb-1d5f-4218-b76f-2366bdbecb9c.jpeg)](https://fontvibe.ai/styles/horror)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/horror](https://fontvibe.ai/styles/horror)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. The lettering is rendered in a bold, graphic consumer Halloween horror style with immediate, striking readability. The composition features harsh, dramatic underlighting with a warm amber-orange key light shining from directly beneath the letters, throwing the upper two-thirds into heavy shadow like a candle held under a face. Extreme contrast defines the surface, with brilliantly lit edges cutting directly into near-black shadow zones without soft mid-tones. The color palette includes deep candy-red crimson accents, fiery amber tones, and subtle hints of dark rust and mold green. The letters are set against a near-black background subtly showing the faint texture of a rough stone wall, accented by a very low-opacity sickly yellow-green ambient glow at the base and faint wisps of ground-level fog drifting along the bottom. Ensure {{TEXT}} is the only legible text in the entire image.
```

Tested on `gemini-2.5-flash-image` with the text "WICKED" on 2026-10-30 — passed (legible, correctly spelled, recognisably this style).

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/cd0b7682-59cf-4ed6-9137-a6aabc4f3315.jpeg)](https://fontvibe.ai/gallery/4950) [![example](https://cos.fontvibe.ai/generations/user/17/d592cfc0-45f6-4380-b638-8cbb1a50359a.jpeg)](https://fontvibe.ai/gallery/13140) [![example](https://cos.fontvibe.ai/generations/user/17/dd66a0db-3fc2-4c3e-ba5f-ed6f5663d958.jpeg)](https://fontvibe.ai/gallery/13141)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
Consumer Halloween horror typography. Graphic, bold, and immediately readable as "spooky" -- the visual language of seasonal design: T-shirts, party invites, phone cases, social media posts.

HALLOWEEN HORROR RULES (apply to every shot):
- Underlighting by default. Warm amber-orange key from directly below, deep shadow filling the upper two-thirds. Candle-beneath-the-face.
- Extreme contrast, no mid-tones. Lit surfaces near-maximum brightness, shadow zones near-black. Nothing gradual, nothing soft.
- Background always dark. Near-black with warm amber or sickly yellow-green secondary fill at very low opacity. No neutral grays.
- Color regime: blood is deep candy-red to dark crimson; fire is amber-orange with bright core; decay is dark brown, rust, mold green.
- Graphic and immediate. If the effect reads clearly on a printed T-shirt or party poster, it is correct.

FORBIDDEN: cinematic framing rules, single-light psychological analysis, desaturated fog atmospherics, flat studio lighting.

When no specific material is defined by the font: default lighting environment -- warm amber-orange underlighting from directly below, deep shadow above, near-black background with sickly yellow-green secondary fill at 8% opacity at ground level.
```

**Scene**

```text
Against a near-black background with rough dark stone wall texture at 10% opacity. Warm amber-orange light from directly below casting deep upward shadows. Faint wisps of ground-level fog. Haunting, Halloween atmospheric composition.
```

## Tips

- Short, punchy Halloween or spooky words work best with this intense underlit style to preserve maximum graphic impact.
- Shift the secondary glow color from sickly yellow-green to dark crimson or purple to alter the mood of the ambient background.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/horror](https://fontvibe.ai/styles/horror) — see [Attribution](../../README.md#attribution).
