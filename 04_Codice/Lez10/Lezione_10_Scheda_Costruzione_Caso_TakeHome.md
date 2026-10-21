# Lezione 10 — Scheda Costruzione Caso TakeHome

## 1. Identificazione del caso

- **Lezione:** 10 — Applicazione in Python: rischio di credito
- **Tipo di caso:** TakeHome
- **Titolo:** Lehman Brothers 2008: rischio sistemico, migrazioni creditizie e perdita di portafoglio
- **Nome file previsto:** `Lezione_10_Scheda_Costruzione_Caso_TakeHome.md`
- **Destinatari:** studenti del secondo anno della Laurea Magistrale in Banca e Risk Management
- **Uso previsto:** lavoro autonomo TakeHome per sviluppare mediante simulazione Monte Carlo un modello di rischio creditizio di portafoglio nel quale le migrazioni dei singoli debitori dipendono da un regime sistemico comune che evolve nel tempo.

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


## 3. Domanda quantitativa e funzione didattica

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

### Collegamento con le lezioni teoriche precedenti

Il caso applica operativamente i contenuti sviluppati nelle lezioni teoriche precedenti sulle catene di Markov, sulle migrazioni creditizie e sulle misure di rischio. In particolare, utilizza:

- la dinamica markoviana di un processo a stati discreti;
- matrici di migrazione creditizia dipendenti dal regime sistemico;
- il ruolo dello stato di default assorbente;
- la distinzione tra indipendenza condizionata e dipendenza incondizionata;
- la costruzione di perdite individuali e aggregate;
- la stima empirica di valore atteso, varianza, VaR e CVaR.

### Concetti teorici da rendere osservabili

Il caso deve rendere osservabili:

- la dipendenza delle probabilità di migrazione dal regime sistemico corrente;
- l’indipendenza delle migrazioni individuali condizionatamente alla traiettoria sistemica comune;
- la dipendenza incondizionata tra le perdite dei debitori;
- il carattere assorbente dello stato di default;
- il passaggio dalle traiettorie creditizie alle perdite individuali;
- il passaggio dalle perdite individuali alla distribuzione della perdita di portafoglio;
- l’effetto della riallocazione dell’investimento iniziale sulla distribuzione delle perdite e sulle misure di rischio.

### Funzione della simulazione o della procedura computazionale

La simulazione Monte Carlo è necessaria per generare congiuntamente le traiettorie del regime sistemico e dei rating individuali, costruire le perdite dei due portafogli a partire dalle stesse repliche sottostanti e stimare le rispettive distribuzioni empiriche e misure di rischio.

### Ruolo dell’informazione, degli stati, degli scenari o dei vincoli

Il regime sistemico costituisce l’informazione comune che modifica le probabilità di migrazione di tutti i debitori. Gli stati creditizi rappresentano l’evoluzione individuale del merito creditizio, mentre le repliche Monte Carlo rappresentano possibili realizzazioni congiunte del sistema. Il vincolo strutturale del confronto è il mantenimento dello stesso investimento complessivo nei due portafogli, con eliminazione della posizione Lehman e riallocazione proporzionale del relativo investimento tra i debitori residui.



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

Il confronto deve essere effettuato utilizzando **le stesse repliche Monte Carlo sottostanti**.

In particolare:

1. la traiettoria del regime sistemico è la stessa per i due portafogli in ciascuna replica;
2. per i $39$ debitori comuni ai due portafogli vengono utilizzate le stesse traiettorie creditizie;
3. la traiettoria Lehman entra soltanto nel portafoglio concentrato;
4. cambiano esclusivamente la presenza della posizione Lehman e gli investimenti iniziali attribuiti alle posizioni residue.

Questa costruzione evita che le differenze tra i due portafogli siano prodotte da realizzazioni casuali differenti.

La simulazione di $N_{\mathrm{MC}}$ repliche produce:

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
N_{\mathrm{MC}}=50\,000.
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
- perdita media del portafoglio concentrato nelle repliche con e senza ingresso nello stato di crisi;
- distribuzione replica per replica della differenza

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

- repliche nelle quali lo stato $C$ non viene mai raggiunto;
- repliche nelle quali lo stato $C$ viene raggiunto almeno una volta.

### 5.3 Grafici

1. Distribuzione empirica della perdita del portafoglio concentrato con indicazione di VaR 95% e VaR 99%.
2. Confronto tra le distribuzioni empiriche delle perdite dei due portafogli, con particolare attenzione alla coda destra.
3. Confronto delle perdite del portafoglio concentrato nelle repliche con e senza ingresso nello stato di crisi.

### 5.4 Controlli

I controlli richiesti devono distinguere tra:

- proprietà verificabili direttamente sui dati, sulle simulazioni o sugli output numerici;
- proprietà logiche o teoriche del modello;
- controlli computazionali relativi all'accoppiamento delle repliche e all'impostazione della simulazione.

#### Controlli numerici

1. Tutte le righe della matrice di transizione del regime sistemico $Q$ devono sommare a uno.

2. Tutte le righe delle matrici di migrazione creditizia $P^{(O)}$, $P^{(S)}$ e $P^{(C)}$ devono sommare a uno.

7. Il portafoglio concentrato deve contenere esattamente $40$ debitori.

8. Il portafoglio controfattuale deve contenere esattamente $39$ debitori, dopo l'eliminazione della posizione Lehman Brothers.

9. L'investimento iniziale complessivo deve essere pari a $173$ milioni di dollari in entrambi i portafogli:

$$
V_0^{P,\mathrm{conc}}
=
V_0^{P,\mathrm{div}}
=
173.
$$

10. La riallocazione dei $25$ milioni inizialmente investiti in Lehman Brothers deve preservare le proporzioni relative degli investimenti dei $39$ debitori residui. Per ogni debitore $i\neq L$ deve risultare:

$$
V_{i,0}^{\mathrm{div}}
=
V_{i,0}\frac{173}{148}.
$$

12. Per ciascuna replica Monte Carlo, la perdita aggregata di ciascun portafoglio deve coincidere con la somma delle rispettive perdite individuali.

14. VaR e CVaR devono essere calcolati direttamente sulle distribuzioni empiriche delle perdite monetarie dei due portafogli, espresse in milioni di dollari. Il CVaR deve essere calcolato secondo la definizione mediante quantili adottata nel Capitolo 9.

15. Le principali misure di rischio devono mostrare una ragionevole stabilità al crescere del numero di repliche simulate. Il controllo costituisce una verifica empirica di sensibilità alla numerosità Monte Carlo e non una dimostrazione formale di convergenza.

#### Controlli logici o teorici

3. Lo stato di default $D$ deve essere assorbente in tutte le matrici di migrazione creditizia:

$$
p_{DD}^{(m)}
=
1.
$$

4. Tutti gli stati simulati devono appartenere agli insiemi definiti dal modello:

$$
\mathcal M
=
\{O,S,C\},
\qquad
\mathcal I
=
\{A,BBB,BB,B,D\}.
$$

5. All'interno di ciascuna replica Monte Carlo deve essere generata una sola traiettoria sistemica comune a tutti i debitori.

6. Condizionatamente alla traiettoria sistemica comune, le migrazioni dei differenti debitori devono essere generate mediante estrazioni casuali individuali e indipendenti.

#### Controlli computazionali

11. I $39$ debitori comuni ai due portafogli devono utilizzare esattamente le stesse traiettorie creditizie nelle due configurazioni. Il confronto deve quindi essere effettuato riutilizzando le medesime traiettorie sistemiche e creditizie sottostanti, così che le differenze osservate dipendano dalla composizione dei portafogli e non da differenti realizzazioni casuali.

13. Il seed assegnato, pari a $2026$, deve essere correttamente impostato come condizione per la riproducibilità della simulazione a parità di implementazione e ambiente computazionale. Il controllo riguarda la corretta impostazione del seed e non deve essere interpretato come garanzia astratta di riproducibilità esatta indipendentemente dall'ambiente computazionale.

## 6. Flusso logico-teorico risolutivo atteso

| Passo | Finalità risolutiva | Formula, definizione, proprietà o teorema | Applicazione nel caso | Output o controllo collegato |
|---:|---|---|---|---|
| 1 | Definire i processi stocastici e la struttura di dipendenza | Catena di Markov $M_t\in\{O,S,C\}$ con $M_0=S$ e matrice $Q$; matrici $P^{(m)}$ con stato $D$ assorbente; indipendenza condizionata delle migrazioni individuali data la traiettoria sistemica comune | Definizione delle regole di transizione del regime sistemico e dei rating individuali dei debitori | Controlli sulle matrici $Q$ e $P^{(m)}$, sul dominio degli stati, sullo stato assorbente e sulla traiettoria sistemica comune |
| 2 | Definire i due portafogli e la funzione di perdita | $L_i=V_{i,0}\varphi(X_{i,0},X_{i,4})$; $\operatorname{EAD}_i=V_{i,0}$; $\operatorname{LGD}=0.65$; portafoglio concentrato con $40$ debitori e portafoglio controfattuale con $39$ debitori; $V_{i,0}^{\mathrm{div}}=V_{i,0}\frac{173}{148}$ | Costruzione della struttura delle esposizioni e della mappa dei tassi di perdita o incremento di valore associati alle migrazioni creditizie | Controlli sulle dimensioni dei portafogli, sull'investimento totale pari a $173$ milioni e sulla conservazione delle proporzioni relative |
| 3 | Generare repliche Monte Carlo accoppiate | Simulazione di $N_{\mathrm{MC}}=50\,000$ repliche con seed $2026$; stesse traiettorie sistemiche e creditizie per i $39$ debitori comuni ai due portafogli | Generazione delle traiettorie sistemiche e creditizie e riutilizzo degli stessi shock nei due portafogli | Controlli sull'accoppiamento delle repliche, sulla riproducibilità e sull'indipendenza condizionata |
| 4 | Analizzare il ruolo del regime sistemico nella distribuzione delle perdite | Evento di ingresso in crisi $I_C^{(r)}=\mathbf{1}_{\{\exists t:M_t^{(r)}=C\}}$; probabilità empirica di crisi e valori medi condizionati | Separazione delle repliche con e senza ingresso nel regime $C$ e confronto delle perdite del portafoglio concentrato | Probabilità simulata di ingresso in $C$, Tabella 4 e Figura 3 |
| 5 | Stimare e confrontare le misure di rischio dei due portafogli | Distribuzione empirica, valore atteso, varianza, deviazione standard, $\operatorname{VaR}_{\alpha}$ e $\operatorname{CVaR}_{\alpha}$ per $\alpha\in\{0.95,0.99\}$ | Stima delle misure di rischio per il portafoglio concentrato e per quello controfattuale e calcolo dei differenziali $\Delta\rho$ | Tabella 3, Figure 1 e 2; controllo della stabilità Monte Carlo e del calcolo di VaR e CVaR |
| 6 | Valutare la differenza replica per replica e completare i controlli | $\Delta L^{(r)}=L_{\mathrm{div}}^{P,(r)}-L_{\mathrm{conc}}^{P,(r)}$; coerenza interna del modello e degli output | Analisi della distribuzione di $\Delta L^{(r)}$ e ricognizione conclusiva dei controlli previsti dalla Scheda Caso | Distribuzione di $\Delta L^{(r)}$, sintesi dei controlli e base quantitativa verificata per l'interpretazione finanziaria finale autonoma |

## 7. Scomposizione attesa in tappe

| Tappa | Titolo | Obiettivo | Input | Regime IA prevalente | Prompt virtuoso di riferimento | Oggetti teorici coinvolti | Operazione | Output | Controllo | Uso successivo |
|---:|---|---|---|:---:|---|---|---|---|---|---|
| 1 | Parametri e strutture del modello | Tradurre in strutture computazionali i parametri assegnati e verificarne la coerenza formale | Matrice $Q$, matrici $P^{(O)}$, $P^{(S)}$, $P^{(C)}$, funzione di perdita $\varphi$ rappresentata mediante la tabella dei tassi migration-based, LGD, $N_{\mathrm{MC}}$, $T$, seed | B | Prompt tappa 1 | Matrici di transizione, probabilità di transizione, stato assorbente, funzione di perdita, LGD | Inizializzare le strutture NumPy/Pandas e verificare le proprietà delle matrici e i domini degli stati | Strutture dati contenenti la calibrazione vincolante del modello | Controlli 1–4: somme di riga pari a 1, stato $D$ assorbente e appartenenza degli stati simulabili ai domini assegnati | Input per la costruzione dei portafogli e per la simulazione |
| 2 | Costruzione dei due portafogli | Costruire il portafoglio concentrato e il portafoglio controfattuale a investimento complessivo invariato | Composizione iniziale, investimenti $V_{i,0}$, posizione Lehman pari a $25$ milioni, regola di riallocazione proporzionale | B | Prompt tappa 2 | Investimento iniziale, concentrazione, riallocazione proporzionale, EAD | Costruire il portafoglio concentrato con $40$ debitori e il portafoglio controfattuale eliminando Lehman e moltiplicando gli investimenti dei $39$ debitori residui per $173/148$ | Tabelle 1 e 2; vettori degli investimenti dei due portafogli | Controlli 7–10: numerosità pari a $40$ e $39$, investimento complessivo pari a $173$ milioni in entrambi i portafogli e conservazione delle proporzioni relative tra i $39$ debitori residui | Input monetario per il calcolo delle perdite |
| 3 | Simulazione delle traiettorie sistemiche e creditizie | Generare repliche Monte Carlo comuni ai due portafogli e traiettorie creditizie individuali | Seed $2026$, $N_{\mathrm{MC}}=50\,000$, $T=4$, $M_0=S$, $Q$, matrici $P^{(m)}$, rating iniziali | B | Prompt tappa 3 | Catena di Markov, migrazioni condizionate al regime, indipendenza condizionata, stato assorbente | Per ogni replica simulare una sola traiettoria sistemica comune; condizionatamente a essa, simulare mediante estrazioni individuali le traiettorie dei $40$ debitori; conservare le stesse traiettorie dei $39$ debitori comuni per entrambi i portafogli | Traiettorie sistemiche e creditizie simulate | Controlli 5, 6, 11 e 13: traiettoria sistemica comune, estrazioni individuali condizionatamente indipendenti, identiche traiettorie creditizie per i $39$ debitori comuni e seed $2026$ correttamente impostato come condizione di riproducibilità | Input per il calcolo delle perdite |
| 4 | Perdite individuali e aggregate | Trasformare gli stati finali simulati in perdite monetarie per i due portafogli | Stati finali $X_{i,4}$, investimenti dei due portafogli, funzione di perdita $\varphi$ | B | Prompt tappa 4 | Perdita migration-based, $\mathrm{EAD}_i=V_{i,0}$, $\mathrm{LGD}=0.65$, aggregazione di portafoglio | Applicare $\varphi(X_{i,0},X_{i,4})$ agli stati finali simulati; nel default utilizzare $\varphi(r_0,D)=0.65$; aggregare le perdite individuali nel portafoglio concentrato e nel portafoglio controfattuale utilizzando le stesse repliche sottostanti | $L_{\mathrm{conc}}^P$, $L_{\mathrm{div}}^P$ e $\Delta L^{(r)}$ | Controllo 12: per ogni replica la perdita aggregata coincide con la somma delle perdite individuali; coerenza dell'applicazione della funzione di perdita e dell'accoppiamento dei due portafogli | Input per le misure di rischio e le analisi condizionate |
| 5 | Misure di rischio e analisi del regime sistemico | Stimare le principali misure di rischio e quantificare l'associazione tra ingresso in crisi e perdita di portafoglio | Campioni $L_{\mathrm{conc}}^P$, $L_{\mathrm{div}}^P$, traiettorie $M$ | B | Prompt tappa 5 | Distribuzione empirica, valore atteso, varianza, deviazione standard, VaR, CVaR, condizionamento per evento | Calcolare perdita media, varianza, deviazione standard, VaR e CVaR ai livelli $0.95$ e $0.99$ per entrambi i portafogli; calcolare $\Delta\rho$; identificare le repliche con ingresso almeno una volta in $C$ e confrontare le perdite medie del portafoglio concentrato | Tabelle 3 e 4 e misure sintetiche richieste | Controlli 14 e 15: VaR e CVaR calcolati sulle distribuzioni empiriche delle perdite monetarie, CVaR secondo la definizione mediante quantili del Capitolo 9 e ragionevole stabilità empirica delle principali misure di rischio al crescere della numerosità Monte Carlo | Input per la rappresentazione grafica e la valutazione finale |
| 6 | Rappresentazione grafica e controlli conclusivi | Produrre gli output grafici, analizzare la differenza replica per replica e verificare complessivamente l'esecuzione del caso | Distribuzioni simulate, $\Delta L^{(r)}$, indicatore di ingresso nel regime $C$ e risultati delle tappe precedenti | B | Prompt tappa 6 | Distribuzioni empiriche, misure di coda, confronto tra portafogli e repliche | Generare le Figure 1, 2 e 3; analizzare la distribuzione di $\Delta L^{(r)}$; ricostruire l'esito complessivo dei controlli previsti dalla Scheda Caso | Figure 1, 2 e 3; distribuzione di $\Delta L^{(r)}$; sintesi conclusiva dei controlli | Verifica complessiva dei controlli 1–15, coerenza tra tabelle, grafici e risultati numerici e distinzione tra verifiche numeriche, proprietà strutturali e controlli computazionali | Base quantitativa verificata per l'interpretazione finanziaria finale autonoma dello studente |

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
| Prompt tappa 1 | B | Tappa 1 | Tradurre i parametri assegnati nelle strutture computazionali del modello e verificarne la coerenza formale | Celle Markdown e codice per stati, matrici, funzione di perdita, LGD e parametri computazionali | Corretta implementazione di $Q$, delle matrici $P^{(O)}$, $P^{(S)}$, $P^{(C)}$, della funzione $\varphi$, dello stato $D$ assorbente, dei domini degli stati e dei parametri assegnati |
| Prompt tappa 2 | B | Tappa 2 | Costruire il portafoglio concentrato e il portafoglio controfattuale a investimento complessivo invariato | Celle Markdown, codice, Tabella 1 e Tabella 2 | Portafoglio concentrato con $40$ debitori, portafoglio controfattuale con $39$ debitori, investimento complessivo pari a $173$ milioni in entrambi i portafogli e corretta riallocazione proporzionale mediante il fattore $173/148$ |
| Prompt tappa 3 | B | Tappa 3 | Implementare la simulazione delle traiettorie sistemiche e creditizie comuni ai due portafogli | Celle Markdown e codice per simulazione del regime sistemico e delle traiettorie creditizie | Traiettoria sistemica unica per replica, indipendenza condizionata delle estrazioni individuali, stato $D$ assorbente, identiche traiettorie creditizie per i $39$ debitori comuni e seed $2026$ correttamente impostato |
| Prompt tappa 4 | B | Tappa 4 | Trasformare gli stati creditizi finali simulati in perdite individuali e aggregate per i due portafogli | Celle Markdown e codice per funzione di perdita, perdite individuali, aggregazione e $\Delta L^{(r)}$ | Corretta applicazione di $\varphi(X_{i,0},X_{i,4})$, coerenza con $\mathrm{LGD}=0.65$ e $\mathrm{EAD}_i=V_{i,0}$, additività delle perdite e utilizzo delle stesse traiettorie creditizie per i debitori comuni |
| Prompt tappa 5 | B | Tappa 5 | Calcolare e confrontare le principali misure di rischio e sviluppare l'analisi del regime sistemico | Celle Markdown, codice, Tabella 3 e Tabella 4 | Corretta implementazione di perdita media, varianza, deviazione standard, VaR, CVaR e $\Delta\rho$; corretta identificazione delle repliche con e senza ingresso in $C$; stabilità empirica delle principali misure di rischio |
| Prompt tappa 6 | B | Tappa 6 | Produrre gli output grafici, analizzare le differenze replica per replica e completare la ricognizione conclusiva dei controlli | Celle Markdown, codice, Figure 1, 2 e 3, distribuzione di $\Delta L^{(r)}$ e sintesi conclusiva dei controlli | Coerenza tra grafici, tabelle e risultati numerici; coerenza della distribuzione di $\Delta L^{(r)}$; copertura degli output richiesti e verifica complessiva dei controlli della Scheda Caso |
| Prompt C eventuale | C | Tappa interessata | Verificare una criticità specifica già individuata dallo studente | Eventuale sostituzione delle celle coinvolte | Criticità accolta oppure respinta |


## 9. Struttura attesa del notebook

Il notebook deve riflettere direttamente la scomposizione operativa validata attraverso il Prompt 3. Nel presente caso, tale scomposizione è articolata in sei tappe operative. Ogni tappa può produrre più celle Markdown, codice e output, purché rimanga riconoscibile come modulo logico unitario.

### Apertura del notebook

**Prompt di riferimento:** Prompt 1.

- Cella Markdown: titolo, contesto Lehman Brothers 2008, domanda quantitativa e Scheda Caso come specifica vincolante.

Dopo la cella iniziale prodotta con il Prompt 1, il notebook deve riportare:

- una cella Markdown con il Flusso logico-teorico risolutivo validato attraverso il Prompt 2;
- una cella Markdown con la scomposizione operativa in tappe input-output validata attraverso il Prompt 3.

Queste due celle documentano le decisioni di progettazione che governano lo sviluppo successivo del notebook e devono precedere le celle operative delle singole tappe.

### Tappa 1 — Parametri e strutture del modello

**Prompt di riferimento:** Prompt tappa 1 — Regime B.

- Cella Markdown: funzione della tappa e richiamo dei parametri vincolanti.
- Cella codice: definizione degli stati sistemici $O$, $S$, $C$ e degli stati creditizi $A$, $BBB$, $BB$, $B$, $D$.
- Cella codice: definizione della matrice $Q$.
- Cella codice: definizione delle matrici $P^{(O)}$, $P^{(S)}$, $P^{(C)}$.
- Cella codice: definizione della funzione di perdita $\varphi$ mediante la tabella dei tassi migration-based.
- Cella codice: definizione della LGD costante pari a $0.65$ e dell'ipotesi $\mathrm{EAD}_i=V_{i,0}$.
- Cella codice: impostazione di $N_{\mathrm{MC}}=50\,000$, $T=4$ e seed $2026$.
- Output: controllo delle somme di riga di $Q$ e delle matrici $P^{(m)}$.
- Output: controllo dello stato $D$ assorbente.
- Controllo: appartenenza degli stati ai domini assegnati.

### Tappa 2 — Costruzione dei due portafogli

**Prompt di riferimento:** Prompt tappa 2 — Regime B.

- Cella Markdown: struttura del portafoglio concentrato e regola di costruzione del portafoglio controfattuale.
- Cella codice: costruzione del portafoglio concentrato con $40$ debitori e investimento complessivo pari a $173$ milioni di dollari.
- Cella codice: eliminazione della posizione Lehman Brothers, pari a $25$ milioni di dollari.
- Cella codice: riallocazione proporzionale dell'investimento Lehman sui $39$ debitori residui mediante

$$
V_{i,0}^{\mathrm{div}}
=
V_{i,0}\frac{173}{148}.
$$

- Output: Tabella 1 — portafoglio iniziale concentrato.
- Output: Tabella 2 — portafoglio controfattuale.
- Controllo: portafoglio concentrato composto da $40$ debitori.
- Controllo: portafoglio controfattuale composto da $39$ debitori.
- Controllo: investimento complessivo pari a $173$ milioni di dollari in entrambi i portafogli.
- Controllo: conservazione delle proporzioni relative degli investimenti dei $39$ debitori residui.

### Tappa 3 — Simulazione delle traiettorie sistemiche e creditizie

**Prompt di riferimento:** Prompt tappa 3 — Regime B.

- Cella Markdown: funzione della tappa e struttura della simulazione Monte Carlo.
- Cella codice: inizializzazione del generatore casuale mediante il seed assegnato $2026$.
- Cella codice: simulazione, per ciascuna replica, di una sola traiettoria sistemica $M_t$ con stato iniziale $M_0=S$.
- Cella codice: utilizzo della medesima traiettoria sistemica per tutti i $40$ debitori della replica.
- Cella codice: simulazione delle traiettorie creditizie mediante la matrice $P^{(M_t)}$ coerente con il regime sistemico corrente.
- Cella codice: utilizzo, condizionatamente alla traiettoria sistemica comune, di estrazioni casuali individuali e indipendenti per i differenti debitori.
- Cella codice: conservazione delle medesime traiettorie creditizie dei $39$ debitori comuni ai due portafogli.
- Output sintetico: dimensioni delle strutture simulate ed eventuali traiettorie campione utili alla verifica del meccanismo.
- Controllo: tutti gli stati simulati appartengono agli insiemi previsti.
- Controllo: esiste una sola traiettoria sistemica comune per replica.
- Controllo: le estrazioni individuali sono distinte, condizionatamente alla traiettoria sistemica comune.
- Controllo: permanenza nello stato $D$ dopo il default.
- Controllo computazionale: i $39$ debitori comuni utilizzano esattamente le stesse traiettorie creditizie nei due portafogli.
- Controllo computazionale: il seed $2026$ è correttamente impostato come condizione per la riproducibilità della simulazione.

### Tappa 4 — Perdite individuali e di portafoglio

**Prompt di riferimento:** Prompt tappa 4 — Regime B.

- Cella Markdown: passaggio dagli stati creditizi finali alle perdite monetarie.
- Cella codice: calcolo, per ciascun debitore, della perdita

$$
L_i
=
V_{i,0}\,
\varphi(X_{i,0},X_{i,4}).
$$

- Cella codice: applicazione del tasso di perdita da default

$$
\varphi(r_0,D)=0.65,
$$

coerente con l'ipotesi $\mathrm{LGD}=0.65$.

- Cella codice: calcolo delle perdite individuali del portafoglio concentrato.
- Cella codice: calcolo delle perdite individuali del portafoglio controfattuale sui medesimi stati finali dei $39$ debitori comuni, utilizzando gli investimenti riallocati $V_{i,0}^{\mathrm{div}}$.
- Cella codice: aggregazione delle perdite individuali e costruzione di $L_{\mathrm{conc}}^P$ e $L_{\mathrm{div}}^P$.
- Cella codice: calcolo della differenza replica per replica

$$
\Delta L^{(r)}
=
L_{\mathrm{div}}^{P,(r)}
-
L_{\mathrm{conc}}^{P,(r)}.
$$

- Controllo: per ciascuna replica, la perdita aggregata di ciascun portafoglio coincide con la somma delle rispettive perdite individuali.
- Controllo: i due portafogli utilizzano le stesse traiettorie sottostanti per i $39$ debitori comuni.

### Tappa 5 — Misure di rischio e analisi del regime sistemico

**Prompt di riferimento:** Prompt tappa 5 — Regime B.

- Cella Markdown: convenzioni operative per perdita media, varianza, deviazione standard, VaR e CVaR.
- Cella Markdown: richiamo esplicito alla definizione del CVaR mediante quantili adottata nel Capitolo 9.
- Cella codice: calcolo delle statistiche descrittive per il portafoglio concentrato e per il portafoglio controfattuale.
- Cella codice: calcolo di $\operatorname{VaR}_{0.95}$ e $\operatorname{VaR}_{0.99}$ sulle distribuzioni empiriche delle perdite monetarie.
- Cella codice: calcolo di $\operatorname{CVaR}_{0.95}$ e $\operatorname{CVaR}_{0.99}$ secondo la definizione mediante quantili adottata nel Capitolo 9.
- Cella codice: calcolo dei differenziali

$$
\Delta\rho
=
\rho(L_{\mathrm{div}}^P)
-
\rho(L_{\mathrm{conc}}^P).
$$

- Cella codice: identificazione delle repliche nelle quali il regime $C$ viene raggiunto almeno una volta.
- Cella codice: calcolo della probabilità simulata di ingresso almeno una volta nel regime $C$.
- Cella codice: calcolo della perdita media del portafoglio concentrato nelle repliche con e senza ingresso nel regime $C$.
- Output: Tabella 3 — misure di rischio.
- Output: Tabella 4 — regime sistemico e perdita.
- Controllo: VaR e CVaR sono calcolati direttamente sulle distribuzioni empiriche delle perdite monetarie.
- Controllo: le principali misure di rischio mostrano una ragionevole stabilità al crescere della numerosità Monte Carlo.
- Nota sul controllo di stabilità: il confronto costituisce una verifica empirica di sensibilità alla numerosità delle simulazioni e non una dimostrazione formale di convergenza.

### Tappa 6 — Rappresentazione grafica, differenze replica per replica e controlli conclusivi

**Prompt di riferimento:** Prompt tappa 6 — Regime B.

- Cella codice/output: Figura 1 — distribuzione empirica della perdita del portafoglio concentrato con indicazione di VaR 95% e VaR 99%.
- Cella codice/output: Figura 2 — confronto tra le distribuzioni empiriche delle perdite del portafoglio concentrato e del portafoglio controfattuale, con particolare attenzione alla coda destra.
- Cella codice/output: Figura 3 — confronto delle perdite del portafoglio concentrato nelle repliche con e senza ingresso nel regime $C$.
- Cella codice/output: costruzione e analisi della distribuzione empirica di

$$
\Delta L^{(r)}
=
L_{\mathrm{div}}^{P,(r)}
-
L_{\mathrm{conc}}^{P,(r)}.
$$

- Cella Markdown: ricognizione complessiva dell'esito dei controlli richiesti dalla Scheda Caso.
- Controllo: coerenza della distribuzione di $\Delta L^{(r)}$ con i due campioni di perdita.
- Controllo: coerenza tra grafici, tabelle e risultati numerici.
- Controllo: verifica conclusiva della copertura dei controlli previsti dalla Scheda Caso.

### Interpretazione finanziaria finale dello studente

Dopo il completamento e la validazione delle sei tappe operative, il notebook deve contenere una cella Markdown dedicata all'interpretazione finanziaria finale.

L'interpretazione deve essere formulata autonomamente dallo studente e deve distinguere almeno:

- effetto del regime sistemico sulla distribuzione e sulla coda delle perdite;
- ruolo della posizione Lehman nel portafoglio concentrato;
- differenza tra indipendenza condizionata e dipendenza incondizionata;
- significato finanziario di VaR e CVaR;
- effetto della riallocazione proporzionale dell'investimento Lehman;
- modifica della composizione per rating prodotta dalla riallocazione;
- interpretazione della distribuzione di $\Delta L^{(r)}$;
- assenza di identificazione del confronto come effetto puro della sola concentrazione;
- limiti dell'ipotesi di matrici omogenee e di LGD costante;
- differenza tra simulazione didattica ex ante e successiva realizzazione storica.

Per questa fase non è previsto un prompt IA obbligatorio. L'eventuale Regime C può essere attivato soltanto se lo studente individua una criticità specifica da verificare; l'IA non deve produrre, riscrivere o completare l'interpretazione finale al posto dello studente.

## 10. Criteri di validazione del notebook

Il notebook è considerato valido se:

1. implementa la specifica teorico-matematica della Scheda Caso senza modificarla;

2. utilizza esclusivamente le matrici, gli investimenti, la funzione di perdita, la LGD, il numero di repliche, il seed e gli altri parametri assegnati;

3. rispetta la scomposizione in tappe input-output validata;

4. mantiene coerenti la notazione matematica e le corrispondenti variabili computazionali;

5. utilizza correttamente la matrice di transizione del regime sistemico $Q$ e le matrici di migrazione creditizia $P^{(O)}$, $P^{(S)}$ e $P^{(C)}$, verificando che le rispettive righe sommino a uno;

6. mantiene lo stato di default $D$ assorbente in tutte le matrici di migrazione creditizia;

7. utilizza esclusivamente stati appartenenti ai domini assegnati:

$$
\mathcal M
=
\{O,S,C\},
\qquad
\mathcal I
=
\{A,BBB,BB,B,D\};
$$

8. genera, per ciascuna replica Monte Carlo, una sola traiettoria del regime sistemico comune a tutti i debitori;

9. preserva, condizionatamente alla traiettoria sistemica comune, l'indipendenza delle estrazioni individuali utilizzate per simulare le migrazioni dei differenti debitori;

10. costruisce correttamente il portafoglio concentrato con $40$ debitori e investimento complessivo pari a $173$ milioni di dollari;

11. costruisce correttamente il portafoglio controfattuale eliminando la posizione Lehman Brothers e riallocando i relativi $25$ milioni proporzionalmente sui $39$ debitori residui secondo

$$
V_{i,0}^{\mathrm{div}}
=
V_{i,0}\frac{173}{148};
$$

12. mantiene invariato l'investimento complessivo nei due portafogli:

$$
V_0^{P,\mathrm{conc}}
=
V_0^{P,\mathrm{div}}
=
173;
$$

13. preserva le proporzioni relative degli investimenti dei $39$ debitori residui nel passaggio dal portafoglio concentrato al portafoglio controfattuale;

14. applica correttamente la funzione di perdita

$$
L_i
=
V_{i,0}\,
\varphi(X_{i,0},X_{i,4}),
$$

utilizzando nel default

$$
\varphi(r_0,D)=0.65,
$$

in coerenza con le ipotesi

$$
\mathrm{LGD}=0.65,
\qquad
\mathrm{EAD}_i=V_{i,0};
$$

15. utilizza, per i $39$ debitori comuni ai due portafogli, esattamente le stesse traiettorie creditizie simulate, così che il confronto dipenda dalla diversa composizione dei portafogli e non da differenti realizzazioni casuali;

16. riconcilia, per ciascuna replica e per ciascun portafoglio, la perdita aggregata con la somma delle rispettive perdite individuali;

17. produce tutti gli output numerici, tabellari e grafici richiesti dalla Scheda Caso;

18. calcola VaR e CVaR direttamente sulle distribuzioni empiriche delle perdite monetarie, espresse in milioni di dollari;

19. implementa il CVaR secondo la definizione mediante quantili adottata nel Capitolo 9;

20. utilizza il seed assegnato $2026$ come condizione per la riproducibilità della simulazione a parità di implementazione e ambiente computazionale;

21. verifica che le principali misure di rischio mostrino una ragionevole stabilità al crescere del numero di repliche simulate; tale controllo costituisce una verifica empirica di sensibilità alla numerosità Monte Carlo e non una dimostrazione formale di convergenza;

22. calcola correttamente la probabilità empirica che il regime $C$ venga raggiunto almeno una volta nell'orizzonte considerato;

23. calcola la perdita media del portafoglio concentrato separatamente nelle repliche con e senza ingresso nel regime $C$;

24. costruisce correttamente la differenza replica per replica

$$
\Delta L^{(r)}
=
L_{\mathrm{div}}^{P,(r)}
-
L_{\mathrm{conc}}^{P,(r)};
$$

25. mantiene coerenza tra distribuzioni simulate, misure di rischio, tabelle, grafici e differenze replica per replica;

26. conclude con una sintesi esplicita dei controlli effettuati, distinguendo:
   - controlli numerici;
   - proprietà logiche o teoriche del modello;
   - controlli computazionali relativi all'accoppiamento delle repliche e all'impostazione del seed;

27. conclude con un'interpretazione finanziaria coerente con gli output e con i limiti del modello, senza attribuire alla simulazione didattica una valenza di previsione storica retrospettiva del successivo default di Lehman Brothers;

28. riconosce esplicitamente che il confronto tra portafoglio concentrato e portafoglio controfattuale non identifica un effetto puro della sola concentrazione, poiché la riallocazione proporzionale modifica anche la distribuzione dell'investimento tra classi di rating.

Un eventuale Prompt in Regime C non costituisce condizione necessaria di validità del notebook. Esso interviene soltanto quando lo studente individua una criticità specifica da verificare.


## 11. Calibrazione docente

La seguente calibrazione è riferita a:

$$
N_{\mathrm{MC}}=50\,000,
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
- la perdita media del portafoglio concentrato nelle repliche che visitano $C$ è circa $18.25$ milioni;
- la perdita media del portafoglio concentrato nelle repliche che non visitano $C$ è circa $8.12$ milioni.

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
- verifica dell'utilizzo delle stesse traiettorie creditizie per i debitori comuni ai due portafogli;
- controllo della funzione di perdita;
- riconciliazione fra perdite individuali e perdita aggregata;
- riproducibilità;
- stabilità delle misure di rischio aumentando il numero delle simulazioni;
- confronto qualitativo tra repliche con e senza condizioni sistemiche di crisi.

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
5. confrontare i due portafogli utilizzando le stesse traiettorie creditizie per i debitori comuni;
6. stimare e interpretare perdita attesa, dispersione, VaR e CVaR;
7. valutare correttamente gli effetti della riallocazione senza identificarli automaticamente con un effetto puro della sola concentrazione;
8. distinguere i risultati prodotti dal modello didattico dagli eventi storici successivamente osservati;
9. formulare autonomamente un'interpretazione finanziaria coerente con le ipotesi, gli output e i limiti del modello.

### Calibrazione qualitativa

Il caso è considerato didatticamente ben calibrato se:

- la posizione Lehman costituisce una concentrazione iniziale economicamente rilevante;
- la sua eliminazione e la riallocazione proporzionale modificano in modo osservabile la distribuzione delle perdite;
- il controfattuale non produce necessariamente una riduzione uniforme di tutte le misure di rischio;
- il regime sistemico comune genera differenze chiaramente osservabili tra repliche con e senza ingresso nello stato di crisi;
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