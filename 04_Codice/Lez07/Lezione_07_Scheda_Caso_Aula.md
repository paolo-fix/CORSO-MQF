# Lezione 07 — Scheda Caso Aula

## 1. Identificazione del caso

- **Lezione:** Lezione 07 — Applicazione in Python: traiettorie, simulazione e pricing Monte Carlo
- **Tipo di caso:** caso aula
- **Titolo:** Inflazione e tassi stocastici: pricing Monte Carlo di un inflation-linked bond
- **Contesto:** obbligazione indicizzata all'inflazione con cedole indicizzate e protezione del capitale nominale a scadenza
- **Uso previsto:** sviluppo guidato in aula, con costruzione progressiva del notebook

Questa Scheda Caso costituisce la **specifica vincolante del lavoro**. Variabili, formule, parametri, output, controlli e ipotesi non devono essere modificati durante lo svolgimento.

La Scheda Caso non contiene la soluzione: il Flusso logico-teorico risolutivo, la scomposizione in tappe, il codice e l'interpretazione finale devono essere costruiti successivamente.

---

## 2. Contesto finanziario e domanda quantitativa

Un investitore deve valutare un'obbligazione i cui flussi dipendono dall'evoluzione futura dell'inflazione. Le cedole sono indicizzate al livello dei prezzi e, a scadenza, il capitale rimborsato non può essere inferiore al valore facciale.

La valutazione dipende congiuntamente da due fattori di rischio:

1. il **tasso istantaneo di inflazione** $i_t$, che determina l'indicizzazione dei flussi;
2. il **tasso nominale istantaneo privo di rischio** $r_t$, che determina l'attualizzazione.

I due fattori sono stocastici e i relativi shock sono correlati.

La domanda quantitativa è:

> **Qual è il valore corrente dell'inflation-linked bond ottenuto mediante simulazione Monte Carlo, e quale ruolo assumono l'indicizzazione, il rimborso protetto e la dipendenza tra inflazione e tasso nominale?**

La variabile finale del caso è il valore attuale dello strumento ottenuto in ciascuno scenario simulato. Il prezzo del bond è stimato come valore medio Monte Carlo di tale variabile.

---

## 3. Modello e struttura del contratto

### Inflazione

Il tasso istantaneo di inflazione segue un processo di Ornstein--Uhlenbeck:

$$di_t = \kappa_i(\theta_i-i_t)\,dt + \sigma_i\,dW_t^{(i)}.$$

Il modello ammette valori negativi di $i_t$, quindi consente scenari di deflazione.

### Tasso nominale

Il tasso nominale istantaneo segue un processo CIR:

$$dr_t = \kappa_r(\theta_r-r_t)\,dt + \sigma_r\sqrt{r_t}\,dW_t^{(r)}.$$

I parametri assegnati soddisfano la condizione di Feller:

$$2\kappa_r\theta_r\geq \sigma_r^2.$$

### Dipendenza tra i fattori

Gli shock browniani soddisfano:

$$dW_t^{(i)}\,dW_t^{(r)} = \rho\,dt.$$

### Indicizzazione

Sia $I_0$ il livello iniziale dell'indice dei prezzi. Il coefficiente cumulato di indicizzazione è

$$J_t = \frac{I_t}{I_0} = \exp\left( \int_0^t i_s\,ds \right).$$

### Fattore di sconto

Il fattore di sconto stocastico fino al tempo $t$ è

$$D(0,t) = \exp\left( -\int_0^t r_s\,ds \right).$$

### Flussi contrattuali

Il bond ha valore facciale $N$, scadenza $T$ e tasso cedolare annuo $c$. Le cedole sono semestrali. Alla data $t_j$,

$$C_{t_j} = \frac{c}{2}N J_{t_j}.$$

A scadenza il rimborso del capitale è

$$R_T = N\max(J_T,1).$$

Il capitale è quindi protetto contro una diminuzione cumulata dell'indice sotto il livello iniziale; le cedole non sono protette.

Per uno scenario simulato $s$, il valore attuale del bond è

$$V^{(s)} = \sum_{j=1}^{m} D^{(s)}(0,t_j)C_{t_j}^{(s)} + D^{(s)}(0,T)R_T^{(s)}.$$

Il prezzo del bond deve essere stimato mediante Monte Carlo a partire dalla distribuzione dei valori $V^{(s)}$.

---

## 4. Parametri assegnati

I parametri hanno funzione didattica e **non costituiscono una calibrazione a dati di mercato**.

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
| Simulazione | $\Delta t$ | $1/12$ |
| Simulazione | $M$ | 50.000 |
| Simulazione | seed | 12345 |

La griglia temporale principale è mensile. Le date di pagamento delle cedole coincidono con i multipli semestrali della griglia.

---

## 5. Quantità da stimare o calcolare

Devono essere determinate almeno le seguenti quantità:

1. **prezzo Monte Carlo del bond**;
2. **errore standard Monte Carlo** del prezzo e relativo intervallo di confidenza al 95%;
3. **valore attuale medio delle cedole**;
4. **stima Monte Carlo del valore attuale atteso del rimborso del capitale**;
5. probabilità simulata di deflazione cumulata a scadenza, $\widehat{\mathbb P}(J_T<1)$;
6. media e deviazione standard simulate di $i_T$, $r_T$ e $J_T$.

---

## 6. Output richiesti

### Tabelle

Produrre:

1. **tabella dei parametri del caso**;
2. **tabella di sintesi del pricing**, contenente almeno valore attuale medio delle cedole, valore attuale atteso del rimborso del capitale e prezzo complessivo;
3. **tabella di diagnostica Monte Carlo** per $M=1\,000,\ 5\,000,\ 10\,000,\ 50\,000$, riportando almeno prezzo stimato ed errore standard;
4. **tabella delle statistiche terminali** di $i_T$, $r_T$ e $J_T$.

### Grafici

Produrre almeno:

1. traiettorie simulate del tasso di inflazione $i_t$;
2. traiettorie simulate del tasso nominale $r_t$;
3. distribuzione simulata di $J_T$;
4. distribuzione dei valori attuali $V^{(s)}$;
5. grafico di convergenza della stima Monte Carlo al crescere di $M$.

I grafici devono avere funzione interpretativa e riportare titoli, assi e unità di misura coerenti.

---

## 7. Controlli richiesti

Il notebook deve verificare esplicitamente che:

1. la correlazione empirica degli shock simulati sia coerente con il valore assegnato $\rho=0,25$;
2. $J_t>0$ per costruzione;
3. il rimborso soddisfi in ogni scenario $R_T\geq N$;
4. eventuali valori negativi di $r_t$ generati dalla discretizzazione siano rilevati e documentati come possibile anomalia numerica;
5. la decomposizione del valore sia coerente:
$$\text{prezzo totale}=\text{valore attuale medio delle cedole}+\text{valore attuale atteso del rimborso}.$$
6. l'errore standard Monte Carlo diminuisca al crescere di $M$, in modo compatibile con l'ordine $1/\sqrt{M}$;
7. il prezzo sia sufficientemente stabile rispetto a una griglia temporale più fine.

---

## 8. Ipotesi e limiti del caso

Ai fini di questa applicazione:

1. i parametri dei processi sono costanti e assegnati;
2. le dinamiche indicate costituiscono direttamente il modello utilizzato per il pricing;
3. non sono richieste stima econometrica, calibrazione o derivazione del cambio di misura;
4. non sono considerati rischio di credito, rischio di liquidità o fiscalità;
5. l'indicizzazione è semplificata e non replica i lag e le convenzioni operative dei TIPS reali;
6. l'indice dei prezzi è costruito direttamente dall'integrazione del tasso istantaneo di inflazione;
7. il modello deve essere interpretato come esercizio di simulazione e pricing, non come modello operativo di quotazione di uno specifico titolo di mercato.
