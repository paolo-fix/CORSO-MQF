# Prompt di tappa in Regime C

**Regime C - Verifica di una criticità specifica.**

## Parte variabile: contributo studente

Sto verificando la Tappa [numero] — [titolo della tappa].

Il materiale che deve essere controllato è:
[riportare o descrivere la formula, l'output, la tabella, il grafico, la cella Markdown o il codice interessato].

Ho individuato questa possibile criticità:
[descrivere il dubbio, l'anomalia o l'incoerenza osservata].

Il mio ragionamento è il seguente:
[spiegare perché il risultato, la formula, il testo o il codice non convince e quale aspetto ritengo necessario verificare].

## Parte fissa: istruzioni per IA

Verifica il problema senza modificare la Scheda Caso e classifica l'esito come **criticità respinta** oppure **criticità accolta**.

Se la criticità è respinta:
- spiega sinteticamente perché il dubbio non richiede modifiche;
- non proporre modifiche al notebook.

Se la criticità è accolta:
- indica la criticità individuata;
- spiega come si è generata, identificando il passaggio, l'assunzione, la formula, la scelta di codice o l'interpretazione che l'ha prodotta;
- indica la modifica necessaria;
- produci soltanto la versione sostitutiva della cella Markdown della tappa interessata, includendo in forma sintetica:
  1. criticità individuata;
  2. origine della criticità;
  3. modifica adottata;
- produci la versione sostitutiva della cella code soltanto se la correzione richiede una modifica del codice;
- non proporre celle aggiuntive;
- non mantenere la versione errata.

Non produrre l'interpretazione finale al posto dello studente.

L'esito sarà utilizzato per [indicare uso successivo].