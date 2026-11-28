# Valutazione TakeHome Lezione 10 Bossola

Data: 27 novembre 2026.

**Valutazione individuale: 97/100.**

## Riferimenti e metodo

Si applicano le Guidelines (??14.10 e 15.8-15.12), la Scheda Caso TakeHome Lez10 (??3-8) e la Scheda Costruzione Caso TakeHome Lez10 (??10-15), nelle cartelle `00_MasterPlan` e `04_Codice/Lez10`.

I massimi delle sei aree sono normativi; l'attribuzione interna dei punti ? un giudizio motivato, non una formula automatica di decurtazione. Non sono introdotte soglie di sufficienza, conversioni in trentesimi o risultati numerici obbligatori uguali alla calibrazione docente. Implementazioni diverse con seed 2026 possono produrre campioni differenti corretti. L'assenza di un Prompt C non ? penalizzata di per s?.

Sono stati esaminati contributi e revisioni del tracciato, celle e output del notebook; le pagine pertinenti e i grafici sono stati controllati anche visivamente. La riesecuzione ordinata ? stata svolta con Python, NumPy 2.1.3 e backend Matplotlib non interattivo, mantenendo disponibili le funzioni di visualizzazione Jupyter. Non sono stati modificati i file consegnati.

## Materiali

- [Lezione_10_Notebook_TakeHome_Bossola.ipynb](Lezione_10_Notebook_TakeHome_Bossola.ipynb): 10 celle di codice eseguite senza errori.
- [Lezione_10_Tracciato_TakeHome_Bossola.pdf](Lezione_10_Tracciato_TakeHome_Bossola.pdf): 75 pagine, con prompt iniziali presenti.

SHA256 notebook: `55d66ccb0e8a6c2ccdbc6121621d688c08a2e8a1a6b945264b60648758e44d44`.

## Punteggi

| Area | Punti | Massimo |
|---|---:|---:|
| Prompt 2 e flusso logico teorico | 29 | 30 |
| Prompt 3 e scomposizione input output | 15 | 15 |
| Notebook e output quantitativi | 20 | 20 |
| Prompt di tappa e regimi IA | 15 | 15 |
| Controlli logici numerici e di coerenza | 14 | 15 |
| Interpretazione finanziaria finale | 4 | 5 |
| **Totale** | **97** | **100** |

## 1 Prompt 2 e flusso logico teorico

**29/30.** Alle pp.24-26 il contributo iniziale distingue correttamente il calendario dei regimi da quello dei rating, il default terminale, le perdite negative e la dipendenza attraverso il regime comune. Sono esplicitati il fattore 173/148, il riuso delle traiettorie, la non linearit? delle misure di rischio e il cambiamento del mix per rating. L'attenzione alla massa sul VaR ? espressamente richiesta. Il flusso viene approvato a p.28.

Il livello ? molto buono. Rimane da formalizzare direttamente la definizione integrale del CVaR, inizialmente indicata pi? come misura da calcolare e problema da verificare che come formula gi? costruita dallo studente.

## 2 Prompt 3 e scomposizione input output

**15/15.** La proposta alle pp.28-30 assegna le dieci tappe a input, simulazione, perdite, rischio, crisi, confronto e stabilit?, con richiamo esplicito a tabelle, figure e controlli. Sono chiari seed, riuso degli output e distinzione tra Delta rho e distribuzione di Delta L. ? presente approvazione esplicita a p.31.

L'allineamento del controfattuale mediante un vettore di quaranta investimenti con Lehman a zero ? tecnicamente equivalente all'uso di trentanove posizioni: le tabelle e il controllo del numero effettivo dei debitori restano a trentanove. Questa scelta non viene penalizzata.

## 3 Notebook e output quantitativi

**20/20.** Le dieci celle di codice si eseguono in ordine senza errori. Tutte le tabelle e figure richieste sono presenti, insieme alla distribuzione di Delta L e alla diagnostica. Sono corretti regime corrente, migrazioni, assorbenza, perdite e confronto accoppiato. La correzione dell'allineamento tra quaranta tassi di perdita e trentanove esposizioni ? recepita nella cella 14.

La media riprodotta ? 11,123087 milioni nel concentrato e 12,179302 nel controfattuale. La formula CVaR=VaR+media((L-VaR)+)/(1-alpha) restituisce il corretto CVaR empirico per i quantili utilizzati. L'interpolazione predefinita del VaR pu? differire di frazioni minime dall'inversa empirica a gradini; non produce qui un errore sostanziale del CVaR.

## 4 Prompt di tappa e regimi IA

**15/15.** Il PDF di 75 pagine contiene inizializzazione, acquisizione del caso, contributi e approvazioni dei Prompt 2 e 3 e dieci richieste B specifiche. Lo studente indica gli input e i vincoli di ciascuna tappa, compreso il corretto trattamento del CVaR discreto.

La verifica C a p.52 identifica esattamente il broadcasting tra (50000,40) e (39,), ne propone la causa e richiama il vettore gi? specificato nel prompt. La correzione viene recepita. Si riconosce il controllo sostanziale dell'allineamento, senza attribuire un premio automatico al fatto che il codice IA iniziale abbia prodotto un errore. Il commento finale ? nel notebook e non richiede generazione IA.

## 5 Controlli logici numerici e di coerenza

**14/15.** I controlli 1-14 sono ricostruibili nelle tappe; la correzione conserva l'accoppiamento dei debitori. Sono presenti domini, assorbenza teorica ed empirica, indipendenza per costruzione, importi e proporzioni. Il seed 2026 ? correttamente impostato e la riesecuzione ordinata riproduce i risultati principali.

La stabilit? ? illustrata tramite sottocampioni e grafici, ma il riepilogo della cella 24 assegna staticamente SUPERATO a tutte le righe e stampa una frase conclusiva che parla di affidabilit? delle code garantita. Gli output sono compatibili con una ragionevole stabilit?, ma un riscontro empirico non garantisce formalmente convergenza o accuratezza. Si sottrae un punto per questa eccessiva forza della validazione, senza negare il controllo effettivamente presente.

## 6 Interpretazione finanziaria finale

**4/5.** La cella 25 usa risultati numerici per spiegare crisi, perdita attesa, dispersione e CVaR 99%. Identifica correttamente la riallocazione da un debitore A verso classi peggiori e riconosce che non tutte le misure aumentano. Il nucleo interpretativo ? autonomo e sostanziale.

Occorre per? distinguere meglio tre aspetti: il minimo di Delta L non ? necessariamente la replica pi? grave in termini di perdita complessiva; il rapporto CVaR/media non dimostra da solo un ordinamento della pesantezza delle code; l'ipotesi di riallocare solo sui debitori A richiederebbe una nuova simulazione prima di concluderne la superiorit?. Mancano inoltre un richiamo esplicito alla calibrazione didattica e ai limiti di una scelta gestionale basata sulle sole perdite. Per queste riserve l'area non raggiunge il massimo.

## Risultati numerici verificati

Importi in milioni di dollari. Il CVaR della tabella seguente ? ricalcolato esattamente sul campione ordinato, distinto dall?eventuale approssimazione del notebook.

| Portafoglio | Media | Deviazione standard | CVaR 95% esatto | CVaR 99% esatto |
|---|---:|---:|---:|---:|
| Concentrato | 11.123087 | 6.941272 | 29.848028 | 37.271720 |
| Controfattuale | 12.179302 | 7.286678 | 31.097905 | 37.229249 |
