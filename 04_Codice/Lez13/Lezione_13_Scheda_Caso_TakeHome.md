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

Gli output devono essere prodotti esclusivamente a partire da configurazioni per le quali il solver restituisce una soluzione valida.

Devono essere coerenti con le quantità definite nelle sezioni precedenti e devono consentire di distinguere chiaramente:

- soluzione benchmark;
- sensitività univariate;
- confronto tra prima e seconda ondata;
- scenario analysis;
- controlli sul vincolo legacy.

### 6.1 Risultati numerici richiesti

Devono essere riportati almeno i seguenti risultati:

1. soluzione ottima benchmark:
   - $x^*$;
   - $g^*$;
   - $u^*$;

2. valore ottimo benchmark:

$$
\Pi^*;
$$

3. residuali dei vincoli di uguaglianza;

4. slack dei vincoli di disuguaglianza;

5. bounds attivi;

6. principali valori marginali restituiti dal solver;

7. risultati delle sensitività univariate rispetto a:

$$
\alpha,
\qquad
\beta,
\qquad
\phi;
$$

8. variazioni del valore ottimo rispetto al benchmark:

$$
\Delta\Pi^*(p)
=
\Pi^*(p)-\Pi^*(1);
$$

9. variazioni delle componenti della soluzione:

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

10. rapporto di utilizzo della capacità di funding:

$$
\rho_t^u(p)
=
\frac{u_t^*(p)}{\bar u_t(p)};
$$

11. stato di fattibilità per ciascuna configurazione parametrica;

12. principali vincoli e bounds attivi nelle diverse configurazioni;

13. comportamento del vincolo:

$$
x_3+x_4\geq35;
$$

14. confronto degli effetti prodotti da uno shock alla prima data e da uno shock alla data terminale;

15. soluzioni ottime nei tre scenari assegnati;

16. perdita di valore degli scenari Mediamente critico e Critico rispetto allo scenario Standard:

$$
L_s
=
\Pi_{\mathrm{Standard}}^*
-
\Pi_s^*.
$$

### 6.2 Tabelle richieste

Devono essere prodotte le seguenti tabelle.

#### Tabella 1 — Benchmark e diagnostica

Deve riportare almeno:

- $x^*$;
- $g^*$;
- $u^*$;
- $\Pi^*$;
- residuali dei bilanci temporali;
- slack dei principali vincoli;
- bounds attivi;
- principali valori marginali;
- stato attivo / non attivo dei vincoli economicamente rilevanti.

#### Tabella 2 — Sensitività ad $\alpha$

Per ciascun valore della griglia deve riportare almeno:

- $\alpha$;
- stato del solver;
- fattibilità;
- $\Pi^*$;
- $\Delta\Pi^*$;
- $x^*$;
- $g^*$;
- $u^*$;
- principali vincoli attivi;
- valori marginali economicamente informativi.

#### Tabella 3 — Sensitività a $\beta$

Deve avere struttura analoga alla Tabella 2, sostituendo $\alpha$ con $\beta$.

#### Tabella 4 — Sensitività a $\phi$

Per ciascun valore della griglia deve riportare almeno:

- $\phi$;
- stato del solver;
- fattibilità;
- $\Pi^*$;
- $\Delta\Pi^*$;
- $x^*$;
- $g^*$;
- $u^*$;
- rapporti di utilizzo:

$$
\rho_t^u(\phi)
=
\frac{u_t^*(\phi)}
{\phi\bar u_t};
$$

- principali vincoli attivi;
- valori marginali economicamente informativi.

#### Tabella 5 — Confronto degli scenari

Deve confrontare Standard, Mediamente critico e Critico riportando almeno:

- $\alpha$;
- $\beta$;
- $\phi$;
- fattibilità;
- $\Pi^*$;
- perdita rispetto allo Standard;
- $x^*$;
- $g^*$;
- $u^*$;
- principali vincoli attivi;
- utilizzo relativo della capacità di funding.

#### Tabella 6 — Controllo del vincolo legacy

Deve riportare, almeno per il benchmark e per le configurazioni nelle quali il vincolo risulta economicamente informativo:

- valore di:

$$
x_3^*+x_4^*;
$$

- distanza dal limite:

$$
35;
$$

- stato attivo / non attivo;
- marginale restituito dal solver per la disuguaglianza codificata;
- verifica perturbativa del relativo significato economico, quando il vincolo è attivo.

La forma economica:

$$
x_3+x_4\geq L,
\qquad
L=35,
$$

deve essere distinta dalla forma solver:

$$
-x_3-x_4\leq b,
\qquad
b=-L.
$$

Se:

$$
F=-\Pi
$$

è la funzione minimizzata dal solver e:

$$
m
=
\frac{\partial F^*}{\partial b},
$$

allora:

$$
\frac{\partial\Pi^*}{\partial L}
=
m.
$$

Le due inversioni di segno associate a:

$$
F=-\Pi
$$

e:

$$
b=-L
$$

si compensano.

### 6.3 Grafici richiesti

Devono essere prodotti i seguenti grafici.

#### Figura 1 — Valore ottimo al variare di $\alpha$

Rappresentare:

$$
\alpha
\longmapsto
\Pi^*(\alpha).
$$

Devono essere riportate esclusivamente configurazioni ammissibili.

#### Figura 2 — Valore ottimo al variare di $\beta$

Rappresentare:

$$
\beta
\longmapsto
\Pi^*(\beta).
$$

Devono essere riportate esclusivamente configurazioni ammissibili.

#### Figura 3 — Valore ottimo e capacità di funding

Rappresentare:

$$
\phi
\longmapsto
\Pi^*(\phi)
$$

e, quando informativo, il comportamento dell'utilizzo relativo della capacità di funding.

#### Figura 4 — Composizione ottima dell'attivo

Per almeno una delle sensitività più informative devono essere rappresentate:

$$
x_1^*(p),\ldots,x_5^*(p).
$$

#### Figura 5 — Utilizzo della capacità di funding

Lungo la sensitività rispetto a $\phi$ devono essere rappresentati i rapporti:

$$
\rho_t^u(\phi)
=
\frac{u_t^*(\phi)}
{\phi\bar u_t},
\qquad
t=1,2,3.
$$

#### Figura 6 — Confronto tra prima e seconda ondata

Deve confrontare direttamente gli effetti delle variazioni di $\alpha$ e $\beta$.

Il confronto deve riguardare almeno:

$$
\Pi^*
$$

e, quando informativo, una o più componenti di:

$$
x^*,
\qquad
g^*,
\qquad
u^*.
$$

### 6.4 Regole per la produzione degli output

Gli output devono rispettare le seguenti regole:

1. utilizzare esclusivamente risultati provenienti da esecuzioni valide del solver;

2. non interpretare `res.x` quando il solver segnala una configurazione non ammissibile;

3. distinguere chiaramente configurazioni ammissibili e non ammissibili;

4. generare tabelle e grafici direttamente dagli oggetti prodotti dal notebook;

5. evitare l'inserimento manuale di valori numerici nelle celle successive;

6. utilizzare titoli ed etichette che rendano identificabili parametro, variabile e scenario;

7. non collegare graficamente come se fossero continui punti separati da configurazioni non ammissibili;

8. mantenere coerenti notazione matematica e nomi delle variabili computazionali;

9. rendere tutti gli output rigenerabili mediante riesecuzione ordinata del notebook;

10. non esportare automaticamente grafici o tabelle in file esterni, salvo indicazione esplicita del docente.

### 6.5 Funzione interpretativa degli output

Gli output devono consentire allo studente di discutere:

1. come cambia il piano ALM al variare del fabbisogno della prima data;

2. come cambia il piano ALM al variare del fabbisogno della quarta data;

3. perché gli effetti di $\alpha$ e $\beta$ possano differire;

4. come la capacità di funding influenzi la soluzione;

5. quale ruolo svolga il vincolo legacy;

6. come cambino composizione dell'attivo, giacenze, funding e valore ottimo;

7. quali vincoli e bounds diventino economicamente rilevanti;

8. come differiscano Standard, Mediamente critico e Critico;

9. quali conclusioni dipendano dalla struttura del modello stilizzato e non possano essere trasferite direttamente al caso storico di First Republic Bank.

L'interpretazione finale deve basarsi esclusivamente su risultati numericamente validati.

---

## 7. Controlli richiesti

I controlli devono verificare separatamente:

1. correttezza numerica della soluzione;
2. coerenza logico-teorica del modello;
3. correttezza della traduzione computazionale.

L'interpretazione finanziaria finale deve utilizzare esclusivamente risultati che abbiano superato tali controlli.

### 7.1 Controlli numerici

1. Il benchmark deve restituire uno stato di ottimizzazione valido.

2. Tutti i bilanci temporali di liquidità devono essere verificati indipendentemente mediante residuali numerici.

3. I residuali dei vincoli di uguaglianza devono essere prossimi a zero entro una tolleranza numerica dichiarata.

4. Deve essere verificato indipendentemente il vincolo prudenziale:

$$
\ell'x^*\leq7.5.
$$

5. Deve essere verificato indipendentemente il vincolo legacy:

$$
x_3^*+x_4^*\geq35.
$$

6. Deve essere verificato indipendentemente il limite sugli altri prestiti:

$$
x_5^*\leq35.
$$

7. Per ciascuna data deve essere verificato il rispetto dei bounds del funding:

$$
0\leq u_t^*\leq\phi\bar u_t,
\qquad
t=1,2,3.
$$

8. Deve essere verificata la non negatività di tutte le variabili:

$$
x_j^*\geq0,
\qquad
j=1,\ldots,5,
$$

$$
g_t^*\geq0,
\qquad
t=1,\ldots,4,
$$

$$
u_t^*\geq0,
\qquad
t=1,2,3.
$$

9. La classificazione dei vincoli di disuguaglianza come attivi o non attivi deve essere coerente con i relativi slack entro una tolleranza numerica dichiarata.

10. I bounds attivi sulle variabili devono essere identificati separatamente verificando la distanza dal relativo lower bound o upper bound.

11. Deve essere verificato numericamente almeno un valore marginale mediante una piccola perturbazione del termine noto o del limite cui esso si riferisce.

12. Quando il vincolo legacy è attivo e il relativo marginale è localmente informativo, deve essere effettuata una verifica perturbativa specifica del parametro:

$$
L
$$

nella formulazione:

$$
x_3+x_4\geq L.
$$

13. Per ogni configurazione parametrica deve essere verificato lo stato del solver prima di utilizzare i valori della soluzione.

14. Quando il problema risulta non ammissibile, eventuali valori presenti negli oggetti restituiti dal solver non devono essere utilizzati né interpretati economicamente.

### 7.2 Controlli logici e teorici

1. La funzione parametrica deve riprodurre la configurazione benchmark quando:

$$
(\alpha,\beta,\phi)
=
(1,1,1).
$$

2. Nella sensitività rispetto ad $\alpha$ devono rimanere fissi:

$$
\beta=1,
\qquad
\phi=1.
$$

3. Nella sensitività rispetto a $\beta$ devono rimanere fissi:

$$
\alpha=1,
\qquad
\phi=1.
$$

4. Nella sensitività rispetto a $\phi$ devono rimanere fissi:

$$
\alpha=1,
\qquad
\beta=1.
$$

5. Il parametro:

$$
\alpha
$$

deve modificare esclusivamente il fabbisogno della prima data.

6. Il parametro:

$$
\beta
$$

deve modificare esclusivamente il fabbisogno della quarta data.

7. Il parametro:

$$
\phi
$$

deve modificare esclusivamente la capacità massima di funding.

8. Il costo del funding deve restare invariato nelle sensitività e negli scenari.

9. Le tre configurazioni della scenario analysis devono utilizzare esattamente i valori assegnati nella Sezione 4.15.

10. Le sensitività ad $\alpha$ e a $\beta$ devono essere costruite separatamente prima di essere confrontate.

11. Il confronto tra $\alpha$ e $\beta$ deve tenere conto della diversa collocazione temporale dello shock.

12. I cambiamenti della soluzione ottima devono essere confrontati con gli eventuali cambiamenti dei vincoli e dei bounds attivi.

13. L'interpretazione dei valori marginali deve essere coerente con il vincolo o il bilancio cui ciascun marginale si riferisce.

14. I valori marginali devono essere interpretati come quantità locali e non come relazioni globali valide lungo l'intera griglia parametrica.

15. La presenza di un vincolo attivo non implica automaticamente che il relativo valore marginale sia economicamente rilevante: attività del vincolo e valore marginale devono essere controllati separatamente.

16. Il vincolo legacy deve essere interpretato nella sua forma economica:

$$
x_3+x_4\geq L,
\qquad
L=35,
$$

anche se per il solver viene codificato come:

$$
-x_3-x_4\leq -L.
$$

17. L'interpretazione del marginale legacy deve tenere conto congiuntamente delle due trasformazioni:

$$
F=-\Pi
$$

e:

$$
b=-L.
$$

18. Se il solver restituisce:

$$
m
=
\frac{\partial F^*}{\partial b},
$$

allora deve essere utilizzata la relazione:

$$
\frac{\partial\Pi^*}{\partial L}
=
m.
$$

19. Non deve essere introdotto un ulteriore cambio di segno meccanico nel passaggio dal marginale restituito dal solver all'effetto economico di una variazione di:

$$
L.
$$

20. La relazione:

$$
\frac{\partial\Pi^*}{\partial L}
=
m
$$

deve essere interpretata localmente e, quando pertinente, verificata mediante una piccola perturbazione di $L$.

21. La sensitività univariata deve restare distinta dalla scenario analysis:
   - nella sensitività varia un solo parametro alla volta;
   - nella scenario analysis $\alpha$, $\beta$ e $\phi$ possono variare congiuntamente.

22. Le configurazioni di scenario devono essere interpretate come configurazioni deterministiche assegnate e non come eventi probabilistici.

### 7.3 Controlli computazionali

1. L'ordinamento delle variabili nel vettore decisionale deve essere dichiarato esplicitamente e mantenuto invariato in tutte le funzioni.

2. Il vettore decisionale deve comprendere correttamente:

- cinque variabili di allocazione:

$$
x_1,\ldots,x_5;
$$

- quattro giacenze:

$$
g_1,\ldots,g_4;
$$

- tre variabili di funding:

$$
u_1,u_2,u_3.
$$

3. Le dimensioni del vettore della funzione obiettivo, di:

$$
A_{\mathrm{eq}},
\qquad
b_{\mathrm{eq}},
\qquad
A_{\mathrm{ub}},
\qquad
b_{\mathrm{ub}}
$$

e dei bounds devono essere reciprocamente compatibili.

4. La trasformazione della funzione obiettivo dal problema economico di massimo alla convenzione di minimizzazione utilizzata da `scipy.optimize.linprog` deve essere verificata esplicitamente.

5. I quattro bilanci temporali devono essere tradotti senza omissioni o errori di indice.

6. Il vincolo legacy:

$$
x_3+x_4\geq35
$$

deve essere codificato come:

$$
-x_3-x_4\leq-35.
$$

7. La riga corrispondente al vincolo legacy in:

$$
A_{\mathrm{ub}}
$$

e il relativo elemento di:

$$
b_{\mathrm{ub}}
$$

devono essere verificati esplicitamente.

8. Per la verifica del marginale legacy deve essere resa esplicita la parametrizzazione:

$$
x_3+x_4\geq L,
$$

$$
b=-L,
$$

$$
F=-\Pi.
$$

9. Se:

$$
m
=
\frac{\partial F^*}{\partial b},
$$

la verifica perturbativa deve confrontare direttamente il marginale con:

$$
\frac{\Pi^*(L+\varepsilon)-\Pi^*(L)}
{\varepsilon}
$$

per un valore di $\varepsilon$ sufficientemente piccolo e in una regione nella quale il confronto locale sia significativo.

10. La costruzione del vettore dei fabbisogni deve rispettare:

$$
d(\alpha,\beta)
=
(32\alpha,18,14,32\beta)'.
$$

11. I bounds del funding devono essere aggiornati correttamente quando varia $\phi$:

$$
0\leq u_t\leq\phi\bar u_t.
$$

12. Una variazione di $\alpha$ non deve modificare coefficienti diversi dal fabbisogno della prima data.

13. Una variazione di $\beta$ non deve modificare coefficienti diversi dal fabbisogno della quarta data.

14. Una variazione di $\phi$ non deve modificare la funzione obiettivo o i costi del funding.

15. I risultati prodotti dalla funzione parametrica nel punto:

$$
(1,1,1)
$$

devono coincidere con quelli della soluzione benchmark diretta entro la tolleranza numerica adottata.

16. Le tabelle e i grafici delle sensitività devono utilizzare esclusivamente risultati provenienti da esecuzioni valide del solver.

17. Le configurazioni non ammissibili devono essere identificate e gestite senza propagare valori numerici non validi nelle tabelle, nei grafici o nei confronti successivi.

18. Gli scenari devono essere passati alla funzione solver senza modifiche rispetto ai valori assegnati.

19. Tabelle e grafici devono essere generati direttamente dagli oggetti prodotti nel notebook.

20. Il notebook deve poter essere rieseguito integralmente dall'inizio senza dipendere da variabili, risultati o oggetti prodotti in esecuzioni precedenti non riproducibili.

### 7.4 Coerenza finale dei controlli

Prima dell'interpretazione conclusiva devono risultare congiuntamente verificati:

1. correttezza della formulazione solver;

2. fattibilità delle configurazioni utilizzate;

3. rispetto dei vincoli e dei bounds;

4. coerenza tra residuali, slack e stato attivo dei vincoli;

5. corretta identificazione dei bounds attivi;

6. corretta associazione dei valori marginali ai rispettivi vincoli e bilanci;

7. corretta gestione del vincolo legacy;

8. corretta relazione:

$$
\frac{\partial\Pi^*}{\partial L}
=
m;
$$

9. assenza di un cambio di segno aggiuntivo non giustificato nell'interpretazione del marginale legacy;

10. corretta azione separata di $\alpha$, $\beta$ e $\phi$;

11. coerenza delle sensitività con i parametri effettivamente modificati;

12. corretto confronto tra shock alla prima data e shock alla data terminale;

13. coerenza delle configurazioni della scenario analysis con i valori assegnati;

14. distinzione fra sensitività univariata e scenario analysis;

15. utilizzo esclusivo di risultati numericamente validi nelle tabelle, nei grafici e nell'interpretazione.

L'interpretazione finanziaria finale deve basarsi esclusivamente su output che abbiano superato tali controlli.

---

## 8. Ipotesi e limiti del caso

### 8.1 Ipotesi modellistiche

Il caso assume che:

1. l'orizzonte sia articolato in quattro date discrete;

2. i cash flow generati dalle classi di attivo siano noti e deterministici una volta fissata la configurazione parametrica;

3. i fabbisogni di liquidità siano noti per ciascuna configurazione di:

$$
(\alpha,\beta,\phi);
$$

4. le decisioni di allocazione siano divisibili;

5. funzione obiettivo e vincoli siano lineari;

6. il parametro:

$$
\alpha
$$

modifichi esclusivamente il fabbisogno della prima data;

7. il parametro:

$$
\beta
$$

modifichi esclusivamente il fabbisogno della quarta data;

8. i fabbisogni delle date intermedie restino invariati;

9. il funding raccolto alla data $t$ sia immediatamente disponibile alla stessa data;

10. il funding raccolto alla data $t$ debba essere rimborsato alla data successiva secondo la struttura specificata dal modello;

11. la capacità massima di funding sia esogena e parametrizzata da:

$$
\bar u_t(\phi)
=
\phi\bar u_t;
$$

12. il costo del funding sia fissato e non dipenda da $\alpha$, $\beta$ o $\phi$;

13. il vincolo:

$$
x_3+x_4\geq35
$$

rappresenti in forma stilizzata una rigidità legacy del portafoglio;

14. il limite:

$$
x_5\leq35
$$

rappresenti un vincolo distinto dalla rigidità legacy;

15. ogni configurazione parametrica venga risolta come problema deterministico autonomo.

### 8.2 Semplificazioni adottate

Il caso adotta le seguenti semplificazioni:

1. il comportamento dei depositanti non viene modellato endogenamente;

2. i fabbisogni di liquidità sono rappresentati direttamente attraverso i parametri assegnati;

3. la capacità di funding è trattata come limite esogeno;

4. il costo del funding non dipende dalla quantità effettivamente raccolta;

5. non sono previste decisioni di funding con durata superiore a quella specificata dal modello;

6. il vincolo legacy è rappresentato mediante una singola disuguaglianza lineare;

7. non vengono introdotte non linearità associate alla liquidazione degli attivi;

8. la struttura dei cash flow degli attivi resta invariata al variare degli scenari;

9. $\alpha$, $\beta$ e $\phi$ sono trattati come parametri deterministici;

10. gli scenari Standard, Mediamente critico e Critico sono configurazioni assegnate e non scenari probabilistici;

11. le decisioni vengono formulate ex ante e non vengono aggiornate sulla base di nuova informazione osservata durante l'orizzonte.

### 8.3 Elementi esclusi

Il modello non include:

1. fire sales endogeni;

2. haircuts dipendenti dallo stress;

3. feedback tra vendite, prezzi e liquidità;

4. mark-to-market endogeno degli attivi;

5. dinamica endogena dei depositi;

6. comportamento strategico dei depositanti;

7. rischio di mercato stocastico;

8. rischio di credito stocastico;

9. probabilità associate agli scenari;

10. variabili casuali per $\alpha$, $\beta$ o $\phi$;

11. ottimizzazione stocastica;

12. decisioni adattive o multistadio;

13. revisione dinamica del portafoglio sulla base di informazione progressivamente osservata;

14. effetti reputazionali;

15. interventi regolamentari endogeni;

16. effetti macrofinanziari di equilibrio generale.

### 8.4 Limiti dell'interpretazione

I risultati devono essere interpretati entro i seguenti limiti.

1. Il caso è un modello didattico deterministico di Asset-Liability Management.

2. I coefficienti numerici non devono essere interpretati come ricostruzione puntuale dei dati storici di First Republic Bank.

3. I parametri:

$$
\alpha,
\qquad
\beta,
\qquad
\phi
$$

non costituiscono stime probabilistiche.

4. Le tre configurazioni di scenario non rappresentano una distribuzione di probabilità.

5. La perdita di valore calcolata negli scenari non costituisce una misura probabilistica di rischio.

6. Il confronto fra $\alpha$ e $\beta$ riguarda il diverso timing dei fabbisogni all'interno del modello e non consente, da solo, inferenze generali sulla dinamica storica delle corse agli sportelli.

7. Il vincolo:

$$
x_3+x_4\geq35
$$

deve essere interpretato esclusivamente come rappresentazione stilizzata di una rigidità legacy.

8. Il valore marginale associato al vincolo legacy ha significato locale e dipende dalla configurazione nella quale viene calcolato.

9. La relazione:

$$
\frac{\partial\Pi^*}{\partial L}
=
m
$$

vale localmente con le convenzioni di codifica definite nel modello e non deve essere interpretata come relazione globale.

10. Un vincolo attivo non è necessariamente il solo determinante economico della soluzione.

11. Un marginale nullo o prossimo a zero non implica che il corrispondente vincolo sia irrilevante in tutte le configurazioni.

12. Una maggiore capacità di funding non implica necessariamente un maggiore utilizzo effettivo del funding.

13. La fattibilità del modello non equivale a sostenibilità economica o finanziaria nel mondo reale.

14. L'ottimalità della soluzione riguarda esclusivamente la funzione obiettivo e i vincoli specificati.

15. I risultati non incorporano effetti di secondo ordine derivanti da comportamento, prezzi, reputazione o mercato.

16. Il modello non consente inferenze causali sulla crisi storica di First Republic Bank.

17. Le conclusioni devono essere formulate come risultati del modello stilizzato, non come ricostruzioni empiriche dell'evento storico.