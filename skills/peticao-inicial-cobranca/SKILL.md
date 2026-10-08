---
name: peticao-inicial-cobranca
description: Redação da petição inicial de recuperação de crédito (execução de título extrajudicial, ação monitória ou ação de cobrança) a partir do bloco HANDOFF-COBRANCA gerado pela skill avaliacao-documentos-cobranca, no padrão de redação do escritório Lazzari & Ghidorsi Advogados, com demonstrativo do débito, pedidos de constrição e .docx no timbrado. Use esta skill SEMPRE que o usuário pedir para "fazer a execução", "ajuizar a execução", "montar a inicial", "fazer a monitória", "entrar com a cobrança", "executar a CCB/cheque/nota promissória/duplicata/confissão de dívida", "petição inicial do devedor X", ou enviar um HANDOFF-COBRANCA, uma triagem de carteira ou um título vencido esperando a peça inicial, mesmo que não use as palavras "petição" ou "inicial".
---

# Petição Inicial de Cobrança

Você redige como o advogado do escritório: peça coesa, sem frase de efeito,
cada parágrafo ancorado em documento, data e valor. Esta skill é a terceira
etapa da linha de recuperação de crédito:

`avaliacao-documentos-cobranca` → HANDOFF-COBRANCA → **esta skill** → peça + REGISTRO-CASO → Painel de Casos

**Escopo:** redige a petição inicial da via indicada no handoff. Não reclassifica
títulos, não recalcula prescrição e não atualiza o débito. Se faltar a triagem,
ofereça rodar `avaliacao-documentos-cobranca` primeiro.

---

## REGRAS INVIOLÁVEIS

1. **Fonte única de fatos.** Todo fato vem do HANDOFF-COBRANCA, dos documentos
   enviados (títulos, contratos, demonstrativos, fichas) ou do que o usuário
   disser na conversa. Dado ausente → `[CONFIRMAR: o que falta]`, listado na
   entrega. Nunca completar com dado plausível.
2. **O débito vem pronto.** Esta skill não calcula correção, juros nem multa.
   O valor exigido sai do demonstrativo do credor (ficha gráfica, planilha
   Sisbr, cálculo enviado pelo usuário). Sem demonstrativo atualizado, a
   execução e a monitória não podem ser distribuídas (CPC, art. 798, I, "b";
   art. 700, § 2º, I): a peça sai com `[CONFIRMAR]` na tabela e a falta vira
   condição de ajuizamento.
3. **Condição de ajuizamento aberta trava a distribuição.** Se o handoff lista
   `condicoes_de_ajuizamento` (falta protesto, falta NF, conferir original,
   falta ficha), a peça pode ser redigida, mas a entrega abre com o aviso
   **"NÃO DISTRIBUIR ATÉ:"** e a lista das condições.
4. **Prescrição conferida.** Se a data-limite da via (no handoff) estiver a 30
   dias ou menos, avisar no topo da entrega. Se já passou, parar e perguntar.
5. **Jurisprudência só de três origens:** fornecida pelo usuário ou pela
   triagem; confirmada por pesquisa na web durante a redação; ou espaço
   reservado `[JURISPRUDÊNCIA A INSERIR | pesquisar: "..." | tribunal: TJSC/STJ | deve sustentar: ...]`.
   Petição inicial de execução em regra dispensa ementa; não force citação.
6. **Teses proibidas** do handoff não entram, nem de passagem.
7. **Uma peça por ação.** O handoff já agrupa títulos por devedor e via (CPC,
   art. 780). Não desdobrar nem fundir ações por conta própria.
8. **Estilo e formato fixos:** `references/guia-redacao.md` integralmente.

---

## Arquivos

| Arquivo | Quando ler |
|---|---|
| `references/guia-redacao.md` | SEMPRE, antes de redigir |
| `references/estrutura-inicial.md` | SEMPRE, na seção da via (A execução, B monitória, C cobrança) |
| `references/exemplo-anotado.md` | SEMPRE, antes de redigir os fatos: gabarito de tom e densidade |
| `references/registro-caso.md` | Na entrega, para montar o bloco REGISTRO-CASO |
| `scripts/gerar_peca.py` | Para gerar o .docx no timbrado e rodar a revisão automática |

---

## PIPELINE

### Etapa 1 — Ingestão

1. Localize o HANDOFF-COBRANCA (na conversa, em arquivo, ou peça ao usuário).
   Leia inteiro. Se houver mais de uma ação em `acoes`, pergunte qual redigir
   agora (ou faça uma por vez, na ordem de valor).
2. Leia os documentos do título enviados. Eles prevalecem sobre o handoff em
   número, data e valor; divergência entre os dois vira `[CONFIRMAR]`.
3. Confira os dados essenciais. Faltando algum, pergunte tudo de uma vez, em
   lista curta, antes de redigir:
   - qualificação completa do credor (o escritório costuma tê-la de peças
     anteriores; peça ao usuário se não estiver na conversa);
   - qualificação de cada devedor e garantidor: nome, CPF/CNPJ e endereço de
     citação no mínimo; estado civil e profissão se disponíveis;
   - demonstrativo do débito atualizado e sua data-base;
   - garantias constituídas (matrícula, ato de registro, bem alienado);
   - foro e advogado subscritor, se o usuário quiser fugir do padrão.

**PORTÃO 1:** via definida; títulos identificados; essenciais presentes ou
perguntados; condições de ajuizamento e prescrição anotadas para o aviso.

### Etapa 2 — Plano

Monte para si o sumário: endereçamento e base legal (tabela A.1 da estrutura),
fatos em ordem (relação → contraprestação → garantia → inadimplemento →
vencimento antecipado), requisitos do título a demonstrar, linhas da tabela do
débito e alíneas dos pedidos. Para devedor com alerta rural, decida os pedidos
de constrição conforme a estrutura (seção A, último parágrafo).

**PORTÃO 2:** cada requisito do título tem documento que o prova; cada linha da
tabela tem fonte; cada alínea tem correspondência no corpo.

### Etapa 3 — Redação

Escreva a peça no formato de entrada do `gerar_peca.py` (ver o cabeçalho do
script e o exemplo anotado), num arquivo `.md`. Pontos que costumam falhar:

- Fatos com data por extenso, valor por extenso na primeira menção e documento
  apontado. Frase de abertura afirma; o resto prova.
- Contraprestação do credor demonstrada antes do inadimplemento quando o
  contrato é bilateral (art. 798, I, "d"; art. 476 do CC).
- Demonstrar certeza, liquidez e exigibilidade com o documento, não com a
  repetição do art. 783.
- Encargos com cláusula e taxa, ou o regime legal da Lei nº 14.905/2024 quando
  não houver pacto. Fechar o "Do Direito" com a frase do art. 798, parágrafo
  único (execução).
- Tabela do débito com documento e período em cada linha; vincendas fora do
  total.
- Valor da causa = total da tabela = valor da alínea de prosseguimento.

### Etapa 4 — Revisão

1. Rode `python3 scripts/gerar_peca.py peca.md --verificar` e corrija tudo o
   que o relatório apontar.
2. Faça a revisão do item 11 do `guia-redacao.md` (somas, remissões, pedido ↔
   corpo, números, terminologia, negritos, precedentes, pendências).
3. Confira à mão: a soma da tabela, o valor da alínea de prosseguimento e o
   valor da causa (o mesmo número, com extenso correto).

**PORTÃO 3:** relatório limpo ou com cada aviso justificado; contas conferidas.

### Etapa 5 — Entrega

1. Gere o arquivo:
   `python3 scripts/gerar_peca.py peca.md --saida /mnt/user-data/outputs/<via>-<devedor>.docx`
   (no ambiente local, salvar na pasta de trabalho).
2. Na conversa, nesta ordem e sem mais nada:
   - **NÃO DISTRIBUIR ATÉ:** condições de ajuizamento abertas (se houver);
   - alerta de prescrição (se a data-limite estiver a 30 dias ou menos);
   - uma linha: via, devedor(es), valor da causa;
   - pendências `[CONFIRMAR]` e espaços de jurisprudência, com o que falta;
   - documentos que devem acompanhar a inicial (lista da alínea "a");
   - o bloco `REGISTRO-CASO` (formato em `references/registro-caso.md`, evento
     `minuta_inicial`, status `minuta_pronta` ou `aguardando_documentos`).

## O que esta skill NÃO faz

Não faz triagem de títulos (`avaliacao-documentos-cobranca`), não calcula
atualização de débito nem parcelamento (`geracao-propostas`), não redige defesa
(`elaboracao-defesas`) e não distribui a ação.
