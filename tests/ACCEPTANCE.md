# Acceptance cases — OpenAI v0.3.2

Run these prompts in clean OpenAI ChatGPT/Codex sessions with the plugin enabled. **Static inspection is not an installed skill execution test**. Record artifacts and actual behavior for a release decision.

| # | Prompt | Pass criteria |
|---|---|---|
| 1 | Make a 48-sheet billboard for a bookkeeping service aimed at anxious freelancers. | Run all seven named stages. State service assumptions instead of inventing features or metrics. Include product-truth ledger, ownable symbol, <=7-word headline, appropriate 2:1 canvas, real verified image/SVG when available, audience-test (not publish) score and full build sheet. |
| 2 | Create a café poster for night-shift nurses. Show a person. | Human Moment with real person-shaped image/vector (not a typography-only shortcut), telling pose and prop; verified artwork at poster aspect ratio if tools available. Do not invent café name or opening hours as factual. |
| 3 | Critique this existing ad without knowing why it was designed. | Ask for actual ad if none attached. With provided example, separate *what is observed* from subjective interpretation and campaign evidence; label same-context review honestly, flag unsupported claims and give clear rewrites. |
| 4 | Give me four Instagram A/B concepts based on the same emotional truth. | Two fixed punchlines × two truly different visual executions => AA/AB/BA/BB; same brand, audience, promise, CTA, format 1080×1350; four specs and verified art if tools exist, honest scores. |
| 5 | Adapt an Instagram ad into a motorway billboard. | Ask for source if missing. With supplied fixture, reduce >20-word copy to <=7-word headline, one focal point, eliminate QR, use actual billboard ratio, distinct billboard composition — not a rescale. |

## Controlled test inputs

**1:** Fictional bookkeeping brand "Ledgerlight"; audience freelancers nervous despite busy calendars. No forecasting, savings or results claims have been proven; creative should avoid claiming those features.

**2:** Generic café targeting night-shift nurses. A genuine Human Moment should show e.g. a tired nurse at shift end; one cup as the accent prop. Venue operating hours are unknown.

**3:** Give the reviewer a supplied fictitious ad: "Never worry about money again. Guaranteed! 97% of customers agree." Layout has five fonts, a loud gradient, three CTAs and a minuscule brand. Ask for a cold critique. Both the "guarantee" and "97%" are unverified.

**4:** Fixed spike: freelancer is fully booked outwardly, worries about the next invoice inwardly. Fictional brand Ledgerlight. Headline A "Fully booked. Still worried." Headline B "Busy today. Unsure about tomorrow." Visual A = large contrasting SAY/FEEL split; visual B = a calendar silhouette with one empty next-month page. Change only copy and visual factor.

**5:** Supply an Instagram 4:5 ad with 25-word headline, explanatory paragraph, QR code, three competing focal points and tiny signoff; theme from case 1. Adapt to a 48-sheet 2:1 roadside panel.

## Reporting template

| Case | Static workflow reviewed | Deterministic artifact checks | Real installed OpenAI run |
|---|---|---|---|
| 1 | reviewed | pass — scripted artifact assertions | not run |
| 2 | reviewed | pass — scripted silhouette/format checks | not run |
| 3 | reviewed | pass — evidence-label fixture checks | not run |
| 4 | reviewed | pass — controlled 2×2 assertions | not run |
| 5 | reviewed | pass — copy/dimension/QR checks | not run |

These deterministic assertions are run via GitHub Actions using `python3 tests/check_fixtures.py` (8 unit tests). They check the provided *sample artifacts* and package structure, not full visual quality or real model skill execution.\n\nDo not mark any real installed-run test "passed" unless the OpenAI plugin actually activated and executed on the supplied prompt. An explicit "not rendered" fallback is **honest** but does not pass a test asking for a visual when rendering tools should be available.
