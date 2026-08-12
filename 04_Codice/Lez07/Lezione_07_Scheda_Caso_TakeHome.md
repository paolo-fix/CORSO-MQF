# Lezione 07 — Scheda Caso Take-Home

## 1. Identificazione del caso

- **Lezione:** Lezione 07 — Applicazione in Python: traiettorie, simulazione e pricing Monte Carlo
- **Tipo di caso:** take-home
- **Titolo:** *Pricing Monte Carlo di una call asiatica sull'EURO STOXX 50 con tasso di interesse stocastico*
- **Contesto:** valutazione di una call asiatica OTC a media aritmetica su indice azionario, con tasso nominale stocastico
- **Data di riferimento:** 27 luglio 2026
- **Uso previsto:** lavoro autonomo mediante notebook Jupyter, successivo al caso sviluppato in aula

Questa Scheda Caso costituisce la **specifica vincolante del lavoro**. Variabili, formule, parametri, output, controlli e ipotesi non devono essere modificati durante lo svolgimento.

La Scheda Caso non contiene la soluzione del problema: il Flusso logico-teorico risolutivo, la scomposizione in tappe, il codice e l'interpretazione finale devono essere costruiti successivamente.

---

## 2. Contesto e domanda quantitativa

Il sottostante è l'**EURO STOXX 50**, uno dei principali benchmark azionari dell'area euro e sottostante di un mercato molto liquido di futures e opzioni vanilla presso Eurex.

Il caso è collocato al **27 luglio 2026**. In quella seduta l'indice chiude a circa 6.286 punti, in prossimità della parte alta del range osservato nei dodici mesi precedenti. Lo strike viene fissato a 6.300 punti, quindi in posizione sostanzialmente at-the-money e coerente con la griglia di strike utilizzata per le opzioni EURO STOXX 50 con scadenza 6--12 mesi.

Il contesto dei tassi riflette l'estate 2026. A giugno la BCE ha aumentato di 25 punti base i tassi ufficiali in risposta alle nuove pressioni inflazionistiche legate allo shock energetico; il 23 luglio ha poi lasciato invariato al 2,25% il tasso sui depositi. Il valore iniziale dello short rate viene ancorato all'€STR del 27 luglio 2026.

Una **call asiatica a media aritmetica** non dipende soltanto dal livello terminale dell'indice, ma dalla media dei livelli osservati a date prefissate. L'averaging riduce la dipendenza da un singolo fixing e rende il contratto adatto a esposizioni o prodotti il cui riferimento economico è una performance media.

Le opzioni asiatiche sono molto diffuse come average-price options nei mercati delle commodity, dove vengono utilizzate per coprire esposizioni distribuite nel tempo. In ambito azionario strutture Asian-style compaiono soprattutto nel mercato OTC, nei prodotti strutturati e in alcuni contratti equity-linked di investitori istituzionali e compagnie di assicurazione. Nel presente caso si considera un contratto **OTC**: non si assume che la call asiatica sia quotata su Eurex.

La domanda quantitativa è:

> **Qual è il valore corrente della call asiatica sull'EURO STOXX 50, stimato mediante simulazione Monte Carlo, quando il livello dell'indice e il tasso nominale evolvono congiuntamente in modo stocastico?**

L'oggetto finale della simulazione è il valore attualizzato del payoff ottenuto in ciascuno scenario.

---

## 3. Modello e struttura del problema

### Dinamica del sottostante

Il livello dell'EURO STOXX 50 segue una dinamica moltiplicativa di tipo GBM con short rate stocastico e dividend yield continuo:

$$dS_t=(r_t-q)S_t\,dt+\sigma_S S_t\,dW_t^{(S)}.$$

Il parametro $q$ rappresenta il dividend yield continuo dell'indice.

### Dinamica del tasso nominale

Il tasso nominale segue un processo CIR:

$$dr_t=\kappa_r(\theta_r-r_t)\,dt+\sigma_r\sqrt{r_t}\,dW_t^{(r)}.$$

I parametri assegnati soddisfano la condizione di Feller:

$$2\kappa_r\theta_r\geq\sigma_r^2.$$

Per la simulazione del CIR deve essere utilizzata la **stessa convenzione numerica adottata nel caso aula**.

### Dipendenza tra i fattori

Gli shock browniani soddisfano:

$$dW_t^{(S)}\,dW_t^{(r)}=\rho\,dt.$$

A ogni passo temporale la dipendenza deve essere costruita a partire da due normali standard indipendenti $Z_{1,k}$ e $Z_{2,k}$:

$$Z_{S,k}=Z_{1,k},\qquad Z_{r,k}=\rho Z_{1,k}+\sqrt{1-\rho^2}\,Z_{2,k}.$$

### Date di fixing e media asiatica

La scadenza è $T=1$ anno. Sono previsti $m=12$ fixing mensili:

$$t_j=\frac{j}{12},\qquad j=1,\ldots,12.$$

La media aritmetica utilizzata dal contratto è:

$$A_T=\frac{1}{m}\sum_{j=1}^{m}S_{t_j}.$$

Il valore iniziale $S_0$ **non** entra nella media.

### Payoff e attualizzazione

Il payoff a scadenza è:

$$H_T=\max(A_T-K,0).$$

Il fattore di sconto associato a una traiettoria del tasso è definito in tempo continuo da:

$$D(0,T)=\exp\left(-\int_0^T r_u\,du\right).$$

Nel caso computazionale il tasso è osservato sulla griglia giornaliera

$$0=t_0<t_1<\cdots<t_N=T,\qquad N=252,\qquad \Delta t=\frac{1}{252}.$$

Per ciascuno scenario $s$, l'integrale del tasso viene approssimato mediante somma di Riemann sinistra:

$$\int_0^T r_u^{(s)}\,du\approx\sum_{k=0}^{N-1}r_{t_k}^{(s)}\Delta t.$$

Il fattore di sconto utilizzato nel pricing è quindi stimato scenario per scenario come:

$$\widehat D^{(s)}(0,T)=\exp\left(-\sum_{k=0}^{N-1}r_{t_k}^{(s)}\Delta t\right).$$

Non deve essere utilizzato il solo valore terminale $r_T$, né un tasso medio calcolato trasversalmente sulle diverse simulazioni.

Per lo scenario simulato $s$:

$$V^{(s)}=\widehat D^{(s)}(0,T)H_T^{(s)}.$$

Con $M$ traiettorie:

$$\widehat V_M=\frac{1}{M}\sum_{s=1}^{M}V^{(s)},$$

e:

$$SE(\widehat V_M)=\frac{s_V}{\sqrt{M}},$$

dove $s_V$ è la deviazione standard campionaria dei valori attualizzati.

---

## 4. Parametri assegnati

I parametri combinano dati osservati, proxy di mercato e scelte modellistiche didattiche. Non costituiscono una calibrazione completa del modello.

| Componente | Parametro | Valore | Natura |
|---|---|---:|---|
| Data | $t_0$ | 27/07/2026 | data di riferimento |
| Sottostante | indice | EURO STOXX 50 | dato di mercato |
| Contratto | $S_0$ | 6.286,35 | chiusura di mercato |
| Contratto | $K$ | 6.300 | strike quasi ATM |
| Contratto | $T$ | 1 anno | specifica contrattuale |
| Contratto | fixing | 12 mensili | specifica contrattuale |
| Dividendi | $q$ | 0,025 | proxy di mercato arrotondata |
| Sottostante | $\sigma_S$ | 0,18 | proxy market-consistent |
| Tasso CIR | $r_0$ | 0,02185 | €STR, 27/07/2026 |
| Tasso CIR | $\kappa_r$ | 1,25 | parametro didattico |
| Tasso CIR | $\theta_r$ | 0,0220 | parametro didattico |
| Tasso CIR | $\sigma_r$ | 0,040 | parametro didattico |
| Dipendenza | $\rho$ | -0,25 | ipotesi modellistica |
| Simulazione | $N$ | 252 | intervalli temporali |
| Simulazione | $\Delta t$ | $1/252$ | griglia giornaliera |
| Simulazione | $M$ | 50.000 | numero di traiettorie |
| Simulazione | seed | 12345 | seme casuale |

La condizione di Feller è soddisfatta:

$$2(1.25)(0.0220)=0.055>0.0016=(0.040)^2.$$

Il dividend yield del 2,5% è una proxy arrotondata coerente con il trailing dividend distribution yield di ETF che replicano l'EURO STOXX 50 a fine luglio 2026. La volatilità del 18% è una proxy coerente con l'ordine di grandezza dei VSTOXX futures osservabili nello stesso periodo. I parametri CIR diversi da $r_0$ e la correlazione $\rho$ sono invece assegnati a fini didattici.

La griglia principale contiene 252 intervalli annui e 253 punti temporali, incluso $t_0=0$. Poiché $252/12=21$, i fixing mensili corrispondono ai passi $21,42,\ldots,252$.

---

## 5. Quantità da stimare o calcolare

Le quantità richieste devono essere determinate nel seguente **ordine operativo**:

1. media e deviazione standard simulate di $S_T$ e $r_T$;
2. media e deviazione standard simulate del prezzo medio $A_T$;
3. **probabilità simulata di esercizio**, $\widehat{\mathbb P}(A_T>K)$;
4. valore medio del payoff non attualizzato $H_T$;
5. **prezzo Monte Carlo della call asiatica** $\widehat V_M$;
6. **errore standard Monte Carlo** e intervallo di confidenza al 95% del prezzo.

Le quantità devono essere ottenute a partire dai singoli scenari simulati. In particolare, la media asiatica, il payoff e il fattore di sconto devono essere determinati scenario per scenario prima dell'aggregazione Monte Carlo.

---

## 6. Output richiesti

### Tabelle

Produrre:

1. **tabella dei parametri del caso**, distinguendo dati osservati, proxy di mercato e parametri didattici;
2. **tabella delle statistiche dei fattori e della media asiatica**, contenente media e deviazione standard di $S_T$, $r_T$ e $A_T$;
3. **tabella di sintesi del payoff e del pricing**, contenente probabilità di esercizio, payoff medio, prezzo Monte Carlo, errore standard e intervallo di confidenza al 95%;
4. **tabella di diagnostica Monte Carlo** per $M=1\,000,\ 5\,000,\ 10\,000,\ 50\,000$, riportando almeno prezzo stimato ed errore standard.

### Grafici

Produrre almeno:

1. alcune traiettorie simulate dell'EURO STOXX 50, $S_t$;
2. alcune traiettorie simulate del tasso nominale $r_t$;
3. distribuzione simulata di $A_T$, con evidenza dello strike $K$;
4. distribuzione dei valori attualizzati $V^{(s)}$;
5. grafico di convergenza della stima Monte Carlo al crescere di $M$.

I grafici devono avere funzione interpretativa e riportare titoli, assi e unità coerenti.

---

## 7. Controlli richiesti

Il notebook deve verificare esplicitamente che:

1. la correlazione empirica degli shock simulati sia coerente con il valore assegnato $\rho=-0,25$;
2. il processo simulato del sottostante soddisfi $S_t>0$;
3. eventuali valori negativi di $r_t$ prodotti dalla discretizzazione siano rilevati e documentati secondo la convenzione numerica adottata nel caso aula;
4. per ogni scenario valga $\min_jS_{t_j}\leq A_T\leq\max_jS_{t_j}$;
5. il payoff soddisfi sempre $H_T\geq0$ e sia nullo quando $A_T\leq K$;
6. l'integrale del tasso sia costruito utilizzando i valori $r_{t_0},\ldots,r_{t_{N-1}}$ della stessa traiettoria e il fattore di sconto soddisfi $\widehat D^{(s)}(0,T)>0$;
7. l'errore standard Monte Carlo diminuisca al crescere di $M$, in modo compatibile con l'ordine $1/\sqrt{M}$;
8. il prezzo sia sufficientemente stabile rispetto a una griglia temporale più fine;
9. i risultati siano replicabili utilizzando il seed assegnato.

---

## 8. Ipotesi e limiti del caso

Ai fini di questa applicazione:

1. le dinamiche assegnate sono utilizzate direttamente ai fini del pricing;
2. $S_0$ e $r_0$ sono ancorati a osservazioni di mercato della data di riferimento;
3. $q$ e $\sigma_S$ sono proxy di mercato arrotondate, non calibrazioni esatte;
4. $\kappa_r$, $\theta_r$, $\sigma_r$ e $\rho$ sono parametri modellistici assegnati;
5. dividend yield, volatilità e correlazione sono costanti;
6. il tasso nominale è rappresentato da un unico fattore CIR;
7. l'integrale del tasso è approssimato sulla griglia giornaliera mediante somma di Riemann sinistra;
8. i fixing sono mensili ed equidistanti;
9. non sono considerati rischio di credito, rischio di liquidità, costi di transazione o fiscalità;
10. non sono richieste formule chiuse di pricing né modelli alternativi;
11. la convenzione numerica adottata per il CIR è quella già utilizzata nel caso aula;
12. la call asiatica è un contratto OTC stilizzato e non deve essere confusa con le opzioni vanilla EURO STOXX 50 quotate su Eurex;
13. il prezzo ottenuto è un risultato del modello assegnato e non una quotazione operativa di mercato.
