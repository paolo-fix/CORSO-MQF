# Lezione 16 — Scheda Costruzione Caso TakeHome

Documento interno di progettazione docente.

## 1. Identificazione del caso

- **Lezione:** 16 — Applicazione in Python: programmazione stocastica
- **Tipo di caso:** Caso TakeHome
- **Titolo:** UK LDI 2022 — Buffer di liquidità, margin call e valore dell'informazione
- **Destinatari:** studenti del secondo anno del Corso di Laurea Magistrale in Finanza e Risk Management
- **Uso previsto:** lavoro autonomo successivo al Caso Aula SVB–ALM, finalizzato a trasferire il medesimo framework di programmazione stocastica lineare a due stadi a un diverso problema finanziario, nel quale la capacità limitata di ricorso rende la fattibilità una componente sostanziale della decisione.

Il Caso TakeHome utilizza esclusivamente un **framework two-stage**.

La struttura informativa è:

\[
x
\longrightarrow
s
\longrightarrow
y_s.
\]

La decisione iniziale è unica e comune agli scenari. Dopo l'osservazione dello scenario completo vengono assunte le decisioni di ricorso scenario-specifiche.

Il caso non introduce:

- rivelazione progressiva dell'informazione;
- decisioni intermedie;
- alberi decisionali multistadio;
- vincoli di non anticipatività tra nodi intermedi.

La non anticipatività della decisione iniziale è incorporata strutturalmente mediante l'unicità di \(x\).

---

## 2. Contesto e motivazione

Le strategie Liability Driven Investment sono utilizzate da fondi pensione defined benefit per gestire la sensibilità delle attività rispetto alle passività future e agli impegni previdenziali.

Nel settembre 2022 il rapido aumento dei rendimenti dei gilt britannici produsse forti perdite di valore sulle posizioni utilizzate nelle strategie LDI e generò richieste di collateral e margin call. In presenza di buffer liquidi insufficienti, diversi investitori istituzionali furono costretti a mobilitare liquidità aggiuntiva e a ridurre rapidamente le esposizioni in condizioni di mercato sfavorevoli.

Il caso utilizza questo episodio come riferimento economico-finanziario, ma adotta una rappresentazione quantitativa deliberatamente stilizzata. Non costituisce la ricostruzione di uno specifico fondo pensione, di uno specifico LDI fund o di un portafoglio storicamente osservato.

La motivazione didattica è mostrare che una decisione iniziale caratterizzata da maggiore esposizione e minore buffer può risultare più redditizia nello scenario normale ma può compromettere la capacità di soddisfare le richieste di liquidità negli scenari estremi.

Rispetto al Caso Aula, il TakeHome introduce una differenza metodologicamente rilevante:

- nel Caso Aula il funding illimitato garantisce ricorso relativamente completo;
- nel Caso TakeHome le capacità di ricorso sono limitate e alcune decisioni di primo stadio possono risultare non ammissibili in determinati scenari.

La fattibilità del ricorso diventa quindi parte centrale dell'analisi.

---

## 3. Domanda quantitativa e funzione didattica

**Domanda quantitativa:**  
quale combinazione iniziale tra buffer di liquidità ed esposizione LDI massimizza il risultato economico atteso quando l'intensità delle margin call, la capacità di monetizzare l'esposizione e il costo delle decisioni di ricorso dipendono dallo scenario futuro?

Come si comporta negli scenari originari la decisione costruita sui valori medi?

Quando tale decisione non è ammissibile in tutti gli scenari, quali conseguenze ne derivano per la definizione di \(z^{EV}\) e del VSS?

Quanto varrebbe conoscere anticipatamente lo scenario che si realizzerà?

**Obiettivo didattico:**  
portare lo studente a costruire, risolvere e validare autonomamente un programma stocastico lineare a due stadi nel quale la fattibilità del ricorso non è garantita per tutte le decisioni di primo stadio.

**Collegamento con le lezioni teoriche precedenti:**

- Lezione 14: decisione iniziale, scenari, ricorso, forma estesa e non anticipatività;
- Lezione 15: fattibilità del ricorso, funzione di ricorso, SP, EV, WS, VSS ed EVPI;
- Capitolo 15: approfondisce inoltre il multistadio, che non viene utilizzato nel presente caso;
- Lezione 16: trasferimento computazionale del framework two-stage.

**Concetti teorici da rendere osservabili:**

1. decisione di primo stadio comune agli scenari;
2. ricorso scenario-specifico;
3. fattibilità del ricorso dipendente da \(x\);
4. differenza tra ricorso relativamente completo e ricorso non garantito;
5. Expected Value problem;
6. rivalutazione di \(x^{EV}\);
7. distinzione tra valore del problema deterministico medio e \(z^{EV}\);
8. condizioni necessarie perché \(z^{EV}\) e VSS siano definiti nella forma standard;
9. benchmark wait-and-see;
10. EVPI.

**Funzione della procedura computazionale:**  
Python e il solver consentono di trattare congiuntamente decisione iniziale e ricorsi scenario-specifici, verificare la fattibilità nei singoli scenari e distinguere in modo operativo una soluzione del problema medio da una decisione effettivamente ammissibile nel problema stocastico originario.

**Ruolo dell'informazione, degli scenari e dei vincoli:**  
la decisione iniziale precede la rivelazione dello scenario. Lo scenario determina la margin call, la capacità di ottenere liquidità dal deleveraging e il costo del ricorso. Le capacità limitate di ricorso possono rendere inammissibili alcune decisioni iniziali.

---

## 4. Specifica teorico-matematica

### Grandezze e variabili

Le risorse iniziali sono:

\[
A_0=100.
\]

La decisione di primo stadio è:

\[
x=
\begin{pmatrix}
x_1\\
x_2
\end{pmatrix},
\]

dove:

- \(x_1\): buffer di liquidità immediatamente disponibile;
- \(x_2\): esposizione LDI.

Il vincolo iniziale è:

\[
x_1+x_2=100.
\]

Vincoli di non negatività:

\[
x_1\geq0,
\qquad
x_2\geq0.
\]

Per preservare una funzione minima di copertura delle passività:

\[
x_2\geq50.
\]

Il contributo economico di primo stadio è:

\[
c'x
=
0.010x_1+0.050x_2.
\]

### Eventi, informazione, stati o scenari

L'insieme degli scenari è:

\[
\mathcal S=\{N,S,E\},
\]

con:

- \(N\): normalizzazione;
- \(S\): stress;
- \(E\): stress estremo.

Le probabilità sono:

| Scenario | Descrizione | \(p_s\) |
|---|---|---:|
| \(N\) | Normalizzazione | 0.50 |
| \(S\) | Stress | 0.30 |
| \(E\) | Stress estremo | 0.20 |

Deve valere:

\[
\sum_{s\in\mathcal S}p_s=1.
\]

La struttura informativa è:

\[
x
\longrightarrow
s
\longrightarrow
y_s,
\]

con:

\[
y_s=
\begin{pmatrix}
e_s\\
f_s\\
g_s
\end{pmatrix}.
\]

### Margin call

La margin call nello scenario \(s\) è proporzionale all'esposizione LDI:

\[
m_s=\alpha_sx_2.
\]

I coefficienti sono:

| Scenario | \(\alpha_s\) |
|---|---:|
| \(N\) | 0.10 |
| \(S\) | 0.25 |
| \(E\) | 0.40 |

### Decisioni di ricorso

Dopo l'osservazione dello scenario il decisore può utilizzare:

\[
e_s\geq0,
\]

liquidità aggiuntiva mobilitata esternamente;

\[
f_s\geq0,
\]

esposizione LDI liquidata o deleverata;

\[
g_s\geq0,
\]

liquidità residua.

Una unità di esposizione liquidata produce:

\[
\beta_s f_s
\]

unità di liquidità.

I coefficienti sono:

| Scenario | \(\beta_s\) |
|---|---:|
| \(N\) | 1.00 |
| \(S\) | 0.90 |
| \(E\) | 0.75 |

Il bilancio di liquidità è:

\[
x_1+e_s+\beta_sf_s
=
\alpha_sx_2+g_s.
\]

### Limiti operativi

La liquidità aggiuntiva è limitata da:

\[
0\leq e_s\leq4.
\]

Il deleveraging è limitato da:

\[
0\leq f_s\leq25.
\]

Inoltre:

\[
f_s\leq x_2.
\]

### Costi di ricorso

Il costo unitario della liquidità aggiuntiva è:

| Scenario | \(\kappa_s\) |
|---|---:|
| \(N\) | 0.020 |
| \(S\) | 0.060 |
| \(E\) | 0.120 |

Il costo economico unitario del deleveraging è indicato con:

\[
\delta_s.
\]

Si adotta \(\delta_s\), anziché \(\lambda_s\), per evitare sovrapposizioni con la notazione delle variabili duali utilizzata nel corso.

I valori sono:

| Scenario | \(\delta_s\) |
|---|---:|
| \(N\) | 0.005 |
| \(S\) | 0.030 |
| \(E\) | 0.080 |

Il costo di ricorso è:

\[
C_s
=
\kappa_se_s+\delta_sf_s.
\]

La funzione di ricorso è:

\[
Q_s(x)
=
\max_{e_s,f_s,g_s}
\left\{
-\kappa_se_s-\delta_sf_s
\right\},
\]

soggetta al bilancio di liquidità e ai limiti di ricorso dello scenario.

### Programma stocastico

Il problema è:

\[
z^{SP}
=
\max
\left\{
0.010x_1+0.050x_2
+
\sum_{s\in\mathcal S}p_sQ_s(x)
\right\}.
\]

La decisione ottima è:

\[
x^{SP}.
\]

### Expected Value problem

I parametri medi sono:

\[
\bar\alpha
=
\sum_s p_s\alpha_s,
\]

\[
\bar\beta
=
\sum_s p_s\beta_s,
\]

\[
\bar\kappa
=
\sum_s p_s\kappa_s,
\]

\[
\bar\delta
=
\sum_s p_s\delta_s.
\]

La soluzione del problema deterministico medio è:

\[
x^{EV}.
\]

La decisione \(x^{EV}\) deve poi essere fissata e rivalutata negli scenari originari.

Se \(x^{EV}\) è ammissibile in tutti gli scenari:

\[
z^{EV}
=
c'x^{EV}
+
\sum_s p_sQ_s(x^{EV}),
\]

e:

\[
VSS
=
z^{SP}-z^{EV}.
\]

Se invece \(x^{EV}\) non è ammissibile in almeno uno scenario originario, \(z^{EV}\) e VSS non sono definiti nella forma standard.

### Wait-and-see

Per ciascuno scenario:

\[
z_s^{WS}
=
\max
\left\{
c'x_s+Q_s(x_s)
\right\}.
\]

Il valore atteso wait-and-see è:

\[
z^{WS}
=
\sum_s p_sz_s^{WS}.
\]

L'Expected Value of Perfect Information è:

\[
EVPI
=
z^{WS}-z^{SP}.
\]

### Quantità teoriche da stimare o calcolare

1. \(x^{SP}\);
2. \(z^{SP}\);
3. \(e_s^{SP},f_s^{SP},g_s^{SP}\);
4. \(\bar\alpha,\bar\beta,\bar\kappa,\bar\delta\);
5. \(x^{EV}\);
6. valore ottimo del problema deterministico medio;
7. ammissibilità di \(x^{EV}\) in ciascuno scenario originario;
8. \(z^{EV}\), se definito;
9. VSS, se definito;
10. \(x_s^{WS}\);
11. \(z_s^{WS}\);
12. \(z^{WS}\);
13. EVPI.

### Proprietà teoriche da verificare

Sempre:

\[
z^{SP}\leq z^{WS},
\]

\[
EVPI\geq0.
\]

Se \(x^{EV}\) è ammissibile in tutti gli scenari:

\[
z^{EV}\leq z^{SP}\leq z^{WS},
\]

\[
VSS\geq0.
\]

### Soglie, target o vincoli rilevanti

\[
x_2\geq50,
\]

\[
e_s\leq4,
\]

\[
f_s\leq25,
\]

\[
f_s\leq x_2.
\]

Questi limiti rendono la fattibilità del ricorso dipendente dalla decisione di primo stadio.

### Quantità finali di interesse

Le quantità centrali sono:

\[
x^{SP},
\quad
x^{EV},
\quad
z^{SP},
\quad
z^{WS},
\quad
EVPI,
\]

oltre allo stato di ammissibilità di \(x^{EV}\) e, quando definiti:

\[
z^{EV},
\quad
VSS.
\]

### Limiti del modello

Il caso:

- è esclusivamente two-stage;
- non rappresenta dinamiche intraday;
- non modella collateral waterfall;
- non rappresenta haircut multipli;
- non modella feedback endogeni sui prezzi dei gilt;
- non rappresenta derivati specifici;
- non modella duration delle passività;
- non rappresenta requisiti regolamentari dettagliati;
- assume costi lineari;
- assume scenari discreti e probabilità note;
- utilizza limiti operativi didattici;
- non costituisce una calibrazione empirica di uno specifico fondo LDI.

---

## 5. Output richiesti

### Stime o risultati numerici

Calcolare:

1. \(x^{SP}\);
2. \(z^{SP}\);
3. \(e_s^{SP},f_s^{SP},g_s^{SP}\);
4. parametri medi;
5. \(x^{EV}\);
6. valore ottimo del problema deterministico medio;
7. stato di ammissibilità di \(x^{EV}\) nei tre scenari;
8. \(z^{EV}\), se definito;
9. VSS, se definito;
10. \(x_s^{WS}\) e \(z_s^{WS}\);
11. \(z^{WS}\);
12. EVPI.

### Tabelle

**Tabella 1 — Parametri del problema**

Deve rappresentare probabilità, \(\alpha_s\), \(\beta_s\), \(\kappa_s\), \(\delta_s\), rendimenti e limiti operativi.

Funzione: verificare la specifica numerica utilizzata dal solver.

**Tabella 2 — Soluzione stocastica**

Deve riportare:

- \(x^{SP}\);
- margin call per scenario;
- \(e_s^{SP}\);
- \(f_s^{SP}\);
- \(g_s^{SP}\);
- costo di ricorso.

Funzione: rendere osservabile il trade-off buffer–esposizione e l'adattamento scenario-specifico.

**Tabella 3 — Expected Value e rivalutazione**

Deve riportare:

- parametri medi;
- \(x^{EV}\);
- valore ottimo del problema medio;
- ammissibilità di \(x^{EV}\) per scenario;
- ricorsi ottimi negli scenari ammissibili;
- eventuale non definibilità di \(z^{EV}\).

Funzione: rendere esplicita la differenza tra soluzione del problema medio e decisione ammissibile nel problema stocastico.

**Tabella 4 — Wait-and-see**

Per ogni scenario:

- \(x_s^{WS}\);
- \(z_s^{WS}\).

Funzione: mostrare come cambia la decisione se lo scenario è noto prima della scelta iniziale.

**Tabella 5 — Confronto dei benchmark**

Deve contenere sempre:

\[
z^{SP},
\qquad
z^{WS},
\qquad
EVPI.
\]

Deve contenere anche:

\[
z^{EV},
\qquad
VSS,
\]

solo quando definiti.

Quando non sono definiti, la tabella deve riportare esplicitamente la relativa motivazione.

### Grafici

**Figura 1 — Confronto tra \(x^{SP}\) e \(x^{EV}\)**

Rappresentare buffer ed esposizione LDI.

Domanda interpretativa: quanto buffer sacrifica la soluzione costruita sui valori medi?

**Figura 2 — Decisioni di ricorso per scenario**

Rappresentare almeno:

\[
e_s
\quad\text{e}\quad
f_s
\]

sotto \(x^{SP}\).

Domanda interpretativa: come cambia il mix di ricorso al crescere della severità dello scenario?

**Figura 3 — Confronto dei benchmark**

Rappresentare:

\[
z^{SP}
\quad\text{e}\quad
z^{WS},
\]

e, soltanto se definito:

\[
z^{EV}.
\]

Se \(z^{EV}\) non è definito, il grafico deve rendere esplicita tale circostanza senza attribuirgli un valore artificiale.

### Controlli

1. \(\sum_s p_s=1\);
2. \(x_1+x_2=100\);
3. \(x_1\geq0\);
4. \(x_2\geq50\);
5. \(0\leq e_s\leq4\);
6. \(0\leq f_s\leq25\);
7. \(f_s\leq x_2\);
8. \(g_s\geq0\);
9. bilancio di liquidità scenario per scenario;
10. successo del solver;
11. ammissibilità della soluzione SP;
12. fissazione di \(x^{EV}\) durante la rivalutazione;
13. verifica dell'ammissibilità di \(x^{EV}\) separatamente in ciascuno scenario;
14. costruzione separata dei problemi WS;
15. verifica sempre di
   \[
   z^{SP}\leq z^{WS};
   \]
16. verifica sempre di
   \[
   EVPI\geq0;
   \]
17. se \(z^{EV}\) è definito, verifica di
   \[
   z^{EV}\leq z^{SP}\leq z^{WS};
   \]
18. se \(z^{EV}\) è definito, verifica di
   \[
   VSS\geq0.
   \]

---

## 6. Flusso logico-teorico risolutivo atteso

| Passo | Finalità risolutiva | Formula, definizione, proprietà o teorema | Applicazione nel caso | Output o controllo collegato |
|---:|---|---|---|---|
| 1 | Identificare struttura informativa, scenari e decisioni | Programma stocastico two-stage | \(x\) comune; \(e_s,f_s,g_s\) scenario-specifici | corretta classificazione di variabili e scenari |
| 2 | Costruire il meccanismo di ricorso | Funzione di ricorso \(Q_s(x)\) e vincoli di secondo stadio | margin call, liquidità esterna, deleveraging e giacenza | forma estesa; bilanci; bounds |
| 3 | Analizzare la fattibilità del ricorso | Dominio di \(Q_s(x)\); ammissibilità scenario-specifica | capacità limitate \(e_s\leq4\), \(f_s\leq25\) | verifica delle decisioni di primo stadio ammissibili |
| 4 | Determinare la soluzione stocastica | \(z^{SP}=\max\{c'x+\sum_sp_sQ_s(x)\}\) | scelta congiunta di buffer, esposizione e ricorsi | \(x^{SP}\), ricorsi, \(z^{SP}\) |
| 5 | Costruire e rivalutare Expected Value | problema deterministico medio; fissazione di \(x^{EV}\) | soluzione sui parametri medi e verifica scenario per scenario | \(x^{EV}\), ammissibilità; \(z^{EV}\) e VSS solo se definiti |
| 6 | Costruire wait-and-see | ottimizzazione separata per scenario | decisione iniziale specifica conoscendo \(s\) | \(x_s^{WS},z_s^{WS},z^{WS},EVPI\) |
| 7 | Interpretare i benchmark effettivamente definiti | \(z^{SP}\leq z^{WS}\); eventuale ordinamento completo | confronto tra buffer, ricorso, fattibilità e informazione | tabelle, grafici e base quantitativa dell'interpretazione finale |

---

## 7. Scomposizione attesa in tappe

| Tappa | Titolo | Obiettivo | Input | Regime IA prevalente | Prompt virtuoso di riferimento | Oggetti teorici coinvolti | Operazione | Output | Controllo | Uso successivo |
|---:|---|---|---|:---:|---|---|---|---|---|---|
| 1 | Struttura del modello e parametri | Tradurre la Scheda Caso in oggetti matematici e computazionali | Scheda Caso, Flusso validato | A/B | chiarimento teorico + definizione parametri | \(x\), scenari, ricorso, probabilità | organizzare dati e variabili | Tabella 1 e schema modello | probabilità e parametri | forma estesa |
| 2 | Forma estesa e soluzione SP | Costruire e risolvere il problema stocastico | parametri validati | B | traduzione operativa in codice | funzione obiettivo, bilanci, bounds | costruire matrici e risolvere con HiGHS | \(x^{SP}\), ricorsi, \(z^{SP}\) | status e vincoli | analisi SP |
| 3 | Fattibilità e analisi del ricorso | Rendere osservabili capacità limitate e bilanci | soluzione SP e vincoli | B | output e controlli | dominio del ricorso, fattibilità | estrarre ricorsi e verificare bounds | Tabella 2 | bilanci, bounds, ammissibilità | benchmark EV |
| 4 | Expected Value e rivalutazione | Costruire \(x^{EV}\) e verificarne l'ammissibilità | parametri medi e scenari originari | B | traduzione operativa in codice | EV, \(x^{EV}\), dominio \(Q_s\) | risolvere EV, fissare \(x^{EV}\), rivalutare per scenario | Tabella 3 | nessuna riottimizzazione di \(x\); ammissibilità | eventuale VSS |
| 5 | Wait-and-see ed EVPI | Costruire il benchmark di informazione perfetta | scenari originari | B | traduzione operativa in codice | WS, EVPI | risolvere un problema per scenario | Tabella 4, \(z^{WS}\), EVPI | ponderazione e \(z^{SP}\leq z^{WS}\) | sintesi benchmark |
| 6 | Sintesi quantitativa e grafica | Integrare output e benchmark definiti | output precedenti | B | output, grafici e controlli | ordinamenti, definibilità di \(z^{EV}\), EVPI | produrre Tabella 5 e Figure 1–3 | pacchetto quantitativo finale | controlli condizionati | interpretazione autonoma |

Il **Regime C non costituisce una tappa ordinaria**. Può essere attivato soltanto se lo studente individua una criticità specifica da verificare.

---

## 8. Sequenza docente dei prompt e mappa prompt-notebook

**Sequenza docente dei prompt virtuosi:**

1. Prompt zero;
2. Prompt 1;
3. Prompt 2;
4. Prompt 3;
5. prompt delle Tappe 1–6;
6. eventuali Prompt C soltanto in presenza di criticità specifiche.

Il numero complessivo dei prompt non viene stabilito a priori.

| Prompt | Regime | Tappa o fase | Funzione del prompt | Celle o output prodotti | Decisione o controllo richiesto |
|---|:---:|---|---|---|---|
| Prompt zero | — | inizializzazione | inizializzare contesto e regole | nessuna cella | acquisizione del protocollo |
| Prompt 1 | — | inquadramento | acquisire la Scheda Caso | Markdown iniziale | fedeltà alla specifica |
| Prompt 2 | A | preliminare | costruire il Flusso logico-teorico | Markdown | completezza e ordine |
| Prompt 3 | A/B | preliminare | costruire le tappe input-output | Markdown | copertura di output e controlli |
| Prompt Tappa 1 | A/B | 1 | organizzare struttura e dati | Markdown e, se pertinente, codice | coerenza del modello |
| Prompt Tappa 2 | B | 2 | costruire e risolvere SP | Markdown + codice | correttezza solver |
| Prompt Tappa 3 | B | 3 | analizzare ricorso e fattibilità | Markdown + codice | bounds e bilanci |
| Prompt Tappa 4 | B | 4 | costruire EV e rivalutare \(x^{EV}\) | Markdown + codice | ammissibilità scenario-specifica |
| Prompt Tappa 5 | B | 5 | costruire WS ed EVPI | Markdown + codice | informazione perfetta |
| Prompt Tappa 6 | B | 6 | costruire sintesi, grafici e controlli | Markdown + codice | benchmark effettivamente definiti |
| Eventuale Prompt C | C | fase interessata | verificare criticità specifica | eventuali celle sostitutive | criticità respinta / accolta |

L'interpretazione finale deve essere prodotta autonomamente dallo studente.

---

## 9. Struttura attesa del notebook

Ordine logico previsto:

1. cella Markdown iniziale;
2. Flusso logico-teorico;
3. scomposizione in tappe;
4. import delle librerie;
5. definizione degli scenari;
6. definizione delle probabilità;
7. controllo delle probabilità;
8. definizione dei parametri di primo stadio;
9. definizione dei parametri di ricorso;
10. Tabella 1 — parametri;
11. costruzione del vettore delle variabili;
12. costruzione della funzione obiettivo SP;
13. costruzione dei vincoli di uguaglianza;
14. costruzione dei vincoli di disuguaglianza;
15. definizione dei bounds;
16. soluzione SP con `scipy.optimize.linprog(method="highs")`;
17. estrazione di \(x^{SP}\);
18. estrazione dei ricorsi;
19. controllo dei bilanci;
20. controllo dei bounds;
21. Tabella 2 — soluzione SP;
22. calcolo dei parametri medi;
23. costruzione del problema EV;
24. soluzione del problema EV;
25. estrazione di \(x^{EV}\);
26. fissazione di \(x^{EV}\);
27. rivalutazione scenario per scenario;
28. verifica dell'ammissibilità di \(x^{EV}\);
29. calcolo di \(z^{EV}\) soltanto se definito;
30. calcolo del VSS soltanto se definito;
31. Tabella 3 — EV e rivalutazione;
32. costruzione dei problemi WS;
33. soluzione dei tre problemi WS;
34. calcolo di \(z^{WS}\);
35. calcolo dell'EVPI;
36. Tabella 4 — wait-and-see;
37. Tabella 5 — benchmark;
38. Figura 1 — \(x^{SP}\) vs \(x^{EV}\);
39. Figura 2 — ricorso per scenario;
40. Figura 3 — benchmark;
41. controlli conclusivi;
42. interpretazione finanziaria finale autonoma;
43. limiti del modello;
44. sintesi finale.

Librerie previste:

- NumPy;
- pandas;
- `scipy.optimize.linprog`;
- matplotlib.

Non sono previste esportazioni automatiche in file esterni.

---

## 10. Criteri di validazione del notebook

Il notebook è considerato valido se:

1. implementa la Scheda Caso senza modificarla;
2. utilizza esclusivamente i parametri assegnati;
3. mantiene unica la decisione iniziale;
4. costruisce correttamente il ricorso scenario-specifico;
5. implementa correttamente i limiti \(e_s\leq4\), \(f_s\leq25\), \(f_s\leq x_2\);
6. costruisce correttamente la forma estesa;
7. mantiene coerente l'ordinamento delle variabili nel solver;
8. produce una soluzione SP ottima e ammissibile;
9. verifica esplicitamente bilanci e bounds;
10. costruisce correttamente il problema EV;
11. mantiene \(x^{EV}\) fissa nella rivalutazione;
12. verifica separatamente la fattibilità del ricorso per ogni scenario;
13. non assegna un valore artificiale a \(z^{EV}\) quando \(x^{EV}\) è inammissibile;
14. calcola il VSS soltanto quando \(z^{EV}\) è definito;
15. costruisce correttamente i problemi WS;
16. calcola correttamente \(z^{WS}\) ed EVPI;
17. verifica sempre:
   \[
   z^{SP}\leq z^{WS};
   \]
18. verifica sempre:
   \[
   EVPI\geq0;
   \]
19. verifica l'ordinamento completo e il VSS soltanto quando applicabili;
20. produce tutte le cinque tabelle e i tre grafici;
21. rispetta la scomposizione in tappe;
22. conclude con interpretazione coerente con output e limiti.

**Criteri specifici del caso:**

- la non fattibilità di \(x^{EV}\) nello scenario estremo deve essere riconosciuta come proprietà del modello, non aggirata modificando i parametri;
- non devono essere introdotte penalità artificiali per trasformare un problema inammissibile in un valore finito;
- la non definibilità standard di \(z^{EV}\) e VSS deve risultare esplicitamente negli output.

---

## 11. Calibrazione docente

### Ordine di grandezza atteso dei risultati

La soluzione stocastica attesa è:

\[
x^{SP}
=
\begin{pmatrix}
25\\
75
\end{pmatrix}.
\]

Il valore ottimo è:

\[
z^{SP}=3.944000.
\]

### Expected Value

La soluzione del problema deterministico medio è:

\[
x^{EV}
=
\begin{pmatrix}
0\\
100
\end{pmatrix}.
\]

Il valore ottimo del problema deterministico medio è:

\[
4.387228.
\]

Fissando:

\[
x=x^{EV},
\]

il problema di ricorso risulta:

- ammissibile nello scenario \(N\);
- ammissibile nello scenario \(S\);
- non ammissibile nello scenario \(E\).

Pertanto \(x^{EV}\) non appartiene all'insieme delle decisioni di primo stadio ammissibili per tutti gli scenari originari.

Di conseguenza:

\[
z^{EV}
\]

non è definito nella forma standard e:

\[
VSS
=
z^{SP}-z^{EV}
\]

non è calcolabile nella forma standard.

### Wait-and-see

Il valore atteso wait-and-see è:

\[
z^{WS}=4.506429.
\]

Pertanto:

\[
EVPI
=
z^{WS}-z^{SP}
=
0.562429.
\]

Deve risultare:

\[
3.944000
<
4.506429.
\]

### Errori o ambiguità prevedibili

1. interpretare la non fattibilità di \(x^{EV}\) come errore del solver;
2. modificare arbitrariamente i limiti di ricorso per rendere \(x^{EV}\) ammissibile;
3. assegnare \(z^{EV}=-\infty\) e utilizzarlo numericamente nel VSS senza discuterne la convenzione;
4. utilizzare il valore ottimo del problema medio al posto di \(z^{EV}\);
5. calcolare comunque un VSS numerico;
6. riottimizzare \(x^{EV}\) dopo l'osservazione dello scenario;
7. confondere il problema EV con il wait-and-see;
8. utilizzare \(\beta_s\) come costo anziché come coefficiente di monetizzazione;
9. confondere \(\kappa_s\) e \(\delta_s\);
10. dimenticare il vincolo \(f_s\leq x_2\);
11. consentire a \(x\) di dipendere dallo scenario nel problema SP;
12. introdurre impropriamente una struttura multistadio.

### Controlli minimi di validazione

Devono risultare esplicitamente verificati:

\[
\sum_s p_s=1,
\]

\[
x_1+x_2=100,
\]

\[
x_2\geq50,
\]

tutti i bounds del ricorso,

i bilanci scenario-specifici,

la non ammissibilità di \(x^{EV}\) nello scenario \(E\),

e:

\[
z^{SP}\leq z^{WS},
\]

\[
EVPI\geq0.
\]

### Limiti interpretativi

La non definibilità del VSS nella calibrazione assegnata non implica che il concetto di VSS sia privo di significato. Significa che la specifica decisione \(x^{EV}\) ottenuta dal problema medio non è ammissibile nel problema stocastico originario e non può quindi essere rivalutata secondo la definizione standard adottata nel corso.

---

## 12. Uso dell'IA e tracciato

- **Uso documentato dell'IA previsto:** sì.
- **Prompt obbligatori:** Prompt zero, Prompt 1, Prompt 2, Prompt 3 e prompt di tappa necessari.
- **Numero dei prompt:** determinato dalla scomposizione operativa validata; eventuali Prompt C possono aggiungersi soltanto quando emerge una criticità specifica individuata dallo studente.
- **Regimi ordinari:** A e B.
- **Regime C:** eventuale e non obbligatorio.

**Usi ammessi dell'IA:**

- chiarire la struttura two-stage;
- supportare la formulazione della forma solver;
- tradurre una tappa già definita in Python;
- verificare bounds e bilanci;
- supportare la rivalutazione di \(x^{EV}\);
- verificare la corretta gestione dell'inammissibilità;
- costruire tabelle e grafici richiesti;
- verificare criticità specifiche.

**Usi non ammessi:**

- modificare la Scheda Caso;
- modificare scenari o probabilità;
- modificare parametri o limiti di ricorso;
- rendere artificialmente ammissibile \(x^{EV}\);
- sostituire il two-stage con un modello multistadio;
- introdurre scenari ulteriori;
- produrre globalmente l'intero notebook;
- attribuire arbitrariamente un valore a \(z^{EV}\);
- calcolare un VSS numerico quando \(z^{EV}\) non è definito;
- produrre autonomamente l'interpretazione finale;
- utilizzare il Regime C come controllo generico dell'intero lavoro.

**Criteri di validazione delle risposte IA:**

1. coerenza con il regime;
2. rispetto degli input;
3. rispetto della Scheda Caso;
4. assenza di modifiche non autorizzate;
5. correttezza della traduzione computazionale;
6. corretta gestione della fattibilità;
7. corretta distinzione tra problema medio e \(z^{EV}\);
8. pertinenza dei controlli;
9. utilità dell'output per la tappa successiva;
10. in Regime C, corretta classificazione della criticità.

- **Tracciato IA richiesto:** sì.
- **Modalità di consegna:** stampa PDF della chat dedicata.
- **Sequenza osservabile:** Prompt zero → Prompt 1 → Prompt 2 → Prompt 3 → prompt di tappa → eventuali Prompt C.

---

## 13. Valutazione

### Criteri per il notebook

1. correttezza del modello two-stage;
2. correttezza della forma estesa;
3. corretto uso del solver;
4. corretta soluzione SP;
5. corretta analisi della fattibilità;
6. corretta costruzione del problema EV;
7. corretta rivalutazione di \(x^{EV}\);
8. corretta identificazione della non definibilità di \(z^{EV}\);
9. corretta gestione del VSS;
10. corretta costruzione di WS;
11. corretto calcolo di EVPI;
12. qualità dei controlli;
13. qualità delle tabelle;
14. qualità dei grafici;
15. leggibilità del codice;
16. coerenza tra notebook e tracciato IA;
17. interpretazione economico-finanziaria;
18. consapevolezza dei limiti.

### Criteri per il tracciato IA

1. contributo iniziale dello studente nel Prompt 2;
2. proposta operativa nel Prompt 3;
3. qualità dei prompt di tappa;
4. corretto uso dei Regimi A/B;
5. eventuale attivazione appropriata del Regime C;
6. capacità di verificare criticamente le risposte;
7. assenza di delega globale;
8. coerenza tra chat e notebook.

### Peso dei controlli e dell'interpretazione

Particolare importanza deve essere attribuita alla capacità dello studente di spiegare:

- perché \(x^{EV}\) risulta più esposta rispetto a \(x^{SP}\);
- perché il problema medio non incorpora correttamente la fattibilità scenario-specifica;
- perché l'inammissibilità di \(x^{EV}\) impedisce di definire \(z^{EV}\) nella forma standard adottata;
- perché il VSS non deve essere forzato numericamente;
- perché EVPI resta invece perfettamente definito;
- quale funzione economica svolge il buffer iniziale.

---

## 14. Rubrica sintetica

Per il Caso TakeHome con uso documentato dell'IA si adotta la seguente articolazione su 100 punti.

| Area | Peso | Criteri principali |
|---|---:|---|
| Prompt 2 — Flusso logico-teorico risolutivo | 30 | contributo iniziale, ordine logico, collegamento tra teoria, fattibilità, output e controlli |
| Prompt 3 — Scomposizione input-output | 15 | proposta operativa, concatenazione delle tappe, copertura degli output |
| Notebook Jupyter e output computazionali | 20 | correttezza del codice, solver, tabelle, grafici e riproducibilità |
| Prompt di tappa e uso dei Regimi A/B; eventuale Regime C | 15 | qualità dei prompt, rispetto dei vincoli, appropriatezza dell'uso dell'IA |
| Verifiche logiche e controlli numerici | 15 | fattibilità, bilanci, bounds, benchmark e gestione corretta di \(z^{EV}\) |
| Interpretazione finanziaria finale | 5 | autonomia, coerenza con gli output e consapevolezza dei limiti |

**Totale:** 100 punti.

---

## 15. Esito atteso e calibrazione qualitativa del caso

**Esito atteso:**  
la soluzione stocastica deve scegliere un buffer positivo che preservi la fattibilità del ricorso nello scenario estremo, mentre la soluzione costruita sui parametri medi deve risultare più esposta e non ammissibile nello scenario \(E\).

**Ordini di grandezza o relazioni attese:**

\[
x^{SP}
=
(25,75)',
\]

\[
x^{EV}
=
(0,100)'.
\]

Deve risultare:

\[
z^{SP}=3.944000,
\]

\[
z^{WS}=4.506429,
\]

e:

\[
EVPI=0.562429.
\]

Nella calibrazione corrente:

\[
z^{EV}
\]

e VSS non sono definiti nella forma standard.

**Funzione didattica degli output:**

- \(x^{SP}\) rende osservabile il valore del buffer come strumento di fattibilità;
- \(x^{EV}\) mostra il limite della sostituzione della distribuzione con parametri medi;
- la rivalutazione scenario-specifica rende osservabile il dominio della funzione di ricorso;
- WS rende osservabile il valore della conoscenza anticipata dello scenario;
- EVPI rimane definito anche quando VSS non può essere calcolato.

**Possibili segnali di cattiva calibrazione:**

1. \(x^{EV}\) risulta ammissibile nello scenario estremo senza modifica dei parametri;
2. \(x^{SP}\) coincide con \(x^{EV}\);
3. la soluzione SP è inammissibile in qualche scenario;
4. \(z^{WS}<z^{SP}\);
5. EVPI negativo;
6. \(z^{EV}\) viene prodotto come numero finito nonostante l'inammissibilità;
7. il VSS viene calcolato artificialmente;
8. i limiti di ricorso non incidono sulla decisione;
9. il buffer non svolge alcuna funzione economica visibile.

---

## 16. Relazione con l'altro caso della lezione

Il Caso TakeHome UK LDI e il Caso Aula SVB–ALM condividono la stessa struttura metodologica:

\[
x
\longrightarrow
s
\longrightarrow
y_s.
\]

### 1. Concetti teorici comuni

Entrambi consolidano:

- programmazione stocastica two-stage;
- decisione iniziale comune agli scenari;
- ricorso scenario-specifico;
- scenari e probabilità;
- forma estesa;
- SP;
- Expected Value;
- wait-and-see;
- EVPI;
- fattibilità del ricorso.

### 2. Strumenti computazionali comuni

Entrambi utilizzano:

- NumPy;
- pandas;
- `scipy.optimize.linprog(method="highs")`;
- matplotlib;
- costruzione esplicita di obiettivo, vincoli e bounds;
- controlli numerici;
- benchmark SP/EV/WS.

### 3. Output comparabili

In entrambi:

- decisione SP;
- ricorso per scenario;
- decisione EV;
- rivalutazione di EV;
- soluzioni WS;
- tabella dei benchmark;
- grafici sulle decisioni e sul ricorso.

### 4. Controlli comparabili

In entrambi:

- probabilità;
- vincoli di primo stadio;
- bilanci di ricorso;
- status del solver;
- decisione EV mantenuta fissa;
- problemi WS separati;
- ordinamenti dei benchmark effettivamente definiti.

### 5. Elementi metodologici comuni

Entrambi seguono:

Scheda Caso  
→ Flusso logico-teorico  
→ scomposizione in tappe  
→ notebook  
→ controlli conclusivi  
→ interpretazione finale autonoma.

### 6. Elementi distintivi del Caso TakeHome rispetto al Caso Aula

Nel Caso Aula:

- il decisore è una banca;
- \(x\) descrive la composizione dell'attivo;
- lo shock è un deposit run;
- il ricorso è principalmente funding;
- il funding non ha limite quantitativo;
- il ricorso è relativamente completo;
- \(z^{EV}\) e VSS sono definiti.

Nel Caso TakeHome:

- il decisore è un investitore istituzionale con strategia LDI;
- \(x\) descrive buffer ed esposizione;
- lo shock produce margin call;
- il ricorso combina liquidità esterna e deleveraging;
- entrambe le capacità di ricorso sono limitate;
- alcune decisioni di primo stadio possono non essere ammissibili;
- \(x^{EV}\) è inammissibile nello scenario estremo;
- \(z^{EV}\) e VSS non sono definiti nella forma standard nella calibrazione assegnata.

La differenza essenziale tra i due casi non è quindi il numero degli stadi, che resta due in entrambi, ma la **struttura della fattibilità del ricorso**.

### 7. Ripartizione delle responsabilità

**Docente:**

- definisce Scheda Costruzione e Scheda Caso;
- valida modello e calibrazione;
- stabilisce output e controlli;
- assegna il TakeHome.

**Studente:**

- costruisce il Flusso logico-teorico;
- propone la scomposizione in tappe;
- formula i prompt;
- implementa e valida il notebook;
- individua eventuali criticità;
- interpreta autonomamente gli output.

**IA:**

- supporta la ricognizione teorica locale;
- supporta la traduzione in codice;
- può verificare criticità specifiche in Regime C;
- non modifica il modello;
- non modifica i parametri;
- non elimina l'inammissibilità di \(x^{EV}\);
- non sostituisce l'interpretazione finale dello studente.