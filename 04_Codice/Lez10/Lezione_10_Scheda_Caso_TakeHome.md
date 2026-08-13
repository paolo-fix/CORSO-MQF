# Lezione 10 — Scheda Caso Take-home

## 1. Identificazione del caso

- **Lezione:** 10 — Applicazione in Python: rischio di credito
- **Tipo di caso:** take-home
- **Titolo:** Lehman Brothers 2008: rischio sistemico, migrazioni creditizie e perdita di portafoglio
- **Contesto sintetico:** giugno 2008, fase di crescente tensione del sistema finanziario internazionale e di deterioramento del merito creditizio di Lehman Brothers.
- **Uso previsto:** lavoro autonomo take-home per sviluppare, mediante simulazione Monte Carlo, un modello di rischio creditizio di portafoglio nel quale le migrazioni dei singoli debitori dipendono da un regime sistemico comune che evolve nel tempo.

La presente Scheda Caso costituisce la **specifica vincolante del lavoro**. Variabili, stati, parametri, formule, ipotesi, output e controlli indicati non devono essere modificati durante lo svolgimento.

La Scheda Caso definisce il problema ma **non ne contiene la soluzione**.

---

## 2. Contesto e domanda quantitativa

Si considera, nel giugno 2008, un portafoglio di esposizioni creditizie verso 40 debitori appartenenti a differenti classi di rating. Una delle posizioni, identificata con Lehman Brothers, presenta un investimento iniziale significativamente superiore a quello delle singole altre posizioni.

Il rischio creditizio dipende da due componenti:

1. l'evoluzione individuale del rating dei singoli debitori;
2. un regime sistemico comune che rappresenta le condizioni generali del sistema finanziario.

Il regime sistemico può trovarsi in tre stati:

- $O$: condizioni ordinarie;
- $S$: stress finanziario;
- $C$: crisi.

Il regime evolve trimestralmente secondo una catena di Markov. La matrice di migrazione creditizia applicata a ciascun debitore dipende dal regime sistemico corrente.

Condizionatamente alla traiettoria del regime comune, le migrazioni dei differenti debitori sono assunte indipendenti. Incondizionatamente, le perdite risultano invece dipendenti perché tutti i debitori sono esposti alla medesima evoluzione sistemica.

Il caso comprende inoltre un confronto controfattuale. La posizione Lehman viene eliminata e il relativo investimento iniziale viene redistribuito proporzionalmente tra gli altri 39 debitori, mantenendo invariato l'investimento complessivo del portafoglio.

La domanda quantitativa è:

**quale distribuzione della perdita a un anno produce il portafoglio concentrato e come cambiano perdita attesa, dispersione, VaR e CVaR quando l'investimento inizialmente concentrato su Lehman Brothers viene riallocato proporzionalmente tra gli altri debitori, a investimento complessivo invariato?**

---

## 3. Modello e struttura del problema

### 3.1 Regime sistemico

Si considera il processo

$$
\{M_t\}_{t=0}^{3},
$$

con

$$
M_t\in\{O,S,C\}.
$$

Il regime iniziale è

$$
M_0=S.
$$

Le probabilità di transizione sono descritte dalla matrice $Q$ riportata nella Sezione 4.

### 3.2 Stati creditizi

Per ogni debitore $i$, il rating evolve secondo

$$
\{X_{i,t}\}_{t=0}^{4},
$$

con spazio degli stati

$$
\mathcal{I}
=
\{A,BBB,BB,B,D\}.
$$

Lo stato $D$ rappresenta il default ed è assorbente.

Per ogni trimestre:

$$
\Pr
\left(
X_{i,t+1}=j
\mid
X_{i,t}=k,M_t=m
\right)
=
p_{kj}^{(m)}.
$$

La matrice utilizzata per la transizione dipende quindi dal regime corrente:

$$
P^{(O)},\qquad
P^{(S)},\qquad
P^{(C)}.
$$

### 3.3 Dipendenza tra i debitori

Condizionatamente alla traiettoria

$$
M_0,M_1,M_2,M_3,
$$

le migrazioni dei differenti debitori sono indipendenti.

Il regime sistemico è invece comune all'intero portafoglio. Una traiettoria che permane o entra nello stato $C$ applica simultaneamente matrici di migrazione più sfavorevoli a tutti i debitori.

### 3.4 Perdita individuale

Per ogni debitore la perdita dipende dal rating iniziale, dal rating finale e dall'investimento iniziale:

$$
L_i
=
V_{i,0}\,
\ell(X_{i,0},X_{i,4}),
$$

dove $V_{i,0}$ è l'investimento iniziale e $\ell(r_0,r_4)$ è il tasso di perdita assegnato alla migrazione dal rating iniziale $r_0$ al rating finale $r_4$.

Il default è incluso direttamente nella funzione $\ell$. In particolare,

$$
\ell(r_0,D)=0.65.
$$

Nel caso didattico si assume:

$$
\mathrm{EAD}_i=V_{i,0},
$$

e

$$
\mathrm{LGD}=0.65.
$$

Questa uguaglianza tra EAD e investimento iniziale costituisce una semplificazione specifica del caso e non una identificazione generale tra i due concetti.

Poiché $D$ è assorbente e la LGD è costante, la perdita da default dipende dallo stato terminale $X_{i,4}=D$ e non dal trimestre nel quale il default si è verificato.

### 3.5 Perdite dei due portafogli

Per la replica Monte Carlo $r$, la perdita del portafoglio concentrato è

$$
L_{\mathrm{conc}}^{P,(r)}
=
\sum_{i=1}^{40}
L_i^{(r)}.
$$

Nel portafoglio controfattuale Lehman è eliminata e gli investimenti dei 39 debitori residui vengono riallocati secondo la regola assegnata. La perdita è

$$
L_{\mathrm{div}}^{P,(r)}
=
\sum_{i\neq L}
V_{i,0}^{\mathrm{div}}
\ell
\left(
X_{i,0},
X_{i,4}^{(r)}
\right).
$$

Il confronto deve essere effettuato utilizzando **gli stessi scenari Monte Carlo sottostanti**:

- la stessa traiettoria sistemica per i due portafogli;
- le stesse traiettorie creditizie per i 39 debitori comuni;
- la traiettoria Lehman soltanto nel portafoglio concentrato.

---

## 4. Parametri assegnati

### 4.1 Matrice di transizione del regime sistemico

L'ordine degli stati è

$$
(O,S,C).
$$

La matrice trimestrale è

$$
Q=
\begin{pmatrix}
0.82 & 0.16 & 0.02\\
0.30 & 0.55 & 0.15\\
0.10 & 0.35 & 0.55
\end{pmatrix}.
$$

### 4.2 Matrici di migrazione creditizia

L'ordine degli stati creditizi è

$$
(A,BBB,BB,B,D).
$$

Nel regime ordinario:

$$
P^{(O)}
=
\begin{pmatrix}
0.960 & 0.035 & 0.004 & 0.0005 & 0.0005\\
0.020 & 0.940 & 0.030 & 0.0070 & 0.0030\\
0.004 & 0.030 & 0.910 & 0.0460 & 0.0100\\
0.001 & 0.004 & 0.025 & 0.9400 & 0.0300\\
0     & 0     & 0     & 0      & 1
\end{pmatrix}.
$$

Nel regime di stress:

$$
P^{(S)}
=
\begin{pmatrix}
0.920 & 0.060 & 0.014 & 0.004 & 0.002\\
0.010 & 0.870 & 0.085 & 0.027 & 0.008\\
0.002 & 0.018 & 0.820 & 0.135 & 0.025\\
0     & 0.002 & 0.018 & 0.880 & 0.100\\
0     & 0     & 0     & 0     & 1
\end{pmatrix}.
$$

Nel regime di crisi:

$$
P^{(C)}
=
\begin{pmatrix}
0.820 & 0.120 & 0.040 & 0.015 & 0.005\\
0.005 & 0.760 & 0.150 & 0.060 & 0.025\\
0     & 0.010 & 0.680 & 0.230 & 0.080\\
0     & 0.001 & 0.009 & 0.740 & 0.250\\
0     & 0     & 0     & 0     & 1
\end{pmatrix}.
$$

### 4.3 Portafoglio iniziale concentrato

Gli importi sono espressi in milioni di dollari.

| Gruppo | Numero debitori | Rating iniziale | Investimento per debitore | Investimento complessivo |
|---|---:|:---:|---:|---:|
| Lehman Brothers | 1 | A | 25 | 25 |
| Altri debitori A | 11 | A | 5 | 55 |
| Debitori BBB | 14 | BBB | 4 | 56 |
| Debitori BB | 9 | BB | 3 | 27 |
| Debitori B | 5 | B | 2 | 10 |
| **Totale** | **40** |  |  | **173** |

### 4.4 Portafoglio controfattuale

La posizione Lehman viene eliminata.

L'investimento iniziale dei restanti 39 debitori è complessivamente

$$
148.
$$

I $25$ milioni precedentemente investiti in Lehman vengono redistribuiti mantenendo inalterate le proporzioni relative degli investimenti residui.

Per ogni debitore $i\neq L$:

$$
V_{i,0}^{\mathrm{div}}
=
V_{i,0}
+
25\frac{V_{i,0}}{148}
=
V_{i,0}\frac{173}{148}.
$$

Il fattore di riscalamento è

$$
\frac{173}{148}
\approx
1.168919.
$$

Il portafoglio controfattuale è:

| Gruppo | Numero debitori | Rating iniziale | Investimento per debitore | Investimento complessivo |
|---|---:|:---:|---:|---:|
| Altri debitori A | 11 | A | 5.8446 | 64.2905 |
| Debitori BBB | 14 | BBB | 4.6757 | 65.4595 |
| Debitori BB | 9 | BB | 3.5068 | 31.5608 |
| Debitori B | 5 | B | 2.3378 | 11.6892 |
| **Totale** | **39** |  |  | **173.0000** |

Pertanto:

$$
V_0^{P,\mathrm{conc}}
=
V_0^{P,\mathrm{div}}
=
173.
$$

La riallocazione modifica anche la distribuzione dell'investimento tra classi di rating. Il confronto non identifica quindi un effetto puro della sola concentrazione, ma l'effetto della specifica strategia controfattuale assegnata.

### 4.5 Tassi di perdita migration-based

| Rating iniziale $\backslash$ finale | A | BBB | BB | B | D |
|---|---:|---:|---:|---:|---:|
| A | 0.00 | 0.03 | 0.10 | 0.22 | 0.65 |
| BBB | -0.02 | 0.00 | 0.06 | 0.16 | 0.65 |
| BB | -0.04 | -0.02 | 0.00 | 0.09 | 0.65 |
| B | -0.06 | -0.04 | -0.02 | 0.00 | 0.65 |

I valori negativi rappresentano incrementi di valore rispetto al riferimento iniziale prodotti da un miglioramento del rating.

### 4.6 Parametri computazionali

Numero di repliche Monte Carlo:

$$
N=50\,000.
$$

Seed:

$$
2026.
$$

Orizzonte:

$$
T=4
$$

trimestri, pari a un anno.

---

## 5. Quantità da stimare o calcolare

Per il portafoglio concentrato e per il portafoglio controfattuale devono essere determinate:

1. la perdita media

$$
\mathbb{E}[L^P];
$$

2. la varianza

$$
\operatorname{Var}(L^P);
$$

3. la deviazione standard;

4. il Value at Risk ai livelli $95\%$ e $99\%$:

$$
\operatorname{VaR}_{0.95}(L^P),
\qquad
\operatorname{VaR}_{0.99}(L^P);
$$

5. il Conditional Value at Risk ai livelli $95\%$ e $99\%$:

$$
\operatorname{CVaR}_{0.95}(L^P),
\qquad
\operatorname{CVaR}_{0.99}(L^P).
$$

Devono inoltre essere determinate:

6. la probabilità che il regime $C$ venga raggiunto almeno una volta durante l'orizzonte;

7. la perdita media del portafoglio concentrato:
   - negli scenari nei quali il regime $C$ viene raggiunto almeno una volta;
   - negli scenari nei quali il regime $C$ non viene mai raggiunto;

8. per ciascuna misura di rischio $\rho$, la variazione

$$
\Delta\rho
=
\rho(L_{\mathrm{div}}^P)
-
\rho(L_{\mathrm{conc}}^P);
$$

9. la differenza scenario per scenario

$$
\Delta L^{(r)}
=
L_{\mathrm{div}}^{P,(r)}
-
L_{\mathrm{conc}}^{P,(r)}.
$$

Il CVaR deve essere calcolato secondo la definizione mediante quantili adottata nel Capitolo 9.

---

## 6. Output richiesti

### 6.1 Risultati numerici

Per entrambi i portafogli devono essere riportati:

- distribuzione simulata della perdita;
- perdita media;
- varianza;
- deviazione standard;
- VaR 95%;
- CVaR 95%;
- VaR 99%;
- CVaR 99%.

Devono inoltre essere riportati:

- differenze tra le misure di rischio dei due portafogli;
- probabilità simulata che il regime $C$ venga raggiunto almeno una volta;
- perdita media del portafoglio concentrato negli scenari con e senza ingresso nello stato $C$;
- distribuzione empirica di

$$
\Delta L^{(r)}
=
L_{\mathrm{div}}^{P,(r)}
-
L_{\mathrm{conc}}^{P,(r)}.
$$

### 6.2 Tabelle

**Tabella 1 — Portafoglio iniziale concentrato**

Rating iniziale, numero di debitori, investimento individuale e investimento complessivo.

**Tabella 2 — Portafoglio controfattuale**

Rating iniziale, numero di debitori, investimento individuale riallocato e investimento complessivo.

**Tabella 3 — Misure di rischio**

Confronto tra:

- portafoglio concentrato;
- portafoglio con riallocazione proporzionale;
- differenza tra le rispettive misure.

**Tabella 4 — Regime sistemico e perdita**

Confronto, per il portafoglio concentrato, tra scenari con e senza ingresso nello stato $C$.

### 6.3 Grafici

**Figura 1 — Distribuzione della perdita del portafoglio concentrato**

Distribuzione empirica di $L_{\mathrm{conc}}^P$ con indicazione di VaR 95% e VaR 99%.

**Figura 2 — Confronto delle distribuzioni**

Confronto tra le distribuzioni empiriche delle perdite del portafoglio concentrato e del portafoglio controfattuale, con particolare attenzione alla coda destra.

**Figura 3 — Regime sistemico e perdita**

Confronto delle perdite del portafoglio concentrato tra scenari nei quali lo stato $C$ viene raggiunto almeno una volta e scenari nei quali non viene mai raggiunto.

---

## 7. Controlli richiesti

Devono essere verificati almeno i seguenti punti.

1. Ogni riga di $Q$ deve sommare a uno.

2. Ogni riga di $P^{(O)}$, $P^{(S)}$ e $P^{(C)}$ deve sommare a uno.

3. Lo stato $D$ deve risultare assorbente in tutte le matrici di migrazione.

4. Tutti gli stati simulati devono appartenere agli insiemi previsti.

5. All'interno della stessa replica deve esistere una sola traiettoria sistemica, comune a tutti i debitori.

6. Condizionatamente alla traiettoria sistemica comune, i debitori devono utilizzare estrazioni casuali individuali.

7. Il portafoglio concentrato deve contenere 40 debitori.

8. Il portafoglio controfattuale deve contenere 39 debitori.

9. L'investimento iniziale complessivo deve essere pari a $173$ milioni in entrambi i portafogli.

10. Le proporzioni relative degli investimenti dei 39 debitori residui devono rimanere invariate dopo la riallocazione.

11. I 39 debitori comuni devono utilizzare gli stessi scenari creditizi nei due portafogli.

12. La perdita di ciascun portafoglio deve coincidere con la somma delle rispettive perdite individuali.

13. I risultati devono essere riproducibili utilizzando il seed assegnato.

14. VaR e CVaR devono essere calcolati sulle distribuzioni empiriche delle perdite monetarie.

15. Le principali misure di rischio devono mostrare una ragionevole stabilità aumentando il numero delle simulazioni.

---

## 8. Ipotesi e limiti del caso

Il modello assume che:

1. il regime sistemico sia una catena di Markov omogenea;
2. le matrici $P^{(O)}$, $P^{(S)}$ e $P^{(C)}$ siano omogenee all'interno del rispettivo regime;
3. il default sia assorbente;
4. a parità di rating corrente e regime sistemico, tutti i debitori condividano la stessa matrice di migrazione;
5. le transizioni individuali siano indipendenti condizionatamente al regime comune;
6. gli investimenti iniziali siano deterministici;
7. nel caso didattico valga

$$
\mathrm{EAD}_i=V_{i,0};
$$

8. la LGD sia deterministica e comune ai debitori;
9. la funzione di perdita migration-based sia deterministica condizionatamente agli stati iniziale e finale;
10. le probabilità utilizzate siano probabilità fisiche.

Il modello non incorpora:

- matrici di transizione specifiche per singolo emittente;
- differenze settoriali nelle matrici di migrazione;
- LGD stocastiche o dipendenti dal regime;
- EAD stocastiche;
- evoluzione autonoma dell'EAD rispetto all'investimento iniziale;
- effetti di contagio diretto tra debitori;
- correlazioni ulteriori rispetto al fattore sistemico comune;
- cambiamenti endogeni delle matrici prodotti dal deterioramento del sistema finanziario;
- funding liquidity risk;
- market liquidity risk;
- probabilità risk-neutral;
- pricing di CDS o altri strumenti di copertura.

Le matrici di transizione, i tassi di perdita e gli investimenti assegnati costituiscono una **calibrazione didattica** e non una stima storica delle probabilità effettive di transizione di Lehman Brothers o del sistema finanziario nel 2008.

La distinzione tra $O$, $S$ e $C$ rappresenta in forma stilizzata differenti condizioni sistemiche e non una classificazione storicamente stimata dei trimestri del 2008.

Il confronto tra i due portafogli non deve essere interpretato come misura pura della sola concentrazione: la riallocazione proporzionale dell'investimento Lehman modifica anche la composizione dell'investimento tra classi di rating.

I risultati ottenuti descrivono il comportamento del modello quantitativo assegnato e non costituiscono una previsione retrospettiva del successivo default di Lehman Brothers.
