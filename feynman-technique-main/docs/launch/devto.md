# dev.to / Hashnode — long form

The article has to stand on its own. If someone reads it and installs nothing, it should
still have been worth their time — that is what makes it circulate, and it is also the only
version that isn't an advertisement wearing an article's clothes.

The hook is not "I made a skill". It is **the measurement**.

Tags: `ai`, `writing`, `claude`, `productivity`.
Cover image: `assets/hero.svg` exported to PNG.

---

## Title

```
Feynman never wrote "basically" — I checked all 88,000 words
```

Alternatives:

```
What 88,000 words of Feynman taught me about explaining things
The word Feynman never used
```

---

## Article

Everything from the next line to the end of the file is the post body. Select it all and
paste it into the dev.to editor as-is — it is already Markdown.

<!-- ─────────────── paste from here ─────────────── -->

## The sentence that started it

A first-grade science textbook asks: *what makes it move?* The teacher's edition gives the answer: **energy makes it move.**

Feynman read that in 1966 and took it apart in front of a room of science teachers. You could equally well say "God makes it move", or "spirit makes it move", or "movability makes it move." The child has learned a word, not a fact. And here is his test for telling the difference, which I have not been able to improve on since:

> "Without using the new word which you have just learned, try to rephrase what you have just learned in your own language."

Cover the term. If the sentence dies without it, you wrote a definition.

I have been getting definitions from AI assistants for two years. Ask why a request is failing and you get *"the response lacks an Access-Control-Allow-Origin header, so the preflight check fails and the fetch is rejected."* Every word true. You still cannot see what happened, so you paste the fix and move on knowing nothing.

So I went looking for how he actually did it — not the four-step version that circulates under his name, which he never wrote.

## The corpus

About 88,000 words of his own writing, across six registers and three decades:

| | Year | Register |
|---|---|---|
| *Six Easy Pieces* | 1963 | teaching undergraduates |
| Nobel Lecture | 1965 | technical, autobiographical |
| *What Is Science?* | 1966 | a talk to schoolteachers |
| *Cargo Cult Science* | 1974 | a commencement address |
| *There's Plenty of Room at the Bottom* | 1959 | a talk to physicists |
| the Brazil chapter of *Surely You're Joking* | 1985 | memoir |

I read it for the method. Then I measured it.

## What the numbers say

**His rhythm is bursty, and that is the single most imitable thing about him.** Median sentence around 20 words — but roughly one in eight runs under eight words, and one in six past thirty-five. He accumulates a long chained sentence and then stops dead:

> "Shake this one, that one shakes later. The sun atom shakes; my eye electron shakes eight minutes later, because of a direct interaction across."

**His pronouns switch by function.** "We" while teaching — 19.95 per thousand words in *Six Easy Pieces*, ten times his "I". "I" when narrating his own confusion: 26.7 per thousand in the Nobel lecture. "You" when instructing: 20.6 per thousand in *Cargo Cult Science*.

**His verbs are ones a body can feel.** *jiggle* 27, *pull* 37, *push* 28, *shake* 20. Water molecules jiggle. They do not exhibit thermal agitation.

**And "basically" appears zero times.** Not rarely — zero, in 88,000 words. "Trivial" appears once. "Obviously", five times in the whole corpus.

That last one changed how I think about writing rules. "Don't say basically" is usually someone's taste. Here it is a measurement of what the most celebrated explainer in modern physics did across thirty years, and it turns out those words survive only in prose that has given up on explaining.

## The four tests, none of which is "explain it to a 12-year-old"

**The rephrase test** is above, and it is the only one he stated as a test.

**The triboluminescence test** is the best thing I found. In Brazil he opened a physics textbook at random and read: *"Triboluminescence is the light emitted when crystals are crushed."* His verdict — you have only said what a word means in terms of other words. You said nothing about nature. No student can go home and try that. Then he rewrote it:

> "When you take a lump of sugar and crush it with a pair of pliers in the dark, you can see a bluish flash. Some other crystals do that too. Nobody knows why. The phenomenon is called 'triboluminescence.'"

Look at the order. Something you can do → what you would see → how far it generalises → an honest admission of ignorance → **and only then, the name.** That is a template, and I have used it on everything since.

**The "look at the water" test** comes from the same trip. His students could recite Brewster's Angle perfectly. He asked them to point a polaroid at the bay outside the window and they froze.

> "If I asked, 'What is Brewster's Angle?' I'm going into the computer with the right keywords. But if I say, 'Look at the water,' nothing happens — they don't have anything under 'Look at the water'!"

Knowledge indexed only by its jargon is useless in the wild, because problems never introduce themselves by name.

**The cargo cult test** is his 1974 address. South Sea islanders built runways, lit fires along them, put a man in a wooden hut with bamboo antennas on his head. *"They're doing everything right. The form is perfect… But it doesn't work. No airplanes land."* After reading an explanation, what can you actually *do* that you couldn't before? If nothing, the runway is beautiful and the planes didn't land.

## The part where I made the exact mistake I was documenting

I turned all of this into an Agent Skill, and wrote into it a rule about answering in the reader's language: compose in it, never translate into it.

Then I wrote the README in English and translated it into nine languages.

A native Brazilian speaker looked at the Portuguese and rejected it on sight. I had rendered "yesterday's page" and "a sentence you nodded at" word for word — correct Portuguese words carrying no meaning whatsoever, because both are English idioms and neither exists there. I had written the rule and violated it in the next paragraph.

What fixed it was not a better rule. It was changing the process: hand each language the *specification* — what has to be conveyed, and to whom — and let someone compose from scratch. Asked for a label meaning "something you agreed to without reading":

- Portuguese quoted the checkbox itself: **LI E CONCORDO**
- Russian named the button: **ПРИНЯЛИ НЕ ЧИТАЯ**
- Chinese described the gesture: **你顺手点了同意** — *you clicked agree offhandedly*

None is a translation of the others, and no amount of care applied to my English sentence would have found any of them.

There is a deeper version of the same failure, which I only caught later. The skill's lowest rung was named "Kitchen table" — which in English is not furniture, it is the idiom for the homely place where ordinary people talk something over. All nine translations rendered it as a table. Correct every time, and dead every time. The scene that does that job in Brazil is the *churrasco*; in Bengal it is the **আড্ডা**, the unhurried gathering where someone will interrupt you with "just say it plainly" and jargon does not survive the room.

**An analogy has to come from the reader's world, not from the writer's.** Feynman's own are local to 1950s America — Dennis the Menace, the Encyclopaedia Britannica, bathroom tiles from Long Island City. Steal the structure; never the props.

## What it does not do

Some things do not simplify, and pretending otherwise is the failure mode this whole thing exists to prevent. Feynman hit that wall in his own kitchen. His father, after MIT and Princeton, asked him how a photon comes out of an atom without having been inside it:

> "I'm sorry; I don't know. I can't explain it to you."

Also: forcing an expert through beginner scaffolding measurably *degrades* their comprehension — the expertise reversal effect, Kalyuga and Sweller — so more explanation is not always better. And a good explanation *feels* like understanding, which is not the same as understanding; that feeling is the illusion of explanatory depth restored, and where it matters you should be the one doing the explaining.

## The skill

It is MIT, it follows the Agent Skills open standard, and it works in Claude Code, ChatGPT, Codex, Cursor, Copilot and Gemini CLI:

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/ft
mkdir -p ~/.claude/skills
cp -r /tmp/ft/skills/feynman-technique ~/.claude/skills/
```

But honestly, the four tests are the portable part. You can apply them to your own writing this afternoon without installing anything, and they will do more for you than the skill will.

One last thing, because the man deserves the accuracy he demanded. Feynman did not invent "the Feynman Technique" — the four-step version was assembled by later popularizers, chiefly Scott H. Young around 2011. "If you can't explain it simply, you don't understand it" has no primary source for him or for Einstein. And *The Feynman Lectures on Physics* is free to read online but remains under Caltech copyright, so what I built quotes him briefly and with attribution rather than reproducing him.

> "The first principle is that you must not fool yourself — and you are the easiest person to fool." — *Cargo Cult Science*, 1974
