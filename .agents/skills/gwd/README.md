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

GWD e um metodo de organização e execucao para tirar compromissos da cabeca, transformar ideias em próximas ações e manter a vida em movimento.

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

A prática recomendada é de baixo para cima: primeiro controle o que está incomodando, depois suba para as decisões maiores.

## Workflow + comandos

| Etapa | Objetivo | Comandos |
|---|---|---|
| Summary | Ver painel geral bonito | `/gwd-summary` |
| Setup | Montar sistema e primeiro sweep | `/gwd-setup` |
| Capture | Tirar tudo da cabeça | `/gwd-capture`, `/gwd-sweep` |
| Clarify | Decidir o que cada item significa | `/gwd-clarify`, `/gwd-refine`, `/gwd-process` |
| Organize | Colocar cada coisa no lugar certo | `/gwd-process`, `/gwd-project`, `/gwd-waiting`, `/gwd-someday` |
| Reflect | Revisar e manter confiança | `/gwd-review`, `/gwd-weekly`, `/gwd-horizons` |
| Engage | Escolher e executar | `/gwd-today`, `/gwd-plan`, `/gwd-next`, `/gwd-start`, `/gwd-done` |
| Align | Checar coerência vertical | `/gwd-align` |

## Arquivos principais

```text
./
|-- inbox.md                  # tabela de capturas com título e descrição
|-- next-actions.md           # H0 próximas ações
|-- projects.md               # H1 projetos
|-- areas.md                  # H2 áreas de foco
|-- goals.md                  # H3 metas e objetivos
|-- vision.md                 # H4 visão 3-5 anos
|-- purpose.md                # H5 propósito e princípios
|-- horizons.md               # mapa geral
|-- gwd-memory.md             # memória operacional
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
.agents/skills/gwd/scripts/gwd-query summary --root . --format md
.agents/skills/gwd/scripts/gwd-query status --root . --format json
.agents/skills/gwd/scripts/gwd-query next --root . --context @computer --time 30
.agents/skills/gwd/scripts/gwd-query horizons --root .
.agents/skills/gwd/scripts/gwd-query review --root . --type weekly
```

Regra: usar `gwd-query` para resumos; ler markdown completo só antes de editar, quando houver ambiguidades, ou quando você pedir detalhes integrais.

Padrão dos arquivos: `SCHEMA.md`.

## Summary

Use `/gwd-summary` para um painel visual das tarefas principais, estado dos horizontes, projetos com problemas, follow-ups vencidos, gaps e próximo comando.

```text
/gwd-summary
/gwd-summary today
/gwd-summary week
```

O comando deve caprichar no visual: banners, caixas ASCII e secoes curtas.

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

`/gwd-align` checa se uma ação, projeto ou objetivo conversa com os horizontes superiores.

`horizons.md` e um snapshot derivado da piramide. Ele deve ser atualizado por `/gwd-horizons`, `/gwd-align all`, final do setup, revisoes mensal/trimestral, e mudancas grandes em areas/metas/visao/proposito/projetos.

```text
/gwd-align projeto Criar canal no YouTube
/gwd-align next action escrever roteiro do video
/gwd-align all
```

Ele também deve rodar automaticamente em:

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
  -> projetos com próxima ação
  -> waiting-for revisado
  -> areas conferidas
  -> foco da semana definido
```

## Loop mensal/trimestral

```text
/gwd-review monthly
  -> areas + metas + alinhamento dos projetos

/gwd-review quarterly
  -> metas + visao + proposito + simplificação
```

## Comandos

```text
/gwd           router/status geral
/gwd-summary   painel visual com tarefas, projetos e horizontes
/gwd-setup     inicializa sistema e roda primeiro sweep
/gwd-capture   captura itens crus
/gwd-clarify   esclarece um item
/gwd-process   processa o inbox
/gwd-plan      planeja dia ou semana
/gwd-today     cria plano diario compacto
/gwd-next      escolhe a melhor próxima ação
/gwd-start     quebra uma ação em passos executaveis
/gwd-done      registra conclusão; também por intenção natural
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
/gwd-reset     arquiva/reseta com confirmação segura
```
