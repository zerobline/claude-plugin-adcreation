# Rendering the static mockup

A mockup makes the taste test honest: lines that read well in a paragraph often fall apart on a canvas. Render every finished ad, then judge the render, not the idea.

## Output

- Default to a **self-contained SVG** (scales cleanly, prints, opens anywhere). Use a single self-contained HTML page instead when the format needs layered UI (Screenshot Confession, Receipt Stack) that is easier to build with HTML/CSS.
- Name files `ad-<slug>-<placement>.svg` (for example `ad-fully-booked-billboard-48sheet.svg`). One file per variant when rendering the 2×2.
- No external assets, web fonts, scripts, or remote images. Use the font stack `Inter, 'Helvetica Neue', Helvetica, Arial, sans-serif`.
- Where the surface supports inline previews or artifacts, show the mockup there as well as saving the file. Where it can only write files, save it and give the path.

## Canvas sizes

Set the SVG `viewBox` to the placement's proportions. Common sizes (always confirm the exact spec, bleed, and safe area with the media owner or printer):

| Placement | Real size | Ratio | Mockup canvas (px) |
|---|---|---|---|
| US bulletin billboard | 14 × 48 ft | 1 : 3.43 | 2400 × 700 |
| UK/EU 48-sheet billboard | 3.05 × 6.10 m | 1 : 2 | 2400 × 1200 |
| UK 96-sheet billboard | 3.05 × 12.19 m | 1 : 4 | 2400 × 600 |
| Swiss F12 | 128 × 268.5 cm | 1 : 2.1 | 2400 × 1144 |
| Swiss F4 (Weltformat), portrait | 89.5 × 128 cm | 0.7 : 1 | 1400 × 2002 |
| 6-sheet / bus shelter, portrait | 1.2 × 1.8 m | 2 : 3 | 1200 × 1800 |
| A-series poster (A0–A3), portrait | — | 1 : 1.414 | 1414 × 2000 |
| Instagram / Facebook feed | — | 4 : 5 or 1 : 1 | 1080 × 1350 or 1080 × 1080 |
| Story / reel cover | — | 9 : 16 | 1080 × 1920 |
| LinkedIn single image | — | 1.91 : 1 or 1 : 1 | 1200 × 627 or 1080 × 1080 |
| Email header | — | ~3 : 1 | 1200 × 400 (displays at 600 wide) |

## Layout rules (the Chokehold Constraints in practice)

- **Palette:** one background, one text colour, one accent. Default black `#0A0A0A`, white `#FFFFFF`, and one accent (red `#FF2D2D`, neon green `#2DFF7A`, or electric blue `#2D5BFF`). A brand colour replaces the accent; it doesn't add to it.
- **Type:** one family, weight 800–900 for the line, 500–700 for small labels. Tight tracking on big type (`letter-spacing` around −0.02em). Break lines by hand with `<tspan>` at natural breath points.
- **Scale:** on a Bold Poster the line spans 60–85% of the canvas width. The brand sign-off is at most a fifth of the line's cap height.
- **Margins:** keep everything at least 5% inside each edge (8% on billboards).
- **One focal point:** if two things compete, shrink or delete one.
- **Accent with intent:** colour only the word that carries the sting.
- **Fit check:** estimate text width as roughly 0.6 × font size per character for bold sans; shrink the font before ever letting a line touch a margin.

## Imagery

Images can't be photographed here. Options, in order of preference:

1. **Typographic or shape-based metaphor** drawn in SVG (a crack across a screen, a stack of tab shapes, a split frame).
2. **Labelled placeholder** — a neutral grey box with a short art-direction note ("Photo: untouched coffee going cold beside a laptop, 11 p.m., single desk lamp") so a designer or photographer can fill it.
3. **Image-generation prompt** in the build sheet when the user wants to generate the photo with another tool.

Never imitate a real person, real brand UI, or a famous meme photo.

## Thumbnail test

If a headless browser or image tool is available, rasterise the mockup to PNG and look at it at about 300 px wide. That approximates a distant glance or a fast scroll. If the line isn't readable at that size, enlarge it or cut words before scoring the 5D grid.

## Mockup ≠ print file

The mockup is for judging the idea. Before printing, a designer or printer must produce the final artwork to the media owner's spec: exact dimensions, bleed, CMYK or the required colour profile, resolution, and any legal text. Say so in the build sheet whenever the placement is printed.

## Template — Mirror Split billboard (48-sheet, 2:1)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2400 1200" width="2400" height="1200">
  <rect x="0" y="0" width="1200" height="1200" fill="#FFFFFF"/>
  <rect x="1200" y="0" width="1200" height="1200" fill="#0A0A0A"/>
  <g font-family="Inter, 'Helvetica Neue', Helvetica, Arial, sans-serif">
    <text x="130" y="300" font-size="56" font-weight="600" letter-spacing="10" fill="#0A0A0A" fill-opacity="0.5">SAYS</text>
    <text font-size="210" font-weight="900" letter-spacing="-5" fill="#0A0A0A">
      <tspan x="130" y="540">Fully</tspan>
      <tspan x="130" y="750">booked.</tspan>
    </text>
    <text x="1330" y="300" font-size="56" font-weight="600" letter-spacing="10" fill="#FFFFFF" fill-opacity="0.5">FEELS</text>
    <text font-size="210" font-weight="900" letter-spacing="-5" fill="#FFFFFF">
      <tspan x="1330" y="540">Still</tspan>
      <tspan x="1330" y="750" fill="#FF2D2D">terrified.</tspan>
    </text>
    <text x="2270" y="1090" text-anchor="end" font-size="52" font-weight="700" fill="#FFFFFF">Steadybook. Know next month.</text>
  </g>
</svg>
```

## Template — Bold Poster (Instagram 4:5)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1350" width="1080" height="1350">
  <rect width="1080" height="1350" fill="#0A0A0A"/>
  <g font-family="Inter, 'Helvetica Neue', Helvetica, Arial, sans-serif" font-weight="900" letter-spacing="-3">
    <text font-size="118" fill="#FFFFFF">
      <tspan x="80" y="560">You’re not</tspan>
      <tspan x="80" y="690">behind.</tspan>
      <tspan x="80" y="860">You’re building</tspan>
      <tspan x="80" y="990" fill="#2DFF7A">in silence.</tspan>
    </text>
  </g>
</svg>
```

Use typographic apostrophes and quotes (’ “ ”) in rendered text; straight quotes look broken at display sizes.

Adapt these templates; don't treat them as the only layouts. The format, not the template, should come from the Style Mapper.
