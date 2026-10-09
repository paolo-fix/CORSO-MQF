# Lezione 16 — Scheda Caso Aula

## 1. Identificazione del caso

- **Lezione:** 16 — Applicazione in Python: programmazione stocastica
- **Tipo di caso:** aula
- **Titolo:** *SVB–ALM 2023 — Asset allocation, liquidità e valore dell'informazione*
- **Contesto sintetico:** crisi di Silicon Valley Bank del marzo 2023, utilizzata come riferimento finanziario per analizzare in forma stilizzata una decisione di asset allocation sotto incertezza, con fabbisogni di liquidità e costi di funding dipendenti dallo scenario.
- **Uso previsto:** sviluppo guidato in aula di un programma stocastico lineare a due stadi, con confronto tra soluzione stocastica, Expected Value e wait-and-see.

La presente Scheda Caso costituisce la **specifica vincolante del lavoro**. Variabili, scenari, parametri, formule, ipotesi, output e controlli indicati non devono essere modificati durante lo svolgimento.

La Scheda Caso definisce il problema ma **non ne contiene la soluzione**.

---

## 2. Contesto e domanda quantitativa

Silicon Valley Bank operava con una struttura dell'attivo caratterizzata da una quota rilevante di attività a più lunga durata e con una raccolta fortemente concentrata. Il rapido aumento dei tassi di interesse e i successivi deflussi dei depositi resero centrale il problema della capacità di trasformare l'attivo in liquidità e di reperire funding aggiuntivo in condizioni di stress.

Il caso qui considerato non ricostruisce quantitativamente il bilancio storico di SVB. Utilizza invece una rappresentazione didattica stilizzata nella quale una banca deve scegliere, prima di conoscere lo scenario futuro, la composizione iniziale dell'attivo tra quattro classi:

1. cassa e riserve;
2. titoli a breve scadenza;
3. titoli a lunga scadenza;
4. prestiti e impieghi meno liquidi.

Dopo la scelta iniziale può verificarsi uno dei tre scenari:

- $N$: condizioni normali;
- $P$: pressione sulla raccolta;
- $R$: run severo.

Ogni scenario modifica:

1. il fabbisogno di liquidità;
2. la quota dei diversi attivi trasformabile in liquidità;
3. il costo economico del funding di emergenza.

La decisione iniziale deve essere unica e comune a tutti gli scenari. Solo dopo avere osservato lo scenario la banca può adattarsi mediante il ricorso a funding di emergenza e la gestione dell'eventuale liquidità residua.

La domanda quantitativa è:

> **quale composizione iniziale dell'attivo massimizza il risultato economico atteso della banca quando fabbisogni di liquidità, liquidabilità degli attivi e costo del funding dipendono dallo scenario futuro, e quanto valgono rispettivamente l'uso della programmazione stocastica e l'informazione perfetta sullo scenario futuro?**

Il caso utilizza i concetti sviluppati nei Capitoli 14 e 15 e richiede di distinguere chiaramente:

- decisione ex ante;
- decisioni di ricorso;
- soluzione stocastica;
- soluzione Expected Value;
- rivalutazione della soluzione Expected Value;
- wait-and-see;
- VSS;
- EVPI.

---

## 3. Modello e struttura del problema

### 3.1 Risorse iniziali e decisione di primo stadio

La banca dispone al tempo iniziale di risorse complessive pari a

$$
A_0=100.
$$

La decisione iniziale è

$$
x=(x_1,x_2,x_3,x_4)',
$$

dove:

1. $x_1$: cassa e riserve;
2. $x_2$: titoli a breve scadenza;
3. $x_3$: titoli a lunga scadenza;
4. $x_4$: prestiti e impieghi meno liquidi.

Il vincolo sulle risorse iniziali è

$$
x_1+x_2+x_3+x_4=100.
$$

Le variabili devono soddisfare:

$$
x_j\geq0,
\qquad
j=1,\ldots,4.
$$

Sono inoltre imposti i limiti:

$$
x_3\leq70,
$$

$$
x_4\leq70.
$$

### 3.2 Redditività iniziale degli attivi

A ciascuna classe di attivo è associato un rendimento unitario $c_j$.

Il rendimento iniziale complessivo è:

$$
c'x
=
\sum_{j=1}^{4}c_jx_j.
$$

### 3.3 Scenari

L'insieme degli scenari è

$$
\mathcal S=\{N,P,R\}.
$$

Le probabilità sono indicate con $p_s$ e devono soddisfare:

$$
\sum_{s\in\mathcal S}p_s=1.
$$

La decisione $x$ viene assunta **prima** di conoscere quale scenario si realizzerà.

### 3.4 Liquidità generata dagli attivi

Il coefficiente

$$
\alpha_{js}
$$

rappresenta la quota dell'investimento nell'attivo $j$ trasformabile in liquidità nello scenario $s$.

La liquidità complessivamente ottenibile dagli attivi nello scenario $s$ è quindi:

$$
\sum_{j=1}^{4}\alpha_{js}x_j.
$$

Il coefficiente $\alpha_{js}$ è un coefficiente di liquidabilità e **non** un rendimento.

### 3.5 Decisioni di ricorso

Dopo avere osservato lo scenario $s$, la banca può utilizzare:

$$
u_s\geq0,
$$

dove $u_s$ rappresenta il funding di emergenza;

e:

$$
g_s\geq0,
$$

dove $g_s$ rappresenta la liquidità residua dopo avere soddisfatto il fabbisogno dello scenario.

Il bilancio di liquidità nello scenario $s$ è:

$$
\sum_{j=1}^{4}\alpha_{js}x_j+u_s
=
d_s+g_s.
$$

La struttura informativa del problema è pertanto:

$$
x
\longrightarrow
s
\longrightarrow
(u_s,g_s).
$$

La decisione $x$ deve essere la stessa in tutti gli scenari.

### 3.6 Funzione obiettivo

Il costo economico unitario del funding di emergenza nello scenario $s$ è indicato con

$$
\kappa_s.
$$

La banca massimizza il rendimento iniziale degli attivi al netto del costo atteso del funding:

$$
\max
\left\{
\sum_{j=1}^{4}c_jx_j
-
\sum_{s\in\mathcal S}
p_s\kappa_su_s
\right\}.
$$

La soluzione ottima del programma stocastico è indicata con

$$
x^{SP},
$$

e il corrispondente valore ottimo con

$$
z^{SP}.
$$

### 3.7 Expected Value problem

Per costruire il problema Expected Value devono essere calcolati i parametri medi:

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

Il problema deterministico costruito su tali valori medi produce una decisione:

$$
x^{EV}.
$$

La decisione $x^{EV}$ deve successivamente essere **fissata** e rivalutata nei tre scenari originari.

Il valore atteso così ottenuto è indicato con:

$$
z^{EEV}.
$$

Non è ammesso riottimizzare $x^{EV}$ separatamente nei tre scenari.

Il valore della soluzione stocastica è:

$$
VSS
=
z^{SP}-z^{EEV}.
$$

### 3.8 Wait-and-see

Nel benchmark wait-and-see si assume che lo scenario futuro sia noto prima della decisione iniziale.

Per ciascuno scenario $s$ viene quindi risolto un problema distinto, ottenendo:

$$
x_s^{WS}
$$

e:

$$
z_s^{WS}.
$$

Il valore atteso wait-and-see è:

$$
z^{WS}
=
\sum_s p_sz_s^{WS}.
$$

Il valore atteso dell'informazione perfetta è:

$$
EVPI
=
z^{WS}-z^{SP}.
$$

Per un problema di massimizzazione devono essere verificate le relazioni:

$$
VSS\geq0,
$$

$$
EVPI\geq0,
$$

e:

$$
z^{EEV}\leq z^{SP}\leq z^{WS}.
$$

---

## 4. Parametri assegnati

I parametri sono stilizzati e hanno funzione didattica. Non costituiscono una ricostruzione dei valori storicamente osservati in Silicon Valley Bank.

### 4.1 Risorse iniziali

$$
A_0=100.
$$

### 4.2 Rendimenti unitari

| Attivo | Descrizione | $c_j$ |
|---|---|---:|
| $x_1$ | Cassa e riserve | 0.010 |
| $x_2$ | Titoli a breve scadenza | 0.025 |
| $x_3$ | Titoli a lunga scadenza | 0.040 |
| $x_4$ | Prestiti e impieghi meno liquidi | 0.050 |

### 4.3 Probabilità degli scenari

| Scenario | Descrizione | $p_s$ |
|---|---|---:|
| $N$ | Condizioni normali | 0.60 |
| $P$ | Pressione sulla raccolta | 0.25 |
| $R$ | Run severo | 0.15 |

### 4.4 Fabbisogni di liquidità

| Scenario | $d_s$ |
|---|---:|
| $N$ | 15 |
| $P$ | 35 |
| $R$ | 65 |

### 4.5 Coefficienti di liquidabilità

| Attivo | $N$ | $P$ | $R$ |
|---|---:|---:|---:|
| Cassa e riserve $x_1$ | 1.00 | 1.00 | 1.00 |
| Titoli a breve $x_2$ | 0.98 | 0.95 | 0.90 |
| Titoli a lunga $x_3$ | 0.85 | 0.70 | 0.50 |
| Prestiti e impieghi $x_4$ | 0.60 | 0.40 | 0.20 |

### 4.6 Costi unitari del funding di emergenza

| Scenario | $\kappa_s$ |
|---|---:|
| $N$ | 0.01 |
| $P$ | 0.06 |
| $R$ | 0.25 |

Il parametro $\kappa_s$ rappresenta un costo economico complessivo del ricorso alla liquidità di emergenza nello scenario e non deve essere interpretato come semplice tasso di interesse di mercato.

### 4.7 Limiti sulle allocazioni

$$
x_3\leq70,
$$

$$
x_4\leq70.
$$

---

## 5. Quantità da calcolare

### 5.1 Soluzione stocastica

Devono essere determinati:

1. il vettore ottimo:

$$
x^{SP};
$$

2. le decisioni di ricorso:

$$
u_s^{SP},
\qquad
g_s^{SP},
\qquad
s\in\{N,P,R\};
$$

3. il rendimento iniziale lordo:

$$
c'x^{SP};
$$

4. il costo atteso del funding:

$$
\sum_s p_s\kappa_su_s^{SP};
$$

5. il valore ottimo:

$$
z^{SP}.
$$

### 5.2 Expected Value ed EEV

Devono essere calcolati:

1. $\bar d$;
2. $\bar\alpha_j$ per $j=1,\ldots,4$;
3. $\bar\kappa$;
4. la soluzione:

$$
x^{EV};
$$

5. le decisioni di ricorso necessarie quando $x^{EV}$ viene rivalutata nei tre scenari originali;
6. il valore:

$$
z^{EEV};
$$

7. il valore della soluzione stocastica:

$$
VSS
=
z^{SP}-z^{EEV}.
$$

### 5.3 Wait-and-see ed EVPI

Per ciascuno scenario devono essere determinati:

$$
x_s^{WS}
$$

e:

$$
z_s^{WS}.
$$

Deve quindi essere calcolato:

$$
z^{WS}
=
\sum_s p_sz_s^{WS},
$$

e infine:

$$
EVPI
=
z^{WS}-z^{SP}.
$$

---

## 6. Output richiesti

### 6.1 Tabelle

Produrre almeno le seguenti tabelle.

**Tabella 1 — Parametri del problema**

Deve contenere:

- rendimenti unitari;
- probabilità degli scenari;
- fabbisogni di liquidità;
- coefficienti di liquidabilità;
- costi del funding;
- limiti sulle allocazioni.

**Tabella 2 — Soluzione stocastica**

Deve riportare:

- $x_j^{SP}$;
- liquidità ottenibile dagli attivi in ciascuno scenario;
- $u_s^{SP}$;
- $g_s^{SP}$;
- costo del funding per scenario.

**Tabella 3 — Expected Value e rivalutazione**

Deve riportare:

- $x^{EV}$;
- parametri medi utilizzati;
- funding necessario nei tre scenari originari;
- valore $z^{EEV}$;
- confronto con $x^{SP}$.

**Tabella 4 — Wait-and-see**

Per ciascuno scenario deve riportare:

- $x_s^{WS}$;
- $z_s^{WS}$.

**Tabella 5 — Valore dell'informazione**

Deve contenere almeno:

$$
z^{EEV},
\qquad
z^{SP},
\qquad
z^{WS},
\qquad
VSS,
\qquad
EVPI.
$$

### 6.2 Grafici

Produrre almeno:

1. un grafico a barre affiancate che confronti:

$$
x^{SP}
\quad\text{e}\quad
x^{EV};
$$

2. un grafico a barre del funding richiesto nei tre scenari sotto:

$$
x^{SP}
$$

e:

$$
x^{EV}.
$$

I grafici devono essere accompagnati da titoli, etichette e unità coerenti e devono avere funzione interpretativa.

### 6.3 Commento finale

Il notebook deve concludersi con un commento che distingua chiaramente:

- la soluzione stocastica dalla soluzione Expected Value;
- il problema EV dal valore EEV;
- il VSS dall'EVPI;
- la decisione implementabile ex ante dal benchmark wait-and-see;
- il trade-off tra rendimento iniziale e capacità di affrontare gli scenari di stress.

---

## 7. Controlli richiesti

Il notebook deve verificare esplicitamente che:

1. le probabilità soddisfino:

$$
\sum_s p_s=1;
$$

2. la soluzione rispetti:

$$
\sum_jx_j=100;
$$

3. siano rispettati:

$$
x_j\geq0;
$$

4. siano rispettati i limiti:

$$
x_3\leq70,
\qquad
x_4\leq70;
$$

5. per ogni scenario sia verificato il bilancio:

$$
\sum_{j=1}^{4}\alpha_{js}x_j+u_s
=
d_s+g_s;
$$

6. valgano:

$$
u_s\geq0,
\qquad
g_s\geq0;
$$

7. il solver restituisca una soluzione ottima;

8. la stessa decisione $x^{SP}$ sia utilizzata in tutti gli scenari;

9. la decisione $x^{EV}$ venga rivalutata nei tre scenari senza essere riottimizzata scenario per scenario;

10. nel wait-and-see i tre problemi vengano effettivamente risolti separatamente;

11. sia verificato:

$$
VSS\geq0;
$$

12. sia verificato:

$$
EVPI\geq0;
$$

13. sia verificato l'ordinamento:

$$
z^{EEV}
\leq
z^{SP}
\leq
z^{WS}.
$$

Devono inoltre rimanere distinti:

- i rendimenti $c_j$;
- i coefficienti di liquidabilità $\alpha_{js}$;
- i fabbisogni $d_s$;
- il funding $u_s$;
- la liquidità residua $g_s$;
- il costo unitario del funding $\kappa_s$.

---

## 8. Ipotesi e limiti del caso

Ai fini di questa applicazione si assume che:

1. gli scenari $N$, $P$ e $R$ siano mutuamente esclusivi ed esaustivi;
2. le probabilità degli scenari siano note al tempo iniziale;
3. la composizione iniziale dell'attivo venga scelta prima della rivelazione dello scenario;
4. solo $u_s$ e $g_s$ possano adattarsi allo scenario osservato;
5. il funding di emergenza sia disponibile senza limite quantitativo;
6. il costo del funding sia lineare;
7. rendimenti, fabbisogni, coefficienti di liquidabilità e costi siano esogeni;
8. tutte le quantità monetarie siano espresse in unità convenzionali su scala $A_0=100$.

Sono deliberatamente esclusi:

- ricostruzione quantitativa del bilancio storico di SVB;
- dinamica endogena dei deposit run;
- capitale regolamentare e insolvenza;
- distinzione contabile tra HTM e AFS;
- duration e mark-to-market espliciti;
- retroazioni tra decisioni della banca e probabilità degli scenari;
- interventi della Federal Reserve o della FDIC;
- costi non lineari del funding;
- più stadi di rivelazione progressiva dell'informazione.

Il caso è quindi un modello didattico di programmazione stocastica a due stadi applicata a un problema di asset allocation e liquidità bancaria.

I risultati non devono essere interpretati come ricostruzione storica di Silicon Valley Bank né come raccomandazione operativa di gestione bancaria.
