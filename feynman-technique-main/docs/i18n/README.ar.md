<div align="center">

<img src="../../assets/hero.ar.svg" alt="feynman-technique — بلا feynman-technique: يفشل الطلب بسبب سياسة المصدر نفسه (CORS). يُرسل المتصفّح طلبًا مبدئيًا من نوع OPTIONS. ولا يردّ الخادم بترويسة الاستجابة المطلوبة. والترويسة هي Access-Control-Allow-Origin. فيُسقط المتصفّح الاستجابة قبل وصولها للصفحة. أقترح إضافة وسيط (middleware) لمعالجة CORS. وضبطه ليضيف الترويسة إلى كل استجابة. هل أضيف middleware الـCORS وأضبط الترويسة؟ — مع feynman-technique: لم تفشل شيفرتك، بل المتصفّح هو من أوقفها. خرج الطلب، وردّ الموقع، فحجب المتصفّح ردّه عنك. فبقيت الصفحة فارغة رغم وصول البيانات. فقد تكون مسجّلًا هناك بحسابك، ولولا المنع لقرأ بياناتك أي تبويب مفتوح. وكان على الموقع أن يذكر عنوانك في ردّه، ولم يفعل. ينجح الطلب نفسه في Postman، ويفشل في المتصفّح. فـPostman لا يحمي أحدًا، أما المتصفّح فيحميك أنت. أقترح تعديل الخادم ليعلن أنّ عنوانك مسموح. فيسمح المتصفّح عندها بتسليم الردّ لصفحتك. هل أجعل الموقع يذكر عنوانك في ردّه؟" width="820">

# طريقة فاينمان

### أعطاك الذكاء الاصطناعي حلًّا، فلصقتَه فاشتغل، وما زلتَ لا تدري لماذا.

**وهذه المهارة تتكفّل بالشقّ الثاني.**

[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-%D9%85%D8%B9%D9%8A%D8%A7%D8%B1%20%D9%85%D9%81%D8%AA%D9%88%D8%AD-6b4fbb)](https://agentskills.io)
[![الرخصة: MIT](https://img.shields.io/badge/%D8%A7%D9%84%D8%B1%D8%AE%D8%B5%D8%A9-MIT-blue.svg)](../../LICENSE)
[![Works with](https://img.shields.io/badge/works%20with-Claude%20·%20ChatGPT%20·%20Codex%20·%20Cursor%20·%20Copilot%20·%20Gemini-333)](#التثبيت)

[English](../../README.md) ·
[中文](README.zh-CN.md) ·
[हिन्दी](README.hi.md) ·
[Español](README.es.md) ·
[Français](README.fr.md) ·
**العربية** ·
[বাংলা](README.bn.md) ·
[Português](README.pt-BR.md) ·
[Русский](README.ru.md) ·
[اردو](README.ur.md)

</div>

---

<div dir="rtl">

## النموذج نفسه، والسؤال نفسه، وسطر واحد من الإعداد

> **«لماذا تظهر لي رسالة `Cannot read properties of undefined (reading 'map')`؟»**

</div>

<table dir="rtl">
<tr>
<th width="50%">بلا المهارة</th>
<th width="50%">مع المهارة</th>
</tr>
<tr valign="top">
<td>

<div dir="rtl">

تُستدعى `.map()` على مرجع غير معرَّف. فالمكوّن يُصيَّر قبل أن يُحسم طلب الجلب غير المتزامن، فتبقى
متغيّرة الحالة غير مهيّأة عند أول تصيير. هيّئها مصفوفةً فارغة، أو احرس مسار التصيير بشرط.

</div>

</td>
<td>

<div dir="rtl">

أنت قلت للصفحة: خذي قائمة العناصر عندي، وارسمي سطرًا لكل عنصر فيها.

لكن القائمة لم تصل بعد، فهي ما تزال في طريقها من الخادم. فلا وجود لقائمة أصلًا في تلك اللحظة،
فتتعثّر الصفحة في الفراغ الذي كان ينبغي أن تجد القائمة فيه.

أعطِها قائمة فارغة تمسك بها ريثما تصل الحقيقية، فترسم لا شيء، ثم تنتظر، ثم ترسم كل شيء.

</div>

</td>
</tr>
<tr valign="top">
<td>

<div dir="rtl">

ستة مصطلحات كان عليك أن تعرفها سلفًا. الجواب صحيح، وما زلت عاجزًا عن تصوّر ما يجري.

</div>

</td>
<td>

<div dir="rtl">

صفر مصطلحات. وصرت تعرف أيّ سطر تغيّره، وما الذي تتوقّعه بعده.

</div>

</td>
</tr>
</table>

<div dir="rtl">

الجوابان صحيحان، وواحد منهما فقط كان شرحًا.

---

## من أين جاءت هذه المهارة

عرض والد فاينمان على ريتشارد طائرًا وهو ما يزال طفلًا، وقال له إنك تستطيع أن تحفظ اسم هذا الطائر
بكل لغات الأرض وتظلّ **لا تعرف عن الطائر شيئًا على الإطلاق**؛ فلن تكون قد عرفت إلا ما يسمّيه به
الناس. وإن أردت أن تعرف الطائر فراقب ما يفعله.

> "There is a difference between the name of the thing and what goes on."
> — Richard Feynman, *What Is Science?*, 1966
>
> *«ثمة فرق بين اسم الشيء وبين ما يجري فعلًا.»*

وهذه هي الفكرة كلها، ويسقط فيها معظم أنظمة الذكاء الاصطناعي تلقائيًا: تسأل عن حقيقة شيء فيردّ
عليك باسمه في كلمات أفخم. «هذه race condition.» «إنه يستخدم connection pooling.» فتومئ برأسك،
ولم ينتقل إليك شيء. تجعل هذه المهارة النموذج يقدّم **الآلية أولًا** والاسم أخيرًا، كما كان
يفعل فاينمان.

بُنيت هذه المهارة على مصادر أولية، لا على تدوينات كُتبت عن فاينمان. حُلِّل نحو **٨٨٬٠٠٠ كلمة**
من كتابته هو لاستخراج المنهج والأسلوب معًا: *Six Easy Pieces*، ومحاضرة نوبل ١٩٦٥،
و*Cargo Cult Science*، و*What Is Science?*، و*There's Plenty of Room at the Bottom*، وفصل
البرازيل من *Surely You're Joking, Mr. Feynman!*

**المستودع بالإنجليزية، أما الإجابات فلا** — تردّ المهارة باللغة التي تخاطبها بها.

---

## الاختبارات الأربعة التي تطبّقها

ليست النسخة الشائعة «اشرحها لطفل في الثانية عشرة»، بل هي اختبارات فاينمان نفسه، وكلٌّ منها
يُردّ إلى مصدر أوليّ.

</div>

<table dir="rtl">
<tr valign="top"><td width="30%">

<div dir="rtl">

**اختبار إعادة الصياغة**

</div>

</td><td>

<div dir="rtl">

*"Without using the new word which you have just learned, try to rephrase what you have just learned in your own language."* (١٩٦٦)

*«من دون استعمال الكلمة الجديدة التي تعلّمتها للتو، أعد صياغة ما تعلّمته بلغتك أنت.»*

غطِّ المصطلح بيدك، فإن ماتت الجملة من دونه فأنت كتبت تعريفًا لا شرحًا.

</div>

</td></tr>
<tr valign="top"><td>

<div dir="rtl">

**اختبار التلألؤ الاحتكاكي**

</div>

</td><td>

<div dir="rtl">

فتح فاينمان كتابًا مدرسيًا على صفحة عشوائية فقرأ: *"Triboluminescence is the light emitted when crystals are crushed."* — *«التلألؤ الاحتكاكي هو الضوء المنبعث حين تُسحق البلّورات.»* وحكمه أنك لم تقل شيئًا سوى ما تعنيه كلمةٌ بكلمات أخرى.

ثم أعاد هو صياغتها: *"When you take a lump of sugar and crush it with a pair of pliers in the dark, you can see a bluish flash. Some other crystals do that too. Nobody knows why. The phenomenon is called 'triboluminescence.'"* — *«خذ قطعة سكّر واسحقها بكمّاشة في الظلام، ترَ ومضة تضرب إلى الزرقة. وتفعل ذلك بلّورات أخرى كذلك. ولا أحد يعرف لماذا. وتسمّى هذه الظاهرة "التلألؤ الاحتكاكي".»*

شيء تستطيع أن تفعله بيدك ← ما الذي سترصده ← اعتراف صريح بالجهل ← **ثم** الاسم.

</div>

</td></tr>
<tr valign="top"><td>

<div dir="rtl">

**اختبار «انظر إلى الماء»**

</div>

</td><td>

<div dir="rtl">

كان طلابه البرازيليون يسمّعون زاوية بروستر عن ظهر قلب، فلمّا طُلب منهم أن يوجّهوا مرشِّح استقطاب نحو الخليج الممتدّ خارج النافذة تجمّدوا في أماكنهم.

والشرح الذي لا تبلغه إلا من طريق كلمته المفتاحية شرحٌ لن تبلغه في الحياة أبدًا.

</div>

</td></tr>
<tr valign="top"><td>

<div dir="rtl">

**اختبار عبادة البضائع**

</div>

</td><td>

<div dir="rtl">

بعد القراءة، ما الذي صرتَ تستطيع *فعله* ولم تكن تستطيعه قبلها؟ الشكل الصحيح وليس خلفه شيء يعني أن الطائرات لن تهبط.

</div>

</td></tr>
</table>

<div dir="rtl">

---

## التثبيت

مجلد واحد لا غير. تتبع المهارة [معيار Agent Skills المفتوح](https://agentskills.io)، فتعمل في
أي أداة تدعمه.

</div>

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/feynman-technique
mkdir -p ~/.claude/skills
cp -r /tmp/feynman-technique/skills/feynman-technique ~/.claude/skills/
```

<div dir="rtl">

بهذا صارت المهارة عندك في Claude Code، متاحةً في كل مشاريعك. ثم اطلب ما شئت:

</div>

```
/feynman-technique اشرح كيف تعمل فهارس قواعد البيانات
```

<details>
<summary><b>Claude Code</b> — على مستوى المشروع، بالاشتراك مع فريقك</summary>

```bash
mkdir -p .claude/skills
cp -r /tmp/feynman-technique/skills/feynman-technique .claude/skills/
```

<div dir="rtl">

أدخِلها في الـ commit فتصل إلى كل من يعمل على المستودع. ونفّذ `/doctor` للتأكد من تحميلها.

</div>

</details>

<details>
<summary><b>أو استعمل السكربت</b> — كي لا تتقادم نسختك</summary>

```bash
./install.sh              # تثبيت شخصي، في Claude Code
./install.sh --project    # داخل هذا المستودع، للفريق
./install.sh --all        # كل أدلّة الأدوات الموجودة على هذا الجهاز
./install.sh --check      # يبلّغك أيّ النسخ تخلّف، ولا يغيّر شيئًا
```

<div dir="rtl">

و`--check` هو الخيار الجدير بأن تتذكّره. فالمهارة المثبَّتة *نسخة*، وهي لا تتبع المستودع. اسحب
آخر التحديثات ثم نفّذه، فيسمّي لك كل نسخة لم تعد مطابقة — وإلا اكتشفت الأمر بعد أسابيع، من
إجابة كان ينبغي أن تكون قد صُحّحت.

</div>

</details>

<details>
<summary><b>Claude.ai</b> — على الويب وسطح المكتب</summary>

<div dir="rtl">

تحتاج خطة **Pro أو Max أو Team أو Enterprise** مع تفعيل تنفيذ الشيفرة.

1. نزّل المستودع ([**ZIP**](https://github.com/guicortei/feynman-technique/archive/refs/heads/main.zip)).
2. اضغط **المجلد نفسه** `skills/feynman-technique`، بحيث يقع `SKILL.md` في جذر الأرشيف:

</div>

```bash
cd skills && zip -r feynman-technique.zip feynman-technique
```

<div dir="rtl">

3. في Claude افتح **الإعدادات ← القدرات ← Skills** (تظهر باسم *Features* في بعض الخطط) واختر
   **Upload skill**.
4. اختر الملف `feynman-technique.zip`.

سيستعملها Claude من تلقاء نفسه حين تطلب شرحًا، ويمكنك أيضًا طلبها بالاسم.

المهارات المخصّصة في claude.ai خاصة بكل مستخدم على حدة — على كل زميل أن يرفع نسخته.

</div>

</details>

<details>
<summary><b>ChatGPT</b> — تطبيق سطح المكتب</summary>

<div dir="rtl">

نزّل المستودع وفكّ ضغطه، ثم افتح تطبيق ChatGPT لسطح المكتب، واختر **Skills** من الشريط
الجانبي، وأضف مجلد `feynman-technique`. لاستدعائها في محادثة، اكتب `@` واخترها من القائمة.

**خطتك لا تدعم المهارات؟** انظر [أي ذكاء اصطناعي آخر](#any-other-ai-no-skills-support) أدناه.

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

ولتثبيتها على مستوى المشروع انسخها إلى `.agents/skills/` في جذر المستودع. استدعِها بـ
`$feynman-technique`، أو نفّذ `/skills` لعرض المتاح.

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

وعلى مستوى المشروع: `.cursor/skills/` أو `.agents/skills/`. ويقرأ Cursor أيضًا
`~/.claude/skills/`، فتثبيت Claude Code يغنيك عن ذلك أصلًا. اكتب `/` في محادثة Agent واختر
**feynman-technique**.

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

وعلى مستوى مساحة العمل: `.github/skills/` أو `.agents/skills/`. اكتب `/` في Copilot Chat واختر
المهارة، ويمكنك أن تُلحق بها سياقًا: `/feynman-technique the auth middleware in this repo`.

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

وعلى مستوى المشروع: `.gemini/skills/` أو `.agents/skills/`. ويطلب Gemini CLI موافقتك قبل
تفعيل أي مهارة.

</div>

</details>

<details>
<summary><b>كل ما عداها</b> — Amp، Goose، Kiro، Junie، Roo، Factory، Tabnine…</summary>

<div dir="rtl">

ومعظمها يقرأ أحد هذه المسارات، وترتيبها هنا تقريبي بحسب انتشارها:

</div>

```
~/.agents/skills/        # العُرف الآخذ في الترسّخ بين الأدوات
~/.claude/skills/        # مدعوم على نطاق واسع كبديل
<خاص-بالأداة>/skills/     # مثل ~/.gemini/skills/ و ~/.cursor/skills/
```

<div dir="rtl">

ضع مجلد `feynman-technique` في المسار الذي توثّقه أداتك. وقائمة العملاء كاملةً على
[agentskills.io/clients](https://agentskills.io/clients).

</div>

</details>

<details>
<summary id="any-other-ai-no-skills-support"><b>أي ذكاء اصطناعي آخر</b> — بلا حاجة إلى دعم المهارات</summary>

<div dir="rtl">

المهارة ملف Markdown خالص، فتصلح موجّهَ نظام في أي مكان.

- **GPT مخصّص / Gem / Assistant:** الصق
  [`skills/feynman-technique/SKILL.md`](../../skills/feynman-technique/SKILL.md)
  (بعد حذف كتلة YAML في أعلاه) في حقل التعليمات، وارفع ملفات `references/` كملفات معرفة.
- **مشروع / تعليمات مخصّصة:** الشيء نفسه، في صندوق التعليمات المخصّصة لمشروعك.
- **استعمال لمرة واحدة:** الصق الملف في المحادثة وأضف *«اتبع هذا في بقية حديثنا.»*

</div>

</details>

<div dir="rtl">

### تحقّق من أنها تعمل

اسأل عن شيء تتقنه أصلًا:

</div>

```
/feynman-technique ما دالة التجزئة (hash function)؟
```

<div dir="rtl">

تبدأ الإجابة الصحيحة بخلاصة في جملة واحدة، ثم مستوى ٠ **بلا أي كلمة تقنية**، وتنتهي بقسم «أين
تنهار الصورة». أما إن بدأت بـ«دالة التجزئة هي دالة تحوّل بيانات ذات حجم اعتباطي إلى…» فالمهارة
لم تُحمَّل.

---

## ما الذي تحصل عليه

</div>

```
**في جملة واحدة:** ...        ← ليتمكّن الخبير من التوقف هنا

**الصورة التي تُمسِك بها:** ...  ← التشبيه الرئيسي

٠ · غداء الجمعة          لا خلفية في المجال إطلاقًا. صفر مصطلحات تقنية.
١ · المستجدّ              الأسماء الحقيقية، مربوطةً بصورة المستوى ٠
٢ · الممارس              كيف تتشابك القطع، وأول مقايضة حقيقية
٣ · القائم على الصيانة   أنماط الأعطال، وما ينكسر، وما استُبعد ولماذا
٤ · المتخصص              الحالات الحدّية، والسلوك عند التوسّع، وحدود النموذج نفسه

أين تنهار الصورة        ← حدود كل تشبيه، مذكورةً صراحةً
كلمات جديدة وردت هنا    ← سطر لكل مصطلح
ما الذي أغفلته          ← مذكور بالاسم، لا محذوف بصمت
```

<div dir="rtl">

تنكمش المستويات لكنها لا تختفي أبدًا. والسؤال الضيّق يأخذ **الصيغة المختصرة**: خلاصة، وصورة،
والمستوى الوحيد الذي يهمّ. أما أن تسوق خبيرًا عبر خمسة مستويات فليس شمولًا في الشرح، بل يُضعف
فهمه إضعافًا قابلًا للقياس
([أثر انعكاس الخبرة](../../skills/feynman-technique/references/evidence.md)).

📄 **[انظر إجابةً كاملة، ثم مشروحةً بحواشيها](../../skills/feynman-technique/assets/worked-example.md)**
— سؤال «ما فهرس قاعدة البيانات؟» مُجابًا كما ينبغي، مع بيان وظيفة كل حركة فيه.

---

## وضع المدرّب — الوضع الذي يعلّمك فعلًا

</div>

```
/feynman-technique اختبرني في كيفية معالجة TCP للازدحام
/feynman-technique أريد التحقق مما إذا كنت أفهم event sourcing حقًا
```

<div dir="rtl">

هنا ترفض المهارة أن تشرح. **أنت** من يشرح، وهي تُنصت وتترصّد الغموض، والمصطلحات التقنية
المستعملة محطةَ نهاية بدل الشرح، والخطوات التي تُقرَّر بلا آلية — ثم تضع إصبعها على ثغرة واحدة
بالضبط في كل مرة، من دون أن تسلّمك الجواب.

وهذا الوضع أقوى أوضاع المهارة سندًا في البحث العلمي. فمن يستعدّ للتدريس يتفوّق على من يستعدّ
للاختبار *حتى إن لم يُدرِّس قط* (Nestojko et al., 2014). وأن تصوغ الشرح بنفسك أفضل من أن تقرأ
شرح غيرك (Chi et al., 1989).

---

## القواعد التي تلتزم بها

| | الموجّه المعتاد «اشرح ببساطة» | هذه المهارة |
|---|---|---|
| **المصطلحات** | جمل أبسط، والمصطلحات نفسها | كل مصطلح جديد يُشرح عند أول استعمال، وإلا فلا يظهر |
| **التشبيهات** | استعارة جديدة في كل فقرة | تشبيه رئيسي واحد يتوسّع كلما زاد التعقيد — **مع بيان أين ينهار** |
| **الدقة** | بُسِّط حتى صار خطأ | كل تقريب مذكور *بحدوده* |
| **العمق** | مستوى واحد مسطّح | سُلَّم تنزل منه عند أي درجة |
| **الخبراء** | يُخاطَبون بتعالٍ | الخلاصة في السطر الأول، ثم الصيغة المختصرة |
| **الأسماء** | الاسم *هو* الجواب | الآلية أولًا، والاسم أخيرًا |
| **الجهل** | يُمرَّر مرور الكرام | تُقال «لا أحد يعرف» صراحةً حين تكون صحيحة |
| **التعلّم** | يُلقي عليك الشرح | وضع المدرّب يجعلك *أنت* تشرح، ويكشف ثغرات فهمك |

**القاعدة صفر: الوضوح ليس عذرًا للخطأ أبدًا.** فإن كان التبسيط سيشوّه المعنى، قالت ذلك صراحةً،
وذكرت لك الحدود، وأعطتك الصيغة الدقيقة في المستوى الذي يليه.

---

## ما بداخل المهارة

ملفات المهارة نفسها بالإنجليزية، كي تبقى حقول frontmatter قياسية.

| الملف | المحتوى |
|---|---|
| [**SKILL.md**](../../skills/feynman-technique/SKILL.md) | المهارة نفسها. ابدأ من هنا. |
| [references/voice.md](../../skills/feynman-technique/references/voice.md) | تشريح دقيق لأسلوب فاينمان، مع إحصاءات المدوّنة النصية |
| [references/ladder.md](../../skills/feynman-technique/references/ladder.md) | معايرة المستويات وكيفية تكييف الشكل |
| [references/analogies.md](../../skills/feynman-technique/references/analogies.md) | بناء التشبيهات وتوسيعها واختبار متانتها |
| [references/failure-modes.md](../../skills/feynman-technique/references/failure-modes.md) | ١٤ نمط فشل، مع إعادة صياغة لكل منها |
| [references/evidence.md](../../skills/feynman-technique/references/evidence.md) | علم التعلّم — وأين يفشل هذا المنهج فعلًا |
| [references/sources.md](../../skills/feynman-technique/references/sources.md) | اقتباسات موثّقة، وأخرى تُنسب إليه زورًا |
| [assets/worked-example.md](../../skills/feynman-technique/assets/worked-example.md) | إجابة كاملة مع حواشيها |
| [assets/checklist.md](../../skills/feynman-technique/assets/checklist.md) | مراجعة ما قبل الإرسال |

### عيّنة من هذا التشريح الأسلوبي

من [voice.md](../../skills/feynman-technique/references/voice.md)، وكلها مقيسة على مدوّنة من
٨٨٬٠٠٠ كلمة:

- **التذبذب الحادّ في طول الجملة هو بصمته.** وسيط الجملة نحو ٢٠ كلمة — لكن نحو جملة من كل ثماني
  تقلّ عن ثماني كلمات، وواحدة من كل ست تتجاوز خمسًا وثلاثين. يبني طويلًا ثم يهبط بجملة قصيرة.
  *"Shake this one, that one shakes later."*
- **تتبدّل الضمائر بحسب الوظيفة.** «we» في التدريس (١٩٫٩٥ لكل ألف كلمة في *Six Easy Pieces*،
  أي عشرة أضعاف «I» عنده)، و«I» عند الاعتراف بالحيرة (٢٦٫٧ لكل ألف في محاضرة نوبل)، و«you» عند
  التوجيه (٢٠٫٦ لكل ألف في *Cargo Cult Science*).
- **أفعال يحسّها الجسد.** *jiggle* ٢٧ مرة، *pull* ٣٧، *push* ٢٨، *shake* ٢٠. الجزيئات
  *تهتزّ*، ولا «تُبدي اضطرابًا حراريًا».
- **كلمة «basically» ترد صفر مرة في ٨٨٬٠٠٠ كلمة.** و*trivial* مرة واحدة. لهذا تمنعها
  المهارة — قياسٌ لا ذوق.

---

## حدود صريحة

وتسري القاعدة صفر على هذه الصفحة نفسها.

- **فاينمان لم يخترع «طريقة فاينمان».** فهو لم ينشر قط منهجًا من أربع خطوات بهذا الاسم. ركّب
  الخطواتِ الأربع ناشرو المعرفة من بعده، وعلى رأسهم سكوت هـ. يونغ نحو ٢٠١١، بوصفها إعادة بناء
  منصفة. وتستعمل هذه المهارة اختباراته *الموثّقة* بدلًا منها، وتقول ذلك صراحةً.
- **«إن لم تستطع شرحه ببساطة فأنت لم تفهمه»** عبارة لا مصدر أوليّ لها، لا عند فاينمان ولا عند
  أينشتاين. ويورد [sources.md](../../skills/feynman-technique/references/sources.md) ما ثبت
  أنه قاله وما لم يقله.
- **بعض الأشياء لا تقبل التبسيط.** اصطدم فاينمان نفسه بهذا الجدار: حين سأله والده كيف يخرج
  الفوتون من الذرّة دون أن يكون فيها أصلًا، أجاب *"I'm sorry; I don't know. I can't explain
  it to you."* — *«آسف، لا أعرف. لا أستطيع أن أشرحه لك.»* وقد صُمِّمت المهارة لتقول هذا بدل
  اختلاق صورة زائفة.
- **تكلّف tokens ووقتًا.** فللاستفسار السريع تكون الصيغة المختصرة — أو ترك المهارة جانبًا — هي
  الخيار الصحيح.
- **قليلة النفع في الحفظ والمهارات الحركية.** فهي تستهدف الفهم السببي والآلي. أما المفردات
  واختصارات لوحة المفاتيح فتحتاج استرجاعًا متباعدًا لا شرحًا.
- **الشرح الجيد *يمنحك إحساسًا* بالفهم.** وهذا الإحساس ليس دليلًا. فحين يكون الأمر مهمًا،
  استعمل وضع المدرّب.

---

## الشكر وحقوق النشر

كتب ريتشارد ب. فاينمان (١٩١٨–١٩٨٨) كل ما يستحق القراءة هنا. ويضمّ هذا المستودع **قواعد
مستخلصة واقتباسات قصيرة منسوبة إليه**، للتحليل والتعليم — وهو لا يعيد نشر أعماله.

ولا تزال نصوصه محمية بحقوق النشر: كتاب *The Feynman Lectures on Physics* متاح *للقراءة*
مجانًا على [feynmanlectures.caltech.edu](https://www.feynmanlectures.caltech.edu/)، لكنه
© Caltech و**ليس مُلكًا عامًا**. فإن عملت fork لهذا المستودع فأبقِ الأمر على حاله: اقتبس
قليلًا، وانسب دائمًا، ولا تنقل فصولًا. بيان المصادر كاملًا في
[sources.md](../../skills/feynman-technique/references/sources.md).

بدأت هذه المهارة باسم `feynman-reply`، وهي مهارة بالبرتغالية من إعداد
[@guicortei](https://github.com/guicortei). ثم أُعيد بناؤها من المصادر الأولية، ووُسِّع نطاقها
ليتجاوز البرمجيات، وأُضيف إليها التحليل الأسلوبي والأساس البحثي ووضع المدرّب — ثم صار اسمها
`feynman-technique`.

لا صلة لها بتركة فاينمان ولا بـ Caltech ولا بـ Anthropic، ولا تحمل تأييد أيٍّ منها.

## المساهمة

التحسينات مرحّب بها، وخصوصًا:

- أمثلة محلولة من مجالات أخرى (الطب، القانون، المالية، الأحياء)
- أنماط فشل رُصدت في الاستعمال الفعلي
- تصحيح أي اقتباس أو نسبة

انظر [CONTRIBUTING.md](../../CONTRIBUTING.md). وطلب واحد: إن أضفت كلامًا عن فاينمان فاذكر
مصدره الأولي. فالتساهل في النسبة مع استحضار اسمه للحديث عن الأمانة الفكرية هو الخلل الوحيد
الذي لا يُغتفر في هذا المستودع.

## الرخصة

[MIT](../../LICENSE). استعملها، واعمل لها fork، وأطلقها.

</div>

---

<div align="center">

> *"The first principle is that you must not fool yourself — and you are the easiest person
> to fool."*
> — Richard Feynman, *Cargo Cult Science*, 1974
>
> *«المبدأ الأول ألّا تخدع نفسك — وأنت أسهل الناس انخداعًا.»*

**[⭐ ضع نجمة على المستودع](https://github.com/guicortei/feynman-technique)** إن غيّر إجابةً
وصلتك اليوم.

</div>
