# Valutazione TakeHome Lezione 10 Ghislandi

Data: 27 novembre 2026.

**Valutazione individuale: 86/100.**

## Riferimenti e metodo

Si applicano le Guidelines (??14.10 e 15.8-15.12), la Scheda Caso TakeHome Lez10 (??3-8) e la Scheda Costruzione Caso TakeHome Lez10 (??10-15), nelle cartelle `00_MasterPlan` e `04_Codice/Lez10`.

I massimi delle sei aree sono normativi; l'attribuzione interna dei punti ? un giudizio motivato, non una formula automatica di decurtazione. Non sono introdotte soglie di sufficienza, conversioni in trentesimi o risultati numerici obbligatori uguali alla calibrazione docente. Implementazioni diverse con seed 2026 possono produrre campioni differenti corretti. L'assenza di un Prompt C non ? penalizzata di per s?.

Sono stati esaminati contributi e revisioni del tracciato, celle e output del notebook; le pagine pertinenti e i grafici sono stati controllati anche visivamente. La riesecuzione ordinata ? stata svolta con Python, NumPy 2.1.3 e backend Matplotlib non interattivo, mantenendo disponibili le funzioni di visualizzazione Jupyter. Non sono stati modificati i file consegnati.

## Materiali

- [Lezione_10_Notebook_TakeHome_Ghislandi.ipynb](Lezione_10_Notebook_TakeHome_Ghislandi.ipynb): 6 celle di codice eseguite senza errori.
- [Lezione_10_Tracciato_TakeHome_Ghislandi.pdf](Lezione_10_Tracciato_TakeHome_Ghislandi.pdf): 131 pagine, con prompt iniziali presenti.

SHA256 notebook: `c6e60888e49dc7dee8a49534a8e1a4247148ce7887256cb38d3f97a35d48f79d`.

## Punteggi

| Area | Punti | Massimo |
|---|---:|---:|
| Prompt 2 e flusso logico teorico | 25 | 30 |
| Prompt 3 e scomposizione input output | 12 | 15 |
| Notebook e output quantitativi | 19 | 20 |
| Prompt di tappa e regimi IA | 14 | 15 |
| Controlli logici numerici e di coerenza | 13 | 15 |
| Interpretazione finanziaria finale | 3 | 5 |
| **Totale** | **86** | **100** |

## 1 Prompt 2 e flusso logico teorico

**25/30.** Alle pp.31-34 la proposta individua correttamente M0,...,M3 e quattro migrazioni, assorbenza, default e non-default, composizione del controfattuale e riuso delle simulazioni. Il contributo ? ampio e specifico.

Restano imprecisioni: matrice sistemica e matrice creditizia non sono sempre nominate distintamente, la ripetizione richiama passaggi in modo non del tutto ordinato, i livelli VaR/CVaR sono chiamati intervalli di confidenza e il CVaR ? descritto come media oltre la soglia alpha. L'IA corregge la distinzione fra livello del quantile e IC e richiama la massa sulla soglia. La versione finale ? migliore della proposta, ma il credito iniziale non pu? essere equiparato a quello di una proposta gi? formalmente corretta.

## 2 Prompt 3 e scomposizione input output

**12/15.** Alle pp.37-38 sono proposte sei tappe che separano sistema, rating, perdite, crisi e confronto. Sono richiamati output e stabilit?, ma controlli e campi input-output non sono mappati con la precisione delle proposte pi? articolate.

Alle pp.43-44 lo studente contesta motivatamente la suddivisione IA in pi? tappe e spiega perch? desidera risultati dei due portafogli nella stessa tappa e un'analisi della crisi separata. ? evidenza positiva di scelta della struttura. Il richiamo nella chat a un massimo di sei tappe ? applicato come esigenza della propria interazione, non trasformato in un nuovo criterio generale per penalizzare gli altri studenti.

## 3 Notebook e output quantitativi

**19/20.** Le sei celle di codice si eseguono in ordine senza errori. Sono presenti quattro tabelle, tre figure, distribuzione di Delta L e diagnostica. Il modello principale rispetta specifica, calendario, indipendenza condizionata, assorbenza e confronto accoppiato. Le medie riprodotte sono 11,118178 e 12,187731 milioni.

Il CVaR nella cella 11 ? calcolato campionando la funzione quantile su una griglia endpoint=False, chiamata impropriamente integrazione esatta. Non ? l'integrale esatto della distribuzione empirica: per il concentrato al 99% il codice d? 37,423448 contro 37,425480 ottenuto dalla media esatta delle 500 statistiche d'ordine superiori; nel controfattuale d? 37,302433 contro 37,304037. L'errore ? piccolo e non cambia la conclusione economica, ma giustifica un punto in meno. Non si tratta dell'errore ben pi? grave di includere tutta la massa maggiore o uguale al VaR.

## 4 Prompt di tappa e regimi IA

**14/15.** Il PDF di 131 pagine documenta proposte iniziali, riordino critico delle tappe, sei richieste B e cinque richieste C. Le revisioni riguardano struttura, incompatibilit? dimensionale, errore Matplotlib e leggibilit? di grafici e legende. Lo studente individua e segnala anomalie e non altera arbitrariamente la specifica.

Il volume del PDF dipende anche da un lungo traceback e non ? trattato come qualit? in s?. Le correzioni tecniche risolte hanno valore metodologico limitato rispetto a una verifica teorica; vengono comunque riconosciute nel controllo della risposta IA. Il piccolo errore nel CVaR non ? individuato. Il testo finale ? fornito dallo studente alle pp.130-131 e richiesto in Markdown senza modifiche: non ? una delega integrale dell'interpretazione.

## 5 Controlli logici numerici e di coerenza

**13/15.** Sono presenti i quindici controlli consolidati nella cella 15, con asserzioni e riscontro degli esiti. Sono corretti importi, proporzioni, traiettorie comuni e assorbenza. La stabilit? ? controllata con confronto tra 40.000 e 50.000 repliche e soglia operativa del 2%, oltre alla tabella sui campioni crescenti.

La correlazione campionaria quasi nulla delle uniformi ? un controllo diagnostico, non una dimostrazione di indipendenza; questa ? sostenuta dalla costruzione del generatore e delle estrazioni. Il controllo 14 non verifica l'identit? esatta del CVaR, ma solo base monetaria e coerenza delle quantit?: tale mancanza di un controllo realmente discriminante ? rilevante nel giudizio sui controlli. Il piccolo errore numerico ? gi? quantificato nell'area output e non riceve un'ulteriore decurtazione automatica. Rimane inoltre poco sviluppata l'interpretazione della stabilit? come riscontro empirico limitato.

## 6 Interpretazione finanziaria finale

**3/5.** La cella 16 riconosce il cambiamento del mix di rating e l'aumento della perdita media condizionato alla crisi. Sono osservazioni economiche pertinenti.

L'affermazione generale secondo cui il controfattuale assume maggiori rischi ? incompleta: nel campione il CVaR 99% si riduce leggermente e questa eccezione non ? discussa. Non ? dimostrato che l'impatto della crisi sia elevato perch? sono simulati pochi periodi; ? un risultato delle transizioni e della funzione di perdita assegnate. Il commento ? in parte dedicato all'uso dell'IA e non quantifica misure, limiti e natura non storica del modello. Autonomia riconoscibile, interpretazione ancora parziale.

## Risultati numerici verificati

Importi in milioni di dollari. Il CVaR della tabella seguente ? ricalcolato esattamente sul campione ordinato, distinto dall?eventuale approssimazione del notebook.

| Portafoglio | Media | Deviazione standard | CVaR 95% esatto | CVaR 99% esatto |
|---|---:|---:|---:|---:|
| Concentrato | 11.118178 | 6.946909 | 29.805876 | 37.425480 |
| Controfattuale | 12.187731 | 7.302986 | 31.067148 | 37.304037 |
