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

Le variabili

$$
x_1,\quad x_2,\quad x_3,\quad x_4,\quad x_5
$$

rappresentano gli importi inizialmente allocati nelle seguenti classi di attivo:

1. $x_1$: cassa e riserve;
2. $x_2$: titoli a breve scadenza;
3. $x_3$: mutui residenziali a lunga durata;
4. $x_4$: prestiti immobiliari commerciali;
5. $x_5$: altri prestiti e crediti a clientela.

Per ciascuna data futura $t=1,\ldots,4$ si definisce:

$$
g_t\geq0,
$$

dove $g_t$ rappresenta la giacenza di liquidità rimasta immediatamente dopo avere soddisfatto il fabbisogno della data $t$.

Per $t=1,2,3$ si definisce:

$$
u_t\geq0,
$$

dove $u_t$ rappresenta il funding esterno raccolto alla data $t$, disponibile immediatamente e da rimborsare alla data successiva.

### 3.2 Cash flow degli attivi

La matrice

$$
A^{\mathrm{CF}}=(a_{tj})
$$

descrive il profilo temporale dei cash flow.

Il coefficiente $a_{tj}$ indica quanta liquidità viene resa disponibile alla data $t$ da una unità investita al tempo iniziale nell'attivo $j$.

Il cash flow complessivamente prodotto dall'attivo alla data $t$ è:

$$
a_t'x
=
\sum_{j=1}^{5}a_{tj}x_j.
$$

### 3.3 Due ondate di fabbisogno di liquidità

Nel benchmark, i fabbisogni alle quattro date sono raccolti nel vettore:

$$
d=(d_1,d_2,d_3,d_4)'.
$$

Per rappresentare due ondate distinte di pressione sulla raccolta si introducono i parametri $\alpha$ e $\beta$:

$$
d(\alpha,\beta)
=
(32\alpha,18,14,32\beta)'.
$$

Il parametro $\alpha$ modifica il fabbisogno della prima data.

Il parametro $\beta$ modifica il fabbisogno della quarta data.

Il benchmark corrisponde a:

$$
\alpha=1,
\qquad
\beta=1.
$$

### 3.4 Giacenze di liquidità

Una giacenza $g_t$ viene trasferita alla data successiva e produce il rendimento $r_t^g$.

Alla data successiva diventa quindi disponibile:

$$
(1+r_t^g)g_t.
$$

### 3.5 Funding esterno

Il funding raccolto alla data $t$ è immediatamente disponibile come risorsa $u_t$ e deve essere rimborsato alla data successiva per:

$$
(1+r_t^u)u_t.
$$

La capacità massima di funding benchmark è $\bar u_t$.

Per analizzare variazioni della capacità disponibile si introduce il parametro $\phi$:

$$
\bar u_t(\phi)
=
\phi\bar u_t.
$$

Il benchmark corrisponde a:

$$
\phi=1.
$$

### 3.6 Funzione obiettivo

La banca massimizza il risultato economico:

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

Nell'implementazione Python occorre tenere conto della convenzione adottata dal solver utilizzato.

### 3.7 Vincolo sulle risorse iniziali

$$
\sum_{j=1}^{5}x_j=A_0.
$$

### 3.8 Bilanci temporali di liquidità

Alla prima data:

$$
a_1'x+u_1-g_1=d_1(\alpha).
$$

Alle date intermedie $t=2,3$:

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

### 3.9 Vincolo prudenziale

A ciascuna classe di attivo è associato un coefficiente di perdita sotto stress $\ell_j$.

La perdita aggregata sotto stress deve rispettare:

$$
\ell'x\leq K.
$$

### 3.10 Vincolo legacy

Una quota minima delle attività a lunga durata deve essere mantenuta:

$$
x_3+x_4\geq35.
$$

Il vincolo rappresenta in forma stilizzata la presenza di attività legacy che non possono essere eliminate o ristrutturate istantaneamente.

### 3.11 Limite sugli altri prestiti

$$
x_5\leq35.
$$

### 3.12 Capacità di funding e non negatività

Per $t=1,2,3$:

$$
0\leq u_t\leq\phi\bar u_t.
$$

Inoltre:

$$
x_j\geq0,
\qquad j=1,\ldots,5,
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
c'
=
(0.008,0.022,0.035,0.045,0.050).
$$

### 4.3 Perdite unitarie sotto stress

$$
\ell'
=
(0,0.015,0.060,0.100,0.120).
$$

### 4.4 Matrice dei cash flow

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

Le righe corrispondono alle date $t=1,\ldots,4$.

Le colonne corrispondono, nell'ordine, a:

$$
(x_1,x_2,x_3,x_4,x_5).
$$

### 4.5 Fabbisogni benchmark

$$
d'
=
(32,18,14,32).
$$

### 4.6 Rendimenti delle giacenze

$$
{r^g}'
=
(0.004,0.005,0.006).
$$

### 4.7 Costi del funding

$$
{r^u}'
=
(0.018,0.025,0.040).
$$

### 4.8 Capacità benchmark di funding

$$
\bar u'
=
(4,3,2).
$$

### 4.9 Limite prudenziale

$$
K=7.5.
$$

### 4.10 Vincolo legacy

$$
x_3+x_4\geq35.
$$

### 4.11 Limite sugli altri prestiti

$$
x_5\leq35.
$$

### 4.12 Griglia di sensitività ad $\alpha$

Con:

$$
\beta=1,
\qquad
\phi=1,
$$

si utilizza:

$$
\alpha
\in
\{0.90,0.95,1.00,1.05,1.10,1.15\}.
$$

### 4.13 Griglia di sensitività a $\beta$

Con:

$$
\alpha=1,
\qquad
\phi=1,
$$

si utilizza:

$$
\beta
\in
\{0.90,0.95,1.00,1.05,1.10,1.15\}.
$$

### 4.14 Griglia di sensitività a $\phi$

Con:

$$
\alpha=1,
\qquad
\beta=1,
$$

si utilizza:

$$
\phi
\in
\{0.30,0.40,0.50,0.60,0.70,0.80,0.90,1.00,1.10,1.20,1.30\}.
$$

### 4.15 Scenari congiunti

Devono essere analizzati i seguenti scenari:

| Scenario | $\alpha$ | $\beta$ | $\phi$ |
|---|---:|---:|---:|
| Standard | 1.00 | 1.00 | 1.00 |
| Mediamente critico | 1.03 | 1.03 | 0.90 |
| Critico | 1.06 | 1.06 | 0.75 |

Lo scenario Standard coincide con il benchmark.

Gli scenari Mediamente critico e Critico modificano congiuntamente l'intensità delle due ondate di fabbisogno e la capacità massima di funding.

Gli scenari devono essere interpretati come configurazioni deterministiche assegnate e non come eventi ai quali siano associate probabilità.

---

## 5. Quantità da stimare o calcolare

### 5.1 Benchmark

Per il benchmark:

$$
(\alpha,\beta,\phi)
=
(1,1,1),
$$

devono essere determinati:

1. il vettore ottimo degli attivi $x^*$;
2. il vettore ottimo delle giacenze $g^*$;
3. il vettore ottimo del funding $u^*$;
4. il valore ottimo $\Pi^*$;
5. i residuali dei vincoli di uguaglianza;
6. gli slack dei vincoli di disuguaglianza;
7. i bounds attivi;
8. i principali valori marginali restituiti dal solver.

### 5.2 Sensitività univariate

Per ciascun parametro:

$$
p\in\{\alpha,\beta,\phi\},
$$

devono essere determinate, per ogni punto della relativa griglia:

1. la fattibilità del problema;
2. il valore ottimo $\Pi^*(p)$;
3. le componenti $x_j^*(p)$;
4. le componenti $g_t^*(p)$;
5. le componenti $u_t^*(p)$;
6. i principali vincoli attivi;
7. i principali valori marginali quando economicamente informativi.

Devono inoltre essere calcolate:

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

### 5.3 Utilizzo della capacità di funding

Per ogni data e per ciascuna analisi parametrica deve essere calcolato:

$$
\rho_t^u(p)
=
\frac{u_t^*(p)}
{\bar u_t(p)}.
$$

Quando il parametro variato non è $\phi$, il denominatore coincide con la capacità benchmark.

### 5.4 Confronto tra prima e seconda ondata

Le sensitività ad $\alpha$ e a $\beta$ devono essere confrontate esplicitamente.

Il confronto deve riguardare almeno:

1. andamento di $\Pi^*$;
2. variazioni di $x^*$;
3. variazioni di $g^*$;
4. variazioni di $u^*$;
5. cambiamenti nei vincoli attivi;
6. stato di fattibilità.

L'obiettivo è verificare se uno stesso aumento relativo del fabbisogno produce effetti differenti quando si manifesta alla prima data oppure alla data terminale.

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
8. risultati completi delle sensitività ad $\alpha$, $\beta$ e $\phi$;
9. variazioni di $\Pi^*$, $x^*$, $g^*$ e $u^*$ rispetto al benchmark;
10. rapporti di utilizzo della capacità di funding;
11. stato di fattibilità lungo ciascuna griglia;
12. confronto fra prima e seconda ondata;
13. risultati completi dei tre scenari;
14. perdita di valore degli scenari Mediamente critico e Critico rispetto allo Standard.

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
- vincolo legacy;
- limite su $x_5$.

**Tabella 2 — Soluzione benchmark**

Deve riportare:

- $x_1^*,\ldots,x_5^*$;
- $g_1^*,\ldots,g_4^*$;
- $u_1^*,u_2^*,u_3^*$;
- $\Pi^*$.

**Tabella 3 — Verifica dei bilanci temporali**

Per ciascuna data deve riportare almeno:

- risorse disponibili;
- fabbisogno;
- eventuale rimborso di funding;
- giacenza finale;
- residuo dell'uguaglianza.

**Tabella 4 — Vincoli e slack benchmark**

Per ciascun vincolo rilevante deve riportare:

- valore assunto;
- limite;
- slack;
- indicazione attivo / non attivo.

**Tabella 5 — Valori marginali benchmark**

Deve riportare almeno i valori marginali:

- dei bilanci temporali;
- dei limiti di funding economicamente rilevanti;
- del vincolo legacy, se informativo.

**Tabella 6 — Sensitività ad $\alpha$**

Per ciascun valore della griglia deve riportare almeno:

- $\alpha$;
- stato del solver;
- fattibilità;
- $\Pi^*$;
- $\Delta\Pi^*$;
- $x_1^*,\ldots,x_5^*$;
- $g_1^*,\ldots,g_4^*$;
- $u_1^*,u_2^*,u_3^*$;
- rapporti $u_t^*/\bar u_t$.

**Tabella 7 — Sensitività a $\beta$**

Con la stessa struttura della Tabella 6, sostituendo $\alpha$ con $\beta$.

**Tabella 8 — Sensitività a $\phi$**

Con la stessa struttura della Tabella 6, sostituendo $\alpha$ con $\phi$.

**Tabella 9 — Confronto prima / seconda ondata**

Deve confrontare, a parità di variazione relativa, gli effetti di $\alpha$ e $\beta$ almeno su:

- $\Pi^*$;
- $x^*$;
- $g^*$;
- $u^*$;
- vincoli attivi;
- fattibilità.

**Tabella 10 — Confronto degli scenari**

Deve confrontare Standard, Mediamente critico e Critico riportando almeno:

- valori di $\alpha$, $\beta$, $\phi$;
- $\Pi^*$;
- perdita rispetto allo Standard;
- $x^*$;
- $g^*$;
- $u^*$;
- principali vincoli attivi;
- utilizzo relativo della capacità di funding.

### 6.3 Figure

Devono essere prodotte le seguenti figure.

**Figura 1 — Valore ottimo e sensitività ad $\alpha$**

Grafico di:

$$
\alpha\longmapsto\Pi^*(\alpha).
$$

Devono essere riportati soltanto i valori per i quali il problema è ammissibile.

**Figura 2 — Composizione ottima dell'attivo rispetto ad $\alpha$**

Grafico delle cinque serie:

$$
x_1^*(\alpha),\ldots,x_5^*(\alpha).
$$

**Figura 3 — Funding e utilizzo della capacità rispetto ad $\alpha$**

Devono essere rappresentati:

$$
u_t^*(\alpha)
$$

e/o:

$$
\frac{u_t^*(\alpha)}{\bar u_t}.
$$

**Figura 4 — Giacenze ottime rispetto ad $\alpha$**

Grafico di:

$$
g_1^*(\alpha),\ldots,g_4^*(\alpha).
$$

**Figura 5 — Valore ottimo e sensitività a $\beta$**

Grafico di:

$$
\beta\longmapsto\Pi^*(\beta).
$$

**Figura 6 — Composizione ottima dell'attivo rispetto a $\beta$**

Grafico delle cinque serie:

$$
x_1^*(\beta),\ldots,x_5^*(\beta).
$$

**Figura 7 — Funding e giacenze rispetto a $\beta$**

Devono essere rappresentati gli andamenti di $u_t^*(\beta)$ e/o $g_t^*(\beta)$ più informativi.

**Figura 8 — Confronto tra prima e seconda ondata**

La figura deve confrontare in modo diretto gli effetti di $\alpha$ e $\beta$ sul valore ottimo e/o sulla struttura del piano ALM.

**Figura 9 — Sensitività a $\phi$**

La figura deve mostrare almeno:

$$
\phi\longmapsto\Pi^*(\phi)
$$

e il comportamento del funding rispetto alla capacità disponibile.

**Figura 10 — Valori marginali e/o vincoli attivi**

Devono essere rappresentati i principali valori marginali oppure lo stato attivo / non attivo dei vincoli più informativi lungo almeno una delle griglie.

**Figura 11 — Valore ottimo nei tre scenari**

Grafico a barre dei valori:

$$
\Pi_{\mathrm{Standard}}^*,
\qquad
\Pi_{\mathrm{Medio}}^*,
\qquad
\Pi_{\mathrm{Critico}}^*.
$$

**Figura 12 — Composizione ottima dell'attivo nei tre scenari**

Grafico a barre, preferibilmente impilate, delle componenti:

$$
x_1^*,x_2^*,x_3^*,x_4^*,x_5^*.
$$

**Figura 13 — Funding nei tre scenari**

Confronto di:

$$
u_1^*,u_2^*,u_3^*.
$$

**Figura 14 — Profilo temporale delle giacenze nei tre scenari**

Per ogni scenario deve essere rappresentato:

$$
t\longmapsto g_t^*,
\qquad t=1,\ldots,4.
$$

---

## 7. Controlli richiesti

Devono essere verificati almeno i seguenti punti.

1. L'ordinamento delle variabili utilizzato nel vettore del solver deve essere dichiarato esplicitamente.

2. La nuova struttura deve comprendere correttamente cinque classi di attivo.

3. Le dimensioni della funzione obiettivo, delle matrici e dei vettori dei vincoli devono essere compatibili.

4. La trasformazione del problema di massimo nella convenzione richiesta dal solver deve essere verificata esplicitamente.

5. Il benchmark deve restituire uno stato di ottimizzazione valido.

6. Tutti i bilanci temporali devono essere verificati indipendentemente mediante residuali numerici.

7. I residuali delle uguaglianze devono essere prossimi a zero entro una tolleranza numerica dichiarata.

8. Il vincolo prudenziale deve essere verificato indipendentemente.

9. Il vincolo legacy

$$
x_3+x_4\geq35
$$

deve essere verificato indipendentemente e tradotto correttamente nella forma richiesta dal solver.

10. Il limite

$$
x_5\leq35
$$

deve essere verificato indipendentemente.

11. I bounds del funding devono essere verificati per ciascuna data.

12. La classificazione attivo / non attivo deve essere coerente con gli slack entro una tolleranza dichiarata.

13. Deve essere verificato numericamente almeno un valore marginale mediante una piccola perturbazione del relativo termine noto o limite.

14. Nell'interpretazione dei valori marginali deve essere tenuto conto della trasformazione massimo / minimo.

15. La funzione parametrica deve riprodurre il benchmark quando:

$$
(\alpha,\beta,\phi)=(1,1,1).
$$

16. Nella sensitività ad $\alpha$ devono restare fissi:

$$
\beta=1,
\qquad
\phi=1.
$$

17. Nella sensitività a $\beta$ devono restare fissi:

$$
\alpha=1,
\qquad
\phi=1.
$$

18. Nella sensitività a $\phi$ devono restare fissi:

$$
\alpha=1,
\qquad
\beta=1.
$$

19. Il parametro $\alpha$ deve modificare soltanto il fabbisogno della prima data.

20. Il parametro $\beta$ deve modificare soltanto il fabbisogno della quarta data.

21. Il parametro $\phi$ deve modificare soltanto la capacità massima di funding.

22. Per ogni configurazione parametrica deve essere controllato lo stato del solver prima di utilizzare i valori delle variabili.

23. Quando il problema è dichiarato non ammissibile, non devono essere utilizzati o interpretati eventuali valori presenti in `res.x`.

24. I grafici delle sensitività devono essere costruiti utilizzando esclusivamente risultati solver validi.

25. Devono essere confrontati i cambiamenti della soluzione ottima con i cambiamenti dei vincoli attivi.

26. Il confronto fra $\alpha$ e $\beta$ deve tenere conto della diversa collocazione temporale dello shock.

27. Le tre configurazioni della scenario analysis devono utilizzare esattamente i valori assegnati nella Sezione 4.15.

---

## 8. Ipotesi e limiti del caso

Il modello assume che:

1. l'orizzonte sia deterministico e articolato in quattro date future;

2. i cash flow degli attivi siano noti e proporzionali agli importi inizialmente investiti;

3. i fabbisogni siano noti all'interno di ciascuna configurazione parametrica;

4. le quantità siano divisibili;

5. funzione obiettivo e vincoli siano lineari;

6. la prima ondata di deposit run sia rappresentata da uno shock esogeno sul fabbisogno della prima data;

7. la seconda ondata sia rappresentata da uno shock esogeno sul fabbisogno della quarta data;

8. i fabbisogni intermedi restino invariati;

9. il funding raccolto alla data $t$ sia immediatamente disponibile e venga rimborsato alla data successiva;

10. la capacità di funding sia esogena;

11. il costo del funding resti invariato nelle analisi principali;

12. il vincolo legacy rappresenti in forma stilizzata l'inerzia del bilancio e non un vincolo contabile storico di First Republic;

13. il comportamento dei depositanti non sia modellato endogenamente;

14. non siano modellati fire sales, haircuts o feedback fra vendite di attività e prezzi di mercato;

15. non sia modellato il mark-to-market endogeno degli attivi;

16. $\alpha$, $\beta$ e $\phi$ siano parametri deterministici e non variabili casuali;

17. i tre scenari non abbiano probabilità associate;

18. la scenario analysis non costituisca un problema di programmazione stocastica;

19. le decisioni non siano adattive rispetto a informazione progressivamente osservata;

20. i dati numerici abbiano finalità didattica e non debbano essere interpretati come una ricostruzione del bilancio storico di First Republic Bank.

L'obiettivo del caso è trasferire la logica della programmazione lineare e dell'ALM deterministico a una struttura diversa da quella del Caso Aula, rendendo osservabile il legame tra:

$$
\text{inerzia del bilancio},
\qquad
\text{tempistica dei fabbisogni},
\qquad
\text{funding},
\qquad
\text{vincoli},
\qquad
\text{soluzione ottima}.
$$
