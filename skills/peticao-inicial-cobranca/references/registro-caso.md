# Bloco REGISTRO-CASO

Formato único com que todas as skills do escritório registram um caso, ou um
evento de um caso, no **Painel de Casos** (a tela no Claude). O usuário copia o
bloco e cola na caixa "Importar registro" do painel; o painel lê o JSON, cria ou
atualiza o caso pela `chave` e acrescenta o evento ao histórico.

Regras:
- Sempre JSON válido, dentro de um bloco de código com a etiqueta
  `REGISTRO-CASO`, ao final da entrega.
- Valores monetários como número (ponto decimal, sem "R$"): `220300.00`.
- Datas em `aaaa-mm-dd`.
- Campo desconhecido: `null`. Nunca inventar.
- `chave` identifica o caso: `<cpf/cnpj do devedor só dígitos>-<via>-<credor curto>`
  (ex.: `00000000000-execucao-cresol`). O mesmo caso, em skills diferentes,
  usa sempre a mesma chave.

```REGISTRO-CASO
{
  "registro": "1.0",
  "chave": "00000000000-execucao-cresol",
  "evento": "minuta_inicial",
  "data_evento": "2026-10-08",
  "skill": "peticao-inicial-cobranca",
  "credor": {"nome": "", "cpf_cnpj": ""},
  "devedores": [
    {"nome": "", "cpf_cnpj": "", "papel": "emitente|avalista|executado|requerido", "rural": false}
  ],
  "via": "execucao|monitoria|cobranca",
  "titulos": [
    {"tipo": "", "numero": "", "emissao": null, "vencimento": null, "valor_face": 0.00}
  ],
  "valor_causa": 0.00,
  "data_base_debito": null,
  "foro": "",
  "processo": null,
  "status": "minuta_pronta|aguardando_documentos|ajuizado|citado|acordo|encerrado",
  "prazos": [
    {"tipo": "prescricao_executiva|prescricao_subsidiaria|processual|acordo_parcela", "data": null, "descricao": ""}
  ],
  "pendencias": [
    {"o_que": "", "quem": "credor|escritorio", "trava": true}
  ],
  "proximo_passo": "",
  "observacoes": ""
}
```

Eventos previstos (cada skill usa o seu):

| evento | skill |
|---|---|
| `triagem` | avaliacao-documentos-cobranca |
| `minuta_inicial` | peticao-inicial-cobranca |
| `proposta` | geracao-propostas |
| `acordo_formalizado` | formalizacao-acordo |
| `parcela_paga` / `parcela_atrasada` | acompanhamento de acordos |
| `ajuizado` / `citado` / `decisao` | atualização manual no painel |
