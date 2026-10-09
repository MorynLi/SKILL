<div align="center">

<img src="../../assets/hero.ur.svg" alt="feynman-technique — skill کے بغیر: یہ CORS کا issue ہے، same-origin policy کے تحت۔ براؤزر preflight OPTIONS ریکویسٹ بھیج رہا ہے۔ response میں Access-Control-Allow-Origin غائب ہے۔ server آپ کے origin کو whitelist نہیں کر رہا۔ allowed origins اور headers set کرنے ہوں گے۔ server.js میں CORS middleware add کر دیتا ہوں۔ server.js میں CORS middleware add کر دوں؟ — skill کے ساتھ: آپ کا کوڈ ناکام نہیں ہوا — براؤزر نے روکا ہے۔ ریکویسٹ وہاں پہنچی، جواب بھی واپس آ گیا۔ براؤزر نے وہ جواب آپ تک پہنچنے نہیں دیا۔ ہو سکتا ہے آپ وہاں پہلے سے لاگ اِن ہوں۔ ورنہ ہر کھلا ٹیب آپ کے لاگ اِن میں جھانک لیتا۔ اُس سائٹ کو آپ کا ڈومین اجازت میں لکھنا تھا۔ اُس نے کبھی نہیں لکھا — اِس لیے جواب رُک گیا۔ Postman میں وہی ریکویسٹ چلتی ہے، براؤزر میں نہیں۔ Postman کسی کو نہیں بچاتا، براؤزر آپ کو بچاتا ہے۔ میں آپ کا پتہ API کی اجازت میں لکھ دیتا ہوں۔ server.js میں آپ کا پتہ اجازت میں لکھ دوں؟" width="820">

# فائن مین تکنیک

### AI نے حل تھمایا۔ آپ نے چسپاں کیا، چل بھی گیا۔ کیوں چلا، یہ آپ آج تک نہیں جانتے۔

**یہ skill اُسی دوسری بات کے لیے ہے۔**

[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-%D9%85%D9%81%D8%AA%D9%88%D8%AD%20%D9%85%D8%B9%DB%8C%D8%A7%D8%B1-6b4fbb)](https://agentskills.io)
[![لائسنس: MIT](https://img.shields.io/badge/%D9%84%D8%A7%D8%A6%D8%B3%D9%86%D8%B3-MIT-blue.svg)](../../LICENSE)
[![Works with](https://img.shields.io/badge/works%20with-Claude%20·%20ChatGPT%20·%20Codex%20·%20Cursor%20·%20Copilot%20·%20Gemini-333)](#تنصیب)

[English](../../README.md) ·
[中文](README.zh-CN.md) ·
[हिन्दी](README.hi.md) ·
[Español](README.es.md) ·
[Français](README.fr.md) ·
[العربية](README.ar.md) ·
[বাংলা](README.bn.md) ·
[Português](README.pt-BR.md) ·
[Русский](README.ru.md) ·
**اردو**

</div>

---

<div dir="rtl">

## وہی ماڈل۔ وہی سوال۔ سیٹ اپ کی صرف ایک سطر۔

> **”مجھے `Cannot read properties of undefined (reading 'map')` کیوں مل رہا ہے؟“**

</div>

<table>
<tr>
<th width="50%">
<div dir="rtl">
skill کے بغیر
</div>
</th>
<th width="50%">
<div dir="rtl">
skill کے ساتھ
</div>
</th>
</tr>
<tr valign="top">
<td>

<div dir="rtl">

`.map()` ایک ایسے ریفرنس پر چلایا جا رہا ہے جو undefined ہے۔ آپ کا کمپوننٹ asynchronous fetch مکمل ہونے سے پہلے رینڈر ہو جاتا ہے، اِس لیے پہلے پینٹ کے وقت state ویری ایبل ابھی initialise نہیں ہوا ہوتا۔ اِسے خالی array سے initialise کیجیے، یا رینڈر پاتھ پر ایک کنڈیشنل گارڈ لگا دیجیے۔

</div>

</td>
<td>

<div dir="rtl">

آپ نے صفحے سے کہا تھا: میری چیزوں کی فہرست لو، اور ہر چیز کے لیے ایک سطر بنا دو۔

مگر فہرست ابھی پہنچی ہی نہیں — وہ اب بھی سرور سے راستے میں ہے۔ اُس لمحے فہرست سرے سے کہیں نہیں ہوتی، اور صفحہ اُسی خالی جگہ سے ٹھوکر کھا جاتا ہے جہاں فہرست ہونی چاہیے تھی۔

اصل فہرست پہنچنے تک اُس کے ہاتھ میں ایک خالی فہرست تھما دیجیے۔ اب وہ پہلے کچھ نہیں بناتا، ٹھہرتا ہے، اور پھر سب کچھ بنا دیتا ہے۔

</div>

</td>
</tr>
<tr valign="top">
<td>

<div dir="rtl">

چھ اصطلاحیں، جو آپ کو پہلے سے آنی چاہیے تھیں۔ بات درست ہے، اور تصویر پھر بھی نہیں بنتی۔

</div>

</td>
<td>

<div dir="rtl">

ایک بھی نہیں۔ اور آپ کو یہ بھی معلوم ہے کہ کون سی سطر بدلنی ہے، اور اُس کے بعد ہونا کیا چاہیے۔

</div>

</td>
</tr>
</table>

<div dir="rtl">

دونوں جواب سچ ہیں۔ وضاحت اُن میں سے صرف ایک تھی۔

---

## یہ کہاں سے آئی ہے

فائن مین کے والد نے اُنہیں ایک پرندہ دکھایا اور کہا: تم اِس کا نام دنیا کی ہر زبان میں سیکھ لو،
پھر بھی اِس پرندے کے بارے میں **بالکل کچھ نہیں جانتے** ہوگے۔ تمہیں صرف اتنا معلوم ہوگا کہ لوگ
اِسے کیا کہتے ہیں۔ پرندے کو جاننا ہو تو دیکھو کہ وہ کرتا کیا ہے۔

> "There is a difference between the name of the thing and what goes on."
> — Richard Feynman, *What Is Science?*, 1966
>
> *”کسی چیز کے نام میں، اور جو کچھ اصل میں ہو رہا ہوتا ہے اُس میں، فرق ہے۔“*

پوری بات یہی ہے، اور تقریباً ہر AI طے شدہ طور پر یہیں ناکام ہوتا ہے۔ کوئی چیز کیا ہے، یہ پوچھیے
تو وہ آپ کو چیز کا *نام* کچھ بھاری بھرکم الفاظ میں واپس تھما دیتا ہے، اور آپ نام ہی کو *چیز*
سمجھ بیٹھتے ہیں۔ ”یہ ریس کنڈیشن ہے۔“ ”یہ کنکشن پُولنگ استعمال کرتا ہے۔“ آپ اثبات میں سر ہلا
دیتے ہیں۔ منتقل کچھ بھی نہیں ہوا۔ یہ skill ماڈل سے پہلے **یہ کہلواتی ہے کہ چیز چلتی کیسے ہے**،
اور نام سب سے آخر میں — جیسے فائن مین کہا کرتے تھے۔

یہ فائن مین کے بارے میں لکھے گئے بلاگوں سے نہیں، اصل مآخذ سے بنی ہے۔ طریقہ اور اندازِ تحریر،
دونوں اخذ کرنے کے لیے اُن کی اپنی تحریروں کے تقریباً **۸۸٬۰۰۰ الفاظ** کا تجزیہ کیا گیا:
*Six Easy Pieces*، ۱۹۶۵ کا نوبل خطبہ، *Cargo Cult Science*، *What Is Science?*،
*There's Plenty of Room at the Bottom*، اور *Surely You're Joking, Mr. Feynman!* کا برازیل
والا باب۔

**ریپازٹری انگریزی میں ہے۔ جواب نہیں** — آپ جس زبان میں لکھیں گے، skill اُسی زبان میں جواب دے
گی۔

---

## یہ چار کسوٹیاں لگاتی ہے

مشہورِ عام ”بارہ سال کے بچے کو سمجھاؤ“ والی صورت نہیں۔ یہ خود فائن مین کی کسوٹیاں ہیں، اور اِن
میں سے ہر ایک بنیادی ماخذ تک جاتی ہے۔

</div>

<table>
<tr valign="top"><td width="30%">

<div dir="rtl">

**دوبارہ بیان کی کسوٹی**

</div>

</td><td>

<div dir="rtl">

*"Without using the new word which you have just learned, try to rephrase what you have just learned in your own language."* (۱۹۶۶)

*”ابھی جو نیا لفظ سیکھا ہے، اُسے استعمال کیے بغیر، جو کچھ سیکھا ہے اُسے اپنی زبان میں دوبارہ کہہ کر دیکھیے۔“*

اصطلاح پر ہاتھ رکھ لیجیے۔ اُس کے بغیر جملہ دم توڑ دے، تو آپ نے تعریف لکھی تھی، وضاحت نہیں۔

</div>

</td></tr>
<tr valign="top"><td>

<div dir="rtl">

**ٹرائبولیومینیسنس کی کسوٹی**

</div>

</td><td>

<div dir="rtl">

فائن مین نے ایک نصابی کتاب اٹکل سے کھولی اور پڑھا: *"Triboluminescence is the light emitted when crystals are crushed."* — *”ٹرائبولیومینیسنس وہ روشنی ہے جو کرسٹل کچلے جانے پر خارج ہوتی ہے۔“* اُن کا فیصلہ یہ تھا کہ آپ نے صرف اتنا بتایا ہے کہ ایک لفظ کا مطلب چند دوسرے لفظوں میں کیا بنتا ہے۔

اور یہ اُن کی اپنی دوبارہ تحریر: *"When you take a lump of sugar and crush it with a pair of pliers in the dark, you can see a bluish flash. Some other crystals do that too. Nobody knows why. The phenomenon is called 'triboluminescence.'"* — *”اندھیرے میں چینی کی ایک ڈلی لے کر پلاس سے کچلیں تو نیلی سی چمک نظر آتی ہے۔ کچھ اور کرسٹل بھی ایسا ہی کرتے ہیں۔ کیوں کرتے ہیں، یہ کوئی نہیں جانتا۔ اِس مظہر کو ’ٹرائبولیومینیسنس‘ کہتے ہیں۔“*

ایسا کام جو آپ خود کر کے دیکھ سکیں ← پھر یہ کہ نظر کیا آئے گا ← پھر جو معلوم نہیں اُس کا صاف اعتراف ← **اور تب** نام۔

</div>

</td></tr>
<tr valign="top"><td>

<div dir="rtl">

**”پانی کو دیکھو“ کی کسوٹی**

</div>

</td><td>

<div dir="rtl">

اُن کے برازیلی طلبہ بروسٹر کا زاویہ حرف بہ حرف سنا دیتے تھے۔ کھڑکی کے باہر پھیلی خلیج کی طرف پولرائیڈ کا رُخ کرنے کو کہا گیا، تو سب ساکت رہ گئے۔

جو وضاحت صرف اپنے کلیدی لفظ کے راستے سے ملتی ہو، وہ اصل دنیا میں کبھی ہاتھ نہیں آتی۔

</div>

</td></tr>
<tr valign="top"><td>

<div dir="rtl">

**کارگو کلٹ کی کسوٹی**

</div>

</td><td>

<div dir="rtl">

پڑھنے کے بعد آپ ایسا کیا *کر* سکتے ہیں جو پہلے نہیں کر سکتے تھے؟ شکل درست ہو اور پیچھے کچھ نہ ہو، تو جہاز نہیں اُترتے۔

</div>

</td></tr>
</table>

<div dir="rtl">

---

## تنصیب

ایک فولڈر۔ ہر اُس ٹول میں چلتی ہے جو [Agent Skills کے کھلے معیار](https://agentskills.io) کو
سپورٹ کرتا ہے۔

</div>

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/feynman-technique
mkdir -p ~/.claude/skills
cp -r /tmp/feynman-technique/skills/feynman-technique ~/.claude/skills/
```

<div dir="rtl">

یہ Claude Code کے لیے ہے۔ اِس کے بعد بس پوچھیے:

</div>

```
/feynman-technique سمجھائیے کہ ڈیٹابیس انڈیکس کیسے کام کرتے ہیں
```

<details>
<summary><b>Claude Code</b> — پروجیکٹ کی سطح پر، پوری ٹیم کے لیے</summary>

```bash
mkdir -p .claude/skills
cp -r /tmp/feynman-technique/skills/feynman-technique .claude/skills/
```

<div dir="rtl">

اِسے commit کر دیجیے، اور ریپازٹری پر کام کرنے والے ہر شخص کو مل جائے گی۔ لوڈ ہوئی یا نہیں، یہ
`/doctor` چلا کر دیکھ لیجیے۔

</div>

</details>

<details>
<summary><b>یا اسکرپٹ چلا لیجیے</b> — تاکہ آپ کی نقل پرانی نہ پڑ جائے</summary>

```bash
./install.sh              # ذاتی سطح پر، Claude Code کے لیے
./install.sh --project    # اِسی ریپازٹری میں، ٹیم کے لیے
./install.sh --all        # اِس مشین پر موجود ہر ٹول کی ڈائرکٹری میں
./install.sh --check      # بتائے گا کون سی نقل پیچھے رہ گئی، بدلے گا کچھ نہیں
```

<div dir="rtl">

یاد رکھنے کے قابل `--check` ہی ہے۔ انسٹال شدہ skill ایک *نقل* ہوتی ہے؛ وہ ریپازٹری کے ساتھ ساتھ
نہیں چلتی۔ pull کیجیے، `--check` چلائیے، اور یہ ہر اُس نقل کا نام لے دے گی جو اب میل نہیں کھاتی
— ورنہ پتا ہفتوں بعد چلتا ہے، کسی ایسے جواب سے جو کب کا درست ہو چکا ہونا چاہیے تھا۔

</div>

</details>

<details>
<summary><b>Claude.ai</b> — ویب اور ڈیسک ٹاپ</summary>

<div dir="rtl">

اِس کے لیے کوڈ ایگزیکیوشن کے ساتھ **Pro، Max، Team یا Enterprise** پلان درکار ہے۔

1. یہ ریپازٹری ڈاؤن لوڈ کیجیے ([**ZIP**](https://github.com/guicortei/feynman-technique/archive/refs/heads/main.zip))۔
2. `skills/feynman-technique` **فولڈر کو ہی** زپ کیجیے، تاکہ `SKILL.md` آرکائیو کی روٹ میں رہے:

</div>

```bash
cd skills && zip -r feynman-technique.zip feynman-technique
```

<div dir="rtl">

3. Claude میں **Settings ← Capabilities ← Skills** پر جائیے (بعض پلانز میں یہ *Features*
   لکھا ہوتا ہے) اور **Upload skill** منتخب کیجیے۔
4. `feynman-technique.zip` چن لیجیے۔

آپ وضاحت مانگیں تو Claude اِسے خود ہی استعمال کر لیتا ہے، اور آپ نام لے کر بھی مانگ سکتے ہیں۔

claude.ai پر کسٹم skills ہر صارف کی اپنی ہوتی ہیں — ہر ساتھی کو اپنی نقل خود اپلوڈ کرنی ہوگی۔

</div>

</details>

<details>
<summary><b>ChatGPT</b> — ڈیسک ٹاپ ایپ</summary>

<div dir="rtl">

ریپازٹری ڈاؤن لوڈ کر کے اَن زپ کیجیے، پھر ChatGPT ڈیسک ٹاپ ایپ کے سائیڈ بار سے **Skills** پر
جائیے اور `feynman-technique` فولڈر شامل کر دیجیے۔ گفتگو کے دوران `@` لکھ کر فہرست میں سے اِسے
چن لیجیے۔

**آپ کے پلان میں skills کی سہولت نہیں؟** نیچے [کوئی اور AI](#any-other-ai-no-skills-support)
والا متبادل استعمال کیجیے — یہ سادہ ChatGPT، کسٹم GPT اور Projects، سب میں چلتا ہے۔

</div>

</details>

<details>
<summary><b>OpenAI Codex CLI</b></summary>

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/feynman-technique
mkdir -p ~/.agents/skills
cp -r /tmp/feynman-technique/skills/feynman-technique ~/.agents/skills/
```

<div dir="rtl">

پروجیکٹ کی سطح پر: ریپازٹری کی روٹ میں `.agents/skills/` کے اندر نقل کیجیے۔ بلانے کے لیے
`$feynman-technique` لکھیے، اور دستیاب skills کی فہرست کے لیے `/skills` چلائیے۔

</div>

</details>

<details>
<summary><b>Cursor</b></summary>

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/feynman-technique
mkdir -p ~/.cursor/skills
cp -r /tmp/feynman-technique/skills/feynman-technique ~/.cursor/skills/
```

<div dir="rtl">

پروجیکٹ کی سطح پر: `.cursor/skills/` یا `.agents/skills/`۔ Cursor `~/.claude/skills/` بھی
پڑھتا ہے، اِس لیے Claude Code میں انسٹال کر رکھی ہو تو وہی کافی ہے۔ Agent چیٹ میں `/` لکھ کر
**feynman-technique** چن لیجیے۔

</div>

</details>

<details>
<summary><b>VS Code / GitHub Copilot</b></summary>

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/feynman-technique
mkdir -p ~/.copilot/skills
cp -r /tmp/feynman-technique/skills/feynman-technique ~/.copilot/skills/
```

<div dir="rtl">

ورک اسپیس کی سطح پر: `.github/skills/` یا `.agents/skills/`۔ Copilot Chat میں `/` لکھ کر skill
چن لیجیے؛ اُس کے بعد سیاق بھی ساتھ لکھ سکتے ہیں۔

</div>

</details>

<details>
<summary><b>Gemini CLI</b></summary>

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/feynman-technique
mkdir -p ~/.gemini/skills
cp -r /tmp/feynman-technique/skills/feynman-technique ~/.gemini/skills/
```

<div dir="rtl">

پروجیکٹ کی سطح پر: `.gemini/skills/` یا `.agents/skills/`۔ Gemini CLI کسی skill کو چلانے سے
پہلے آپ سے اجازت مانگتا ہے۔

</div>

</details>

<details>
<summary><b>باقی سب کچھ</b> — Amp، Goose، Kiro، Junie، Roo، Factory، Tabnine…</summary>

<div dir="rtl">

Amp، Goose، OpenCode، OpenHands، Roo Code، Kiro، Factory، JetBrains Junie، Letta،
Firebender، Tabnine، Trae، Mistral Vibe، Snowflake Cortex Code، Databricks Genie Code اور
کئی دوسرے ٹولز اِس معیار کو سپورٹ کرتے ہیں۔ اِن میں سے اکثر اِن راستوں میں سے کوئی ایک پڑھتے ہیں:

</div>

```
~/.agents/skills/        # ٹولز کے درمیان ابھرتا ہوا مشترک ضابطہ
~/.claude/skills/        # متبادل کے طور پر وسیع پیمانے پر معاون
<ٹول-مخصوص>/skills/       # مثلاً ~/.gemini/skills/ اور ~/.cursor/skills/
```

<div dir="rtl">

`feynman-technique` فولڈر وہیں رکھیے جہاں آپ کے ٹول کی دستاویز بتاتی ہے۔ کلائنٹس کی مکمل فہرست
[agentskills.io/clients](https://agentskills.io/clients) پر ہے۔

</div>

</details>

<details>
<summary id="any-other-ai-no-skills-support"><b>کوئی اور AI (skills کی سہولت کے بغیر)</b></summary>

<div dir="rtl">

یہ skill سادہ Markdown ہے، اِس لیے کہیں بھی سسٹم پرامپٹ کے طور پر کام کر جاتی ہے۔

- **کسٹم GPT / Gem / Assistant:**
  [`skills/feynman-technique/SKILL.md`](../../skills/feynman-technique/SKILL.md)
  (اوپر والا YAML بلاک ہٹا کر) ہدایات کے خانے میں چسپاں کر دیجیے۔ `references/` کی فائلیں نالج
  فائلوں کے طور پر اپلوڈ کیجیے۔
- **پروجیکٹ / کسٹم ہدایات:** یہی کام، اپنے پروجیکٹ کے کسٹم ہدایات والے خانے میں۔
- **ایک بار کے لیے:** فائل چیٹ میں چسپاں کیجیے اور ساتھ لکھ دیجیے: *”باقی گفتگو میں اِسی پر عمل
  کیجیے۔“*

</div>

</details>

<div dir="rtl">

### جانچیے کہ کام کر رہی ہے

کوئی ایسی چیز پوچھیے جو آپ پہلے ہی اچھی طرح سمجھتے ہوں:

</div>

```
/feynman-technique ہیش فنکشن کیا ہے؟
```

<div dir="rtl">

درست جواب ایک جملے کے خلاصے سے شروع ہوگا، پھر **ایک بھی اصطلاح کے بغیر** سطح ۰ آئے گی، اور آخر
میں ”تصویر کہاں ٹوٹتی ہے“ والا حصہ ہوگا۔ اگر جواب ”ہیش فنکشن ایک ایسا فنکشن ہے جو من مانے حجم
کے ڈیٹا کو…“ سے شروع ہو، تو skill لوڈ نہیں ہوئی۔

---

## آپ کو کیا ملے گا

</div>

```
**ایک جملے میں:** ...          ← تاکہ ماہر یہیں رک سکے

**جو تصویر تھامنی ہے:** ...     ← مرکزی تشبیہ

۰ · گھر کا دسترخوان   شعبے کا کوئی پس منظر نہیں۔ صفر اصطلاحات۔
۱ · نووارد            اصل نام، سطح ۰ کی تصویر سے بندھے ہوئے
۲ · پیشہ ور           حصے کیسے جڑتے ہیں، اور پہلا اصل سمجھوتہ
۳ · سنبھالنے والا     ناکامی کی صورتیں، کیا ٹوٹتا ہے، کیا چھوڑا گیا اور کیوں
۴ · ماہر              کنارے، پیمانہ، اور خود ماڈل کی حدود

تصویر کہاں ٹوٹتی ہے      ← ہر تشبیہ کی حدود، صراحتاً بیان
یہاں آئے نئے الفاظ       ← ہر نئی اصطلاح پر ایک سطر
میں نے کیا چھوڑا         ← نام لے کر بتایا گیا، خاموشی سے نہیں
```

<div dir="rtl">

سطحیں سکڑ سکتی ہیں، غائب نہیں ہوتیں۔ تنگ سوال کو **مختصر صورت** ملتی ہے — خلاصہ، تصویر، اور
وہی ایک سطح جو کام کی ہے۔ کسی ماہر کو زبردستی پانچوں سطحوں سے گزارنا باریک بینی نہیں؛ اِس سے
اُس کی فہم قابلِ پیمائش حد تک *کم* ہو جاتی ہے
([expertise reversal effect](../../skills/feynman-technique/references/evidence.md) — ماہر پر
تفصیل کا اُلٹا اثر)۔

ایک [مکمل حل شدہ مثال](../../skills/feynman-technique/assets/worked-example.md) بھی موجود ہے —
”ڈیٹابیس انڈیکس کیا ہے؟“ کا پورا جواب، اور پھر حاشیوں میں یہ کہ اُس کا ہر حصہ کر کیا رہا ہے۔

---

## کوچ موڈ — جو واقعی سکھاتا ہے

</div>

```
/feynman-technique مجھ سے پوچھیے کہ TCP کنجیشن کیسے سنبھالتا ہے
/feynman-technique میں جانچنا چاہتا ہوں کہ ایونٹ سورسنگ واقعی سمجھ آئی یا نہیں
```

<div dir="rtl">

یہاں skill سمجھانے سے انکار کر دیتی ہے۔ سمجھاتے **آپ** ہیں؛ وہ سنتی ہے — مبہم بات، وہ اصطلاحیں
جو بات آگے بڑھانے کے بجائے اُسے وہیں روک دیتی ہیں، وہ مرحلے جو بتا تو دیے گئے مگر یہ نہیں کہ
چلتے کیسے ہیں — اور ایک وقت میں ٹھیک ایک جھول کی نشان دہی کرتی ہے، جواب ہاتھ میں تھمائے بغیر۔

سب سے مضبوط تحقیق اِسی موڈ کے پیچھے ہے۔ جو لوگ پڑھانے کی تیاری کرتے ہیں، وہ امتحان کی تیاری
کرنے والوں سے بہتر نکلتے ہیں — *تب بھی جب پڑھانے کی نوبت کبھی آتی ہی نہیں*
(Nestojko et al., 2014)۔ اپنی وضاحت خود بنانا، کسی اور کی لکھی وضاحت پڑھنے سے بہتر ہے
(Chi et al., 1989)۔

---

## یہ کن اصولوں پر چلتی ہے

| | عام ”آسان الفاظ میں سمجھاؤ“ والا پرامپٹ | یہ skill |
|---|---|---|
| **اصطلاحات** | جملے آسان، اصطلاحیں وہی | ہر نئی اصطلاح پہلی بار آتے ہی سمجھائی جاتی ہے، ورنہ آتی ہی نہیں |
| **تشبیہات** | ہر پیراگراف میں ایک نیا استعارہ | ایک ہی مرکزی تشبیہ، پیچیدگی بڑھا بڑھا کر آگے لے جائی گئی — **اور یہ بھی کہ وہ کہاں ٹوٹتی ہے** |
| **درستی** | اتنی سادہ کہ غلط ہو جائے | ہر تخمینی بات *اپنی حدود سمیت* نشان زد |
| **گہرائی** | ایک ہی ہموار سطح | ایک سیڑھی، جس کے کسی بھی زینے پر اُتر سکتے ہیں |
| **ماہرین** | اُن سے بھی نوآموز جیسا سلوک | پہلی سطر میں اصل بات، پھر مختصر صورت |
| **نام** | نام *ہی* جواب ہے | پہلے یہ کہ چلتا کیسے ہے، نام سب سے آخر میں |
| **لاعلمی** | ٹال دی جاتی ہے | جہاں سچ ہو، وہاں صاف کہا جاتا ہے: ”کوئی نہیں جانتا“ |
| **سیکھنا** | آپ پر وضاحت اُنڈیل دیتی ہے | کوچ موڈ *آپ سے* سمجھواتا ہے، اور آپ کی سمجھ کے جھول پکڑتا ہے |

صفر نمبر اصول: **واضح ہونا کبھی غلط ہونے کا بہانہ نہیں بن سکتا۔** بات سادہ کرنے سے بگڑتی ہو تو
یہ صاف کہہ دیتی ہے، حدود بتاتی ہے، اور ایک سطح اوپر والا درست بیان ساتھ ہی دے دیتی ہے۔

---

## اندر کیا ہے

skill کی فائلیں انگریزی میں ہیں، تاکہ frontmatter معیاری رہے۔

| فائل | مواد |
|---|---|
| [**SKILL.md**](../../skills/feynman-technique/SKILL.md) | خود skill۔ شروع یہیں سے کیجیے۔ |
| [references/voice.md](../../skills/feynman-technique/references/voice.md) | فائن مین کے اندازِ تحریر کا فرانزک تجزیہ، کارپس کے اعداد و شمار کے ساتھ |
| [references/ladder.md](../../skills/feynman-technique/references/ladder.md) | سطحوں کی درجہ بندی، اور ساخت کو موقعے کے مطابق ڈھالنے کا طریقہ |
| [references/analogies.md](../../skills/feynman-technique/references/analogies.md) | تشبیہ بنانا، بڑھانا اور اُس کی کڑی جانچ کرنا |
| [references/failure-modes.md](../../skills/feynman-technique/references/failure-modes.md) | وضاحتیں جن ۱۴ طریقوں سے ناکام ہوتی ہیں، ہر ایک کے ساتھ دوبارہ تحریر |
| [references/evidence.md](../../skills/feynman-technique/references/evidence.md) | سیکھنے کی سائنس — اور یہ طریقہ واقعی کہاں ناکام ہوتا ہے |
| [references/sources.md](../../skills/feynman-technique/references/sources.md) | تصدیق شدہ اقتباسات، اور وہ جو غلط طور پر اُن سے منسوب ہیں |
| [assets/worked-example.md](../../skills/feynman-technique/assets/worked-example.md) | ایک مکمل جواب، حاشیوں کے ساتھ |
| [assets/checklist.md](../../skills/feynman-technique/assets/checklist.md) | بھیجنے سے پہلے کی جانچ |

### اسلوبی تجزیے کی ایک جھلک

[voice.md](../../skills/feynman-technique/references/voice.md) سے؛ سب کچھ ۸۸٬۰۰۰ الفاظ کے
کارپس پر ماپا گیا:

- **جملوں کی لمبائی کا اُتار چڑھاؤ ہی اُن کی اصل پہچان ہے۔** درمیانی جملہ تقریباً ۲۰ الفاظ کا —
  مگر ہر آٹھ میں سے تقریباً ایک آٹھ الفاظ سے چھوٹا، اور ہر چھ میں سے ایک پینتیس سے لمبا۔ وہ لمبا
  بُنتے ہیں اور چھوٹے جملے پر اُترتے ہیں۔ *"Shake this one, that one shakes later."*
- **ضمیر کام کے مطابق بدلتا ہے۔** پڑھاتے وقت ”we“ (*Six Easy Pieces* میں فی ہزار الفاظ ۱۹٫۹۵
  بار — اُن کے ”I“ سے دس گنا)، اُلجھن مانتے وقت ”I“ (نوبل خطبے میں ۲۶٫۷ فی ہزار)، اور ہدایت
  دیتے وقت ”you“ (*Cargo Cult Science* میں ۲۰٫۶ فی ہزار)۔
- **ایسے افعال جو جسم محسوس کرے۔** *jiggle* ۲۷، *pull* ۳۷، *push* ۲۸، *shake* ۲۰۔ سالمے
  *لرزتے* ہیں؛ وہ ”حرارتی اضطراب کا مظاہرہ“ نہیں کرتے۔
- **”basically“ ۸۸٬۰۰۰ الفاظ میں ایک بار بھی نہیں آیا۔** *trivial* ایک بار آیا۔ skill نے اِن
  الفاظ پر پابندی اِسی لیے لگائی ہے — یہ پیمائش ہے، ذوق نہیں۔

---

## دیانت دار حدود

صفر نمبر اصول اِس صفحے پر بھی لاگو ہوتا ہے۔

- **فائن مین نے ”فائن مین تکنیک“ ایجاد نہیں کی تھی۔** اُنہوں نے اِس نام سے چار مرحلوں کا کوئی
  طریقہ کبھی شائع نہیں کیا۔ یہ چار مرحلے بعد میں آنے والوں نے مرتب کیے، خاص طور پر اسکاٹ ایچ
  ینگ نے ۲۰۱۱ کے آس پاس، اور تشکیلِ نو کے طور پر یہ منصفانہ ہیں۔ اِن کے بجائے یہ skill فائن مین
  کی *دستاویزی* کسوٹیاں استعمال کرتی ہے، اور یہ بات صاف کہہ دیتی ہے۔
- **”اگر آپ کسی بات کو آسانی سے نہیں سمجھا سکتے، تو آپ نے خود بھی نہیں سمجھی“** — اِس جملے کا
  کوئی بنیادی ماخذ نہ فائن مین کے نام سے ملتا ہے، نہ آئن سٹائن کے۔
  [sources.md](../../skills/feynman-technique/references/sources.md) میں درج ہے کہ ثابت شدہ
  طور پر اُنہوں نے کیا کہا اور کیا نہیں کہا۔
- **کچھ چیزیں سادہ ہو ہی نہیں سکتیں۔** خود فائن مین اِس دیوار سے ٹکرائے: اُن کے اپنے والد نے
  پوچھا کہ فوٹون ایٹم کے اندر ہوئے بغیر اُس سے باہر کیسے آ جاتا ہے، تو اُن کا جواب تھا
  *"I'm sorry; I don't know. I can't explain it to you."* یہ skill جھوٹی تصویر گھڑنے کے بجائے
  یہی کہنے کے لیے بنی ہے۔
- **اِس میں ٹوکن بھی خرچ ہوتے ہیں اور وقت بھی۔** جلدی سے کچھ دیکھنا ہو تو مختصر صورت — یا سرے
  سے کوئی skill نہ استعمال کرنا — ہی درست فیصلہ ہے۔
- **رٹنے اور جسمانی مہارتوں میں یہ زیادہ کام نہیں آتی۔** اِس کا ہدف یہ سمجھانا ہے کہ چیزیں کس
  سبب سے اور کس طرح چلتی ہیں۔ ذخیرۂ الفاظ اور کی بورڈ شارٹ کٹس کے لیے وقفے وقفے سے دہرائی
  (spaced retrieval) چاہیے، وضاحت نہیں۔
- **اچھی وضاحت سمجھ آ جانے جیسی *محسوس* ہوتی ہے۔** یہ احساس ثبوت نہیں۔ جہاں معاملہ اہم ہو،
  وہاں کوچ موڈ استعمال کیجیے۔

---

## کریڈٹ اور حقوقِ اشاعت

رچرڈ پی فائن مین (۱۹۱۸–۱۹۸۸) نے وہ سب کچھ لکھا جو یہاں پڑھنے کے لائق ہے۔ اِس ریپازٹری میں
**اُن سے اخذ کیے گئے اصول اور حوالے کے ساتھ مختصر اقتباسات** ہیں، جو تجزیے اور تدریس کے لیے
رکھے گئے ہیں — یہ اُن کی تحریریں دوبارہ شائع نہیں کرتی۔

اُن کی تحریریں اب بھی حقوقِ اشاعت میں محفوظ ہیں: *The Feynman Lectures on Physics* کو
[feynmanlectures.caltech.edu](https://www.feynmanlectures.caltech.edu/) پر مفت *پڑھا* جا سکتا
ہے، مگر وہ © Caltech ہے اور **پبلک ڈومین میں نہیں**۔ فورک کریں تو یہی طریقہ برقرار رکھیے:
اقتباس مختصر لیجیے، حوالہ ہمیشہ دیجیے، پورے ابواب کبھی نقل نہ کیجیے۔ پوری اسناد
[sources.md](../../skills/feynman-technique/references/sources.md) میں ہیں۔

یہ skill پہلے `feynman-reply` تھی — [@guicortei](https://github.com/guicortei) کی بنائی ہوئی
پرتگالی زبان کی ایک skill۔ اِسے بنیادی مآخذ سے نئے سرے سے بنایا گیا، سافٹ ویئر سے آگے تک عام
کیا گیا، اور اسلوبی تجزیہ، شواہد کی بنیاد اور کوچ موڈ اِس میں شامل کیے گئے — پھر اِس کا نام
`feynman-technique` رکھ دیا گیا۔

فائن مین اسٹیٹ، Caltech یا Anthropic سے نہ اِس کی کوئی وابستگی ہے، نہ اِسے اُن کی توثیق حاصل ہے۔

## شراکت

بہتری کی ہر کوشش خوش آئند ہے — خاص طور پر:

- دوسرے شعبوں کی حل شدہ مثالیں (طب، قانون، مالیات، حیاتیات)
- حقیقی استعمال میں سامنے آنے والی ناکامی کی صورتیں
- کسی بھی اقتباس یا انتساب کی تصحیح

[CONTRIBUTING.md](../../CONTRIBUTING.md) دیکھ لیجیے۔ ایک درخواست: فائن مین کے بارے میں کوئی
دعویٰ شامل کریں تو بنیادی ماخذ کا حوالہ ضرور دیجیے۔ علمی دیانت کے لیے اُن کا نام لینا، اور ساتھ
ہی انتساب میں لاپروائی برتنا — اِس ریپازٹری کا واحد ناقابلِ معافی bug یہی ہوگا۔

## لائسنس

[MIT](../../LICENSE)۔ استعمال کیجیے، فورک کیجیے، شائع کیجیے۔

</div>

---

<div align="center">

> *"The first principle is that you must not fool yourself — and you are the easiest person
> to fool."*
> — Richard Feynman, *Cargo Cult Science*, 1974
>
> *”پہلا اصول یہ ہے کہ آپ خود کو دھوکا نہ دیں — اور سب سے آسانی سے دھوکا کھانے والے آپ ہی ہیں۔“*

**[⭐ اِس ریپازٹری کو اسٹار دیجیے](https://github.com/guicortei/feynman-technique)** — اگر آج
اِس نے آپ کو ملنے والا کوئی جواب بدل دیا ہو۔

</div>
