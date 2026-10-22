# Lezione 13 — Scheda Caso TakeHome

## 1. Identificazione del caso

- **Lezione:** 13 — Applicazione in Python: programmazione lineare e ALM deterministico
- **Tipo di caso:** TakeHome
- **Titolo:** First Republic Bank 2023: due ondate di deposit run e vincoli di ristrutturazione del bilancio
- **Contesto sintetico:** crisi di First Republic Bank del 2023, utilizzata come riferimento finanziario per analizzare in forma stilizzata un problema ALM caratterizzato da attività creditizie a lunga durata, una quota minima di attività legacy e due ondate distinte di fabbisogno di liquidità.
- **Uso previsto:** sviluppo autonomo di un modello di programmazione lineare multiperiodale, con traduzione in forma solver, soluzione benchmark, sensitività univariate e scenario analysis.

La presente Scheda Caso costituisce la **specifica vincolante del lavoro**. Variabili, parametri, formule, ipotesi, output e controlli indicati non devono essere modificati durante lo svolgimento.

La Scheda Caso definisce il problema ma **non ne contiene la soluzione**.

---

## 2. Contesto e domanda quantitativa

First Republic Bank operava con una forte presenza di clientela ad alta patrimonializzazione e con una rilevante componente di prestiti e mutui a lunga durata. La struttura della raccolta presentava inoltre una quota elevata di depositi non assicurati.

Dopo il fallimento di Silicon Valley Bank e Signature Bank, la perdita di fiducia dei depositanti determinò deflussi molto rilevanti. La banca riuscì inizialmente a fronteggiare le richieste di liquidità, ma il protrarsi della pressione sulla raccolta e la difficoltà di ristrutturare rapidamente il bilancio ridussero progressivamente le opzioni disponibili.

Il caso qui considerato non ricostruisce quantitativamente il bilancio storico di First Republic. Utilizza invece un modello didattico stilizzato, distinto da quello del Caso Aula SVB, nel quale:

1. sono presenti cinque classi di attivo;
2. una quota minima di attività a lunga durata deve essere mantenuta;
3. la pressione di liquidità si manifesta in due ondate separate;
4. la capacità di funding può ridursi.

I tre driver analizzati sono:

- $\alpha$: intensità della prima ondata di deflussi;
- $\beta$: intensità della seconda ondata di deflussi;
- $\phi$: capacità massima di funding.

La domanda quantitativa è:

**come deve essere costruito il piano ALM ottimo di First Republic in presenza di una quota minima di attività legacy e come cambia tale piano al variare dell'intensità della prima ondata di deflussi, della seconda ondata e della capacità disponibile di funding?**

L'analisi deve consentire anche di confrontare gli effetti di uno shock che si manifesta all'inizio dell'orizzonte con quelli di uno shock che si manifesta alla data terminale.

---

## 3. Modello e struttura del problema

### 3.1 Variabili decisionali

La banca dispone al tempo iniziale di risorse complessive pari a $A_0$.

Le variabili di allocazione sono:

- $x_1$: cassa e riserve;
- $x_2$: titoli a breve scadenza;
- $x_3$: mutui residenziali a lunga durata;
- $x_4$: prestiti immobiliari commerciali;
- $x_5$: altri prestiti e crediti a clientela.

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
\sum_{j=1}^{5}a_{tj}x_j.
$$

I fabbisogni parametrizzati sono:

$$
d(\alpha,\beta)
=
(32\alpha,18,14,32\beta)'.
$$

Il parametro $\alpha$ modifica esclusivamente il fabbisogno della prima data, mentre $\beta$ modifica esclusivamente quello della quarta data.

La capacità massima di funding è:

$$
\bar u_t(\phi)
=
\phi\bar u_t.
$$

Le giacenze trasferite alla data successiva diventano disponibili per:

$$
(1+r_t^g)g_t,
$$

mentre il funding raccolto alla data $t$ deve essere rimborsato alla data successiva per:

$$
(1+r_t^u)u_t.
$$

### 3.3 Funzione obiettivo

La banca massimizza:

$$
\Pi(x,g,u)
=
c'x
+
\sum_{t=1}^{3}r_t^g g_t
-
\sum_{t=1}^{3}r_t^u u_t.
$$

Il problema è quindi:

$$
\max_{x,g,u}\Pi(x,g,u).
$$

Nell'implementazione Python deve essere rispettata la convenzione di minimizzazione utilizzata dal solver.

### 3.4 Vincoli

Le risorse iniziali soddisfano:

$$
\sum_{j=1}^{5}x_j=A_0.
$$

Il primo bilancio temporale è:

$$
a_1'x+u_1-g_1=d_1(\alpha).
$$

Per $t=2,3$:

$$
a_t'x
+
(1+r_{t-1}^g)g_{t-1}
+
u_t
-
(1+r_{t-1}^u)u_{t-1}
-
g_t
=
d_t.
$$

Alla data terminale:

$$
a_4'x
+
(1+r_3^g)g_3
-
(1+r_3^u)u_3
-
g_4
=
d_4(\beta).
$$

Il vincolo prudenziale è:

$$
\ell'x\leq K.
$$

Il vincolo legacy è:

$$
x_3+x_4\geq35.
$$

Il limite sugli altri prestiti è:

$$
x_5\leq35.
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
j=1,\ldots,5,
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
| Redditività degli attivi | $c'=(0.008,0.022,0.035,0.045,0.050)$ |
| Perdite unitarie sotto stress | $\ell'=(0,0.015,0.060,0.100,0.120)$ |
| Fabbisogni benchmark | $d'=(32,18,14,32)$ |
| Rendimenti delle giacenze | ${r^g}'=(0.004,0.005,0.006)$ |
| Costi del funding | ${r^u}'=(0.018,0.025,0.040)$ |
| Capacità benchmark di funding | $\bar u'=(4,3,2)$ |
| Limite prudenziale | $K=7.5$ |
| Vincolo legacy | $x_3+x_4\geq35$ |
| Limite sugli altri prestiti | $x_5\leq35$ |

La matrice dei cash flow è:

$$
A^{\mathrm{CF}}
=
\begin{pmatrix}
1.00 & 0.70 & 0.05 & 0.05 & 0.10\\
0.00 & 0.30 & 0.10 & 0.15 & 0.20\\
0.00 & 0.00 & 0.25 & 0.30 & 0.30\\
0.00 & 0.00 & 0.60 & 0.50 & 0.40
\end{pmatrix}.
$$

Le righe corrispondono alle date $t=1,\ldots,4$ e le colonne, nell'ordine, a:

$$
(x_1,x_2,x_3,x_4,x_5).
$$

### 4.2 Griglie di sensitività

Le sensitività univariate utilizzano le seguenti griglie:

| Parametro variato | Valori | Parametri mantenuti al benchmark |
|---|---|---|
| $\alpha$ | $\{0.90,0.95,1.00,1.05,1.10,1.15\}$ | $\beta=1$, $\phi=1$ |
| $\beta$ | $\{0.90,0.95,1.00,1.05,1.10,1.15\}$ | $\alpha=1$, $\phi=1$ |
| $\phi$ | $\{0.30,0.40,\ldots,1.30\}$ | $\alpha=1$, $\beta=1$ |

Le sensitività ad $\alpha$ e $\beta$ devono essere sviluppate separatamente prima del loro confronto.

### 4.3 Scenari congiunti

| Scenario | $\alpha$ | $\beta$ | $\phi$ |
|---|---:|---:|---:|
| Standard | 1.00 | 1.00 | 1.00 |
| Mediamente critico | 1.03 | 1.03 | 0.90 |
| Critico | 1.06 | 1.06 | 0.75 |

Lo scenario Standard coincide con il benchmark.

Gli scenari Mediamente critico e Critico modificano congiuntamente l'intensità delle due ondate di fabbisogno e la capacità massima di funding.

Gli scenari costituiscono configurazioni deterministiche assegnate e non eventi ai quali siano associate probabilità.

---

## 5. Quantità da stimare o calcolare

Per il benchmark e per le analisi parametriche devono essere determinate le seguenti quantità.

### 5.1 Benchmark

Per:

$$
(\alpha,\beta,\phi)
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
p\in\{\alpha,\beta,\phi\}
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

### 5.3 Confronto tra prima e seconda ondata

Le sensitività ad $\alpha$ e a $\beta$ devono essere confrontate rispetto a:

1. valore ottimo;

2. composizione dell'attivo;

3. giacenze;

4. funding;

5. principali vincoli e bounds attivi;

6. stato di fattibilità.

Il confronto deve verificare se uno stesso aumento relativo del fabbisogno produce effetti differenti quando si manifesta alla prima data oppure alla data terminale.

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

Gli output devono essere prodotti esclusivamente a partire da configurazioni per le quali il solver restituisce una soluzione valida.

Devono consentire di distinguere chiaramente:

1. soluzione benchmark;
2. diagnostica della soluzione;
3. sensitività univariate;
4. confronto tra prima e seconda ondata;
5. scenario analysis;
6. ruolo del vincolo legacy.

### 6.1 Risultati numerici

Devono essere riportati almeno:

1. soluzione ottima benchmark:

$$
x^*,
\qquad
g^*,
\qquad
u^*;
$$

2. valore ottimo benchmark:

$$
\Pi^*;
$$

3. residuali dei vincoli di uguaglianza;

4. slack dei vincoli di disuguaglianza;

5. bounds attivi;

6. principali valori marginali restituiti dal solver;

7. risultati delle sensitività rispetto a:

$$
\alpha,
\qquad
\beta,
\qquad
\phi;
$$

8. variazioni rispetto al benchmark:

$$
\Delta\Pi^*(p),
\qquad
\Delta x_j^*(p),
\qquad
\Delta g_t^*(p),
\qquad
\Delta u_t^*(p);
$$

9. rapporti di utilizzo della capacità di funding:

$$
\rho_t^u(p)
=
\frac{u_t^*(p)}{\bar u_t(p)};
$$

10. stato di fattibilità per ciascuna configurazione parametrica;

11. principali vincoli e bounds attivi;

12. confronto tra gli effetti di uno shock alla prima data e alla data terminale;

13. comportamento del vincolo legacy:

$$
x_3+x_4\geq35;
$$

14. risultati dei tre scenari assegnati;

15. perdita di valore degli scenari Mediamente critico e Critico rispetto allo Standard:

$$
L_s
=
\Pi_{\mathrm{Standard}}^*
-
\Pi_s^*.
$$

### 6.2 Tabelle

Devono essere prodotte le seguenti tabelle:

1. **Benchmark e diagnostica**;

2. **Sensitività ad $\alpha$**;

3. **Sensitività a $\beta$**;

4. **Sensitività a $\phi$**;

5. **Confronto degli scenari**;

6. **Controllo del vincolo legacy**.

Le tabelle devono contenere le quantità necessarie a rappresentare gli output definiti nella Sezione 5 e i controlli richiesti nella Sezione 7.

Per il vincolo legacy deve essere resa osservabile la distinzione tra la forma economica:

$$
x_3+x_4\geq L,
\qquad
L=35,
$$

e la forma utilizzata dal solver:

$$
-x_3-x_4\leq b,
\qquad
b=-L.
$$

Se:

$$
m
=
\frac{\partial F^*}{\partial b},
\qquad
F=-\Pi,
$$

il valore marginale deve essere interpretato e verificato coerentemente con:

$$
\frac{\partial\Pi^*}{\partial L}
=
m.
$$

La relazione ha significato locale e deve essere verificata, quando informativa, mediante una piccola perturbazione del limite $L$.


### 6.3 Grafici

Devono essere prodotti i seguenti grafici:

1. valore ottimo al variare di $\alpha$;

2. valore ottimo al variare di $\beta$;

3. valore ottimo al variare di $\phi$;

4. composizione ottima dell'attivo lungo almeno una sensitività informativa;

5. utilizzo della capacità di funding lungo la sensitività rispetto a $\phi$;

6. confronto diretto tra gli effetti delle variazioni di $\alpha$ e $\beta$.

I grafici devono utilizzare esclusivamente configurazioni ammissibili.

### 6.4 Regole di produzione

1. Tabelle e grafici devono essere generati direttamente dagli oggetti prodotti nel notebook.

2. Non devono essere utilizzati o interpretati valori della soluzione quando il solver segnala una configurazione non ammissibile.

3. Le configurazioni ammissibili e non ammissibili devono essere distinte chiaramente.

4. Non devono essere inseriti manualmente nelle celle successive valori numerici prodotti in precedenza dal solver.

5. I punti separati da configurazioni non ammissibili non devono essere collegati graficamente come se appartenessero a una relazione continua.

6. Gli output devono essere rigenerabili mediante riesecuzione ordinata del notebook.

7. Non devono essere previste esportazioni automatiche in file esterni, salvo indicazione esplicita del docente.

### 6.5 Funzione interpretativa

Gli output devono consentire di discutere:

1. come cambia il piano ALM al variare del fabbisogno della prima data;

2. come cambia il piano ALM al variare del fabbisogno terminale;

3. perché shock relativi analoghi nelle due date possano produrre effetti differenti;

4. come la capacità di funding influenzi la soluzione;

5. quale ruolo svolga il vincolo legacy;

6. quali vincoli e bounds diventino economicamente rilevanti;

7. come differiscano Standard, Mediamente critico e Critico;

8. quali conclusioni dipendano dalla struttura del modello stilizzato.

L'interpretazione finale deve basarsi esclusivamente su risultati numericamente validati.

---

## 7. Controlli richiesti

L'interpretazione finale deve utilizzare esclusivamente risultati provenienti da configurazioni per le quali il solver restituisce una soluzione valida.

### 7.1 Controlli numerici

Devono essere verificati:

1. stato di ottimizzazione valido del benchmark e di ogni configurazione utilizzata;

2. residuali dei bilanci temporali prossimi a zero entro una tolleranza dichiarata;

3. rispetto dei vincoli:

$$
\ell'x^*\leq7.5,
$$

$$
x_3^*+x_4^*\geq35,
$$

$$
x_5^*\leq35,
$$

$$
0\leq u_t^*\leq\phi\bar u_t,
\qquad
t=1,2,3,
$$

e della non negatività delle variabili;

4. coerenza tra slack e classificazione dei vincoli come attivi o non attivi;

5. identificazione dei bounds attivi mediante la distanza dai rispettivi limiti;

6. verifica numerica di almeno un valore marginale mediante una piccola perturbazione del termine noto o del limite cui esso si riferisce;

7. quando il vincolo legacy è attivo e il relativo marginale è localmente informativo, verifica perturbativa specifica del limite economico $L$.

I risultati relativi a configurazioni non ammissibili non devono essere utilizzati né interpretati economicamente.

### 7.2 Controlli logici e teorici

Devono essere verificati:

1. riproduzione del benchmark per:

$$
(\alpha,\beta,\phi)
=
(1,1,1);
$$

2. variazione di un solo parametro alla volta nelle sensitività univariate;

3. azione corretta dei tre driver:
   - $\alpha$ modifica esclusivamente il fabbisogno della prima data;
   - $\beta$ modifica esclusivamente il fabbisogno della quarta data;
   - $\phi$ modifica esclusivamente la capacità massima di funding;

4. invariabilità del costo del funding nelle sensitività e negli scenari;

5. sviluppo separato delle sensitività ad $\alpha$ e a $\beta$ prima del loro confronto;

6. confronto tra shock iniziale e shock terminale tenendo conto della diversa collocazione temporale del fabbisogno;

7. coerenza tra cambiamenti della soluzione e cambiamenti dei vincoli o bounds attivi;

8. associazione dei valori marginali al corretto vincolo o bilancio e loro interpretazione locale;

9. distinzione tra vincolo attivo e valore marginale economicamente informativo;

10. distinzione tra forma economica del vincolo legacy:

$$
x_3+x_4\geq L,
\qquad
L=35,
$$

e forma solver:

$$
-x_3-x_4\leq b,
\qquad
b=-L;
$$

11. con:

$$
F=-\Pi,
\qquad
m
=
\frac{\partial F^*}{\partial b},
$$

corretta interpretazione:

$$
\frac{\partial\Pi^*}{\partial L}
=
m,
$$

senza applicare un ulteriore cambio di segno;

12. distinzione tra sensitività univariata e scenario analysis;

13. interpretazione degli scenari come configurazioni deterministiche assegnate e non come eventi probabilistici.

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

4. corretta codifica del vincolo legacy:

$$
-x_3-x_4\leq-35;
$$

5. corretta parametrizzazione:

$$
d(\alpha,\beta)
=
(32\alpha,18,14,32\beta)',
$$

$$
0\leq u_t\leq\phi\bar u_t;
$$

6. assenza di effetti di $\alpha$, $\beta$ e $\phi$ su elementi diversi da quelli assegnati;

7. riproduzione della soluzione benchmark da parte della funzione parametrica valutata in:

$$
(1,1,1);
$$

8. utilizzo nelle tabelle e nei grafici esclusivamente di risultati provenienti da esecuzioni valide del solver;

9. gestione delle configurazioni non ammissibili senza propagazione di valori numerici non validi;

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

6. la capacità massima di funding sia esogena e parametrizzata mediante:

$$
\bar u_t(\phi)
=
\phi\bar u_t,
$$

mentre il costo del funding rimanga invariato al variare di $\alpha$, $\beta$ e $\phi$;

7. $\alpha$ modifichi esclusivamente il fabbisogno della prima data e $\beta$ esclusivamente quello della quarta data;

8. il vincolo:

$$
x_3+x_4\geq35
$$

rappresenti una rigidità legacy del portafoglio, distinta dal limite:

$$
x_5\leq35;
$$

9. ogni configurazione parametrica e ciascuno scenario costituiscano problemi deterministici autonomi.

### 8.2 Semplificazioni adottate

Il caso utilizza una rappresentazione stilizzata nella quale:

1. le classi di attivo e i cash flow sono aggregati;

2. i fabbisogni e la capacità di funding sono descritti mediante parametri assegnati;

3. il costo del funding non dipende dalla quantità effettivamente raccolta;

4. il vincolo legacy è rappresentato mediante una singola disuguaglianza lineare;

5. la struttura dei cash flow rimane invariata nelle diverse configurazioni;

6. non vengono introdotte decisioni adattive né non linearità associate alla liquidazione degli attivi.

### 8.3 Elementi esclusi

Il modello non include:

1. fire sales, haircuts dipendenti dallo stress o feedback tra vendite, prezzi e liquidità;

2. dinamiche endogene dei depositi o comportamento strategico dei depositanti;

3. rischio di mercato o di credito stocastico;

4. probabilità associate agli scenari o variabili casuali per $\alpha$, $\beta$ e $\phi$;

5. ottimizzazione stocastica, decisioni adattive o struttura multistadio;

6. effetti reputazionali, regolamentari o macrofinanziari endogeni;

7. una ricostruzione empirica completa della crisi di First Republic Bank.

### 8.4 Limiti dell'interpretazione

Il caso è un modello didattico deterministico di Asset--Liability Management ispirato alla crisi di First Republic Bank del 2023.

Pertanto:

1. i coefficienti numerici non rappresentano una ricostruzione puntuale del bilancio storico della banca;

2. $\alpha$, $\beta$ e $\phi$ sono parametri deterministici e gli scenari Standard, Mediamente critico e Critico non costituiscono una distribuzione di probabilità;

3. il confronto tra $\alpha$ e $\beta$ riguarda esclusivamente il diverso timing dei fabbisogni nel modello;

4. il vincolo:

$$
x_3+x_4\geq35
$$

deve essere interpretato esclusivamente come rappresentazione stilizzata di una rigidità legacy;

5. il marginale associato al vincolo legacy ha significato locale e, con le convenzioni adottate:

$$
\frac{\partial\Pi^*}{\partial L}
=
m;
$$

6. una maggiore capacità di funding non implica necessariamente un maggiore utilizzo effettivo del funding;

7. fattibilità e ottimalità riguardano esclusivamente il modello specificato e non equivalgono alla sostenibilità economico-finanziaria della banca nel mondo reale;

8. i risultati non consentono inferenze causali sulla crisi storica e non devono essere estesi oltre le ipotesi e i vincoli dichiarati.