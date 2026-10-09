<div align="center">

<img src="../../assets/hero.fr.svg" alt="feynman-technique — sans feynman-technique: La console indique un blocage CORS sur votre appel. La politique de même origine s&#x27;applique à la requête. L&#x27;en-tête Access-Control-Allow-Origin est absent. La requête préliminaire OPTIONS reste sans réponse. Il faut configurer le middleware CORS de l&#x27;API. Je propose de corriger la configuration CORS de l&#x27;API. J&#x27;ajoute le middleware et l&#x27;en-tête d&#x27;origine ? — avec feynman-technique: Votre code n&#x27;a pas planté : c&#x27;est le navigateur. La requête est partie, la réponse est revenue. Le navigateur l&#x27;a gardée et n&#x27;a rien donné à la page. Vous êtes peut-être connecté sur ce site-là. Sans cette règle, n&#x27;importe quel onglet vous lirait. L&#x27;autre site doit déclarer votre adresse bienvenue. Il ne l&#x27;a jamais fait, alors le navigateur refuse. Dans Postman ça passe, dans le navigateur ça bloque. Postman ne protège personne. Le navigateur, lui, si. Je vais ajouter cette déclaration sur votre serveur. Je fais dire au serveur « cette adresse est OK » ?" width="820">

# Technique de Feynman

### L'IA vous a donné un correctif. Vous l'avez collé, ça passe. Vous ne savez toujours pas pourquoi.

**Ici, on s'occupe du pourquoi.**

[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-standard%20ouvert-6b4fbb)](https://agentskills.io)
[![Licence : MIT](https://img.shields.io/badge/Licence-MIT-blue.svg)](../../LICENSE)
[![Works with](https://img.shields.io/badge/works%20with-Claude%20·%20ChatGPT%20·%20Codex%20·%20Cursor%20·%20Copilot%20·%20Gemini-333)](#installation)
[![Bâti sur](https://img.shields.io/badge/b%C3%A2ti%20sur-88%20000%20mots%20de%20Feynman-c2410c)](#doù-ça-vient)

[English](../../README.md) ·
[中文](README.zh-CN.md) ·
[हिन्दी](README.hi.md) ·
[Español](README.es.md) ·
**Français** ·
[العربية](README.ar.md) ·
[বাংলা](README.bn.md) ·
[Português](README.pt-BR.md) ·
[Русский](README.ru.md) ·
[اردو](README.ur.md)

</div>

---

## Même modèle. Même question. Une ligne d'installation.

> **« Pourquoi j'ai `Cannot read properties of undefined (reading 'map')` ? »**

<table>
<tr>
<th width="50%">Sans le skill</th>
<th width="50%">Avec le skill</th>
</tr>
<tr valign="top">
<td>

`.map()` est appelé sur une référence `undefined`. Votre composant effectue son rendu avant que le fetch asynchrone ne soit résolu : au premier paint, la variable d'état n'est donc pas encore initialisée. Initialisez-la à un tableau vide, ou protégez le rendu par une condition.

</td>
<td>

Vous avez dit à la page : prends ma liste et dessine une ligne pour chaque élément.

Sauf que la liste n'est pas encore arrivée — elle est toujours en route depuis le serveur. À cet instant précis, il n'y a pas de liste du tout, et la page se prend le vide à l'endroit où la liste aurait dû être.

Donnez-lui une liste vide à tenir, le temps que la vraie arrive. Elle ne dessine rien, elle attend, puis elle dessine tout.

</td>
</tr>
<tr valign="top">
<td>

Six termes qu'il fallait déjà connaître. C'est juste, et vous ne voyez toujours pas la scène.

</td>
<td>

Zéro. Et vous savez quelle ligne changer, et ce que ça donnera ensuite.

</td>
</tr>
</table>

Les deux réponses sont vraies. Une seule était une explication.

---

## D'où ça vient

Le père de Feynman lui a montré un oiseau et lui a dit qu'on peut apprendre son nom dans
toutes les langues de la Terre et ne **rien savoir du tout de l'oiseau**. On saurait
seulement comment les gens l'appellent. Pour connaître l'oiseau, il faut regarder ce qu'il
fait.

> "There is a difference between the name of the thing and what goes on."
> — Richard Feynman, *What Is Science?*, 1966
>
> *« Il y a une différence entre le nom de la chose et ce qui se passe. »*

Toute l'idée est là, et presque toutes les IA la ratent par défaut. Demandez ce qu'est une
chose : on vous rend son nom, en mots plus chics. Ce skill oblige le modèle à sortir **le
mécanisme d'abord**, et le nom en dernier — comme le faisait Feynman.

Il est bâti sur des sources primaires, pas sur des billets de blog à propos de Feynman.
Environ **88 000 mots** de ses propres écrits ont été analysés pour en tirer la méthode
autant que le style : *Six Easy Pieces*, la conférence Nobel de 1965, *Cargo Cult Science*,
*What Is Science?*, *There's Plenty of Room at the Bottom* et le chapitre brésilien de
*Surely You're Joking, Mr. Feynman!*

**Le dépôt est en anglais. Les réponses, non** — le skill répond dans la langue que vous
employez pour lui écrire.

---

## Les quatre tests qu'il applique

Pas la version qui circule sur les blogs. Ce sont les tests de Feynman lui-même, chacun
remontant à une source primaire.

<table>
<tr valign="top"><td width="30%">

**Le test de reformulation**

</td><td>

*"Without using the new word which you have just learned, try to rephrase what you have just learned in your own language."* (1966)

*« Sans employer le mot nouveau que vous venez d'apprendre, essayez de reformuler avec vos propres mots ce que vous venez d'apprendre. »*

Cachez le terme. Si la phrase meurt sans lui, c'était une définition, pas une explication.

</td></tr>
<tr valign="top"><td>

**Le test de la triboluminescence**

</td><td>

Feynman a ouvert un manuel au hasard : *"Triboluminescence is the light emitted when crystals are crushed."* — *« La triboluminescence est la lumière émise lorsqu'on écrase des cristaux. »* Son verdict : on a seulement dit ce qu'un mot veut dire au moyen d'autres mots.

Sa réécriture : *"When you take a lump of sugar and crush it with a pair of pliers in the dark, you can see a bluish flash. Some other crystals do that too. Nobody knows why. The phenomenon is called 'triboluminescence.'"* — *« Prenez un morceau de sucre, écrasez-le avec une pince dans le noir : vous verrez un éclair bleuté. D'autres cristaux font ça aussi. Personne ne sait pourquoi. Le phénomène s'appelle la triboluminescence. »*

Quelque chose qu'on peut faire → ce qu'on verrait → l'aveu franc de ce qu'on ignore → **et seulement là**, le nom.

</td></tr>
<tr valign="top"><td>

**Le test « regardez l'eau »**

</td><td>

Ses étudiants brésiliens récitaient l'angle de Brewster sans une faute. Quand on leur a demandé d'orienter un polaroïd vers la baie qu'on voyait par la fenêtre, ils se sont figés.

Une explication qu'on n'atteint que par son mot-clé, on ne la retrouvera jamais dans la vraie vie.

</td></tr>
<tr valign="top"><td>

**Le test du culte du cargo**

</td><td>

Après lecture, que savez-vous *faire* que vous ne saviez pas faire avant ? La forme est juste, il n'y a rien derrière : les avions ne se posent pas.

</td></tr>
</table>

---

## Installation

Un seul dossier à copier. Ça marche dans tout outil qui gère le
[standard ouvert Agent Skills](https://agentskills.io).

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/feynman-technique
mkdir -p ~/.claude/skills
cp -r /tmp/feynman-technique/skills/feynman-technique ~/.claude/skills/
```

Ça, c'est Claude Code. Ensuite, il suffit de demander :

```
/feynman-technique explique comment fonctionnent les index de base de données
```

<details>
<summary><b>Claude Code</b> — par projet, partagé avec l'équipe</summary>

```bash
mkdir -p .claude/skills
cp -r /tmp/feynman-technique/skills/feynman-technique .claude/skills/
```

Versionnez-le et toute l'équipe l'a. Lancez `/doctor` pour vérifier qu'il s'est bien chargé.

</details>

<details>
<summary><b>Ou passez par le script</b> — et gardez votre copie à jour</summary>

```bash
./install.sh              # personnel, Claude Code
./install.sh --project    # dans ce dépôt, pour l'équipe
./install.sh --all        # tous les dossiers d'outils présents sur la machine
./install.sh --check      # signale les copies en retard, sans rien modifier
```

C'est `--check` qui vaut la peine d'être retenu. Un skill installé est une *copie*, et une
copie ne suit pas le dépôt. Faites un `git pull`, lancez `--check`, et il vous nomme toute
copie qui ne correspond plus — sinon vous l'apprenez des semaines plus tard, par une
réponse qui aurait déjà dû être corrigée.

</details>

<details>
<summary><b>Claude.ai</b> (web et application de bureau)</summary>

Nécessite un abonnement **Pro, Max, Team ou Enterprise**, avec l'exécution de code activée.

1. Téléchargez ce dépôt ([**ZIP**](https://github.com/guicortei/feynman-technique/archive/refs/heads/main.zip)).
2. Compressez le dossier `skills/feynman-technique` **lui-même**, pour que `SKILL.md` se
   retrouve à la racine de l'archive :
   ```bash
   cd skills && zip -r feynman-technique.zip feynman-technique
   ```
3. Dans Claude, ouvrez **Paramètres → Capacités → Skills** (affiché sous *Features* dans
   certains abonnements) et choisissez **Upload skill**.
4. Sélectionnez `feynman-technique.zip`.

Claude s'en servira tout seul dès que vous demanderez une explication ; vous pouvez aussi
l'appeler par son nom.

> Sur claude.ai, les skills personnalisés sont propres à chaque utilisateur — chacun
> téléverse sa propre copie.

</details>

<details>
<summary><b>ChatGPT</b> (application de bureau)</summary>

1. Téléchargez ce dépôt et décompressez-le.
2. Ouvrez l'application de bureau ChatGPT et sélectionnez **Skills** dans la barre latérale.
3. Ajoutez le dossier `feynman-technique`.
4. Appelez-le dans une conversation en tapant `@`, puis en le choisissant dans la liste.

**Votre abonnement ne gère pas les skills ?** Prenez la solution de repli décrite dans
[Toute autre IA](#toute-autre-ia-sans-prise-en-charge-des-skills) plus bas — elle marche
dans ChatGPT tel quel, dans les GPT personnalisés et dans les Projets.

</details>

<details>
<summary><b>OpenAI Codex CLI</b></summary>

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/feynman-technique
mkdir -p ~/.agents/skills
cp -r /tmp/feynman-technique/skills/feynman-technique ~/.agents/skills/
```

Pour une installation par projet : copiez plutôt le dossier dans `.agents/skills/`, à la
racine du dépôt.

Appelez-le avec `$feynman-technique` ; `/skills` liste ce qui est disponible.

</details>

<details>
<summary><b>Cursor</b></summary>

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/feynman-technique
mkdir -p ~/.cursor/skills
cp -r /tmp/feynman-technique/skills/feynman-technique ~/.cursor/skills/
```

Par projet : `.cursor/skills/` ou `.agents/skills/` dans votre dépôt.
Cursor lit aussi `~/.claude/skills/` : une installation faite pour Claude Code suffit donc.

Tapez `/` dans le chat de l'agent et choisissez **feynman-technique**.

</details>

<details>
<summary><b>VS Code / GitHub Copilot</b></summary>

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/feynman-technique
mkdir -p ~/.copilot/skills
cp -r /tmp/feynman-technique/skills/feynman-technique ~/.copilot/skills/
```

Au niveau du workspace : `.github/skills/` ou `.agents/skills/`.

Tapez `/` dans Copilot Chat et choisissez le skill. Vous pouvez lui passer du contexte à la
suite : `/feynman-technique le middleware d'authentification de ce dépôt`.

</details>

<details>
<summary><b>Gemini CLI</b></summary>

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/feynman-technique
mkdir -p ~/.gemini/skills
cp -r /tmp/feynman-technique/skills/feynman-technique ~/.gemini/skills/
```

Par projet : `.gemini/skills/` ou `.agents/skills/`.
Gemini CLI demande votre accord avant d'activer un skill.

</details>

<details>
<summary><b>Autres outils compatibles</b></summary>

Amp, Goose, OpenCode, OpenHands, Roo Code, Kiro, Factory, JetBrains Junie, Letta,
Firebender, Tabnine, Trae, Mistral Vibe, Snowflake Cortex Code, Databricks Genie Code et
d'autres encore prennent tous en charge le standard.

La plupart lisent l'un de ces chemins, dans cet ordre d'adoption approximatif :

```
~/.agents/skills/        # la convention qui s'impose entre outils
~/.claude/skills/        # largement pris en charge en repli
<propre-à-l-outil>/skills/  # ex. ~/.gemini/skills/, ~/.cursor/skills/
```

Déposez le dossier `feynman-technique` dans celui que documente votre outil. La liste
complète des clients est sur [agentskills.io/clients](https://agentskills.io/clients).

</details>

<details>
<summary id="toute-autre-ia-sans-prise-en-charge-des-skills"><b>Toute autre IA (sans prise en charge des skills)</b></summary>

Le skill n'est que du Markdown : il fait office de prompt système n'importe où.

- **GPT personnalisé / Gem / Assistant :** collez
  [`skills/feynman-technique/SKILL.md`](../../skills/feynman-technique/SKILL.md)
  (sans le bloc YAML du début) dans le champ d'instructions. Téléversez les fichiers de
  `references/` comme fichiers de connaissance.
- **Projet / instructions personnalisées :** pareil, dans la zone d'instructions
  personnalisées du projet.
- **Usage ponctuel :** collez le fichier dans le chat et ajoutez *« Suis ceci pour le reste
  de notre conversation. »*

</details>

### Vérifier que ça marche

Posez une question sur un sujet que vous maîtrisez déjà :

```
/feynman-technique qu'est-ce qu'une fonction de hachage ?
```

Une réponse correcte s'ouvre sur une thèse d'une phrase, enchaîne sur un niveau 0 **sans le
moindre mot technique** et se termine par une section « où l'image casse ». Si elle démarre
par « Une fonction de hachage est une fonction qui associe des données de taille
arbitraire… », c'est que le skill ne s'est pas chargé.

---

## Ce que vous recevez

```
**En une phrase :** ...           ← pour qu'un expert puisse s'arrêter là

**L'image à garder en tête :** ...  ← l'analogie maîtresse

0 · Repas de famille   aucune connaissance du domaine. Zéro terme technique.
1 · Nouveau venu       les vrais noms, rattachés à l'image du niveau 0
2 · Praticien          comment les pièces s'emboîtent, et le premier vrai compromis
3 · Mainteneur         modes de défaillance, ce qui casse, ce qui a été écarté et pourquoi
4 · Spécialiste        cas limites, montée en charge, et les limites du modèle lui-même

Où l'image casse            ← les limites de toute analogie, énoncées
Mots introduits ici         ← une ligne par terme nouveau
Ce que j'ai laissé de côté  ← nommé, pas passé sous silence
```

Les niveaux se compriment, mais ne disparaissent jamais. Une question étroite reçoit la
**forme compacte** : thèse, image, le seul niveau qui compte. Faire défiler cinq niveaux à
un expert, ce n'est pas de la rigueur ; cela *dégrade* sa compréhension, et de façon
mesurable : c'est l'[effet d'inversion de l'expertise](../../skills/feynman-technique/references/evidence.md).

Voir l'[exemple complet](../../skills/feynman-technique/assets/worked-example.md) :
« qu'est-ce qu'un index de base de données ? », traité de bout en bout, puis annoté pour
montrer ce que fait chaque partie.

---

## Mode coach — celui qui vous apprend vraiment

```
/feynman-technique interroge-moi sur la gestion de la congestion par TCP
/feynman-technique je veux vérifier si je comprends vraiment l'event sourcing
```

Là, le skill refuse d'expliquer. C'est **vous** qui expliquez ; lui, il écoute. Il guette le
flou, les termes techniques posés comme point final, les étapes affirmées sans mécanisme —
puis il montre du doigt une lacune, une seule à la fois, sans vous donner la réponse.

C'est le mode que la recherche appuie le plus solidement. Ceux qui se préparent à enseigner
obtiennent de meilleurs résultats que ceux qui se préparent à un examen, *même quand
l'enseignement n'a jamais lieu* (Nestojko et al., 2014). Fabriquer sa propre explication
vaut mieux que lire celle d'un autre (Chi et al., 1989).

---

## Les règles qu'il suit

| | Prompt classique « explique simplement » | Ce skill |
|---|---|---|
| **Jargon** | des phrases plus simples, les mêmes termes | tout terme nouveau est expliqué dès sa première apparition, sinon il n'apparaît pas |
| **Analogies** | une métaphore neuve à chaque paragraphe | une seule analogie maîtresse, qu'on étend en la compliquant — **et l'endroit où elle cesse de tenir** |
| **Exactitude** | simplifié jusqu'à devenir faux | approximations signalées *avec leurs limites* |
| **Profondeur** | un seul niveau, plat | une échelle dont on descend au barreau qu'on veut |
| **Experts** | traités avec condescendance | thèse dès la première ligne, puis forme compacte |
| **Noms** | le nom *est* la réponse | le mécanisme d'abord, le nom en dernier |
| **Ignorance** | escamotée | « personne ne sait », dit franchement, quand c'est le cas |
| **Apprentissage** | on vous fait la leçon | le mode coach vous fait expliquer, *vous*, et repère vos lacunes |

Règle zéro : **être clair n'excuse jamais d'avoir tort.** Si simplifier revient à déformer, le
skill le dit, donne les limites, et livre la version exacte au barreau du dessus.

---

## Sous le capot

Les fichiers du skill sont en anglais, pour que le frontmatter reste canonique.

| Fichier | Contenu |
|---|---|
| [**SKILL.md**](../../skills/feynman-technique/SKILL.md) | Le skill lui-même. Commencez ici. |
| [references/voice.md](../../skills/feynman-technique/references/voice.md) | Analyse stylistique de la prose de Feynman, chiffres du corpus à l'appui |
| [references/ladder.md](../../skills/feynman-technique/references/ladder.md) | Calibrage des niveaux et adaptation du format |
| [references/analogies.md](../../skills/feynman-technique/references/analogies.md) | Construire, étendre et éprouver les analogies |
| [references/failure-modes.md](../../skills/feynman-technique/references/failure-modes.md) | 14 façons de rater une explication, chacune avec sa réécriture |
| [references/evidence.md](../../skills/feynman-technique/references/evidence.md) | Les sciences de l'apprentissage — et là où la méthode échoue pour de bon |
| [references/sources.md](../../skills/feynman-technique/references/sources.md) | Citations vérifiées, et celles qu'on lui attribue à tort |
| [assets/worked-example.md](../../skills/feynman-technique/assets/worked-example.md) | Une réponse complète, annotée |
| [assets/checklist.md](../../skills/feynman-technique/assets/checklist.md) | L'audit avant envoi |

### Un aperçu de l'analyse stylistique

Extrait de [voice.md](../../skills/feynman-technique/references/voice.md), tout mesuré sur
le corpus de 88 000 mots :

- **La rupture de rythme est la signature.** Phrase médiane ≈ 20 mots — mais environ 1 sur
  8 tient en moins de huit mots et 1 sur 6 dépasse les trente-cinq. Il construit long, il
  atterrit court. *"Shake this one, that one shakes later."* — *« Secouez celui-ci, l'autre
  bougera plus tard. »*
- **Les pronoms changent selon la fonction.** « We » quand il enseigne (19,95 pour 1 000
  mots dans *Six Easy Pieces*, dix fois plus que ses « I »), « I » quand il avoue sa
  confusion (26,7/1k dans la conférence Nobel), « you » quand il donne des consignes
  (20,6/1k dans *Cargo Cult Science*).
- **Des verbes qu'un corps peut sentir.** *jiggle* 27, *pull* 37, *push* 28, *shake* 20.
  Les molécules *frétillent* ; elles ne « manifestent » aucune « agitation thermique ».
- **« Basically » n'apparaît pas une seule fois en 88 000 mots.** *Trivial* apparaît une
  fois. D'où l'interdiction de ces mots dans le skill : c'est une mesure, pas une question de goût.

---

## Limites assumées

La règle zéro vaut aussi pour cette page.

- **Feynman n'a pas inventé la « technique de Feynman ».** Il n'a jamais publié de méthode
  en quatre étapes portant ce nom. Ces quatre étapes ont été assemblées plus tard par des
  vulgarisateurs, Scott H. Young au premier chef, vers 2011 — une reconstruction honnête.
  Ce skill s'appuie plutôt sur ses tests *documentés*, et le dit.
- **« Si vous ne pouvez pas l'expliquer simplement, c'est que vous ne l'avez pas compris »**
  n'a aucune source primaire, ni chez Feynman ni chez Einstein.
  [sources.md](../../skills/feynman-technique/references/sources.md) recense ce qu'il a dit
  de vérifiable, et ce qu'il n'a jamais dit.
- **Certaines choses ne se simplifient pas.** Feynman s'est cogné lui-même à ce mur : quand
  son propre père lui a demandé comment un photon sort d'un atome sans y avoir jamais été,
  il a répondu *"I'm sorry; I don't know. I can't explain it to you."* — *« Désolé ; je ne
  sais pas. Je ne peux pas te l'expliquer. »* Le skill est fait pour dire cela plutôt que
  de fabriquer une image.
- **Cela coûte des tokens et du temps.** Pour une simple vérification, la forme compacte —
  ou pas de skill du tout — reste le bon choix.
- **Il n'apporte pas grand-chose à la mémorisation ni aux automatismes moteurs.** Il vise
  la compréhension causale, mécanique. Le vocabulaire et les raccourcis clavier réclament
  de la récupération espacée, pas des explications.
- **Une bonne explication *donne l'impression* d'avoir compris.** Cette impression ne
  prouve rien. Quand l'enjeu compte, passez en mode coach.

---

## Crédits et droits d'auteur

Richard P. Feynman (1918–1988) a écrit tout ce qui, ici, vaut la peine d'être lu. Ce dépôt
contient **des règles dérivées et de courtes citations attribuées**, à des fins d'analyse
et d'enseignement — il ne redistribue pas son œuvre.

Ses textes restent sous copyright : *The Feynman Lectures on Physics* se *lit* gratuitement
sur [feynmanlectures.caltech.edu](https://www.feynmanlectures.caltech.edu/), mais le texte
est © Caltech et **n'appartient pas au domaine public**. Si vous forkez ce dépôt, tenez la
même ligne : citez court, attribuez toujours, ne recopiez jamais de chapitres. Provenance
complète dans [sources.md](../../skills/feynman-technique/references/sources.md).

Ce skill a commencé sous le nom de `feynman-reply`, un skill en portugais signé
[@guicortei](https://github.com/guicortei). Il a été reconstruit à partir des sources
primaires, élargi au-delà du logiciel, puis enrichi de l'analyse stylistique, de la base de
preuves et du mode coach — et rebaptisé `feynman-technique`.

Ce projet n'est ni affilié ni approuvé par la succession Feynman, Caltech ou Anthropic.

## Contribuer

Les contributions sont bienvenues — en particulier :

- des exemples traités dans d'autres domaines (médecine, droit, finance, biologie)
- des modes d'échec rencontrés en usage réel
- des corrections sur une citation ou une attribution

Voir [CONTRIBUTING.md](../../CONTRIBUTING.md). Une demande, une seule : si vous ajoutez une
affirmation sur Feynman, citez la source primaire. Bâcler l'attribution tout en invoquant
son nom au nom de l'honnêteté intellectuelle, c'est le seul bug impardonnable de ce dépôt.

## Licence

[MIT](../../LICENSE). Utilisez-le, forkez-le, diffusez-le.

---

<div align="center">

> *"The first principle is that you must not fool yourself — and you are the easiest person
> to fool."*
> — Richard Feynman, *Cargo Cult Science*, 1974
>
> *« Le premier principe, c'est qu'il ne faut pas se duper soi-même — et vous êtes la
> personne la plus facile à duper. »*

**[⭐ Mettez une étoile au dépôt](https://github.com/guicortei/feynman-technique)** si ça a
changé une réponse que vous avez eue aujourd'hui.

</div>
