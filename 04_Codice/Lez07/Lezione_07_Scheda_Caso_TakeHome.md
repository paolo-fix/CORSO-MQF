# Lezione 07 — Scheda Caso Take-Home

## 1. Identificazione del caso

- **Lezione:** Lezione 07 — Applicazione in Python: traiettorie, simulazione e pricing Monte Carlo
- **Tipo di caso:** take-home
- **Titolo:** *Path-dependence e tassi stocastici: pricing Monte Carlo di un'opzione asiatica*
- **Contesto:** valutazione di una call asiatica a media aritmetica in presenza di sottostante azionario e tasso nominale stocastici
- **Uso previsto:** lavoro autonomo mediante notebook Jupyter, successivo al caso sviluppato in aula

Questa Scheda Caso costituisce la **specifica vincolante del lavoro**. Variabili, formule, parametri, output, controlli e ipotesi non devono essere modificati durante lo svolgimento.

La Scheda Caso non contiene la soluzione del problema: il Flusso logico-teorico risolutivo, la scomposizione in tappe, il codice e l'interpretazione finale devono essere costruiti successivamente.

---

## 2. Contesto e domanda quantitativa

Un intermediario finanziario deve valutare una **call asiatica a media aritmetica** scritta su un titolo azionario. A differenza di una call europea ordinaria, il payoff non dipende soltanto dal prezzo terminale del sottostante, ma dalla media dei prezzi osservati in un insieme prefissato di date di fixing.

Il valore del contratto dipende quindi dalla traiettoria del prezzo azionario. Si assume inoltre che il tasso nominale privo di rischio sia stocastico: il fattore utilizzato per attualizzare il payoff deve essere costruito a partire dalla traiettoria simulata del tasso.

Le due fonti di rischio sono pertanto:

1. il **prezzo del sottostante** $S_t$, che determina la media asiatica e quindi il payoff;
2. il **tasso nominale istantaneo** $r_t$, che determina l'attualizzazione.

Gli shock che guidano i due processi sono correlati.

La domanda quantitativa è:

> **Qual è il valore corrente della call asiatica, stimato mediante simulazione Monte Carlo, quando il sottostante azionario e il tasso nominale evolvono congiuntamente in modo stocastico?**

L'oggetto finale della simulazione è il valore attualizzato del payoff ottenuto in ciascuno scenario. Il prezzo dell'opzione è stimato come media Monte Carlo di tali valori.

---

## 3. Modello e struttura del problema

### Dinamica del sottostante

Il prezzo azionario segue una dinamica moltiplicativa di tipo GBM, con tasso privo di rischio stocastico:

$$dS_t=r_tS_t\,dt+\sigma_S S_t\,dW_t^{(S)}.$$

Non sono previsti dividendi.

### Dinamica del tasso nominale

Il tasso nominale segue un processo CIR:

$$dr_t=\kappa_r(\theta_r-r_t)\,dt+\sigma_r\sqrt{r_t}\,dW_t^{(r)}.$$

I parametri assegnati soddisfano la condizione di Feller:

$$2\kappa_r\theta_r\geq\sigma_r^2.$$

Per la simulazione del CIR deve essere utilizzata la **stessa convenzione numerica adottata nel caso aula**. Non deve essere introdotta autonomamente una tecnica di simulazione differente.

### Dipendenza tra i fattori

Gli shock browniani soddisfano:

$$dW_t^{(S)}\,dW_t^{(r)}=\rho\,dt.$$

A ogni passo temporale la dipendenza deve essere costruita a partire da due normali standard indipendenti $Z_{1,k}$ e $Z_{2,k}$:

$$Z_{S,k}=Z_{1,k},\qquad Z_{r,k}=\rho Z_{1,k}+\sqrt{1-\rho^2}\,Z_{2,k}.$$

### Date di fixing e media asiatica

La scadenza è $T=1$ anno. Sono previsti $m=12$ fixing mensili alle date

$$t_j=\frac{j}{12},\qquad j=1,\ldots,12.$$

La media aritmetica utilizzata dal contratto è:

$$A_T=\frac{1}{m}\sum_{j=1}^{m}S_{t_j}.$$

Il valore iniziale $S_0$ **non** entra nella media.

### Payoff e attualizzazione

Il payoff della call asiatica a scadenza è:

$$H_T=\max(A_T-K,0).$$

Il fattore di sconto associato a una traiettoria del tasso è:

$$D(0,T)=\exp\left(-\int_0^T r_u\,du\right).$$

Per lo scenario simulato $s$, il valore attualizzato è:

$$V^{(s)}=D^{(s)}(0,T)H_T^{(s)}.$$

Con $M$ traiettorie, il prezzo Monte Carlo è:

$$\widehat V_M=\frac{1}{M}\sum_{s=1}^{M}V^{(s)},$$

e il relativo errore standard è:

$$SE(\widehat V_M)=\frac{s_V}{\sqrt{M}},$$

dove $s_V$ è la deviazione standard campionaria dei valori attualizzati $V^{(s)}$.

---

## 4. Parametri assegnati

I parametri sono assegnati a fini didattici e **non costituiscono una calibrazione a dati di mercato**.

| Componente | Parametro | Valore |
|---|---|---:|
| Contratto | $S_0$ | 100 |
| Contratto | $K$ | 100 |
| Contratto | $T$ | 1 anno |
| Contratto | fixing | 12 mensili |
| Sottostante | $\sigma_S$ | 0,20 |
| Tasso CIR | $r_0$ | 0,030 |
| Tasso CIR | $\kappa_r$ | 1,50 |
| Tasso CIR | $\theta_r$ | 0,030 |
| Tasso CIR | $\sigma_r$ | 0,10 |
| Dipendenza | $\rho$ | -0,30 |
| Simulazione | $\Delta t$ | $1/252$ |
| Simulazione | $M$ | 50.000 |
| Simulazione | seed | 12345 |

La griglia principale è giornaliera, con 252 passi annui. Poiché $252/12=21$, i fixing mensili corrispondono ai passi $21,42,\ldots,252$.

---

## 5. Quantità da stimare o calcolare

Devono essere determinate almeno le seguenti quantità:

1. media e deviazione standard simulate di $S_T$ e $r_T$.
2. media e deviazione standard simulate del prezzo medio $A_T$;
3. **probabilità simulata di esercizio**, $\widehat{\mathbb P}(A_T>K)$;
4. valore medio del payoff non attualizzato $H_T$;

5. **prezzo Monte Carlo della call asiatica** $\widehat V_M$;
6. **errore standard Monte Carlo** e intervallo di confidenza al 95% del prezzo;

Le quantità devono essere ottenute a partire dai singoli scenari simulati: il payoff deve essere determinato scenario per scenario prima dell'aggregazione Monte Carlo.

---

## 6. Output richiesti

### Tabelle

Produrre:

1. **tabella dei parametri del caso**;
2. **tabella delle statistiche terminali**, contenente media e deviazione standard di $S_T$, $r_T$ e $A_T$;
3. **tabella di sintesi del pricing**, contenente almeno prezzo Monte Carlo, errore standard, intervallo di confidenza al 95%, probabilità di esercizio e payoff medio;
4. **tabella di diagnostica Monte Carlo** per $M=1\,000,\ 5\,000,\ 10\,000,\ 50\,000$, riportando almeno prezzo stimato ed errore standard.


### Grafici

Produrre almeno:

1. alcune traiettorie simulate del sottostante $S_t$;
2. alcune traiettorie simulate del tasso nominale $r_t$;
3. distribuzione simulata di $A_T$, con evidenza dello strike $K$;
4. distribuzione dei valori attualizzati $V^{(s)}$;
5. grafico di convergenza della stima Monte Carlo al crescere di $M$.

I grafici devono avere funzione interpretativa e riportare titoli, assi e unità coerenti.

---

## 7. Controlli richiesti

Il notebook deve verificare esplicitamente che:

1. la correlazione empirica degli shock simulati sia coerente con il valore assegnato $\rho=-0,30$;
2. il processo simulato del sottostante soddisfi $S_t>0$;
3. eventuali valori negativi di $r_t$ prodotti dalla discretizzazione siano rilevati e documentati secondo la convenzione numerica adottata nel caso aula;
4. per ogni scenario valga $\min_j S_{t_j}\leq A_T\leq\max_j S_{t_j}$;
5. il payoff soddisfi sempre $H_T\geq0$ e sia nullo quando $A_T\leq K$;
6. il fattore di sconto soddisfi $D(0,T)>0$;
7. l'errore standard Monte Carlo diminuisca al crescere di $M$, in modo compatibile con l'ordine $1/\sqrt{M}$;
8. il prezzo sia sufficientemente stabile rispetto a una griglia temporale più fine;
9. i risultati siano replicabili utilizzando il seed assegnato.

---

## 8. Ipotesi e limiti del caso

Ai fini di questa applicazione:

1. le dinamiche assegnate sono utilizzate direttamente ai fini del pricing;
2. i parametri sono costanti e non devono essere stimati o calibrati;
3. il sottostante non distribuisce dividendi;
4. volatilità azionaria e correlazione sono costanti;
5. il tasso nominale è rappresentato da un unico fattore CIR;
6. i fixing sono mensili ed equidistanti;
7. non sono considerati rischio di credito, rischio di liquidità, costi di transazione o fiscalità;
8. non sono richieste formule chiuse di pricing né modelli alternativi;
9. la convenzione numerica adottata per il CIR è quella già utilizzata nel caso aula e costituisce parte della specifica del lavoro;
10. il modello ha finalità didattica: il prezzo ottenuto non deve essere interpretato come quotazione operativa di uno specifico contratto di mercato.
