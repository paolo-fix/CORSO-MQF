# Lezione 04 — Scheda Caso Aula

## 1. Identificazione del caso

- **Lezione:** Lezione 04 — Applicazione in Python: probabilità, variabili casuali e condizionamento
- **Tipo di caso:** aula
- **Titolo:** *Perdita obbligazionaria condizionata a regimi di tasso*
- **Contesto:** portafoglio obbligazionario a tasso fisso esposto a shock dei rendimenti
- **Uso previsto:** sviluppo guidato in aula, con costruzione progressiva del notebook

Questa Scheda Caso costituisce la **specifica vincolante del lavoro**. Variabili, formule, parametri, output, controlli e ipotesi non devono essere modificati durante lo svolgimento.

La Scheda Caso non contiene la soluzione del problema: il Flusso logico-teorico risolutivo, la scomposizione in tappe, il codice e l'interpretazione finale devono essere costruiti successivamente.

---

## 2. Contesto e domanda quantitativa

Il caso considera un portafoglio obbligazionario a tasso fisso esposto a variazioni dei rendimenti di mercato. Il riferimento economico è una fase di rapido rialzo dei tassi: quando i rendimenti aumentano, il valore di un portafoglio a tasso fisso tende a diminuire e l'intensità della variazione dipende, in prima approssimazione, dalla duration modificata.

L'incertezza non viene rappresentata mediante un'unica distribuzione dello shock di rendimento. Si assume invece che il mercato possa trovarsi in tre diversi **regimi informativi**, ciascuno caratterizzato da una diversa distribuzione condizionata dello shock.

La domanda quantitativa è:

> **Qual è la distribuzione della perdita del portafoglio e come cambia la perdita attesa condizionando sui diversi regimi di tasso?**

Il caso non ha finalità previsionali. La simulazione serve a rendere osservabile il legame tra shock di rendimento, perdita, partizione informativa, distribuzioni condizionate e valori attesi condizionati.

---

## 3. Modello e struttura del problema

Il portafoglio ha valore iniziale $V_0$ e duration modificata $D$. Lo shock di rendimento a un periodo è la variabile casuale continua $\Delta y$.

La variazione approssimata del valore del portafoglio è:

$$\Delta V\simeq-DV_0\Delta y.$$

La perdita è definita come diminuzione del valore del portafoglio:

$$L=-\Delta V\simeq DV_0\Delta y.$$

Il segno è quindi scelto in modo che $\Delta y>0$ produca $L>0$, mentre una diminuzione dei rendimenti possa generare una perdita negativa, interpretabile come guadagno.

### Partizione informativa

Lo spazio degli esiti è suddiviso nei tre eventi:

$$\Omega=A_1\cup A_2\cup A_3,\qquad A_i\cap A_j=\emptyset\quad\text{per }i\neq j.$$

| Evento | Descrizione | Interpretazione finanziaria |
|---|---|---|
| $A_1$ | Disinflazione ordinata | rendimenti poco mossi o in moderata diminuzione |
| $A_2$ | Inflazione persistente | rialzo moderato dei rendimenti |
| $A_3$ | Repricing severo | rialzo marcato e maggiore volatilità |

La sigma-algebra informativa è:

$$\mathcal{G}=\sigma(A_1,A_2,A_3).$$

Condizionatamente al regime $A_g$:

$$\Delta y\mid A_g\sim\mathcal{N}(\mu_g,\sigma_g^2),\qquad g=1,2,3.$$

La distribuzione non condizionata di $\Delta y$ deriva quindi dalla combinazione delle probabilità dei regimi e delle rispettive distribuzioni condizionate.

La soglia di shock che produce una perdita pari a $\ell$ è:

$$\Delta y^\star=\frac{\ell}{DV_0}.$$

Con i parametri assegnati:

$$\Delta y^\star=\frac{500.000}{6\cdot10.000.000}=0,008333\ldots,$$

cioè circa 83,33 punti base. Pertanto:

$$L>\ell\quad\Longleftrightarrow\quad\Delta y>0,008333\ldots.$$

---

## 4. Parametri assegnati

I parametri sono stilizzati e hanno funzione didattica. Non sono stime storiche e non hanno finalità previsionali.

### Parametri finanziari e computazionali

| Grandezza | Valore | Unità |
|---|---:|---|
| $V_0$ | 10.000.000 | euro |
| $D$ | 6 | anni |
| $\ell$ | 500.000 | euro |
| $n$ | 50.000 | simulazioni |
| seed | 12345 | — |

### Probabilità dei regimi

| Evento | Probabilità |
|---|---:|
| $A_1$ | 0,35 |
| $A_2$ | 0,45 |
| $A_3$ | 0,20 |

### Distribuzioni condizionate dello shock

| Evento | $\mu_g$ | $\sigma_g$ | Lettura finanziaria |
|---|---:|---:|---|
| $A_1$ | -0,0010 | 0,0040 | lieve riduzione media dei rendimenti |
| $A_2$ | 0,0030 | 0,0060 | rialzo moderato |
| $A_3$ | 0,0100 | 0,0100 | rialzo marcato e maggiore dispersione |

Gli shock sono espressi in unità decimali: per esempio, $0,0030$ corrisponde a 30 punti base.

---

## 5. Quantità da stimare o calcolare

Devono essere determinate almeno le seguenti quantità non condizionate:

$$\mathbb{E}[L],\qquad\mathbb{P}(L>\ell),\qquad q_\alpha(L).$$

Per ciascun regime devono inoltre essere stimate le perdite attese condizionate:

$$\mathbb{E}[L\mid A_g],\qquad g=1,2,3.$$

Il valore atteso condizionato rispetto all'informazione di regime è la variabile casuale:

$$\mathbb{E}[L\mid\mathcal{G}]=\sum_{g=1}^{3}\mathbb{E}[L\mid A_g]\mathbf{1}_{A_g}.$$

Deve essere verificata la formula del valore atteso totale:

$$\mathbb{E}[L]=\sum_{g=1}^{3}\mathbb{P}(A_g)\mathbb{E}[L\mid A_g].$$

Nel notebook, la corrispondente identità empirica deve risultare soddisfatta salvo l'errore campionario e gli arrotondamenti.

---

## 6. Output richiesti

### Tabelle

Produrre almeno:

1. **tabella dei parametri**, comprendente parametri finanziari, probabilità dei regimi e parametri condizionati;
2. **tabella di controllo della simulazione**, con frequenze empiriche dei regimi e media/deviazione standard empirica di $\Delta y\mid A_g$;
3. **tabella descrittiva della perdita $L$**, con media, deviazione standard, minimo, massimo e quantili principali;
4. **tabella delle quantità di rischio**, comprendente $\widehat{\mathbb{P}}(L>\ell)$ e le tre medie condizionate $\widehat{\mathbb{E}}[L\mid A_g]$;
5. **tabella di verifica del valore atteso totale**, confrontando la media globale della perdita con la media pesata delle medie condizionate.

### Grafici

Produrre almeno:

1. istogramma delle frequenze percentuali dello shock di rendimento $\Delta y$;
2. istogramma delle frequenze percentuali della perdita $L$, con evidenza della soglia $\ell$;
3. grafico delle medie condizionate $\widehat{\mathbb{E}}[L\mid A_g]$;
4. confronto tra le distribuzioni condizionate della perdita.

I grafici devono avere funzione interpretativa e non puramente decorativa.

---

## 7. Controlli richiesti

Il notebook deve verificare esplicitamente che:

1. le probabilità dei tre regimi sommino a uno e le frequenze empiriche siano coerenti con esse;
2. le medie e deviazioni standard empiriche di $\Delta y\mid A_g$ siano coerenti con $\mu_g$ e $\sigma_g$;
3. il vettore della perdita abbia dimensione $n$ e rispetti $L=DV_0\Delta y$;
4. la coerenza dei segni sia rispettata: $\Delta y>0\Rightarrow L>0$ e $\Delta y<0\Rightarrow L<0$;
5. la probabilità di superamento della soglia sia coerente con $\Delta y^\star=0,008333\ldots$;
6. la media globale di $L$ coincida, salvo arrotondamenti, con la media pesata delle medie condizionate;
7. i quantili rispettino l'ordinamento atteso e la media cada tra minimo e massimo campionario.

Devono inoltre rimanere distinti:

- gli eventi $A_g$, che sono blocchi informativi;
- lo shock $\Delta y$;
- la perdita $L$;
- il numero $\mathbb{E}[L\mid A_g]$;
- la variabile casuale $\mathbb{E}[L\mid\mathcal{G}]$.

L'interpretazione finale deve riconoscere $A_3$ come regime con perdita attesa maggiore, $A_2$ come situazione intermedia e la possibilità che $A_1$ presenti una perdita media negativa. L'informazione di regime modifica la distribuzione rilevante, ma non elimina l'incertezza.

---

## 8. Ipotesi e limiti del caso

Il modello assume:

1. portafoglio rappresentato esclusivamente da $V_0$ e duration modificata $D$;
2. approssimazione lineare della variazione di valore mediante la duration;
3. unica fonte di incertezza pari a $\Delta y$;
4. informazione rappresentata dalla partizione $\{A_1,A_2,A_3\}$;
5. distribuzione normale di $\Delta y$ condizionatamente a ciascun regime;
6. simulazione Monte Carlo utilizzata per approssimare frequenze, probabilità e valori attesi.

Sono deliberatamente esclusi flussi cedolari espliciti, scadenze multiple, convessità, struttura a termine, movimenti non paralleli della curva, rischio di credito, rischio di liquidità, ribilanciamento, dinamica multiperiodale e stima dei parametri da dati reali.

Il caso è quindi un modello didattico di rischio di tasso a un periodo. I risultati non devono essere interpretati come previsione dei tassi o come valutazione completa di un portafoglio obbligazionario reale.
