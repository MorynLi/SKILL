<div align="center">

<img src="../../assets/hero.hi.svg" alt="feynman-technique — feynman-technique के बिना: same-origin policy इसे block कर रही है। browser पहले preflight request भेजता है। API की response में CORS headers नहीं हैं। Access-Control-Allow-Origin set नहीं है। इसलिए browser response drop कर देता है। मैं server में CORS middleware add करूँगा। index.js में CORS middleware add करें? — feynman-technique के साथ: आपका code fail नहीं हुआ, browser ने रोका। request वहाँ गई, जवाब भी आ गया। browser ने वो जवाब page को नहीं दिया। वजह: वहाँ आपका login हो सकता है। वरना कोई भी tab उसे पढ़ लेता। API को यह address allow करना था, किया नहीं। वही request Postman में चल जाती है। Postman किसी को नहीं बचाता। browser आपको बचा रहा है। मैं API से यह address allow करवा देता हूँ। API से कहलवा दूँ कि आपका page allowed है?" width="820">

# फ़ाइनमैन तकनीक

### AI ने fix थमा दिया। वह चल भी गया। समझ अब भी नहीं आया कि चला क्यों।

**यह skill उसी "क्यों" के लिए है।**

[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-%E0%A4%96%E0%A5%81%E0%A4%B2%E0%A4%BE%20%E0%A4%AE%E0%A4%BE%E0%A4%A8%E0%A4%95-6b4fbb)](https://agentskills.io)
[![लाइसेंस: MIT](https://img.shields.io/badge/%E0%A4%B2%E0%A4%BE%E0%A4%87%E0%A4%B8%E0%A5%87%E0%A4%82%E0%A4%B8-MIT-blue.svg)](../../LICENSE)
[![Works with](https://img.shields.io/badge/works%20with-Claude%20·%20ChatGPT%20·%20Codex%20·%20Cursor%20·%20Copilot%20·%20Gemini-333)](#इंस्टॉलेशन)

[English](../../README.md) ·
[中文](README.zh-CN.md) ·
**हिन्दी** ·
[Español](README.es.md) ·
[Français](README.fr.md) ·
[العربية](README.ar.md) ·
[বাংলা](README.bn.md) ·
[Português](README.pt-BR.md) ·
[Русский](README.ru.md) ·
[اردو](README.ur.md)

</div>

---

## वही मॉडल। वही सवाल। सेटअप की एक लाइन।

> **"मुझे `Cannot read properties of undefined (reading 'map')` क्यों मिल रहा है?"**

<table>
<tr>
<th width="50%">skill के बिना</th>
<th width="50%">skill के साथ</th>
</tr>
<tr valign="top">
<td>

`.map()` किसी ऐसे reference पर call हो रहा है जो undefined है। आपका component asynchronous fetch के resolve होने से पहले ही render हो जाता है, इसलिए पहले paint के वक़्त state variable अब भी uninitialised रहता है। उसे empty array से initialise कीजिए, या render path पर conditional guard लगा दीजिए।

</td>
<td>

आपने page से कहा था: मेरी चीज़ों की list लो और हर चीज़ के लिए एक पंक्ति बना दो।

पर वह list अभी पहुँची ही नहीं है — वह अब भी server से रास्ते में है। उस पल वहाँ कोई list है ही नहीं, और page उसी ख़ाली जगह से टकराकर गिर जाता है जहाँ list होनी चाहिए थी।

असली list आने तक page के हाथ में एक ख़ाली list थमा दीजिए। अब वह पहले कुछ नहीं बनाता, इंतज़ार करता है, और फिर सब कुछ एक साथ बना देता है।

</td>
</tr>
<tr valign="top">
<td>

छह शब्द, जो आपको पहले से आने चाहिए थे। जवाब सही है, और तस्वीर फिर भी नहीं बनती।

</td>
<td>

पहले से जानना ज़रूरी हो, ऐसा एक भी शब्द नहीं। और आपको पता है कि बदलनी कौन-सी लाइन है, और उसके बाद होगा क्या।

</td>
</tr>
</table>

दोनों जवाब सच हैं। व्याख्या उनमें से सिर्फ़ एक थी।

---

## यह कहाँ से आया

फ़ाइनमैन के पिता ने उन्हें एक चिड़िया दिखाई और कहा कि इसका नाम तुम दुनिया की हर भाषा में सीख
सकते हो, और फिर भी **उस चिड़िया के बारे में कुछ भी नहीं जानोगे**। पता बस इतना होगा कि लोग उसे
क्या कहते हैं। चिड़िया को जानना हो, तो देखिए कि वह करती क्या है।

> "There is a difference between the name of the thing and what goes on."
> — Richard Feynman, *What Is Science?*, 1966
>
> *"चीज़ के नाम में और जो असल में हो रहा है, उसमें फ़र्क़ होता है।"*

पूरी बात बस इतनी है, और यहीं ज़्यादातर AI अपने-आप मात खा जाते हैं। पूछिए कि कोई चीज़ है क्या, और
जवाब में वही नाम कुछ भारी शब्दों में लौट आता है। "यह race condition है।" "यह connection pooling
इस्तेमाल करता है।" आप सिर हिला देते हैं। पहुँचा कुछ भी नहीं। यह skill मॉडल से पहले
**मैकेनिज़्म** कहलवाता है और नाम सबसे आख़िर में — ठीक जैसे फ़ाइनमैन कहा करते थे।

यह मूल स्रोतों से बना है, फ़ाइनमैन पर लिखे ब्लॉग लेखों से नहीं। तरीक़ा और गद्य-शैली, दोनों निकालने
के लिए उनके अपने लिखे लगभग **88,000 शब्दों** का विश्लेषण किया गया: *Six Easy Pieces*, 1965 का
नोबेल व्याख्यान, *Cargo Cult Science*, *What Is Science?*, *There's Plenty of Room at the
Bottom*, और *Surely You're Joking, Mr. Feynman!* का ब्राज़ील वाला अध्याय।

**रिपॉज़िटरी अंग्रेज़ी में है। जवाब नहीं** — आप जिस भाषा में लिखेंगे, skill उसी भाषा में जवाब देगा।

---

## चार कसौटियाँ, जो यह लगाता है

प्रचलित "बारह साल के बच्चे को समझाओ" वाला संस्करण नहीं। ये फ़ाइनमैन की अपनी कसौटियाँ हैं, और
चारों मूल स्रोतों में दर्ज हैं।

<table>
<tr valign="top"><td width="30%">

**फिर से कहकर देखने की कसौटी**

</td><td>

*"Without using the new word which you have just learned, try to rephrase what you have just learned in your own language."* (1966)

*"अभी-अभी सीखे हुए नए शब्द का इस्तेमाल किए बिना, जो सीखा है उसे अपनी ही भाषा में दोबारा कहकर देखिए।"*

उस शब्द पर उँगली रखकर उसे ढक दीजिए। उसके बिना वाक्य ढह जाए, तो आपने परिभाषा लिखी थी, व्याख्या नहीं।

</td></tr>
<tr valign="top"><td>

**ट्राइबोल्यूमिनसेंस की कसौटी**

</td><td>

फ़ाइनमैन ने एक पाठ्यपुस्तक जहाँ से खुली, वहीं से पढ़ा: *"Triboluminescence is the light emitted when crystals are crushed."* — *"ट्राइबोल्यूमिनसेंस वह प्रकाश है जो क्रिस्टलों को कुचलने पर निकलता है।"* उनका फ़ैसला — आपने सिर्फ़ इतना बताया है कि एक शब्द का मतलब कुछ दूसरे शब्दों में क्या होता है।

उनका अपना लिखा हुआ रूप: *"When you take a lump of sugar and crush it with a pair of pliers in the dark, you can see a bluish flash. Some other crystals do that too. Nobody knows why. The phenomenon is called 'triboluminescence.'"* — *"अँधेरे में चीनी की एक डली लेकर उसे pliers से कुचलिए, तो आपको नीली-सी एक चमक दिखेगी। कुछ और क्रिस्टल भी ऐसा ही करते हैं। क्यों करते हैं, यह कोई नहीं जानता। इस घटना का नाम है 'ट्राइबोल्यूमिनसेंस'।"*

जो आप ख़ुद करके देख सकें → आपको दिखेगा क्या → अज्ञान की ईमानदार स्वीकृति → **और तब** नाम।

</td></tr>
<tr valign="top"><td>

**"पानी को देखो" वाली कसौटी**

</td><td>

ब्राज़ील में उनके विद्यार्थी ब्रूस्टर कोण की परिभाषा हूबहू सुना देते थे। जब कहा गया कि खिड़की के बाहर वाली खाड़ी की तरफ़ पोलेरॉइड करके देखो, वे वहीं ठिठक गए।

जिस व्याख्या तक सिर्फ़ उसके कीवर्ड से पहुँचा जा सके, असल हालात में उस तक आप कभी नहीं पहुँचेंगे।

</td></tr>
<tr valign="top"><td>

**कार्गो कल्ट की कसौटी**

</td><td>

पढ़ लेने के बाद आप असल में ऐसा क्या *कर* सकते हैं जो पहले नहीं कर सकते थे? रूप सही और पीछे कुछ नहीं — यानी जहाज़ नहीं उतरते।

</td></tr>
</table>

---

## इंस्टॉलेशन

एक फ़ोल्डर, बस इतना ही। [Agent Skills के खुले मानक](https://agentskills.io) पर चलने वाले हर टूल
में यह काम करता है।

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/feynman-technique
mkdir -p ~/.claude/skills
cp -r /tmp/feynman-technique/skills/feynman-technique ~/.claude/skills/
```

यह हुआ Claude Code। अब बस पूछिए:

```
/feynman-technique समझाइए कि डेटाबेस इंडेक्स कैसे काम करते हैं
```

<details>
<summary><b>Claude Code</b> — प्रोजेक्ट के स्तर पर, टीम के साथ साझा</summary>

```bash
mkdir -p .claude/skills
cp -r /tmp/feynman-technique/skills/feynman-technique .claude/skills/
```

इसे commit कर दीजिए, और रिपॉज़िटरी पर काम करने वाले हर व्यक्ति को यह मिल जाएगा। लोड हुआ या नहीं,
यह `/doctor` चलाकर देख लीजिए।

</details>

<details>
<summary><b>या स्क्रिप्ट से</b> — ताकि आपकी कॉपी पुरानी न पड़ती रहे</summary>

```bash
./install.sh              # निजी, Claude Code के लिए
./install.sh --project    # इसी रिपॉज़िटरी में, टीम के लिए
./install.sh --all        # इस मशीन पर मौजूद हर टूल की डायरेक्टरी में
./install.sh --check      # बताता है कि कौन-सी कॉपी पीछे छूट गई है, बदलता कुछ नहीं
```

याद रखने लायक़ `--check` ही है। इंस्टॉल किया हुआ skill एक *कॉपी* है; वह रिपॉज़िटरी के पीछे-पीछे
नहीं चलती। pull कीजिए, `--check` चलाइए, और जो कॉपी अब मेल नहीं खाती, वह नाम लेकर बता दी जाएगी —
वरना यह बात हफ़्तों बाद ऐसे जवाब से पता चलती है, जो कब का ठीक हो चुका होना चाहिए था।

</details>

<details>
<summary><b>Claude.ai</b> (वेब और डेस्कटॉप ऐप)</summary>

इसके लिए **Pro, Max, Team या Enterprise** प्लान चाहिए, जिसमें कोड एक्ज़ीक्यूशन चालू हो।

1. यह रिपॉज़िटरी डाउनलोड कीजिए ([**ZIP**](https://github.com/guicortei/feynman-technique/archive/refs/heads/main.zip))।
2. `skills/feynman-technique` **फ़ोल्डर को ही** ज़िप कीजिए, ताकि `SKILL.md` ज़िप के रूट में रहे:
   ```bash
   cd skills && zip -r feynman-technique.zip feynman-technique
   ```
3. Claude में **Settings → Capabilities → Skills** में जाइए (कुछ प्लान में यह *Features*
   दिखता है) और **Upload skill** चुनिए।
4. `feynman-technique.zip` चुनिए।

आप जब भी कुछ समझाने को कहेंगे, Claude इसे अपने आप लगा लेगा; नाम लेकर भी बुला सकते हैं।

> claude.ai पर कस्टम skills हर उपयोगकर्ता के अपने होते हैं — टीम के हर सदस्य को अपनी कॉपी ख़ुद
> अपलोड करनी होगी।

</details>

<details>
<summary><b>ChatGPT</b> (डेस्कटॉप ऐप)</summary>

1. यह रिपॉज़िटरी डाउनलोड करके अनज़िप कीजिए।
2. ChatGPT डेस्कटॉप ऐप खोलिए और साइडबार में **Skills** चुनिए।
3. `feynman-technique` फ़ोल्डर जोड़िए।
4. बातचीत में `@` टाइप कीजिए और सूची में से इसे चुन लीजिए।

**आपके प्लान में skills का सपोर्ट नहीं है?** नीचे
[कोई भी अन्य AI](#कोई-भी-अन्य-ai-skills-समर्थन-के-बिना) वाला रास्ता अपनाइए — यह सादे ChatGPT
में, कस्टम GPT में और Projects में चलता है।

</details>

<details>
<summary><b>OpenAI Codex CLI</b></summary>

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/feynman-technique
mkdir -p ~/.agents/skills
cp -r /tmp/feynman-technique/skills/feynman-technique ~/.agents/skills/
```

प्रोजेक्ट के स्तर पर चाहिए तो: अपनी रिपॉज़िटरी के रूट में `.agents/skills/` में कॉपी कीजिए।

`$feynman-technique` से बुलाइए, या `/skills` चलाकर देखिए कि क्या-क्या उपलब्ध है।

</details>

<details>
<summary><b>Cursor</b></summary>

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/feynman-technique
mkdir -p ~/.cursor/skills
cp -r /tmp/feynman-technique/skills/feynman-technique ~/.cursor/skills/
```

प्रोजेक्ट के स्तर पर: रिपॉज़िटरी में `.cursor/skills/` या `.agents/skills/`।
Cursor `~/.claude/skills/` भी पढ़ता है, इसलिए Claude Code में इंस्टॉल कर चुके हैं तो काम पहले ही
हो चुका है।

Agent चैट में `/` टाइप कीजिए और **feynman-technique** चुनिए।

</details>

<details>
<summary><b>VS Code / GitHub Copilot</b></summary>

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/feynman-technique
mkdir -p ~/.copilot/skills
cp -r /tmp/feynman-technique/skills/feynman-technique ~/.copilot/skills/
```

वर्कस्पेस के स्तर पर: `.github/skills/` या `.agents/skills/`।

Copilot Chat में `/` टाइप करके skill चुनिए। उसके बाद संदर्भ भी जोड़ सकते हैं:
`/feynman-technique इस रिपॉज़िटरी का ऑथ मिडलवेयर`।

</details>

<details>
<summary><b>Gemini CLI</b></summary>

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/feynman-technique
mkdir -p ~/.gemini/skills
cp -r /tmp/feynman-technique/skills/feynman-technique ~/.gemini/skills/
```

प्रोजेक्ट के स्तर पर: `.gemini/skills/` या `.agents/skills/`।
Gemini CLI कोई skill चालू करने से पहले आपसे पूछ लेता है।

</details>

<details>
<summary><b>अन्य समर्थित टूल</b></summary>

Amp, Goose, OpenCode, OpenHands, Roo Code, Kiro, Factory, JetBrains Junie, Letta,
Firebender, Tabnine, Trae, Mistral Vibe, Snowflake Cortex Code, Databricks Genie Code और
बाक़ी कई टूल इसी मानक पर चलते हैं।

ज़्यादातर टूल इनमें से कोई एक जगह पढ़ते हैं, मोटे तौर पर प्रचलन के क्रम में:

```
~/.agents/skills/        # टूलों के बीच उभरती साझा परिपाटी
~/.claude/skills/        # विकल्प के रूप में व्यापक रूप से समर्थित
<टूल-विशिष्ट>/skills/     # जैसे ~/.gemini/skills/, ~/.cursor/skills/
```

`feynman-technique` फ़ोल्डर वहीं रख दीजिए जहाँ आपके टूल का दस्तावेज़ कहता है। क्लाइंट्स की पूरी
सूची [agentskills.io/clients](https://agentskills.io/clients) पर है।

</details>

<details>
<summary id="कोई-भी-अन्य-ai-skills-समर्थन-के-बिना"><b>कोई भी अन्य AI (skills समर्थन के बिना)</b></summary>

यह skill सादा Markdown है, इसलिए सिस्टम प्रॉम्प्ट की तरह कहीं भी काम कर जाता है।

- **कस्टम GPT / Gem / Assistant:**
  [`skills/feynman-technique/SKILL.md`](../../skills/feynman-technique/SKILL.md)
  को (ऊपर का YAML ब्लॉक हटाकर) निर्देश वाले फ़ील्ड में चिपका दीजिए। `references/` की फ़ाइलें
  नॉलेज फ़ाइल के तौर पर अपलोड कीजिए।
- **प्रोजेक्ट / कस्टम निर्देश:** यही सब, अपने प्रोजेक्ट के कस्टम-निर्देश बॉक्स में।
- **एक बार के लिए:** फ़ाइल चैट में चिपकाकर लिख दीजिए — *"हमारी बाक़ी बातचीत में इसी का पालन
  कीजिए।"*

</details>

### जाँच लीजिए कि यह काम कर रहा है

कुछ ऐसा पूछिए जो आप पहले से अच्छी तरह जानते हों:

```
/feynman-technique हैश फ़ंक्शन क्या है?
```

सही जवाब एक वाक्य के सार से शुरू होगा, फिर स्तर 0 आएगा जिसमें **एक भी तकनीकी शब्द नहीं** होगा,
और आख़िर में "तस्वीर कहाँ टूटती है" वाला खंड। अगर जवाब "हैश फ़ंक्शन एक ऐसा फ़ंक्शन है जो मनमाने
आकार के डेटा को…" से शुरू हो, तो skill लोड ही नहीं हुआ।

---

## जवाब में क्या मिलता है

```
**एक वाक्य में:** ...        ← ताकि विशेषज्ञ यहीं रुक सके

**थामे रखने वाली तस्वीर:** ...  ← मुख्य उपमा

0 · चाय की दुकान   क्षेत्र की कोई पृष्ठभूमि नहीं। शून्य पारिभाषिक शब्द।
1 · नवागंतुक        असली नाम, स्तर 0 की तस्वीर से बँधे हुए
2 · पेशेवर          हिस्से कैसे जुड़ते हैं, और पहला असली समझौता
3 · संभालने वाला    विफलता के तरीक़े, क्या टूटता है, क्या छोड़ा गया और क्यों
4 · विशेषज्ञ        किनारे, पैमाना, और स्वयं मॉडल की सीमाएँ

तस्वीर कहाँ टूटती है      ← हर उपमा की सीमाएँ, स्पष्ट रूप से बताई गईं
यहाँ आए नए शब्द          ← हर नए शब्द पर एक पंक्ति
मैंने क्या छोड़ा           ← नाम लेकर बताया गया, चुपचाप नहीं
```

स्तर सिकुड़ते हैं, ग़ायब कभी नहीं होते। सीमित दायरे के सवाल पर **संक्षिप्त रूप** मिलता है — सार,
तस्वीर, और वही एक स्तर जो मायने रखता है। किसी विशेषज्ञ को पाँचों स्तरों से गुज़ारना गहनता नहीं है;
इससे उसकी समझ उलटे *घटती* है, और यह नापा जा चुका है (
[expertise reversal effect](../../skills/feynman-technique/references/evidence.md))।

एक [पूरा हल किया हुआ उदाहरण](../../skills/feynman-technique/assets/worked-example.md) देखिए —
"डेटाबेस इंडेक्स क्या है?" का पूरा जवाब, और उसके बाद टिप्पणियाँ, जो दिखाती हैं कि हर हिस्सा कर
क्या रहा है।

---

## कोच मोड — जो सचमुच सिखाता है

```
/feynman-technique मुझसे पूछिए कि TCP कंजेशन कैसे संभालता है
/feynman-technique मैं जाँचना चाहता हूँ कि इवेंट सोर्सिंग सचमुच समझ आया या नहीं
```

यहाँ skill समझाने से साफ़ मना कर देता है। समझाते **आप** हैं; वह सुनता रहता है — कहाँ बात गोल-मोल
है, कौन-सा तकनीकी शब्द सोच रोकने के लिए रखा गया है, कौन-सा क़दम बिना मैकेनिज़्म बताए मान लिया गया
है — और एक बार में ठीक एक छेद पर उँगली रखता है, जवाब थमाए बिना।

शोध की सबसे मज़बूत बुनियाद इसी मोड के पीछे है। जो लोग पढ़ाने की तैयारी करते हैं, वे परीक्षा की
तैयारी करने वालों से आगे निकल जाते हैं — *तब भी, जब पढ़ाने की नौबत कभी आती ही नहीं* (Nestojko et
al., 2014)। अपनी व्याख्या ख़ुद गढ़ना, किसी और की पढ़ लेने से बेहतर पड़ता है (Chi et al., 1989)।

---

## जिन नियमों पर यह चलता है

| | आम "आसान भाषा में समझाओ" प्रॉम्प्ट | यह skill |
|---|---|---|
| **जार्गन** | वाक्य आसान, शब्द वही | हर नया शब्द पहली बार आते ही समझाया जाता है, वरना वह आता ही नहीं |
| **उपमाएँ** | हर पैराग्राफ़ में नया रूपक | एक मुख्य उपमा, जिसे उलझनें जोड़-जोड़कर आगे बढ़ाया जाता है — **और वह कहाँ टूटती है** |
| **सटीकता** | इतना सरल कि ग़लत हो जाए | हर मोटे अनुमान पर *उसकी सीमा भी दर्ज* |
| **गहराई** | एक ही सपाट स्तर | एक सीढ़ी, जिससे आप किसी भी पायदान पर उतर सकते हैं |
| **विशेषज्ञ** | उन्हें बच्चा समझकर समझाया जाता है | पहली पंक्ति में सार, फिर संक्षिप्त रूप |
| **नाम** | नाम *ही* जवाब है | पहले मैकेनिज़्म, नाम सबसे आख़िर में |
| **अज्ञान** | टाल दिया जाता है | जहाँ सच हो, वहाँ "कोई नहीं जानता" साफ़ कहा जाता है |
| **सीखना** | आप पर व्याख्या उड़ेल देता है | कोच मोड *आपसे* समझवाता है, और आपकी समझ के छेद ढूँढ़ निकालता है |

नियम शून्य: **साफ़ कहना कभी भी ग़लत होने का बहाना नहीं बनता।** सरल करने से बात बिगड़ती हो, तो
skill यह कह देता है, सीमा बता देता है, और एक पायदान ऊपर वाला सटीक रूप भी साथ ही दे देता है।

---

## भीतर क्या है

skill की फ़ाइलें अंग्रेज़ी में हैं, ताकि frontmatter मानक के मुताबिक़ रहे।

| फ़ाइल | इसमें क्या है |
|---|---|
| [**SKILL.md**](../../skills/feynman-technique/SKILL.md) | skill ख़ुद। शुरुआत यहीं से कीजिए। |
| [references/voice.md](../../skills/feynman-technique/references/voice.md) | फ़ाइनमैन की गद्य-शैली का फ़ोरेंसिक विश्लेषण, कॉर्पस के आँकड़ों समेत |
| [references/ladder.md](../../skills/feynman-technique/references/ladder.md) | स्तर कैसे तय करें, और ढाँचे को कैसे ढालें |
| [references/analogies.md](../../skills/feynman-technique/references/analogies.md) | उपमाएँ गढ़ना, बढ़ाना और उन्हें तोड़-तोड़कर परखना |
| [references/failure-modes.md](../../skills/feynman-technique/references/failure-modes.md) | व्याख्याएँ जिन 14 तरीक़ों से नाकाम होती हैं, हर एक के साथ सुधरा हुआ रूप |
| [references/evidence.md](../../skills/feynman-technique/references/evidence.md) | सीखने का विज्ञान — और यह तरीक़ा सचमुच कहाँ नाकाम रहता है |
| [references/sources.md](../../skills/feynman-technique/references/sources.md) | प्रमाणित उद्धरण, और वे जो ग़लती से उनके नाम चढ़ा दिए जाते हैं |
| [assets/worked-example.md](../../skills/feynman-technique/assets/worked-example.md) | एक पूरा जवाब, टिप्पणियों समेत |
| [assets/checklist.md](../../skills/feynman-technique/assets/checklist.md) | भेजने से पहले की जाँच |

### शैली-फ़ोरेंसिक की एक झलक

[voice.md](../../skills/feynman-technique/references/voice.md) से; सब कुछ 88,000 शब्दों के
कॉर्पस पर नापा हुआ:

- **वाक्य-लंबाई का तीखा उतार-चढ़ाव ही उनकी पहचान है।** वाक्य की माध्यिका लगभग 20 शब्द — पर हर
  आठ में से क़रीब एक वाक्य आठ शब्दों से छोटा, और हर छह में से क़रीब एक पैंतीस से लंबा। वे बुनते
  लंबा हैं और उतरते छोटे पर हैं। *"Shake this one, that one shakes later."*
- **सर्वनाम काम के हिसाब से बदलते हैं।** पढ़ाते समय "we" (*Six Easy Pieces* में प्रति 1,000
  शब्द 19.95 बार — अपने "I" से दस गुना), उलझन क़बूलते समय "I" (नोबेल व्याख्यान में 26.7/1k),
  निर्देश देते समय "you" (*Cargo Cult Science* में 20.6/1k)।
- **ऐसी क्रियाएँ जिन्हें शरीर महसूस कर सके।** *jiggle* 27, *pull* 37, *push* 28, *shake* 20।
  अणु *थरथराते* हैं; वे "तापीय क्षोभ प्रदर्शित" नहीं करते।
- **88,000 शब्दों में "Basically" एक बार भी नहीं आता।** *Trivial* सिर्फ़ एक बार। इसीलिए skill
  इन शब्दों पर रोक लगाता है — यह माप है, पसंद-नापसंद नहीं।

---

## ईमानदार सीमाएँ

नियम शून्य इस पन्ने पर भी उतना ही लागू है।

- **फ़ाइनमैन ने "फ़ाइनमैन तकनीक" ईजाद नहीं की।** उन्होंने इस नाम से चार चरणों वाली कोई विधि कभी
  प्रकाशित नहीं की। ये चार चरण बाद में उन्हें लोकप्रिय बनाने वालों ने जोड़े — ख़ासकर स्कॉट एच.
  यंग ने, लगभग 2011 में — और पुनर्रचना के तौर पर वे वाजिब हैं। यह skill उनकी जगह वे कसौटियाँ
  लगाता है जो *दस्तावेज़ों में दर्ज* हैं, और यह बात साफ़ कहता है।
- **"अगर आप इसे सरलता से नहीं समझा सकते, तो आपने समझा ही नहीं"** — इसका कोई मूल स्रोत न फ़ाइनमैन
  के नाम मिलता है, न आइंस्टाइन के।
  [sources.md](../../skills/feynman-technique/references/sources.md) में दर्ज है कि उन्होंने
  प्रमाणित रूप से क्या कहा और क्या नहीं।
- **कुछ चीज़ें सरल की ही नहीं जा सकतीं।** ख़ुद फ़ाइनमैन इस दीवार से टकराए थे: उनके अपने पिता ने
  पूछा कि फ़ोटॉन परमाणु के भीतर हुए बिना उसमें से बाहर कैसे आ जाता है, तो उन्होंने कहा *"I'm
  sorry; I don't know. I can't explain it to you."* यह skill झूठी तस्वीर गढ़ने के बजाय यही कहने
  के लिए बना है।
- **इसमें token और समय ख़र्च होता है।** झटपट कुछ देख भर लेना हो, तो संक्षिप्त रूप — या कोई skill
  न लगाना — ही सही फ़ैसला है।
- **रटने या शारीरिक कौशल में यह ज़्यादा काम नहीं आता।** इसका निशाना कारण और मैकेनिज़्म की समझ है।
  शब्दावली और कीबोर्ड शॉर्टकट के लिए अंतराल पर दोहराकर याद करना चाहिए, व्याख्या नहीं।
- **अच्छी व्याख्या समझ जैसी *महसूस* होती है।** वह एहसास कोई सबूत नहीं है। जहाँ बात अहम हो, वहाँ
  कोच मोड इस्तेमाल कीजिए।

---

## श्रेय और कॉपीराइट

रिचर्ड पी. फ़ाइनमैन (1918–1988) ने वह सब लिखा जो यहाँ पढ़ने लायक़ है। इस रिपॉज़िटरी में उनके काम
से **निकाले गए नियम और स्रोत-सहित छोटे उद्धरण** हैं, जो विश्लेषण और शिक्षण के लिए हैं — यह उनकी
रचनाएँ दोबारा नहीं बाँटती।

उनकी रचनाएँ आज भी कॉपीराइट में हैं: *The Feynman Lectures on Physics*
[feynmanlectures.caltech.edu](https://www.feynmanlectures.caltech.edu/) पर मुफ़्त *पढ़ी* जा
सकती हैं, पर वे © Caltech हैं और **पब्लिक डोमेन में नहीं** हैं। इसे fork कीजिए, तो यही तरीक़ा
बनाए रखिए: थोड़ा-सा उद्धृत कीजिए, स्रोत हमेशा दीजिए, अध्याय कभी मत चिपकाइए। पूरा स्रोत-विवरण
[sources.md](../../skills/feynman-technique/references/sources.md) में है।

यह skill `feynman-reply` के नाम से शुरू हुआ था — [@guicortei](https://github.com/guicortei) का
बनाया, पुर्तगाली भाषा का एक skill। इसे मूल स्रोतों से दोबारा बनाया गया, सॉफ़्टवेयर से आगे बढ़ाकर
हर विषय के लायक़ किया गया, और शैली-विश्लेषण, प्रमाणों के आधार तथा कोच मोड के साथ बढ़ाया गया —
फिर नाम `feynman-technique` रखा गया।

फ़ाइनमैन एस्टेट, Caltech या Anthropic से न इसका कोई संबंध है, न इनका कोई अनुमोदन।

## योगदान

सुधारों का स्वागत है — ख़ासकर इनका:

- दूसरे क्षेत्रों के हल किए हुए उदाहरण (चिकित्सा, क़ानून, वित्त, जीवविज्ञान)
- असल इस्तेमाल में मिले, व्याख्या के नाकाम होने के तरीक़े
- किसी भी उद्धरण या श्रेय में सुधार

[CONTRIBUTING.md](../../CONTRIBUTING.md) देखिए। एक गुज़ारिश: फ़ाइनमैन के बारे में कोई दावा
जोड़िए, तो मूल स्रोत भी दीजिए। बौद्धिक ईमानदारी के नाम पर उन्हीं का हवाला देते हुए श्रेय देने में
लापरवाही करना — इस रिपॉज़िटरी का यही एकमात्र अक्षम्य bug होगा।

## लाइसेंस

[MIT](../../LICENSE)। इस्तेमाल कीजिए, fork कीजिए, ship कर दीजिए।

---

<div align="center">

> *"The first principle is that you must not fool yourself — and you are the easiest person
> to fool."*
> — Richard Feynman, *Cargo Cult Science*, 1974
>
> *"पहला सिद्धांत यह है कि आपको ख़ुद को धोखा नहीं देना चाहिए — और सबसे आसानी से धोखा खाने वाले
> व्यक्ति आप ही हैं।"*

आज इसने आपको मिला कोई जवाब बदल दिया हो, तो
**[⭐ इस रिपॉज़िटरी को स्टार दीजिए](https://github.com/guicortei/feynman-technique)**।

</div>
