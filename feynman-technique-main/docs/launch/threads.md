# Threads

Where the conversation this project belongs to is actually happening, and what to say
when it is.

## What I can and cannot see

| | |
|---|---|
| Hacker News | readable and searchable (Algolia API) |
| dev.to, lobste.rs | readable |
| **Reddit** | **blocked** — cannot search or read it at all |
| **Stack Overflow** | **blocked** (the API works; the site does not) |

Reddit is where most of this audience is, and it is the one place I am blind. Those
threads are yours to find. `find-threads.py` covers Hacker News.

## The rule, restated because it is the only one that matters

Before posting anywhere: **delete the link. Does the comment still help the person?**

If yes, post it. If no, it was an advertisement and it will be read as one.

Corollary that is easy to miss: when a comment passes that test *comfortably*, the link
usually makes it worse. A genuinely useful comment earns a profile click on its own. A
useful comment with a link stapled to it reads as bait, and on Hacker News it gets
called out in the first reply.

## Wrong target: Stack Overflow CORS questions

I went looking there first and it was the wrong instinct. Someone asking why
`scala-http4s` is not emitting an `Access-Control-Allow-Origin` header wants their bug
fixed. A skill about explanation quality is off-topic by the site's own rules, and
rightly so. Answer their question if you can actually answer it; otherwise leave it.

The audience is not people with a CORS bug. It is people arguing about whether working
with an AI leaves you understanding anything.

---

## Live now — post this one first

**"Agent Skill to Force Docs in ASD-STE100 Simplified Technical English"**
https://news.ycombinator.com/item?id=49114639 — 310 points, 113 comments, ~18h old

Someone built an Agent Skill that constrains documentation to Simplified Technical
English. It is the adjacent problem to ours, it is on the front page right now, and a
commenter (`tajd`) has already shared their own related skill — an Economist style-guide
plugin — without anyone objecting. Sharing a related skill is welcome in this thread.

But do not lead with the skill. Lead with the thing nobody in the thread has said:

**STE fixes the sentence. It cannot reach whether the sentence explains anything.**

ASD-STE100 fixes the sentence. What it can't reach is that a perfectly clear sentence can still be a definition rather than an explanation.

Feynman caught a textbook doing exactly this in Brazil: "Triboluminescence is the light emitted when crystals are crushed." Run that through STE and you get something like "Crystals emit light when you crush them" — short words, active voice, one idea per sentence, no ambiguity. It passes. And it still says nothing about nature; it says what a word means in terms of other words.

His replacement: "When you take a lump of sugar and crush it with a pair of pliers in the dark, you can see a bluish flash. Some other crystals do that too. Nobody knows why. The phenomenon is called 'triboluminescence.'"

Same fact, and notice it isn't shorter. What changed is the order — something you can do, then what you'd see, then how far it generalises, then an honest admission that nobody knows the mechanism, and only then the name. You can go test that one tonight with a sugar cube and a dark room.

The test he gave for telling the two apart, from a 1966 talk to science teachers: "Without using the new word which you have just learned, try to rephrase what you have just learned in your own language." Cover the term. If the sentence dies without it, it was a definition.

I ended up building the same shape of thing as OP but aimed at that layer instead of the vocabulary one: github.com/guicortei/feynman-technique. Genuinely different constraint, and I think the two would compose — STE for the sentence, ordering for the paragraph.

Why this one works: the insight is real and specific, it takes OP's work seriously rather than competing with it, and the closing line offers composition instead of replacement. Delete the link and the comment still earns its place — which is the test.

**One warning from that same thread.** A commenter (`bayesnet`) called out OP's README for "all the tells of being LLM-written", quoting its punchy triple constructions. Our README has some of the same rhythm. If that lands on us, the honest answer is yes, an assistant helped write it, here is the corpus and the validator, judge the work. Do not deny it.

---

## Also live

**"Why do we think we understand the world more than we actually do?"**
https://news.ycombinator.com/item?id=49079175 — 28 Jul 2026, 93 points, 71 comments

This is the illusion of explanatory depth — Rozenblit & Keil 2002 — which is the exact
mechanism `references/evidence.md` is built on. The thread has drifted into
Dunning-Kruger and jokes about badly designed doors. Nobody has brought the finding that
makes the paper interesting, or the one operational test that comes out of it.

**Post this with no link.** It stands entirely on its own, and that is the point.

The finding that makes this more than "people overrate themselves" is how narrow it is. Rozenblit and Keil tested several kinds of knowledge and the collapse only appeared for *explanatory* knowledge — causal, mechanistic understanding. Self-ratings for facts, procedures and narratives held up fine. Ask someone how a zipper works and it falls apart the moment they have to produce the steps.

So it isn't really a story about confidence. It is about one specific kind of knowledge that feels retrievable because you can picture the object, and isn't, because you have only ever seen it from the outside.

The most useful practical version I know is Feynman's, from a 1966 talk to science teachers, and it is sharper than "explain it to a twelve-year-old" — which he never said:

"Without using the new word which you have just learned, try to rephrase what you have just learned in your own language."

Cover the term and restate the claim. If the sentence dies without it, you had a definition rather than an explanation. He had caught a first-grade textbook answering "what makes it move?" with "energy makes it move", and pointed out you could equally say "God makes it move" or "movability makes it move" — the child cannot tell those apart, and cannot argue with any of them.

The example I keep returning to is a rewrite he did in Brazil. The textbook said: "Triboluminescence is the light emitted when crystals are crushed." His replacement: "When you take a lump of sugar and crush it with a pair of pliers in the dark, you can see a bluish flash. Some other crystals do that too. Nobody knows why. The phenomenon is called 'triboluminescence.'"

Same fact. But the second one you can go and test tonight, and it tells you where the knowledge stops.

If someone replies asking where you got the corpus figures, *then* the link is on-topic
and welcome. Not before.

---

## Also live, lower fit

**"2x, not 10x: coding with LLMs in 2026"** https://news.ycombinator.com/item?id=49048000-ish — 25 Jul, 270 points, 218 comments

Six days old, so cooling. Only worth a comment if you have something specific about *understanding* the code an assistant produced, from your own experience. Do not retrofit the project into it.

---

## Dead — do not bother

These matched on topic but are months old. HN comments after about 72 hours are read by almost nobody.

- "Vibe coding and agentic engineering are getting closer than I'd like" — 6 May, 885c
- "The cult of vibe coding is dogfooding run amok" — 6 Apr, 512c
- "An AI Vibe Coding Horror Story" — 14 Apr, 211c

They are useful as evidence that the conversation recurs. Run `find-threads.py` weekly and one of these will come around again.
