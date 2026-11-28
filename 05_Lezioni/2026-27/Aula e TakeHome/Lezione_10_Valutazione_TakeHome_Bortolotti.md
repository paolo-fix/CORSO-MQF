# Valutazione TakeHome Lezione 10 Bortolotti

Data: 27 novembre 2026.

**Valutazione individuale: 99/100.**

## Riferimenti e metodo

Si applicano le Guidelines (??14.10 e 15.8-15.12), la Scheda Caso TakeHome Lez10 (??3-8) e la Scheda Costruzione Caso TakeHome Lez10 (??10-15), nelle cartelle `00_MasterPlan` e `04_Codice/Lez10`.

I massimi delle sei aree sono normativi; l'attribuzione interna dei punti ? un giudizio motivato, non una formula automatica di decurtazione. Non sono introdotte soglie di sufficienza, conversioni in trentesimi o risultati numerici obbligatori uguali alla calibrazione docente. Implementazioni diverse con seed 2026 possono produrre campioni differenti corretti. L'assenza di un Prompt C non ? penalizzata di per s?.

Sono stati esaminati contributi e revisioni del tracciato, celle e output del notebook; le pagine pertinenti e i grafici sono stati controllati anche visivamente. La riesecuzione ordinata ? stata svolta con Python, NumPy 2.1.3 e backend Matplotlib non interattivo, mantenendo disponibili le funzioni di visualizzazione Jupyter. Non sono stati modificati i file consegnati.

## Materiali

- [Lezione_10_Notebook_TakeHome_Bortolotti.ipynb](Lezione_10_Notebook_TakeHome_Bortolotti.ipynb): 11 celle di codice eseguite senza errori.
- [Lezione_10_Tracciato_TakeHome_Bortolotti.pdf](Lezione_10_Tracciato_TakeHome_Bortolotti.pdf): 105 pagine, con prompt iniziali presenti.

SHA256 notebook: `e0c47a3def300b4c3832a93710a41d3d83c2bb8b6abc3182e3f36bde82c2707e`.

## Punteggi

| Area | Punti | Massimo |
|---|---:|---:|
| Prompt 2 e flusso logico teorico | 29 | 30 |
| Prompt 3 e scomposizione input output | 15 | 15 |
| Notebook e output quantitativi | 20 | 20 |
| Prompt di tappa e regimi IA | 15 | 15 |
| Controlli logici numerici e di coerenza | 15 | 15 |
| Interpretazione finanziaria finale | 5 | 5 |
| **Totale** | **99** | **100** |

## 1 Prompt 2 e flusso logico teorico

**29/30.** Alle pp.20-22 del PDF il contributo iniziale distingue accuratamente indipendenza condizionata e dipendenza incondizionata, convenzione temporale M0,...,M3, default assorbente, perdite migration-based comprese quelle negative, confronto accoppiato e differenze tra misure rispetto a misure della differenza. Sono esplicitati calibrazione sotto misura fisica, costanza dell'investimento e cambiamento della composizione per rating. Le domande sul trimestre del default e sulla differenza replica per replica sono pertinenti. La validazione del flusso ? visibile a p.25.

Il contributo ? molto completo e ragionato. Il punto non attribuito riguarda il livello di formalizzazione delle misure di coda: ? richiamata correttamente la definizione mediante quantili, senza svilupparne direttamente la costruzione empirica e la gestione della massa sulla soglia.

## 2 Prompt 3 e scomposizione input output

**15/15.** Alle pp.25-26 la proposta in undici tappe mappa input, operazioni, output, uso successivo e controlli numerati. Separa le procedure di una replica dalla ripetizione Monte Carlo e distingue confronto, crisi e verifica finale. Tabelle e figure sono assegnate esplicitamente. Non ? necessario imporre le sei tappe del riferimento docente: la rubrica valuta coerenza e completezza della scomposizione validata, non l'identit? del numero di tappe.

## 3 Notebook e output quantitativi

**20/20.** Le undici celle di codice si eseguono in ordine senza errori e producono gli output prescritti. Sono corretti matrici, stati iniziali, assorbenza, applicazione del regime corrente, estrazioni individuali, funzione di perdita, scala monetaria e riscalamento 173/148. Il controfattuale riutilizza i 39 debitori comuni. Le quattro tabelle e le tre figure richieste sono presenti; le diverse viste sono correttamente identificate. Il focus sulla coda conserva la densit? incondizionata.

La media riprodotta ? 11,155311 milioni per il concentrato e 12,205262 per il controfattuale. VaR e CVaR mediante quantili sono implementati correttamente, inclusa la massa sulla soglia. Le differenze rispetto alla calibrazione docente sono compatibili con l'implementazione e non sono trattate come errori.

## 4 Prompt di tappa e regimi IA

**15/15.** Il PDF di 105 pagine documenta la sequenza iniziale e undici tappe B con parti variabili dettagliate: precisione degli investimenti, domini, allineamento degli scenari e confini del compito IA sono specificati prima del codice. La capacit? di delimitare il compito ? osservabile, senza premiare la sola lunghezza del tracciato.

L'assenza di una verifica C autonoma non comporta penalit?: il Regime C non ? obbligatorio. I contributi iniziali e le richieste di controllo mostrano gi? un governo consapevole. Il PDF termina con il riepilogo computazionale, mentre l'interpretazione autonoma ? nel notebook: non ? necessario chiederne la generazione all'IA o ripeterla nella chat.

## 5 Controlli logici numerici e di coerenza

**15/15.** I quindici controlli sono ricostruibili e consolidati nella cella 25. Sono verificati conservazione degli importi, proporzioni, traiettorie comuni, assorbenza, perdite aggregate e domini. L'indipendenza delle estrazioni ? sostenuta dalla costruzione del generatore, non dedotta soltanto da una correlazione nulla.

Il CVaR ? verificato anche tramite l'identit? equivalente e un campione con pareggi sulla soglia. La stabilit? ? esaminata sui sottocampioni crescenti e distinta esplicitamente dalla riproducibilit?. I campioni di prova iniziali con generatore locale non fissato non modificano il generatore con seed 2026 della simulazione principale; non sono quindi una violazione del seed assegnato.

## 6 Interpretazione finanziaria finale

**5/5.** La cella 26 interpreta i risultati con valori e unit?: aumento della media, diverso comportamento della coda estrema, ruolo della grande posizione Lehman e perdita condizionata alla crisi. Distingue il quantile di Delta L dalla differenza dei VaR e riconosce che la riallocazione modifica il mix di rating.

La discussione non trasforma il vantaggio su alcune misure in una raccomandazione automatica: ricorda l'assenza di rendimenti attesi e presenta il limite del 10% come ipotesi per un nuovo scenario da simulare, non come risultato dimostrato. Il testo non ? prodotto dall'IA nel tracciato e risulta coerente con gli output. La piccola cella finale vuota non ha rilievo valutativo.

## Risultati numerici verificati

Importi in milioni di dollari. Il CVaR della tabella seguente ? ricalcolato esattamente sul campione ordinato, distinto dall?eventuale approssimazione del notebook.

| Portafoglio | Media | Deviazione standard | CVaR 95% esatto | CVaR 99% esatto |
|---|---:|---:|---:|---:|
| Concentrato | 11.155311 | 6.999675 | 30.035052 | 37.554840 |
| Controfattuale | 12.205262 | 7.328133 | 31.168699 | 37.250243 |
