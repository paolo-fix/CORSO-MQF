# Lezione 04 — Scheda macro del caso aula

## Caso aula

**Titolo provvisorio:**  
Perdita obbligazionaria condizionata a regimi di tasso

**Tipo di materiale:**  
Scheda macro per la progettazione del caso aula, dei prompt virtuosi e del notebook docente.

**Collocazione nel corso:**  
Lezione applicativa Python collegata ai contenuti teorici delle prime tre lezioni: spazi di probabilità, eventi, variabili casuali, distribuzioni, momenti, probabilità condizionata, valore atteso condizionato rispetto a eventi, partizioni e sigma-algebre informative.

---

## 1. Premessa storica e finanziaria

Tra il 2022 e il 2023 l’area euro ha attraversato una fase di rapido irrigidimento monetario. Dopo un lungo periodo di tassi ufficiali molto bassi o negativi, l’aumento dell’inflazione ha indotto la Banca Centrale Europea ad alzare progressivamente i tassi di riferimento. Il tasso sui depositi, che rappresenta oggi il principale riferimento operativo per l’orientamento della politica monetaria, ha raggiunto il 4,00% nel settembre 2023.

Questo passaggio ha avuto implicazioni dirette per la valutazione degli strumenti obbligazionari. Quando i rendimenti di mercato aumentano, il prezzo di un’obbligazione a tasso fisso tende a diminuire. L’intensità della variazione dipende, in prima approssimazione, dalla duration modificata del titolo o del portafoglio.

La lezione non ha l’obiettivo di ricostruire empiricamente il mercato obbligazionario europeo, né di stimare un modello storico dei tassi. Il caso utilizza invece una simulazione controllata, ispirata al contesto recente, per rendere osservabile il legame tra:

- shock di rendimento;
- perdita di valore di un portafoglio obbligazionario;
- stati informativi del mercato dei tassi;
- distribuzione empirica delle perdite;
- valori attesi condizionati.

La domanda didattica centrale è: come cambia la valutazione della perdita attesa quando l’analista dispone di un’informazione di scenario sul regime dei tassi?

---

## 2. Domanda quantitativa

Si considera un portafoglio obbligazionario semplificato, con valore iniziale $V_0$ e duration modificata $D$.

La variabile casuale rilevante è uno shock di rendimento a un periodo, indicato con $\Delta y$. La perdita approssimata del portafoglio è definita da:

$$
L = D V_0 \Delta y.
$$

Il segno è scelto in modo che uno shock positivo dei rendimenti, $\Delta y>0$, generi una perdita positiva.

La domanda quantitativa è:

$$
\text{Qual è la distribuzione della perdita } L
\text{ e come cambia la perdita attesa condizionando su diversi regimi di tasso?}
$$

In particolare, si vogliono stimare:

$$
\mathbb{E}[L],
\qquad
\mathbb{P}(L>\ell),
\qquad
q_{\alpha}(L),
\qquad
\mathbb{E}[L\mid Z=g],
\qquad
\mathbb{E}[L\mid\mathcal{G}],
$$

dove $Z$ rappresenta lo stato informativo del mercato dei tassi e $\mathcal{G}=\sigma(Z)$.

---

## 3. Grandezze finanziarie

Le grandezze finanziarie del caso sono:

- $V_0$: valore iniziale del portafoglio obbligazionario;
- $D$: duration modificata del portafoglio;
- $\Delta y$: variazione del rendimento di mercato, espressa in unità decimali;
- $L$: perdita approssimata del portafoglio;
- $\ell$: soglia di perdita rilevante per l’analisi;
- $Z$: stato informativo relativo al regime dei tassi.

La relazione finanziaria fondamentale è:

$$
\frac{\Delta P}{P} \simeq -D\Delta y.
$$

Se $V_0$ è il valore iniziale del portafoglio, la variazione approssimata di valore è:

$$
\Delta V \simeq -D V_0 \Delta y.
$$

La perdita, definita come diminuzione del valore del portafoglio, è quindi:

$$
L=-\Delta V\simeq D V_0 \Delta y.
$$

Questa approssimazione è lineare. Essa è didatticamente utile perché rende immediato il legame tra shock di tasso e perdita, ma deve essere interpretata come modello locale e semplificato.

---

## 4. Variabili casuali e stati informativi

Il caso utilizza due variabili casuali principali:

$$
Z:\Omega\to\{1,2,3\},
$$

dove $Z$ identifica il regime di tasso, e

$$
\Delta y:\Omega\to\mathbb{R},
$$

dove $\Delta y$ identifica lo shock di rendimento.

La perdita $L$ è una variabile casuale derivata:

$$
L = D V_0 \Delta y.
$$

Gli stati informativi sono definiti come eventi:

$$
A_1=\{Z=1\},
\qquad
A_2=\{Z=2\},
\qquad
A_3=\{Z=3\}.
$$

Interpretazione finanziaria degli stati:

| Stato | Descrizione | Interpretazione |
|---|---|---|
| $A_1$ | Disinflazione ordinata | I rendimenti tendono a muoversi poco o a diminuire moderatamente |
| $A_2$ | Inflazione persistente | I rendimenti tendono ad aumentare in modo moderato |
| $A_3$ | Repricing severo | I rendimenti aumentano in modo marcato e con maggiore volatilità |

Gli eventi $A_1,A_2,A_3$ formano una partizione di $\Omega$. La sigma-algebra informativa generata dallo stato $Z$ è:

$$
\mathcal{G}=\sigma(A_1,A_2,A_3).
$$

Il valore atteso condizionato rispetto a $\mathcal{G}$ sarà una variabile casuale costante su ciascun blocco della partizione:

$$
\mathbb{E}[L\mid\mathcal{G}]
=
\sum_{g=1}^{3}
\mathbb{E}[L\mid A_g]\mathbf{1}_{A_g}.
$$

---

## 5. Specificazione parametrica iniziale

La specificazione seguente è proposta come base docente per la prima versione del notebook. I valori sono stilizzati e hanno funzione didattica, non previsionale.

### Parametri finanziari

| Grandezza | Valore iniziale | Commento |
|---|---:|---|
| $V_0$ | 10.000.000 | Valore iniziale del portafoglio |
| $D$ | 6 | Duration modificata |
| $\ell$ | 500.000 | Soglia di perdita rilevante |
| $n$ | 50.000 | Numero di simulazioni Monte Carlo |
| seed | 12345 | Seme per la replicabilità |

### Probabilità degli stati

| Stato | Descrizione | Probabilità |
|---|---|---:|
| $A_1$ | Disinflazione ordinata | 0,35 |
| $A_2$ | Inflazione persistente | 0,45 |
| $A_3$ | Repricing severo | 0,20 |

### Distribuzioni condizionate degli shock di rendimento

Si assume:

$$
\Delta y\mid A_g \sim \mathcal{N}(\mu_g,\sigma_g^2).
$$

| Stato | $\mu_g$ | $\sigma_g$ | Lettura finanziaria |
|---|---:|---:|---|
| $A_1$ | -0,0010 | 0,0040 | lieve riduzione media dei rendimenti |
| $A_2$ | 0,0030 | 0,0060 | rialzo moderato dei rendimenti |
| $A_3$ | 0,0100 | 0,0100 | rialzo marcato e maggiore dispersione |

Tutti gli shock sono espressi in unità decimali. Per esempio, $0,0030$ corrisponde a 30 punti base.

---

## 6. Ipotesi modellistiche

Il caso si fonda sulle seguenti ipotesi:

1. Il portafoglio è rappresentato da un valore iniziale $V_0$ e da una duration modificata $D$.
2. La variazione di valore del portafoglio è approssimata linearmente mediante la formula di duration.
3. L’incertezza è concentrata nello shock di rendimento $\Delta y$.
4. Lo stato informativo $Z$ è osservabile prima della valutazione condizionata.
5. Condizionatamente allo stato $Z=g$, lo shock $\Delta y$ segue una distribuzione normale con parametri specifici.
6. Gli stati $A_1,A_2,A_3$ costituiscono una partizione dello spazio degli esiti.
7. La simulazione Monte Carlo approssima le quantità teoriche mediante frequenze e medie empiriche.
8. Il modello non include convessità, rischio di credito, variazioni non parallele della curva, liquidità, ribilanciamento o dinamica multiperiodale.

---

## 7. Quantità teoriche da stimare

Le quantità teoriche principali sono:

### Media non condizionata della perdita

$$
\mathbb{E}[L].
$$

### Probabilità di superamento soglia

$$
\mathbb{P}(L>\ell).
$$

### Quantili della perdita

$$
q_{\alpha}(L),
$$

con particolare attenzione a livelli come $\alpha=0,95$ e $\alpha=0,99$.

### Valori attesi condizionati sui singoli stati

$$
\mathbb{E}[L\mid A_g],
\qquad g=1,2,3.
$$

### Valore atteso condizionato rispetto alla sigma-algebra informativa

$$
\mathbb{E}[L\mid\mathcal{G}]
=
\sum_{g=1}^{3}
\mathbb{E}[L\mid A_g]\mathbf{1}_{A_g}.
$$

### Verifica della formula del valore atteso totale

$$
\mathbb{E}[L]
=
\sum_{g=1}^{3}
\mathbb{P}(A_g)\mathbb{E}[L\mid A_g].
$$

Nel notebook questa uguaglianza sarà verificata empiricamente confrontando:

$$
\widehat{\mathbb{E}}[L]
$$

con

$$
\sum_{g=1}^{3}
\widehat{\mathbb{P}}(A_g)
\widehat{\mathbb{E}}[L\mid A_g].
$$

---

## 8. Output computazionali attesi

Il notebook docente dovrà produrre almeno i seguenti output.

### Tabelle

1. Tabella dei parametri finanziari.
2. Tabella degli stati informativi e delle probabilità assegnate.
3. Tabella dei parametri condizionati $(\mu_g,\sigma_g)$.
4. Tabella delle frequenze simulate degli stati.
5. Tabella delle statistiche descrittive della perdita:
   - media;
   - deviazione standard;
   - minimo;
   - massimo;
   - quantili principali.
6. Tabella delle perdite attese condizionate:
   - $\widehat{\mathbb{E}}[L\mid A_1]$;
   - $\widehat{\mathbb{E}}[L\mid A_2]$;
   - $\widehat{\mathbb{E}}[L\mid A_3]$.
7. Tabella di verifica della formula del valore atteso totale.

### Grafici

1. Istogramma della distribuzione empirica della perdita $L$.
2. Istogrammi o densità empiriche della perdita condizionate agli stati $A_1,A_2,A_3$.
3. Grafico delle perdite attese condizionate per regime.
4. Grafico della distribuzione empirica con evidenza della soglia $\ell$.
5. Eventuale ECDF della perdita.

### Output interpretativi

1. Commento sul segno e sull’ordine di grandezza delle perdite simulate.
2. Commento sulla differenza tra media non condizionata e medie condizionate.
3. Discussione del ruolo informativo di $Z$.
4. Discussione dei limiti dell’approssimazione lineare di duration.
5. Discussione della natura simulativa e non previsionale dell’esercizio.

---

## 9. Controlli richiesti

Il notebook deve includere controlli numerici, logici e interpretativi.

### Controlli numerici

1. Le probabilità degli stati devono sommare a uno.
2. Le frequenze simulate degli stati devono essere ragionevolmente vicine alle probabilità teoriche.
3. Ogni stato deve contenere un numero sufficiente di osservazioni simulate.
4. La perdita deve essere coerente con il segno dello shock:
   - se $\Delta y>0$, la perdita tende a essere positiva;
   - se $\Delta y<0$, la perdita può essere negativa, cioè un guadagno.
5. La media empirica non condizionata deve essere vicina alla media pesata delle medie condizionate.

### Controlli logici

1. $Z$ non è la perdita: è l’informazione disponibile sul regime.
2. $\Delta y$ non è osservato direttamente al momento della classificazione del regime.
3. $L$ è una variabile casuale derivata da $\Delta y$.
4. $\mathbb{E}[L\mid A_g]$ è un numero.
5. $\mathbb{E}[L\mid\mathcal{G}]$ è una variabile casuale costante su ciascun blocco informativo.

### Controlli interpretativi

1. Il regime di repricing severo deve mostrare una perdita attesa maggiore rispetto agli altri stati.
2. Il regime di disinflazione ordinata può produrre perdita media negativa, cioè guadagno medio da riduzione dei rendimenti.
3. L’informazione $Z$ non elimina l’incertezza, ma modifica la distribuzione condizionata della perdita.
4. Il valore atteso condizionato non è una previsione perfetta, ma una previsione coerente con l’informazione disponibile.
5. Il modello è utile per comprendere la struttura probabilistica del problema, non per produrre una misura regolamentare o una previsione di mercato.

---

## 10. Funzione didattica rispetto ai regimi A/B/C

### Regime A — Ricognizione teorico-modellistica

Nel Regime A lo studente deve identificare:

- grandezze finanziarie;
- variabili casuali;
- eventi;
- stati informativi;
- sigma-algebra generata dagli stati;
- quantità teoriche da stimare;
- ipotesi del modello;
- limiti dell’approssimazione.

L’AI può aiutare a organizzare il ragionamento, ma non deve scegliere autonomamente il modello finale, cambiare la definizione di perdita, introdurre strumenti non ancora trattati o trasformare l’esercizio in un modello avanzato di curva dei tassi.

### Regime B — Traduzione operativa in codice

Nel Regime B l’AI può aiutare a costruire:

- struttura del notebook;
- celle Markdown;
- codice Python per la simulazione;
- tabelle;
- grafici;
- controlli numerici.

La specifica teorica deve però essere già fissata. L’AI non deve modificare $V_0$, $D$, $Z$, $\Delta y$, $L$, le probabilità degli stati, le distribuzioni condizionate o il significato finanziario del problema.

### Regime C — Verifica e interpretazione critica

Nel Regime C lo studente deve verificare:

- coerenza dei risultati numerici;
- correttezza della formula del valore atteso totale;
- significato finanziario delle perdite condizionate;
- ruolo dell’informazione $Z$;
- limiti del modello.

L’AI può intervenire come revisore critico, ma solo su un’interpretazione già formulata dallo studente o dal docente. Non deve produrre l’interpretazione finale al posto dello studente.

---

## 11. Confini del caso

Il caso non tratta:

- pricing obbligazionario completo;
- curva dei rendimenti per scadenza;
- duration key-rate;
- convessità;
- rischio di credito;
- rischio di liquidità;
- modelli dinamici dei tassi;
- dati reali di mercato;
- requisiti regolamentari di rischio di tasso.

Questi elementi possono essere menzionati come limiti o sviluppi successivi, ma non devono entrare nella costruzione operativa della Lezione 04.

---

## 12. Specifica congelata per la progettazione successiva

Per lo sviluppo delle tappe micro, dei prompt virtuosi e del notebook docente, la specifica iniziale del caso aula è la seguente:

$$
V_0=10.000.000,
\qquad
D=6,
\qquad
L=D V_0 \Delta y,
\qquad
\ell=500.000.
$$

Gli stati informativi sono:

$$
A_1=\{\text{disinflazione ordinata}\},
\qquad
A_2=\{\text{inflazione persistente}\},
\qquad
A_3=\{\text{repricing severo}\}.
$$

Le probabilità degli stati sono:

$$
\mathbb{P}(A_1)=0,35,
\qquad
\mathbb{P}(A_2)=0,45,
\qquad
\mathbb{P}(A_3)=0,20.
$$

Le distribuzioni condizionate sono:

$$
\Delta y\mid A_1\sim\mathcal{N}(-0,0010,0,0040^2),
$$

$$
\Delta y\mid A_2\sim\mathcal{N}(0,0030,0,0060^2),
$$

$$
\Delta y\mid A_3\sim\mathcal{N}(0,0100,0,0100^2).
$$

Il numero di simulazioni è:

$$
n=50.000.
$$

Il seme casuale è:

$$
seed=12345.
$$

Questa specifica può essere modificata solo in fase di calibrazione docente, non durante l’interazione ordinaria con l’AI.