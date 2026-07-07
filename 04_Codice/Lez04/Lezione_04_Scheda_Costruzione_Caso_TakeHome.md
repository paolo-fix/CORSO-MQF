# Lezione 04 — Scheda Costruzione Caso Take-Home

Documento interno di progettazione del caso applicativo.

La Scheda Costruzione Caso resta nelle mani del docente. Ha funzione creativa primaria e deve essere redatta prima della Scheda Caso, prima della scomposizione in tappe, prima della sequenza dei prompt e prima della costruzione o valutazione del notebook.

Da questa scheda derivano:

1. la Scheda Caso Take-Home;
2. il Flusso logico-teorico risolutivo di riferimento;
3. la scomposizione in tappe input-output;
4. la sequenza dei prompt virtuosi;
5. la struttura attesa del notebook;
6. i controlli richiesti;
7. la rubrica di valutazione.

---

## 1. Identificazione del caso

- **Lezione:** Lezione 04 — Applicazione in Python: probabilità, variabili casuali e condizionamento
- **Tipo di caso:** caso take-home
- **Titolo:** Shortfall di margine condizionato a regimi del costo dell’energia
- **Collocazione nella lezione applicativa:** caso autonomo assegnato dopo il caso aula
- **Destinatari:** studenti del V anno di Banca e Risk Management
- **Uso previsto:** lavoro autonomo con uso documentato dell’IA, costruzione del notebook e consegna del tracciato IA

---

## 2. Contesto storico-finanziario, probabilistico o decisionale

Il caso è ispirato alla forte instabilità dei costi energetici osservata in Europa negli anni recenti. Per imprese manifatturiere energivore, un aumento improvviso del prezzo dell’energia può comprimere in modo rilevante il margine operativo disponibile.

Il problema non riguarda la previsione puntuale del prezzo dell’energia. Il caso è stilizzato e ha finalità didattica: rappresentare, mediante simulazione, come diversi regimi del mercato energetico possano modificare la distribuzione di uno shortfall di margine.

L’impresa considerata sostiene un fabbisogno energetico dato, espresso in MWh. Il costo unitario dell’energia è incerto e dipende dal regime di mercato. La variabile di interesse non è direttamente il prezzo dell’energia, ma lo shortfall rispetto a un margine minimo desiderato.

Il caso è rilevante per studenti di Banca e Risk Management perché collega:

1. rischio di mercato su un fattore di costo;
2. margine operativo;
3. distribuzione condizionata;
4. probabilità di superamento soglia;
5. valore atteso condizionato;
6. interpretazione gestionale del rischio.

---

## 3. Domanda quantitativa e obiettivo didattico

### Domanda quantitativa

Si considera un’impresa con contribuzione operativa netta non energetica del periodo pari a $G_0$ e fabbisogno energetico pari a $Q_E$.

Il costo unitario dell’energia è indicato con $P_E$. Il costo energetico totale è:

$$
C_E = Q_E P_E.
$$

Il margine operativo dopo il costo dell’energia è:

$$
M = G_0 - Q_E P_E.
$$

Fissato un margine minimo desiderato $m^\star$, lo shortfall di margine è:

$$
S = (m^\star - M)^+
=
\max\{m^\star - M,0\}.
$$

Poiché $M=G_0-Q_E P_E$, si ha:

$$
S
=
\max\{m^\star-G_0+Q_E P_E,0\}.
$$

La domanda quantitativa è:

$$
\text{Qual è la distribuzione dello shortfall } S
\text{ e come cambia lo shortfall atteso condizionando sui diversi regimi energetici?}
$$

In particolare, si vogliono stimare:

$$
\mathbb{E}[S],
\qquad
\mathbb{P}(S>0),
\qquad
\mathbb{P}(S>s^\star),
\qquad
q_{\alpha}(S),
\qquad
\mathbb{E}[S\mid A_g],
\qquad
\mathbb{E}[S\mid\mathcal{G}].
$$

### Obiettivo didattico

Il caso deve consolidare:

1. spazio di probabilità;
2. eventi;
3. partizioni informative;
4. variabili casuali;
5. distribuzioni condizionate;
6. trasformazioni non lineari di variabili casuali;
7. parte positiva;
8. probabilità di superamento soglia;
9. quantili;
10. valore atteso condizionato rispetto a eventi;
11. valore atteso condizionato rispetto alla sigma-algebra generata da una partizione;
12. formula del valore atteso totale.

Dal punto di vista computazionale, il caso deve consolidare una procedura Monte Carlo gerarchica in Python, con costruzione di dataset simulati, tabelle, grafici, controlli numerici e interpretazione critica.

Dal punto di vista interpretativo, il caso deve mostrare che l’informazione di regime non elimina l’incertezza sul costo dell’energia, ma modifica la distribuzione rilevante dello shortfall.

---

## 4. Funzione del caso nella lezione applicativa

### Concetti teorici da rendere osservabili

Il caso take-home deve rendere osservabili, mediante simulazione, i seguenti concetti:

1. partizione dello spazio degli esiti;
2. sigma-algebra generata da una partizione;
3. distribuzione condizionata;
4. variabile casuale derivata;
5. trasformazione non lineare mediante parte positiva;
6. distribuzione empirica;
7. massa in zero;
8. probabilità di shortfall positivo;
9. probabilità di shortfall severo;
10. quantili empirici;
11. valore atteso condizionato rispetto a eventi;
12. valore atteso condizionato rispetto alla sigma-algebra informativa;
13. formula del valore atteso totale.

### Funzione della simulazione

La simulazione Monte Carlo consente di costruire artificialmente un campione di scenari energetici coerente con una specifica teorica fissata.

La finalità non è produrre una previsione del prezzo dell’energia, ma mostrare come una struttura probabilistica condizionata si traduca in:

1. osservazioni simulate;
2. costi energetici simulati;
3. margini operativi simulati;
4. shortfall simulati;
5. distribuzioni empiriche;
6. probabilità di superamento soglia;
7. valori attesi condizionati;
8. controlli di coerenza.

### Ruolo dell’informazione condizionante

L’informazione condizionante è rappresentata da una partizione dello spazio degli esiti:

$$
\Omega=A_1\cup A_2\cup A_3,
\qquad
A_i\cap A_j=\emptyset
\quad \text{per } i\neq j.
$$

Gli eventi $A_1,A_2,A_3$ rappresentano tre regimi informativi del mercato energetico.

Condizionare su tale partizione significa sostituire una valutazione globale dello shortfall con valutazioni specifiche per regime.

### Prodotto computazionale finale

Il prodotto finale è un notebook Jupyter che produce:

1. simulazione degli eventi della partizione;
2. simulazione del prezzo dell’energia condizionato agli eventi;
3. calcolo del costo energetico, del margine e dello shortfall;
4. distribuzione empirica dello shortfall;
5. stime di media, quantili e probabilità di superamento soglia;
6. valori attesi condizionati per regime;
7. verifica empirica della formula del valore atteso totale;
8. interpretazione critica del ruolo dell’informazione di scenario.

---

## 5. Specifica teorico-matematica del caso

### Grandezze e oggetti del caso

Le grandezze economico-finanziarie sono:

- $G_0$: contribuzione operativa netta non energetica del periodo;
- $Q_E$: fabbisogno energetico del periodo, espresso in MWh;
- $P_E$: costo unitario dell’energia, espresso in euro/MWh;
- $C_E$: costo energetico totale;
- $M$: margine operativo dopo il costo dell’energia;
- $m^\star$: margine minimo desiderato;
- $S$: shortfall di margine;
- $s^\star$: soglia di shortfall severo.

La contribuzione operativa netta non energetica $G_0$ rappresenta la differenza tra ricavi del periodo e costi operativi non energetici. È la contribuzione disponibile per assorbire il costo dell’energia e conservare un margine operativo sufficiente.

### Partizione informativa

Il caso non richiede l’introduzione di una variabile casuale discreta ausiliaria. Si parte direttamente da una partizione informativa dello spazio degli esiti:

$$
\Omega=A_1\cup A_2\cup A_3,
\qquad
A_i\cap A_j=\emptyset
\quad \text{per } i\neq j.
$$

Gli eventi $A_1,A_2,A_3$ rappresentano tre regimi informativi del mercato energetico.

| Evento | Descrizione | Interpretazione economica |
|---|---|---|
| $A_1$ | Normalizzazione energetica | il costo dell’energia tende a rientrare su livelli contenuti |
| $A_2$ | Tensione persistente | il costo dell’energia resta elevato ma non estremo |
| $A_3$ | Shock energetico severo | il costo dell’energia aumenta in modo marcato e con maggiore dispersione |

La sigma-algebra informativa generata dalla partizione è:

$$
\mathcal{G}=\sigma(A_1,A_2,A_3).
$$

### Variabili casuali

Il prezzo unitario dell’energia è una variabile casuale continua:

$$
P_E:\Omega\to\mathbb{R}.
$$

Condizionatamente all’evento informativo $A_g$, il prezzo unitario dell’energia segue una distribuzione normale:

$$
P_E\mid A_g \sim \mathcal{N}(\mu_g,\sigma_g^2),
\qquad g=1,2,3.
$$

Il costo energetico totale è:

$$
C_E=Q_E P_E.
$$

Il margine operativo dopo il costo dell’energia è:

$$
M=G_0-Q_E P_E.
$$

Lo shortfall rispetto al margine minimo desiderato è:

$$
S=(m^\star-M)^+.
$$

Sostituendo la formula di $M$:

$$
S
=
\max\{m^\star-G_0+Q_E P_E,0\}.
$$

### Quantità teoriche da stimare o calcolare

Le quantità principali sono:

$$
\mathbb{E}[S],
\qquad
\mathbb{P}(S>0),
\qquad
\mathbb{P}(S>s^\star),
\qquad
q_{\alpha}(S).
$$

Le quantità condizionate sono:

$$
\mathbb{E}[S\mid A_g],
\qquad g=1,2,3.
$$

Il valore atteso condizionato rispetto alla sigma-algebra informativa è:

$$
\mathbb{E}[S\mid\mathcal{G}]
=
\sum_{g=1}^{3}
\mathbb{E}[S\mid A_g]\mathbf{1}_{A_g}.
$$

La proprietà da verificare è la formula del valore atteso totale:

$$
\mathbb{E}[S]
=
\sum_{g=1}^{3}
\mathbb{P}(A_g)\mathbb{E}[S\mid A_g].
$$

Nel notebook, la controparte empirica sarà:

$$
\widehat{\mathbb{E}}[S]
\approx
\sum_{g=1}^{3}
\widehat{\mathbb{P}}(A_g)
\widehat{\mathbb{E}}[S\mid A_g].
$$

Occorre distinguere chiaramente:

1. $\mathbb{E}[S\mid A_g]$, che è un numero;
2. $\mathbb{E}[S\mid\mathcal{G}]$, che è una variabile casuale costante sui blocchi della partizione;
3. $\mathbb{E}[S]$, che è il valore atteso non condizionato.

---

## 6. Specifica parametrica iniziale

I parametri seguenti sono stilizzati e hanno funzione didattica. Non sono stime storiche e non hanno finalità previsionali.

### Parametri economico-finanziari

| Grandezza | Valore | Unità | Significato |
|---|---:|---|---|
| $G_0$ | 8.000.000 | euro | contribuzione operativa netta non energetica |
| $Q_E$ | 50.000 | MWh | fabbisogno energetico del periodo |
| $m^\star$ | 2.000.000 | euro | margine minimo desiderato |
| $s^\star$ | 1.000.000 | euro | soglia di shortfall severo |
| $n$ | 50.000 | simulazioni | dimensione Monte Carlo |
| seed | 24680 | — | seme casuale |

### Probabilità degli eventi informativi

| Evento | Descrizione | Probabilità |
|---|---|---:|
| $A_1$ | Normalizzazione energetica | 0,35 |
| $A_2$ | Tensione persistente | 0,45 |
| $A_3$ | Shock energetico severo | 0,20 |

### Distribuzioni condizionate del prezzo dell’energia

| Evento | $\mu_g$ | $\sigma_g$ | Lettura economica |
|---|---:|---:|---|
| $A_1$ | 75 | 15 | costo unitario contenuto |
| $A_2$ | 115 | 25 | costo unitario elevato |
| $A_3$ | 170 | 45 | costo unitario molto elevato e più disperso |

Tutti i prezzi sono espressi in euro/MWh.

### Soglie implicite del prezzo dell’energia

La soglia di prezzo che porta il margine esattamente al livello minimo desiderato è:

$$
S>0
\quad\Longleftrightarrow\quad
M<m^\star.
$$

Poiché:

$$
M=G_0-Q_E P_E,
$$

si ottiene:

$$
S>0
\quad\Longleftrightarrow\quad
P_E>\frac{G_0-m^\star}{Q_E}.
$$

Con i parametri proposti:

$$
p_E^\star
=
\frac{8.000.000-2.000.000}{50.000}
=
120.
$$

Quindi:

$$
S>0
\quad\Longleftrightarrow\quad
P_E>120.
$$

La soglia di prezzo associata allo shortfall severo $S>s^\star$ è:

$$
S>s^\star
\quad\Longleftrightarrow\quad
P_E>\frac{G_0-m^\star+s^\star}{Q_E}.
$$

Con i parametri proposti:

$$
\frac{8.000.000-2.000.000+1.000.000}{50.000}
=
140.
$$

Quindi:

$$
S>s^\star
\quad\Longleftrightarrow\quad
P_E>140.
$$

### Vincoli di calibrazione

Il caso è calibrato in modo da produrre:

1. shortfall atteso basso o nullo in $A_1$;
2. shortfall atteso positivo ma intermedio in $A_2$;
3. shortfall atteso elevato e più disperso in $A_3$;
4. massa visibile in zero nella distribuzione di $S$;
5. probabilità non trascurabile di shortfall positivo;
6. probabilità rilevante ma non banale di shortfall severo;
7. differenze visibili tra media non condizionata e medie condizionate;
8. verifica empirica stabile della formula del valore atteso totale.

---

## 7. Ipotesi modellistiche e limiti

### Ipotesi principali

1. La contribuzione operativa netta non energetica $G_0$ è nota e fissata.
2. Il fabbisogno energetico $Q_E$ è noto e fissato.
3. L’unica fonte di incertezza modellata è il prezzo unitario dell’energia $P_E$.
4. L’informazione disponibile è rappresentata dalla partizione $\{A_1,A_2,A_3\}$.
5. Condizionatamente a ciascun evento $A_g$, il prezzo dell’energia segue una distribuzione normale.
6. Gli eventi $A_1,A_2,A_3$ costituiscono una partizione dello spazio degli esiti.
7. La simulazione Monte Carlo approssima quantità teoriche mediante frequenze e medie empiriche.
8. Lo shortfall è definito mediante la parte positiva $(m^\star-M)^+$.

### Ipotesi semplificatrici

1. Non si modellano ricavi aleatori.
2. Non si modellano costi non energetici aleatori.
3. Non si considera elasticità della produzione al prezzo dell’energia.
4. Non si considera copertura finanziaria o contrattuale del costo energetico.
5. Non si considerano contratti forward, opzioni o hedging energetico.
6. Non si considera dinamica multiperiodale.
7. Non si stimano parametri da dati reali.
8. Non si modellano correlazioni con altri fattori di rischio.

### Aspetti esclusi dal modello

Il caso non tratta:

1. previsione del prezzo dell’energia;
2. pricing di contratti energetici;
3. ottimizzazione della produzione;
4. gestione di hedging;
5. scenari macroeconomici completi;
6. rischio di liquidità;
7. rischio di credito;
8. dinamica multiperiodale dei margini;
9. dati reali di mercato.

### Limiti da dichiarare nell’interpretazione

Il modello è utile per comprendere il ruolo dell’informazione condizionante e della distribuzione condizionata dello shortfall, ma non produce una misura gestionale completa del rischio energetico.

L’uso di distribuzioni normali per prezzi dell’energia è una semplificazione didattica. Poiché una normale può generare valori negativi, il notebook deve controllare se compaiono osservazioni $P_E<0$. Con la calibrazione proposta l’evento dovrebbe essere raro, ma se presente va segnalato come limite del modello, non eliminato senza dichiarazione.

La simulazione non deve essere interpretata come previsione del prezzo dell’energia.

---

## 8. Output richiesti

### Tabelle

1. Tabella dei parametri economico-finanziari.
2. Tabella degli eventi $A_1,A_2,A_3$ e delle probabilità.
3. Tabella dei parametri condizionati $(\mu_g,\sigma_g)$.
4. Tabella delle soglie implicite $P_E>120$ e $P_E>140$.
5. Tabella delle frequenze simulate degli eventi.
6. Tabella di controllo delle statistiche empiriche di $P_E\mid A_g$.
7. Tabella descrittiva dello shortfall $S$:
   - media;
   - deviazione standard;
   - minimo;
   - massimo;
   - quantili principali.
8. Tabella delle probabilità:
   - $\widehat{\mathbb{P}}(S>0)$;
   - $\widehat{\mathbb{P}}(S>s^\star)$.
9. Tabella delle medie condizionate:
   - $\widehat{\mathbb{E}}[S\mid A_1]$;
   - $\widehat{\mathbb{E}}[S\mid A_2]$;
   - $\widehat{\mathbb{E}}[S\mid A_3]$.
10. Tabella di verifica della formula del valore atteso totale.
11. Eventuale tabella finale con evento simulato, $P_E$, $C_E$, $M$, $S$ e valore della variabile a gradini $\widehat{\mathbb{E}}[S\mid\mathcal{G}]$.

### Grafici

1. Istogramma o densità empirica del prezzo dell’energia $P_E$.
2. Istogramma o densità empirica dello shortfall $S$.
3. Grafico della distribuzione empirica di $S$ con evidenza della soglia $s^\star$.
4. Grafico della massa in zero di $S$.
5. Grafico delle medie condizionate $\widehat{\mathbb{E}}[S\mid A_g]$.
6. Confronto tra distribuzioni condizionate dello shortfall.
7. Eventuale confronto tra distribuzioni condizionate del prezzo dell’energia.
8. Eventuale ECDF dello shortfall.

### Stime, indicatori o quantità numeriche

1. $\widehat{\mathbb{E}}[S]$.
2. $\widehat{\mathbb{P}}(S>0)$.
3. $\widehat{\mathbb{P}}(S>s^\star)$.
4. Quantili empirici di $S$.
5. $\widehat{\mathbb{E}}[S\mid A_g]$ per $g=1,2,3$.
6. Verifica empirica della media ricomposta:
   $$
   \sum_{g=1}^{3}
   \widehat{\mathbb{P}}(A_g)
   \widehat{\mathbb{E}}[S\mid A_g].
   $$

### Controlli numerici

1. Le probabilità degli eventi devono sommare a uno.
2. Le frequenze empiriche degli eventi devono essere vicine alle probabilità teoriche.
3. Ogni evento deve avere numerosità sufficiente.
4. Le medie e deviazioni standard empiriche di $P_E\mid A_g$ devono essere coerenti con $\mu_g,\sigma_g$.
5. Il notebook deve controllare l’eventuale presenza di $P_E<0$.
6. I vettori $P_E$, $C_E$, $M$ e $S$ devono avere dimensione $n$.
7. Il costo energetico deve rispettare la relazione $C_E=Q_E P_E$.
8. Il margine deve rispettare la relazione $M=G_0-Q_E P_E$.
9. Lo shortfall deve rispettare $S\ge 0$.
10. Deve risultare $S=0$ se $M\ge m^\star$.
11. Deve risultare $S=m^\star-M$ se $M<m^\star$.
12. La media globale di $S$ deve coincidere, salvo arrotondamenti, con la media pesata delle medie condizionate.
13. I quantili devono rispettare l’ordinamento atteso.
14. La media deve collocarsi tra minimo e massimo campionario.

### Controlli logici

1. Gli eventi $A_1,A_2,A_3$ sono blocchi informativi della partizione, non valori del prezzo o dello shortfall.
2. $P_E$ non è il costo totale dell’energia.
3. $C_E$ è il costo energetico totale.
4. $M$ è il margine dopo il costo dell’energia.
5. $S$ è una trasformazione non lineare del margine.
6. La massa in zero di $S$ indica assenza di shortfall, non assenza di costo energetico.
7. $\mathbb{E}[S\mid A_g]$ è un numero.
8. $\mathbb{E}[S\mid\mathcal{G}]$ è una variabile casuale costante sui blocchi della partizione.
9. La formula del valore atteso totale non implica che $\mathbb{E}[S]$ ed $\mathbb{E}[S\mid\mathcal{G}]$ coincidano come oggetti.
10. La verifica campionaria della media ricomposta deve essere distinta dalla proprietà teorica.

### Controlli interpretativi

1. L’evento $A_3$ deve mostrare shortfall atteso maggiore rispetto agli altri eventi.
2. L’evento $A_1$ deve mostrare shortfall basso o nullo con elevata frequenza.
3. L’evento $A_2$ deve rappresentare una situazione intermedia.
4. L’informazione della partizione non elimina l’incertezza, ma modifica la distribuzione condizionata rilevante.
5. La probabilità globale di shortfall positivo deve essere interpretata come probabilità non condizionata, non come probabilità valida in ogni regime.
6. La massa in zero deve essere interpretata correttamente come assenza di shortfall rispetto alla soglia $m^\star$.
7. La simulazione non deve essere interpretata come previsione del prezzo dell’energia.

---

## 9. Flusso logico-teorico risolutivo

Questa sezione costituisce il cuore intellettuale del caso.

Il suo compito non è descrivere il codice, né anticipare la scomposizione operativa del notebook, ma ricostruire la sequenza dei richiami teorico-matematici necessari per passare dalla domanda quantitativa agli output richiesti.

| Passo | Finalità risolutiva | Formula teorico-matematica / definizione / proprietà / teorema | Applicazione nel caso | Output o controllo collegato |
|---:|---|---|---|---|
| 1 | Identificare la variabile economica finale e il legame con il fattore di rischio | Shortfall come variabile casuale derivata: $S=(m^\star-M)^+$, con $M=G_0-Q_E P_E$ | La quantità di interesse è lo shortfall $S$, determinato dal prezzo dell’energia tramite costo energetico e margine operativo. | Formula da implementare; controllo $S\ge 0$; distinzione tra prezzo, costo, margine e shortfall. |
| 2 | Definire le soglie di rischio e tradurle nel fattore di rischio | Eventi $\{S>0\}$ e $\{S>s^\star\}$; equivalenze $S>0 \Longleftrightarrow P_E>(G_0-m^\star)/Q_E$ e $S>s^\star \Longleftrightarrow P_E>(G_0-m^\star+s^\star)/Q_E$ | Le soglie monetarie diventano soglie implicite sul prezzo unitario dell’energia. | Calcolo delle soglie $120$ e $140$ euro/MWh; output $\widehat{\mathbb{P}}(S>0)$ e $\widehat{\mathbb{P}}(S>s^\star)$. |
| 3 | Rappresentare l’informazione di scenario | Partizione di $\Omega$: $\Omega=A_1\cup A_2\cup A_3$, $A_i\cap A_j=\emptyset$ per $i\neq j$; probabilità $p_g=\mathbb{P}(A_g)$, $\sum_g p_g=1$ | I tre eventi rappresentano regimi del mercato energetico e le loro probabilità guidano l’estrazione Monte Carlo del regime. | Tabella degli eventi e delle probabilità; controllo $\sum_g p_g=1$; frequenze empiriche $\widehat{\mathbb{P}}(A_g)$. |
| 4 | Specificare il comportamento del fattore di rischio nei diversi regimi | Distribuzione condizionata: $P_E\mid A_g\sim\mathcal{N}(\mu_g,\sigma_g^2)$ | Ogni regime genera prezzi dell’energia con media e volatilità diverse. | Tabella dei parametri $(\mu_g,\sigma_g)$; controllo di media e deviazione standard empiriche per regime; controllo eventuale $P_E<0$. |
| 5 | Costruire la distribuzione non condizionata tramite simulazione gerarchica | Formula di miscela e campionamento gerarchico: prima $A_g$, poi $P_E\mid A_g$ | La distribuzione globale di $P_E$ nasce dalla combinazione tra probabilità dei regimi e distribuzioni condizionate. | Dataset simulato con evento e $P_E$; controllo frequenze dei regimi; controllo dei prezzi condizionati. |
| 6 | Trasformare il prezzo simulato in costo, margine e shortfall | $C_{E,i}=Q_E P_{E,i}$, $M_i=G_0-Q_E P_{E,i}$, $S_i=(m^\star-M_i)^+$ | Da ogni prezzo simulato si ottengono costo energetico, margine operativo e shortfall. | Dataset con evento, $P_E$, $C_E$, $M$, $S$; controllo formula-codice; controllo dimensione $n$. |
| 7 | Produrre la lettura non condizionata del rischio | Distribuzione empirica, media, quantili, probabilità di superamento soglia | Si analizza la distribuzione globale dello shortfall senza distinguere i regimi. | $\widehat{\mathbb{E}}[S]$, quantili empirici, $\widehat{\mathbb{P}}(S>0)$, $\widehat{\mathbb{P}}(S>s^\star)$, grafici della distribuzione di $S$. |
| 8 | Produrre la lettura condizionata per regime | Valore atteso condizionato rispetto a un evento: $\mathbb{E}[S\mid A_g]$ | Si confronta lo shortfall atteso nei tre regimi energetici. | Tabella delle medie condizionate $\widehat{\mathbb{E}}[S\mid A_g]$; grafico delle medie condizionate. |
| 9 | Collegare l’informazione disponibile al valore atteso condizionato | Valore atteso condizionato rispetto alla sigma-algebra: $\mathbb{E}[S\mid\mathcal{G}]=\sum_g \mathbb{E}[S\mid A_g]\mathbf{1}_{A_g}$ | La previsione condizionata diventa una variabile casuale costante sui blocchi della partizione. | Eventuale colonna $\widehat{\mathbb{E}}[S\mid\mathcal{G}]$; distinzione tra numero condizionato e variabile casuale a gradini. |
| 10 | Verificare la coerenza complessiva e interpretare il ruolo dell’informazione | Formula del valore atteso totale: $\mathbb{E}[S]=\sum_g\mathbb{P}(A_g)\mathbb{E}[S\mid A_g]$; interpretazione del condizionamento | La media globale viene ricostruita come media pesata delle medie di regime. L’informazione modifica la distribuzione rilevante, ma non elimina l’incertezza. | Controllo tra media campionaria e media ricomposta; commento finale su regimi, shortfall atteso, massa in zero, soglie e limiti del modello. |

La sequenza del Flusso logico-teorico risolutivo deve guidare la successiva scomposizione in tappe input-output. Le tappe operative non devono nascere direttamente dal codice, ma dalla successione teorica fissata in questa tabella.

---

## 10. Scomposizione attesa in tappe input-output

La scomposizione in tappe traduce il Flusso logico-teorico risolutivo in una sequenza operativa.

Ogni tappa deve avere un input osservabile, un’operazione definita, un output controllabile e un uso nella tappa successiva.

| Tappa | Titolo | Input | Operazione | Output | Controllo | Uso successivo | Regime IA |
|---:|---|---|---|---|---|---|---|
| 1 | Specifica teorica e parametri | Scheda Caso, $G_0,Q_E,m^\star,s^\star,n,seed$ | definizione di grandezze, partizione informativa, variabili e parametri | tabelle parametri e oggetti Python | somma probabilità; soglie implicite $120$ e $140$ | simulazione degli eventi informativi | A/B |
| 2 | Simulazione della partizione informativa | probabilità di $A_1,A_2,A_3$, $n$, seed | assegnazione di ciascuna simulazione a uno dei tre eventi della partizione | vettore di etichette $A_1,A_2,A_3$ e frequenze empiriche | frequenze vicine alle probabilità teoriche; assenza di etichette non ammesse | simulazione condizionata di $P_E$ | B |
| 3 | Simulazione di $P_E\mid A_g$, margine e shortfall | etichette degli eventi, parametri $(\mu_g,\sigma_g)$, $G_0,Q_E,m^\star$ | simulazione dei prezzi, calcolo di $C_E$, $M$ e $S$ | dataset con evento, $P_E$, $C_E$, $M$, $S$ | dimensioni; eventuale $P_E<0$; $S\ge0$; regole di calcolo dello shortfall | distribuzione empirica dello shortfall | B |
| 4 | Distribuzione empirica e rischio non condizionato | vettore $S$, soglie $0$ e $s^\star$ | statistiche descrittive, quantili, probabilità $S>0$ e $S>s^\star$ | tabelle e grafici globali | ordine dei quantili; media compresa tra minimo e massimo; coerenza delle probabilità; massa in zero | confronto con analisi condizionata | B/C |
| 5 | Valori attesi condizionati e valore atteso totale | dataset con evento e $S$ | medie condizionate per blocco e media pesata | tabella $\widehat{\mathbb{E}}[S\mid A_g]$, verifica della media totale, eventuale colonna $\widehat{\mathbb{E}}[S\mid\mathcal{G}]$ | differenza tra media globale e media ricomposta; distinzione tra numero e variabile casuale a gradini | interpretazione critica | B/C |
| 6 | Interpretazione critica e limiti | output delle tappe precedenti | commento autonomo su ruolo dell’informazione, rischio residuo, massa in zero e limiti del modello | sezione finale del notebook | non confondere condizionamento con eliminazione del rischio; non sovrainterpretare la simulazione | chiusura del lavoro | C |

---

## 11. Sequenza docente dei prompt virtuosi

La sequenza dei prompt virtuosi descrive il modo in cui il caso take-home può essere sviluppato passo passo con supporto dell’IA, mantenendo il controllo dello studente su specifica teorica, scomposizione, codice, output, controlli e interpretazione.

La sequenza è costruita a partire dalla Scheda Caso validata. L’IA non deve modificare la partizione informativa, le grandezze economico-finanziarie, le formule, i parametri, le soglie o gli output richiesti.

La sequenza deve partire da:

1. Prompt zero;
2. Prompt 1 — acquisizione non produttiva della Scheda Caso;
3. Prompt 2 — costruzione del Flusso logico-teorico risolutivo;
4. prompt di tappa.

### 11.1 Mappa sintetica dei prompt

| Prompt / gruppo di prompt | Tappa o fase collegata | Regime IA | Output richiesto | Destinazione nel notebook / tracciato |
|---:|---|---|---|---|
| 0 | Inizializzazione generale | — | conferma minima di comprensione dei vincoli generali | tracciato IA |
| 1 | Acquisizione della Scheda Caso Take-Home | — | conferma minima: “OK, scheda acquisita” | tracciato IA |
| 2 | Flusso logico-teorico risolutivo | A | tabella del flusso logico-teorico, costruita a partire da un contributo iniziale dello studente | tracciato IA; base per la scomposizione |
| 3 | Scomposizione del caso in tappe input-output | A | proposta di scomposizione in tappe | tracciato IA; sezione di struttura del notebook |
| 4 | Validazione della scomposizione | C | verifica di completezza, coerenza e assenza di salti logici | tracciato IA |
| 5 | Tappa 1 — Specifica teorica e parametri | B | celle Markdown e codice per parametri, probabilità, soglie implicite e controlli iniziali | notebook |
| 6 | Tappa 2 — Simulazione della partizione informativa | B | celle Markdown e codice per assegnare le simulazioni agli eventi $A_1,A_2,A_3$ | notebook |
| 7 | Tappa 3 — Simulazione di $P_E\mid A_g$, margine e shortfall | B | celle Markdown e codice per simulare $P_E$, calcolare $C_E$, $M$, $S$ e costruire il dataset | notebook |
| 8 | Tappa 4 — Analisi non condizionata dello shortfall | B/C | tabelle, grafici e controlli su distribuzione empirica, quantili, massa in zero e soglie | notebook |
| 9 | Tappa 5 — Analisi condizionata e valore atteso totale | B/C | medie condizionate, variabile a gradini, verifica della formula del valore atteso totale | notebook |
| 10 | Tappa 6 — Interpretazione critica | C | revisione critica di una bozza autonoma dello studente | notebook; tracciato IA |
| 11 | Controllo finale del tracciato IA | C | checklist di completezza del tracciato | file `.md` finale |

### 11.2 Input forniti all’IA ed esempio di formulazione

| Prompt / gruppo di prompt | Tappa o fase collegata | Input fornito all’IA | Esempio sintetico di input/prompt |
|---:|---|---|---|
| 0 | Inizializzazione generale | Regole generali del corso MQF, distinzione tra notebook e tracciato IA, regimi A/B/C, divieto di anticipare contenuti non richiesti. Il caso specifico non viene ancora fornito. | Sto svolgendo un caso take-home del corso MQF. Per ora devi solo acquisire i vincoli generali: Regime A per ricognizione teorico-modellistica, Regime B per traduzione operativa in codice, Regime C per verifica critica. Non produrre contenuti, formule, codice, esempi o piani di lavoro. Conferma soltanto di avere compreso. |
| 1 | Acquisizione della Scheda Caso Take-Home | Scheda Caso Take-Home completa. L’IA deve solo acquisirla come specifica vincolante. | Ti fornisco la Scheda Caso Take-Home. Devi soltanto leggerla e acquisirla come specifica vincolante del lavoro. Non devi produrre sintesi, formule aggiuntive, codice, tappe operative, interpretazioni, controlli o suggerimenti. Rispondi soltanto “OK, scheda acquisita” se tutto è chiaro. |
| 2 | Flusso logico-teorico risolutivo | Scheda Caso acquisita e contributo teorico iniziale dello studente. | Regime A. Sulla base della Scheda Caso acquisita, devo costruire il Flusso logico-teorico risolutivo. Secondo me gli elementi teorici necessari, nell’ordine logico utile alla soluzione, sono: [elenco iniziale dello studente]. Aiutami a verificare, completare e ordinare questa sequenza, senza scrivere codice e senza proporre ancora la scomposizione operativa del notebook. |
| 3 | Scomposizione del caso in tappe input-output | Scheda Caso, flusso logico-teorico validato, output richiesti, controlli obbligatori. | Scomponi il caso in tappe input-output. Per ogni tappa indica input, operazione, output, controllo, uso nella tappa successiva e regime IA prevalente. Non scrivere codice, non calcolare risultati e non modificare la specifica del caso. |
| 4 | Validazione della scomposizione | Scomposizione proposta, Scheda Caso, flusso logico-teorico validato, lista degli output richiesti e controlli obbligatori. | Verifica se la scomposizione copre tutti gli output richiesti, se ogni tappa ha input e output osservabili, e se gli output vengono riutilizzati correttamente. Non riscrivere integralmente la scomposizione: segnala solo correzioni necessarie. |
| 5 | Tappa 1 — Specifica teorica e parametri | Specifica teorica validata, parametri $G_0,Q_E,m^\star,s^\star,n,seed$, probabilità degli eventi, parametri condizionati $(\mu_g,\sigma_g)$, soglie implicite da calcolare. | Produci per la Tappa 1 una cella Markdown e una cella Python. Il Markdown deve spiegare grandezze, parametri e partizione informativa. Il codice deve definire i parametri, produrre le tabelle iniziali, controllare la somma delle probabilità e calcolare le soglie implicite di prezzo associate a $S>0$ e $S>s^\star$. |
| 6 | Tappa 2 — Simulazione della partizione informativa | Probabilità di $A_1,A_2,A_3$, numero di simulazioni $n$, seed, etichette degli eventi. La specifica non prevede una variabile teorica ausiliaria. | Produci Markdown e codice per assegnare ciascuna simulazione a uno degli eventi $A_1,A_2,A_3$. Non introdurre una variabile teorica discreta aggiuntiva. Nel codice puoi usare un vettore di etichette operative. Produci frequenze empiriche e controlli sugli scostamenti dalle probabilità teoriche. |
| 7 | Tappa 3 — Simulazione di $P_E\mid A_g$, margine e shortfall | Etichette operative degli eventi, parametri condizionati $(\mu_g,\sigma_g)$, formule $C_E=Q_E P_E$, $M=G_0-Q_E P_E$, $S=(m^\star-M)^+$. | Produci Markdown e codice per simulare $P_E\mid A_g$, calcolare $C_E$, $M$ e $S$, e costruire il dataset principale. Mantieni le formule fissate. Inserisci controlli su dimensioni, eventuali $P_E<0$, $S\ge0$, $S=0$ se $M\ge m^\star$ e $S=m^\star-M$ se $M<m^\star$. |
| 8 | Tappa 4 — Analisi non condizionata dello shortfall | Dataset con evento, $P_E$, $C_E$, $M$, $S$; soglie $0$ e $s^\star$; livelli di quantile; output richiesti per analisi globale. | Produci Markdown e codice per stimare la distribuzione empirica dello shortfall $S$: media, deviazione standard, minimo, massimo, quantili, $\widehat{\mathbb{P}}(S>0)$ e $\widehat{\mathbb{P}}(S>s^\star)$. Produci grafici che evidenzino la massa in zero e la soglia di shortfall severo. Inserisci controlli su quantili e probabilità. |
| 9 | Tappa 5 — Analisi condizionata e valore atteso totale | Dataset con evento e $S$, frequenze empiriche, media globale, definizione di $\mathcal{G}=\sigma(A_1,A_2,A_3)$, distinzione tra $\mathbb{E}[S\mid A_g]$ e $\mathbb{E}[S\mid\mathcal{G}]$. | Produci Markdown e codice per calcolare $\widehat{\mathbb{E}}[S\mid A_g]$, costruire se utile la variabile a gradini $\widehat{\mathbb{E}}[S\mid\mathcal{G}]$ e verificare la formula del valore atteso totale. Distingui chiaramente numero condizionato, variabile casuale condizionata e media globale. |
| 10 | Tappa 6 — Interpretazione critica | Bozza autonoma dello studente basata sugli output delle tappe precedenti: distribuzione di $S$, massa in zero, medie condizionate, ruolo della partizione, limiti del modello. | Ho scritto questa interpretazione. Segnala errori, ambiguità, affermazioni troppo forti, confusioni tra quantità teoriche e stime empiriche, e limiti mancanti. Non riscrivere integralmente la conclusione e non sostituirti a me. |
| 11 | Controllo finale del tracciato IA | Tracciato IA compilato, elenco dei prompt, regimi dichiarati, decisioni dello studente, collegamenti alle sezioni del notebook, output e controlli. | Controlla se il tracciato documenta prompt, regime, risposta utilizzata, decisione dello studente, output prodotto e controllo svolto. Non valutare la qualità intrinseca delle risposte IA: valuta solo completezza, coerenza e tracciabilità del processo. |

---

## 12. Struttura attesa del notebook

La struttura attesa del notebook deve derivare dalla scomposizione in tappe.

| Sezione | Titolo della sezione notebook | Tappa o fase collegata | Prompt / gruppo di prompt di riferimento | Tipo cella | Contenuto e output attesi |
|---:|---|---|---|---|---|
| 1 | Titolo, contesto e domanda quantitativa | Acquisizione del caso | 1 | Markdown | Presenta il caso take-home, il contesto energetico, la domanda quantitativa e il ruolo dell’informazione rappresentata dalla partizione $A_1,A_2,A_3$. Deve chiarire che il caso è simulativo e non previsionale. |
| 2 | Flusso logico-teorico risolutivo | Prompt 2 | 2 | Markdown | Riporta la tabella del Flusso logico-teorico risolutivo costruita con contributo iniziale dello studente e validata criticamente. Deve distinguere richiami teorici, applicazione nel caso e output collegati. |
| 3 | Scomposizione del lavoro in tappe | Scomposizione e validazione | 3-4 | Markdown | Riporta la sequenza validata delle tappe input-output. Per ogni tappa indica input, operazione, output, controllo e uso nella tappa successiva. |
| 4 | Parametri economico-finanziari e probabilistici | Tappa 1 | 5 | Markdown + codice | Definisce $G_0$, $Q_E$, $m^\star$, $s^\star$, $n$, seed, probabilità degli eventi e parametri condizionati $(\mu_g,\sigma_g)$. Produce tabelle dei parametri e controlli iniziali: somma probabilità e soglie implicite $120$ e $140$. |
| 5 | Simulazione della partizione informativa | Tappa 2 | 6 | Markdown + codice | Assegna ogni simulazione a uno dei tre eventi $A_1,A_2,A_3$. Produce tabella di frequenze empiriche, confronto con probabilità teoriche e controllo di assenza di etichette non ammesse. |
| 6 | Simulazione del prezzo dell’energia | Tappa 3 | 7 | Markdown + codice | Simula $P_E\mid A_g$ usando i parametri condizionati. Produce una tabella di controllo per evento con media e deviazione standard empiriche di $P_E$, da confrontare con $\mu_g$ e $\sigma_g$. Include controllo su eventuali $P_E<0$. |
| 7 | Calcolo del costo energetico, del margine e dello shortfall | Tappa 3 | 7 | Markdown + codice | Calcola $C_E=Q_E P_E$, $M=G_0-Q_E P_E$ e $S=(m^\star-M)^+$. Costruisce il dataset con evento, $P_E$, $C_E$, $M$, $S$. Include controlli su dimensione, relazioni formula-codice e definizione della parte positiva. |
| 8 | Analisi non condizionata dello shortfall | Tappa 4 | 8 | Markdown + codice | Produce statistiche descrittive di $S$, quantili, $\widehat{\mathbb{P}}(S>0)$ e $\widehat{\mathbb{P}}(S>s^\star)$. Include grafici della distribuzione di $S$, massa in zero e soglia $s^\star$. |
| 9 | Analisi condizionata per evento | Tappa 5 | 9 | Markdown + codice | Calcola $\widehat{\mathbb{E}}[S\mid A_1]$, $\widehat{\mathbb{E}}[S\mid A_2]$, $\widehat{\mathbb{E}}[S\mid A_3]$, frequenze empiriche e distribuzioni condizionate. Produce tabella e grafico delle medie condizionate. |
| 10 | Valore atteso condizionato rispetto a $\mathcal{G}$ e valore atteso totale | Tappa 5 | 9 | Markdown + codice | Costruisce, se utile, una colonna con la variabile a gradini $\widehat{\mathbb{E}}[S\mid\mathcal{G}]$. Verifica la ricomposizione della media globale mediante frequenze empiriche e medie condizionate. Deve distinguere tra verifica campionaria e proprietà teorica. |
| 11 | Interpretazione critica dei risultati | Tappa 6 | 10 | Markdown | Contiene commento autonomo dello studente sul ruolo della partizione informativa, sulla differenza tra analisi globale e condizionata, sulla massa in zero, sullo shortfall atteso nei diversi eventi e sul significato delle soglie. |
| 12 | Limiti del modello e sintesi finale | Tappa 6 / controllo finale | 10-11 | Markdown | Dichiara i limiti: distribuzioni normali dei prezzi, assenza di dinamica multiperiodale, assenza di hedging, assenza di dati reali, $G_0$ e $Q_E$ fissati. Chiude con una sintesi proporzionata agli output simulati. |

---

## 13. Criteri di validazione del notebook

Il notebook è accettabile se:

1. implementa la specifica teorica senza modificarla;
2. parte direttamente dalla partizione $A_1,A_2,A_3$ senza introdurre una variabile teorica ausiliaria non necessaria;
3. mantiene distinti eventi informativi, prezzo dell’energia, costo energetico, margine e shortfall;
4. simula correttamente l’assegnazione delle osservazioni ai tre eventi della partizione;
5. simula $P_E\mid A_g$ con parametri coerenti;
6. controlla e commenta l’eventuale presenza di valori $P_E<0$;
7. costruisce $C_E$, $M$ e $S$ secondo le formule fissate;
8. verifica correttamente la definizione di shortfall mediante parte positiva;
9. produce tabelle e grafici leggibili;
10. include controlli numerici e logici;
11. verifica la formula del valore atteso totale;
12. contiene un’interpretazione critica autonoma;
13. dichiara i limiti del modello.

Il notebook non è accettabile se:

1. modifica il modello senza dichiararlo;
2. sostituisce $S=(m^\star-M)^+$ con una grandezza diversa;
3. interpreta gli eventi $A_g$ come valori del prezzo o dello shortfall;
4. confonde prezzo unitario, costo energetico totale, margine e shortfall;
5. elimina o corregge valori $P_E<0$ senza dichiararlo;
6. usa dati reali non richiesti;
7. introduce hedging, dinamica multiperiodale, ottimizzazione produttiva o contratti energetici non richiesti;
8. presenta output senza controlli;
9. delega l’interpretazione finale all’IA.

---

## 14. Criteri di valutazione del tracciato IA

Il tracciato IA è valutato come documento metodologico.

La valutazione riguarda il modo in cui lo studente usa l’IA nel processo di costruzione del lavoro, non la qualità intrinseca delle risposte prodotte dall’IA.

Sono elementi da valutare:

1. correttezza del Prompt zero;
2. acquisizione non produttiva della Scheda Caso tramite Prompt 1;
3. qualità del contributo iniziale dello studente al Prompt 2;
4. qualità del Flusso logico-teorico risolutivo finale;
5. rispetto dei regimi A/B/C;
6. qualità dei prompt di tappa;
7. validazione delle risposte IA;
8. correzione di errori, ambiguità o modifiche non autorizzate;
9. collegamento tra prompt, notebook e output;
10. autonomia dell’interpretazione finale.

Nel Prompt 2 il docente valuta in modo specifico quanto il Flusso logico-teorico risolutivo finale derivi da una proposta teorica iniziale autonoma dello studente e quanto invece sia stato completato dall’IA.

Sono indicatori positivi:

1. proposta iniziale dello studente non vuota e non generica;
2. presenza di definizioni, proprietà, formule o teoremi pertinenti;
3. ordine logico almeno parzialmente motivato;
4. collegamento tra richiami teorici e quantità da stimare;
5. collegamento tra richiami teorici e output richiesti;
6. richiesta all’IA di verificare, completare e ordinare, non di sostituire integralmente;
7. correzione o selezione critica della risposta IA;
8. tabella finale coerente con la Scheda Caso.

Sono indicatori deboli:

1. Prompt 2 formulato come richiesta generica del tipo “costruisci il flusso logico-teorico del caso”;
2. assenza di contributo teorico iniziale dello studente;
3. elenco puramente nominale copiato dalla Scheda Caso;
4. confusione tra flusso logico-teorico e scomposizione operativa del notebook;
5. accettazione integrale della risposta IA senza controllo;
6. flusso finale non collegato agli output richiesti.

---

## 15. Rubrica sintetica

| Area | Peso | Criteri |
|---|---:|---|
| Premesse teorico-matematiche | 15 | corretta identificazione di partizione $A_1,A_2,A_3$, $P_E$, $C_E$, $M$, $S$, $\mathcal{G}$, ipotesi e quantità teoriche |
| Flusso logico-teorico risolutivo | 15 | sequenza teorica coerente, contributo iniziale dello studente, uso corretto di definizioni, proprietà e formule, collegamento con output e controlli |
| Scomposizione input-output | 15 | tappe coerenti, output riutilizzati, controlli previsti, assenza di salti logici |
| Notebook e output computazionali | 20 | codice corretto, simulazioni, tabelle, grafici, riproducibilità, struttura ordinata del notebook |
| Prompt e rispetto dei regimi A/B/C | 15 | qualità degli input, vincoli, validazioni, uso corretto dei regimi, collegamento prompt-notebook |
| Controlli numerici e logici | 10 | probabilità, frequenze, $P_E\mid A_g$, formule $C_E$, $M$, $S$, massa in zero, verifica valore atteso totale |
| Interpretazione critica | 10 | ruolo dell’informazione, shortfall condizionato, soglie, massa in zero, limiti del modello, autonomia del commento finale |

---

## 16. Esito atteso e calibrazione qualitativa del caso

Il lavoro deve concludersi con:

1. notebook Jupyter eseguibile;
2. tracciato IA in formato Markdown;
3. tabelle dei parametri, delle frequenze, delle statistiche e delle medie condizionate;
4. grafici della distribuzione di $P_E$ e dello shortfall $S$;
5. evidenza della massa in zero dello shortfall;
6. stima di $\widehat{\mathbb{P}}(S>0)$ e $\widehat{\mathbb{P}}(S>s^\star)$;
7. verifica empirica della formula del valore atteso totale;
8. commento finale sul ruolo dell’informazione di scenario e sui limiti della simulazione.

Il caso è calibrato correttamente se produce una distinzione visibile tra i tre eventi della partizione:

1. $A_1$: shortfall atteso basso o nullo, coerente con normalizzazione energetica;
2. $A_2$: shortfall atteso positivo e intermedio;
3. $A_3$: shortfall atteso elevato e maggiore dispersione.

Il risultato atteso non è una previsione del prezzo dell’energia, ma una rappresentazione controllata del modo in cui l’informazione di scenario modifica la distribuzione rilevante dello shortfall.

### Possibili segnali di cattiva calibrazione

1. Le distribuzioni condizionate risultano troppo simili tra loro.
2. Le soglie implicite $120$ e $140$ rendono banali $\widehat{\mathbb{P}}(S>0)$ o $\widehat{\mathbb{P}}(S>s^\star)$.
3. La massa in zero è assente o totalizzante, rendendo poco interessante la distribuzione di $S$.
4. Le medie condizionate non sono ordinate in modo coerente con l’interpretazione economica dei tre regimi.
5. Il caso può essere risolto senza usare il valore atteso condizionato.
6. L’interpretazione finale diventa un semplice commento tecnico ai grafici, senza discutere il ruolo dell’informazione.