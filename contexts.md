# Contextos identificáveis

Locais e situações cadastrados pelo usuário para ajudar a inferir onde ele está agora.
A lista começa vazia e é criada inteiramente pelo usuário.

Etiquetas genéricas de próximas ações, como `@phone`, `@computer` ou `@online`, não precisam ser cadastradas aqui. Este arquivo serve para contextos pessoais identificáveis por sinais, como casa, trabalho, escritório ou estúdio.

## Colunas

- `Contexto`: nome único iniciado por `@`. Ex.: `@casa`, `@trabalho`.
- `Definição`: significado do contexto e quando ele se aplica.
- `Sinais fortes`: evidências confirmadas pelo usuário que indicam esse contexto. Ex.: hostname específico, endereço ou localização confirmada.
- `Sinais auxiliares`: indícios úteis, porém inconclusivos. Ex.: cidade obtida pelo IP, provedor de internet, horário ou nome da rede.
- `Capacidades`: recursos disponíveis nesse contexto. Ex.: VPN corporativa, impressora, dois monitores ou ferramentas.
- `Restrições`: ações impossíveis ou inadequadas nesse contexto. Ex.: ausência de acesso corporativo ou impossibilidade de fazer ligações.
- `Estado`: `ativo` para permitir inferências; `arquivado` para manter o histórico sem usar o contexto em novas inferências.

## Exemplo

O exemplo abaixo é apenas ilustrativo. Não o copie automaticamente para a tabela.

| Contexto | Definição | Sinais fortes | Sinais auxiliares | Capacidades | Restrições | Estado |
|---|---|---|---|---|---|---|
| @trabalho | Escritório onde realizo trabalho profissional | hostname `notebook-empresa`; localização confirmada no escritório | cidade compatível; horário comercial | VPN corporativa, impressora, dois monitores | sem acesso a recursos domésticos | ativo |
| @casa-antiga | Residência anterior | endereço antigo confirmado | provedor usado anteriormente | scanner | não moro mais nesse local | arquivado |

## Contextos cadastrados

| Contexto | Definição | Sinais fortes | Sinais auxiliares | Capacidades | Restrições | Estado |
|---|---|---|---|---|---|---|
