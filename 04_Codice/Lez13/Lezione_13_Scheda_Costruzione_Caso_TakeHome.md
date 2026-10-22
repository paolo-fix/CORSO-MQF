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

Il caso deve verificare esplicitamente:

1. la fattibilità numerica della soluzione benchmark;
2. la soddisfazione dei bilanci temporali di liquidità;
3. la coerenza tra residuali numerici e vincoli di uguaglianza;
4. la coerenza tra slack e stato attivo o non attivo delle disuguaglianze;
5. la coerenza tra valori delle variabili e bounds attivi;
6. il rispetto dei limiti di funding:

$$
u_t^*\leq\phi\bar u_t;
$$

7. il rispetto del vincolo prudenziale:

$$
\ell'x^*\leq K;
$$

8. il rispetto del vincolo legacy:

$$
x_3^*+x_4^*\geq35;
$$

9. il rispetto del limite sugli altri prestiti:

$$
x_5^*\leq35;
$$

10. la corretta trasformazione del vincolo legacy da

$$
x_3+x_4\geq35
$$

a

$$
-x_3-x_4\leq-35;
$$

11. la corretta interpretazione del marginale associato al vincolo legacy: il solver restituisce il marginale rispetto al termine noto della disuguaglianza codificata, cioè rispetto a $-35$, e non direttamente rispetto al limite economico $35$;

12. la conseguente ricostruzione del segno quando si interpreta economicamente l'effetto marginale di un aumento del livello minimo richiesto delle attività legacy;

13. la coerenza dei valori marginali con i vincoli e i bilanci ai quali si riferiscono;
14. la corretta distinzione tra configurazioni ammissibili e non ammissibili;
15. la coerenza tra variazioni di $\alpha$, $\beta$ e $\phi$, cambiamenti dei vincoli attivi e modifiche della soluzione ottima;
16. la distinzione tra gli effetti di uno shock alla prima data e quelli di uno shock alla data terminale;
17. la distinzione tra sensitività univariata e variazione congiunta dei driver negli scenari.

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

Gli output devono avere una funzione informativa, diagnostica o interpretativa esplicita e devono restare riconducibili alle quantità teoriche definite nella specifica del caso.

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

7. soluzioni ottime lungo la griglia di $\alpha$;

8. soluzioni ottime lungo la griglia di $\beta$;

9. soluzioni ottime lungo la griglia di $\phi$;

10. variazioni del valore ottimo rispetto al benchmark:

$$
\Delta\Pi^*(p)
=
\Pi^*(p)-\Pi^*(1);
$$

11. variazioni delle componenti della soluzione:

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

12. rapporto di utilizzo della capacità di funding:

$$
\rho_t^u(p)
=
\frac{u_t^*(p)}{\bar u_t(p)};
$$

13. stato di fattibilità per ciascuna configurazione analizzata;

14. stato attivo o non attivo dei principali vincoli nelle diverse configurazioni;

15. comportamento specifico del vincolo legacy:

$$
x_3+x_4\geq35;
$$

16. valori marginali associati ai principali bilanci temporali e ai vincoli economicamente rilevanti;

17. soluzioni ottime nei tre scenari congiunti;

18. perdita di valore di ciascuno scenario rispetto allo scenario Standard.

### Tabelle

Devono essere prodotte almeno le seguenti tabelle.

1. **Tabella benchmark**

   Deve riportare:

   - $x^*$;
   - $g^*$;
   - $u^*$;
   - $\Pi^*$;
   - stato dei principali vincoli;
   - principali residuali;
   - principali slack;
   - bounds attivi;
   - principali valori marginali.

   La funzione della tabella è fornire una sintesi verificabile della soluzione benchmark.

2. **Tabella di sensitività rispetto ad $\alpha$**

   Per ciascun valore della griglia deve riportare almeno:

   - fattibilità;
   - $\Pi^*$;
   - componenti principali di $x^*$;
   - componenti di $u^*$;
   - principali vincoli attivi;
   - valori marginali rilevanti.

   La funzione della tabella è rendere osservabile l'effetto di una variazione del fabbisogno alla prima data.

3. **Tabella di sensitività rispetto a $\beta$**

   Deve riportare le stesse tipologie di informazioni della tabella precedente.

   La funzione della tabella è rendere osservabile l'effetto di una variazione del fabbisogno alla data terminale.

4. **Tabella di sensitività rispetto a $\phi$**

   Per ciascun valore della griglia deve riportare almeno:

   - fattibilità;
   - $\Pi^*$;
   - componenti principali di $x^*$;
   - $u_t^*$;
   - rapporto di utilizzo della capacità di funding;
   - principali vincoli attivi;
   - valori marginali rilevanti.

   La funzione della tabella è mostrare come varia il piano ottimo quando cambia la capacità disponibile di funding.

5. **Tabella di confronto degli scenari congiunti**

   Deve confrontare:

   - scenario Standard;
   - scenario Mediamente critico;
   - scenario Critico.

   Per ciascuno scenario devono essere riportati almeno:

   - $(\alpha,\beta,\phi)$;
   - fattibilità;
   - $\Pi^*$;
   - perdita di valore rispetto allo Standard;
   - principali componenti di $x^*$;
   - utilizzo del funding;
   - principali vincoli attivi.

   La funzione della tabella è confrontare configurazioni nelle quali più driver cambiano simultaneamente.

6. **Tabella di controllo del vincolo legacy**

   Deve riportare, almeno per il benchmark e per le configurazioni nelle quali il vincolo risulta economicamente rilevante:

   - valore di $x_3^*+x_4^*$;
   - slack rispetto al limite minimo 35;
   - stato attivo / non attivo;
   - marginale restituito dal solver per la disuguaglianza codificata;
   - marginale reinterpretato rispetto al limite economico originale.

   La funzione della tabella è impedire ambiguità tra il vincolo economico:

$$
x_3+x_4\geq35
$$

   e la forma utilizzata nel solver:

$$
-x_3-x_4\leq-35.
$$

### Grafici

Devono essere prodotti grafici con funzione analitica esplicita.

1. **Valore ottimo al variare di $\alpha$**

   Rappresentare:

$$
\alpha
\longmapsto
\Pi^*(\alpha).
$$

   Il grafico deve rendere visibile il costo economico di una maggiore pressione di liquidità alla prima data.

2. **Valore ottimo al variare di $\beta$**

   Rappresentare:

$$
\beta
\longmapsto
\Pi^*(\beta).
$$

   Il grafico deve permettere il confronto con l'effetto di uno shock iniziale.

3. **Valore ottimo al variare di $\phi$**

   Rappresentare:

$$
\phi
\longmapsto
\Pi^*(\phi).
$$

   Il grafico deve rendere visibile il valore economico della capacità disponibile di funding.

4. **Composizione ottima dell'attivo**

   Rappresentare, per almeno una delle sensitività economicamente più informative, l'evoluzione delle componenti:

$$
x_j^*(p).
$$

   Il grafico deve mostrare come cambia la composizione del portafoglio al variare del parametro.

5. **Utilizzo della capacità di funding**

   Rappresentare:

$$
\rho_t^u(p)
=
\frac{u_t^*(p)}{\bar u_t(p)}
$$

   lungo la sensitività rispetto a $\phi$.

   Il grafico deve consentire di individuare date nelle quali la capacità disponibile diventa vincolante.

6. **Confronto tra prima e seconda ondata di deflussi**

   Deve mettere a confronto, in una rappresentazione coerente, la risposta del valore ottimo e/o delle principali componenti della soluzione alle variazioni di $\alpha$ e $\beta$.

   La funzione del grafico è rendere osservabile che uno shock alla prima data e uno shock alla data terminale possono produrre effetti diversi sul piano ALM.

I grafici devono essere prodotti come output delle rispettive celle del notebook e devono essere rigenerabili mediante riesecuzione delle celle.

Non è richiesta automaticamente l'esportazione in file esterni.

### Controlli

Devono essere previsti ed eseguiti almeno i seguenti controlli.

#### Controlli numerici

1. verifica dei residuali dei vincoli di uguaglianza;

2. verifica degli slack delle disuguaglianze;

3. verifica dei bounds attivi;

4. controllo del rispetto del vincolo prudenziale:

$$
\ell'x^*\leq7.5;
$$

5. controllo del rispetto del vincolo legacy:

$$
x_3^*+x_4^*\geq35;
$$

6. controllo del rispetto del limite:

$$
x_5^*\leq35;
$$

7. controllo dei limiti di funding:

$$
0\leq u_t^*\leq\phi\bar u_t;
$$

8. controllo della non negatività di tutte le variabili;

9. verifica dello stato di fattibilità per ogni configurazione parametrica e per ogni scenario.

#### Controlli logici e teorici

1. verifica della corretta distinzione tra shock alla prima data, governato da $\alpha$, e shock alla quarta data, governato da $\beta$;

2. verifica che nelle sensitività univariate vari un solo parametro alla volta;

3. verifica che negli scenari congiunti $\alpha$, $\beta$ e $\phi$ assumano simultaneamente i valori assegnati;

4. verifica della coerenza tra slack nullo e identificazione di un vincolo attivo;

5. verifica della coerenza tra variazioni dei parametri, cambiamenti dei vincoli attivi e variazioni della soluzione ottima;

6. verifica della corretta interpretazione economica dei principali valori marginali.

#### Controlli computazionali

1. verifica della corretta costruzione di $A_{\mathrm{eq}}$, $b_{\mathrm{eq}}$, $A_{\mathrm{ub}}$, $b_{\mathrm{ub}}$ e dei bounds;

2. verifica della corretta traduzione della funzione obiettivo nella convenzione utilizzata da `scipy.optimize.linprog`;

3. verifica della corretta codifica del vincolo legacy:

$$
x_3+x_4\geq35
$$

come:

$$
-x_3-x_4\leq-35;
$$

4. verifica che il marginale restituito dal solver per tale riga sia interpretato rispetto al termine noto codificato $-35$;

5. ricostruzione del segno necessario per interpretare economicamente l'effetto marginale di una variazione del limite minimo 35;

6. esclusione dall'analisi economica delle configurazioni per le quali il solver segnala non ammissibilità;

7. verifica che tabelle e grafici siano generati esclusivamente a partire da risultati di esecuzioni valide;

8. verifica della riproducibilità degli output mediante riesecuzione ordinata del notebook.

### Funzione interpretativa degli output

Gli output devono consentire allo studente di discutere, sulla base dei risultati numerici già validati:

1. come la presenza di attività legacy modifica la flessibilità del bilancio;
2. perché una pressione di liquidità iniziale può avere effetti diversi da una pressione terminale;
3. quando la capacità di funding diventa una risorsa scarsa;
4. quali vincoli determinano il piano ottimo nelle diverse configurazioni;
5. come cambiano composizione dell'attivo, funding e valore ottimo nei diversi regimi;
6. quali effetti sono riconducibili alla struttura del modello e quali non possono essere estesi al caso storico reale di First Republic Bank.

L'interpretazione finale resta responsabilità dello studente e non deve essere prodotta automaticamente dall'IA.

## 6. Flusso logico-teorico risolutivo atteso

| Passo | Finalità risolutiva | Formula, definizione, proprietà o teorema | Applicazione nel caso | Output o controllo collegato |
|---:|---|---|---|---|
| 1 | Ricostruire e tradurre il nuovo modello ALM | Struttura del programma lineare e forma matriciale per il solver | Identificare cinque classi di attivo, bilanci temporali, funding, vincolo legacy e bounds | Matrici e vettori con controllo dimensionale |
| 2 | Risolvere e validare il benchmark | Ammissibilità, ottimalità, slack e valori marginali | Risolvere il caso $(\alpha,\beta,\phi)=(1,1,1)$ | Soluzione benchmark, residuali, vincoli attivi e marginals |
| 3 | Parametrizzare i driver di stress | Analisi parametrica di termini noti e bounds | Introdurre $\alpha$, $\beta$ e $\phi$ nella funzione solver | Funzione generale di soluzione validata sul benchmark |
| 4 | Svolgere le sensitività univariate | Comparative statics numerica | Variare separatamente $\alpha$, $\beta$ e $\phi$ sulle griglie assegnate | DataFrame, variazioni della soluzione ottima, vincoli attivi e grafici |
| 5 | Confrontare le due ondate di liquidità | Struttura temporale dei bilanci ALM | Valutare differenze fra stress iniziale e stress terminale | Confronto fra sensitività ad $\alpha$ e a $\beta$ |
| 6 | Confrontare gli scenari e interpretare | Scenario analysis deterministica | Risolvere Standard, Mediamente critico e Critico | Tabella, grafici e interpretazione economico-finanziaria finale |

## 7. Scomposizione attesa in tappe

| Tappa | Regime | Input | Operazione | Output | Controllo | Uso successivo |
|---:|:---:|---|---|---|---|---|
| 1 | A/B | Scheda Caso e modello teorico | Definire ordinamento delle variabili, parametri, matrici e vincolo legacy | Struttura solver completa | Dimensioni, indici, coefficienti e segni | Risoluzione benchmark |
| 2 | B/C | Modello benchmark | Risolvere il LP e costruire la diagnostica | $x^*$, $g^*$, $u^*$, $\Pi^*$, residuali, slack e marginals | Fattibilità, vincoli attivi e verifica di almeno un marginale | Validazione del modello |
| 3 | A/B | Modello validato | Costruire una funzione parametrica in $\alpha$, $\beta$, $\phi$ | Solver parametrico riutilizzabile | Riproduzione del benchmark per $(1,1,1)$ | Analisi parametrica |
| 4 | B | Funzione parametrica e tre griglie | Eseguire le sensitività univariate e costruire tabelle e grafici | Tre DataFrame di sensitività e relativi grafici | Un solo parametro varia alla volta; gestione degli scenari infeasible | Comparative statics |
| 5 | B/C | Risultati delle sensitività | Confrontare prima e seconda ondata e leggere vincoli attivi e valori marginali | Sintesi comparativa delle tre sensitività | Coerenza fra risultati numerici e interpretazione temporale | Scenario analysis |
| 6 | B/C | Tre scenari congiunti | Risolvere e confrontare Standard, Mediamente critico e Critico | Tabella comparativa, grafici e commento finale | Coerenza fra parametri, soluzione ottima, vincoli attivi e interpretazione | Chiusura del caso |

## 8. Mappa tra prompt e notebook

| Prompt | Regime | Tappa | Celle o output prodotti | Decisione o controllo richiesto |
|---:|:---:|---:|---|---|
| 0 | — | — | Inizializzazione della chat | Applicazione delle regole generali |
| 1 | — | — | Cella Markdown iniziale | Fedeltà alla Scheda Caso |
| 2 | A | — | Flusso logico-teorico risolutivo | Correttezza dell'ordine logico |
| 3 | A | — | Scomposizione in tappe | Coerenza input / output / controlli |
| 4 | A/B | 1 | Definizione del modello e vincolo legacy | Ordinamento delle variabili e controllo delle matrici |
| 5 | B/C | 2 | Solver benchmark e diagnostica | Residuali, slack, vincoli attivi e verifica di un marginale |
| 6 | A/B | 3 | Funzione parametrica | Corretta azione di $\alpha$, $\beta$ e $\phi$ |
| 7 | B | 4 | Tre sensitività, DataFrame e grafici | Isolamento corretto dei parametri |
| 8 | B/C | 5 | Confronto delle sensitività | Lettura della diversa collocazione temporale dello stress |
| 9 | B/C | 6 | Scenari e revisione critica finale | Coerenza del confronto multivariato e interpretazione conclusiva |
| 10, solo se necessario | C | trasversale | Correzione mirata di una criticità effettiva | Verifica della correzione |

## 9. Struttura attesa del notebook

1. Cella Markdown iniziale prodotta dal Prompt 1.
2. Cella Markdown con il Flusso logico-teorico risolutivo.
3. Cella Markdown con la scomposizione in tappe.
4. Cella codice per l'importazione delle librerie.
5. Cella codice per la definizione dei parametri benchmark.
6. Cella Markdown con l'ordinamento delle variabili.
7. Cella codice per la costruzione delle matrici e del vincolo legacy.
8. Cella codice per i controlli dimensionali.
9. Cella codice per la soluzione benchmark.
10. Output con stato del solver, valore ottimo e vettori $x^*$, $g^*$, $u^*$.
11. Cella codice per la ricostruzione dei bilanci e dei residuali.
12. Cella codice per slack, bounds attivi e valori marginali.
13. Output con tabella diagnostica.
14. Cella codice per la verifica di almeno un valore marginale mediante perturbazione.
15. Cella Markdown con interpretazione della verifica.
16. Cella Markdown per la definizione di $\alpha$, $\beta$ e $\phi$.
17. Cella codice per la funzione solver parametrica.
18. Cella codice di test della funzione in $(1,1,1)$.
19. Cella codice per la sensitività ad $\alpha$.
20. Output DataFrame e grafici relativi ad $\alpha$.
21. Cella codice per la sensitività a $\beta$.
22. Output DataFrame e grafici relativi a $\beta$.
23. Cella codice per la sensitività a $\phi$.
24. Output DataFrame e grafici relativi a $\phi$.
25. Cella Markdown e output di confronto fra prima e seconda ondata.
26. Cella Markdown con la definizione dei tre scenari.
27. Cella codice per la risoluzione degli scenari.
28. Output con tabella comparativa.
29. Celle codice / output con grafici di scenario.
30. Cella Markdown finale con interpretazione economico-finanziaria e limiti del modello.

Il notebook deve essere eseguibile sequenzialmente dall'inizio alla fine. Tutte le tabelle e tutti i grafici devono derivare dagli oggetti prodotti dal solver. Non devono essere inseriti manualmente valori della soluzione nelle celle successive.

## 10. Calibrazione docente

- **Ordine di grandezza atteso dei risultati:**
  - nel benchmark la soluzione attesa, a tolleranza numerica, è:

    $$
    x^*
    \approx
    (0,\;36.190,\;0,\;35.000,\;28.810)';
    $$

    $$
    g^*
    \approx
    (0,\;1.797,\;6.949,\;4.014)';
    $$

    $$
    u^*
    \approx
    (2.036,\;0,\;0)';
    $$

    $$
    \Pi^*
    \approx
    3.8257;
    $$

  - il vincolo legacy deve risultare attivo:

    $$
    x_3+x_4=35;
    $$

  - il funding viene utilizzato nel primo periodo ma non deve necessariamente saturare la capacità benchmark;
  - la sensitività ad $\alpha$ deve deteriorare progressivamente il valore ottimo e, oltre una certa intensità, portare alla perdita di fattibilità;
  - la sensitività a $\beta$ deve evidenziare un effetto diverso da quello di $\alpha$, perché lo shock interviene nella data terminale;
  - la sensitività a $\phi$ deve mostrare una regione in cui la capacità è scarsa e una regione in cui capacità addizionale non modifica più la soluzione;
  - con la calibrazione corrente, la soglia di fattibilità rispetto ad $\alpha$ è approssimativamente:

    $$
    \alpha_{\mathrm{crit}}
    \simeq
    1.134;
    $$

  - la soglia di fattibilità rispetto a $\beta$ è approssimativamente:

    $$
    \beta_{\mathrm{crit}}
    \simeq
    1.136;
    $$

  - tali soglie sono informazioni interne docente e non devono essere riportate nella Scheda Caso destinata agli studenti;
  - lo scenario Mediamente critico:

    $$
    (\alpha,\beta,\phi)=(1.03,1.03,0.90)
    $$

    deve risultare ammissibile;
  - lo scenario Critico:

    $$
    (\alpha,\beta,\phi)=(1.06,1.06,0.75)
    $$

    deve risultare ancora ammissibile ma con maggiore tensione sulla capacità di funding e una significativa ricomposizione del piano.

- **Errori o ambiguità prevedibili:**
  1. riutilizzare meccanicamente la struttura delle matrici del Caso Aula senza adattarla alle cinque classi di attivo;
  2. dimenticare il vincolo legacy o trasformarlo con segno errato nella forma $A_{\mathrm{ub}}z\leq b_{\mathrm{ub}}$;
  3. applicare $\alpha$ anche ai fabbisogni intermedi;
  4. applicare $\beta$ alla data sbagliata;
  5. confondere la capacità di funding $\phi\bar u_t$ con il funding effettivamente utilizzato;
  6. dimenticare il rimborso del funding alla data successiva;
  7. confondere rendimento dell'attivo e quota di cash flow disponibile;
  8. interpretare come equivalenti uno shock alla prima e uno alla quarta data;
  9. utilizzare `res.x` in configurazioni non ammissibili;
  10. interpretare direttamente i marginals del problema trasformato senza controllo del segno;
  11. confondere scenario analysis e sensitività univariata;
  12. interpretare $\alpha$, $\beta$ e $\phi$ come misure storiche effettive di First Republic.

- **Controlli minimi di validazione:**
  1. verifica delle dimensioni del nuovo vettore delle variabili;
  2. verifica della matrice dei cash flow a cinque colonne;
  3. verifica dei quattro bilanci temporali;
  4. verifica del vincolo legacy;
  5. verifica del limite su $x_5$;
  6. verifica dei bounds sul funding;
  7. coerenza fra slack e vincoli attivi;
  8. verifica numerica di almeno un valore marginale;
  9. test della funzione parametrica nel punto $(1,1,1)$;
  10. verifica che in ciascuna sensitività restino fissi gli altri due parametri;
  11. separazione degli scenari feasible / infeasible prima della costruzione dei grafici;
  12. riproducibilità integrale del notebook.

- **Limiti interpretativi:**
  1. il modello è deterministico;
  2. le due ondate di deflussi sono rappresentate mediante shock esogeni e non mediante comportamento endogeno dei depositanti;
  3. il vincolo legacy è una rappresentazione stilizzata dell'inerzia del bilancio;
  4. non sono modellati fire sales o feedback prezzo-vendita;
  5. non è modellato il mark-to-market endogeno degli attivi;
  6. la capacità di funding è esogena;
  7. il costo del funding è mantenuto fisso nelle analisi principali;
  8. $\alpha$, $\beta$ e $\phi$ non sono variabili casuali;
  9. i tre scenari non hanno probabilità associate;
  10. non si effettua ottimizzazione stocastica;
  11. le decisioni non sono adattive rispetto a informazione progressiva;
  12. le estensioni stocastiche appartengono alle Lezioni 14–16;
  13. i coefficienti numerici non devono essere interpretati come dati storici effettivi di First Republic.

## 11. Uso dell'IA e tracciato

- **Prompt obbligatori:**
  1. Prompt zero;
  2. Prompt 1;
  3. Prompt 2 in Regime A;
  4. Prompt 3 in Regime A;
  5. prompt di tappa coerenti con la scomposizione approvata;
  6. almeno un intervento in Regime C fondato su un dubbio, controllo o anomalia concreta.

- **Numero minimo e massimo di prompt:** indicativamente da 9 a 10 prompt complessivi, inclusi Prompt zero e Prompt 1. Un eventuale prompt aggiuntivo in Regime C è ammesso soltanto se motivato da una criticità effettivamente emersa.

- **Usi ammessi dell'IA:**
  1. verifica della nuova traduzione matriciale;
  2. supporto alla costruzione di codice per una tappa già definita;
  3. controllo di dimensioni, indici e segni;
  4. supporto alla corretta codifica del vincolo legacy;
  5. costruzione della funzione parametrica;
  6. supporto nella gestione dei DataFrame;
  7. costruzione dei grafici richiesti;
  8. spiegazione dell'output del solver;
  9. verifica di residuali, slack e valori marginali;
  10. revisione di codice a seguito di un errore identificato;
  11. controllo della coerenza fra grafici, tabelle e output numerici;
  12. revisione critica dell'interpretazione finale.

- **Usi non ammessi:**
  1. chiedere all'IA di trasformare automaticamente il Caso Aula SVB nel caso First Republic sostituendo soltanto i dati;
  2. chiedere all'IA di risolvere integralmente il caso in un unico prompt;
  3. delegare all'IA la formulazione del modello;
  4. introdurre autonomamente nuovi parametri o scenari;
  5. modificare le griglie assegnate senza motivazione e senza approvazione;
  6. eliminare o modificare il vincolo legacy;
  7. chiedere un notebook completo senza passare attraverso flusso e tappe;
  8. accettare valori marginali o interpretazioni del solver senza controllo;
  9. interpretare automaticamente i grafici senza confronto con tabelle e vincoli;
  10. attribuire valore storico ai parametri stilizzati del caso.

## 12. Valutazione

- **Criteri per il notebook:**
  1. corretta riformulazione del problema rispetto al Caso Aula;
  2. corretta gestione delle cinque classi di attivo;
  3. corretta codifica del vincolo legacy;
  4. correttezza della forma solver;
  5. riproducibilità;
  6. corretta soluzione del benchmark;
  7. presenza dei controlli numerici richiesti;
  8. corretta parametrizzazione di $\alpha$, $\beta$ e $\phi$;
  9. costruzione corretta delle tre sensitività univariate;
  10. qualità e completezza dei DataFrame;
  11. qualità e leggibilità dei grafici;
  12. capacità di distinguere economicamente prima e seconda ondata di stress;
  13. collegamento fra cambiamenti della soluzione e vincoli attivi;
  14. corretta costruzione della scenario analysis;
  15. coerenza fra risultati numerici e interpretazione.

- **Criteri per il tracciato IA:**
  1. contributo autonomo dello studente nei Prompt 2 e 3;
  2. capacità di riconoscere quali elementi del Caso Aula sono trasferibili e quali devono essere riformulati;
  3. distinzione corretta fra Regime A, B e C;
  4. specificità dei prompt di tappa;
  5. esplicitazione di input, output e controlli;
  6. presenza di verifiche critiche e non soltanto richieste di generazione di codice;
  7. uso del Regime C fondato su criticità effettivamente osservate.

- **Peso dei controlli e dell'interpretazione:** nel TakeHome deve essere attribuito un peso maggiore rispetto al Caso Aula alla capacità di trasferire il metodo in una struttura diversa. Non è sufficiente ottenere una soluzione numerica plausibile. La valutazione deve premiare la corretta riformulazione, la verifica del vincolo legacy, la distinzione fra le due ondate di fabbisogno, la lettura dei vincoli attivi e la coerenza fra sensitività, scenari e interpretazione economico-finanziaria.

## 13. Relazione con l'altro caso della lezione

Il Caso TakeHome First Republic è metodologicamente comparabile al Caso Aula SVB perché utilizza:

- programmazione lineare;
- bilanci ALM multiperiodali;
- funding intertemporale;
- slack e vincoli attivi;
- valori marginali;
- sensitività univariate;
- scenario analysis;
- analisi delle variazioni della soluzione ottima.

La struttura finanziaria è però deliberatamente diversa.

Nel Caso Aula SVB:

- vi sono quattro classi di attivo;
- il modello teorico è già noto dal Capitolo 12;
- lo stress principale è concentrato sui fabbisogni iniziali;
- le sensitività riguardano fabbisogno, capacità e costo del funding;
- lo studente parte da un benchmark già noto e lo estende.

Nel Caso TakeHome First Republic:

- vi sono cinque classi di attivo;
- compare un vincolo legacy su attività a lunga durata;
- la crisi di liquidità è rappresentata da due ondate distinte;
- le sensitività distinguono esplicitamente prima e seconda ondata;
- la capacità di funding costituisce il terzo driver;
- lo studente deve costruire e validare autonomamente il nuovo benchmark.

La relazione didattica è quindi:

$$
\text{Caso Aula SVB:}
\quad
\text{implementare}
\longrightarrow
\text{validare}
\longrightarrow
\text{estendere},
$$

$$
\text{Caso TakeHome First Republic:}
\quad
\text{riconoscere}
\longrightarrow
\text{riformulare}
\longrightarrow
\text{trasferire il metodo}.
$$

La comparabilità riguarda gli strumenti quantitativi; la differenza riguarda la struttura economico-finanziaria del problema.
