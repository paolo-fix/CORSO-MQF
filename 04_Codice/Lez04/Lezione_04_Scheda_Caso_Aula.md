# Lezione 04 — Scheda Caso Aula

## 1. Identificazione del caso

- **Lezione:** Lezione 04 — Applicazione in Python: probabilità, variabili casuali e condizionamento
- **Tipo di caso:** caso aula
- **Titolo:** Perdita obbligazionaria condizionata a regimi di tasso
- **Contesto:** portafoglio obbligazionario a tasso fisso esposto a shock dei rendimenti
- **Uso previsto:** sviluppo guidato in aula, con costruzione progressiva del notebook

Questa Scheda Caso è la specifica operativa del lavoro.

La Scheda Caso deve essere acquisita come vincolante prima di costruire:

1. il Flusso logico-teorico risolutivo;
2. la scomposizione in tappe input-output;
3. le singole celle del notebook;
4. gli output numerici e grafici;
5. l’interpretazione finale.

La Scheda Caso non è una soluzione del problema. Non contiene già svolti il Flusso logico-teorico risolutivo, la scomposizione operativa, il notebook o l’interpretazione finale.

---

## 2. Contesto finanziario

Il caso è ispirato alla fase di rapido rialzo dei tassi osservata nell’area euro nel periodo 2022-2023. Dopo una lunga fase di tassi molto bassi o negativi, l’aumento dell’inflazione ha indotto la Banca Centrale Europea ad alzare progressivamente i tassi di riferimento. Questo cambiamento ha avuto effetti diretti sulla valutazione degli strumenti obbligazionari a tasso fisso.

Quando i rendimenti di mercato aumentano, il prezzo di un’obbligazione a tasso fisso tende a diminuire. L’intensità della variazione dipende, in prima approssimazione, dalla duration modificata del titolo o del portafoglio.

Il caso non ha l’obiettivo di stimare un modello storico dei tassi né di produrre una previsione di mercato. Utilizza una simulazione controllata per rendere osservabile il legame tra:

1. shock di rendimento;
2. perdita obbligazionaria;
3. regimi informativi del mercato dei tassi;
4. distribuzione empirica delle perdite;
5. valori attesi condizionati.

---

## 3. Domanda quantitativa

Si considera un portafoglio obbligazionario semplificato, con valore iniziale $V_0$ e duration modificata $D$.

La variabile casuale rilevante è lo shock di rendimento a un periodo, indicato con $\Delta y$. La perdita approssimata del portafoglio è definita da:

$$
L \simeq D V_0 \Delta y.
$$

Il segno è scelto in modo che uno shock positivo dei rendimenti, $\Delta y>0$, generi una perdita positiva.

La domanda quantitativa è:

$$
\text{Qual è la distribuzione della perdita } L
\text{ e come cambia la perdita attesa condizionando sui diversi regimi di tasso?}
$$

In particolare, si vogliono stimare:

$$
\mathbb{E}[L],
\qquad
\mathbb{P}(L>\ell),
\qquad
q_{\alpha}(L),
\qquad
\mathbb{E}[L\mid A_g],
\qquad
\mathbb{E}[L\mid\mathcal{G}].
$$

---

## 4. Obiettivo didattico

Il caso serve a consolidare, in forma computazionale, i concetti introdotti nelle lezioni teoriche precedenti:

1. spazio di probabilità;
2. eventi;
3. partizioni informative;
4. variabili casuali;
5. distribuzioni condizionate;
6. trasformazioni di variabili casuali;
7. probabilità di superamento soglia;
8. quantili;
9. valore atteso condizionato rispetto a eventi;
10. valore atteso condizionato rispetto alla sigma-algebra generata da una partizione;
11. formula del valore atteso totale.

Dal punto di vista computazionale, il caso introduce una procedura Monte Carlo gerarchica in Python.

Dal punto di vista interpretativo, il caso deve mostrare che l’informazione di regime non elimina l’incertezza, ma modifica la distribuzione rilevante e la perdita attesa condizionata.

---

## 5. Grandezze e oggetti del caso

Le grandezze finanziarie sono:

- $V_0$: valore iniziale del portafoglio obbligazionario;
- $D$: duration modificata del portafoglio;
- $\Delta y$: shock di rendimento a un periodo, espresso in unità decimali;
- $\Delta V$: variazione approssimata del valore del portafoglio;
- $L$: perdita approssimata del portafoglio;
- $\ell$: soglia di perdita rilevante.

La relazione finanziaria di riferimento è l’approssimazione lineare di duration:

$$
\frac{\Delta P}{P} \simeq -D\Delta y.
$$

Per un portafoglio di valore iniziale $V_0$, la variazione approssimata di valore è:

$$
\Delta V \simeq -D V_0 \Delta y.
$$

La perdita è definita come diminuzione del valore del portafoglio:

$$
L=-\Delta V\simeq D V_0 \Delta y.
$$

---

## 6. Partizione informativa

Il caso parte direttamente da una partizione informativa dello spazio degli esiti. Non deve essere introdotta una variabile casuale discreta ausiliaria.

La partizione è:

$$
\Omega=A_1\cup A_2\cup A_3,
\qquad
A_i\cap A_j=\emptyset
\quad \text{per } i\neq j.
$$

Gli eventi $A_1,A_2,A_3$ rappresentano tre regimi informativi del mercato dei tassi.

| Evento | Descrizione | Interpretazione finanziaria |
|---|---|---|
| $A_1$ | Disinflazione ordinata | i rendimenti tendono a muoversi poco o a diminuire moderatamente |
| $A_2$ | Inflazione persistente | i rendimenti tendono ad aumentare in modo moderato |
| $A_3$ | Repricing severo | i rendimenti aumentano in modo marcato e con maggiore volatilità |

La sigma-algebra informativa generata dalla partizione è:

$$
\mathcal{G}=\sigma(A_1,A_2,A_3).
$$

---

## 7. Distribuzioni condizionate

Lo shock di rendimento è una variabile casuale continua:

$$
\Delta y:\Omega\to\mathbb{R}.
$$

Condizionatamente all’evento informativo $A_g$, lo shock segue una distribuzione normale:

$$
\Delta y\mid A_g \sim \mathcal{N}(\mu_g,\sigma_g^2),
\qquad g=1,2,3.
$$

La simulazione Monte Carlo deve quindi seguire uno schema gerarchico:

1. estrarre il regime $A_g$ secondo le probabilità assegnate;
2. estrarre $\Delta y$ dalla distribuzione condizionata al regime estratto;
3. calcolare la perdita $L=D V_0\Delta y$.

La distribuzione non condizionata di $\Delta y$ si ricava dall'insieme delle osservazioni simulate.

---

## 8. Parametri del caso

I parametri sono stilizzati e hanno funzione didattica. Non sono stime storiche e non hanno finalità previsionali.

### Parametri finanziari

| Grandezza | Valore | Unità | Significato |
|---|---:|---|---|
| $V_0$ | 10.000.000 | euro | valore iniziale del portafoglio |
| $D$ | 6 | anni | duration modificata del portafoglio |
| $\ell$ | 500.000 | euro | soglia di perdita rilevante |
| $n$ | 50.000 | simulazioni | dimensione Monte Carlo |
| seed | 12345 | — | seme casuale |

### Probabilità degli eventi informativi

| Evento | Descrizione | Probabilità |
|---|---|---:|
| $A_1$ | Disinflazione ordinata | 0,35 |
| $A_2$ | Inflazione persistente | 0,45 |
| $A_3$ | Repricing severo | 0,20 |

Le probabilità devono sommare a uno.

### Distribuzioni condizionate degli shock di rendimento

| Evento | $\mu_g$ | $\sigma_g$ | Lettura finanziaria |
|---|---:|---:|---|
| $A_1$ | -0,0010 | 0,0040 | lieve riduzione media dei rendimenti |
| $A_2$ | 0,0030 | 0,0060 | rialzo moderato dei rendimenti |
| $A_3$ | 0,0100 | 0,0100 | rialzo marcato e maggiore dispersione |

Tutti gli shock sono espressi in unità decimali. Per esempio, $0,0030$ corrisponde a 30 punti base.

---

## 9. Soglia implicita dello shock di rendimento

La soglia di shock che porta la perdita esattamente a $\ell$ è:

$$
\Delta y^\star
=
\frac{\ell}{D V_0}.
$$

Con i parametri assegnati:

$$
\Delta y^\star
=
\frac{500.000}{6\cdot 10.000.000}
=
0,008333\ldots
$$

cioè circa 83,33 punti base.

Quindi:

$$
L>\ell
\quad\Longleftrightarrow\quad
\Delta y > 0,008333\ldots.
$$

Questa soglia consente di collegare direttamente shock di rendimento, duration, valore del portafoglio e perdita monetaria.

---

## 10. Quantità da stimare o calcolare

Le quantità non condizionate richieste sono:

$$
\mathbb{E}[L],
\qquad
\mathbb{P}(L>\ell),
\qquad
q_{\alpha}(L).
$$

Le quantità condizionate richieste sono:

$$
\mathbb{E}[L\mid A_g],
\qquad g=1,2,3.
$$

Il valore atteso condizionato rispetto alla sigma-algebra informativa è:

$$
\mathbb{E}[L\mid\mathcal{G}]
=
\sum_{g=1}^{3}
\mathbb{E}[L\mid A_g]\mathbf{1}_{A_g}.
$$

La proprietà da verificare è la formula del valore atteso totale:

$$
\mathbb{E}[L]
=
\sum_{g=1}^{3}
\mathbb{P}(A_g)\mathbb{E}[L\mid A_g].
$$

Nel notebook, la controparte empirica sarà:

$$
\widehat{\mathbb{E}}[L]
\approx
\sum_{g=1}^{3}
\widehat{\mathbb{P}}(A_g)
\widehat{\mathbb{E}}[L\mid A_g].
$$

Occorre distinguere chiaramente:

1. $\mathbb{E}[L\mid A_g]$, che è un numero;
2. $\mathbb{E}[L\mid\mathcal{G}]$, che è una variabile casuale costante sui blocchi della partizione;
3. $\mathbb{E}[L]$, che è il valore atteso non condizionato.

---

## 11. Output richiesti

### Tabelle

Devono essere prodotte almeno le seguenti tabelle:

1. tabella dei parametri finanziari;
2. tabella degli eventi $A_1,A_2,A_3$ e delle probabilità;
3. tabella dei parametri condizionati $(\mu_g,\sigma_g)$;
4. tabella delle frequenze simulate degli eventi;
5. tabella di controllo delle statistiche empiriche di $\Delta y\mid A_g$;
6. tabella descrittiva della perdita $L$:
   - media;
   - deviazione standard;
   - minimo;
   - massimo;
   - quantili principali;
7. tabella della probabilità $\widehat{\mathbb{P}}(L>\ell)$;
8. tabella delle medie condizionate:
   - $\widehat{\mathbb{E}}[L\mid A_1]$;
   - $\widehat{\mathbb{E}}[L\mid A_2]$;
   - $\widehat{\mathbb{E}}[L\mid A_3]$;
9. tabella di verifica della formula del valore atteso totale.

È possibile aggiungere una tabella finale con evento simulato, $\Delta y$, $L$ e valore della variabile a gradini $\widehat{\mathbb{E}}[L\mid\mathcal{G}]$.

### Grafici

Devono essere prodotti grafici con funzione interpretativa, non puramente decorativa.

Sono richiesti almeno:

1. istogramma delle frequenze percentuali dello shock di rendimento $\Delta y$;
2. istogramma delle frequenze percentuali della perdita $L$, con evidenza della soglia $\ell$;
3. grafico delle medie condizionate $\widehat{\mathbb{E}}[L\mid A_g]$;
4. confronto tra distribuzioni condizionate della perdita.


---

## 12. Controlli richiesti

### Controlli numerici

Il notebook deve verificare che:

1. le probabilità degli eventi sommino a uno;
2. le frequenze empiriche degli eventi siano coerenti con le probabilità teoriche;
3. le medie e deviazioni standard empiriche di $\Delta y\mid A_g$ siano coerenti con $\mu_g,\sigma_g$;
4. il vettore della perdita abbia dimensione $n$;
5. la perdita rispetti la relazione $L=D V_0\Delta y$;
6. la coerenza dei segni sia rispettata:
   - se $\Delta y>0$, allora $L>0$;
   - se $\Delta y<0$, allora $L<0$;
7. la media globale di $L$ coincida, salvo arrotondamenti, con la media pesata delle medie condizionate;
8. i quantili rispettino l’ordinamento atteso;
9. la media si collochi tra minimo e massimo campionario.

### Controlli logici

Il notebook deve mantenere distinte le seguenti nozioni:

1. gli eventi $A_1,A_2,A_3$ sono blocchi informativi della partizione, non valori di perdita;
2. $\Delta y$ non è la perdita, ma lo shock di rendimento;
3. $L$ è una variabile casuale derivata da $\Delta y$;
4. $\mathbb{E}[L\mid A_g]$ è un numero;
5. $\mathbb{E}[L\mid\mathcal{G}]$ è una variabile casuale costante sui blocchi della partizione;
6. la formula del valore atteso totale non implica che $\mathbb{E}[L]$ ed $\mathbb{E}[L\mid\mathcal{G}]$ coincidano come oggetti;
7. la verifica campionaria della media ricomposta deve essere distinta dalla proprietà teorica.

### Controlli interpretativi

L’interpretazione finale deve rispettare almeno questi punti:

1. l’evento $A_3$ deve essere letto come il regime con perdita attesa maggiore;
2. l’evento $A_1$ può mostrare perdita media negativa, cioè guadagno medio dovuto a riduzione dei rendimenti;
3. l’evento $A_2$ deve rappresentare una situazione intermedia;
4. l’informazione della partizione non elimina l’incertezza, ma modifica la distribuzione condizionata rilevante;
5. la probabilità di superamento della soglia globale deve essere interpretata come probabilità non condizionata;
6. la simulazione non deve essere interpretata come previsione dei tassi.

---

## 13. Ipotesi del modello

### Ipotesi principali

1. Il portafoglio è rappresentato da un valore iniziale $V_0$ e da una duration modificata $D$.
2. La variazione di valore del portafoglio è approssimata linearmente mediante la formula di duration.
3. L’unica fonte di incertezza modellata è lo shock di rendimento $\Delta y$.
4. L’informazione disponibile è rappresentata dalla partizione $\{A_1,A_2,A_3\}$.
5. Condizionatamente a ciascun evento $A_g$, lo shock di rendimento segue una distribuzione normale.
6. Gli eventi $A_1,A_2,A_3$ costituiscono una partizione dello spazio degli esiti.
7. La simulazione Monte Carlo approssima quantità teoriche mediante frequenze e medie empiriche.

### Ipotesi semplificatrici

1. Non si modellano flussi cedolari.
2. Non si modellano scadenze multiple.
3. Non si considera convessità.
4. Non si considera una struttura a termine dei tassi.
5. Non si considerano movimenti non paralleli della curva.
6. Non si considera rischio di credito.
7. Non si considera rischio di liquidità.
8. Non si considera ribilanciamento del portafoglio.
9. Non si considera dinamica multiperiodale.
10. Non si stimano parametri da dati reali.

---

## 14. Uso dell’IA e documentazione del lavoro

Per l’uso dell’IA lo studente deve fare riferimento al documento:

**Istruzioni per lo studente — Uso virtuoso dell’IA nei casi applicativi MQF**

In particolare, devono essere rispettati:

1. la sequenza obbligatoria Prompt zero, Prompt 1, Prompt 2, Prompt 3 e prompt di tappa;
2. la distinzione tra Regime A, Regime B e Regime C nel formulare i prompt;
3. il vincolo che la Scheda Caso non deve essere modificata dall’IA;
4. la necessità di documentare l’interazione con l’IA mediante stampa PDF della chat;
5. l’obbligo di mantenere nella chat solo interazioni pertinenti al caso.

La presente Scheda Caso contiene la specifica vincolante del problema.  
Gli esempi di prompt, i criteri di uso dell’IA e la tabella indicativa di valutazione sono riportati nel documento di istruzioni per lo studente.