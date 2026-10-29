---
id: wedding
slug: wedding
category: occasions
tags: ["calm", "romantic", "gold", "foil", "letterpress", "classic", "luxury", "elegant", "serif"]
names:
  en: "Wedding"
  ja: "ウェディング"
  zh: "婚礼"
  es: "Boda"
  pt: "Casamento"
  de: "Hochzeit"
description:
  en: "Gold-foil serif with soft script flourishes on warm ivory cotton paper with a deckled edge, blush roses and eucalyptus in one corner."
  ja: "暖かなアイボリーの耳付きコットン紙に金箔のセリフ体と柔らかな筆記体の飾り。隅にはブラッシュピンクのバラとユーカリ。"
  zh: "暖象牙色毛边棉纸上的烫金衬线字，配柔和手写花饰，一角点缀腮红玫瑰与尤加利叶。"
  es: "Serifa en lámina dorada con suaves adornos caligráficos sobre papel de algodón marfil cálido de borde irregular, con rosas rubor y eucalipto en una esquina."
  pt: "Serifa em folha dourada com floreios caligráficos suaves sobre papel de algodão marfim quente de borda irregular, com rosas blush e eucalipto num canto."
  de: "Goldfolien-Serifen mit sanften kalligrafischen Schwüngen auf warmem elfenbeinfarbenem Baumwollpapier mit Büttenrand, zartrosa Rosen und Eukalyptus in einer Ecke."
fontvibe_url: https://fontvibe.ai/styles/wedding
preview_image: https://cos.fontvibe.ai/generations/user/17/b697f890-d426-4116-a510-dce7e9a0bbae.jpeg
examples:
  - url: https://fontvibe.ai/gallery/17708
    image: https://cos.fontvibe.ai/generations/user/17/67c7e657-8b2a-4a89-aaa0-7de4bb52ca81.jpeg
  - url: https://fontvibe.ai/gallery/1512
    image: https://cos.fontvibe.ai/generations/user/17/7790fd20e6934982911b6278dce2f567.jpeg
  - url: https://fontvibe.ai/gallery/456
    image: https://cos.fontvibe.ai/generations/user/17/d469104c-1555-4477-a760-146bcaefaea0.jpeg
test:
  model: gemini-2.5-flash-image
  date: 2026-10-30
  text: "FOREVER"
  image: "https://cos.fontvibe.ai/opensource/text-effect-prompts/wedding.jpg"
  passed: true
  note: "Gold foil letters on deckled card with roses; spelled right."
license: CC-BY-4.0
---

# Wedding

> Gold-foil serif with soft script flourishes on warm ivory cotton paper with a deckled edge, blush roses and eucalyptus in one corner.

[![Wedding on FontVibe](https://cos.fontvibe.ai/generations/user/17/b697f890-d426-4116-a510-dce7e9a0bbae.jpeg)](https://fontvibe.ai/styles/wedding)

**Try it with your own words on FontVibe → [fontvibe.ai/styles/wedding](https://fontvibe.ai/styles/wedding)**

## Standalone prompt

Replace `{{TEXT}}` with your words. Written for general image models; tested on `gemini-2.5-flash-image`.

```text
Render the text "{{TEXT}}" exactly as written, character by character. The text sits centered with generous, airy spacing on a luxurious sheet of warm ivory cotton paper featuring a soft deckled edge. The lettering is rendered in rich, warm antique gold-leaf foil with metallic gold ink, showing a bright specular highlight along one edge and a darker metallic shadow along the other to establish tangible depth. Crisp, subtle letterpress indentation presses the characters gently into the paper, creating soft debossed shadows around the gilded strokes. Gentle, directional daylight rakes across the textured surface, illuminating the metallic sheen while preserving the quiet, refined atmosphere. Delicate botanical accents—sparing sprigs of eucalyptus and soft blush roses—subtly frame one corner without crowding the text. The composition maintains generous negative space, harmonizing ivory, champagne, and antique gold with muted eucalyptus greens for an elegant, calm stationery aesthetic.
```

Generic-model test (`gemini-2.5-flash-image`, text "FOREVER", 2026-10-30):

![test render](https://cos.fontvibe.ai/opensource/text-effect-prompts/wedding.jpg)

## Examples made on FontVibe

[![example](https://cos.fontvibe.ai/generations/user/17/67c7e657-8b2a-4a89-aaa0-7de4bb52ca81.jpeg)](https://fontvibe.ai/gallery/17708) [![example](https://cos.fontvibe.ai/generations/user/17/7790fd20e6934982911b6278dce2f567.jpeg)](https://fontvibe.ai/gallery/1512) [![example](https://cos.fontvibe.ai/generations/user/17/d469104c-1555-4477-a760-146bcaefaea0.jpeg)](https://fontvibe.ai/gallery/456)

## Original FontVibe style layer

This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to "the chosen font". Use the standalone prompt above with other tools.

**Surface, colour & lighting**

```text
the hushed luxury of a fine wedding suite. GROUND: warm ivory, cream and champagne cotton paper with a soft deckled edge, or a tone-on-tone neutral stock. LIGHT: soft daylight with a gentle directional rake across the surface — enough to strike a bright specular flash along the gilded strokes so the metal reads rich, not flat. FINISH: where the lettering catches light it reads as rich gold-leaf foil and warm metallic gold ink — deep saturated antique gold and warm yellow-gold with a bright specular highlight on one edge and a darker gold shadow on the other for real metallic depth (champagne only as a soft secondary tone, never the whole gold); elsewhere it reads as letterpress and blind-emboss, pressed crisply into the paper so the strokes sit slightly below the surface with a soft debossed shadow. ORNAMENT: delicate botanical accents — eucalyptus, roses, peonies in fine line or soft watercolor — kept sparing, framing not flooding. PALETTE: ivory and cream base, rich warm antique gold and gold-leaf (saturated, not pale), with champagne, sage and eucalyptus green, dusty blue, and forest-green or navy as a deep old-money accent; generous negative space and lightness throughout. LETTERFORM PRIORITY: when the chosen font carries its own material or color (gold foil, rose-gold, letterpress emboss, watercolor, velvet), that font treatment takes absolute priority and owns the letter surface; this style governs only the paper, light, ornament and surrounding palette. FALLBACK MATERIAL: if the font carries no material of its own, render the letters in rich warm gold-leaf metallic ink on ivory paper with a bright specular highlight and a whisper of letterpress impression, so the premium wedding feel always reads.
```

**Scene**

```text
The text sits centered with generous airy spacing on a sheet of warm ivory cotton paper with a soft deckled edge, the quiet focal point of a fine wedding suite. A few delicate botanical sprigs — eucalyptus, a blush rose or two — frame one corner, never crowding. Soft diffused daylight, a faint debossed shadow and a whisper of gold catching the light. Calm, luxurious, editorial wedding-stationery composition with plenty of negative space.
```

## Tips

- Short phrases, couples' names, or single celebratory words best complement the refined, spacious layout.
- Swap the eucalyptus and blush rose botanicals for olive leaves, winter pine, or white peonies to easily shift the seasonal mood.
- Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.
- Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.

---

Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [fontvibe.ai/styles/wedding](https://fontvibe.ai/styles/wedding) — see [Attribution](../../README.md#attribution).
