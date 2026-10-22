# Scheda Costruzione Caso Applicativo

Documento interno di progettazione docente. Compilazione riferita al **Caso TakeHome** della Lezione 13.

## 1. Identificazione del caso

- **Lezione:** 13 — Applicazione in Python: programmazione lineare e ALM deterministico
- **Tipo di caso:** TakeHome
- **Titolo:** **First Republic Bank 2023 — due ondate di deposit run e vincoli di ristrutturazione del bilancio**
- **Destinatari:** studenti del secondo anno del Corso di Laurea Magistrale in Finanza e Risk Management
- **Uso previsto:** caso applicativo autonomo per trasferire il metodo di programmazione lineare e ALM deterministico sviluppato nel Caso Aula SVB a una struttura finanziaria differente, caratterizzata da un portafoglio più loan-heavy, da una quota minima di attività legacy non immediatamente smobilizzabili, da due ondate distinte di pressione sui depositi e da una capacità di funding che può ridursi.

## 2. Contesto e motivazione

Il caso è ispirato alla crisi di First Republic Bank del 2023.

First Republic presentava un modello di business fortemente orientato alla clientela ad alta patrimonializzazione, con una rilevante componente di prestiti e mutui e una forte dipendenza da depositi non assicurati. Dopo il fallimento di Silicon Valley Bank e Signature Bank, la perdita di fiducia dei depositanti determinò deflussi molto rilevanti. La banca riuscì inizialmente a fronteggiare le richieste di liquidità, ma il perdurare della pressione sulla raccolta e i vincoli alla ristrutturazione del bilancio limitarono progressivamente le opzioni disponibili.

Il caso didattico non ricostruisce quantitativamente il bilancio storico di First Republic. La calibrazione è stilizzata e serve a rappresentare tre caratteristiche strutturali diverse da quelle del Caso Aula SVB:

1. una maggiore incidenza di attività creditizie a lunga durata;
2. una quota minima di attività legacy che non può essere eliminata liberamente dalla soluzione ottima;
3. una crisi di liquidità rappresentata da due ondate distinte di deflussi, una iniziale e una successiva.

Il TakeHome deve quindi richiedere allo studente di trasferire il metodo, non di replicare la struttura del Caso Aula con coefficienti diversi.

La sequenza logica è:

$$
\text{modello ALM differente}
\longrightarrow
\text{forma solver}
\longrightarrow
\text{benchmark}
\longrightarrow
\text{sensitività}
\longrightarrow
\text{scenari congiunti}
\longrightarrow
\text{interpretazione}.
$$

## 3. Domanda quantitativa e funzione didattica

**Domanda quantitativa:**  
dato un bilancio stilizzato di First Republic Bank caratterizzato da attivit\`a a liquidit\`a differenziata, da una quota minima di attivit\`a legacy e da due ondate distinte di fabbisogno di liquidit\`a, come si costruisce e si risolve il corrispondente programma lineare e come cambia il piano ALM ottimo al variare dell'intensit\`a della prima ondata di deflussi, della seconda ondata e della capacit\`a disponibile di funding?

**Obiettivo didattico:**  
portare lo studente a:

1. riconoscere la struttura di un problema di Asset--Liability Management gi\`a studiato quando viene trasferita a una configurazione finanziaria diversa;
2. riformulare autonomamente variabili, vincoli e matrice dei cash flow senza replicare meccanicamente il Caso Aula;
3. gestire una dimensione dell'attivo maggiore rispetto al Caso Aula;
4. introdurre e interpretare un vincolo strutturale su attivit\`a legacy;
5. costruire e validare una funzione solver parametrica;
6. distinguere gli effetti di una pressione di liquidit\`a iniziale da quelli di una pressione che si manifesta alla data terminale;
7. analizzare separatamente l'effetto della capacit\`a massima di funding;
8. distinguere sensitività univariata e scenario analysis multivariata;
9. interpretare variazioni del valore ottimo, della composizione dell'attivo, delle giacenze, del funding, dei vincoli attivi e dei valori marginali;
10. trasferire il metodo sviluppato nel Caso Aula mantenendo continuit\`a metodologica ma autonomia del problema finanziario.

**Collegamento con le lezioni teoriche precedenti:**  
il caso utilizza direttamente i risultati sviluppati nei Capitoli 11 e 12 e la loro traduzione computazionale nel Capitolo 13.

Dal Capitolo 11 riprende:

- la formulazione di un problema di programmazione lineare;
- la distinzione tra funzione obiettivo, vincoli e bounds;
- la nozione di regione ammissibile;
- il ruolo dei vincoli attivi;
- la sensitività della soluzione;
- la dualit\`a e l'interpretazione economica dei valori marginali.

Dal Capitolo 12 riprende:

- la rappresentazione temporale dei cash flow degli attivi;
- i bilanci di liquidit\`a alle diverse date;
- le giacenze trasferite nel tempo;
- il ricorso a funding esterno e il relativo rimborso;
- i vincoli di capacit\`a del funding;
- l'interpretazione marginale dei vincoli temporali.

Dal Capitolo 13 riprende:

- la traduzione del modello ALM nella forma richiesta da `scipy.optimize.linprog`;
- la distinzione tra vettore obiettivo, uguaglianze, disuguaglianze e bounds;
- la lettura di residuali, slack e valori marginali;
- la costruzione di funzioni solver parametrizzate;
- l'analisi di sensitività e di scenari.

Il Caso TakeHome richiede per\`o un trasferimento del metodo a una struttura diversa da quella di Silicon Valley Bank: aumenta il numero delle classi di attivo, introduce un vincolo minimo su attivit\`a legacy e distribuisce la pressione di liquidit\`a in due date distinte.

**Concetti teorici da rendere osservabili:**  
il caso deve rendere operativamente osservabili:

1. la corrispondenza tra formulazione economico-finanziaria e forma matriciale del programma lineare;
2. la distinzione tra vincoli di uguaglianza, disuguaglianze e bounds;
3. il ruolo dei bilanci temporali nel garantire la fattibilit\`a del piano ALM;
4. il significato economico dei vincoli strutturali sul portafoglio;
5. la differenza tra vincoli superiori e vincoli inferiori;
6. la necessit\`a di trasformare un vincolo del tipo

$$
x_3+x_4\geq35
$$

nella forma compatibile con il solver:

$$
-x_3-x_4\leq-35;
$$

7. la relazione tra forma codificata del vincolo e interpretazione del valore marginale restituito dal solver;
8. la distinzione tra shock di liquidit\`a iniziale e shock terminale;
9. la dipendenza della soluzione ottima dalla capacit\`a disponibile di funding;
10. la differenza tra sensitività univariata e variazione congiunta dei driver negli scenari;
11. il possibile cambiamento dei vincoli attivi al variare dei parametri;
12. la distinzione tra configurazioni ammissibili e non ammissibili.

**Funzione della procedura computazionale:**  
il ricorso a Python e al solver \`e necessario per trasferire sistematicamente la struttura teorica del modello a una configurazione pi\`u articolata rispetto al Caso Aula e per risolvere ripetutamente il programma lineare al variare dei parametri $\alpha$, $\beta$ e $\phi$.

La procedura computazionale deve consentire di:

1. costruire la forma solver del modello First Republic;
2. verificare la corretta codifica dei vincoli, compreso il vincolo legacy;
3. risolvere e validare la configurazione benchmark;
4. controllare residuali, slack, bounds attivi e fattibilit\`a;
5. estrarre e interpretare i principali valori marginali restituiti dal solver;
6. costruire una funzione parametrica dipendente da $\alpha$, $\beta$ e $\phi$;
7. risolvere il modello lungo le tre griglie di sensitività;
8. confrontare gli effetti di shock alla prima e alla quarta data;
9. analizzare l'utilizzo della capacit\`a di funding;
10. confrontare configurazioni congiunte mediante scenario analysis.

La procedura computazionale deve rendere osservabili e verificabili le propriet\`a del modello, senza sostituire l'interpretazione economico-finanziaria finale dello studente.

**Ruolo dell'informazione, degli scenari e dei vincoli:**  
il caso \`e deterministico. Non sono presenti variabili casuali, probabilit\`a di scenario o decisioni adattive a informazione futura.

Per ciascuna configurazione di $(\alpha,\beta,\phi)$, coefficienti, cash flow, fabbisogni e capacit\`a di funding sono considerati noti.

I tre parametri hanno funzioni distinte:

- $\alpha$ modifica il fabbisogno della prima data e rappresenta l'intensit\`a della prima ondata di deflussi;
- $\beta$ modifica il fabbisogno della quarta data e rappresenta l'intensit\`a della seconda ondata di deflussi;
- $\phi$ modifica la capacit\`a massima di funding disponibile alle prime tre date.

Le sensitività univariate modificano un solo parametro alla volta, mantenendo gli altri al valore benchmark.

La scenario analysis modifica invece congiuntamente $\alpha$, $\beta$ e $\phi$ secondo configurazioni assegnate. Tali configurazioni non rappresentano eventi aleatori e non hanno probabilit\`a associate.

I vincoli hanno una funzione centrale nell'interpretazione del caso:

- i bilanci temporali impongono che i fabbisogni siano soddisfatti alle rispettive date;
- il vincolo prudenziale limita l'esposizione complessiva alla perdita sotto stress;
- il vincolo

$$
x_3+x_4\geq35
$$

impone il mantenimento di una quota minima di attivit\`a legacy e rappresenta una rigidit\`a strutturale nella ristrutturazione del bilancio;

- il limite

$$
x_5\leq35
$$

impedisce una concentrazione eccessiva negli altri prestiti;

- i bounds sul funding limitano la capacit\`a di utilizzare risorse esterne.

L'analisi di slack, bounds attivi e valori marginali deve consentire di identificare quali restrizioni determinano il piano ottimo nelle diverse configurazioni e di distinguere correttamente il significato economico del vincolo originale dalla forma algebrica utilizzata per il solver.

## 4. Specifica teorico-matematica

### Grandezze e variabili

- $x_j$, $j=1,\ldots,5$: ammontare inizialmente allocato nelle cinque classi di attivo:
  1. cassa e riserve;
  2. titoli a breve scadenza;
  3. mutui residenziali a lunga durata;
  4. prestiti immobiliari commerciali;
  5. altri prestiti e crediti a clientela;

- $g_t$, $t=1,\ldots,4$: giacenza di liquidità immediatamente successiva al soddisfacimento del fabbisogno alla data $t$;

- $u_t$, $t=1,2,3$: funding esterno raccolto alla data $t$, disponibile immediatamente e da rimborsare alla data successiva;

- $c_j$: coefficiente di redditività dell'attivo $j$;

- $\ell_j$: perdita unitaria sotto stress associata all'attivo $j$;

- $a_{tj}$: quota di una unità dell'attivo $j$ resa liquida alla data $t$;

- $d_t$: fabbisogno di liquidità benchmark alla data $t$;

- $r_t^g$: rendimento della giacenza trasferita dalla data $t$ alla data $t+1$;

- $r_t^u$: costo del funding raccolto alla data $t$;

- $\bar u_t$: capacità benchmark di funding alla data $t$;

- $\alpha$: moltiplicatore dell'intensità della prima ondata di deflussi;

- $\beta$: moltiplicatore dell'intensità della seconda ondata di deflussi;

- $\phi$: moltiplicatore della capacità massima di funding.

### Eventi, informazione, stati o scenari

Il caso è deterministico e non prevede variabili casuali, stati informativi aleatori o probabilità associate agli scenari.

La configurazione benchmark è:

$$
(\alpha,\beta,\phi)=(1,1,1).
$$

La sensitività rispetto ad $\alpha$, mantenendo $\beta=1$ e $\phi=1$, utilizza:

$$
\alpha
\in
\{0.90,0.95,1.00,1.05,1.10,1.15\}.
$$

La sensitività rispetto a $\beta$, mantenendo $\alpha=1$ e $\phi=1$, utilizza:

$$
\beta
\in
\{0.90,0.95,1.00,1.05,1.10,1.15\}.
$$

La sensitività rispetto a $\phi$, mantenendo $\alpha=1$ e $\beta=1$, utilizza:

$$
\phi
\in
\{0.30,0.40,0.50,0.60,0.70,0.80,0.90,1.00,1.10,1.20,1.30\}.
$$

Gli scenari congiunti assegnati sono:

- scenario Standard:

$$
(\alpha,\beta,\phi)=(1.00,1.00,1.00);
$$

- scenario Mediamente critico:

$$
(\alpha,\beta,\phi)=(1.03,1.03,0.90);
$$

- scenario Critico:

$$
(\alpha,\beta,\phi)=(1.06,1.06,0.75).
$$

Gli scenari rappresentano configurazioni deterministiche dei parametri e non eventi ai quali siano associate probabilità.

### Parametri e dati

Le risorse iniziali sono:

$$
A_0=100.
$$

Il vettore dei coefficienti di redditività è:

$$
c'
=
(0.008,0.022,0.035,0.045,0.050).
$$

Il vettore delle perdite unitarie sotto stress è:

$$
\ell'
=
(0,0.015,0.060,0.100,0.120).
$$

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

Le righe corrispondono alle date $t=1,\ldots,4$ e le colonne, nell'ordine, alle variabili:

$$
(x_1,x_2,x_3,x_4,x_5).
$$

I fabbisogni benchmark sono:

$$
d'
=
(32,18,14,32).
$$

I rendimenti delle giacenze sono:

$$
{r^g}'
=
(0.004,0.005,0.006).
$$

I costi del funding sono:

$$
{r^u}'
=
(0.018,0.025,0.040).
$$

Le capacità benchmark di funding sono:

$$
\bar u'
=
(4,3,2).
$$

Il limite prudenziale è:

$$
K=7.5.
$$

Il vincolo minimo sulle attività legacy è:

$$
x_3+x_4\geq35.
$$

Il limite massimo sugli altri prestiti è:

$$
x_5\leq35.
$$

### Ipotesi modellistiche

Il caso assume:

1. orizzonte deterministico a quattro date;
2. coefficienti, cash flow e fabbisogni noti per ogni configurazione parametrica;
3. divisibilità delle quantità;
4. assenza di costi fissi;
5. linearità della funzione obiettivo e dei vincoli;
6. effetto di $\alpha$ limitato al fabbisogno della prima data;
7. effetto di $\beta$ limitato al fabbisogno della quarta data;
8. fabbisogni intermedi invariati rispetto al benchmark;
9. variazione proporzionale della capacità massima di funding con $\phi$;
10. costo del funding invariato nelle sensitività e negli scenari principali;
11. presenza di una quota minima di attività legacy che non può essere ristrutturata istantaneamente;
12. variazione di un solo parametro alla volta nelle sensitività univariate;
13. variazione congiunta di $\alpha$, $\beta$ e $\phi$ nella scenario analysis;
14. assenza di probabilità associate agli scenari;
15. natura stilizzata e didattica del caso, che non costituisce una ricostruzione quantitativa del bilancio storico di First Republic Bank.

### Formule vincolanti

I fabbisogni parametrizzati sono:

$$
d(\alpha,\beta)
=
(32\alpha,18,14,32\beta)'.
$$

La capacità massima di funding è:

$$
\bar u_t(\phi)
=
\phi\bar u_t.
$$

La funzione obiettivo è:

$$
\max_{x,g,u}
\Pi(x,g,u)
=
c'x
+
\sum_{t=1}^{3}r_t^g g_t
-
\sum_{t=1}^{3}r_t^u u_t.
$$

Il vincolo sulle risorse iniziali è:

$$
\sum_{j=1}^{5}x_j=A_0.
$$

Il primo bilancio temporale è:

$$
a_1'x+u_1-g_1=d_1(\alpha).
$$

I bilanci intermedi, per $t=2,3$, sono:

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

Il bilancio terminale è:

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

Per la codifica nella forma standard richiesta dal solver il vincolo legacy deve essere riscritto come:

$$
-x_3-x_4\leq-35.
$$

Il limite sugli altri prestiti è:

$$
x_5\leq35.
$$

I limiti di funding sono:

$$
0\leq u_t\leq\phi\bar u_t,
\qquad
t=1,2,3.
$$

Le condizioni di non negatività sono:

$$
x_j\geq0,
\qquad
j=1,\ldots,5,
$$

e:

$$
g_t\geq0,
\qquad
t=1,\ldots,4.
$$

### Quantità teoriche da stimare o calcolare

Devono essere determinate:

1. la soluzione ottima benchmark $x^*$, $g^*$ e $u^*$;
2. il valore ottimo $\Pi^*$;
3. i residuali dei vincoli di uguaglianza;
4. gli slack dei vincoli di disuguaglianza;
5. i bounds attivi;
6. i principali valori marginali restituiti dal solver;
7. l'evoluzione di $\Pi^*$ lungo le griglie di $\alpha$, $\beta$ e $\phi$;
8. l'evoluzione di $x^*$, $g^*$ e $u^*$ lungo le tre griglie;
9. la variazione del valore ottimo rispetto al benchmark:

$$
\Delta\Pi^*(p)
=
\Pi^*(p)-\Pi^*(1);
$$

10. le variazioni delle componenti ottime:

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

11. il rapporto di utilizzo della capacità di funding:

$$
\rho_t^u(p)
=
\frac{u_t^*(p)}{\bar u_t(p)};
$$

12. lo stato di fattibilità lungo le griglie di $\alpha$, $\beta$ e $\phi$;
13. i principali vincoli attivi nelle diverse configurazioni;
14. il comportamento del vincolo legacy al variare dei parametri;
15. le soluzioni ottime nei tre scenari congiunti;
16. la perdita di valore di ciascuno scenario rispetto allo scenario Standard.

### Proprietà teoriche da verificare

Devono essere verificate almeno le seguenti proprietà.

1. La soluzione deve soddisfare il vincolo sulle risorse iniziali:

$$
\sum_{j=1}^{5}x_j=100.
$$

2. Devono essere soddisfatti i quattro bilanci temporali di liquidità.

3. I residuali numerici dei vincoli di uguaglianza devono essere coerenti con la tolleranza numerica adottata.

4. Gli slack devono essere coerenti con la classificazione dei vincoli di disuguaglianza come attivi o non attivi.

5. I valori delle variabili devono essere coerenti con l'identificazione dei bounds attivi.

6. Devono essere rispettati i limiti di funding:

$$
0\leq u_t\leq\phi\bar u_t,
\qquad
t=1,2,3.
$$

7. Deve essere rispettato il vincolo prudenziale:

$$
\ell'x\leq7.5.
$$

8. Deve essere rispettato il vincolo legacy:

$$
x_3+x_4\geq35.
$$

9. Deve essere rispettato il limite:

$$
x_5\leq35.
$$

10. I valori marginali devono essere associati correttamente ai vincoli e ai bilanci ai quali si riferiscono e devono essere interpretati come quantità locali.

11. Per il vincolo legacy occorre distinguere la forma economica:

$$
x_3+x_4\geq L,
\qquad
L=35,
$$

dalla forma utilizzata dal solver:

$$
-x_3-x_4\leq b,
\qquad
b=-L.
$$

12. Se il problema economico massimizza:

$$
\Pi
$$

mentre il solver minimizza:

$$
F=-\Pi,
$$

e se il marginale restituito dal solver per la riga del vincolo legacy è:

$$
m
=
\frac{\partial F^*}{\partial b},
$$

allora deve essere verificata la relazione:

$$
\frac{\partial\Pi^*}{\partial L}
=
m.
$$

Infatti:

$$
\frac{\partial F^*}{\partial L}
=
\frac{\partial F^*}{\partial b}
\frac{\partial b}{\partial L}
=
m(-1)
=
-m,
$$

e, poiché:

$$
F^*=-\Pi^*,
$$

si ha:

$$
-\frac{\partial\Pi^*}{\partial L}
=
-m,
$$

da cui:

$$
\frac{\partial\Pi^*}{\partial L}
=
m.
$$

Le due inversioni di segno, dovute rispettivamente a:

$$
F=-\Pi
$$

e:

$$
b=-L,
$$

si compensano.

13. Non deve quindi essere applicato un ulteriore cambio di segno meccanico al marginale restituito dal solver quando lo si interpreta rispetto al limite economico:

$$
L.
$$

14. Quando il vincolo legacy è attivo e il marginale è localmente informativo, la relazione:

$$
\frac{\partial\Pi^*}{\partial L}
=
m
$$

deve essere verificata numericamente mediante una piccola perturbazione di:

$$
L.
$$

15. La verifica perturbativa deve utilizzare una perturbazione sufficientemente piccola da restare, per quanto possibile, nello stesso regime locale della soluzione.

16. La funzione parametrica deve distinguere correttamente gli effetti di:

$$
\alpha,
\qquad
\beta,
\qquad
\phi.
$$

17. Il parametro:

$$
\alpha
$$

deve modificare esclusivamente il fabbisogno della prima data.

18. Il parametro:

$$
\beta
$$

deve modificare esclusivamente il fabbisogno della quarta data.

19. Il parametro:

$$
\phi
$$

deve modificare esclusivamente la capacità massima di funding.

20. Nelle sensitività univariate deve variare un solo parametro alla volta.

21. Le configurazioni non ammissibili devono essere distinte dalle configurazioni ammissibili prima di utilizzare risultati numerici, tabelle o grafici.

22. I cambiamenti della soluzione ottima devono essere confrontati con gli eventuali cambiamenti dei vincoli e dei bounds attivi.

23. Gli effetti di una variazione di:

$$
\alpha
$$

devono essere distinti dagli effetti di una variazione di:

$$
\beta,
$$

in modo da rendere osservabile il ruolo della collocazione temporale del fabbisogno.

24. La sensitività univariata deve restare distinta dalla scenario analysis, nella quale:

$$
\alpha,
\qquad
\beta,
\qquad
\phi
$$

possono variare congiuntamente.

25. Gli scenari devono essere interpretati come configurazioni deterministiche assegnate e non come eventi probabilistici.

### Soglie, target o vincoli rilevanti

Le principali soglie e condizioni di ammissibilità sono:

- risorse iniziali:

$$
\sum_{j=1}^{5}x_j=100;
$$

- limite prudenziale:

$$
\ell'x\leq7.5;
$$

- quota minima di attività legacy:

$$
x_3+x_4\geq35;
$$

- limite agli altri prestiti:

$$
x_5\leq35;
$$

- capacità massime benchmark di funding:

$$
\bar u'=(4,3,2),
$$

modificate mediante $\phi$;

- non negatività di $x$, $g$ e $u$;

- soddisfacimento dei fabbisogni alle quattro date secondo:

$$
d(\alpha,\beta)
=
(32\alpha,18,14,32\beta)'.
$$

### Quantità finali di interesse

Le quantità finali da utilizzare nell'interpretazione sono:

1. valore ottimo e composizione del piano ALM benchmark;
2. struttura delle giacenze e del funding;
3. vincoli e bounds attivi;
4. ruolo economico del vincolo legacy;
5. valori marginali economicamente informativi;
6. risposta del piano ottimo alla prima ondata di deflussi;
7. risposta del piano ottimo alla seconda ondata di deflussi;
8. risposta del piano ottimo alla variazione della capacità di funding;
9. grado di utilizzo della capacità di funding;
10. eventuali cambiamenti di regime nella soluzione;
11. confronto tra gli scenari Standard, Mediamente critico e Critico.

### Limiti del modello

Il modello:

1. è deterministico;
2. non attribuisce probabilità agli scenari;
3. assume coefficienti e cash flow noti;
4. rappresenta le due ondate di pressione sulla raccolta esclusivamente attraverso i fabbisogni delle date 1 e 4;
5. rappresenta la rigidità delle attività legacy mediante un singolo vincolo lineare;
6. non descrive processi dinamici di ristrutturazione del portafoglio durante l'orizzonte;
7. non rappresenta costi fissi, non linearità o altre frizioni non previste dalla specifica;
8. utilizza una calibrazione didattica e stilizzata;
9. non costituisce una ricostruzione storica del bilancio di First Republic Bank;
10. consente di interpretare i risultati soltanto nell'ambito delle ipotesi, dei parametri e dei vincoli esplicitamente assegnati.

## 5. Output richiesti

Gli output devono avere una funzione informativa, diagnostica o interpretativa esplicita e devono essere collegati alle quantità teoriche definite nella specifica del caso.

Devono essere costruiti esclusivamente a partire da configurazioni per le quali il solver restituisce una soluzione valida.

### Stime o risultati numerici

Devono essere prodotti almeno i seguenti risultati:

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

13. comportamento del vincolo legacy:

$$
x_3+x_4\geq35;
$$

14. confronto degli effetti prodotti da uno shock alla prima data e da uno shock alla data terminale;

15. soluzioni ottime nei tre scenari congiunti;

16. perdita di valore degli scenari Mediamente critico e Critico rispetto allo scenario Standard:

$$
L_s
=
\Pi_{\mathrm{Standard}}^*
-
\Pi_s^*.
$$

### Tabelle

Devono essere prodotte le seguenti tabelle.

1. **Tabella 1 — Benchmark e diagnostica**

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

   La funzione della tabella è fornire una sintesi verificabile della soluzione benchmark e della relativa diagnostica.

2. **Tabella 2 — Sensitività ad $\alpha$**

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

   La funzione della tabella è rendere osservabile l'effetto di una variazione del fabbisogno della prima data.

3. **Tabella 3 — Sensitività a $\beta$**

   Deve utilizzare una struttura analoga alla Tabella 2, sostituendo $\alpha$ con $\beta$.

   La funzione della tabella è rendere osservabile l'effetto di una variazione del fabbisogno alla data terminale.

4. **Tabella 4 — Sensitività a $\phi$**

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

   La funzione della tabella è mostrare come cambia il piano ottimo quando varia la capacità disponibile di funding.

5. **Tabella 5 — Confronto degli scenari**

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

   La funzione della tabella è confrontare configurazioni nelle quali le due ondate di fabbisogno e la capacità di funding cambiano congiuntamente.

6. **Tabella 6 — Controllo del vincolo legacy**

   Deve riportare, almeno per il benchmark e per le configurazioni nelle quali il vincolo risulta economicamente informativo:

   - valore di:

$$
x_3^*+x_4^*;
$$

   - distanza dal limite minimo:

$$
35;
$$

   - stato attivo / non attivo;
   - marginale restituito dal solver per la disuguaglianza codificata;
   - verifica perturbativa del significato economico del marginale, quando il vincolo è attivo.

   La tabella deve mantenere distinta la forma economica:

$$
x_3+x_4\geq L,
\qquad
L=35,
$$

   dalla forma codificata:

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

   Le due inversioni di segno, dovute rispettivamente a:

$$
F=-\Pi
$$

   e:

$$
b=-L,
$$

   si compensano.

   La funzione della tabella è impedire interpretazioni errate del marginale dovute alla forma algebrica utilizzata dal solver.

### Grafici

Devono essere prodotti i seguenti grafici.

1. **Figura 1 — Valore ottimo al variare di $\alpha$**

   Rappresentare:

$$
\alpha
\longmapsto
\Pi^*(\alpha).
$$

   Devono essere riportate esclusivamente configurazioni ammissibili.

   La funzione del grafico è rendere visibile il costo economico di una maggiore pressione di liquidità alla prima data.

2. **Figura 2 — Valore ottimo al variare di $\beta$**

   Rappresentare:

$$
\beta
\longmapsto
\Pi^*(\beta).
$$

   Devono essere riportate esclusivamente configurazioni ammissibili.

   La funzione del grafico è rendere visibile il costo economico di una maggiore pressione di liquidità alla data terminale.

3. **Figura 3 — Valore ottimo e capacità di funding**

   Rappresentare:

$$
\phi
\longmapsto
\Pi^*(\phi)
$$

   insieme, quando informativo, al comportamento dell'utilizzo relativo della capacità di funding.

   La funzione del grafico è rendere osservabile il valore economico della capacità di funding disponibile.

4. **Figura 4 — Composizione ottima dell'attivo**

   Per almeno una delle sensitività economicamente più informative devono essere rappresentate le componenti:

$$
x_1^*(p),\ldots,x_5^*(p).
$$

   La funzione del grafico è mostrare come la variazione del parametro provochi una ricomposizione del portafoglio.

5. **Figura 5 — Utilizzo della capacità di funding**

   Lungo la sensitività rispetto a $\phi$ devono essere rappresentati i rapporti:

$$
\rho_t^u(\phi)
=
\frac{u_t^*(\phi)}
{\phi\bar u_t},
\qquad
t=1,2,3.
$$

   La funzione del grafico è identificare le date nelle quali la capacità disponibile di funding diventa maggiormente vincolante.

6. **Figura 6 — Confronto tra prima e seconda ondata**

   Deve confrontare direttamente gli effetti delle variazioni di $\alpha$ e $\beta$.

   Il confronto deve riguardare almeno:

$$
\Pi^*,
$$

   e, quando informativo, una o più componenti di:

$$
x^*,
\qquad
g^*,
\qquad
u^*.
$$

   La funzione del grafico è rendere osservabile che uno stesso aumento relativo del fabbisogno può produrre effetti diversi a seconda della data nella quale si manifesta.

I grafici devono essere prodotti come output delle rispettive celle del notebook e devono essere rigenerabili mediante riesecuzione delle celle.

Non è richiesta automaticamente l'esportazione in file esterni.

### Controlli

Devono essere previsti ed eseguiti almeno i seguenti controlli.

#### Controlli numerici

1. verifica dei residuali dei vincoli di uguaglianza;

2. verifica degli slack delle disuguaglianze;

3. verifica dei bounds attivi;

4. controllo del vincolo prudenziale:

$$
\ell'x^*\leq7.5;
$$

5. controllo del vincolo legacy:

$$
x_3^*+x_4^*\geq35;
$$

6. controllo del limite:

$$
x_5^*\leq35;
$$

7. controllo dei limiti di funding:

$$
0\leq u_t^*\leq\phi\bar u_t;
$$

8. controllo della non negatività di tutte le variabili;

9. verifica dello stato di fattibilità per ciascuna configurazione parametrica e per ciascuno scenario.

#### Controlli logici e teorici

1. verifica che $\alpha$ modifichi esclusivamente il fabbisogno della prima data;

2. verifica che $\beta$ modifichi esclusivamente il fabbisogno della quarta data;

3. verifica che $\phi$ modifichi esclusivamente la capacità massima di funding;

4. verifica che nelle sensitività univariate vari un solo parametro alla volta;

5. verifica che negli scenari congiunti i tre parametri assumano simultaneamente i valori assegnati;

6. verifica della coerenza tra slack e stato attivo / non attivo dei vincoli;

7. verifica della coerenza tra variazioni dei parametri, cambiamenti dei vincoli attivi e modifiche della soluzione ottima;

8. verifica della corretta interpretazione economica dei principali valori marginali;

9. confronto esplicito tra gli effetti di uno shock alla prima data e quelli di uno shock alla data terminale.

#### Controlli computazionali

1. verifica della corretta costruzione di $A_{\mathrm{eq}}$, $b_{\mathrm{eq}}$, $A_{\mathrm{ub}}$, $b_{\mathrm{ub}}$ e dei bounds;

2. verifica della corretta trasformazione della funzione obiettivo nella convenzione utilizzata da `scipy.optimize.linprog`;

3. verifica della corretta codifica del vincolo:

$$
x_3+x_4\geq35
$$

come:

$$
-x_3-x_4\leq-35;
$$

4. verifica esplicita della riga del vincolo legacy in $A_{\mathrm{ub}}$ e del relativo termine noto;

5. interpretazione del marginale del vincolo legacy tenendo conto congiuntamente di:

$$
F=-\Pi
$$

e:

$$
b=-L;
$$

6. verifica numerica mediante piccola perturbazione di $L$ della relazione:

$$
\frac{\partial\Pi^*}{\partial L}
=
m,
$$

quando il marginale è localmente informativo;

7. verifica della corretta costruzione di:

$$
d(\alpha,\beta)
=
(32\alpha,18,14,32\beta)';
$$

8. verifica del corretto aggiornamento dei bounds del funding quando varia $\phi$;

9. esclusione dall'analisi economica delle configurazioni per le quali il solver segnala non ammissibilità;

10. verifica che tabelle e grafici siano generati esclusivamente a partire da risultati di esecuzioni valide;

11. verifica della riproducibilità degli output mediante riesecuzione ordinata del notebook.

### Funzione interpretativa degli output

Gli output devono consentire allo studente di discutere, sulla base di risultati numerici già validati:

1. come la presenza di attività legacy riduca la flessibilità di ristrutturazione del bilancio;

2. perché uno shock alla prima data possa produrre effetti diversi da uno shock alla data terminale;

3. quando la capacità di funding diventi una risorsa scarsa;

4. quali vincoli determinino il piano ottimo nelle diverse configurazioni;

5. come cambino composizione dell'attivo, giacenze, funding e valore ottimo;

6. quale ruolo economico svolga il vincolo legacy;

7. come differiscano gli scenari Standard, Mediamente critico e Critico;

8. quali conclusioni dipendano dalla struttura del modello stilizzato e non possano essere trasferite direttamente al caso storico di First Republic Bank.

L'interpretazione finanziaria finale resta responsabilità dello studente e deve basarsi esclusivamente su output già validati.

## 6. Flusso logico-teorico risolutivo atteso

Il Flusso logico-teorico deve ricostruire, in forma sintetica, la sequenza concettuale necessaria per trasferire il metodo appreso nel Caso Aula a una struttura ALM differente.

Il Flusso non deve replicare la granularità delle celle del notebook. Deve individuare pochi snodi teorico-operativi, ciascuno dei quali può articolarsi successivamente in più operazioni computazionali.

Il percorso deve partire dalla nuova specifica del problema:

$$
\text{nuovo problema}
\longrightarrow
\text{nuova forma solver}
\longrightarrow
\text{benchmark}
\longrightarrow
\text{analisi parametrica}
\longrightarrow
\text{scenari}
\longrightarrow
\text{interpretazione}.
$$

| Passo | Finalità risolutiva | Formula teorico-matematica / definizione / proprietà | Applicazione nel caso | Output o controllo collegato |
|---:|---|---|---|---|
| 1 | Ricostruire autonomamente il nuovo problema e tradurlo nella forma solver | Programmazione lineare ALM; distinzione tra variabili, uguaglianze, disuguaglianze e bounds; equivalenza tra $\max\Pi$ e $\min F=-\Pi$ | Identificare cinque classi di attivo, quattro giacenze, tre variabili di funding, doppia ondata, vincolo legacy e limite su $x_5$; costruire vettore decisionale, obiettivo, matrici e bounds | Mappa teorica del caso; struttura solver completa; controlli dimensionali, dei segni e dell'ordinamento |
| 2 | Risolvere e validare il benchmark, con attenzione al vincolo legacy e al relativo marginale | Ammissibilità; ottimalità; residuali; slack; vincoli e bounds attivi; dualità e sensitività locale; vincolo inferiore trasformato in forma $\leq$ | Risolvere $(\alpha,\beta,\phi)=(1,1,1)$; verificare tutti i vincoli; distinguere $x_3+x_4\geq L$ da $-x_3-x_4\leq-L$; verificare localmente $\partial\Pi^*/\partial L=m$ | $x^*$, $g^*$, $u^*$, $\Pi^*$; diagnostica benchmark; Tabella 1 e Tabella 6; verifica perturbativa del marginale legacy |
| 3 | Costruire il solver parametrico senza alterare la struttura del modello | Analisi parametrica di termini noti e bounds | Introdurre $\alpha$, $\beta$ e $\phi$ esclusivamente negli elementi previsti dalla Scheda Caso e verificare la riproduzione del benchmark | Funzione solver parametrica; controllo in $(1,1,1)$ |
| 4 | Analizzare separatamente le due ondate e confrontarne il timing | Comparative statics; struttura temporale dei bilanci ALM | Variare prima $\alpha$ con $\beta=\phi=1$, poi $\beta$ con $\alpha=\phi=1$; confrontare variazioni relative omogenee senza modificare simultaneamente i due parametri | Sensitività ad $\alpha$ e $\beta$; Tabelle 2–3; Figure 1–2, 4 e 6; confronto diretto prima/seconda ondata |
| 5 | Analizzare il ruolo della capacità disponibile di funding | Bounds parametrizzati; scarsità di una risorsa esterna | Variare $\phi$ mantenendo $\alpha=\beta=1$ e modificando esclusivamente i bounds del funding | Sensitività a $\phi$; Tabella 4; Figure 3 e 5; utilizzo della capacità; vincoli e bounds attivi |
| 6 | Confrontare i tre driver e il ruolo dei vincoli strutturali | Comparative statics; cambiamenti di regime; vincoli attivi; valori marginali locali | Mettere in relazione $\alpha$, $\beta$ e $\phi$ con variazioni di soluzione, vincolo legacy, limite su $x_5$ e bounds del funding | Sintesi comparativa delle sensitività; lettura del timing, della rigidità legacy e della capacità di funding |
| 7 | Analizzare configurazioni con variazione congiunta dei driver | Scenario analysis deterministica | Risolvere Standard, Mediamente critico e Critico con i valori assegnati di $(\alpha,\beta,\phi)$ | Tabella 5; confronto tra scenari; perdita rispetto allo Standard; variazioni di $x^*$, $g^*$, $u^*$ e vincoli attivi |
| 8 | Verificare la coerenza complessiva e delimitare l'interpretazione | Coerenza modello--solver--output; validità locale dei marginali; limiti del modello deterministico | Controllare completezza, riproducibilità, autonomia rispetto all'Aula e uso esclusivo di risultati validi | Controlli conclusivi; elementi quantitativi per l'interpretazione finale; richiamo dei limiti del modello |

### 6.1 Passaggio teorico specifico sul vincolo legacy

Il vincolo:

$$
x_3+x_4\geq L
$$

deve essere trattato esplicitamente nella validazione del benchmark.

Per la forma solver si utilizza:

$$
-x_3-x_4\leq -L.
$$

Ponendo:

$$
b=-L
$$

e indicando con:

$$
F=-\Pi
$$

la funzione minimizzata dal solver, se:

$$
m
=
\frac{\partial F^*}{\partial b},
$$

allora:

$$
\frac{\partial F^*}{\partial L}
=
\frac{\partial F^*}{\partial b}
\frac{\partial b}{\partial L}
=
-m.
$$

Poiché:

$$
F^*=-\Pi^*,
$$

segue:

$$
-\frac{\partial\Pi^*}{\partial L}
=
-m,
$$

e quindi:

$$
\boxed{
\frac{\partial\Pi^*}{\partial L}
=
m
}.
$$

Le due inversioni di segno si compensano.

Il risultato deve essere validato mediante una piccola perturbazione di $L$ quando il vincolo è attivo e la soluzione resta nello stesso regime locale.

### 6.2 Passaggio teorico specifico sul confronto $\alpha$–$\beta$

Le due sensitività devono essere sviluppate separatamente prima del confronto.

Per $\alpha$:

$$
d(\alpha,1)
=
(32\alpha,18,14,32)'.
$$

Per $\beta$:

$$
d(1,\beta)
=
(32,18,14,32\beta)'.
$$

Il confronto deve utilizzare variazioni relative omogenee e deve verificare se:

$$
\alpha-1
=
\beta-1
$$

produca o meno gli stessi effetti su:

$$
\Pi^*,
\qquad
x^*,
\qquad
g^*,
\qquad
u^*.
$$

L'eventuale differenza deve essere interpretata attraverso la struttura temporale dei bilanci ALM.

Il principio da rendere osservabile è:

$$
\text{stesso aumento relativo del fabbisogno}
\not\Rightarrow
\text{stesso effetto sul piano ALM}.
$$

### 6.3 Logica della sequenza

Il flusso deve rispettare l'ordine:

$$
\text{ricognizione e forma solver}
\longrightarrow
\text{benchmark e legacy}
\longrightarrow
\text{solver parametrico}
$$

$$
\longrightarrow
\alpha
\longrightarrow
\beta
\longrightarrow
\text{confronto }\alpha\text{--}\beta
\longrightarrow
\phi
$$

$$
\longrightarrow
\text{confronto dei driver}
\longrightarrow
\text{scenari}
\longrightarrow
\text{controlli conclusivi}.
$$

La verifica del vincolo legacy deve precedere l'analisi parametrica, perché la sua corretta codifica e interpretazione costituiscono parte della validazione del modello.

Le sensitività ad $\alpha$ e a $\beta$ devono essere costruite separatamente prima del loro confronto.

### 6.4 Relazione con la scomposizione in tappe

La successiva scomposizione operativa deriva da questo Flusso logico-teorico.

In particolare:

- il Passo 1 alimenta la **Tappa 1 — Ricognizione del nuovo problema e forma solver**;
- i Passi 2–3 alimentano la **Tappa 2 — Benchmark, vincolo legacy e solver parametrico**;
- il Passo 4 alimenta la **Tappa 3 — Sensitività ad $\alpha$, a $\beta$ e confronto tra le due ondate**;
- i Passi 5–6 alimentano la **Tappa 4 — Sensitività a $\phi$ e confronto complessivo dei driver**;
- il Passo 7 alimenta la **Tappa 5 — Scenario analysis**;
- il Passo 8 alimenta la **Tappa 6 — Controlli conclusivi e predisposizione dell'interpretazione**.

Il Flusso definisce l'ordine concettuale della soluzione. Le tappe raggruppano blocchi operativi coerenti e non devono coincidere con singole celle o singole operazioni.

## 7. Scomposizione attesa in tappe

La scomposizione operativa deve derivare dal Flusso logico-teorico risolutivo e deve rendere visibile, per ciascuna tappa, il collegamento tra input, oggetti teorici, operazione computazionale, output, controllo e utilizzo successivo.

Le tappe devono costituire **blocchi operativi ampi** e non coincidere con singole operazioni, tabelle, grafici o celle del notebook.

Il Regime IA indicato nella tabella rappresenta il regime prevalente della tappa ordinaria.

Il Regime C non costituisce una tappa programmata del percorso. Può essere attivato soltanto quando lo studente individua una criticità specifica nel materiale prodotto e formula una richiesta mirata di verifica.

| Tappa | Titolo | Obiettivo | Input | Regime IA prevalente | Prompt virtuoso di riferimento | Oggetti teorici coinvolti | Operazione | Output | Controllo | Uso successivo |
|---:|---|---|---|:---:|---|---|---|---|---|---|
| 1 | Ricognizione del nuovo problema e forma solver | Riconoscere gli elementi strutturali distintivi del TakeHome e tradurre la nuova specifica in una struttura compatibile con `linprog` | Scheda Caso TakeHome; metodo appreso nel Caso Aula; parametri e formule assegnati | A/B | Ricostruire cinque attivi, doppia ondata, legacy, limite $x_5$, ordinamento delle variabili, obiettivo, uguaglianze, disuguaglianze e bounds | ALM multiperiodale; programmazione lineare; bilanci temporali; vincoli; bounds; trasformazione massimo/minimo | Identificare gli elementi nuovi e costruire vettore decisionale, vettore obiettivo, $A_{\mathrm{eq}}$, $b_{\mathrm{eq}}$, $A_{\mathrm{ub}}$, $b_{\mathrm{ub}}$ e bounds | Mappa teorico-operativa e struttura solver completa | Autonomia rispetto all'Aula; dimensioni; segni; ordine delle variabili; coerenza formula-coefficienti | Benchmark |
| 2 | Benchmark, vincolo legacy e solver parametrico | Risolvere e validare il benchmark, verificare il marginale legacy e generalizzare il modello ai tre driver | Struttura solver della Tappa 1; $(\alpha,\beta,\phi)=(1,1,1)$ | A/B | Risolvere il benchmark, costruire la diagnostica, verificare il vincolo legacy e il suo marginale e costruire la funzione parametrica | Ammissibilità; residuali; slack; bounds attivi; dualità; vincolo inferiore; sensitività locale; analisi parametrica | Eseguire `linprog`; ricostruire $\Pi^*$; verificare $x_3+x_4\geq L$ e la forma $-x_3-x_4\leq-L$; perturbare $L$; implementare `solve(\alpha,\beta,\phi)` | Tabella 1; Tabella 6; diagnostica benchmark; verifica perturbativa; funzione solver parametrica | Stato solver; vincoli; marginale legacy con $\partial\Pi^*/\partial L=m$; riproduzione benchmark; corretta azione separata dei parametri | Sensitività |
| 3 | Sensitività ad $\alpha$, a $\beta$ e confronto tra le due ondate | Analizzare separatamente prima e seconda ondata e confrontarne gli effetti temporali | Funzione parametrica; griglie di $\alpha$ e $\beta$ | A/B | Risolvere separatamente le due griglie e confrontare variazioni relative omogenee senza modificare simultaneamente i due parametri | Comparative statics; timing della liquidità; vincoli attivi | Eseguire griglia $\alpha$ con $\beta=\phi=1$; eseguire griglia $\beta$ con $\alpha=\phi=1$; costruire confronto diretto | Tabelle 2–3; Figure 1–2, 4 e 6; confronto di $\Pi^*$, $x^*$, $g^*$, $u^*$ e vincoli attivi | Unico parametro variato; stato solver; coerenza tra differenze osservate e timing dei fabbisogni | Capacità di funding e confronto globale |
| 4 | Sensitività a $\phi$ e confronto complessivo dei driver | Analizzare la capacità disponibile di funding e mettere in relazione i tre driver | Funzione parametrica; griglia di $\phi$; risultati della Tappa 3 | A/B | Risolvere la griglia di $\phi$ e confrontare $\alpha$, $\beta$, $\phi$ rispetto a valore, soluzione e vincoli strutturali | Bounds parametrizzati; scarsità della capacità; comparative statics; cambiamenti di regime | Variare $\phi$ con $\alpha=\beta=1$; costruire rapporti di utilizzo; collegare i risultati alle due ondate e al ruolo di legacy, $x_5$ e bounds del funding | Tabella 4; Figure 3 e 5; sintesi comparativa dei driver | $\phi$ modifica solo i bounds; capacità distinta da funding effettivamente utilizzato; coerenza tra soluzione e vincoli attivi | Scenario analysis |
| 5 | Scenario analysis | Analizzare configurazioni nelle quali le due ondate e la capacità di funding variano congiuntamente | Funzione parametrica; tre scenari assegnati | B | Risolvere Standard, Mediamente critico e Critico e confrontarne le soluzioni | Scenario analysis deterministica | Risolvere le tre configurazioni; calcolare perdita rispetto allo Standard; confrontare $x^*$, $g^*$, $u^*$ e vincoli attivi | Tabella 5; output di scenario | Parametri esatti; Standard uguale al benchmark; stato solver; uso esclusivo di risultati validi | Controllo conclusivo |
| 6 | Controlli conclusivi e predisposizione dell'interpretazione | Verificare coerenza complessiva e predisporre la lettura finale del caso | Tutti gli output precedenti | A | Riesaminare formule, codice, output, vincoli e limiti interpretativi | Coerenza globale; limiti del modello; trasferimento metodologico | Eseguire la checklist finale, verificare completezza e riproducibilità e delimitare il significato dei risultati | Sintesi quantitativa validata e base per il commento finale | Coerenza Scheda Caso--notebook; riproducibilità; autonomia rispetto all'Aula; limiti del modello | Chiusura del notebook |

### Verifica specifica del vincolo legacy

La Tappa 2 deve rendere esplicita la catena:

$$
x_3+x_4\geq L,
\qquad
L=35.
$$

La forma compatibile con `linprog` è:

$$
-x_3-x_4\leq -L.
$$

Ponendo:

$$
b=-L
$$

e indicando con:

$$
F=-\Pi
$$

la funzione minimizzata dal solver, se:

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

Le due inversioni di segno dovute a $F=-\Pi$ e $b=-L$ si compensano.

La verifica deve essere effettuata mediante una piccola perturbazione di $L$ quando il vincolo è attivo e il marginale è localmente informativo.

### Eventuale attivazione del Regime C

Il Regime C non deve essere incorporato preventivamente nella sequenza delle tappe.

Può essere utilizzato, dopo una qualsiasi tappa, soltanto se lo studente individua una criticità specifica, ad esempio:

- incoerenza tra forma economica e forma codificata del vincolo legacy;
- marginale apparentemente incompatibile con una perturbazione di $L$;
- residuale inatteso;
- configurazione dichiarata ammissibile o non ammissibile in modo sorprendente;
- incoerenza fra formula, codice e output;
- incoerenza fra tabella, grafico e risultato numerico.

Il prompt in Regime C deve indicare:

1. tappa interessata;
2. criticità specifica osservata;
3. elementi quantitativi che motivano il dubbio.

L'esito deve essere classificato come **criticità respinta** oppure **criticità accolta**.

Un eventuale intervento in Regime C non modifica la numerazione ordinaria delle tappe.

## 8. Sequenza docente dei prompt e mappa prompt-notebook

### 8.1 Sequenza docente dei prompt virtuosi

La sequenza ordinaria dei prompt è:

1. Prompt zero;
2. Prompt 1;
3. Prompt 2;
4. Prompt 3;
5. prompt di tappa derivati dalla scomposizione operativa validata.

Il Regime C non costituisce una fase obbligatoria né una tappa programmata del lavoro.

Può essere attivato soltanto quando lo studente individua una criticità specifica in una parte del notebook, in un output, in un controllo o nell'interpretazione di un risultato e formula una richiesta mirata di verifica.

La sequenza ordinaria è quindi:

$$
\text{Prompt zero}
\longrightarrow
\text{Prompt 1}
\longrightarrow
\text{Prompt 2}
\longrightarrow
\text{Prompt 3}
\longrightarrow
\text{prompt di tappa}.
$$

L'eventuale intervento in Regime C si inserisce soltanto nel punto in cui emerge una criticità specifica e non modifica la struttura ordinaria del percorso.

### 8.2 Funzione dei prompt iniziali

**Prompt zero**

Funzione:
- inizializzare il contesto;
- acquisire le regole generali;
- fissare il significato dei Regimi A, B e C;
- richiamare i vincoli sul ruolo dell'IA.

Non produce direttamente una cella del notebook.

**Prompt 1**

Funzione:
- acquisire integralmente la Scheda Caso come specifica vincolante;
- produrre esclusivamente la cella Markdown iniziale di inquadramento.

La cella deve:
- sintetizzare titolo, contesto e domanda quantitativa;
- riportare le quantità da stimare o calcolare;
- riportare gli output richiesti;
- riportare i controlli richiesti;
- dichiarare che la Scheda Caso non può essere modificata.

Non deve contenere:
- codice;
- soluzione;
- Flusso logico-teorico risolutivo;
- tappe operative;
- risultati numerici;
- interpretazioni conclusive.

**Prompt 2 — Regime A**

Funzione:
- costruire il Flusso logico-teorico risolutivo.

Lo studente deve proporre una prima sequenza teorico-logica che evidenzi in particolare:

1. struttura ALM multiperiodale;
2. doppia ondata di fabbisogno;
3. ruolo della capacità di funding;
4. vincolo legacy;
5. differenze rispetto al Caso Aula.

L'IA può:
- verificare;
- completare;
- correggere;
- ordinare.

L'output deve essere una sola cella Markdown contenente il Flusso logico-teorico risolutivo in un numero contenuto di passi e comunque non superiore a otto.

**Prompt 3 — Regime A/B**

Funzione:
- trasformare il Flusso logico-teorico validato nella scomposizione operativa in tappe.

Lo studente deve proporre una prima articolazione delle tappe.

L'IA può:
- verificarla;
- completarla;
- ordinarla;
- associare a ciascuna tappa il regime IA prevalente.

Il Prompt 3 deve verificare che la scomposizione non riduca il TakeHome a una replica del Caso Aula con coefficienti diversi.

La scomposizione deve utilizzare blocchi operativi ampi e comunque non più di sei tappe.

Non deve ancora sviluppare integralmente il codice delle singole tappe.

L'output deve essere una sola cella Markdown contenente la scomposizione operativa validata.

### 8.3 Prompt di tappa

I prompt di tappa devono essere costruiti a partire dalla Sezione 7 e devono indicare almeno:

1. numero e titolo della tappa;
2. obiettivo;
3. input disponibili;
4. oggetti teorici coinvolti;
5. operazione richiesta;
6. output atteso;
7. controllo da svolgere;
8. uso dell'output nella tappa successiva;
9. regime IA prevalente.

Il Regime A deve essere utilizzato quando la funzione principale della tappa è teorico-modellistica o interpretativa.

Il Regime B deve essere utilizzato quando una struttura già definita deve essere tradotta in codice o in una procedura computazionale.

Una stessa tappa può richiedere più interazioni e più celle Markdown o Python. L'accorpamento delle operazioni in una stessa tappa non implica che esse debbano essere svolte in un'unica risposta IA o in un'unica cella.

### 8.4 Mappa prompt-notebook

| Prompt | Regime | Tappa o fase | Funzione del prompt | Celle o output prodotti | Decisione o controllo richiesto |
|---:|:---:|---|---|---|---|
| Prompt zero | — | Inizializzazione | Acquisire regole generali, struttura del lavoro e disciplina dei Regimi IA | Nessuna cella obbligatoria | Verifica dell'acquisizione delle regole |
| Prompt 1 | — | Inquadramento | Acquisire la Scheda Caso e produrre la cella Markdown iniziale | Cella Markdown iniziale | Fedeltà integrale alla Scheda Caso; assenza di soluzione o suggerimenti risolutivi |
| Prompt 2 | A | Flusso teorico | Costruire il Flusso logico-teorico risolutivo a partire dal contributo iniziale dello studente | Cella Markdown con il Flusso in massimo 8 passi | Completezza teorica; corretta individuazione delle differenze rispetto al Caso Aula |
| Prompt 3 | A/B | Scomposizione operativa | Tradurre il Flusso validato nella sequenza di tappe input-output | Cella Markdown con massimo 6 tappe | Coerenza con il Flusso; copertura di output e controlli; autonomia rispetto al Caso Aula |
| Prompt di tappa 1 | A/B | Tappa 1 — Ricognizione e forma solver | Identificare gli elementi distintivi del TakeHome e costruire la struttura matriciale | Celle Markdown e codice per ricognizione, parametri, matrici e bounds | Cinque attivi; doppia ondata; legacy; limite $x_5$; dimensioni; segni; formula-coefficienti |
| Prompt di tappa 2 | A/B | Tappa 2 — Benchmark, legacy e solver parametrico | Risolvere il benchmark, validare il vincolo legacy e costruire la funzione parametrica | Celle codice, diagnostica, verifica perturbativa e funzione `solve` | Stato solver; vincoli; $\partial\Pi^*/\partial L=m$; riproduzione benchmark |
| Prompt di tappa 3 | A/B | Tappa 3 — $\alpha$, $\beta$ e confronto delle ondate | Eseguire separatamente le due griglie e confrontarne gli effetti | DataFrame, figure e Markdown di confronto | Unico parametro variato; timing dei fabbisogni; nessuna variazione simultanea di $\alpha$ e $\beta$ |
| Prompt di tappa 4 | A/B | Tappa 4 — $\phi$ e confronto dei driver | Analizzare la capacità di funding e mettere in relazione i tre driver | DataFrame, figure e sintesi quantitativa | $\phi$ solo sui bounds; capacità distinta da utilizzo; ruolo di legacy, $x_5$ e bounds |
| Prompt di tappa 5 | B | Tappa 5 — Scenario analysis | Risolvere Standard, Mediamente critico e Critico | Tabella comparativa e output di scenario | Parametri esatti; Standard = benchmark; stato solver; uso esclusivo di risultati validi |
| Prompt di tappa 6 | A | Tappa 6 — Controlli conclusivi | Verificare completezza, coerenza e limiti del notebook | Celle di controllo e Markdown conclusivo | Coerenza Scheda Caso--notebook; riproducibilità; autonomia rispetto all'Aula; limiti interpretativi |

### 8.5 Controllo specifico nel prompt sul vincolo legacy

Il prompt relativo alla Tappa 2 deve rendere esplicita la distinzione tra:

$$
x_3+x_4\geq L,
\qquad
L=35,
$$

e la forma solver:

$$
-x_3-x_4\leq -L.
$$

Ponendo:

$$
F=-\Pi,
\qquad
b=-L,
$$

e indicando con:

$$
m
=
\frac{\partial F^*}{\partial b}
$$

il marginale restituito dal solver per la riga codificata, il prompt deve richiedere di verificare che:

$$
\frac{\partial\Pi^*}{\partial L}
=
m.
$$

Non deve essere richiesto genericamente di «cambiare il segno» del marginale.

### 8.6 Eventuale Prompt in Regime C

Un Prompt C può essere attivato soltanto se lo studente identifica una criticità specifica.

Non deve essere previsto automaticamente un «Prompt C finale» né deve essere richiesto un numero minimo di interventi in Regime C.

Nel Caso TakeHome possono costituire esempi di criticità specifica:

- possibile errore nella riga del vincolo legacy;
- marginale legacy apparentemente incoerente con una perturbazione di $L$;
- errore nell'individuazione della data modificata da $\alpha$ o $\beta$;
- incoerenza fra capacità di funding e funding effettivamente utilizzato;
- configurazione inaspettatamente non ammissibile;
- incoerenza fra tabella, grafico e risultato numerico.

Il Prompt C deve indicare:

1. tappa interessata;
2. cella, output o controllo interessato;
3. criticità osservata;
4. ragionamento che motiva il dubbio.

L'IA deve verificare esclusivamente la criticità indicata e classificare l'esito come:

- **criticità respinta**;
- **criticità accolta**.

Se la criticità è respinta, non devono essere proposte modifiche al notebook.

Se la criticità è accolta, devono essere proposte soltanto le correzioni necessarie alla parte interessata.

### 8.7 Regole di coerenza della sequenza

La sequenza dei prompt deve rispettare le seguenti condizioni:

1. il Prompt 2 precede sempre il Prompt 3;
2. il Prompt 3 precede i prompt operativi di tappa;
3. il Flusso logico-teorico deve contenere non più di otto passi;
4. la scomposizione operativa deve contenere non più di sei tappe;
5. le tappe devono derivare dal Flusso logico-teorico validato;
6. nessun prompt può modificare variabili, parametri, formule, griglie, scenari, output o controlli fissati dalla Scheda Caso;
7. ogni prompt di tappa deve essere riconducibile a una tappa della Sezione 7;
8. tutti gli output e tutti i controlli della Scheda Caso devono risultare coperti dalla sequenza complessiva;
9. il TakeHome non deve essere costruito mediante mera duplicazione del notebook Aula;
10. il vincolo legacy deve essere trattato esplicitamente e non assorbito implicitamente nella matrice;
11. $\alpha$ e $\beta$ devono essere analizzati separatamente prima del loro confronto;
12. ogni output computazionale deve essere validato prima di essere utilizzato nelle operazioni successive;
13. l'IA non deve produrre in un unico passaggio l'intero notebook;
14. l'interpretazione finanziaria finale resta responsabilità dello studente;
15. il Regime C resta eventuale e subordinato all'individuazione autonoma di una criticità specifica.

## 9. Struttura attesa del notebook

Il notebook deve riflettere la sequenza logico-operativa validata nelle Sezioni 6 e 7 e deve rendere evidente che il Caso TakeHome richiede un trasferimento autonomo del metodo sviluppato nel Caso Aula.

La struttura deve rendere riconoscibile il percorso:

$$
\text{inquadramento}
\longrightarrow
\text{Flusso logico-teorico}
\longrightarrow
\text{tappe operative}
\longrightarrow
\text{ricognizione e forma solver}
$$

$$
\longrightarrow
\text{benchmark e legacy}
\longrightarrow
\text{solver parametrico}
\longrightarrow
\alpha
\longrightarrow
\beta
\longrightarrow
\text{confronto }\alpha\text{--}\beta
$$

$$
\longrightarrow
\phi
\longrightarrow
\text{confronto dei driver}
\longrightarrow
\text{scenari}
\longrightarrow
\text{controlli conclusivi}
\longrightarrow
\text{interpretazione finale}.
$$

La struttura del notebook non deve replicare meccanicamente il numero dei passi del Flusso o delle operazioni elementari. Ciascuna delle sei tappe può articolarsi in più celle Markdown, codice e output.

### 9.1 Sequenza delle celle e degli output

La sequenza attesa è la seguente.

1. **Cella Markdown iniziale — Prompt 1**
   - titolo;
   - contesto;
   - domanda quantitativa;
   - quantità da calcolare;
   - output richiesti;
   - controlli richiesti;
   - richiamo alla natura vincolante della Scheda Caso.

2. **Cella Markdown — Prompt 2**
   - Flusso logico-teorico risolutivo validato in massimo otto passi.

3. **Cella Markdown — Prompt 3**
   - scomposizione operativa validata in massimo sei tappe.

4. **Tappa 1 — Ricognizione del nuovo problema e forma solver**
   - cella Markdown di ricognizione con cinque classi di attivo, doppia ondata, ruolo distinto di $\alpha$ e $\beta$, capacità parametrizzata da $\phi$, vincolo legacy, limite su $x_5$ e differenze rispetto al Caso Aula;
   - celle codice per importazioni e parametri benchmark;
   - ordinamento dichiarato e invariato delle variabili;
   - celle codice per vettore obiettivo, $A_{\mathrm{eq}}$, $b_{\mathrm{eq}}$, $A_{\mathrm{ub}}$, $b_{\mathrm{ub}}$ e bounds;
   - controlli dimensionali, dei coefficienti e dei segni;
   - breve richiamo alla trasformazione $\max\Pi\leftrightarrow\min(-\Pi)$.

5. **Tappa 2 — Benchmark, vincolo legacy e solver parametrico**
   - cella Markdown introduttiva;
   - soluzione benchmark in $(1,1,1)$;
   - Tabella 1 — Benchmark e diagnostica;
   - cella Markdown dedicata alla forma economica e alla forma solver del vincolo legacy;
   - Tabella 6 — Controllo del vincolo legacy;
   - verifica perturbativa di $L$ e richiamo alla relazione $\partial\Pi^*/\partial L=m$;
   - breve Markdown di interpretazione locale;
   - definizione dei tre driver;
   - funzione $\operatorname{solve}(\alpha,\beta,\phi)$;
   - verifica della riproduzione del benchmark.

6. **Tappa 3 — Sensitività ad $\alpha$, a $\beta$ e confronto tra le due ondate**
   - cella Markdown che distingue i due shock;
   - esecuzione della griglia di $\alpha$;
   - Tabella 2 e Figura 1;
   - esecuzione della griglia di $\beta$;
   - Tabella 3 e Figura 2;
   - Figura 4 lungo almeno una sensitività informativa;
   - confronto diretto tra configurazioni omogenee di $\alpha$ e $\beta$;
   - Figura 6 e Markdown di interpretazione del timing.

7. **Tappa 4 — Sensitività a $\phi$ e confronto complessivo dei driver**
   - cella Markdown introduttiva;
   - esecuzione della griglia di $\phi$;
   - Tabella 4;
   - Figure 3 e 5;
   - controllo del rapporto tra capacità disponibile e funding effettivamente utilizzato;
   - Markdown di confronto complessivo tra $\alpha$, $\beta$ e $\phi$;
   - collegamento con vincolo legacy, limite su $x_5$ e bounds del funding.

8. **Tappa 5 — Scenario analysis**
   - cella Markdown con Standard, Mediamente critico e Critico;
   - risoluzione delle tre configurazioni;
   - Tabella 5 — Confronto degli scenari;
   - eventuali ulteriori output grafici se utili alla lettura, senza introdurre requisiti non presenti nella Scheda Caso.

9. **Tappa 6 — Controlli conclusivi e predisposizione dell'interpretazione**
   - cella Markdown e/o codice con checklist conclusiva;
   - verifica della formulazione solver;
   - verifica del benchmark;
   - verifica del vincolo e marginale legacy;
   - verifica della funzione parametrica;
   - verifica delle sensitività ad $\alpha$, $\beta$ e $\phi$;
   - verifica del confronto $\alpha$--$\beta$;
   - verifica degli scenari;
   - verifica dell'uso esclusivo di risultati validi;
   - verifica della riproducibilità;
   - cella Markdown con gli elementi quantitativi necessari all'interpretazione economico-finanziaria;
   - cella Markdown finale dello studente per il commento autonomo.

Gli output delle celle codice costituiscono parte integrante della sequenza e non richiedono una numerazione autonoma delle celle.

### 9.2 Corrispondenza con le tappe operative

La struttura deve mantenere riconoscibile la seguente corrispondenza:

- **Tappa 1 — Ricognizione del nuovo problema e forma solver:** riconoscimento della nuova struttura e costruzione della forma computazionale;

- **Tappa 2 — Benchmark, vincolo legacy e solver parametrico:** soluzione benchmark, diagnostica, verifica del marginale legacy e funzione parametrica;

- **Tappa 3 — Sensitività ad $\alpha$, a $\beta$ e confronto tra le due ondate:** sviluppo separato dei due shock e lettura del timing;

- **Tappa 4 — Sensitività a $\phi$ e confronto complessivo dei driver:** capacità di funding e sintesi delle comparative statics;

- **Tappa 5 — Scenario analysis:** variazione congiunta dei tre driver nelle configurazioni assegnate;

- **Tappa 6 — Controlli conclusivi e predisposizione dell'interpretazione:** validazione globale e base quantitativa per il commento finale.

La numerosità delle celle è indicativa e deve essere determinata dalla leggibilità del notebook e dalla necessità di mantenere visibile la sequenza:

$$
\text{operazione}
\longrightarrow
\text{output}
\longrightarrow
\text{controllo}
\longrightarrow
\text{uso successivo}.
$$

Una singola tappa può quindi contenere più coppie o blocchi di celle Markdown/Python.

### 9.3 Regole di costruzione del notebook

Il notebook deve rispettare le seguenti regole:

1. essere eseguibile sequenzialmente dall'inizio alla fine;

2. non dipendere da oggetti prodotti in esecuzioni precedenti non riproducibili;

3. non contenere celle errate duplicate o versioni alternative non utilizzate;

4. mantenere invariato l'ordinamento delle variabili dopo che è stato dichiarato;

5. generare tabelle e grafici direttamente dagli oggetti prodotti dal solver;

6. non inserire manualmente nelle celle successive valori numerici della soluzione;

7. verificare sempre lo stato del solver prima di utilizzare:

$$
x^*,
\qquad
g^*,
\qquad
u^*,
\qquad
\Pi^*;
$$

8. non utilizzare risultati provenienti da configurazioni non ammissibili;

9. mantenere invariato il costo del funding lungo tutte le sensitività e gli scenari;

10. applicare $\alpha$ esclusivamente al fabbisogno della prima data;

11. applicare $\beta$ esclusivamente al fabbisogno della quarta data;

12. applicare $\phi$ esclusivamente ai bounds del funding;

13. mantenere distinto il vincolo legacy dal limite su $x_5$;

14. trattare esplicitamente il vincolo legacy e il relativo marginale prima della costruzione delle sensitività;

15. non introdurre un cambio di segno aggiuntivo nella relazione:

$$
\frac{\partial\Pi^*}{\partial L}
=
m;
$$

16. sviluppare separatamente le sensitività ad $\alpha$ e a $\beta$ prima di confrontarle;

17. collocare il confronto $\alpha$–$\beta$ prima della sintesi complessiva dei driver;

18. distinguere chiaramente sensitività univariate e scenario analysis;

19. produrre tutti gli output richiesti dalla Scheda Caso;

20. eseguire i controlli previsti nel punto in cui diventano necessari e prima dell'interpretazione conclusiva;

21. mantenere coerenti notazione matematica e nomi delle variabili computazionali;

22. non prevedere automaticamente directory di output o esportazioni esterne;

23. utilizzare le celle Markdown per introdurre e collegare i blocchi operativi, evitando di trasformare ogni singola operazione in una tappa autonoma.

### 9.4 Funzione specifica della ricognizione iniziale

La ricognizione iniziale resta parte sostanziale del TakeHome, ma è incorporata nella Tappa 1.

Essa deve mostrare che lo studente ha riconosciuto autonomamente che il nuovo caso contiene:

1. una dimensione dell'attivo diversa;

2. un diverso vettore dei fabbisogni;

3. due driver temporali distinti:

$$
\alpha
\qquad\text{e}\qquad
\beta;
$$

4. un vincolo inferiore legacy;

5. un limite separato su:

$$
x_5;
$$

6. una struttura parametrica differente da quella del Caso Aula;

7. assenza di un parametro dedicato al costo del funding.

La ricognizione non deve consistere nella modifica meccanica del notebook Aula.

### 9.5 Funzione delle celle Markdown

Le celle Markdown devono rendere riconoscibili:

1. obiettivo della tappa;

2. input disponibili;

3. oggetti teorici coinvolti;

4. operazioni da svolgere all'interno della tappa;

5. output attesi;

6. controlli associati;

7. collegamento con la tappa successiva;

8. interpretazioni locali necessarie alla comprensione degli output.

Le celle Markdown non devono duplicare estensivamente il manuale o le slides.

Una tappa può contenere più celle Markdown quando servono a separare momenti logicamente distinti, ad esempio benchmark e vincolo legacy, oppure sensitività ad $\alpha$, sensitività a $\beta$ e relativo confronto.

### 9.6 Funzione delle celle di controllo

I controlli devono essere collocati nel momento in cui diventano necessari.

In particolare:

- controllo dimensionale dopo la costruzione della forma solver;

- residuali, slack e bounds dopo il benchmark;

- verifica dedicata del vincolo legacy e del relativo marginale prima della parametrizzazione;

- controllo della riproduzione del benchmark dopo la costruzione della funzione parametrica;

- controllo dello stato del solver lungo ciascuna griglia;

- confronto separato $\alpha$–$\beta$ dopo avere validato entrambe le sensitività;

- controllo della capacità effettivamente utilizzata durante la sensitività a $\phi$;

- controllo delle configurazioni assegnate durante la scenario analysis;

- controllo complessivo prima dell'interpretazione finale.

Il notebook deve quindi rendere visibile la sequenza:

$$
\text{operazione}
\longrightarrow
\text{output}
\longrightarrow
\text{controllo}
\longrightarrow
\text{uso successivo}.
$$

## 10. Criteri di validazione del notebook

Il notebook del Caso TakeHome è considerato valido se implementa integralmente la Scheda Caso senza modificarne il modello, produce tutti gli output richiesti, esegue i controlli previsti ed è riproducibile mediante esecuzione sequenziale dall'inizio alla fine.

### 10.1 Fedeltà alla specifica del caso

Il notebook deve:

1. utilizzare esclusivamente le variabili, i parametri, le formule, le griglie e gli scenari definiti nella Scheda Caso;

2. mantenere invariato l'ordinamento delle variabili una volta dichiarato;

3. rispettare la specifica:

$$
d(\alpha,\beta)
=
(32\alpha,18,14,32\beta)';
$$

4. rispettare la parametrizzazione della capacità di funding:

$$
\bar u_t(\phi)
=
\phi\bar u_t;
$$

5. mantenere invariato il costo del funding lungo le sensitività e gli scenari;

6. rispettare il vincolo prudenziale:

$$
\ell'x\leq7.5;
$$

7. rispettare il vincolo legacy:

$$
x_3+x_4\geq35;
$$

8. rispettare il limite:

$$
x_5\leq35;
$$

9. utilizzare esattamente le griglie parametriche assegnate;

10. utilizzare esattamente le configurazioni Standard, Mediamente critico e Critico previste dalla Scheda Caso;

11. non introdurre parametri, vincoli, scenari o modifiche del modello non autorizzati.

### 10.2 Validazione della forma solver

La traduzione computazionale è considerata valida se:

1. il vettore decisionale contiene correttamente le variabili:

$$
x_1,\ldots,x_5,
\qquad
g_1,\ldots,g_4,
\qquad
u_1,u_2,u_3;
$$

2. le dimensioni del vettore obiettivo, di $A_{\mathrm{eq}}$, $b_{\mathrm{eq}}$, $A_{\mathrm{ub}}$, $b_{\mathrm{ub}}$ e dei bounds sono reciprocamente compatibili;

3. il passaggio dal problema economico di massimizzazione alla convenzione di minimizzazione di `scipy.optimize.linprog` è effettuato correttamente;

4. i quattro bilanci temporali sono tradotti senza omissioni o errori di indice;

5. il vincolo prudenziale è codificato correttamente;

6. il vincolo legacy:

$$
x_3+x_4\geq35
$$

è codificato come:

$$
-x_3-x_4\leq-35;
$$

7. il limite:

$$
x_5\leq35
$$

è codificato correttamente;

8. i bounds del funding rispettano:

$$
0\leq u_t\leq\phi\bar u_t;
$$

9. le condizioni di non negatività sono correttamente rappresentate;

10. la forma solver può essere ricostruita direttamente dalle formule della Scheda Caso.

### 10.3 Validazione del benchmark

Il benchmark è considerato validato se:

1. il solver restituisce uno stato di ottimizzazione valido per:

$$
(\alpha,\beta,\phi)
=
(1,1,1);
$$

2. il vettore $x^*$ soddisfa il vincolo sulle risorse iniziali;

3. tutti i bilanci temporali risultano soddisfatti entro una tolleranza numerica dichiarata;

4. il vincolo prudenziale è rispettato;

5. il vincolo legacy è rispettato;

6. il limite su $x_5$ è rispettato;

7. tutti i bounds del funding sono rispettati;

8. tutte le variabili soddisfano le condizioni di non negatività;

9. slack e classificazione attivo / non attivo risultano coerenti;

10. i bounds attivi sono identificati correttamente;

11. il valore economico della funzione obiettivo è ricostruito correttamente;

12. i principali valori marginali sono associati al corretto vincolo o bilancio;

13. almeno un valore marginale è verificato mediante piccola perturbazione numerica.

### 10.4 Validazione specifica del vincolo legacy

La gestione del vincolo legacy è considerata valida se il notebook rende esplicita la distinzione tra forma economica e forma solver.

La forma economica è:

$$
x_3+x_4\geq L,
\qquad
L=35.
$$

La forma solver è:

$$
-x_3-x_4\leq -L.
$$

Ponendo:

$$
b=-L
$$

e:

$$
F=-\Pi,
$$

se il solver restituisce:

$$
m
=
\frac{\partial F^*}{\partial b},
$$

deve essere riconosciuto che:

$$
\frac{\partial\Pi^*}{\partial L}
=
m.
$$

La validazione richiede quindi:

1. corretta identificazione della riga del vincolo in $A_{\mathrm{ub}}$;

2. corretta identificazione del relativo termine noto;

3. assenza di un ulteriore cambio di segno introdotto meccanicamente;

4. verifica perturbativa di $L$ quando il vincolo è attivo e il marginale è localmente informativo;

5. coerenza tra variazione numerica di $\Pi^*$ e marginale restituito dal solver.

### 10.5 Validazione della funzione parametrica

La funzione solver parametrica è considerata valida se:

1. nel punto:

$$
(\alpha,\beta,\phi)
=
(1,1,1)
$$

riproduce la soluzione benchmark entro la tolleranza numerica adottata;

2. una variazione di $\alpha$ modifica esclusivamente il fabbisogno della prima data;

3. una variazione di $\beta$ modifica esclusivamente il fabbisogno della quarta data;

4. una variazione di $\phi$ modifica esclusivamente i bounds del funding;

5. il costo del funding resta invariato;

6. nessuna variazione parametrica altera accidentalmente coefficienti che devono restare fissi;

7. lo stato del solver viene controllato prima di utilizzare i valori della soluzione.

### 10.6 Validazione delle sensitività univariate

Ciascuna sensitività è considerata valida se:

1. varia un solo parametro alla volta;

2. gli altri due parametri restano pari ai valori benchmark;

3. viene utilizzata integralmente la griglia assegnata;

4. per ogni punto viene registrato almeno lo stato del solver e la fattibilità;

5. valori di $x^*$, $g^*$, $u^*$ e $\Pi^*$ vengono utilizzati soltanto quando la soluzione è valida;

6. le variazioni rispetto al benchmark sono calcolate coerentemente;

7. i rapporti di utilizzo della capacità di funding utilizzano il denominatore corretto:

$$
\phi\bar u_t;
$$

8. i cambiamenti della soluzione vengono confrontati con gli eventuali cambiamenti dei vincoli e dei bounds attivi;

9. il ruolo del vincolo legacy viene monitorato lungo le griglie;

10. le interpretazioni dei valori marginali restano locali e coerenti con la configurazione considerata.

### 10.7 Validazione del confronto tra $\alpha$ e $\beta$

Il confronto tra prima e seconda ondata è considerato valido se:

1. le due sensitività sono costruite separatamente;

2. nelle configurazioni confrontate la variazione relativa del parametro è confrontabile;

3. non vengono modificati simultaneamente $\alpha$ e $\beta$;

4. il confronto considera almeno:

$$
\Pi^*,
$$

e, quando informativo:

$$
x^*,
\qquad
g^*,
\qquad
u^*;
$$

5. le differenze osservate vengono interpretate alla luce del diverso timing dei fabbisogni;

6. non viene attribuito automaticamente lo stesso effetto economico a shock della stessa intensità relativa ma collocati in date diverse.

### 10.8 Validazione della scenario analysis

La scenario analysis è considerata valida se:

1. utilizza esattamente le tre configurazioni assegnate;

2. $\alpha$, $\beta$ e $\phi$ vengono modificati congiuntamente secondo ciascuno scenario;

3. lo scenario Standard riproduce il benchmark;

4. lo stato del solver viene controllato separatamente per ogni scenario;

5. soltanto gli scenari con soluzione valida vengono utilizzati nell'analisi numerica ed economica;

6. la perdita rispetto allo scenario Standard è calcolata come:

$$
L_s
=
\Pi_{\mathrm{Standard}}^*
-
\Pi_s^*;
$$

7. la scenario analysis resta distinta dalle sensitività univariate;

8. agli scenari non vengono attribuite probabilità.

### 10.9 Validazione degli output

Gli output sono considerati validi se:

1. tutti i risultati numerici richiesti nella Scheda Caso sono presenti;

2. tutte le tabelle richieste sono presenti;

3. tutti i grafici richiesti sono presenti;

4. tabelle e grafici utilizzano esclusivamente risultati validi;

5. la tabella dedicata al vincolo legacy mantiene distinta la forma economica dalla forma codificata;

6. nessun valore della soluzione è inserito manualmente nelle celle successive;

7. titoli, etichette e grandezze rappresentate consentono di identificare chiaramente parametro, variabile o scenario;

8. gli output hanno una funzione informativa, diagnostica o interpretativa riconoscibile;

9. gli output possono essere rigenerati mediante riesecuzione delle celle;

10. non sono richieste esportazioni in file esterni salvo indicazione esplicita del docente.

### 10.10 Validazione della struttura del notebook

Il notebook deve:

1. seguire una sequenza coerente con il Flusso logico-teorico risolutivo e con la scomposizione in tappe validata;

2. mantenere distinguibili:
   - ricognizione del nuovo problema;
   - forma solver;
   - benchmark;
   - controllo del vincolo legacy;
   - parametrizzazione;
   - sensitività ad $\alpha$;
   - sensitività a $\beta$;
   - confronto tra le due ondate;
   - sensitività a $\phi$;
   - scenario analysis;
   - controlli conclusivi;

3. integrare celle Markdown e codice in modo da rendere tracciabile il passaggio dalla formulazione teorica all'operazione computazionale;

4. non contenere celle errate duplicate o versioni alternative non utilizzate;

5. essere eseguibile sequenzialmente dall'inizio alla fine;

6. non dipendere da oggetti prodotti da esecuzioni precedenti non riproducibili;

7. mantenere coerenti notazione matematica e nomi delle variabili computazionali;

8. non essere una semplice copia del notebook Aula con coefficienti sostituiti.

### 10.11 Validazione dell'uso dell'IA

Quando l'IA è utilizzata, il notebook e il relativo tracciato devono risultare coerenti con il protocollo previsto.

In particolare:

1. Prompt zero, Prompt 1, Prompt 2 e Prompt 3 devono precedere i prompt operativi di tappa;

2. il Flusso logico-teorico deve essere validato prima della scomposizione in tappe;

3. la scomposizione in tappe deve essere validata prima dello sviluppo operativo;

4. i prompt di tappa devono essere riconducibili alle tappe approvate;

5. il Regime A non deve produrre codice Python;

6. il Regime B deve tradurre in codice strutture già definite e validate;

7. il Regime C non deve essere attivato automaticamente;

8. un eventuale Regime C deve partire da una criticità specifica individuata dallo studente;

9. l'IA non deve modificare autonomamente la Scheda Caso;

10. l'IA non deve trasformare il TakeHome in una replica automatica del Caso Aula;

11. la risposta dell'IA deve essere verificata prima di essere incorporata nel notebook.

### 10.12 Criteri specifici del Caso TakeHome

Oltre ai criteri generali, il notebook del Caso TakeHome è considerato valido soltanto se:

1. riproduce correttamente il benchmark del modello First Republic;

2. rende esplicita la nuova struttura con cinque classi di attivo;

3. tratta separatamente la prima e la seconda ondata di fabbisogno;

4. distingue chiaramente il ruolo di $\alpha$ e $\beta$;

5. implementa correttamente il vincolo legacy;

6. interpreta correttamente il relativo marginale;

7. verifica mediante perturbazione il significato economico del marginale legacy quando pertinente;

8. implementa correttamente il limite:

$$
x_5\leq35;
$$

9. mantiene invariato il costo del funding;

10. analizza correttamente la capacità di funding mediante $\phi$;

11. confronta esplicitamente gli effetti della prima e della seconda ondata;

12. produce tutti gli output previsti nella Scheda Caso;

13. conclude con controlli complessivi coerenti con i limiti del modello;

14. dimostra trasferimento autonomo del metodo appreso nel Caso Aula.

Un notebook che restituisca semplicemente `success=True` nel benchmark ma non soddisfi i controlli, gli output e i criteri precedenti non è considerato validato.

## 11. Calibrazione docente

La presente sezione contiene informazioni interne di calibrazione e validazione preventiva del Caso TakeHome.

Tali informazioni servono al docente per verificare che il caso sia numericamente non banale, coerente con gli obiettivi didattici e sufficientemente distinto dal Caso Aula.

I valori numerici e le conclusioni riportati in questa sezione non devono essere trasferiti nella Scheda Caso destinata agli studenti.

### 11.1 Obiettivo della calibrazione

La calibrazione deve garantire che il Caso TakeHome:

1. sia ammissibile nel benchmark;

2. produca una soluzione economicamente interpretabile;

3. renda effettivamente rilevante il vincolo legacy;

4. renda osservabili differenze fra shock alla prima data e shock alla data terminale;

5. renda informativa la sensitività rispetto alla capacità di funding;

6. produca scenari congiunti sufficientemente distinti;

7. non sia risolvibile mediante semplice sostituzione dei coefficienti del Caso Aula;

8. richieda allo studente un effettivo trasferimento del metodo.

### 11.2 Configurazione benchmark

La configurazione benchmark è:

$$
(\alpha,\beta,\phi)
=
(1,1,1).
$$

In tale configurazione devono essere verificati almeno:

1. ammissibilità del problema;

2. soddisfacimento dei quattro bilanci temporali;

3. rispetto del vincolo prudenziale:

$$
\ell'x\leq7.5;
$$

4. rispetto del vincolo legacy:

$$
x_3+x_4\geq35;
$$

5. rispetto del limite:

$$
x_5\leq35;
$$

6. rispetto dei bounds del funding:

$$
0\leq u_t\leq\bar u_t;
$$

7. non negatività di tutte le variabili;

8. presenza di almeno un vincolo o bound economicamente informativo.

La soluzione benchmark deve costituire una base leggibile per le successive analisi di sensitività.

### 11.3 Calibrazione del vincolo legacy

Il vincolo:

$$
x_3+x_4\geq35
$$

deve svolgere una funzione economica effettiva nel caso.

La calibrazione deve evitare due situazioni estreme:

1. vincolo sempre molto lasco e quindi sostanzialmente irrilevante;

2. vincolo talmente stringente da rendere il problema quasi sempre non ammissibile.

Il caso è ben calibrato se il vincolo legacy:

1. limita effettivamente la flessibilità del portafoglio;

2. può diventare attivo o quasi attivo in configurazioni economicamente significative;

3. modifica la capacità del modello di reagire agli shock;

4. produce un valore marginale interpretabile quando attivo.

La forma economica:

$$
x_3+x_4\geq L
$$

deve essere mantenuta distinta dalla forma solver:

$$
-x_3-x_4\leq -L.
$$

Se:

$$
F=-\Pi,
\qquad
b=-L,
$$

e:

$$
m
=
\frac{\partial F^*}{\partial b},
$$

allora deve essere verificata localmente la relazione:

$$
\frac{\partial\Pi^*}{\partial L}
=
m.
$$

La calibrazione docente deve verificare numericamente tale relazione mediante una piccola perturbazione di \(L\) quando il vincolo è attivo e il marginale è informativo.

### 11.4 Calibrazione della doppia ondata

La struttura:

$$
d(\alpha,\beta)
=
(32\alpha,18,14,32\beta)'
$$

deve produrre effetti distinguibili fra:

- aumento di \(\alpha\);
- aumento di \(\beta\).

La calibrazione deve consentire di osservare che la stessa variazione relativa del fabbisogno non genera necessariamente la stessa risposta quando lo shock si verifica:

- alla prima data;
- alla data terminale.

Le differenze possono emergere in:

1. valore ottimo;

2. composizione dell'attivo;

3. giacenze;

4. utilizzo del funding;

5. vincoli attivi;

6. ruolo del vincolo legacy.

Il confronto non deve essere costruito artificialmente per produrre un risultato predeterminato, ma deve risultare sufficientemente informativo da giustificare una discussione economico-finanziaria.

### 11.5 Calibrazione della capacità di funding

La sensitività rispetto a:

$$
\phi
$$

deve evidenziare il ruolo della capacità disponibile di funding.

La calibrazione deve produrre almeno una regione nella quale una riduzione di \(\phi\):

1. comprime la capacità di risposta del sistema;

2. modifica l'utilizzo effettivo del funding o la composizione ottima dell'attivo;

3. incide sul valore ottimo;

4. modifica, quando rilevante, l'insieme dei bounds attivi.

Deve inoltre essere possibile osservare una regione nella quale ulteriore capacità di funding non produca necessariamente benefici marginali rilevanti.

### 11.6 Calibrazione degli scenari

Devono essere validate mediante solver le configurazioni:

**Standard**

$$
(\alpha,\beta,\phi)
=
(1.00,1.00,1.00);
$$

**Mediamente critico**

$$
(\alpha,\beta,\phi)
=
(1.03,1.03,0.90);
$$

**Critico**

$$
(\alpha,\beta,\phi)
=
(1.06,1.06,0.75).
$$

Lo scenario Standard deve coincidere con il benchmark.

Gli scenari Mediamente critico e Critico devono produrre configurazioni sufficientemente diverse da rendere osservabili:

1. variazioni del valore ottimo;

2. ricomposizione dell'attivo;

3. variazione delle giacenze;

4. variazione del funding;

5. ruolo del vincolo legacy;

6. eventuali modifiche dei vincoli e dei bounds attivi.

Gli scenari non devono essere calibrati in modo da risultare:

- quasi identici allo Standard;
- talmente estremi da perdere utilità didattica.

### 11.7 Relazioni qualitative attese

La calibrazione deve produrre almeno le seguenti relazioni qualitative.

1. Un aumento di \(\alpha\) deve aumentare la pressione di liquidità alla prima data.

2. Un aumento di \(\beta\) deve aumentare la pressione di liquidità alla data terminale.

3. Gli effetti di \(\alpha\) e \(\beta\) non devono essere necessariamente simmetrici.

4. Una riduzione di \(\phi\) deve ridurre la capacità disponibile di funding.

5. Il vincolo legacy deve limitare la possibilità di ristrutturare liberamente il portafoglio.

6. Il limite:

$$
x_5\leq35
$$

deve essere correttamente distinguibile dal vincolo legacy.

7. Cambiamenti nella soluzione ottima devono poter essere messi in relazione con cambiamenti nei vincoli attivi.

8. Le sensitività univariate devono produrre una lettura distinta dalla scenario analysis.

### 11.8 Errori o ambiguità prevedibili

Gli errori più probabili sono:

1. trattare il TakeHome come copia del Caso Aula;

2. dimenticare la quinta classe di attivo;

3. confondere \(\alpha\) e \(\beta\);

4. applicare \(\alpha\) o \(\beta\) a date non corrette;

5. dimenticare che il costo del funding è invariato;

6. applicare \(\phi\) al funding effettivamente utilizzato anziché alla capacità;

7. codificare erroneamente:

$$
x_3+x_4\geq35;
$$

8. interpretare il marginale del vincolo legacy introducendo un cambio di segno non necessario;

9. confondere il limite:

$$
x_5\leq35
$$

con il vincolo legacy;

10. dimenticare il rimborso del funding raccolto nella data precedente;

11. utilizzare valori del solver quando il problema non è ammissibile;

12. confondere sensitività univariata e scenario analysis;

13. confrontare \(\alpha\) e \(\beta\) facendo variare simultaneamente entrambi;

14. interpretare i parametri stilizzati come dati storici effettivi di First Republic Bank;

15. attribuire probabilità agli scenari;

16. interpretare un marginale locale come relazione globale;

17. ignorare il ruolo temporale dei cash flow degli attivi;

18. interpretare un vincolo attivo come automaticamente economicamente dominante.

### 11.9 Controlli minimi di calibrazione

Prima di considerare il caso pronto per l'utilizzo didattico, il docente deve verificare almeno:

1. ammissibilità del benchmark;

2. errori dei bilanci temporali entro la tolleranza adottata;

3. rispetto del vincolo prudenziale;

4. rispetto del vincolo legacy;

5. rispetto del limite su \(x_5\);

6. rispetto dei bounds del funding;

7. coerenza fra slack e classificazione dei vincoli attivi;

8. corretta identificazione dei bounds attivi;

9. verifica numerica di almeno un valore marginale;

10. verifica specifica del marginale legacy mediante perturbazione di \(L\);

11. riproduzione del benchmark mediante la funzione parametrica;

12. variazione di un solo parametro alla volta nelle sensitività;

13. corretta separazione fra effetti di \(\alpha\) e \(\beta\);

14. corretto aggiornamento dei bounds quando varia \(\phi\);

15. coerenza fra variazioni della soluzione e cambiamenti dei vincoli attivi;

16. validità numerica delle tre configurazioni di scenario;

17. riproducibilità integrale del notebook mediante esecuzione sequenziale.

### 11.10 Limiti interpretativi da preservare

La calibrazione deve mantenere visibili i seguenti limiti.

1. Il modello è deterministico.

2. Ogni configurazione parametrica è nota al tempo iniziale.

3. Il comportamento dei depositanti non è modellato endogenamente.

4. Non sono modellati fire sales o feedback fra vendite e prezzi.

5. Non è modellato un mark-to-market endogeno degli attivi.

6. La capacità di funding è esogena.

7. Il costo del funding è fissato e non varia con \(\alpha\), \(\beta\) o \(\phi\).

8. Il vincolo legacy è una rappresentazione stilizzata.

9. \(\alpha\), \(\beta\) e \(\phi\) non sono variabili casuali.

10. Gli scenari non costituiscono una distribuzione probabilistica.

11. Non vengono assegnate probabilità agli scenari.

12. Non viene effettuata ottimizzazione stocastica.

13. Le decisioni non sono adattive rispetto a informazione osservata progressivamente.

14. I coefficienti numerici non devono essere interpretati come dati storici effettivi di First Republic Bank.

### 11.11 Segnali di possibile cattiva calibrazione

Il caso deve essere riesaminato se emerge una delle seguenti situazioni:

1. benchmark non ammissibile;

2. vincolo legacy completamente irrilevante in tutte le configurazioni;

3. vincolo legacy così stringente da dominare trivialmente tutto il problema;

4. \(\alpha\) e \(\beta\) producono risposte praticamente indistinguibili;

5. la sensitività a \(\phi\) non produce alcun effetto;

6. il limite su \(x_5\) non svolge alcun ruolo in nessuna configurazione;

7. gli scenari risultano quasi identici;

8. lo scenario Critico risulta privo di utilità interpretativa;

9. le variazioni della soluzione sono dominate da artefatti numerici;

10. il caso può essere risolto modificando soltanto i coefficienti del notebook Aula senza riformulare la struttura;

11. gli output non consentono di discutere il timing delle due ondate;

12. non emerge alcun elemento che distingua realmente il TakeHome dal Caso Aula.

La calibrazione finale deve garantire un caso numericamente stabile, non banale, autonomo rispetto all'Aula e coerente con la funzione di trasferimento metodologico prevista per il TakeHome.

## 12. Uso dell'IA e tracciato

### 12.1 Uso documentato dell'IA previsto

L'uso documentato dell'IA è previsto.

Nel Caso TakeHome l'IA deve svolgere una funzione di supporto controllato, senza sostituire il trasferimento autonomo del metodo da parte dello studente.

L'IA può assistere:

1. nella ricognizione della struttura del nuovo problema;
2. nella traduzione computazionale di strutture già definite;
3. nella costruzione dei controlli;
4. nella verifica di output specifici;
5. nella revisione di una criticità puntuale.

Non deve sostituire:

1. la Scheda Caso;
2. il riconoscimento delle differenze strutturali rispetto al Caso Aula;
3. la costruzione del Flusso logico-teorico;
4. la scomposizione in tappe;
5. la validazione degli output;
6. l'interpretazione finanziaria finale.

### 12.2 Prompt obbligatori

La sequenza obbligatoria comprende:

1. Prompt zero;
2. Prompt 1;
3. Prompt 2;
4. Prompt 3;
5. prompt di tappa necessari a sviluppare la scomposizione operativa validata.

Il Regime C non costituisce un prompt obbligatorio.

Un eventuale Prompt C può essere aggiunto soltanto quando lo studente individua una criticità specifica da verificare.

La sequenza ordinaria è quindi:

$$
\text{Prompt zero}
\longrightarrow
\text{Prompt 1}
\longrightarrow
\text{Prompt 2}
\longrightarrow
\text{Prompt 3}
\longrightarrow
\text{prompt di tappa}.
$$

### 12.3 Numero dei prompt

Il numero complessivo dei prompt non deve essere fissato artificialmente a priori.

Deve derivare dalla scomposizione operativa validata e dal numero di interazioni effettivamente necessarie per:

1. sviluppare le tappe previste;
2. produrre gli output richiesti;
3. eseguire i controlli;
4. correggere eventuali errori ordinari all'interno dei Regimi A o B.

Un eventuale Prompt C si aggiunge alla sequenza soltanto in presenza di una criticità specifica individuata dallo studente.

Non è richiesto un numero minimo di Prompt C.

Non deve essere introdotto un Prompt C puramente formale allo scopo di soddisfare un requisito quantitativo.

### 12.4 Regimi IA utilizzati

I regimi ordinariamente utilizzati sono:

- **Regime A — Ricognizione teorico-modellistica**;
- **Regime B — Traduzione operativa in codice**.

Il **Regime C — Verifica di una criticità specifica** è eventuale.

#### Regime A

Il Regime A deve essere utilizzato quando occorre:

1. riconoscere la struttura del problema;
2. distinguere il TakeHome dal Caso Aula;
3. ordinare i passaggi logici;
4. chiarire il ruolo di $\alpha$, $\beta$ e $\phi$;
5. chiarire il ruolo del vincolo legacy;
6. confrontare prima e seconda ondata;
7. interpretare risultati già prodotti;
8. collegare variazioni della soluzione e vincoli attivi.

Il Regime A non deve produrre codice Python.

#### Regime B

Il Regime B deve essere utilizzato quando una struttura già definita deve essere tradotta in codice.

Può riguardare:

1. costruzione delle matrici;
2. implementazione del solver;
3. calcolo di residuali e slack;
4. implementazione del vincolo legacy;
5. costruzione della funzione parametrica;
6. esecuzione delle griglie;
7. produzione di DataFrame;
8. produzione dei grafici;
9. controlli numerici;
10. perturbazione del limite legacy;
11. scenario analysis.

Il Regime B non può modificare la specifica teorica del caso.

#### Regime C

Il Regime C può essere attivato soltanto quando lo studente identifica una possibile criticità specifica.

Il prompt deve contenere:

1. tappa interessata;
2. cella, formula, output o controllo interessato;
3. criticità osservata;
4. ragionamento che motiva il dubbio.

L'IA deve classificare l'esito come:

- **criticità respinta**;
- **criticità accolta**.

Il Regime C non può essere utilizzato per richiedere:

- una revisione generica dell'intero notebook;
- una nuova soluzione completa del caso;
- una trasformazione automatica del notebook Aula;
- un'interpretazione finale delegata all'IA.

### 12.5 Usi ammessi dell'IA

Sono ammessi:

1. verifica della traduzione tra formulazione teorica e forma solver;

2. controllo dell'ordinamento delle variabili;

3. controllo delle dimensioni di vettori e matrici;

4. supporto alla costruzione di codice per una tappa già definita;

5. supporto alla corretta codifica del vincolo:

$$
x_3+x_4\geq35;
$$

6. supporto alla costruzione di:

$$
d(\alpha,\beta)
=
(32\alpha,18,14,32\beta)';
$$

7. costruzione della funzione parametrica in:

$$
(\alpha,\beta,\phi);
$$

8. supporto alla gestione dei DataFrame;

9. costruzione dei grafici richiesti;

10. spiegazione tecnica degli oggetti restituiti da `scipy.optimize.linprog`;

11. supporto alla verifica di residuali, slack e bounds attivi;

12. supporto alla verifica numerica di un valore marginale;

13. verifica perturbativa del limite legacy;

14. controllo della corretta applicazione di $\alpha$, $\beta$ e $\phi$;

15. supporto alla gestione delle configurazioni non ammissibili;

16. confronto tra output numerici, tabelle e grafici;

17. revisione di codice dopo che sia stato identificato un errore o un malfunzionamento;

18. supporto alla verifica della coerenza fra variazioni della soluzione e variazioni dei vincoli attivi;

19. supporto alla revisione critica di una specifica interpretazione già formulata dallo studente.

### 12.6 Usi non ammessi dell'IA

Non sono ammessi:

1. chiedere all'IA di risolvere integralmente il caso in un unico prompt;

2. chiedere all'IA di trasformare automaticamente il Caso Aula nel TakeHome;

3. delegare all'IA l'individuazione autonoma delle differenze strutturali senza un contributo iniziale dello studente;

4. modificare variabili, formule, parametri, vincoli o scenari fissati dalla Scheda Caso;

5. eliminare o modificare il vincolo legacy;

6. modificare il limite:

$$
x_5\leq35;
$$

7. introdurre un parametro di costo del funding che non esiste nella specifica;

8. modificare le griglie assegnate senza autorizzazione;

9. modificare le tre configurazioni di scenario;

10. chiedere un notebook completo senza passare attraverso Flusso logico-teorico e scomposizione in tappe;

11. accettare automaticamente il significato del marginale legacy senza verifica della convenzione:

$$
F=-\Pi,
\qquad
b=-L;
$$

12. interpretare automaticamente grafici e tabelle senza confronto con la soluzione numerica e con i vincoli attivi;

13. attribuire valore storico ai parametri stilizzati del modello;

14. utilizzare il Regime C per una revisione generica del lavoro;

15. chiedere all'IA di scrivere autonomamente l'interpretazione finanziaria finale da consegnare come contributo dello studente.

### 12.7 Criteri di validazione delle risposte IA

Ogni risposta dell'IA deve essere verificata prima di essere incorporata nel notebook.

La validazione deve controllare almeno:

1. coerenza con il Regime richiesto;

2. coerenza con la Scheda Caso;

3. utilizzo esclusivo degli input disponibili nella tappa;

4. rispetto delle variabili e della notazione fissate;

5. assenza di modifiche non autorizzate al modello;

6. corretta distinzione fra $\alpha$ e $\beta$;

7. corretta gestione di $\phi$ come parametro della capacità di funding;

8. corretta gestione del vincolo legacy;

9. correttezza della traduzione computazionale quando pertinente;

10. pertinenza degli output proposti;

11. presenza dei controlli richiesti dalla tappa;

12. utilità dell'output prodotto per la tappa successiva;

13. coerenza fra codice, output numerici e formule;

14. assenza di automatismi derivati dal Caso Aula non giustificati dalla nuova specifica.

Se la risposta è in Regime C deve essere inoltre verificato che:

1. la criticità sia stata formulata prima dallo studente;

2. l'IA abbia verificato esclusivamente la criticità indicata;

3. l'esito sia classificato come **criticità respinta** oppure **criticità accolta**;

4. in caso di criticità respinta non siano state introdotte modifiche arbitrarie;

5. in caso di criticità accolta la correzione sia limitata alla parte effettivamente interessata.

### 12.8 Tracciato IA richiesto

Il tracciato IA è richiesto.

La modalità ordinaria di consegna è la stampa PDF della chat dedicata al caso.

La chat deve essere utilizzata esclusivamente per il lavoro relativo al Caso TakeHome.

Non deve contenere:

1. conversazioni estranee;
2. materiale personale;
3. prove casuali non pertinenti;
4. richieste riferite ad altri casi;
5. messaggi che rendano ambiguo il tracciato del processo.

### 12.9 Sequenza osservabile richiesta nel tracciato

Il tracciato deve rendere osservabile la sequenza:

$$
\text{Prompt zero}
\longrightarrow
\text{Prompt 1}
\longrightarrow
\text{Prompt 2}
\longrightarrow
\text{Prompt 3}
\longrightarrow
\text{prompt di tappa effettivamente utilizzati}.
$$

Quando presente, un eventuale Prompt C deve essere collocato nel punto in cui la criticità è effettivamente emersa.

Il tracciato deve permettere di ricostruire:

1. il contributo iniziale dello studente;

2. la risposta dell'IA;

3. la decisione dello studente di accettare, correggere, ridurre o rifiutare la risposta;

4. la traduzione nel notebook;

5. l'output prodotto;

6. il controllo effettuato;

7. il passaggio alla tappa successiva.

Nel Caso TakeHome il tracciato deve inoltre rendere osservabile che lo studente abbia autonomamente riconosciuto:

1. la presenza di cinque classi di attivo;

2. la doppia ondata di fabbisogno;

3. il ruolo distinto di $\alpha$ e $\beta$;

4. il vincolo legacy;

5. il limite su $x_5$;

6. la diversa struttura parametrica rispetto al Caso Aula.

### 12.10 Elementi del tracciato oggetto di valutazione

Sono oggetto di valutazione:

1. contributo autonomo dello studente nel Prompt 2;

2. contributo autonomo dello studente nel Prompt 3;

3. capacità di riconoscere le differenze strutturali rispetto al Caso Aula;

4. capacità di formulare prompt di tappa coerenti con la scomposizione validata;

5. corretta distinzione tra Regime A e Regime B;

6. specificità degli input forniti all'IA;

7. chiarezza dell'output richiesto;

8. presenza dei controlli all'interno dei prompt di tappa;

9. capacità di verificare criticamente le risposte IA;

10. capacità di non delegare all'IA decisioni già fissate dalla Scheda Caso;

11. coerenza tra conversazione, notebook e output prodotti;

12. eventuale qualità dell'attivazione del Regime C quando sia emersa una criticità reale.

L'assenza di un Prompt C non costituisce penalizzazione quando non è emersa alcuna criticità specifica che ne giustificasse l'utilizzo.

### 12.11 Responsabilità dello studente

Restano responsabilità dello studente:

1. riconoscere le differenze strutturali rispetto al Caso Aula;

2. validare il Flusso logico-teorico;

3. validare la scomposizione in tappe;

4. controllare il codice prodotto dall'IA;

5. eseguire il notebook;

6. verificare gli output;

7. eseguire i controlli previsti;

8. verificare la corretta gestione del vincolo legacy;

9. distinguere correttamente gli effetti di $\alpha$ e $\beta$;

10. riconoscere eventuali anomalie;

11. decidere se una risposta IA debba essere accettata, modificata o respinta;

12. formulare eventuali criticità da verificare in Regime C;

13. redigere l'interpretazione finanziaria finale.

L'uso dell'IA deve restare tracciabile, controllato e subordinato al trasferimento autonomo del metodo da parte dello studente.

## 13. Valutazione

La valutazione deve considerare congiuntamente:

1. correttezza della formulazione quantitativa;
2. qualità della traduzione computazionale;
3. completezza e validità degli output;
4. qualità dei controlli;
5. capacità di trasferire autonomamente il metodo dal Caso Aula;
6. uso documentato e consapevole dell'IA;
7. coerenza dell'interpretazione finale.

L'ottenimento di una soluzione numerica non è sufficiente, da solo, per considerare corretto il lavoro.

### 13.1 Criteri per il notebook

Il notebook deve essere valutato almeno rispetto ai seguenti aspetti.

1. **Ricognizione autonoma del nuovo problema**
   - corretta identificazione delle cinque classi di attivo;
   - corretta identificazione della doppia ondata di fabbisogno;
   - riconoscimento del vincolo legacy;
   - riconoscimento del limite su $x_5$;
   - distinzione rispetto alla struttura del Caso Aula.

2. **Corretta costruzione della forma solver**
   - ordinamento delle variabili;
   - vettore obiettivo;
   - uguaglianze;
   - disuguaglianze;
   - bounds.

3. **Fedeltà alla Scheda Caso**
   - nessuna modifica non autorizzata a variabili, formule, parametri, griglie o scenari;
   - corretta implementazione di $\alpha$, $\beta$ e $\phi$;
   - mantenimento invariato del costo del funding.

4. **Soluzione benchmark**
   - stato valido del solver;
   - soluzione coerente;
   - corretta ricostruzione di $\Pi^*$.

5. **Controlli numerici**
   - residuali;
   - slack;
   - bounds attivi;
   - rispetto del vincolo prudenziale;
   - rispetto del vincolo legacy;
   - rispetto del limite su $x_5$;
   - rispetto dei limiti sul funding;
   - non negatività.

6. **Gestione del vincolo legacy**
   - corretta codifica:

$$
x_3+x_4\geq35
$$

come:

$$
-x_3-x_4\leq-35;
$$

   - corretta associazione del marginale alla riga codificata;
   - corretta interpretazione rispetto al limite economico originario;
   - verifica perturbativa quando il marginale è localmente informativo.

7. **Qualità della funzione parametrica**
   - riproduzione del benchmark;
   - corretta azione separata di $\alpha$, $\beta$ e $\phi$;
   - assenza di modifiche accidentali alla struttura del modello.

8. **Sensitività ad $\alpha$**
   - corretta variazione del fabbisogno alla prima data;
   - mantenimento di $\beta=\phi=1$;
   - qualità di tabelle e grafici;
   - corretta gestione dei vincoli attivi.

9. **Sensitività a $\beta$**
   - corretta variazione del fabbisogno alla quarta data;
   - mantenimento di $\alpha=\phi=1$;
   - qualità di tabelle e grafici;
   - corretta gestione dei vincoli attivi.

10. **Confronto $\alpha$–$\beta$**
    - confronto di configurazioni omogenee;
    - corretta lettura del diverso timing;
    - capacità di distinguere gli effetti della prima e della seconda ondata.

11. **Sensitività a $\phi$**
    - corretta variazione della capacità di funding;
    - utilizzo del denominatore corretto nei rapporti di utilizzo;
    - capacità di individuare regioni nelle quali la capacità è scarsa o abbondante.

12. **Scenario analysis**
    - utilizzo esatto delle configurazioni assegnate;
    - confronto coerente tra Standard, Mediamente critico e Critico;
    - corretta lettura della perdita di valore e delle modifiche del piano ALM.

13. **Qualità degli output**
    - completezza;
    - leggibilità;
    - pertinenza;
    - coerenza con le quantità richieste;
    - assenza di grafici o tabelle puramente decorativi.

14. **Riproducibilità**
    - esecuzione sequenziale dall'inizio alla fine;
    - assenza di dipendenze nascoste;
    - assenza di valori inseriti manualmente.

### 13.2 Criteri per il trasferimento metodologico

Il Caso TakeHome deve valutare in modo esplicito la capacità dello studente di trasferire il metodo appreso nel Caso Aula.

Devono essere osservati almeno i seguenti aspetti:

1. capacità di distinguere elementi riutilizzabili ed elementi da riformulare;

2. capacità di adattare la struttura solver alla presenza di cinque classi di attivo;

3. capacità di trattare separatamente $\alpha$ e $\beta$;

4. capacità di integrare il vincolo legacy nella forma solver;

5. capacità di gestire il limite su $x_5$;

6. capacità di mantenere invariato il costo del funding quando la nuova specifica non ne prevede la parametrizzazione;

7. capacità di costruire autonomamente nuovi controlli coerenti con la struttura del caso;

8. capacità di non riprodurre meccanicamente analisi non pertinenti importate dal Caso Aula.

Un notebook ottenuto mediante semplice sostituzione dei coefficienti del Caso Aula non soddisfa il requisito di trasferimento metodologico.

### 13.3 Criteri per il tracciato IA

Il tracciato IA deve essere valutato almeno rispetto a:

1. presenza e corretto utilizzo di Prompt zero, Prompt 1, Prompt 2 e Prompt 3;

2. contributo autonomo dello studente nella costruzione del Flusso logico-teorico risolutivo;

3. contributo autonomo dello studente nella scomposizione in tappe;

4. capacità di riconoscere le differenze strutturali rispetto al Caso Aula;

5. qualità dei prompt di tappa;

6. corretta distinzione tra Regime A e Regime B;

7. capacità di fornire all'IA input completi ma non ridondanti;

8. esplicitazione di output e controlli richiesti;

9. capacità di verificare criticamente le risposte dell'IA;

10. capacità di accettare, modificare o rifiutare una risposta motivando la scelta;

11. assenza di delega all'IA delle decisioni già fissate dalla Scheda Caso;

12. coerenza tra tracciato IA e notebook finale;

13. eventuale corretto utilizzo del Regime C quando effettivamente giustificato da una criticità specifica.

L'assenza di un intervento in Regime C non costituisce una carenza quando non emerge una criticità specifica.

### 13.4 Peso dei controlli e dell'interpretazione

La valutazione deve attribuire rilievo elevato alla correttezza dei controlli e alla capacità di leggere gli output.

Non è sufficiente ottenere:

```text
success = True
```

dal solver.

Lo studente deve mostrare di sapere verificare:

1. bilanci temporali;
2. vincolo prudenziale;
3. vincolo legacy;
4. limite su $x_5$;
5. bounds del funding;
6. residuali;
7. slack;
8. valori marginali;
9. fattibilità;
10. coerenza tra output numerici e rappresentazioni grafiche;
11. relazione tra cambiamenti della soluzione e cambiamenti dei vincoli attivi.

### 13.5 Elementi particolarmente rilevanti nel Caso TakeHome

Nel Caso TakeHome First Republic assumono particolare rilievo valutativo:

1. corretta traduzione autonoma della nuova struttura ALM;

2. corretta gestione delle cinque classi di attivo;

3. corretta implementazione di:

$$
d(\alpha,\beta)
=
(32\alpha,18,14,32\beta)';
$$

4. corretta distinzione fra shock alla prima data e shock alla quarta data;

5. corretta implementazione del vincolo legacy:

$$
x_3+x_4\geq35;
$$

6. corretta interpretazione del marginale legacy;

7. verifica perturbativa della relazione:

$$
\frac{\partial\Pi^*}{\partial L}
=
m;
$$

8. corretta gestione del limite:

$$
x_5\leq35;
$$

9. corretta parametrizzazione della capacità di funding tramite $\phi$;

10. mantenimento invariato del costo del funding;

11. confronto economico fra prima e seconda ondata;

12. capacità di distinguere risultati del modello e fatti storici relativi a First Republic Bank.

### 13.6 Errori che devono incidere significativamente sulla valutazione

Devono incidere in modo rilevante:

1. modifica non autorizzata della Scheda Caso;

2. trattamento del TakeHome come replica automatica del Caso Aula;

3. errore nella forma solver;

4. errore nella codifica del vincolo legacy;

5. introduzione di un cambio di segno non corretto nell'interpretazione del marginale legacy;

6. confusione tra $\alpha$ e $\beta$;

7. applicazione di $\alpha$ o $\beta$ alla data errata;

8. modifica del costo del funding quando deve restare invariato;

9. errata applicazione di $\phi$;

10. utilizzo di risultati provenienti da configurazioni non ammissibili;

11. mancata verifica dei vincoli;

12. assenza di controlli numerici;

13. confusione tra sensitività e scenario analysis;

14. confronto $\alpha$–$\beta$ costruito facendo variare simultaneamente entrambi i parametri;

15. notebook non riproducibile;

16. delega all'IA dell'intera soluzione o dell'interpretazione finale.

### 13.7 Qualità attesa dell'interpretazione finale

L'interpretazione finale dello studente deve:

1. basarsi su risultati numericamente validati;

2. collegare il valore ottimo alla composizione dell'attivo, alle giacenze e al funding;

3. discutere il ruolo del vincolo legacy;

4. discutere il ruolo del limite su $x_5$ quando economicamente rilevante;

5. confrontare gli effetti della prima e della seconda ondata;

6. discutere il ruolo della capacità di funding;

7. collegare i cambiamenti della soluzione ai cambiamenti dei vincoli attivi;

8. confrontare gli scenari assegnati;

9. richiamare i limiti del modello;

10. evitare inferenze storiche non giustificate dai dati stilizzati.

La qualità dell'interpretazione deve essere valutata sulla coerenza con gli output e con i limiti dichiarati, non sulla lunghezza del commento.

## 14. Rubrica sintetica

Per il Caso TakeHome con uso documentato dell'IA, la valutazione assume come riferimento una articolazione complessiva su 100 punti coerente con il template normativo del corso.

La rubrica valuta non soltanto il risultato finale, ma anche la qualità del processo mediante il quale lo studente trasferisce autonomamente il metodo sviluppato nel Caso Aula al nuovo problema First Republic.

| Area | Peso | Criteri principali |
|---|---:|---|
| Prompt 2 — Flusso logico-teorico risolutivo | 30 | contributo iniziale dello studente; riconoscimento della nuova struttura ALM; corretto ruolo di $\alpha$, $\beta$ e $\phi$; presenza del vincolo legacy; ordine teorico; collegamento tra teoria, output e controlli |
| Prompt 3 — Scomposizione input-output | 15 | proposta operativa iniziale dello studente; coerenza delle tappe con il Flusso; corretta sequenza benchmark → legacy → sensitività → scenari; collegamento input-output; corretto regime IA attribuito alle tappe |
| Notebook Jupyter e output computazionali | 20 | correttezza della forma solver; soluzione benchmark; funzione parametrica; sensitività; confronto $\alpha$–$\beta$; scenario analysis; tabelle e grafici richiesti; riproducibilità |
| Prompt di tappa e uso dei Regimi A/B; eventuale Regime C | 15 | qualità e specificità dei prompt; rispetto degli input disponibili; uso appropriato dei Regimi A e B; autonomia rispetto al Caso Aula; eventuale Regime C attivato solo su criticità specifica |
| Verifiche logiche e controlli numerici | 15 | residuali; slack; bounds; fattibilità; vincolo prudenziale; vincolo legacy; limite su $x_5$; funding; marginale legacy; controlli parametrici; uso esclusivo di risultati validi |
| Interpretazione finanziaria finale | 5 | autonomia; coerenza con gli output; ruolo del timing, della rigidità legacy e della capacità di funding; consapevolezza dei limiti del modello |

**Totale: 100 punti.**

### 14.1 Prompt 2 — Flusso logico-teorico risolutivo — 30 punti

La valutazione deve considerare:

1. qualità del contributo iniziale dello studente;

2. capacità di riconoscere che il TakeHome non costituisce una semplice replica del Caso Aula;

3. corretta identificazione di:

$$
x_1,\ldots,x_5;
$$

4. corretta identificazione della doppia ondata di fabbisogno;

5. corretta distinzione tra:

$$
\alpha
\qquad\text{e}\qquad
\beta;
$$

6. corretta identificazione del ruolo di:

$$
\phi;
$$

7. riconoscimento del vincolo legacy:

$$
x_3+x_4\geq35;
$$

8. riconoscimento del limite:

$$
x_5\leq35;
$$

9. corretta collocazione teorica della verifica del marginale legacy;

10. corretto ordine tra:
   - benchmark;
   - verifica del vincolo legacy;
   - funzione parametrica;
   - sensitività ad $\alpha$;
   - sensitività a $\beta$;
   - confronto $\alpha$–$\beta$;
   - sensitività a $\phi$;
   - scenario analysis;

11. collegamento esplicito tra teoria, output e controlli;

12. assenza di anticipazioni improprie di codice in Regime A.

Una proposta iniziale scarsamente autonoma, pur successivamente corretta dall'IA, deve incidere sulla valutazione di questa area.

### 14.2 Prompt 3 — Scomposizione input-output — 15 punti

La valutazione deve considerare:

1. qualità della proposta operativa iniziale dello studente;

2. derivazione delle tappe dal Flusso logico-teorico validato;

3. presenza, per ogni tappa, di:
   - obiettivo;
   - input;
   - oggetti teorici;
   - operazione;
   - output;
   - controllo;
   - uso successivo;

4. corretta distinzione dei Regimi A e B;

5. corretta collocazione della ricognizione iniziale del nuovo problema;

6. presenza di una tappa autonoma per il vincolo legacy e il relativo marginale;

7. sviluppo separato delle sensitività ad $\alpha$ e a $\beta$ prima del loro confronto;

8. collocazione della sensitività a $\phi$ dopo il confronto prima/seconda ondata;

9. distinzione tra sensitività univariate e scenario analysis;

10. copertura integrale degli output e dei controlli richiesti dalla Scheda Caso.

### 14.3 Notebook Jupyter e output computazionali — 20 punti

La valutazione deve considerare:

1. corretta costruzione del vettore decisionale;

2. corretta costruzione del vettore obiettivo;

3. corretta costruzione di:

$$
A_{\mathrm{eq}},
\qquad
b_{\mathrm{eq}},
\qquad
A_{\mathrm{ub}},
\qquad
b_{\mathrm{ub}};
$$

4. corretta definizione dei bounds;

5. corretta trasformazione:

$$
\max\Pi
\quad\longleftrightarrow\quad
\min F=-\Pi;
$$

6. corretta soluzione del benchmark;

7. corretta costruzione della funzione:

$$
d(\alpha,\beta)
=
(32\alpha,18,14,32\beta)';
$$

8. corretta parametrizzazione:

$$
\bar u_t(\phi)
=
\phi\bar u_t;
$$

9. mantenimento invariato del costo del funding;

10. corretta implementazione del vincolo legacy;

11. corretta implementazione del limite:

$$
x_5\leq35;
$$

12. corretta costruzione delle sensitività ad $\alpha$, $\beta$ e $\phi$;

13. corretto confronto $\alpha$–$\beta$;

14. corretta implementazione dei tre scenari;

15. completezza delle tabelle richieste;

16. completezza dei grafici richiesti;

17. uso esclusivo di risultati solver validi;

18. assenza di valori della soluzione inseriti manualmente nelle celle successive;

19. coerenza tra Markdown, codice e output;

20. riproducibilità mediante riesecuzione sequenziale del notebook.

### 14.4 Prompt di tappa e uso dei Regimi IA — 15 punti

La valutazione deve considerare:

1. specificità dei prompt rispetto alla tappa;

2. corretta indicazione degli input disponibili;

3. corretta indicazione dell'output richiesto;

4. presenza del controllo da eseguire;

5. collegamento con la tappa successiva;

6. uso del Regime A per ricognizione teorica, confronto e interpretazione locale;

7. uso del Regime B per traduzione in codice di strutture già definite;

8. assenza di delega all'IA della riformulazione completa del TakeHome;

9. assenza di trasformazione automatica del notebook Aula;

10. capacità dello studente di verificare, accettare, correggere o respingere le risposte IA;

11. coerenza tra tracciato IA e notebook finale.

Il Regime C non è obbligatorio.

Quando presente, deve essere valutato soltanto se:

1. parte da una criticità specifica già individuata dallo studente;

2. riguarda una cella, formula, output o controllo preciso;

3. conduce alla classificazione:

   - **criticità respinta**;

   oppure:

   - **criticità accolta**;

4. non si trasforma in una revisione generica dell'intero notebook.

L'assenza di un Prompt C non comporta penalizzazione.

### 14.5 Verifiche logiche e controlli numerici — 15 punti

La valutazione deve considerare almeno:

1. verifica dello stato del solver;

2. verifica dei bilanci temporali;

3. residuali prossimi a zero entro una tolleranza dichiarata;

4. verifica del vincolo prudenziale:

$$
\ell'x^*\leq7.5;
$$

5. verifica del vincolo legacy:

$$
x_3^*+x_4^*\geq35;
$$

6. verifica del limite:

$$
x_5^*\leq35;
$$

7. verifica dei bounds del funding:

$$
0\leq u_t^*\leq\phi\bar u_t;
$$

8. verifica della non negatività;

9. coerenza tra slack e stato attivo dei vincoli;

10. corretta identificazione dei bounds attivi;

11. corretta gestione della relazione:

$$
F=-\Pi,
\qquad
b=-L,
$$

12. corretta interpretazione:

$$
\frac{\partial\Pi^*}{\partial L}
=
m,
$$

senza applicare un ulteriore cambio di segno;

13. verifica perturbativa del marginale legacy quando localmente informativo;

14. controllo che $\alpha$ modifichi esclusivamente la prima data;

15. controllo che $\beta$ modifichi esclusivamente la quarta data;

16. controllo che $\phi$ modifichi esclusivamente la capacità di funding;

17. controllo che il costo del funding resti invariato;

18. verifica che nelle sensitività vari un solo parametro alla volta;

19. verifica delle configurazioni di scenario assegnate;

20. esclusione dall'analisi di configurazioni non ammissibili.

### 14.6 Interpretazione finanziaria finale — 5 punti

L'interpretazione finale deve essere valutata rispetto a:

1. coerenza con i risultati numericamente validati;

2. capacità di collegare:

$$
\Pi^*
$$

alla composizione dell'attivo, alle giacenze e al funding;

3. discussione del ruolo del vincolo legacy;

4. discussione del limite su $x_5$ quando economicamente rilevante;

5. confronto tra shock alla prima data e shock terminale;

6. discussione della capacità di funding;

7. collegamento tra cambiamenti della soluzione e cambiamenti dei vincoli attivi;

8. confronto tra Standard, Mediamente critico e Critico;

9. richiamo dei limiti del modello;

10. distinzione tra risultati del modello stilizzato e ricostruzione storica di First Republic Bank.

La qualità dell'interpretazione deve essere valutata sulla coerenza e sull'autonomia, non sulla lunghezza del testo.

### 14.7 Errori sostanziali

Devono incidere significativamente sulla valutazione:

1. trattamento del TakeHome come copia del Caso Aula;

2. modifica non autorizzata della Scheda Caso;

3. errore nella forma solver;

4. omissione o errata codifica del vincolo legacy;

5. errore nell'interpretazione del relativo marginale;

6. applicazione di un cambio di segno aggiuntivo non corretto;

7. confusione tra $\alpha$ e $\beta$;

8. applicazione dei due parametri alla data errata;

9. errata applicazione di $\phi$;

10. modifica del costo del funding;

11. omissione del rimborso del funding;

12. mancata verifica del limite su $x_5$;

13. utilizzo di risultati provenienti da configurazioni non ammissibili;

14. assenza dei controlli essenziali;

15. confusione tra sensitività e scenario analysis;

16. confronto $\alpha$–$\beta$ ottenuto facendo variare simultaneamente entrambi;

17. notebook non riproducibile;

18. delega all'IA dell'intera soluzione;

19. delega all'IA dell'interpretazione finanziaria finale;

20. attribuzione di significato storico ai parametri stilizzati.

### 14.8 Criterio complessivo

Una soluzione numericamente corretta non è sufficiente, da sola, per ottenere una valutazione elevata.

La valutazione complessiva deve riflettere la capacità dello studente di costruire autonomamente la catena:

$$
\text{ricognizione}
\longrightarrow
\text{Flusso teorico}
\longrightarrow
\text{tappe}
\longrightarrow
\text{codice}
\longrightarrow
\text{output}
\longrightarrow
\text{controlli}
\longrightarrow
\text{interpretazione}.
$$

L'uso dell'IA costituisce parte del processo valutato, ma non sostituisce la responsabilità teorica, computazionale e interpretativa dello studente.


## 15. Esito atteso e calibrazione qualitativa del caso

### 15.1 Esito atteso

Se il caso è correttamente costruito e risolto, deve emergere in modo osservabile che il trasferimento del metodo dal Caso Aula richiede una vera riformulazione del problema e non una semplice sostituzione di coefficienti.

Lo studente deve poter ricostruire la catena:

$$
\text{nuova struttura ALM}
\longrightarrow
\text{nuova forma solver}
\longrightarrow
\text{nuovi vincoli rilevanti}
\longrightarrow
\text{nuove sensitività}
\longrightarrow
\text{nuova interpretazione}.
$$

Il caso deve inoltre rendere evidente che la posizione temporale di un fabbisogno è parte integrante del problema.

In particolare, uno shock alla prima data e uno shock alla data terminale non devono essere interpretati come variazioni equivalenti della stessa quantità aggregata.

### 15.2 Relazioni qualitative attese

Gli output devono rendere osservabili almeno le seguenti relazioni.

1. Un aumento di $\alpha$ deve aumentare la pressione di liquidità alla prima data.

2. Un aumento di $\beta$ deve aumentare la pressione di liquidità alla quarta data.

3. Gli effetti prodotti da $\alpha$ e $\beta$ possono differire anche quando i due parametri subiscono la stessa variazione relativa.

4. Le differenze fra prima e seconda ondata devono poter emergere attraverso:
   - valore ottimo;
   - composizione dell'attivo;
   - giacenze;
   - funding;
   - vincoli attivi.

5. Una riduzione di $\phi$ deve ridurre la capacità disponibile di funding e può costringere il modello a una diversa ricomposizione dell'attivo.

6. Il vincolo legacy:

$$
x_3+x_4\geq35
$$

deve limitare la flessibilità di ristrutturazione del portafoglio.

7. Il limite:

$$
x_5\leq35
$$

deve essere concettualmente distinto dal vincolo legacy e deve essere interpretato separatamente.

8. I cambiamenti del valore ottimo non devono essere letti separatamente dai cambiamenti nella composizione della soluzione.

9. I cambiamenti della soluzione devono essere messi in relazione con l'eventuale variazione dei vincoli e dei bounds attivi.

10. Gli scenari congiunti devono fornire una lettura diversa da quella ottenuta attraverso le singole sensitività univariate.

### 15.3 Funzione didattica del vincolo legacy

Il vincolo:

$$
x_3+x_4\geq35
$$

deve svolgere una funzione didattica specifica.

Deve consentire allo studente di comprendere che un portafoglio può non essere liberamente ristrutturabile anche quando il problema è formulato in termini lineari.

La presenza di attività legacy deve rendere osservabile che:

1. alcune quote dell'attivo restano strutturalmente vincolate;

2. lo spazio delle soluzioni ammissibili si restringe;

3. la risposta agli shock può risultare meno flessibile;

4. il valore marginale del vincolo può acquisire significato economico quando esso è attivo.

L'interpretazione del marginale deve restare coerente con la relazione:

$$
\frac{\partial\Pi^*}{\partial L}
=
m,
$$

quando:

$$
x_3+x_4\geq L,
$$

$$
F=-\Pi,
$$

$$
b=-L,
$$

e:

$$
m
=
\frac{\partial F^*}{\partial b}.
$$

### 15.4 Funzione didattica del confronto $\alpha$–$\beta$

Il confronto fra prima e seconda ondata deve consentire di osservare che:

$$
\text{stesso aumento relativo del fabbisogno}
$$

non implica necessariamente:

$$
\text{stesso effetto economico}.
$$

La differenza deve poter essere ricondotta alla struttura temporale del modello.

In particolare, uno shock iniziale può incidere su:

1. capacità di coprire i fabbisogni immediati;

2. giacenze disponibili nelle date successive;

3. ricorso anticipato al funding;

4. composizione dell'attivo scelta ex ante.

Uno shock terminale può invece interagire diversamente con:

1. cash flow accumulati nelle date precedenti;

2. giacenze già costruite;

3. rimborsi del funding;

4. struttura residua del portafoglio.

Il caso deve quindi rendere osservabile la differenza tra:

$$
\text{liquidità aggregata}
$$

e:

$$
\text{liquidità disponibile alla data necessaria}.
$$

### 15.5 Funzione didattica della sensitività a $\phi$

La sensitività rispetto a:

$$
\phi
$$

deve consentire di distinguere:

$$
\text{capacità disponibile di funding}
$$

da:

$$
\text{funding effettivamente utilizzato}.
$$

Una maggiore capacità non implica necessariamente un maggiore utilizzo.

Una minore capacità può invece diventare economicamente rilevante quando il bound:

$$
u_t\leq\phi\bar u_t
$$

diventa attivo o prossimo all'attivazione.

Il caso deve quindi consentire di osservare regioni in cui:

1. la capacità è scarsa;

2. la capacità è sufficiente ma utilizzata solo in parte;

3. ulteriore capacità non produce benefici marginali rilevanti.

### 15.6 Funzione didattica degli scenari

Gli scenari Standard, Mediamente critico e Critico devono consentire di osservare gli effetti congiunti di:

1. maggiore pressione alla prima data;

2. maggiore pressione alla quarta data;

3. minore capacità di funding.

Gli scenari devono essere interpretati come configurazioni deterministiche assegnate.

Non devono essere interpretati come:

- scenari probabilistici;
- quantili;
- realizzazioni casuali;
- previsioni storiche.

La loro funzione è mostrare come più driver possano agire simultaneamente sul piano ALM.

### 15.7 Relazioni che non devono essere imposte artificialmente

La calibrazione non deve imporre a priori:

1. simmetria fra effetti di $\alpha$ e $\beta$;

2. monotonicità perfetta di tutte le variabili decisionali;

3. saturazione permanente del funding;

4. attivazione permanente del vincolo legacy;

5. attivazione permanente del limite su $x_5$;

6. un ordine prestabilito delle componenti dell'asset allocation;

7. linearità globale delle risposte lungo le griglie;

8. un determinato marginale come economicamente dominante in tutte le configurazioni;

9. differenze artificialmente elevate fra scenari.

Le proprietà devono emergere dal modello e dalla calibrazione.

### 15.8 Possibili segnali di cattiva calibrazione

Costituiscono segnali di possibile cattiva calibrazione:

1. benchmark non ammissibile;

2. vincolo legacy completamente irrilevante in tutte le configurazioni;

3. vincolo legacy sempre dominante in modo triviale;

4. limite su $x_5$ privo di qualsiasi ruolo;

5. sensitività ad $\alpha$ e a $\beta$ praticamente indistinguibili;

6. sensitività a $\phi$ priva di qualsiasi effetto;

7. composizione dell'attivo invariata lungo tutte le griglie;

8. funding sempre nullo o sempre completamente saturato senza variazioni informative;

9. scenari quasi indistinguibili dal benchmark;

10. scenario Critico eccessivamente estremo o non interpretabile;

11. risultati dominati da artefatti numerici;

12. impossibilità di collegare i cambiamenti della soluzione ai vincoli attivi;

13. notebook ottenibile mediante copia meccanica del Caso Aula;

14. assenza di una vera differenza didattica tra Aula e TakeHome.

### 15.9 Criterio qualitativo finale

La calibrazione è considerata soddisfacente se il caso consente allo studente di osservare con chiarezza che:

$$
\text{timing dei fabbisogni},
$$

$$
\text{rigidità legacy},
$$

e:

$$
\text{capacità di funding}
$$

interagiscono nel determinare:

$$
\text{asset allocation},
\qquad
\text{giacenze},
\qquad
\text{funding},
\qquad
\text{valore ottimo}.
$$

Il caso deve inoltre rendere evidente che:

$$
\text{trasferire un metodo}
\neq
\text{copiare una soluzione}.
$$

Il TakeHome è qualitativamente ben calibrato se risulta:

1. numericamente stabile;

2. non banale;

3. economicamente interpretabile;

4. autonomo rispetto al Caso Aula;

5. coerente con i Capitoli 11 e 12;

6. coerente con la funzione computazionale della Lezione 13;

7. sufficientemente ricco da richiedere riformulazione e controllo autonomi;

8. sufficientemente delimitato da non anticipare i modelli stocastici delle lezioni successive.

## 16. Relazione con l'altro caso della lezione

Il Caso TakeHome First Republic Bank e il Caso Aula Silicon Valley Bank devono essere metodologicamente comparabili, ma strutturalmente distinti.

La relazione tra i due casi deve mostrare che lo studente è chiamato a trasferire un metodo già appreso a una nuova configurazione ALM.

### 16.1 Concetti teorici comuni

I due casi condividono i seguenti concetti:

1. formulazione di un problema di programmazione lineare;

2. distinzione tra:
   - funzione obiettivo;
   - uguaglianze;
   - disuguaglianze;
   - bounds;

3. rappresentazione temporale dei cash flow degli attivi;

4. bilanci multiperiodali di liquidità;

5. utilizzo di giacenze trasferite tra date successive;

6. utilizzo di funding esterno e relativo rimborso;

7. fattibilità del piano ALM;

8. residuali dei vincoli di uguaglianza;

9. slack dei vincoli di disuguaglianza;

10. vincoli e bounds attivi;

11. valori marginali e loro interpretazione locale;

12. analisi di sensitività;

13. cambiamenti della soluzione ottima al variare dei parametri;

14. scenario analysis deterministica;

15. distinzione tra risultati del modello e interpretazione del caso storico.

### 16.2 Strumenti computazionali comuni

Entrambi i casi utilizzano:

1. Python in ambiente Jupyter / VS Code;

2. `scipy.optimize.linprog`;

3. costruzione esplicita di:
   - vettore della funzione obiettivo;
   - $A_{\mathrm{eq}}$;
   - $b_{\mathrm{eq}}$;
   - $A_{\mathrm{ub}}$;
   - $b_{\mathrm{ub}}$;
   - bounds;

4. funzioni solver parametrizzate;

5. DataFrame per organizzare le analisi;

6. grafici prodotti a partire dagli output del solver;

7. controlli su residuali, slack e bounds;

8. lettura dei valori marginali restituiti dal solver;

9. verifica dello stato del solver prima dell'utilizzo dei risultati;

10. riesecuzione sequenziale e riproducibile del notebook.

### 16.3 Struttura metodologica comune

La struttura metodologica dei due casi deve essere:

$$
\text{Scheda Caso}
\longrightarrow
\text{Flusso logico-teorico}
\longrightarrow
\text{scomposizione in tappe}
\longrightarrow
\text{notebook}
$$

$$
\longrightarrow
\text{output}
\longrightarrow
\text{controlli}
\longrightarrow
\text{interpretazione finale}.
$$

Anche il protocollo IA mantiene la stessa struttura:

$$
\text{Prompt zero}
\longrightarrow
\text{Prompt 1}
\longrightarrow
\text{Prompt 2}
\longrightarrow
\text{Prompt 3}
\longrightarrow
\text{prompt di tappa}.
$$

L'eventuale Regime C resta subordinato, in entrambi i casi, all'individuazione di una criticità specifica da parte dello studente.

### 16.4 Differenze strutturali rispetto al Caso Aula

Il Caso TakeHome deve essere autonomo rispetto al Caso Aula almeno nelle seguenti dimensioni.

#### Numero e composizione delle classi di attivo

Nel Caso Aula SVB:

- quattro classi di attivo.

Nel Caso TakeHome First Republic:

- cinque classi di attivo;
- maggiore articolazione delle attività creditizie;
- presenza di una struttura legacy più esplicita.

#### Struttura dei fabbisogni

Nel Caso Aula lo stress principale è rappresentato da:

$$
\theta,
$$

che modifica i fabbisogni delle prime due date.

Nel Caso TakeHome sono presenti due driver distinti:

$$
\alpha
$$

per la prima data e:

$$
\beta
$$

per la quarta data.

Il TakeHome deve quindi consentire un confronto diretto tra:

$$
\text{shock iniziale}
\qquad\text{e}\qquad
\text{shock terminale}.
$$

#### Struttura dei vincoli

Nel Caso Aula compare il limite:

$$
x_3\leq30.
$$

Nel Caso TakeHome compaiono:

$$
x_3+x_4\geq35
$$

e:

$$
x_5\leq35.
$$

Il primo introduce una rigidità legacy che deve essere trattata esplicitamente anche nella forma solver.

#### Driver parametrici

Nel Caso Aula:

$$
(\theta,\phi,\psi)
$$

consentono di analizzare:

1. aumento dei fabbisogni;
2. capacità di funding;
3. costo del funding.

Nel Caso TakeHome:

$$
(\alpha,\beta,\phi)
$$

consentono di analizzare:

1. prima ondata di fabbisogno;
2. seconda ondata di fabbisogno;
3. capacità di funding.

Il costo del funding resta invariato.

### 16.5 Differenze negli output interpretativi

Nel Caso Aula assumono particolare rilievo:

1. frontiera di fattibilità rispetto a $\theta$;

2. ruolo congiunto di fabbisogni, capacità e costo del funding;

3. variazione dei vincoli attivi lungo le tre sensitività.

Nel Caso TakeHome assumono particolare rilievo:

1. confronto tra effetti di $\alpha$ e $\beta$;

2. ruolo del timing dei fabbisogni;

3. ruolo del vincolo legacy;

4. interazione tra rigidità del portafoglio e capacità di funding;

5. trasferimento autonomo del metodo a una nuova struttura.

### 16.6 Differenza della responsabilità didattica

Nel Caso Aula il docente:

1. guida maggiormente la lettura del problema;

2. accompagna la costruzione della forma solver;

3. discute gli errori tipici;

4. orienta l'interpretazione dei principali output.

Nel Caso TakeHome lo studente deve invece assumere maggiore responsabilità nella:

1. ricognizione del nuovo problema;

2. individuazione delle differenze rispetto al Caso Aula;

3. costruzione della nuova forma solver;

4. gestione autonoma del vincolo legacy;

5. distinzione tra prima e seconda ondata;

6. selezione dei controlli pertinenti;

7. interpretazione finale.

### 16.7 Ruolo dell'IA nei due casi

Nel Caso Aula l'IA può supportare un processo maggiormente guidato.

Nel Caso TakeHome deve risultare particolarmente evidente che l'IA non sostituisce il trasferimento metodologico dello studente.

L'IA non deve:

1. trasformare automaticamente il notebook Aula nel notebook TakeHome;

2. limitarsi a sostituire coefficienti;

3. decidere autonomamente quali elementi del modello modificare;

4. eliminare o alterare il vincolo legacy;

5. introdurre parametri non previsti;

6. importare automaticamente nel TakeHome analisi specifiche del Caso Aula che non siano richieste.

Lo studente deve mostrare di saper distinguere:

$$
\text{ciò che è trasferibile}
$$

da:

$$
\text{ciò che deve essere riformulato}.
$$

### 16.8 Elementi trasferibili dal Caso Aula

Sono trasferibili:

1. struttura generale di un problema PL;

2. logica di costruzione delle matrici;

3. uso di `linprog`;

4. controllo di residuali e slack;

5. distinzione tra vincoli e bounds;

6. lettura dei valori marginali;

7. costruzione di una funzione parametrica;

8. organizzazione delle sensitività;

9. costruzione di tabelle e grafici;

10. verifica della riproducibilità.

### 16.9 Elementi da riformulare autonomamente

Devono invece essere riformulati:

1. vettore delle attività;

2. matrice dei cash flow;

3. vettore dei fabbisogni;

4. struttura dei vincoli;

5. vincolo legacy;

6. limite su $x_5$;

7. funzione parametrica in $\alpha$, $\beta$, $\phi$;

8. confronto tra prima e seconda ondata;

9. interpretazione del ruolo temporale degli shock;

10. scenario analysis specifica del TakeHome.

### 16.10 Criterio conclusivo di comparabilità

La coppia di casi è considerata ben costruita se sono contemporaneamente riconoscibili:

$$
\text{metodo comune}
$$

e:

$$
\text{problema finanziario differente}.
$$

Il Caso TakeHome non deve apparire come:

$$
\text{Caso Aula}
+
\text{nuovi coefficienti}.
$$

Deve invece rappresentare:

$$
\text{metodo appreso}
+
\text{riformulazione autonoma}
+
\text{nuova interpretazione}.
$$

La relazione didattica finale deve quindi essere:

$$
\text{Caso Aula SVB:}
\quad
\text{apprendere e consolidare il metodo},
$$

$$
\text{Caso TakeHome First Republic:}
\quad
\text{trasferire autonomamente il metodo}.
$$