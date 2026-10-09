# Reddit

Post to **r/ClaudeAI** first. If it goes well, r/ChatGPTCoding and r/LocalLLaMA follow —
rewritten, not copy-pasted; crossposting the same text reads as spam.

Read each subreddit's self-promotion rule before posting. Most allow "I built this" from a
participating account and remove it from a fresh one. If your account has no history there,
comment on other people's posts for a few days first. This is not a formality — it is the
difference between the post staying up and being removed in twenty minutes.

Lead with the image. `assets/hero.svg` rendered to PNG, or a real screenshot of your own
terminal, which does better.

---

## r/ClaudeAI

**Title**

```
I analysed 88,000 words of Feynman's writing and turned it into a skill
```

**Body**

I kept getting answers that were right and useless. Ask why a request is failing and you get "the response lacks an Access-Control-Allow-Origin header, so the preflight fails" — correct, and you still can't picture what happened, so you paste the fix and move on knowing nothing.

So I built a skill for it, and I wanted it based on what Feynman actually did rather than the four-step version that gets passed around under his name. I went through about 88,000 words of his own writing — Six Easy Pieces, the Nobel lecture, Cargo Cult Science, the 1966 talk to science teachers, the Brazil chapter of Surely You're Joking.

**What the skill does to an answer**

- Mechanism first, name last. "It's a race condition" explains nothing; describing two people writing in the same notebook and one erasing the other does, and *then* the name means something.
- One analogy for the whole answer, extended rather than replaced — and it tells you where the analogy stops being true, so you don't reason past it.
- A ladder: level 0 for someone with no background at all, up to level 4 for whoever maintains the thing. Thesis in line one so you can bail immediately if you already know.
- Every new term explained at first use, or it doesn't appear.
- It answers in whatever language you write in.

**A couple of findings from the corpus that surprised me**

The word "basically" appears **zero** times in 88,000 words. "Trivial" appears once. That's why the skill bans them — it's a measurement, not a style preference.

And the famous test isn't his. "Explain it to a 12-year-old" was never something he said. What he did say, in 1966: *"Without using the new word which you have just learned, try to rephrase what you have just learned in your own language."* Cover the term. If the sentence collapses without it, you wrote a definition, not an explanation.

**Install**

```
git clone https://github.com/guicortei/feynman-technique.git /tmp/ft
mkdir -p ~/.claude/skills
cp -r /tmp/ft/skills/feynman-technique ~/.claude/skills/
```

Then `/feynman-technique <anything>`. It follows the Agent Skills standard, so it also works in ChatGPT, Codex, Cursor, Copilot and Gemini CLI.

**What it doesn't do**

Some things don't simplify, and it's built to say so instead of faking a picture. Feynman hit that wall himself — asked by his own father how a photon leaves an atom without having been inside it, he said "I'm sorry; I don't know. I can't explain it to you."

It also costs tokens, and it's useless for memorisation. And he didn't invent "the Feynman Technique" — that framing came from later popularizers; the repo documents which quotes are verifiable and which get misattributed to him.

It's MIT. Repo and the full corpus breakdown are in the comments.

<!-- ─────────────── paste to here ─────────────── -->

**First comment**, posted by you immediately after the post goes up. Keep the link out of the body: most subs rank a self-post with a link lower, and a link in your own comment reads as courtesy rather than as the point of the post.

<!-- ─────────────── paste from here ─────────────── -->

Repo: https://github.com/guicortei/feynman-technique

Longer write-up with the numbers, if anyone wants the corpus detail: https://dev.to/guicortei/feynman-never-wrote-basically-i-checked-all-88000-words-58bd

Happy to run it on a question from this thread if someone wants to see real output rather than my description of it.

<!-- ─────────────── paste to here ─────────────── -->

---

## r/ChatGPTCoding — rewrite, don't repost

Same skill, different framing: this crowd cares that it is not Claude-specific. Lead with
the standard, mention that the same folder works in Codex and Cursor, and use the
`Cannot read properties of undefined (reading 'map')` example rather than CORS — it is the
error that audience meets most.

## r/LocalLLaMA — only if you can speak to it honestly

They will ask how it behaves on smaller local models. If you have not tested that, say so
outright, or skip the sub. Guessing there gets found out fast.
