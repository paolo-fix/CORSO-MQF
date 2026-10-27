# Lezione 07 — Scheda Caso TakeHome

## 1. Identificazione del caso

- **Lezione:** Lezione 07 — Applicazione in Python: simulazione di traiettorie e pricing
- **Tipo di caso:** TakeHome
- **Titolo:** *Pricing Monte Carlo di una call asiatica sull'EURO STOXX 50 con tasso di interesse stocastico*
- **Contesto:** valutazione di una call asiatica OTC a media aritmetica su indice azionario, con tasso nominale stocastico
- **Data di riferimento:** 27 luglio 2026
- **Uso previsto:** lavoro autonomo mediante notebook Jupyter, successivo al Caso Aula

Questa Scheda Caso costituisce la **specifica vincolante del lavoro**. Variabili, formule, parametri, output, controlli e ipotesi non devono essere modificati durante lo svolgimento.

La Scheda Caso non contiene la soluzione del problema. Il Flusso logico-teorico risolutivo, la scomposizione in tappe, il codice e l'interpretazione finale devono essere costruiti successivamente.

---

## 2. Contesto e domanda quantitativa

Il sottostante è l'**EURO STOXX 50**, uno dei principali benchmark azionari dell'area euro e sottostante di un mercato liquido di futures e opzioni vanilla.

Il caso è collocato al **27 luglio 2026**. Il valore iniziale dell'indice utilizzato è

$
S_0=6\,286.35.
$

Lo strike è fissato a

$
K=6\,300
$,

così da considerare un contratto sostanzialmente at-the-money all'origine.

Il livello iniziale dello short rate è

$
r_0=0.02185
$,

ancorato all'€STR (Euro Short-Term Rate) della data di riferimento.

Per il dividend yield continuo, si utilizza

$
q=0.025
$,

mentre per la volatilità dell'indice si assume

$
\sigma_S=0.18
$.

Questi due valori sono proxy di mercato arrotondate e non costituiscono una calibrazione esatta.

Il prodotto considerato è una **call asiatica OTC a media aritmetica**. Il payoff non dipende soltanto dal livello terminale dell'indice, ma dalla media dei livelli osservati a dodici date di fixing mensili.

Il contratto è quindi path-dependent: la conoscenza del solo $S_T$ non è sufficiente per determinare il payoff.

La domanda quantitativa è:

> **Qual è il valore corrente della call asiatica sull'EURO STOXX 50, stimato mediante simulazione Monte Carlo, quando il livello dell'indice e il tasso nominale evolvono congiuntamente in modo stocastico sotto la misura risk-neutral $\mathbb Q$?**

Il prezzo deve essere costruito a partire dai payoff attualizzati ottenuti nelle singole repliche Monte Carlo.

---

## 3. Modello e struttura del problema

### Misura di pricing

Le dinamiche dei fattori sono assegnate direttamente sotto la misura risk-neutral $
\mathbb Q$.


Non è richiesto derivare il cambio di misura.

### Dinamica del sottostante

Il livello dell'EURO STOXX 50 segue la diffusione geometrica

$
dS_t =
(r_t-q)S_t\,dt
+
\sigma_S S_t\,dW_t^{(S)}$.


Il drift è stocastico perché dipende dal tasso istantaneo $r_t$.

### Dinamica del tasso nominale

Il tasso nominale istantaneo segue un processo CIR:

$
dr_t =
\kappa_r(\theta_r-r_t)\,dt
+
\sigma_r\sqrt{r_t}\,dW_t^{(r)}$.


I parametri assegnati soddisfano la condizione di Feller:

$
2\kappa_r\theta_r
\geq
\sigma_r^2$.


### Convenzione numerica per il CIR

Sulla griglia temporale deve essere utilizzata la convenzione

$
r_{t_{j+1}}^{(k)} =
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
Z_{r,j+1}^{(k)}$.


L'operatore
$
\max(r_{t_j}^{(k)},0)
$
agisce soltanto all'interno della radice quadrata.

Il nuovo valore $r_{t_{j+1}}^{(k)}$ non deve essere automaticamente sostituito con zero quando risulta negativo. Eventuali valori negativi prodotti dalla discretizzazione devono essere rilevati e documentati.

### Dipendenza tra i fattori

Gli shock browniani soddisfano

$
dW_t^{(S)}\,dW_t^{(r)} =
\rho\,dt$.


Per ogni replica $k$ e intervallo temporale $j$, a partire da due normali standard indipendenti,

$
Z_{1,j}^{(k)}$ e
$Z_{2,j}^{(k)}$,


si costruiscono

$
Z_{S,j}^{(k)}=
Z_{1,j}^{(k)}$,

$
Z_{r,j}^{(k)}=
\rho Z_{1,j}^{(k)}
+
\sqrt{1-\rho^2}\,
Z_{2,j}^{(k)}$.

La correlazione assegnata riguarda gli shock dei due fattori.

### Discretizzazione del sottostante

Per il sottostante si utilizza una discretizzazione logaritmica:

$S_{t_{j+1}}^{(k)}=
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
\right]$.

La costruzione implica

$
S_{t_j}^{(k)}>0$.


### Date di fixing e media asiatica

La scadenza è $T=1$ anno.

La simulazione utilizza $
N=252$ e $\Delta t=\frac1{252}$.

Sono previsti dodici fixing mensili:

$
\tau_h=\frac{h}{12}$ con
$h=1,\ldots,12$.


Poiché
$
\frac{252}{12}=21$, 
i fixing corrispondono ai passi
$
21,42,\ldots,252$.


Per ogni replica $k$, la media asiatica è

$
A_T^{(k)}=
\frac1{12}
\sum_{h=1}^{12}
S_{\tau_h}^{(k)}$.


Il valore iniziale $S_0$ **non** entra nella media.

### Payoff

Il payoff della replica $k$ è

$
H_T^{(k)}=
\max
\left(
A_T^{(k)}-K,0
\right)$.


### Fattore di sconto

Il fattore di sconto è definito da

$
D(0,T)=
\exp
\left(
-\int_0^T r_u\,du
\right)$.

Per la replica $k$, l'integrale viene approssimato mediante somma di Riemann sinistra:

$
\int_0^T r_u^{(k)}\,du
\approx
\sum_{j=0}^{N-1}
r_{t_j}^{(k)}\Delta t$.


Il fattore di sconto utilizzato nel pricing è quindi

$
\widehat D^{(k)}(0,T)=
\exp
\left(
-\sum_{j=0}^{N-1}
r_{t_j}^{(k)}\Delta t
\right)$.


Non deve essere utilizzato il solo valore terminale $r_T$, né un tasso medio calcolato trasversalmente tra repliche.

### Valore attualizzato e prezzo Monte Carlo

Il valore attualizzato nella replica $k$ è

$
V^{(k)}=
\widehat D^{(k)}(0,T)
H_T^{(k)}$.


Con $
k=1,\ldots,M$, il prezzo Monte Carlo è

$
\widehat V_M=
\frac1M
\sum_{k=1}^{M}
V^{(k)}$.


Indicando con $s_V$ la deviazione standard campionaria dei valori $V^{(k)}$,

$
SE(\widehat V_M) =
\frac{s_V}{\sqrt M}$.


Un intervallo di confidenza Monte Carlo approssimato al $95\%$ è

$
\widehat V_M
\pm
1.96\,SE(\widehat V_M)$.


### Probabilità simulata di esercizio

Poiché le traiettorie sono generate sotto la misura $\mathbb Q$, la frequenza simulata di esercizio stima

$
\widehat{\mathbb Q}(A_T>K)=
\frac1M
\sum_{k=1}^{M}
\mathbf 1_{\{A_T^{(k)}>K\}}$.


Essa deve essere interpretata come probabilità sotto la misura di pricing del modello assegnato, non come probabilità fisica di mercato.

---

## 4. Parametri assegnati

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
| Simulazione | $\Delta t$ | 1/252 | griglia principale |
| Simulazione | $M$ | 50.000 | repliche Monte Carlo |
| Simulazione | seed | 12345 | seme pseudo-casuale |

La condizione di Feller è soddisfatta:

$
2(1.25)(0.0220)=
0.055 >
0.0016 =
(0.040)^2$.


La griglia principale contiene $252$ intervalli e $253$ nodi, compresa la data iniziale.

---

## 5. Quantità da stimare o calcolare

Devono essere determinate:

1. media e deviazione standard simulate di $S_T$ e $r_T$;
2. media e deviazione standard simulate di $A_T$;
3. probabilità simulata di esercizio sotto $\mathbb Q$, $\widehat{\mathbb Q}(A_T>K)$;
4. valore medio del payoff non attualizzato $H_T$;
5. prezzo Monte Carlo della call asiatica $\widehat V_M$;
6. errore standard Monte Carlo e intervallo di confidenza al $95\%$.

Le quantità path-dependent e finanziarie devono essere costruite replica per replica prima dell'aggregazione Monte Carlo.

---

## 6. Output richiesti

### Tabelle

Produrre:

1. **tabella dei parametri del caso**, distinguendo dati osservati, proxy di mercato, specifiche contrattuali e parametri didattici;
2. **tabella delle statistiche dei fattori e della media asiatica**, contenente media e deviazione standard di $S_T$, $r_T$, $A_T$;
3. **tabella di sintesi del payoff e del pricing**, contenente almeno:
   - probabilità simulata di esercizio;
   - payoff medio;
   - prezzo Monte Carlo;
   - errore standard;
   - intervallo di confidenza al $95\%$;
4. **tabella di diagnostica Monte Carlo** per $
   M=
   1\,000,\;
   5\,000,\;
   10\,000,\;
   50\,000
   $,
   riportando almeno prezzo stimato ed errore standard.

### Grafici

Produrre almeno:

1. alcune traiettorie simulate dell'EURO STOXX 50, $S_t$;
2. alcune traiettorie simulate del tasso nominale $r_t$;
3. distribuzione simulata di $A_T$, con evidenza dello strike $K$;
4. distribuzione dei valori attualizzati $V^{(k)}$;
5. grafico di convergenza della stima Monte Carlo al crescere di $M$.

I grafici devono riportare titoli, assi e unità coerenti e devono avere una funzione interpretativa.

---

## 7. Controlli richiesti

Il notebook deve verificare esplicitamente che:

1. la correlazione empirica degli shock simulati sia coerente con $\rho=-0.25$;

2. il sottostante soddisfi $S_{t_j}^{(k)}>0$ per ogni replica e data;

3. eventuali valori negativi di $r_t$ prodotti dalla discretizzazione siano rilevati e documentati senza azzerare sistematicamente il valore aggiornato;

4. per ogni replica valga $\min_h S_{\tau_h}^{(k)}\leq A_T^{(k)}
\leq\max_h S_{\tau_h}^{(k)}$;

5. il payoff soddisfi $H_T^{(k)}\geq0$ e sia nullo quando $A_T^{(k)}\leq K$;

6. l'integrale del tasso sia costruito utilizzando $r_{t_0}^{(k)},\ldots,r_{t_{N-1}}^{(k)}$ appartenenti alla stessa replica e il fattore di sconto soddisfi $\widehat D^{(k)}(0,T)>0$;

7. il valore attualizzato soddisfi $
   V^{(k)}=
   \widehat D^{(k)}(0,T)H_T^{(k)}$;

8. l'errore standard Monte Carlo diminuisca al crescere di $M$ in modo compatibile con $O(M^{-1/2})$;

9. il prezzo sia sufficientemente stabile rispetto a una griglia temporale più fine;

10. i risultati principali siano riproducibili mediante il seed assegnato.

Il controllo rispetto a $M$ e quello rispetto alla griglia temporale riguardano problemi diversi:

$
M
\longrightarrow
\text{precisione Monte Carlo},
$

$
\Delta t
\longrightarrow
\text{approssimazione temporale}$.

---

## 8. Ipotesi e limiti del caso

Ai fini di questa applicazione:

1. le dinamiche assegnate sono utilizzate direttamente sotto la misura risk-neutral \(\mathbb Q\);
2. non è richiesta la derivazione del cambio di misura;
3. $S_0$ e $r_0$ sono ancorati alla data di riferimento;
4. $q$ e $\sigma_S$ sono proxy di mercato arrotondate e non calibrazioni esatte;
5. $\kappa_r$, $\theta_r$, $\sigma_r$ e $\rho$ sono parametri modellistici assegnati;
6. dividend yield, volatilità e correlazione sono costanti;
7. il tasso nominale è rappresentato mediante un unico fattore CIR;
8. indice e tasso sono simulati sulla stessa griglia temporale;
9. l'integrale del tasso è approssimato mediante somma di Riemann sinistra;
10. i fixing sono mensili ed equidistanti;
11. $S_0$ non appartiene alle date di fixing;
12. non sono considerati rischio di credito, rischio di liquidità, costi di transazione o fiscalità;
13. non sono richieste formule chiuse di pricing né modelli alternativi;
14. la call asiatica è un contratto OTC stilizzato e non deve essere confusa con le opzioni vanilla EURO STOXX 50 quotate su Eurex;
15. il prezzo ottenuto è il risultato del modello assegnato e non una quotazione operativa di mercato.