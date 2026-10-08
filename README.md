# Skills do Lazzari & Ghidorsi Advogados

Fonte oficial das skills do escritório: cada skill é escrita, testada e
versionada aqui e depois instalada no claude.ai.

## Estrutura

```
compartilhado/            fonte única do que várias skills usam
  guia-redacao.md         padrão de escrita das peças (extraído de peças reais)
  registro-caso.md        formato do bloco REGISTRO-CASO (alimenta o painel)
  gerar_peca.py           gera a peça .docx no timbrado + revisão automática
  timbrado-peca.docx      timbrado das peças processuais
skills/<nome>/            uma pasta por skill, pronta para empacotar
  SKILL.md
  compartilhado.txt       quais arquivos de compartilhado/ a skill recebe
  references/ scripts/ assets/
ferramentas/
  sincronizar.py          copia o compartilhado, valida e gera dist/<nome>.zip
```

Nunca edite a cópia de um arquivo compartilhado dentro de `skills/`: edite em
`compartilhado/` e rode o sincronizador, que atualiza todas as skills.

## Como operar

1. **Gerar o pacote:** `python3 ferramentas/sincronizar.py` cria
   `dist/<nome>.zip` para cada skill (a pasta `dist/` não vai para o GitHub).
2. **Instalar:** no claude.ai, Configurações → Capacidades → Skills → enviar o
   `.zip`. Para atualizar uma skill, enviar o novo `.zip` com o mesmo nome.
3. **Usar:** num chat (de preferência dentro do Projeto do escritório), enviar
   os documentos e pedir a tarefa. A skill dispara sozinha.
4. **Registrar:** ao final, a skill entrega um bloco `REGISTRO-CASO`. Copie e
   cole no Painel de Casos para manter a carteira atualizada.

## Linha de trabalho

```
Recuperação de crédito
  avaliacao-documentos-cobranca ─HANDOFF-COBRANCA─> peticao-inicial-cobranca ─┐
  geracao-propostas ─REGISTRO-TRATATIVA─> formalizacao-acordo                  ├─REGISTRO-CASO─> Painel de Casos
Contencioso                                                                     │
  avaliacao-processual ─HANDOFF-DEFESA─> elaboracao-defesas / recursos ────────┘
```

## Roteiro

| # | Item | Situação |
|---|---|---|
| a | `peticao-inicial-cobranca` | pronta para teste |
| b | `formalizacao-acordo` | a fazer |
| d | `elaboracao-recursos` | a fazer |
| e | `cumprimento-sentenca` | a fazer |
| f | `relatorio-cliente` | a fazer |
| g | monitor de jurisprudência → posts | a fazer |
| h | revisão de prescrição da carteira | a fazer |
| i | acompanhamento de acordos | a fazer |
| j | `onboarding-cliente` | a fazer |
| k | painel da carteira | a fazer (formato do registro já definido) |
| l | `notificacao-extrajudicial` | a fazer |

## Privacidade

Este repositório não guarda peças de clientes. Os exemplos são anonimizados.
Peças reais enviadas como modelo ficam só na conversa.
