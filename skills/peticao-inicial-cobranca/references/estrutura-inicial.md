# Estrutura da Petição Inicial por Via

Esqueletos das três vias que saem do HANDOFF-COBRANCA. A lógica de escrita é a
do `guia-redacao.md`; aqui está o que muda de uma via para outra. Os
dispositivos citados devem ser conferidos no texto vigente antes de a peça
sair; súmula ou tema que não esteja nesta lista só entra após pesquisa.

---

## A. EXECUÇÃO DE TÍTULO EXTRAJUDICIAL

### A.1 Preâmbulo

> [CENTRO] AO DOUTO JUÍZO DA VARA CÍVEL DA COMARCA DE [COMARCA]/SC
>
> **[CREDOR]**, [qualificação], vem, por intermédio do procurador que esta
> subscreve, com fundamento nos arts. 771, 783, 784, inciso [X], e 824 e
> seguintes do Código de Processo Civil, [+ lei própria do título], propor
> **EXECUÇÃO DE TÍTULO EXTRAJUDICIAL** em face de **[DEVEDOR]**, [qualificação],
> [e de **[AVALISTA]**, na qualidade de avalista,] pelos fatos e fundamentos que
> passa a expor.

Endereçamento: credor instituição financeira ou cooperativa de crédito →
conferir se a matéria e a comarca estão na competência da Vara Estadual de
Direito Bancário do TJSC (o escritório já atua nela; processos com final
`.8.24.0930`). Nos demais casos, foro do domicílio do executado (CPC, art. 46),
do lugar do pagamento do título (art. 53, III, "d") ou o de eleição (art. 63).
Na dúvida, `[CONFIRMAR: foro competente]`.

Base legal por título (inciso do art. 784 + lei própria):

| Título | Art. 784 | Lei própria |
|---|---|---|
| Nota promissória, letra de câmbio | I | Decreto nº 57.663/66 (Lei Uniforme) |
| Cheque | I | Lei nº 7.357/85 |
| Duplicata | I | Lei nº 5.474/68, art. 15 |
| Escritura pública / documento público assinado pelo devedor | II | |
| Documento particular assinado pelo devedor e por 2 testemunhas (confissão de dívida, contrato) | III | assinatura eletrônica com integridade conferida por provedor dispensa testemunhas (§ 4º) |
| Contrato com hipoteca, penhor, anticrese ou caução | V | |
| Cédula de Crédito Bancário | XII | Lei nº 10.931/2004, art. 28 |
| Cédulas de crédito rural | XII | Decreto-Lei nº 167/67 |
| Cédula de Produto Rural | XII | Lei nº 8.929/94 |

### A.2 Seções

**1. DOS FATOS.** Narrativa cronológica, em prosa, do negócio ao
inadimplemento. Ordem: (a) a relação e o título, com data, número e valor por
extenso; (b) a contraprestação do credor, quando houver (liberação do crédito,
entrega do bem); (c) as garantias (aval, alienação fiduciária, hipoteca), com
matrícula e ato de registro; (d) o inadimplemento: última parcela paga, data do
primeiro atraso, parcelas vencidas; (e) vencimento antecipado, se houver, com a
cláusula; (f) tentativa de composição, se houver, em uma frase; (g) fecho de
uma linha que conduz à execução ("Diante da impossibilidade de composição
amigável, [o exequente] não possui outro meio senão a execução do título
extrajudicial.").

**2. DO DIREITO** (ou "DO TÍTULO EXECUTIVO"). Um parágrafo para cada requisito,
cada um ancorado no documento:
- natureza de título executivo (inciso do art. 784 + lei própria), com a forma
  de assinatura (devedor, avalistas, testemunhas com nome e CPF, firma
  reconhecida, assinatura eletrônica certificada);
- certeza, liquidez e exigibilidade (art. 783): de onde vem o valor e por que
  ele não depende de apuração;
- contraprestação cumprida pelo credor, quando o contrato é bilateral (art.
  798, I, "d"; afasta a exceção do art. 476 do CC);
- constituição em mora: termo certo → mora de pleno direito (art. 397, caput,
  do CC); sem termo → interpelação, com a data;
- encargos: os pactuados, com cláusula e taxa (remuneratórios, moratórios,
  multa, capitalização). Sem pacto: correção pelo IPCA (CC, art. 389, parágrafo
  único) e juros pela taxa legal (CC, art. 406), na redação da Lei nº
  14.905/2024. Multa contratual com cláusula e base (arts. 408 e 409 do CC);
- responsabilidade dos garantidores: aval é obrigação autônoma e solidária
  (Lei Uniforme, art. 32; Lei nº 10.931/2004, art. 44 para a CCB);
- fecho: "Ficam os critérios declinados para os fins do art. 798, parágrafo
  único, do Código de Processo Civil."

Peculiaridades por título que precisam aparecer quando aplicáveis:
- **CCB**: art. 28 da Lei nº 10.931/2004; o demonstrativo deve evidenciar, de
  modo claro, o valor principal, os encargos e a forma de cálculo (§ 2º).
  Crédito rotativo/conta garantida exige planilha da evolução do saldo.
- **Duplicata sem aceite**: protesto + comprovante de entrega da mercadoria
  (Lei nº 5.474/68, art. 15, II). Canhoto assinado não é aceite.
- **Cheque**: apresentação e devolução com o motivo (alínea), datas; protesto
  facultativo para a execução contra o emitente.
- **Título vinculado a contrato**: demonstrar a liquidez do negócio subjacente
  (afastar a Súmula 258 do STJ).
- **Assinatura de terceiro** (marcador do handoff): qualificar o assinante e
  invocar a teoria da aparência com o local da entrega.

**3. DO DÉBITO.** Abrir com "Para os fins do art. 798, inciso I, alínea 'b', do
Código de Processo Civil, o crédito exequendo se compõe como segue." e trazer a
tabela:

| RUBRICA | VALOR |
|---|---|
| [Título/parcelas], [data(s) de vencimento] | R$ |
| Encargos até [data-base], conforme demonstrativo anexo | R$ |
| Multa contratual de [x]% (cláusula [y]) | R$ |
| **DÉBITO NA DATA DA PROPOSITURA** | **R$** |

Os valores vêm do demonstrativo do credor (ficha gráfica, planilha Sisbr) ou
do cálculo que o usuário fornecer. **Esta skill não atualiza débito.** Sem
demonstrativo, a tabela leva `[CONFIRMAR: valor atualizado até dd/mm/aaaa,
conforme demonstrativo do credor]` e a falta vira condição de ajuizamento.
Parcelas vincendas ficam em linha separada, fora do total exigível, com pedido
próprio de inclusão (CPC, art. 323, aplicado à execução pelo art. 771,
parágrafo único).

**4. DOS PEDIDOS.** Alíneas, nesta ordem:

a) o recebimento e o processamento da execução, com a juntada da procuração,
   do título [original/via digital], do demonstrativo do débito e dos demais
   documentos [listar];
b) a citação do(s) executado(s) para pagar a dívida no prazo de três dias,
   nos termos do art. 829 do CPC, fixados os honorários advocatícios em 10%
   sobre o valor da execução, com a ressalva da redução pela metade no caso de
   pagamento tempestivo (art. 827, § 1º);
c) o prosseguimento da execução pelo valor de R$ [total], conforme o
   demonstrativo do item 3 (o número tem de ser idêntico ao da tabela);
d) [se houver vincendas] a inclusão das parcelas que se vencerem no curso do
   processo (arts. 323 e 771, parágrafo único, do CPC);
e) a incidência dos encargos [pactuados / correção pelo IPCA e juros pela taxa
   legal] desde [termo inicial] até o efetivo pagamento;
f) a expedição de certidão de admissão da execução, para averbação no registro
   de imóveis, de veículos ou de outros bens sujeitos a penhora (art. 828);
g) não efetuado o pagamento, a penhora de ativos financeiros pelo sistema
   SISBAJUD (art. 854) e, sendo infrutífera ou insuficiente, a pesquisa, a
   restrição e a penhora de veículos pelo RENAJUD [e a pesquisa de bens pelo
   INFOJUD/SNIPER, quando o caso justificar];
h) [havendo garantia real] a penhora preferencial do bem dado em garantia
   (art. 835, § 3º), com a intimação dos titulares de direitos reais (art.
   799), [identificando matrícula e ato de registro];
i) [devedor não localizado] o arresto de bens (art. 830);
j) o ressarcimento das custas e despesas adiantadas e a majoração dos
   honorários na forma do art. 827, § 2º, do CPC, na hipótese de rejeição de
   eventuais embargos;
k) que as intimações e publicações sejam realizadas exclusivamente em nome do
   procurador subscritor, sob pena de nulidade.

Valor da causa: o do débito exigível na propositura (art. 292, I), igual ao
total da tabela.

Devedor **produtor rural pessoa física** (alerta do handoff): não pedir penhora
de imóvel rural sem antes confirmar que não se trata de pequena propriedade
trabalhada pela família (CPC, art. 833, VIII); priorizar ativos financeiros,
veículos e garantias reais constituídas.

---

## B. AÇÃO MONITÓRIA

### B.1 Preâmbulo

> **[CREDOR]**, [qualificação], vem, por intermédio do procurador que esta
> subscreve, com fundamento nos arts. 700 e seguintes do Código de Processo
> Civil, propor **AÇÃO MONITÓRIA** em face de **[DEVEDOR]**, [qualificação],
> pelos fatos e fundamentos que passa a expor.

### B.2 Seções

**1. DOS FATOS.** Mesma ordem da execução, com ênfase no negócio subjacente e
na entrega/contraprestação, porque a prova escrita não tem eficácia de título.

**2. DO CABIMENTO DA VIA MONITÓRIA.** Por que o documento é prova escrita (art.
700): quem o assinou, o que ele contém (produto, quantidade, valor), por que não
basta para a execução (requisito faltante ou prazo executivo vencido, dito com
franqueza) e por que basta para a monitória. Enunciados úteis, conforme o
documento (conferir a redação): Súmula 299/STJ (cheque prescrito), Súmula
503/STJ (prazo quinquenal do cheque, do dia seguinte à emissão), Súmula 504/STJ
(prazo quinquenal da nota promissória, do dia seguinte ao vencimento), Súmula
531/STJ (dispensa de menção ao negócio subjacente no cheque prescrito), Súmula
247/STJ (contrato de abertura de crédito com demonstrativo).

**3. DO DÉBITO.** A importância devida com memória de cálculo (art. 700, § 2º,
I), em tabela no mesmo formato da execução. A falta da memória leva ao
indeferimento (art. 700, § 4º), por isso ela é condição de ajuizamento.

**4. DOS PEDIDOS.**
a) o recebimento da inicial, com os documentos que a acompanham;
b) a expedição de mandado de pagamento, para que [o requerido] pague R$ [total]
   no prazo de quinze dias, acrescido de honorários de 5% do valor atribuído à
   causa, com a advertência da isenção de custas em caso de cumprimento (art.
   701, caput e § 1º);
c) não havendo pagamento nem embargos, a constituição de pleno direito do
   título executivo judicial (art. 701, § 2º), prosseguindo-se na forma do
   cumprimento de sentença;
d) opostos embargos, a sua rejeição, com a condenação [do requerido] em custas
   e honorários (art. 85);
e) a incidência de [encargos] desde [termo inicial];
f) intimações em nome do procurador subscritor.

Valor da causa: a importância do art. 700, § 2º, I (art. 700, § 3º).

---

## C. AÇÃO DE COBRANÇA (procedimento comum)

### C.1 Preâmbulo

> **[CREDOR]**, [qualificação], vem, por intermédio do procurador que esta
> subscreve, com fundamento nos arts. 318 e 319 do Código de Processo Civil
> [e nos arts. do CC que regem a obrigação], propor **AÇÃO DE COBRANÇA** em face
> de **[DEVEDOR]**, [qualificação], pelos fatos e fundamentos que passa a
> expor.

### C.2 Seções

**1. DOS FATOS.** Narrativa completa, porque a prova será construída no
processo. Indicar desde já cada elemento de prova (mensagens, pedidos,
romaneios, testemunhas).

**2. DO DIREITO.** Obrigação (fonte contratual ou legal), inadimplemento, mora,
encargos. Um subitem por fundamento, se houver mais de um.

**3. DO DÉBITO.** Tabela.

**4. DOS PEDIDOS.**
a) o recebimento da inicial;
b) a designação de audiência de conciliação, ou a manifestação de desinteresse
   (art. 319, VII), conforme orientação do credor;
c) a citação [do requerido];
d) a procedência para condenar [o requerido] ao pagamento de R$ [total], com
   [encargos] desde [termo];
e) as provas especificadas (documental, depoimento pessoal, testemunhas
   indicadas, exibição de documentos);
f) custas e honorários (art. 85);
g) intimações em nome do procurador subscritor.

---

## D. Cumulação e litisconsórcio

- Títulos do mesmo devedor na mesma via vão numa só petição (art. 780, para a
  execução). O HANDOFF já agrupa; não desdobrar ações que ele uniu.
- Avalistas e garantidores entram no polo passivo da execução quando o título
  os vincula. Na monitória, só quem assinou a prova escrita.
- Execução não cumula com monitória nem com cobrança: cada via é uma peça.
