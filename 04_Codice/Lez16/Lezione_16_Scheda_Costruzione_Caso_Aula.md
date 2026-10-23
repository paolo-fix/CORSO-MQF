# Lezione 16 — Scheda Costruzione Caso Aula

Documento interno di progettazione docente.

## 1. Identificazione del caso

- **Lezione:** 16 — Applicazione in Python: programmazione stocastica
- **Tipo di caso:** Caso Aula
- **Titolo:** SVB–ALM 2023 — Asset allocation, liquidità e valore dell'informazione
- **Destinatari:** studenti del secondo anno del Corso di Laurea Magistrale in Finanza e Risk Management
- **Uso previsto:** caso guidato in aula per consolidare computazionalmente il framework di programmazione stocastica lineare a due stadi sviluppato nelle Lezioni 14 e 15, con particolare attenzione a decisione iniziale comune agli scenari, ricorso scenario-specifico, fattibilità, Expected Value, wait-and-see, VSS ed EVPI.

Il Caso Aula utilizza una **versione ridotta two-stage del caso SVB–ALM** sviluppato nei Capitoli 14 e 15. Non viene riprodotta integralmente la struttura multiperiodale del caso teorico: l'incertezza futura è compressa in tre scenari completi di liquidità e il ricorso è rappresentato mediante un unico blocco di decisioni scenario-specifiche.

Rimangono invariati i principi essenziali del modello a due stadi:

1. una decisione iniziale unica e comune agli scenari;
2. rivelazione dello scenario successiva alla decisione iniziale;
3. decisioni di ricorso dipendenti dallo scenario osservato;
4. valutazione ex ante mediante probabilità;
5. confronto tra SP, EV e WS.

---

## 2. Contesto e motivazione

Il caso è contestualizzato nella crisi di Silicon Valley Bank del marzo 2023.

La vicenda storica viene utilizzata come riferimento economico-finanziario per rappresentare il trade-off tra:

- rendimento della composizione iniziale dell'attivo;
- liquidabilità delle diverse classi di attivo;
- intensità dei deflussi di raccolta;
- costo del funding di emergenza.

Il modello è deliberatamente stilizzato e non costituisce una ricostruzione del bilancio storico di SVB.

La motivazione didattica consiste nel mostrare che una decisione iniziale più redditizia può risultare maggiormente esposta ai costi di ricorso negli scenari avversi. La programmazione stocastica consente di incorporare ex ante la distribuzione degli scenari e le possibilità di adattamento lasciate aperte dalla scelta iniziale.

Il caso permette inoltre di rendere operativi concetti già sviluppati teoricamente:

1. decisione here-and-now;
2. scenari e probabilità;
3. ricorso;
4. forma estesa;
5. fattibilità del ricorso;
6. soluzione stocastica;
7. Expected Value;
8. wait-and-see;
9. Value of the Stochastic Solution;
10. Expected Value of Perfect Information.

**Fonti storiche di riferimento per il docente:** Federal Reserve, *Review of the Federal Reserve's Supervision and Regulation of Silicon Valley Bank*, aprile 2023; FDIC, documentazione sulla receivership di Silicon Valley Bank.

I valori numerici del caso hanno finalità didattica e sono espressi nella scala normalizzata \(A_0=100\).

---

## 3. Domanda quantitativa e funzione didattica

**Domanda quantitativa:**  
quale composizione iniziale dell'attivo massimizza il risultato economico atteso della banca quando fabbisogni di liquidità, liquidabilità degli attivi e costo del funding dipendono dallo scenario futuro? Quanto valore produce una decisione stocastica rispetto alla decisione costruita sullo scenario medio e quanto varrebbe conoscere anticipatamente lo scenario che si realizzerà?

**Obiettivo didattico:**  
portare lo studente dalla formulazione teorica a due stadi alla costruzione, soluzione e validazione in Python di un programma stocastico lineare, rendendo osservabili la distinzione tra decisione ex ante, adattamento ex post e informazione perfetta.

**Collegamento con le lezioni teoriche precedenti:**  

- Lezione 14: scenari, decisione di primo stadio, ricorso, forma estesa e non anticipatività;
- Lezione 15: fattibilità del ricorso, proprietà della soluzione, SP, EV, WS, VSS ed EVPI;
- Capitolo 15: fornisce inoltre l'estensione teorica multistadio, che non viene implementata nel presente caso.

**Concetti teorici da rendere osservabili:**

1. unicità della decisione iniziale \(x\);
2. dipendenza scenario-specifica del ricorso;
3. ricorso relativamente completo;
4. forma estesa deterministica;
5. rivalutazione della soluzione Expected Value;
6. distinzione tra valore ottimo del problema medio e \(z^{EV}\);
7. ordinamento \(z^{EV}\leq z^{SP}\leq z^{WS}\) nel problema di massimizzazione;
8. interpretazione di VSS ed EVPI.

**Funzione della procedura computazionale:**  
la dimensione della forma estesa, la presenza di più scenari e la necessità di costruire e confrontare SP, EV e WS rendono naturale l'utilizzo di un solver lineare. Python consente inoltre di rendere espliciti controlli, rivalutazioni, tabelle e grafici.

**Ruolo dell'informazione, degli scenari e dei vincoli:**  
la decisione iniziale viene assunta prima della rivelazione dello scenario. Lo scenario determina fabbisogno, liquidabilità e costo del funding. Dopo l'osservazione dello scenario possono adattarsi soltanto le decisioni di ricorso. La non anticipatività è incorporata strutturalmente mediante un'unica decisione \(x\) comune a tutti gli scenari.

---

## 4. Specifica teorico-matematica

### Grandezze e variabili

Le risorse iniziali sono:

\[
A_0=100.
\]

La decisione di primo stadio è:

\[
x=(x_1,x_2,x_3,x_4)'.
\]

Le componenti rappresentano:

| Variabile | Classe di attivo | Rendimento unitario |
|---|---|---:|
| \(x_1\) | Cassa e riserve | 0.010 |
| \(x_2\) | Titoli a breve scadenza | 0.025 |
| \(x_3\) | Titoli a lunga scadenza | 0.040 |
| \(x_4\) | Prestiti e impieghi meno liquidi | 0.050 |

Vincolo di bilancio:

\[
x_1+x_2+x_3+x_4=100.
\]

Vincoli:

\[
x_j\geq0,
\qquad j=1,\ldots,4,
\]

\[
x_3\leq70,
\qquad
x_4\leq70.
\]

Le decisioni di ricorso nello scenario \(s\) sono:

\[
u_s\geq0,
\]

funding di emergenza, e

\[
g_s\geq0,
\]

liquidità residua.

### Eventi, informazione, stati o scenari

L'insieme degli scenari è:

\[
\mathcal S=\{N,P,R\},
\]

con:

- \(N\): condizioni normali;
- \(P\): pressione sulla raccolta;
- \(R\): run severo.

Le probabilità sono:

| Scenario | \(p_s\) |
|---|---:|
| \(N\) | 0.60 |
| \(P\) | 0.25 |
| \(R\) | 0.15 |

Deve risultare:

\[
\sum_{s\in\mathcal S}p_s=1.
\]

La struttura informativa è:

\[
x
\longrightarrow
s
\longrightarrow
(u_s,g_s).
\]

### Parametri e dati

I fabbisogni di liquidità sono:

| Scenario | \(d_s\) |
|---|---:|
| \(N\) | 15 |
| \(P\) | 35 |
| \(R\) | 65 |

Il coefficiente \(\alpha_{js}\) rappresenta la quota dell'investimento \(x_j\) trasformabile in liquidità nello scenario \(s\).

| Attivo | \(N\) | \(P\) | \(R\) |
|---|---:|---:|---:|
| Cassa e riserve \(x_1\) | 1.00 | 1.00 | 1.00 |
| Titoli brevi \(x_2\) | 0.98 | 0.95 | 0.90 |
| Titoli lunghi \(x_3\) | 0.85 | 0.70 | 0.50 |
| Prestiti/impieghi \(x_4\) | 0.60 | 0.40 | 0.20 |

Il costo unitario complessivo del funding di emergenza è:

| Scenario | \(\kappa_s\) |
|---|---:|
| \(N\) | 0.01 |
| \(P\) | 0.06 |
| \(R\) | 0.25 |

### Ipotesi modellistiche

1. Gli scenari sono mutuamente esclusivi ed esaustivi.
2. Le probabilità sono note al tempo iniziale.
3. La decisione \(x\) è unica e comune agli scenari.
4. Dopo l'osservazione dello scenario possono adattarsi soltanto \(u_s\) e \(g_s\).
5. Il funding di emergenza è disponibile senza limite quantitativo.
6. Il ricorso è pertanto relativamente completo nel modello assegnato.
7. Il costo del funding è lineare.
8. Rendimenti, liquidabilità, fabbisogni e costi sono esogeni.
9. Le quantità monetarie sono espresse nella scala normalizzata \(A_0=100\).
10. Il modello non costituisce una ricostruzione quantitativa di SVB.

### Formule vincolanti

Per ogni scenario:

\[
\sum_{j=1}^{4}\alpha_{js}x_j+u_s
=
d_s+g_s.
\]

Il programma stocastico è:

\[
\max
\left\{
\sum_{j=1}^{4}c_jx_j
-
\sum_{s\in\mathcal S}p_s\kappa_su_s
\right\}.
\]

Il valore ottimo è:

\[
z^{SP},
\]

con decisione:

\[
x^{SP}.
\]

Per il problema Expected Value:

\[
\bar d
=
\sum_s p_sd_s,
\]

\[
\bar\alpha_j
=
\sum_s p_s\alpha_{js},
\]

\[
\bar\kappa
=
\sum_s p_s\kappa_s.
\]

La soluzione del problema medio è:

\[
x^{EV}.
\]

La decisione \(x^{EV}\) deve essere fissata e rivalutata negli scenari originari. Il valore ottenuto è:

\[
z^{EV}.
\]

Per il problema di massimizzazione:

\[
VSS
=
z^{SP}-z^{EV}.
\]

Nel benchmark wait-and-see:

\[
z^{WS}
=
\sum_s p_sz_s^{WS},
\]

e:

\[
EVPI
=
z^{WS}-z^{SP}.
\]

### Quantità teoriche da stimare o calcolare

1. \(x^{SP}\);
2. \(u_s^{SP}\) e \(g_s^{SP}\);
3. \(z^{SP}\);
4. \(x^{EV}\);
5. valore ottimo del problema deterministico medio;
6. \(z^{EV}\);
7. \(VSS\);
8. \(x_s^{WS}\);
9. \(z_s^{WS}\);
10. \(z^{WS}\);
11. \(EVPI\).

### Proprietà teoriche da verificare

\[
z^{EV}\leq z^{SP}\leq z^{WS},
\]

\[
VSS\geq0,
\qquad
EVPI\geq0.
\]

Devono inoltre essere distinti:

- problema deterministico medio;
- decisione \(x^{EV}\);
- valore stocastico rivalutato \(z^{EV}\);
- benchmark wait-and-see.

### Soglie, target o vincoli rilevanti

\[
x_3\leq70,
\qquad
x_4\leq70.
\]

Tali limiti impediscono concentrazioni estreme che renderebbero didatticamente poco informativa la soluzione.

### Quantità finali di interesse

Le quantità centrali sono:

\[
x^{SP},
\quad
x^{EV},
\quad
z^{EV},
\quad
z^{SP},
\quad
z^{WS},
\quad
VSS,
\quad
EVPI,
\]

insieme ai ricorsi scenario-specifici.

### Limiti del modello

Il caso:

- non ricostruisce quantitativamente SVB;
- non modella una corsa agli sportelli endogena;
- non considera capitale regolamentare o insolvenza;
- non distingue HTM e AFS;
- non modella duration e mark-to-market in modo esplicito;
- non considera feedback tra decisioni e probabilità degli scenari;
- non include strumenti pubblici di emergenza;
- assume costo lineare del funding;
- assume scenari discreti e probabilità note;
- concentra tutto l'adattamento in un unico secondo stadio.

---

## 5. Output richiesti

Gli output devono consentire di ricostruire il passaggio dalla formulazione alla soluzione, verificare la correttezza numerica e interpretare il trade-off rendimento–liquidità.

### Stime o risultati numerici

Calcolare:

1. \(x^{SP}\);
2. rendimento iniziale lordo;
3. \(u_s^{SP}\) e \(g_s^{SP}\);
4. costo atteso del funding;
5. \(z^{SP}\);
6. parametri medi;
7. \(x^{EV}\);
8. valore ottimo del problema deterministico medio;
9. \(z^{EV}\);
10. \(VSS\);
11. \(x_s^{WS}\) e \(z_s^{WS}\);
12. \(z^{WS}\);
13. \(EVPI\).

### Tabelle

**Tabella 1 — Parametri del problema**

Deve rappresentare rendimenti, probabilità, fabbisogni, liquidabilità, costi del funding e limiti sulle allocazioni.

Funzione: rendere verificabile la specifica numerica utilizzata dal solver.

**Tabella 2 — Soluzione stocastica**

Deve riportare:

- \(x_j^{SP}\);
- liquidità ottenibile dagli attivi per scenario;
- \(u_s^{SP}\);
- \(g_s^{SP}\);
- costo del funding per scenario.

Funzione: rendere osservabile la decisione comune e il ricorso scenario-specifico.

**Tabella 3 — Expected Value e rivalutazione**

Deve riportare:

- parametri medi;
- \(x^{EV}\);
- valore ottimo del problema medio;
- ricorso necessario negli scenari originari;
- \(z^{EV}\);
- confronto con \(x^{SP}\).

Funzione: distinguere problema medio e valutazione stocastica della decisione media.

**Tabella 4 — Wait-and-see**

Per ciascuno scenario:

- \(x_s^{WS}\);
- \(z_s^{WS}\).

Funzione: rendere osservabile l'effetto dell'informazione perfetta.

**Tabella 5 — Confronto dei benchmark**

Deve contenere:

\[
z^{EV},
\qquad
z^{SP},
\qquad
z^{WS},
\qquad
VSS,
\qquad
EVPI.
\]

Funzione: sintetizzare il valore della modellizzazione stocastica e dell'informazione perfetta.

### Grafici

**Figura 1 — Composizione dell'attivo**

Confronto a barre tra:

\[
x^{SP}
\quad\text{e}\quad
x^{EV}.
\]

Domanda interpretativa: quale sacrificio di rendimento o liquidità distingue la decisione stocastica dalla decisione costruita sullo scenario medio?

**Figura 2 — Funding per scenario**

Confronto del funding necessario sotto:

\[
x^{SP}
\quad\text{e}\quad
x^{EV}
\]

nei tre scenari.

Domanda interpretativa: in quale misura la scelta Expected Value espone maggiormente la banca allo scenario severo?

### Controlli

1. \(\sum_s p_s=1\);
2. \(\sum_jx_j=100\);
3. \(x_j\geq0\);
4. \(x_3\leq70\);
5. \(x_4\leq70\);
6. bilancio di liquidità in ciascuno scenario;
7. \(u_s,g_s\geq0\);
8. successo del solver;
9. assenza di violazioni significative dei vincoli;
10. unicità della decisione \(x^{SP}\) tra gli scenari;
11. fissazione di \(x^{EV}\) nella rivalutazione;
12. separazione dei problemi WS;
13. verifica di
   \[
   z^{EV}\leq z^{SP}\leq z^{WS};
   \]
14. verifica di
   \[
   VSS\geq0,
   \qquad
   EVPI\geq0.
   \]

---

## 6. Flusso logico-teorico risolutivo atteso

| Passo | Finalità risolutiva | Formula, definizione, proprietà o teorema | Applicazione nel caso | Output o controllo collegato |
|---:|---|---|---|---|
| 1 | Identificare struttura informativa, scenari e decisioni | Programma stocastico a due stadi; decisione ex ante e ricorso ex post | \(x\) precede lo scenario; \(u_s,g_s\) dipendono dallo scenario osservato | classificazione corretta delle variabili; controllo delle probabilità |
| 2 | Costruire il ricorso e la forma estesa | Bilanci di secondo stadio; ricorso relativamente completo; unicità di \(x\) | liquidità degli attivi più funding deve coprire il fabbisogno | bilanci per scenario; fattibilità; struttura solver |
| 3 | Determinare la soluzione stocastica | Massimizzazione del rendimento al netto del costo atteso del ricorso | ottimizzazione congiunta di \(x,u_s,g_s\) | \(x^{SP},u_s^{SP},g_s^{SP},z^{SP}\) |
| 4 | Costruire e rivalutare Expected Value | Problema sui parametri medi; rivalutazione di \(x^{EV}\) negli scenari originari | \(x^{EV}\) resta fissa, si riottimizza soltanto il ricorso | \(x^{EV}\), valore del problema medio, \(z^{EV}\), \(VSS\) |
| 5 | Costruire wait-and-see | Ottimizzazione scenario per scenario con informazione perfetta | decisione iniziale scenario-specifica \(x_s^{WS}\) | \(x_s^{WS},z_s^{WS},z^{WS},EVPI\) |
| 6 | Verificare e interpretare i benchmark | \(z^{EV}\leq z^{SP}\leq z^{WS}\); \(VSS,EVPI\geq0\) | confronto tra composizioni, funding e valori | tabelle, grafici, controlli conclusivi e base quantitativa per l'interpretazione dello studente |

---

## 7. Scomposizione attesa in tappe

| Tappa | Titolo | Obiettivo | Input | Regime IA prevalente | Prompt virtuoso di riferimento | Oggetti teorici coinvolti | Operazione | Output | Controllo | Uso successivo |
|---:|---|---|---|:---:|---|---|---|---|---|---|
| 1 | Struttura del modello e dati | Tradurre la Scheda Caso nella struttura matematica e computazionale | Scheda Caso, Flusso validato | A/B | chiarimento teorico + definizione parametri | scenari, \(x\), \(y_s\), probabilità, vincoli | organizzare dati e struttura del problema | Tabella 1 e schema delle variabili | probabilità, parametri, ordinamento variabili | costruzione della forma estesa |
| 2 | Forma estesa e soluzione SP | Costruire e risolvere il programma stocastico | parametri e struttura validati | B | traduzione operativa in codice | forma estesa, funzione obiettivo, bilanci | costruire matrici, bounds e risolvere con HiGHS | soluzione SP | status solver, residui, vincoli | analisi del ricorso |
| 3 | Analisi e controlli della soluzione SP | Rendere osservabili decisione iniziale e ricorso | soluzione SP | B | output e controlli | fattibilità, bilanci, unicità di \(x\) | estrarre risultati e costruire controlli | Tabella 2 | bilanci, bounds, unicità di \(x\) | confronto con EV |
| 4 | Expected Value e rivalutazione | Costruire \(x^{EV}\) e valutarla correttamente | parametri originari e medi | B | traduzione operativa in codice | problema medio, \(x^{EV}\), \(z^{EV}\), VSS | risolvere EV, fissare \(x^{EV}\), rivalutare il ricorso | Tabella 3, \(z^{EV}\), VSS | nessuna riottimizzazione di \(x\); \(z^{EV}\leq z^{SP}\) | confronto informativo |
| 5 | Wait-and-see e informazione perfetta | Costruire il benchmark con conoscenza anticipata dello scenario | scenari originari | B | traduzione operativa in codice | WS, \(z^{WS}\), EVPI | risolvere tre problemi scenario-specifici | Tabella 4, \(z^{WS}\), EVPI | ponderazione corretta; \(z^{SP}\leq z^{WS}\) | sintesi finale |
| 6 | Confronto, grafici e controlli conclusivi | Integrare benchmark e output quantitativi senza delegare l'interpretazione finale | output delle tappe 1–5 | B | output, grafici e controlli | ordinamento SP/EV/WS, VSS, EVPI | produrre Tabella 5, Figure 1–2 e controlli finali | pacchetto quantitativo finale | ordinamento, segni, completezza output | interpretazione autonoma dello studente |

Il **Regime C non costituisce una tappa ordinaria**. Può essere attivato in qualunque fase soltanto se lo studente individua una criticità specifica da verificare.

---

## 8. Sequenza docente dei prompt e mappa prompt-notebook

**Sequenza docente dei prompt virtuosi:**

1. Prompt zero;
2. Prompt 1;
3. Prompt 2;
4. Prompt 3;
5. prompt relativi alle Tappe 1–6 secondo i regimi A/B validati;
6. eventuali Prompt C esclusivamente in presenza di criticità specifiche individuate dallo studente.

Il numero complessivo dei prompt **non è fissato a priori**: deriva dalla scomposizione operativa effettivamente validata e dagli eventuali approfondimenti necessari.

| Prompt | Regime | Tappa o fase | Funzione del prompt | Celle o output prodotti | Decisione o controllo richiesto |
|---|:---:|---|---|---|---|
| Prompt zero | — | inizializzazione | inizializzare regole e regimi | nessuna cella | acquisizione del protocollo |
| Prompt 1 | — | inquadramento | acquisire la Scheda Caso | Markdown iniziale | fedeltà alla Scheda Caso |
| Prompt 2 | A | preliminare | costruire il Flusso logico-teorico | Markdown | ordine teorico e completezza |
| Prompt 3 | A/B | preliminare | costruire la scomposizione input-output | Markdown | copertura di output e controlli |
| Prompt Tappa 1 | A/B | 1 | chiarire struttura e organizzare dati | Markdown e, se pertinente, codice | coerenza parametri e variabili |
| Prompt Tappa 2 | B | 2 | costruire la forma estesa e risolvere SP | Markdown + codice | correttezza solver |
| Prompt Tappa 3 | B | 3 | estrarre e controllare SP | Markdown + codice | fattibilità e bilanci |
| Prompt Tappa 4 | B | 4 | costruire EV e rivalutazione | Markdown + codice | distinzione problema medio / \(z^{EV}\) |
| Prompt Tappa 5 | B | 5 | costruire WS ed EVPI | Markdown + codice | informazione perfetta e ponderazione |
| Prompt Tappa 6 | B | 6 | produrre sintesi quantitativa e controlli | Markdown + codice | completezza e ordinamento benchmark |
| Eventuale Prompt C | C | fase interessata | verificare una criticità specifica già individuata | eventuale sostituzione delle celle interessate | criticità respinta / accolta |

L'interpretazione finanziaria finale non viene delegata a un prompt C: è responsabilità dello studente.

---

## 9. Struttura attesa del notebook

Ordine logico previsto:

1. cella Markdown iniziale derivata dal Prompt 1;
2. Flusso logico-teorico risolutivo;
3. scomposizione in tappe input-output;
4. import delle librerie;
5. definizione dei parametri;
6. controllo preliminare dei dati;
7. Tabella 1 — parametri;
8. costruzione del vettore delle variabili della forma estesa;
9. costruzione della funzione obiettivo SP;
10. costruzione delle uguaglianze;
11. costruzione dei bounds;
12. soluzione SP con `scipy.optimize.linprog(method="highs")`;
13. estrazione di \(x^{SP},u_s^{SP},g_s^{SP}\);
14. controlli di fattibilità e residui;
15. Tabella 2 — soluzione stocastica;
16. calcolo dei parametri medi;
17. costruzione e soluzione del problema EV;
18. estrazione di \(x^{EV}\);
19. rivalutazione di \(x^{EV}\) negli scenari originari;
20. calcolo di \(z^{EV}\);
21. calcolo del VSS;
22. Tabella 3 — EV e rivalutazione;
23. costruzione dei tre problemi WS;
24. soluzione dei problemi WS;
25. calcolo di \(z^{WS}\);
26. calcolo dell'EVPI;
27. Tabella 4 — wait-and-see;
28. Tabella 5 — confronto dei benchmark;
29. Figura 1 — confronto \(x^{SP}\) / \(x^{EV}\);
30. Figura 2 — funding per scenario;
31. controlli conclusivi;
32. interpretazione finanziaria finale autonoma;
33. limiti del modello;
34. sintesi finale.

Librerie previste:

- NumPy;
- pandas;
- `scipy.optimize.linprog`;
- matplotlib.

Le tabelle e i grafici devono essere output rigenerabili del notebook. Non sono previste esportazioni automatiche in file esterni.

---

## 10. Criteri di validazione del notebook

Il notebook è valido se:

1. implementa senza modifiche la specifica della Scheda Caso;
2. utilizza i parametri assegnati;
3. mantiene un'unica decisione iniziale \(x\) comune agli scenari;
4. costruisce correttamente la forma estesa;
5. mantiene coerente l'ordinamento delle variabili nel solver;
6. produce una soluzione ottima e ammissibile;
7. verifica esplicitamente i bilanci scenario-specifici;
8. calcola correttamente SP;
9. costruisce il problema EV utilizzando i parametri medi;
10. mantiene \(x^{EV}\) fissa nella rivalutazione;
11. distingue il valore ottimo del problema medio da \(z^{EV}\);
12. costruisce separatamente i tre problemi WS;
13. calcola correttamente VSS ed EVPI;
14. verifica:
   \[
   z^{EV}\leq z^{SP}\leq z^{WS};
   \]
15. verifica:
   \[
   VSS\geq0,
   \qquad
   EVPI\geq0;
   \]
16. produce tutte le cinque tabelle previste;
17. produce entrambe le figure previste;
18. rispetta la scomposizione in tappe validata;
19. mantiene coerenti notazione matematica e nomi Python;
20. conclude con un'interpretazione compatibile con output e limiti.

**Criteri specifici del caso:**

- nessuna decisione di primo stadio può diventare scenario-specifica nel programma SP;
- il funding illimitato deve rendere ammissibile il ricorso per ogni \(x\) ammissibile di primo stadio;
- la rivalutazione di \(x^{EV}\) deve modificare esclusivamente le variabili di ricorso;
- il benchmark WS deve consentire una nuova \(x_s^{WS}\) per ciascuno scenario.

---

## 11. Calibrazione docente

### Ordine di grandezza atteso dei risultati

La soluzione stocastica attesa è:

\[
x^{SP}
=
(0,\ 30,\ 70,\ 0)'.
\]

Funding:

\[
u_N^{SP}=0,
\qquad
u_P^{SP}=0,
\qquad
u_R^{SP}=3.
\]

Valore:

\[
z^{SP}=3.4375.
\]

La soluzione Expected Value attesa è:

\[
x^{EV}
=
(0,\ 0,\ 30,\ 70)'.
\]

Rivalutazione:

\[
u_N^{EV}=0,
\qquad
u_P^{EV}=0,
\qquad
u_R^{EV}=36.
\]

\[
z^{EV}=3.3500.
\]

Pertanto:

\[
VSS
=
3.4375-3.3500
=
0.0875.
\]

Per il wait-and-see:

\[
z_N^{WS}=4.7000,
\]

\[
z_P^{WS}=4.7000,
\]

\[
z_R^{WS}=3.4375.
\]

Quindi:

\[
z^{WS}
=
4.510625.
\]

Infine:

\[
EVPI
=
4.510625-3.4375
=
1.073125.
\]

L'ordinamento atteso è:

\[
3.3500
<
3.4375
<
4.510625.
\]

### Errori o ambiguità prevedibili

1. consentire a \(x\) di dipendere dallo scenario;
2. confondere \(x^{EV}\) con \(x^{SP}\);
3. confondere il valore ottimo del problema medio con \(z^{EV}\);
4. riottimizzare \(x^{EV}\) nella rivalutazione;
5. dimenticare le probabilità nella funzione obiettivo SP;
6. ponderare due volte i costi;
7. confondere \(\alpha_{js}\) con un rendimento;
8. interpretare \(\kappa_s\) come puro tasso di interesse;
9. confondere \(u_s\) e \(g_s\);
10. invertire i segni di VSS o EVPI;
11. costruire WS mantenendo artificialmente comune \(x\);
12. interpretare WS come decisione implementabile ex ante.

### Controlli minimi di validazione

Devono risultare verificati:

\[
\sum_s p_s=1,
\]

\[
\sum_jx_j^{SP}=100,
\]

\[
u_s,g_s\geq0,
\]

i limiti sulle allocazioni, i bilanci scenario-specifici e:

\[
z^{EV}\leq z^{SP}\leq z^{WS},
\]

\[
VSS\geq0,
\qquad
EVPI\geq0.
\]

### Limiti interpretativi

Gli output devono essere interpretati esclusivamente entro la specificazione stilizzata assegnata.

---

## 12. Uso dell'IA e tracciato

- **Uso documentato dell'IA previsto:** sì.
- **Prompt obbligatori:** Prompt zero, Prompt 1, Prompt 2, Prompt 3 e prompt di tappa necessari secondo la scomposizione validata.
- **Numero dei prompt:** determinato dalla scomposizione operativa effettivamente utilizzata; eventuali Prompt C si aggiungono soltanto se emerge una criticità specifica individuata dallo studente.
- **Regimi IA ordinari:** A e B.
- **Regime C:** eventuale, non obbligatorio, esclusivamente per verificare una criticità specifica già individuata.

**Usi ammessi dell'IA:**

- chiarimento della struttura two-stage;
- verifica del collegamento tra formule e forma solver;
- supporto alla traduzione in Python;
- costruzione locale di codice per una tappa già definita;
- revisione di tabelle e grafici;
- verifica mirata di criticità specifiche;
- controllo della coerenza tra output e vincoli.

**Usi non ammessi:**

- modifica della Scheda Caso;
- modifica di scenari, probabilità o parametri;
- sostituzione del modello two-stage con un modello diverso;
- delega globale del notebook;
- modifica delle definizioni di SP, EV, WS, VSS ed EVPI;
- confusione tra valore del problema medio e \(z^{EV}\);
- produzione autonoma dell'interpretazione finale;
- uso del Regime C come verifica generica dell'intero notebook.

**Criteri di validazione delle risposte IA:**

1. rispetto del regime richiesto;
2. rispetto degli input disponibili;
3. assenza di modifiche non autorizzate;
4. coerenza con la Scheda Caso;
5. correttezza della traduzione computazionale;
6. pertinenza degli output;
7. presenza dei controlli richiesti;
8. utilità dell'output per la tappa successiva;
9. nel Regime C, corretta classificazione in criticità respinta o accolta.

- **Tracciato IA richiesto:** sì.
- **Modalità di consegna:** stampa PDF della chat dedicata.
- **Sequenza osservabile:** Prompt zero → Prompt 1 → Prompt 2 → Prompt 3 → prompt di tappa effettivamente utilizzati → eventuali Prompt C.

---

## 13. Valutazione

### Criteri per il notebook

1. correttezza della formulazione matematica;
2. correttezza della forma estesa;
3. corretto utilizzo del solver;
4. correttezza della soluzione SP;
5. corretta costruzione e rivalutazione di EV;
6. corretta costruzione di WS;
7. corretto calcolo di VSS ed EVPI;
8. qualità dei controlli;
9. leggibilità e modularità del codice;
10. qualità delle tabelle;
11. significatività dei grafici;
12. coerenza tra formule e output;
13. interpretazione economico-finanziaria;
14. consapevolezza dei limiti.

### Criteri per il tracciato IA

1. qualità del contributo iniziale dello studente in Prompt 2;
2. qualità della proposta operativa in Prompt 3;
3. specificità dei prompt di tappa;
4. corretto uso dei Regimi A/B;
5. eventuale uso del Regime C soltanto su criticità specifiche;
6. capacità di valutare criticamente le risposte IA;
7. assenza di delega globale;
8. coerenza tra tracciato e notebook finale.

### Peso dei controlli e dell'interpretazione

Particolare importanza deve essere attribuita alla capacità di spiegare:

- perché \(x^{SP}\) differisce da \(x^{EV}\);
- perché il funding nello scenario \(R\) è molto maggiore sotto \(x^{EV}\);
- perché il VSS misura il valore dell'utilizzo esplicito della distribuzione degli scenari;
- perché EVPI misura il valore dell'informazione perfetta;
- perché WS non è una strategia implementabile ex ante.

---

## 14. Rubrica sintetica

Per il Caso Aula la rubrica ha funzione prevalentemente formativa e può essere utilizzata come riferimento per il controllo del lavoro svolto.

| Area | Peso | Criteri principali |
|---|---:|---|
| Prompt 2 — Flusso logico-teorico | 20 | ordine teorico, collegamento tra modello, output e controlli |
| Prompt 3 — Scomposizione input-output | 15 | coerenza delle tappe e collegamento tra input e output |
| Notebook e output computazionali | 30 | correttezza del codice, solver, tabelle, grafici e riproducibilità |
| Prompt di tappa e uso dei Regimi A/B | 10 | specificità, rispetto dei vincoli e appropriatezza dell'uso dell'IA |
| Verifiche logiche e numeriche | 20 | vincoli, bilanci, benchmark, ordinamenti e controlli |
| Interpretazione finanziaria finale | 5 | autonomia, coerenza e consapevolezza dei limiti |

**Totale:** 100 punti.

L'eventuale Regime C viene valutato all'interno della qualità del processo soltanto quando effettivamente attivato su una criticità specifica.

---

## 15. Esito atteso e calibrazione qualitativa del caso

**Esito atteso:**  
la soluzione stocastica deve risultare più orientata alla liquidità rispetto alla soluzione Expected Value e deve ridurre sensibilmente il ricorso al funding nello scenario severo.

**Ordini di grandezza o relazioni attese:**

\[
x^{SP}
=
(0,30,70,0)',
\]

\[
x^{EV}
=
(0,0,30,70)',
\]

\[
z^{EV}
<
z^{SP}
<
z^{WS}.
\]

Il funding nello scenario severo deve risultare molto più elevato sotto \(x^{EV}\) che sotto \(x^{SP}\).

**Funzione didattica degli output:**

- \(x^{SP}\) rende osservabile il compromesso ex ante tra rendimento e costo del ricorso;
- \(x^{EV}\) mostra il limite della sostituzione degli scenari con i valori medi;
- il confronto dei funding rende visibile l'esposizione agli scenari avversi;
- VSS misura il valore della modellizzazione stocastica;
- EVPI misura il valore dell'informazione perfetta.

**Possibili segnali di cattiva calibrazione:**

1. \(x^{SP}=x^{EV}\) senza ragione economica;
2. VSS nullo o negativo per errori di costruzione;
3. EVPI negativo;
4. funding identico nei tre scenari;
5. soluzione SP concentrata su un unico attivo per effetto di parametri degeneri;
6. violazione dell'ordinamento dei benchmark;
7. output numericamente corretti ma privi di differenze economicamente interpretabili.

---

## 16. Relazione con l'altro caso della lezione

Il Caso Aula SVB–ALM e il Caso TakeHome UK LDI 2022 devono essere metodologicamente comparabili ma finanziariamente differenti.

### 1. Concetti teorici comuni

Entrambi consolidano:

- programmazione stocastica two-stage;
- decisione iniziale unica;
- scenari discreti;
- ricorso scenario-specifico;
- forma estesa;
- SP;
- Expected Value;
- wait-and-see;
- EVPI;
- fattibilità del ricorso.

Il VSS viene calcolato quando \(z^{EV}\) è definito nella forma standard.

### 2. Strumenti computazionali comuni

Entrambi utilizzano:

- NumPy;
- pandas;
- `scipy.optimize.linprog(method="highs")`;
- matplotlib;
- costruzione esplicita della forma solver;
- controlli sui vincoli;
- confronto dei benchmark.

### 3. Output comparabili

Entrambi producono:

- decisione SP;
- ricorso per scenario;
- decisione EV;
- rivalutazione di EV;
- soluzioni WS;
- benchmark informativi;
- tabelle comparative;
- grafici delle decisioni e del ricorso.

### 4. Controlli comparabili

Entrambi richiedono:

- controllo delle probabilità;
- controllo dei vincoli di primo stadio;
- controllo dei bilanci di secondo stadio;
- controllo dello status del solver;
- fissazione di \(x^{EV}\) nella rivalutazione;
- separazione dei problemi WS;
- verifica dei benchmark effettivamente definiti.

### 5. Elementi metodologici comuni

In entrambi i casi vale la sequenza:

Scheda Caso  
→ Flusso logico-teorico  
→ scomposizione in tappe  
→ notebook  
→ controlli conclusivi  
→ interpretazione autonoma dello studente.

### 6. Elementi distintivi del Caso TakeHome

Nel Caso Aula:

- il decisore è una banca;
- la decisione iniziale riguarda la composizione dell'attivo;
- lo shock riguarda fabbisogni e liquidabilità;
- il ricorso principale è funding di emergenza;
- il funding illimitato garantisce ricorso relativamente completo;
- \(z^{EV}\) e VSS sono definiti.

Nel Caso TakeHome:

- il decisore è un investitore istituzionale con strategia LDI;
- la decisione riguarda buffer ed esposizione;
- lo shock produce margin call;
- il ricorso combina liquidità aggiuntiva e deleveraging;
- le capacità di ricorso sono limitate;
- la fattibilità del ricorso diventa parte sostanziale dell'analisi;
- la soluzione Expected Value può risultare inammissibile in uno scenario, rendendo non definibili nella forma standard \(z^{EV}\) e VSS.

Il TakeHome resta quindi **two-stage** e non introduce informazione progressiva o vincoli di non anticipatività tra nodi intermedi.

### 7. Ripartizione delle responsabilità

**Docente:**

- definisce e valida Scheda Costruzione e Scheda Caso;
- verifica la calibrazione;
- guida il Caso Aula;
- valida il protocollo e i benchmark.

**Studente:**

- propone il Flusso logico-teorico;
- propone la scomposizione in tappe;
- formula i prompt;
- valida le risposte IA;
- esegue i controlli;
- produce l'interpretazione finale.

**IA:**

- supporta la ricognizione teorica locale;
- supporta la traduzione operativa in codice;
- verifica criticità specifiche quando attivata in Regime C;
- non modifica la specifica del caso;
- non sostituisce l'interpretazione autonoma dello studente.