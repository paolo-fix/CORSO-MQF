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


## 3. Domanda quantitativa e funzione didattica

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

### Collegamento con le lezioni teoriche precedenti

Il caso applica operativamente i contenuti sviluppati nelle lezioni teoriche precedenti sulle catene di Markov, sulle migrazioni creditizie e sulle misure di rischio. In particolare, utilizza:

- la dinamica markoviana di un processo a stati discreti;
- matrici di transizione dipendenti dallo stato sistemico;
- il ruolo dello stato di default assorbente;
- la distinzione tra dipendenza condizionata e dipendenza incondizionata;
- la costruzione di perdite individuali e aggregate;
- la stima empirica di valore atteso, varianza, VaR e CVaR.

### Concetti teorici da rendere osservabili

Il caso deve rendere osservabili:

- la dipendenza tra le probabilità di migrazione e il regime sistemico corrente;
- l’indipendenza delle migrazioni individuali condizionatamente alla traiettoria del regime comune;
- la dipendenza incondizionata tra le perdite dei debitori;
- il carattere assorbente dello stato di default;
- il legame tra tempo di default, regime sistemico e LGD;
- il passaggio dalle perdite individuali alla distribuzione della perdita di portafoglio;
- l’effetto della concentrazione single-name sulle misure di rischio.

### Funzione della simulazione o della procedura computazionale

La simulazione Monte Carlo è necessaria per generare congiuntamente le traiettorie del regime sistemico e dei rating individuali, determinare gli eventuali tempi di default, applicare la funzione di perdita coerente con ciascuna traiettoria e costruire la distribuzione empirica della perdita di portafoglio.

### Ruolo dell’informazione, degli stati, degli scenari o dei vincoli

Il regime sistemico costituisce l’informazione comune che modifica le probabilità di transizione creditizia di tutti i debitori. Gli stati creditizi descrivono l’evoluzione individuale del merito creditizio, mentre le repliche Monte Carlo rappresentano possibili realizzazioni congiunte del sistema. Il vincolo di concentrazione single-name determina il portafoglio alternativo da confrontare con quello iniziale.

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

Applicando alle stesse traiettorie simulate il vettore degli investimenti soggetto al limite si ottiene

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

Una quantità aggiuntiva utile è la differenza replica per replica:

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
9. mantenendo invariate le stesse traiettorie simulate, si applica il vettore degli investimenti soggetto al limite e si calcola la seconda perdita di portafoglio.

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

Confronto, per il portafoglio iniziale, tra repliche con e senza ingresso nel regime $C$.

### 5.3 Grafici

1. Distribuzione empirica della perdita del portafoglio iniziale con indicazione di VaR 95% e VaR 99%.
2. Confronto delle code delle distribuzioni del portafoglio iniziale e del portafoglio soggetto al limite.
3. Distribuzione di $\Delta L$ oppure confronto delle perdite nelle repliche con e senza ingresso nel regime di crisi.

### 5.4 Controlli

I controlli richiesti devono distinguere tra:

- proprietà verificabili direttamente sui dati, sulle simulazioni o sugli output numerici;
- proprietà strutturali garantite dalla costruzione dell'algoritmo;
- controlli computazionali relativi all'accoppiamento delle repliche e all'impostazione della simulazione

#### Controlli numerici

1. Tutte le righe della matrice di transizione del regime sistemico $Q$ devono sommare a uno.

2. Tutte le righe delle matrici di migrazione creditizia $P^{(N)}$, $P^{(S)}$ e $P^{(C)}$ devono sommare a uno.

11. L'investimento complessivo deve essere pari a $200$ milioni di dollari sia nel portafoglio iniziale sia nel portafoglio soggetto al limite.

12. Nel portafoglio soggetto al limite deve risultare che:
   - la posizione Evergrande è pari a $20$ milioni di dollari;
   - l'importo complessivamente riallocato è pari a $10$ milioni di dollari;
   - la riallocazione interessa esclusivamente i gruppi inizialmente BBB e BB;
   - la proporzione relativa tra gli investimenti complessivi dei gruppi BBB e BB è preservata.

14. Per ciascuna replica Monte Carlo e per ciascuno dei due portafogli, la perdita aggregata deve coincidere con la somma delle perdite individuali.

16. La stabilità delle stime Monte Carlo deve essere valutata confrontando, per entrambi i portafogli, le principali misure di rischio ottenute con il campione completo e con un sotto-campione sufficientemente ampio. Il controllo costituisce una verifica empirica di sensibilità alla numerosità Monte Carlo e non una dimostrazione formale di convergenza.

17. VaR e CVaR devono essere calcolati direttamente sulle distribuzioni empiriche delle perdite monetarie dei due portafogli, espresse in milioni di dollari. Il CVaR deve essere implementato secondo la definizione mediante quantili adottata nel Capitolo 9; nel campione empirico discreto non deve essere sostituito automaticamente dalla media condizionata delle osservazioni maggiori o uguali al VaR.

#### Controlli logici o teorici

3. Lo stato di default $D$ deve essere assorbente in tutte le matrici di migrazione creditizia e, una volta raggiunto, deve permanere tale nelle successive date simulate.

4. Il regime sistemico iniziale deve essere $M_0=S$ in ogni replica Monte Carlo.

5. Per ciascuna replica deve essere generata una sola traiettoria sistemica $M^{(r)}$, successivamente utilizzata per tutti i $36$ debitori. Questa proprietà è garantita per costruzione dall'architettura della simulazione e non deve essere rappresentata come una verifica statistica distinta.

6. Condizionatamente alla traiettoria sistemica comune, le migrazioni dei differenti debitori devono essere simulate mediante estrazioni casuali individuali distinte. Anche questa proprietà è garantita per costruzione dalla procedura di simulazione e deve essere documentata come tale.

7. Per ogni debitore, il tempo di default $\tau_i$ deve coincidere con il primo trimestre nel quale la traiettoria creditizia entra nello stato $D$.

8. Per tutti i debitori e tutte le repliche nelle quali si verifica un default, la LGD applicata deve corrispondere al regime sistemico $M_{\tau_i-1}$ che governa la transizione verso $D$. Il controllo deve riguardare l'intero insieme dei default simulati e non un singolo caso campione.

9. Un debitore che abbia raggiunto lo stato $D$ non deve successivamente uscire dal default.

10. La funzione di perdita migration-based $\varphi(X_{i,0},X_{i,4})$ deve essere applicata esclusivamente ai debitori per i quali $\tau_i>4$. Per tutti i debitori in default deve invece essere applicata la perdita basata sulla LGD. Il controllo deve essere effettuato sull'intero insieme delle osservazioni pertinenti e non su un singolo caso campione.

#### Controlli computazionali

13. Il confronto tra portafoglio iniziale e portafoglio soggetto al limite deve utilizzare esattamente le medesime traiettorie sistemiche e creditizie simulate. Tale proprietà deriva dal riutilizzo degli stessi oggetti simulati per il calcolo delle perdite dei due portafogli e deve essere documentata come proprietà strutturale del confronto mediante *Common Random Numbers*.

15. Deve essere impostato il seed assegnato, pari a $2027$, come condizione per la riproducibilità della simulazione a parità di implementazione e ambiente computazionale. Il controllo deve verificare l'impostazione del seed e non deve essere rappresentato mediante una condizione numerica estranea alla riproducibilità.

## 6. Flusso logico-teorico risolutivo atteso

| Passo | Finalità risolutiva | Formula, definizione, proprietà o teorema | Applicazione nel caso | Output o controllo collegato |
|---:|---|---|---|---|
| 1 | Definire la struttura dei portafogli e la politica di concentrazione | Portafoglio iniziale con $V_0^P=200$ milioni; vincolo single-name pari al $10\%$ dell'investimento complessivo; riallocazione proporzionale dei $10$ milioni liberati dalla riduzione della posizione Evergrande verso i gruppi BBB e BB | Costruzione del portafoglio iniziale e del portafoglio soggetto al limite, mantenendo invariato l'investimento complessivo | Tabelle 1 e 2; controlli sulla composizione e sulla riallocazione |
| 2 | Rappresentare l'evoluzione del regime sistemico | Catena di Markov $M_t\in\{N,S,C\}$ con stato iniziale $M_0=S$ e matrice di transizione $Q$ | Simulazione della traiettoria trimestrale del regime sistemico comune ai debitori | Probabilità di ingresso nel regime $C$; controlli sulla matrice $Q$, sullo stato iniziale e sulla riproducibilità |
| 3 | Modellizzare le migrazioni creditizie condizionate al regime | $\Pr(X_{i,t+1}=j\mid X_{i,t}=k,M_t=m)=p_{kj}^{(m)}$; stato $D$ assorbente; indipendenza condizionata delle migrazioni individuali data la traiettoria sistemica comune | Simulazione dei rating dei $36$ debitori mediante la matrice $P^{(M_t)}$ coerente con il regime corrente | Controlli sulle matrici di migrazione, sullo stato assorbente, sulla traiettoria sistemica comune e sull'indipendenza condizionata |
| 4 | Determinare il default e trasformare le traiettorie creditizie in perdite individuali | $\tau_i=\min\{t\in\{1,\ldots,4\}:X_{i,t}=D\}$; se $\tau_i>4$, $L_i=V_{i,0}\varphi(X_{i,0},X_{i,4})$; se $\tau_i\leq4$, $L_i=V_{i,0}\operatorname{LGD}^{(M_{\tau_i-1})}$ | Identificazione del primo ingresso in default e applicazione della perdita migration-based oppure della LGD dipendente dal regime che governa la transizione verso $D$ | Numero medio di default; controlli sul tempo di default, sulla LGD applicata e sull'esclusività fra perdita migration-based e perdita da default |
| 5 | Aggregare le perdite individuali e costruire le distribuzioni di portafoglio | $L^P=\sum_{i=1}^{36}L_i$; confronto fra portafoglio iniziale e portafoglio soggetto al limite mediante le stesse repliche sistemiche e creditizie | Costruzione di $L_{\mathrm{base}}^P$, $L_{\mathrm{lim}}^P$ e della differenza replica per replica $\Delta L^{(r)}=L_{\mathrm{lim}}^{P,(r)}-L_{\mathrm{base}}^{P,(r)}$ | Distribuzioni empiriche; controlli di additività delle perdite e di accoppiamento delle repliche |
| 6 | Stimare le misure di rischio e valutare l'effetto del regime sistemico e della politica di concentrazione | Stima di $\mathbb{E}[L^P]$, $\operatorname{Var}(L^P)$, $\sigma(L^P)$, $\operatorname{VaR}_{\alpha}(L^P)$ e $\operatorname{CVaR}_{\alpha}(L^P)$ per $\alpha\in\{0.95,0.99\}$ | Confronto delle misure di rischio tra i due portafogli e analisi della perdita condizionata all'ingresso o meno nel regime $C$ | Tabelle 3 e 4; Figure 1, 2 e 3; controlli sulla stabilità Monte Carlo e sul calcolo di VaR e CVaR |

## 7. Scomposizione attesa in tappe

| Tappa | Titolo | Obiettivo | Input | Regime IA prevalente | Prompt virtuoso di riferimento | Oggetti teorici coinvolti | Operazione | Output | Controllo | Uso successivo |
|---:|---|---|---|:---:|---|---|---|---|---|---|
| 1 | Parametri e strutture del modello | Tradurre in strutture computazionali i parametri assegnati e verificarne la coerenza formale | Matrice $Q$, matrici $P^{(N)}$, $P^{(S)}$, $P^{(C)}$, funzione di perdita $\varphi$ rappresentata mediante la tabella dei tassi migration-based, LGD, $N_{\mathrm{MC}}$, $T$, seed | B | Prompt tappa 1 | Matrici di transizione, probabilità di transizione, stato assorbente, funzione di perdita, LGD | Inizializzare le strutture NumPy/Pandas e verificare le proprietà delle matrici | Strutture dati contenenti la calibrazione vincolante del modello | Somme di riga pari a 1 e stato $D$ assorbente | Input per la costruzione dei portafogli e per la simulazione |
| 2 | Costruzione dei due portafogli | Costruire il portafoglio iniziale e quello soggetto al limite di concentrazione | Composizione iniziale, investimenti $V_{i,0}$, limite single-name del $10\%$, regola di riallocazione | B | Prompt tappa 2 | Investimento iniziale, concentrazione single-name, riallocazione proporzionale | Costruire i vettori $V_{\mathrm{base}}$ e $V_{\mathrm{lim}}$ e le relative tabelle | Tabelle 1 e 2; vettori degli investimenti dei due portafogli | Investimento totale invariato, Evergrande a 20 milioni, riallocazione di 10 milioni esclusivamente a BBB e BB e mantenimento delle proporzioni | Input monetario per il calcolo delle perdite |
| 3 | Simulazione delle traiettorie sistemiche e creditizie | Generare repliche con una traiettoria sistemica comune, migrazioni individuali e tempi di default | Seed, $N_{\mathrm{MC}}$, $T$, $M_0=S$, $Q$, matrici $P^{(m)}$, rating iniziali | B | Prompt tappa 3 | Catena di Markov, migrazioni condizionate al regime, indipendenza condizionata, stato assorbente, tempo di default | Impostare il seed 2027; simulare per ogni replica una sola traiettoria $M_t$ comune ai 36 debitori; condizionatamente a tale traiettoria, simulare le traiettorie $X_{i,t}$ mediante estrazioni individuali distinte; identificare il primo ingresso nello stato $D$ e registrare $\tau_i$ e il regime che governa la transizione verso il default | Traiettorie sistemiche e creditizie e tempi di default $\tau_i$ | Verifica di $M_0=S$, del primo ingresso in $D$ e dell'assorbimento del default; unicità della traiettoria sistemica comune e indipendenza condizionata documentate come proprietà **PER COSTRUZIONE**; seed 2027 correttamente impostato come condizione per la riproducibilità | Input per la determinazione delle perdite individuali |
| 4 | Perdite individuali e di portafoglio | Trasformare le traiettorie simulate in perdite monetarie per le due configurazioni di portafoglio | Traiettorie $M$, $X$, $\tau$, $V_{\mathrm{base}}$, $V_{\mathrm{lim}}$, funzione di perdita $\varphi$, LGD | B | Prompt tappa 4 | Perdita migration-based, EAD, LGD dipendente dal regime, aggregazione di portafoglio, *Common Random Numbers* | Per ogni debitore applicare $\varphi(X_{i,0},X_{i,4})$ esclusivamente se $\tau_i>4$ e la LGD associata a $M_{\tau_i-1}$ esclusivamente se $\tau_i\leq4$; utilizzare le stesse repliche sistemiche e creditizie per entrambi i portafogli; aggregare le perdite individuali e calcolare $\Delta L^{(r)}$ | $L_{\mathrm{base}}^P$, $L_{\mathrm{lim}}^P$, $\Delta L^{(r)}$ e numero di default per replica | Verifica, sull'intero insieme dei default, della corretta LGD; verifica, sull'intero insieme delle osservazioni pertinenti, dell'esclusività tra perdita migration-based e perdita da default; uso delle stesse repliche documentato come proprietà strutturale del confronto mediante *Common Random Numbers*; additività delle perdite verificata per ogni replica e per entrambi i portafogli | Input per le misure di rischio e le analisi condizionate |
| 5 | Misure di rischio e analisi condizionata | Stimare le principali misure di rischio e quantificare l'effetto del regime sistemico | Campioni $L_{\mathrm{base}}^P$, $L_{\mathrm{lim}}^P$, $\Delta L^{(r)}$ e traiettorie $M$ | B | Prompt tappa 5 | Distribuzione empirica, valore atteso, varianza, deviazione standard, VaR, CVaR, condizionamento per evento | Calcolare statistiche descrittive, VaR e CVaR direttamente sulle distribuzioni empiriche delle perdite monetarie; implementare il CVaR secondo la definizione mediante quantili adottata nel Capitolo 9; calcolare $\Delta\rho$, probabilità di ingresso in $C$, numero medio di default e perdite medie condizionate | Tabelle 3 e 4 e misure sintetiche richieste | Verifica diretta del calcolo di VaR e CVaR sulle perdite monetarie; verifica della ragionevole stabilità delle principali misure di rischio per entrambi i portafogli mediante confronto tra campione completo e sotto-campione sufficientemente ampio; il controllo di stabilità è una verifica empirica di sensibilità e non una dimostrazione formale di convergenza | Input per la rappresentazione grafica e i controlli conclusivi |
| 6 | Rappresentazione grafica e controlli conclusivi | Produrre gli output grafici richiesti e verificare complessivamente l'esecuzione dei controlli previsti | Distribuzioni simulate, differenze di perdita, indicatori di crisi e risultati delle tappe precedenti | B | Prompt tappa 6 | Distribuzioni empiriche, misure di coda, confronto tra repliche e portafogli | Generare le Figure 1, 2 e 3 e ricostruire l'esito complessivo dei controlli, distinguendo controlli numerici o computazionali da proprietà strutturali **PER COSTRUZIONE** | Figure 1, 2 e 3 e sintesi dei controlli effettuati | Verifica complessiva della copertura dei controlli della Scheda Caso e coerenza degli output prodotti | Base quantitativa verificata per l'interpretazione finanziaria finale autonoma dello studente |

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
| Prompt tappa 1 | B | Tappa 1 | Tradurre i parametri assegnati nelle strutture computazionali del modello e verificarne la coerenza formale | Celle Markdown e codice per matrici, parametri e controlli preliminari | Corretta implementazione di $Q$, delle matrici $P^{(m)}$, della funzione $\varphi$, delle LGD e dello stato assorbente |
| Prompt tappa 2 | B | Tappa 2 | Costruire il portafoglio iniziale e quello soggetto al limite di concentrazione | Celle Markdown, codice e Tabelle 1 e 2 | Investimento totale invariato, posizione Evergrande pari a 20 milioni e corretta riallocazione dei 10 milioni verso BBB e BB |
| Prompt tappa 3 | B | Tappa 3 | Implementare la simulazione delle traiettorie sistemiche e creditizie e identificare i tempi di default | Celle Markdown e codice per simulazione di regime, rating e default | Stato iniziale corretto, regime sistemico comune, indipendenza condizionata, default assorbente e riproducibilità |
| Prompt tappa 4 | B | Tappa 4 | Trasformare le traiettorie simulate in perdite individuali e aggregate per i due portafogli | Celle Markdown e codice per funzione di perdita, LGD, aggregazione e $\Delta L^{(r)}$ | Corretta applicazione della LGD, esclusività tra perdita migration-based e perdita da default, stesse traiettorie simulate nei due portafogli e additività delle perdite |
| Prompt tappa 5 | B | Tappa 5 | Calcolare le misure di rischio e sviluppare l'analisi condizionata al regime sistemico | Celle Markdown, codice, Tabelle 3 e 4 e misure sintetiche | Corretta implementazione di media, varianza, deviazione standard, VaR, CVaR, probabilità di crisi e perdite condizionate |
| Prompt tappa 6 | B | Tappa 6 | Produrre gli output grafici richiesti e completare la ricognizione dei controlli | Celle Markdown, codice, Figure 1, 2 e 3 e sintesi conclusiva dei controlli | Coerenza dei grafici con gli output numerici e verifica complessiva dei controlli previsti dalla Scheda Caso |
| Prompt C eventuale | C | Tappa interessata | Verificare una criticità specifica già individuata dallo studente | Eventuale sostituzione delle celle coinvolte | Criticità accolta oppure respinta |


## 9. Struttura attesa del notebook

Il notebook deve riflettere direttamente la scomposizione operativa validata attraverso il Prompt 3. Nel presente caso, tale scomposizione è articolata in sei tappe operative. Ogni tappa può produrre più celle Markdown, codice e output, purché rimanga riconoscibile come modulo logico unitario.

### Apertura del notebook

**Prompt di riferimento:** Prompt 1.

- Cella Markdown: titolo, contesto Evergrande 2021, domanda quantitativa e Scheda Caso come specifica vincolante.

Dopo la cella iniziale prodotta con il Prompt 1, il notebook deve riportare:

- una cella Markdown con il Flusso logico-teorico risolutivo validato attraverso il Prompt 2;
- una cella Markdown con la scomposizione operativa in tappe input-output validata attraverso il Prompt 3.

Queste due celle documentano le decisioni di progettazione che governano lo sviluppo successivo del notebook e devono precedere le celle operative delle singole tappe.

### Tappa 1 — Parametri e strutture del modello

**Prompt di riferimento:** Prompt tappa 1 — Regime B.

- Cella Markdown: funzione della tappa e richiamo dei parametri vincolanti.
- Cella codice: definizione degli stati sistemici e creditizi.
- Cella codice: definizione della matrice $Q$.
- Cella codice: definizione delle matrici $P^{(N)}$, $P^{(S)}$, $P^{(C)}$.
- Cella codice: definizione della funzione di perdita $\varphi$, rappresentata mediante la tabella dei tassi di perdita migration-based.
- Cella codice: definizione delle LGD per regime.
- Cella codice: impostazione di $N_{\mathrm{MC}}$, $T$ e seed.
- Output: controlli sulle somme di riga delle matrici.
- Output: controllo dello stato $D$ assorbente.

### Tappa 2 — Costruzione dei due portafogli

**Prompt di riferimento:** Prompt tappa 2 — Regime B.

- Cella Markdown: struttura del portafoglio iniziale e regola del limite single-name.
- Cella codice: costruzione del vettore degli investimenti iniziali.
- Cella codice: applicazione del limite del $10\%$ alla posizione Evergrande.
- Cella codice: riallocazione dei $10$ milioni liberati esclusivamente verso BBB e BB secondo la regola proporzionale assegnata.
- Output: Tabella 1 — portafoglio iniziale.
- Output: Tabella 2 — portafoglio soggetto al limite.
- Controllo: investimento totale pari a $200$ milioni in entrambi i portafogli.
- Controllo: posizione Evergrande pari a $20$ milioni nel portafoglio soggetto al limite.
- Controllo: riallocazione complessiva pari a $10$ milioni e rispetto delle proporzioni assegnate.

### Tappa 3 — Simulazione delle traiettorie sistemiche e creditizie

**Prompt di riferimento:** Prompt tappa 3 — Regime B.

- Cella Markdown: funzione della tappa, struttura della simulazione e distinzione tra controlli numerici e proprietà garantite per costruzione.
- Cella codice: inizializzazione del generatore casuale mediante il seed assegnato $2027$.
- Cella codice: simulazione di una sola traiettoria sistemica $M_t$ per ciascuna replica Monte Carlo, con $M_0=S$.
- Cella codice: utilizzo della stessa traiettoria sistemica per tutti i $36$ debitori appartenenti alla medesima replica.
- Cella codice: simulazione delle traiettorie creditizie mediante la matrice $P^{(M_t)}$ coerente con il regime corrente e mediante estrazioni casuali individuali distinte per i differenti debitori.
- Cella codice: identificazione del primo ingresso nello stato $D$.
- Cella codice: registrazione del tempo di default $\tau_i$ e del regime sistemico che governa la transizione verso $D$.
- Output sintetico: dimensioni delle strutture simulate ed eventuali informazioni campione utili alla verifica del meccanismo.
- Controllo: $M_0=S$ in ogni replica.
- Controllo: il tempo $\tau_i$ coincide con il primo ingresso nello stato $D$.
- Controllo: permanenza nello stato assorbente dopo il default.
- Proprietà **PER COSTRUZIONE**: per ciascuna replica viene utilizzata una sola traiettoria sistemica comune ai $36$ debitori.
- Proprietà **PER COSTRUZIONE**: condizionatamente alla traiettoria sistemica comune, i differenti debitori utilizzano estrazioni casuali individuali distinte.
- Controllo computazionale: il seed assegnato $2027$ è correttamente impostato come condizione per la riproducibilità della simulazione a parità di implementazione e ambiente computazionale.

### Tappa 4 — Perdite individuali e di portafoglio

**Prompt di riferimento:** Prompt tappa 4 — Regime B.

- Cella Markdown: distinzione tra perdita migration-based e perdita da default e relativa regola di esclusività.
- Cella codice: applicazione della funzione di perdita $\varphi(X_{i,0},X_{i,4})$ esclusivamente ai debitori per i quali $\tau_i>4$.
- Cella codice: applicazione della $\operatorname{LGD}^{(M_{\tau_i-1})}$ esclusivamente ai debitori per i quali $\tau_i\leq4$.
- Cella codice: calcolo delle perdite individuali del portafoglio iniziale.
- Cella codice: calcolo delle perdite individuali del portafoglio soggetto al limite utilizzando le stesse traiettorie sistemiche e creditizie simulate.
- Cella codice: aggregazione delle perdite individuali e costruzione di $L_{\mathrm{base}}^P$ e $L_{\mathrm{lim}}^P$.
- Cella codice: calcolo della differenza replica per replica
  $$
  \Delta L^{(r)}
  =
  L_{\mathrm{lim}}^{P,(r)}
  -
  L_{\mathrm{base}}^{P,(r)}.
  $$
- Cella codice: calcolo del numero di default per replica.
- Controllo: per tutti i default simulati, la LGD applicata corrisponde al regime $M_{\tau_i-1}$ che governa la transizione verso $D$.
- Controllo: sull'intero insieme delle osservazioni pertinenti, la funzione di perdita migration-based è applicata soltanto ai non-default e la perdita basata sulla LGD soltanto ai default.
- Proprietà strutturale: i due portafogli utilizzano esattamente gli stessi oggetti simulati $M$, $X$ e $\tau$; il confronto mediante *Common Random Numbers* è quindi garantito dalla costruzione del calcolo.
- Controllo: per ciascuna replica e per entrambi i portafogli, la perdita aggregata coincide con la somma delle perdite individuali.

### Tappa 5 — Misure di rischio e analisi condizionata

**Prompt di riferimento:** Prompt tappa 5 — Regime B.

- Cella Markdown: convenzioni operative per perdita media, varianza, deviazione standard, VaR e CVaR, con richiamo alla definizione del CVaR mediante quantili adottata nel Capitolo 9.
- Cella codice: calcolo delle statistiche descrittive per entrambi i portafogli.
- Cella codice: calcolo di $VaR_{0.95}$, $CVaR_{0.95}$, $VaR_{0.99}$ e $CVaR_{0.99}$ direttamente sulle distribuzioni empiriche delle perdite monetarie.
- Cella codice: implementazione del CVaR secondo la definizione mediante quantili adottata nel Capitolo 9, in modo coerente anche nel caso di distribuzioni empiriche discrete.
- Cella codice: calcolo dei differenziali
  $$
  \Delta\rho
  =
  \rho(L_{\mathrm{lim}}^P)
  -
  \rho(L_{\mathrm{base}}^P).
  $$
- Cella codice: calcolo della probabilità simulata di ingresso almeno una volta nel regime $C$.
- Cella codice: calcolo del numero medio di default.
- Cella codice: calcolo delle perdite medie del portafoglio iniziale condizionate alle repliche con e senza ingresso nel regime $C$.
- Output: Tabella 3 — misure di rischio.
- Output: Tabella 4 — regime sistemico e perdita.
- Controllo: VaR e CVaR vengono ricalcolati direttamente sulle distribuzioni empiriche delle perdite monetarie dei due portafogli e confrontati con le misure memorizzate.
- Controllo: la ragionevole stabilità delle principali misure di rischio viene verificata, per entrambi i portafogli, confrontando il campione Monte Carlo completo con un sotto-campione sufficientemente ampio.
- Nota sul controllo di stabilità: il confronto costituisce una verifica empirica di sensibilità alla numerosità delle simulazioni e non una dimostrazione formale di convergenza.

### Tappa 6 — Rappresentazione grafica e controlli conclusivi

**Prompt di riferimento:** Prompt tappa 6 — Regime B.

- Cella codice/output: Figura 1 — distribuzione della perdita del portafoglio iniziale con indicazione di VaR 95% e VaR 99%.
- Cella codice/output: Figura 2 — confronto delle code delle distribuzioni dei due portafogli.
- Cella codice/output: Figura 3 — confronto delle perdite nelle repliche con e senza ingresso nel regime $C$.
- Cella Markdown: ricognizione complessiva dell'esito dei controlli richiesti dalla Scheda Caso.
- Controllo: coerenza tra grafici, tabelle e risultati numerici.
- Controllo: verifica conclusiva della copertura degli output e dei controlli previsti.

### Interpretazione finanziaria finale dello studente

Dopo il completamento e la validazione delle sei tappe operative, il notebook deve contenere una cella Markdown dedicata all'interpretazione finanziaria finale.

L'interpretazione deve essere formulata autonomamente dallo studente e deve distinguere almeno:

- ruolo del regime sistemico nelle migrazioni;
- ruolo del regime sistemico nella severità del default;
- differenza fra rischio idiosincratico e dipendenza sistemica;
- effetto della concentrazione Evergrande;
- effetto del limite single-name;
- significato finanziario di VaR e CVaR;
- assenza di dominanza replica per replica tra le due allocazioni;
- limiti delle matrici omogenee e delle LGD deterministiche per regime;
- differenza tra modello didattico ex ante e successivi eventi storici.

Per questa fase non è previsto un prompt IA obbligatorio. L'eventuale Regime C può essere attivato soltanto se lo studente individua una criticità specifica da verificare; l'IA non deve produrre, riscrivere o completare l'interpretazione finale al posto dello studente.

## 10. Criteri di validazione del notebook

Il notebook è considerato valido se:

1. implementa la specifica teorico-matematica della Scheda Caso senza modificarla;

2. utilizza esclusivamente le matrici, le LGD, gli investimenti, il limite di concentrazione e gli altri parametri assegnati;

3. rispetta la scomposizione in tappe input-output validata;

4. mantiene coerenti la notazione matematica e le corrispondenti variabili computazionali;

5. simula, per ciascuna replica Monte Carlo, una sola traiettoria del regime sistemico e utilizza la medesima traiettoria per tutti i $36$ debitori; tale proprietà deve essere riconosciuta come caratteristica **PER COSTRUZIONE** dell'algoritmo;

6. preserva l'indipendenza condizionata delle migrazioni individuali mediante estrazioni casuali distinte per i differenti debitori, condizionatamente alla traiettoria sistemica comune; anche questa proprietà deve essere riconosciuta come **PER COSTRUZIONE**;

7. mantiene lo stato di default $D$ assorbente e identifica correttamente, per ciascun debitore, il primo ingresso nello stato $D$ mediante il tempo di default $\tau_i$;

8. verifica, sull'intero insieme dei default simulati, che la perdita da default utilizzi la LGD associata al regime sistemico $M_{\tau_i-1}$ che governa la transizione verso $D$;

9. applica la funzione di perdita migration-based $\varphi(X_{i,0},X_{i,4})$ esclusivamente ai debitori che non entrano in default entro l'orizzonte e applica esclusivamente la perdita basata sulla LGD ai debitori in default; la verifica deve riguardare l'intero insieme delle osservazioni pertinenti e non singoli casi campione;

10. costruisce correttamente il portafoglio soggetto al limite, mantenendo l'investimento complessivo pari a $200$ milioni e riallocando esattamente $10$ milioni esclusivamente tra le posizioni inizialmente BBB e BB secondo la regola proporzionale assegnata;

11. utilizza esattamente le stesse traiettorie sistemiche e creditizie per confrontare il portafoglio iniziale e quello soggetto al limite; tale proprietà deve derivare dal riutilizzo degli stessi oggetti simulati e deve essere riconosciuta come proprietà strutturale del confronto mediante *Common Random Numbers*;

12. riconcilia, per ciascuna replica e per entrambi i portafogli, le perdite aggregate con la somma delle perdite individuali;

13. produce tutti gli output numerici, tabellari e grafici richiesti dalla Scheda Caso;

14. calcola VaR e CVaR direttamente sulle distribuzioni empiriche delle perdite monetarie dei due portafogli;

15. implementa il CVaR secondo la definizione mediante quantili adottata nel Capitolo 9, in modo coerente anche nel caso di distribuzioni empiriche discrete, senza sostituirlo automaticamente con la media delle osservazioni maggiori o uguali al VaR;

16. imposta correttamente il seed assegnato $2027$ come condizione per la riproducibilità della simulazione a parità di implementazione e ambiente computazionale; la validazione non deve essere ricondotta a condizioni numeriche estranee all'impostazione del generatore casuale;

17. verifica la ragionevole stabilità delle principali misure di rischio per entrambi i portafogli confrontando le stime ottenute sul campione Monte Carlo completo con quelle ottenute su un sotto-campione sufficientemente ampio; tale verifica costituisce un controllo empirico di sensibilità alla numerosità delle simulazioni e non una dimostrazione formale di convergenza;

18. conclude con una sintesi esplicita dei controlli effettuati, distinguendo chiaramente:
   - controlli numerici o computazionali effettivamente verificati;
   - proprietà strutturali documentate **PER COSTRUZIONE**;
   - eventuali controlli di sensibilità empirica;

19. mantiene coerenza tra grafici, tabelle, misure di rischio e risultati numerici;

20. conclude con un'interpretazione finanziaria coerente con gli output e con i limiti del modello, senza attribuire al modello didattico una valenza di previsione storica o empirica non prevista dalla specifica.

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

Il risultato non deve tuttavia essere interpretato come una dominanza deterministica del portafoglio soggetto al limite. I due portafogli utilizzano le stesse repliche, ma in alcune realizzazioni la riallocazione sulle altre posizioni può produrre una perdita superiore a quella del portafoglio iniziale.

La politica viene valutata sulla **distribuzione complessiva delle perdite**, non sulla superiorità in ogni singola replica.

### 11.4 Ruolo del regime sistemico

Con la calibrazione assegnata:

- la probabilità simulata di raggiungere il regime $C$ almeno una volta è circa il $37.1\%$;
- il numero medio di default è circa $5.36$ per replica;
- la perdita media del portafoglio iniziale nelle repliche che visitano $C$ è circa $40.92$ milioni;
- la perdita media nelle repliche che non visitano $C$ è circa $17.50$ milioni.

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
- verifica dell'utilizzo delle stesse traiettorie simulate nei due portafogli;
- riconciliazione delle perdite individuali e aggregate;
- riproducibilità;
- stabilità delle misure di rischio al crescere delle simulazioni;
- confronto tra repliche con e senza ingresso nel regime di crisi.

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
5. confrontare il portafoglio iniziale con quello soggetto al limite di concentrazione utilizzando le stesse traiettorie simulate;
6. stimare e interpretare perdita attesa, dispersione, VaR e CVaR;
7. valutare l'effetto della politica di concentrazione sulla distribuzione complessiva delle perdite e sulle misure di coda;
8. distinguere i risultati prodotti dal modello didattico dagli eventi storici successivamente osservati;
9. formulare autonomamente un'interpretazione finanziaria coerente con le ipotesi, gli output e i limiti del modello.

### Calibrazione qualitativa

Il caso è considerato didatticamente ben calibrato se:

- il portafoglio iniziale presenta una concentrazione chiaramente visibile sulla posizione Evergrande;
- il limite single-name modifica in modo economicamente leggibile la distribuzione delle perdite senza produrre una dominanza deterministica replica per replica;
- il regime sistemico influenza in misura osservabile sia le probabilità di migrazione e default sia la severità della perdita;
- le repliche che raggiungono il regime di crisi presentano, in media, perdite sensibilmente superiori alle altre repliche;
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