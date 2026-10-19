# Lezione 10 — Scheda Costruzione Caso TakeHome

## 1. Identificazione del caso

- **Lezione:** 10 — Applicazione in Python: rischio di credito
- **Tipo di caso:** TakeHome
- **Titolo:** Lehman Brothers 2008: rischio sistemico, migrazioni creditizie e perdita di portafoglio
- **Nome file previsto:** `Lezione_10_Scheda_Costruzione_Caso_TakeHome.md`
- **Destinatari:** studenti del secondo anno della Laurea Magistrale in Banca e Risk Management
- **Uso previsto:** caso applicativo guidato per sviluppare mediante simulazione Monte Carlo un modello di rischio creditizio di portafoglio nel quale le migrazioni dei singoli debitori dipendono da un regime sistemico comune che evolve nel tempo.

## 2. Contesto e motivazione

Il caso è ambientato nel **giugno 2008**, in una fase di crescente tensione del sistema finanziario internazionale e di deterioramento del merito creditizio di Lehman Brothers.

Il punto di osservazione è deliberatamente ex ante: il risk manager non conosce ancora l'esito che si realizzerà nei mesi successivi e deve misurare il rischio a un anno di un portafoglio di esposizioni creditizie.

Il portafoglio comprende quaranta debitori distribuiti tra differenti classi di rating. Una delle posizioni, identificata con Lehman Brothers, presenta un investimento iniziale significativamente più elevato di quello associato ai singoli altri debitori.

L'elemento centrale del caso non è tuttavia il singolo default di Lehman, ma la presenza di un **fattore sistemico comune**. Le condizioni generali del mercato finanziario possono trovarsi in uno stato ordinario, di stress o di crisi e possono cambiare da un trimestre al successivo. A ciascun regime corrisponde una diversa matrice di migrazione dei rating.

Le transizioni dei singoli debitori sono assunte indipendenti **condizionatamente alla traiettoria del regime sistemico**, ma non sono indipendenti incondizionatamente. Una traiettoria sistemica sfavorevole modifica contemporaneamente le probabilità di downgrade e default di tutti i debitori.

La simulazione Monte Carlo ha pertanto una funzione quantitativa sostanziale: serve a costruire la distribuzione congiunta delle perdite di portafoglio generata dall'interazione fra regime sistemico dinamico, migrazioni creditizie individuali, composizione iniziale del portafoglio e funzione di perdita.

Il caso comprende inoltre un confronto controfattuale. La posizione Lehman viene eliminata e il corrispondente investimento iniziale viene redistribuito proporzionalmente tra gli altri debitori, mantenendo invariato l'investimento complessivo del portafoglio. Il confronto consente di valutare gli effetti della sostituzione di una posizione fortemente concentrata con una riallocazione proporzionale sulle restanti posizioni.

Le matrici di transizione, la composizione del portafoglio e i parametri economici utilizzati nel caso sono **dati didattici calibrati**. Non costituiscono stime storiche delle probabilità effettive di transizione di Lehman Brothers o del sistema finanziario nel 2008.

**Riferimenti storici docente:** Lehman Brothers Holdings Inc., Form 10-Q 2008; SEC, documentazione relativa al Chapter 11 del 15 settembre 2008.

## 3. Domanda quantitativa e obiettivo didattico

### Domanda quantitativa

Nel giugno 2008, quale distribuzione della perdita a un anno può essere associata a un portafoglio di esposizioni creditizie se:

1. il regime sistemico evolve trimestralmente secondo una catena di Markov;
2. le probabilità di migrazione dei rating dipendono dal regime sistemico corrente;
3. i debitori appartengono inizialmente a differenti classi di rating;
4. le migrazioni individuali sono indipendenti condizionatamente al regime sistemico comune;
5. a ogni migrazione creditizia è associata una conseguenza economica?

Quali valori assumono perdita attesa, dispersione, VaR e CVaR?

Come cambiano tali quantità se l'investimento inizialmente concentrato su Lehman Brothers viene redistribuito proporzionalmente tra gli altri debitori, mantenendo invariato l'investimento complessivo del portafoglio?

### Obiettivo didattico

Lo studente deve essere in grado di passare da una struttura markoviana a due livelli a una distribuzione simulata delle perdite di portafoglio:

$$
\text{regime sistemico}
\longrightarrow
\text{matrici di migrazione condizionate}
\longrightarrow
\text{traiettorie creditizie}
\longrightarrow
\text{perdite individuali}
\longrightarrow
\text{perdita di portafoglio}
\longrightarrow
\widehat{F}_{L^P}
\longrightarrow
\widehat{\mathrm{VaR}},
\widehat{\mathrm{CVaR}}.
$$

L'applicazione deve inoltre rendere osservabili due meccanismi distinti:

1. il fattore sistemico comune genera dipendenza tra perdite creditizie che sarebbero indipendenti condizionatamente alla traiettoria del regime;
2. a parità di investimento complessivo, una differente allocazione iniziale delle posizioni modifica la distribuzione della perdita di portafoglio.

## 4. Specifica teorico-matematica

### 4.1 Regime sistemico

Si introduce il processo

$$
\{M_t\}_{t=0}^{3},
$$

con spazio degli stati

$$
\mathcal{M}
=
\{O,S,C\},
$$

dove:

- $O$ = condizioni ordinarie;
- $S$ = stress finanziario;
- $C$ = crisi.

Il regime osservato all'inizio del caso è

$$
M_0=S.
$$

La matrice trimestrale di transizione del regime è

$$
Q=
\begin{pmatrix}
0.82 & 0.16 & 0.02\\
0.30 & 0.55 & 0.15\\
0.10 & 0.35 & 0.55
\end{pmatrix}.
$$

La riga identifica il regime corrente e la colonna il regime del trimestre successivo.

### 4.2 Stati creditizi

Per ogni debitore $i$, il merito creditizio è rappresentato dal processo

$$
\{X_{i,t}\}_{t=0}^{4},
$$

con spazio degli stati

$$
\mathcal{I}
=
\{A,BBB,BB,B,D\},
$$

dove $D$ rappresenta il default ed è assorbente.

### 4.3 Matrici di migrazione condizionate al regime

Se il regime sistemico corrente è ordinario, si utilizza

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

Se il regime è di stress,

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

Se il regime è di crisi,

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

Per ogni debitore $i$,

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

### 4.4 Dipendenza tra i debitori

Condizionatamente alla traiettoria

$$
M_0,M_1,M_2,M_3,
$$

le transizioni dei differenti debitori sono assunte indipendenti.

Pertanto, per $i\neq r$,

$$
X_{i,t+1}
\perp
X_{r,t+1}
\mid
M_t,X_{i,t},X_{r,t}.
$$

L'indipendenza condizionata non implica indipendenza incondizionata.

Tutti i debitori sono infatti esposti alla medesima realizzazione del processo sistemico. Una traiettoria che permane o entra nello stato $C$ applica simultaneamente matrici di migrazione più sfavorevoli all'intero portafoglio.

### 4.5 Portafoglio iniziale concentrato

Indichiamo con $V_{i,0}$ l'investimento iniziale nella posizione creditizia verso il debitore $i$.

Il portafoglio contiene $40$ debitori e presenta un investimento iniziale complessivo pari a

$$
V_0^P
=
\sum_{i=1}^{40}V_{i,0}
=
173.
$$

Gli importi sono espressi in milioni di dollari.

| Gruppo | Numero debitori | Rating iniziale | Investimento iniziale per debitore | Investimento iniziale complessivo |
|---|---:|:---:|---:|---:|
| Lehman Brothers | 1 | A | 25 | 25 |
| Altri debitori A | 11 | A | 5 | 55 |
| Debitori BBB | 14 | BBB | 4 | 56 |
| Debitori BB | 9 | BB | 3 | 27 |
| Debitori B | 5 | B | 2 | 10 |
| **Totale** | **40** |  |  | **173** |

Lehman Brothers segue la stessa matrice di migrazione degli altri debitori appartenenti alla medesima classe di rating. La sua specificità nel modello deriva dall'ammontare dell'investimento iniziale.

### 4.6 Portafoglio controfattuale con riallocazione proporzionale

Nel portafoglio controfattuale la posizione Lehman viene eliminata.

L'investimento iniziale associato a Lehman,

$$
V_{L,0}=25,
$$

viene redistribuito tra i restanti $39$ debitori mantenendo inalterate le proporzioni relative dei loro investimenti iniziali.

L'investimento complessivo nei debitori diversi da Lehman è

$$
\sum_{i\neq L}V_{i,0}
=
148.
$$

Per ogni debitore $i\neq L$, il nuovo investimento è pertanto

$$
V_{i,0}^{\mathrm{div}}
=
V_{i,0}
+
25
\frac{V_{i,0}}{148},
$$

ossia

$$
V_{i,0}^{\mathrm{div}}
=
V_{i,0}
\frac{173}{148}.
$$

Il fattore di riscalamento è

$$
\frac{173}{148}
\approx
1.168919.
$$

La nuova struttura del portafoglio è quindi:

| Gruppo | Numero debitori | Rating iniziale | Investimento per debitore | Investimento complessivo |
|---|---:|:---:|---:|---:|
| Altri debitori A | 11 | A | 5.8446 | 64.2905 |
| Debitori BBB | 14 | BBB | 4.6757 | 65.4595 |
| Debitori BB | 9 | BB | 3.5068 | 31.5608 |
| Debitori B | 5 | B | 2.3378 | 11.6892 |
| **Totale** | **39** |  |  | **173.0000** |

I due portafogli presentano quindi lo stesso investimento iniziale complessivo:

$$
V_0^{P,\mathrm{conc}}
=
V_0^{P,\mathrm{div}}
=
173.
$$

Il confronto non deve essere interpretato come una variazione della dimensione del portafoglio, ma come una diversa allocazione dello stesso investimento complessivo.

La riallocazione proporzionale modifica anche la distribuzione dell'investimento tra classi di rating. Il confronto non identifica pertanto un effetto puro e isolato della sola concentrazione, ma misura l'effetto della specifica strategia controfattuale adottata: eliminazione della posizione Lehman e redistribuzione proporzionale dell'investimento sulle posizioni residue.

### 4.7 Funzione di perdita migration-based

La perdita del debitore dipende dal rating iniziale, dal rating finale e dall'ammontare investito nella posizione.

Si definisce

$$
L_i
=
V_{i,0}\,
\varphi(X_{i,0},X_{i,4}),
$$

dove $\varphi(r_0,r_4)$ è il tasso di perdita rispetto al valore di riferimento iniziale.

La calibrazione didattica è:

| Rating iniziale $\backslash$ finale | A | BBB | BB | B | D |
|---|---:|---:|---:|---:|---:|
| A | 0.00 | 0.03 | 0.10 | 0.22 | 0.65 |
| BBB | -0.02 | 0.00 | 0.06 | 0.16 | 0.65 |
| BB | -0.04 | -0.02 | 0.00 | 0.09 | 0.65 |
| B | -0.06 | -0.04 | -0.02 | 0.00 | 0.65 |

I valori negativi rappresentano incrementi di valore prodotti da un miglioramento del rating rispetto alla classe iniziale.

Nel default,

$$
\varphi(r_0,D)=0.65.
$$

Per raccordare questa specificazione con la notazione PD–LGD–EAD del Capitolo 9, nel caso didattico si assume che, in assenza di ammortamenti, utilizzi aggiuntivi o variazioni dell'esposizione nominale,

$$
\mathrm{EAD}_i=V_{i,0}.
$$

Questa uguaglianza è una **ipotesi semplificatrice del caso** e non costituisce una identificazione generale tra investimento iniziale ed EAD.

Con

$$
\mathrm{LGD}=0.65,
$$

la perdita in default risulta quindi

$$
L_i^D
=
\mathrm{EAD}_i\mathrm{LGD}
=
V_{i,0}(0.65).
$$

Nel portafoglio controfattuale la medesima ipotesi viene applicata ai nuovi investimenti $V_{i,0}^{\mathrm{div}}$.

### 4.8 Perdite di portafoglio e disegno della simulazione

Per la replica Monte Carlo $r$, la perdita del portafoglio concentrato è

$$
L_{\mathrm{conc}}^{P,(r)}
=
\sum_{i=1}^{40}
L_i^{(r)}.
$$

La perdita del portafoglio controfattuale è

$$
L_{\mathrm{div}}^{P,(r)}
=
\sum_{i\neq L}
V_{i,0}^{\mathrm{div}}
\varphi
\left(
X_{i,0},
X_{i,4}^{(r)}
\right).
$$

Il confronto deve essere effettuato utilizzando **gli stessi scenari Monte Carlo sottostanti**.

In particolare:

1. la traiettoria del regime sistemico è la stessa per i due portafogli in ciascuna replica;
2. per i $39$ debitori comuni ai due portafogli vengono utilizzate le stesse traiettorie creditizie;
3. la traiettoria Lehman entra soltanto nel portafoglio concentrato;
4. cambiano esclusivamente la presenza della posizione Lehman e gli investimenti iniziali attribuiti alle posizioni residue.

Questa costruzione evita che le differenze tra i due portafogli siano prodotte da scenari casuali differenti.

La simulazione di $N$ repliche produce:

$$
L_{\mathrm{conc}}^{P,(1)},
\ldots,
L_{\mathrm{conc}}^{P,(N)}
$$

e

$$
L_{\mathrm{div}}^{P,(1)},
\ldots,
L_{\mathrm{div}}^{P,(N)}.
$$

Da tali campioni vengono costruite le distribuzioni empiriche

$$
\widehat F_{\mathrm{conc}}
\qquad\text{e}\qquad
\widehat F_{\mathrm{div}}.
$$

Le principali quantità di interesse sono:

$$
\widehat{\mathbb E}[L^P],
\qquad
\widehat{\operatorname{Var}}(L^P),
\qquad
\widehat{\mathrm{VaR}}_{0.95},
\qquad
\widehat{\mathrm{CVaR}}_{0.95},
$$

e

$$
\widehat{\mathrm{VaR}}_{0.99},
\qquad
\widehat{\mathrm{CVaR}}_{0.99}.
$$

Le variazioni prodotte dalla riallocazione possono essere sintetizzate mediante

$$
\Delta \rho
=
\rho(L_{\mathrm{div}}^P)
-
\rho(L_{\mathrm{conc}}^P),
$$

dove $\rho$ rappresenta, di volta in volta, perdita attesa, deviazione standard, VaR o CVaR.

Il CVaR deve essere calcolato secondo la definizione mediante quantili adottata nel Capitolo 9.

### 4.9 Simulazione di una replica

Per ogni replica $r$:

1. si pone $M_0=S$;
2. per $t=0,\ldots,3$, la transizione creditizia $X_{i,t}\rightarrow X_{i,t+1}$ viene simulata utilizzando $P^{(M_t)}$;
3. condizionatamente a $M_t$, ogni debitore utilizza una propria estrazione casuale indipendente;
4. per $t<3$, il regime successivo $M_{t+1}$ viene simulato mediante $Q$;
5. al termine del quarto trimestre si osservano gli stati $X_{i,4}$;
6. si calcola la perdita del portafoglio concentrato;
7. si eliminano la posizione Lehman e la sua traiettoria dal portafoglio controfattuale;
8. agli stessi stati finali dei $39$ debitori residui vengono applicati gli investimenti iniziali riallocati;
9. si calcola la perdita del portafoglio controfattuale.

Il numero base di repliche è

$$
N=50\,000.
$$

Per la riproducibilità del Caso TakeHome viene utilizzato il seed

$$
2026.
$$

### 4.10 Ipotesi

1. Il regime sistemico è markoviano e omogeneo nel tempo.
2. Le matrici $P^{(O)}$, $P^{(S)}$, $P^{(C)}$ sono omogenee all'interno del rispettivo regime.
3. Il default è assorbente.
4. A parità di rating corrente e regime sistemico, tutti i debitori condividono la stessa matrice di migrazione.
5. Le transizioni individuali sono indipendenti condizionatamente al regime comune.
6. Gli investimenti iniziali sono deterministici.
7. Nel caso base si assume $\mathrm{EAD}_i=V_{i,0}$.
8. La LGD è deterministica e comune ai debitori.
9. La funzione di perdita migration-based è deterministica condizionatamente agli stati iniziale e finale.
10. Il modello utilizza probabilità fisiche.
11. Non viene modellato il pricing di strumenti derivati o l'impiego di probabilità risk-neutral.
12. Le matrici e i parametri costituiscono una calibrazione didattica, non una stima storica.

## 5. Output richiesti

### 5.1 Risultati numerici

Per entrambi i portafogli:

- distribuzione simulata della perdita;
- perdita media;
- varianza e deviazione standard;
- $VaR_{0.95}$;
- $CVaR_{0.95}$;
- $VaR_{0.99}$;
- $CVaR_{0.99}$.

Inoltre:

- differenza tra le misure di rischio dei due portafogli;
- probabilità simulata che il regime di crisi venga raggiunto almeno una volta nell'orizzonte;
- perdita media del portafoglio concentrato negli scenari con e senza ingresso nello stato di crisi;
- distribuzione scenario per scenario della differenza

$$
\Delta L^{(r)}
=
L_{\mathrm{div}}^{P,(r)}
-
L_{\mathrm{conc}}^{P,(r)}.
$$

### 5.2 Tabelle

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

Per il portafoglio concentrato, confronto tra:

- scenari nei quali lo stato $C$ non viene mai raggiunto;
- scenari nei quali lo stato $C$ viene raggiunto almeno una volta.

### 5.3 Grafici

1. Distribuzione empirica della perdita del portafoglio concentrato con indicazione di VaR 95% e VaR 99%.
2. Confronto tra le distribuzioni empiriche delle perdite dei due portafogli, con particolare attenzione alla coda destra.
3. Confronto delle perdite del portafoglio concentrato negli scenari con e senza ingresso nello stato di crisi.

### 5.4 Controlli

- tutte le righe di $Q$ devono sommare a uno;
- tutte le righe delle tre matrici $P^{(m)}$ devono sommare a uno;
- lo stato $D$ deve essere assorbente in tutte le matrici;
- tutti gli stati simulati devono appartenere agli insiemi previsti;
- all'interno di una replica la traiettoria sistemica deve essere unica e comune a tutti i debitori;
- condizionatamente a tale traiettoria, i debitori devono utilizzare estrazioni casuali individuali;
- il portafoglio concentrato deve contenere $40$ debitori;
- il portafoglio controfattuale deve contenere $39$ debitori;
- l'investimento iniziale complessivo deve essere pari a $173$ milioni in entrambi i portafogli;
- le proporzioni relative degli investimenti dei $39$ debitori residui devono rimanere invariate dopo la riallocazione;
- i $39$ debitori comuni devono utilizzare gli stessi scenari creditizi nei due portafogli;
- la perdita di ciascun portafoglio deve coincidere con la somma delle rispettive perdite individuali;
- i risultati devono essere riproducibili con il seed assegnato;
- VaR e CVaR devono essere calcolati sulle distribuzioni empiriche delle perdite monetarie.

## 6. Flusso logico-teorico risolutivo atteso

| Passo | Finalità risolutiva | Formula, definizione, proprietà o teorema | Applicazione nel caso | Output o controllo collegato |
|---:|---|---|---|---|
| 1 | Costruire il modello probabilistico e i due portafogli | Catena di Markov; probabilità condizionata; indipendenza condizionata; vincolo di investimento complessivo | Definizione di $M_t$, $X_{i,t}$, $Q$, $P^{(O)}$, $P^{(S)}$, $P^{(C)}$, portafoglio concentrato e portafoglio controfattuale | Specifica teorico-matematica validata |
| 2 | Generare scenari congiunti di regime e rating | $\Pr(X_{i,t+1}=j\mid X_{i,t}=k,M_t=m)=p_{kj}^{(m)}$ | Simulazione della traiettoria sistemica comune e delle migrazioni individuali condizionate | Stati finali dei debitori e controlli sulle traiettorie |
| 3 | Trasformare gli stessi scenari creditizi nelle perdite dei due portafogli | $L_i=V_{i,0}\varphi(X_{i,0},X_{i,4})$ e aggregazione | Applicazione dei due vettori di investimento agli stessi scenari dei debitori comuni | Campioni $L_{\mathrm{conc}}^{P,(r)}$ e $L_{\mathrm{div}}^{P,(r)}$ |
| 4 | Stimare e confrontare distribuzioni e rischio di coda | Distribuzione empirica, valore atteso, dispersione, quantile, VaR, CVaR | Stima delle misure per entrambi i portafogli e analisi degli scenari con e senza crisi | Tabelle, grafici e differenze tra misure di rischio |
| 5 | Controllare il modello e interpretare i risultati | Ipotesi di Markov, omogeneità, indipendenza condizionata, allocazione, rischio di modello | Valutazione delle ipotesi, controllo conclusivo e interpretazione del ruolo del regime sistemico e della riallocazione dell'investimento Lehman | Interpretazione finale e, se emerge una criticità specifica, eventuale verifica in Regime C |

## 7. Scomposizione attesa in tappe

| Tappa | Titolo | Obiettivo | Input | Regime IA prevalente | Prompt virtuoso di riferimento | Oggetti teorici coinvolti | Operazione | Output | Controllo | Uso successivo |
|---:|---|---|---|:---:|---|---|---|---|---|---|
| 1 | Modello teorico e struttura della simulazione | Formalizzare il modello probabilistico, i due portafogli, la funzione di perdita e le quantità finali | Scheda Caso | A | Prompt tappa 1 | Catene di Markov, probabilità condizionata, indipendenza condizionata, investimento iniziale, EAD, funzione di perdita, riallocazione proporzionale | Identificare i due livelli markoviani, i due portafogli, le ipotesi di dipendenza, la funzione di perdita e le quantità finali | Specifica teorico-matematica ordinata e algoritmo concettuale | Coerenza con la Scheda Caso; distinzione tra investimento iniziale ed EAD; investimento totale invariato nel controfattuale | Base vincolante della simulazione |
| 2 | Simulazione congiunta del regime e delle migrazioni | Generare scenari coerenti di regime sistemico e rating | $Q$, $P^{(O)}$, $P^{(S)}$, $P^{(C)}$, rating iniziali, $N$, seed | B | Prompt tappa 2 | Catene di Markov, matrici di transizione, stato assorbente, indipendenza condizionata | Simulare congiuntamente traiettorie sistemiche e creditizie per quattro trimestri | Regimi simulati e stati creditizi finali per ogni replica | Matrici stocastiche; default assorbente; regime comune; estrazioni individuali condizionate | Costruzione delle perdite |
| 3 | Dagli scenari creditizi ai due portafogli di perdita | Trasformare gli stessi scenari creditizi nelle perdite dei due portafogli | Stati simulati, investimenti iniziali, regola di riallocazione, funzione $\varphi$ | B | Prompt tappa 3 | Funzione di perdita, EAD, LGD, aggregazione di portafoglio, riallocazione proporzionale | Costruire i due vettori di investimento, calcolare le perdite individuali e aggregarle sugli stessi scenari | Campioni $L_{\mathrm{conc}}^{P,(r)}$, $L_{\mathrm{div}}^{P,(r)}$ e $\Delta L^{(r)}$ | Investimento totale pari a $173$ in entrambi i portafogli; proporzioni residue conservate; stessi scenari per i debitori comuni | Stima delle distribuzioni |
| 4 | Distribuzioni simulate e misure di rischio | Stimare e confrontare le distribuzioni di perdita e le principali misure di rischio | Campioni delle perdite e traiettorie sistemiche | B | Prompt tappa 4 | Distribuzione empirica, valore atteso, varianza, VaR, CVaR, condizionamento per evento | Costruire le distribuzioni empiriche e stimare perdita media, dispersione, VaR e CVaR; confrontare i due portafogli e gli scenari crisi/non crisi | Tabelle, grafici e misure di rischio | Coerenza quantili/CVaR; stabilità Monte Carlo; interpretazione corretta del confronto | Interpretazione finanziaria |
| 5 | Controlli conclusivi | Verificare la coerenza complessiva del notebook rispetto alla Scheda Caso e agli output richiesti | Notebook completo, risultati, controlli e ipotesi | — | Nessun prompt obbligatorio; eventuale Prompt C sulla tappa interessata | Ipotesi modellistiche, rischio di modello e coerenza interna | Svolgere i controlli conclusivi; ricorrere al Regime C solo se emerge una criticità specifica da verificare | Notebook validato ed eventuale correzione delle celle interessate | Coerenza notebook-Scheda Caso; distinzione modello/realtà storica; se viene attivato il Regime C, criticità accolta oppure respinta | Base verificata per l'interpretazione finanziaria finale autonoma dello studente |

## 8. Sequenza docente dei prompt e mappa prompt-notebook

La sequenza ordinaria del caso è:

1. Prompt zero;
2. Prompt 1;
3. Prompt 2;
4. Prompt 3;
5. prompt delle tappe operative previste dalla scomposizione validata;
6. eventuali Prompt C, soltanto quando lo studente individua una criticità specifica da verificare.

La sequenza dei prompt di tappa non costituisce una struttura autonoma rispetto al Prompt 3: deriva dalla scomposizione operativa validata e deve conservarne obiettivi, input, output e controlli.

La corrispondenza tra prompt, tappe e notebook è riportata nella tabella seguente.


| Prompt | Regime | Tappa o fase | Funzione del prompt | Celle o output prodotti | Decisione o controllo richiesto |
|---|:---:|---|---|---|---|
| Prompt zero | — | Inizializzazione | Definire il contesto generale, i vincoli di interazione con l'IA e le regole del lavoro | Nessuna cella specifica del caso | Corretta acquisizione dei vincoli generali |
| Prompt 1 | — | Apertura | Acquisire la Scheda Caso come specifica vincolante e produrre l'inquadramento iniziale | Cella Markdown iniziale con contesto, domanda quantitativa e specifica del caso | Coerenza con la Scheda Caso e assenza di anticipazioni della soluzione |
| Prompt 2 | A | Progettazione teorica | Verificare, completare e ordinare il Flusso logico-teorico risolutivo proposto | Cella Markdown con il Flusso logico-teorico risolutivo validato | Coerenza tra passaggi teorici, output e controlli |
| Prompt 3 | A/B | Progettazione operativa | Verificare, completare e ordinare la scomposizione del notebook in tappe input-output | Cella Markdown con la scomposizione operativa validata | Coerenza dei collegamenti input-output e copertura degli output e controlli richiesti |
| Prompt tappa 1 | A | Tappa 1 | Formalizzare il modello teorico, i due portafogli e la regola di riallocazione senza produrre codice | Celle Markdown di impostazione teorico-matematica e algoritmo concettuale | Correttezza del modello a due livelli, distinzione investimento/EAD e costruzione del controfattuale |
| Prompt tappa 2 | B | Tappa 2 | Tradurre la specifica validata nell'algoritmo di simulazione del regime e delle migrazioni creditizie | Celle Markdown e codice per matrici e simulazione delle traiettorie | Corretta implementazione del regime comune, dello stato assorbente e delle transizioni individuali |
| Prompt tappa 3 | B | Tappa 3 | Implementare la funzione di perdita, la riallocazione proporzionale e l'aggregazione dei due portafogli | Celle Markdown e codice per i due vettori di investimento, funzione di perdita e aggregazione | Coerenza della riallocazione, stato-perdita, investimento complessivo e riuso degli stessi scenari |
| Prompt tappa 4 | B | Tappa 4 | Costruire distribuzioni, misure di rischio, tabelle e grafici previsti | Celle Markdown, codice, tabelle e grafici per distribuzioni e misure di rischio | Corretta implementazione di VaR/CVaR, stabilità Monte Carlo e corretto confronto fra i portafogli |
| Prompt C eventuale | C | Tappa interessata | Verificare una criticità specifica già individuata dallo studente | Eventuale sostituzione delle celle coinvolte | Criticità accolta oppure respinta |


## 9. Struttura attesa del notebook

Il notebook deve seguire le cinque tappe risolutive. Ogni tappa costituisce un modulo logico riconoscibile, ma può comprendere più celle Markdown, codice e output.

### Apertura del notebook

**Prompt di riferimento:** Prompt 1.

- Cella Markdown: titolo del caso, contesto, domanda quantitativa e Scheda Caso come specifica vincolante.

Dopo la cella iniziale prodotta con il Prompt 1, il notebook deve riportare:

- una cella Markdown con il Flusso logico-teorico risolutivo validato attraverso il Prompt 2;
- una cella Markdown con la scomposizione operativa in tappe input-output validata attraverso il Prompt 3.

Queste due celle documentano le decisioni di progettazione che governano lo sviluppo successivo del notebook e devono precedere le celle operative delle singole tappe.

### Tappa 1 — Modello teorico e struttura della simulazione

**Prompt di riferimento:** Prompt tappa 1 — Regime A.

- Cella Markdown: definizione del processo sistemico $M_t$.
- Cella Markdown: definizione dei processi creditizi $X_{i,t}$.
- Cella Markdown: significato di $Q$ e delle tre matrici $P^{(O)}$, $P^{(S)}$, $P^{(C)}$.
- Cella Markdown: spiegazione dell'indipendenza condizionata e della dipendenza incondizionata.
- Cella Markdown: definizione dell'investimento iniziale $V_{i,0}$ e distinzione rispetto all'EAD.
- Cella Markdown: composizione del portafoglio concentrato.
- Cella Markdown: regola di costruzione del portafoglio controfattuale a investimento totale invariato.
- Cella Markdown: funzione di perdita e quantità finali di interesse.
- Cella Markdown: algoritmo concettuale della singola replica Monte Carlo.

### Tappa 2 — Simulazione congiunta del regime e delle migrazioni

**Prompt di riferimento:** Prompt tappa 2 — Regime B.

- Cella codice: definizione degli stati e delle matrici $Q$, $P^{(O)}$, $P^{(S)}$, $P^{(C)}$.
- Cella codice: controlli sulle matrici.
- Cella codice: costruzione dei rating iniziali dei $40$ debitori.
- Cella codice: impostazione del seed e del numero di repliche.
- Cella codice: simulazione delle traiettorie del regime sistemico.
- Cella codice: simulazione delle traiettorie creditizie condizionate al regime comune.
- Output: controlli sul numero e sulla validità degli stati simulati.
- Output sintetico: alcune traiettorie campione utilizzate esclusivamente per rendere leggibile il meccanismo dinamico.

### Tappa 3 — Dagli scenari creditizi ai due portafogli di perdita

**Prompt di riferimento:** Prompt tappa 3 — Regime B.

- Cella Markdown: definizione operativa della funzione $\varphi(r_0,r_4)$.
- Cella codice: implementazione della matrice dei tassi di perdita.
- Cella codice: costruzione del vettore degli investimenti del portafoglio concentrato.
- Cella codice: costruzione del vettore degli investimenti del portafoglio controfattuale.
- Output: controllo dell'investimento totale e della conservazione delle proporzioni relative.
- Cella codice: calcolo delle perdite individuali e aggregate del portafoglio concentrato.
- Cella codice: calcolo delle perdite individuali e aggregate del portafoglio controfattuale utilizzando gli stessi scenari dei $39$ debitori comuni.
- Output: campioni delle due perdite di portafoglio.
- Output: differenze scenario per scenario $\Delta L^{(r)}$.
- Controllo: riconciliazione delle perdite aggregate con le componenti individuali.

### Tappa 4 — Distribuzioni simulate e misure di rischio

**Prompt di riferimento:** Prompt tappa 4 — Regime B.

- Cella Markdown: funzione delle misure richieste e convenzioni per VaR e CVaR.
- Cella codice: costruzione delle distribuzioni empiriche dei due portafogli.
- Cella codice: perdita media, varianza e deviazione standard.
- Cella codice: $VaR_{0.95}$, $CVaR_{0.95}$, $VaR_{0.99}$, $CVaR_{0.99}$.
- Output: tabella comparativa delle misure di rischio e delle rispettive differenze.
- Cella codice/output: grafico della distribuzione empirica del portafoglio concentrato con indicazione dei VaR.
- Cella codice/output: confronto delle distribuzioni e delle code dei due portafogli.
- Cella codice/output: confronto, per il portafoglio concentrato, tra scenari con ingresso nello stato $C$ e scenari senza ingresso nello stato $C$.
- Controllo: verifica della stabilità delle principali stime rispetto alla dimensione del campione Monte Carlo.

### Tappa 5 — Controlli conclusivi e interpretazione

**Prompt di riferimento:** nessun prompt obbligatorio. Il Regime C può essere attivato soltanto in presenza di una criticità specifica individuata dallo studente.

- Cella Markdown: controlli conclusivi sulla coerenza tra notebook e Scheda Caso.
- Cella Markdown: interpretazione finanziaria finale formulata autonomamente dallo studente.
- Se emerge una criticità specifica, eventuale Prompt C riferito alla tappa interessata.
- Classificazione dell'eventuale verifica: criticità accolta oppure criticità respinta.
- Se la criticità viene accolta, sostituzione delle celle interessate con versioni corrette.

L'interpretazione deve distinguere almeno:

- effetto del regime sistemico sulla coda della distribuzione;
- ruolo della posizione Lehman nel portafoglio concentrato;
- differenza tra indipendenza condizionata e dipendenza incondizionata;
- significato di VaR e CVaR;
- effetto della riallocazione proporzionale dell'investimento Lehman;
- modifica della composizione per rating prodotta dalla riallocazione;
- limiti dell'ipotesi di matrici omogenee all'interno dei tre regimi;
- differenza tra simulazione didattica ex ante e successiva realizzazione storica.

## 10. Criteri di validazione del notebook

Il notebook è considerato valido se:

1. implementa la specifica teorico-matematica della Scheda Caso senza modificarla;
2. utilizza esclusivamente le matrici, gli investimenti, la funzione di perdita, la regola di riallocazione e gli altri parametri assegnati;
3. rispetta la scomposizione in tappe input-output validata;
4. mantiene coerenti la notazione matematica e le corrispondenti variabili computazionali;
5. simula una sola traiettoria del regime sistemico per ciascuna replica e la utilizza per tutti i debitori;
6. preserva l'indipendenza delle estrazioni individuali condizionatamente alla traiettoria sistemica comune;
7. mantiene lo stato di default assorbente;
8. costruisce correttamente il portafoglio controfattuale eliminando la posizione Lehman e redistribuendo il relativo investimento proporzionalmente tra i 39 debitori residui;
9. mantiene invariato l'investimento complessivo, pari a $173$ milioni, e conserva le proporzioni relative degli investimenti dei debitori residui;
10. utilizza gli stessi scenari sistemici e creditizi per i 39 debitori comuni ai due portafogli;
11. applica correttamente la funzione $\varphi$ agli stati iniziali e finali e riconcilia le perdite aggregate con la somma delle perdite individuali;
12. produce tutti gli output numerici, tabellari e grafici richiesti;
13. calcola VaR e CVaR sulle distribuzioni delle perdite monetarie secondo le convenzioni adottate nel corso;
14. distingue correttamente gli scenari con e senza ingresso nello stato di crisi;
15. produce risultati riproducibili con il seed assegnato e sufficientemente stabili rispetto alla dimensione del campione Monte Carlo;
16. conclude con controlli espliciti e con un'interpretazione finanziaria coerente con gli output e con i limiti del modello.

Un eventuale Prompt in Regime C non costituisce condizione necessaria di validità del notebook. Esso interviene soltanto quando lo studente individua una criticità specifica da verificare.


## 11. Calibrazione docente

La seguente calibrazione è riferita a:

$$
N=50\,000,
\qquad
\text{seed}=2026.
$$

I valori sono indicativi e servono al docente per verificare l'ordine di grandezza degli output.

### 11.1 Portafoglio concentrato

| Misura | Valore indicativo, milioni USD |
|---|---:|
| Perdita media | 11.11 |
| Deviazione standard | 6.92 |
| VaR 95% | 24.73 |
| CVaR 95% | 29.69 |
| VaR 99% | 32.78 |
| CVaR 99% | 37.54 |

### 11.2 Portafoglio controfattuale con riallocazione proporzionale

| Misura | Valore indicativo, milioni USD |
|---|---:|
| Perdita media | 12.16 |
| Deviazione standard | 7.26 |
| VaR 95% | 26.56 |
| CVaR 95% | 30.92 |
| VaR 99% | 33.66 |
| CVaR 99% | 37.03 |

### 11.3 Differenze indotte dalla riallocazione

Definendo

$$
\Delta\rho
=
\rho(L_{\mathrm{div}}^P)
-
\rho(L_{\mathrm{conc}}^P),
$$

si ottengono indicativamente:

| Misura | $\Delta\rho$, milioni USD |
|---|---:|
| Perdita media | +1.05 |
| Deviazione standard | +0.33 |
| VaR 95% | +1.83 |
| CVaR 95% | +1.23 |
| VaR 99% | +0.88 |
| CVaR 99% | -0.52 |

Il risultato non deve essere interpretato mediante l'affermazione semplicistica secondo cui la rimozione della posizione concentrata riduce necessariamente tutte le misure di rischio.

La riallocazione dell'investimento Lehman interessa proporzionalmente anche debitori inizialmente classificati BBB, BB e B. La composizione per rating del portafoglio viene quindi modificata.

Con questa calibrazione, la riallocazione aumenta la perdita attesa e diverse misure di rischio, mentre il CVaR al $99\%$ si riduce leggermente. Quest'ultimo risultato evidenzia che la grande posizione Lehman continua ad avere un effetto rilevante sulle realizzazioni più estreme della coda, anche se la sua eliminazione non produce una riduzione generalizzata delle altre misure.

### 11.4 Ruolo del regime sistemico

Con la calibrazione assegnata:

- la probabilità simulata di visitare lo stato $C$ almeno una volta nell'orizzonte è circa il $29.5\%$;
- la perdita media del portafoglio concentrato negli scenari che visitano $C$ è circa $18.25$ milioni;
- la perdita media del portafoglio concentrato negli scenari che non visitano $C$ è circa $8.12$ milioni.

Il confronto deve rendere evidente la funzione del fattore sistemico comune.

### 11.5 Errori o ambiguità prevedibili

1. Confondere investimento iniziale ed EAD come se fossero concetti identici per definizione.
2. Eliminare Lehman senza redistribuirne l'investimento, riducendo così la dimensione complessiva del portafoglio.
3. Redistribuire l'investimento Lehman in parti uguali anziché proporzionalmente agli investimenti residui.
4. Modificare le proporzioni relative tra i $39$ debitori residui.
5. Utilizzare simulazioni differenti per confrontare i due portafogli.
6. Simulare un regime sistemico differente per ciascun debitore.
7. Utilizzare la stessa estrazione casuale individuale per tutti i debitori, generando comovimento perfetto invece di indipendenza condizionata.
8. Confondere $Q$ con le matrici di migrazione creditizia.
9. Utilizzare sempre $P^{(S)}$ perché il regime iniziale è $S$, ignorando l'evoluzione di $M_t$.
10. Applicare la matrice corrispondente al regime futuro anziché al regime corrente senza dichiarare la convenzione temporale.
11. Permettere a un debitore in default di uscire dallo stato $D$.
12. Utilizzare il solo default nella funzione di perdita, ignorando le migrazioni non-default.
13. Trattare i valori negativi della funzione di perdita come errori anziché come guadagni rispetto al riferimento.
14. Calcolare VaR e CVaR sui rating o sul numero di default anziché sulle perdite monetarie.
15. Calcolare il CVaR discreto come semplice media delle osservazioni maggiori o uguali al VaR senza rispettare la massa necessaria a costruire esattamente la coda $1-\alpha$.
16. Interpretare il confronto tra i due portafogli come misura pura della sola concentrazione, ignorando la modifica della composizione per rating.
17. Interpretare la simulazione come previsione storica del default di Lehman.
18. Concludere che la presenza del fattore comune rappresenti integralmente la dipendenza creditizia reale.

### 11.6 Controlli minimi di validazione

- validazione di $Q$ e delle tre $P^{(m)}$;
- controllo dello stato assorbente;
- verifica dell'investimento complessivo di $173$ milioni in entrambi i portafogli;
- verifica della conservazione delle proporzioni relative tra i $39$ debitori residui;
- verifica della traiettoria sistemica unica per replica;
- verifica delle estrazioni individuali indipendenti condizionatamente al regime;
- verifica dell'utilizzo degli stessi scenari per i debitori comuni ai due portafogli;
- controllo della funzione di perdita;
- riconciliazione fra perdite individuali e perdita aggregata;
- riproducibilità;
- stabilità delle misure di rischio aumentando il numero delle simulazioni;
- confronto qualitativo tra scenari con e senza condizioni sistemiche di crisi.

### 11.7 Limiti interpretativi

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

La distinzione tra $O$, $S$ e $C$ deve essere interpretata come rappresentazione stilizzata di differenti condizioni sistemiche, non come classificazione storicamente stimata dei trimestri del 2008.

## 12. Uso dell'IA e tracciato

### Prompt obbligatori

La sequenza obbligatoria comprende:

- Prompt zero;
- Prompt 1;
- Prompt 2;
- Prompt 3;
- i prompt di tappa necessari per realizzare la scomposizione operativa validata con il Prompt 3.

Nel presente caso, i prompt di tappa necessari derivano dalla scomposizione operativa validata attraverso il Prompt 3. I controlli conclusivi e l'interpretazione finanziaria finale non richiedono un prompt obbligatorio; l'eventuale Regime C può essere attivato soltanto quando lo studente individua una criticità specifica da verificare.

### Prompt eventuali in Regime C

Il Regime C non costituisce una tappa obbligatoria del caso.

Un Prompt C viene utilizzato soltanto quando lo studente individua un dubbio, un'anomalia o una possibile incoerenza specifica nel notebook, negli output o nella propria interpretazione. Il prompt deve indicare la parte interessata, la criticità individuata e il ragionamento che la motiva.

L'esito della verifica deve essere classificato come:

- criticità respinta;
- criticità accolta.

Se la criticità è accolta, vengono sostituite le celle della tappa interessata. Se è respinta, il notebook non viene modificato.



### Usi ammessi dell'IA

- ordinamento e verifica della formulazione teorico-matematica proposta dallo studente;
- traduzione in codice della specifica validata;
- costruzione tecnica dell'algoritmo di simulazione;
- implementazione della riallocazione proporzionale specificata;
- generazione di tabelle e grafici;
- implementazione delle misure di rischio;
- verifica di controlli proposti dallo studente;
- analisi critica di una possibile incoerenza formulata dallo studente.

### Usi non ammessi

- modifica autonoma di $Q$;
- modifica autonoma delle matrici $P^{(m)}$;
- modifica della composizione iniziale del portafoglio;
- modifica autonoma della regola di riallocazione;
- modifica della funzione di perdita;
- sostituzione dell'ipotesi di indipendenza condizionata con una diversa struttura di dipendenza;
- introduzione autonoma di copule, modelli strutturali o modelli a fattori non previsti dalla Scheda Caso;
- utilizzo di dati storici esterni in sostituzione dei parametri didattici;
- produzione dell'interpretazione finale al posto dello studente.

### Tracciato IA da consegnare

Il tracciato ordinario dell'interazione con l'IA è costituito dalla stampa in PDF della chat dedicata al caso.

Il PDF deve consentire di ricostruire in ordine cronologico:

- Prompt zero;
- Prompt 1;
- Prompt 2;
- Prompt 3;
- i prompt di tappa effettivamente utilizzati;
- gli eventuali Prompt C;
- le risposte dell'IA associate a ciascun prompt.

Il tracciato deve essere coerente con il notebook consegnato. In particolare, le celle prodotte o modificate attraverso l'interazione con l'IA devono risultare riconducibili alla sequenza documentata dei prompt.

Eventuali materiali aggiuntivi possono accompagnare il PDF, ma non sostituiscono il tracciato ordinario della chat dedicata.

## 13. Valutazione

### Criteri per il notebook

- corretta rappresentazione dei due livelli markoviani;
- corretta gestione della dipendenza attraverso il regime sistemico comune;
- corretta distinzione tra investimento iniziale ed EAD;
- corretta implementazione della simulazione;
- corretta costruzione del portafoglio controfattuale;
- mantenimento dell'investimento complessivo;
- corretta trasformazione rating-perdita;
- corretta aggregazione di portafoglio;
- corretta stima delle distribuzioni empiriche;
- corretta implementazione di VaR e CVaR;
- qualità dei controlli;
- chiarezza di tabelle e grafici;
- capacità di interpretare correttamente il confronto tra le due allocazioni.

### Criteri per il tracciato IA

- qualità del contributo iniziale dello studente in Regime A;
- rispetto della Scheda Caso come specifica vincolante;
- corretta separazione tra scelte teoriche e traduzione computazionale;
- qualità della scomposizione del problema;
- capacità di specificare all'IA input e output di ciascuna tappa;
- qualità dell'eventuale verifica in Regime C, quando attivata a partire da una criticità specifica individuata dallo studente;
- capacità di accettare o respingere motivatamente una proposta dell'IA;
- assenza di delega dell'interpretazione finale.

### Peso dei controlli e dell'interpretazione

La qualità del codice non deve essere valutata per complessità autonoma.

Il nucleo della valutazione è costituito dalla capacità di governare correttamente la catena:

$$
\text{modello probabilistico}
\longrightarrow
\text{simulazione}
\longrightarrow
\text{allocazione}
\longrightarrow
\text{perdita}
\longrightarrow
\text{distribuzione}
\longrightarrow
\text{misure di rischio}
\longrightarrow
\text{confronto}
\longrightarrow
\text{controlli conclusivi}
\longrightarrow
\text{interpretazione}.
$$


## 14. Rubrica sintetica

| Dimensione | Peso |
|---|---:|
| Prompt 2 — qualità del Flusso logico-teorico risolutivo proposto e validato | 30 |
| Prompt 3 — qualità della scomposizione operativa in tappe input-output | 15 |
| Notebook e output quantitativi | 20 |
| Qualità dei prompt di tappa e corretto uso dei Regimi A/B; eventuale Regime C | 15 |
| Controlli logici, numerici e di coerenza | 15 |
| Interpretazione finanziaria finale | 5 |
| **Totale** | **100** |

La valutazione del Regime C riguarda la qualità del suo eventuale utilizzo quando emerge una criticità specifica; l'assenza di un Prompt C non costituisce di per sé elemento negativo.

## 15. Esito atteso e calibrazione qualitativa del caso

Al termine del caso, lo studente deve essere in grado di:

1. rappresentare correttamente la dipendenza tra regime sistemico comune e migrazioni creditizie individuali;
2. distinguere indipendenza condizionata e dipendenza incondizionata tra le perdite dei debitori;
3. trasformare gli stati creditizi simulati in perdite monetarie mediante la funzione di perdita assegnata;
4. costruire correttamente il portafoglio controfattuale eliminando la posizione Lehman e redistribuendone proporzionalmente l'investimento;
5. confrontare i due portafogli utilizzando gli stessi scenari Monte Carlo per i debitori comuni;
6. stimare e interpretare perdita attesa, dispersione, VaR e CVaR;
7. valutare correttamente gli effetti della riallocazione senza identificarli automaticamente con un effetto puro della sola concentrazione;
8. distinguere i risultati prodotti dal modello didattico dagli eventi storici successivamente osservati;
9. formulare autonomamente un'interpretazione finanziaria coerente con le ipotesi, gli output e i limiti del modello.

### Calibrazione qualitativa

Il caso è considerato didatticamente ben calibrato se:

- la posizione Lehman costituisce una concentrazione iniziale economicamente rilevante;
- la sua eliminazione e la riallocazione proporzionale modificano in modo osservabile la distribuzione delle perdite;
- il controfattuale non produce necessariamente una riduzione uniforme di tutte le misure di rischio;
- il regime sistemico comune genera differenze chiaramente osservabili tra scenari con e senza ingresso nello stato di crisi;
- la riallocazione rende evidente che una riduzione della concentrazione può modificare anche la composizione per rating del portafoglio;
- gli output numerici rimangono compatibili con gli ordini di grandezza riportati nella calibrazione docente;
- il problema richiede il trasferimento autonomo della struttura metodologica sviluppata nel Caso Aula, senza ridursi a una semplice sostituzione di parametri.

Gli esiti numerici indicativi riportati nella calibrazione docente hanno funzione di controllo e non devono essere comunicati allo studente come risultati da riprodurre meccanicamente.

## 16. Relazione con l'altro caso della lezione

Il Caso Aula è contestualizzato nella crisi di **China Evergrande del 2021**.

L'isomorfismo metodologico riguarda:

$$
\text{regime sistemico markoviano}
\longrightarrow
\text{matrici di rating condizionate}
\longrightarrow
\text{simulazione congiunta}
\longrightarrow
\text{perdita di portafoglio}
\longrightarrow
VaR/CVaR
\longrightarrow
\text{analisi controfattuale}
\longrightarrow
\text{controlli conclusivi}
\longrightarrow
\text{interpretazione}.
$$

Il Caso TakeHome non costituisce una semplice sostituzione dei valori numerici.

Cambiano almeno:

- contesto economico e istituzionale;
- interpretazione dei regimi sistemici;
- composizione per rating del portafoglio;
- struttura degli investimenti iniziali;
- matrici $Q$ e $P^{(m)}$;
- funzione di perdita o relativa calibrazione;
- natura della posizione principale;
- struttura dell'analisi controfattuale;
- criticità economico-finanziaria da discutere.

Nel caso TakeHome, il fattore sistemico rappresenta la dinamica delle condizioni del sistema finanziario durante la crisi del 2008 e Lehman costituisce la posizione iniziale di maggiore dimensione.

Nel Caso Aula, il fattore comune è reinterpretato in relazione alle condizioni del settore immobiliare e finanziario cinese e la posizione principale è associata a Evergrande.