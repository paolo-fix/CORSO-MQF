# Lezione 07 — Scheda Caso Aula

## 1. Identificazione del caso

- **Lezione:** Lezione 07 — Applicazione in Python: simulazione di traiettorie e pricing
- **Tipo di caso:** Aula
- **Titolo:** *Inflazione e tassi stocastici: pricing Monte Carlo di un inflation-linked bond*
- **Contesto:** obbligazione indicizzata all'inflazione con cedole indicizzate e protezione del capitale nominale a scadenza
- **Uso previsto:** sviluppo guidato in aula mediante notebook Jupyter

Questa Scheda Caso costituisce la **specifica vincolante del lavoro**. Variabili, formule, parametri, output, controlli e ipotesi non devono essere modificati durante lo svolgimento.

La Scheda Caso non contiene la soluzione del problema. Il Flusso logico-teorico risolutivo, la scomposizione in tappe, il codice e l'interpretazione finale devono essere costruiti successivamente.

---

## 2. Contesto finanziario e domanda quantitativa

Un investitore deve valutare un'obbligazione i cui flussi dipendono dall'evoluzione futura dell'inflazione.

Le cedole sono indicizzate al livello dei prezzi. A scadenza, il capitale rimborsato è anch'esso indicizzato, ma non può essere inferiore al valore facciale.

La valutazione dipende congiuntamente da due fattori di rischio:

1. il **tasso istantaneo di inflazione** $i_t$, che determina l'indicizzazione dei flussi;
2. il **tasso nominale istantaneo privo di rischio** $r_t$, che determina l'attualizzazione.

Gli shock dei due fattori sono correlati.

La domanda quantitativa è:

> **Qual è il valore corrente dell'inflation-linked bond ottenuto mediante simulazione Monte Carlo, e quale ruolo assumono l'indicizzazione, il rimborso protetto e la dipendenza tra inflazione e tasso nominale?**

Il prezzo deve essere costruito a partire dai valori attuali ottenuti nelle singole repliche Monte Carlo.

---

## 3. Modello e struttura del contratto

### Inflazione

Il tasso istantaneo di inflazione segue un processo di Ornstein--Uhlenbeck:

$$
di_t=
\kappa_i(\theta_i-i_t)\,dt
+
\sigma_i\,dW_t^{(i)}.$$

Il modello ammette valori negativi di $i_t$, compatibili con periodi di deflazione.

### Tasso nominale

Il tasso nominale istantaneo segue un processo CIR:

$$
dr_t=
\kappa_r(\theta_r-r_t)\,dt
+
\sigma_r\sqrt{r_t}\,dW_t^{(r)}.$$

I parametri assegnati soddisfano la condizione di Feller:

$$
2\kappa_r\theta_r
\geq
\sigma_r^2.$$

Nella discretizzazione numerica, il termine diffusivo deve utilizzare

$$
\sqrt{\max(r_t,0)}.$$

L'operatore $\max(r_t,0)$ agisce soltanto all'interno della radice quadrata. Eventuali valori negativi del tasso prodotti dalla discretizzazione non devono essere automaticamente azzerati, ma rilevati e documentati.

### Dipendenza tra i fattori

Gli shock browniani soddisfano:

$$
dW_t^{(i)}\,dW_t^{(r)}=\rho\,dt.$$

La dipendenza deve essere preservata all'interno della stessa replica Monte Carlo.

### Indicizzazione

Sia $I_t$ il livello dell'indice dei prezzi e sia $I_0$ il suo valore iniziale.

Il fattore cumulato di indicizzazione è

$$
J_t=\frac{I_t}{I_0}=
\exp\left(
\int_0^t i_s\,ds
\right).$$

Sulla griglia temporale, l'integrale deve essere approssimato numericamente utilizzando i valori dell'inflazione appartenenti alla stessa replica.

### Fattore di sconto

Il fattore di sconto stocastico è

$$
D(0,t)=\exp\left(
-\int_0^t r_s\,ds
\right).$$

Anche questo integrale deve essere approssimato lungo la singola traiettoria del tasso. Non deve essere utilizzato il solo valore terminale $r_T$, né un tasso medio calcolato tra repliche differenti.

### Flussi contrattuali

Il bond ha valore facciale $N$, scadenza $T$ e tasso cedolare annuo $c$.

Le cedole sono semestrali. Alla data $t_j$,

$$
C_{t_j}=\frac{c}{2}N J_{t_j}.$$

Le cedole non sono protette contro la deflazione.

A scadenza il capitale rimborsato è

$$R_T=N\max(J_T,1).$$

Il floor protegge quindi il capitale nominale, non le cedole.

Per la replica Monte Carlo $k$,

$$
V^{(k)}=\sum_{j=1}^{m}
D^{(k)}(0,t_j)
C_{t_j}^{(k)}
+
D^{(k)}(0,T)
R_T^{(k)}.$$

Con $M$ repliche, il prezzo Monte Carlo è

$$
\widehat V_M=\frac{1}{M}
\sum_{k=1}^{M}
V^{(k)}.$$

Indicando con $s_V$ la deviazione standard campionaria dei valori $V^{(k)}$,

$$
SE(\widehat V_M)=\frac{s_V}{\sqrt{M}}.$$

Un intervallo di confidenza Monte Carlo approssimato al $95\%$ è

$$
\widehat V_M
\pm
1.96\,SE(\widehat V_M).$$

---

## 4. Parametri assegnati

I parametri sono assegnati a fini didattici e **non costituiscono una calibrazione a dati di mercato**.

| Componente | Parametro | Valore |
|---|---|---:|
| Contratto | $N$ | 100 |
| Contratto | $T$ | 5 anni |
| Contratto | $c$ | 1,5% annuo |
| Contratto | frequenza cedole | semestrale |
| Indice prezzi | $I_0$ | 100 |
| Inflazione OU | $i_0$ | 0,025 |
| Inflazione OU | $\kappa_i$ | 0,80 |
| Inflazione OU | $\theta_i$ | 0,020 |
| Inflazione OU | $\sigma_i$ | 0,015 |
| Tasso CIR | $r_0$ | 0,030 |
| Tasso CIR | $\kappa_r$ | 1,20 |
| Tasso CIR | $\theta_r$ | 0,030 |
| Tasso CIR | $\sigma_r$ | 0,10 |
| Dipendenza | $\rho$ | 0,25 |
| Simulazione | $\Delta t$ | 1/12 |
| Simulazione | $M$ | 50.000 |
| Simulazione | seed | 12345 |

La griglia principale è mensile e contiene 60 intervalli temporali.

Le date semestrali di pagamento coincidono con i passi $6,12,\ldots,60$.

---

## 5. Quantità da stimare o calcolare

Devono essere determinate almeno le seguenti quantità:

1. **prezzo Monte Carlo del bond**;
2. **errore standard Monte Carlo** del prezzo e relativo intervallo di confidenza al $95\%$;
3. **valore attuale medio delle cedole**;
4. **valore attuale atteso del rimborso del capitale**;
5. probabilità simulata di deflazione cumulata a scadenza, $\widehat{\mathbb P}(J_T<1)$;
6. media e deviazione standard simulate di $i_T$, $r_T$, $J_T$.

Tutte le quantità finanziarie devono essere costruite replica per replica prima dell'aggregazione Monte Carlo.

---

## 6. Output richiesti

### Tabelle

Produrre:

1. **tabella dei parametri del caso**;
2. **tabella di sintesi del pricing**, contenente almeno:
   - valore attuale medio delle cedole;
   - valore attuale atteso del rimborso;
   - prezzo complessivo;
3. **tabella di diagnostica Monte Carlo** per $M=
1\,000,\;
5\,000,\;
10\,000,\;
50\,000$, riportando almeno prezzo stimato ed errore standard;
4. **tabella delle statistiche terminali** di $i_T$, $r_T$ e $J_T$.

### Grafici

Produrre almeno:

1. alcune traiettorie simulate del tasso di inflazione $i_t$;
2. alcune traiettorie simulate del tasso nominale $r_t$;
3. distribuzione simulata di $J_T$;
4. distribuzione dei valori attuali $V^{(k)}$;
5. grafico di convergenza della stima Monte Carlo al crescere di $M$.

I grafici devono riportare titoli, assi e unità coerenti e devono avere una funzione interpretativa.

---

## 7. Controlli richiesti

Il notebook deve verificare esplicitamente che:

1. la correlazione empirica degli shock simulati sia coerente con
$\rho=0.25$;

2. il fattore di indicizzazione soddisfi
$J_{t_j}^{(k)}>0$ per ogni replica e data;

3. il rimborso soddisfi in ogni replica
$R_T^{(k)}\geq N$;

4. eventuali valori negativi di $r_t$ prodotti dalla discretizzazione siano rilevati, conteggiati e documentati, senza imporre automaticamente $r_t=0$;

5. la decomposizione del prezzo soddisfi
$
\widehat V_M=\widehat{PV}_C+\widehat{PV}_R$;

6. l'errore standard Monte Carlo diminuisca al crescere di $M$ in modo compatibile con l'ordine $\frac{1}{\sqrt M}$;

7. il prezzo sia sufficientemente stabile rispetto a una griglia temporale più fine.

Il controllo rispetto a $M$ e quello rispetto alla griglia temporale riguardano problemi diversi:

$M
\longrightarrow
\text{precisione Monte Carlo}$,


$\Delta t
\longrightarrow
\text{approssimazione temporale}$.

---

## 8. Ipotesi e limiti del caso

Ai fini di questa applicazione:

1. i parametri dei processi sono costanti e assegnati;
2. le dinamiche indicate vengono utilizzate direttamente ai fini della valutazione;
3. non sono richiesti stima econometrica, calibrazione di mercato o derivazione del cambio di misura;
4. non sono considerati rischio di credito, rischio di liquidità o fiscalità;
5. l'indicizzazione è semplificata e non replica integralmente le convenzioni operative di specifici titoli inflation-linked;
6. l'indice dei prezzi è costruito mediante integrazione del tasso istantaneo di inflazione;
7. inflazione e tasso nominale sono simulati sulla medesima griglia temporale;
8. la simulazione utilizza una rappresentazione discretizzata di processi formulati in tempo continuo;
9. il prezzo ottenuto deve essere interpretato come risultato del modello assegnato e non come quotazione osservabile di mercato.