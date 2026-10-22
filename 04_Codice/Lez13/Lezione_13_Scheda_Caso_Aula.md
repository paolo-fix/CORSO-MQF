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

Le variabili $x_1,x_2,x_3,x_4$ rappresentano gli importi inizialmente allocati nelle seguenti classi di attivo:

1. $x_1$: cassa e riserve;
2. $x_2$: titoli a breve scadenza;
3. $x_3$: titoli a lunga scadenza;
4. $x_4$: prestiti e impieghi meno liquidi.

Gli importi $x_j$ sono espressi nelle stesse unità monetarie di $A_0$.

Per ciascuna data futura $t=1,\ldots,4$ si definisce $g_t\geq0$, dove $g_t$ rappresenta la giacenza di liquidità rimasta immediatamente dopo avere soddisfatto il fabbisogno della data $t$.

Per $t=1,2,3$ si definisce $u_t\geq0$, dove $u_t$ rappresenta il funding esterno raccolto alla data $t$, disponibile immediatamente e da rimborsare alla data successiva.

### 3.2 Cash flow degli attivi

La matrice

$$
A^{\mathrm{CF}}=(a_{tj})
$$

descrive il profilo temporale dei cash flow.

Il coefficiente $a_{tj}$ indica quanta liquidità viene resa disponibile alla data $t$ da una unità investita al tempo iniziale nell'attivo $j$.

Il cash flow complessivamente prodotto dall'attivo alla data $t$ è:

$$
a_t'x=\sum_{j=1}^{4}a_{tj}x_j.
$$

### 3.3 Fabbisogni di liquidità

Nel benchmark, i fabbisogni alle quattro date sono raccolti nel vettore $d=(d_1,d_2,d_3,d_4)'$.

Per l'analisi dello stress sui fabbisogni si introduce il parametro $\theta$:

$$
d(\theta)=(30\theta,30\theta,22,15)'.
$$

Il benchmark corrisponde a $\theta=1$.

### 3.4 Giacenze di liquidità

Una giacenza $g_t$ viene trasferita alla data successiva e produce il rendimento $r_t^g$. Pertanto, alla data successiva diventa disponibile:

$$
(1+r_t^g)g_t.
$$

### 3.5 Funding esterno

Il funding raccolto alla data $t$ è immediatamente disponibile come risorsa $u_t$ e alla data successiva deve essere rimborsato per:

$$
(1+r_t^u)u_t.
$$

La capacità massima di funding benchmark è $\bar u_t$.

Per la sensitività alla disponibilità di funding:

$$
\bar u_t(\phi)=\phi\bar u_t.
$$

Il benchmark corrisponde a $\phi=1$.

Per la sensitività al costo del funding:

$$
r_t^u(\psi)=\psi r_t^u.
$$

Il benchmark corrisponde a $\psi=1$.

Il parametro $\psi$ modifica sia il costo del funding nella funzione obiettivo sia l'ammontare da rimborsare alla data successiva.

### 3.6 Funzione obiettivo

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

Nell'implementazione Python occorre tenere conto della convenzione adottata dal solver utilizzato.

### 3.7 Vincolo sulle risorse iniziali

$$
\sum_{j=1}^{4}x_j=A_0.
$$

### 3.8 Bilanci temporali di liquidità

Alla prima data:

$$
a_1'x+u_1-g_1=d_1(\theta).
$$

Alle date intermedie $t=2,3$:

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

### 3.9 Vincolo prudenziale

$$
\ell'x\leq K.
$$

### 3.10 Limite di concentrazione

$$
x_3\leq30.
$$

### 3.11 Capacità di funding e non negatività

$$
0\leq u_t\leq\phi\bar u_t,
\qquad t=1,2,3.
$$

Inoltre:

$$
x_j\geq0,
\qquad j=1,\ldots,4,
$$

e:

$$
g_t\geq0,
\qquad t=1,\ldots,4.
$$

---

## 4. Parametri assegnati

### 4.1 Risorse iniziali

$$
A_0=100.
$$

### 4.2 Redditività degli attivi

$$
c'=(0.010,0.025,0.040,0.050).
$$

### 4.3 Perdite unitarie sotto stress

$$
\ell'=(0,0.02,0.15,0.08).
$$

### 4.4 Matrice dei cash flow

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

Le righe corrispondono alle date $t=1,\ldots,4$ e le colonne, nell'ordine, a $(x_1,x_2,x_3,x_4)$.

### 4.5 Fabbisogni benchmark

$$
d'=(30,30,22,15).
$$

### 4.6 Rendimenti delle giacenze

$$
{r^g}'=(0.005,0.006,0.007).
$$

### 4.7 Costi benchmark del funding

$$
{r^u}'=(0.015,0.020,0.025).
$$

### 4.8 Capacità benchmark di funding

$$
\bar u'=(10,8,6).
$$

### 4.9 Limite prudenziale

$$
K=7.
$$

### 4.10 Griglia di sensitività a $\theta$

Con $\phi=1$ e $\psi=1$:

$$
\theta\in\{1.00,1.01,\ldots,1.10\}.
$$

La griglia deve essere utilizzata anche per individuare l'intervallo nel quale cambia lo stato di fattibilità. Dopo avere individuato tale intervallo, deve essere effettuato un raffinamento della ricerca.

### 4.11 Griglia di sensitività a $\phi$

Con $\theta=1$ e $\psi=1$:

$$
\phi\in\{0.50,0.60,0.70,0.80,0.90,1.00,1.10,1.20,1.30,1.40,1.50\}.
$$

### 4.12 Griglia di sensitività a $\psi$

Con $\theta=1$ e $\phi=1$:

$$
\psi\in\{0.50,0.75,1.00,1.25,1.50,1.75,2.00\}.
$$

### 4.13 Scenari congiunti

| Scenario | $\theta$ | $\phi$ | $\psi$ |
|---|---:|---:|---:|
| Standard | 1.00 | 1.00 | 1.00 |
| Mediamente critico | 1.03 | 0.90 | 1.25 |
| Critico | 1.06 | 0.70 | 1.50 |

Lo scenario Standard coincide con il benchmark.

Gli scenari Mediamente critico e Critico modificano contemporaneamente fabbisogni iniziali, capacità massima di funding e costo del funding.

Gli scenari devono essere interpretati come configurazioni deterministiche assegnate e non come eventi ai quali siano associate probabilità.

---

## 5. Quantità da stimare o calcolare

### 5.1 Benchmark

Per il benchmark $(\theta,\phi,\psi)=(1,1,1)$ devono essere determinati:

1. il vettore ottimo degli attivi $x^*$;
2. il vettore ottimo delle giacenze $g^*$;
3. il vettore ottimo del funding $u^*$;
4. il valore ottimo $\Pi^*$;
5. i residuali dei vincoli di uguaglianza;
6. gli slack dei vincoli di disuguaglianza;
7. i bounds attivi;
8. i principali valori marginali restituiti dal solver.

### 5.2 Sensitività univariate

Per ciascun parametro $p\in\{\theta,\phi,\psi\}$ devono essere determinate, per ogni punto della relativa griglia:

1. la fattibilità del problema;
2. il valore ottimo $\Pi^*(p)$;
3. le componenti $x_j^*(p)$;
4. le componenti $g_t^*(p)$;
5. le componenti $u_t^*(p)$;
6. i principali vincoli attivi;
7. i principali valori marginali quando economicamente informativi.

Devono inoltre essere calcolate:

$$
\Delta\Pi^*(p)=\Pi^*(p)-\Pi^*(1),
$$

$$
\Delta_{\%}\Pi^*(p)
=
100\left[
\frac{\Pi^*(p)}{\Pi^*(1)}-1
\right],
$$

$$
\Delta x_j^*(p)=x_j^*(p)-x_j^*(1),
$$

$$
\Delta g_t^*(p)=g_t^*(p)-g_t^*(1),
$$

$$
\Delta u_t^*(p)=u_t^*(p)-u_t^*(1).
$$

### 5.3 Utilizzo della capacità di funding

Per ogni data e per ciascuna analisi parametrica:

$$
\rho_t^u(p)
=
\frac{u_t^*(p)}{\bar u_t(p)}.
$$

Quando il parametro variato non è $\phi$, il denominatore coincide con la capacità benchmark.

### 5.4 Frontiera di fattibilità rispetto a $\theta$

Sulla griglia assegnata devono essere individuati:

1. l'ultimo valore di $\theta$ per il quale il problema è ammissibile;
2. il primo valore di $\theta$ per il quale il problema non è ammissibile.

Nell'intervallo così individuato deve essere effettuato un raffinamento della ricerca, con passo più fine, in modo da determinare un intervallo ristretto contenente:

$$
\theta_{\mathrm{crit}}.
$$

Il valore $\theta_{\mathrm{crit}}$ rappresenta la frontiera di fattibilità del modello stilizzato e non deve essere interpretato come stima dei deflussi storicamente osservati presso SVB.

### 5.5 Scenario analysis

Per ciascuno dei tre scenari devono essere determinati:

1. $\Pi^*$;
2. $x^*$;
3. $g^*$;
4. $u^*$;
5. i principali vincoli attivi;
6. il rapporto di utilizzo della capacità di funding;
7. i principali valori marginali, se economicamente rilevanti.

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

Gli output devono avere una funzione informativa, diagnostica o interpretativa esplicita e devono essere costruiti esclusivamente a partire da configurazioni per le quali il solver restituisce una soluzione valida.

### 6.1 Stime o risultati numerici

Devono essere riportati:

1. soluzione ottima benchmark $x^*$;
2. giacenze ottime benchmark $g^*$;
3. funding ottimo benchmark $u^*$;
4. valore ottimo benchmark $\Pi^*$;
5. residuali dei vincoli di uguaglianza nel benchmark;
6. slack, bounds attivi e principali vincoli attivi nel benchmark;
7. principali valori marginali benchmark;
8. risultati delle tre sensitività univariate rispetto a $\theta$, $\phi$ e $\psi$;
9. variazioni assolute del valore ottimo:

$$
\Delta\Pi^*(p)
=
\Pi^*(p)-\Pi^*(1);
$$

10. variazioni percentuali del valore ottimo:

$$
\Delta_{\%}\Pi^*(p)
=
100
\left[
\frac{\Pi^*(p)}{\Pi^*(1)}-1
\right];
$$

11. variazioni delle componenti della soluzione ottima:

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
u_t^*(p)-u_t^*(1);
$$

12. rapporti di utilizzo della capacità di funding:

$$
\rho_t^u(p)
=
\frac{u_t^*(p)}{\bar u_t(p)};
$$

13. stato di fattibilità per ciascun punto delle griglie parametriche;
14. ultimo valore ammissibile e primo valore non ammissibile della griglia di $\theta$;
15. intervallo raffinato contenente $\theta_{\mathrm{crit}}$;
16. risultati completi dei tre scenari congiunti;
17. perdita di valore degli scenari Mediamente critico e Critico rispetto allo scenario Standard:

$$
L_s
=
\Pi_{\mathrm{Standard}}^*
-
\Pi_s^*.
$$

### 6.2 Tabelle

Devono essere costruite le seguenti tabelle.

**Tabella 1 — Parametri benchmark**

Deve riportare almeno:

- $A_0$;
- $c$;
- $\ell$;
- $d$;
- $r^g$;
- $r^u$;
- $\bar u$;
- $K$;
- limite su $x_3$.

La tabella deve rendere immediatamente verificabile la configurazione di riferimento utilizzata dal solver.

**Tabella 2 — Soluzione benchmark**

Deve riportare:

- $x_1^*,\ldots,x_4^*$;
- $g_1^*,\ldots,g_4^*$;
- $u_1^*,u_2^*,u_3^*$;
- $\Pi^*$.

La tabella deve sintetizzare il piano ALM ottimo benchmark.

**Tabella 3 — Verifica dei bilanci temporali**

Per ciascuna data deve riportare almeno:

- cash flow degli attivi;
- giacenza proveniente dalla data precedente, quando presente;
- funding raccolto, quando presente;
- rimborso del funding precedente, quando presente;
- fabbisogno;
- giacenza finale;
- residuo dell'uguaglianza.

La tabella deve rendere verificabile la soddisfazione dei bilanci temporali.

**Tabella 4 — Vincoli, bounds e slack benchmark**

Per ciascun vincolo o bound rilevante deve riportare:

- valore assunto;
- limite;
- slack o distanza dal bound;
- indicazione attivo / non attivo.

**Tabella 5 — Valori marginali benchmark**

Deve riportare almeno i valori marginali economicamente informativi relativi:

- ai bilanci temporali;
- ai limiti di funding;
- agli altri vincoli rilevanti quando il solver ne fornisce un marginale interpretabile.

**Tabella 6 — Sensitività a $\theta$**

Per ciascun valore della griglia deve riportare almeno:

- $\theta$;
- stato del solver;
- fattibilità;
- $\Pi^*$;
- $\Delta\Pi^*$;
- $\Delta_{\%}\Pi^*$;
- $x^*$;
- $g^*$;
- $u^*$;
- rapporti di utilizzo della capacità di funding;
- principali vincoli attivi.

**Tabella 7 — Sensitività a $\phi$**

Deve utilizzare una struttura analoga alla Tabella 6, sostituendo $\theta$ con $\phi$ e mettendo in evidenza l'utilizzo della capacità disponibile di funding.

**Tabella 8 — Sensitività a $\psi$**

Deve utilizzare una struttura analoga alla Tabella 6, sostituendo $\theta$ con $\psi$ e mettendo in evidenza l'effetto del costo del funding sul valore ottimo e sul ricorso al funding.

**Tabella 9 — Raffinamento della frontiera di fattibilità**

Deve riportare, nell'intervallo individuato dalla griglia iniziale:

- valori raffinati di $\theta$;
- stato del solver;
- fattibilità.

La tabella deve consentire di individuare un intervallo ristretto contenente $\theta_{\mathrm{crit}}$.

**Tabella 10 — Confronto degli scenari**

Deve confrontare Standard, Mediamente critico e Critico riportando almeno:

- $\theta$;
- $\phi$;
- $\psi$;
- fattibilità;
- $\Pi^*$;
- perdita rispetto allo Standard;
- $x^*$;
- $g^*$;
- $u^*$;
- principali vincoli attivi;
- utilizzo relativo della capacità di funding.

### 6.3 Figure

Devono essere prodotte le seguenti figure.

**Figura 1 — Valore ottimo e sensitività a $\theta$**

Grafico di:

$$
\theta
\longmapsto
\Pi^*(\theta).
$$

Devono essere rappresentati soltanto i punti corrispondenti a problemi ammissibili.

**Figura 2 — Variazione del valore ottimo rispetto a $\theta$**

Grafico di:

$$
\theta
\longmapsto
\Delta\Pi^*(\theta)
$$

oppure della corrispondente variazione percentuale.

**Figura 3 — Composizione ottima dell'attivo rispetto a $\theta$**

Grafico delle serie:

$$
x_1^*(\theta),\ldots,x_4^*(\theta).
$$

**Figura 4 — Variazioni dell'asset allocation rispetto al benchmark**

Grafico delle serie:

$$
\Delta x_j^*(\theta).
$$

**Figura 5 — Funding ottimo e utilizzo della capacità rispetto a $\theta$**

Devono essere rappresentati $u_t^*(\theta)$ e/o:

$$
\frac{u_t^*(\theta)}{\bar u_t}.
$$

**Figura 6 — Giacenze ottime rispetto a $\theta$**

Grafico delle serie:

$$
g_1^*(\theta),\ldots,g_4^*(\theta).
$$

**Figura 7 — Sensitività a $\phi$**

Deve mostrare almeno:

$$
\phi
\longmapsto
\Pi^*(\phi)
$$

e il comportamento del funding rispetto alla capacità disponibile.

**Figura 8 — Sensitività a $\psi$**

Deve mostrare almeno:

$$
\psi
\longmapsto
\Pi^*(\psi)
$$

e l'evoluzione del funding ottimo.

**Figura 9 — Valori marginali**

Deve rappresentare i valori marginali dei bilanci temporali e/o dei limiti di funding più informativi lungo almeno una delle griglie.

**Figura 10 — Mappa dei principali vincoli attivi**

Deve rendere visibile il cambiamento dello stato attivo / non attivo dei principali vincoli almeno lungo la sensitività a $\theta$.

**Figura 11 — Valore ottimo nei tre scenari**

Confronto dei valori:

$$
\Pi_{\mathrm{Standard}}^*,
\qquad
\Pi_{\mathrm{Medio}}^*,
\qquad
\Pi_{\mathrm{Critico}}^*.
$$

**Figura 12 — Composizione ottima dell'attivo nei tre scenari**

Confronto delle componenti:

$$
x_1^*,x_2^*,x_3^*,x_4^*.
$$

**Figura 13 — Funding nei tre scenari**

Confronto di:

$$
u_1^*,u_2^*,u_3^*.
$$

**Figura 14 — Profilo temporale delle giacenze nei tre scenari**

Per ogni scenario deve essere rappresentato:

$$
t
\longmapsto
g_t^*,
\qquad
t=1,\ldots,4.
$$

### 6.4 Regole di produzione degli output

Le tabelle e le figure devono essere prodotte come output delle rispettive celle del notebook e devono essere rigenerabili mediante riesecuzione delle celle.

Non devono essere rappresentati nei grafici valori provenienti da configurazioni non ammissibili.

Non è richiesta automaticamente l'esportazione di tabelle o figure in file esterni. Eventuali esportazioni devono essere effettuate soltanto se richieste esplicitamente dal docente.

Gli output devono essere utilizzati per verificare e interpretare il modello, non come elementi puramente decorativi.

---

## 7. Controlli richiesti

I controlli devono verificare separatamente la correttezza numerica della soluzione, la coerenza logico-teorica del modello e la correttezza della traduzione computazionale.

### 7.1 Controlli numerici

1. Il benchmark deve restituire uno stato di ottimizzazione valido.

2. Tutti i bilanci temporali devono essere verificati indipendentemente mediante residuali numerici.

3. I residuali dei vincoli di uguaglianza devono essere prossimi a zero entro una tolleranza numerica dichiarata.

4. Deve essere verificato indipendentemente il vincolo prudenziale:

$$
\ell'x^*\leq7.
$$

5. Deve essere verificato indipendentemente il limite di concentrazione:

$$
x_3^*\leq30.
$$

6. Per ciascuna data deve essere verificato il rispetto dei bounds del funding:

$$
0\leq u_t^*\leq\phi\bar u_t.
$$

7. Deve essere verificata la non negatività di tutte le variabili:

$$
x_j^*\geq0,
\qquad
g_t^*\geq0,
\qquad
u_t^*\geq0.
$$

8. La classificazione dei vincoli di disuguaglianza come attivi o non attivi deve essere coerente con i relativi slack entro una tolleranza numerica dichiarata.

9. I bounds attivi sulle variabili devono essere identificati separatamente, verificando quando una variabile si trova sul proprio lower bound o upper bound.

10. Deve essere verificato numericamente almeno un valore marginale mediante una piccola perturbazione del termine noto o del limite cui il marginale si riferisce.

11. Per ogni configurazione parametrica deve essere verificato lo stato del solver prima di utilizzare i valori della soluzione.

12. Quando il problema risulta non ammissibile, eventuali valori presenti negli oggetti restituiti dal solver non devono essere utilizzati né interpretati economicamente.

### 7.2 Controlli logici e teorici

1. La funzione parametrica deve riprodurre la configurazione benchmark quando:

$$
(\theta,\phi,\psi)=(1,1,1).
$$

2. Nella sensitività rispetto a $\theta$ devono rimanere fissi:

$$
\phi=1,
\qquad
\psi=1.
$$

3. Nella sensitività rispetto a $\phi$ devono rimanere fissi:

$$
\theta=1,
\qquad
\psi=1.
$$

4. Nella sensitività rispetto a $\psi$ devono rimanere fissi:

$$
\theta=1,
\qquad
\phi=1.
$$

5. Il parametro $\theta$ deve modificare esclusivamente i fabbisogni delle prime due date.

6. Il parametro $\phi$ deve modificare esclusivamente la capacità massima di funding.

7. Il parametro $\psi$ deve modificare:

- il costo del funding nella funzione obiettivo;
- l'ammontare da rimborsare nei bilanci temporali.

8. I cambiamenti della soluzione ottima devono essere confrontati con gli eventuali cambiamenti dei vincoli e dei bounds attivi.

9. L'interpretazione dei valori marginali deve essere coerente con il vincolo o il bilancio cui ciascun marginale si riferisce.

10. Nell'interpretazione dei valori marginali deve essere tenuto conto del passaggio dal problema economico di massimizzazione alla convenzione di minimizzazione utilizzata da `scipy.optimize.linprog`.

11. La presenza di un vincolo attivo non deve essere automaticamente interpretata come prova di un valore marginale economicamente rilevante: attività del vincolo e valore marginale devono essere verificati separatamente.

12. L'intervallo contenente $\theta_{\mathrm{crit}}$ deve essere determinato esclusivamente sulla base del passaggio tra configurazioni ammissibili e non ammissibili.

13. Il valore $\theta_{\mathrm{crit}}$ deve essere interpretato come frontiera di fattibilità del modello stilizzato e non come stima empirica dei deflussi storici di Silicon Valley Bank.

14. Le tre configurazioni della scenario analysis devono utilizzare esattamente i valori assegnati nella Sezione 4.13.

15. La sensitività univariata e la scenario analysis devono restare concettualmente distinte: nella prima varia un solo parametro alla volta, nella seconda i tre driver possono variare congiuntamente.

### 7.3 Controlli computazionali

1. L'ordinamento delle variabili nel vettore decisionale del solver deve essere dichiarato esplicitamente e mantenuto invariato in tutte le funzioni e nelle successive analisi.

2. Le dimensioni del vettore della funzione obiettivo, di $A_{\mathrm{eq}}$, $b_{\mathrm{eq}}$, $A_{\mathrm{ub}}$, $b_{\mathrm{ub}}$ e dei bounds devono essere reciprocamente compatibili.

3. La trasformazione della funzione obiettivo dal problema di massimo alla convenzione richiesta dal solver deve essere verificata esplicitamente.

4. La costruzione del vettore dei fabbisogni deve rispettare:

$$
d(\theta)
=
(30\theta,30\theta,22,15)'.
$$

5. I bounds del funding devono essere aggiornati correttamente quando varia $\phi$:

$$
0\leq u_t\leq\phi\bar u_t.
$$

6. Quando varia $\psi$, il coefficiente modificato deve essere utilizzato coerentemente sia nella funzione obiettivo sia nei termini di rimborso presenti nei bilanci temporali.

7. I risultati del benchmark prodotti dalla funzione parametrica devono coincidere con quelli ottenuti dalla soluzione benchmark diretta, entro la tolleranza numerica adottata.

8. I punti non ammissibili non devono essere collegati artificialmente alla curva di:

$$
\Pi^*(\theta).
$$

9. Le tabelle e i grafici delle sensitività devono utilizzare esclusivamente risultati provenienti da esecuzioni valide del solver.

10. Le configurazioni non ammissibili devono essere identificate e gestite senza propagare valori numerici non validi nelle tabelle, nei grafici o nei confronti successivi.

11. Il raffinamento della ricerca di $\theta_{\mathrm{crit}}$ deve essere effettuato soltanto dopo avere individuato, sulla griglia iniziale, un intervallo compreso tra l'ultimo valore ammissibile e il primo valore non ammissibile.

12. Le tre configurazioni della scenario analysis devono essere passate alla funzione solver senza modifiche rispetto ai valori assegnati.

13. Tabelle e grafici devono essere prodotti come output delle rispettive celle del notebook e devono essere rigenerabili mediante riesecuzione ordinata delle celle.

14. Il notebook deve poter essere rieseguito integralmente dall'inizio senza dipendere da variabili, risultati o oggetti prodotti in esecuzioni precedenti non riproducibili.

### 7.4 Coerenza finale dei controlli

Prima dell'interpretazione conclusiva devono risultare congiuntamente verificati:

1. correttezza della formulazione solver;
2. fattibilità delle configurazioni utilizzate;
3. rispetto dei vincoli e dei bounds;
4. coerenza tra residuali, slack e stato attivo dei vincoli;
5. corretta identificazione dei bounds attivi;
6. correttezza dell'interpretazione dei valori marginali;
7. coerenza delle sensitività con i parametri effettivamente modificati;
8. corretta individuazione della frontiera di fattibilità rispetto a $\theta$;
9. coerenza delle configurazioni della scenario analysis con i valori assegnati;
10. utilizzo esclusivo di risultati numericamente validi nelle tabelle, nei grafici e nell'interpretazione.

L'interpretazione finanziaria finale deve basarsi esclusivamente su output che abbiano superato tali controlli.

---

## 8. Ipotesi e limiti del caso

### 8.1 Ipotesi modellistiche

Il modello assume che:

1. l'orizzonte sia deterministico e articolato in quattro date future;

2. i cash flow degli attivi siano noti e proporzionali agli importi inizialmente investiti;

3. i fabbisogni di liquidità siano noti all'interno di ciascuna configurazione parametrica;

4. le quantità siano divisibili;

5. la funzione obiettivo e i vincoli siano lineari per ciascun valore assegnato di $\theta$, $\phi$ e $\psi$;

6. il funding raccolto alla data $t$ sia immediatamente disponibile e venga rimborsato alla data successiva;

7. la capacità massima di funding sia esogena e vari proporzionalmente con $\phi$;

8. il costo del funding sia esogeno e vari proporzionalmente con $\psi$;

9. il parametro $\theta$ modifichi esclusivamente i fabbisogni delle prime due date;

10. il parametro $\psi$ modifichi sia il costo del funding nella funzione obiettivo sia il relativo rimborso nei bilanci temporali;

11. nelle sensitività univariate vari un solo parametro alla volta;

12. negli scenari congiunti $\theta$, $\phi$ e $\psi$ assumano simultaneamente le configurazioni assegnate;

13. $\theta$, $\phi$ e $\psi$ siano parametri deterministici e non variabili casuali;

14. gli scenari non abbiano probabilità associate.

### 8.2 Semplificazioni adottate

Il caso adotta le seguenti semplificazioni:

1. la struttura dei cash flow degli attivi resta assegnata nelle diverse configurazioni;

2. il comportamento dei depositanti è rappresentato attraverso fabbisogni esogeni di liquidità e non mediante un modello comportamentale endogeno;

3. la disponibilità di funding è rappresentata mediante capacità massime esogene;

4. il costo del funding varia attraverso un moltiplicatore assegnato e non mediante una curva di offerta endogena;

5. il limite prudenziale e il limite di concentrazione sono rappresentati mediante vincoli lineari;

6. non vengono introdotte non linearità, indivisibilità o costi fissi;

7. il caso utilizza una calibrazione didattica finalizzata a rendere osservabile il funzionamento del modello ALM deterministico.

### 8.3 Elementi esclusi

Il modello non rappresenta:

1. fire sales degli attivi;

2. haircuts variabili nel tempo;

3. feedback tra vendite di attività e prezzi di mercato;

4. variazioni endogene del valore di mercato delle attività causate dallo stress di liquidità;

5. comportamento endogeno dei depositanti;

6. rischio di credito dinamico;

7. rischio di tasso modellato mediante scenari stocastici;

8. costi di transazione o altri costi fissi;

9. probabilità associate agli scenari;

10. decisioni adattive a nuova informazione osservata nel corso dell'orizzonte;

11. una struttura di programmazione stocastica o multistadio.

### 8.4 Limiti dell'interpretazione

Il caso è un modello didattico stilizzato e non costituisce una ricostruzione quantitativa del bilancio storico di Silicon Valley Bank.

In particolare:

1. i valori numerici assegnati non devono essere interpretati come stime dei corrispondenti dati storici di SVB;

2. le configurazioni Standard, Mediamente critico e Critico sono scenari deterministici di analisi e non valutazioni probabilistiche degli eventi storici;

3. i valori marginali devono essere interpretati come proprietà locali del programma lineare nelle configurazioni considerate e non come prezzi di mercato osservabili;

4. l'eventuale variazione dei vincoli attivi al modificarsi dei parametri segnala un cambiamento della struttura locale della soluzione e limita l'uso meccanico di una stessa interpretazione marginale lungo tutta la griglia;

5. il valore $\theta_{\mathrm{crit}}$ misura esclusivamente la frontiera di fattibilità del modello stilizzato:

$$
\theta_{\mathrm{crit}}
\neq
\text{stima del livello storico dei deflussi di SVB};
$$

6. i risultati possono essere interpretati soltanto nell'ambito dei parametri, dei vincoli e delle ipotesi esplicitamente assegnati.

L'obiettivo del caso è rendere osservabile, mediante programmazione lineare e analisi computazionale, il legame tra:

$$
\text{struttura dell'attivo},
\qquad
\text{profilo temporale della liquidità},
\qquad
\text{funding},
\qquad
\text{vincoli},
\qquad
\text{soluzione ottima}.
$$

I risultati non devono essere estesi oltre questo perimetro modellistico.