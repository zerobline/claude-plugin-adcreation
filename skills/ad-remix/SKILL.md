---
name: ad-remix
description: Turns one ad into test-ready variants, runs the pre-launch checklist, rescues ads that flopped, and scales a winning idea into 5–20 ads, using the Mastermind A/B War Room (2×2 punchline × visual grid), Launch Checklist, and Remix Recipes. Use when someone asks for "variations", "A/B versions", "more options of this ad", "is this ready to post/print", "launch checklist", "this ad got no engagement — fix it", or wants a batch of ads from one idea.
---

# Ad Remix — the A/B War Room, Launch Checklist, and Remix Recipes

Don't pick a favourite. Build the collision, test it in the wild, and remix what doesn't land. One real ad beats ten clever drafts.

Work out which mode the user needs from the request; if it's unclear, assume **Variants**.

## Mode 1 — Variants (the 2×2 Remix Grid)

Start from the current ad. If there's no Spike Core on record, state the emotional truth the ad is built on in one sentence first. If the user supplies neither the emotional truth nor an ad, choose one *explicitly labelled creative assumption* rather than passing imagined market research off as fact. Never invent a current ad image.

0. **Freeze the test:** use the same brand, audience, product truth, offer, CTA, platform, aspect ratio and placement for all four variants. Only two factors can change: copy (A/B) and visual execution (A/B). Never invent proof or objective claims.
1. **Punchline A** = the current emotional spike winner. **Punchline B** = a sharper *or* softer remix of the same truth (switch the weapon: Shame Mirror ↔ Contradiction Cut ↔ Identity Unlock).
2. **Visual A** = the best layout for the chosen placement. **Visual B** = a meaningfully different composition or ownable object/gesture, still for the *same placement*. Visual A should remain visually consistent in AA and BA; Visual B must remain consistent in AB and BB.
3. Build the grid:

| | Visual A | Visual B |
|---|---|---|
| **Copy A** | Punchline A + Format A | Punchline A + Format B |
| **Copy B** | Punchline B + Format A | Punchline B + Format B |

4. When OpenAI artifact tools exist, render and inspect all four mockups with identical aspect ratios (see `ad-blueprint/references/render-mockup.md`). Name verified files `ad-<slug>-AA.svg`, `-AB`, `-BA`, `-BB`. Otherwise provide four detailed production-ready layouts and state **not rendered**, never invent file paths.
5. Score each on the 5D grid as a **subjective creative comparison**. An actual independent-context reviewer may be used only if supported and actually launched; otherwise label the ranking internal. Test creative preference and objective-relevant results with real viewers before choosing a winning campaign.

## Mode 2 — Launch Checklist (the Screenshot Protocol)

"If it hits in silence, it's ready." Confirm the ad has: a truth that stings, a punchline that snaps, a visual that stops the scroll, a format that fits the platform, and a tribe that flinches when they see it.

**5-Point Gut Check** (1–5 each):

| Filter | Ask |
|---|---|
| Clarity | Is the core message instantly obvious in 1.5 seconds? |
| Surprise | Does it flip a cliché or say what others won't? |
| Emotion | Does it sting, soothe, or hit like truth? |
| Recognition | Would the tribe whisper "that's me"? |
| Visual Power | Would someone screenshot or save it without context? |

**20–25** ready for an audience test · **16–19** revise · **below 16** rebuild. Model scores never establish campaign success.

**Platform fit:**

| Platform | Native format | Caption style |
|---|---|---|
| Instagram | Bold Poster / carousel | "Save this for when it hits again." |
| TikTok | Skit / screenshot | "Stitch if your life's like this." |
| LinkedIn | Pain post / story | "What's your version of this truth?" |
| Email | Confession / shift | "I almost didn't send this…" |
| Billboard / poster / print | Bold Poster or Mirror Split | No caption — the line is the ad, plus a small brand sign-off |

Ask: "Does this feel like it belongs here — or like a slide deck in disguise?"

**Pre-flight for paid and printed placements:** spelling and legal lines checked; claims can be backed up; no invented testimonials or stats; imagery is original or licensed; roadside line ≤7 words and no QR code; final artwork produced to the media owner's spec (size, bleed, colour profile, resolution).

**Launch dare:**

1. Post the ad (Instagram, TikTok, LinkedIn, or email).
2. Caption prompt: "Which part of this hit you hardest?" or "Tag someone who needs to see this."
3. Track **saves, DMs, replies, and shares** — proof of emotional velocity. Ignore likes.

Out-of-home has no saves or DMs: pair it with a unique short URL, an offer code, or a branded search term, and pretest the same creative as a social static.

## Mode 3 — Flop Remix (Remix Recipes)

Still no traction? Don't panic. Diagnose which signal is missing, then remix:

| If it didn't… | Try this… |
|---|---|
| Get saved | Flip to a screenshot or meme style |
| Get shared | Make the punchline shorter and simpler |
| Trigger emotion | Add a confession-style caption |
| Feel scroll-worthy | Boost contrast. Strip the clutter. |

If nobody sends it to a friend, the problem is upstream: return to the Spike Core and find a truth that stings more. One honest remix can revive a "dead" ad. Keep every version — they become the user's own swipe file.

Ask for the numbers if the user has them (reach, saves, shares, DMs, clicks). Low reach is a distribution problem, not a creative one; say so rather than remixing the creative.

## Mode 4 — Scale (5–20 ads from one engine)

1. Lock **one to three Spike Cores** that scored 4+ on the Spike Meter.
2. For each core, write one punchline per weapon (Shame Mirror, Contradiction Cut, Identity Unlock).
3. Pair each punchline with the two formats the Style Mapper suggests for its emotion.
4. Adapt to each placement with the platform grids — never just resize.
5. Score every ad on the 5D grid and prioritize **20+** for real audience testing; refine 16–19s and rebuild weak concepts. Do not declare launch confidence from model self-scoring.

Present the batch as a matrix (core × weapon × format × placement × score) and render mockups for the launch set only.

## Output

Lead with the recommendation (which variant to run, whether it's ready, or the one remix to try), then the supporting grid or checklist, then the mockup paths.
