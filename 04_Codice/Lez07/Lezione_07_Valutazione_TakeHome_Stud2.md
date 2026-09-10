# Valutazione del lavoro take-home — Lezione 07 — Studente 2

## Esito

**Punteggio: 36/100 — insufficiente.**

La consegna presenta un notebook formalmente ordinato, eseguibile e completo di tabelle, grafici e controlli, ma non rispetta la specifica vincolante del caso: sono stati modificati parametri essenziali senza autorizzazione. Il PDF del tracciato mostra inoltre che tali modifiche derivano da una Scheda Caso incompleta nel Prompt 1 e che non sono state rilevate durante le successive validazioni. L'interpretazione finale non è autonoma e non è coerente con gli output del notebook.

La valutazione considera congiuntamente:

- `Lezione_07_Tracciato_Takehome_Stud2.pdf` (23 pagine);
- `Lezione_07_Notebook_TakeHome_Stud2.ipynb`, rieseguito integralmente senza errori in una copia temporanea;
- la rubrica delle Guidelines (Sez. 14.10 e 15.11) e la Scheda Costruzione Caso Take-Home della Lezione 07.

## Punteggio analitico

| Area | Peso | Punti | Valutazione |
|---|---:|---:|---|
| Prompt 2 — Flusso logico-teorico risolutivo | 30 | **10** | Il contributo iniziale è non vuoto, ma è un elenco nominale, duplicato e senza definizioni, formule o collegamenti autonomi fra teoria, output e controlli. Il flusso in otto passaggi è costruito quasi interamente dall'IA. |
| Prompt 3 — Scomposizione input-output | 15 | **3** | La proposta personale si limita a «tappe 4-5-6 unite» e «tappe 7-8 unite»: non specifica input, operazioni, output o controlli. La scomposizione completa in sette tappe è generata dall'IA. È positivo il rilievo successivo sulla necessità della cella Markdown. |
| Notebook Jupyter e output computazionali | 20 | **10** | Il notebook è lineare, leggibile e rieseguibile; contiene le quattro tabelle, i cinque grafici e le formule operative principali. Il prodotto, tuttavia, risolve un modello diverso da quello assegnato a causa della modifica dei parametri. |
| Prompt e uso dei regimi A/B/C | 15 | **6** | Prompt zero e scansione per tappe sono formalmente presenti. Il Prompt 1 non trasmette però la Scheda Caso integrale; in Regime B vengono quindi accettati parametri inventati dall'IA. Le verifiche in Regime C non intercettano né tale errore né le incoerenze dell'interpretazione. |
| Verifiche logiche e controlli numerici | 15 | **7** | I nove controlli prescritti sono rappresentati, e diversi sono implementati correttamente. Manca il controllo decisivo di conformità alla Scheda Caso; il seed è soltanto impostato, non verificato con una seconda esecuzione, e il confronto fra griglie non separa in modo netto errore di discretizzazione e variabilità Monte Carlo. |
| Interpretazione critica finale | 5 | **0** | Lo studente chiede all'IA di elaborare i quattro punti e ne trasferisce sostanzialmente il testo. I dati richiamati nell'interpretazione non coincidono con quelli del notebook e la risposta IA li approva erroneamente. |
| **Totale** | **100** | **36** | |

## Evidenze determinanti

### 1. Specifica vincolante non rispettata

Nel PDF, il Prompt 1 riporta soltanto alcuni dati iniziali e non include la tabella dei parametri assegnati dalla Scheda Caso. Nella Tappa 1, l'IA propone e il notebook adotta valori diversi da quelli vincolanti:

| Parametro | Scheda Caso | Notebook e tracciato |
|---|---:|---:|
| $M$ della simulazione principale | 50.000 | 10.000 |
| $q$ | 0,025 | 0,030 |
| $\sigma_S$ | 0,18 | 0,20 |
| $\kappa_r$ | 1,25 | 0,80 |
| $\theta_r$ | 0,0220 | 0,0250 |
| $\sigma_r$ | 0,040 | 0,050 |

La modifica non è una scelta di discretizzazione: altera drift, volatilità e dinamica del tasso, quindi tutte le statistiche e il prezzo stimato. Il notebook classifica inoltre $q$ e $\sigma_S$ come parametri didattici/modello, mentre la Scheda Caso li indica come proxy di mercato.

### 2. Qualità del tracciato IA

Nel Prompt 2 lo studente propone voci quali «generazione sottostante azionario», «quantità di interesse per opzione asiatica» e «parti precedenti in formato teorico», con duplicazioni. L'IA rileva e completa autonomamente gli elementi mancanti. Le due successive verifiche in Regime C classificano come *criticità respinta* l'assenza iniziale di generazione degli shock correlati e dell'integrazione dello sconto, perché tali passaggi sono ormai stati introdotti dalla risposta IA: non costituiscono quindi una correzione autonoma dello studente.

Nel Prompt 3 non compare una proposta operativa effettiva. Lo studente controlla correttamente il solo requisito formale della cella Markdown, ma non valida il contenuto della scomposizione né la sua fedeltà ai parametri assegnati.

### 3. Incoerenza dell'interpretazione con gli output

Il notebook eseguito riporta:

- probabilità di esercizio: **45,18%**;
- prezzo Monte Carlo della simulazione base: **283,34 punti**;
- errore standard per $M=1.000$: **14,3728 punti**;
- errore standard per $M=10.000$: **4,6640 punti**;
- errore standard per $M=50.000$: **2,0417 punti**.

L'interpretazione nel PDF usa invece probabilità fra **50% e 55%**, errori standard di circa **2,2**, **0,7** e **0,3** punti e un prezzo di **210–220 punti**. Nessuno di questi dati proviene dalle tabelle del notebook. L'IA dichiara poi la bozza «accolta e validata»; lo studente non segnala la contraddizione.

### 4. Aspetti tecnici positivi

- costruzione corretta degli shock correlati;
- fixing mensili correttamente collocati ai passi 21, 42, ..., 252, senza includere $S_0$;
- media asiatica, payoff e sconto calcolati scenario per scenario;
- uso della somma di Riemann sinistra su $r_{t_0},\ldots,r_{t_{N-1}}$;
- presenza di tabelle, grafici, intervallo di confidenza e diagnostica Monte Carlo;
- esecuzione integrale del notebook senza errori memorizzati o errori in riesecuzione.

## Condizioni per una nuova consegna

1. Usare nel Prompt 1 la Scheda Caso completa, compresa la tabella dei parametri e la loro natura.
2. Ripristinare tutti i valori vincolanti e usare $M=50.000$ come simulazione principale.
3. Rieseguire notebook, tabelle, grafici, controlli e sintesi con i parametri corretti.
4. Inserire un controllo esplicito di coerenza fra dizionario `params` e Scheda Caso.
5. Dimostrare la replicabilità ripetendo l'esecuzione con lo stesso seed e confrontando gli output.
6. Scrivere un'interpretazione autonoma, basata esclusivamente sugli output prodotti, e usare l'IA soltanto per una revisione critica verificabile.

