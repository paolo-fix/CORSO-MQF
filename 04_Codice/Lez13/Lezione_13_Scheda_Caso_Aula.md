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

### 6.1 Risultati numerici

Devono essere riportati:

1. soluzione ottima benchmark $x^*$;
2. giacenze ottime benchmark $g^*$;
3. funding ottimo benchmark $u^*$;
4. valore ottimo benchmark $\Pi^*$;
5. residuali benchmark;
6. slack e vincoli attivi benchmark;
7. principali valori marginali benchmark;
8. risultati completi delle tre sensitività univariate;
9. variazioni assolute e percentuali di $\Pi^*$;
10. variazioni delle componenti della soluzione ottima;
11. rapporti di utilizzo della capacità di funding;
12. ultimo valore ammissibile e primo valore non ammissibile della griglia di $\theta$;
13. intervallo raffinato contenente $\theta_{\mathrm{crit}}$;
14. risultati completi dei tre scenari;
15. perdita di valore degli scenari Mediamente critico e Critico rispetto allo Standard.

### 6.2 Tabelle

Devono essere costruite:

1. **Tabella 1 — Parametri benchmark**: $A_0$, $c$, $\ell$, $d$, $r^g$, $r^u$, $\bar u$, $K$ e limite su $x_3$.
2. **Tabella 2 — Soluzione benchmark**: $x_1^*,\ldots,x_4^*$, $g_1^*,\ldots,g_4^*$, $u_1^*,u_2^*,u_3^*$ e $\Pi^*$.
3. **Tabella 3 — Verifica dei bilanci temporali**: per ciascuna data, risorse disponibili, fabbisogno, eventuale rimborso di funding, giacenza finale e residuo.
4. **Tabella 4 — Vincoli e slack benchmark**: valore assunto, limite, slack e stato attivo / non attivo.
5. **Tabella 5 — Valori marginali benchmark**: almeno bilanci temporali e limiti di funding economicamente rilevanti.
6. **Tabella 6 — Sensitività a $\theta$**.
7. **Tabella 7 — Sensitività a $\phi$**.
8. **Tabella 8 — Sensitività a $\psi$**.
9. **Tabella 9 — Raffinamento della frontiera di fattibilità**.
10. **Tabella 10 — Confronto degli scenari**.

Le Tabelle 6–8 devono riportare almeno: valore del parametro, stato del solver, fattibilità, $\Pi^*$, $\Delta\Pi^*$, $x^*$, $g^*$, $u^*$ e rapporti $u_t^*/\bar u_t$.

La Tabella 10 deve riportare almeno: valori di $\theta$, $\phi$, $\psi$, $\Pi^*$, perdita rispetto allo Standard, $x^*$, $g^*$, $u^*$, principali vincoli attivi e utilizzo relativo della capacità di funding.

### 6.3 Figure

Devono essere prodotte:

1. **Figura 1 — Valore ottimo e sensitività a $\theta$**: grafico di $\theta\mapsto\Pi^*(\theta)$, limitato ai valori ammissibili.
2. **Figura 2 — Variazione del valore ottimo rispetto a $\theta$**: grafico di $\theta\mapsto\Delta\Pi^*(\theta)$ oppure della corrispondente variazione percentuale.
3. **Figura 3 — Composizione ottima dell'attivo rispetto a $\theta$**: $x_1^*(\theta),\ldots,x_4^*(\theta)$.
4. **Figura 4 — Variazioni dell'asset allocation rispetto al benchmark**: $\Delta x_j^*(\theta)$.
5. **Figura 5 — Funding ottimo e utilizzo della capacità rispetto a $\theta$**.
6. **Figura 6 — Giacenze ottime rispetto a $\theta$**.
7. **Figura 7 — Sensitività a $\phi$**: almeno $\phi\mapsto\Pi^*(\phi)$ e comportamento del funding rispetto alla capacità disponibile.
8. **Figura 8 — Sensitività a $\psi$**: almeno $\psi\mapsto\Pi^*(\psi)$ ed evoluzione del funding ottimo.
9. **Figura 9 — Valori marginali**: bilanci temporali e/o limiti di funding più informativi lungo almeno una griglia.
10. **Figura 10 — Mappa dei principali vincoli attivi**: almeno lungo la sensitività a $\theta$.
11. **Figura 11 — Valore ottimo nei tre scenari**.
12. **Figura 12 — Composizione ottima dell'attivo nei tre scenari**.
13. **Figura 13 — Funding nei tre scenari**.
14. **Figura 14 — Profilo temporale delle giacenze nei tre scenari**.

---

## 7. Controlli richiesti

Devono essere verificati almeno i seguenti punti.

1. L'ordinamento delle variabili utilizzato nel vettore del solver deve essere dichiarato esplicitamente.
2. Le dimensioni della funzione obiettivo, delle matrici e dei vettori dei vincoli devono essere compatibili.
3. La trasformazione del problema di massimo nella convenzione richiesta dal solver deve essere verificata esplicitamente.
4. Il benchmark deve restituire uno stato di ottimizzazione valido.
5. Tutti i bilanci temporali devono essere verificati indipendentemente mediante residuali numerici.
6. I residuali delle uguaglianze devono essere prossimi a zero entro una tolleranza numerica dichiarata.
7. Il vincolo prudenziale deve essere verificato indipendentemente.
8. Il limite $x_3\leq30$ deve essere verificato indipendentemente.
9. I bounds del funding devono essere verificati per ciascuna data.
10. La classificazione attivo / non attivo deve essere coerente con gli slack entro una tolleranza dichiarata.
11. Deve essere verificato numericamente almeno un valore marginale mediante una piccola perturbazione del relativo termine noto o limite.
12. Nell'interpretazione dei valori marginali deve essere tenuto conto della trasformazione massimo / minimo.
13. La funzione parametrica deve riprodurre il benchmark quando $(\theta,\phi,\psi)=(1,1,1)$.
14. Nella sensitività a $\theta$ devono restare fissi $\phi=1$ e $\psi=1$.
15. Nella sensitività a $\phi$ devono restare fissi $\theta=1$ e $\psi=1$.
16. Nella sensitività a $\psi$ devono restare fissi $\theta=1$ e $\phi=1$.
17. Il parametro $\psi$ deve modificare sia il costo del funding nella funzione obiettivo sia il rimborso del funding nei bilanci temporali.
18. Per ogni configurazione parametrica deve essere controllato lo stato del solver prima di utilizzare i valori delle variabili.
19. Quando il problema è dichiarato non ammissibile, non devono essere utilizzati o interpretati eventuali valori presenti in `res.x`.
20. I punti non ammissibili non devono essere collegati artificialmente alla curva di $\Pi^*$.
21. L'intervallo contenente $\theta_{\mathrm{crit}}$ deve essere determinato sulla base della fattibilità.
22. I grafici delle sensitività devono essere costruiti utilizzando esclusivamente risultati solver validi.
23. Devono essere confrontati i cambiamenti della soluzione ottima con i cambiamenti dei vincoli attivi.
24. Le tre configurazioni della scenario analysis devono utilizzare esattamente i valori assegnati nella Sezione 4.13.

---

## 8. Ipotesi e limiti del caso

Il modello assume che:

1. l'orizzonte sia deterministico e articolato in quattro date future;
2. i cash flow degli attivi siano noti e proporzionali agli importi inizialmente investiti;
3. i fabbisogni siano noti all'interno di ciascuna configurazione parametrica;
4. le quantità siano divisibili;
5. funzione obiettivo e vincoli siano lineari per ciascun valore assegnato di $\theta$, $\phi$ e $\psi$;
6. il funding raccolto alla data $t$ sia immediatamente disponibile e venga rimborsato alla data successiva;
7. la capacità di funding sia esogena;
8. il costo del funding sia esogeno e venga modificato mediante il moltiplicatore $\psi$;
9. il comportamento dei depositanti non sia modellato endogenamente;
10. non siano modellati fire sales, haircuts o feedback fra vendite di attività e prezzi di mercato;
11. lo stress non modifichi endogenamente il valore di mercato delle attività;
12. $\theta$, $\phi$ e $\psi$ siano parametri deterministici e non variabili casuali;
13. i tre scenari non abbiano probabilità associate;
14. la scenario analysis non costituisca un problema di programmazione stocastica;
15. le decisioni non siano adattive rispetto a informazione progressivamente osservata;
16. i dati numerici abbiano finalità didattica e non debbano essere interpretati come una ricostruzione del bilancio storico di Silicon Valley Bank;
17. il valore di $\theta_{\mathrm{crit}}$ ottenuto nel caso misuri esclusivamente la frontiera di fattibilità del modello stilizzato e non il livello storico dei deflussi osservati presso SVB.

L'obiettivo del caso è utilizzare la programmazione lineare per rendere osservabile il legame tra:

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
