# Scheda Costruzione Caso Applicativo

Documento interno di progettazione docente.  
**Lezione 7 — Caso TakeHome.**

## 1. Identificazione del caso

- **Lezione:** 7 — Applicazione in Python: simulazione di traiettorie e pricing
- **Tipo di caso:** TakeHome
- **Titolo:** *Pricing Monte Carlo di una call asiatica sull'EURO STOXX 50 con tasso di interesse stocastico*
- **Destinatari:** studenti del secondo anno del Corso di Laurea Magistrale in Finanza e Risk Management
- **Uso previsto:** lavoro autonomo successivo alla lezione applicativa, sviluppato mediante notebook Jupyter e uso documentato dell'IA secondo il protocollo MQF
- **Data di riferimento del caso:** 27 luglio 2026

Il caso consolida operativamente i contenuti dei Capitoli 5 e 6 e trasferisce al Caso TakeHome l'architettura quantitativa sviluppata nel Capitolo 7:

- organizzazione di molte traiettorie simulate;
- distinzione tra dimensione temporale e dimensione Monte Carlo;
- diffusione geometrica dell'indice con drift stocastico;
- dividend yield nel drift risk-neutral;
- processo CIR per il tasso nominale;
- simulazione con shock correlati;
- costruzione di una quantità path-dependent;
- attualizzazione replica per replica;
- pricing e diagnostica Monte Carlo.

La Scheda Costruzione costituisce il documento docente a monte della Scheda Caso, del Flusso logico-teorico risolutivo, della scomposizione in tappe, della sequenza dei prompt, del notebook e del tracciato IA.

Il Caso TakeHome deve essere metodologicamente confrontabile con il Caso Aula sull'inflation-linked bond, senza costituirne una semplice variazione parametrica.

---

## 2. Contesto e motivazione

### 2.1 Contesto finanziario

Il sottostante è l'**EURO STOXX 50**, benchmark azionario dell'area euro e sottostante di un mercato liquido di futures e opzioni vanilla.

Il caso è collocato al **27 luglio 2026**. Il valore iniziale utilizzato è

$$
S_0=6\,286.35.
$$

Lo strike è fissato a

$$
K=6\,300,
$$

così da considerare un contratto sostanzialmente at-the-money all'origine.

Il livello iniziale dello short rate viene ancorato all'€STR del 27 luglio 2026:

$$
r_0=0.02185.
$$

Per il dividend yield continuo si utilizza la proxy

$$
q=0.025,
$$

mentre per la volatilità dell'indice si assume

$$
\sigma_S=0.18.
$$

I valori di $q$ e $\sigma_S$ hanno funzione di proxy market-consistent e non costituiscono una calibrazione esatta.

I restanti parametri CIR e la correlazione tra indice e tasso sono assegnati a fini didattici.

### 2.2 Natura del contratto

Il prodotto è una **call asiatica OTC a media aritmetica**.

Il payoff non dipende esclusivamente da $S_T$, ma dalla media dei livelli dell'indice osservati a dodici date di fixing mensili.

La scelta rende direttamente osservabile la path-dependence:

$$
\text{traiettoria di }S_t
\longrightarrow
\text{fixing}
\longrightarrow
A_T
\longrightarrow
H_T.
$$

L'averaging riduce la dipendenza del payoff da un singolo fixing terminale. Nel caso didattico la struttura Asian viene utilizzata per mostrare perché l'intera traiettoria simulata può essere necessaria anche quando il contratto genera un unico payoff terminale.

Il contratto è stilizzato e OTC. Non deve essere presentato come un'opzione asiatica quotata su Eurex.

### 2.3 Funzione didattica

Il Caso TakeHome non deve riprodurre meccanicamente il notebook del Caso Aula.

Lo studente deve riconoscere e trasferire la stessa architettura quantitativa:

$$
\text{fattori stocastici}
\rightarrow
\text{shock correlati}
\rightarrow
\text{traiettorie}
\rightarrow
\text{quantità path-dependent}
$$

$$
\rightarrow
\text{payoff}
\rightarrow
\text{attualizzazione per replica}
\rightarrow
\text{stima Monte Carlo}
\rightarrow
\text{diagnostica e interpretazione}.
$$

Cambiano il primo fattore di rischio e il funzionale della traiettoria; rimane invariato il metodo generale.

---

## 3. Domanda quantitativa e obiettivo didattico

### Domanda quantitativa

**Qual è il valore corrente di una call asiatica a media aritmetica sull'EURO STOXX 50 quando il livello dell'indice e il tasso nominale evolvono congiuntamente in modo stocastico sotto la misura risk-neutral $\mathbb Q$?**

In particolare, occorre passare dalle traiettorie simulate dei due fattori alla media asiatica, al payoff, al fattore di sconto della stessa replica e infine al prezzo Monte Carlo.

### Obiettivo didattico

Lo studente deve comprendere e costruire la catena

$$
\text{diffusione geometrica di }S_t
+
\text{CIR per }r_t
$$

$$
\downarrow
$$

$$
\text{shock correlati e traiettorie}
$$

$$
\downarrow
$$

$$
\text{fixing mensili}
\rightarrow
A_T
$$

$$
\downarrow
$$

$$
H_T=(A_T-K)^+
$$

$$
\downarrow
$$

$$
D(0,T)H_T
$$

$$
\downarrow
$$

$$
V^{(k)}
\rightarrow
\widehat V_M
$$

$$
\downarrow
$$

$$
\text{diagnostica e interpretazione}.
$$

Il caso deve consolidare in particolare:

1. la distinzione tra valore terminale $S_T$ e funzionale path-dependent $A_T$;
2. la selezione delle sole date contrattuali dalla griglia di simulazione;
3. la costruzione del payoff replica per replica prima dell'aggregazione;
4. l'attualizzazione mediante la traiettoria del tasso appartenente alla stessa replica;
5. la distinzione tra operazioni lungo il tempo e aggregazioni tra repliche;
6. la distinzione tra dati osservati, proxy di mercato e parametri modellistici didattici;
7. la distinzione tra risultato del modello assegnato e quotazione operativa di mercato.

---

## 4. Specifica teorico-matematica

### 4.1 Convenzione Monte Carlo

Il numero di repliche è indicato con

$$
M.
$$

La singola replica è indicata con

$$
k=1,\ldots,M.
$$

Per un processo $X_t$, il valore al tempo $t_j$ nella replica $k$ è indicato con

$$
X_{t_j}^{(k)}.
$$

L'intera traiettoria della replica $k$ è rappresentata da

$$
X^{(k)}
=
\left(
X_{t_0}^{(k)},\ldots,X_{t_N}^{(k)}
\right).
$$

Il termine **scenario** non deve essere utilizzato per indicare una replica Monte Carlo.

### 4.2 Misura di pricing

Le dinamiche dei fattori sono assegnate direttamente sotto la misura risk-neutral

$$
\mathbb Q.
$$

La simulazione Monte Carlo approssima quindi il valore atteso attualizzato del payoff sotto $\mathbb Q$.

Non viene richiesto allo studente di derivare il cambio di misura.

### 4.3 Dinamica del sottostante

Il livello dell'EURO STOXX 50 segue la diffusione geometrica

$$
dS_t
=
(r_t-q)S_t\,dt
+
\sigma_S S_t\,dW_t^{(S)}.
$$

Il drift è stocastico perché dipende dal tasso istantaneo $r_t$, al netto del dividend yield continuo $q$.

Questa dinamica non deve essere descritta nel caso come un GBM standard a drift costante.

### 4.4 Dinamica del tasso nominale

Il tasso nominale istantaneo segue un processo CIR:

$$
dr_t
=
\kappa_r(\theta_r-r_t)\,dt
+
\sigma_r\sqrt{r_t}\,dW_t^{(r)}.
$$

I parametri assegnati soddisfano la condizione di Feller:

$$
2\kappa_r\theta_r
\geq
\sigma_r^2.
$$

### 4.5 Convenzione numerica vincolante per il CIR

Il Caso TakeHome utilizza la medesima convenzione numerica fissata nel Caso Aula.

Sulla griglia temporale:

$$
r_{t_{j+1}}^{(k)}
=
r_{t_j}^{(k)}
+
\kappa_r
\left(
\theta_r-r_{t_j}^{(k)}
\right)\Delta t
+
\sigma_r
\sqrt{\max(r_{t_j}^{(k)},0)}
\sqrt{\Delta t}\,
Z_{r,j+1}^{(k)}.
$$

L'operatore

$$
\max(r_{t_j}^{(k)},0)
$$

agisce esclusivamente all'interno della radice quadrata.

Il valore aggiornato $r_{t_{j+1}}^{(k)}$ non deve essere successivamente forzato a zero.

Eventuali valori negativi prodotti dalla discretizzazione devono essere mantenuti, rilevati, conteggiati e documentati come possibile anomalia numerica.

Il TakeHome non deve introdurre autonomamente una diversa tecnica di simulazione del CIR.

### 4.6 Dipendenza tra i fattori

I moti browniani soddisfano

$$
dW_t^{(S)}\,dW_t^{(r)}
=
\rho\,dt.
$$

Per ogni replica $k$ e intervallo temporale $j$, a partire da due normali standard indipendenti

$$
Z_{1,j}^{(k)},
\qquad
Z_{2,j}^{(k)},
$$

si costruiscono

$$
Z_{S,j}^{(k)}
=
Z_{1,j}^{(k)},
$$

$$
Z_{r,j}^{(k)}
=
\rho Z_{1,j}^{(k)}
+
\sqrt{1-\rho^2}\,
Z_{2,j}^{(k)}.
$$

La correlazione empirica da verificare riguarda gli **shock**, non i livelli simulati di $S_t$ e $r_t$.

Gli shock dei due fattori devono appartenere allo stesso intervallo temporale e alla stessa replica.

### 4.7 Discretizzazione del sottostante

Per preservare la struttura moltiplicativa e la positività del sottostante, si utilizza una discretizzazione logaritmica:

$$
S_{t_{j+1}}^{(k)}
=
S_{t_j}^{(k)}
\exp
\left[
\left(
r_{t_j}^{(k)}
-q
-\frac12\sigma_S^2
\right)\Delta t
+
\sigma_S\sqrt{\Delta t}\,
Z_{S,j+1}^{(k)}
\right].
$$

Ne consegue per costruzione

$$
S_{t_j}^{(k)}>0.
$$

Il tasso utilizzato nel drift sul passo è quello della stessa replica.

### 4.8 Griglia e date di fixing

La scadenza è

$$
T=1
$$

anno.

La griglia principale utilizza

$$
N=252,
\qquad
\Delta t=\frac1{252}.
$$

Sono quindi presenti $253$ nodi, inclusa la data iniziale.

Le dodici date contrattuali di fixing sono indicate con

$$
\tau_h=\frac{h}{12},
\qquad
h=1,\ldots,12.
$$

Poiché

$$
\frac{252}{12}=21,
$$

i fixing corrispondono ai passi

$$
21,42,\ldots,252.
$$

Il valore iniziale $S_0$ non entra nella media asiatica.

### 4.9 Media asiatica

Per ogni replica $k$,

$$
A_T^{(k)}
=
\frac1{12}
\sum_{h=1}^{12}
S_{\tau_h}^{(k)}.
$$

Deve valere

$$
\min_h S_{\tau_h}^{(k)}
\leq
A_T^{(k)}
\leq
\max_h S_{\tau_h}^{(k)}.
$$

La media deve essere calcolata sui soli dodici fixing contrattuali, non su tutti i punti della griglia.

### 4.10 Payoff

Il payoff della call asiatica nella replica $k$ è

$$
H_T^{(k)}
=
\max
\left(
A_T^{(k)}-K,0
\right).
$$

Devono valere

$$
H_T^{(k)}\geq0
$$

e

$$
A_T^{(k)}\leq K
\quad\Longrightarrow\quad
H_T^{(k)}=0.
$$

Il payoff deve essere costruito separatamente in ciascuna replica prima di qualsiasi media tra simulazioni.

### 4.11 Fattore di sconto

In tempo continuo,

$$
D(0,T)
=
\exp
\left(
-\int_0^T r_u\,du
\right).
$$

Nel caso computazionale, per la replica $k$,

$$
\int_0^T r_u^{(k)}\,du
\approx
\sum_{j=0}^{N-1}
r_{t_j}^{(k)}\Delta t,
$$

mediante somma di Riemann sinistra.

Il fattore di sconto è quindi

$$
\widehat D^{(k)}(0,T)
=
\exp
\left(
-\sum_{j=0}^{N-1}
r_{t_j}^{(k)}\Delta t
\right).
$$

Deve risultare

$$
\widehat D^{(k)}(0,T)>0.
$$

Non deve essere utilizzato il solo $r_T^{(k)}$, né un tasso medio calcolato trasversalmente sulle repliche.

### 4.12 Valore attualizzato per replica

Il valore attualizzato del payoff nella replica $k$ è

$$
V^{(k)}
=
\widehat D^{(k)}(0,T)
H_T^{(k)}.
$$

La costruzione deve utilizzare payoff e fattore di sconto appartenenti alla stessa replica.

### 4.13 Stima Monte Carlo

Il prezzo stimato è

$$
\widehat V_M
=
\frac1M
\sum_{k=1}^{M}
V^{(k)}.
$$

Indicando con $s_V$ la deviazione standard campionaria dei valori $V^{(k)}$,

$$
SE(\widehat V_M)
=
\frac{s_V}{\sqrt M}.
$$

Un intervallo di confidenza Monte Carlo approssimato al $95\%$ è

$$
\widehat V_M
\pm
1.96\,SE(\widehat V_M).
$$

### 4.14 Probabilità simulata di esercizio

Poiché le traiettorie sono simulate sotto $\mathbb Q$, la frequenza campionaria di esercizio stima la corrispondente probabilità sotto la misura di pricing:

$$
\widehat{\mathbb Q}(A_T>K)
=
\frac1M
\sum_{k=1}^{M}
\mathbf 1_{\{A_T^{(k)}>K\}}.
$$

Questa quantità ha funzione descrittiva all'interno del modello assegnato e non deve essere interpretata come probabilità fisica di mercato.

---

## 5. Parametri assegnati

I parametri combinano dati osservati, proxy di mercato e scelte modellistiche didattiche. Non costituiscono una calibrazione completa del modello.

| Componente | Parametro | Valore | Natura |
|---|---|---:|---|
| Data | $t_0$ | 27/07/2026 | data di riferimento |
| Sottostante | indice | EURO STOXX 50 | riferimento di mercato |
| Sottostante | $S_0$ | 6.286,35 | dato osservato |
| Contratto | $K$ | 6.300 | scelta contrattuale |
| Contratto | $T$ | 1 anno | specifica contrattuale |
| Contratto | fixing | 12 mensili | specifica contrattuale |
| Dividendi | $q$ | 0,025 | proxy di mercato arrotondata |
| Sottostante | $\sigma_S$ | 0,18 | proxy market-consistent |
| Tasso CIR | $r_0$ | 0,02185 | dato osservato |
| Tasso CIR | $\kappa_r$ | 1,25 | parametro didattico |
| Tasso CIR | $\theta_r$ | 0,0220 | parametro didattico |
| Tasso CIR | $\sigma_r$ | 0,040 | parametro didattico |
| Dipendenza | $\rho$ | -0,25 | ipotesi modellistica |
| Simulazione | $N$ | 252 | intervalli temporali |
| Simulazione | $\Delta t$ | $1/252$ | griglia principale |
| Simulazione | $M$ | 50.000 | repliche Monte Carlo |
| Simulazione | seed | 12345 | seme pseudo-casuale |

La condizione di Feller è soddisfatta:

$$
2(1.25)(0.0220)
=
0.055
>
0.0016
=
(0.040)^2.
$$

La distinzione tra natura dei parametri deve rimanere visibile sia nella Scheda Caso sia nel notebook:

- **dati osservati:** $S_0$, $r_0$;
- **proxy di mercato:** $q$, $\sigma_S$;
- **specifiche contrattuali:** $K$, $T$, fixing;
- **parametri modellistici didattici:** $\kappa_r$, $\theta_r$, $\sigma_r$, $\rho$;
- **parametri computazionali:** $N$, $\Delta t$, $M$, seed.

---

## 6. Quantità e output richiesti

La Scheda Costruzione deve riprodurre esattamente il perimetro quantitativo destinato alla Scheda Caso.

### 6.1 Quantità numeriche obbligatorie

Devono essere determinate:

1. media e deviazione standard simulate di $S_T$ e $r_T$;
2. media e deviazione standard simulate di $A_T$;
3. probabilità simulata di esercizio sotto $\mathbb Q$,
   $\widehat{\mathbb Q}(A_T>K)$;
4. valore medio del payoff non attualizzato $H_T$;
5. prezzo Monte Carlo della call asiatica $\widehat V_M$;
6. errore standard Monte Carlo e intervallo di confidenza al $95\%$.

Non costituiscono output obbligatori aggiuntivi:

- una sensitivity analysis rispetto a $\rho$;
- una sensitivity analysis rispetto a $K$, $q$ o $\sigma_S$;
- confronti con formule chiuse o modelli alternativi;
- una calibrazione della volatilità o del CIR.

Tali analisi possono essere svolte dal docente come approfondimenti, purché restino distinte dalla consegna vincolante.

### 6.2 Tabelle obbligatorie

**Tabella 1 — Parametri del caso e natura del dato**

Contratto, dati osservati, proxy di mercato, CIR, correlazione e simulazione.

**Tabella 2 — Statistiche dei fattori e della media asiatica**

Media e deviazione standard di:

$$
S_T,
\qquad
r_T,
\qquad
A_T.
$$

**Tabella 3 — Payoff e pricing**

Almeno:

- probabilità simulata di esercizio;
- payoff medio;
- prezzo Monte Carlo;
- errore standard;
- intervallo di confidenza al $95\%$.

**Tabella 4 — Diagnostica Monte Carlo**

Per

$$
M=
1\,000,\;
5\,000,\;
10\,000,\;
50\,000
$$

riportare almeno:

- prezzo stimato;
- errore standard.

Il controllo della correlazione non richiede una tabella autonoma obbligatoria; può essere documentato mediante un output numerico locale.

### 6.3 Grafici obbligatori

Produrre almeno:

1. alcune traiettorie simulate di $S_t$;
2. alcune traiettorie simulate di $r_t$;
3. distribuzione simulata di $A_T$, con evidenza dello strike $K$;
4. distribuzione dei valori attualizzati $V^{(k)}$;
5. grafico di convergenza della stima Monte Carlo al crescere di $M$.

I grafici devono avere funzione interpretativa e riportare titoli, assi e unità coerenti.

---

## 7. Controlli obbligatori

Il notebook deve verificare esplicitamente:

1. **correlazione degli shock**

$$
\widehat\rho\approx-0.25;
$$

2. **positività del sottostante**

$$
S_{t_j}^{(k)}>0
$$

per ogni replica e data;

3. **anomalia numerica CIR**

rilevare, conteggiare e documentare eventuali valori

$$
r_{t_j}^{(k)}<0
$$

prodotti dalla discretizzazione, senza azzerare sistematicamente il valore aggiornato;

4. **coerenza della media asiatica**

$$
\min_hS_{\tau_h}^{(k)}
\leq
A_T^{(k)}
\leq
\max_hS_{\tau_h}^{(k)}
$$

per ogni replica;

5. **coerenza del payoff**

$$
H_T^{(k)}\geq0
$$

e

$$
A_T^{(k)}\leq K
\Longrightarrow
H_T^{(k)}=0;
$$

6. **coerenza dell'attualizzazione**

l'integrale del tasso deve utilizzare i valori

$$
r_{t_0}^{(k)},\ldots,r_{t_{N-1}}^{(k)}
$$

della stessa replica e deve risultare

$$
\widehat D^{(k)}(0,T)>0;
$$

7. **coerenza del valore attualizzato**

$$
V^{(k)}
=
\widehat D^{(k)}(0,T)
H_T^{(k)};
$$

8. **precisione Monte Carlo**

verificare che l'errore standard diminuisca al crescere di $M$ in modo compatibile con

$$
O(M^{-1/2});
$$

9. **stabilità rispetto alla griglia temporale**

confrontare il prezzo principale con quello ottenuto mediante almeno una griglia più fine che mantenga coerenti le date di fixing;

10. **riproducibilità**

verificare che la procedura principale sia riproducibile con il seed assegnato.

I controlli 1--7 riguardano la coerenza della costruzione quantitativa. I controlli 8 e 9 riguardano invece due differenti fonti di approssimazione:

$$
M
\longrightarrow
\text{errore Monte Carlo},
$$

$$
\Delta t
\longrightarrow
\text{errore di discretizzazione}.
$$

---

## 8. Flusso logico-teorico risolutivo atteso

Il Flusso logico-teorico deve precedere la scomposizione operativa del notebook. Non descrive il codice: ricostruisce il percorso teorico necessario per passare dalla domanda quantitativa agli output richiesti.

| Passo | Finalità risolutiva | Formula teorico-matematica / definizione / proprietà | Applicazione nel caso | Output o controllo collegato |
|---:|---|---|---|---|
| 1 | Identificare la misura e i fattori di rischio | Valutazione sotto $\mathbb Q$; diffusione geometrica e CIR | Definire $S_t$, $r_t$, condizioni iniziali e parametri | Parametri; verifica di Feller |
| 2 | Rappresentare la dipendenza | Correlazione fra Browniani | Costruire coppie di shock correlati nella stessa replica | Correlazione empirica degli shock |
| 3 | Passare dal continuo alla griglia | Discretizzazione dei due processi | Simulare $S_t^{(k)}$ e $r_t^{(k)}$ sulle $M$ repliche | Traiettorie; statistiche terminali; diagnostica CIR |
| 4 | Identificare le osservazioni contrattuali | Date di fixing | Selezionare i dodici valori $S_{\tau_h}^{(k)}$ | Controllo calendario/griglia |
| 5 | Costruire la quantità path-dependent | Media aritmetica dei fixing | Calcolare $A_T^{(k)}$ | Media, deviazione standard, distribuzione e controllo min/max |
| 6 | Identificare l'esercizio | Evento $A_T>K$ | Stimare la frequenza di esercizio sotto $\mathbb Q$ | $\widehat{\mathbb Q}(A_T>K)$ |
| 7 | Costruire il payoff | $H_T=(A_T-K)^+$ | Calcolare $H_T^{(k)}$ | Payoff medio; non negatività |
| 8 | Costruire l'attualizzazione | $D(0,T)=\exp(-\int_0^T r_u\,du)$ | Approssimare l'integrale del tasso nella stessa replica | $\widehat D^{(k)}(0,T)$; positività |
| 9 | Costruire il valore per replica | $V^{(k)}=\widehat D^{(k)}H_T^{(k)}$ | Combinare payoff e sconto della stessa replica | Distribuzione dei valori attualizzati |
| 10 | Aggregare tra repliche | Media campionaria, deviazione standard, SE | Calcolare $\widehat V_M$ e IC 95% | Tabelle di pricing |
| 11 | Valutare precisione e discretizzazione | $SE=O(M^{-1/2})$; confronto tra griglie | Variare $M$ e raffinare $\Delta t$ | Diagnostica Monte Carlo e stabilità temporale |
| 12 | Interpretare il risultato | Path-dependence, misura di pricing e limiti del modello | Collegare traiettorie, payoff, sconto e prezzo | Commento finanziario conclusivo |

Il Flusso deve restare riconoscibile nella successiva costruzione del notebook.

---

## 9. Scomposizione attesa in tappe input-output

La scomposizione operativa viene costruita **dopo** il Flusso logico-teorico. Le dodici unità concettuali precedenti vengono raccolte in sei tappe computazionali.

| Tappa | Regime ordinario | Input | Operazione principale | Output essenziali | Controlli principali | Uso successivo |
|---:|:---:|---|---|---|---|---|
| 1 | B | Scheda Caso, parametri, $M$, $N$, $\Delta t$, seed, $\rho$ | Definire ambiente, griglia e fixing; generare gli shock correlati | Tabella parametri; griglia; fixing; matrici $Z_S,Z_r$ | Feller; dimensioni; calendario; correlazione empirica | Simulazione fattori |
| 2 | B | Parametri e shock correlati | Simulare congiuntamente $S_t$ e $r_t$ con le convenzioni assegnate | Matrici delle traiettorie; statistiche di $S_T,r_T$ | $S_t>0$; anomalie CIR; coerenza dimensionale | Costruzione della media asiatica |
| 3 | B | Traiettorie $S_t$ e fixing | Estrarre i dodici fixing e costruire $A_T$; stimare l'esercizio | $A_T^{(k)}$; statistiche; $\widehat{\mathbb Q}(A_T>K)$ | Vincolo min/max; calendario dei fixing | Payoff |
| 4 | B | $A_T$, $K$, traiettorie $r_t$ | Costruire $H_T$ e $\widehat D(0,T)$ replica per replica | $H_T^{(k)}$; payoff medio; $\widehat D^{(k)}(0,T)$ | $H_T\geq0$; payoff nullo sotto strike; $D>0$ | Pricing |
| 5 | B | $H_T^{(k)}$, $\widehat D^{(k)}(0,T)$ | Calcolare $V^{(k)}$, prezzo, SE, IC e tabelle di sintesi | $\widehat V_M$; SE; IC 95%; Tabelle 2 e 3 | $V^{(k)}=\widehat D^{(k)}H_T^{(k)}$ | Diagnostica finale |
| 6 | B | Procedura completa e output precedenti | Costruire diagnostica per diversi $M$, confronto della griglia, grafici obbligatori e interpretazione conclusiva | Tabella 4; cinque grafici; confronto $\Delta t$; conclusione | $1/\sqrt M$; stabilità temporale; coerenza complessiva; rieseguibilità | Chiusura del caso |

La Tappa 6 fa parte della soluzione ordinaria e **non costituisce di per sé Regime C**.

Il Regime C viene utilizzato soltanto quando lo studente individua una criticità specifica in una formula, nel codice, in un output, in un controllo o in una bozza interpretativa.

---

## 10. Mappa tra prompt e notebook

| Prompt | Regime | Funzione | Prodotto nel notebook o nel tracciato | Vincolo |
|---|:---:|---|---|---|
| Prompt zero | — | Inizializzare contesto, regole e regimi | Nessuna cella quantitativa obbligatoria | Rispetto del protocollo |
| Prompt 1 | — | Acquisire la Scheda Caso | Cella Markdown iniziale di inquadramento | Nessuna soluzione anticipata |
| Prompt 2 | A | Costruire il Flusso logico-teorico a partire dalla proposta dello studente | Una cella Markdown con tabella del Flusso | Contributo iniziale dello studente visibile |
| Prompt 3 | — | Trasformare il Flusso validato in tappe input-output | Una cella Markdown con le sei tappe | Contributo iniziale dello studente; nessun codice |
| Prompt Tappa 1 | B | Implementare la Tappa 1 validata | Markdown + codice + output + controllo | Non modificare la Scheda Caso |
| Prompt Tappa 2 | B | Implementare la Tappa 2 validata | Markdown + codice + output + controllo | Convenzione CIR vincolante |
| Prompt Tappa 3 | B | Implementare la Tappa 3 validata | Markdown + codice + output + controllo | Usare esclusivamente i dodici fixing |
| Prompt Tappa 4 | B | Implementare la Tappa 4 validata | Markdown + codice + output + controllo | Payoff e sconto replica per replica |
| Prompt Tappa 5 | B | Implementare la Tappa 5 validata | Markdown + codice + tabelle + controllo | Aggregazione solo dopo la costruzione di $V^{(k)}$ |
| Prompt Tappa 6 | B | Completare diagnostica, grafici e supportare la lettura degli output | Codice + output; elementi utili all'interpretazione | Distinguere errori MC, discretizzazione e modello |
| Eventuale Prompt C | C | Verificare una criticità concreta individuata dallo studente | Eventuale sostituzione delle celle interessate | Non obbligatorio; nessuna certificazione generica |

L'interpretazione finanziaria finale resta responsabilità autonoma dello studente.

---

## 11. Struttura attesa del notebook

Il notebook deve rendere visibile sia il ragionamento sia la costruzione computazionale.

L'ordine atteso è:

1. **Titolo, data di riferimento e inquadramento del caso** — Markdown derivato dal Prompt 1.
2. **Flusso logico-teorico risolutivo** — Markdown derivato dal Prompt 2.
3. **Scomposizione in sei tappe input-output** — Markdown derivato dal Prompt 3.
4. **Tappa 1 — setup, griglia, fixing e shock correlati.**
5. **Tappa 2 — simulazione congiunta di indice e tasso.**
6. **Tappa 3 — fixing, media asiatica e probabilità simulata di esercizio.**
7. **Tappa 4 — payoff e fattore di sconto replica per replica.**
8. **Tappa 5 — valori attualizzati e pricing Monte Carlo.**
9. **Tappa 6 — diagnostica Monte Carlo, controllo della griglia e grafici.**
10. **Interpretazione finanziaria finale autonoma.**
11. **Limiti del modello e riproducibilità del notebook.**

Ogni tappa deve essere preceduta da una breve cella Markdown che chiarisca:

- input disponibili;
- operazione quantitativa;
- output attesi;
- controllo da eseguire;
- collegamento con la tappa successiva.

Tabelle e grafici devono essere rigenerabili mediante riesecuzione del notebook.

Non devono essere previste automaticamente esportazioni in file esterni se non richieste esplicitamente dalla consegna.

---

## 12. Criteri di validazione del notebook

### 12.1 Coerenza strutturale

Il notebook è strutturalmente coerente se:

- contiene il Flusso logico-teorico prima delle tappe;
- contiene la scomposizione input-output prima dell'implementazione;
- conserva la catena tra le sei tappe;
- non introduce output obbligatori non presenti nella Scheda Caso;
- non elimina output o controlli richiesti;
- utilizza $k=1,\ldots,M$ per le repliche Monte Carlo;
- rende riconoscibile la distinzione tra operazioni lungo il tempo e aggregazioni tra repliche.

### 12.2 Coerenza con la misura di pricing

Il notebook deve:

- utilizzare le dinamiche assegnate sotto $\mathbb Q$;
- includere il dividend yield $q$ nel drift;
- utilizzare il tasso $r_t^{(k)}$ della stessa replica nel drift del sottostante;
- costruire il prezzo come media dei payoff attualizzati replica per replica;
- non reinterpretare le frequenze simulate sotto $\mathbb Q$ come probabilità fisiche.

### 12.3 Coerenza computazionale

Devono essere verificati:

- forma degli array coerente con repliche sulle righe e tempo sulle colonne;
- corretto uso degli assi NumPy;
- allineamento degli shock dei due fattori nella stessa replica e nello stesso intervallo;
- corretta selezione dei passi $21,42,\ldots,252$;
- esclusione di $S_0$ dalla media asiatica;
- somma di Riemann costruita lungo la dimensione temporale;
- fattore di sconto costruito replica per replica;
- assenza di aggregazioni premature tra repliche.

### 12.4 Convenzione CIR

È da considerare non coerente una soluzione che:

- sostituisca sistematicamente ogni nuovo valore negativo del CIR con zero;
- introduca una diversa discretizzazione senza modifica della Scheda Caso;
- elimini i valori negativi prima di poterli diagnosticare.

La protezione numerica

$$
\sqrt{\max(r_t,0)}
$$

riguarda esclusivamente il termine diffusivo.

### 12.5 Coerenza del contratto

Devono essere rispettati:

$$
S_t^{(k)}>0,
$$

$$
\min_h S_{\tau_h}^{(k)}
\leq
A_T^{(k)}
\leq
\max_h S_{\tau_h}^{(k)},
$$

$$
H_T^{(k)}
=
\max(A_T^{(k)}-K,0),
$$

$$
V^{(k)}
=
\widehat D^{(k)}(0,T)H_T^{(k)}.
$$

### 12.6 Coerenza numerica

Devono essere distinti:

- errore Monte Carlo;
- errore di discretizzazione;
- errore di modello.

Una riduzione dell'errore standard all'aumentare di $M$ non dimostra la stabilità rispetto a $\Delta t$.

### 12.7 Riproducibilità

Il notebook deve poter essere eseguito integralmente dall'inizio in ambiente pulito.

Il seed principale è

$$
12345.
$$

Non devono esistere celle che dipendono da variabili prodotte da esecuzioni precedenti ma non ricostruite nel notebook corrente.

---

## 13. Errori o ambiguità prevedibili

1. descrivere la dinamica di $S_t$ come GBM standard a drift costante;
2. omettere che le dinamiche sono assegnate sotto $\mathbb Q$;
3. confondere una replica Monte Carlo con uno scenario teorico;
4. utilizzare $s$ come indice delle repliche invece di $k$;
5. utilizzare $k$ contemporaneamente come indice temporale e indice di replica;
6. dimenticare il dividend yield $q$ nel drift;
7. usare un tasso comune alle repliche nel drift del sottostante;
8. confondere la correlazione degli shock con quella dei livelli simulati;
9. generare processi indipendenti nonostante $\rho\neq0$;
10. utilizzare lo stesso shock per entrambi i processi, imponendo correlazione perfetta;
11. azzerare sistematicamente i nuovi valori negativi del CIR;
12. interpretare valori CIR negativi da discretizzazione come proprietà economica del processo continuo;
13. utilizzare $S_T$ al posto di $A_T$;
14. includere $S_0$ nella media;
15. mediare tutti i punti della griglia anziché i soli dodici fixing;
16. confondere media aritmetica e geometrica;
17. calcolare il payoff sulla media tra repliche anziché replica per replica;
18. calcolare prima il payoff medio e poi applicare il massimo;
19. attualizzare mediante $r_T$;
20. utilizzare un tasso medio trasversale comune alle repliche;
21. combinare il payoff di una replica con il fattore di sconto di un'altra;
22. interpretare $\widehat{\mathbb Q}(A_T>K)$ come probabilità fisica di esercizio;
23. presentare la call asiatica come opzione quotata su Eurex;
24. presentare la simulazione come formula esatta di pricing;
25. utilizzare il Regime C come fase ordinaria e obbligatoria;
26. omettere Flusso logico-teorico e scomposizione in tappe passando direttamente dalla Scheda Caso al codice.

---

## 14. Ipotesi e limiti interpretativi

Ai fini del caso:

1. le dinamiche assegnate sono utilizzate direttamente sotto la misura risk-neutral $\mathbb Q$;
2. non viene richiesto di derivare il cambio di misura;
3. $S_0$ e $r_0$ sono ancorati alla data di riferimento indicata;
4. $q$ e $\sigma_S$ sono proxy di mercato arrotondate;
5. $\kappa_r$, $\theta_r$, $\sigma_r$ e $\rho$ sono parametri modellistici assegnati;
6. dividend yield, volatilità e correlazione sono costanti;
7. il tasso nominale è rappresentato da un unico fattore CIR;
8. indice e tasso sono simulati sulla medesima griglia;
9. l'integrale del tasso è approssimato mediante somma di Riemann sinistra;
10. i fixing sono mensili ed equidistanti;
11. non sono considerati rischio di credito, liquidità, costi di transazione o fiscalità;
12. non sono richieste formule chiuse di pricing né modelli alternativi;
13. la call asiatica è un contratto OTC stilizzato;
14. il risultato ottenuto è il valore prodotto dal modello assegnato e non una quotazione operativa di mercato.

L'interpretazione conclusiva deve distinguere:

$$
\text{valore prodotto dal modello sotto }\mathbb Q
$$

da

$$
\text{quotazione operativa osservabile sul mercato}.
$$

---

## 15. Uso dell'IA e tracciato

### 15.1 Uso documentato

L'uso documentato dell'IA è previsto.

Lo studente deve consegnare:

1. il notebook Jupyter finale;
2. il tracciato completo dell'interazione con l'IA, ordinariamente mediante stampa PDF della chat dedicata al caso.

I due documenti devono essere coerenti ma svolgono funzioni diverse:

- il notebook documenta il prodotto quantitativo validato;
- il tracciato documenta il processo metodologico con cui il prodotto è stato costruito, verificato e corretto.

### 15.2 Prompt obbligatori

La sequenza ordinaria comprende:

- Prompt zero;
- Prompt 1;
- Prompt 2;
- Prompt 3;
- i prompt di tappa necessari alle sei tappe validate.

Il numero complessivo dei prompt non è fissato a priori.

Possono aggiungersi Prompt C soltanto quando lo studente individua una criticità specifica da verificare.

### 15.3 Regimi

- **Regime A:** Prompt 2 e ogni eventuale ricognizione teorico-modellistica locale necessaria.
- **Regime B:** traduzione operativa delle tappe validate.
- **Regime C:** esclusivamente verifica di una criticità specifica individuata dallo studente.

Il Regime C non costituisce una tappa conclusiva obbligatoria.

### 15.4 Usi ammessi dell'IA

L'IA può essere utilizzata per:

- verificare e completare il Flusso logico-teorico proposto dallo studente;
- verificare la scomposizione operativa proposta dallo studente;
- tradurre in Python una singola tappa già validata;
- chiarire la distinzione tra $S_T$ e $A_T$;
- chiarire il ruolo del dividend yield;
- supportare la selezione tecnica dei fixing già specificati;
- implementare la costruzione degli shock correlati;
- implementare tabelle e grafici già definiti nella loro funzione informativa;
- spiegare localmente codice e output;
- implementare i controlli richiesti;
- verificare una criticità specifica;
- supportare la lettura di output già prodotti.

### 15.5 Usi non ammessi

L'IA non deve:

- sostituire la Scheda Caso;
- modificare modello, parametri, calendario, strike o payoff;
- produrre l'intero notebook in un'unica risposta;
- saltare il Flusso logico-teorico o la scomposizione in tappe;
- eliminare il dividend yield;
- trasformare l'opzione asiatica in una call europea;
- introdurre una diversa discretizzazione CIR;
- introdurre modelli o formule chiuse non previsti;
- eliminare controlli perché i risultati appaiono plausibili;
- aggiungere autonomamente output obbligatori o sensitivity analysis;
- produrre l'interpretazione finanziaria finale al posto dello studente.

### 15.6 Regime C

La sequenza prevista è:

$$
\text{criticità individuata dallo studente}
\rightarrow
\text{Prompt C mirato}
\rightarrow
\text{criticità respinta o accolta}
$$

$$
\rightarrow
\text{eventuale sostituzione delle celle interessate}.
$$

In assenza di una criticità specifica non deve essere generato artificialmente un Prompt C.

### 15.7 Sequenza osservabile nel tracciato

Nel tracciato devono risultare riconoscibili:

$$
\text{Prompt zero}
\rightarrow
\text{Prompt 1}
\rightarrow
\text{Prompt 2}
\rightarrow
\text{Prompt 3}
$$

$$
\rightarrow
\text{prompt di tappa}
\rightarrow
\text{eventuali Prompt C}.
$$

Devono inoltre essere osservabili:

- contributo iniziale dello studente al Prompt 2;
- contributo iniziale dello studente al Prompt 3;
- risposte IA effettivamente utilizzate;
- decisioni di accettazione, modifica, rifiuto o correzione;
- output prodotti;
- controlli svolti;
- eventuali criticità specifiche e relativo esito;
- interpretazione finale autonoma.

---

## 16. Valutazione e rubrica sintetica

La valutazione riguarda congiuntamente notebook e tracciato IA.

Un notebook quantitativamente corretto non è sufficiente se il tracciato mostra delega sostanziale del ragionamento. Simmetricamente, un uso metodologicamente corretto dell'IA non compensa errori teorici, computazionali o interpretativi.

La rubrica di riferimento è:

| Area | Peso | Criteri principali |
|---|---:|---|
| **Prompt 2 — Flusso logico-teorico risolutivo** | 30 | contributo iniziale dello studente, ordine logico, collegamento tra teoria, output e controlli |
| **Prompt 3 — Scomposizione input-output** | 15 | proposta operativa iniziale dello studente, coerenza delle tappe, collegamento input-output |
| **Notebook Jupyter e output computazionali** | 20 | correttezza del codice, tabelle, grafici, riproducibilità, coerenza degli output richiesti |
| **Prompt di tappa e uso dei Regimi A/B; eventuale Regime C** | 15 | qualità dei prompt, rispetto dei vincoli, contributo dello studente, uso appropriato dell'IA e, quando presente, qualità dell'attivazione del Regime C |
| **Verifiche logiche e controlli numerici** | 15 | controlli su formule, simulazioni, vincoli, quantità teoriche e proprietà del modello |
| **Interpretazione finanziaria finale** | 5 | autonomia, coerenza con gli output, interpretazione finanziaria e consapevolezza dei limiti |

**Totale: 100 punti.**

### Criteri specifici del notebook

La valutazione deve considerare in particolare:

- correttezza della simulazione congiunta;
- corretta inclusione del dividend yield;
- rispetto della misura $\mathbb Q$;
- corretta convenzione CIR;
- corretta selezione dei fixing;
- corretta costruzione di $A_T$;
- corretta costruzione del payoff;
- corretta attualizzazione replica per replica;
- pricing Monte Carlo;
- misurazione dell'errore Monte Carlo;
- controllo della discretizzazione;
- riproducibilità;
- qualità di tabelle e grafici;
- corretta distinzione tra dati osservati, proxy e parametri didattici.

### Criteri specifici del tracciato IA

Devono essere valutati:

- qualità del contributo teorico iniziale dello studente;
- corretta identificazione della path-dependence;
- capacità di scomporre il problema;
- uso appropriato dei Regimi A e B;
- eventuale uso del Regime C soltanto a fronte di criticità specifiche;
- capacità di verificare il codice suggerito;
- decisioni autonome sulle risposte IA;
- coerenza tra tracciato e notebook finale.

---

## 17. Relazione con il Caso Aula

Caso Aula e Caso TakeHome condividono la stessa architettura metodologica:

$$
\text{fattori stocastici}
\rightarrow
\text{shock correlati}
\rightarrow
\text{traiettorie}
\rightarrow
\text{quantità path-dependent}
$$

$$
\rightarrow
\text{flussi/payoff}
\rightarrow
\text{attualizzazione per replica}
\rightarrow
\text{stima Monte Carlo}
\rightarrow
\text{diagnostica}
\rightarrow
\text{interpretazione}.
$$

Condividono inoltre:

- $M$ come numero di repliche Monte Carlo;
- $k$ come indice di replica;
- organizzazione matriciale repliche $\times$ tempo;
- costruzione di shock correlati;
- processo CIR con la medesima convenzione numerica;
- fattore di sconto costruito dalla traiettoria del tasso;
- valore finanziario costruito replica per replica;
- errore standard Monte Carlo;
- controllo della convergenza rispetto a $M$;
- controllo della discretizzazione;
- seed per la riproducibilità;
- sequenza Prompt zero → Prompt 1 → Prompt 2 → Prompt 3 → prompt di tappa;
- Regime C soltanto in presenza di una criticità specifica.

### Caso Aula

- primo fattore: inflazione OU;
- quantità path-dependent: $J_t$;
- prodotto: inflation-linked bond;
- flussi: cedole indicizzate e rimborso protetto;
- dinamiche assegnate utilizzate direttamente ai fini della valutazione.

### Caso TakeHome

- primo fattore: EURO STOXX 50 con diffusione geometrica e drift stocastico;
- quantità path-dependent: media aritmetica $A_T$;
- prodotto: call asiatica OTC;
- payoff: $(A_T-K)^+$;
- dinamiche assegnate esplicitamente sotto la misura risk-neutral $\mathbb Q$.

Il Caso TakeHome trasferisce quindi il **metodo**, non il codice né la soluzione del Caso Aula.

La responsabilità è inoltre diversa:

- nel Caso Aula il docente guida lo sviluppo;
- nel Caso TakeHome lo studente propone Flusso e tappe, governa l'interazione con l'IA, verifica gli output e formula autonomamente l'interpretazione finale.

---

## 18. Esito atteso e calibrazione qualitativa

Prima dell'assegnazione agli studenti il notebook docente di riferimento deve essere rieseguito integralmente e validato.

Non deve essere imposto ex ante un prezzo-obiettivo.

La calibrazione qualitativa deve verificare che:

- il contratto risulti prossimo all'at-the-money all'origine;
- la distribuzione di $A_T$ presenti massa rilevante su entrambi i lati dello strike;
- la probabilità simulata di esercizio non sia estrema;
- il payoff medio sia positivo ma non dominato da un numero trascurabile di repliche;
- i tassi simulati rimangano concentrati su valori economicamente compatibili con i parametri assegnati;
- gli shock presentino correlazione empirica compatibile con $\rho=-0.25$;
- eventuali valori CIR negativi siano diagnosticati senza alterare silenziosamente le traiettorie;
- il prezzo mostri stabilità Monte Carlo al crescere di $M$;
- il raffinamento della griglia non produca variazioni economicamente rilevanti rispetto alla scala del problema;
- tabelle, grafici e interpretazione forniscano una lettura reciprocamente coerente.

Possibili segnali di cattiva calibrazione sono:

1. probabilità di esercizio praticamente nulla o prossima a uno;
2. distribuzione di $A_T$ quasi interamente lontana dallo strike;
3. forte instabilità del prezzo rispetto alla griglia;
4. valori CIR negativi numericamente frequenti;
5. output dominati da poche repliche estreme;
6. errore Monte Carlo non compatibile con la numerosità utilizzata.

Il notebook costituisce una soluzione quantitativa completa solo se resta ricostruibile la sequenza

$$
\text{ipotesi}
\rightarrow
\text{simulazione}
\rightarrow
\text{fixing e media asiatica}
\rightarrow
\text{payoff}
$$

$$
\rightarrow
\text{attualizzazione}
\rightarrow
\text{prezzo}
\rightarrow
\text{controlli}
\rightarrow
\text{interpretazione}.
$$

---

## 19. Fonti di calibrazione e contesto per il docente

Le fonti richiamate nella progettazione corrente del caso sono:

- Eurex, specifiche delle EURO STOXX 50 Index Options (OESX), per sottostante, mercato delle opzioni vanilla e struttura degli strike;
- BCE, €STR con data di riferimento 27 luglio 2026 e contesto di politica monetaria;
- iShares / BlackRock, ETF EURO STOXX 50, come riferimento per l'ordine di grandezza del dividend yield;
- Eurex, VSTOXX futures, come riferimento per l'ordine di grandezza della volatilità;
- CME Group, materiale sulle Average Price Options, per il ruolo economico delle opzioni basate su prezzi medi;
- letteratura su equity-linked securities e Asian-style options, per l'impiego dell'averaging in prodotti strutturati e assicurativi.

Le fonti hanno funzione di contestualizzazione e calibrazione docente. I parametri assegnati nel caso restano quelli definiti nella Scheda Caso e non devono essere modificati autonomamente dallo studente.