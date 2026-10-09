# Hero image

`hero.svg` is the current header image: two Claude Code sessions side by side, the same
problem in both. Each assistant diagnoses it correctly, proposes the same fix, and stops
to ask permission — because that is what these tools do. On the left you approve
something you cannot picture. On the right you can actually answer. It is a plain SVG — no fonts to download, no
external requests, renders instantly on GitHub in both light and dark themes.

If you want a richer, photographic header instead, generate one and drop it here as
`hero.png` (or `.webp`), then change one line at the top of the root `README.md`:

```html
<img src="assets/hero.svg" alt="..." width="820">
```

Target **1600 × 900** or wider. Keep the file under ~500 KB so the page stays fast.

---

## Prompts

Paste any of these into ChatGPT, Midjourney, or another image model. Each is written to
produce something that carries the skill's actual thesis, not generic "AI brain" stock art.

### 1 — Triboluminescence (recommended)

This is the skill's central story rendered literally: Feynman's rewrite of a dead textbook
sentence into something you can go home and try. Dramatic, and it contains no person, no
logo, and no text to get garbled.

```
Extreme macro photograph, near-total darkness. A pair of worn steel pliers crushes a
single white sugar cube. At the instant of fracture the cube emits a faint electric-blue
flash from within, lighting the fracture planes and the tips of the pliers from the
inside. Everything else falls off into black. Shallow depth of field, sharp on the
fracture, cold blue light as the only source. Shot on a 100mm macro, f/4, high shutter
speed, visible crystal dust suspended in the air. Cinematic, restrained, scientific —
like a photograph from a physics paper that happens to be beautiful. No text, no people,
no logos. 16:9.
```

### 2 — The bird

Feynman's father's lesson, made visual: the names peel away, the bird remains.

```
A single brown thrush perched on a weathered tree stump, photographed in soft overcast
morning light against a deep desaturated background. Around the bird, a dozen small
handwritten paper name tags hang from thin threads — each showing a different language's
word for the bird — and they are blurred, out of focus, drifting away from the frame. The
bird itself is tack sharp, mid-motion, preening one wing. Muted natural palette, film
grain, 85mm lens, shallow depth of field. Quiet and observational, not whimsical. No
readable text in focus, no people. 16:9.
```

### 3 — The blackboard

Colder and more graphic. Good if you want something that reads as a header even at
thumbnail size.

```
A wide slate blackboard in a dim lecture hall, raking side light. On the left half, dense
illegible chalk equations crowd together, half-erased, chaotic. On the right half, almost
empty, a single clean chalk drawing: an open notebook with one large numeral 5, and two
arrows converging on it from opposite sides. A stub of chalk rests in the tray. Warm
dust in the air catching the light. Photographic, high contrast, deep blacks, no people,
no readable words. 16:9 cinematic crop.
```

---

## If the model garbles text

Image models still mangle lettering. Two ways out:

1. Ask for **no text at all** (every prompt above already does), and let the README's own
   headline carry the words.
2. Generate the imagery clean, then set type over it yourself in Figma, Canva or Keynote.

## Checklist before committing an image

- [ ] Renders legibly at 820 px wide — that is the width the README requests.
- [ ] Readable on both GitHub light and dark themes. Avoid pure-white backgrounds.
- [ ] Under ~500 KB.
- [ ] `alt` text in the README updated to describe the new image.
- [ ] No depiction of Richard Feynman or any other real person. The repository takes care
      not to put words in his mouth; it should not put a face on him either.

---

## The ten language versions

`hero.svg` is English; `hero.<lang>.svg` is each translation. All are produced by
[`generate_heroes.py`](generate_heroes.py) from one layout and ten sets of words:

```bash
python3 assets/generate_heroes.py
```

To change the wording, edit `hero-strings.json` and re-run. To add a language, add an
entry there and a font stack in the generator.

**Compose — do not translate.** The English entry is a content specification, not a source
text. Hand a native writer the *idea* and let them start from scratch in their language.
The first version of this image was written in English and translated nine ways; a native
speaker rejected the Portuguese on sight. Composing produced things translation cannot
reach — Portuguese ends the payoff on "dá pau", Spanish on the 2 a.m. complaint
"en Postman me funciona", Chinese on 报跨域, the verb people actually complain in.

Two decisions worth keeping if you edit the layout by hand:

- **The strike-through is `text-decoration`, not a drawn line.** A hand-placed `<line>`
  is computed against one font's metrics; the moment a viewer renders Devanagari or
  Arabic with something else, the rule misses the text. Let the renderer do it.
- **The height is computed from the content, not fixed.** A translation that needs one
  extra line would otherwise print straight through the footer rule.

Arabic and Urdu flip to `direction="rtl"` with end-anchored text and mirrored arrows.
