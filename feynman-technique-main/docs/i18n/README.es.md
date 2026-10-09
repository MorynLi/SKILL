<div align="center">

<img src="../../assets/hero.es.svg" alt="feynman-technique — sin feynman-technique: El fallo es de CORS: política de mismo origen. El navegador hace una solicitud de verificación previa. La respuesta no incluye Access-Control-Allow-Origin. Por eso el navegador descarta la respuesta. Propongo añadir un middleware de CORS en la API. Ahí configuro el origen permitido y los métodos. ¿Añado el middleware de CORS con el origen permitido? — con feynman-technique: Tu código no falló. Lo bloqueó el navegador. La petición salió y la respuesta llegó de vuelta. El navegador la recibió y no te la entregó. Puede que estés logueado en ese otro servidor. Sin esa regla, cualquier pestaña leería tus datos. El otro servidor tiene que nombrar tu dominio. Nunca lo nombró, así que el navegador corta. En Postman funciona. En curl también. Aquí no. Postman no protege a nadie. El navegador sí: a ti. Voy a hacer que el servidor nombre tu dominio. ¿Le digo al servidor que tu dominio es bienvenido?" width="820">

# Técnica de Feynman

### La IA te dio la solución. Funcionó. Sigues sin saber por qué.

**Esto es para el porqué.**

[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-est%C3%A1ndar%20abierto-6b4fbb)](https://agentskills.io)
[![Licencia: MIT](https://img.shields.io/badge/Licencia-MIT-blue.svg)](../../LICENSE)
[![Works with](https://img.shields.io/badge/works%20with-Claude%20·%20ChatGPT%20·%20Codex%20·%20Cursor%20·%20Copilot%20·%20Gemini-333)](#instalación)
[![Hecho con](https://img.shields.io/badge/hecho%20con-88.000%20palabras%20de%20Feynman-c2410c)](#de-dónde-sale-esto)

[English](../../README.md) ·
[中文](README.zh-CN.md) ·
[हिन्दी](README.hi.md) ·
**Español** ·
[Français](README.fr.md) ·
[العربية](README.ar.md) ·
[বাংলা](README.bn.md) ·
[Português](README.pt-BR.md) ·
[Русский](README.ru.md) ·
[اردو](README.ur.md)

</div>

---

## El mismo modelo. La misma pregunta. Una línea de instalación.

> **"¿Por qué me sale `Cannot read properties of undefined (reading 'map')`?"**

<table>
<tr>
<th width="50%">Sin el skill</th>
<th width="50%">Con el skill</th>
</tr>
<tr valign="top">
<td>

Se está invocando `.map()` sobre una referencia indefinida. El componente se renderiza antes de que se resuelva el fetch asíncrono, así que la variable de estado sigue sin inicializar en el primer pintado. Inicialízala como array vacío o protege el render con una condicional.

</td>
<td>

Le dijiste a la página: toma mi lista de artículos y dibuja una fila por cada uno.

Pero la lista todavía no llegó: sigue viajando desde el servidor. En ese instante no hay ninguna lista, y la página tropieza con el hueco donde tendría que haber una.

Dale una lista vacía para que la sostenga hasta que aterrice la de verdad. Así no dibuja nada, espera, y después lo dibuja todo.

</td>
</tr>
<tr valign="top">
<td>

Seis términos que ya tenías que saber. Es correcto, y sigues sin poder imaginártelo.

</td>
<td>

Cero. Y sabes qué línea tocar, y qué esperar después.

</td>
</tr>
</table>

Las dos respuestas son ciertas. Solo una de ellas explicaba algo.

---

## De dónde sale esto

El padre de Feynman le enseñó un pájaro y le dijo que puedes aprenderte su nombre en todos
los idiomas de la Tierra y seguir sin saber **absolutamente nada del pájaro**. Sabrías cómo
lo llama la gente, y nada más. Para conocer al pájaro hay que mirar lo que hace.

> "There is a difference between the name of the thing and what goes on."
> — Richard Feynman, *What Is Science?*, 1966
>
> *"Hay una diferencia entre el nombre de la cosa y lo que ocurre."*

Ahí está la idea entera, y casi todas las IA fallan en eso por defecto. Preguntas qué es algo
y recibes su nombre dicho con palabras más finas. "Es una race condition." "Usa connection
pooling." Asientes con la cabeza. No se ha transmitido nada. Este skill hace que el modelo
entregue **primero el mecanismo** y el nombre al final, como hacía Feynman.

Está hecho a partir de fuentes primarias, no de artículos de blog sobre Feynman. Para sacar
de ahí tanto el método como el estilo de la prosa se analizaron unas **88.000 palabras**
escritas por él: *Six Easy Pieces*, la Conferencia Nobel de 1965, *Cargo Cult Science*,
*What Is Science?*, *There's Plenty of Room at the Bottom* y el capítulo brasileño de
*Surely You're Joking, Mr. Feynman!*

**El repositorio está en inglés. Las respuestas no** — el skill contesta en el idioma en que
le escribas.

---

## Las cuatro pruebas que aplica

Nada del manido "explícaselo a un niño de 12 años". Son las pruebas del propio Feynman, y
todas se pueden rastrear hasta una fuente primaria.

<table>
<tr valign="top"><td width="30%">

**La prueba de la reformulación**

</td><td>

*"Without using the new word which you have just learned, try to rephrase what you have just learned in your own language."* (1966)

*"Sin usar la palabra nueva que acabas de aprender, intenta reformular en tu propio lenguaje lo que acabas de aprender."*

Tapa el término. Si la frase se cae sin él, lo que escribiste era una definición, no una explicación.

</td></tr>
<tr valign="top"><td>

**La prueba de la triboluminiscencia**

</td><td>

Feynman abrió un libro de texto al azar: *"Triboluminescence is the light emitted when crystals are crushed."* — *"La triboluminiscencia es la luz que se emite cuando se trituran ciertos cristales."* Su veredicto: solo has dicho lo que significa una palabra usando otras palabras.

Su reescritura: *"When you take a lump of sugar and crush it with a pair of pliers in the dark, you can see a bluish flash. Some other crystals do that too. Nobody knows why. The phenomenon is called 'triboluminescence.'"* — *"Si tomas un terrón de azúcar y lo aplastas con unos alicates a oscuras, ves un destello azulado. Algunos otros cristales hacen lo mismo. Nadie sabe por qué. Al fenómeno se le llama 'triboluminiscencia'."*

Algo que puedes hacer → lo que verías → ignorancia honesta → **y solo entonces** el nombre.

</td></tr>
<tr valign="top"><td>

**La prueba de "mira el agua"**

</td><td>

Sus alumnos brasileños recitaban el ángulo de Brewster sin un fallo. Cuando les pidió que apuntaran un polaroid a la bahía que tenían al otro lado de la ventana, se quedaron parados.

Una explicación a la que solo se llega por su palabra clave es una explicación a la que nunca vas a llegar cuando de verdad la necesites.

</td></tr>
<tr valign="top"><td>

**La prueba del culto cargo**

</td><td>

Después de leer, ¿qué puedes *hacer* que antes no podías? Si la forma es correcta pero detrás no hay nada, los aviones no aterrizan.

</td></tr>
</table>

---

## Instalación

Una sola carpeta. Funciona en cualquier herramienta que implemente el
[estándar abierto Agent Skills](https://agentskills.io).

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/feynman-technique
mkdir -p ~/.claude/skills
cp -r /tmp/feynman-technique/skills/feynman-technique ~/.claude/skills/
```

Eso es Claude Code. A partir de ahí, basta con pedírselo:

```
/feynman-technique explica cómo funcionan los índices de base de datos
```

<details>
<summary><b>Claude Code</b> (por proyecto, compartido con tu equipo)</summary>

```bash
mkdir -p .claude/skills
cp -r /tmp/feynman-technique/skills/feynman-technique .claude/skills/
```

Haz commit y lo tiene todo el que trabaje en el repositorio. Ejecuta `/doctor` para
comprobar que se ha cargado.

</details>

<details>
<summary><b>O usa el script</b> (y evita que tu copia se quede vieja)</summary>

```bash
./install.sh              # personal, Claude Code
./install.sh --project    # en este repositorio, para el equipo
./install.sh --all        # todos los directorios de herramientas de esta máquina
./install.sh --check      # dice qué copias se han quedado atrás, sin tocar nada
```

`--check` es el que conviene recordar. Un skill instalado es una *copia*: no sigue al
repositorio. Haz `pull`, ejecuta `--check` y te nombra las copias que ya no coinciden — si
no, te enteras semanas después, por una respuesta que ya tendría que estar corregida.

</details>

<details>
<summary><b>Claude.ai</b> (web y app de escritorio)</summary>

Requiere un plan **Pro, Max, Team o Enterprise** con la ejecución de código activada.

1. Descarga este repositorio ([**ZIP**](https://github.com/guicortei/feynman-technique/archive/refs/heads/main.zip)).
2. Comprime la carpeta `skills/feynman-technique` **en sí misma**, de modo que `SKILL.md`
   quede en la raíz del comprimido:
   ```bash
   cd skills && zip -r feynman-technique.zip feynman-technique
   ```
3. En Claude, entra en **Ajustes → Capacidades → Skills** (en algunos planes aparece como
   *Features*) y elige **Upload skill**.
4. Selecciona `feynman-technique.zip`.

Claude lo usará por su cuenta cuando pidas una explicación; también puedes pedirlo por su
nombre.

> Los skills personalizados en claude.ai van por usuario: cada miembro del equipo sube su
> propia copia.

</details>

<details>
<summary><b>ChatGPT</b> (app de escritorio)</summary>

1. Descarga este repositorio y descomprímelo.
2. Abre la app de escritorio de ChatGPT y entra en **Skills**, en la barra lateral.
3. Añade la carpeta `feynman-technique`.
4. Para invocarlo en una conversación, escribe `@` y elígelo de la lista.

**¿Tu plan no admite skills?** Usa la alternativa de
[Cualquier otra IA](#cualquier-otra-ia-sin-soporte-de-skills), más abajo: funciona en ChatGPT
normal, en GPTs personalizados y en Proyectos.

</details>

<details>
<summary><b>OpenAI Codex CLI</b></summary>

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/feynman-technique
mkdir -p ~/.agents/skills
cp -r /tmp/feynman-technique/skills/feynman-technique ~/.agents/skills/
```

Si lo prefieres por proyecto: cópialo a `.agents/skills/` en la raíz del repositorio.

Invócalo con `$feynman-technique`, o ejecuta `/skills` para ver qué tienes disponible.

</details>

<details>
<summary><b>Cursor</b></summary>

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/feynman-technique
mkdir -p ~/.cursor/skills
cp -r /tmp/feynman-technique/skills/feynman-technique ~/.cursor/skills/
```

Por proyecto: `.cursor/skills/` o `.agents/skills/` en tu repositorio.
Cursor también lee `~/.claude/skills/`, así que si ya lo instalaste para Claude Code, está
cubierto.

Escribe `/` en el chat del Agent y elige **feynman-technique**.

</details>

<details>
<summary><b>VS Code / GitHub Copilot</b></summary>

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/feynman-technique
mkdir -p ~/.copilot/skills
cp -r /tmp/feynman-technique/skills/feynman-technique ~/.copilot/skills/
```

Por workspace: `.github/skills/` o `.agents/skills/`.

Escribe `/` en Copilot Chat y elige el skill. Puedes pasarle contexto detrás:
`/feynman-technique el middleware de autenticación de este repositorio`.

</details>

<details>
<summary><b>Gemini CLI</b></summary>

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/feynman-technique
mkdir -p ~/.gemini/skills
cp -r /tmp/feynman-technique/skills/feynman-technique ~/.gemini/skills/
```

Por proyecto: `.gemini/skills/` o `.agents/skills/`.
Gemini CLI pide permiso antes de activar un skill.

</details>

<details>
<summary><b>Otras herramientas compatibles</b></summary>

Amp, Goose, OpenCode, OpenHands, Roo Code, Kiro, Factory, JetBrains Junie, Letta,
Firebender, Tabnine, Trae, Mistral Vibe, Snowflake Cortex Code, Databricks Genie Code y
otras admiten el estándar.

Casi todas leen una de estas rutas, en orden aproximado de adopción:

```
~/.agents/skills/        # la convención que se está imponiendo entre herramientas
~/.claude/skills/        # ampliamente soportada como alternativa
<específico-de-la-herramienta>/skills/  # p. ej. ~/.gemini/skills/, ~/.cursor/skills/
```

Deja la carpeta `feynman-technique` en la ruta que documente tu herramienta. La lista
completa de clientes está en [agentskills.io/clients](https://agentskills.io/clients).

</details>

<details>
<summary id="cualquier-otra-ia-sin-soporte-de-skills"><b>Cualquier otra IA (sin soporte de skills)</b></summary>

El skill es Markdown puro, así que sirve como prompt de sistema en cualquier parte.

- **GPT personalizado / Gem / Assistant:** pega
  [`skills/feynman-technique/SKILL.md`](../../skills/feynman-technique/SKILL.md)
  (sin el bloque YAML de la cabecera) en el campo de instrucciones. Sube los archivos de
  `references/` como archivos de conocimiento.
- **Proyecto / instrucciones personalizadas:** lo mismo, en la caja de instrucciones
  personalizadas del proyecto.
- **Uso puntual:** pega el archivo en el chat y añade *"Sigue esto durante el resto de
  nuestra conversación."*

</details>

### Comprueba que funciona

Pregúntale por algo que ya entiendas bien:

```
/feynman-technique ¿qué es una función hash?
```

Una respuesta correcta empieza con una tesis de una sola frase, sigue con un nivel 0 **sin
una sola palabra técnica** y termina con un apartado de "dónde se rompe la imagen". Si
empieza por "Una función hash es una función que mapea datos de tamaño arbitrario…", el skill
no se ha cargado.

---

## Qué te devuelve

```
**En una frase:** ...              ← para que un experto pueda dejar de leer aquí

**La imagen que hay que sostener:** ...  ← la analogía maestra

0 · La sobremesa     ningún conocimiento del campo. Cero términos técnicos.
1 · Recién llegado   los nombres reales, atados a la imagen del nivel 0
2 · Profesional      cómo encajan las piezas, y el primer trade-off real
3 · Mantenedor       modos de fallo, qué se rompe, qué se descartó y por qué
4 · Especialista     bordes, escala y los límites del propio modelo

Dónde se rompe la imagen     ← los límites de toda analogía, declarados
Palabras nuevas de aquí      ← una línea por término nuevo
Qué he dejado fuera          ← nombrado, no omitido en silencio
```

Los niveles se comprimen, pero nunca desaparecen. Una pregunta acotada recibe **forma
compacta**: tesis, imagen y el único nivel que importa. Hacer desfilar a un experto por los
cinco niveles no es rigor; le *degrada* la comprensión, y de forma medible (el
[efecto de reversión de la pericia](../../skills/feynman-technique/references/evidence.md)).

Hay un [ejemplo completo resuelto](../../skills/feynman-technique/assets/worked-example.md):
"¿qué es un índice de base de datos?", respondido entero y luego anotado para enseñar qué
hace cada parte.

---

## Modo entrenador — el que de verdad te enseña

```
/feynman-technique pregúntame sobre cómo TCP maneja la congestión
/feynman-technique quiero comprobar si entiendo de verdad event sourcing
```

Aquí el skill se niega a explicar. Explicas **tú**; él escucha en busca de vaguedades, de
palabras técnicas usadas como punto final, de pasos que afirmas sin mecanismo — y te señala
una sola laguna cada vez, sin darte la respuesta.

Es el modo que tiene la investigación más sólida detrás. Quien se prepara para enseñar rinde
más que quien se prepara para un examen, *incluso cuando la clase no llega a darse nunca*
(Nestojko et al., 2014). Construir tu propia explicación funciona mejor que leer la de otro
(Chi et al., 1989).

---

## Las reglas que sigue

| | Prompt típico de "explícalo simple" | Este skill |
|---|---|---|
| **Jerga** | frases más simples, los mismos términos | todo término nuevo se explica la primera vez que aparece, o no aparece |
| **Analogías** | una metáfora nueva en cada párrafo | una sola analogía maestra, que crece a base de complicarla — **y dónde se rompe** |
| **Precisión** | simplificada hasta quedar falsa | aproximaciones marcadas *con sus límites* |
| **Profundidad** | un solo nivel plano | una escalera de la que puedes bajarte en cualquier peldaño |
| **Expertos** | tratados con condescendencia | tesis en la primera línea, luego forma compacta |
| **Nombres** | el nombre *es* la respuesta | primero el mecanismo, el nombre al final |
| **Ignorancia** | se pasa de puntillas | "nadie lo sabe", dicho sin rodeos, cuando es cierto |
| **Aprendizaje** | te suelta la explicación encima | el modo entrenador te hace explicar a *ti*, y detecta tus lagunas |

Regla cero: **ser claro nunca es excusa para estar equivocado.** Si simplificar deformara el
asunto, lo dice, da los límites y entrega la versión exacta un nivel más arriba.

---

## Por dentro

Los archivos del skill están en inglés, para que el frontmatter siga siendo el canónico.

| Archivo | Contenido |
|---|---|
| [**SKILL.md**](../../skills/feynman-technique/SKILL.md) | El skill en sí. Empieza aquí. |
| [references/voice.md](../../skills/feynman-technique/references/voice.md) | Análisis forense del estilo de Feynman, con estadísticas del corpus |
| [references/ladder.md](../../skills/feynman-technique/references/ladder.md) | Calibración de los niveles y cómo adaptar el formato |
| [references/analogies.md](../../skills/feynman-technique/references/analogies.md) | Construir analogías, extenderlas y ponerlas a prueba |
| [references/failure-modes.md](../../skills/feynman-technique/references/failure-modes.md) | 14 formas de arruinar una explicación, cada una con su reescritura |
| [references/evidence.md](../../skills/feynman-technique/references/evidence.md) | La ciencia del aprendizaje — y dónde falla de verdad este método |
| [references/sources.md](../../skills/feynman-technique/references/sources.md) | Las citas verificadas, y las que se le atribuyen en falso |
| [assets/worked-example.md](../../skills/feynman-technique/assets/worked-example.md) | Una respuesta completa, anotada |
| [assets/checklist.md](../../skills/feynman-technique/assets/checklist.md) | La auditoría antes de enviar |

### Una muestra del análisis forense de estilo

De [voice.md](../../skills/feynman-technique/references/voice.md), todo medido sobre el
corpus de 88.000 palabras:

- **La irregularidad es la firma.** Mediana de frase ≈ 20 palabras — pero ~1 de cada 8 baja
  de las ocho palabras y ~1 de cada 6 pasa de treinta y cinco. Construye largo y aterriza
  corto. *"Shake this one, that one shakes later."*
- **Los pronombres cambian según la función.** "We" al enseñar (19,95 por cada 1.000 palabras
  en *Six Easy Pieces*, diez veces su "I"), "I" al admitir que está confundido (26,7/1k en la
  Conferencia Nobel), "you" al instruir (20,6/1k en *Cargo Cult Science*).
- **Verbos que el cuerpo siente.** *jiggle* 27, *pull* 37, *push* 28, *shake* 20. Las
  moléculas se menean; no "exhiben agitación térmica".
- **"Basically" aparece cero veces en 88.000 palabras.** *Trivial* aparece una. Por eso el
  skill las prohíbe — medición, no gusto personal.

---

## Limitaciones honestas

La regla cero vale también para esta página.

- **Feynman no inventó la "Técnica de Feynman".** Nunca publicó ningún método de cuatro pasos
  con ese nombre. Los cuatro pasos los armaron divulgadores posteriores, sobre todo Scott H.
  Young hacia 2011, y son una reconstrucción razonable. Este skill usa en su lugar las
  pruebas que él sí documentó, y lo dice.
- **"Si no puedes explicarlo de forma simple, no lo entiendes"** no tiene fuente primaria ni
  en Feynman ni en Einstein.
  [sources.md](../../skills/feynman-technique/references/sources.md) recoge lo que dijo de
  forma verificable y lo que no.
- **Hay cosas que no se simplifican.** El propio Feynman chocó con ese muro: cuando su padre
  le preguntó cómo sale un fotón de un átomo sin haber estado dentro, respondió *"I'm sorry;
  I don't know. I can't explain it to you."* El skill está hecho para decir eso antes que
  inventarse una imagen.
- **Cuesta tokens y tiempo.** Para una consulta rápida, lo que toca es la forma compacta, o
  directamente ningún skill.
- **Sirve de poco para memorizar o para las habilidades motoras.** Apunta a la comprensión
  causal, la de los mecanismos. El vocabulario y los atajos de teclado piden recuperación
  espaciada, no explicaciones.
- **Una buena explicación *da la sensación* de haber entendido.** Esa sensación no es una
  prueba. Cuando importa, usa el modo entrenador.

---

## Créditos y derechos de autor

Richard P. Feynman (1918–1988) escribió todo lo que vale la pena leer aquí. Este repositorio
contiene **reglas derivadas y citas breves con atribución**, usadas para analizar y enseñar
— no redistribuye su obra.

Sus textos siguen bajo derechos de autor: *The Feynman Lectures on Physics* se puede *leer*
gratis en [feynmanlectures.caltech.edu](https://www.feynmanlectures.caltech.edu/), pero es ©
de Caltech y **no es de dominio público**. Si haces un fork, mantenlo así: cita lo justo,
atribuye siempre, no pegues capítulos enteros. Toda la procedencia está en
[sources.md](../../skills/feynman-technique/references/sources.md).

Este skill empezó como `feynman-reply`, un skill en portugués de
[@guicortei](https://github.com/guicortei). Se reconstruyó a partir de fuentes primarias, se
generalizó más allá del software y se amplió con el análisis de estilo, la base de evidencias
y el modo entrenador — y después pasó a llamarse `feynman-technique`.

Sin relación ni respaldo de los herederos de Feynman, de Caltech ni de Anthropic.

## Contribuir

Se agradecen mejoras, sobre todo ejemplos resueltos de otros campos, modos de fallo
detectados en uso real y correcciones a cualquier cita. Consulta
[CONTRIBUTING.md](../../CONTRIBUTING.md).

Una petición: si añades una afirmación sobre Feynman, cita la fuente primaria. Invocar su
nombre para hablar de honestidad intelectual y a la vez ser descuidado con las atribuciones
es el único bug imperdonable de este repositorio.

## Licencia

[MIT](../../LICENSE). Úsalo, haz un fork, publícalo.

---

<div align="center">

> *"The first principle is that you must not fool yourself — and you are the easiest person
> to fool."*
> — Richard Feynman, *Cargo Cult Science*, 1974
>
> *"El primer principio es que no debes engañarte a ti mismo — y tú eres la persona más
> fácil de engañar."*

**[⭐ Dale una estrella al repositorio](https://github.com/guicortei/feynman-technique)** si
ha cambiado alguna respuesta que hayas recibido hoy.

</div>
