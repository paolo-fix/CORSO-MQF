# Lezione 10 — Scheda Caso Aula

## 1. Identificazione del caso

- **Lezione:** 10 — Applicazione in Python: rischio di credito
- **Tipo di caso:** Aula
- **Titolo:** China Evergrande 2021: crisi immobiliare, dipendenza sistemica e controllo della concentrazione creditizia
- **Contesto sintetico:** estate 2021, fase di forte deterioramento delle condizioni finanziarie del settore immobiliare cinese e del merito creditizio di China Evergrande Group.
- **Uso previsto:** sviluppo guidato in aula di un modello Monte Carlo per il rischio creditizio di portafoglio.

La presente Scheda Caso costituisce la **specifica vincolante del lavoro**. Variabili, stati, parametri, formule, ipotesi, output e controlli indicati non devono essere modificati durante lo svolgimento.

La Scheda Caso definisce il problema ma **non ne contiene la soluzione**.

---

## 2. Contesto e domanda quantitativa

Si considera un portafoglio di esposizioni creditizie verso 36 debitori cinesi appartenenti a differenti classi di rating. Una delle posizioni, riferita a China Evergrande Group, rappresenta una quota rilevante dell'investimento complessivo.

Il rischio creditizio dipende da due componenti:

1. l'evoluzione individuale del rating dei singoli debitori;
2. un regime sistemico comune che rappresenta le condizioni del settore immobiliare e del credito.

Il regime sistemico può trovarsi in tre stati:

- $N$: normalizzazione;
- $S$: stress;
- $C$: crisi.

Il regime evolve trimestralmente secondo una catena di Markov. La matrice di migrazione creditizia applicata a ciascun debitore dipende dal regime sistemico corrente.

Condizionatamente alla traiettoria del regime comune, le migrazioni dei differenti debitori sono assunte indipendenti. Incondizionatamente, le loro perdite risultano invece dipendenti perché tutti i debitori sono esposti alla medesima evoluzione sistemica.

La severità della perdita in caso di default dipende inoltre dal regime sistemico nel quale il default si verifica.

La domanda quantitativa è:

**quale distribuzione della perdita a un anno produce il portafoglio e come cambiano perdita attesa, dispersione, VaR e CVaR se viene introdotto un limite del 10% alla concentrazione verso un singolo debitore, riducendo l'investimento in Evergrande e riallocando la quota liberata verso posizioni inizialmente BBB e BB?**

---

## 3. Modello e struttura del problema

### 3.1 Grandezze economico-finanziarie

Per ogni debitore \(i\), \(V_{i,0}\) rappresenta l'investimento iniziale.

Nel caso didattico si assume:

$$
\operatorname{EAD}_i=V_{i,0}.
$$

Questa uguaglianza costituisce una semplificazione specifica del caso e non una identificazione generale tra investimento iniziale ed EAD.

La perdita individuale è indicata con \(L_i\), mentre la perdita di portafoglio è

$$
L^P
=
\sum_{i=1}^{36}L_i.
$$

Il portafoglio iniziale presenta un investimento complessivo pari a

$$
V_0^P=200
$$

milioni di dollari.

La posizione Evergrande è pari a

$$
V_{E,0}=30,
$$

ossia al \(15\%\) dell'investimento complessivo.

### 3.2 Variabili casuali e stati del modello

Si considera il processo di regime sistemico

$$
\{M_t\}_{t=0}^{3},
$$

con

$$
M_t\in\{N,S,C\}.
$$

Il regime iniziale è

$$
M_0=S.
$$

Le probabilità di transizione sono descritte dalla matrice \(Q\) riportata nella Sezione 4.

Per ogni debitore \(i\), il rating evolve secondo

$$
\{X_{i,t}\}_{t=0}^{4},
$$

con spazio degli stati

$$
\mathcal{I}
=
\{BBB,BB,B,CCC,D\}.
$$

Lo stato \(D\) rappresenta il default ed è assorbente.

Per ogni debitore si definisce inoltre il tempo di default

$$
\tau_i
=
\min
\left\{
t\in\{1,\ldots,4\}:
X_{i,t}=D
\right\}.
$$

Se il debitore non entra in default entro l'orizzonte considerato, si pone

$$
\tau_i>4.
$$

### 3.3 Eventi, stati informativi e dipendenza

Condizionatamente alla traiettoria

$$
M_0,M_1,M_2,M_3,
$$

le migrazioni dei differenti debitori sono indipendenti.

Il regime sistemico è invece comune all'intero portafoglio. Una realizzazione sfavorevole di \(M_t\) modifica simultaneamente le probabilità di downgrade e default di tutti i debitori.

Se il default si verifica durante la transizione da \(t\) a \(t+1\), il regime rilevante per la perdita da default è \(M_t\).

### 3.4 Relazioni strutturali e formule principali

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
P^{(N)},\qquad
P^{(S)},\qquad
P^{(C)}.
$$

Se il debitore non entra in default entro l'orizzonte:

$$
L_i
=
V_{i,0}
\varphi(X_{i,0},X_{i,4}),
\qquad
\tau_i>4,
$$

dove \(\varphi\) è il tasso di perdita migration-based assegnato.

Se invece il debitore entra in default:

$$
L_i
=
V_{i,0}
\operatorname{LGD}^{(M_{\tau_i-1})},
\qquad
\tau_i\leq4.
$$

### 3.5 Soglie, target e vincoli

Si considera una politica alternativa che impone

$$
\max_i
\frac{V_{i,0}}{V_0^P}
\leq
10\%.
$$

L'investimento massimo consentito per un singolo debitore è pertanto

$$
20.
$$

La posizione Evergrande viene ridotta da \(30\) a \(20\) milioni.

I \(10\) milioni liberati vengono redistribuiti **esclusivamente** tra le posizioni inizialmente BBB e BB, proporzionalmente ai rispettivi investimenti iniziali.

Il portafoglio iniziale e quello soggetto al limite devono essere confrontati utilizzando **le stesse traiettorie sistemiche e creditizie simulate**.

---

## 4. Parametri assegnati

### 4.1 Matrice di transizione del regime sistemico

$$
Q=
\begin{pmatrix}
0.84 & 0.15 & 0.01\\
0.20 & 0.62 & 0.18\\
0.08 & 0.30 & 0.62
\end{pmatrix}.
$$

L'ordine degli stati è:

$$
(N,S,C).
$$

### 4.2 Matrici di migrazione creditizia

L'ordine degli stati creditizi è:

$$
(BBB,BB,B,CCC,D).
$$

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

### 4.3 Portafoglio iniziale

Gli importi sono espressi in milioni di dollari.

| Gruppo | Numero debitori | Rating iniziale | Investimento per debitore | Investimento complessivo |
|---|---:|:---:|---:|---:|
| China Evergrande Group | 1 | B | 30 | 30 |
| Debitori BBB | 10 | BBB | 6 | 60 |
| Debitori BB | 10 | BB | 5 | 50 |
| Altri debitori B | 10 | B | 4 | 40 |
| Debitori CCC | 5 | CCC | 4 | 20 |
| **Totale** | **36** |  |  | **200** |

### 4.4 Tassi di perdita migration-based

Per i debitori che non entrano in default:

| Rating iniziale $\backslash$ finale | BBB | BB | B | CCC |
|---|---:|---:|---:|---:|
| BBB | 0.00 | 0.04 | 0.11 | 0.26 |
| BB | -0.03 | 0.00 | 0.07 | 0.19 |
| B | -0.07 | -0.04 | 0.00 | 0.13 |
| CCC | -0.12 | -0.08 | -0.04 | 0.00 |

I valori negativi rappresentano incrementi di valore rispetto al riferimento iniziale.

### 4.5 LGD in caso di default

$$
\operatorname{LGD}^{(N)}=0.55,
$$

$$
\operatorname{LGD}^{(S)}=0.70,
$$

$$
\operatorname{LGD}^{(C)}=0.85.
$$

### 4.6 Portafoglio soggetto al limite

La posizione Evergrande viene ridotta a

$$
20.
$$

I $10$ milioni liberati sono redistribuiti tra BBB e BB.

Il nuovo portafoglio è:

| Gruppo | Numero debitori | Rating iniziale | Investimento per debitore | Investimento complessivo |
|---|---:|:---:|---:|---:|
| China Evergrande Group | 1 | B | 20.0000 | 20.0000 |
| Debitori BBB | 10 | BBB | 6.5455 | 65.4545 |
| Debitori BB | 10 | BB | 5.4545 | 54.5455 |
| Altri debitori B | 10 | B | 4.0000 | 40.0000 |
| Debitori CCC | 5 | CCC | 4.0000 | 20.0000 |
| **Totale** | **36** |  |  | **200.0000** |

### 4.7 Parametri computazionali

Numero di repliche Monte Carlo:

$$
N_{\mathrm{MC}}=50\,000.
$$

Seed:

$$
2027.
$$

Orizzonte:

$$
T=4
$$

trimestri, pari a un anno.

---

## 5. Quantità da stimare o calcolare

Per il portafoglio iniziale e per quello soggetto al limite devono essere determinate:

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

7. il numero medio di default nel portafoglio;

8. la perdita media del portafoglio iniziale condizionata:
   - agli scenari nei quali il regime $C$ viene raggiunto;
   - agli scenari nei quali il regime $C$ non viene raggiunto;

9. per ciascuna misura di rischio $\rho$, la variazione

$$
\Delta\rho
=
\rho(L_{\mathrm{lim}}^P)
-
\rho(L_{\mathrm{base}}^P);
$$

10. la differenza scenario per scenario

$$
\Delta L^{(r)}
=
L_{\mathrm{lim}}^{P,(r)}
-
L_{\mathrm{base}}^{P,(r)}.
$$

---

## 6. Output richiesti

### 6.1 Risultati numerici

Per entrambi i portafogli devono essere riportati:

- perdita media;
- varianza;
- deviazione standard;
- VaR 95%;
- CVaR 95%;
- VaR 99%;
- CVaR 99%.

Devono inoltre essere costruite:

- la distribuzione empirica della perdita del portafoglio iniziale;
- la distribuzione empirica della perdita del portafoglio soggetto al limite;
- la distribuzione empirica di

$$
\Delta L^{(r)}
=
L_{\mathrm{lim}}^{P,(r)}
-
L_{\mathrm{base}}^{P,(r)}.
$$

Devono inoltre essere riportati:

- probabilità simulata di ingresso nel regime $C$;
- numero medio di default;
- perdita media negli scenari con e senza ingresso in $C$;
- differenze tra le misure di rischio dei due portafogli;
- incidenza della politica di concentrazione sulle misure di coda.

### 6.2 Tabelle

**Tabella 1 — Portafoglio iniziale**

Composizione per rating, numero di debitori, investimento individuale e investimento complessivo.

**Tabella 2 — Portafoglio soggetto al limite**

Composizione del portafoglio dopo la riduzione della posizione Evergrande e la riallocazione dell'investimento.

**Tabella 3 — Misure di rischio**

Confronto tra:

- portafoglio iniziale;
- portafoglio soggetto al limite;
- differenza tra le rispettive misure.

**Tabella 4 — Regime sistemico e perdita**

Confronto, per il portafoglio iniziale, tra scenari con e senza ingresso nello stato $C$.

### 6.3 Grafici

**Figura 1 — Distribuzione della perdita del portafoglio iniziale**

Distribuzione empirica di $L_{\mathrm{base}}^P$ con indicazione di VaR 95% e VaR 99%.

**Figura 2 — Confronto delle code**

Confronto tra le distribuzioni delle perdite del portafoglio iniziale e del portafoglio soggetto al limite, con particolare attenzione alla coda destra.

**Figura 3 — Regime sistemico e perdita**

Confronto della distribuzione delle perdite del portafoglio iniziale tra scenari con ingresso nel regime $C$ e scenari senza ingresso nel regime $C$.

---

## 7. Controlli richiesti

Devono essere verificati almeno i seguenti punti.

### Controlli numerici

1. Verifica che ogni riga della matrice di transizione di regime \(Q\) sommi a 1.

2. Verifica che ogni riga delle matrici di migrazione creditizia \(P^{(N)}\), \(P^{(S)}\) e \(P^{(C)}\) sommi a 1.

11. Verifica che l'investimento complessivo \(V_0^P\) sia pari a 200 milioni di USD in entrambi i portafogli.

12. Verifica che nel portafoglio soggetto al limite:
   - la posizione Evergrande sia pari a 20 milioni di USD;
   - vengano riallocati esattamente 10 milioni di USD;
   - la riallocazione interessi esclusivamente i gruppi BBB e BB;
   - sia mantenuta la proporzione relativa originale tra gli investimenti dei gruppi BBB e BB.

14. Verifica che la perdita aggregata di portafoglio coincida con la somma delle perdite dei singoli debitori.

16. Verifica della stabilità delle stime delle principali misure di rischio all'aumentare delle simulazioni Monte Carlo.

17. Verifica che VaR e CVaR siano calcolati direttamente sulle distribuzioni delle perdite monetarie dei due portafogli.

### Controlli logici o teorici

3. Verifica che lo stato di default \(D\) risulti assorbente in tutte le matrici di migrazione creditizia.

4. Verifica che il regime sistemico iniziale sia \(M_0=S\) in ogni replica Monte Carlo.

5. Verifica che all'interno della stessa replica esista una sola traiettoria sistemica, comune a tutti i 36 debitori.

6. Verifica che, condizionatamente alla traiettoria di regime comune, le estrazioni stocastiche per le migrazioni dei debitori siano indipendenti.

7. Verifica che il tempo di default \(\tau_i\) coincida esattamente con il primo trimestre di ingresso nello stato \(D\).

8. Verifica che la LGD applicata in caso di default corrisponda al regime sistemico \(M_{\tau_i-1}\) che governa la transizione verso \(D\).

9. Verifica che un debitore entrato nello stato \(D\) non possa successivamente uscire dal default.

10. Verifica che la funzione di perdita migration-based \(\varphi\) sia applicata unicamente ai debitori che non sono entrati in default \((\tau_i>4)\).

### Controlli computazionali

13. Verifica che il confronto tra portafoglio iniziale e portafoglio soggetto al limite utilizzi rigorosamente le medesime traiettorie sistemiche e creditizie simulate.

15. Verifica la riproducibilità esatta dei risultati numerici impostando il seed 2027.

---

## 8. Ipotesi e limiti del caso

Il modello assume che:

1. il regime sistemico sia una catena di Markov omogenea;
2. le matrici di migrazione siano omogenee all'interno di ciascun regime;
3. tutti i debitori con lo stesso rating corrente utilizzino la medesima matrice di migrazione;
4. le migrazioni individuali siano indipendenti condizionatamente al regime sistemico comune;
5. il default sia assorbente;
6. gli investimenti iniziali siano deterministici;
7. nel caso didattico valga

$$
\operatorname{EAD}_i=V_{i,0};
$$

8. la LGD sia deterministica una volta noto il regime sistemico nel quale avviene il default;
9. la funzione di perdita non-default dipenda soltanto dal rating iniziale e da quello finale;
10. le probabilità utilizzate siano probabilità fisiche.

Il modello non incorpora:

- matrici di transizione specifiche per singolo emittente;
- differenze settoriali tra le matrici dei debitori;
- contagio diretto tra imprese e intermediari;
- EAD stocastica;
- LGD specifica per singolo debitore;
- collateral e seniority;
- rischio valutario;
- rischio di liquidità;
- interventi governativi o ristrutturazioni;
- probabilità risk-neutral;
- pricing di obbligazioni o CDS.

Le matrici di transizione, i tassi di perdita, le LGD e gli investimenti assegnati costituiscono una **calibrazione didattica**.

I bucket di rating utilizzati nel modello non devono essere interpretati come ricostruzione esatta dei rating storicamente attribuiti a Evergrande da una specifica agenzia.

I risultati ottenuti descrivono il comportamento del modello quantitativo assegnato e non costituiscono una previsione retrospettiva degli eventi storici successivamente osservati.
