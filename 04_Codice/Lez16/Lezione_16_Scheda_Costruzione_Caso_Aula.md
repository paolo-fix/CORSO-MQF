# Lezione 16 — Scheda Costruzione Caso Aula

Documento interno di progettazione docente.

## 1. Identificazione del caso

- **Lezione:** 16 — Applicazione in Python: programmazione stocastica
- **Tipo di caso:** aula
- **Titolo:** SVB–ALM 2023 — Asset allocation, liquidità e valore dell'informazione
- **Destinatari:** studenti del V anno di Banca e Risk Management
- **Uso previsto:** caso guidato in aula per consolidare computazionalmente la programmazione stocastica a due stadi sviluppata nei Capitoli 14 e 15, con particolare attenzione a soluzione stocastica, ricorso, Expected Value, wait-and-see, VSS ed EVPI.

## 2. Contesto e motivazione

Il caso è contestualizzato nella crisi di Silicon Valley Bank del marzo 2023. La vicenda storica viene utilizzata esclusivamente come cornice finanziaria: la struttura quantitativa del caso è una modellizzazione didattica semplificata e non una ricostruzione del bilancio effettivo della banca.

La crisi di SVB rende particolarmente naturale il collegamento tra composizione iniziale dell'attivo, esposizione al rischio di tasso, concentrazione della raccolta, deflussi di depositi e necessità di reperire liquidità in condizioni di stress.

Il caso sviluppa direttamente il problema guida SVB–ALM dei Capitoli 14 e 15. La banca deve scegliere al tempo iniziale la composizione dell'attivo prima di conoscere lo scenario futuro. Dopo la rivelazione dello scenario può ricorrere a funding di emergenza e può conservare eventuale liquidità eccedente.

La struttura del caso è volutamente a due stadi. L'obiettivo della Lezione 16 non è introdurre un nuovo modello, ma rendere computazionali concetti già sviluppati teoricamente:

1. decisione di primo stadio;
2. scenari e probabilità;
3. decisioni di ricorso;
4. forma estesa;
5. fattibilità del ricorso;
6. soluzione stocastica;
7. Expected Value;
8. wait-and-see;
9. VSS;
10. EVPI.

**Fonti storiche di riferimento per il docente:** Federal Reserve, *Review of the Federal Reserve's Supervision and Regulation of Silicon Valley Bank*, aprile 2023; FDIC, documentazione sulla receivership di Silicon Valley Bank.

I valori numerici utilizzati nel caso non sono dati storici di SVB e devono essere presentati agli studenti come parametrizzazione didattica in scala $A_0=100$.

## 3. Domanda quantitativa e obiettivo didattico

**Domanda quantitativa:** quale composizione iniziale dell'attivo massimizza il risultato economico atteso della banca quando l'intensità dei deflussi e il costo della liquidità di emergenza dipendono dallo scenario futuro? Quanto valore produce una decisione stocastica rispetto a una decisione costruita sullo scenario medio e quanto varrebbe conoscere anticipatamente lo scenario che si realizzerà?

**Obiettivo didattico:** portare lo studente dalla formulazione teorica dei Capitoli 14 e 15 alla costruzione e soluzione in Python di un programma stocastico lineare a due stadi, verificando operativamente la differenza tra informazione disponibile ex ante, adattamento ex post e informazione perfetta.

Il caso deve inoltre rendere evidente che:

- una decisione con rendimento atteso più elevato può esporre la banca a maggiori costi di ricorso negli scenari avversi;
- lo scenario medio non sostituisce la distribuzione degli scenari;
- il valore della programmazione stocastica deriva dal considerare congiuntamente probabilità, conseguenze e possibilità di ricorso;
- il wait-and-see rappresenta un benchmark informativo non realizzabile ex ante.

## 4. Specifica teorico-matematica

### Grandezze e variabili

La banca dispone al tempo iniziale di

$$
A_0=100.
$$

La decisione di primo stadio è

$$
x=(x_1,x_2,x_3,x_4)',
$$

dove:

| Variabile | Classe di attivo | Rendimento unitario $c_j$ |
|---|---|---:|
| $x_1$ | Cassa e riserve | 0.010 |
| $x_2$ | Titoli a breve scadenza | 0.025 |
| $x_3$ | Titoli a lunga scadenza | 0.040 |
| $x_4$ | Prestiti e impieghi meno liquidi | 0.050 |

Vincolo di bilancio iniziale:

$$
x_1+x_2+x_3+x_4=100.
$$

Vincoli di non negatività:

$$
x_j\geq0,
\qquad j=1,\ldots,4.
$$

Per evitare che la semplificazione del modello produca concentrazioni didatticamente poco informative:

$$
x_3\leq70,
\qquad
x_4\leq70.
$$

Le decisioni di secondo stadio nello scenario $s$ sono:

$$
u_s\geq0,
$$

funding di emergenza;

$$
g_s\geq0,
$$

liquidità residua dopo avere soddisfatto il fabbisogno.

### Eventi, informazione o scenari

L'insieme degli scenari è

$$
\mathcal S=\{N,P,R\},
$$

con:

- $N$: condizioni normali;
- $P$: pressione sulla raccolta;
- $R$: run severo.

Le probabilità sono:

| Scenario | $p_s$ |
|---|---:|
| $N$ | 0.60 |
| $P$ | 0.25 |
| $R$ | 0.15 |

Controllo obbligatorio:

$$
\sum_{s\in\mathcal S}p_s=1.
$$

La decisione $x$ viene assunta prima della rivelazione dello scenario.

Le decisioni $u_s$ e $g_s$ vengono assunte dopo l'osservazione dello scenario.

La struttura informativa è pertanto:

$$
x
\longrightarrow
s
\longrightarrow
(u_s,g_s).
$$

### Parametri e dati

Il fabbisogno di liquidità nello scenario $s$ è $d_s$:

| Scenario | $d_s$ |
|---|---:|
| $N$ | 15 |
| $P$ | 35 |
| $R$ | 65 |

Il coefficiente $\alpha_{js}$ rappresenta la quota dell'investimento $x_j$ trasformabile in liquidità nello scenario $s$.

| Attivo | $N$ | $P$ | $R$ |
|---|---:|---:|---:|
| Cassa e riserve $x_1$ | 1.00 | 1.00 | 1.00 |
| Titoli brevi $x_2$ | 0.98 | 0.95 | 0.90 |
| Titoli lunghi $x_3$ | 0.85 | 0.70 | 0.50 |
| Prestiti/impieghi $x_4$ | 0.60 | 0.40 | 0.20 |

Il costo unitario complessivo del funding di emergenza è:

| Scenario | $\kappa_s$ |
|---|---:|
| $N$ | 0.01 |
| $P$ | 0.06 |
| $R$ | 0.25 |

Il parametro $\kappa_s$ deve essere interpretato come costo economico complessivo del ricorso alla liquidità in quello scenario, non come semplice tasso di interesse di mercato.

### Ipotesi

1. Gli scenari sono mutuamente esclusivi ed esaustivi.
2. Le probabilità $p_s$ sono note al tempo iniziale.
3. La composizione $x$ è comune a tutti gli scenari e non può essere modificata dopo la rivelazione dell'incertezza.
4. Dopo l'osservazione dello scenario la banca può adattare esclusivamente $u_s$ e $g_s$.
5. Il funding di emergenza è disponibile senza limite quantitativo; ciò garantisce ricorso relativamente completo nel modello didattico.
6. Il costo marginale del funding è lineare all'interno di ciascuno scenario.
7. Non vengono modellati capitale regolamentare, default della banca, assicurazione dei depositi, dinamiche reputazionali o contagio.
8. Rendimenti, coefficienti di liquidabilità, fabbisogni e costi sono dati esogeni.
9. Tutte le quantità monetarie sono espresse in unità convenzionali su scala $A_0=100$.
10. La parametrizzazione non costituisce una stima dei valori storicamente osservati in SVB.

### Formule vincolanti

Per ogni scenario:

$$
\sum_{j=1}^{4}\alpha_{js}x_j+u_s
=
d_s+g_s.
$$

Funzione obiettivo del programma stocastico:

$$
\max
\left\{
\sum_{j=1}^{4}c_jx_j
-
\sum_{s\in\mathcal S}
p_s\kappa_su_s
\right\}.
$$

Il valore ottimo del programma stocastico è indicato con

$$
z^{SP}.
$$

La corrispondente decisione iniziale è

$$
x^{SP}.
$$

Per l'Expected Value problem si utilizzano i parametri medi:

$$
\bar d
=
\sum_s p_sd_s,
$$

$$
\bar\alpha_j
=
\sum_s p_s\alpha_{js},
$$

$$
\bar\kappa
=
\sum_s p_s\kappa_s.
$$

La soluzione del problema medio è $x^{EV}$.

La decisione $x^{EV}$ deve poi essere fissata e rivalutata nel problema stocastico originale, ottenendo il valore

$$
z^{EEV}.
$$

Per un problema di massimizzazione:

$$
VSS
=
z^{SP}-z^{EEV}.
$$

Per il benchmark wait-and-see si risolve un problema separato per ciascuno scenario assumendo di conoscere $s$ prima della decisione $x$. Se $z_s^{WS}$ è il valore ottimo nello scenario $s$:

$$
z^{WS}
=
\sum_s p_sz_s^{WS}.
$$

Per un problema di massimizzazione:

$$
EVPI
=
z^{WS}-z^{SP}.
$$

Devono risultare:

$$
VSS\geq0,
\qquad
EVPI\geq0.
$$

### Quantità finali di interesse

1. $x^{SP}$;
2. $u_s^{SP}$ e $g_s^{SP}$ per ciascuno scenario;
3. $z^{SP}$;
4. $x^{EV}$;
5. $z^{EEV}$;
6. $VSS$;
7. $x_s^{WS}$ e $z_s^{WS}$;
8. $z^{WS}$;
9. $EVPI$;
10. confronto economico tra $x^{SP}$, $x^{EV}$ e $x_s^{WS}$.

## 5. Output richiesti

### Stime o risultati numerici

1. soluzione ottima del programma stocastico;
2. rendimento iniziale lordo della soluzione;
3. funding richiesto nei tre scenari;
4. costo atteso del funding;
5. valore $z^{SP}$;
6. soluzione Expected Value;
7. rivalutazione $z^{EEV}$;
8. $VSS$;
9. tre soluzioni wait-and-see;
10. $z^{WS}$;
11. $EVPI$.

### Tabelle

**Tabella 1 — Parametri del problema**

Rendimenti, probabilità, fabbisogni, costi di funding e coefficienti di liquidabilità.

**Tabella 2 — Soluzione stocastica**

Per ciascun attivo: allocazione $x_j^{SP}$.

Per ciascuno scenario: liquidità generata dagli attivi, funding $u_s$, liquidità residua $g_s$, costo del ricorso.

**Tabella 3 — Confronto informativo**

Colonne:

- SP;
- EV/EEV;
- WS.

Righe:

- decisione iniziale;
- valore;
- funding nello scenario severo;
- informazione disponibile al momento della decisione.

**Tabella 4 — Valore dell'informazione**

$$
z^{EEV},\quad z^{SP},\quad z^{WS},\quad VSS,\quad EVPI.
$$

### Grafici

**Figura 1 — Composizione dell'attivo**

Grafico a barre affiancate per confrontare:

$$
x^{SP}
\quad\text{e}\quad
x^{EV}.
$$

**Figura 2 — Funding per scenario**

Grafico a barre del funding necessario sotto $x^{SP}$ e $x^{EV}$ nei tre scenari.

Il secondo grafico deve rendere visibile la diversa esposizione allo scenario $R$.

### Controlli

1. verifica $\sum_s p_s=1$;
2. verifica $\sum_jx_j=100$;
3. verifica dei limiti $x_3\leq70$, $x_4\leq70$;
4. verifica dei bilanci di liquidità per ogni scenario;
5. verifica della non negatività delle variabili;
6. verifica dello status ottimo del solver;
7. verifica numerica della fattibilità del ricorso;
8. verifica che la stessa $x^{SP}$ sia utilizzata in tutti gli scenari;
9. verifica che $x^{EV}$ sia rivalutata senza riottimizzarla scenario per scenario;
10. verifica
$$
z^{EEV}\leq z^{SP}\leq z^{WS};
$$
11. verifica
$$
VSS\geq0,
\qquad
EVPI\geq0.
$$

## 6. Flusso logico-teorico risolutivo atteso

| Passo | Finalità risolutiva | Formula, definizione, proprietà o teorema | Applicazione nel caso | Output o controllo collegato |
|---:|---|---|---|---|
| 1 | Identificare struttura informativa, decisioni e scenari | Programma stocastico a due stadi; decisione ex ante e ricorso ex post | La composizione $x$ precede la rivelazione di $s$; $u_s$ e $g_s$ dipendono dallo scenario osservato | Corretta distinzione tra primo e secondo stadio; verifica $\sum_s p_s=1$ |
| 2 | Costruire il problema di ricorso e la forma estesa | Bilanci di secondo stadio; ricorso relativamente completo; non anticipatività della decisione iniziale | Per ogni scenario, la liquidità degli attivi e il funding devono coprire il fabbisogno; la stessa $x$ vale in tutti gli scenari | Bilanci scenario per scenario; fattibilità del ricorso; modello pronto per il solver |
| 3 | Determinare la soluzione stocastica | Massimizzazione del rendimento iniziale al netto del costo atteso del ricorso | Ottimizzazione congiunta di $x$ e delle decisioni $u_s,g_s$ nei tre scenari | $x^{SP}$, $u_s^{SP}$, $g_s^{SP}$, $z^{SP}$; controlli di fattibilità e optimality |
| 4 | Costruire e valutare la soluzione Expected Value | Problema sui parametri medi e rivalutazione della soluzione $x^{EV}$ nel problema stocastico originale | Risoluzione del problema medio, fissazione di $x^{EV}$ e calcolo delle conseguenze nei tre scenari | $x^{EV}$, $z^{EEV}$, funding scenario-specifico; verifica $z^{EEV}\leq z^{SP}$ |
| 5 | Costruire il benchmark wait-and-see e misurare il valore dell'informazione | Soluzioni scenario-specifiche con informazione perfetta; definizioni di $VSS$ ed $EVPI$ | Riottimizzazione separata in $N$, $P$, $R$ e confronto con SP ed EEV | $x_s^{WS}$, $z_s^{WS}$, $z^{WS}$, $VSS$, $EVPI$; verifica $z^{EEV}\leq z^{SP}\leq z^{WS}$ |
| 6 | Interpretare economicamente il confronto tra regimi informativi | Trade-off rendimento–liquidità; valore della modellizzazione stocastica e dell'informazione perfetta | Confronto tra composizioni dell'attivo, funding nei diversi scenari e valori dei benchmark | Tabelle, grafici e commento conclusivo su $x^{SP}$, $x^{EV}$, $VSS$, $EVPI$ e limiti del modello |

## 7. Scomposizione attesa in tappe

| Tappa | Regime | Input | Operazione | Output | Controllo | Uso successivo |
|---:|:---:|---|---|---|---|---|
| 1 | A | Scheda Caso, parametri, Capitoli 14–15 | Ricostruire struttura informativa e modello | Schema matematico | Distinzione corretta primo/secondo stadio | Formulazione solver |
| 2 | B | Parametri e formulazione | Implementare dati e forma estesa con `scipy.optimize.linprog(method="highs")` | Soluzione SP | Status solver, vincoli, bilanci | Analisi SP |
| 3 | C/B | Soluzione SP | Estrarre e controllare $x^{SP},u_s,g_s,z^{SP}$ | Tabella SP | Residui dei vincoli | Benchmark EV |
| 4 | B | Parametri medi | Risolvere EV e rivalutare $x^{EV}$ negli scenari originali | $x^{EV},z^{EEV},VSS$ | $VSS\geq0$ | Benchmark WS |
| 5 | B | Tre scenari | Risolvere i tre problemi wait-and-see | $x_s^{WS},z^{WS},EVPI$ | $EVPI\geq0$ | Confronto |
| 6 | C | Tutti gli output | Costruire tabelle, figure e interpretazione finale | Sintesi economico-finanziaria | $z^{EEV}\leq z^{SP}\leq z^{WS}$ | Conclusione notebook |

## 8. Mappa tra prompt e notebook

| Prompt | Regime | Tappa | Celle o output prodotti | Decisione o controllo richiesto |
|---:|:---:|---:|---|---|
| Prompt zero | — | — | Nessuna cella | Inizializzazione del contesto IA |
| Prompt 1 | — | — | Cella Markdown iniziale | Fedeltà alla Scheda Caso |
| Prompt 2 | A | preliminare | Cella Markdown: Flusso logico-teorico | Completezza e ordine del ragionamento |
| Prompt 3 | A | preliminare | Cella Markdown: scomposizione in tappe | Coerenza input-output |
| Prompt tappa 1 | A | 1 | Cella Markdown teorico-modellistica | Corretta struttura informativa |
| Prompt tappa 2 | B | 2 | Celle codice SP | Correttezza della forma solver |
| Prompt tappa 3 | C/B | 3 | Celle di controllo e Tabella SP | Fattibilità e residui |
| Prompt tappa 4 | B | 4 | Celle EV/EEV/VSS | EV non confuso con EEV |
| Prompt tappa 5 | B | 5 | Celle WS/EVPI | Informazione perfetta correttamente interpretata |
| Prompt conclusivo | C | 6 | Commento finale e verifica notebook | Completezza, controlli, limiti |

## 9. Struttura attesa del notebook

Ordine previsto:

1. cella Markdown iniziale prodotta dal Prompt 1;
2. cella Markdown con Flusso logico-teorico risolutivo;
3. cella Markdown con scomposizione in tappe;
4. import delle librerie;
5. definizione dei parametri;
6. controlli preliminari sui dati;
7. costruzione della forma estesa SP;
8. soluzione con HiGHS;
9. estrazione della soluzione;
10. controlli di fattibilità e residui;
11. Tabella 2 — soluzione stocastica;
12. costruzione e soluzione del problema Expected Value;
13. rivalutazione di $x^{EV}$ negli scenari originali;
14. calcolo di $VSS$;
15. costruzione dei tre problemi wait-and-see;
16. calcolo di $z^{WS}$;
17. calcolo di $EVPI$;
18. Tabella 3 — confronto informativo;
19. Tabella 4 — valore dell'informazione;
20. Figura 1 — composizione dell'attivo;
21. Figura 2 — funding per scenario;
22. cella Markdown conclusiva con interpretazione e limiti.

L'implementazione deve privilegiare strutture trasparenti: array NumPy, DataFrame Pandas per l'esposizione dei risultati e `scipy.optimize.linprog(method="highs")` per la soluzione dei programmi lineari.

Non è richiesto costruire classi Python o un framework general-purpose di programmazione stocastica.

## 10. Calibrazione docente

### Ordine di grandezza atteso dei risultati

Con i parametri previsti, salvo differenze numeriche dovute alle tolleranze del solver:

$$
x^{SP}
=
(0,\ 30,\ 70,\ 0)'.
$$

Funding SP:

$$
u_N^{SP}=0,
\qquad
u_P^{SP}=0,
\qquad
u_R^{SP}=3.
$$

Valore:

$$
z^{SP}=3.4375.
$$

La soluzione Expected Value attesa è:

$$
x^{EV}
=
(0,\ 0,\ 30,\ 70)'.
$$

Rivalutando tale decisione negli scenari originali:

$$
u_N^{EV}=0,
\qquad
u_P^{EV}=0,
\qquad
u_R^{EV}=36.
$$

Pertanto:

$$
z^{EEV}=3.3500.
$$

Il valore della soluzione stocastica è:

$$
VSS
=
3.4375-3.3500
=
0.0875.
$$

Per il wait-and-see:

$$
z_N^{WS}=4.7000,
$$

$$
z_P^{WS}=4.7000,
$$

$$
z_R^{WS}=3.4375.
$$

Quindi:

$$
z^{WS}
=
0.60(4.7000)
+
0.25(4.7000)
+
0.15(3.4375)
=
4.510625.
$$

Infine:

$$
EVPI
=
4.510625-3.4375
=
1.073125.
$$

L'ordine fondamentale da ottenere è:

$$
3.3500
<
3.4375
<
4.510625.
$$

### Errori o ambiguità prevedibili

1. confondere $x^{EV}$ con la decisione stocastica;
2. calcolare il valore EV sul problema medio e utilizzarlo direttamente come $z^{EEV}$;
3. riottimizzare $x^{EV}$ dopo avere osservato ciascuno scenario;
4. consentire a $x$ di dipendere dallo scenario nel programma SP;
5. dimenticare le probabilità nella funzione obiettivo;
6. pesare due volte le probabilità;
7. usare $\alpha_{js}$ come rendimento anziché come coefficiente di liquidabilità;
8. interpretare $\kappa_s$ come puro tasso bancario;
9. confondere giacenza $g_s$ e funding $u_s$;
10. invertire i segni di VSS o EVPI in un problema di massimizzazione;
11. confrontare $z^{EV}$ con $z^{SP}$ anziché $z^{EEV}$ con $z^{SP}$;
12. presentare il wait-and-see come strategia realmente implementabile ex ante.

### Controlli minimi di validazione

Devono essere verificati esplicitamente:

$$
\sum_s p_s=1,
$$

$$
\sum_jx_j^{SP}=100,
$$

tutti i bilanci di scenario,

$$
u_s,g_s\geq0,
$$

i limiti di concentrazione,

$$
VSS\geq0,
$$

$$
EVPI\geq0,
$$

e

$$
z^{EEV}\leq z^{SP}\leq z^{WS}.
$$

### Limiti interpretativi

Il caso:

- non ricostruisce quantitativamente SVB;
- non modella una corsa agli sportelli endogena;
- non considera feedback tra decisioni della banca e probabilità degli scenari;
- non considera capitale regolamentare o insolvenza;
- non distingue HTM e AFS;
- non modella duration o mark-to-market dei titoli in modo esplicito;
- non include interventi della Federal Reserve, FDIC o altri strumenti pubblici;
- assume costo lineare del funding;
- assume scenari discreti e probabilità note;
- concentra tutto l'adattamento in un unico secondo stadio.

Questi limiti devono essere dichiarati nella conclusione del notebook.

## 11. Uso dell'IA e tracciato

- **Prompt obbligatori:** Prompt zero; Prompt 1; Prompt 2; Prompt 3; prompt di tappa; prompt conclusivo di verifica in Regime C.
- **Numero minimo e massimo di prompt:** 9–11, conteggiando Prompt zero e Prompt 1.
- **Usi ammessi dell'IA:** chiarimento della struttura a due stadi; verifica della forma solver; supporto alla traduzione in Python; controllo di output già prodotti; revisione di tabelle e grafici; individuazione di errori; verifica finale di completezza e interpretazione.
- **Usi non ammessi:** modifica dei parametri della Scheda Caso; introduzione autonoma di nuovi scenari; sostituzione del problema con un modello diverso; delega globale dell'intero notebook con un unico prompt; modifica delle definizioni di SP, EV, EEV, WS, VSS o EVPI; produzione di interpretazioni storiche non supportate dalle fonti assegnate.

Nel caso aula il docente può guidare la sequenza dei prompt e interrompere il lavoro per discutere collettivamente errori o alternative.

## 12. Valutazione

### Criteri per il notebook

1. correttezza della formulazione matematica;
2. corretta costruzione della forma estesa;
3. corretto utilizzo del solver;
4. correttezza di SP, EV/EEV e WS;
5. calcolo corretto di VSS ed EVPI;
6. qualità dei controlli;
7. leggibilità del codice;
8. qualità delle tabelle;
9. significatività dei grafici;
10. interpretazione economico-finanziaria;
11. dichiarazione dei limiti del modello.

### Criteri per il tracciato IA

1. coerenza con i tre regimi;
2. presenza di contributo iniziale dello studente nei prompt in Regime A;
3. specificità dei prompt in Regime B;
4. uso del Regime C a partire da output o dubbi effettivi;
5. capacità di verificare criticamente le risposte dell'IA;
6. assenza di delega globale;
7. coerenza tra tracciato e notebook finale.

### Peso dei controlli e dell'interpretazione

Per il Caso Aula il docente deve attribuire particolare importanza alla capacità dello studente di spiegare:

- perché $x^{SP}$ differisce da $x^{EV}$;
- perché il funding nello scenario severo è molto maggiore sotto $x^{EV}$;
- perché $VSS$ misura il valore della modellizzazione stocastica e non il valore dell'informazione perfetta;
- perché $EVPI$ costituisce un limite superiore al valore economico della conoscenza anticipata dello scenario.

I risultati numerici privi di controlli e interpretazione non devono essere considerati sufficienti.

## 13. Relazione con l'altro caso della lezione

Il Caso Aula SVB–ALM e il Caso TakeHome sulla crisi LDI britannica del 2022 devono essere progettati come applicazioni metodologicamente comparabili ma finanziariamente differenti.

Nel Caso Aula:

- l'intermediario è una banca;
- la decisione iniziale riguarda la composizione dell'attivo;
- lo shock si manifesta attraverso deflussi della raccolta e deterioramento della liquidabilità degli attivi;
- il ricorso assume la forma di funding di emergenza;
- la struttura principale è a due stadi;
- il focus è su SP, EV/EEV, WS, VSS ed EVPI.

Nel Caso TakeHome:

- il decisore è un investitore istituzionale/fondo pensione con strategia LDI;
- la decisione iniziale riguarda buffer di liquidità ed esposizione;
- lo shock si manifesta attraverso movimenti dei gilt e margin call;
- il ricorso comporta collateral, utilizzo del buffer, vendite e/o deleveraging;
- l'informazione può essere rappresentata in forma progressiva;
- il focus deve estendersi alla non anticipatività e alla logica multistadio.

I due casi condividono quindi la medesima domanda metodologica:

> Quanto conviene sacrificare oggi rendimento o capacità di investimento per preservare possibilità di adattamento quando le condizioni future sono incerte?

La diversità del meccanismo finanziario evita che il TakeHome sia una semplice variazione parametrica del Caso Aula.
