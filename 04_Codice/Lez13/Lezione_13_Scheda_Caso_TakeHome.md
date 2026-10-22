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

Per il vincolo legacy deve essere resa osservabile la distinzione tra:

$$
x_3+x_4\geq L,
\qquad
L=35,
$$

e la forma solver:

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

e la non negatività di tutte le variabili.

4. La classificazione dei vincoli come attivi o non attivi deve essere coerente con i relativi slack.

5. I bounds attivi devono essere identificati verificando la distanza della variabile dal relativo lower bound o upper bound.

6. Almeno un valore marginale deve essere verificato mediante una piccola perturbazione del termine noto o del limite cui esso si riferisce.

7. Quando il vincolo legacy è attivo e il relativo marginale è localmente informativo, deve essere effettuata una verifica perturbativa specifica del limite economico.

8. Per ogni configurazione parametrica deve essere verificato lo stato del solver prima di utilizzare i risultati.

9. I risultati di configurazioni non ammissibili non devono essere utilizzati né interpretati economicamente.

### 7.2 Controlli logici e teorici

1. La funzione parametrica deve riprodurre il benchmark in:

$$
(\alpha,\beta,\phi)
=
(1,1,1).
$$

2. Nelle sensitività univariate deve variare un solo parametro alla volta.

3. Il parametro $\alpha$ deve modificare esclusivamente il fabbisogno della prima data.

4. Il parametro $\beta$ deve modificare esclusivamente il fabbisogno della quarta data.

5. Il parametro $\phi$ deve modificare esclusivamente la capacità massima di funding.

6. Il costo del funding deve rimanere invariato nelle sensitività e negli scenari.

7. Le sensitività ad $\alpha$ e a $\beta$ devono essere sviluppate separatamente prima del loro confronto.

8. Il confronto tra $\alpha$ e $\beta$ deve tenere conto della diversa collocazione temporale dello shock.

9. I cambiamenti della soluzione devono essere confrontati con gli eventuali cambiamenti dei vincoli e dei bounds attivi.

10. I valori marginali devono essere associati al corretto vincolo o bilancio e interpretati come quantità locali.

11. La presenza di un vincolo attivo non implica automaticamente un valore marginale economicamente rilevante.

12. La forma economica del vincolo legacy:

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

13. Se:

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

14. Non deve quindi essere applicato un ulteriore cambio di segno al marginale legacy restituito dal solver.

15. La sensitività univariata deve rimanere distinta dalla scenario analysis.

16. Gli scenari devono essere interpretati come configurazioni deterministiche assegnate e non come eventi probabilistici.

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

4. Il vincolo legacy deve essere codificato come:

$$
-x_3-x_4\leq-35.
$$

5. La parametrizzazione dei fabbisogni deve rispettare:

$$
d(\alpha,\beta)
=
(32\alpha,18,14,32\beta)'.
$$

6. I bounds del funding devono rispettare:

$$
0\leq u_t\leq\phi\bar u_t.
$$

7. La variazione di $\alpha$ non deve modificare elementi diversi dal fabbisogno della prima data.

8. La variazione di $\beta$ non deve modificare elementi diversi dal fabbisogno della quarta data.

9. La variazione di $\phi$ non deve modificare la funzione obiettivo o i costi del funding.

10. La funzione parametrica valutata in:

$$
(1,1,1)
$$

deve riprodurre la soluzione benchmark diretta entro la tolleranza numerica adottata.

11. Le tabelle e i grafici devono utilizzare esclusivamente risultati provenienti da esecuzioni valide del solver.

12. Le configurazioni non ammissibili devono essere gestite senza propagare valori numerici non validi.

13. Gli scenari devono essere passati al solver senza modifiche rispetto ai valori assegnati.

14. Tabelle e grafici devono essere rigenerabili mediante riesecuzione ordinata del notebook.

15. Il notebook deve poter essere eseguito integralmente dall'inizio senza dipendere da oggetti prodotti in esecuzioni precedenti non riproducibili.

### 7.4 Controllo conclusivo

Prima dell'interpretazione finale devono risultare verificati congiuntamente:

1. corretta formulazione solver;

2. fattibilità delle configurazioni utilizzate;

3. rispetto dei vincoli e dei bounds;

4. coerenza tra residuali, slack e stato attivo dei vincoli;

5. corretta identificazione dei bounds attivi;

6. corretta interpretazione locale dei valori marginali;

7. corretta relazione:

$$
\frac{\partial\Pi^*}{\partial L}
=
m;
$$

8. corretta azione separata di $\alpha$, $\beta$ e $\phi$;

9. corretto confronto tra shock iniziale e shock terminale;

10. coerenza degli scenari con i valori assegnati;

11. utilizzo esclusivo di risultati numericamente validi.

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

8. la capacità massima di funding sia esogena e parametrizzata mediante:

$$
\bar u_t(\phi)
=
\phi\bar u_t;
$$

9. il costo del funding sia esogeno e rimanga invariato al variare di $\alpha$, $\beta$ e $\phi$;

10. $\alpha$ modifichi esclusivamente il fabbisogno della prima data;

11. $\beta$ modifichi esclusivamente il fabbisogno della quarta data;

12. il vincolo:

$$
x_3+x_4\geq35
$$

rappresenti in forma stilizzata una rigidità legacy del portafoglio;

13. il limite:

$$
x_5\leq35
$$

rappresenti un vincolo distinto dalla rigidità legacy;

14. ogni configurazione parametrica venga risolta come problema deterministico autonomo;

15. gli scenari siano configurazioni deterministiche assegnate e non eventi probabilistici.

### 8.2 Semplificazioni adottate

Il caso utilizza una rappresentazione stilizzata nella quale:

1. le classi di attivo sono aggregate;

2. i fabbisogni di liquidità sono rappresentati direttamente mediante parametri assegnati;

3. la capacità di funding è trattata come limite esogeno;

4. il costo del funding non dipende dalla quantità effettivamente raccolta;

5. il vincolo legacy è rappresentato mediante una singola disuguaglianza lineare;

6. la struttura dei cash flow degli attivi resta invariata nelle diverse configurazioni;

7. non vengono introdotte non linearità associate alla liquidazione degli attivi;

8. le decisioni non vengono aggiornate sulla base di nuova informazione osservata durante l'orizzonte.

### 8.3 Elementi esclusi

Il modello non include:

1. fire sales endogeni;

2. haircuts dipendenti dallo stress;

3. feedback tra vendite, prezzi e liquidità;

4. mark-to-market endogeno degli attivi;

5. dinamica endogena dei depositi;

6. comportamento strategico dei depositanti;

7. rischio di mercato o di credito stocastico;

8. probabilità associate agli scenari;

9. variabili casuali per $\alpha$, $\beta$ o $\phi$;

10. ottimizzazione stocastica;

11. decisioni adattive o multistadio;

12. revisione dinamica del portafoglio;

13. effetti reputazionali, regolamentari o macrofinanziari endogeni;

14. una ricostruzione empirica completa della crisi di First Republic Bank.

### 8.4 Limiti dell'interpretazione

Il caso è un modello didattico deterministico di Asset--Liability Management ispirato alla crisi di First Republic Bank del 2023.

Pertanto:

1. i coefficienti numerici non devono essere interpretati come ricostruzione puntuale del bilancio storico della banca;

2. $\alpha$, $\beta$ e $\phi$ sono parametri deterministici e non stime probabilistiche;

3. Standard, Mediamente critico e Critico non costituiscono una distribuzione di probabilità;

4. la perdita di valore calcolata negli scenari non è una misura probabilistica di rischio;

5. il confronto tra $\alpha$ e $\beta$ riguarda il diverso timing dei fabbisogni nel modello e non consente inferenze generali sulla dinamica storica dei deposit run;

6. il vincolo:

$$
x_3+x_4\geq35
$$

deve essere interpretato esclusivamente come rappresentazione stilizzata di una rigidità legacy;

7. il marginale associato al vincolo legacy ha significato locale;

8. con le convenzioni adottate:

$$
\frac{\partial\Pi^*}{\partial L}
=
m
$$

vale localmente e non costituisce una relazione globale lungo tutte le configurazioni;

9. un vincolo attivo non è necessariamente l'unico determinante economico della soluzione;

10. una maggiore capacità di funding non implica necessariamente un maggiore utilizzo effettivo del funding;

11. la fattibilità del problema non equivale alla sostenibilità economico-finanziaria della banca nel mondo reale;

12. l'ottimalità riguarda esclusivamente la funzione obiettivo e i vincoli specificati;

13. i risultati non incorporano effetti di secondo ordine derivanti da comportamento, prezzi, reputazione o mercato;

14. il modello non consente inferenze causali sulla crisi storica di First Republic Bank;

15. le conclusioni devono essere formulate come risultati del modello stilizzato e non come ricostruzioni empiriche dell'evento storico.