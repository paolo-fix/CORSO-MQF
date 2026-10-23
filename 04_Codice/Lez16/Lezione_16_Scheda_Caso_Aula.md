# Lezione 16 — Scheda Caso Aula

## 1. Identificazione del caso

- **Lezione:** 16 — Applicazione in Python: programmazione stocastica
- **Tipo di caso:** Caso Aula
- **Titolo:** SVB–ALM 2023 — Asset allocation, liquidità e valore dell'informazione
- **Contesto sintetico:** gestione della composizione dell'attivo e della liquidità bancaria sotto scenari alternativi di deflusso della raccolta
- **Uso previsto:** sviluppo guidato in aula mediante notebook Python

La presente Scheda Caso costituisce la specifica vincolante del lavoro.

Non contiene la soluzione del problema e non deve essere modificata durante lo svolgimento, salvo esplicita indicazione del docente.

Il caso utilizza una rappresentazione stilizzata ispirata alla crisi di Silicon Valley Bank del marzo 2023. Non costituisce una ricostruzione quantitativa del bilancio storico della banca.

---

## 2. Contesto e domanda quantitativa

### Contesto

Una banca deve scegliere al tempo iniziale la composizione del proprio attivo prima di conoscere l'evoluzione futura delle condizioni di liquidità.

La decisione iniziale riguarda quattro classi di attivo caratterizzate da rendimenti e livelli di liquidabilità differenti.

Successivamente si realizza uno tra tre scenari:

- condizioni normali;
- pressione sulla raccolta;
- run severo.

Lo scenario determina:

1. il fabbisogno di liquidità;
2. la quota delle diverse attività trasformabile in liquidità;
3. il costo del funding di emergenza.

Dopo l'osservazione dello scenario, la banca può ricorrere a funding aggiuntivo e può detenere eventuale liquidità residua.

Il caso utilizza un framework di programmazione stocastica lineare a due stadi:

\[
x
\longrightarrow
s
\longrightarrow
(u_s,g_s).
\]

La decisione iniziale \(x\) è unica e comune agli scenari. Le decisioni \(u_s\) e \(g_s\) possono invece dipendere dallo scenario osservato.

### Domanda quantitativa

Determinare la composizione iniziale dell'attivo che massimizza il risultato economico atteso della banca tenendo conto congiuntamente di:

- rendimento delle attività;
- probabilità degli scenari;
- liquidabilità delle attività;
- fabbisogni di liquidità;
- costo del funding di emergenza.

Confrontare inoltre la soluzione stocastica con:

1. la decisione ottenuta sostituendo gli scenari con parametri medi;
2. il benchmark nel quale lo scenario è conosciuto prima della decisione iniziale.

Utilizzare tali confronti per determinare il valore della soluzione stocastica e il valore dell'informazione perfetta.

---

## 3. Modello e struttura del problema

### Grandezze economico-finanziarie

Le risorse iniziali sono:

\[
A_0=100.
\]

La decisione di primo stadio è:

\[
x=(x_1,x_2,x_3,x_4)',
\]

dove:

- \(x_1\): cassa e riserve;
- \(x_2\): titoli a breve scadenza;
- \(x_3\): titoli a lunga scadenza;
- \(x_4\): prestiti e impieghi meno liquidi.

I rendimenti unitari delle quattro classi di attivo sono indicati con:

\[
c=(c_1,c_2,c_3,c_4)'.
\]

### Variabili decisionali

La decisione iniziale soddisfa:

\[
x_j\geq0,
\qquad j=1,\ldots,4.
\]

Per ogni scenario \(s\), le decisioni di secondo stadio sono:

\[
u_s\geq0,
\]

funding di emergenza, e

\[
g_s\geq0,
\]

liquidità residua.

### Scenari

L'insieme degli scenari è:

\[
\mathcal S=\{N,P,R\},
\]

dove:

- \(N\): condizioni normali;
- \(P\): pressione sulla raccolta;
- \(R\): run severo.

A ciascuno scenario è associata una probabilità \(p_s\), con:

\[
p_s\geq0,
\qquad
\sum_{s\in\mathcal S}p_s=1.
\]

### Relazioni strutturali e formule principali

Il vincolo di bilancio iniziale è:

\[
x_1+x_2+x_3+x_4=100.
\]

Sono inoltre imposti:

\[
x_3\leq70,
\qquad
x_4\leq70.
\]

Il coefficiente \(\alpha_{js}\) indica la quota dell'investimento \(x_j\) trasformabile in liquidità nello scenario \(s\).

Il bilancio di liquidità nello scenario \(s\) è:

\[
\sum_{j=1}^{4}\alpha_{js}x_j+u_s
=
d_s+g_s,
\]

dove \(d_s\) è il fabbisogno di liquidità dello scenario.

La funzione obiettivo del problema stocastico è:

\[
\max
\left\{
\sum_{j=1}^{4}c_jx_j
-
\sum_{s\in\mathcal S}p_s\kappa_su_s
\right\},
\]

dove \(\kappa_s\) rappresenta il costo unitario del funding nello scenario \(s\).

Il valore ottimo del problema stocastico è indicato con:

\[
z^{SP}.
\]

### Expected Value

Definire i parametri medi:

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

La soluzione del problema costruito sui parametri medi è indicata con:

\[
x^{EV}.
\]

La decisione \(x^{EV}\) deve successivamente essere mantenuta fissa e rivalutata negli scenari originari.

Il valore ottenuto è:

\[
z^{EV}.
\]

Per il problema formulato in massimizzazione:

\[
VSS
=
z^{SP}-z^{EV}.
\]

### Wait-and-see

Per ciascuno scenario viene inoltre risolto un problema nel quale la decisione iniziale può essere assunta conoscendo anticipatamente lo scenario.

Il valore atteso dei problemi scenario-specifici è:

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

---

## 4. Parametri assegnati

I parametri sono deliberatamente stilizzati e hanno finalità didattica.

### Parametri economico-finanziari

| Attivo | Interpretazione | Rendimento unitario |
|---|---|---:|
| \(x_1\) | Cassa e riserve | 0.010 |
| \(x_2\) | Titoli a breve scadenza | 0.025 |
| \(x_3\) | Titoli a lunga scadenza | 0.040 |
| \(x_4\) | Prestiti e impieghi meno liquidi | 0.050 |

### Probabilità e fabbisogni

| Scenario | Descrizione | \(p_s\) | \(d_s\) |
|---|---|---:|---:|
| \(N\) | Condizioni normali | 0.60 | 15 |
| \(P\) | Pressione sulla raccolta | 0.25 | 35 |
| \(R\) | Run severo | 0.15 | 65 |

### Coefficienti di liquidabilità

| Attivo | \(N\) | \(P\) | \(R\) |
|---|---:|---:|---:|
| Cassa e riserve \(x_1\) | 1.00 | 1.00 | 1.00 |
| Titoli brevi \(x_2\) | 0.98 | 0.95 | 0.90 |
| Titoli lunghi \(x_3\) | 0.85 | 0.70 | 0.50 |
| Prestiti/impieghi \(x_4\) | 0.60 | 0.40 | 0.20 |

### Costi del funding

| Scenario | \(\kappa_s\) |
|---|---:|
| \(N\) | 0.01 |
| \(P\) | 0.06 |
| \(R\) | 0.25 |

### Vincoli assegnati

\[
x_1+x_2+x_3+x_4=100,
\]

\[
x_j\geq0,
\qquad j=1,\ldots,4,
\]

\[
x_3\leq70,
\qquad
x_4\leq70.
\]

Il funding di emergenza non presenta un limite quantitativo superiore.

---

## 5. Quantità da stimare o calcolare

Determinare:

1. la soluzione stocastica
   \[
   x^{SP};
   \]

2. le decisioni di ricorso
   \[
   u_s^{SP},
   \qquad
   g_s^{SP};
   \]

3. il valore ottimo
   \[
   z^{SP};
   \]

4. i parametri medi
   \[
   \bar d,
   \qquad
   \bar\alpha_j,
   \qquad
   \bar\kappa;
   \]

5. la soluzione Expected Value
   \[
   x^{EV};
   \]

6. il valore ottimo del problema deterministico medio;

7. il valore della decisione \(x^{EV}\) rivalutata negli scenari originari
   \[
   z^{EV};
   \]

8. il Value of the Stochastic Solution
   \[
   VSS=z^{SP}-z^{EV};
   \]

9. le soluzioni wait-and-see
   \[
   x_s^{WS};
   \]

10. i valori scenario-specifici
   \[
   z_s^{WS};
   \]

11. il valore atteso wait-and-see
   \[
   z^{WS};
   \]

12. l'Expected Value of Perfect Information
   \[
   EVPI=z^{WS}-z^{SP}.
   \]

---

## 6. Output richiesti

### Risultati numerici

Il notebook deve riportare in modo leggibile:

- soluzione SP;
- ricorsi scenario-specifici;
- valore \(z^{SP}\);
- soluzione EV;
- valore del problema medio;
- rivalutazione di \(x^{EV}\);
- \(z^{EV}\);
- VSS;
- soluzioni WS;
- \(z^{WS}\);
- EVPI.

### Tabelle

**Tabella 1 — Parametri del problema**

Deve contenere i parametri economico-finanziari, probabilistici e modellistici utilizzati.

**Tabella 2 — Soluzione stocastica**

Deve riportare:

- composizione \(x^{SP}\);
- liquidità ottenibile dagli attivi per scenario;
- funding \(u_s^{SP}\);
- liquidità residua \(g_s^{SP}\);
- costo del funding per scenario.

**Tabella 3 — Expected Value e rivalutazione**

Deve riportare:

- parametri medi;
- \(x^{EV}\);
- valore ottimo del problema medio;
- ricorsi necessari negli scenari originari;
- \(z^{EV}\).

**Tabella 4 — Wait-and-see**

Deve riportare per ciascuno scenario:

- \(x_s^{WS}\);
- \(z_s^{WS}\).

**Tabella 5 — Confronto dei benchmark**

Deve confrontare:

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

### Grafici

**Figura 1 — Composizione dell'attivo**

Confronto tra:

\[
x^{SP}
\quad\text{e}\quad
x^{EV}.
\]

**Figura 2 — Funding per scenario**

Confronto del funding necessario nei tre scenari sotto:

\[
x^{SP}
\quad\text{e}\quad
x^{EV}.
\]

Le tabelle e i grafici devono essere prodotti come output del notebook e devono essere rigenerabili mediante riesecuzione delle celle.

Non sono richieste esportazioni automatiche in file esterni.

---

## 7. Controlli richiesti

### Controlli numerici

Verificare:

\[
\sum_s p_s=1,
\]

\[
\sum_jx_j=100,
\]

\[
x_j\geq0,
\]

\[
x_3\leq70,
\qquad
x_4\leq70.
\]

Per ogni scenario verificare:

\[
\sum_j\alpha_{js}x_j+u_s
=
d_s+g_s,
\]

e:

\[
u_s\geq0,
\qquad
g_s\geq0.
\]

### Controlli logici e teorici

Verificare che:

1. la decisione di primo stadio sia unica e comune agli scenari;
2. \(x^{EV}\) rimanga fissa durante la rivalutazione;
3. i problemi wait-and-see siano risolti separatamente per scenario;
4. il valore del problema medio non venga confuso con \(z^{EV}\);
5. risulti:

\[
z^{EV}\leq z^{SP}\leq z^{WS};
\]

6. risultino:

\[
VSS\geq0,
\qquad
EVPI\geq0.
\]

### Controlli computazionali

Verificare:

1. successo del solver;
2. assenza di violazioni numericamente significative dei vincoli;
3. coerenza tra ordinamento delle variabili matematiche e ordinamento utilizzato nel solver;
4. riproducibilità degli output mediante riesecuzione completa del notebook.

---

## 8. Ipotesi e limiti del caso

### Ipotesi modellistiche

1. Gli scenari sono mutuamente esclusivi ed esaustivi.
2. Le probabilità sono note al tempo iniziale.
3. La decisione iniziale è unica e comune agli scenari.
4. Le decisioni di ricorso vengono assunte dopo l'osservazione dello scenario.
5. Il funding di emergenza è disponibile senza limite quantitativo.
6. Il costo del funding è lineare.
7. Rendimenti, fabbisogni, liquidabilità e costi sono esogeni.
8. Le quantità monetarie sono espresse nella scala normalizzata \(A_0=100\).

### Semplificazioni adottate

1. L'incertezza futura è rappresentata mediante tre scenari discreti.
2. L'intero adattamento successivo alla decisione iniziale è concentrato in un unico secondo stadio.
3. La liquidabilità delle attività è rappresentata mediante coefficienti esogeni.
4. Il costo del funding è rappresentato mediante un coefficiente lineare scenario-specifico.

### Elementi esclusi

Il modello non considera:

- dinamica endogena di una corsa agli sportelli;
- capitale regolamentare;
- insolvenza;
- distinzione HTM/AFS;
- duration e mark-to-market espliciti;
- feedback tra decisioni e probabilità degli scenari;
- strumenti pubblici di emergenza.

### Limiti dell'interpretazione

Il caso è una rappresentazione quantitativa stilizzata finalizzata allo studio della programmazione stocastica a due stadi.

I risultati devono essere interpretati esclusivamente all'interno del modello assegnato e non possono essere letti come stime empiriche o ricostruzioni delle decisioni effettivamente assunte da Silicon Valley Bank.