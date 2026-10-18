---
name: quick-ad
description: Builds a scroll-stopping static ad in about 15 minutes with the Mastermind Quickstart Builder — one emotional truth, one punchline formula, one visual format, an optional native caption, and a three-question test — then renders a simple mockup. Use when someone wants an ad, poster, billboard line, or social static "quickly", "in 15 minutes", "without overthinking", says they're not a copywriter, or needs a fast first draft before a full build.
---

# Quickstart Builder — built in 15, flinch in 3

The shortcut version of the Mastermind method for beginners, overthinkers, time-crunched creators, and teams that need fast output. Hand the user structure, format, and fire, step by step. Results before perfection.

Use a concise, respectful workflow without assumptions about the user's competence. Creativity judgments here are hypotheses, not measured audience behavior.

## Inputs

Ask only for what's missing, in one message: what is being advertised, who it's for, and where it will run. If the user says "just make something", pick reasonable assumptions and state them in one line.

Before Step 1, note user-provided product facts versus assumptions; never invent hours, quantified proof, testimonials, capabilities or guarantees. Brand and legal constraints outrank black/white/accent defaults.

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
| Exhaustion, longing, relief | Human Moment | One person's pose says it before the words do |

Quick gut check: if the sting lives in a person's body (slumped shoulders, eyes closed over a coffee), use the Human Moment and show a person — don't default to type-only.

Drop the line into that format. Done is better than beautiful. For billboards, prefer Bold Poster, Mirror Split, or a big Human Moment figure — the others are too dense to read at distance.

Constraints: black/white + one accent colour, one font, one focal point, no gradients, and no stock faces (a specific person in a telling moment is fine — a posed, smiling model is not). Screenshot and meme formats use invented conversations and original or licensed imagery — never real people, real brand UIs, or famous meme photos.

## Step 4 — Add a native caption (optional)

| Platform | Start with… | Add… |
|---|---|---|
| Instagram | "Ever felt this way?" | "Save this for when it hits again." |
| TikTok | "If this is you… stitch it." | "Send this to your messy twin." |
| LinkedIn | "Not everyone will get this…" | "What's your version of this story?" |
| Email | "I almost didn't send this…" | "Reply if this hit." |

Pick the tone that fits the tribe. Don't explain — echo their thoughts. Billboards, posters, and print get no caption; add a small brand sign-off instead.

## Step 5 — Render it

If an artifact tool is available in the OpenAI surface, render a self-contained SVG mockup at the placement's proportions (Instagram 1080×1350, story 1080×1920, LinkedIn 1200×627, 48-sheet billboard 2400×1200, US bulletin 2400×700, portrait poster 1414×2000). Use `Inter, 'Helvetica Neue', Helvetica, Arial, sans-serif`, weight 900 for the line, typographic apostrophes, and the accent on the one word that stings.

For a Human Moment, draw the person directly as a bold vector figure: a few big shapes (head, neck, torso cropped by the bottom edge, thick round-capped limbs), profile or three-quarter back, a minimal or no face, the pose carrying the emotion, and the one prop in the accent colour. If the user wants a real photo, add a short photo brief (subject, moment, framing with empty space for text, light, aspect ratio, no text or logos) they can generate or shoot, and offer to drop their photo into the layout in black and white. When the `ad-blueprint` skill is installed, its `references/render-mockup.md` has full templates, figure-construction rules, and the compositing template.

Provide an image preview if possible, or a file link **only when the file really exists and was verified**. If an SVG/image cannot be created, supply the exact visual plan and mark **not rendered**. A text-only layout does not satisfy a requested person-led image.

## Step 6 — Test with three questions

Give the user these to ask someone cold (and answer them yourself, honestly, first):

1. "What emotion do you feel in 3 seconds?"
2. "Would you screenshot this?"
3. "Would you send it to a friend?"

Yes → candidate for real audience testing. No → cut words, try a more appropriate format, or rethink the insight. Answering these questions internally is not evidence of actual viewer response.

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
