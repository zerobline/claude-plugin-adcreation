---
name: quick-ad
description: Builds a scroll-stopping static ad in about 15 minutes with the Mastermind Quickstart Builder — one emotional truth, one punchline formula, one visual format, an optional native caption, and a three-question test — then renders a simple mockup. Use when someone wants an ad, poster, billboard line, or social static "quickly", "in 15 minutes", "without overthinking", says they're not a copywriter, or needs a fast first draft before a full build.
---

# Quickstart Builder — built in 15, flinch in 3

The shortcut version of the Mastermind method for beginners, overthinkers, time-crunched creators, and teams that need fast output. Hand the user structure, format, and fire, step by step. Results before perfection.

Assume the user is overwhelmed, not a copywriter, and doesn't know what to say. That's fine — the structure does the work.

## Inputs

Ask only for what's missing, in one message: what is being advertised, who it's for, and where it will run. If the user says "just make something", pick reasonable assumptions and state them in one line.

## Step 1 — Pick the emotional truth

Write two or three fill-ins and choose the one that makes you flinch a little:

> "They want to be seen as **[admirable identity]**, but secretly feel **[raw emotion]**."
>
> "They crave **[positive thing]**, but it's wrapped in **[uncomfortable truth]**."

Don't overthink. The one that hits becomes the **truth core**.

## Step 2 — Turn it into a punchline

| Type | Formula | Example |
|---|---|---|
| Shame Mirror | "You're not [label]. You're just [truth]." | "You're not lazy. You're just scared." |
| Contradiction | "Not [assumption]. [New truth]." | "Not structure. Permission." |
| Identity Unlock | "[Hidden trait]. [Empowering truth]." | "Messy minds. Powerful results." |

Write two or three versions. Read them aloud. The winner hits in 3 seconds and makes you whisper "oof". Roadside billboards: 7 words or fewer.

## Step 3 — Choose a visual format

| Feeling | Format | Why it works |
|---|---|---|
| Shame or guilt | Screenshot Confession | Feels private, like a text thread |
| Identity shift | Bold Poster | Looks iconic; lets the line breathe |
| Pretend vs. panic | Mirror Split | Exposes the contradiction visually |
| Chaos or stress | Receipt Stack | Clutter becomes the metaphor |
| Irony or sarcasm | Meme Flip | Scroll-stopper with bite |

Drop the line into that format. Done is better than beautiful. For billboards, prefer Bold Poster or Mirror Split — the others are too dense to read at distance.

Constraints: black/white + one accent colour, one font, one focal point, no stock faces, no gradients. Screenshot and meme formats use invented conversations and original or licensed imagery — never real people, real brand UIs, or famous meme photos.

## Step 4 — Add a native caption (optional)

| Platform | Start with… | Add… |
|---|---|---|
| Instagram | "Ever felt this way?" | "Save this for when it hits again." |
| TikTok | "If this is you… stitch it." | "Send this to your messy twin." |
| LinkedIn | "Not everyone will get this…" | "What's your version of this story?" |
| Email | "I almost didn't send this…" | "Reply if this hit." |

Pick the tone that fits the tribe. Don't explain — echo their thoughts. Billboards, posters, and print get no caption; add a small brand sign-off instead.

## Step 5 — Render it

Render a self-contained SVG mockup at the placement's proportions (Instagram 1080×1350, story 1080×1920, LinkedIn 1200×627, 48-sheet billboard 2400×1200, US bulletin 2400×700, portrait poster 1414×2000). Use `Inter, 'Helvetica Neue', Helvetica, Arial, sans-serif`, weight 900 for the line, typographic apostrophes, and the accent on the one word that stings. When the `ad-blueprint` skill is installed, its `references/render-mockup.md` has full templates and sizes.

Show the mockup inline where the surface allows; otherwise save it as `ad-<slug>-<placement>.svg` and give the path.

## Step 6 — Test with three questions

Give the user these to ask someone cold (and answer them yourself, honestly, first):

1. "What emotion do you feel in 3 seconds?"
2. "Would you screenshot this?"
3. "Would you send it to a friend?"

Yes → ship it. No → cut five words, try a new format, or punch harder.

## Output

```markdown
**Truth core:** …
**Punchline:** "…"  (alternates: "…", "…")
**Format:** … · accent: … · placement: …
**Caption / sign-off:** …
**3-question check:** emotion … · screenshot? … · send? …
**Mockup:** [inline or file path]
```

Close with one line offering the full build: the `ad-blueprint` skill runs all seven steps with scoring, tribe work, and variants when the user wants to go deeper.
