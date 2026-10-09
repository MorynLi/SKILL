# Contributing

Thanks for wanting to improve this. A few things make a contribution easy to accept.

## The one hard rule

**Any claim about what Feynman said, wrote, or did must cite a primary source** — the
work, the year, and ideally the chapter or talk.

This repository exists to argue that naming a thing is not explaining it, and that you
should lean over backwards to show where you might be wrong. Attributing a made-up quote
to Feynman while making that argument would be the one unforgivable bug here.

Before adding a quotation, check
[references/sources.md](skills/feynman-technique/references/sources.md). It already lists
several widely repeated quotes that he did **not** say. If you find another, a PR adding
it to the "do not attribute" section is genuinely valuable.

## Especially wanted

- **Worked examples from other fields.** The current one is a database index. Medicine,
  law, finance, biology, civil engineering, statistics — all would make the skill
  demonstrably domain-general. Follow the format in
  [assets/worked-example.md](skills/feynman-technique/assets/worked-example.md),
  including the annotated section explaining what each part is doing.
- **Failure modes observed in real use.** If the skill produced a bad answer, that is
  data. Open an issue with the prompt and the output.
- **Corpus analysis.** The style forensics in
  [references/voice.md](skills/feynman-technique/references/voice.md) covers six sources.
  More sources, or a correction to any measurement, is welcome — include the method so
  the number can be reproduced.
- **Translations of the README.** Ten languages live in [`docs/i18n/`](docs/i18n/) as
  `README.<code>.md`. To add one, copy the English README, translate the prose, leave
  every code block and install path byte-identical, and add your language to the switcher
  bar in **all** existing files — the bar must stay symmetric, with each file bolding its
  own language and linking to the other nine.
  Keep the skill files themselves in English so the frontmatter stays canonical.
  Feynman quotations keep their English original, with a translation on the line below.

## Not wanted

- Emoji, exclamation marks, or cheerleading added to the skill's prose. Feynman's corpus
  runs about one exclamation mark per thirty-six sentences and no cheerleading at all.
- Extra levels in the ladder. Five is already a lot; the failure mode is bloat.
- New analogies inside `SKILL.md`. The skill teaches how to *build* analogies; baking in
  a fixed set makes answers repetitive.
- Anything that would bulk `SKILL.md` past 500 lines or ~5,000 tokens. That is a hard
  budget from the Agent Skills specification. Deeper material belongs in `references/`,
  which loads on demand.

## Style for the skill files

Match the voice they describe, since the file is its own worst critic if it doesn't:

- Vary sentence length hard. Land a short sentence after a run of long ones.
- Physical verbs over Latinate abstractions.
- Concrete nouns with real quantities.
- No *basically*, *simply*, *obviously*, *trivially*, *just*.
- Mark every approximation with its limits.

## Practical steps

1. Fork and branch.
2. Make the change.
3. Run the validator — CI runs the same check:
   ```bash
   python3 .github/validate.py
   ```
4. If you touched `SKILL.md`, test it in at least one real client and paste a sample
   answer in the PR. Claims about behaviour need evidence, same as everything else here.
5. Open a PR describing what changed and why.

## Reporting a problem

Open an issue with the prompt you used, the tool and model, the output you got, and the
output you expected. A concrete reproduction beats a description every time.
