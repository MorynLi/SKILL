# Show HN

Post at **news.ycombinator.com/submit**. Weekday, 09:00–11:00 ET, is when Show HN
gets read. Submit the repo URL, then immediately post the comment below as the first
reply — that is the convention, and the comment is what people actually read.

**This is the one shot that does not reload.** A Show HN that lands flat cannot be
resubmitted. Fire the others first.

---

## Title

```
Show HN: An Agent Skill derived from 88k words of Feynman's own writing
```

76 characters. Alternatives if that reads wrong to you:

```
Show HN: Feynman Technique – a skill that makes AI explain mechanisms, not names
Show HN: I analysed 88k words of Feynman to build an explanation skill
```

## URL

```
https://github.com/guicortei/feynman-technique
```

---

## First comment

The itch was answers that are correct and useless. Ask why a fetch is failing and you get "the response lacks an Access-Control-Allow-Origin header, so the preflight fails" — true, and you still cannot picture what happened.

Feynman had a name for this. His father showed him a bird and told him you can learn its name in every language on earth and still know nothing about the bird. So I tried to build the correction as an Agent Skill, and I wanted it grounded in what he actually did rather than in the four-step listicle that circulates under his name.

I pulled together about 88,000 words of his own writing — Six Easy Pieces, the 1965 Nobel lecture, Cargo Cult Science, the 1966 NSTA address, There's Plenty of Room at the Bottom, and the Brazil chapter of Surely You're Joking — and went through it two ways: for the method, and for the prose.

Some of what came out was measurable. His sentence lengths are bursty in a specific way: median around 20 words, but roughly one sentence in eight runs under eight words and one in six past thirty-five. He builds long and lands short. His pronouns switch by function — "we" while teaching (19.95 per thousand words in Six Easy Pieces, ten times his "I"), "I" when admitting confusion, "you" when instructing. And the word "basically" appears zero times in the entire corpus. "Trivial" appears once. That is why the skill bans those words: measurement, not taste.

Some of it was better than the folk version. The popular test is "explain it to a 12-year-old", which he never said. What he did say, in 1966, is sharper and checkable: "Without using the new word which you have just learned, try to rephrase what you have just learned in your own language." Cover the term; if the sentence dies without it, you wrote a definition.

A few things I'd flag rather than have you discover them:

- He did not invent "the Feynman Technique". The four steps were assembled by later popularizers, chiefly Scott H. Young around 2011. references/sources.md separates the quotations that are verifiable from the ones commonly misattributed — "if you can't explain it simply you don't understand it" has no primary source for him or Einstein.
- Some things genuinely do not simplify, and the skill is built to say so. Feynman hit that wall himself: asked by his own father how a photon leaves an atom without having been inside it, he answered "I'm sorry; I don't know. I can't explain it to you."
- Forcing an expert through beginner scaffolding measurably degrades their comprehension — the expertise reversal effect — so the ladder has a compact form and puts the thesis in line one, which is an expert's exit.

The unexpectedly hard part was the ten languages. I wrote the README in English and translated it nine ways, and a native speaker rejected the Portuguese on sight: I had rendered "yesterday's page" and "a sentence you nodded at" literally, which are correct words and no meaning at all. What fixed it was not more rules — I had already written the rule — but changing the process: hand each language the specification and let someone compose in it. Asked for a label meaning "agreed to without reading", Portuguese quoted the checkbox itself ("LI E CONCORDO"), Russian named the button, Chinese described the gesture. None is a translation of the others. That whole failure is documented in references/voice.md, since it is the exact mistake the skill exists to prevent.

MIT. It follows the Agent Skills open standard, so it works in Claude Code, ChatGPT, Codex, Cursor, Copilot and Gemini CLI. Feynman's texts are quoted briefly and attributed; the Lectures are free to read but remain Caltech copyright, so nothing is redistributed.

---

## If it takes off, expect these

**"This is just a prompt."** It is. That's what an Agent Skill is — a Markdown file the agent loads on demand. What's in the file is the work: the corpus analysis, the four documented tests, the failure catalogue. Say that plainly; don't get defensive.

**"Feynman didn't invent this."** Correct, and the README says so before they do. Point at references/sources.md.

**"Show me output."** Have a real answer ready to paste — not the README's example, a fresh one from a question they asked. That converts better than anything else.

**"Does it actually change anything?"** Honest answer: it changes the shape of the answer reliably, and whether that helps you is a judgement you should make from the sample above, not from my claim.
