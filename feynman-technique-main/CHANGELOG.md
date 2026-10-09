# Changelog

All notable changes to this skill are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.0.0] — 2026-07-28

First public release. Rebuilt from primary sources rather than from secondary writing
about Feynman.

### Added

- **`feynman-technique` skill**, conforming to the
  [Agent Skills open standard](https://agentskills.io/specification).
- **Primary-source grounding.** Four documented Feynman tests replace the popular
  "explain it to a 12-year-old" heuristic:
  - the rephrase test (*What Is Science?*, 1966, verbatim);
  - the triboluminescence order — mechanism → observation → honest ignorance → name
    (*Surely You're Joking*, Brazil chapter);
  - the "look at the water" test for keyword-only knowledge (same chapter);
  - the cargo cult test (*Cargo Cult Science*, 1974).
- **[references/voice.md](skills/feynman-technique/references/voice.md)** — forensic style
  analysis over an ≈88,000-word corpus spanning six sources and three decades, with
  measured statistics for sentence-length burstiness, pronoun use by rhetorical function,
  question rate, kinesthetic verb frequency and discourse markers. Includes the finding
  that "basically" appears **zero** times in the corpus, which is the empirical basis for
  the banned-words rule.
- **Adaptive ladder.** Five named levels (Kitchen table → Newcomer → Practitioner →
  Maintainer → Specialist), domain-general rather than software-specific, plus a
  **compact form** for narrow questions and expert readers — addressing the expertise
  reversal effect, which the fixed five-level format ignored.
- **Thesis-first output**, so an expert can stop reading after one sentence.
- **Analogy engineering** ([references/analogies.md](skills/feynman-technique/references/analogies.md)):
  the escalating-complication pattern, the zoom ladder, the parallel experiment,
  arithmetic in the open, negative definition when no honest analogy exists, and a
  five-point stress test.
- **Coach mode** — inverts the skill so the user does the explaining, backed by the
  self-explanation effect and the protégé effect.
- **Self-audit pass** before sending, grounded in the illusion of explanatory depth.
- **[references/evidence.md](skills/feynman-technique/references/evidence.md)** — the
  supporting research, the folklore it separates out, and an honest account of where the
  method fails.
- **[references/sources.md](skills/feynman-technique/references/sources.md)** — verified
  quotations with provenance, plus quotations commonly *mis*attributed to Feynman.
- **[references/failure-modes.md](skills/feynman-technique/references/failure-modes.md)** —
  14 failure modes, each with a rewrite.
- **[assets/worked-example.md](skills/feynman-technique/assets/worked-example.md)** — a
  complete answer, then annotated to show what every part is doing.
- **[assets/checklist.md](skills/feynman-technique/assets/checklist.md)** — the pre-send audit.
- **Spec validator** (`.github/validate.py`) and CI: checks frontmatter constraints, the
  500-line / 5,000-token budget, relative link resolution, and the skill's own
  banned-word rule against itself.
- Install instructions for Claude Code, claude.ai, ChatGPT, Codex CLI, Cursor,
  VS Code / Copilot, Gemini CLI, and a fallback for tools without skills support.

### Changed from `feynman-reply` (the predecessor)

- Skill and repository both renamed `feynman-reply` → `feynman-technique`. GitHub keeps a
  permanent redirect, so old clone URLs and links continue to work.
- Repository and documentation moved to English; **answers still come back in the user's
  own language**.
- Levels generalised from software roles (junior/mid/senior/staff) to domain-neutral ones,
  so the skill works for medicine, law, finance and science as well as engineering.
- The obligation to always emit five full levels became an adaptive shape. The old
  behaviour was actively harmful to expert readers.
- The four "steps" are now attributed accurately — to later popularizers, chiefly Scott H.
  Young, rather than to Feynman.
- The claim that "Feynman hated the word *obviously*" was replaced with corpus
  measurements, which turn out to make a stronger case.

---

## [1.1.0] — 2026-07-28

### Added

- **§8.1 "Writing in a language other than English"** in `SKILL.md`. The voice guidance
  was derived entirely from English prose — English sentence-length medians, English
  pronoun rates, English banned words — with nothing telling the model to *compose* in
  the reader's language. It would therefore draft in English and translate, producing
  the exact calque prose this project rejects. The new section requires composing
  natively, bans the local equivalents of *basically / obviously / simply*, and ends with
  the test: if it reads like a good translation, it has already failed.
- **[references/voice.md §14](skills/feynman-technique/references/voice.md)** — how the
  voice crosses languages: what transfers (shape, physical verbs, concrete quantities)
  versus what does not (the measurements themselves), per-language notes, and a table of
  real calques caught in this repository's own Portuguese README.
- **`.github/validate_i18n.py`** and a CI step. Checks every translation against the
  English source: link and anchor resolution, language-switcher symmetry, install
  commands unaltered, table shapes, Feynman quotes still verbatim in English, and — for
  Arabic and Urdu — balanced `dir="rtl"` blocks with no code fence trapped inside one.

### Fixed

- **All nine translations rewritten by native-speaker review.** The first pass was
  calque: correct words in English syntax. A native reader rejected the Portuguese, and
  the same disease was present throughout. Representative fixes in Portuguese —
  "Você concorda com a cabeça" → "Você faz que sim com a cabeça"; "uma subida graduada" →
  "uma subida em degraus"; "acha os seus buracos" → "encontra as suas lacunas".
- Broken in-page anchor `#any-other-ai-no-skills-support` in the English README, found by
  the new validator.

[1.0.0]: https://github.com/guicortei/feynman-technique/releases/tag/v1.0.0
[1.1.0]: https://github.com/guicortei/feynman-technique/releases/tag/v1.1.0
