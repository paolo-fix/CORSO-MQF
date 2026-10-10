# Lezione 16 — Scheda Costruzione Caso TakeHome

Documento interno di progettazione docente.

## 1. Identificazione

- **Lezione:** 16 — Applicazione in Python: programmazione stocastica
- **Tipo di caso:** TakeHome
- **Titolo:** **UK LDI 2022 — Buffer di liquidità, margin call e valore dell'informazione**
- **Target:** studenti del V anno / secondo anno magistrale di Banca e Risk Management
- **Funzione didattica:** trasferire in un contesto finanziario distinto dal Caso Aula SVB la struttura di programmazione stocastica lineare a due stadi sviluppata nei Capitoli 14–15.
- **Framework vincolante:** esclusivamente **two-stage**.

Il caso deve consolidare:

1. decisione here-and-now;
2. scenari discreti e probabilità;
3. ricorso scenario-specifico;
4. forma estesa deterministica;
5. non anticipatività della decisione iniziale;
6. soluzione stocastica SP;
7. soluzione deterministica basata sui valori medi EV e sua rivalutazione negli scenari originari;
8. benchmark wait-and-see WS;
9. Value of the Stochastic Solution (VSS);
10. Expected Value of Perfect Information (EVPI).

Il caso non introduce un modello multistadio. Anche se l'episodio storico del 2022 si è sviluppato nel tempo, nel modello didattico l'incertezza futura è compressa in uno scenario completo osservato in un unico momento di ricorso.

---

## 2. Contesto e motivazione

### 2.1 Contesto storico-finanziario

Nel settembre 2022 il rapido aumento dei rendimenti dei gilt britannici a lunga scadenza produsse forti perdite di valore sulle posizioni utilizzate nelle strategie Liability-Driven Investment (LDI) e generò ingenti richieste di margine e collateral call su repo e derivati. In diversi casi i fondi LDI dovettero mobilizzare attività liquide, richiedere nuovi apporti ai fondi pensione investitori e vendere gilt in condizioni di mercato deteriorate. Le vendite forzate contribuirono ad amplificare la disfunzione del mercato, inducendo l'intervento temporaneo della Bank of England.

Il caso utilizza questo episodio come **cornice storica**. Non costituisce una ricostruzione empirica di uno specifico fondo pensione o fondo LDI.

### 2.2 Motivazione didattica

Il contesto LDI consente di trasferire la logica della programmazione stocastica a due stadi dal bilancio bancario del Caso Aula a un soggetto istituzionale diverso.

La tensione economica centrale è:

> quanto rendimento corrente conviene sacrificare ex ante per detenere un buffer di liquidità e collateral capace di assorbire margin call future, evitando apporti straordinari e vendite forzate costose?

La decisione iniziale riguarda la quota del portafoglio mantenuta come buffer immediatamente disponibile. Dopo l'osservazione dello scenario, il decisore può reagire mediante ricorso scenario-specifico.

Il caso deve rendere visibile che:

- una strategia costruita sullo scenario medio può sottostimare il costo degli scenari di stress;
- il modello stocastico sceglie una sola decisione iniziale, comune a tutti gli scenari;
- il ricorso può invece differire dopo la rivelazione dello scenario;
- il valore della soluzione stocastica e il valore dell'informazione perfetta misurano vantaggi economici distinti.

### 2.3 Riferimenti storici per il docente

Per il solo inquadramento storico utilizzare prioritariamente fonti ufficiali Bank of England e BIS relative alla crisi LDI del 2022, in particolare:

- Bank of England, *Financial Stability Report*, December 2022;
- Bank of England, *Financial Policy Summary and Record*, October 2022;
- Bank of England, materiali successivi sulla resilienza dei fondi LDI;
- Bank for International Settlements / BCBS, documenti sul periodo di stress LDI.

I valori numerici del modello seguente sono **dati didattici stilizzati** costruiti per rendere trasparente il trade-off rendimento–liquidità–ricorso. Non devono essere presentati come stime storiche.

---

## 3. Domanda quantitativa e obiettivo didattico

### 3.1 Domanda quantitativa

Un investitore istituzionale che utilizza una strategia LDI deve decidere al tempo iniziale quanta parte di un patrimonio normalizzato mantenere come buffer immediatamente disponibile e quanta lasciare investita in attività a maggiore rendimento.

La domanda quantitativa è:

> quale composizione iniziale massimizza il risultato economico atteso quando l'entità delle future margin call e il costo delle azioni di emergenza dipendono dallo scenario?

Una volta determinata la soluzione stocastica, occorre misurare:

1. il costo di scegliere il buffer sulla base dei valori medi anziché dell'intera distribuzione degli scenari;
2. il valore economico della conoscenza perfetta dello scenario futuro.

### 3.2 Obiettivo didattico

Lo studente deve saper:

1. distinguere la decisione iniziale dalle decisioni di ricorso;
2. costruire la forma estesa di un programma lineare stocastico a due stadi;
3. tradurre il modello in una forma risolvibile con `scipy.optimize.linprog(method="highs")`;
4. determinare SP, EV e WS;
5. valutare correttamente la decisione $x^{EV}$ negli scenari originari;
6. calcolare e interpretare VSS ed EVPI;
7. verificare fattibilità, bilanci, bounds e ordinamento dei benchmark;
8. interpretare gli output senza estendere le conclusioni oltre il modello.

---

## 4. Specifica teorico-matematica

### 4.1 Scala e decisione di primo stadio

Il patrimonio iniziale è normalizzato a

$$
A_0=100.
$$

La decisione iniziale è

$$
x=(x_1,x_2)'.
$$

Le componenti sono:

| Variabile | Significato | Coefficiente economico |
|---|---|---:|
| $x_1$ | buffer immediatamente disponibile per collateral e margin call | $c_1=0.015$ |
| $x_2$ | portafoglio investito non mantenuto come buffer immediato | $c_2=0.050$ |

Il vincolo iniziale è

$$
x_1+x_2=100,
\qquad
x_1,x_2\geq0.
$$

Il contributo economico di primo stadio è

$$
c'x=0.015x_1+0.050x_2.
$$

La differenza tra i coefficienti rappresenta il costo opportunità di mantenere risorse nel buffer anziché nel portafoglio investito.

### 4.2 Scenari

L'insieme degli scenari è

$$
\mathcal S=\{N,S,E\},
$$

con:

- $N$: condizioni ordinarie;
- $S$: tensione di mercato;
- $E$: shock estremo sui gilt.

Le probabilità sono:

| Scenario | $p_s$ |
|---|---:|
| $N$ | 0.65 |
| $S$ | 0.30 |
| $E$ | 0.05 |

Deve essere verificato

$$
\sum_{s\in\mathcal S}p_s=1.
$$

### 4.3 Margin call scenario-specifica

La richiesta di liquidità/collateral nello scenario $s$ è indicata con

$$
m_s.
$$

I valori assegnati sono:

| Scenario | $m_s$ |
|---|---:|
| $N$ | 10 |
| $S$ | 25 |
| $E$ | 45 |

La quantità $m_s$ rappresenta un fabbisogno aggregato al secondo stadio. Non descrive la sequenza temporale delle margin call effettivamente osservate nel 2022.

### 4.4 Decisioni di secondo stadio

Dopo l'osservazione dello scenario, il decisore può utilizzare:

$$
y_s=(g_s,e_s,f_s)',
$$

dove:

- $g_s\geq0$: liquidità residua dopo il soddisfacimento della margin call;
- $e_s\geq0$: apporto straordinario di collateral/capitale mobilizzato dal fondo pensione o dall'investitore;
- $f_s\geq0$: ammontare nominale di attività del portafoglio vendute in condizioni di stress.

Le decisioni $e_s$, $f_s$ e $g_s$ sono scenario-specifiche e vengono prese dopo l'osservazione dello scenario.

### 4.5 Capacità di apporto straordinario

L'apporto straordinario è limitato da

$$
0\leq e_s\leq\bar e_s,
$$

con:

| Scenario | $\bar e_s$ |
|---|---:|
| $N$ | 5 |
| $S$ | 8 |
| $E$ | 5 |

Il limite rappresenta in forma stilizzata i vincoli operativi e temporali alla mobilizzazione di nuove risorse.

### 4.6 Vendite forzate e coefficiente di conversione in liquidità

Le vendite non possono eccedere il portafoglio investito:

$$
0\leq f_s\leq x_2.
$$

Una unità nominale venduta produce liquidità pari a

$$
\beta_s f_s,
$$

dove:

| Scenario | $\beta_s$ |
|---|---:|
| $N$ | 0.98 |
| $S$ | 0.90 |
| $E$ | 0.75 |

Il coefficiente $\beta_s$ è un **coefficiente di conversione in liquidità**, non un rendimento. La sua riduzione negli scenari peggiori rappresenta la minore efficacia con cui il portafoglio può essere monetizzato rapidamente in condizioni di mercato deteriorate.

### 4.7 Bilancio di liquidità del secondo stadio

Per ogni scenario deve valere

$$
x_1+e_s+\beta_s f_s=m_s+g_s.
$$

Il buffer iniziale $x_1$ è comune a tutti gli scenari. Le variabili di ricorso si adattano invece allo scenario osservato.

### 4.8 Costi economici del ricorso

L'apporto straordinario ha costo economico unitario $\kappa_s$, mentre la vendita forzata ha costo economico unitario $\delta_s$:

| Scenario | $\kappa_s$ | $\delta_s$ |
|---|---:|---:|
| $N$ | 0.08 | 0.15 |
| $S$ | 0.10 | 0.22 |
| $E$ | 0.15 | 0.35 |

Questi coefficienti non devono essere interpretati come semplici tassi di interesse di mercato.

- $\kappa_s e_s$ rappresenta il costo economico complessivo della mobilizzazione straordinaria di collateral/capitale;
- $\delta_s f_s$ rappresenta il costo economico complessivo della vendita forzata, includendo in forma sintetica dislocazione di prezzo, costi di transazione e perdita di capacità di investimento/hedging.

### 4.9 Funzione di ricorso

Per una decisione iniziale $x$, il problema di ricorso nello scenario $s$ è

$$
Q_s(x)
=
\max_{g_s,e_s,f_s}
\left\{
-\kappa_s e_s-\delta_s f_s
\right\}
$$

soggetto a

$$
x_1+e_s+\beta_s f_s=m_s+g_s,
$$

$$
0\leq e_s\leq\bar e_s,
\qquad
0\leq f_s\leq x_2,
\qquad
g_s\geq0.
$$

### 4.10 Programma stocastico SP

Il problema stocastico è

$$
z^{SP}
=
\max_{x_1,x_2,\{y_s\}}
\left\{
0.015x_1+0.050x_2
-
\sum_{s\in\mathcal S}p_s
\left(
\kappa_s e_s+\delta_s f_s
\right)
\right\}
$$

soggetto al vincolo iniziale e ai vincoli di ricorso di tutti gli scenari.

La non anticipatività del primo stadio è incorporata direttamente dalla presenza di un unico vettore $x$, comune a tutti gli scenari.

### 4.11 Ricorso relativamente completo

La calibrazione deve garantire che ogni decisione iniziale ammissibile consenta un ricorso ammissibile in tutti gli scenari.

Nel caso estremo, anche per $x_1=0$ e $x_2=100$, la liquidità massima mobilizzabile è

$$
\bar e_E+\beta_E x_2
=
5+0.75(100)
=80>45=m_E.
$$

La stessa proprietà vale negli altri scenari. Il problema possiede quindi, per la regione ammissibile considerata, ricorso relativamente completo.

### 4.12 Problema Expected Value

Si costruisce il problema deterministico medio utilizzando i coefficienti attesi:

$$
\bar m=\sum_s p_sm_s,
\qquad
\bar\beta=\sum_s p_s\beta_s,
$$

$$
\bar\kappa=\sum_s p_s\kappa_s,
\qquad
\bar\delta=\sum_s p_s\delta_s,
\qquad
\bar e=\sum_s p_s\bar e_s.
$$

Con la calibrazione assegnata:

$$
\bar m=16.25,
\qquad
\bar\beta=0.9445,
$$

$$
\bar\kappa=0.0895,
\qquad
\bar\delta=0.181,
\qquad
\bar e=5.9.
$$

La soluzione iniziale ottima del problema medio è indicata con

$$
x^{EV}.
$$

Il valore ottimo del problema deterministico medio **non** è $z^{EV}$.

Per calcolare $z^{EV}$, si deve fissare

$$
x=x^{EV}
$$

nel problema stocastico originario e riottimizzare esclusivamente il ricorso scenario per scenario.

### 4.13 Wait-and-see

Nel benchmark wait-and-see lo scenario è noto prima della scelta del buffer iniziale. Per ogni scenario si risolve quindi

$$
z_s^{WS}
=
\max_{x_s,y_s}
\left\{
c'x_s-
\kappa_s e_s-
\delta_s f_s
\right\},
$$

con un diverso vettore iniziale $x_s$ per ciascuno scenario.

Il valore atteso è

$$
z^{WS}
=
\sum_s p_s z_s^{WS}.
$$

### 4.14 VSS ed EVPI

Poiché il problema è formulato come massimizzazione:

$$
z^{WS}\geq z^{SP}\geq z^{EV}.
$$

Si definiscono

$$
VSS=z^{SP}-z^{EV}\geq0,
$$

$$
EVPI=z^{WS}-z^{SP}\geq0.
$$

Il VSS misura il valore dell'uso esplicito della distribuzione degli scenari nella decisione iniziale; l'EVPI misura il valore dell'informazione perfetta sullo scenario futuro.

### 4.15 Ipotesi

1. Gli scenari sono mutuamente esclusivi ed esaustivi.
2. Le probabilità sono note al tempo iniziale.
3. Il buffer $x_1$ e il portafoglio investito $x_2$ sono scelti prima dell'osservazione dello scenario.
4. Tutte le variabili di ricorso sono scelte dopo l'osservazione dello scenario completo.
5. Non esistono decisioni intermedie tra il primo e il secondo stadio.
6. Le margin call $m_s$ sono esogene.
7. I coefficienti $\beta_s$, $\kappa_s$, $\delta_s$ e i limiti $\bar e_s$ sono esogeni.
8. I costi di ricorso sono lineari.
9. La vendita forzata è limitata dall'ammontare investito $x_2$.
10. Non vengono modellati endogenamente feedback tra vendite del singolo fondo e prezzi di mercato.
11. Il patrimonio è normalizzato a 100.
12. I dati numerici sono didattici e non costituiscono stime storiche.

---

## 5. Output richiesti

### 5.1 Risultati numerici

1. soluzione $x^{SP}$;
2. valore $z^{SP}$;
3. ricorso ottimo $(g_s,e_s,f_s)$ per ciascuno scenario;
4. costo atteso del ricorso sotto SP;
5. coefficienti del problema medio;
6. soluzione $x^{EV}$;
7. valore ottimo del problema deterministico medio, mantenuto distinto da $z^{EV}$;
8. valore $z^{EV}$ ottenuto rivalutando $x^{EV}$ negli scenari originari;
9. $VSS$;
10. soluzioni $x_s^{WS}$ e valori $z_s^{WS}$;
11. $z^{WS}$;
12. $EVPI$.

### 5.2 Tabelle

**Tabella 1 — Parametri del caso**

Deve riportare probabilità, margin call, coefficienti di conversione in liquidità, limiti di apporto straordinario e costi del ricorso.

**Tabella 2 — Soluzione SP per scenario**

Colonne minime:

- scenario;
- probabilità;
- buffer iniziale $x_1^{SP}$;
- portafoglio investito $x_2^{SP}$;
- margin call $m_s$;
- apporto straordinario $e_s$;
- vendita forzata $f_s$;
- liquidità residua $g_s$;
- costo di ricorso.

**Tabella 3 — Confronto SP vs EV**

Deve confrontare almeno:

- $x_1$ e $x_2$;
- utilizzo dell'apporto straordinario nei tre scenari;
- vendite forzate nei tre scenari;
- valore stocastico della decisione.

**Tabella 4 — Benchmark informativi**

Deve riportare:

- $z^{EV}$;
- $z^{SP}$;
- $z^{WS}$;
- $VSS$;
- $EVPI$.

### 5.3 Grafici

**Figura 1 — Composizione iniziale SP vs EV**

Grafico a barre con $x_1$ e $x_2$ per le due decisioni iniziali.

Funzione didattica: rendere visibile quanto il problema medio riduca il buffer rispetto alla soluzione stocastica.

**Figura 2 — Azioni di ricorso per scenario: SP vs EV**

Grafico che confronti, per ciascuno scenario, almeno:

- apporto straordinario $e_s$;
- vendita forzata $f_s$.

Funzione didattica: mostrare come una decisione iniziale più aggressiva possa trasferire costo e fragilità al secondo stadio.

---


### 5.4 Controlli richiesti


#### 5.4.1 Controlli sui dati

1. verificare $\sum_s p_s=1$;
2. verificare positività e bounds dei parametri;
3. verificare $0<\beta_s\leq1$;
4. verificare la coerenza delle dimensioni e della scala monetaria.

#### 5.4.2 Controlli sulla soluzione

1. solver con stato `optimal`;
2. $x_1+x_2=100$ entro tolleranza numerica;
3. $x_1,x_2\geq0$;
4. per ogni scenario:

   $$
   x_1+e_s+\beta_sf_s-m_s-g_s=0;
   $$

5. $0\leq e_s\leq\bar e_s$;
6. $0\leq f_s\leq x_2$;
7. $g_s\geq0$;
8. stessa decisione $x^{SP}$ in tutti gli scenari;
9. nessuna riottimizzazione di $x^{EV}$ durante la sua rivalutazione stocastica;
10. distinzione tra valore ottimo del problema medio e $z^{EV}$;
11. ordinamento

   $$
   z^{EV}\leq z^{SP}\leq z^{WS};
   $$

12. $VSS\geq0$ ed $EVPI\geq0$.

#### 5.4.3 Controlli interpretativi

1. $\beta_s$ non deve essere interpretato come rendimento;
2. $\kappa_s$ e $\delta_s$ non devono essere letti come tassi di mercato osservati;
3. WS non è una politica implementabile ex ante: è un benchmark informativo;
4. VSS non misura il valore dell'informazione perfetta;
5. EVPI non misura il beneficio del solo uso della distribuzione degli scenari;
6. le differenze fra SP ed EV devono essere interpretate attraverso il diverso ricorso richiesto negli scenari originari.

---

## 6. Flusso logico-teorico risolutivo atteso

| Passo | Finalità risolutiva | Formula teorico-matematica / definizione / proprietà / teorema | Applicazione nel caso | Output o controllo collegato |
|---:|---|---|---|---|
| 1 | Separare decisione ex ante e decisioni adattive | struttura two-stage; non anticipatività | $x=(x_1,x_2)'$ comune; $y_s=(g_s,e_s,f_s)'$ scenario-specifico | schema informativo e controllo della decisione comune |
| 2 | Rappresentare l'incertezza | $\mathcal S$, $p_s$, $\sum_s p_s=1$ | scenari $N,S,E$ | tabella parametri e controllo probabilità |
| 3 | Formalizzare il ricorso | funzione $Q_s(x)$ e vincolo di bilancio | margin call, apporto straordinario, vendita forzata, liquidità residua | verifica di fattibilità e bilanci |
| 4 | Costruire la forma estesa e risolvere SP | $\max\{c'x+\sum_s p_sQ_s(x)\}$ | unico buffer iniziale e tre blocchi di ricorso | $x^{SP}$, $z^{SP}$, tabella SP |
| 5 | Costruire e valutare EV | problema medio; fissaggio di $x^{EV}$ negli scenari originari | media dei coefficienti e rivalutazione senza modificare $x^{EV}$ | $x^{EV}$, $z^{EV}$, VSS |
| 6 | Costruire WS | ottimizzazione scenario per scenario con informazione perfetta | un diverso $x_s$ per ogni scenario | $z_s^{WS}$, $z^{WS}$ |
| 7 | Misurare il valore dell'informazione e della soluzione stocastica | $VSS=z^{SP}-z^{EV}$, $EVPI=z^{WS}-z^{SP}$ | confronto dei tre benchmark | ordinamento e indicatori |
| 8 | Interpretare economicamente | trade-off rendimento–liquidità–ricorso | buffer iniziale vs costi di emergenza | tabelle, grafici e interpretazione finale |

---

## 7. Scomposizione attesa in tappe

La scomposizione è intenzionalmente contenuta in **sei tappe**.

| Tappa | Regime IA prevalente | Input | Operazione | Output | Controllo | Uso successivo |
|---:|:---:|---|---|---|---|---|
| 1 | A | Scheda Caso, flusso teorico | ricostruire struttura informativa, variabili, scenari e vincoli | cella Markdown di specifica operativa | nessuna modifica alla Scheda Caso; corretta distinzione primo/secondo stadio | base teorica per il solver |
| 2 | B | parametri e formulazione | costruire vettore variabili, funzione obiettivo, uguaglianze, disuguaglianze e bounds della forma estesa | struttura LP e codice solver | probabilità, dimensioni, segni, bounds | soluzione SP |
| 3 | B | soluzione del solver | estrarre $x^{SP}$, ricorsi, valore e residui | tabella SP | optimality, budget, bilanci, bounds | benchmark EV e confronto |
| 4 | B | dati originari e $x^{SP}$ | costruire problema medio, trovare $x^{EV}$, fissarlo e rivalutarlo negli scenari originari | $x^{EV}$, valore medio, $z^{EV}$, VSS | nessuna riottimizzazione del primo stadio; distinzione valore medio/$z^{EV}$ | confronto informativo |
| 5 | B | tre scenari originari | risolvere i tre problemi WS e aggregare | $x_s^{WS}$, $z_s^{WS}$, $z^{WS}$, EVPI | un problema per scenario; ordinamento dei valori | output finali |
| 6 | C | notebook completo e output prodotti | verifica mirata di coerenza, tabelle, grafici e interpretazione | eventuali celle sostitutive e interpretazione finale dello studente | criticità respinta/accolta; completezza rispetto alla Scheda Caso | consegna finale |

Il Regime C non deve essere usato come certificazione generica. Deve partire da un dubbio, da un'anomalia o da una verifica effettivamente formulata dallo studente.

---

## 8. Mappa prompt–notebook

| Prompt | Regime | Funzione | Output nel notebook |
|---|:---:|---|---|
| Prompt zero | — | inizializzazione del contesto e delle regole | nessuna cella autonoma obbligatoria |
| Prompt 1 | — | acquisizione Scheda Caso | cella Markdown iniziale |
| Prompt 2 | A | costruzione del Flusso logico-teorico | cella Markdown con tabella del flusso |
| Prompt 3 | A | scomposizione in tappe | cella Markdown con tabella delle tappe |
| Prompt Tappa 1 | A | specifica teorico-operativa del modello | Markdown di tappa |
| Prompt Tappa 2 | B | costruzione della forma solver | Markdown + code |
| Prompt Tappa 3 | B | estrazione e controllo SP | Markdown + code + output |
| Prompt Tappa 4 | B | EV, rivalutazione e VSS | Markdown + code + output |
| Prompt Tappa 5 | B | WS ed EVPI | Markdown + code + output |
| Prompt conclusivo | C | verifica mirata e revisione finale | eventuale sostituzione di celle; nessuna cella extra di verifica |

**Intervallo progettuale dei prompt per il TakeHome:** 9–11 prompt complessivi, includendo Prompt zero e Prompt 1. L'intervallo è una scelta docente per questo caso e deve essere comunicato agli studenti nella Scheda Caso o nella traccia di consegna.

---

## 9. Struttura attesa del notebook

Sequenza consigliata:

1. cella Markdown iniziale prodotta dal Prompt 1;
2. Flusso logico-teorico risolutivo;
3. scomposizione in tappe input-output;
4. import delle librerie;
5. definizione dei parametri;
6. tabella dei parametri e controlli preliminari;
7. definizione dell'ordinamento delle variabili della forma estesa;
8. costruzione della funzione obiettivo;
9. costruzione delle uguaglianze;
10. costruzione delle disuguaglianze e dei bounds;
11. soluzione SP con HiGHS;
12. estrazione delle variabili;
13. controllo di budget, bilanci e bounds;
14. Tabella SP per scenario;
15. costruzione del problema deterministico medio;
16. soluzione del problema medio e determinazione di $x^{EV}$;
17. rivalutazione di $x^{EV}$ nei tre scenari originari;
18. calcolo di $z^{EV}$ e VSS;
19. soluzione dei tre problemi WS;
20. calcolo di $z^{WS}$ ed EVPI;
21. tabella dei benchmark;
22. Figura 1 — composizione SP vs EV;
23. Figura 2 — ricorso SP vs EV;
24. verifica conclusiva mirata;
25. interpretazione finale autonoma dello studente;
26. limiti del modello.

Librerie minime previste:

- `numpy`;
- `pandas`;
- `scipy.optimize.linprog` con `method="highs"`;
- `matplotlib`.

Non è necessario introdurre classi, programmazione a oggetti o framework generali di stochastic programming.

---

## 10. Calibrazione docente

La calibrazione è stata verificata mediante programmazione lineare.

### 11.1 Soluzione stocastica SP

La soluzione attesa è

$$
x^{SP}
=
\begin{pmatrix}
25\\
75
\end{pmatrix}.
$$

Quindi il modello mantiene 25 unità nel buffer e 75 nel portafoglio investito.

Il ricorso atteso è:

| Scenario | $e_s^{SP}$ | $f_s^{SP}$ | $g_s^{SP}$ |
|---|---:|---:|---:|
| $N$ | 0 | 0 | 15 |
| $S$ | 0 | 0 | 0 |
| $E$ | 5 | 20 | 0 |

Nel caso estremo:

$$
25+5+0.75(20)=45.
$$

Il valore ottimo è

$$
z^{SP}=3.7375.
$$

Interpretazione attesa: la soluzione stocastica sceglie un buffer sufficiente a coprire integralmente la margin call dello scenario di tensione, ma non quella dello scenario estremo a bassa probabilità. Nell'estremo utilizza l'intero apporto straordinario disponibile e completa la copertura con vendite forzate.

### 11.2 Problema deterministico medio

I coefficienti medi sono

$$
\bar m=16.25,
\qquad
\bar\beta=0.9445,
$$

$$
\bar\kappa=0.0895,
\qquad
\bar\delta=0.181,
\qquad
\bar e=5.9.
$$

La soluzione del problema medio è

$$
x^{EV}
=
\begin{pmatrix}
16.25\\
83.75
\end{pmatrix}.
$$

Il valore ottimo del problema deterministico medio è

$$
4.43125.
$$

Questo valore non deve essere etichettato come $z^{EV}$.

### 11.3 Rivalutazione di $x^{EV}$ negli scenari originari

Con $x=x^{EV}$ fissato, il ricorso ottimo atteso è:

| Scenario | $e_s$ | $f_s$ | $g_s$ |
|---|---:|---:|---:|
| $N$ | 0 | 0 | 6.25 |
| $S$ | 8 | 0.833333 | 0 |
| $E$ | 5 | 31.666667 | 0 |

Il valore stocastico della decisione EV è

$$
z^{EV}=3.5445833333.
$$

Pertanto

$$
VSS
=
z^{SP}-z^{EV}
=
0.1929166667.
$$

Interpretazione attesa: il problema medio suggerisce un buffer più basso. La decisione appare efficiente nello scenario medio costruito artificialmente, ma negli scenari originari richiede ricorso già nello scenario di tensione e vendite molto più ampie nello scenario estremo.

### 11.4 Wait-and-see

Le soluzioni scenario-specifiche attese sono:

| Scenario | $x_{1,s}^{WS}$ | $x_{2,s}^{WS}$ | $z_s^{WS}$ |
|---|---:|---:|---:|
| $N$ | 10 | 90 | 4.650 |
| $S$ | 25 | 75 | 4.125 |
| $E$ | 45 | 55 | 3.425 |

Il valore atteso wait-and-see è

$$
z^{WS}=4.43125.
$$

Quindi

$$
EVPI
=
z^{WS}-z^{SP}
=
0.69375.
$$

Si verifica

$$
3.5445833333
<
3.7375
<
4.43125.
$$

ossia

$$
z^{EV}<z^{SP}<z^{WS}.
$$

### 11.5 Nota sulla coincidenza numerica

Con questa calibrazione, il valore ottimo del **problema deterministico medio** è numericamente uguale a $z^{WS}=4.43125$.

La coincidenza è accidentale e non esprime alcuna identità teorica. Deve essere utilizzata come occasione di controllo concettuale:

- il valore del problema medio deriva da un unico problema costruito con coefficienti medi;
- $z^{WS}$ è la media ponderata dei valori ottimi scenario-specifici;
- $z^{EV}$ è invece il valore della decisione $x^{EV}$ quando viene riportata negli scenari originari.

Lo studente non deve confondere queste tre quantità.

---


### 10.6 Errori e criticità attese


Errori da monitorare nella costruzione del notebook e nel tracciato IA:

1. trasformare implicitamente il caso in un modello multistadio;
2. introdurre decisioni di ricorso prima della completa osservazione dello scenario;
3. scegliere un diverso $x$ per ciascuno scenario nel problema SP;
4. confondere $\beta_s$ con un rendimento;
5. interpretare $\kappa_s$ o $\delta_s$ come tassi storici osservati;
6. dimenticare il vincolo $f_s\leq x_2$;
7. omettere il limite $e_s\leq\bar e_s$;
8. usare il valore ottimo del problema medio come $z^{EV}$;
9. rivalutare $x^{EV}$ consentendo al primo stadio di cambiare per scenario;
10. mediare le soluzioni WS per costruire $x^{EV}$;
11. invertire i segni di VSS ed EVPI in un problema di massimizzazione;
12. attribuire significato teorico alla coincidenza numerica tra valore del problema medio e $z^{WS}$;
13. descrivere WS come strategia realmente implementabile ex ante;
14. interpretare VSS come valore dell'informazione perfetta;
15. ignorare la distinzione tra capacità di generare liquidità e costo economico della liquidazione.

Un eventuale Prompt in Regime C deve nascere da una criticità effettivamente osservata nel notebook o da un dubbio formulato dallo studente. Una possibile criticità didatticamente fertile è proprio la distinzione fra valore del problema medio, $z^{EV}$ e $z^{WS}$.

---


### 10.7 Limiti del modello


Il caso deve dichiarare esplicitamente che:

1. non ricostruisce un fondo LDI specifico;
2. non modella separatamente repo, swap e collateral agreement;
3. non rappresenta la dinamica giornaliera delle margin call;
4. non contiene decisioni intermedie: è un modello a due stadi;
5. non modella endogenamente il prezzo dei gilt;
6. non incorpora il feedback sistemico vendite–prezzi–nuove margin call;
7. non rappresenta la duration delle passività pensionistiche;
8. non calcola il funding ratio del fondo pensione;
9. non modella l'effetto di un aumento dei rendimenti sul valore attuale delle passività;
10. non incorpora esplicitamente l'intervento della Bank of England nella funzione di ricorso;
11. assume probabilità e coefficienti noti ex ante;
12. utilizza costi di ricorso lineari;
13. normalizza il patrimonio a 100;
14. usa dati numerici didattici e stilizzati.

Il limite più importante da discutere è che l'episodio storico ebbe una dinamica progressiva e auto-rinforzante, mentre il modello didattico la comprime deliberatamente in un solo passaggio

$$
x\longrightarrow s\longrightarrow y_s.
$$

Questa semplificazione è coerente con l'obiettivo del TakeHome: consolidare in un nuovo contesto il framework two-stage dei Capitoli 14–15, non introdurre un secondo esercizio multistadio.

---

## 11. Uso dell'IA e tracciato

### 13.1 Sequenza obbligatoria

Il tracciato deve rispettare la sequenza:

1. Prompt zero;
2. Prompt 1;
3. Prompt 2 in Regime A;
4. Prompt 3 in Regime A;
5. prompt di tappa;
6. eventuale Prompt C mirato;
7. verifica conclusiva o revisione dell'interpretazione, se prevista.

### 13.2 Usi ammessi

L'IA può essere utilizzata per:

- verificare la distinzione fra primo e secondo stadio;
- ordinare il flusso teorico proposto dallo studente;
- tradurre la forma estesa in matrici per `linprog`;
- costruire codice coerente con la specifica fissata;
- organizzare tabelle e grafici richiesti;
- verificare residui, bounds e ordinamento dei benchmark;
- controllare un dubbio specifico su EV, WS, VSS o EVPI;
- rivedere criticamente una bozza interpretativa già scritta dallo studente.

### 13.3 Usi non ammessi

L'IA non deve:

- cambiare scenari, probabilità o parametri;
- sostituire il framework two-stage con un modello multistadio;
- introdurre un albero di scenari non previsto;
- modificare variabili o funzione obiettivo;
- scegliere autonomamente un modello alternativo;
- produrre l'intero notebook con un'unica richiesta globale;
- generare direttamente l'interpretazione finale senza una bozza dello studente;
- presentare i parametri didattici come dati storici.

### 13.4 Intervallo dei prompt

Per questo TakeHome si propone un intervallo di

**9–11 prompt complessivi**, includendo Prompt zero e Prompt 1.

La quantità è coerente con una scomposizione in sei tappe e con una eventuale verifica conclusiva mirata.

---

## 12. Valutazione

La valutazione segue la struttura generale delle Guidelines.

| Area | Peso | Elementi specifici del caso |
|---|---:|---|
| Prompt 2 — Flusso logico-teorico | 30 | distinzione two-stage, recourse, benchmark, collegamento teoria–output–controlli |
| Prompt 3 — Scomposizione input-output | 15 | ordine SP → EV → rivalutazione → WS → indicatori; controlli espliciti |
| Notebook e output | 20 | formulazione LP, solver, tabelle, grafici, riproducibilità |
| Prompt e uso A/B/C | 15 | delimitazione del compito IA, rispetto della Scheda Caso, qualità del controllo |
| Verifiche logiche e numeriche | 15 | bilanci, bounds, rivalutazione EV, ordinamento dei valori, segni VSS/EVPI |
| Interpretazione critica finale | 5 | trade-off buffer/rendimento, significato dei benchmark, limiti storici e modellistici |

### 14.1 Elementi particolarmente rilevanti

Lo studente deve essere in grado di spiegare:

1. perché $x$ deve essere comune a tutti gli scenari in SP;
2. perché $e_s$, $f_s$ e $g_s$ possono cambiare dopo l'osservazione dello scenario;
3. perché il problema medio non coincide con il problema stocastico;
4. perché il valore ottimo del problema medio non è $z^{EV}$;
5. perché WS costituisce un benchmark informativo;
6. perché VSS ed EVPI rispondono a due domande economiche differenti.

---

## 13. Relazione con il Caso Aula

### 16.1 Elementi comuni

Entrambi i casi richiedono:

- decisione iniziale sotto incertezza;
- scenari discreti con probabilità;
- ricorso scenario-specifico;
- forma estesa lineare;
- non anticipatività del primo stadio;
- soluzione SP;
- problema EV e rivalutazione della decisione media;
- benchmark WS;
- VSS ed EVPI;
- controlli di fattibilità e coerenza informativa.

### 16.2 Elementi distintivi

**Caso Aula — SVB**

- soggetto: banca;
- problema: composizione dell'attivo e liquidità;
- fonte di stress: outflow e capacità di generare liquidità;
- ricorso: funding/liquidità di emergenza;
- lettura economica: rendimento dell'attivo contro robustezza del bilancio.

**Caso TakeHome — UK LDI**

- soggetto: investitore istituzionale / fondo pensione con strategia LDI;
- problema: dimensione del buffer di collateral;
- fonte di stress: margin call conseguente al rialzo dei rendimenti dei gilt;
- ricorso: apporto straordinario e vendita forzata di attività;
- lettura economica: rendimento corrente contro capacità di assorbire richieste di collateral.

Il TakeHome non è quindi una variazione parametrica del Caso Aula. Mantiene la stessa architettura metodologica, ma cambia il meccanismo economico-finanziario che rende necessario il ricorso.

### 16.3 Domanda metodologica comune

La domanda che unifica i due casi è:

> quanto conviene sacrificare oggi rendimento o capacità di investimento per ridurre il costo delle azioni correttive che potrebbero diventare necessarie dopo la rivelazione dell'incertezza?
