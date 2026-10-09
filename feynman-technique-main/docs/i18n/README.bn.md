<div align="center">

<img src="../../assets/hero.bn.svg" alt="feynman-technique — feynman-technique বন্ধ: এটা same-origin policy-জনিত CORS ত্রুটি। browser আগে preflight OPTIONS পাঠাচ্ছে। response-এ Access-Control-Allow-Origin নেই। তাই response body-টা browser block করেছে। API-র allowed origins-এ আপনার origin নেই। server-এ CORS middleware যোগ করে দিচ্ছি। middleware-এ CORS header config যোগ করব? — feynman-technique চালু: আপনার কোড ফেল করেনি, browser-ই থামিয়ে দিয়েছে। request গেছে, উত্তরও ফিরেছে, browser আপনাকে দেয়নি। আপনি হয়তো ওখানে আগে থেকেই ঢুকে আছেন। নিয়মটা না থাকলে যে কেউ আপনার login-এর ভেতরটা পড়ত। ওই server-কে বলতে হয় আপনার origin চলবে। সে কথাটা কখনো বলেনি, তাই আটকে গেছে। একই request Postman-এ চলে, browser-এ আটকায়। Postman কাউকে বাঁচাচ্ছে না, browser আপনাকে বাঁচাচ্ছে। সেই কথাটাই আমি ওই server-এ লিখে দেব। ওই server-এ আপনার origin-কে অনুমতি দিয়ে দিই?" width="820">

# ফাইনম্যান টেকনিক

### AI একটা fix ধরিয়ে দিল। কাজও হয়ে গেল। কেন হলো, আপনি আজও জানেন না।

**এই skill বানানো হয়েছে ওই শেষ কথাটার জন্যই।**

[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-%E0%A6%AE%E0%A7%81%E0%A6%95%E0%A7%8D%E0%A6%A4%20%E0%A6%AE%E0%A6%BE%E0%A6%A8-6b4fbb)](https://agentskills.io)
[![লাইসেন্স: MIT](https://img.shields.io/badge/%E0%A6%B2%E0%A6%BE%E0%A6%87%E0%A6%B8%E0%A7%87%E0%A6%A8%E0%A7%8D%E0%A6%B8-MIT-blue.svg)](../../LICENSE)
[![Works with](https://img.shields.io/badge/works%20with-Claude%20·%20ChatGPT%20·%20Codex%20·%20Cursor%20·%20Copilot%20·%20Gemini-333)](#ইনস্টলেশন)
[![ফাইনম্যানের 88,000 শব্দ থেকে](https://img.shields.io/badge/%E0%A6%89%E0%A7%8E%E0%A6%B8-%E0%A6%AB%E0%A6%BE%E0%A6%87%E0%A6%A8%E0%A6%AE%E0%A7%8D%E0%A6%AF%E0%A6%BE%E0%A6%A8%E0%A7%87%E0%A6%B0%2088%2C000%20%E0%A6%B6%E0%A6%AC%E0%A7%8D%E0%A6%A6-c2410c)](#এটা-কোথা-থেকে-এসেছে)

[English](../../README.md) ·
[中文](README.zh-CN.md) ·
[हिन्दी](README.hi.md) ·
[Español](README.es.md) ·
[Français](README.fr.md) ·
[العربية](README.ar.md) ·
**বাংলা** ·
[Português](README.pt-BR.md) ·
[Русский](README.ru.md) ·
[اردو](README.ur.md)

</div>

---

## একই মডেল। একই প্রশ্ন। সেটআপে এক লাইন।

> **"`Cannot read properties of undefined (reading 'map')` কেন আসছে?"**

<table>
<tr>
<th width="50%">skill ছাড়া</th>
<th width="50%">skill চালু থাকলে</th>
</tr>
<tr valign="top">
<td>

একটা undefined reference-এর উপর `.map()` কল করা হচ্ছে। asynchronous fetch resolve হওয়ার আগেই কম্পোনেন্টটা render হয়ে যাচ্ছে, তাই first paint-এর সময় state variable-টা তখনো uninitialised। ওটাকে empty array দিয়ে initialise করুন, নয়তো conditional দিয়ে render path-টা guard করুন।

</td>
<td>

আপনি পাতাটাকে বলেছেন: আমার জিনিসের তালিকাটা নাও, আর প্রতিটার জন্য একটা করে সারি আঁকো।

কিন্তু তালিকাটা এখনো এসে পৌঁছায়নি — server থেকে আসছে, পথেই আছে। ওই মুহূর্তে তালিকা বলে কিছুই নেই, আর যেখানে সেটা থাকার কথা ছিল সেই ফাঁকা জায়গাটাতেই পাতাটা হোঁচট খায়।

আসলটা না আসা পর্যন্ত ওর হাতে একটা খালি তালিকা ধরিয়ে দিন। তখন সে প্রথমে কিছুই আঁকে না, অপেক্ষা করে, তারপর সবটা আঁকে।

</td>
</tr>
<tr valign="top">
<td>

ছ'টা শব্দ, যেগুলো আপনার আগে থেকেই জানা থাকতে হবে। কথাটা ঠিক, তবু ছবিটা চোখে ভাসে না।

</td>
<td>

একটাও নয়। আর আপনি জানেন কোন লাইনটা বদলাবেন, বদলালে কী হবে।

</td>
</tr>
</table>

দুটো উত্তরই সত্যি। কিন্তু দুটোর মধ্যে ব্যাখ্যা ছিল একটাই।

---

## এটা কোথা থেকে এসেছে

ফাইনম্যান ছোট থাকতে তাঁর বাবা তাঁকে একটা পাখি দেখিয়ে বলেছিলেন, পৃথিবীর সব ভাষায় ওই পাখির নাম
শিখে ফেলা যায়, অথচ **পাখিটার সম্পর্কে কিচ্ছু জানা হয় না**। জানা হয় শুধু লোকে ওটাকে কী বলে
ডাকে। পাখিটাকে চিনতে হলে তাকিয়ে দেখতে হয়, ও করে কী।

> "There is a difference between the name of the thing and what goes on."
> — Richard Feynman, *What Is Science?*, 1966
>
> *"জিনিসটার নাম আর সেখানে আসলে যা ঘটছে — এ দুটো এক নয়।"*

পুরো ব্যাপারটা এটুকুই, আর প্রায় প্রতিটা AI নিজে থেকে ঠিক এখানেই ব্যর্থ হয়। ওরা জিনিসটার *নাম*
ধরিয়ে দেয়, আর নামটাকেই *জিনিস* বলে ভুল করতে দেয়। "এটা একটা race condition।" "এটা connection
pooling ব্যবহার করে।" আপনি সায় দিয়ে মাথা নাড়েন। আসলে কিছুই পৌঁছাল না। এই skill মডেলকে দিয়ে
বলায় **আগে মেকানিজমটা**, আর নাম বলায় সবার শেষে — ফাইনম্যান যেভাবে বলতেন।

এটা বানানো হয়েছে মূল উৎস ঘেঁটে, ফাইনম্যানকে নিয়ে লেখা ব্লগ পড়ে নয়। পদ্ধতি আর গদ্যের ঢং —
দুটোই বের করতে তাঁর নিজের লেখার প্রায় **88,000 শব্দ** বিশ্লেষণ করা হয়েছে: *Six Easy Pieces*,
1965 সালের নোবেল বক্তৃতা, *Cargo Cult Science*, *What Is Science?*, *There's Plenty of Room
at the Bottom*, আর *Surely You're Joking, Mr. Feynman!*-এর ব্রাজিল অধ্যায়।

**রিপোজিটরিটা ইংরেজিতে। উত্তরগুলো নয়** — আপনি যে ভাষায় লিখবেন, skill সেই ভাষাতেই উত্তর দেবে।

---

## যে চারটে পরীক্ষা এটা চালায়

লোকমুখে চলা সংস্করণটা নয়। এগুলো ফাইনম্যানের নিজের পরীক্ষা, প্রতিটাই মূল উৎসে নথিভুক্ত।

<table>
<tr valign="top"><td width="30%">

**নিজের ভাষায় বলার পরীক্ষা**

</td><td>

*"Without using the new word which you have just learned, try to rephrase what you have just learned in your own language."* (1966)

*"এইমাত্র যে নতুন শব্দটা শিখলেন, সেটা ব্যবহার না করে যা শিখলেন তা নিজের ভাষায় আবার বলার চেষ্টা করুন।"*

শব্দটা ঢেকে দিন। ওটা ছাড়া বাক্যটা যদি দাঁড়াতেই না পারে, তাহলে আপনি সংজ্ঞা লিখেছেন, ব্যাখ্যা নয়।

</td></tr>
<tr valign="top"><td>

**ট্রাইবোলুমিনেসেন্স পরীক্ষা**

</td><td>

ফাইনম্যান একটা পাঠ্যবই যেখানে খুশি খুলে পড়লেন: *"Triboluminescence is the light emitted when crystals are crushed."* — *"স্ফটিক গুঁড়িয়ে দিলে যে আলো বেরোয়, তাকে বলে ট্রাইবোলুমিনেসেন্স।"* তাঁর রায়: একটা শব্দের মানে আরেক গুচ্ছ শব্দ দিয়ে বলা হলো, এর বেশি কিছু নয়।

তিনি নিজে লিখে দেখালেন: *"When you take a lump of sugar and crush it with a pair of pliers in the dark, you can see a bluish flash. Some other crystals do that too. Nobody knows why. The phenomenon is called 'triboluminescence.'"* — *"অন্ধকারে এক টুকরো চিনি নিয়ে সাঁড়াশি দিয়ে গুঁড়িয়ে দিলে নীলচে একটা ঝিলিক চোখে পড়ে। আরও কিছু স্ফটিকেও এটা হয়। কেন হয়, কেউ জানে না। ব্যাপারটার নাম 'ট্রাইবোলুমিনেসেন্স'।"*

হাতে করে দেখা যায় এমন কিছু → কী চোখে পড়বে → না-জানাটা সোজাসুজি স্বীকার → **তারপর** নাম।

</td></tr>
<tr valign="top"><td>

**"পানির দিকে তাকাও" পরীক্ষা**

</td><td>

তাঁর ব্রাজিলীয় ছাত্ররা ব্রুস্টার কোণ গড়গড় করে বলে যেতে পারত। জানালার বাইরের উপসাগরের দিকে একটা পোলারয়েড তাক করতে বলায় তারা থমকে গেল।

যে ব্যাখ্যার কাছে কেবল তার কীওয়ার্ড ধরে পৌঁছানো যায়, বাস্তব পরিস্থিতিতে তার কাছে আপনি কোনোদিন পৌঁছাবেন না।

</td></tr>
<tr valign="top"><td>

**কার্গো কাল্ট পরীক্ষা**

</td><td>

পড়ার পর আপনি সত্যিই এমন কী *করতে* পারেন, যা আগে পারতেন না? বাইরের চেহারা ঠিক অথচ পেছনে কিছু নেই — তাহলে প্লেন নামে না।

</td></tr>
</table>

---

## ইনস্টলেশন

একটাই ফোল্ডার। [Agent Skills ওপেন স্ট্যান্ডার্ড](https://agentskills.io) মেনে চলে, এমন যেকোনো
টুলেই এটা চলে।

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/feynman-technique
mkdir -p ~/.claude/skills
cp -r /tmp/feynman-technique/skills/feynman-technique ~/.claude/skills/
```

Claude Code-এ এটুকুই যথেষ্ট। এবার শুধু জিজ্ঞেস করুন:

```
/feynman-technique ডেটাবেস ইনডেক্স কীভাবে কাজ করে বুঝিয়ে দিন
```

<details>
<summary><b>Claude Code</b> (প্রজেক্ট স্তরে, টিমের সঙ্গে ভাগ করা)</summary>

```bash
mkdir -p .claude/skills
cp -r /tmp/feynman-technique/skills/feynman-technique .claude/skills/
```

commit করে দিন, তাহলে রিপোজিটরিতে যে-ই কাজ করবে সে skill-টা পেয়ে যাবে। লোড হয়েছে কি না
দেখতে `/doctor` চালান।

</details>

<details>
<summary><b>স্ক্রিপ্টটাও আছে</b> (আর কপিটা বাসি হতে না দেওয়ার উপায়)</summary>

```bash
./install.sh              # ব্যক্তিগত, Claude Code
./install.sh --project    # এই রিপোজিটরিতে, টিমের জন্য
./install.sh --all        # এই মেশিনে টুলের যত ফোল্ডার আছে, সব কটিতে
./install.sh --check      # কোন কপিগুলো পিছিয়ে পড়েছে জানায়, কিছুই বদলায় না
```

মনে রাখার মতো অপশনটা `--check`। ইনস্টল করা skill আসলে একটা *কপি*; রিপোজিটরির সঙ্গে সে নিজে
থেকে বদলায় না। pull করার পর `--check` চালান — কোন কপিটা আর মিলছে না, সে নাম ধরে বলে দেবে।
নইলে কথাটা জানবেন সপ্তাহ কয়েক পরে, এমন একটা উত্তর থেকে, যেটা এতদিনে ঠিক হয়ে যাওয়ার কথা ছিল।

</details>

<details>
<summary><b>Claude.ai</b> (ওয়েব ও ডেস্কটপ অ্যাপ)</summary>

কোড এক্সিকিউশন চালু আছে, এমন **Pro, Max, Team বা Enterprise** প্ল্যান লাগবে।

1. এই রিপোজিটরিটা ডাউনলোড করুন ([**ZIP**](https://github.com/guicortei/feynman-technique/archive/refs/heads/main.zip))।
2. `skills/feynman-technique` **ফোল্ডারটাকেই** জিপ করুন, যাতে `SKILL.md` আর্কাইভের একদম
   গোড়ায় থাকে:
   ```bash
   cd skills && zip -r feynman-technique.zip feynman-technique
   ```
3. Claude-এ **Settings → Capabilities → Skills**-এ যান (কোনো কোনো প্ল্যানে এটা *Features*
   নামে দেখায়), তারপর **Upload skill** বেছে নিন।
4. `feynman-technique.zip` বেছে নিন।

ব্যাখ্যা চাইলে Claude নিজে থেকেই এটা ব্যবহার করবে, নাহলে নাম ধরে ডেকে নিতে পারেন।

> claude.ai-তে কাস্টম skill প্রতিটা ব্যবহারকারীর নিজের — টিমের প্রত্যেককে নিজের কপি আপলোড
> করতে হবে।

</details>

<details>
<summary><b>ChatGPT</b> (ডেস্কটপ অ্যাপ)</summary>

1. এই রিপোজিটরিটা ডাউনলোড করে আনজিপ করুন।
2. ChatGPT ডেস্কটপ অ্যাপ খুলে সাইডবারে **Skills** বেছে নিন।
3. `feynman-technique` ফোল্ডারটা যোগ করুন।
4. কথোপকথনে `@` লিখে তালিকা থেকে বেছে নিয়ে ডাকুন।

**আপনার প্ল্যানে skills নেই?** নিচের
[অন্য যেকোনো AI](#অন্য-যেকোনো-ai-skills-সমর্থন-ছাড়া) অংশের বিকল্পটা কাজে লাগান — এটা সাধারণ
ChatGPT, কাস্টম GPT আর Projects-এ চলে।

</details>

<details>
<summary><b>OpenAI Codex CLI</b></summary>

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/feynman-technique
mkdir -p ~/.agents/skills
cp -r /tmp/feynman-technique/skills/feynman-technique ~/.agents/skills/
```

প্রজেক্ট স্তরে চাইলে: রিপোজিটরির গোড়ায় `.agents/skills/`-এ কপি করুন।

`$feynman-technique` দিয়ে ডাকুন, বা কী কী আছে দেখতে `/skills` চালান।

</details>

<details>
<summary><b>Cursor</b></summary>

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/feynman-technique
mkdir -p ~/.cursor/skills
cp -r /tmp/feynman-technique/skills/feynman-technique ~/.cursor/skills/
```

প্রজেক্ট স্তরে: রিপোজিটরিতে `.cursor/skills/` বা `.agents/skills/`।
Cursor `~/.claude/skills/`-ও পড়ে, তাই Claude Code-এ ইনস্টল করা থাকলে আলাদা করে কিছু লাগবে না।

Agent চ্যাটে `/` লিখে **feynman-technique** বেছে নিন।

</details>

<details>
<summary><b>VS Code / GitHub Copilot</b></summary>

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/feynman-technique
mkdir -p ~/.copilot/skills
cp -r /tmp/feynman-technique/skills/feynman-technique ~/.copilot/skills/
```

ওয়ার্কস্পেস স্তরে: `.github/skills/` বা `.agents/skills/`।

Copilot Chat-এ `/` লিখে skill-টা বেছে নিন। পরে প্রসঙ্গও জুড়ে দিতে পারেন:
`/feynman-technique এই রিপোজিটরির অথ মিডলওয়্যার`।

</details>

<details>
<summary><b>Gemini CLI</b></summary>

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/feynman-technique
mkdir -p ~/.gemini/skills
cp -r /tmp/feynman-technique/skills/feynman-technique ~/.gemini/skills/
```

প্রজেক্ট স্তরে: `.gemini/skills/` বা `.agents/skills/`।
Gemini CLI কোনো skill চালু করার আগে আপনার অনুমতি চায়।

</details>

<details>
<summary><b>অন্যান্য সমর্থিত টুল</b></summary>

Amp, Goose, OpenCode, OpenHands, Roo Code, Kiro, Factory, JetBrains Junie, Letta,
Firebender, Tabnine, Trae, Mistral Vibe, Snowflake Cortex Code, Databricks Genie Code আর
আরও অনেকে এই স্ট্যান্ডার্ড সমর্থন করে।

বেশিরভাগ টুল এই পথগুলোর কোনো একটা পড়ে, মোটামুটি প্রচলনের ক্রমে:

```
~/.agents/skills/        # টুলগুলোর মধ্যে গড়ে ওঠা সাধারণ রীতি
~/.claude/skills/        # বিকল্প হিসেবে ব্যাপকভাবে সমর্থিত
<টুল-নির্দিষ্ট>/skills/    # যেমন ~/.gemini/skills/, ~/.cursor/skills/
```

আপনার টুলের ডকুমেন্টেশনে যে পথটার কথা বলা আছে, সেখানেই `feynman-technique` ফোল্ডারটা রাখুন।
ক্লায়েন্টের পুরো তালিকা [agentskills.io/clients](https://agentskills.io/clients)-এ।

</details>

<details>
<summary id="অন্য-যেকোনো-ai-skills-সমর্থন-ছাড়া"><b>অন্য যেকোনো AI (skills সমর্থন ছাড়া)</b></summary>

skill-টা সাধারণ Markdown, তাই সিস্টেম প্রম্পট হিসেবে যেকোনো জায়গায় চলে।

- **কাস্টম GPT / Gem / Assistant:**
  [`skills/feynman-technique/SKILL.md`](../../skills/feynman-technique/SKILL.md)
  (উপরের YAML ব্লকটা বাদ দিয়ে) নির্দেশনার ঘরে পেস্ট করুন। `references/`-এর ফাইলগুলো নলেজ
  ফাইল হিসেবে আপলোড করুন।
- **প্রজেক্ট / কাস্টম ইনস্ট্রাকশন:** একই কাজ, প্রজেক্টের কাস্টম-ইনস্ট্রাকশনের বাক্সে।
- **একবারের জন্য:** ফাইলটা চ্যাটে পেস্ট করে লিখুন *"বাকি কথোপকথনে এটা মেনে চলুন।"*

</details>

### ঠিকমতো কাজ করছে কি না দেখে নিন

আপনি ভালো বোঝেন, এমন কিছু জিজ্ঞেস করুন:

```
/feynman-technique হ্যাশ ফাংশন কী?
```

ঠিক উত্তর শুরু হবে এক বাক্যের মূল কথা দিয়ে, তারপর **একটাও পারিভাষিক শব্দ ছাড়া** শূন্য নম্বর
স্তর, আর শেষ হবে "ছবিটা কোথায় ভাঙে" অংশ দিয়ে। উত্তর যদি শুরু হয় "হ্যাশ ফাংশন হলো এমন একটা
ফাংশন যা যেকোনো আকারের ডেটাকে…" দিয়ে, তাহলে skill লোড হয়নি।

---

## উত্তরে যা পাবেন

```
**এক বাক্যে:** ...          ← যাতে বিশেষজ্ঞ এখানেই থামতে পারেন

**যে ছবিটি ধরে রাখবেন:** ...  ← মূল উপমা

০ · আড্ডা         ক্ষেত্রটির কোনো পূর্বজ্ঞান নেই। শূন্য পারিভাষিক শব্দ।
১ · নবাগত        আসল নামগুলো, স্তর ০-এর ছবির সঙ্গে বাঁধা
২ · পেশাদার      অংশগুলো কীভাবে জোড়া লাগে, আর প্রথম সত্যিকারের আপস
৩ · দেখভালকারী   ব্যর্থতার ধরন, কী ভাঙে, কী বাদ দেওয়া হলো ও কেন
৪ · বিশেষজ্ঞ      প্রান্তসীমা, মাপ, এবং মডেলটির নিজেরই সীমা

ছবিটি কোথায় ভাঙে       ← প্রতিটি উপমার সীমা, স্পষ্ট করে বলা
এখানে আসা নতুন শব্দ    ← প্রতি নতুন শব্দে এক লাইন
যা বাদ দিলাম           ← নাম ধরে বলা, চুপচাপ বাদ নয়
```

স্তরগুলো ছোট হয়ে আসে, কিন্তু কখনো উধাও হয় না। ছোট, নির্দিষ্ট প্রশ্নের উত্তর আসে **সংক্ষিপ্ত
রূপে** — মূল কথা, ছবি, আর যে একটামাত্র স্তর দরকার সেটা। বিশেষজ্ঞকে জোর করে পাঁচটা স্তর পার
করানোকে খুঁটিয়ে বোঝানো বলে না; মেপে দেখা গেছে, এতে তাঁর বোঝাটা উল্টে *খারাপ* হয় (একে বলে
[expertise reversal effect](../../skills/feynman-technique/references/evidence.md))।

দেখে নিন [শুরু থেকে শেষ পর্যন্ত করা একটা উদাহরণ](../../skills/feynman-technique/assets/worked-example.md) —
"ডেটাবেস ইনডেক্স কী?" প্রশ্নের পুরো উত্তর, তারপর টীকা দিয়ে দেখানো কোন অংশটা কী কাজ করছে।

---

## কোচ মোড — যেটা সত্যিই শেখায়

```
/feynman-technique TCP কীভাবে কনজেশন সামলায় তা নিয়ে আমাকে প্রশ্ন করুন
/feynman-technique আমি যাচাই করতে চাই ইভেন্ট সোর্সিং সত্যিই বুঝেছি কি না
```

এখানে skill ব্যাখ্যা করতে রাজি হয় না। ব্যাখ্যা করেন **আপনি**; সে শুধু শোনে — কোথায় কথা
ফাঁকা, কোথায় পারিভাষিক শব্দ বসিয়ে কথা থামিয়ে দেওয়া হলো, কোন ধাপটা মেকানিজম ছাড়াই দাবি করা
হলো। তারপর একবারে ঠিক একটা ফাঁক দেখিয়ে দেয়, উত্তরটা হাতে তুলে না দিয়ে।

গবেষণার সবচেয়ে জোরালো ভিত্তি এই মোডটার পেছনেই। যারা শেখানোর প্রস্তুতি নেয়, তারা পরীক্ষার
প্রস্তুতি নেওয়াদের চেয়ে ভালো করে — *শেখানোর ঘটনাটা কখনো না ঘটলেও* (Nestojko et al., 2014)।
নিজের ব্যাখ্যা নিজে দাঁড় করানো অন্যের ব্যাখ্যা পড়ার চেয়ে ভালো (Chi et al., 1989)।

---

## যে নিয়মগুলো এটা মেনে চলে

| | চেনা "সহজ করে বলো" প্রম্পট | এই skill |
|---|---|---|
| **পরিভাষা** | বাক্য সহজ হয়, শব্দ একই থাকে | প্রতিটা নতুন শব্দ প্রথম ব্যবহারেই ব্যাখ্যা হয়, নইলে শব্দটা আসেই না |
| **উপমা** | প্রতি অনুচ্ছেদে নতুন রূপক | একটাই মূল উপমা, জটিলতা যোগ করে বাড়ানো — **আর সেটা কোথায় ভাঙে** |
| **নির্ভুলতা** | সরল করতে গিয়ে ভুল হয়ে যায় | আন্দাজে বলা কথাগুলো *কতদূর খাটে তা জানিয়ে* বলা হয় |
| **গভীরতা** | একটাই সমতল স্তর | সিঁড়ি, যার যেকোনো ধাপে নেমে যেতে পারেন |
| **বিশেষজ্ঞ** | তাঁদের ছোট করে দেখা হয় | প্রথম লাইনেই মূল কথা, তারপর সংক্ষিপ্ত রূপ |
| **নাম** | নামটাই উত্তর | আগে মেকানিজম, নাম সবার শেষে |
| **অজ্ঞতা** | চেপে যাওয়া হয় | সত্যি হলে "কেউ জানে না" সোজা বলে দেওয়া হয় |
| **শেখা** | আপনাকে শুধু বলে যায় | কোচ মোড *আপনাকে* দিয়ে বলায়, আর ফাঁকগুলো ধরিয়ে দেয় |

শূন্য নম্বর নিয়ম: **স্পষ্ট হওয়ার অজুহাতে ভুল বলা চলবে না।** সরল করতে গিয়ে কথাটা বেঁকে যাবে
বুঝলে skill সেটা বলে দেয়, কতদূর পর্যন্ত কথাটা খাটে জানিয়ে দেয়, আর এক ধাপ উপরের নিখুঁত রূপটাও
ধরিয়ে দেয়।

---

## ভেতরে কী আছে

skill-এর ফাইলগুলো ইংরেজিতেই রাখা, যাতে frontmatter প্রামাণিক থাকে।

| ফাইল | কী আছে |
|---|---|
| [**SKILL.md**](../../skills/feynman-technique/SKILL.md) | skill নিজেই। শুরু করুন এখান থেকে। |
| [references/voice.md](../../skills/feynman-technique/references/voice.md) | ফাইনম্যানের গদ্যের ফরেনসিক বিশ্লেষণ, কর্পাসের পরিসংখ্যানসহ |
| [references/ladder.md](../../skills/feynman-technique/references/ladder.md) | স্তরের মাপজোক, আর কাঠামোটা কীভাবে বদলাতে হয় |
| [references/analogies.md](../../skills/feynman-technique/references/analogies.md) | উপমা বানানো, বাড়ানো আর চাপ দিয়ে পরীক্ষা করা |
| [references/failure-modes.md](../../skills/feynman-technique/references/failure-modes.md) | ব্যাখ্যা ভেস্তে যাওয়ার 14টা ধরন, প্রতিটার সঙ্গে নতুন করে লেখা রূপ |
| [references/evidence.md](../../skills/feynman-technique/references/evidence.md) | শেখার বিজ্ঞান — আর এই পদ্ধতি সত্যিই কোথায় খাটে না |
| [references/sources.md](../../skills/feynman-technique/references/sources.md) | যাচাই করা উদ্ধৃতি, আর যেগুলো ভুল করে তাঁর নামে চালানো হয় |
| [assets/worked-example.md](../../skills/feynman-technique/assets/worked-example.md) | একটা পূর্ণ উত্তর, টীকাসহ |
| [assets/checklist.md](../../skills/feynman-technique/assets/checklist.md) | পাঠানোর আগে শেষ যাচাই |

### গদ্য-বিশ্লেষণের একটা নমুনা

[voice.md](../../skills/feynman-technique/references/voice.md) থেকে; সবই 88,000 শব্দের
কর্পাসে মাপা:

- **বাক্যের দৈর্ঘ্যের এই ওঠানামাই তাঁর স্বাক্ষর।** বাক্যের মধ্যমা প্রায় 20 শব্দ — কিন্তু প্রতি
  আটটার মধ্যে একটা আট শব্দেরও ছোট, আর প্রতি ছয়টার মধ্যে একটা পঁয়ত্রিশ ছাড়িয়ে যায়। তিনি
  লম্বা করে গড়েন, আর নামেন ছোট বাক্যে। *"Shake this one, that one shakes later."*
- **সর্বনাম বদলায় কাজ অনুযায়ী।** শেখানোর সময় "we" (*Six Easy Pieces*-এ প্রতি 1,000 শব্দে
  19.95 বার — তাঁর "I"-এর দশ গুণ), নিজের গুলিয়ে যাওয়ার কথা বলতে গেলে "I" (নোবেল বক্তৃতায়
  প্রতি হাজারে 26.7), নির্দেশ দেওয়ার সময় "you" (*Cargo Cult Science*-এ প্রতি হাজারে 20.6)।
- **শরীর টের পায় এমন ক্রিয়া।** *jiggle* 27, *pull* 37, *push* 28, *shake* 20। অণু *কাঁপে*;
  অণু "তাপীয় আলোড়ন প্রদর্শন" করে না।
- **"Basically" 88,000 শব্দে একবারও আসেনি।** *Trivial* এসেছে একবার। এ কারণেই skill এই
  শব্দগুলো নিষিদ্ধ করে — এটা মাপজোক, রুচি নয়।

---

## সৎ সীমাবদ্ধতা

শূন্য নম্বর নিয়ম এই পাতাটার ক্ষেত্রেও খাটে।

- **ফাইনম্যান "ফাইনম্যান টেকনিক" বলে কিছু বানাননি।** এই নামে চার ধাপের কোনো পদ্ধতি তিনি
  কখনো প্রকাশ করেননি। ধাপ চারটে সাজিয়েছেন পরের জনপ্রিয় লেখকরা — মূলত স্কট এইচ. ইয়ং, 2011
  সালের দিকে — একটা ন্যায্য পুনর্গঠন হিসেবে। এই skill তার বদলে তাঁর *নথিভুক্ত* পরীক্ষাগুলো
  ব্যবহার করে, আর সেটা বলেও দেয়।
- **"সহজ করে বোঝাতে না পারলে আপনি নিজেই বোঝেননি"** — এই কথার কোনো মূল উৎস নেই, ফাইনম্যানেরও
  না, আইনস্টাইনেরও না। [sources.md](../../skills/feynman-technique/references/sources.md)-এ
  আছে তিনি প্রমাণসহ কী বলেছেন আর কী বলেননি।
- **সব জিনিস সরল হয় না।** ফাইনম্যান নিজেই এই দেয়ালে ধাক্কা খেয়েছেন: তাঁর নিজের বাবা যখন
  জিজ্ঞেস করলেন, পরমাণুর ভেতরে না থেকেও ফোটন কী করে বেরিয়ে আসে, তিনি বলেছিলেন *"I'm sorry;
  I don't know. I can't explain it to you."* বানানো একটা ছবি ধরিয়ে দেওয়ার বদলে এই কথাটাই
  বলার জন্য skill-টা তৈরি।
- **এতে token আর সময় খরচ হয়।** চটজলদি কিছু দেখে নিতে হলে সংক্ষিপ্ত রূপ, বা skill একেবারেই
  না চালানো — সেটাই ঠিক সিদ্ধান্ত।
- **মুখস্থ করা বা হাতের দক্ষতায় এটা বিশেষ কাজে আসে না।** এর লক্ষ্য কারণ আর মেকানিজম বোঝা।
  শব্দভাণ্ডার আর কি-বাইন্ডিংয়ের জন্য দরকার নির্দিষ্ট বিরতিতে বারবার মনে করার অনুশীলন
  (spaced retrieval), ব্যাখ্যা নয়।
- **ভালো ব্যাখ্যা পড়লে বুঝে ফেলেছেন বলে *মনে হয়*।** ওই অনুভূতিটা প্রমাণ নয়। যেখানে সত্যিই
  দরকার, সেখানে কোচ মোড ব্যবহার করুন।

---

## কৃতিত্ব ও কপিরাইট

রিচার্ড পি. ফাইনম্যান (1918–1988) এখানে পড়ার মতো যা কিছু আছে, সবই লিখেছেন। এই রিপোজিটরিতে
আছে **তাঁর লেখা থেকে বের করা নিয়ম আর উৎস উল্লেখ করে দেওয়া ছোট ছোট উদ্ধৃতি**, বিশ্লেষণ আর
শেখানোর কাজে — তাঁর লেখা এখানে নতুন করে বিলি করা হয় না।

তাঁর লেখা এখনো কপিরাইটে: *The Feynman Lectures on Physics*
[feynmanlectures.caltech.edu](https://www.feynmanlectures.caltech.edu/)-এ বিনামূল্যে *পড়া*
যায়, কিন্তু এটা © Caltech, আর **পাবলিক ডোমেইনে নয়**। fork করলে ব্যাপারটা এভাবেই রাখুন: অল্প
উদ্ধৃত করুন, সবসময় উৎস দিন, কখনো গোটা অধ্যায় পেস্ট করবেন না। পুরো উৎস-বিবরণ
[sources.md](../../skills/feynman-technique/references/sources.md)-এ।

এই skill-এর শুরু `feynman-reply` নামে, [@guicortei](https://github.com/guicortei)-এর একটা
পর্তুগিজ skill হিসেবে। পরে মূল উৎস থেকে নতুন করে বানানো হয়েছে, সফটওয়্যারের বাইরেও ছড়ানো
হয়েছে, আর সঙ্গে যোগ হয়েছে গদ্য-বিশ্লেষণ, প্রমাণের ভিত্তি আর কোচ মোড — তারপর নাম বদলে
`feynman-technique`।

ফাইনম্যান এস্টেট, Caltech বা Anthropic-এর সঙ্গে এর কোনো সম্পর্ক নেই, কারও অনুমোদনও নেই।

## অবদান

উন্নতির প্রস্তাব স্বাগত — বিশেষ করে:

- অন্য ক্ষেত্রের কষে দেখানো উদাহরণ (চিকিৎসা, আইন, ফিনান্স, জীববিজ্ঞান)
- বাস্তব ব্যবহারে ধরা পড়া ব্যর্থতার ধরন
- যেকোনো উদ্ধৃতি বা উৎস-নির্দেশের সংশোধন

দেখুন [CONTRIBUTING.md](../../CONTRIBUTING.md)। একটাই অনুরোধ: ফাইনম্যানকে নিয়ে নতুন কোনো দাবি
যোগ করলে মূল উৎসটা উল্লেখ করুন। বুদ্ধিবৃত্তিক সততার কথা বলতে বলতে তাঁর নাম নেওয়া, অথচ উৎস
উল্লেখে গা-ছাড়া ভাব — এই রিপোজিটরিতে এটাই একমাত্র অমার্জনীয় bug।

## লাইসেন্স

[MIT](../../LICENSE)। ব্যবহার করুন, fork করুন, ship করুন।

---

<div align="center">

> *"The first principle is that you must not fool yourself — and you are the easiest person
> to fool."*
> — Richard Feynman, *Cargo Cult Science*, 1974
>
> *"প্রথম নীতি হলো, নিজেকে ঠকানো চলবে না — আর ঠকানো সবচেয়ে সহজ যাকে, সে আপনি নিজেই।"*

**[⭐ রিপোজিটরিটায় স্টার দিন](https://github.com/guicortei/feynman-technique)** — আজ পাওয়া
কোনো একটা উত্তর যদি এটা বদলে দিয়ে থাকে।

</div>
