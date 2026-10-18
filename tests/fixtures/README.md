# Illustrative fixture artifacts — not OpenAI runtime tests

The SVG files are *deterministic hand-authored examples* showing expected visual requirements, not autonomous executions of the installed skill.

- Case 1: `case1-billboard.svg` (2400×1200) and `case1-build-sheet.md`.
- Case 2: `case2-human-poster.svg` (1200×1800) includes an actual person silhouette and cup; café name remains a placeholder.
- Case 3: `case3-critique.md` separates facts in the supplied text/description, subjective opinions, and nonexistent measured evidence.
- Case 4: AA, AB, BA, BB SVGs (1080×1350). Identical copy in AA/AB and in BA/BB; same visual family in AA/BA and AB/BB. Same product and brand.
- Case 5: `case5-motorway.svg` (2400×1200) is a redesigned composition with five-word main claim, no QR.
- None are real audience-tested outcomes, nor final print production files.

Use `tests/ACCEPTANCE.md` for true clean-session ChatGPT/Codex evaluation after installation.
