# Rendering the static mockup

A mockup makes the taste test honest: lines that read well in a paragraph often fall apart on a canvas. Render every finished ad, then judge the render, not the idea.

## Output

- Default to a **self-contained SVG** (scales cleanly, prints, opens anywhere). Use a single self-contained HTML page instead when the format needs layered UI (Screenshot Confession, Receipt Stack) that is easier to build with HTML/CSS.
- Name files `ad-<slug>-<placement>.svg` (for example `ad-fully-booked-billboard-48sheet.svg`). One file per variant when rendering the 2×2.
- No external assets, web fonts, scripts, or remote images. Use the font stack `Inter, 'Helvetica Neue', Helvetica, Arial, sans-serif`.
- If the environment can display images inline, show the mockup there as well as saving the file. Otherwise save it and give the path.

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

## People and imagery

When Step 4 says the sting lives in a body, the ad needs a person. Don't fall back to type-only because type is easier. The model draws vectors directly; it does not create photographs in this workflow. So there are two ways to put a person in the ad, and both work with no outside service:

| Route | What the model does | Best for |
|---|---|---|
| **A. Vector figure** (default) | Draws the person directly in the SVG as a bold, pictogram-style figure | Billboards, posters, any time a finished visual is wanted now |
| **B. Photo** | Writes an image brief, builds the layout around a sized placeholder, and composites the photo when the user supplies it | When the user wants photographic realism and will generate or shoot the image |

Offer route B alongside route A whenever realism would add something; deliver route A in the same turn so the user always has a finished mockup.

### Route A — drawing a vector figure

Think Swiss poster or airport pictogram, not cartoon or realism.

- **Build from 5–8 big primitives:** head (ellipse), neck (rounded rect), torso (one path, cropped by the canvas edge), limbs (thick round-capped strokes), hair as one or two solid shapes. No outlines around the whole figure.
- **Separate overlapping parts with the double-stroke trick:** draw a limb twice — first a wider stroke in the background colour, then the figure-colour stroke on top — so an arm reads in front of the torso.
- **Profile or three-quarter back.** Faces are minimal: a closed-eye curve, a nose wedge, or nothing. Never attempt a realistic face.
- **The pose is the emotion:** slumped shoulders and closed eyes (exhausted), head down (shame), arms up (relief), back turned (lonely), leaning forward (urgent).
- **One prop carries the story and takes the accent colour** (cup, phone, keys, laptop glow). Everything else is the figure colour on the background.
- **Crop big:** the figure fills 60–90% of the canvas height and bleeds off the bottom edge. Small figures disappear at distance.
- **Characterise with silhouette cues**, such as a scrubs V-neck, hard hat, headset, apron, or hair bun. Don't caricature facial or body features, and keep the cast varied and respectful across a campaign.
- **Check the thumbnail:** at about 300 px wide the pose and the prop must still read.

### Route B — photo brief and compositing

Write the brief so it pastes straight into any image generator or goes to a photographer:

```
PHOTO BRIEF — [ad slug]
Subject: one [specific person: role, age range, clothing], fictional, not a real or famous person
Moment: [the telling action, e.g. "hands wrapped around a paper cup, eyes closed, still in scrubs"]
Expression: candid, unposed, not smiling at the camera, not looking at the camera
Framing: [crop, e.g. "medium close-up, subject on the left third, empty dark space on the right for text"]
Light and time: [e.g. "blue pre-dawn light through a café window, single warm lamp"]
Setting: [a real-feeling place, minimal background]
Style: documentary photography, 35 mm, natural grain, shallow depth of field
Aspect ratio: [the photo area's ratio, e.g. 13:12 for the left panel of a 2:1 billboard]
Exclude: text, logos, watermarks, extra people, brand names, stock-photo smiles
```

Then:

1. Build the layout now with a placeholder: a `#3A3A3A` rectangle in the photo area, labelled in small type with the brief's "Moment" line.
2. When the user provides the image, save it next to the mockup and swap the placeholder for an `<image>` element. Convert the photo to black and white with an SVG filter so the accent stays the only colour (template below).
3. Put the line on a solid area — a split panel, or genuinely empty space in the photo. Never lay text over a busy part of the image, and don't use gradient scrims (Chokehold: no gradients).
4. To make the file fully self-contained, embed the photo as a base64 data URI; otherwise reference it by relative path and keep the two files together.

The user is responsible for the rights to the photo they provide. Follow the platform's and the country's disclosure rules for AI-generated imagery, and never present a generated person as a real customer.

### Route C — objects and metaphor

When the sting lives in a thing, draw the thing: a crack across a screen, a stack of tab shapes, a cold cup, a calendar with every slot filled. The same rules apply: big shapes, one accent.

Never imitate a real person, a real brand's interface, or a famous meme photo.

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

## Template — Human Moment, vector figure (Swiss F12, 2.1:1)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2400 1144" width="2400" height="1144">
  <rect width="2400" height="1144" fill="#0A0A0A"/>
  <!-- Figure: night-shift nurse in profile, facing right, cropped by the bottom edge -->
  <g fill="#F2F2F2">
    <path d="M230 1144 C230 900 290 760 410 700 C470 672 540 664 600 668 C690 676 760 716 800 796 C838 872 850 1000 850 1144 Z"/>
    <rect x="500" y="560" width="100" height="140" rx="30"/>
    <ellipse cx="560" cy="450" rx="130" ry="150"/>
    <path d="M680 440 L725 500 L678 515 Z"/>
    <circle cx="430" cy="330" r="70"/>
  </g>
  <path d="M440 400 C470 300 580 280 660 330" stroke="#0A0A0A" stroke-width="14" fill="none" stroke-linecap="round"/>
  <path d="M600 430 Q625 445 650 430" stroke="#0A0A0A" stroke-width="10" fill="none" stroke-linecap="round"/>
  <path d="M500 690 L560 790 L620 690" stroke="#0A0A0A" stroke-width="12" fill="none" stroke-linejoin="round"/>
  <!-- Arm drawn twice: wide background stroke, then figure stroke, so it separates from the torso -->
  <path d="M740 780 L800 980 L930 760" stroke="#0A0A0A" stroke-width="112" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M740 780 L800 980 L930 760" stroke="#F2F2F2" stroke-width="84" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <!-- The prop carries the accent -->
  <rect x="870" y="590" width="130" height="150" rx="18" fill="#FFB300"/>
  <path d="M1000 630 C1052 630 1052 700 1000 700" stroke="#FFB300" stroke-width="22" fill="none"/>
  <g stroke="#F2F2F2" stroke-width="12" fill="none" stroke-linecap="round" opacity="0.7">
    <path d="M910 560 C890 530 930 510 910 480"/>
    <path d="M955 560 C935 530 975 510 955 480"/>
  </g>
  <g font-family="Inter, 'Helvetica Neue', Helvetica, Arial, sans-serif" font-weight="900" letter-spacing="-4">
    <text font-size="170" fill="#F2F2F2">
      <tspan x="1220" y="470">Your night</tspan>
      <tspan x="1220" y="640">ends here.</tspan>
    </text>
    <text x="1220" y="900" font-size="54" font-weight="700" letter-spacing="0" fill="#FFB300">[Café name] · Open 05:30</text>
  </g>
</svg>
```

## Template — Human Moment, photo split (48-sheet, 2:1)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2400 1200" width="2400" height="1200">
  <defs>
    <filter id="mono"><feColorMatrix type="saturate" values="0"/></filter>
  </defs>
  <rect width="2400" height="1200" fill="#0A0A0A"/>
  <!-- Until the photo exists: placeholder sized to the photo area -->
  <!-- <rect width="1300" height="1200" fill="#3A3A3A"/> -->
  <!-- <text x="60" y="1140" font-family="Inter, Arial, sans-serif" font-size="32" fill="#BBBBBB">PHOTO: nurse in scrubs, eyes closed, hands around a cup, pre-dawn</text> -->
  <image href="photo.jpg" x="0" y="0" width="1300" height="1200" preserveAspectRatio="xMidYMid slice" filter="url(#mono)"/>
  <g font-family="Inter, 'Helvetica Neue', Helvetica, Arial, sans-serif" font-weight="900" letter-spacing="-4">
    <text font-size="150" fill="#F2F2F2">
      <tspan x="1400" y="520">Your night</tspan>
      <tspan x="1400" y="670">ends here.</tspan>
    </text>
    <text x="1400" y="1060" font-size="52" font-weight="700" letter-spacing="0" fill="#FFB300">[Café name] · Open 05:30</text>
  </g>
</svg>
```

Adapt these templates; don't treat them as the only layouts. The format, not the template, should come from the Style Mapper.
