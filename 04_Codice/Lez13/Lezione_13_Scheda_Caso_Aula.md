# Lezione 13 — Scheda Caso Aula

## 1. Identificazione del caso

- **Lezione:** 13 — Applicazione in Python: programmazione lineare e ALM deterministico
- **Tipo di caso:** aula
- **Titolo:** Silicon Valley Bank 2023: piano ALM, sensitività e scenari di stress
- **Contesto sintetico:** crisi di Silicon Valley Bank del marzo 2023, utilizzata come riferimento finanziario per analizzare in forma stilizzata l'interazione tra composizione dell'attivo, fabbisogni di liquidità, capacità di funding e costo del funding.
- **Uso previsto:** sviluppo guidato in aula di un modello di programmazione lineare multiperiodale, implementato con un solver Python, seguito da analisi di sensitività univariata, stress test di fattibilità e scenario analysis.

La presente Scheda Caso costituisce la **specifica vincolante del lavoro**. Variabili, parametri, formule, ipotesi, output e controlli indicati non devono essere modificati durante lo svolgimento.

La Scheda Caso definisce il problema ma **non ne contiene la soluzione**.

---

## 2. Contesto e domanda quantitativa

Silicon Valley Bank operava in un contesto caratterizzato da una raccolta fortemente concentrata e da una rilevante esposizione verso attività a più lunga durata. Il rapido aumento dei tassi di interesse e i successivi deflussi di depositi resero centrale il problema della disponibilità di liquidità nelle diverse date.

Il caso qui considerato non ricostruisce quantitativamente il bilancio storico di SVB. Utilizza invece un modello didattico stilizzato, già introdotto nel Capitolo 12, nel quale una banca deve scegliere la composizione iniziale dell'attivo e gestire nel tempo:

1. i cash flow prodotti dalle diverse classi di attivo;
2. i fabbisogni di liquidità;
3. le giacenze trasferite da una data alla successiva;
4. il ricorso a funding esterno;
5. il rimborso del funding raccolto.

Il caso viene sviluppato in quattro momenti:

1. soluzione e verifica del modello benchmark;
2. sensitività univariata rispetto a tre driver;
3. ricerca della frontiera di fattibilità rispetto allo stress sui fabbisogni;
4. confronto di tre scenari nei quali i driver variano congiuntamente.

I tre driver sono:

- $\theta$: intensità dei fabbisogni di liquidità nelle prime due date;
- $\phi$: capacità massima di funding;
- $\psi$: costo del funding.

La domanda quantitativa è:

**come cambia il piano ALM ottimo di SVB al variare separatamente e congiuntamente del fabbisogno di liquidità, della capacità massima di funding e del costo del funding, e fino a quale livello di aumento dei fabbisogni iniziali il problema rimane ammissibile?**

L'analisi deve distinguere chiaramente:

- **sensitività univariata:** varia un solo parametro alla volta;
- **stress test di fattibilità:** si ricerca il passaggio da soluzione ammissibile a problema non ammissibile;
- **scenario analysis:** più driver vengono modificati congiuntamente secondo configurazioni assegnate.

---

## 3. Modello e struttura del problema

### 3.1 Variabili decisionali

La banca dispone al tempo iniziale di risorse complessive pari a $A_0$.

Le variabili di allocazione sono:

- $x_1$: cassa e riserve;
- $x_2$: titoli a breve scadenza;
- $x_3$: titoli a lunga scadenza;
- $x_4$: prestiti e impieghi meno liquidi.

Per $t=1,\ldots,4$:

$$
g_t\geq0
$$

rappresenta la giacenza di liquidità successiva al soddisfacimento del fabbisogno della data $t$.

Per $t=1,2,3$:

$$
u_t\geq0
$$

rappresenta il funding esterno raccolto alla data $t$, disponibile immediatamente e rimborsato alla data successiva.

### 3.2 Cash flow, fabbisogni e funding

La matrice:

$$
A^{\mathrm{CF}}=(a_{tj})
$$

descrive i cash flow temporali degli attivi, con:

$$
a_t'x
=
\sum_{j=1}^{4}a_{tj}x_j.
$$

I fabbisogni parametrizzati sono:

$$
d(\theta)
=
(30\theta,30\theta,22,15)'.
$$

La capacità massima di funding è:

$$
\bar u_t(\phi)
=
\phi\bar u_t,
$$

mentre il costo del funding è:

$$
r_t^u(\psi)
=
\psi r_t^u.
$$

Il parametro $\psi$ modifica sia il costo del funding nella funzione obiettivo sia il rimborso del funding nei bilanci temporali.

Le giacenze trasferite alla data successiva diventano disponibili per:

$$
(1+r_t^g)g_t.
$$

### 3.3 Funzione obiettivo

La banca massimizza:

$$
\Pi(x,g,u;\psi)
=
c'x
+
\sum_{t=1}^{3}r_t^g g_t
-
\sum_{t=1}^{3}\psi r_t^u u_t.
$$

Il problema è quindi:

$$
\max_{x,g,u}\Pi(x,g,u;\psi).
$$

Nell'implementazione Python deve essere rispettata la convenzione di minimizzazione utilizzata dal solver.

### 3.4 Vincoli

Le risorse iniziali soddisfano:

$$
\sum_{j=1}^{4}x_j=A_0.
$$

Il primo bilancio temporale è:

$$
a_1'x+u_1-g_1=d_1(\theta).
$$

Per $t=2,3$:

$$
a_t'x
+
(1+r_{t-1}^g)g_{t-1}
+
u_t
-
(1+\psi r_{t-1}^u)u_{t-1}
-
g_t
=
d_t(\theta).
$$

Alla data terminale:

$$
a_4'x
+
(1+r_3^g)g_3
-
(1+\psi r_3^u)u_3
-
g_4
=
d_4.
$$

Il vincolo prudenziale è:

$$
\ell'x\leq K.
$$

Il limite di concentrazione è:

$$
x_3\leq30.
$$

La capacità di funding soddisfa:

$$
0\leq u_t\leq\phi\bar u_t,
\qquad
t=1,2,3.
$$

Infine:

$$
x_j\geq0,
\qquad
j=1,\ldots,4,
$$

$$
g_t\geq0,
\qquad
t=1,\ldots,4.
$$

---

## 4. Parametri assegnati

### 4.1 Parametri benchmark

| Quantità | Valore |
|---|---|
| Risorse iniziali | $A_0=100$ |
| Redditività degli attivi | $c'=(0.010,0.025,0.040,0.050)$ |
| Perdite unitarie sotto stress | $\ell'=(0,0.02,0.15,0.08)$ |
| Fabbisogni benchmark | $d'=(30,30,22,15)$ |
| Rendimenti delle giacenze | ${r^g}'=(0.005,0.006,0.007)$ |
| Costi benchmark del funding | ${r^u}'=(0.015,0.020,0.025)$ |
| Capacità benchmark di funding | $\bar u'=(10,8,6)$ |
| Limite prudenziale | $K=7$ |
| Limite di concentrazione | $x_3\leq30$ |

La matrice dei cash flow è:

$$
A^{\mathrm{CF}}
=
\begin{pmatrix}
1.00 & 0.65 & 0.05 & 0.05\\
0.00 & 0.35 & 0.10 & 0.15\\
0.00 & 0.00 & 0.25 & 0.30\\
0.00 & 0.00 & 0.60 & 0.50
\end{pmatrix}.
$$

Le righe corrispondono alle date $t=1,\ldots,4$ e le colonne, nell'ordine, a:

$$
(x_1,x_2,x_3,x_4).
$$

### 4.2 Griglie di sensitività

Le sensitività univariate utilizzano le seguenti griglie:

| Parametro variato | Valori | Parametri mantenuti al benchmark |
|---|---|---|
| $\theta$ | $\{1.00,1.01,\ldots,1.10\}$ | $\phi=1$, $\psi=1$ |
| $\phi$ | $\{0.50,0.60,\ldots,1.50\}$ | $\theta=1$, $\psi=1$ |
| $\psi$ | $\{0.50,0.75,1.00,1.25,1.50,1.75,2.00\}$ | $\theta=1$, $\phi=1$ |

Per $\theta$, la griglia iniziale deve essere utilizzata anche per individuare l'intervallo compreso tra l'ultimo valore ammissibile e il primo valore non ammissibile; tale intervallo deve poi essere raffinato per localizzare:

$$
\theta_{\mathrm{crit}}.
$$

### 4.3 Scenari congiunti

| Scenario | $\theta$ | $\phi$ | $\psi$ |
|---|---:|---:|---:|
| Standard | 1.00 | 1.00 | 1.00 |
| Mediamente critico | 1.03 | 0.90 | 1.25 |
| Critico | 1.06 | 0.70 | 1.50 |

Lo scenario Standard coincide con il benchmark.

Gli scenari Mediamente critico e Critico modificano congiuntamente fabbisogni iniziali, capacità massima di funding e costo del funding.

Gli scenari costituiscono configurazioni deterministiche assegnate e non eventi ai quali siano associate probabilità.

---

## 5. Quantità da stimare o calcolare

Per il benchmark e per le analisi parametriche devono essere determinate le seguenti quantità.

### 5.1 Benchmark

Per:

$$
(\theta,\phi,\psi)
=
(1,1,1)
$$

devono essere calcolati:

1. soluzione ottima:

$$
x^*,
\qquad
g^*,
\qquad
u^*;
$$

2. valore ottimo:

$$
\Pi^*;
$$

3. residuali dei vincoli di uguaglianza;

4. slack dei vincoli di disuguaglianza;

5. bounds attivi;

6. principali valori marginali restituiti dal solver.

### 5.2 Sensitività univariate

Per ciascun parametro:

$$
p\in\{\theta,\phi,\psi\}
$$

e per ogni valore della relativa griglia devono essere determinati:

1. stato di fattibilità;

2. valore ottimo:

$$
\Pi^*(p);
$$

3. soluzione ottima:

$$
x^*(p),
\qquad
g^*(p),
\qquad
u^*(p);
$$

4. principali vincoli e bounds attivi;

5. principali valori marginali, quando economicamente informativi.

Devono inoltre essere calcolate le variazioni rispetto al benchmark:

$$
\Delta\Pi^*(p)
=
\Pi^*(p)-\Pi^*(1),
$$

$$
\Delta_{\%}\Pi^*(p)
=
100
\left[
\frac{\Pi^*(p)}{\Pi^*(1)}-1
\right],
$$

$$
\Delta x_j^*(p)
=
x_j^*(p)-x_j^*(1),
$$

$$
\Delta g_t^*(p)
=
g_t^*(p)-g_t^*(1),
$$

$$
\Delta u_t^*(p)
=
u_t^*(p)-u_t^*(1).
$$

Per il funding deve essere inoltre determinato:

$$
\rho_t^u(p)
=
\frac{u_t^*(p)}{\bar u_t(p)}.
$$

Quando il parametro variato non è $\phi$, il denominatore coincide con la capacità benchmark.

### 5.3 Frontiera di fattibilità

Per la sensitività rispetto a $\theta$ devono essere individuati:

1. l'ultimo valore ammissibile della griglia iniziale;

2. il primo valore non ammissibile;

3. un intervallo raffinato contenente:

$$
\theta_{\mathrm{crit}}.
$$

Il valore $\theta_{\mathrm{crit}}$ rappresenta esclusivamente la frontiera di fattibilità del modello stilizzato.

### 5.4 Scenario analysis

Per ciascuno degli scenari Standard, Mediamente critico e Critico devono essere determinati:

1. fattibilità;

2. valore ottimo:

$$
\Pi^*;
$$

3. soluzione ottima:

$$
x^*,
\qquad
g^*,
\qquad
u^*;
$$

4. principali vincoli e bounds attivi;

5. utilizzo della capacità di funding;

6. principali valori marginali, quando economicamente informativi.

Per gli scenari Mediamente critico e Critico deve essere inoltre calcolata la perdita di valore rispetto allo Standard:

$$
L_s
=
\Pi_{\mathrm{Standard}}^*
-
\Pi_s^*.
$$

---

## 6. Output richiesti

Gli output devono essere prodotti esclusivamente per configurazioni nelle quali il solver restituisce una soluzione valida e devono rendere distinguibili:

1. benchmark e relativa diagnostica;
2. sensitività univariate;
3. frontiera di fattibilità rispetto a $\theta$;
4. scenario analysis.

### 6.1 Risultati numerici

Devono essere riportati:

1. soluzione e valore ottimi del benchmark;

2. residuali dei vincoli di uguaglianza, slack dei vincoli di disuguaglianza e bounds attivi;

3. principali valori marginali;

4. per le sensitività a $\theta$, $\phi$ e $\psi$: fattibilità, valore e soluzione ottimi, variazioni rispetto al benchmark, utilizzo della capacità di funding e principali vincoli o bounds attivi;

5. intervallo raffinato contenente:

$$
\theta_{\mathrm{crit}};
$$

6. risultati dei tre scenari assegnati e perdita di valore degli scenari Mediamente critico e Critico rispetto allo Standard.

### 6.2 Tabelle

Devono essere prodotte le seguenti tabelle:

1. **Benchmark e parametri principali**;
2. **Soluzione benchmark**;
3. **Verifica dei bilanci temporali**;
4. **Vincoli, bounds e slack nel benchmark**;
5. **Valori marginali principali**;
6. **Sensitività a $\theta$**;
7. **Sensitività a $\phi$**;
8. **Sensitività a $\psi$**;
9. **Raffinamento della frontiera di fattibilità rispetto a $\theta$**;
10. **Confronto degli scenari**.

Le tabelle devono contenere le quantità necessarie a rappresentare i risultati definiti nella Sezione 5 e i controlli richiesti nella Sezione 7.

### 6.3 Grafici

Devono essere prodotti i seguenti grafici:

1. valore ottimo al variare di $\theta$;

2. variazione assoluta o percentuale del valore ottimo rispetto al benchmark al variare di $\theta$;

3. composizione ottima dell'attivo al variare di $\theta$;

4. variazioni dell'asset allocation rispetto al benchmark al variare di $\theta$;

5. funding ottimo e/o utilizzo della relativa capacità al variare di $\theta$;

6. giacenze ottime al variare di $\theta$;

7. sensitività rispetto a $\phi$, rappresentando almeno valore ottimo e comportamento del funding;

8. sensitività rispetto a $\psi$, rappresentando almeno valore ottimo e funding ottimo;

9. principali valori marginali lungo almeno una griglia informativa;

10. mappa dei principali vincoli attivi, almeno lungo la sensitività rispetto a $\theta$;

11. confronto del valore ottimo nei tre scenari;

12. confronto della composizione ottima dell'attivo nei tre scenari;

13. confronto del funding nei tre scenari;

14. confronto del profilo temporale delle giacenze nei tre scenari.

I grafici devono utilizzare esclusivamente configurazioni per le quali il solver restituisce una soluzione valida.

### 6.4 Regole di produzione

1. Tabelle e grafici devono essere generati direttamente dagli oggetti prodotti nel notebook.

2. I risultati di configurazioni non ammissibili non devono essere utilizzati o interpretati.

3. Configurazioni ammissibili e non ammissibili devono essere chiaramente distinguibili.

4. I valori numerici prodotti dal solver non devono essere ricopiati manualmente nelle celle successive.

5. Gli output devono essere rigenerabili mediante riesecuzione ordinata del notebook.

6. Non sono richieste esportazioni automatiche in file esterni, salvo indicazione esplicita del docente.

### 6.5 Funzione interpretativa

Gli output devono consentire di discutere:

1. effetti dei fabbisogni iniziali, della capacità di funding e del costo del funding sul piano ALM;

2. cambiamenti dei principali vincoli e bounds attivi;

3. posizione della frontiera di fattibilità rispetto a $\theta$;

4. differenze tra gli scenari Standard, Mediamente critico e Critico;

5. dipendenza delle conclusioni dalla struttura del modello stilizzato.

L'interpretazione deve basarsi esclusivamente su risultati numericamente validati.

---

## 7. Controlli richiesti

L'interpretazione finale deve utilizzare esclusivamente risultati provenienti da configurazioni per le quali il solver restituisce una soluzione valida.

### 7.1 Controlli numerici

Devono essere verificati:

1. stato di ottimizzazione valido del benchmark e di ogni configurazione utilizzata;

2. residuali dei bilanci temporali prossimi a zero entro una tolleranza dichiarata;

3. rispetto dei vincoli:

$$
\ell'x^*\leq7,
$$

$$
x_3^*\leq30,
$$

$$
0\leq u_t^*\leq\phi\bar u_t,
\qquad
t=1,2,3,
$$

e della non negatività delle variabili;

4. coerenza tra slack e classificazione dei vincoli come attivi o non attivi;

5. identificazione dei bounds attivi mediante la distanza dai rispettivi limiti;

6. verifica numerica di almeno un valore marginale mediante una piccola perturbazione del termine noto o del limite cui esso si riferisce.

I risultati relativi a configurazioni non ammissibili non devono essere utilizzati né interpretati economicamente.

### 7.2 Controlli logici e teorici

Devono essere verificati:

1. riproduzione del benchmark per:

$$
(\theta,\phi,\psi)
=
(1,1,1);
$$

2. variazione di un solo parametro alla volta nelle sensitività univariate;

3. azione corretta dei tre driver:
   - $\theta$ modifica esclusivamente i fabbisogni delle prime due date;
   - $\phi$ modifica esclusivamente la capacità massima di funding;
   - $\psi$ modifica sia il costo del funding nella funzione obiettivo sia il rimborso del funding nei bilanci temporali;

4. coerenza tra cambiamenti della soluzione e cambiamenti dei vincoli o bounds attivi;

5. associazione dei valori marginali al corretto vincolo o bilancio e loro interpretazione locale, tenendo conto della trasformazione del problema di massimizzazione nella convenzione di minimizzazione del solver;

6. distinzione tra vincolo attivo e valore marginale economicamente informativo;

7. individuazione della frontiera di fattibilità rispetto a $\theta$ mediante il passaggio tra configurazioni ammissibili e non ammissibili;

8. interpretazione di:

$$
\theta_{\mathrm{crit}}
$$

come frontiera del modello stilizzato e non come stima empirica dei deflussi storici di Silicon Valley Bank;

9. utilizzo esatto degli scenari assegnati nella Sezione 4.3;

10. distinzione tra sensitività univariata e scenario analysis.

### 7.3 Controlli computazionali

Devono essere verificati:

1. ordinamento dichiarato e invariato delle variabili decisionali;

2. compatibilità dimensionale di:

$$
f,
\qquad
A_{\mathrm{eq}},
\qquad
b_{\mathrm{eq}},
\qquad
A_{\mathrm{ub}},
\qquad
b_{\mathrm{ub}}
$$

e dei bounds;

3. corretta trasformazione:

$$
\max\Pi
\quad\longleftrightarrow\quad
\min(-\Pi);
$$

4. corretta parametrizzazione:

$$
d(\theta)
=
(30\theta,30\theta,22,15)',
$$

$$
0\leq u_t\leq\phi\bar u_t;
$$

5. applicazione di $\psi$ sia alla funzione obiettivo sia ai rimborsi del funding;

6. riproduzione della soluzione benchmark da parte della funzione parametrica valutata in:

$$
(1,1,1);
$$

7. utilizzo nelle tabelle e nei grafici esclusivamente di risultati provenienti da esecuzioni valide del solver;

8. mancata interpolazione o connessione artificiale di punti separati da configurazioni non ammissibili;

9. raffinamento della ricerca di:

$$
\theta_{\mathrm{crit}}
$$

soltanto dopo avere individuato sulla griglia iniziale l'ultimo valore ammissibile e il primo non ammissibile;

10. utilizzo senza modifiche delle configurazioni assegnate nella scenario analysis;

11. rigenerabilità di tabelle e grafici mediante riesecuzione ordinata del notebook;

12. eseguibilità integrale del notebook dall'inizio senza dipendenze da oggetti prodotti in esecuzioni precedenti non riproducibili.

Prima dell'interpretazione finanziaria finale devono risultare congiuntamente soddisfatti i controlli numerici, logico-teorici e computazionali sopra indicati.

---

## 8. Ipotesi e limiti del caso

### 8.1 Ipotesi modellistiche

Il modello assume che:

1. l'orizzonte sia deterministico e articolato in quattro date future;

2. le decisioni iniziali di allocazione siano assunte al tempo iniziale e rimangano invariate lungo l'orizzonte;

3. i cash flow degli attivi e i fabbisogni di liquidità siano deterministici all'interno di ciascuna configurazione parametrica;

4. le quantità siano divisibili e funzione obiettivo e vincoli siano lineari;

5. il funding raccolto alla data $t$ sia immediatamente disponibile e venga rimborsato alla data successiva;

6. capacità e costo del funding siano esogeni e agiscano secondo le parametrizzazioni assegnate;

7. nelle sensitività univariate vari un solo parametro alla volta, mentre gli scenari modifichino congiuntamente i driver secondo le configurazioni assegnate.

### 8.2 Semplificazioni adottate

Il caso utilizza una rappresentazione stilizzata nella quale:

1. le classi di attivo e i cash flow sono aggregati e descritti mediante coefficienti deterministici;

2. la liquidità è rappresentata attraverso bilanci temporali discreti;

3. il funding è descritto mediante capacità e costi assegnati;

4. il vincolo prudenziale è lineare;

5. non vengono modellati aggiustamenti endogeni di prezzi, tassi o costi conseguenti alle decisioni della banca.

### 8.3 Elementi esclusi

Il modello non include:

1. incertezza probabilistica sui fabbisogni e dinamiche stocastiche dei tassi;

2. variazioni endogene dei prezzi degli attivi, fire sales o feedback di mercato;

3. interazioni strategiche con depositanti, controparti o autorità;

4. rischio di credito dinamico e requisiti regolamentari completi;

5. decisioni adattive, struttura stocastica o multistadio;

6. una ricostruzione empirica completa della crisi di Silicon Valley Bank.

### 8.4 Limiti dell'interpretazione

Il caso è un modello didattico stilizzato ispirato alla crisi di Silicon Valley Bank del 2023.

Pertanto:

1. i parametri non rappresentano una ricostruzione puntuale del bilancio storico della banca;

2. sensitività e scenari descrivono la risposta del modello ai parametri assegnati e non relazioni causali empiricamente osservate;

3. la frontiera:

$$
\theta_{\mathrm{crit}}
$$

è una soglia di fattibilità del modello e non una stima dei deflussi storici effettivi;

4. i valori marginali hanno significato locale e possono cambiare al variare dell'insieme dei vincoli attivi;

5. gli scenari Standard, Mediamente critico e Critico sono configurazioni deterministiche di confronto e non scenari probabilizzati;

6. i risultati non devono essere estesi oltre le ipotesi, i vincoli e l'orizzonte dichiarati.