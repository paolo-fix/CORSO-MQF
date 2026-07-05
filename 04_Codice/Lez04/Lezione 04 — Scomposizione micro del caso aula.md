# Lezione 04 — Scomposizione micro del caso aula

## Caso aula

**Titolo:** Perdita obbligazionaria condizionata a regimi di tasso

Questa scomposizione articola il caso aula in tappe operative. Ogni tappa è trattata come modulo input-output:

$$
\text{input}_k
\longrightarrow
\text{operazione}_k
\longrightarrow
\text{output}_k
\longrightarrow
\text{uso in } k+1.
$$

La sequenza è pensata per generare successivamente:

1. il piano dei prompt virtuosi;
2. il notebook docente;
3. gli output numerici e grafici;
4. i controlli e l’interpretazione critica.

---

## Tappa 1 — Contesto e domanda quantitativa

### Input dalla tappa precedente

Nessun input computazionale. La tappa apre il caso.

### Obiettivo della tappa

Introdurre il contesto finanziario: ciclo di rialzo dei tassi, impatto dei rendimenti sul valore dei portafogli obbligazionari, necessità di valutare la perdita in presenza di scenari informativi.

La domanda quantitativa da fissare è:

$$
\text{Qual è la distribuzione della perdita } L
\text{ e come cambia la perdita attesa condizionando sui regimi di tasso?}
$$

### Regime prevalente

**Regime A — Ricognizione teorico-modellistica.**

### Oggetti teorici coinvolti

- portafoglio obbligazionario;
- rendimento di mercato;
- shock di rendimento;
- perdita;
- informazione di scenario;
- previsione non condizionata;
- previsione condizionata.

### Operazione computazionale richiesta

Nessuna operazione computazionale. La tappa produce una specifica testuale e concettuale.

### Output prodotto

Una formulazione chiara del problema:

- contesto storico-finanziario;
- domanda quantitativa;
- distinzione tra oggetto finanziario e modello probabilistico;
- chiarimento che il caso è simulativo e non previsionale.

### Controllo numerico, logico o interpretativo

Controllo logico: il problema non deve essere formulato come previsione dei tassi reali futuri, ma come simulazione didattica di perdite condizionate a regimi informativi.

### Uso dell’output nella tappa successiva

La domanda quantitativa guida la definizione delle variabili e della formula di perdita.

---

## Tappa 2 — Variabili e formula della perdita

### Input dalla tappa precedente

Domanda quantitativa e contesto finanziario.

### Obiettivo della tappa

Definire le grandezze finanziarie e la relazione tra shock di tasso e perdita del portafoglio.

### Regime prevalente

**Regime A — Ricognizione teorico-modellistica.**

### Oggetti teorici coinvolti

- valore iniziale del portafoglio $V_0$;
- duration modificata $D$;
- shock di rendimento $\Delta y$;
- variazione di valore $\Delta V$;
- perdita $L$.

La relazione finanziaria di base è:

$$
\frac{\Delta P}{P} \simeq -D\Delta y.
$$

Per il portafoglio:

$$
\Delta V \simeq -D V_0 \Delta y.
$$

La perdita è definita come:

$$
L=-\Delta V\simeq D V_0 \Delta y.
$$

### Operazione computazionale richiesta

Nessuna simulazione. Si definisce la formula che sarà implementata in codice nelle tappe successive.

### Output prodotto

Specificazione teorica:

$$
L = D V_0 \Delta y.
$$

### Controllo numerico, logico o interpretativo

Controllo del segno:

- se $\Delta y>0$, i rendimenti aumentano e il portafoglio perde valore;
- se $\Delta y<0$, i rendimenti diminuiscono e il portafoglio può registrare un guadagno, cioè $L<0$.

### Uso dell’output nella tappa successiva

La formula di perdita sarà applicata agli shock simulati $\Delta y$ dopo avere definito gli stati informativi.

---

## Tappa 3 — Stati informativi

### Input dalla tappa precedente

Formula della perdita:

$$
L = D V_0 \Delta y.
$$

### Obiettivo della tappa

Definire l’informazione disponibile prima della valutazione della perdita. L’informazione è rappresentata da uno stato discreto $Z$.

### Regime prevalente

**Regime A — Ricognizione teorico-modellistica.**

### Oggetti teorici coinvolti

- variabile casuale discreta $Z$;
- eventi informativi $A_1,A_2,A_3$;
- partizione dello spazio degli esiti;
- sigma-algebra informativa $\mathcal{G}$.

Si definisce:

$$
Z:\Omega\to\{1,2,3\}.
$$

Gli eventi informativi sono:

$$
A_1=\{Z=1\},
\qquad
A_2=\{Z=2\},
\qquad
A_3=\{Z=3\}.
$$

Interpretazione:

| Stato | Descrizione | Interpretazione finanziaria |
|---|---|---|
| $A_1$ | Disinflazione ordinata | rendimenti stabili o in lieve riduzione |
| $A_2$ | Inflazione persistente | rialzo moderato dei rendimenti |
| $A_3$ | Repricing severo | rialzo marcato e maggiore volatilità |

La sigma-algebra informativa è:

$$
\mathcal{G}=\sigma(A_1,A_2,A_3).
$$

### Operazione computazionale richiesta

Nessuna simulazione. Si definisce la struttura informativa che sarà codificata nel notebook.

### Output prodotto

Definizione degli stati, della partizione e di $\mathcal{G}$.

### Controllo numerico, logico o interpretativo

Controllo logico: $Z$ non è la perdita e non è lo shock di rendimento. È l’informazione di scenario rispetto alla quale si condizionano le distribuzioni.

### Uso dell’output nella tappa successiva

Gli stati informativi permettono di assegnare probabilità e distribuzioni condizionate agli shock di rendimento.

---

## Tappa 4 — Parametri di simulazione

### Input dalla tappa precedente

Stati informativi $A_1,A_2,A_3$ e formula della perdita.

### Obiettivo della tappa

Fissare i parametri finanziari, probabilistici e computazionali della simulazione.

### Regime prevalente

**Regime A con transizione verso Regime B.**

La scelta dei parametri è ancora modellistica; la loro organizzazione in tabelle e strutture dati prepara il codice.

### Oggetti teorici coinvolti

- probabilità degli stati;
- distribuzioni condizionate;
- numero di simulazioni;
- soglia di perdita;
- replicabilità tramite seme casuale.

Parametri finanziari:

$$
V_0=10.000.000,
\qquad
D=6,
\qquad
\ell=500.000.
$$

Probabilità degli stati:

$$
\mathbb{P}(A_1)=0,35,
\qquad
\mathbb{P}(A_2)=0,45,
\qquad
\mathbb{P}(A_3)=0,20.
$$

Distribuzioni condizionate:

$$
\Delta y\mid A_1\sim\mathcal{N}(-0,0010,0,0040^2),
$$

$$
\Delta y\mid A_2\sim\mathcal{N}(0,0030,0,0060^2),
$$

$$
\Delta y\mid A_3\sim\mathcal{N}(0,0100,0,0100^2).
$$

Parametri computazionali:

$$
n=50.000,
\qquad
seed=12345.
$$

### Operazione computazionale richiesta

Preparare una rappresentazione ordinata dei parametri, ad esempio tramite dizionari Python o tabelle `pandas`.

### Output prodotto

- tabella dei parametri finanziari;
- tabella degli stati;
- tabella delle probabilità;
- tabella dei parametri condizionati;
- oggetti Python utilizzabili nelle simulazioni.

### Controllo numerico, logico o interpretativo

Controllo numerico:

$$
0,35+0,45+0,20=1.
$$

Controllo interpretativo: i parametri devono produrre regimi economicamente distinguibili.

### Uso dell’output nella tappa successiva

Le probabilità degli stati sono usate per simulare $Z$.

---

## Tappa 5 — Simulazione di $Z$

### Input dalla tappa precedente

Probabilità degli stati:

$$
(0,35,\;0,45,\;0,20).
$$

Numero di simulazioni:

$$
n=50.000.
$$

Seme casuale:

$$
seed=12345.
$$

### Obiettivo della tappa

Simulare una sequenza di stati informativi:

$$
Z_1,\ldots,Z_n.
$$

Ogni simulazione rappresenta uno scenario possibile del regime dei tassi.

### Regime prevalente

**Regime B — Traduzione operativa in codice.**

### Oggetti teorici coinvolti

- variabile casuale discreta;
- distribuzione di probabilità su un insieme finito;
- frequenze empiriche.

### Operazione computazionale richiesta

Utilizzare Python per estrarre $n$ realizzazioni della variabile $Z$ secondo le probabilità assegnate.

### Output prodotto

Un vettore simulato:

$$
(z_1,\ldots,z_n).
$$

Una tabella di frequenze:

| Stato | Probabilità teorica | Frequenza empirica | Numero simulazioni |
|---|---:|---:|---:|

### Controllo numerico, logico o interpretativo

Controllo numerico: le frequenze empiriche devono essere vicine alle probabilità teoriche.

Controllo logico: tutti e tre gli stati devono essere rappresentati da un numero sufficiente di osservazioni.

### Uso dell’output nella tappa successiva

Per ogni simulazione, il valore di $Z_i$ determina da quale distribuzione condizionata estrarre lo shock $\Delta y_i$.

---

## Tappa 6 — Simulazione di $\Delta y\mid Z$

### Input dalla tappa precedente

Sequenza simulata degli stati:

$$
z_1,\ldots,z_n.
$$

Parametri condizionati:

$$
(\mu_g,\sigma_g),
\qquad g=1,2,3.
$$

### Obiettivo della tappa

Simulare uno shock di rendimento per ogni scenario, usando la distribuzione condizionata corrispondente allo stato osservato.

### Regime prevalente

**Regime B — Traduzione operativa in codice.**

### Oggetti teorici coinvolti

- distribuzione condizionata;
- variabile casuale continua;
- simulazione Monte Carlo;
- miscela di distribuzioni condizionate.

Per ogni simulazione:

$$
\Delta y_i \mid Z_i=g
\sim
\mathcal{N}(\mu_g,\sigma_g^2).
$$

### Operazione computazionale richiesta

Generare un vettore:

$$
(\Delta y_1,\ldots,\Delta y_n),
$$

dove ogni shock è simulato condizionatamente allo stato corrispondente.

### Output prodotto

Dataset simulato con almeno le colonne:

| simulazione | stato | descrizione stato | delta_y |
|---:|---:|---|---:|

### Controllo numerico, logico o interpretativo

Controllo numerico: per ciascuno stato, la media empirica e la deviazione standard empirica di $\Delta y$ devono essere ragionevolmente vicine ai parametri teorici $\mu_g$ e $\sigma_g$.

### Uso dell’output nella tappa successiva

Gli shock simulati $\Delta y_i$ sono trasformati in perdite $L_i$ mediante la formula di duration.

---

## Tappa 7 — Costruzione di $L$

### Input dalla tappa precedente

Shock simulati:

$$
\Delta y_1,\ldots,\Delta y_n.
$$

Parametri finanziari:

$$
V_0=10.000.000,
\qquad
D=6.
$$

### Obiettivo della tappa

Costruire la perdita simulata del portafoglio in ciascuno scenario.

### Regime prevalente

**Regime B — Traduzione operativa in codice.**

### Oggetti teorici coinvolti

- trasformazione di variabile casuale;
- perdita come variabile casuale derivata;
- formula di duration.

Per ogni simulazione:

$$
L_i = D V_0 \Delta y_i.
$$

### Operazione computazionale richiesta

Aggiungere al dataset una colonna `loss` calcolata dalla formula:

$$
L = D V_0 \Delta y.
$$

### Output prodotto

Dataset simulato con almeno le colonne:

| simulazione | stato | descrizione stato | delta_y | loss |
|---:|---:|---|---:|---:|

### Controllo numerico, logico o interpretativo

Controllo del segno:

- se $\Delta y_i>0$, allora $L_i>0$;
- se $\Delta y_i<0$, allora $L_i<0$.

Controllo dell’ordine di grandezza: con $D=6$ e $V_0=10.000.000$, uno shock di 100 punti base produce una perdita approssimata di:

$$
6 \times 10.000.000 \times 0,01 = 600.000.
$$

### Uso dell’output nella tappa successiva

La variabile $L$ diventa l’oggetto principale per analizzare la distribuzione empirica delle perdite.

---

## Tappa 8 — Distribuzione empirica della perdita

### Input dalla tappa precedente

Dataset con perdite simulate:

$$
L_1,\ldots,L_n.
$$

### Obiettivo della tappa

Descrivere la distribuzione empirica della perdita non condizionata.

### Regime prevalente

**Regime B con avvio del Regime C.**

La produzione di statistiche e grafici è operativa; la lettura della forma distributiva introduce la verifica critica.

### Oggetti teorici coinvolti

- distribuzione empirica;
- media;
- deviazione standard;
- minimo;
- massimo;
- quantili descrittivi.

### Operazione computazionale richiesta

Calcolare statistiche descrittive e produrre un grafico della distribuzione empirica di $L$.

### Output prodotto

Tabella descrittiva:

| Statistica | Valore |
|---|---:|
| media |  |
| deviazione standard |  |
| minimo |  |
| massimo |  |
| quantile 5% |  |
| mediana |  |
| quantile 95% |  |
| quantile 99% |  |

Grafico:

- istogramma della perdita;
- eventuale ECDF della perdita.

### Controllo numerico, logico o interpretativo

Controllo interpretativo: la distribuzione non condizionata è una miscela dei tre regimi. Non deve essere letta come se provenisse da un unico regime omogeneo.

### Uso dell’output nella tappa successiva

La distribuzione empirica consente di calcolare quantili di rischio e probabilità di superamento soglia.

---

## Tappa 9 — Quantili e probabilità di superamento soglia

### Input dalla tappa precedente

Perdite simulate:

$$
L_1,\ldots,L_n.
$$

Soglia:

$$
\ell=500.000.
$$

### Obiettivo della tappa

Stimare misure empiriche di rischio associate alla coda destra della distribuzione della perdita.

### Regime prevalente

**Regime B con controllo C.**

### Oggetti teorici coinvolti

- evento di superamento soglia;
- probabilità empirica;
- quantili;
- indicatore di evento.

L’evento di interesse è:

$$
B=\{L>\ell\}.
$$

La probabilità da stimare è:

$$
\mathbb{P}(L>\ell).
$$

La stima empirica è:

$$
\widehat{\mathbb{P}}(L>\ell)
=
\frac{1}{n}
\sum_{i=1}^{n}
\mathbf{1}_{\{L_i>\ell\}}.
$$

### Operazione computazionale richiesta

Calcolare:

- quantile al 95%;
- quantile al 99%;
- probabilità empirica di superamento della soglia;
- grafico della distribuzione con soglia evidenziata.

### Output prodotto

Tabella:

| Quantità | Stima empirica |
|---|---:|
| $q_{0,95}(L)$ |  |
| $q_{0,99}(L)$ |  |
| $\widehat{\mathbb{P}}(L>\ell)$ |  |

Grafico:

- istogramma di $L$ con linea verticale in corrispondenza di $\ell$.

### Controllo numerico, logico o interpretativo

Controllo logico: la soglia deve essere confrontabile con la scala della perdita prodotta dalla simulazione.

Controllo interpretativo: una probabilità di superamento soglia non è una previsione puntuale, ma una frequenza stimata nel modello simulativo.

### Uso dell’output nella tappa successiva

Dopo avere analizzato il rischio non condizionato, si passa alla perdita attesa condizionata sui regimi informativi.

---

## Tappa 10 — Valori attesi condizionati

### Input dalla tappa precedente

Dataset simulato con:

- stato $Z_i$;
- perdita $L_i$.

### Obiettivo della tappa

Stimare le perdite attese condizionate su ciascun regime informativo.

### Regime prevalente

**Regime B con forte componente C.**

### Oggetti teorici coinvolti

- valore atteso condizionato rispetto a un evento;
- partizione;
- valore atteso condizionato rispetto a una sigma-algebra;
- previsione condizionata.

Per ciascuno stato:

$$
\mathbb{E}[L\mid A_g],
\qquad g=1,2,3.
$$

La stima empirica è:

$$
\widehat{\mathbb{E}}[L\mid A_g]
=
\frac{1}{n_g}
\sum_{i:Z_i=g} L_i,
$$

dove $n_g$ è il numero di simulazioni nello stato $g$.

Il valore atteso condizionato rispetto a $\mathcal{G}$ è:

$$
\mathbb{E}[L\mid\mathcal{G}]
=
\sum_{g=1}^{3}
\mathbb{E}[L\mid A_g]\mathbf{1}_{A_g}.
$$

### Operazione computazionale richiesta

Raggruppare il dataset per stato e calcolare:

- numero di simulazioni per stato;
- media della perdita per stato;
- deviazione standard della perdita per stato;
- quantili condizionati eventuali.

### Output prodotto

Tabella:

| Stato | Numero simulazioni | Frequenza | Perdita attesa condizionata | Deviazione standard |
|---|---:|---:|---:|---:|

Grafico:

- barplot delle perdite attese condizionate;
- eventuale confronto grafico tra distribuzioni condizionate.

### Controllo numerico, logico o interpretativo

Controllo interpretativo:

- il regime di repricing severo dovrebbe avere la perdita attesa più elevata;
- il regime di disinflazione ordinata può presentare perdita attesa negativa;
- l’informazione $Z$ modifica la previsione, ma non elimina la dispersione interna a ciascun regime.

### Uso dell’output nella tappa successiva

Le perdite attese condizionate sono utilizzate per verificare la formula del valore atteso totale.

---

## Tappa 11 — Verifica della formula del valore atteso totale

### Input dalla tappa precedente

- media empirica non condizionata della perdita;
- frequenze empiriche degli stati;
- medie empiriche condizionate.

### Obiettivo della tappa

Verificare empiricamente la coerenza tra media non condizionata e media pesata delle medie condizionate.

### Regime prevalente

**Regime C — Verifica e interpretazione critica.**

### Oggetti teorici coinvolti

- formula del valore atteso totale;
- media non condizionata;
- media condizionata;
- partizione informativa.

La relazione teorica è:

$$
\mathbb{E}[L]
=
\sum_{g=1}^{3}
\mathbb{P}(A_g)\mathbb{E}[L\mid A_g].
$$

La verifica empirica confronta:

$$
\widehat{\mathbb{E}}[L]
$$

con:

$$
\sum_{g=1}^{3}
\widehat{\mathbb{P}}(A_g)
\widehat{\mathbb{E}}[L\mid A_g].
$$

### Operazione computazionale richiesta

Calcolare:

1. media empirica diretta di $L$;
2. media pesata delle medie condizionate;
3. differenza assoluta tra le due quantità;
4. eventuale differenza relativa.

### Output prodotto

Tabella:

| Quantità | Valore |
|---|---:|
| Media empirica non condizionata |  |
| Media pesata delle medie condizionate |  |
| Differenza assoluta |  |
| Differenza relativa |  |

### Controllo numerico, logico o interpretativo

Controllo numerico: la differenza deve essere nulla o trascurabile, salvo arrotondamenti.

Controllo concettuale: la verifica non è una proprietà specifica del modello normale, ma deriva dalla struttura della partizione informativa.

### Uso dell’output nella tappa successiva

La verifica consente di passare dall’esecuzione tecnica alla discussione critica del significato finanziario e dei limiti del modello.

---

## Tappa 12 — Interpretazione critica

### Input dalla tappa precedente

Tutti gli output del notebook:

- statistiche descrittive;
- quantili;
- probabilità di superamento soglia;
- perdite attese condizionate;
- verifica del valore atteso totale;
- grafici.

### Obiettivo della tappa

Formulare una lettura finanziaria e metodologica dei risultati.

### Regime prevalente

**Regime C — Verifica e interpretazione critica.**

### Oggetti teorici coinvolti

- previsione non condizionata;
- previsione condizionata;
- informazione disponibile;
- incertezza residua;
- limiti del modello;
- distinzione tra simulazione didattica e previsione empirica.

### Operazione computazionale richiesta

Nessuna nuova operazione necessaria. Eventuali calcoli aggiuntivi devono essere giustificati come controlli.

### Output prodotto

Commento finale strutturato su quattro punti:

1. Che cosa indica la distribuzione non condizionata della perdita.
2. Come cambiano le perdite attese passando da $\mathbb{E}[L]$ a $\mathbb{E}[L\mid A_g]$.
3. Quale ruolo svolge l’informazione $Z$.
4. Quali sono i principali limiti del modello.

### Controllo numerico, logico o interpretativo

Controllo interpretativo finale:

- non confondere condizionamento con eliminazione del rischio;
- non confondere simulazione con previsione;
- non attribuire alla duration lineare una validità globale;
- non trasformare il caso in un modello completo di rischio di tasso.

### Uso dell’output nella tappa successiva

La tappa conclude il caso aula e fornisce la base per:

- costruire il caso take-home isomorfo;
- definire la rubrica di valutazione;
- preparare il template del tracciato AI dello studente.