# Lezione 16 — Scheda Caso TakeHome

## 1. Identificazione del caso

- **Lezione:** 16 — Applicazione in Python: programmazione stocastica
- **Tipo di caso:** Caso TakeHome
- **Titolo:** UK LDI 2022 — Buffer di liquidità, margin call e valore dell'informazione
- **Contesto sintetico:** gestione di un portafoglio LDI sotto scenari alternativi di margin call, con capacità limitata di ricorso mediante liquidità aggiuntiva e deleveraging
- **Uso previsto:** lavoro individuale TakeHome mediante notebook Python

La presente Scheda Caso costituisce la specifica vincolante del lavoro.

Non contiene la soluzione del problema e non deve essere modificata durante lo svolgimento, salvo esplicita indicazione del docente.

Il caso utilizza una rappresentazione stilizzata ispirata alla crisi britannica delle strategie Liability Driven Investment del 2022. Non costituisce la ricostruzione quantitativa di uno specifico fondo pensione o portafoglio LDI.

---

## 2. Contesto e domanda quantitativa

### Contesto

Un investitore istituzionale deve scegliere al tempo iniziale come ripartire le proprie risorse tra:

- buffer di liquidità immediatamente disponibile;
- esposizione a una strategia LDI.

La decisione deve essere presa prima di conoscere le future condizioni di mercato.

Successivamente si realizza uno tra tre scenari:

- normalizzazione;
- stress;
- stress estremo.

Lo scenario determina:

1. l'intensità della margin call;
2. la quantità di liquidità ottenibile mediante deleveraging;
3. il costo della liquidità aggiuntiva;
4. il costo economico del deleveraging.

Dopo l'osservazione dello scenario, il decisore può mobilitare liquidità aggiuntiva e ridurre l'esposizione LDI, entro limiti operativi assegnati.

Il caso utilizza esclusivamente un framework di programmazione stocastica lineare a due stadi:

\[
x
\longrightarrow
s
\longrightarrow
y_s.
\]

La decisione iniziale \(x\) è unica e comune agli scenari. Le decisioni di ricorso sono invece scenario-specifiche.

Il caso non introduce informazione progressiva, decisioni intermedie o vincoli di non anticipatività tra nodi intermedi.

### Domanda quantitativa

Determinare la combinazione iniziale tra buffer di liquidità ed esposizione LDI che massimizza il risultato economico atteso, tenendo conto congiuntamente di:

- rendimento delle due componenti iniziali;
- probabilità degli scenari;
- margin call;
- capacità limitata di mobilizzare liquidità aggiuntiva;
- capacità limitata di deleveraging;
- costi di ricorso.

Confrontare inoltre la soluzione stocastica con:

1. la decisione ottenuta sostituendo gli scenari con parametri medi;
2. il benchmark nel quale lo scenario è conosciuto prima della decisione iniziale.

La decisione Expected Value deve essere rivalutata negli scenari originari verificandone esplicitamente l'ammissibilità.

---

## 3. Modello e struttura del problema

### Grandezze economico-finanziarie

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

Il contributo economico di primo stadio è:

\[
0.010x_1+0.050x_2.
\]

### Variabili decisionali

La decisione iniziale soddisfa:

\[
x_1+x_2=100,
\]

\[
x_1\geq0,
\qquad
x_2\geq0,
\]

\[
x_2\geq50.
\]

Per ogni scenario \(s\), le decisioni di secondo stadio sono:

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

### Scenari

L'insieme degli scenari è:

\[
\mathcal S=\{N,S,E\},
\]

dove:

- \(N\): normalizzazione;
- \(S\): stress;
- \(E\): stress estremo.

A ciascuno scenario è associata una probabilità \(p_s\), con:

\[
p_s\geq0,
\qquad
\sum_{s\in\mathcal S}p_s=1.
\]

### Margin call

La margin call nello scenario \(s\) è:

\[
m_s=\alpha_sx_2.
\]

### Liquidità prodotta dal deleveraging

Una unità di esposizione liquidata produce:

\[
\beta_sf_s
\]

unità di liquidità.

### Bilancio di liquidità

Per ogni scenario:

\[
x_1+e_s+\beta_sf_s
=
\alpha_sx_2+g_s.
\]

### Limiti del ricorso

La liquidità aggiuntiva soddisfa:

\[
0\leq e_s\leq4.
\]

Il deleveraging soddisfa:

\[
0\leq f_s\leq25,
\]

e:

\[
f_s\leq x_2.
\]

### Costo di ricorso

Il costo nello scenario \(s\) è:

\[
C_s
=
\kappa_se_s+\delta_sf_s,
\]

dove:

- \(\kappa_s\): costo unitario della liquidità aggiuntiva;
- \(\delta_s\): costo economico unitario del deleveraging.

La funzione di ricorso può essere scritta come:

\[
Q_s(x)
=
\max_{e_s,f_s,g_s}
\left\{
-\kappa_se_s-\delta_sf_s
\right\},
\]

soggetta ai vincoli di secondo stadio.

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

La soluzione ottima di primo stadio è indicata con:

\[
x^{SP}.
\]

### Expected Value

Definire:

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

La soluzione del problema costruito sui parametri medi è indicata con:

\[
x^{EV}.
\]

La decisione \(x^{EV}\) deve essere successivamente mantenuta fissa e rivalutata separatamente negli scenari originari.

Se il ricorso è ammissibile in tutti gli scenari, definire:

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

Se \(x^{EV}\) non è ammissibile in almeno uno scenario, tale circostanza deve essere esplicitamente rilevata e discussa.

### Wait-and-see

Per ciascuno scenario viene inoltre risolto un problema nel quale la decisione iniziale può essere assunta conoscendo anticipatamente lo scenario.

Il valore atteso è:

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

| Variabile | Interpretazione | Rendimento unitario |
|---|---|---:|
| \(x_1\) | Buffer di liquidità | 0.010 |
| \(x_2\) | Esposizione LDI | 0.050 |

### Probabilità degli scenari

| Scenario | Descrizione | \(p_s\) |
|---|---|---:|
| \(N\) | Normalizzazione | 0.50 |
| \(S\) | Stress | 0.30 |
| \(E\) | Stress estremo | 0.20 |

### Coefficienti di margin call

| Scenario | \(\alpha_s\) |
|---|---:|
| \(N\) | 0.10 |
| \(S\) | 0.25 |
| \(E\) | 0.40 |

### Coefficienti di monetizzazione del deleveraging

| Scenario | \(\beta_s\) |
|---|---:|
| \(N\) | 1.00 |
| \(S\) | 0.90 |
| \(E\) | 0.75 |

### Costi della liquidità aggiuntiva

| Scenario | \(\kappa_s\) |
|---|---:|
| \(N\) | 0.020 |
| \(S\) | 0.060 |
| \(E\) | 0.120 |

### Costi economici del deleveraging

| Scenario | \(\delta_s\) |
|---|---:|
| \(N\) | 0.005 |
| \(S\) | 0.030 |
| \(E\) | 0.080 |

### Vincoli operativi

\[
x_1+x_2=100,
\]

\[
x_1\geq0,
\qquad
x_2\geq50,
\]

\[
0\leq e_s\leq4,
\]

\[
0\leq f_s\leq25,
\]

\[
f_s\leq x_2,
\]

\[
g_s\geq0.
\]

---

## 5. Quantità da stimare o calcolare

Determinare:

1. la soluzione stocastica
   \[
   x^{SP};
   \]

2. il valore ottimo
   \[
   z^{SP};
   \]

3. le decisioni di ricorso
   \[
   e_s^{SP},
   \qquad
   f_s^{SP},
   \qquad
   g_s^{SP};
   \]

4. i parametri medi
   \[
   \bar\alpha,
   \qquad
   \bar\beta,
   \qquad
   \bar\kappa,
   \qquad
   \bar\delta;
   \]

5. la soluzione Expected Value
   \[
   x^{EV};
   \]

6. il valore ottimo del problema deterministico medio;

7. l'ammissibilità di \(x^{EV}\) in ciascuno scenario originario;

8. \(z^{EV}\), se definito;

9. il VSS, se definito;

10. le soluzioni wait-and-see
    \[
    x_s^{WS};
    \]

11. i valori scenario-specifici
    \[
    z_s^{WS};
    \]

12. il valore atteso
    \[
    z^{WS};
    \]

13. l'Expected Value of Perfect Information
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
- parametri medi;
- soluzione EV;
- valore del problema medio;
- esito della rivalutazione di \(x^{EV}\) in ciascuno scenario;
- \(z^{EV}\), se definito;
- VSS, se definito;
- soluzioni WS;
- \(z^{WS}\);
- EVPI.

### Tabelle

**Tabella 1 — Parametri del problema**

Deve contenere:

- rendimenti;
- probabilità;
- \(\alpha_s\);
- \(\beta_s\);
- \(\kappa_s\);
- \(\delta_s\);
- limiti operativi.

**Tabella 2 — Soluzione stocastica**

Deve riportare:

- \(x^{SP}\);
- margin call per scenario;
- \(e_s^{SP}\);
- \(f_s^{SP}\);
- \(g_s^{SP}\);
- costo di ricorso per scenario.

**Tabella 3 — Expected Value e rivalutazione**

Deve riportare:

- parametri medi;
- \(x^{EV}\);
- valore ottimo del problema medio;
- stato di ammissibilità di \(x^{EV}\) in ciascuno scenario;
- ricorsi negli scenari ammissibili;
- \(z^{EV}\), se definito.

Se \(z^{EV}\) non è definito nella forma standard, la tabella deve indicarne esplicitamente la ragione.

**Tabella 4 — Wait-and-see**

Deve riportare per ciascuno scenario:

- \(x_s^{WS}\);
- \(z_s^{WS}\).

**Tabella 5 — Confronto dei benchmark**

Deve riportare sempre:

\[
z^{SP},
\qquad
z^{WS},
\qquad
EVPI.
\]

Deve riportare inoltre:

\[
z^{EV},
\qquad
VSS,
\]

soltanto quando definiti.

### Grafici

**Figura 1 — Decisioni di primo stadio**

Confronto tra:

\[
x^{SP}
\quad\text{e}\quad
x^{EV}.
\]

**Figura 2 — Ricorso per scenario**

Rappresentare almeno:

\[
e_s^{SP}
\quad\text{e}\quad
f_s^{SP}.
\]

**Figura 3 — Confronto dei benchmark**

Rappresentare:

\[
z^{SP}
\quad\text{e}\quad
z^{WS},
\]

e, se definito:

\[
z^{EV}.
\]

Se \(z^{EV}\) non è definito, tale circostanza deve essere rappresentata senza attribuirgli un valore numerico artificiale.

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
x_1+x_2=100,
\]

\[
x_1\geq0,
\qquad
x_2\geq50.
\]

Per ogni scenario verificare:

\[
0\leq e_s\leq4,
\]

\[
0\leq f_s\leq25,
\]

\[
f_s\leq x_2,
\]

\[
g_s\geq0,
\]

e il bilancio:

\[
x_1+e_s+\beta_sf_s
=
\alpha_sx_2+g_s.
\]

### Controlli logici e teorici

Verificare che:

1. la decisione di primo stadio sia unica e comune agli scenari;
2. \(x^{EV}\) rimanga fissa durante la rivalutazione;
3. l'ammissibilità di \(x^{EV}\) venga verificata separatamente in ciascuno scenario;
4. i problemi wait-and-see siano risolti separatamente;
5. risulti sempre:
   \[
   z^{SP}\leq z^{WS};
   \]
6. risulti:
   \[
   EVPI\geq0.
   \]

Se \(z^{EV}\) è definito, verificare inoltre:

\[
z^{EV}\leq z^{SP}\leq z^{WS},
\]

e:

\[
VSS\geq0.
\]

Se \(z^{EV}\) non è definito, non deve essere sostituito con un valore numerico arbitrario e il VSS non deve essere calcolato artificialmente.

### Controlli computazionali

Verificare:

1. successo del solver nei problemi ammissibili;
2. corretta identificazione degli eventuali problemi di ricorso inammissibili;
3. assenza di violazioni numericamente significative dei vincoli;
4. coerenza tra ordinamento delle variabili matematiche e ordinamento utilizzato nel solver;
5. riproducibilità degli output mediante riesecuzione completa del notebook.

---

## 8. Ipotesi e limiti del caso

### Ipotesi modellistiche

1. Gli scenari sono mutuamente esclusivi ed esaustivi.
2. Le probabilità sono note al tempo iniziale.
3. La decisione iniziale è unica e comune agli scenari.
4. Le decisioni di ricorso vengono assunte dopo l'osservazione dello scenario.
5. La margin call è proporzionale all'esposizione LDI.
6. La capacità di liquidità aggiuntiva è limitata.
7. La capacità di deleveraging è limitata.
8. I costi di ricorso sono lineari.
9. Le quantità monetarie sono espresse nella scala normalizzata \(A_0=100\).

### Semplificazioni adottate

1. L'incertezza è rappresentata mediante tre scenari discreti.
2. L'intero adattamento è concentrato in un unico secondo stadio.
3. La monetizzazione del deleveraging è rappresentata mediante coefficienti scenario-specifici.
4. Margin call e costi sono esogeni.
5. Non vengono modellati effetti dinamici successivi al ricorso.

### Elementi esclusi

Il modello non considera:

- dinamiche intraday;
- collateral waterfall;
- haircut multipli;
- feedback endogeni sui prezzi dei gilt;
- derivati specifici;
- duration delle passività;
- requisiti regolamentari dettagliati;
- informazione progressiva;
- decisioni multistadio.

### Limiti dell'interpretazione

Il caso è una rappresentazione quantitativa stilizzata finalizzata allo studio della programmazione stocastica a due stadi e della fattibilità del ricorso.

I risultati devono essere interpretati esclusivamente all'interno del modello assegnato e non possono essere letti come stime empiriche o ricostruzioni delle decisioni effettivamente assunte da specifici fondi pensione o operatori LDI.