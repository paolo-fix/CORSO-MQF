# Lezione 16 — Scheda Caso TakeHome

## 1. Identificazione del caso

- **Lezione:** 16 — Applicazione in Python: programmazione stocastica
- **Tipo di caso:** TakeHome
- **Titolo:** *UK LDI 2022 — Buffer di liquidità, margin call e valore dell'informazione*
- **Contesto:** crisi delle strategie Liability Driven Investment (LDI) dei fondi pensione britannici nell'autunno 2022.
- **Framework metodologico:** programmazione stocastica lineare **two-stage**.
- **Prodotti da consegnare:** notebook Jupyter eseguibile e tracciato IA secondo le istruzioni generali del corso.
- **Numero complessivo di prompt nel tracciato IA:** da 9 a 11, comprendendo Prompt zero e Prompt 1.

La presente Scheda Caso costituisce la **specifica vincolante del lavoro**. Variabili, scenari, parametri, formule, quantità da calcolare, output richiesti, controlli e ipotesi non devono essere modificati durante lo svolgimento.

La Scheda Caso non contiene la soluzione del problema.

---

## 2. Contesto e domanda quantitativa

Le strategie Liability Driven Investment sono utilizzate da fondi pensione defined benefit per gestire la sensibilità del valore delle attività rispetto alle passività future.

Nel settembre 2022 il rapido aumento dei rendimenti dei gilt britannici generò forti richieste di collateral e margin call sulle strategie LDI. In presenza di buffer liquidi insufficienti, alcuni investitori dovettero mobilitare liquidità aggiuntiva e ridurre rapidamente le proprie esposizioni in condizioni di mercato sfavorevoli.

Il caso utilizza questo episodio come riferimento economico-finanziario, ma adotta un modello quantitativo stilizzato. Il decisore dispone inizialmente di risorse pari a 100 e deve scegliere quanta parte mantenere come buffer di liquidità e quanta destinare all'esposizione LDI.

Dopo la decisione iniziale si realizza uno fra tre scenari completi. Lo scenario determina l'intensità della margin call, l'efficacia con cui l'esposizione liquidata può essere trasformata in liquidità e i costi delle decisioni di ricorso.

La domanda quantitativa centrale è:

> **Quale combinazione iniziale tra buffer di liquidità ed esposizione LDI massimizza il risultato economico atteso, tenendo conto delle margin call e delle possibilità di ricorso nei diversi scenari?**

Il lavoro deve inoltre rispondere a due domande collegate:

1. quanto vale utilizzare esplicitamente la distribuzione degli scenari rispetto a una decisione costruita sui valori medi;
2. quanto varrebbe conoscere anticipatamente lo scenario futuro.

---

## 3. Modello e struttura del problema

### 3.1 Decisione di primo stadio

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
x_2\geq0,
$$

e, per preservare una funzione minima di copertura delle passività:

$$
x_2\geq50.
$$

Il contributo economico di primo stadio è:

$$
c'x
=
0.010x_1+0.050x_2.
$$

### 3.2 Scenari

L'insieme degli scenari è:

$$
\mathcal S=\{N,S,E\},
$$

dove:

- $N$ = normalizzazione;
- $S$ = stress;
- $E$ = stress estremo.

La decisione $x$ viene assunta prima di conoscere quale scenario si realizzerà.

### 3.3 Margin call

Nello scenario $s$, la margin call è proporzionale all'esposizione LDI iniziale:

$$
m_s=\alpha_sx_2.
$$

### 3.4 Decisioni di ricorso

Dopo avere osservato lo scenario $s$, il decisore può utilizzare tre variabili di secondo stadio:

$$
e_s\geq0,
$$

liquidità aggiuntiva mobilitata esternamente;

$$
f_s\geq0,
$$

quota di esposizione LDI liquidata o deleverata;

$$
g_s\geq0,
$$

liquidità residua dopo avere soddisfatto la margin call.

Una unità di esposizione liquidata nello scenario $s$ genera:

$$
\beta_s f_s
$$

unità di liquidità.

Il bilancio di liquidità è:

$$
x_1+e_s+\beta_sf_s
=
\alpha_sx_2+g_s.
$$

I limiti operativi sono:

$$
0\leq e_s\leq4,
$$

$$
0\leq f_s\leq25,
$$

$$
f_s\leq x_2.
$$

### 3.5 Costi di ricorso

Il costo economico del ricorso nello scenario $s$ è:

$$
C_s
=
\kappa_se_s+\lambda_sf_s.
$$

La funzione di ricorso è:

$$
Q_s(x)
=
\max_{e_s,f_s,g_s}
\left\{
-\kappa_se_s-\lambda_sf_s
\right\}
$$

soggetta al bilancio di liquidità e ai limiti operativi dello scenario.

### 3.6 Problema stocastico

Il programma stocastico è:

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

La decisione ottima di primo stadio è indicata con:

$$
x^{SP}.
$$

La struttura informativa del caso è esclusivamente two-stage:

$$
x
\longrightarrow
s
\longrightarrow
y_s,
$$

con:

$$
y_s=
\begin{pmatrix}
e_s \\
f_s \\
g_s
\end{pmatrix}.
$$

Non sono previste decisioni intermedie tra la scelta iniziale e l'osservazione dello scenario completo.

### 3.7 Expected Value

Per costruire il problema deterministico medio utilizzare:

$$
\bar\alpha
=
\sum_{s\in\mathcal S}p_s\alpha_s,
$$

$$
\bar\beta
=
\sum_{s\in\mathcal S}p_s\beta_s,
$$

$$
\bar\kappa
=
\sum_{s\in\mathcal S}p_s\kappa_s,
$$

$$
\bar\lambda
=
\sum_{s\in\mathcal S}p_s\lambda_s.
$$

La decisione iniziale ottima del problema medio è indicata con:

$$
x^{EV}.
$$

Per valutarla sotto l'incertezza originaria, $x^{EV}$ deve essere mantenuta fissa e il ricorso deve essere nuovamente ottimizzato in ciascuno scenario originale.

Il valore stocastico della decisione $x^{EV}$ è:

$$
z^{EV}
=
c'x^{EV}
+
\sum_{s\in\mathcal S}p_sQ_s(x^{EV}).
$$

Il Value of the Stochastic Solution è:

$$
VSS
=
z^{SP}-z^{EV}.
$$

### 3.8 Wait-and-see

Nel benchmark wait-and-see lo scenario è noto prima della decisione iniziale.

Per ciascuno scenario $s$ si risolve:

$$
z_s^{WS}
=
\max
\left\{
c'x_s+Q_s(x_s)
\right\}.
$$

Il valore wait-and-see è:

$$
z^{WS}
=
\sum_{s\in\mathcal S}p_sz_s^{WS}.
$$

L'Expected Value of Perfect Information è:

$$
EVPI
=
z^{WS}-z^{SP}.
$$

Per il problema di massimizzazione deve risultare:

$$
z^{EV}
\leq
z^{SP}
\leq
z^{WS}.
$$

---

## 4. Parametri assegnati

### 4.1 Parametri di primo stadio

| Parametro | Significato | Valore |
|---|---|---:|
| $A_0$ | risorse iniziali | 100 |
| $c_1$ | rendimento unitario del buffer | 0.010 |
| $c_2$ | rendimento unitario dell'esposizione LDI | 0.050 |
| $x_2^{\min}$ | esposizione LDI minima | 50 |

### 4.2 Parametri di scenario

| Scenario | $p_s$ | $\alpha_s$ | $\beta_s$ | $\kappa_s$ | $\lambda_s$ |
|---|---:|---:|---:|---:|---:|
| $N$ | 0.50 | 0.10 | 1.00 | 0.020 | 0.005 |
| $S$ | 0.30 | 0.25 | 0.90 | 0.060 | 0.030 |
| $E$ | 0.20 | 0.40 | 0.75 | 0.120 | 0.080 |

Interpretazione dei parametri:

- $p_s$ = probabilità dello scenario;
- $\alpha_s$ = margin call per unità di esposizione LDI;
- $\beta_s$ = liquidità ottenuta per unità di esposizione liquidata;
- $\kappa_s$ = costo unitario della liquidità aggiuntiva;
- $\lambda_s$ = costo economico unitario del deleveraging.

### 4.3 Limiti di ricorso

Per ogni scenario:

$$
0\leq e_s\leq4,
$$

$$
0\leq f_s\leq25,
$$

$$
g_s\geq0,
$$

$$
f_s\leq x_2.
$$

Tutte le quantità monetarie sono espresse nella scala normalizzata del modello con $A_0=100$.

I parametri sono **didattici e stilizzati**. Sono costruiti per rappresentare il meccanismo economico di una crisi LDI e non costituiscono una calibrazione empirica di uno specifico fondo pensione.

---

## 5. Quantità da stimare o calcolare

Determinare:

1. la soluzione stocastica di primo stadio $x^{SP}$;
2. il valore ottimo $z^{SP}$;
3. le decisioni di ricorso ottime $e_s$, $f_s$, $g_s$ per ciascuno scenario sotto $x^{SP}$;
4. i valori dei parametri medi $\bar\alpha$, $\bar\beta$, $\bar\kappa$, $\bar\lambda$;
5. la decisione iniziale del problema medio $x^{EV}$;
6. il valore $z^{EV}$ ottenuto fissando $x=x^{EV}$ e rivalutando tale decisione negli scenari originari;
7. il Value of the Stochastic Solution:

$$
VSS=z^{SP}-z^{EV};
$$

8. le soluzioni wait-and-see $x_s^{WS}$ e i valori $z_s^{WS}$ per ciascuno scenario;
9. il valore:

$$
z^{WS}
=
\sum_{s\in\mathcal S}p_sz_s^{WS};
$$

10. l'Expected Value of Perfect Information:

$$
EVPI=z^{WS}-z^{SP}.
$$

Il valore ottimo del problema deterministico medio deve essere tenuto distinto da $z^{EV}$.

---

## 6. Output richiesti

### 6.1 Risultati numerici

Il notebook deve riportare chiaramente:

1. $x^{SP}$ e $z^{SP}$;
2. $e_s$, $f_s$, $g_s$ per ciascuno scenario sotto $x^{SP}$;
3. $\bar\alpha$, $\bar\beta$, $\bar\kappa$, $\bar\lambda$;
4. $x^{EV}$ e valore ottimo del problema deterministico medio;
5. $z^{EV}$;
6. $VSS$;
7. $x_s^{WS}$ e $z_s^{WS}$ per ciascuno scenario;
8. $z^{WS}$;
9. $EVPI$.

### 6.2 Tabelle

Produrre almeno le seguenti tabelle:

1. **Tabella dei parametri del caso**, con probabilità e coefficienti scenario-specifici;
2. **Tabella della soluzione SP**, con decisione iniziale, margin call, ricorsi e liquidità residua per scenario;
3. **Tabella di rivalutazione di $x^{EV}$**, con ricorsi ottimi nei tre scenari originari e contributo economico scenario-specifico;
4. **Tabella wait-and-see**, con $x_s^{WS}$ e $z_s^{WS}$ per ciascuno scenario;
5. **Tabella riepilogativa dei benchmark**, contenente almeno $z^{EV}$, $z^{SP}$, $z^{WS}$, $VSS$ ed $EVPI$.

### 6.3 Grafici

Produrre tre grafici:

1. **Confronto tra $x^{SP}$ e $x^{EV}$**, distinguendo buffer ed esposizione LDI;
2. **Decisioni di ricorso per scenario**, mostrando almeno $e_s$ e $f_s$ sotto la soluzione stocastica;
3. **Confronto dei benchmark**, rappresentando $z^{EV}$, $z^{SP}$ e $z^{WS}$.

Ogni grafico deve avere titolo, assi ed etichette leggibili e deve essere accompagnato da una breve interpretazione collegata alla domanda quantitativa del caso.

---

## 7. Controlli richiesti

Il notebook deve includere verifiche osservabili sui seguenti punti.

### 7.1 Probabilità e dati

Verificare:

$$
\sum_{s\in\mathcal S}p_s=1.
$$

Controllare inoltre che tutti i parametri utilizzati dal codice coincidano con quelli della Scheda Caso.

### 7.2 Vincoli di primo stadio

Verificare numericamente:

$$
x_1+x_2=100,
$$

$$
x_1\geq0,
$$

$$
x_2\geq50.
$$

### 7.3 Vincoli di ricorso

Per ogni scenario verificare:

$$
0\leq e_s\leq4,
$$

$$
0\leq f_s\leq25,
$$

$$
g_s\geq0,
$$

$$
f_s\leq x_2.
$$

### 7.4 Bilancio di liquidità

Per ogni scenario verificare che il residuo del bilancio:

$$
x_1+e_s+\beta_sf_s-\alpha_sx_2-g_s
$$

sia numericamente nullo entro una tolleranza coerente con il solver.

### 7.5 Soluzione del solver

Controllare:

- successo dell'ottimizzazione;
- ammissibilità della soluzione;
- assenza di violazioni significative dei vincoli;
- coerenza tra variabili estratte e ordinamento utilizzato nel vettore del solver.

### 7.6 Expected Value

Verificare che:

1. $x^{EV}$ sia ottenuta dal problema costruito con i parametri medi;
2. nel calcolo di $z^{EV}$ la decisione $x^{EV}$ resti **fissa**;
3. per ciascuno scenario originale vengano riottimizzate soltanto le decisioni di ricorso.

### 7.7 Wait-and-see

Verificare che ogni problema WS utilizzi i dati di un solo scenario e consenta di scegliere una decisione iniziale scenario-specifica $x_s^{WS}$.

Controllare inoltre:

$$
z^{WS}
=
\sum_{s\in\mathcal S}p_sz_s^{WS}.
$$

### 7.8 Ordinamento dei benchmark

Verificare:

$$
z^{EV}
\leq
z^{SP}
\leq
z^{WS}.
$$

Verificare inoltre:

$$
VSS\geq0,
$$

$$
EVPI\geq0.
$$

Eventuali violazioni devono essere investigate prima di formulare l'interpretazione finale.

---

## 8. Ipotesi e limiti del caso

Il caso adotta le seguenti ipotesi e semplificazioni.

1. Il problema è **two-stage**: la decisione iniziale viene presa prima della rivelazione dell'incertezza e tutte le decisioni di ricorso vengono assunte dopo l'osservazione dello scenario completo.

2. Gli scenari $N$, $S$ ed $E$ sono mutuamente esclusivi ed esaustivi rispetto all'incertezza rappresentata nel modello.

3. Le probabilità degli scenari sono assegnate e non devono essere stimate.

4. La margin call è rappresentata mediante una relazione lineare:

$$
m_s=\alpha_sx_2.
$$

5. La capacità di trasformare il deleveraging in liquidità è lineare e rappresentata dal coefficiente $\beta_s$.

6. I costi della liquidità aggiuntiva e del deleveraging sono lineari.

7. I limiti $e_s\leq4$ e $f_s\leq25$ rappresentano capacità operative didattiche e non limiti storicamente osservati.

8. Il modello non rappresenta dinamiche intraday, collateral waterfall, haircut multipli, feedback endogeni sui prezzi dei gilt, derivati specifici, duration delle passività o requisiti regolamentari dettagliati.

9. Non sono presenti decisioni intermedie, alberi informativi multistadio o vincoli di non anticipatività tra nodi intermedi.

10. I parametri numerici sono stilizzati. Il caso è ispirato alla crisi LDI britannica del 2022, ma non costituisce una ricostruzione empirica di un singolo fondo o portafoglio.

11. I risultati devono essere interpretati esclusivamente all'interno del modello assegnato. In particolare, VSS ed EVPI misurano valori economici relativi alla specifica distribuzione degli scenari, ai costi e ai vincoli adottati.

12. L'interpretazione finale deve essere formulata dallo studente sulla base degli output effettivamente ottenuti nel notebook. L'IA può essere utilizzata soltanto per una revisione critica mirata secondo le istruzioni generali del corso.
