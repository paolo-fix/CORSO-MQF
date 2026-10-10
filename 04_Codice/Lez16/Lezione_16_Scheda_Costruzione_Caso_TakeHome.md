# Lezione 16 — Scheda Costruzione Caso TakeHome

## 1. Identificazione del caso

- **Lezione:** 16 — Applicazione in Python: programmazione stocastica
- **Tipo di caso:** TakeHome
- **Titolo:** *UK LDI 2022 — Buffer di liquidità, margin call e valore dell'informazione*
- **Contesto:** crisi delle strategie Liability Driven Investment (LDI) dei fondi pensione britannici nell'autunno 2022.
- **Framework metodologico:** programmazione stocastica lineare **two-stage**.
- **Uso previsto:** lavoro autonomo successivo al Caso Aula SVB, con contesto finanziario differente ma struttura metodologica comparabile.

Il caso deve consolidare i concetti dei Capitoli 14 e 15 relativi a decisione di primo stadio, decisioni di ricorso, soluzione stocastica, Expected Value, wait-and-see, VSS ed EVPI.

Il caso non deve utilizzare una struttura multistadio e non deve introdurre vincoli di non anticipatività tra nodi intermedi.

---

## 2. Contesto e motivazione

Le strategie Liability Driven Investment sono utilizzate da fondi pensione defined benefit per gestire la sensibilità del valore delle attività rispetto alle passività future.

Nel settembre 2022 il rapido aumento dei rendimenti dei gilt britannici produsse forti perdite di valore sulle posizioni utilizzate nelle strategie LDI e generò richieste di collateral e margin call. In presenza di buffer liquidi insufficienti, alcuni investitori dovettero mobilitare liquidità aggiuntiva e vendere attività in condizioni di mercato sfavorevoli.

Il caso utilizza questo episodio storico come riferimento economico-finanziario, ma la specificazione quantitativa è deliberatamente stilizzata e didattica. Non rappresenta la ricostruzione di uno specifico fondo pensione o di uno specifico LDI fund.

La motivazione didattica è mostrare che una decisione iniziale più redditizia ma meno liquida può risultare fragile quando si manifesta uno scenario avverso e che la programmazione stocastica consente di valutare ex ante il trade-off tra rendimento e capacità di assorbire richieste di liquidità future.

---

## 3. Domanda quantitativa e obiettivo didattico

### Domanda quantitativa

Quale combinazione iniziale tra buffer di liquidità ed esposizione LDI massimizza il risultato economico atteso quando l'intensità delle margin call, la capacità di monetizzare l'esposizione e il costo del ricorso dipendono dallo scenario futuro?

Quanto valore produce la soluzione stocastica rispetto a una decisione costruita sui valori medi?

Quanto varrebbe conoscere anticipatamente lo scenario che si realizzerà?

### Obiettivi didattici

Lo studente deve essere in grado di:

1. distinguere decisione di primo stadio e decisioni di ricorso;
2. rappresentare una crisi di liquidità mediante scenari discreti;
3. formulare un programma lineare stocastico two-stage;
4. costruire la forma estesa del problema;
5. risolvere il problema stocastico;
6. costruire e valutare il problema Expected Value;
7. costruire il benchmark wait-and-see;
8. calcolare VSS ed EVPI;
9. verificare fattibilità, bilanci e ordinamento dei benchmark;
10. interpretare economicamente il ruolo del buffer iniziale.

---

## 4. Specifica teorico-matematica

### 4.1 Decisione di primo stadio

Le risorse iniziali sono normalizzate a:

$$
A_0=100.
$$

La decisione iniziale è:

$$
x=
\begin{pmatrix}
x_1 \\
x_2
\end{pmatrix},
$$

dove:

- $x_1$ è il buffer di liquidità immediatamente disponibile;
- $x_2$ è l'esposizione LDI.

Il vincolo iniziale è:

$$
x_1+x_2=100.
$$

Si impone inoltre:

$$
x_1\geq0,
\qquad
x_2\geq0.
$$

Per preservare una funzione minima di copertura delle passività si impone:

$$
x_2\geq50.
$$

Il rendimento unitario delle due componenti è:

$$
c_1=0.010,
\qquad
c_2=0.050.
$$

Il rendimento iniziale del portafoglio è quindi:

$$
c'x
=
0.010x_1+0.050x_2.
$$

### 4.2 Scenari

Si considerano tre scenari completi:

$$
\mathcal S=\{N,S,E\},
$$

dove:

- $N$ = normalizzazione;
- $S$ = stress;
- $E$ = stress estremo.

Le probabilità sono:

| Scenario | Descrizione | $p_s$ |
|---|---|---:|
| $N$ | Normalizzazione | 0.50 |
| $S$ | Stress | 0.30 |
| $E$ | Stress estremo | 0.20 |

Deve valere:

$$
\sum_{s\in\mathcal S}p_s=1.
$$

### 4.3 Margin call

La margin call nello scenario $s$ è proporzionale all'esposizione LDI iniziale:

$$
m_s=\alpha_s x_2.
$$

I coefficienti assegnati sono:

| Scenario | $\alpha_s$ |
|---|---:|
| $N$ | 0.10 |
| $S$ | 0.25 |
| $E$ | 0.40 |

### 4.4 Decisioni di ricorso

Dopo avere osservato lo scenario $s$, il decisore può utilizzare:

$$
e_s\geq0,
$$

dove $e_s$ rappresenta liquidità aggiuntiva mobilitata esternamente;

$$
f_s\geq0,
$$

dove $f_s$ rappresenta esposizione LDI liquidata o deleverata;

$$
g_s\geq0,
$$

dove $g_s$ rappresenta liquidità residua dopo avere soddisfatto la margin call.

La monetizzazione dell'esposizione liquidata dipende dallo scenario. Una unità di $f_s$ genera:

$$
\beta_s f_s
$$

unità di liquidità.

I coefficienti sono:

| Scenario | $\beta_s$ |
|---|---:|
| $N$ | 1.00 |
| $S$ | 0.90 |
| $E$ | 0.75 |

Il bilancio di liquidità nello scenario $s$ è:

$$
x_1+e_s+\beta_s f_s
=
m_s+g_s.
$$

Sostituendo $m_s=\alpha_sx_2$:

$$
x_1+e_s+\beta_s f_s
=
\alpha_sx_2+g_s.
$$

### 4.5 Limiti operativi

La liquidità aggiuntiva mobilitabile è limitata da:

$$
0\leq e_s\leq4.
$$

Il deleveraging massimo è:

$$
0\leq f_s\leq25.
$$

Non è possibile liquidare una quantità superiore all'esposizione LDI iniziale:

$$
f_s\leq x_2.
$$

### 4.6 Costi di ricorso

Il costo unitario della liquidità aggiuntiva è:

| Scenario | $\kappa_s$ |
|---|---:|
| $N$ | 0.020 |
| $S$ | 0.060 |
| $E$ | 0.120 |

Il costo economico unitario del deleveraging è:

| Scenario | $\lambda_s$ |
|---|---:|
| $N$ | 0.005 |
| $S$ | 0.030 |
| $E$ | 0.080 |

Il costo di ricorso nello scenario $s$ è:

$$
C_s
=
\kappa_s e_s+\lambda_s f_s.
$$

La funzione di ricorso può essere scritta come:

$$
Q_s(x)
=
\max_{e_s,f_s,g_s}
\left\{
-\kappa_s e_s-\lambda_s f_s
\right\}
$$

soggetta ai vincoli di liquidità e ai limiti operativi dello scenario.

### 4.7 Problema stocastico

Il problema stocastico è:

$$
z^{SP}
=
\max
\left\{
0.010x_1+0.050x_2
+
\sum_{s\in\mathcal S}p_sQ_s(x)
\right\}.
$$

La decisione ottima di primo stadio è:

$$
x^{SP}.
$$

La decisione iniziale deve essere unica e comune a tutti gli scenari.

La struttura informativa è:

$$
x
\longrightarrow
s
\longrightarrow
y_s,
$$

dove:

$$
y_s=
\begin{pmatrix}
e_s \\
f_s \\
g_s
\end{pmatrix}.
$$

### 4.8 Expected Value

Il problema deterministico medio utilizza:

$$
\bar\alpha
=
\sum_s p_s\alpha_s,
$$

$$
\bar\beta
=
\sum_s p_s\beta_s,
$$

$$
\bar\kappa
=
\sum_s p_s\kappa_s,
$$

$$
\bar\lambda
=
\sum_s p_s\lambda_s.
$$

La soluzione del problema medio è indicata con:

$$
x^{EV}.
$$

Per determinare il valore della decisione Expected Value, $x^{EV}$ deve essere fissata e rivalutata negli scenari originari.

Il valore stocastico della decisione $x^{EV}$ è:

$$
z^{EV}
=
c'x^{EV}
+
\sum_s p_sQ_s(x^{EV}).
$$

Il Value of the Stochastic Solution è:

$$
VSS
=
z^{SP}-z^{EV}.
$$

### 4.9 Wait-and-see

Nel benchmark wait-and-see lo scenario futuro è noto prima della decisione iniziale.

Per ciascuno scenario $s$ si risolve:

$$
z_s^{WS}
=
\max
\left\{
c'x_s+Q_s(x_s)
\right\}.
$$

Il valore atteso wait-and-see è:

$$
z^{WS}
=
\sum_s p_sz_s^{WS}.
$$

L'Expected Value of Perfect Information è:

$$
EVPI
=
z^{WS}-z^{SP}.
$$

Per un problema di massimizzazione deve valere:

$$
z^{EV}
\leq
z^{SP}
\leq
z^{WS}.
$$

Devono inoltre risultare:

$$
VSS\geq0,
$$

$$
EVPI\geq0.
$$

---

## 5. Output richiesti

### Stime o risultati numerici

Calcolare:

1. $x^{SP}$;
2. $z^{SP}$;
3. decisioni di ricorso $e_s$, $f_s$, $g_s$ sotto $x^{SP}$;
4. $x^{EV}$;
5. $z^{EV}$;
6. $VSS$;
7. $x_s^{WS}$ per ciascuno scenario;
8. $z_s^{WS}$ per ciascuno scenario;
9. $z^{WS}$;
10. $EVPI$.

### Tabelle

Produrre:

1. tabella dei parametri;
2. tabella della soluzione SP;
3. tabella della rivalutazione di $x^{EV}$ negli scenari originari;
4. tabella dei problemi wait-and-see;
5. tabella riepilogativa dei benchmark $z^{EV}$, $z^{SP}$, $z^{WS}$, $VSS$, $EVPI$.

### Grafici

Produrre almeno:

1. confronto tra $x^{SP}$ e $x^{EV}$;
2. confronto delle decisioni di ricorso per scenario;
3. confronto tra i valori $z^{EV}$, $z^{SP}$ e $z^{WS}$.

### Controlli

Verificare:

1. somma delle probabilità;
2. vincolo $x_1+x_2=100$;
3. vincolo $x_2\geq50$;
4. non negatività;
5. limiti su $e_s$ e $f_s$;
6. vincolo $f_s\leq x_2$;
7. bilanci di liquidità;
8. ottimalità del solver;
9. corretta rivalutazione di $x^{EV}$;
10. corretta costruzione dei problemi WS;
11. ordinamento dei benchmark.

---

## 6. Flusso logico-teorico risolutivo atteso

| Passo | Finalità risolutiva | Formula teorico-matematica / definizione / proprietà / teorema | Applicazione nel caso | Output o controllo collegato |
|---:|---|---|---|---|
| 1 | Identificare struttura informativa, decisioni e scenari | Modello stocastico two-stage: decisione iniziale comune $x$ e ricorso scenario-specifico $y_s$ | $x=(x_1,x_2)'$ è comune; dopo lo scenario $s\in\{N,S,E\}$ si scelgono $e_s,f_s,g_s$ | corretta classificazione di variabili, scenari e tempi decisionali |
| 2 | Costruire il meccanismo di ricorso e verificarne la fattibilità | Funzione di ricorso $Q_s(x)$ e vincoli di secondo stadio | margin call $\alpha_sx_2$; bilancio $x_1+e_s+\beta_sf_s=\alpha_sx_2+g_s$; limiti su $e_s$ e $f_s$ | forma estesa, controlli dei bilanci, bounds e fattibilità |
| 3 | Determinare la soluzione stocastica | $z^{SP}=\max\{c'x+\sum_sp_sQ_s(x)\}$ | scelta congiunta del buffer e dell'esposizione LDI tenendo conto dei tre scenari | $x^{SP}$, ricorsi ottimi, $z^{SP}$ |
| 4 | Costruire il benchmark Expected Value e valutarlo correttamente | Problema deterministico sui parametri medi; fissazione di $x^{EV}$ e rivalutazione negli scenari originari | determinazione di $x^{EV}$ e calcolo di $z^{EV}$ | $x^{EV}$, $z^{EV}$, $VSS=z^{SP}-z^{EV}$ |
| 5 | Costruire il benchmark wait-and-see e misurare il valore dell'informazione | Ottimizzazione separata per scenario e $z^{WS}=\sum_sp_sz_s^{WS}$ | scelta di una decisione iniziale diversa conoscendo anticipatamente ciascuno scenario | $x_s^{WS}$, $z_s^{WS}$, $z^{WS}$, $EVPI=z^{WS}-z^{SP}$ |
| 6 | Verificare e interpretare i benchmark | Per massimizzazione: $z^{EV}\leq z^{SP}\leq z^{WS}$, $VSS\geq0$, $EVPI\geq0$ | interpretazione del trade-off rendimento/liquidità e del valore della modellizzazione stocastica rispetto all'informazione perfetta | tabella finale dei benchmark, grafici e commento economico-finanziario |

---

## 7. Scomposizione attesa in tappe

| Tappa | Regime | Input | Operazione | Output | Controllo | Uso successivo |
|---:|:---:|---|---|---|---|---|
| 1 | A | Scheda Caso | ricostruire variabili, scenari e logica two-stage | struttura teorica del caso | distinzione primo/secondo stadio | preparazione modello |
| 2 | B | parametri del caso | costruire dati e controllare probabilità | strutture dati | probabilità sommano a uno | input solver |
| 3 | B | modello e dati | formulare e risolvere SP | $x^{SP}$, ricorsi, $z^{SP}$ | fattibilità e bilanci | benchmark principale |
| 4 | B | parametri medi | costruire EV e rivalutare $x^{EV}$ | $x^{EV}$, $z^{EV}$ | nessuna riottimizzazione di $x$ | calcolo VSS |
| 5 | B | scenari originari | risolvere WS scenario per scenario | $x_s^{WS}$, $z_s^{WS}$, $z^{WS}$ | ponderazione corretta | calcolo EVPI |
| 6 | C | tutti gli output | verificare benchmark, tabelle, grafici e interpretazione | notebook finale validato | $z^{EV}\leq z^{SP}\leq z^{WS}$ | conclusione |

---

## 8. Mappa tra prompt e notebook

| Prompt | Regime | Funzione | Sezione notebook |
|---|:---:|---|---|
| Prompt zero | — | inizializzazione del contesto | nessuna cella |
| Prompt 1 | — | acquisizione Scheda Caso | cella Markdown iniziale |
| Prompt 2 | A | Flusso logico-teorico | cella Markdown |
| Prompt 3 | A | scomposizione in tappe | cella Markdown |
| Tappa 1 | A | chiarimento della struttura two-stage | Markdown |
| Tappa 2 | B | dati e parametri | Markdown + code |
| Tappa 3 | B | soluzione SP | Markdown + code |
| Tappa 4 | B | EV e rivalutazione | Markdown + code |
| Tappa 5 | B | WS, VSS ed EVPI | Markdown + code |
| Verifica finale | C | controllo mirato di completezza e coerenza | eventuali celle sostitutive |
| Interpretazione finale | C | revisione critica di una bozza dello studente | Markdown finale |

Per il TakeHome si prevede un intervallo di **9–11 prompt complessivi**, contando Prompt zero e Prompt 1.

---

## 9. Struttura attesa del notebook

Il notebook deve contenere, in ordine logico:

1. cella Markdown iniziale;
2. Flusso logico-teorico;
3. scomposizione in tappe;
4. import delle librerie;
5. definizione degli scenari;
6. definizione delle probabilità;
7. controllo della somma delle probabilità;
8. definizione dei parametri di primo stadio;
9. definizione dei parametri di ricorso;
10. costruzione del vettore delle variabili;
11. costruzione della funzione obiettivo SP;
12. costruzione dei vincoli di uguaglianza;
13. costruzione dei vincoli di disuguaglianza e bounds;
14. soluzione con `scipy.optimize.linprog(method="highs")`;
15. estrazione di $x^{SP}$;
16. estrazione delle decisioni di ricorso;
17. controllo dei bilanci;
18. controllo dei bounds;
19. costruzione della tabella SP;
20. calcolo dei parametri medi;
21. costruzione e soluzione del problema EV;
22. fissazione di $x^{EV}$;
23. rivalutazione negli scenari originari;
24. calcolo di $z^{EV}$;
25. calcolo di $VSS$;
26. costruzione dei problemi WS;
27. soluzione dei tre problemi WS;
28. calcolo di $z^{WS}$;
29. calcolo di $EVPI$;
30. tabella di confronto dei benchmark;
31. grafici richiesti;
32. controlli finali;
33. interpretazione finale autonoma;
34. limiti del modello.

Le librerie previste sono:

- NumPy;
- pandas;
- `scipy.optimize.linprog`;
- matplotlib.

Non è necessario introdurre classi, programmazione a oggetti o framework generali di stochastic programming.

---

## 10. Calibrazione docente

La calibrazione deve essere verificata con solver prima della distribuzione del caso.

### Soluzione stocastica

La soluzione attesa è:

$$
x^{SP}
=
\begin{pmatrix}
25 \\
75
\end{pmatrix}.
$$

Il valore ottimo atteso è:

$$
z^{SP}=3.7375.
$$

### Expected Value

La soluzione del problema medio è:

$$
x^{EV}
=
\begin{pmatrix}
16.25 \\
83.75
\end{pmatrix}.
$$

La rivalutazione negli scenari originari produce:

$$
z^{EV}
=
3.5445833.
$$

Pertanto:

$$
VSS
=
z^{SP}-z^{EV}
=
0.1929167.
$$

### Wait-and-see

Il valore atteso wait-and-see è:

$$
z^{WS}=4.43125.
$$

Pertanto:

$$
EVPI
=
z^{WS}-z^{SP}
=
0.69375.
$$

Deve risultare:

$$
3.5445833
<
3.7375
<
4.43125.
$$

### Nota sulla calibrazione

Il valore ottimo del problema deterministico medio coincide numericamente, nella calibrazione adottata, con $z^{WS}$.

Questa coincidenza è accidentale e non deve essere interpretata come identità teorica.

Devono rimanere distinti:

- valore ottimo del problema medio;
- $z^{EV}$, cioè valore stocastico della decisione $x^{EV}$;
- $z^{WS}$, valore atteso dei problemi scenario-specifici con informazione perfetta.

---

## 11. Uso dell'IA e tracciato

Il lavoro deve seguire la sequenza:

1. Prompt zero;
2. Prompt 1;
3. Prompt 2;
4. Prompt 3;
5. prompt di tappa;
6. eventuali prompt C;
7. verifica finale;
8. interpretazione finale autonoma.

Il Regime A deve essere usato per:

- ricostruire la struttura del problema;
- distinguere primo stadio e recourse;
- collegare modello, benchmark e controlli.

Il Regime B deve essere usato per:

- costruire il modello per il solver;
- implementare SP;
- implementare EV;
- rivalutare $x^{EV}$;
- implementare WS;
- produrre tabelle e grafici.

Il Regime C deve partire da:

- un dubbio;
- un output già prodotto;
- una possibile incoerenza;
- una verifica concreta.

Non è ammesso chiedere all'IA di:

- modificare la Scheda Caso;
- cambiare scenari o probabilità;
- cambiare parametri;
- sostituire SP con un modello multistadio;
- introdurre nuovi scenari;
- produrre globalmente tutto il notebook;
- scrivere autonomamente l'interpretazione finale.

---

## 12. Valutazione

La valutazione deve considerare:

1. correttezza del Flusso logico-teorico;
2. qualità della scomposizione in tappe;
3. corretta formulazione del modello two-stage;
4. corretta costruzione di SP;
5. corretta costruzione e rivalutazione di EV;
6. corretta costruzione di WS;
7. corretto calcolo di VSS ed EVPI;
8. controlli di fattibilità e bilancio;
9. qualità delle tabelle;
10. qualità dei grafici;
11. coerenza tra notebook e tracciato IA;
12. uso corretto dei Regimi A/B/C;
13. interpretazione economico-finanziaria;
14. consapevolezza dei limiti del modello.

Particolare attenzione deve essere dedicata a:

- distinzione tra problema EV e valore $z^{EV}$;
- distinzione tra $z^{EV}$ e $z^{WS}$;
- significato di VSS;
- significato di EVPI;
- ruolo del buffer;
- costo economico della liquidità insufficiente;
- differenza tra una scelta robusta ex ante e una scelta effettuata conoscendo già lo scenario.

---

## 13. Relazione con il Caso Aula

Il Caso Aula e il Caso TakeHome condividono la stessa struttura metodologica:

$$
x
\longrightarrow
s
\longrightarrow
y_s.
$$

Nel Caso Aula:

- il decisore è una banca;
- la decisione iniziale riguarda la composizione dell'attivo;
- il rischio principale è il fabbisogno di liquidità associato a un deposit run;
- il ricorso principale è il funding di emergenza.

Nel Caso TakeHome:

- il decisore è un investitore istituzionale con strategia LDI;
- la decisione iniziale riguarda il trade-off tra buffer ed esposizione;
- il rischio principale è la margin call;
- il ricorso comprende liquidità aggiuntiva e deleveraging.

I due casi sono quindi isomorfi sul piano metodologico ma differenti nel meccanismo finanziario.

La domanda comune è:

> Quanto conviene sacrificare oggi rendimento o esposizione strategica per mantenere capacità di adattamento quando le condizioni future sono incerte?

La specificità del TakeHome è mostrare lo stesso metodo in un problema di collateral e leverage, evitando che lo studente replichi semplicemente il caso bancario con parametri differenti.
