# Awesome Text Effect Prompts

**Copy-paste prompts for AI text effects — neon, chrome, liquid glass, ink brush, pixel art,
pop art, Art Deco and more — with a `{{TEXT}}` placeholder for your own words.**

Every prompt here comes from a style on **[FontVibe](https://fontvibe.ai/styles)**, rewritten so it
works on its own in a general image model, and then **actually run on one** before it was allowed
in. Prompts that didn't hold up on the general model were left out and are listed below, rather than
published and hoped for.

<!-- counts:start -->
```
  129   styles published, each with a standalone prompt tested on a general image model
    5   categories
    6   languages for names and descriptions (en · ja · zh · es · pt · de)
    4   styles on FontVibe left out for trademark reasons
    5   styles left out because their standalone prompt failed the test
```
<!-- counts:end -->

> **Honest note: results are best on FontVibe.** These prompts carry a style's material, colour,
> lighting and scene. On [fontvibe.ai](https://fontvibe.ai/styles) the same style is also paired with
> a real font description, a font reference image that pins down the letter shapes, and the image
> model that style was tuned on. A general model gets the look and the mood, but draws its own
> letters — and on long phrases it misspells sooner. If you need the exact letterforms, or more than
> a word or two, use the "Try it" link.

## Use it

1. Open a style below and copy its **Standalone prompt**.
2. Replace `{{TEXT}}` with your words. Short is safest: 1–3 words.
3. Paste it into any text-to-image model.

```text
Render the text "{{TEXT}}" exactly as written, character by character. The letters are formed from
real bent glass neon tubes complete with visible tube brackets, mounting hardware ...
```

As data:

```bash
npm i text-effect-prompts        # or: npx text-effect-prompts neon-glow "OPEN LATE"
pip install text-effect-prompts  # or: python -m text_effect_prompts neon-glow "OPEN LATE"
```

```js
const tep = require('text-effect-prompts')
tep.prompt('neon-glow', 'OPEN LATE')          // the prompt with your words filled in
tep.search('ネオン')                            // names & descriptions in en · ja · zh · es · pt · de
tep.list({ category: 'effects' })
```

```python
import text_effect_prompts as tep
tep.prompt("neon-glow", "OPEN LATE")
tep.search("ネオン")
tep.list_styles(category="effects")
```

```python
import json
styles = json.load(open("index.json", encoding="utf-8"))["styles"]
p = next(s for s in styles if s["slug"] == "neon-glow")["prompt"].replace("{{TEXT}}", "OPEN LATE")
```

Each style page in [`prompts/`](prompts/) carries:

- **Standalone prompt** — self-contained, `{{TEXT}}` placeholder, tested.
- **Original FontVibe style layer** — the exact text FontVibe uses, for people who want to see how
  the site builds its prompts. It is *not* a complete prompt on its own (see below).
- **Examples** made on FontVibe, linked to their pages, and **tips**.
- Front-matter with names and descriptions in six languages, tags, the test record, and links.

## The styles

<!-- tables:start -->
### Effects (37)

| Preview | Style | Prompt | Try it |
|---|---|---|---|
| <img src="https://cos.fontvibe.ai/generations/user/17/e557d84c-6e8b-4bca-bf27-ef76ea5e3d38.jpeg" width="120" alt="3D Bold"> | **3D Bold**<br>Chunky block capitals with deep extrusions, each letter a different glossy candy color, lit from above so highlights roll over rounded edges and colored reflections pool on the floor. | [prompt](prompts/effects/3d-bold.md) | [fontvibe.ai](https://fontvibe.ai/styles/3d-bold) |
| <img src="https://cos.fontvibe.ai/generations/user/17/da620311-614d-4437-86a6-6c11bb2074c5.jpeg" width="120" alt="Gold 3D"> | **Gold 3D**<br>Premium 3D gold metallic text with rich warm tones and mirror-like highlights. Award energy, luxury brand feel — channel banners, birthday cards, chat-server headers. | [prompt](prompts/effects/3d-bold-gold.md) | [fontvibe.ai](https://fontvibe.ai/styles/3d-bold-gold) |
| <img src="https://cos.fontvibe.ai/generations/user/17/7d12764d-c9e3-4d6b-a67c-4bedec0f5e55.jpeg" width="120" alt="Holographic 3D"> | **Holographic 3D**<br>Iridescent chrome 3D block letters with oil-slick rainbow color shifts — cycling through pink, violet, cyan to gold. Premium CGI holographic font effect, free to generate and download. | [prompt](prompts/effects/3d-bold-holographic.md) | [fontvibe.ai](https://fontvibe.ai/styles/3d-bold-holographic) |
| <img src="https://cos.fontvibe.ai/generations/user/17/759d4099-4cb2-4a30-91a5-33928bdfd57c.jpeg" width="120" alt="Bubble 3D"> | **Bubble 3D**<br>Puffy, air-filled bubble font with glossy candy 3D surfaces. Y2K vibes, balloon bounce energy — birthday posts, chat-server headers, phone wallpapers. | [prompt](prompts/effects/3d-bold-inflated.md) | [fontvibe.ai](https://fontvibe.ai/styles/3d-bold-inflated) |
| <img src="https://cos.fontvibe.ai/generations/user/17/fb22e98f-9a02-4685-9efe-298d0de9160f.jpeg" width="120" alt="Neon Synthwave 3D"> | **Neon Synthwave 3D**<br>Bold chunky 3D letters glowing with synthwave neon — electric magenta, cyan, and sunset orange. Built for retro-futuristic energy. | [prompt](prompts/effects/3d-bold-neon.md) | [fontvibe.ai](https://fontvibe.ai/styles/3d-bold-neon) |
| <img src="https://cos.fontvibe.ai/generations/user/17/f2e648b3-fc98-48bd-a0a7-830d6407aaea.jpeg" width="120" alt="Bubble"> | **Bubble**<br>Playful inflated bubble-letter typography — glossy candy gradients, shiny highlights and soft refraction. Perfect for bubble text, name art, stickers and kids designs. | [prompt](prompts/effects/bubble.md) | [fontvibe.ai](https://fontvibe.ai/styles/bubble) |
| <img src="https://cos.fontvibe.ai/generations/user/17/268d3e8f-8aeb-41eb-8b3a-f1c65e88c0ba.jpeg" width="120" alt="Chrome Metal 3D"> | **Chrome Metal 3D**<br>Mirror-finish chrome 3D metallic text with razor-sharp silver highlights and cold industrial precision. Gaming branding, music covers, esports teams — the go-to for bold metallic authority. | [prompt](prompts/effects/chrome-metal-3d.md) | [fontvibe.ai](https://fontvibe.ai/styles/chrome-metal-3d) |
| <img src="https://cos.fontvibe.ai/generations/user/17/b97be45e-e274-46f2-883e-56455388d608.jpeg" width="120" alt="Drip Font"> | **Drip Font**<br>Heavy glossy red block letters with thick paint drips hanging from every base, teardrop ends and pooled paint on the floor, against a dark concrete wall. | [prompt](prompts/effects/drip-font.md) | [fontvibe.ai](https://fontvibe.ai/styles/drip-font) |
| <img src="https://cos.fontvibe.ai/generations/user/17/f38864d6-1b55-4b4a-a49b-73adaf3989f6.jpeg" width="120" alt="Blood Drip Font"> | **Blood Drip Font**<br>Bold crimson letters with a wet, dark-red surface and long blood drips ending in round drops, isolated on pure black under side light. | [prompt](prompts/effects/drip-font-blood.md) | [fontvibe.ai](https://fontvibe.ai/styles/drip-font-blood) |
| <img src="https://cos.fontvibe.ai/generations/user/17/481a9fca-4c50-4152-9490-bc0429ed9e4a.jpeg" width="120" alt="Ice Cream Drip Font"> | **Ice Cream Drip Font**<br>Chunky letters swirled with pink and cream soft-serve, melting into thick rounded drips over a pastel pink background. | [prompt](prompts/effects/drip-font-ice.md) | [fontvibe.ai](https://fontvibe.ai/styles/drip-font-ice) |
| <img src="https://cos.fontvibe.ai/generations/user/17/51f51094-2675-49e7-93fb-b5dbebf9cc2e.jpeg" width="120" alt="Melting Font"> | **Melting Font**<br>Glossy orange-red letters liquefying from the base down, with molten drips, warped lower edges and a glowing puddle on a dark charcoal floor. | [prompt](prompts/effects/drip-font-melting.md) | [fontvibe.ai](https://fontvibe.ai/styles/drip-font-melting) |
| <img src="https://cos.fontvibe.ai/generations/user/17/9b28045c-3443-42f8-b84c-9c5eb03f95d2.jpeg" width="120" alt="Duotone"> | **Duotone**<br>Bold condensed slab capitals in one bright color with a halftone dot texture and a solid offset shadow in a second color, on a flat contrasting ground. | [prompt](prompts/effects/duotone.md) | [fontvibe.ai](https://fontvibe.ai/styles/duotone) |
| <img src="https://cos.fontvibe.ai/generations/user/17/4cfa112b-122d-448e-a3b5-6cf953ff9763.jpeg" width="120" alt="Embossed"> | **Embossed**<br>Serif capitals blind-embossed into ivory cotton paper: no ink, only a raised relief with a crisp highlight ridge and soft shadow from low raking light. | [prompt](prompts/effects/emboss.md) | [fontvibe.ai](https://fontvibe.ai/styles/emboss) |
| <img src="https://cos.fontvibe.ai/generations/user/17/d83cc3c9-414b-4dc6-b720-1f7cddfebb68.jpeg" width="120" alt="Fire & Smoke"> | **Fire & Smoke**<br>Blazing fire and smoke effects, dramatic heat waves and ember glow. | [prompt](prompts/effects/fire-smoke.md) | [fontvibe.ai](https://fontvibe.ai/styles/fire-smoke) |
| <img src="https://cos.fontvibe.ai/generations/user/17/f4ea2a02-a238-46dc-b335-216018b85757.jpeg" width="120" alt="Futuristic"> | **Futuristic**<br>Capitals built from glowing blue wireframe triangles, semi-transparent with a bright scan beam, floating over a grid floor between HUD corner brackets. | [prompt](prompts/effects/futuristic.md) | [fontvibe.ai](https://fontvibe.ai/styles/futuristic) |
| <img src="https://cos.fontvibe.ai/generations/user/17/8d4b8d8d-24aa-4036-a63b-6a1d9ef87d77.jpeg" width="120" alt="Glass"> | **Glass**<br>Clear optical-glass capitals refracting light, with bright edge highlights and caustics, reflected on a dark surface under a green-blue aurora sky. | [prompt](prompts/effects/glass.md) | [fontvibe.ai](https://fontvibe.ai/styles/glass) |
| <img src="https://cos.fontvibe.ai/generations/user/17/3dadf071-745b-43f6-baa4-d8c622b527db.jpeg" width="120" alt="Broken Glass"> | **Broken Glass**<br>Shattered into sharp glass fragments exploding outward — razor-sharp shards radiating from the impact center with jagged fracture lines. Cinematic high-impact destruction quality. | [prompt](prompts/effects/glass-broken.md) | [fontvibe.ai](https://fontvibe.ai/styles/glass-broken) |
| <img src="https://cos.fontvibe.ai/generations/user/17/5e5f1724-6c89-4796-a202-42e41f614506.jpeg" width="120" alt="Color Glass"> | **Color Glass**<br>Thick solid glass letters, each a different jewel tone, casting colored light pools and caustic fans across a bright white studio floor. | [prompt](prompts/effects/glass-color.md) | [fontvibe.ai](https://fontvibe.ai/styles/glass-color) |
| <img src="https://cos.fontvibe.ai/generations/user/17/4d245e38-cea1-4abb-8e85-16a490f9cc03.jpeg" width="120" alt="Crystal"> | **Crystal**<br>Carved from pure gemstone crystal — faceted diamond-cut surfaces with brilliant rainbow prism dispersion and luxury sparkle. Caustic light patterns cast below. | [prompt](prompts/effects/glass-crystal.md) | [fontvibe.ai](https://fontvibe.ai/styles/glass-crystal) |
| <img src="https://cos.fontvibe.ai/generations/user/17/0f7ebd64-c757-4472-be6f-07358821cae4.jpeg" width="120" alt="Frozen Ice"> | **Frozen Ice**<br>Encased in solid ice — thick frozen block with sharp edge facets, deep internal frost cracks, and icicle drips. Photorealistic frozen water quality. | [prompt](prompts/effects/glass-frozen.md) | [fontvibe.ai](https://fontvibe.ai/styles/glass-frozen) |
| <img src="https://cos.fontvibe.ai/generations/user/17/6e185478-936e-491e-ba06-1fabb453aad2.jpeg" width="120" alt="Liquid Glass"> | **Liquid Glass**<br>Rounded letters of flowing liquid glass in clear aqua, with glossy wet highlights and soft internal refraction, on a pale lavender-to-blue gradient. | [prompt](prompts/effects/glass-liquid.md) | [fontvibe.ai](https://fontvibe.ai/styles/glass-liquid) |
| <img src="https://cos.fontvibe.ai/generations/user/17/985d9f4a-3047-44d8-ab14-37662e36bb9a.jpeg" width="120" alt="Frosted Glass"> | **Frosted Glass**<br>Milky semi-transparent frosted glass panels with soft blur and glassmorphism aesthetic — thin glass border, blurred colorful background visible through surface. Modern UI quality. | [prompt](prompts/effects/glass-morphism.md) | [fontvibe.ai](https://fontvibe.ai/styles/glass-morphism) |
| <img src="https://cos.fontvibe.ai/generations/user/17/eb45177c-8ee4-4334-a8c4-4be1d4161a28.jpeg" width="120" alt="Glitch"> | **Glitch**<br>White sans capitals split by red and cyan channel offsets, sliced by horizontal displacement bands and scanlines, reflected on a wet neon street at night. | [prompt](prompts/effects/glitch.md) | [fontvibe.ai](https://fontvibe.ai/styles/glitch) |
| <img src="https://cos.fontvibe.ai/generations/user/17/ec3a64e8-c9e7-41e2-b6b7-646a86804a23.jpeg" width="120" alt="Holographic"> | **Holographic**<br>Rounded sans letters with an iridescent foil surface shifting violet, cyan, pink and gold, glossy reflections on a dark floor with small light specks. | [prompt](prompts/effects/holographic.md) | [fontvibe.ai](https://fontvibe.ai/styles/holographic) |
| <img src="https://cos.fontvibe.ai/generations/user/17/f68ab0eb-1d5f-4218-b76f-2366bdbecb9c.jpeg" width="120" alt="Horror"> | **Horror**<br>Thin jagged red letters dripping blood, lit by a single bare bulb in a flooded tunnel, reflected in dark still water. | [prompt](prompts/effects/horror.md) | [fontvibe.ai](https://fontvibe.ai/styles/horror) |
| <img src="https://cos.fontvibe.ai/generations/user/17/0b3bf19f-6d6d-44a0-93b7-addb831e20ac.jpeg" width="120" alt="Ice Crystal"> | **Ice Crystal**<br>Translucent ice-crystal capitals with spiky frost feathering along every edge, glowing under icy blue backlight with drifting snow dust. | [prompt](prompts/effects/ice-crystal.md) | [fontvibe.ai](https://fontvibe.ai/styles/ice-crystal) |
| <img src="https://cos.fontvibe.ai/generations/user/17/29f7399e-0199-4da4-bac1-896862648199.jpeg" width="120" alt="Long Shadow"> | **Long Shadow**<br>Bold 45-degree text shadow effects in flat retro-poster colors — the long shadow look vintage design templates are built on. | [prompt](prompts/effects/kagemoji.md) | [fontvibe.ai](https://fontvibe.ai/styles/kagemoji) |
| <img src="https://cos.fontvibe.ai/styles/laser_cut/laser_cut_preview.jpg" width="120" alt="Laser Cut"> | **Laser Cut**<br>Bold sans capitals cut from warm birch wood with charred kerf edges and visible grain, raised from a dark walnut board under amber side light. | [prompt](prompts/effects/laser-cut.md) | [fontvibe.ai](https://fontvibe.ai/styles/laser-cut) |
| <img src="https://cos.fontvibe.ai/generations/user/17/bb06e9cd-2d74-4e78-bf8a-03a274369039.jpeg" width="120" alt="Luxury Gold"> | **Luxury Gold**<br>Heavy cast-gold capitals with a fine foil crinkle, deep amber shadows in the recesses and bright specular peaks, isolated on black under one spotlight. | [prompt](prompts/effects/luxury-gold.md) | [fontvibe.ai](https://fontvibe.ai/styles/luxury-gold) |
| <img src="https://cos.fontvibe.ai/generations/user/17/b16e73f6-131b-449e-acbb-4a5846cf122f.jpeg" width="120" alt="Metallic"> | **Metallic**<br>Beveled 3D capitals mixing polished gold and brushed steel, with sharp highlight lines and a cool reflective floor under directional studio light. | [prompt](prompts/effects/metallic.md) | [fontvibe.ai](https://fontvibe.ai/styles/metallic) |
| <img src="https://cos.fontvibe.ai/generations/user/17/938f01f8-5f76-4233-b386-a16cae92f301.jpeg" width="120" alt="Neon 80s"> | **Neon 80s**<br>Slanted chrome capitals reflecting a pink-to-purple sunset and a cyan grid, with neon edge glow, over a perspective grid floor lined with palm silhouettes. | [prompt](prompts/effects/neon-80s.md) | [fontvibe.ai](https://fontvibe.ai/styles/neon-80s) |
| <img src="https://cos.fontvibe.ai/generations/user/17/801e9efa-8206-4c03-bfa4-8f7f716650a9.jpeg" width="120" alt="Neon Glow"> | **Neon Glow**<br>Rounded neon-tube capitals alternating cyan and magenta, with bright tube cores, soft bloom and colored reflections on wet ground in the dark. | [prompt](prompts/effects/neon-glow.md) | [fontvibe.ai](https://fontvibe.ai/styles/neon-glow) |
| <img src="https://cos.fontvibe.ai/generations/user/17/3c61c9b4-3d1c-4541-9fdf-a7a8f8dddce5.jpeg" width="120" alt="Neon Outline"> | **Neon Outline**<br>Hollow outline capitals traced by a single glowing blue-violet neon line, dark inside, with a soft halo and a glossy floor reflection. | [prompt](prompts/effects/neon-outline.md) | [fontvibe.ai](https://fontvibe.ai/styles/neon-outline) |
| <img src="https://cos.fontvibe.ai/generations/user/17/ae761597-5c7e-4623-899d-e81e2dcd0f50.jpeg" width="120" alt="Neon Sign"> | **Neon Sign**<br>Classic roadside neon sign: glass tubes glowing warm pink and amber on a dark brick wall, with brackets and wet pavement reflections. | [prompt](prompts/effects/neon-sign.md) | [fontvibe.ai](https://fontvibe.ai/styles/neon-sign) |
| <img src="https://cos.fontvibe.ai/generations/user/17/3a30c874-63c6-4ac9-b9ba-267e64268ee5.jpeg" width="120" alt="Pixel Art"> | **Pixel Art**<br>Blocky 8-bit pixel capitals glowing amber-orange on a curved CRT arcade screen, with scanlines, phosphor bloom and a small INSERT COIN line. | [prompt](prompts/effects/pixel-art.md) | [fontvibe.ai](https://fontvibe.ai/styles/pixel-art) |
| <img src="https://cos.fontvibe.ai/generations/user/17/6c8093f0-97f2-419d-bc64-4a6bb91dc382.jpeg" width="120" alt="Pop Art"> | **Pop Art**<br>Pop-art comic capitals filled with Ben-Day dots in flat red and yellow, thick black outlines and a hard drop shadow, bursting from a starburst on a dotted blue ground. | [prompt](prompts/effects/pop-art.md) | [fontvibe.ai](https://fontvibe.ai/styles/pop-art) |
| <img src="https://cos.fontvibe.ai/generations/user/17/04c70c44-8999-4337-8eea-f2de3c3da070.jpeg" width="120" alt="Rainbow"> | **Rainbow**<br>Vibrant multi-color rainbow gradient text effects with smooth color transitions, prismatic light and joyful chromatic typography. | [prompt](prompts/effects/rainbow.md) | [fontvibe.ai](https://fontvibe.ai/styles/rainbow) |

### Aesthetics (46)

| Preview | Style | Prompt | Try it |
|---|---|---|---|
| <img src="https://cos.fontvibe.ai/generations/user/17/068a39a1-3ac3-491a-87f0-56e744f3dcf1.jpeg" width="120" alt="Anime"> | **Anime**<br>Shounen manga title lettering: heavy hand-inked black outlines, flat cel shading split into hard highlight and shadow bands, slanted dynamic letters on white with radiating speed lines. | [prompt](prompts/aesthetics/anime.md) | [fontvibe.ai](https://fontvibe.ai/styles/anime) |
| <img src="https://cos.fontvibe.ai/generations/user/17/d848e7c0-6409-4ea5-b331-b316143bfd49.jpeg" width="120" alt="Anime Character"> | **Anime Character**<br>Original anime characters with big glossy eyes, clean line art and cel shading over pastel skies, sunset rooftops or rainy night streets, in pastels or black and red. | [prompt](prompts/aesthetics/anime-character.md) | [fontvibe.ai](https://fontvibe.ai/styles/anime-character) |
| <img src="https://cos.fontvibe.ai/generations/user/17/a4f01141-9103-46db-a160-d8922a30f195.jpeg" width="120" alt="Art Deco"> | **Art Deco**<br>Opulent 1920s Art Deco typography — geometric symmetry, polished gold and chrome, sunburst motifs on black-and-gold lacquer. Perfect for luxury logos, Jazz Age invites and premium packaging. | [prompt](prompts/aesthetics/art-deco.md) | [fontvibe.ai](https://fontvibe.ai/styles/art-deco) |
| <img src="https://cos.fontvibe.ai/generations/user/17/7eece551-0b15-4fe1-abab-f0d51b9657a2.jpeg" width="120" alt="Black & White Aesthetic"> | **Black & White Aesthetic**<br>Moody black-and-white portraits cropped close in deep shadow, with hard side light, rain and smoke, heavy film grain, a soft vignette and at most one small red accent. | [prompt](prompts/aesthetics/bw-aesthetic.md) | [fontvibe.ai](https://fontvibe.ai/styles/bw-aesthetic) |
| <img src="https://cos.fontvibe.ai/generations/user/17/a66c2435-d08a-49a6-9c92-f53870fbc41e.jpeg" width="120" alt="Celestial Symbol"> | **Celestial Symbol**<br>Silver display capitals with crescent moons, stars and planet symbols inlaid into the letters, glowing under cold moonlight in a dark stone observatory. | [prompt](prompts/aesthetics/celestial-symbol.md) | [fontvibe.ai](https://fontvibe.ai/styles/celestial-symbol) |
| <img src="https://cos.fontvibe.ai/generations/user/17/91803a7c-c779-40e4-b937-b492139cbf8a.jpeg" width="120" alt="Chalk"> | **Chalk**<br>Hand-lettered cream chalk on a dark slate board: mixed script and serif lines, flourishes and small doodles, soft chalk-dust edges under warm café lighting. | [prompt](prompts/aesthetics/chalk.md) | [fontvibe.ai](https://fontvibe.ai/styles/chalk) |
| <img src="https://cos.fontvibe.ai/generations/user/17/1697b07a-db67-4362-8ce4-983375b76f4d.jpeg" width="120" alt="Chibi"> | **Chibi**<br>Super-deformed cute characters two to three heads tall with big shiny eyes and blush cheeks, thick soft line art, pastel cel colours and floating hearts, as stickers or cozy scenes. | [prompt](prompts/aesthetics/chibi.md) | [fontvibe.ai](https://fontvibe.ai/styles/chibi) |
| <img src="https://cos.fontvibe.ai/generations/user/17/e1af4232-13c7-4f89-8736-7ad04b8bb5af.jpeg" width="120" alt="Chicano"> | **Chicano**<br>Flowing black Chicano script with long dramatic swashes and sharp Old English capitals, laid down in glossy sign-painter ink with a faint grey shadow, often on skin or cream paper. | [prompt](prompts/aesthetics/chicano.md) | [fontvibe.ai](https://fontvibe.ai/styles/chicano) |
| <img src="https://cos.fontvibe.ai/generations/user/17/e66bcd9a-23a9-498c-99ca-5a41e80172f2.jpeg" width="120" alt="Comic Book"> | **Comic Book**<br>Bold comic book action typography with halftone dots, speed lines, pow/bam burst effects and classic superhero lettering style. | [prompt](prompts/aesthetics/comic-book.md) | [fontvibe.ai](https://fontvibe.ai/styles/comic-book) |
| <img src="https://cos.fontvibe.ai/generations/user/17/f3ada9b8-c945-4a4f-bc2d-2671b4906d02.jpeg" width="120" alt="Cursive"> | **Cursive**<br>Flowing pen-and-ink cursive: connected letters, looped ascenders and long swash entry and exit strokes, written in black ink on fine white paper with soft raking light. | [prompt](prompts/aesthetics/cursive.md) | [fontvibe.ai](https://fontvibe.ai/styles/cursive) |
| <img src="https://cos.fontvibe.ai/generations/user/17/6e218d7f-790b-4a2a-9667-87ff55a6b059.jpeg" width="120" alt="Aesthetic Cursive"> | **Aesthetic Cursive**<br>Thin pink cursive with bouncy loops, a pearly glitter fill and tiny hearts, on a soft blush background with a satin bow and sparkles. | [prompt](prompts/aesthetics/cursive-aesthetic.md) | [fontvibe.ai](https://fontvibe.ai/styles/cursive-aesthetic) |
| <img src="https://cos.fontvibe.ai/generations/user/17/4a8d0703-12fe-4a89-b065-80de8a15731e.jpeg" width="120" alt="Calligraphy Script"> | **Calligraphy Script**<br>Formal pointed-pen copperplate: strong thick-thin contrast, slanted oval letters and swash capitals, crisp black ink on cream paper with faint ruled guidelines. | [prompt](prompts/aesthetics/cursive-calligraphy.md) | [fontvibe.ai](https://fontvibe.ai/styles/cursive-calligraphy) |
| <img src="https://cos.fontvibe.ai/generations/user/17/236ae420-53dc-42f9-816c-ce59568f5ec8.jpeg" width="120" alt="Modern Cursive"> | **Modern Cursive**<br>Bold modern brush script: heavy loaded-brush strokes, a bouncing baseline and dry-brush drag where the brush lifts, matte black ink on a clean light ground. | [prompt](prompts/aesthetics/cursive-modern.md) | [fontvibe.ai](https://fontvibe.ai/styles/cursive-modern) |
| <img src="https://cos.fontvibe.ai/generations/user/17/bceb5c8b-153d-4eea-8f3a-b71bd5928453.jpeg" width="120" alt="Signature Script"> | **Signature Script**<br>A hand-signed autograph: one fluid pen line with a dominant capital, small connected letters and a long underline swash, in flat blue-black ink on white paper. | [prompt](prompts/aesthetics/cursive-signature.md) | [fontvibe.ai](https://fontvibe.ai/styles/cursive-signature) |
| <img src="https://cos.fontvibe.ai/generations/user/17/f545b0c8-7c3f-4b86-b0ea-6581060af8f4.jpeg" width="120" alt="Elegant Script"> | **Elegant Script**<br>Fine gold script with long hairline swashes and a looping capital, laid on matte black or ivory card beside luxury props under soft grazing light. | [prompt](prompts/aesthetics/elegant-script.md) | [fontvibe.ai](https://fontvibe.ai/styles/elegant-script) |
| <img src="https://cos.fontvibe.ai/generations/user/17/cd18a030-9db4-498b-a824-bcdea699447d.jpeg" width="120" alt="Fairy Tale"> | **Fairy Tale**<br>Ornate silver serif capitals with a small crown, glowing softly in a midnight castle room beside an open storybook, with drifting golden sparkles. | [prompt](prompts/aesthetics/fairy-tale.md) | [fontvibe.ai](https://fontvibe.ai/styles/fairy-tale) |
| <img src="https://cos.fontvibe.ai/generations/user/17/c255989f-02a5-406f-a86e-5a814b8ef41d.jpeg" width="120" alt="Flat Cartoon"> | **Flat Cartoon**<br>Friendly flat vector characters with dot eyes and simple shapes on plain colour fields or soft blobs, in bright coral, yellow and sky blue or muted terracotta and sage. | [prompt](prompts/aesthetics/flat-cartoon.md) | [fontvibe.ai](https://fontvibe.ai/styles/flat-cartoon) |
| <img src="https://cos.fontvibe.ai/generations/user/17/2a9253cd-357a-4af4-9cd6-f7249d6a04b8.jpeg" width="120" alt="Geometric"> | **Geometric**<br>Bauhaus capitals built from circles, squares and straight strokes in flat red, blue, yellow and black, standing as solid blocks under hard overhead light. | [prompt](prompts/aesthetics/geometric.md) | [fontvibe.ai](https://fontvibe.ai/styles/geometric) |
| <img src="https://cos.fontvibe.ai/generations/user/17/5024c3e6-4780-4066-b03e-b4ab1e607e60.jpeg" width="120" alt="Gothic Dark"> | **Gothic Dark**<br>Iron blackletter with sharp spurs and forged texture, edges burning crimson from backlight, inside a dark cathedral with cobwebs and drifting smoke. | [prompt](prompts/aesthetics/gothic-dark.md) | [fontvibe.ai](https://fontvibe.ai/styles/gothic-dark) |
| <img src="https://cos.fontvibe.ai/generations/user/17/b944c4f9-3742-44c3-9b06-a977c7f2a6ee.jpeg" width="120" alt="Graffiti"> | **Graffiti**<br>Wildstyle spray-paint letters with sharp arrows and overlapping shapes, filled in bright layered colors, locked in a thick black outline with drips on a red brick wall. | [prompt](prompts/aesthetics/graffiti.md) | [fontvibe.ai](https://fontvibe.ai/styles/graffiti) |
| <img src="https://cos.fontvibe.ai/generations/user/17/12f78b1e-bb3c-495e-bf77-349fe35da045.jpeg" width="120" alt="Grunge"> | **Grunge**<br>Ransom-note letters cut from mixed newspaper type, taped onto raw photocopied paper with halftone speckle, torn edges and a single punk-red accent. | [prompt](prompts/aesthetics/grunge.md) | [fontvibe.ai](https://fontvibe.ai/styles/grunge) |
| <img src="https://cos.fontvibe.ai/generations/user/17/2bce3941-5133-45cf-b826-550a26c6528b.jpeg" width="120" alt="Handwritten Script"> | **Handwritten Script**<br>Delicate handwritten script in walnut-brown ink on warm cream paper, with flowing connected letters and soft loops, beside a dip pen and an inkwell. | [prompt](prompts/aesthetics/handwritten-script.md) | [fontvibe.ai](https://fontvibe.ai/styles/handwritten-script) |
| <img src="https://cos.fontvibe.ai/generations/user/17/dcd8af2b-020e-401d-a71a-47625a69efdd.jpeg" width="120" alt="Hawaiian"> | **Hawaiian**<br>Tropical Hawaiian typography with tiki bar aesthetics, hibiscus flower accents, bamboo textures, ocean sunset gradients and island paradise vibes. | [prompt](prompts/aesthetics/hawaiian.md) | [fontvibe.ai](https://fontvibe.ai/styles/hawaiian) |
| <img src="https://cos.fontvibe.ai/generations/user/17/efa7f788-225b-4101-8b5f-067dfcd1ce83.jpeg" width="120" alt="Kawaii"> | **Kawaii**<br>Rounded retro computer windows with a slim info bar, scattered heart and sparkle stickers, soft daylight, a cream base with two pastels, grid paper and lace. | [prompt](prompts/aesthetics/kawaii.md) | [fontvibe.ai](https://fontvibe.ai/styles/kawaii) |
| <img src="https://cos.fontvibe.ai/generations/user/17/6bcdcde5-c71e-487d-bced-39208ac7ce6e.jpeg" width="120" alt="Magic Fantasy"> | **Magic Fantasy**<br>Ancient spellbook typography with mystical runes, arcane glow effects, dark magical atmosphere and wizard-inspired ornate letterforms. | [prompt](prompts/aesthetics/magic-fantasy.md) | [fontvibe.ai](https://fontvibe.ai/styles/magic-fantasy) |
| <img src="https://cos.fontvibe.ai/generations/user/17/68e85eec-360d-4d03-b7ce-491664850bfe.jpeg" width="120" alt="Medieval"> | **Medieval**<br>Ancient manuscript-inspired typography with illuminated letterforms, parchment textures, ornate borders and medieval calligraphy. | [prompt](prompts/aesthetics/medieval.md) | [fontvibe.ai](https://fontvibe.ai/styles/medieval) |
| <img src="https://cos.fontvibe.ai/generations/user/17/f6078a53-1efd-44a9-91a8-94786ae197ff.jpeg" width="120" alt="Origami"> | **Origami**<br>Capitals folded from colored paper in coral, teal, mustard and sky blue, with sharp creases and angular facets catching light, on clean white. | [prompt](prompts/aesthetics/origami.md) | [fontvibe.ai](https://fontvibe.ai/styles/origami) |
| <img src="https://cos.fontvibe.ai/generations/user/17/3add9cda-dd76-4769-88e7-e65df2e00e0b.jpeg" width="120" alt="Post Apocalyptic"> | **Post Apocalyptic**<br>Tall condensed capitals of battle-worn dark metal, split by cracks glowing with molten orange lava, with embers and ash over scorched ground. | [prompt](prompts/aesthetics/post-apocalyptic.md) | [fontvibe.ai](https://fontvibe.ai/styles/post-apocalyptic) |
| <img src="https://cos.fontvibe.ai/generations/user/17/ca3f4d4d-5c4d-43e3-9115-58ed1e6a4d37.jpeg" width="120" alt="Psychedelic"> | **Psychedelic**<br>Melting glossy bubble letters in hot pink, orange and yellow, set against vibrating concentric rainbow waves with daisies and swirls. | [prompt](prompts/aesthetics/psychedelic.md) | [fontvibe.ai](https://fontvibe.ai/styles/psychedelic) |
| <img src="https://cos.fontvibe.ai/generations/user/17/f9775b5a-6f96-476c-8102-502cf4799ea6.jpeg" width="120" alt="Racing"> | **Racing**<br>High-speed racing typography with dynamic italic angles, checkered flag patterns, metallic chrome finish and motorsport energy. | [prompt](prompts/aesthetics/racing.md) | [fontvibe.ai](https://fontvibe.ai/styles/racing) |
| <img src="https://cos.fontvibe.ai/generations/user/17/b345dea2-0d0f-4dc9-83d4-b6604341959d.jpeg" width="120" alt="Retro Pop"> | **Retro Pop**<br>Bold mid-century pop art (1950s–70s) — thick black outlines, flat candy colors, Ben-Day halftone dots and starbursts. | [prompt](prompts/aesthetics/retro-pop.md) | [fontvibe.ai](https://fontvibe.ai/styles/retro-pop) |
| <img src="https://cos.fontvibe.ai/generations/user/17/8791f87d-c0ad-4798-a85c-c059d086c2cc.jpeg" width="120" alt="Sand & Stone"> | **Sand & Stone**<br>Roman-style serif capitals carved deep into warm sandstone, V-cut grooves catching amber raking light, with sedimentary grain lines across the rock. | [prompt](prompts/aesthetics/sand-stone.md) | [fontvibe.ai](https://fontvibe.ai/styles/sand-stone) |
| <img src="https://cos.fontvibe.ai/generations/user/17/b63b87f1-24ed-4b79-af15-545a87c7eb1a.jpeg" width="120" alt="Steampunk"> | **Steampunk**<br>Victorian steampunk typography with brass gear mechanisms, copper pipe frameworks, steam-powered industrial textures and clockwork ornamental details. | [prompt](prompts/aesthetics/steampunk.md) | [fontvibe.ai](https://fontvibe.ai/styles/steampunk) |
| <img src="https://cos.fontvibe.ai/generations/user/17/3c53fc61-1f2d-4377-99cb-a3babbd68230.jpeg" width="120" alt="Stencil"> | **Stencil**<br>Olive-green military stencil capitals with bridged gaps and soft overspray, sprayed onto weathered wooden crate boards with metal corner plates. | [prompt](prompts/aesthetics/stencil.md) | [fontvibe.ai](https://fontvibe.ai/styles/stencil) |
| <img src="https://cos.fontvibe.ai/generations/user/17/2692aa77-55df-4fc1-a497-261733dbeeb6.jpeg" width="120" alt="Superhero"> | **Superhero**<br>Slanted chrome-edged red and blue 3D capitals with a flowing red cape, blasting out of a white light burst wrapped in crackling lightning. | [prompt](prompts/aesthetics/superhero.md) | [fontvibe.ai](https://fontvibe.ai/styles/superhero) |
| <img src="https://cos.fontvibe.ai/generations/user/17/04772f9f-43a5-4848-94f4-dc34340b2661.jpeg" width="120" alt="Synthwave"> | **Synthwave**<br>Chrome capitals striped with a pink-to-cyan sunset reflection and neon edge glow, over a neon grid highway with a striped retro sun and mountains. | [prompt](prompts/aesthetics/synthwave.md) | [fontvibe.ai](https://fontvibe.ai/styles/synthwave) |
| <img src="https://cos.fontvibe.ai/generations/user/17/a6067e8d-612c-4ae3-8b31-e3e4fd69cac9.jpeg" width="120" alt="Vaporwave"> | **Vaporwave**<br>Chrome block capitals in pastel pink and cyan, floating over a checkerboard floor beside a marble bust, palms and small katakana text. | [prompt](prompts/aesthetics/vaporwave.md) | [fontvibe.ai](https://fontvibe.ai/styles/vaporwave) |
| <img src="https://cos.fontvibe.ai/generations/user/17/d3e13c3c-737b-44ad-b3df-4f63c47670a3.jpeg" width="120" alt="Viking"> | **Viking**<br>Norse Viking runic typography with carved stone textures, Nordic knotwork patterns, battle-worn metallic finishes and ancient Scandinavian aesthetics. | [prompt](prompts/aesthetics/viking.md) | [fontvibe.ai](https://fontvibe.ai/styles/viking) |
| <img src="https://cos.fontvibe.ai/generations/user/17/60d62230-2f9a-4fd2-9eee-1f67ac9f3958.jpeg" width="120" alt="Vintage"> | **Vintage**<br>Serif capitals letterpress-bitten into cream cotton card with slightly broken ink, set on an old press bed among scattered metal type. | [prompt](prompts/aesthetics/vintage.md) | [fontvibe.ai](https://fontvibe.ai/styles/vintage) |
| <img src="https://cos.fontvibe.ai/generations/user/17/555e7b6d-6f08-46cf-83dc-7740d16ef242.jpeg" width="120" alt="Watercolor"> | **Watercolor**<br>Serif capitals filled with transparent watercolor washes and small floral sprigs, white paper glowing through, on deckled cold-press paper beside a paint palette. | [prompt](prompts/aesthetics/watercolor.md) | [fontvibe.ai](https://fontvibe.ai/styles/watercolor) |
| <img src="https://cos.fontvibe.ai/generations/user/17/2bf93dd7-bc9f-441b-a3dc-edb1ec26945a.jpeg" width="120" alt="Western"> | **Western**<br>Weathered red-painted slab and wood-type capitals on a sun-bleached plank sign, with rope and horseshoe details on a dusty saloon porch. | [prompt](prompts/aesthetics/western.md) | [fontvibe.ai](https://fontvibe.ai/styles/western) |
| <img src="https://cos.fontvibe.ai/generations/user/17/9d201cf9-b642-48c3-85ca-1f7fced92b06.jpeg" width="120" alt="Y2K"> | **Y2K**<br>Year 2000 nostalgia aesthetics — chrome bubbles, holographic gradients, liquid metal, and bubbly pink. The signature visual language of the early internet era. | [prompt](prompts/aesthetics/y2k.md) | [fontvibe.ai](https://fontvibe.ai/styles/y2k) |
| <img src="https://cos.fontvibe.ai/generations/user/17/4c979f43-0938-4c4d-8d9c-1545e223518a.jpeg" width="120" alt="Y2K Bubbly"> | **Y2K Bubbly**<br>Y2K bubbly inflated letters — round pillow-soft inflated forms in pastel pink-purple with glossy candy surface. Sweet 2000s party girl aesthetic. | [prompt](prompts/aesthetics/y2k-bubbly.md) | [fontvibe.ai](https://fontvibe.ai/styles/y2k-bubbly) |
| <img src="https://cos.fontvibe.ai/generations/user/17/3944206c-e33d-4b88-8cf9-4a0d1a6a95ba.jpeg" width="120" alt="Y2K Chrome"> | **Y2K Chrome**<br>Puffy chrome capitals with iridescent rainbow reflections in pink, green and blue, glowing softly on a bright white-to-pastel background. | [prompt](prompts/aesthetics/y2k-chrome.md) | [fontvibe.ai](https://fontvibe.ai/styles/y2k-chrome) |
| <img src="https://cos.fontvibe.ai/generations/user/17/4ded5ac2-1c21-4439-bd7c-b714f8f8794c.jpeg" width="120" alt="Y2K Holographic"> | **Y2K Holographic**<br>Y2K holographic gradient letters — vivid pink-purple-cyan iridescent surface with starbursts and holographic foil shimmer. Iconic millennium party aesthetic. | [prompt](prompts/aesthetics/y2k-holographic.md) | [fontvibe.ai](https://fontvibe.ai/styles/y2k-holographic) |
| <img src="https://cos.fontvibe.ai/generations/user/17/94cc7d16-0d2c-4401-80ac-db9c6d30de8f.jpeg" width="120" alt="Y2K Liquid"> | **Y2K Liquid**<br>Y2K liquid chrome letters — flowing organic metallic forms with chrome liquid drips and fluid body deformation. The iconic liquid metal aesthetic of the 2000s. | [prompt](prompts/aesthetics/y2k-liquid.md) | [fontvibe.ai](https://fontvibe.ai/styles/y2k-liquid) |

### Text styles (9)

| Preview | Style | Prompt | Try it |
|---|---|---|---|
| <img src="https://cos.fontvibe.ai/generations/user/17/c0d81fec-68d3-456a-bcb9-31ede53cb364.jpeg" width="120" alt="Chinese Ink Brush"> | **Chinese Ink Brush**<br>Chinese sumi ink brush calligraphy style applied to Latin letterforms. Deep black ink with authentic bristle texture, thick-to-thin stroke variation, and rice paper atmosphere. Perfect for Chinese restaurant branding, martial arts, wellness, and cultural design. | [prompt](prompts/text_styles/brush-chinese-ink.md) | [fontvibe.ai](https://fontvibe.ai/styles/brush-chinese-ink) |
| <img src="https://cos.fontvibe.ai/generations/user/17/82e7d584-a0ea-4046-9b2f-82e43895d45c.jpeg" width="120" alt="Dry Brush"> | **Dry Brush**<br>Raw dry brush and paint brush lettering with heavy texture, bristle spread, and imperfect grain. Bold paint-loaded strokes, grungy distressed edges, and authentic hand-painted energy. Perfect for streetwear, music branding, sports, packaging, and any project needing raw tactile power. | [prompt](prompts/text_styles/brush-dry.md) | [fontvibe.ai](https://fontvibe.ai/styles/brush-dry) |
| <img src="https://cos.fontvibe.ai/generations/user/17/896c92d8-1e25-4e8e-b269-ac7a6ba6518e.jpeg" width="120" alt="Japanese Ink Brush"> | **Japanese Ink Brush**<br>Japanese Shodo ink brush calligraphy style applied to Latin letterforms. Deep sumi black ink with authentic fude brush energy, controlled single-direction strokes, and washi paper atmosphere. Perfect for Japanese restaurant branding, tattoo design, anime, martial arts, and cultural projects. | [prompt](prompts/text_styles/brush-japanese-ink.md) | [fontvibe.ai](https://fontvibe.ai/styles/brush-japanese-ink) |
| <img src="https://cos.fontvibe.ai/generations/user/17/f5d3a32a-fad6-4e40-bba3-fbf9b2decd9a.jpeg" width="120" alt="Brush Script"> | **Brush Script**<br>Western brush script with connected letters: thick pressure downstrokes, hairline upstrokes, visible bristle streaks and dry-brush trails in warm off-black ink on textured paper. | [prompt](prompts/text_styles/brush-stroke.md) | [fontvibe.ai](https://fontvibe.ai/styles/brush-stroke) |
| <img src="https://cos.fontvibe.ai/generations/user/17/26ed817a-5f55-43cc-ab2d-869e9e5a18ed.jpeg" width="120" alt="Gothic Font"> | **Gothic Font**<br>Precise Textura blackletter: narrow broken strokes, diamond terminals and strong thick-thin contrast, in black ink with gold-touched edges on dark aged parchment. | [prompt](prompts/text_styles/gothic-font.md) | [fontvibe.ai](https://fontvibe.ai/styles/gothic-font) |
| <img src="https://cos.fontvibe.ai/generations/user/17/0e206d80-c871-4b57-b935-35ba274d8058.jpeg" width="120" alt="Minimal"> | **Minimal**<br>Dark grey geometric sans with generous spacing and a single hairline rule beneath, flat and matte on an almost empty off-white ground. | [prompt](prompts/text_styles/minimal.md) | [fontvibe.ai](https://fontvibe.ai/styles/minimal) |
| <img src="https://cos.fontvibe.ai/generations/user/17/a6fde25d-8269-49db-9404-b1d70f1761bd.jpeg" width="120" alt="Tattoo Font"> | **Tattoo Font**<br>Old English tattoo lettering inked in black with a slight blue-black cast and fine shading, healed into real skin on a forearm or wrist. | [prompt](prompts/text_styles/tattoo.md) | [fontvibe.ai](https://fontvibe.ai/styles/tattoo) |
| <img src="https://cos.fontvibe.ai/generations/user/17/c50d58c0-8dd4-4974-9998-13f7022cf670.jpeg" width="120" alt="Typewriter"> | **Typewriter**<br>Monospaced slab-serif type struck into cream paper, with uneven ink density, ribbon texture, faint letter misalignment and soft paper fibers. | [prompt](prompts/text_styles/typewriter.md) | [fontvibe.ai](https://fontvibe.ai/styles/typewriter) |
| <img src="https://cos.fontvibe.ai/generations/user/17/8ed980d9-b858-4815-9f22-84bbb4763cc8.jpeg" width="120" alt="Viking Runic"> | **Viking Runic**<br>Angular runic-style capitals made only of straight and 45-degree strokes, carved into cold steel-grey stone under an aurora night sky. | [prompt](prompts/text_styles/viking-runic.md) | [fontvibe.ai](https://fontvibe.ai/styles/viking-runic) |

### Scenes (19)

| Preview | Style | Prompt | Try it |
|---|---|---|---|
| <img src="https://cos.fontvibe.ai/styles/cinematic/preview_image.jpg" width="120" alt="Movie & Film"> | **Movie & Film**<br>Monumental movie-title capitals in warm gold metal, rim-lit by a low sun with lens flare, floating over a vast mountain landscape at golden hour. | [prompt](prompts/scenes/cinematic.md) | [fontvibe.ai](https://fontvibe.ai/styles/cinematic) |
| <img src="https://cos.fontvibe.ai/generations/user/17/c503b6e0-c179-476e-8260-2427ec024241.jpeg" width="120" alt="Action Movie"> | **Action Movie**<br>Condensed chrome-steel capitals with fine brushed grain, split warm-orange and cold-blue side light, anamorphic flare and rain-soaked city streets behind. | [prompt](prompts/scenes/cinematic-action.md) | [fontvibe.ai](https://fontvibe.ai/styles/cinematic-action) |
| <img src="https://cos.fontvibe.ai/generations/user/17/9b92aa6c-19c0-45a4-b932-a7de19acf86a.jpeg" width="120" alt="Blockbuster"> | **Blockbuster**<br>Hollywood-scale movie title lettering with chrome-polished metallic surface, intense dramatic spotlight, and volumetric lens flare. Built for epic posters, game titles, and high-impact visual projects. | [prompt](prompts/scenes/cinematic-blockbuster.md) | [fontvibe.ai](https://fontvibe.ai/styles/cinematic-blockbuster) |
| <img src="https://cos.fontvibe.ai/generations/user/17/370cce37-5784-475a-a78d-d5d9b45ed65d.jpeg" width="120" alt="Horror Movie"> | **Horror Movie**<br>Horror movie title lettering with cracked, blood-stained surfaces and dim sickly lighting. Perfect for Halloween designs, thriller posters, and dark atmospheric visuals. | [prompt](prompts/scenes/cinematic-horror.md) | [fontvibe.ai](https://fontvibe.ai/styles/cinematic-horror) |
| <img src="https://cos.fontvibe.ai/generations/user/17/ed2acd0c-2f24-4033-ae2a-155e515b0b58.jpeg" width="120" alt="Sci-Fi"> | **Sci-Fi**<br>Science fiction film title typography with cold brushed titanium surface, precision-machined edges, and deep space backgrounds. Ideal for game titles, tech brands, and futuristic designs. | [prompt](prompts/scenes/cinematic-scifi.md) | [fontvibe.ai](https://fontvibe.ai/styles/cinematic-scifi) |
| <img src="https://cos.fontvibe.ai/generations/user/17/f62eb4f9-659f-4d5a-a2ea-41f10582dba8.jpeg" width="120" alt="Video Creator"> | **Video Creator**<br>Tall condensed sans capitals in warm yellow with a dark outline and glow, a small episode line above, over a golden-hour city rooftop. | [prompt](prompts/scenes/cinematic-youtube-creator.md) | [fontvibe.ai](https://fontvibe.ai/styles/cinematic-youtube-creator) |
| <img src="https://cos.fontvibe.ai/generations/user/17/dea1ad21-e39b-4b88-8056-e3415c72fdd6.jpeg" width="120" alt="Cyberpunk"> | **Cyberpunk**<br>Chrome block capitals with magenta and cyan color fringing, horizontal glitch slices and scanlines, glowing over a rainy neon megacity at night. | [prompt](prompts/scenes/cyberpunk.md) | [fontvibe.ai](https://fontvibe.ai/styles/cyberpunk) |
| <img src="https://cos.fontvibe.ai/generations/user/17/8268ac13-9826-4615-a182-eaaa90b6d1f4.jpeg" width="120" alt="Acid Rain"> | **Acid Rain**<br>Toxic acid-rain corrosion effect with dripping green chemicals and rusted metal surfaces. Industrial dystopia aesthetic. | [prompt](prompts/scenes/cyberpunk-acid-rain.md) | [fontvibe.ai](https://fontvibe.ai/styles/cyberpunk-acid-rain) |
| <img src="https://cos.fontvibe.ai/generations/user/17/3d3053cb-aaad-4152-96e8-91338671b2b7.jpeg" width="120" alt="Bio Mech"> | **Bio Mech**<br>Biomechanical fusion of organic tissue and metal machinery. H.R. Giger-inspired dark industrial aesthetic. | [prompt](prompts/scenes/cyberpunk-bio-mech.md) | [fontvibe.ai](https://fontvibe.ai/styles/cyberpunk-bio-mech) |
| <img src="https://cos.fontvibe.ai/styles/cyberpunk_chrome/cover.jpg" width="120" alt="Chrome Metal"> | **Chrome Metal**<br>Hyper-reflective liquid chrome with mirror-finish surfaces and sharp specular highlights. Cold, premium and futuristic. | [prompt](prompts/scenes/cyberpunk-chrome.md) | [fontvibe.ai](https://fontvibe.ai/styles/cyberpunk-chrome) |
| <img src="https://cos.fontvibe.ai/generations/user/17/a1fff21e-79fa-49b9-8eb4-9a9b038fec0a.jpeg" width="120" alt="Data Stream"> | **Data Stream**<br>Cascading data stream text with digital rain and terminal green glow. Hacker and code aesthetic. | [prompt](prompts/scenes/cyberpunk-data-stream.md) | [fontvibe.ai](https://fontvibe.ai/styles/cyberpunk-data-stream) |
| <img src="https://cos.fontvibe.ai/styles/cyberpunk_electric_neon/cover.jpg" width="120" alt="Electric Neon"> | **Electric Neon**<br>Classic neon tube glow effect — single vivid color, soft light bloom and the authentic warmth of a real neon sign. | [prompt](prompts/scenes/cyberpunk-electric-neon.md) | [fontvibe.ai](https://fontvibe.ai/styles/cyberpunk-electric-neon) |
| <img src="https://cos.fontvibe.ai/generations/user/17/7cc275d7-6369-469c-ab63-7292a221737e.jpeg" width="120" alt="Hologram"> | **Hologram**<br>Translucent holographic projection effect with layered scan lines and iridescent cyan glow. Sci-fi UI aesthetic. | [prompt](prompts/scenes/cyberpunk-hologram.md) | [fontvibe.ai](https://fontvibe.ai/styles/cyberpunk-hologram) |
| <img src="https://cos.fontvibe.ai/generations/user/17/b0a06fa0-46d0-4e63-b182-33fbbe90ec2c.jpeg" width="120" alt="Neon Glitch"> | **Neon Glitch**<br>RGB color-split glitch effect with chromatic aberration and pixel distortion. Iconic look for gaming and streaming. | [prompt](prompts/scenes/cyberpunk-neon-glitch.md) | [fontvibe.ai](https://fontvibe.ai/styles/cyberpunk-neon-glitch) |
| <img src="https://cos.fontvibe.ai/generations/user/17/f92a2299-8811-4ee2-8256-1f0e9a832e35.jpeg" width="120" alt="Synthwave"> | **Synthwave**<br>Retro 80s synthwave aesthetic with neon pink-purple gradient text and iconic grid floor. Vaporwave nostalgia meets cyberpunk. | [prompt](prompts/scenes/cyberpunk-synthwave.md) | [fontvibe.ai](https://fontvibe.ai/styles/cyberpunk-synthwave) |
| <img src="https://cos.fontvibe.ai/generations/user/17/a0992207-7d12-4050-8069-c33d9a905966.jpeg" width="120" alt="Tech HUD"> | **Tech HUD**<br>Sci-fi heads-up display interface style — scan lines, targeting brackets, data readouts and tactical UI framing. | [prompt](prompts/scenes/cyberpunk-tech-hud.md) | [fontvibe.ai](https://fontvibe.ai/styles/cyberpunk-tech-hud) |
| <img src="https://cos.fontvibe.ai/generations/user/17/b56e4d82-f51d-4a61-ba9c-40af464fa0a6.jpeg" width="120" alt="Esports"> | **Esports**<br>Flat slash-cut panels with a title plate and info bar, dark arena rim light, one team colour plus one acid accent, film grain and halftone edges. | [prompt](prompts/scenes/esports.md) | [fontvibe.ai](https://fontvibe.ai/styles/esports) |
| <img src="https://cos.fontvibe.ai/generations/user/17/24bbbdc1-f7b3-46bf-bbdd-5880c580d921.jpeg" width="120" alt="Sports"> | **Sports**<br>Heavy condensed chrome capitals with a screen-printed grain, red and blue rim light and an athlete silhouette bursting through speed lines behind. | [prompt](prompts/scenes/sports.md) | [fontvibe.ai](https://fontvibe.ai/styles/sports) |
| <img src="https://cos.fontvibe.ai/generations/user/17/d0b93158-fa39-42f8-b020-8abd4dce9d4e.jpeg" width="120" alt="Football & Soccer"> | **Football & Soccer**<br>Bold capitals filled with national flag colors and outlined in gold, glowing in a floodlit stadium with confetti and a trophy shine behind. | [prompt](prompts/scenes/sports-football.md) | [fontvibe.ai](https://fontvibe.ai/styles/sports-football) |

### Occasions (18)

| Preview | Style | Prompt | Try it |
|---|---|---|---|
| <img src="https://cos.fontvibe.ai/generations/user/17/b2058c49-64e7-40eb-8bae-90d6ea98f6e3.jpeg" width="120" alt="Anniversary"> | **Anniversary**<br>Gold serif capitals catching warm candlelight against deep navy velvet, with pillar candles, rose petals and soft bokeh framing the words. | [prompt](prompts/occasions/anniversary.md) | [fontvibe.ai](https://fontvibe.ai/styles/anniversary) |
| <img src="https://cos.fontvibe.ai/generations/user/17/be25ff51-8983-4ddb-90f5-d4da8d5faddb.jpeg" width="120" alt="Birthday"> | **Birthday**<br>Rainbow-striped bubbly capitals with a crisp white outline, surrounded by confetti bursts and balloon clusters on a saturated pink-to-turquoise party background. | [prompt](prompts/occasions/birthday.md) | [fontvibe.ai](https://fontvibe.ai/styles/birthday) |
| <img src="https://cos.fontvibe.ai/generations/user/17/84ca0397-f0e0-41c8-b745-29c98678eb18.jpeg" width="120" alt="Kids Birthday"> | **Kids Birthday**<br>Vibrant rainbow cartoon birthday text effects designed for children. Each letter in a different bright saturated color, chunky bubble shapes, colorful balloons and confetti explosions. Perfect for kids birthday cards, party banners and 1st birthday celebrations. | [prompt](prompts/occasions/birthday-kids.md) | [fontvibe.ai](https://fontvibe.ai/styles/birthday-kids) |
| <img src="https://cos.fontvibe.ai/generations/user/17/f8222b77-ba7a-49f2-91c4-74d5a9423a02.jpeg" width="120" alt="Luxury Birthday"> | **Luxury Birthday**<br>Elegant gold foil text on deep dark backgrounds. Premium birthday effects with minimal decoration — no colorful confetti, just refined gold lettering and subtle sparkle for milestone celebrations and high-end cards. | [prompt](prompts/occasions/birthday-luxury.md) | [fontvibe.ai](https://fontvibe.ai/styles/birthday-luxury) |
| <img src="https://cos.fontvibe.ai/generations/user/17/a646bacd-30c1-414a-9002-99c85f75e44b.jpeg" width="120" alt="Cute Halloween"> | **Cute Halloween**<br>Chubby little ghosts, smiling pumpkins and a sleepy black cat scattered like stickers on cream, in pumpkin orange, peach and soft lilac with thick soft outlines and flat light. | [prompt](prompts/occasions/cute-halloween.md) | [fontvibe.ai](https://fontvibe.ai/styles/cute-halloween) |
| <img src="https://cos.fontvibe.ai/generations/user/17/aedd77c0-cc7b-468c-bfb0-3fd921f22cd9.jpeg" width="120" alt="For Parents"> | **For Parents**<br>Warm family-love typography — cozy knit, soft golden light and heartfelt hand-written warmth. Perfect for family name signs, home quotes and cozy decor. | [prompt](prompts/occasions/family-love.md) | [fontvibe.ai](https://fontvibe.ai/styles/family-love) |
| <img src="https://cos.fontvibe.ai/generations/user/17/3383dafc-35a0-4592-847c-5754452aaf4d.jpeg" width="120" alt="Kids Gift"> | **Kids Gift**<br>Shiny foil-balloon letters in pink, yellow, blue and green, floating among small balloons, confetti, stars and hearts on a light sky-blue background. | [prompt](prompts/occasions/kids-gift.md) | [fontvibe.ai](https://fontvibe.ai/styles/kids-gift) |
| <img src="https://cos.fontvibe.ai/generations/user/17/a38a8529-92aa-4567-b68d-a2d705d8d492.jpeg" width="120" alt="Mother's Day"> | **Mother's Day**<br>Cream-gold brush script woven with pink peonies, roses and lavender sprigs, petals resting on the strokes, over warm burgundy bokeh. | [prompt](prompts/occasions/mothers-day.md) | [fontvibe.ai](https://fontvibe.ai/styles/mothers-day) |
| <img src="https://cos.fontvibe.ai/generations/user/17/3ba5314b-1025-4a22-86a3-0fa5acda823a.jpeg" width="120" alt="Nutcracker"> | **Nutcracker**<br>Theatrical storybook scenes with nutcracker soldiers, gilded stage arches and velvet curtains in crimson, emerald and antique gold under warm golden stage light. | [prompt](prompts/occasions/nutcracker.md) | [fontvibe.ai](https://fontvibe.ai/styles/nutcracker) |
| <img src="https://cos.fontvibe.ai/generations/user/17/c8532e94-505a-4ff8-9083-c2d6bb665fa2.jpeg" width="120" alt="Pink Christmas"> | **Pink Christmas**<br>Blush and bubblegum pink fields with glossy pink baubles, a frosted pink tree, satin bows and rose gold accents under warm fairy-light glow and soft bokeh. | [prompt](prompts/occasions/pink-christmas.md) | [fontvibe.ai](https://fontvibe.ai/styles/pink-christmas) |
| <img src="https://cos.fontvibe.ai/generations/user/17/f72b696f-ba2d-4ffa-b79b-fe8b130e11e5.jpeg" width="120" alt="Pink Halloween"> | **Pink Halloween**<br>Blush and bubblegum pink scenes of glittery pink pumpkins, little ghosts in satin bows, cobwebs, bats and candies, with black accents under soft even light. | [prompt](prompts/occasions/pink-halloween.md) | [fontvibe.ai](https://fontvibe.ai/styles/pink-halloween) |
| <img src="https://cos.fontvibe.ai/generations/user/17/6f977182-39b4-4ba7-9be5-779be27420de.jpeg" width="120" alt="Preppy Christmas"> | **Preppy Christmas**<br>Tartan, gingham and candy-stripe borders and panels with neat bows, a wreath crest and a cream text panel in red, green and navy with a touch of gold foil. | [prompt](prompts/occasions/preppy-christmas.md) | [fontvibe.ai](https://fontvibe.ai/styles/preppy-christmas) |
| <img src="https://cos.fontvibe.ai/generations/user/17/0ad0e3f1-169d-42e1-b16b-08287a99e7b4.jpeg" width="120" alt="For Her"> | **For Her**<br>Rose-gold script with soft glitter and flourishing swashes, framed by blush roses and peonies on a dreamy pink bokeh background. | [prompt](prompts/occasions/romantic-her.md) | [fontvibe.ai](https://fontvibe.ai/styles/romantic-her) |
| <img src="https://cos.fontvibe.ai/generations/user/17/558c881a-9e91-4255-87c0-c115d6b721a0.jpeg" width="120" alt="Spooky Halloween"> | **Spooky Halloween**<br>A moonlit Halloween night: a huge full moon, a haunted house, gravestones, bare trees and a row of glowing jack-o-lanterns in deep indigo and pumpkin orange. | [prompt](prompts/occasions/spooky-halloween.md) | [fontvibe.ai](https://fontvibe.ai/styles/spooky-halloween) |
| <img src="https://cos.fontvibe.ai/generations/user/17/a529595d-4eb1-4868-9193-33a8308b3371.jpeg" width="120" alt="Teachers' Day"> | **Teachers' Day**<br>Warm daylight teacher appreciation cards — hand-lettered thanks on a desk of books, a globe, a red apple and fresh flowers. Made for Teachers' Day and for the whole school year. | [prompt](prompts/occasions/teachers-day.md) | [fontvibe.ai](https://fontvibe.ai/styles/teachers-day) |
| <img src="https://cos.fontvibe.ai/generations/user/17/639c6444-a697-4303-a428-febfc53b9872.jpeg" width="120" alt="Vintage Halloween"> | **Vintage Halloween**<br>Old Halloween postcards and paper decorations: grinning jack-o-lanterns, arched black cats and moon faces printed in orange, black and cream on aged card, or a sheet ghost in an old gilt-framed oil painting. | [prompt](prompts/occasions/vintage-halloween.md) | [fontvibe.ai](https://fontvibe.ai/styles/vintage-halloween) |
| <img src="https://cos.fontvibe.ai/generations/user/17/7c59eed3-a5c8-4702-8276-012021e83bb4.jpeg" width="120" alt="Watercolor Christmas"> | **Watercolor Christmas**<br>Loose wet-on-wet watercolor winter scenes of snowy villages, pines and hills in slate blue, sage and brick red, fading into white cold-press paper. | [prompt](prompts/occasions/watercolor-christmas.md) | [fontvibe.ai](https://fontvibe.ai/styles/watercolor-christmas) |
| <img src="https://cos.fontvibe.ai/generations/user/17/b697f890-d426-4116-a510-dce7e9a0bbae.jpeg" width="120" alt="Wedding"> | **Wedding**<br>Gold-foil serif with soft script flourishes on warm ivory cotton paper with a deckled edge, blush roses and eucalyptus in one corner. | [prompt](prompts/occasions/wedding.md) | [fontvibe.ai](https://fontvibe.ai/styles/wedding) |
<!-- tables:end -->

## How the prompts were made and tested

1. **Source.** Every style's layer, names, descriptions and example works come from FontVibe's public
   API. [`scripts/export.py`](scripts/export.py) rebuilds this whole repository from it.
2. **Trademark screen.** Styles whose identity depends on a brand, franchise or real person were left
   out entirely. In the rest, mentions of brands, franchises and real people were rewritten into plain
   descriptions (e.g. a named pop artist → "classic 1960s comic-panel pop art"). Every exclusion and
   every rewrite, with its reason, is in [`data/curation.json`](data/curation.json).
3. **Standalone rewrite.** FontVibe's style layer is written to sit next to a font in FontVibe's own
   pipeline, so it says things like *"when the chosen font carries its own treatment, that font's
   letterform shapes take priority"*. An LLM rewrote each layer into a self-contained prompt with
   those pipeline instructions removed and the defaults stated directly
   ([`scripts/draft_standalone.py`](scripts/draft_standalone.py)); the drafts were then checked
   mechanically for leftover pipeline wording and denylisted terms.
4. **Test on a general model.** Each standalone prompt was rendered on Google's
   `gemini-2.5-flash-image` with a short sample word
   ([`scripts/test_prompts.py`](scripts/test_prompts.py)), at most two attempts per style. Every
   image was then looked at side by side with the FontVibe preview — by an AI assistant (Claude)
   working for us, not by an automatic score — and passed only if the words were **legible and
   spelled right** and the image was **recognisably the same style**. Anything else (a swapped
   letter, an added accent, a duplicated word, stray gibberish text) was a fail. The result, model and date are
   in each page's front-matter and in [`data/tests.json`](data/tests.json).
5. **Verification.** [`scripts/verify.py`](scripts/verify.py) (stdlib only) checks that every number
   in this README matches the data, that every published style has a passed test, that no
   denylisted term survives in any published file, and that the links answer.

A pass means "this prompt produced a correct, on-style image on that model on that day" — not that it
will every time. Image models are stochastic, and other models will differ.

### Left out after testing

<!-- excluded:start -->
| Style | Try it on FontVibe | Why the standalone prompt was left out |
|---|---|---|
| `coquette_christmas` | [coquette-christmas](https://fontvibe.ai/styles/coquette-christmas) | Both attempts rendered 'NOËL' instead of 'NOEL' (added a diaeresis). |
| `floral` | [floral](https://fontvibe.ai/styles/floral) | Both attempts: flowers cover the letters and the word is not reliably readable. |
| `romantic_him` | [romantic-him](https://fontvibe.ai/styles/romantic-him) | Both attempts: legible, but brass letters on a wood panel instead of stitched leather — not recognisably this style. |
| `spring_holiday` | [spring-holiday](https://fontvibe.ai/styles/spring-holiday) | Both attempts: letters built from flowers; the word is barely readable. |
| `vintage_christmas` | [vintage-christmas](https://fontvibe.ai/styles/vintage-christmas) | Both attempts rendered 'NOËL' instead of 'NOEL' (added a diaeresis). |
<!-- excluded:end -->

These styles still work on FontVibe — they just didn't survive without FontVibe's font pipeline, so a
standalone prompt for them would have been a promise we couldn't keep.

In addition, styles whose identity depends on a brand, franchise or real person were left out before
testing; [`data/curation.json`](data/curation.json) lists them with the reason for each.

### Languages

Names and descriptions are FontVibe's own translations, not machine-translated for this repo. Where a
translation would have carried a brand name it was dropped instead of rewritten, so a few fields are
empty. Styles with a non-empty field, per language:

<!-- languages:start -->
| | en | ja | zh | es | pt | de |
|---|---:|---:|---:|---:|---:|---:|
| names | 129 | 128 | 128 | 128 | 128 | 128 |
| descriptions | 129 | 129 | 128 | 128 | 128 | 128 |
<!-- languages:end -->

## Files

| Path | What |
|---|---|
| `prompts/<category>/<slug>.md` | One page per style: prompts, examples, tips, test record |
| `index.json` | Everything above in one file; the npm package ships the same file |
| `data/source.json` | The screened snapshot of FontVibe's public API that the pages are built from |
| `data/standalone.json` | The standalone prompts, tips and test words, with a hash of the layer each was written from |
| `data/tests.json` | Every test generation: model, date, sample text, result and reviewer note |
| `data/curation.json` | Exclusions, rewrites and the denylist, each with a reason |
| `scripts/` | `export.py` (rebuild), `verify.py` (check), `draft_standalone.py`, `test_prompts.py` |
| `npm/` | The `text-effect-prompts` package |

Images are **not** stored here: previews and examples are hotlinked from FontVibe's CDN and link to
their pages on fontvibe.ai.

---

## Attribution

The prompts and data are [CC BY 4.0](LICENSE). CC BY asks you to credit the source "in any
reasonable manner requested by the licensor". Here's what we ask for — copy whichever fits, and
use the style's own page where you can:

**Markdown**
```markdown
Prompt from [FontVibe](https://fontvibe.ai/styles/neon-glow) ·
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
```

**HTML**
```html
Prompt from <a href="https://fontvibe.ai/styles/neon-glow">FontVibe</a> ·
<a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>
```

**Plain text** (for a CLI, a NOTICE file, an app's about screen)
```
Prompt from FontVibe — https://fontvibe.ai/styles/neon-glow — CC BY 4.0
```

Using many of them? Link the collection: `https://fontvibe.ai/styles`.
From code, `tep.attribution('neon-glow', 'html')` returns the right line for any style.

A few things worth saying plainly:

- **Please link the site, not just this repo.** Each style's page on fontvibe.ai is where it can be
  tried with your own words and real fonts — that's what your readers will actually find useful.
  This repo is the raw material behind it.
- **Add `rel="nofollow"` if you prefer.** It's your page; we're not asking you to pass ranking
  signals, and we'd rather you credit us with a nofollow link than not credit us at all.
- **A link is not strictly required** — CC BY's own words are "to the extent reasonably
  practicable". In a printed piece or a terminal app, plain text is fine.
- **This is about republishing the prompts or data.** We don't ask for credit on the images you
  make with them (though we're always glad to see them).

## Citing it

There's a [`CITATION.cff`](CITATION.cff), so GitHub's "Cite this repository" button works.

```bibtex
@misc{fontvibe_text_effect_prompts,
  title        = {Awesome Text Effect Prompts},
  author       = {{FontVibe}},
  year         = {2026},
  version      = {1.0.0},
  howpublished = {\url{https://fontvibe.ai/styles}},
  note         = {AI text-effect prompts tested on a general image model, names in six languages. CC BY 4.0}
}
```

## License

- **Prompts, style layers, names, descriptions and all other data**: [CC BY 4.0](LICENSE).
- **Code** (`scripts/`, and the JavaScript in `npm/`): [MIT](LICENSE-CODE).
- **Images** are not part of this repository; they're hotlinked from FontVibe and remain under
  [FontVibe's terms](https://fontvibe.ai/terms).

## Contributing

Ran a prompt on another model? [Open an issue](https://github.com/Funovate-Technology/awesome-text-effect-prompts/issues/new)
with the model name and the result — pass or fail. That's the most useful thing anyone can add here.
Found a brand or a real person's name that slipped through? Same place; it's a bug.

---

Built and maintained by [FontVibe](https://fontvibe.ai). Try every style with your own words at
[fontvibe.ai/styles](https://fontvibe.ai/styles).
