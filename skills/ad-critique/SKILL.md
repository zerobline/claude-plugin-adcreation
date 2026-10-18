---
name: ad-critique
description: Critiques and scores an existing ad, billboard, poster, social static, or ad line like a cold-blooded creative director, using the Mastermind taste tools (first-glance read, Spike Meter, Scroll-Test or Glance Test, Recognition Filter, 5D Taste Calibration Grid), and names exactly what to cut, sharpen, or rebuild. Use when someone shares an ad image, mockup, or copy and asks "is this good", "rate my ad", "score this billboard", "roast/tear apart this ad", "will this work", or "why isn't this ad performing".
---

# Ad Critique — the cold-blooded creative director

Judge the ad the way the audience meets it: fast, distracted, and uninterested. Be honest, not polite. Critique the work, never the person.

## Inputs

- **The ad**: an image or mockup file (open and look at it), or the copy plus a description of the visual.
- **Placement**: billboard, poster, print, Instagram, LinkedIn, TikTok cover, email, etc. If unknown, judge it as a social static and say so.
- **Audience and goal**, if given. Don't block on them; infer, and state the inference.

## 1. First-glance read (before analysing anything)

Look once, as a passer-by would, and write down immediately:

- What it says in **1.5 seconds** (social) or **one glance** (out-of-home).
- The **first emotion** it triggers, if any.
- Where the eye lands first, and whether that's the right place.

If the message can't be stated after one look, that is the headline finding: a clarity failure. Everything else is secondary.

## 2. Find the Spike Core (or its absence)

State the emotional truth the ad is built on in one sentence. If it is built on a feature, a price, or a generic benefit ("fast", "easy", "quality"), say so plainly: the root problem is the absence of an emotional truth, and polishing won't fix it.

## 3. Score

**Spike Meter** for the main line (1–5 each): Specificity · Emotional Hit · Self-Recognition. Average below 4 = the line dies.

**Scroll-Test** (social) or **Glance Test** (out-of-home), pass/fail each:

1. Get it in 1.5 seconds (or one glance at distance)?
2. Does the image *extend* the punchline rather than just match it?
3. Does it feel premium, clean, confident — like a top-tier brand?
4. Would someone screenshot it (or repeat the line later)?

3+ of 4 = shippable; missing more than 2 = strip, simplify, sharpen.

**Recognition Filter** (when the audience is known, 0–5 each): emotional specificity · identity tension · social relatability · non-job-dependent. 16–20 = the tribe is clear.

**5D Taste Calibration Grid** (1–5 each):

| Dimension | Ask | If low, fix by… |
|---|---|---|
| Clarity | Is the core message instantly obvious? | Remove clever phrasing. Cut to the bone. |
| Surprise | Does it flip a cliché or subvert the expected tone? | Revisit the belief flip or the metaphor. |
| Emotion | Do I *feel* something — shame, joy, relief? | Push deeper into the contradiction. |
| Recognition | Would the tribe say "that's literally me"? | Adjust voice or visual for resonance. |
| Visual Power | Would I stop on the look alone? | Increase contrast. Strip filler. |

**Verdict:** 20–25 **Publish** · 16–19 **Tweak** (name the one word, one visual, one tone) · below 16 **Rebuild** from the Spike Core.

Bonus filter: would someone share it with one word — "Mood"?

### Scoring discipline

- A 5 is diary-worthy — it feels like a secret being exposed. Most ads deserve 2s and 3s; say so.
- Feature-led lines cap at 3 on Emotional Hit.
- Don't soften a verdict because the user made the ad or seems invested. The kind thing is the useful thing.

## 4. Constraint audit (Chokehold Constraints)

List each violation found:

- More than black/white + one accent colour.
- More than one focal point competing.
- Stock faces instead of metaphor or screenshot.
- More than one font, or gradients.
- Out-of-home only: main line over 7 words (roadside), QR code on a roadside billboard, a sign-off that competes with the line, text unreadable at thumbnail size.
- Risks: invented testimonials or stats, real people or brand UIs imitated in a screenshot, copyrighted meme or stock imagery, a line that mocks rather than mirrors.

## 5. Fixes

Make every fix concrete:

- **Three rewritten lines** using the punchline templates ("Not [thing]. [Truth]." / "You're not [X]. You're just [truth]." / "Still [problem]? Try [new mindset].") — each grounded in the Spike Core found or proposed in step 2.
- **A format swap** if the visual fights the emotion (shame → Mirror Split, overwhelm → Receipt Stack, identity shift → Bold Poster, sarcasm → Screenshot or Meme Flip).
- **The single highest-leverage change**, stated first.

When the verdict is Rebuild and the `ad-blueprint` skill is available, offer to run it from Step 1.

## Output

```markdown
## First glance
Says: … · Feels: … · Eye lands on: …

## Verdict: [Publish | Tweak | Rebuild] — xx/25
Clarity x · Surprise x · Emotion x · Recognition x · Visual x
Spike Meter (line): x.x · Scroll/Glance Test: x/4 · Recognition: xx/20 (if scored)

## What's working
- …

## What's killing it
- … (most damaging first)

## Fix this first
…

## Rewrites
1. "…"
2. "…"
3. "…"
Format swap: … (if needed)

## Test it cold
Peer questions: "Would you share this or scroll past it?" · "What's the first emotion this gave you?" · "If this was made for you, would it feel like it gets you?"
```

The peer questions come from the Reality Loop: the user should still put the ad in front of real people from the tribe and track saves, DMs, replies, and shares — not likes.
