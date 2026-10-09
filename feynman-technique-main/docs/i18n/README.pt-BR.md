<div align="center">

<img src="../../assets/hero.pt-BR.svg" alt="feynman-technique — sem feynman-technique: O erro vem da política de mesma origem do navegador. A resposta da API não traz Access-Control-Allow-Origin. A requisição preflight OPTIONS não é respondida. Sem esses cabeçalhos, o fetch é bloqueado no cliente. A correção é liberar a origem no middleware da API. Vou adicionar um middleware de CORS no seu servidor. Posso configurar o middleware de CORS na API? — com feynman-technique: Seu código não deu erro. Quem bloqueou foi o navegador. A requisição saiu e a resposta voltou inteirinha. O navegador segurou e não entregou para a sua tela. Motivo: você pode estar logado no outro site. Sem isso, qualquer aba leria os seus dados de lá. O outro site precisa liberar o seu endereço. Ele nunca liberou. É só isso que está faltando. No Postman e no curl funciona. No navegador, dá pau. Postman não protege ninguém. O navegador protege você. Vou pôr o seu endereço na lista de liberados da API. Posso colocar o seu site na lista de liberados da API?" width="820">

# Técnica de Feynman

### A IA te deu a correção. Você colou, funcionou. E continua sem saber por quê.

**Isto aqui é para a segunda parte.**

[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-padr%C3%A3o%20aberto-6b4fbb)](https://agentskills.io)
[![Licença: MIT](https://img.shields.io/badge/Licen%C3%A7a-MIT-blue.svg)](../../LICENSE)
[![Works with](https://img.shields.io/badge/works%20with-Claude%20·%20ChatGPT%20·%20Codex%20·%20Cursor%20·%20Copilot%20·%20Gemini-333)](#instalação)
[![Feita de](https://img.shields.io/badge/feita%20de-88.000%20palavras%20de%20Feynman-c2410c)](#de-onde-isso-vem)

[English](../../README.md) ·
[中文](README.zh-CN.md) ·
[हिन्दी](README.hi.md) ·
[Español](README.es.md) ·
[Français](README.fr.md) ·
[العربية](README.ar.md) ·
[বাংলা](README.bn.md) ·
**Português** ·
[Русский](README.ru.md) ·
[اردو](README.ur.md)

</div>

---

## Mesmo modelo. Mesma pergunta. Uma linha de instalação.

> **"Por que está dando `Cannot read properties of undefined (reading 'map')`?"**

<table>
<tr>
<th width="50%">Sem a skill</th>
<th width="50%">Com a skill</th>
</tr>
<tr valign="top">
<td>

O `.map()` está sendo chamado sobre uma referência `undefined`. Seu componente renderiza antes de a requisição assíncrona resolver, então a variável de estado ainda está não inicializada no primeiro paint. Inicialize com um array vazio ou proteja o caminho de render com uma condicional.

</td>
<td>

Você mandou a página fazer o seguinte: pega a minha lista de itens e desenha uma linha para cada um.

Só que a lista ainda não chegou — ela ainda está vindo do servidor. Naquele instante não existe lista nenhuma, e a página tropeça no vazio onde deveria haver uma.

Entregue uma lista vazia para ela segurar até a de verdade chegar. Aí ela desenha nada, espera, e depois desenha tudo.

</td>
</tr>
<tr valign="top">
<td>

Seis termos que você já precisava saber. Está certo, e você continua sem enxergar a cena.

</td>
<td>

Nenhum. E você sabe que linha mudar e o que esperar depois.

</td>
</tr>
</table>

As duas respostas estão certas. Só uma delas explicou alguma coisa.

---

## De onde isso vem

O pai de Feynman mostrou um pássaro para ele e disse que dá para aprender o nome daquele
pássaro em todas as línguas do mundo e continuar sem saber **absolutamente nada sobre o
pássaro**. Você saberia só como as pessoas o chamam. Para conhecer o bicho, olhe o que ele
faz.

> "There is a difference between the name of the thing and what goes on."
> — Richard Feynman, *What Is Science?*, 1966
>
> *"Há uma diferença entre o nome da coisa e o que acontece."*

A ideia é essa, e quase toda IA falha nela por padrão. Você pergunta o que uma coisa é e
recebe o nome dela em palavras mais bonitas. "É uma race condition." "Usa connection
pooling." Você faz que sim com a cabeça. Não passou nada. Esta skill faz o modelo entregar
o **mecanismo primeiro** e o nome por último — do jeito que Feynman fazia.

Ela vem de fontes primárias, não de posts de blog sobre Feynman. Cerca de **88.000 palavras**
escritas por ele foram analisadas para extrair o método e também o estilo da prosa:
*Six Easy Pieces*, a Palestra do Nobel de 1965, *Cargo Cult Science*, *What Is Science?*,
*There's Plenty of Room at the Bottom* e o capítulo sobre o Brasil de *Surely You're Joking,
Mr. Feynman!*

**O repositório está em inglês. As respostas, não** — a skill responde no idioma em que você
escrever para ela.

---

## Os quatro testes que ela aplica

Em vez do batido "explique para uma criança de 12 anos", a skill usa os testes do próprio
Feynman — todos documentados em fontes primárias.

<table>
<tr valign="top"><td width="30%">

**O teste da reformulação**

</td><td>

*"Without using the new word which you have just learned, try to rephrase what you have just learned in your own language."* (1966)

*"Sem usar a palavra nova que você acabou de aprender, tente reformular o que aprendeu na sua própria linguagem."*

Tape o termo com o dedo. Se a frase morre sem ele, era uma definição, não uma explicação.

</td></tr>
<tr valign="top"><td>

**O teste da triboluminescência**

</td><td>

Feynman abriu um livro didático numa página qualquer: *"Triboluminescence is the light emitted when crystals are crushed."* — *"Triboluminescência é a luz emitida quando cristais são esmagados."* Veredito dele: você disse apenas o que uma palavra significa em termos de outras palavras.

A reescrita que ele fez: *"When you take a lump of sugar and crush it with a pair of pliers in the dark, you can see a bluish flash. Some other crystals do that too. Nobody knows why. The phenomenon is called 'triboluminescence.'"* — *"Pegue um torrão de açúcar e esmague com um alicate no escuro: dá para ver um clarão azulado. Alguns outros cristais fazem o mesmo. Ninguém sabe por quê. O fenômeno se chama 'triboluminescência.'"*

Algo que você pode fazer → o que você veria → ignorância honesta → **só então** o nome.

</td></tr>
<tr valign="top"><td>

**O teste do "olhe para a água"**

</td><td>

Os alunos brasileiros dele recitavam o ângulo de Brewster sem errar uma vírgula. Quando ele pediu que apontassem um polaroide para a baía que estava logo ali, na janela, ninguém se mexeu.

Uma explicação em que você só chega pela palavra-chave é uma explicação em que você nunca vai chegar fora da sala de aula, com o problema na sua frente.

</td></tr>
<tr valign="top"><td>

**O teste do cargo cult**

</td><td>

Depois de ler, o que você consegue de fato *fazer* que não conseguia antes? Forma certa e nada por trás: os aviões não pousam.

</td></tr>
</table>

---

## Instalação

Uma pasta só. Funciona em qualquer ferramenta que adote o
[padrão aberto Agent Skills](https://agentskills.io).

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/feynman-technique
mkdir -p ~/.claude/skills
cp -r /tmp/feynman-technique/skills/feynman-technique ~/.claude/skills/
```

Pronto: isso é o Claude Code, na sua máquina e disponível em todos os projetos. Reinicie o
Claude Code (ou rode `/doctor` para confirmar que carregou) e depois é só pedir:

```
/feynman-technique explique como funcionam os índices de banco de dados
```

<details>
<summary><b>Claude Code</b> (por projeto, versionado no repositório e compartilhado com o time)</summary>

```bash
mkdir -p .claude/skills
cp -r /tmp/feynman-technique/skills/feynman-technique .claude/skills/
```

Faça o commit e todo mundo que trabalha no repositório passa a ter a skill. Rode `/doctor`
para confirmar que carregou.

</details>

<details>
<summary><b>Ou use o script</b> (e evite que a sua cópia fique para trás)</summary>

```bash
./install.sh              # pessoal, Claude Code
./install.sh --project    # neste repositório, para o time
./install.sh --all        # todas as pastas de ferramenta que existirem nesta máquina
./install.sh --check      # mostra quais cópias ficaram desatualizadas, sem mudar nada
```

`--check` é o que vale a pena guardar. Skill instalada é *cópia*, e cópia não acompanha o
repositório. Depois de um `git pull`, rode `--check`: o script aponta cada cópia que já não
confere — senão você descobre semanas depois, por uma resposta que já devia estar corrigida.

</details>

<details>
<summary><b>Claude.ai</b> (web e app de desktop)</summary>

Requer plano **Pro, Max, Team ou Enterprise** com execução de código habilitada.

1. Baixe este repositório ([**ZIP**](https://github.com/guicortei/feynman-technique/archive/refs/heads/main.zip)).
2. Compacte a **própria pasta** `skills/feynman-technique`, para que `SKILL.md` fique na
   raiz do zip:
   ```bash
   cd skills && zip -r feynman-technique.zip feynman-technique
   ```
3. No Claude, vá em **Configurações → Capacidades → Skills** (aparece como *Features* em
   alguns planos) e escolha **Upload skill**.
4. Selecione `feynman-technique.zip`.

O Claude passa a usá-la sozinho quando você pede uma explicação; se preferir, chame pelo
nome.

> Skills personalizadas no claude.ai são por usuário — cada colega envia a sua própria cópia.

</details>

<details>
<summary><b>ChatGPT</b> (app de desktop)</summary>

1. Baixe e descompacte este repositório.
2. Abra o app de desktop do ChatGPT e selecione **Skills** na barra lateral.
3. Adicione a pasta `feynman-technique`.
4. Numa conversa, digite `@` e escolha a skill na lista.

**Seu plano não tem suporte a skills?** Use a alternativa em
[Qualquer outra IA](#qualquer-outra-ia-sem-suporte-a-skills) mais abaixo — funciona no
ChatGPT comum, em GPTs personalizados e em Projetos.

</details>

<details>
<summary><b>OpenAI Codex CLI</b></summary>

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/feynman-technique
mkdir -p ~/.agents/skills
cp -r /tmp/feynman-technique/skills/feynman-technique ~/.agents/skills/
```

No nível de projeto: copie para `.agents/skills/` na raiz do seu repositório.

Chame com `$feynman-technique`, ou rode `/skills` para ver o que está disponível.

</details>

<details>
<summary><b>Cursor</b></summary>

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/feynman-technique
mkdir -p ~/.cursor/skills
cp -r /tmp/feynman-technique/skills/feynman-technique ~/.cursor/skills/
```

No nível de projeto: `.cursor/skills/` ou `.agents/skills/` no seu repositório.
O Cursor também lê `~/.claude/skills/`, então quem já instalou pelo Claude Code está
resolvido.

Digite `/` no chat do Agent e escolha **feynman-technique**.

</details>

<details>
<summary><b>VS Code / GitHub Copilot</b></summary>

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/feynman-technique
mkdir -p ~/.copilot/skills
cp -r /tmp/feynman-technique/skills/feynman-technique ~/.copilot/skills/
```

No nível de workspace: `.github/skills/` ou `.agents/skills/`.

Digite `/` no Copilot Chat e escolha a skill. Dá para passar contexto depois:
`/feynman-technique o middleware de autenticação deste repositório`.

</details>

<details>
<summary><b>Gemini CLI</b></summary>

```bash
git clone https://github.com/guicortei/feynman-technique.git /tmp/feynman-technique
mkdir -p ~/.gemini/skills
cp -r /tmp/feynman-technique/skills/feynman-technique ~/.gemini/skills/
```

No nível de projeto: `.gemini/skills/` ou `.agents/skills/`.
O Gemini CLI pede consentimento antes de ativar uma skill.

</details>

<details>
<summary><b>Outras ferramentas suportadas</b></summary>

Amp, Goose, OpenCode, OpenHands, Roo Code, Kiro, Factory, JetBrains Junie, Letta,
Firebender, Tabnine, Trae, Mistral Vibe, Snowflake Cortex Code, Databricks Genie Code e
outras — todas suportam o padrão.

A maioria lê um destes caminhos, em ordem aproximada de adoção:

```
~/.agents/skills/        # a convenção que está virando padrão entre ferramentas
~/.claude/skills/        # amplamente suportado como alternativa
<específico-da-ferramenta>/skills/  # ex.: ~/.gemini/skills/, ~/.cursor/skills/
```

Coloque a pasta `feynman-technique` no caminho que a sua ferramenta documentar. A lista
completa de clientes está em [agentskills.io/clients](https://agentskills.io/clients).

</details>

<details>
<summary id="qualquer-outra-ia-sem-suporte-a-skills"><b>Qualquer outra IA (sem suporte a skills)</b></summary>

A skill é Markdown puro, então funciona como prompt de sistema em qualquer lugar.

- **GPT personalizado / Gem / Assistant:** cole
  [`skills/feynman-technique/SKILL.md`](../../skills/feynman-technique/SKILL.md)
  (sem o bloco YAML do topo) no campo de instruções. Envie os arquivos de `references/`
  como arquivos de conhecimento.
- **Projeto / instruções personalizadas:** o mesmo, na caixa de instruções personalizadas
  do seu projeto.
- **Uso avulso:** cole o arquivo no chat e acrescente *"Siga isto pelo resto da nossa
  conversa."*

</details>

### Verifique se funcionou

Peça algo que você já entende bem:

```
/feynman-technique o que é uma função hash?
```

Uma resposta correta abre com uma tese de uma frase, depois vem um nível 0 **sem nenhuma
palavra técnica**, e termina com uma seção "onde a imagem quebra". Se abrir com "Uma função
hash é uma função que mapeia dados de tamanho arbitrário…", a skill não carregou.

---

## O que você recebe de volta

```
**Em uma frase:** ...           ← para um especialista poder parar de ler aqui

**A imagem que fica:** ...      ← a analogia mestra

0 · Churrasco de domingo   nenhum conhecimento da área. Zero termos técnicos.
1 · Recém-chegado          os nomes reais, amarrados na imagem do nível 0
2 · Profissional           como as peças se encaixam, e o primeiro trade-off de verdade
3 · Mantenedor             modos de falha, o que quebra, o que foi descartado e por quê
4 · Especialista           bordas, escala e os limites do próprio modelo

Onde a imagem quebra           ← os limites de toda analogia, declarados
Palavras novas desta resposta  ← uma linha por termo novo
O que eu deixei de fora        ← nomeado, não omitido em silêncio
```

Os níveis encolhem; nunca somem. Pergunta estreita recebe **forma compacta**: tese, imagem e
o único nível que importa. Arrastar um especialista pelos cinco níveis não é rigor — isso
*piora* a compreensão dele, e de forma mensurável (o
[efeito de reversão da expertise](../../skills/feynman-technique/references/evidence.md)).

Veja um [exemplo completo resolvido](../../skills/feynman-technique/assets/worked-example.md) —
"o que é um índice de banco de dados?" respondido por inteiro e depois anotado, mostrando o
que cada parte está fazendo.

---

## Modo treinador — o que realmente te ensina

```
/feynman-technique me questione sobre como o TCP lida com congestionamento
/feynman-technique quero checar se eu realmente entendo event sourcing
```

Aqui a skill se recusa a explicar. Quem explica é **você**; ela escuta atrás de vaguezas, de
termos técnicos usados como ponto final e de passos afirmados sem mecanismo — e aponta
exatamente uma lacuna de cada vez, sem entregar a resposta.

É o modo com a pesquisa mais sólida por trás. Quem se prepara para ensinar tem desempenho
melhor do que quem se prepara para a prova — *mesmo quando o ensino nunca acontece*
(Nestojko et al., 2014). Produzir a própria explicação vale mais do que ler a de outra
pessoa (Chi et al., 1989).

---

## As regras que ela segue

| | Prompt comum de "explique de forma simples" | Esta skill |
|---|---|---|
| **Jargão** | frases mais simples, mesmos termos | todo termo novo explicado no primeiro uso, ou não aparece |
| **Analogias** | uma metáfora nova por parágrafo | uma analogia mestra, que vai ganhando complicação — **e onde ela quebra** |
| **Precisão** | simplificada até ficar errada | aproximações marcadas *com seus limites* |
| **Profundidade** | um nível só, sem relevo | uma escada em que você para no degrau que quiser |
| **Especialistas** | tratados com condescendência | tese na primeira linha, depois forma compacta |
| **Nomes** | o nome *é* a resposta | mecanismo primeiro, nome por último |
| **Ignorância** | passa batido | "ninguém sabe" dito com todas as letras, quando for verdade |
| **Aprendizado** | explica *para* você | o modo treinador faz *você* explicar e encontra as suas lacunas |

Regra zero: **ser claro nunca é desculpa para estar errado.** Se simplificar for distorcer,
a skill diz isso, dá os limites e entrega a versão exata um degrau acima.

---

## Por dentro

Os arquivos da skill estão em inglês, para manter o frontmatter canônico.

| Arquivo | Conteúdo |
|---|---|
| [**SKILL.md**](../../skills/feynman-technique/SKILL.md) | A skill em si. Comece por aqui. |
| [references/voice.md](../../skills/feynman-technique/references/voice.md) | Análise forense do estilo de Feynman, com estatísticas do corpus |
| [references/ladder.md](../../skills/feynman-technique/references/ladder.md) | Calibração dos níveis e como adaptar o formato |
| [references/analogies.md](../../skills/feynman-technique/references/analogies.md) | Como construir, estender e testar analogias sob estresse |
| [references/failure-modes.md](../../skills/feynman-technique/references/failure-modes.md) | 14 jeitos de uma explicação falhar, cada um com uma reescrita |
| [references/evidence.md](../../skills/feynman-technique/references/evidence.md) | A ciência do aprendizado — e onde este método realmente falha |
| [references/sources.md](../../skills/feynman-technique/references/sources.md) | Citações verificadas, e as que são falsamente atribuídas a ele |
| [assets/worked-example.md](../../skills/feynman-technique/assets/worked-example.md) | Uma resposta completa, anotada |
| [assets/checklist.md](../../skills/feynman-technique/assets/checklist.md) | A auditoria antes de enviar |

### Da análise forense do estilo

De [voice.md](../../skills/feynman-technique/references/voice.md), tudo medido no corpus de
88.000 palavras:

- **A assinatura é a variação brusca.** A frase mediana tem ≈ 20 palavras — mas ~1 em cada 8
  fica abaixo de oito, e ~1 em cada 6 passa de trinta e cinco. Ele constrói longo e aterrissa
  curto. *"Shake this one, that one shakes later."*
- **Os pronomes mudam conforme a função.** "We" ao ensinar (19,95 por 1.000 palavras em
  *Six Easy Pieces*, dez vezes mais do que o "I" dele), "I" ao admitir confusão (26,7/1k na
  Palestra do Nobel), "you" ao instruir (20,6/1k em *Cargo Cult Science*).
- **Verbos que o corpo sente.** *jiggle* 27, *pull* 37, *push* 28, *shake* 20. As moléculas
  *chacoalham*; elas não "exibem agitação térmica".
- **"Basically" aparece zero vezes em 88.000 palavras.** *Trivial* aparece uma. É por isso
  que a skill proíbe essas palavras — medição, não gosto pessoal.

---

## Limitações honestas

A regra zero vale para esta página também.

- **Feynman não inventou a "Técnica de Feynman".** Ele nunca publicou um método de quatro
  passos com esse nome. Os quatro passos foram montados por divulgadores posteriores,
  principalmente Scott H. Young, por volta de 2011, como uma reconstrução justa. Esta skill
  usa os testes *documentados* dele, e diz isso.
- **"Se você não consegue explicar de forma simples, você não entendeu"** não tem fonte
  primária — nem em Feynman nem em Einstein.
  [sources.md](../../skills/feynman-technique/references/sources.md) lista o que ele
  comprovadamente disse e o que não disse.
- **Algumas coisas não simplificam.** O próprio Feynman bateu nesse muro: quando o pai
  perguntou como um fóton sai de um átomo sem nunca ter estado lá dentro, ele respondeu
  *"I'm sorry; I don't know. I can't explain it to you."* A skill foi feita para dar essa
  resposta em vez de inventar uma imagem.
- **Custa tokens e tempo.** Para uma consulta rápida, o certo é a forma compacta — ou skill
  nenhuma.
- **Faz pouco por memorização e habilidade motora.** O alvo dela é entendimento causal, de
  mecanismo. Vocabulário e atalhos de teclado pedem recuperação espaçada, não explicação.
- **Uma boa explicação *dá a sensação* de compreensão.** A sensação não é prova. Quando isso
  importa, use o modo treinador.

---

## Créditos e direitos autorais

Richard P. Feynman (1918–1988) escreveu tudo que vale a pena ler aqui. Este repositório traz
**regras derivadas e citações curtas com atribuição**, para análise e ensino — e não
redistribui a obra dele.

Os textos continuam sob direitos autorais: *The Feynman Lectures on Physics* é livre para
*leitura* em [feynmanlectures.caltech.edu](https://www.feynmanlectures.caltech.edu/), mas é
© Caltech e **não é domínio público**. Se você fizer um fork, mantenha assim: cite pouco,
sempre atribua, nunca cole capítulos. Toda a procedência está em
[sources.md](../../skills/feynman-technique/references/sources.md).

Esta skill começou como `feynman-reply`, uma skill em português de
[@guicortei](https://github.com/guicortei). Foi reconstruída a partir de fontes primárias,
deixou de valer só para software e ganhou a análise de estilo, a base de evidências e o modo
treinador — e então virou `feynman-technique`.

Sem vínculo e sem endosso do espólio de Feynman, da Caltech ou da Anthropic.

## Contribuindo

Melhorias são bem-vindas — especialmente:

- exemplos resolvidos de outras áreas (medicina, direito, finanças, biologia)
- modos de falha encontrados em uso real
- correções em qualquer citação ou atribuição

Veja [CONTRIBUTING.md](../../CONTRIBUTING.md). Um pedido: se você acrescentar alguma
afirmação sobre Feynman, cite a fonte primária. Invocar o nome dele em nome da honestidade
intelectual e ser relaxado com atribuição é o único bug imperdoável deste repositório.

## Licença

[MIT](../../LICENSE). Use, faça fork, publique.

---

<div align="center">

> *"The first principle is that you must not fool yourself — and you are the easiest person
> to fool."*
> — Richard Feynman, *Cargo Cult Science*, 1974
>
> *"O primeiro princípio é que você não deve enganar a si mesmo — e você é a pessoa mais
> fácil de enganar."*

**[⭐ Dê uma estrela no repositório](https://github.com/guicortei/feynman-technique)** se ele
mudou alguma resposta que você recebeu hoje.

</div>
