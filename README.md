# Mastermind Ad Engine — OpenAI

**Static advertising built around a recognisable emotional truth, a defensible product promise, and a visual that works in the actual placement.**

Version **0.3.2** is an **OpenAI-only skills plugin** for ChatGPT and Codex. No Claude-specific manifest, MCP server, authentication, external account or background service is needed.

## Workflow

**Clarify → Flip → Write → Design → Tribe → Platform → Taste Test**

In addition to the original framework, the OpenAI edition includes a product-truth and claim ledger, Symbol Lock, placement-first final rendering, capability-aware SVG/image output, and an evidence-honest creative assessment. A 20+/25 creative score means *test this concept with actual viewers* — not "guaranteed to work".

| Skill | Purpose |
| --- | --- |
| `skills/ad-blueprint/SKILL.md` | Build a complete billboard, poster or social ad and deliver its build sheet and visual when possible |
| `skills/quick-ad/SKILL.md` | Develop a lean ad concept quickly |
| `skills/ad-critique/SKILL.md` | Critique an actual supplied ad, separating observations from assumptions |
| `skills/ad-remix/SKILL.md` | Make a controlled 2×2 copy × visual grid, diagnose failures and scale concepts |

These are instruction-based skills. They do **not** give independent access to image editing, advertising accounts, audience analytics or unrelated files. The current OpenAI surface determines which artifact tools exist. Skills must not claim a file was produced without actually verifying it.

## Install and submit

A portable root `plugin.json` contains `extensions.com.openai`; `.agents/plugins/marketplace.json` provides Codex marketplace metadata. On supported Codex installations:

```text
codex plugin marketplace add zerobline/claude-plugin-adcreation
codex plugin add mastermind-ad-engine@zerobline-adcreation
```

**Public listing status (24 October 2026):** The OpenAI submission portal currently reports **"We are not accepting more skills-only submissions at this time."** Therefore the existing skills-only plugin cannot currently be submitted for public listing through that route. This restriction is separate from packaging or metadata and is not bypassed by declaring a fictional MCP server. See [Publishing status](docs/PUBLISHING.md) for details and a legitimate MCP-based alternative.

Current package format documentation: https://developers.openai.com/plugins/build/plugins .

## Five acceptance cases

See [tests/ACCEPTANCE.md](tests/ACCEPTANCE.md) for full input fixtures, pass/fail checks and live-test limitations.

1. Make a 48-sheet billboard for a bookkeeping service aimed at anxious freelancers.
2. Create a café poster for night-shift nurses. Show a person.
3. Critique this existing ad without knowing why it was designed. (Attach the actual ad.)
4. Give me four Instagram A/B concepts based on the same emotional truth.
5. Adapt an Instagram ad into a motorway billboard. (Provide the source ad.)

## Publisher and policy information

The manifest uses the supported OpenAI category **Creativity**. The public support, privacy and terms documents are published on GitHub. Please review these publisher-specific legal/privacy drafts for accuracy before submitting any future listing:

- [Support](SUPPORT.md)
- [Privacy Policy](PRIVACY.md)
- [Terms of Service](TERMS.md)
- [Submission eligibility and MCP alternative](docs/PUBLISHING.md)

## Limits and safety

- No fabricated statistics, comparisons, testimonials, efficacy claims, availability hours or product features.
- Do not imply real customer testing or independence if the model is critiquing its own work.
- Hard brand/legal constraints override black-white-accent design defaults.
- SVG or generated mockups are concepts, **not** printer-ready art. Check media owner specs, safe areas, bleed, color and approval rules.
- No external service is connected **by this plugin**. Other OpenAI tools follow their own permissions and data policies.

MIT © zerobline.
