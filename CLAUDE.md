# CLAUDE.md

Contexto fixo lido automaticamente pelo Claude Code em toda sessão neste repositório.

## Escritório

- **Nome:** Lazzari & Ghidorsi Advogados
- **Cidade:** Concórdia/SC
- **Contato do usuário:** sghidorsi.adv@gmail.com

## Áreas de atuação

- Direito bancário (inclusive recuperação de crédito para cooperativas como SICOOB e CRESOL)
- Direito do consumidor
- Direito empresarial
- Direito cível

## Skills disponíveis e quando usar

| Tarefa | Skill |
| --- | --- |
| Analisar a íntegra de um processo e avaliar os riscos | `avaliacao-processual` |
| Redigir contestação, embargos, impugnação, réplica ou manifestação | `elaboracao-defesas` |
| Triagem de títulos e documentos de dívida para cobrança | `avaliacao-documentos-cobranca` |
| Petição inicial de execução, monitória ou cobrança | `peticao-inicial-cobranca` |
| Proposta de renegociação (Price, convenção Sisbr 2.0) | `geracao-propostas` |
| Procuração e contrato de honorários | `procuracao-contrato` |
| Posts para Instagram ou LinkedIn do escritório | `posts-lazzari-ghidorsi` |

Fluxos encadeados:
- `avaliacao-processual` → bloco HANDOFF-DEFESA → `elaboracao-defesas`
- `avaliacao-documentos-cobranca` → bloco HANDOFF-COBRANCA → `peticao-inicial-cobranca` → REGISTRO-CASO

## Repositório de skills

Este repositório é a fonte das skills do escritório (ver `README.md`).
- Padrão de redação de toda peça: `compartilhado/guia-redacao.md`.
- Arquivos em `compartilhado/` são editados ali e propagados com
  `python3 ferramentas/sincronizar.py`; nunca editar a cópia dentro de `skills/`.
- Toda skill nova que redige peça recebe `guia-redacao.md`, `gerar_peca.py` e o
  timbrado, e termina a entrega com o bloco `REGISTRO-CASO`.
- O repositório é público: não commitar peças, nomes, CPFs ou números de
  processo de clientes. Exemplos sempre anonimizados.

## Preferências de trabalho

- Responder sempre em português do Brasil.
- Linguagem jurídica técnica, elegante e sem enchimento.
- Tribunal de referência: TJSC (e STJ para súmulas e temas repetitivos).

## A preencher

<!-- Complete com o que quiser que o Claude sempre saiba. -->
- Sócios / advogados e OABs:
- Endereço do escritório:
- Clientes recorrentes:
- Preferências de formatação de peças:
- Outras observações:
