# Lezione 04 — Scheda Caso Take-Home

## 1. Identificazione del caso

- **Lezione:** Lezione 04 — Applicazione in Python: probabilità, variabili casuali e condizionamento
- **Tipo di caso:** take-home
- **Titolo:** *Shortfall di margine condizionato a regimi del costo dell'energia*
- **Contesto:** impresa manifatturiera energivora esposta all'incertezza del prezzo dell'energia
- **Uso previsto:** lavoro individuale con notebook Python e interazione documentata con l'IA

Questa Scheda Caso costituisce la **specifica vincolante del lavoro**. Variabili, formule, parametri, output, controlli e ipotesi non devono essere modificati durante lo svolgimento.

La Scheda Caso non contiene la soluzione del problema: il Flusso logico-teorico risolutivo, la scomposizione in tappe, il codice e l'interpretazione finale devono essere costruiti successivamente.

---

## 2. Contesto e domanda quantitativa

Si considera un'impresa manifatturiera energivora per la quale il prezzo dell'energia rappresenta una fonte rilevante di rischio operativo. Un aumento del prezzo unitario dell'energia incrementa il costo energetico totale e riduce il margine operativo.

L'impresa fissa un margine minimo desiderato $m^\star$. Quando il margine effettivo scende sotto questa soglia, si genera uno **shortfall di margine**, cioè una carenza rispetto all'obiettivo economico.

L'incertezza del prezzo energetico è rappresentata attraverso tre regimi informativi, ciascuno caratterizzato da una diversa distribuzione condizionata del prezzo.

La domanda quantitativa è:

> **Qual è la distribuzione dello shortfall di margine e come cambia lo shortfall atteso condizionando sui diversi regimi del costo dell'energia?**

Il caso non ha finalità previsionali. La simulazione serve a rendere osservabile la relazione tra prezzo energetico, costo, margine, shortfall, soglie di rischio e informazione di regime.

---

## 3. Modello e struttura del problema

Le grandezze principali sono:

- $G_0$: contribuzione operativa netta non energetica;
- $Q_E$: fabbisogno energetico;
- $P_E$: prezzo unitario dell'energia;
- $C_E$: costo energetico totale;
- $M$: margine operativo dopo il costo energetico;
- $m^\star$: margine minimo desiderato;
- $S$: shortfall di margine;
- $s^\star$: soglia di shortfall severo.

Le relazioni economiche sono:

$$C_E=Q_EP_E,$$

$$M=G_0-Q_EP_E,$$

$$S=(m^\star-M)^+=(m^\star-G_0+Q_EP_E)^+.$$

Per costruzione, $S\geq0$.

### Partizione informativa

Lo spazio degli esiti è suddiviso nei tre eventi:

$$\Omega=A_1\cup A_2\cup A_3,\qquad A_i\cap A_j=\emptyset\quad\text{per }i\neq j.$$

| Evento | Descrizione | Interpretazione economica |
|---|---|---|
| $A_1$ | Normalizzazione energetica | prezzi relativamente contenuti |
| $A_2$ | Tensione persistente | prezzi elevati ma non estremi |
| $A_3$ | Shock energetico severo | prezzi molto elevati e più volatili |

La sigma-algebra informativa è:

$$\mathcal{G}=\sigma(A_1,A_2,A_3).$$

Condizionatamente al regime $A_g$:

$$P_E\mid A_g\sim\mathcal{N}(\mu_g,\sigma_g^2),\qquad g=1,2,3.$$

La distribuzione normale è una scelta didattica semplificata. Eventuali prezzi simulati negativi devono essere rilevati e discussi come limite del modello, non eliminati senza motivazione.

### Soglie implicite

Lo shortfall è positivo quando:

$$S>0\quad\Longleftrightarrow\quad P_E>\frac{G_0-m^\star}{Q_E}=120\ \text{euro/MWh}.$$

Lo shortfall supera la soglia severa quando:

$$S>s^\star\quad\Longleftrightarrow\quad P_E>\frac{G_0-m^\star+s^\star}{Q_E}=140\ \text{euro/MWh}.$$

Queste soglie collegano direttamente il fattore di rischio $P_E$ alle due condizioni economiche di interesse.

---

## 4. Parametri assegnati

I parametri sono stilizzati e hanno funzione didattica. Non sono stime storiche e non hanno finalità previsionali.

### Parametri economico-finanziari e computazionali

| Grandezza | Valore | Unità |
|---|---:|---|
| $G_0$ | 8.000.000 | euro |
| $Q_E$ | 50.000 | MWh |
| $m^\star$ | 2.000.000 | euro |
| $s^\star$ | 1.000.000 | euro |
| $n$ | 50.000 | simulazioni |
| seed | 24680 | — |

### Probabilità dei regimi

| Evento | Probabilità |
|---|---:|
| $A_1$ | 0,35 |
| $A_2$ | 0,45 |
| $A_3$ | 0,20 |

### Distribuzioni condizionate del prezzo dell'energia

| Evento | $\mu_g$ | $\sigma_g$ | Unità |
|---|---:|---:|---|
| $A_1$ | 75 | 15 | euro/MWh |
| $A_2$ | 115 | 25 | euro/MWh |
| $A_3$ | 170 | 45 | euro/MWh |

---

## 5. Quantità da stimare o calcolare

Devono essere determinate almeno le seguenti quantità non condizionate:

$$\mathbb{E}[S],\qquad\mathbb{P}(S>0),\qquad\mathbb{P}(S>s^\star),\qquad q_\alpha(S).$$

Per ciascun regime devono inoltre essere stimate:

$$\mathbb{E}[S\mid A_g],\qquad g=1,2,3.$$

Il valore atteso condizionato rispetto all'informazione di regime è:

$$\mathbb{E}[S\mid\mathcal{G}]=\sum_{g=1}^{3}\mathbb{E}[S\mid A_g]\mathbf{1}_{A_g}.$$

Deve essere verificata la formula del valore atteso totale:

$$\mathbb{E}[S]=\sum_{g=1}^{3}\mathbb{P}(A_g)\mathbb{E}[S\mid A_g].$$

Nel notebook deve essere mantenuta la distinzione tra $\mathbb{E}[S\mid A_g]$, che è un numero, $\mathbb{E}[S\mid\mathcal{G}]$, che è una variabile casuale, ed $\mathbb{E}[S]$, che è il valore atteso non condizionato.

---

## 6. Output richiesti

### Tabelle

Produrre almeno:

1. **tabella dei parametri**, comprendente dati economico-finanziari, probabilità dei regimi, parametri condizionati e soglie implicite;
2. **tabella di controllo della simulazione**, con frequenze empiriche dei regimi e media/deviazione standard empirica di $P_E\mid A_g$;
3. **tabella descrittiva delle grandezze principali**, comprendente almeno $P_E$, $M$ e $S$, con media, deviazione standard e principali statistiche descrittive;
4. **tabella delle quantità di rischio**, comprendente $\widehat{\mathbb{P}}(S>0)$, $\widehat{\mathbb{P}}(S>s^\star)$, quantili principali e le tre medie condizionate $\widehat{\mathbb{E}}[S\mid A_g]$;
5. **tabella di verifica del valore atteso totale**, confrontando la media globale dello shortfall con la media pesata delle medie condizionate.

### Grafici

Produrre almeno:

1. istogramma o densità empirica del prezzo dell'energia $P_E$;
2. istogramma o densità empirica del margine operativo $M$;
3. distribuzione empirica dello shortfall $S$, con evidenza della massa in zero quando osservabile e della soglia $s^\star$;
4. grafico delle medie condizionate $\widehat{\mathbb{E}}[S\mid A_g]$;
5. confronto tra le distribuzioni condizionate dello shortfall.

I grafici devono avere funzione interpretativa e non puramente decorativa.

---

## 7. Controlli richiesti

Il notebook deve verificare esplicitamente che:

1. le probabilità dei regimi sommino a uno, le frequenze empiriche siano coerenti con esse e ciascun regime abbia numerosità sufficiente;
2. le medie e deviazioni standard empiriche di $P_E\mid A_g$ siano coerenti con $\mu_g$ e $\sigma_g$;
3. sia rilevata l'eventuale presenza di valori negativi di $P_E$;
4. siano rispettate le relazioni $C_E=Q_EP_E$, $M=G_0-Q_EP_E$ e $S=(m^\star-M)^+$;
5. lo shortfall sia sempre non negativo;
6. $\widehat{\mathbb{P}}(S>0)$ sia coerente con la soglia $P_E>120$;
7. $\widehat{\mathbb{P}}(S>s^\star)$ sia coerente con la soglia $P_E>140$;
8. la media globale di $S$ coincida, salvo arrotondamenti, con la media pesata delle medie condizionate;
9. i quantili rispettino l'ordinamento atteso e la media cada tra minimo e massimo campionario.

Devono inoltre rimanere distinti il fattore di rischio $P_E$, il costo $C_E$, il margine $M$, lo shortfall $S$, gli eventi informativi $A_g$ e i diversi oggetti di valore atteso condizionato.

L'interpretazione finale deve riconoscere $A_3$ come regime con shortfall atteso maggiore, $A_2$ come situazione intermedia e la possibilità che in $A_1$ lo shortfall sia nullo in molte simulazioni. La massa in zero dello shortfall deve essere collegata alla definizione mediante parte positiva.

---

## 8. Ipotesi e limiti del caso

Il modello assume:

1. impresa rappresentata da $G_0$ e da un fabbisogno energetico fisso $Q_E$;
2. unica fonte di incertezza pari al prezzo unitario $P_E$;
3. costo energetico proporzionale al prezzo;
4. margine determinato da $M=G_0-Q_EP_E$;
5. shortfall definito da $S=(m^\star-M)^+$;
6. informazione rappresentata dalla partizione $\{A_1,A_2,A_3\}$;
7. distribuzione normale di $P_E$ condizionatamente a ciascun regime;
8. simulazione Monte Carlo utilizzata per approssimare frequenze, probabilità e valori attesi.

Sono deliberatamente esclusi ricavi aleatori, altri costi aleatori, elasticità della produzione, trasferimento dei maggiori costi sui prezzi di vendita, coperture energetiche, acquisti a termine, dinamica multiperiodale, correlazioni con altre variabili macroeconomiche e stima dei parametri da dati reali.

Non viene imposta positività al prezzo tramite distribuzioni troncate. Eventuali valori negativi simulati devono essere trattati come limite della specificazione normale.

Il caso è quindi un modello didattico di rischio operativo legato al costo dell'energia. I risultati non devono essere interpretati come previsione del prezzo energetico o come rappresentazione completa della redditività di un'impresa reale.
