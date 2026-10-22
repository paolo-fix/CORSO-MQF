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

Gli output devono essere prodotti esclusivamente a partire da configurazioni per le quali il solver restituisce una soluzione valida.

Devono consentire di distinguere chiaramente:

1. soluzione benchmark;
2. diagnostica della soluzione;
3. sensitività univariate;
4. frontiera di fattibilità rispetto a $\theta$;
5. scenario analysis.

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
\theta,
\qquad
\phi,
\qquad
\psi;
$$

8. variazioni rispetto al benchmark:

$$
\Delta\Pi^*(p),
\qquad
\Delta_{\%}\Pi^*(p),
$$

$$
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

12. intervallo contenente:

$$
\theta_{\mathrm{crit}};
$$

13. risultati dei tre scenari assegnati;

14. perdita di valore degli scenari Mediamente critico e Critico rispetto allo scenario Standard.

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

Le tabelle devono contenere le quantità necessarie a rappresentare gli output definiti nella Sezione 5 e i controlli richiesti nella Sezione 7.

### 6.3 Grafici

Devono essere prodotti i seguenti grafici:

1. **Valore ottimo al variare di $\theta$**:

$$
\theta
\longmapsto
\Pi^*(\theta);
$$

2. **Variazione del valore ottimo rispetto al benchmark al variare di $\theta$**:

$$
\theta
\longmapsto
\Delta\Pi^*(\theta)
$$

oppure la corrispondente variazione percentuale;

3. **Composizione ottima dell'attivo al variare di $\theta$**:

$$
x_1^*(\theta),\ldots,x_4^*(\theta);
$$

4. **Variazioni dell'asset allocation rispetto al benchmark**:

$$
\Delta x_j^*(\theta);
$$

5. **Funding ottimo e utilizzo della capacità al variare di $\theta$**, mediante $u_t^*(\theta)$ e/o:

$$
\frac{u_t^*(\theta)}{\bar u_t};
$$

6. **Giacenze ottime al variare di $\theta$**:

$$
g_1^*(\theta),\ldots,g_4^*(\theta);
$$

7. **Sensitività rispetto a $\phi$**, rappresentando almeno:

$$
\phi
\longmapsto
\Pi^*(\phi)
$$

e il comportamento del funding rispetto alla capacità disponibile;

8. **Sensitività rispetto a $\psi$**, rappresentando almeno:

$$
\psi
\longmapsto
\Pi^*(\psi)
$$

e l'evoluzione del funding ottimo;

9. **Valori marginali**, rappresentando i marginali dei bilanci temporali e/o dei limiti di funding più informativi lungo almeno una delle griglie;

10. **Mappa dei principali vincoli attivi**, mostrando almeno lungo la sensitività rispetto a $\theta$ il passaggio tra stato attivo e non attivo;

11. **Valore ottimo nei tre scenari**, confrontando:

$$
\Pi_{\mathrm{Standard}}^*,
\qquad
\Pi_{\mathrm{Medio}}^*,
\qquad
\Pi_{\mathrm{Critico}}^*;
$$

12. **Composizione ottima dell'attivo nei tre scenari**, confrontando:

$$
x_1^*,x_2^*,x_3^*,x_4^*;
$$

13. **Funding nei tre scenari**, confrontando:

$$
u_1^*,u_2^*,u_3^*;
$$

14. **Profilo temporale delle giacenze nei tre scenari**, rappresentando per ciascuno scenario:

$$
t
\longmapsto
g_t^*,
\qquad
t=1,\ldots,4.
$$

I grafici devono utilizzare esclusivamente configurazioni per le quali il solver restituisce una soluzione valida.

### 6.4 Regole di produzione

1. Tabelle e grafici devono essere generati direttamente dagli oggetti prodotti nel notebook.

2. Non devono essere utilizzati o interpretati valori della soluzione quando il solver segnala una configurazione non ammissibile.

3. Le configurazioni ammissibili e non ammissibili devono essere distinte chiaramente.

4. Non devono essere inseriti manualmente nelle celle successive valori numerici prodotti in precedenza dal solver.

5. Gli output devono essere rigenerabili mediante riesecuzione ordinata del notebook.

6. Non devono essere previste esportazioni automatiche in file esterni, salvo indicazione esplicita del docente.

### 6.5 Funzione interpretativa

Gli output devono consentire di discutere:

1. come cambia il piano ALM al variare dei fabbisogni iniziali;

2. come cambia la soluzione al variare della capacità di funding;

3. come cambia la soluzione al variare del costo del funding;

4. quali vincoli e bounds diventano attivi nelle diverse configurazioni;

5. dove si colloca la frontiera di fattibilità rispetto a $\theta$;

6. come differiscono Standard, Mediamente critico e Critico;

7. quali conclusioni dipendono dalla struttura del modello stilizzato.

L'interpretazione deve basarsi esclusivamente su risultati numericamente validati.

---

## 7. Controlli richiesti

I controlli devono verificare separatamente:

1. correttezza numerica della soluzione;
2. coerenza logico-teorica del modello;
3. correttezza della traduzione computazionale.

L'interpretazione finale deve utilizzare esclusivamente risultati che abbiano superato tali controlli.

### 7.1 Controlli numerici

1. Il benchmark deve restituire uno stato di ottimizzazione valido.

2. I bilanci temporali devono essere verificati mediante residuali numerici prossimi a zero entro una tolleranza dichiarata.

3. Devono essere verificati:

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

e la non negatività di tutte le variabili.

4. La classificazione dei vincoli come attivi o non attivi deve essere coerente con i relativi slack.

5. I bounds attivi devono essere identificati verificando la distanza della variabile dal relativo lower bound o upper bound.

6. Almeno un valore marginale deve essere verificato numericamente mediante una piccola perturbazione del termine noto o del limite cui esso si riferisce.

7. Per ogni configurazione parametrica deve essere verificato lo stato del solver prima di utilizzare i risultati.

8. I risultati di configurazioni non ammissibili non devono essere utilizzati né interpretati economicamente.

### 7.2 Controlli logici e teorici

1. La funzione parametrica deve riprodurre il benchmark in:

$$
(\theta,\phi,\psi)=(1,1,1).
$$

2. Nelle sensitività univariate deve variare un solo parametro alla volta.

3. Il parametro $\theta$ deve modificare esclusivamente i fabbisogni delle prime due date.

4. Il parametro $\phi$ deve modificare esclusivamente la capacità massima di funding.

5. Il parametro $\psi$ deve modificare sia:

- il costo del funding nella funzione obiettivo;
- il rimborso del funding nei bilanci temporali.

6. I cambiamenti della soluzione devono essere confrontati con gli eventuali cambiamenti dei vincoli e dei bounds attivi.

7. I valori marginali devono essere associati al corretto vincolo o bilancio e interpretati come quantità locali.

8. Nell'interpretazione dei marginali deve essere considerato il passaggio dal problema economico di massimizzazione alla convenzione di minimizzazione utilizzata dal solver.

9. La presenza di un vincolo attivo non implica automaticamente un valore marginale economicamente rilevante.

10. La frontiera di fattibilità rispetto a $\theta$ deve essere determinata esclusivamente mediante il passaggio tra configurazioni ammissibili e non ammissibili.

11. Il valore:

$$
\theta_{\mathrm{crit}}
$$

deve essere interpretato come frontiera del modello stilizzato e non come stima empirica dei deflussi storicamente osservati presso Silicon Valley Bank.

12. Gli scenari devono utilizzare esattamente i valori assegnati nella Sezione 4.13.

13. Sensitività univariata e scenario analysis devono rimanere distinte: nella prima varia un solo driver, nella seconda più driver possono variare congiuntamente.

### 7.3 Controlli computazionali

1. L'ordinamento delle variabili decisionali deve essere dichiarato e mantenuto invariato.

2. Devono essere compatibili le dimensioni di:

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

e dei bounds.

3. Deve essere verificata correttamente la trasformazione:

$$
\max\Pi
\quad\longleftrightarrow\quad
\min(-\Pi).
$$

4. La parametrizzazione dei fabbisogni deve rispettare:

$$
d(\theta)
=
(30\theta,30\theta,22,15)'.
$$

5. I bounds del funding devono rispettare:

$$
0\leq u_t\leq\phi\bar u_t.
$$

6. La variazione di $\psi$ deve essere applicata coerentemente sia alla funzione obiettivo sia ai rimborsi del funding.

7. La funzione parametrica, valutata in:

$$
(1,1,1),
$$

deve riprodurre la soluzione benchmark diretta entro la tolleranza numerica adottata.

8. Le tabelle e i grafici devono utilizzare esclusivamente risultati provenienti da esecuzioni valide del solver.

9. I punti non ammissibili non devono essere interpolati o collegati artificialmente alle curve delle quantità ottime.

10. Il raffinamento della ricerca di:

$$
\theta_{\mathrm{crit}}
$$

deve essere effettuato soltanto dopo avere individuato sulla griglia iniziale l'ultimo valore ammissibile e il primo non ammissibile.

11. Le configurazioni della scenario analysis devono essere passate al solver senza modifiche.

12. Tabelle e grafici devono essere rigenerabili mediante riesecuzione ordinata del notebook.

13. Il notebook deve poter essere eseguito integralmente dall'inizio senza dipendere da oggetti prodotti in esecuzioni precedenti non riproducibili.

### 7.4 Controllo conclusivo

Prima dell'interpretazione finale devono risultare verificati congiuntamente:

1. corretta formulazione solver;

2. fattibilità delle configurazioni utilizzate;

3. rispetto dei vincoli e dei bounds;

4. coerenza tra residuali, slack e stato attivo dei vincoli;

5. corretta identificazione dei bounds attivi;

6. corretta interpretazione locale dei valori marginali;

7. corretta azione di $\theta$, $\phi$ e $\psi$;

8. corretta individuazione della frontiera di fattibilità;

9. coerenza degli scenari con i valori assegnati;

10. utilizzo esclusivo di risultati numericamente validi.

L'interpretazione finanziaria finale deve basarsi esclusivamente su output che abbiano superato tali controlli.

---

## 8. Ipotesi e limiti del caso

### 8.1 Ipotesi modellistiche

Il modello assume che:

1. l'orizzonte sia deterministico e articolato in quattro date future;

2. le decisioni iniziali di allocazione siano assunte al tempo iniziale e rimangano invariate lungo l'orizzonte;

3. i cash flow degli attivi siano noti e proporzionali agli importi inizialmente investiti;

4. i fabbisogni di liquidità siano deterministici all'interno di ciascuna configurazione parametrica;

5. le quantità siano divisibili;

6. la funzione obiettivo e i vincoli siano lineari;

7. il funding raccolto alla data $t$ sia immediatamente disponibile e venga rimborsato alla data successiva;

8. la capacità massima di funding sia esogena;

9. il costo del funding sia esogeno;

10. nelle sensitività univariate vari un solo parametro alla volta;

11. gli scenari siano configurazioni deterministiche assegnate e non eventi probabilistici.

### 8.2 Semplificazioni adottate

Il caso utilizza una rappresentazione stilizzata nella quale:

1. le classi di attivo sono aggregate;

2. i cash flow sono rappresentati mediante coefficienti deterministici;

3. non vengono modellati aggiustamenti endogeni dei tassi o dei prezzi conseguenti alle decisioni della banca;

4. non vengono modellati costi di transazione o frizioni di mercato diversi dai costi esplicitamente inclusi;

5. il funding è rappresentato mediante capacità e costi assegnati;

6. il vincolo prudenziale è rappresentato in forma lineare;

7. la disponibilità di liquidità viene descritta attraverso bilanci temporali discreti.

### 8.3 Elementi esclusi

Il modello non include:

1. incertezza probabilistica sui fabbisogni futuri;

2. dinamiche stocastiche dei tassi di interesse;

3. variazioni endogene dei prezzi di mercato degli attivi;

4. fire sales o effetti di mercato prodotti dalla liquidazione degli attivi;

5. interazione strategica con depositanti, controparti o autorità;

6. rischio di credito dinamico;

7. requisiti regolamentari completi;

8. una struttura stocastica o multistadio delle decisioni;

9. una ricostruzione empirica completa della crisi di Silicon Valley Bank.

### 8.4 Limiti dell'interpretazione

Il caso è ispirato alla crisi di Silicon Valley Bank del 2023, ma utilizza un modello didattico stilizzato.

Pertanto:

1. i parametri non devono essere interpretati come una ricostruzione puntuale del bilancio storico della banca;

2. le sensitività descrivono la risposta del modello a variazioni dei parametri assegnati, non relazioni causali osservate empiricamente;

3. la frontiera:

$$
\theta_{\mathrm{crit}}
$$

rappresenta una soglia di fattibilità del modello e non una stima dei deflussi storici effettivi;

4. i valori marginali devono essere interpretati localmente e soltanto nella configurazione nella quale risultano informativi;

5. un cambiamento dei vincoli attivi può modificare la relazione marginale osservata;

6. gli scenari Standard, Mediamente critico e Critico sono configurazioni deterministiche di confronto e non scenari probabilizzati;

7. i risultati non devono essere estesi oltre le ipotesi, i vincoli e l'orizzonte temporale dichiarati.

Il caso ha finalità didattica: deve rendere osservabile come composizione dell'attivo, fabbisogni temporali, giacenze, funding e vincoli interagiscano in un problema ALM deterministico.