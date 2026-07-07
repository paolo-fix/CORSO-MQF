# Lezione 04 — Scheda Costruzione Caso Aula

Documento interno di progettazione del caso applicativo.

La Scheda Costruzione Caso resta nelle mani del docente. Ha funzione creativa primaria e deve essere redatta prima della Scheda Caso, prima della scomposizione in tappe, prima della sequenza dei prompt e prima della costruzione del notebook.

Da questa scheda derivano:

1. la Scheda Caso Aula;
2. il Flusso logico-teorico risolutivo di riferimento;
3. la scomposizione in tappe input-output;
4. la sequenza dei prompt virtuosi;
5. la struttura attesa del notebook;
6. i controlli richiesti;
7. la rubrica di valutazione.

---

## 1. Identificazione del caso

- **Lezione:** Lezione 04 — Applicazione in Python: probabilità, variabili casuali e condizionamento
- **Tipo di caso:** caso aula
- **Titolo:** Perdita obbligazionaria condizionata a regimi di tasso
- **Collocazione nella lezione applicativa:** primo caso applicativo Python del corso
- **Destinatari:** studenti del V anno di Banca e Risk Management
- **Uso previsto:** sviluppo guidato in aula, con supporto dell’IA e costruzione progressiva del notebook

---

## 2. Contesto storico-finanziario, probabilistico o decisionale

Il caso è ispirato alla fase di rapido rialzo dei tassi osservata nell’area euro nel periodo 2022-2023. Dopo una lunga fase di tassi molto bassi o negativi, l’aumento dell’inflazione ha indotto la Banca Centrale Europea ad alzare progressivamente i tassi di riferimento. Questo cambiamento ha avuto effetti diretti sulla valutazione degli strumenti obbligazionari a tasso fisso.

Quando i rendimenti di mercato aumentano, il prezzo di un’obbligazione a tasso fisso tende a diminuire. L’intensità della variazione dipende, in prima approssimazione, dalla duration modificata del titolo o del portafoglio.

Il caso non ha l’obiettivo di stimare un modello storico dei tassi né di produrre una previsione di mercato. Utilizza invece una simulazione controllata, ispirata a un contesto finanziario realistico, per rendere osservabile il legame tra:

1. shock di rendimento;
2. perdita di valore di un portafoglio obbligazionario;
3. regimi informativi del mercato dei tassi;
4. distribuzione empirica delle perdite;
5. valori attesi condizionati.

Il caso è rilevante per studenti di Banca e Risk Management perché collega un concetto finanziario familiare, la sensitivity obbligazionaria ai tassi, con gli strumenti probabilistici introdotti nelle prime lezioni del corso.

---

## 3. Domanda quantitativa e obiettivo didattico

### Domanda quantitativa

Si considera un portafoglio obbligazionario semplificato, con valore iniziale $V_0$ e duration modificata $D$.

La variabile casuale rilevante è lo shock di rendimento a un periodo, indicato con $\Delta y$. La perdita approssimata del portafoglio è definita da:

$$
L = D V_0 \Delta y.
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

### Obiettivo didattico

Il caso deve consolidare:

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

Dal punto di vista computazionale, il caso deve introdurre una prima procedura Monte Carlo controllata in Python, con costruzione di dataset simulati, tabelle, grafici e controlli.

Dal punto di vista interpretativo, il caso deve mostrare che l’informazione di regime non elimina l’incertezza, ma modifica la distribuzione rilevante e la perdita attesa condizionata.

---

## 4. Funzione del caso nella lezione applicativa

### Concetti teorici da rendere osservabili

Il caso aula deve rendere osservabili, mediante simulazione, i seguenti concetti:

1. partizione dello spazio degli esiti;
2. sigma-algebra generata da una partizione;
3. distribuzione condizionata;
4. variabile casuale derivata;
5. distribuzione empirica;
6. probabilità di superamento soglia;
7. quantili empirici;
8. valore atteso condizionato rispetto a eventi;
9. valore atteso condizionato rispetto alla sigma-algebra informativa;
10. formula del valore atteso totale.

### Funzione della simulazione

La simulazione Monte Carlo consente di costruire artificialmente un campione di scenari di mercato coerente con una specifica teorica fissata.

La finalità non è produrre una previsione dei tassi, ma mostrare come una struttura probabilistica condizionata si traduca in:

1. osservazioni simulate;
2. distribuzioni empiriche;
3. medie e quantili;
4. probabilità di superamento soglia;
5. valori attesi condizionati;
6. controlli di coerenza.

### Ruolo dell’informazione condizionante

L’informazione condizionante è rappresentata da una partizione dello spazio degli esiti:

$$
\Omega=A_1\cup A_2\cup A_3,
\qquad
A_i\cap A_j=\emptyset
\quad \text{per } i\neq j.
$$

Gli eventi $A_1,A_2,A_3$ rappresentano tre regimi informativi del mercato dei tassi.

Condizionare su tale partizione significa sostituire una valutazione globale della perdita con valutazioni specifiche per regime.

### Prodotto computazionale finale

Il prodotto finale è un notebook Jupyter che produce:

1. simulazione degli eventi della partizione;
2. simulazione degli shock di rendimento condizionati agli eventi;
3. calcolo della perdita obbligazionaria;
4. distribuzione empirica della perdita;
5. stime di media, quantili e probabilità di superamento soglia;
6. valori attesi condizionati per regime;
7. verifica empirica della formula del valore atteso totale;
8. interpretazione critica del ruolo dell’informazione di scenario.

---

## 5. Specifica teorico-matematica del caso

### Grandezze e oggetti del caso

Le grandezze finanziarie sono:

- $V_0$: valore iniziale del portafoglio obbligazionario;
- $D$: duration modificata del portafoglio;
- $\Delta y$: shock di rendimento a un periodo, espresso in unità decimali;
- $\Delta V$: variazione approssimata del valore del portafoglio;
- $L$: perdita approssimata del portafoglio;
- $\ell$: soglia di perdita rilevante.

### Partizione informativa

Il caso non richiede l’introduzione di una variabile casuale discreta ausiliaria. Si parte direttamente da una partizione informativa dello spazio degli esiti:

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

### Variabili casuali

Lo shock di rendimento è una variabile casuale continua:

$$
\Delta y:\Omega\to\mathbb{R}.
$$

Condizionatamente all’evento informativo $A_g$, lo shock segue una distribuzione normale:

$$
\Delta y\mid A_g \sim \mathcal{N}(\mu_g,\sigma_g^2),
\qquad g=1,2,3.
$$

La relazione finanziaria fondamentale è l’approssimazione lineare di duration:

$$
\frac{\Delta P}{P} \simeq -D\Delta y.
$$

Per un portafoglio di valore iniziale $V_0$, la variazione approssimata di valore è:

$$
\Delta V \simeq -D V_0 \Delta y.
$$

La perdita, definita come diminuzione del valore del portafoglio, è:

$$
L=-\Delta V\simeq D V_0 \Delta y.
$$

### Quantità teoriche da stimare o calcolare

Le quantità principali sono:

$$
\mathbb{E}[L],
\qquad
\mathbb{P}(L>\ell),
\qquad
q_{\alpha}(L).
$$

Le quantità condizionate sono:

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

## 6. Specifica parametrica iniziale

I parametri seguenti sono stilizzati e hanno funzione didattica. Non sono stime storiche e non hanno finalità previsionali.

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

### Distribuzioni condizionate degli shock di rendimento

| Evento | $\mu_g$ | $\sigma_g$ | Lettura finanziaria |
|---|---:|---:|---|
| $A_1$ | -0,0010 | 0,0040 | lieve riduzione media dei rendimenti |
| $A_2$ | 0,0030 | 0,0060 | rialzo moderato dei rendimenti |
| $A_3$ | 0,0100 | 0,0100 | rialzo marcato e maggiore dispersione |

Tutti gli shock sono espressi in unità decimali. Per esempio, $0,0030$ corrisponde a 30 punti base.

### Soglia implicita dello shock di rendimento

La soglia di shock che porta la perdita esattamente a $\ell$ è:

$$
\Delta y^\star
=
\frac{\ell}{D V_0}.
$$

Con i parametri proposti:

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

Questa soglia ha funzione didattica: consente di collegare direttamente shock di rendimento, duration, valore del portafoglio e perdita monetaria.

### Vincoli di calibrazione

Il caso è calibrato in modo da produrre:

1. perdita media contenuta o negativa in $A_1$;
2. perdita media positiva e moderata in $A_2$;
3. perdita media elevata e maggiore dispersione in $A_3$;
4. probabilità non trascurabile di superamento della soglia $\ell$;
5. differenze visibili tra media non condizionata e medie condizionate;
6. verifica empirica stabile della formula del valore atteso totale.

---

## 7. Ipotesi modellistiche e limiti

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

### Aspetti esclusi dal modello

Il caso non tratta:

1. pricing obbligazionario completo;
2. curva dei rendimenti per scadenza;
3. duration key-rate;
4. convessità;
5. rischio di credito;
6. rischio di liquidità;
7. modelli dinamici dei tassi;
8. dati reali di mercato;
9. requisiti regolamentari di rischio di tasso.

### Limiti da dichiarare nell’interpretazione

Il modello è utile per comprendere il ruolo dell’informazione condizionante e della distribuzione condizionata della perdita, ma non produce una misura gestionale completa del rischio di tasso.

In particolare, non è un modello completo di pricing obbligazionario, non è una procedura di misurazione regolamentare del rischio di tasso, non incorpora convessità e non descrive la dinamica della curva dei rendimenti.

L’uso di distribuzioni normali per gli shock di rendimento è una semplificazione didattica. La simulazione non deve essere interpretata come previsione di mercato.

---

## 8. Output richiesti

### Tabelle

1. Tabella dei parametri finanziari.
2. Tabella degli eventi $A_1,A_2,A_3$ e delle probabilità.
3. Tabella dei parametri condizionati $(\mu_g,\sigma_g)$.
4. Tabella delle frequenze simulate degli eventi.
5. Tabella di controllo delle statistiche empiriche di $\Delta y\mid A_g$.
6. Tabella descrittiva della perdita $L$:
   - media;
   - deviazione standard;
   - minimo;
   - massimo;
   - quantili principali.
7. Tabella della probabilità $\widehat{\mathbb{P}}(L>\ell)$.
8. Tabella delle medie condizionate:
   - $\widehat{\mathbb{E}}[L\mid A_1]$;
   - $\widehat{\mathbb{E}}[L\mid A_2]$;
   - $\widehat{\mathbb{E}}[L\mid A_3]$.
9. Tabella di verifica della formula del valore atteso totale.
10. Eventuale tabella finale con evento simulato, $\Delta y$, $L$ e valore della variabile a gradini $\widehat{\mathbb{E}}[L\mid\mathcal{G}]$.

### Grafici

1. Istogramma o densità empirica dello shock di rendimento $\Delta y$.
2. Istogramma o densità empirica della perdita $L$.
3. Grafico della distribuzione empirica di $L$ con evidenza della soglia $\ell$.
4. Grafico delle medie condizionate $\widehat{\mathbb{E}}[L\mid A_g]$.
5. Confronto tra distribuzioni condizionate della perdita.
6. Eventuale confronto tra distribuzioni condizionate dello shock $\Delta y$.
7. Eventuale ECDF della perdita.

### Stime, indicatori o quantità numeriche

1. $\widehat{\mathbb{E}}[L]$.
2. $\widehat{\mathbb{P}}(L>\ell)$.
3. Quantili empirici di $L$.
4. $\widehat{\mathbb{E}}[L\mid A_g]$ per $g=1,2,3$.
5. Verifica empirica della media ricomposta:
   $$
   \sum_{g=1}^{3}
   \widehat{\mathbb{P}}(A_g)
   \widehat{\mathbb{E}}[L\mid A_g].
   $$

### Controlli numerici

1. Le probabilità degli eventi devono sommare a uno.
2. Le frequenze empiriche degli eventi devono essere vicine alle probabilità teoriche.
3. Ogni evento deve avere numerosità sufficiente.
4. Le medie e deviazioni standard empiriche di $\Delta y\mid A_g$ devono essere coerenti con $\mu_g,\sigma_g$.
5. Il vettore della perdita deve avere dimensione $n$.
6. La perdita deve rispettare la relazione $L=D V_0\Delta y$.
7. La coerenza dei segni deve essere verificata:
   - se $\Delta y>0$, allora $L>0$;
   - se $\Delta y<0$, allora $L<0$.
8. La media globale di $L$ deve coincidere, salvo arrotondamenti, con la media pesata delle medie condizionate.
9. I quantili devono rispettare l’ordinamento atteso.
10. La media deve collocarsi tra minimo e massimo campionario.

### Controlli logici

1. Gli eventi $A_1,A_2,A_3$ sono blocchi informativi della partizione, non valori di perdita.
2. $\Delta y$ non è la perdita: è lo shock di rendimento.
3. $L$ è una variabile casuale derivata da $\Delta y$.
4. $\mathbb{E}[L\mid A_g]$ è un numero.
5. $\mathbb{E}[L\mid\mathcal{G}]$ è una variabile casuale costante sui blocchi della partizione.
6. La formula del valore atteso totale non implica che $\mathbb{E}[L]$ ed $\mathbb{E}[L\mid\mathcal{G}]$ coincidano come oggetti.
7. La verifica campionaria della media ricomposta deve essere distinta dalla proprietà teorica.

### Controlli interpretativi

1. L’evento $A_3$ deve mostrare perdita attesa maggiore rispetto agli altri eventi.
2. L’evento $A_1$ può mostrare perdita media negativa, cioè guadagno medio dovuto a riduzione dei rendimenti.
3. L’evento $A_2$ deve rappresentare una situazione intermedia.
4. L’informazione della partizione non elimina l’incertezza, ma modifica la distribuzione condizionata rilevante.
5. La probabilità di superamento della soglia globale deve essere interpretata come media non condizionata, non come probabilità valida in ogni regime.
6. La simulazione non deve essere interpretata come previsione dei tassi.

---

## 9. Flusso logico-teorico risolutivo

Questa sezione costituisce il cuore intellettuale del caso.

Il suo compito non è descrivere il codice, né anticipare la scomposizione operativa del notebook, ma ricostruire la sequenza dei richiami teorico-matematici necessari per passare dalla domanda quantitativa agli output richiesti.

## 9. Flusso logico-teorico risolutivo

Questa sezione costituisce il cuore intellettuale del caso.

Il suo compito non è descrivere il codice, né anticipare la scomposizione operativa del notebook, ma ricostruire la sequenza dei richiami teorico-matematici necessari per passare dalla domanda quantitativa agli output richiesti.

| Passo | Finalità risolutiva | Formula teorico-matematica / definizione / proprietà / teorema | Applicazione nel caso | Output o controllo collegato |
|---:|---|---|---|---|
| 1 | Identificare la variabile finanziaria finale e il legame con il fattore di rischio | Approssimazione lineare di duration: \(L=D V_0\Delta y\) | La perdita \(L\) è la variabile casuale derivata dallo shock di rendimento \(\Delta y\). Uno shock positivo dei rendimenti produce una perdita positiva. | Formula da implementare; controllo della relazione \(L=D V_0\Delta y\); controllo dei segni. |
| 2 | Definire la soglia di rischio e tradurla nel fattore di rischio | Evento di superamento soglia: \(\{L>\ell\}\); equivalenza \(L>\ell \Longleftrightarrow \Delta y>\ell/(D V_0)\) | La soglia monetaria \(\ell\) viene letta anche come soglia implicita sullo shock di rendimento. | Calcolo di \(\Delta y^\star=\ell/(D V_0)\); output \(\widehat{\mathbb{P}}(L>\ell)\). |
| 3 | Rappresentare l’informazione di scenario | Partizione di \(\Omega\): \(\Omega=A_1\cup A_2\cup A_3\), \(A_i\cap A_j=\emptyset\); probabilità \(p_g=\mathbb{P}(A_g)\), \(\sum_g p_g=1\) | I tre eventi rappresentano i regimi di tasso e le loro probabilità guidano l’estrazione Monte Carlo del regime. | Tabella degli eventi e delle probabilità; controllo \(\sum_g p_g=1\); frequenze empiriche \(\widehat{\mathbb{P}}(A_g)\). |
| 4 | Specificare il comportamento del fattore di rischio nei diversi regimi | Distribuzione condizionata: \(\Delta y\mid A_g\sim\mathcal{N}(\mu_g,\sigma_g^2)\) | Ogni regime genera shock di rendimento con media e volatilità diverse. | Tabella dei parametri \((\mu_g,\sigma_g)\); controllo di media e deviazione standard empiriche per regime. |
| 5 | Costruire la distribuzione non condizionata tramite simulazione gerarchica | Formula di miscela e campionamento gerarchico: prima \(A_g\), poi \(\Delta y\mid A_g\) | La distribuzione globale di \(\Delta y\) nasce dalla combinazione tra probabilità dei regimi e distribuzioni condizionate. | Dataset simulato con evento e \(\Delta y\); controllo frequenze dei regimi; controllo degli shock condizionati. |
| 6 | Trasformare gli shock simulati in perdite simulate | Trasformazione di variabile casuale: \(L_i=D V_0\Delta y_i\) | Ogni shock simulato viene trasformato nella perdita obbligazionaria corrispondente. | Dataset con evento, \(\Delta y\), \(L\); controllo formula-codice; controllo dimensione \(n\). |
| 7 | Produrre la lettura non condizionata del rischio | Distribuzione empirica, media, quantili, probabilità di superamento soglia | Si analizza la distribuzione globale della perdita senza distinguere i regimi. | \(\widehat{\mathbb{E}}[L]\), quantili empirici, \(\widehat{\mathbb{P}}(L>\ell)\), grafici della distribuzione di \(L\). |
| 8 | Produrre la lettura condizionata per regime | Valore atteso condizionato rispetto a un evento: \(\mathbb{E}[L\mid A_g]\) | Si confronta la perdita attesa nei tre regimi di tasso. | Tabella delle medie condizionate \(\widehat{\mathbb{E}}[L\mid A_g]\); grafico delle medie condizionate. |
| 9 | Collegare l’informazione disponibile al valore atteso condizionato | Valore atteso condizionato rispetto alla sigma-algebra: \(\mathbb{E}[L\mid\mathcal{G}]=\sum_g \mathbb{E}[L\mid A_g]\mathbf{1}_{A_g}\) | La previsione condizionata diventa una variabile casuale costante sui blocchi della partizione. | Eventuale colonna \(\widehat{\mathbb{E}}[L\mid\mathcal{G}]\); distinzione tra numero condizionato e variabile casuale a gradini. |
| 10 | Verificare la coerenza complessiva e interpretare il ruolo dell’informazione | Formula del valore atteso totale: \(\mathbb{E}[L]=\sum_g\mathbb{P}(A_g)\mathbb{E}[L\mid A_g]\); interpretazione del condizionamento | La media globale viene ricostruita come media pesata delle medie di regime. L’informazione modifica la distribuzione rilevante, ma non elimina l’incertezza. | Controllo tra media campionaria e media ricomposta; commento finale su regimi, perdita attesa, soglia e limiti del modello. |

La sequenza del Flusso logico-teorico risolutivo deve guidare la successiva scomposizione in tappe input-output. Le tappe operative non devono nascere direttamente dal codice, ma dalla successione teorica fissata in questa tabella.

---

## 10. Scomposizione attesa in tappe input-output

La scomposizione in tappe traduce il Flusso logico-teorico risolutivo in una sequenza operativa.

Ogni tappa deve avere un input osservabile, un’operazione definita, un output controllabile e un uso nella tappa successiva.

| Tappa | Titolo | Input | Operazione | Output | Controllo | Uso successivo | Regime IA |
|---:|---|---|---|---|---|---|---|
| 1 | Specifica teorica e parametri | Scheda Caso, $V_0,D,\ell,n,seed$ | definizione di grandezze, partizione informativa, variabili e parametri | tabelle parametri e oggetti Python | somma probabilità; soglia implicita $\Delta y^\star$ | simulazione degli eventi informativi | A/B |
| 2 | Simulazione della partizione informativa | probabilità di $A_1,A_2,A_3$, $n$, seed | assegnazione di ciascuna simulazione a uno dei tre eventi della partizione | vettore di etichette $A_1,A_2,A_3$ e frequenze empiriche | frequenze vicine alle probabilità teoriche; assenza di etichette non ammesse | simulazione condizionata di $\Delta y$ | B |
| 3 | Simulazione di $\Delta y\mid A_g$ e perdita $L$ | etichette degli eventi, parametri $(\mu_g,\sigma_g)$, $V_0,D$ | simulazione degli shock e calcolo della perdita | dataset con evento, $\Delta y$, $L$ | dimensioni; coerenza del segno tra $\Delta y$ e $L$ | distribuzione empirica | B |
| 4 | Distribuzione empirica e rischio non condizionato | vettore $L$, soglia $\ell$ | statistiche descrittive, quantili, probabilità $L>\ell$ | tabelle e grafici globali | ordine dei quantili; media compresa tra minimo e massimo; coerenza della probabilità | confronto con analisi condizionata | B/C |
| 5 | Valori attesi condizionati e valore atteso totale | dataset con evento e $L$ | medie condizionate per blocco e media pesata | tabella $\widehat{\mathbb{E}}[L\mid A_g]$, verifica della media totale, eventuale colonna $\widehat{\mathbb{E}}[L\mid\mathcal{G}]$ | differenza tra media globale e media ricomposta; distinzione tra numero e variabile casuale a gradini | interpretazione critica | B/C |
| 6 | Interpretazione critica e limiti | output delle tappe precedenti | commento autonomo su ruolo dell’informazione, rischio residuo e limiti del modello | sezione finale del notebook | non confondere condizionamento con eliminazione del rischio; non sovrainterpretare la simulazione | chiusura del lavoro | C |

---

## 11. Sequenza docente dei prompt virtuosi

La sequenza dei prompt virtuosi descrive il modo in cui il caso aula può essere sviluppato passo passo con supporto dell’IA, mantenendo il controllo del docente su specifica teorica, scomposizione, codice, output, controlli e interpretazione.

La sequenza è costruita a partire dalla Scheda Caso validata. L’IA non deve modificare la partizione informativa, le grandezze finanziarie, le formule, i parametri, la soglia o gli output richiesti.

La sequenza deve partire da:

1. Prompt zero;
2. Prompt 1 — acquisizione non produttiva della Scheda Caso;
3. Prompt 2 — costruzione del Flusso logico-teorico risolutivo;
4. prompt di tappa.

### 11.1 Mappa sintetica dei prompt

| Prompt / gruppo di prompt | Tappa o fase collegata | Regime IA | Output richiesto | Destinazione nel notebook / tracciato |
|---:|---|---|---|---|
| 0 | Inizializzazione generale | — | conferma minima di comprensione dei vincoli generali | tracciato IA |
| 1 | Acquisizione della Scheda Caso Aula | — | conferma minima: “OK, scheda acquisita” | tracciato IA |
| 2 | Flusso logico-teorico risolutivo | A | tabella del flusso logico-teorico | tracciato IA; base per la scomposizione |
| 3 | Scomposizione del caso in tappe input-output | A | proposta di scomposizione in tappe | tracciato IA; sezione di struttura del notebook |
| 4 | Validazione della scomposizione | C | verifica di completezza, coerenza e assenza di salti logici | tracciato IA |
| 5 | Tappa 1 — Specifica teorica e parametri | B | celle Markdown e codice per parametri, probabilità, soglia implicita e controlli iniziali | notebook |
| 6 | Tappa 2 — Simulazione della partizione informativa | B | celle Markdown e codice per assegnare le simulazioni agli eventi $A_1,A_2,A_3$ | notebook |
| 7 | Tappa 3 — Simulazione di $\Delta y\mid A_g$ e perdita $L$ | B | celle Markdown e codice per simulare $\Delta y$, calcolare $L$ e costruire il dataset | notebook |
| 8 | Tappa 4 — Analisi non condizionata della perdita | B/C | tabelle, grafici e controlli su distribuzione empirica, quantili e soglia | notebook |
| 9 | Tappa 5 — Analisi condizionata e valore atteso totale | B/C | medie condizionate, variabile a gradini, verifica della formula del valore atteso totale | notebook |
| 10 | Tappa 6 — Interpretazione critica | C | revisione critica di una bozza interpretativa del docente | notebook; tracciato IA |
| 11 | Controllo finale del tracciato IA | C | checklist di completezza del tracciato | file `.md` finale |

### 11.2 Input forniti all’IA ed esempio di formulazione

| Prompt / gruppo di prompt | Tappa o fase collegata | Input fornito all’IA | Esempio sintetico di input/prompt |
|---:|---|---|---|
| 0 | Inizializzazione generale | Regole generali del corso MQF, distinzione tra notebook e tracciato IA, regimi A/B/C, divieto di anticipare contenuti non richiesti. Il caso specifico non viene ancora fornito. | Sto sviluppando un caso applicativo del corso MQF. Per ora devi solo acquisire i vincoli generali: Regime A per ricognizione teorico-modellistica, Regime B per traduzione operativa in codice, Regime C per verifica critica. Non produrre contenuti, formule, codice, esempi o piani di lavoro. Conferma soltanto di avere compreso. |
| 1 | Acquisizione della Scheda Caso Aula | Scheda Caso Aula completa. L’IA deve solo acquisirla come specifica vincolante. | Ti fornisco la Scheda Caso Aula. Devi soltanto leggerla e acquisirla come specifica vincolante del lavoro. Non devi produrre sintesi, formule aggiuntive, codice, tappe operative, interpretazioni, controlli o suggerimenti. Rispondi soltanto “OK, scheda acquisita” se tutto è chiaro. |
| 2 | Flusso logico-teorico risolutivo | Scheda Caso acquisita e contributo teorico iniziale del docente o dello studente. | Regime A. Sulla base della Scheda Caso acquisita, devo costruire il Flusso logico-teorico risolutivo. Secondo me gli elementi teorici necessari, nell’ordine logico utile alla soluzione, sono: [elenco iniziale]. Aiutami a verificare, completare e ordinare questa sequenza, senza scrivere codice e senza proporre ancora la scomposizione operativa del notebook. |
| 3 | Scomposizione del caso in tappe input-output | Scheda Caso, flusso logico-teorico validato, output richiesti, controlli obbligatori. | Scomponi il caso in tappe input-output. Per ogni tappa indica input, operazione, output, controllo, uso nella tappa successiva e regime IA prevalente. Non scrivere codice, non calcolare risultati e non modificare la specifica del caso. |
| 4 | Validazione della scomposizione | Scomposizione proposta, Scheda Caso, flusso logico-teorico validato, lista degli output richiesti e controlli obbligatori. | Verifica se la scomposizione copre tutti gli output richiesti, se ogni tappa ha input e output osservabili, e se gli output vengono riutilizzati correttamente. Non riscrivere integralmente la scomposizione: segnala solo correzioni necessarie. |
| 5 | Tappa 1 — Specifica teorica e parametri | Specifica teorica validata, parametri $V_0,D,\ell,n,seed$, probabilità degli eventi, parametri condizionati $(\mu_g,\sigma_g)$, soglia implicita $\Delta y^\star$ da calcolare. | Produci per la Tappa 1 una cella Markdown e una cella Python. Il Markdown deve spiegare grandezze, parametri e partizione informativa. Il codice deve definire i parametri, produrre le tabelle iniziali, controllare la somma delle probabilità e calcolare la soglia implicita di shock associata a $L>\ell$. |
| 6 | Tappa 2 — Simulazione della partizione informativa | Probabilità di $A_1,A_2,A_3$, numero di simulazioni $n$, seed, etichette degli eventi. La specifica non prevede una variabile teorica ausiliaria. | Produci Markdown e codice per assegnare ciascuna simulazione a uno degli eventi $A_1,A_2,A_3$. Non introdurre una variabile teorica discreta aggiuntiva. Nel codice puoi usare un vettore di etichette operative. Produci frequenze empiriche e controlli sugli scostamenti dalle probabilità teoriche. |
| 7 | Tappa 3 — Simulazione di $\Delta y\mid A_g$ e perdita $L$ | Etichette operative degli eventi, parametri condizionati $(\mu_g,\sigma_g)$, formula $L=D V_0\Delta y$. | Produci Markdown e codice per simulare $\Delta y\mid A_g$, calcolare $L$ e costruire il dataset principale. Mantieni la formula fissata. Inserisci controlli su dimensioni, coerenza dei segni e relazione $L=D V_0\Delta y$. |
| 8 | Tappa 4 — Analisi non condizionata della perdita | Dataset con evento, $\Delta y$, $L$; soglia $\ell$; livelli di quantile; output richiesti per analisi globale. | Produci Markdown e codice per stimare la distribuzione empirica della perdita $L$: media, deviazione standard, minimo, massimo, quantili e $\widehat{\mathbb{P}}(L>\ell)$. Produci grafici che evidenzino la soglia di perdita. Inserisci controlli su quantili, probabilità e posizione della media. |
| 9 | Tappa 5 — Analisi condizionata e valore atteso totale | Dataset con evento e $L$, frequenze empiriche, media globale, definizione di $\mathcal{G}=\sigma(A_1,A_2,A_3)$, distinzione tra $\mathbb{E}[L\mid A_g]$ e $\mathbb{E}[L\mid\mathcal{G}]$. | Produci Markdown e codice per calcolare $\widehat{\mathbb{E}}[L\mid A_g]$, costruire se utile la variabile a gradini $\widehat{\mathbb{E}}[L\mid\mathcal{G}]$ e verificare la formula del valore atteso totale. Distingui chiaramente numero condizionato, variabile casuale condizionata e media globale. |
| 10 | Tappa 6 — Interpretazione critica | Bozza interpretativa basata sugli output delle tappe precedenti: distribuzione di $L$, medie condizionate, ruolo della partizione, limiti dell’approssimazione lineare. | Ho scritto questa interpretazione. Segnala errori, ambiguità, affermazioni troppo forti, confusioni tra quantità teoriche e stime empiriche, e limiti mancanti. Non riscrivere integralmente la conclusione e non sostituirti a me. |
| 11 | Controllo finale del tracciato IA | Tracciato IA compilato, elenco dei prompt, regimi dichiarati, decisioni, collegamenti alle sezioni del notebook, output e controlli. | Controlla se il tracciato documenta prompt, regime, risposta utilizzata, decisione presa, output prodotto e controllo svolto. Non valutare la qualità intrinseca delle risposte IA: valuta solo completezza, coerenza e tracciabilità del processo. |

---

## 12. Struttura attesa del notebook

La struttura attesa del notebook deve derivare dalla scomposizione in tappe.

| Sezione | Titolo della sezione notebook | Tappa o fase collegata | Prompt / gruppo di prompt di riferimento | Tipo cella | Contenuto e output attesi |
|---:|---|---|---|---|---|
| 1 | Titolo, contesto e domanda quantitativa | Acquisizione del caso | 1 | Markdown | Presenta il caso aula, il contesto obbligazionario, la domanda quantitativa e il ruolo dell’informazione rappresentata dalla partizione $A_1,A_2,A_3$. Deve chiarire che il caso è simulativo e non previsionale. |
| 2 | Flusso logico-teorico risolutivo | Prompt 2 | 2 | Markdown | Riporta la tabella del Flusso logico-teorico risolutivo validata. Deve distinguere richiami teorici, applicazione nel caso e output collegati. |
| 3 | Scomposizione del lavoro in tappe | Scomposizione e validazione | 3-4 | Markdown | Riporta la sequenza validata delle tappe input-output. Per ogni tappa indica input, operazione, output, controllo e uso nella tappa successiva. |
| 4 | Parametri finanziari e probabilistici | Tappa 1 | 5 | Markdown + codice | Definisce parametri finanziari, probabilità degli eventi e parametri condizionati $(\mu_g,\sigma_g)$. Produce tabelle dei parametri e controlli iniziali: somma probabilità e soglia implicita $\Delta y^\star$. |
| 5 | Simulazione della partizione informativa | Tappa 2 | 6 | Markdown + codice | Assegna ogni simulazione a uno dei tre eventi $A_1,A_2,A_3$. Produce tabella di frequenze empiriche, confronto con probabilità teoriche e controllo di assenza di etichette non ammesse. |
| 6 | Simulazione degli shock di rendimento | Tappa 3 | 7 | Markdown + codice | Simula $\Delta y\mid A_g$ usando i parametri condizionati. Produce una tabella di controllo per evento con media e deviazione standard empiriche di $\Delta y$, da confrontare con $\mu_g$ e $\sigma_g$. |
| 7 | Calcolo della perdita obbligazionaria | Tappa 3 | 7 | Markdown + codice | Calcola $L=D V_0\Delta y$ e costruisce il dataset con evento, $\Delta y$ e $L$. Include controlli su dimensione, relazione formula-codice e coerenza dei segni. |
| 8 | Analisi non condizionata della perdita | Tappa 4 | 8 | Markdown + codice | Produce statistiche descrittive di $L$, quantili e $\widehat{\mathbb{P}}(L>\ell)$. Include grafico della distribuzione di $L$ con evidenza della soglia $\ell$. |
| 9 | Analisi condizionata per evento | Tappa 5 | 9 | Markdown + codice | Calcola $\widehat{\mathbb{E}}[L\mid A_1]$, $\widehat{\mathbb{E}}[L\mid A_2]$, $\widehat{\mathbb{E}}[L\mid A_3]$, frequenze empiriche e distribuzioni condizionate. Produce tabella e grafico delle medie condizionate. |
| 10 | Valore atteso condizionato rispetto a $\mathcal{G}$ e valore atteso totale | Tappa 5 | 9 | Markdown + codice | Costruisce, se utile, una colonna con la variabile a gradini $\widehat{\mathbb{E}}[L\mid\mathcal{G}]$. Verifica la ricomposizione della media globale mediante frequenze empiriche e medie condizionate. Deve distinguere tra verifica campionaria e proprietà teorica. |
| 11 | Interpretazione critica dei risultati | Tappa 6 | 10 | Markdown | Contiene commento autonomo sul ruolo della partizione informativa, sulla differenza tra analisi globale e condizionata, sulla perdita attesa nei diversi eventi e sul significato della soglia. |
| 12 | Limiti del modello e sintesi finale | Tappa 6 / controllo finale | 10-11 | Markdown | Dichiara i limiti: approssimazione lineare di duration, assenza di convessità, assenza di curva dei rendimenti, assenza di rischio di credito, assenza di dati reali. Chiude con una sintesi proporzionata agli output simulati. |

---

## 13. Criteri di validazione del notebook

Il notebook è accettabile se:

1. implementa la specifica teorica senza modificarla;
2. parte direttamente dalla partizione $A_1,A_2,A_3$ senza introdurre una variabile teorica ausiliaria non necessaria;
3. mantiene distinti eventi informativi, shock di rendimento e perdita;
4. simula correttamente l’assegnazione delle osservazioni ai tre eventi della partizione;
5. simula $\Delta y\mid A_g$ con parametri coerenti;
6. costruisce $L$ secondo la formula fissata;
7. produce tabelle e grafici leggibili;
8. include controlli numerici e logici;
9. verifica la formula del valore atteso totale;
10. contiene un’interpretazione critica autonoma;
11. dichiara i limiti del modello.

Il notebook non è accettabile se:

1. modifica il modello senza dichiararlo;
2. sostituisce $L=D V_0\Delta y$ con una perdita diversa;
3. interpreta gli eventi $A_g$ come valori di perdita o shock;
4. usa dati reali non richiesti;
5. introduce modelli di curva dei tassi, convessità, key-rate duration o dinamiche multiperiodali;
6. presenta output senza controlli;
7. delega l’interpretazione finale all’IA.

---

## 14. Criteri di valutazione del tracciato IA

Il tracciato IA è valutato come documento metodologico.

La valutazione riguarda il modo in cui l’IA viene usata nel processo di costruzione del lavoro, non la qualità intrinseca delle risposte prodotte dall’IA.

Sono elementi da valutare:

1. correttezza del Prompt zero;
2. acquisizione non produttiva della Scheda Caso tramite Prompt 1;
3. qualità del contributo iniziale al Prompt 2;
4. qualità del Flusso logico-teorico risolutivo finale;
5. rispetto dei regimi A/B/C;
6. qualità dei prompt di tappa;
7. validazione delle risposte IA;
8. correzione di errori, ambiguità o modifiche non autorizzate;
9. collegamento tra prompt, notebook e output;
10. autonomia dell’interpretazione finale.

Nel Prompt 2 il docente valuta in modo specifico quanto il Flusso logico-teorico risolutivo finale derivi da una proposta teorica iniziale autonoma e quanto invece sia stato completato dall’IA.

---

## 15. Rubrica sintetica

| Area | Peso | Criteri |
|---|---:|---|
| Premesse teorico-matematiche | 15 | corretta identificazione di partizione $A_1,A_2,A_3$, $\Delta y$, $L$, $\mathcal{G}$, ipotesi e quantità teoriche |
| Flusso logico-teorico risolutivo | 15 | sequenza teorica coerente, uso corretto di definizioni, proprietà e formule, collegamento con output e controlli |
| Scomposizione input-output | 15 | tappe coerenti, output riutilizzati, controlli previsti, assenza di salti logici |
| Notebook e output computazionali | 20 | codice corretto, simulazioni, tabelle, grafici, riproducibilità, struttura ordinata del notebook |
| Prompt e rispetto dei regimi A/B/C | 15 | qualità degli input, vincoli, validazioni, uso corretto dei regimi, collegamento prompt-notebook |
| Controlli numerici e logici | 10 | probabilità, frequenze, $\Delta y\mid A_g$, formula $L=D V_0\Delta y$, verifica valore atteso totale |
| Interpretazione critica | 10 | ruolo dell’informazione, perdita condizionata, soglia, limiti del modello, autonomia del commento finale |

---

## 16. Esito atteso e calibrazione qualitativa del caso

Il lavoro deve concludersi con:

1. notebook Jupyter eseguibile;
2. eventuale tracciato IA in formato Markdown;
3. tabelle dei parametri, delle frequenze, delle statistiche e delle medie condizionate;
4. grafici della distribuzione di $\Delta y$ e della perdita $L$;
5. verifica empirica della formula del valore atteso totale;
6. commento finale sul ruolo dell’informazione di scenario e sui limiti della simulazione.

Il caso è calibrato correttamente se produce una distinzione visibile tra i tre eventi della partizione:

1. $A_1$: perdita media negativa o contenuta, coerente con riduzione o stabilità dei rendimenti;
2. $A_2$: perdita media positiva e moderata;
3. $A_3$: perdita media elevata e maggiore dispersione.

Il risultato atteso non è una previsione del mercato obbligazionario, ma una rappresentazione controllata del modo in cui l’informazione di scenario modifica la distribuzione rilevante della perdita.

### Possibili segnali di cattiva calibrazione

1. Le distribuzioni condizionate risultano troppo simili tra loro.
2. La soglia $\ell$ è troppo alta o troppo bassa e rende banale $\widehat{\mathbb{P}}(L>\ell)$.
3. Le medie condizionate non sono ordinate in modo coerente con l’interpretazione finanziaria dei tre regimi.
4. Il caso può essere risolto senza usare il valore atteso condizionato.
5. L’interpretazione finale diventa un semplice commento tecnico ai grafici, senza discutere il ruolo dell’informazione.