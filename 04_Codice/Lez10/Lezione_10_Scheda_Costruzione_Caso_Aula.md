# Lezione 10 — Scheda Costruzione Caso Aula

## 1. Identificazione del caso

- **Lezione:** 10 — Applicazione in Python: rischio di credito
- **Tipo di caso:** Aula
- **Titolo:** China Evergrande 2021: crisi immobiliare, dipendenza sistemica e controllo della concentrazione creditizia
- **Nome file previsto:** `Lezione_10_Scheda_Costruzione_Caso_Aula.md`
- **Destinatari:** studenti del secondo anno della Laurea Magistrale in Banca e Risk Management
- **Uso previsto:** sviluppo guidato in aula di un caso applicativo basato su una struttura markoviana a due livelli, finalizzato a simulare il rischio di credito di un portafoglio esposto al settore immobiliare cinese e a valutare gli effetti di una politica di contenimento della concentrazione single-name.

## 2. Contesto e motivazione

Il caso è ambientato nell'**estate del 2021**, durante la fase di rapido deterioramento delle condizioni finanziarie del settore immobiliare cinese e del merito creditizio di China Evergrande Group.

Il punto di osservazione è deliberatamente ex ante. Lo studente assume il ruolo di un risk manager che deve valutare il rischio a un anno di un portafoglio di esposizioni creditizie verso emittenti cinesi con differenti classi di rating.

La posizione verso China Evergrande presenta un investimento iniziale significativamente superiore a quello delle singole altre posizioni. Il portafoglio è quindi esposto contemporaneamente:

1. al deterioramento creditizio dei singoli debitori;
2. a un fattore sistemico comune legato alle condizioni del comparto immobiliare e del credito;
3. alla concentrazione della posizione verso Evergrande.

Il regime sistemico può trovarsi in una condizione di normalizzazione, stress o crisi e può cambiare da un trimestre al successivo. A ogni regime corrisponde una diversa matrice di migrazione dei rating.

Le transizioni dei singoli debitori sono indipendenti condizionatamente alla traiettoria del regime sistemico comune, ma non sono indipendenti incondizionatamente.

Il caso introduce inoltre un ulteriore elemento. La severità della perdita in caso di default dipende dalle condizioni sistemiche prevalenti nel periodo nel quale il default si verifica. Una situazione di crisi riduce quindi non soltanto la qualità delle transizioni creditizie, ma anche il recovery rate.

La simulazione Monte Carlo è necessaria per generare congiuntamente:

- la traiettoria del regime sistemico;
- le migrazioni creditizie dei debitori;
- il momento degli eventuali default;
- la LGD associata al regime nel quale il default avviene;
- la perdita aggregata di portafoglio.

Il caso comprende inoltre un confronto con una politica di gestione del rischio. Viene imposto un limite massimo del $10\%$ all'investimento iniziale verso un singolo debitore. La posizione Evergrande viene conseguentemente ridotta e l'investimento liberato viene riallocato sulle posizioni inizialmente classificate BBB e BB.

Le matrici di transizione, la composizione del portafoglio, le LGD e gli altri parametri sono **dati didattici calibrati**. Non costituiscono stime storiche delle probabilità effettive di transizione, delle recovery o delle perdite di China Evergrande Group.

**Riferimenti storici docente:** comunicazioni societarie China Evergrande Group; comunicazioni delle principali agenzie di rating relative ai downgrade del 2021; documentazione relativa al successivo default sulle obbligazioni offshore.

## 3. Domanda quantitativa e obiettivo didattico

### Domanda quantitativa

Quale distribuzione della perdita a un anno emerge per il portafoglio se:

1. le condizioni sistemiche del settore evolvono secondo una catena di Markov;
2. le probabilità di migrazione dei rating dipendono dal regime sistemico corrente;
3. i debitori appartengono inizialmente a differenti classi di rating;
4. le migrazioni individuali sono indipendenti condizionatamente al regime comune;
5. la perdita da migrazione dipende dal rating finale;
6. la LGD in caso di default dipende dal regime sistemico nel quale il default si verifica?

Quali valori assumono perdita attesa, dispersione, VaR e CVaR?

Come cambia la distribuzione della perdita se viene introdotto un limite di concentrazione single-name pari al $10\%$ dell'investimento complessivo, riducendo la posizione Evergrande e riallocando l'investimento sulle posizioni BBB e BB?

### Obiettivo didattico

Lo studente deve costruire e simulare la sequenza:

$$
\text{regime sistemico}
\longrightarrow
\text{migrazioni creditizie condizionate}
\longrightarrow
\text{tempo e regime di eventuale default}
\longrightarrow
\text{perdite individuali}
\longrightarrow
\text{perdita di portafoglio}
\longrightarrow
\widehat F_{L^P}
\longrightarrow
\widehat{\operatorname{VaR}},
\widehat{\operatorname{CVaR}}.
$$

Il caso deve inoltre consentire di distinguere:

- dipendenza sistemica e rischio idiosincratico;
- probabilità di default e severità della perdita;
- rischio di migrazione e rischio di default;
- composizione iniziale del portafoglio e EAD;
- misura del rischio e decisione di gestione della concentrazione.

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
\{N,S,C\},
$$

dove:

- $N$ = normalizzazione delle condizioni finanziarie;
- $S$ = stress del settore immobiliare e del credito;
- $C$ = crisi settoriale e finanziaria.

Il regime iniziale è

$$
M_0=S.
$$

La matrice trimestrale di transizione del regime è

$$
Q=
\begin{pmatrix}
0.84 & 0.15 & 0.01\\
0.20 & 0.62 & 0.18\\
0.08 & 0.30 & 0.62
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
\{BBB,BB,B,CCC,D\}.
$$

Lo stato $D$ rappresenta il default ed è assorbente.

Le classi utilizzate costituiscono bucket interni del modello didattico e non devono essere identificate automaticamente con uno specifico rating storico assegnato da una determinata agenzia.

### 4.3 Matrici di migrazione condizionate al regime

Nel regime di normalizzazione:

$$
P^{(N)}
=
\begin{pmatrix}
0.955 & 0.038 & 0.005 & 0.001 & 0.001\\
0.025 & 0.925 & 0.038 & 0.009 & 0.003\\
0.005 & 0.035 & 0.885 & 0.060 & 0.015\\
0.001 & 0.004 & 0.025 & 0.900 & 0.070\\
0     & 0     & 0     & 0     & 1
\end{pmatrix}.
$$

Nel regime di stress:

$$
P^{(S)}
=
\begin{pmatrix}
0.925 & 0.060 & 0.011 & 0.003 & 0.001\\
0.012 & 0.875 & 0.085 & 0.022 & 0.006\\
0.003 & 0.020 & 0.810 & 0.135 & 0.032\\
0     & 0.003 & 0.022 & 0.855 & 0.120\\
0     & 0     & 0     & 0     & 1
\end{pmatrix}.
$$

Nel regime di crisi:

$$
P^{(C)}
=
\begin{pmatrix}
0.830 & 0.115 & 0.035 & 0.015 & 0.005\\
0.004 & 0.745 & 0.145 & 0.075 & 0.031\\
0     & 0.008 & 0.650 & 0.242 & 0.100\\
0     & 0     & 0.008 & 0.692 & 0.300\\
0     & 0     & 0     & 0     & 1
\end{pmatrix}.
$$

Per ogni debitore:

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

Condizionatamente alla traiettoria sistemica

$$
M_0,M_1,M_2,M_3,
$$

le transizioni creditizie dei differenti debitori sono assunte indipendenti.

Per $i\neq r$:

$$
X_{i,t+1}
\perp
X_{r,t+1}
\mid
M_t,X_{i,t},X_{r,t}.
$$

La dipendenza incondizionata deriva dall'esposizione di tutti i debitori alla stessa traiettoria del regime sistemico.

### 4.5 Portafoglio iniziale

Indichiamo con $V_{i,0}$ l'investimento iniziale nella posizione creditizia verso il debitore $i$.

Il portafoglio contiene $36$ debitori e presenta un investimento complessivo pari a

$$
V_0^P
=
\sum_{i=1}^{36}V_{i,0}
=
200.
$$

Gli importi sono espressi in milioni di dollari.

| Gruppo | Numero debitori | Rating iniziale | Investimento iniziale per debitore | Investimento iniziale complessivo |
|---|---:|:---:|---:|---:|
| China Evergrande Group | 1 | B | 30 | 30 |
| Debitori BBB | 10 | BBB | 6 | 60 |
| Debitori BB | 10 | BB | 5 | 50 |
| Altri debitori B | 10 | B | 4 | 40 |
| Debitori CCC | 5 | CCC | 4 | 20 |
| **Totale** | **36** |  |  | **200** |

La posizione Evergrande rappresenta quindi

$$
\frac{30}{200}
=
15\%
$$

dell'investimento iniziale complessivo.

Evergrande segue la stessa matrice di migrazione degli altri debitori appartenenti alla medesima classe creditizia. La sua specificità nel modello deriva dall'elevato investimento iniziale.

### 4.6 Funzione di perdita in assenza di default

Se il debitore non entra in default entro l'orizzonte, la perdita dipende dal rating iniziale e dal rating finale.

Si definisce

$$
L_i^{M}
=
V_{i,0}\,
\varphi(X_{i,0},X_{i,4}),
$$

dove $\varphi(r_0,r_4)$ rappresenta il tasso di perdita migration-based.

La calibrazione didattica è:

| Rating iniziale $\backslash$ finale | BBB | BB | B | CCC |
|---|---:|---:|---:|---:|
| BBB | 0.00 | 0.04 | 0.11 | 0.26 |
| BB | -0.03 | 0.00 | 0.07 | 0.19 |
| B | -0.07 | -0.04 | 0.00 | 0.13 |
| CCC | -0.12 | -0.08 | -0.04 | 0.00 |

I valori negativi rappresentano incrementi di valore rispetto al riferimento iniziale prodotti da un miglioramento del rating.

### 4.7 Default e LGD dipendente dal regime

Si definisce il tempo di default del debitore $i$ come

$$
\tau_i
=
\min
\left\{
t\in\{1,\ldots,4\}:
X_{i,t}=D
\right\}.
$$

Se il debitore entra in default durante la transizione dal trimestre $t$ al trimestre $t+1$, la matrice utilizzata per tale transizione è determinata da $M_t$.

La LGD dipende dal regime sistemico in tale momento:

$$
\operatorname{LGD}^{(N)}
=
0.55,
$$

$$
\operatorname{LGD}^{(S)}
=
0.70,
$$

$$
\operatorname{LGD}^{(C)}
=
0.85.
$$

Nel caso didattico, si assume

$$
\operatorname{EAD}_i
=
V_{i,0}.
$$

Questa uguaglianza è una ipotesi semplificatrice specifica del caso e non costituisce una identificazione generale tra investimento iniziale ed $\operatorname{EAD}$.

Se $\tau_i=t+1$, la perdita da default è quindi

$$
L_i^D
=
V_{i,0}
\operatorname{LGD}^{(M_t)}.
$$

La perdita individuale complessiva è pertanto

$$
L_i
=
\begin{cases}
V_{i,0}\varphi(X_{i,0},X_{i,4}),
&
\text{se }\tau_i>4,\\[2mm]
V_{i,0}\operatorname{LGD}^{(M_{\tau_i-1})},
&
\text{se }\tau_i\leq4.
\end{cases}
$$

La perdita da default dipende quindi non soltanto dallo stato finale, ma anche dalla traiettoria che conduce al default.

### 4.8 Portafoglio con limite di concentrazione

Viene considerata una politica alternativa che impone

$$
\max_i
\frac{V_{i,0}}{V_0^P}
\leq
10\%.
$$

Poiché

$$
V_0^P=200,
$$

l'investimento massimo consentito verso un singolo debitore è

$$
20.
$$

La posizione Evergrande viene pertanto ridotta da

$$
30
$$

a

$$
20.
$$

L'investimento liberato,

$$
10,
$$

viene riallocato esclusivamente sulle posizioni inizialmente classificate BBB e BB, in proporzione ai rispettivi investimenti iniziali.

L'investimento complessivo iniziale di tali gruppi è

$$
60+50=110.
$$

Per ciascun debitore BBB:

$$
V_{i,0}^{\mathrm{lim}}
=
6+
10\frac{6}{110}
=
6.54545.
$$

Per ciascun debitore BB:

$$
V_{i,0}^{\mathrm{lim}}
=
5+
10\frac{5}{110}
=
5.45455.
$$

Le altre posizioni restano invariate.

La struttura del portafoglio dopo l'applicazione del limite è:

| Gruppo | Numero debitori | Rating iniziale | Investimento per debitore | Investimento complessivo |
|---|---:|:---:|---:|---:|
| China Evergrande Group | 1 | B | 20.0000 | 20.0000 |
| Debitori BBB | 10 | BBB | 6.5455 | 65.4545 |
| Debitori BB | 10 | BB | 5.4545 | 54.5455 |
| Altri debitori B | 10 | B | 4.0000 | 40.0000 |
| Debitori CCC | 5 | CCC | 4.0000 | 20.0000 |
| **Totale** | **36** |  |  | **200.0000** |

L'investimento complessivo rimane quindi invariato:

$$
V_0^{P,\mathrm{base}}
=
V_0^{P,\mathrm{lim}}
=
200.
$$

La politica non costituisce una semplice eliminazione della posizione Evergrande: essa combina riduzione della concentrazione e riallocazione verso classi creditizie iniziali migliori.

### 4.9 Perdite dei due portafogli

Per la replica Monte Carlo $r$, la perdita del portafoglio iniziale è

$$
L_{\mathrm{base}}^{P,(r)}
=
\sum_{i=1}^{36}
L_i^{(r)}.
$$

Applicando agli stessi scenari simulati il vettore degli investimenti soggetto al limite si ottiene

$$
L_{\mathrm{lim}}^{P,(r)}.
$$

Il confronto deve utilizzare **esattamente le stesse traiettorie sistemiche e creditizie** per i due portafogli.

Cambiano esclusivamente gli investimenti iniziali attribuiti alle posizioni.

La simulazione produce quindi i due campioni:

$$
L_{\mathrm{base}}^{P,(1)},
\ldots,
L_{\mathrm{base}}^{P,(N_{\mathrm{MC}})}
$$

e

$$
L_{\mathrm{lim}}^{P,(1)},
\ldots,
L_{\mathrm{lim}}^{P,(N_{\mathrm{MC}})}.
$$

Per ciascuna misura di rischio $\rho$ si definisce

$$
\Delta\rho
=
\rho(L_{\mathrm{lim}}^P)
-
\rho(L_{\mathrm{base}}^P).
$$

Una quantità aggiuntiva utile è la differenza scenario per scenario:

$$
\Delta L^{(r)}
=
L_{\mathrm{lim}}^{P,(r)}
-
L_{\mathrm{base}}^{P,(r)}.
$$

### 4.10 Simulazione di una replica

Per ogni replica $r$:

1. si pone $M_0=S$;
2. per $t=0,\ldots,3$, le migrazioni dei debitori vengono simulate utilizzando $P^{(M_t)}$;
3. per ogni debitore che entra per la prima volta in $D$ vengono registrati il tempo di default e il regime $M_t$ che ha governato la transizione;
4. condizionatamente a $M_t$, le estrazioni individuali dei differenti debitori sono indipendenti;
5. per $t<3$, il nuovo regime $M_{t+1}$ viene simulato mediante $Q$;
6. per i debitori sopravvissuti si applica la funzione di perdita migration-based;
7. per i debitori in default si applica la LGD associata al regime nel quale il default si è verificato;
8. si calcola la perdita del portafoglio iniziale;
9. mantenendo invariati gli stessi scenari, si applica il vettore degli investimenti soggetto al limite e si calcola la seconda perdita di portafoglio.

Il numero base di simulazioni è

$$
N_{\mathrm{MC}}
=
50\,000.
$$

Per la riproducibilità del Caso Aula, viene utilizzato il seed

$$
2027.
$$

### 4.11 Ipotesi

1. Il regime sistemico è markoviano e omogeneo nel tempo.
2. Le matrici $P^{(N)}$, $P^{(S)}$ e $P^{(C)}$ sono omogenee all'interno del rispettivo regime.
3. Il default è assorbente.
4. A parità di rating corrente e regime sistemico, i debitori condividono la stessa matrice di migrazione.
5. Le transizioni individuali sono indipendenti condizionatamente al regime comune.
6. Gli investimenti iniziali sono deterministici.
7. Nel modello didattico si assume $\operatorname{EAD}_i=V_{i,0}$.
8. La LGD dipende dal regime sistemico che governa la transizione nel default.
9. Le LGD sono deterministiche condizionatamente al regime.
10. La funzione di perdita migration-based è deterministica condizionatamente ai rating iniziale e finale.
11. Il modello utilizza probabilità fisiche.
12. Non vengono utilizzate probabilità risk-neutral.
13. Le matrici, le LGD e gli investimenti costituiscono una calibrazione didattica.

## 5. Output richiesti

### 5.1 Risultati numerici

Per il portafoglio iniziale e per il portafoglio soggetto al limite:

- distribuzione simulata della perdita;
- perdita media;
- varianza;
- deviazione standard;
- $VaR_{0.95}$;
- $CVaR_{0.95}$;
- $VaR_{0.99}$;
- $CVaR_{0.99}$.

Inoltre:

- numero medio di default;
- probabilità di raggiungere almeno una volta il regime $C$;
- perdita media condizionata al raggiungimento o meno del regime $C$;
- differenze tra le misure di rischio dei due portafogli;
- distribuzione di $\Delta L$;
- incidenza della politica di concentrazione sulle misure di coda.

### 5.2 Tabelle

**Tabella 1 — Portafoglio iniziale**

Numero di debitori, rating iniziale, investimento individuale e investimento complessivo.

**Tabella 2 — Portafoglio soggetto al limite**

Investimenti dopo la riduzione della posizione Evergrande e la riallocazione.

**Tabella 3 — Misure di rischio**

Confronto tra:

- portafoglio iniziale;
- portafoglio soggetto al limite;
- differenza tra le rispettive misure.

**Tabella 4 — Regime sistemico e perdita**

Confronto, per il portafoglio iniziale, tra scenari con e senza ingresso nel regime $C$.

### 5.3 Grafici

1. Distribuzione empirica della perdita del portafoglio iniziale con indicazione di VaR 95% e VaR 99%.
2. Confronto delle code delle distribuzioni del portafoglio iniziale e del portafoglio soggetto al limite.
3. Distribuzione di $\Delta L$ oppure confronto delle perdite negli scenari con e senza ingresso nel regime di crisi.

### 5.4 Controlli

- tutte le righe di $Q$ devono sommare a uno;
- tutte le righe delle tre matrici $P^{(m)}$ devono sommare a uno;
- lo stato $D$ deve essere assorbente;
- $M_0=S$ in tutte le repliche;
- la traiettoria sistemica deve essere unica per tutti i debitori di una replica;
- le estrazioni individuali devono essere indipendenti condizionatamente al regime;
- il tempo di default deve coincidere con il primo ingresso nello stato $D$;
- la LGD deve essere determinata dal regime che governa la transizione nel default;
- l'investimento complessivo deve essere pari a $200$ milioni in entrambi i portafogli;
- la posizione Evergrande deve passare da $30$ a $20$ milioni;
- la riallocazione complessiva deve essere esattamente pari a $10$ milioni;
- la riallocazione deve interessare esclusivamente i gruppi BBB e BB e rispettarne le proporzioni iniziali;
- i due portafogli devono utilizzare gli stessi scenari Monte Carlo;
- la perdita aggregata deve coincidere con la somma delle perdite individuali;
- i risultati devono essere riproducibili con il seed assegnato;
- VaR e CVaR devono essere calcolati sulle perdite monetarie.

## 6. Flusso logico-teorico risolutivo atteso

| Passo | Finalità risolutiva | Formula, definizione, proprietà o teorema | Applicazione nel caso | Output o controllo collegato |
|---:|---|---|---|---|
| 1 | Costruire il modello probabilistico e la politica di concentrazione | Catene di Markov, probabilità condizionata, indipendenza condizionata, vincolo single-name | Definizione di $M_t$, $X_{i,t}$, matrici, portafoglio iniziale e portafoglio soggetto al limite | Specifica teorico-matematica validata |
| 2 | Generare gli scenari creditizi con fattore sistemico comune | $\Pr(X_{i,t+1}=j\mid X_{i,t}=k,M_t=m)=p_{kj}^{(m)}$ | Simulazione dei regimi, delle migrazioni e dei tempi di default | Traiettorie simulate e controlli |
| 3 | Trasformare le traiettorie in perdite monetarie | Perdita migration-based; $\operatorname{EAD}\times\operatorname{LGD}$; LGD dipendente dal regime | Applicazione della perdita non-default o della LGD determinata dal regime al default | Campione delle perdite individuali e di portafoglio |
| 4 | Stimare e confrontare il rischio dei due portafogli | Distribuzione empirica, valore atteso, dispersione, VaR, CVaR | Stima delle misure e valutazione della politica di concentrazione | Tabelle, grafici e differenze tra misure |
| 5 | Controllare il modello e interpretare i risultati | Markovianità, omogeneità, indipendenza condizionata, recovery, concentrazione, rischio di modello | Valutazione delle ipotesi, controllo conclusivo e interpretazione della politica di concentrazione | Interpretazione finale e, se emerge una criticità specifica, eventuale verifica in Regime C |

## 7. Scomposizione attesa in tappe

| Tappa | Titolo | Obiettivo | Input | Regime IA prevalente | Prompt virtuoso di riferimento | Oggetti teorici coinvolti | Operazione | Output | Controllo | Uso successivo |
|---:|---|---|---|:---:|---|---|---|---|---|---|
| 1 | Modello teorico e politica di concentrazione | Formalizzare il modello probabilistico, la funzione di perdita e la politica di concentrazione | Scheda Caso | A | Prompt tappa 1 | Catene di Markov, probabilità condizionata, indipendenza condizionata, tempo di default, EAD, LGD, perdita da migrazione, vincolo single-name | Identificare i due processi markoviani, il ruolo del tempo di default, la LGD dipendente dal regime, i due portafogli e le quantità finali | Specifica teorico-matematica e algoritmo concettuale | Coerenza con la Scheda Caso; distinzione investimento/EAD; corretta definizione della politica di concentrazione | Base vincolante della simulazione |
| 2 | Simulazione delle traiettorie e dei default | Generare scenari coerenti di regime sistemico, rating e default | $Q$, $P^{(N)}$, $P^{(S)}$, $P^{(C)}$, rating iniziali, $N_{\mathrm{MC}}$, seed | B | Prompt tappa 2 | Catene di Markov, matrice di transizione, stato assorbente, indipendenza condizionata | Simulare regime sistemico, migrazioni creditizie e primo ingresso nel default | Regimi, stati finali, tempi e regimi di default | Matrici stocastiche; default assorbente; regime comune; indipendenza condizionata | Costruzione delle perdite |
| 3 | Costruzione delle perdite | Trasformare le traiettorie simulate in perdite individuali e di portafoglio per le due allocazioni | Traiettorie simulate, investimenti, funzione $\varphi$, LGD per regime | B | Prompt tappa 3 | Perdita migration-based, EAD, LGD, aggregazione di portafoglio, riallocazione dell'investimento | Calcolare le perdite migration-based o da default; costruire i due vettori di investimento e aggregare | $L_{\mathrm{base}}^{P,(r)}$, $L_{\mathrm{lim}}^{P,(r)}$, $\Delta L^{(r)}$ | Corretta LGD al default; investimento totale invariato; stessi scenari nei due portafogli | Stima delle distribuzioni |
| 4 | Distribuzioni e misure di rischio | Stimare e confrontare le distribuzioni di perdita e le principali misure di rischio | Campioni delle perdite e informazioni sui regimi | B | Prompt tappa 4 | Distribuzione empirica, valore atteso, varianza, VaR, CVaR, condizionamento per evento | Stimare distribuzioni, perdita media, dispersione, VaR e CVaR; confrontare i portafogli e gli scenari sistemici | Tabelle, grafici e variazioni delle misure di rischio | Coerenza VaR/CVaR; stabilità Monte Carlo; corretta lettura del confronto | Interpretazione finanziaria |
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
| Prompt tappa 1 | A | Tappa 1 | Formalizzare il modello teorico e la politica di concentrazione senza produrre codice | Celle Markdown di impostazione teorico-matematica | Correttezza del modello, della LGD dipendente dal regime e della politica di concentrazione |
| Prompt tappa 2 | B | Tappa 2 | Tradurre la specifica validata nell'algoritmo di simulazione delle traiettorie e dei default | Celle Markdown e codice per simulazione di regimi, rating e default | Corretta implementazione delle traiettorie, dello stato assorbente e del regime comune |
| Prompt tappa 3 | B | Tappa 3 | Implementare la trasformazione delle traiettorie in perdite e costruire i due portafogli | Celle Markdown e codice per perdite individuali, due portafogli e aggregazione | Coerenza perdita-regime-investimento, corretta LGD e corretta applicazione del limite |
| Prompt tappa 4 | B | Tappa 4 | Costruire distribuzioni, misure di rischio, tabelle e grafici previsti | Celle Markdown, codice, tabelle e grafici per distribuzioni e misure di rischio | Corretta implementazione di VaR/CVaR, stabilità Monte Carlo e corretto confronto tra portafogli |
| Prompt C eventuale | C | Tappa interessata | Verificare una criticità specifica già individuata dallo studente | Eventuale sostituzione delle celle coinvolte | Criticità accolta oppure respinta |


## 9. Struttura attesa del notebook

Il notebook deve riflettere direttamente le cinque tappe risolutive. Ogni tappa può produrre più celle, purché rimanga riconoscibile come modulo logico unitario.

### Apertura del notebook

**Prompt di riferimento:** Prompt 1.

- Cella Markdown: titolo, contesto Evergrande 2021, domanda quantitativa e Scheda Caso come specifica vincolante.

Dopo la cella iniziale prodotta con il Prompt 1, il notebook deve riportare:

- una cella Markdown con il Flusso logico-teorico risolutivo validato attraverso il Prompt 2;
- una cella Markdown con la scomposizione operativa in tappe input-output validata attraverso il Prompt 3.

Queste due celle documentano le decisioni di progettazione che governano lo sviluppo successivo del notebook e devono precedere le celle operative delle singole tappe.

### Tappa 1 — Modello teorico e politica di concentrazione

**Prompt di riferimento:** Prompt tappa 1 — Regime A.

- Cella Markdown: definizione del processo sistemico $M_t$.
- Cella Markdown: definizione dei processi creditizi $X_{i,t}$.
- Cella Markdown: interpretazione di $Q$ e delle matrici $P^{(N)}$, $P^{(S)}$, $P^{(C)}$.
- Cella Markdown: indipendenza condizionata e dipendenza incondizionata.
- Cella Markdown: definizione del tempo di default $\tau_i$.
- Cella Markdown: distinzione tra perdita da migrazione e perdita da default.
- Cella Markdown: relazione tra investimento iniziale ed EAD come ipotesi specifica del caso.
- Cella Markdown: portafoglio iniziale e politica del limite single-name.
- Cella Markdown: algoritmo concettuale della simulazione.

### Tappa 2 — Simulazione delle traiettorie e dei default

**Prompt di riferimento:** Prompt tappa 2 — Regime B.

- Cella codice: definizione degli stati e delle matrici.
- Cella codice: controlli sulle matrici.
- Cella codice: costruzione del portafoglio iniziale.
- Cella codice: impostazione del seed e di $N_{\mathrm{MC}}$.
- Cella codice: simulazione delle traiettorie sistemiche.
- Cella codice: simulazione delle traiettorie creditizie.
- Cella codice: individuazione del primo ingresso nello stato $D$.
- Cella codice: registrazione del regime che ha governato ciascun default.
- Output sintetico: alcune traiettorie campione.
- Output: controlli sugli stati e sui default.

### Tappa 3 — Costruzione delle perdite

**Prompt di riferimento:** Prompt tappa 3 — Regime B.

- Cella Markdown: funzione di perdita migration-based e LGD dipendente dal regime.
- Cella codice: implementazione della matrice delle perdite non-default.
- Cella codice: associazione della corretta LGD ai debitori in default.
- Cella codice: costruzione del vettore degli investimenti iniziali.
- Cella codice: costruzione del vettore soggetto al limite di concentrazione.
- Output: controllo dell'investimento totale e della riallocazione.
- Cella codice: perdite individuali e aggregate del portafoglio iniziale.
- Cella codice: perdite individuali e aggregate del portafoglio soggetto al limite.
- Output: campioni delle due perdite.
- Output: $\Delta L^{(r)}$.

### Tappa 4 — Distribuzioni e misure di rischio

**Prompt di riferimento:** Prompt tappa 4 — Regime B.

- Cella Markdown: convenzioni operative per perdita attesa, VaR e CVaR.
- Cella codice: costruzione delle distribuzioni empiriche.
- Cella codice: perdita media, varianza e deviazione standard.
- Cella codice: $VaR_{0.95}$, $CVaR_{0.95}$, $VaR_{0.99}$, $CVaR_{0.99}$.
- Output: tabella comparativa.
- Cella codice/output: distribuzione della perdita del portafoglio iniziale.
- Cella codice/output: confronto delle code dei due portafogli.
- Cella codice/output: confronto tra scenari con e senza ingresso nel regime $C$.
- Controllo: stabilità delle stime rispetto al numero di repliche.

### Tappa 5 — Controlli conclusivi e interpretazione

**Prompt di riferimento:** nessun prompt obbligatorio. Il Regime C può essere attivato soltanto in presenza di una criticità specifica individuata dallo studente.

- Cella Markdown: controlli conclusivi sulla coerenza tra notebook e Scheda Caso.
- Cella Markdown: interpretazione finanziaria finale formulata autonomamente dallo studente.
- Se emerge una criticità specifica, eventuale Prompt C riferito alla tappa interessata.
- Classificazione dell'eventuale verifica: criticità accolta oppure criticità respinta.
- Se la criticità viene accolta, sostituzione delle celle interessate con versioni corrette.

L'interpretazione deve distinguere almeno:

- ruolo del regime sistemico nelle migrazioni;
- ruolo del regime sistemico nella severità del default;
- differenza fra rischio idiosincratico e dipendenza sistemica;
- effetto della concentrazione Evergrande;
- effetto del limite single-name;
- significato finanziario di VaR e CVaR;
- assenza di dominanza scenario per scenario tra le due allocazioni;
- limiti delle matrici omogenee e delle LGD deterministiche per regime;
- differenza tra modello didattico ex ante e successivi eventi storici.

## 10. Criteri di validazione del notebook

Il notebook è considerato valido se:

1. implementa la specifica teorico-matematica della Scheda Caso senza modificarla;
2. utilizza esclusivamente le matrici, le LGD, gli investimenti, il limite di concentrazione e gli altri parametri assegnati;
3. rispetta la scomposizione in tappe input-output validata;
4. mantiene coerenti la notazione matematica e le corrispondenti variabili computazionali;
5. simula una sola traiettoria del regime sistemico per ciascuna replica e la utilizza per tutti i debitori;
6. preserva l'indipendenza delle estrazioni individuali condizionatamente alla traiettoria sistemica comune;
7. mantiene lo stato di default assorbente e identifica correttamente il primo ingresso in $D$;
8. applica, in caso di default, la LGD associata al regime che governa la transizione verso $D$;
9. applica la funzione di perdita migration-based soltanto ai debitori che non entrano in default entro l'orizzonte;
10. costruisce correttamente il portafoglio soggetto al limite, mantenendo l'investimento complessivo pari a $200$ milioni e riallocando esattamente $10$ milioni esclusivamente tra le posizioni BBB e BB secondo la regola assegnata;
11. utilizza gli stessi scenari sistemici e creditizi per confrontare il portafoglio iniziale e quello soggetto al limite;
12. riconcilia le perdite aggregate con la somma delle perdite individuali;
13. produce tutti gli output numerici, tabellari e grafici richiesti;
14. calcola VaR e CVaR sulle distribuzioni delle perdite monetarie secondo le convenzioni adottate nel corso;
15. produce risultati riproducibili con il seed assegnato e sufficientemente stabili rispetto alla dimensione del campione Monte Carlo;
16. conclude con controlli espliciti e con un'interpretazione finanziaria coerente con gli output e con i limiti del modello.

Un eventuale Prompt in Regime C non costituisce condizione necessaria di validità del notebook. Esso interviene soltanto quando lo studente individua una criticità specifica da verificare.

## 11. Calibrazione docente

La calibrazione di riferimento utilizza:

$$
N_{\mathrm{MC}}
=
50\,000,
\qquad
\text{seed}=2027.
$$

### 11.1 Portafoglio iniziale

| Misura | Valore indicativo, milioni USD |
|---|---:|
| Perdita media | 26.20 |
| Deviazione standard | 16.64 |
| VaR 95% | 60.74 |
| CVaR 95% | 69.29 |
| VaR 99% | 74.51 |
| CVaR 99% | 79.92 |

### 11.2 Portafoglio soggetto al limite di concentrazione

| Misura | Valore indicativo, milioni USD |
|---|---:|
| Perdita media | 24.91 |
| Deviazione standard | 15.04 |
| VaR 95% | 55.52 |
| CVaR 95% | 63.36 |
| VaR 99% | 68.20 |
| CVaR 99% | 73.83 |

### 11.3 Effetto della politica di concentrazione

Definendo

$$
\Delta\rho
=
\rho(L_{\mathrm{lim}}^P)
-
\rho(L_{\mathrm{base}}^P),
$$

si ottengono indicativamente:

| Misura | $\Delta\rho$, milioni USD |
|---|---:|
| Perdita media | -1.29 |
| Deviazione standard | -1.60 |
| VaR 95% | -5.22 |
| CVaR 95% | -5.93 |
| VaR 99% | -6.31 |
| CVaR 99% | -6.09 |

La riduzione della posizione Evergrande ha quindi un effetto più pronunciato sulle misure di coda che sulla perdita media.

Il risultato non deve tuttavia essere interpretato come una dominanza deterministica del portafoglio soggetto al limite. I due portafogli utilizzano gli stessi scenari, ma in alcune realizzazioni la riallocazione sulle altre posizioni può produrre una perdita superiore a quella del portafoglio iniziale.

La politica viene valutata sulla **distribuzione complessiva delle perdite**, non sulla superiorità in ogni singolo scenario.

### 11.4 Ruolo del regime sistemico

Con la calibrazione assegnata:

- la probabilità simulata di raggiungere il regime $C$ almeno una volta è circa il $37.1\%$;
- il numero medio di default è circa $5.36$ per replica;
- la perdita media del portafoglio iniziale negli scenari che visitano $C$ è circa $40.92$ milioni;
- la perdita media negli scenari che non visitano $C$ è circa $17.50$ milioni.

Il confronto deve rendere evidente che il regime sistemico agisce attraverso due canali:

1. modifica le probabilità di migrazione e default;
2. modifica la severità della perdita in caso di default.

### 11.5 Errori o ambiguità prevedibili

1. Confondere investimento iniziale ed EAD.
2. Utilizzare la LGD del regime finale anziché quella del regime che governa la transizione nel default.
3. Continuare a modificare la LGD dopo che il debitore è già entrato nello stato assorbente.
4. Applicare una perdita migration-based a un debitore già in default.
5. Applicare contemporaneamente perdita migration-based e perdita da default allo stesso debitore.
6. Simulare un regime sistemico diverso per ogni debitore.
7. Utilizzare estrazioni individuali perfettamente comuni ai debitori.
8. Confondere $Q$ con le matrici di rating.
9. Utilizzare sempre $P^{(S)}$ perché $M_0=S$.
10. Permettere l'uscita dallo stato $D$.
11. Applicare il limite del $10\%$ all'EAD anziché all'investimento iniziale.
12. Ridurre Evergrande da $30$ a $20$ senza riallocare i $10$ milioni liberati.
13. Riallocare i $10$ milioni anche sulle classi B o CCC.
14. Redistribuire l'importo in parti uguali anziché proporzionalmente agli investimenti BBB e BB.
15. Utilizzare simulazioni differenti per confrontare i due portafogli.
16. Calcolare VaR e CVaR sui rating o sul numero di default.
17. Calcolare il CVaR discreto con una convenzione incoerente con il Capitolo 9.
18. Interpretare i bucket di rating didattici come rating storici esatti di Evergrande.
19. Interpretare il modello come previsione storica del default avvenuto successivamente.
20. Considerare la LGD dipendente dal regime come una stima empirica anziché una calibrazione didattica.

### 11.6 Controlli minimi di validazione

- validazione di $Q$ e delle tre $P^{(m)}$;
- controllo dello stato assorbente;
- verifica del tempo di primo default;
- verifica del regime utilizzato per la LGD;
- verifica dell'investimento totale di $200$ milioni;
- verifica del limite massimo di $20$ milioni;
- verifica della riallocazione di esattamente $10$ milioni;
- verifica dei destinatari BBB e BB della riallocazione;
- verifica dell'utilizzo degli stessi scenari nei due portafogli;
- riconciliazione delle perdite individuali e aggregate;
- riproducibilità;
- stabilità delle misure di rischio al crescere delle simulazioni;
- confronto tra scenari con e senza ingresso nel regime di crisi.

### 11.7 Limiti interpretativi

Il modello non incorpora:

- matrici specifiche per singolo emittente;
- matrici differenziate per settore o tipologia di debitore;
- effetti di contagio diretto tra società immobiliari, banche e altri intermediari;
- evoluzione stocastica dell'EAD;
- LGD continua o specifica per singolo debitore;
- dipendenza della LGD da collateral, seniority o struttura contrattuale;
- correlazioni ulteriori rispetto al fattore sistemico comune;
- variazioni endogene delle matrici di transizione;
- rischio di liquidità;
- rischio valutario;
- interventi governativi o ristrutturazioni;
- probabilità risk-neutral;
- pricing di obbligazioni o CDS.

I tre regimi costituiscono una rappresentazione stilizzata delle condizioni del sistema e non una classificazione empirica ufficiale delle fasi della crisi Evergrande.

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

- ordinamento e verifica della specifica teorico-matematica proposta dallo studente;
- traduzione della specifica validata in codice;
- implementazione dell'algoritmo di simulazione;
- registrazione tecnica dei tempi e dei regimi di default;
- applicazione della LGD secondo la regola assegnata;
- implementazione della politica di concentrazione;
- produzione di tabelle e grafici;
- implementazione di VaR e CVaR;
- verifica di criticità formulate dallo studente.

### Usi non ammessi

- modifica autonoma di $Q$;
- modifica autonoma delle matrici $P^{(m)}$;
- modifica delle LGD assegnate;
- modifica della composizione iniziale del portafoglio;
- modifica autonoma del limite del $10\%$;
- modifica della regola di riallocazione;
- sostituzione della struttura di dipendenza;
- introduzione autonoma di copule, modelli a fattori o modelli strutturali;
- sostituzione dei parametri didattici con dati storici esterni;
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
- corretta simulazione della dipendenza sistemica;
- corretta individuazione del tempo di default;
- corretta applicazione della LGD dipendente dal regime;
- corretta distinzione tra investimento iniziale ed EAD;
- corretta costruzione del portafoglio soggetto al limite;
- mantenimento dell'investimento totale;
- corretto riutilizzo degli stessi scenari nei due portafogli;
- corretta aggregazione delle perdite;
- corretta stima delle distribuzioni empiriche;
- corretta implementazione di VaR e CVaR;
- qualità dei controlli;
- chiarezza di tabelle e grafici;
- capacità di interpretare economicamente la politica di concentrazione.

### Criteri per il tracciato IA

- qualità del contributo iniziale dello studente in Regime A;
- rispetto della Scheda Caso come specifica vincolante;
- corretta separazione tra formulazione teorica e implementazione;
- qualità della scomposizione del problema;
- capacità di specificare input e output delle tappe;
- qualità dell'eventuale verifica in Regime C, quando attivata a partire da una criticità specifica individuata dallo studente;
- capacità di accettare o respingere motivatamente una proposta dell'IA;
- assenza di delega dell'interpretazione finale.

### Peso dei controlli e dell'interpretazione

La qualità del codice non deve essere valutata per complessità autonoma.

Il nucleo della valutazione è costituito dalla capacità di governare la sequenza:

$$
\text{modello}
\longrightarrow
\text{simulazione}
\longrightarrow
\text{default e recovery}
\longrightarrow
\text{perdita}
\longrightarrow
\text{distribuzione}
\longrightarrow
\text{misure di rischio}
\longrightarrow
\text{politica di concentrazione}
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

1. rappresentare correttamente la dipendenza tra rischio sistemico comune e migrazioni creditizie individuali;
2. distinguere il rischio di migrazione dal rischio di default;
3. applicare la LGD al regime sistemico che governa la transizione nel default;
4. trasformare le traiettorie simulate in perdite individuali e di portafoglio;
5. confrontare il portafoglio iniziale con quello soggetto al limite di concentrazione utilizzando gli stessi scenari Monte Carlo;
6. stimare e interpretare perdita attesa, dispersione, VaR e CVaR;
7. valutare l'effetto della politica di concentrazione sulla distribuzione complessiva delle perdite e sulle misure di coda;
8. distinguere i risultati prodotti dal modello didattico dagli eventi storici successivamente osservati;
9. formulare autonomamente un'interpretazione finanziaria coerente con le ipotesi, gli output e i limiti del modello.

### Calibrazione qualitativa

Il caso è considerato didatticamente ben calibrato se:

- il portafoglio iniziale presenta una concentrazione chiaramente visibile sulla posizione Evergrande;
- il limite single-name modifica in modo economicamente leggibile la distribuzione delle perdite senza produrre una dominanza deterministica scenario per scenario;
- il regime sistemico influenza in misura osservabile sia le probabilità di migrazione e default sia la severità della perdita;
- gli scenari che raggiungono il regime di crisi presentano, in media, perdite sensibilmente superiori agli altri scenari;
- le differenze tra portafoglio iniziale e portafoglio soggetto al limite risultano più informative nelle misure di coda che nella sola perdita media;
- gli output numerici rimangono compatibili con gli ordini di grandezza riportati nella calibrazione docente;
- il problema è sufficientemente articolato da richiedere una vera scomposizione teorico-computazionale, ma non introduce elementi estranei agli strumenti già sviluppati nel corso.

Gli esiti numerici indicativi riportati nella calibrazione docente hanno funzione di controllo e non devono essere comunicati allo studente come risultati da riprodurre meccanicamente.

## 16. Relazione con il caso TakeHome

I due casi sono metodologicamente isomorfi perché entrambi utilizzano:

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

Non costituiscono tuttavia una semplice variazione parametrica.

### Caso TakeHome — Lehman Brothers 2008

- contesto: crisi del sistema finanziario internazionale;
- posizione principale inizialmente nella classe A;
- LGD comune e deterministica;
- controfattuale: eliminazione della posizione Lehman e riallocazione proporzionale dell'investimento tra tutti i debitori residui;
- domanda gestionale: conseguenze della sostituzione di una forte concentrazione single-name.

### Caso Aula — China Evergrande 2021

- contesto: crisi del settore immobiliare e del credito cinese;
- posizione principale inizialmente nella classe B del modello;
- LGD dipendente dal regime sistemico nel quale avviene il default;
- controfattuale: mantenimento di Evergrande ma introduzione di un limite single-name del $10\%$;
- riallocazione selettiva dell'investimento liberato verso posizioni BBB e BB;
- domanda gestionale: efficacia di una politica esplicita di controllo della concentrazione in presenza di deterioramento sistemico e recovery pro-ciclica.

Il Caso TakeHome richiede quindi allo studente di trasferire autonomamente la struttura metodologica sviluppata nel Caso Aula a un problema nuovo, mantenendo l'architettura generale del modello ma modificandone il contesto, la funzione di perdita e la struttura del confronto controfattuale.