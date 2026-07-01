# GWD - Get Work Done

```text
   _____ __        ______
  / ____|\ \      / / __ \
 | |  __  \ \ /\ / / |  | |
 | | |_ |  \ V  V /| |  | |
 | |__| |   \_/\_/ | |__| |
  \_____|          |_____/

        GET WORK DONE
```

GWD e um metodo de organizacao e execucao para tirar compromissos da cabeca, transformar ideias em proximas acoes e manter a vida em movimento.

Ele combina dois movimentos:

```text
1. Controle     -> clarear o que esta puxando sua atencao agora
2. Perspectiva  -> conectar a execucao com areas, metas, visao e principios
```

## Workflow GWD

```text
+---------+     +-----------+     +----------+     +---------+     +---------+
| CAPTURE | --> | CLARIFY   | --> | ORGANIZE | --> | REFLECT | --> | ENGAGE  |
+---------+     +-----------+     +----------+     +---------+     +---------+
     ^                                                                     |
     |_____________________________________________________________________|
```

## Horizontes de foco

```text
                 +--------------------------------+
                 | H5  PROPOSITO + PRINCIPIOS    |  /gwd-purpose
                 +--------------------------------+
                 | H4  VISAO 3-5 ANOS            |  /gwd-vision
                 +--------------------------------+
                 | H3  METAS 3M-2A               |  /gwd-goals
                 +--------------------------------+
                 | H2  AREAS DE FOCO             |  /gwd-areas
                 +--------------------------------+
                 | H1  PROJETOS                  |  /gwd-project
                 +--------------------------------+
                 | H0  PROXIMAS ACOES            |  /gwd-next
                 +--------------------------------+
```

A pratica recomendada e de baixo para cima: primeiro controle o que esta incomodando, depois suba para as decisoes maiores.

## Workflow + comandos

| Etapa | Objetivo | Comandos |
|---|---|---|
| Setup | Montar sistema e primeiro sweep | `/gwd-setup` |
| Capture | Tirar tudo da cabeca | `/gwd-capture`, `/gwd-sweep` |
| Clarify | Decidir o que cada item significa | `/gwd-clarify`, `/gwd-process` |
| Organize | Colocar cada coisa no lugar certo | `/gwd-process`, `/gwd-project`, `/gwd-waiting`, `/gwd-someday` |
| Reflect | Revisar e manter confianca | `/gwd-review`, `/gwd-weekly`, `/gwd-horizons` |
| Engage | Escolher e executar | `/gwd-today`, `/gwd-plan`, `/gwd-next`, `/gwd-start`, `/gwd-done` |
| Align | Checar coerencia vertical | `/gwd-align` |

## Arquivos principais

```text
./
|-- inbox.md                  # captura bruta
|-- next-actions.md           # H0 proximas acoes
|-- projects.md               # H1 projetos
|-- areas.md                  # H2 areas de foco
|-- goals.md                  # H3 metas e objetivos
|-- vision.md                 # H4 visao 3-5 anos
|-- purpose.md                # H5 proposito e principios
|-- horizons.md               # mapa geral
|-- waiting-for.md
|-- someday-maybe.md
|-- calendar.md
|-- daily/
|-- reviews/
|-- projects/
|   |-- active/
|   `-- archived/
`-- reference/
```

## Scripts token-saver

A skill inclui scripts read-only para consultar o sistema sem carregar arquivos grandes no contexto.

```text
.agents/skills/gwd/scripts/gwd-query status --root . --format json
.agents/skills/gwd/scripts/gwd-query next --root . --context @computer --time 30
.agents/skills/gwd/scripts/gwd-query horizons --root .
.agents/skills/gwd/scripts/gwd-query review --root . --type weekly
```

Regra: usar `gwd-query` para resumos; ler markdown completo so antes de editar, quando houver ambiguidades, ou quando voce pedir detalhes integrais.

Padrao dos arquivos: `SCHEMA.md`.

## Setup

Cria a base do sistema e inicia automaticamente o primeiro sweep.

Antes de perguntar, GWD pode analisar arquivos locais uteis na pasta atual: `.md`, `.txt`, `.csv`, exports de tarefas, planos e notas.

```text
/gwd-setup Quero organizar trabalho, saude, familia e projetos pessoais
/gwd-setup use tarefas.csv e minhas-notas.md como referencia
```

## Sweep

O sweep entrevista por ramos e recomenda uma resposta para cada pergunta.

```text
/gwd-sweep all
/gwd-sweep trabalho
/gwd-sweep all usando tarefas.csv como referencia
```

Ramos:

```text
open loops -> actions -> projects -> areas -> goals -> vision -> purpose
```

## Alinhamento

`/gwd-align` checa se uma acao, projeto ou objetivo conversa com os horizontes superiores.

```text
/gwd-align projeto Criar canal no YouTube
/gwd-align next action escrever roteiro do video
/gwd-align all
```

Ele tambem deve rodar automaticamente em:

```text
/gwd-project
/gwd-review monthly
/gwd-review quarterly
/gwd-setup
/gwd-sweep quando surgir um compromisso grande
```

## Loop diario

```text
Morning
  /gwd-today

During the day
  /gwd-capture
  /gwd-next
  /gwd-start
  /gwd-done

Shutdown
  /gwd-process inbox
  /gwd-review daily
```

## Loop semanal

```text
/gwd-weekly
  -> inbox zero
  -> projetos com proxima acao
  -> waiting-for revisado
  -> areas conferidas
  -> foco da semana definido
```

## Loop mensal/trimestral

```text
/gwd-review monthly
  -> areas + metas + alinhamento dos projetos

/gwd-review quarterly
  -> metas + visao + proposito + simplificacao
```

## Comandos

```text
/gwd           router/status geral
/gwd-setup     inicializa sistema e roda primeiro sweep
/gwd-capture   captura itens crus
/gwd-clarify   esclarece um item
/gwd-process   processa o inbox
/gwd-plan      planeja dia ou semana
/gwd-today     cria plano diario compacto
/gwd-next      escolhe a melhor proxima acao
/gwd-start     quebra uma acao em passos executaveis
/gwd-done      registra conclusao
/gwd-project   cria/revisa projeto
/gwd-areas     revisa areas de foco
/gwd-goals     revisa metas 3 meses-2 anos
/gwd-vision    revisa visao 3-5 anos
/gwd-purpose   revisa proposito e principios
/gwd-horizons  mostra piramide, gaps e status
/gwd-align     checa alinhamento vertical
/gwd-waiting   gerencia aguardando/respostas/delegados
/gwd-someday   gerencia talvez/futuro
/gwd-review    roda revisao diaria/semanal/mensal/trimestral
/gwd-weekly    roda revisao semanal completa
/gwd-sweep     faz varredura mental por horizontes
/gwd-reset     arquiva/reseta com confirmacao segura
```
