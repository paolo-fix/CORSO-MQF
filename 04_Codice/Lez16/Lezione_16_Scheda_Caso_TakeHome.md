# Lezione 16 — Scheda Caso TakeHome

## 1. Identificazione del caso

- **Lezione:** 16 — Applicazione in Python: programmazione stocastica
- **Tipo di caso:** TakeHome
- **Titolo:** *UK LDI 2022 — Buffer di liquidità, margin call e non anticipatività*
- **Contesto sintetico:** crisi delle strategie Liability Driven Investment (LDI) dei fondi pensione britannici nell'autunno 2022, utilizzata come riferimento finanziario per analizzare in forma stilizzata un problema multistadio con margin call, deleveraging, liquidità aggiuntiva e vincoli di non anticipatività.
- **Uso previsto:** lavoro autonomo successivo al Caso Aula, finalizzato a trasferire la programmazione stocastica da una struttura a due stadi a una struttura multistadio con informazione progressiva.

La presente Scheda Caso costituisce la **specifica vincolante del lavoro**. Variabili, scenari, parametri, formule, ipotesi, output e controlli indicati non devono essere modificati durante lo svolgimento.

La Scheda Caso definisce il problema ma **non ne contiene la soluzione**.

---

## 2. Contesto e domanda quantitativa

Le strategie Liability Driven Investment sono utilizzate da fondi pensione defined benefit per gestire l'esposizione delle passività a tassi di interesse e inflazione. Una parte di tali strategie può fare ricorso a leva mediante derivati sui tassi e operazioni repo su gilt.

Nel settembre 2022 il forte aumento dei rendimenti dei gilt generò richieste di collateral e margin call rilevanti. In presenza di risorse liquide insufficienti, alcuni investitori dovettero mobilitare liquidità aggiuntiva e ridurre rapidamente l'esposizione attraverso vendite o deleveraging. Il meccanismo risultò particolarmente critico perché le decisioni dovevano essere assunte progressivamente, man mano che l'informazione sul mercato diventava disponibile.

Il caso qui considerato non ricostruisce quantitativamente uno specifico fondo pensione o LDI fund. Utilizza invece una rappresentazione didattica stilizzata nella quale il decisore deve scegliere inizialmente come ripartire risorse tra:

1. un buffer di liquidità;
2. un'esposizione LDI.

Successivamente l'incertezza si rivela in due fasi.

Al primo stadio aleatorio si osserva uno dei due nodi:

- $M$: repricing moderato;
- $S$: repricing severo.

Dopo questa osservazione il decisore può:

- deleverare una parte della posizione;
- mobilitare liquidità aggiuntiva;
- conservare eventuale liquidità residua.

In seguito si osserva un secondo sviluppo del mercato:

- da $M$: $MR$ oppure $MP$;
- da $S$: $SR$ oppure $SS$.

Solo a quel punto possono essere assunte le decisioni terminali.

La domanda quantitativa è:

> **quale combinazione iniziale tra buffer di liquidità ed esposizione LDI massimizza il risultato economico atteso quando le margin call si manifestano progressivamente e le decisioni di adattamento devono rispettare l'informazione effettivamente disponibile? Quanto valore apparente si ottiene violando la non anticipatività e quanto varrebbe conoscere fin dall'inizio l'intero percorso futuro degli shock?**

Il caso utilizza i concetti sviluppati nei Capitoli 14 e 15 e richiede di distinguere chiaramente:

- decisioni iniziali;
- decisioni ai nodi intermedi;
- decisioni terminali;
- probabilità condizionate;
- probabilità dei percorsi;
- non anticipatività;
- soluzione multistadio;
- rilassamento anticipativo;
- wait-and-see;
- EVPI.

---

## 3. Modello e struttura del problema

### 3.1 Risorse iniziali e decisioni al tempo zero

Le risorse iniziali sono:

$$
A_0=100.
$$

La decisione iniziale è composta da:

$$
b\geq0,
$$

buffer di liquidità,

e:

$$
h\geq0,
$$

esposizione LDI.

Il vincolo sulle risorse è:

$$
b+h=100.
$$

Per preservare una funzione minima di copertura delle passività si impone:

$$
h\geq50.
$$

### 3.2 Redditività iniziale

Il rendimento unitario del buffer è:

$$
r_b=0.010,
$$

mentre quello dell'esposizione LDI è:

$$
r_h=0.045.
$$

Il rendimento iniziale complessivo è quindi:

$$
r_bb+r_hh.
$$

### 3.3 Primo stadio aleatorio

Il primo shock può condurre a:

- $M$: repricing moderato;
- $S$: repricing severo.

Le probabilità sono:

| Nodo | Probabilità |
|---|---:|
| $M$ | 0.65 |
| $S$ | 0.35 |

La prima margin call è proporzionale all'esposizione LDI iniziale:

$$
a_n h,
$$

con coefficienti:

| Nodo | $a_n$ |
|---|---:|
| $M$ | 0.10 |
| $S$ | 0.22 |

### 3.4 Decisioni al nodo intermedio

Dopo avere osservato $n\in\{M,S\}$ il decisore può scegliere:

$$
y_n\geq0,
$$

deleveraging intermedio,

$$
u_n\geq0,
$$

liquidità aggiuntiva mobilitata,

e:

$$
g_n\geq0,
$$

liquidità residua dopo avere soddisfatto la prima margin call.

Il bilancio di liquidità al nodo intermedio è:

$$
b+u_n+y_n
=
a_nh+g_n.
$$

I limiti operativi sono:

$$
0\leq y_n\leq25,
$$

$$
0\leq u_n\leq4.
$$

### 3.5 Secondo stadio aleatorio

Dal nodo $M$ possono verificarsi:

- $MR$: reversal/normalizzazione;
- $MP$: persistenza dello stress.

Le probabilità condizionate sono:

$$
\mathbb P(MR\mid M)=0.60,
$$

$$
\mathbb P(MP\mid M)=0.40.
$$

Dal nodo $S$ possono verificarsi:

- $SR$: stabilizzazione;
- $SS$: ulteriore stress.

Le probabilità condizionate sono:

$$
\mathbb P(SR\mid S)=0.45,
$$

$$
\mathbb P(SS\mid S)=0.55.
$$

Le probabilità dei quattro percorsi terminali sono:

| Percorso | Probabilità |
|---|---:|
| $MR$ | 0.3900 |
| $MP$ | 0.2600 |
| $SR$ | 0.1575 |
| $SS$ | 0.1925 |

Deve essere verificato:

$$
0.3900+0.2600+0.1575+0.1925=1.
$$

### 3.6 Decisioni terminali

Per ciascun percorso terminale $\ell$ si definiscono:

$$
z_\ell\geq0,
$$

ulteriore deleveraging,

$$
v_\ell\geq0,
$$

ulteriore liquidità mobilitata,

e:

$$
G_\ell\geq0,
$$

liquidità residua terminale.

La seconda margin call è proporzionale all'esposizione residua dopo il deleveraging intermedio:

$$
\beta_\ell
\left(
h-y_{n(\ell)}
\right),
$$

dove $n(\ell)$ indica il nodo padre del percorso terminale.

I coefficienti sono:

| Percorso | $\beta_\ell$ |
|---|---:|
| $MR$ | 0.00 |
| $MP$ | 0.10 |
| $SR$ | 0.05 |
| $SS$ | 0.20 |

Il bilancio terminale è:

$$
g_{n(\ell)}+v_\ell+z_\ell
=
\beta_\ell
\left(
h-y_{n(\ell)}
\right)
+
G_\ell.
$$

I limiti operativi sono:

$$
0\leq z_\ell\leq10,
$$

$$
0\leq v_\ell\leq4.
$$

Il deleveraging complessivo lungo ciascun percorso non può superare:

$$
y_{n(\ell)}+z_\ell\leq40.
$$

### 3.7 Struttura informativa

La struttura informativa del problema è:

$$
(b,h)
\longrightarrow
\{M,S\}
\longrightarrow
(y_n,u_n,g_n)
\longrightarrow
\{MR,MP,SR,SS\}
\longrightarrow
(z_\ell,v_\ell,G_\ell).
$$

Le decisioni iniziali $b$ e $h$ vengono prese prima di osservare qualsiasi shock.

Le decisioni $y_n,u_n,g_n$ possono dipendere dal nodo osservato $M$ o $S$, ma non dal successivo sviluppo del ramo.

Le decisioni terminali possono invece dipendere dall'intero percorso osservato.

### 3.8 Non anticipatività

Nel modello corretto devono valere:

$$
y_{MR}=y_{MP},
$$

$$
u_{MR}=u_{MP},
$$

$$
g_{MR}=g_{MP},
$$

e:

$$
y_{SR}=y_{SS},
$$

$$
u_{SR}=u_{SS},
$$

$$
g_{SR}=g_{SS}.
$$

Le decisioni iniziali devono inoltre essere comuni a tutti i percorsi:

$$
b_{MR}=b_{MP}=b_{SR}=b_{SS},
$$

$$
h_{MR}=h_{MP}=h_{SR}=h_{SS}.
$$

Nella formulazione a nodi queste uguaglianze possono essere incorporate direttamente usando una sola variabile per ciascun nodo.

### 3.9 Costi di adattamento

I costi unitari del deleveraging intermedio sono:

| Nodo | $\lambda_n$ |
|---|---:|
| $M$ | 0.025 |
| $S$ | 0.050 |

I costi unitari della liquidità aggiuntiva intermedia sono:

| Nodo | $\kappa_n$ |
|---|---:|
| $M$ | 0.020 |
| $S$ | 0.040 |

I costi unitari del deleveraging terminale sono:

| Percorso | $\mu_\ell$ |
|---|---:|
| $MR$ | 0.005 |
| $MP$ | 0.020 |
| $SR$ | 0.020 |
| $SS$ | 0.050 |

I costi unitari della liquidità aggiuntiva terminale sono:

| Percorso | $\eta_\ell$ |
|---|---:|
| $MR$ | 0.015 |
| $MP$ | 0.030 |
| $SR$ | 0.030 |
| $SS$ | 0.030 |

I coefficienti di costo rappresentano costi economici complessivi di aggiustamento, mobilitazione della liquidità e deleveraging. Non devono essere interpretati come spread o commissioni storicamente osservati.

### 3.10 Funzione obiettivo del problema multistadio

Il problema multistadio corretto massimizza:

$$
r_bb+r_hh
-
\sum_{n\in\{M,S\}}
p_n
\left(
\lambda_ny_n+\kappa_nu_n
\right)
-
\sum_{\ell}
p_\ell
\left(
\mu_\ell z_\ell+\eta_\ell v_\ell
\right).
$$

Il valore ottimo è indicato con:

$$
z^{MS}.
$$

---

## 4. Rilassamento anticipativo e wait-and-see

### 4.1 Rilassamento anticipativo

Per misurare l'effetto dei vincoli di non anticipatività deve essere costruito un secondo modello nel quale:

- $b$ e $h$ restano comuni a tutti i percorsi;
- le decisioni intermedie vengono rese, illegittimamente, specifiche del percorso terminale.

In particolare, vengono rimossi i vincoli che impongono l'uguaglianza delle decisioni intermedie tra percorsi con la stessa storia.

Il valore ottimo di questo problema è indicato con:

$$
z^{AR}.
$$

Deve risultare:

$$
z^{AR}\geq z^{MS}.
$$

La quantità:

$$
\Delta_{NA}
=
z^{AR}-z^{MS}
$$

misura il vantaggio artificiale prodotto dalla violazione della non anticipatività.

$\Delta_{NA}$ è una misura diagnostica e non deve essere confusa con VSS o EVPI.

### 4.2 Wait-and-see

Nel benchmark wait-and-see l'intero percorso terminale è noto già al tempo iniziale.

Per ciascun percorso $\ell$ viene quindi risolto un problema deterministico separato, ottenendo:

$$
z_\ell^{WS}.
$$

Il valore atteso con informazione perfetta è:

$$
z^{WS}
=
\sum_\ell p_\ell z_\ell^{WS}.
$$

Il valore atteso dell'informazione perfetta è:

$$
EVPI
=
z^{WS}-z^{MS}.
$$

Deve essere verificato:

$$
z^{MS}
\leq
z^{AR}
\leq
z^{WS}.
$$

---

## 5. Quantità da calcolare

### 5.1 Soluzione multistadio

Devono essere determinati:

1. il buffer iniziale:

$$
b^{MS};
$$

2. l'esposizione LDI iniziale:

$$
h^{MS};
$$

3. le decisioni ai nodi intermedi:

$$
y_M,\quad y_S,
$$

$$
u_M,\quad u_S,
$$

$$
g_M,\quad g_S;
$$

4. le decisioni terminali:

$$
z_\ell,\quad v_\ell,\quad G_\ell,
$$

per ciascuno dei quattro percorsi;

5. il valore:

$$
z^{MS}.
$$

### 5.2 Rilassamento anticipativo

Devono essere determinati:

1. il valore:

$$
z^{AR};
$$

2. le decisioni intermedie specifiche dei percorsi;
3. la differenza:

$$
\Delta_{NA}
=
z^{AR}-z^{MS}.
$$

### 5.3 Wait-and-see

Per ciascun percorso terminale devono essere determinati:

$$
z_\ell^{WS}.
$$

Deve quindi essere calcolato:

$$
z^{WS}
=
\sum_\ell p_\ell z_\ell^{WS},
$$

e infine:

$$
EVPI
=
z^{WS}-z^{MS}.
$$

---

## 6. Output richiesti

### 6.1 Tabelle

Produrre almeno le seguenti tabelle.

**Tabella 1 — Albero degli scenari e parametri**

Deve contenere:

- nodi e percorsi;
- probabilità dei nodi;
- probabilità condizionate;
- probabilità dei percorsi;
- coefficienti di margin call;
- costi di deleveraging;
- costi di liquidità aggiuntiva;
- limiti operativi.

**Tabella 2 — Soluzione multistadio**

Deve riportare:

- $b^{MS}$ e $h^{MS}$;
- decisioni ai nodi $M$ e $S$;
- decisioni terminali nei quattro percorsi;
- liquidità residua;
- costi di adattamento.

**Tabella 3 — Verifica della non anticipatività**

Deve confrontare le decisioni che devono coincidere sui percorsi con storia comune.

In particolare:

$$
MR\leftrightarrow MP
$$

per le decisioni assunte al nodo $M$,

e:

$$
SR\leftrightarrow SS
$$

per le decisioni assunte al nodo $S$.

**Tabella 4 — Confronto dei benchmark informativi**

Colonne:

- multistadio corretto;
- rilassamento anticipativo;
- wait-and-see.

Righe:

- informazione disponibile;
- decisione iniziale;
- principali decisioni di adattamento;
- valore obiettivo.

**Tabella 5 — Valore dell'informazione**

Deve contenere almeno:

$$
z^{MS},
\qquad
z^{AR},
\qquad
\Delta_{NA},
\qquad
z^{WS},
\qquad
EVPI.
$$

### 6.2 Grafici

Produrre almeno:

1. una rappresentazione dell'albero degli scenari con probabilità e coefficienti di margin call;
2. un grafico del deleveraging intermedio e terminale nei diversi nodi e percorsi;
3. un grafico di confronto tra modello multistadio corretto e rilassamento anticipativo, evidenziando le decisioni che differiscono quando la non anticipatività viene violata.

I grafici devono avere funzione interpretativa e devono essere accompagnati da titoli, etichette e unità coerenti.

### 6.3 Commento finale

Il notebook deve concludersi con un commento che distingua chiaramente:

- decisioni iniziali, intermedie e terminali;
- informazione disponibile ai diversi stadi;
- non anticipatività;
- soluzione multistadio;
- rilassamento anticipativo;
- wait-and-see;
- $\Delta_{NA}$;
- EVPI.

Il commento deve inoltre spiegare il ruolo del buffer iniziale, del deleveraging e della liquidità aggiuntiva nella gestione dello stress.

---

## 7. Controlli richiesti

Il notebook deve verificare esplicitamente che:

1. le probabilità dei nodi iniziali soddisfino:

$$
p_M+p_S=1;
$$

2. le probabilità condizionate di ciascun nodo sommino a uno;

3. le probabilità dei quattro percorsi soddisfino:

$$
\sum_\ell p_\ell=1;
$$

4. sia rispettato:

$$
b+h=100;
$$

5. sia rispettato:

$$
h\geq50;
$$

6. siano rispettati:

$$
0\leq y_n\leq25;
$$

7. siano rispettati:

$$
0\leq u_n\leq4;
$$

8. siano rispettati:

$$
0\leq z_\ell\leq10;
$$

9. siano rispettati:

$$
0\leq v_\ell\leq4;
$$

10. sia rispettato:

$$
y_{n(\ell)}+z_\ell\leq40;
$$

11. per ogni nodo intermedio sia verificato:

$$
b+u_n+y_n
=
a_nh+g_n;
$$

12. per ogni percorso terminale sia verificato:

$$
g_{n(\ell)}+v_\ell+z_\ell
=
\beta_\ell
\left(
h-y_{n(\ell)}
\right)
+
G_\ell;
$$

13. tutte le variabili soggette a non negatività rispettino il vincolo;

14. il solver restituisca una soluzione ottima;

15. nel modello multistadio corretto siano rispettati i vincoli di non anticipatività;

16. nel rilassamento anticipativo $b$ e $h$ rimangano comunque comuni a tutti i percorsi;

17. sia verificato:

$$
z^{AR}\geq z^{MS};
$$

18. sia verificato:

$$
z^{WS}\geq z^{AR};
$$

19. sia verificato:

$$
EVPI\geq0.
$$

Devono inoltre rimanere distinti:

- probabilità dei nodi;
- probabilità condizionate;
- probabilità dei percorsi;
- deleveraging intermedio;
- deleveraging terminale;
- liquidità aggiuntiva;
- liquidità residua;
- costo di deleveraging;
- costo della liquidità aggiuntiva.

---

## 8. Ipotesi e limiti del caso

Ai fini di questa applicazione si assume che:

1. l'albero degli scenari sia discreto;
2. tutte le probabilità siano note al tempo iniziale;
3. $b$ e $h$ vengano scelti prima di osservare qualsiasi shock;
4. le decisioni al nodo $M$ possano dipendere dall'osservazione di $M$, ma non dal successivo verificarsi di $MR$ o $MP$;
5. le decisioni al nodo $S$ possano dipendere dall'osservazione di $S$, ma non dal successivo verificarsi di $SR$ o $SS$;
6. le decisioni terminali possano dipendere dall'intero percorso osservato;
7. una unità di deleveraging generi una unità di liquidità;
8. i costi economici associati al deleveraging siano rappresentati separatamente;
9. la liquidità aggiuntiva mobilitabile sia limitata;
10. il deleveraging terminale sia soggetto a capacità limitata;
11. tutti i parametri siano esogeni;
12. tutte le quantità monetarie siano espresse in unità convenzionali su scala $A_0=100$.

Sono deliberatamente esclusi:

- ricostruzione quantitativa di uno specifico fondo pensione o LDI fund;
- prezzi dei gilt modellati esplicitamente;
- duration e convexity;
- distinzione tra derivati sui tassi, repo e gilt fisici;
- haircuts contrattuali reali;
- dinamiche endogene di fire sale;
- feedback tra vendite e prezzi di mercato;
- intervento della Bank of England come decisione endogena;
- costi non lineari;
- alberi con un numero elevato di nodi.

Il caso è quindi un modello didattico di programmazione stocastica multistadio con informazione progressiva e vincoli di non anticipatività.

I risultati non devono essere interpretati come ricostruzione storica della crisi LDI britannica né come raccomandazione operativa per un fondo pensione reale.
