# Lezione 16 — Scheda Costruzione Caso TakeHome

Documento interno di progettazione docente.

## 1. Identificazione del caso

- **Lezione:** 16 — Applicazione in Python: programmazione stocastica
- **Tipo di caso:** TakeHome
- **Titolo:** UK LDI 2022 — Buffer di liquidità, margin call e non anticipatività
- **Destinatari:** studenti del V anno di Banca e Risk Management
- **Uso previsto:** lavoro autonomo successivo al Caso Aula, finalizzato a trasferire la programmazione stocastica dal contesto bancario SVB a un investitore istituzionale con strategia Liability Driven Investment, sviluppando una struttura multistadio con informazione progressiva e vincoli di non anticipatività.

## 2. Contesto e motivazione

Il caso è contestualizzato nella crisi delle strategie Liability Driven Investment (LDI) dei fondi pensione britannici nell'autunno 2022.

Le strategie LDI erano utilizzate da fondi pensione defined benefit per allineare maggiormente il valore degli attivi alla sensibilità delle passività rispetto ai tassi di interesse e all'inflazione. Una parte rilevante di tali strategie utilizzava leva mediante derivati sui tassi e operazioni repo su gilt.

Nel settembre 2022 il rapido aumento dei rendimenti dei gilt, e in particolare dei titoli a lunga scadenza, determinò forti riduzioni del valore delle attività utilizzate nelle strategie LDI e generò richieste di collateral e margin call. Gli investitori dovettero mobilitare liquidità, richiedere contributi aggiuntivi ai pension scheme e, nei casi più critici, vendere gilt o ridurre rapidamente la leva. Le vendite forzate contribuirono a esercitare ulteriore pressione sui prezzi dei gilt, generando un meccanismo di amplificazione che rese necessario l'intervento temporaneo della Bank of England.

Il caso utilizza questo episodio esclusivamente come riferimento economico-finanziario. La specificazione quantitativa è interamente didattica e non costituisce una ricostruzione di un particolare fondo pensione o LDI fund.

Rispetto al Caso Aula, il problema non è più organizzato in due soli stadi. L'incertezza si rivela progressivamente:

1. al tempo iniziale viene scelto il rapporto tra buffer di liquidità ed esposizione LDI;
2. si osserva un primo shock sui gilt;
3. vengono assunte decisioni di adattamento coerenti con l'informazione disponibile;
4. si osserva una seconda evoluzione del mercato;
5. vengono assunte le decisioni finali di ricorso.

Il caso è quindi progettato per rendere computazionali i concetti di programmazione stocastica multistadio e non anticipatività sviluppati nei Capitoli 14 e 15.

**Fonti storiche di riferimento per il docente:** Bank of England, *Financial Stability Report*, dicembre 2022; Bank of England, documentazione sulle operazioni temporanee di acquisto di gilt del 2022; documentazione Bank of England sulla resilienza dei fondi LDI.

I valori numerici assegnati nel caso sono stilizzati e non devono essere presentati come stime empiriche della crisi LDI.

## 3. Domanda quantitativa e obiettivo didattico

**Domanda quantitativa:** quale combinazione iniziale tra buffer di liquidità ed esposizione LDI massimizza il risultato economico atteso quando le margin call si manifestano progressivamente e le decisioni di deleveraging e mobilitazione di liquidità devono rispettare l'informazione effettivamente disponibile? Quanto valore apparente si ottiene se si violano i vincoli di non anticipatività e quanto varrebbe conoscere fin dall'inizio l'intero percorso futuro degli shock?

**Obiettivo didattico:** portare lo studente a costruire e risolvere in Python un programma stocastico lineare multistadio su un piccolo albero di scenari, distinguendo:

- decisioni iniziali;
- decisioni ai nodi intermedi;
- decisioni terminali;
- probabilità condizionate e probabilità dei percorsi;
- vincoli di non anticipatività;
- soluzione multistadio corretta;
- rilassamento anticipativo utilizzato come diagnostica;
- benchmark wait-and-see e valore dell'informazione perfetta.

Il caso deve rendere evidente che una decisione assunta a un nodo dell'albero può dipendere dalla storia già osservata, ma non dal ramo futuro che non si è ancora realizzato.

## 4. Specifica teorico-matematica

### Grandezze e variabili

Al tempo iniziale il fondo dispone di risorse complessive normalizzate pari a

$$
A_0=100.
$$

La decisione iniziale è composta da:

- $b\geq0$: buffer di liquidità;
- $h\geq0$: esposizione LDI.

Il vincolo iniziale è

$$
b+h=100.
$$

Per preservare una funzione minima di copertura delle passività si impone:

$$
h\geq50.
$$

Il rendimento unitario iniziale del buffer è

$$
r_b=0.010,
$$

mentre il rendimento unitario dell'esposizione LDI è

$$
r_h=0.045.
$$

Dopo la prima osservazione del mercato, per ciascun nodo $n\in\{M,S\}$ si definiscono:

- $y_n\geq0$: deleveraging effettuato al nodo intermedio;
- $u_n\geq0$: liquidità aggiuntiva mobilitata dal pension scheme;
- $g_n\geq0$: liquidità residua dopo la prima margin call.

Dopo la seconda osservazione, per ciascun percorso terminale $\ell$ si definiscono:

- $z_\ell\geq0$: ulteriore deleveraging;
- $v_\ell\geq0$: ulteriore liquidità mobilitata;
- $G_\ell\geq0$: liquidità residua terminale.

### Eventi, informazione o scenari

Al primo stadio aleatorio sono possibili due nodi:

- $M$: repricing moderato;
- $S$: repricing severo.

Le probabilità sono:

| Nodo | Probabilità |
|---|---:|
| $M$ | 0.65 |
| $S$ | 0.35 |

Dal nodo $M$ possono verificarsi:

- $MR$: reversal/normalizzazione;
- $MP$: persistenza dello stress.

Con probabilità condizionate:

$$
\mathbb P(MR\mid M)=0.60,
$$

$$
\mathbb P(MP\mid M)=0.40.
$$

Dal nodo $S$ possono verificarsi:

- $SR$: stabilizzazione;
- $SS$: ulteriore stress.

Con probabilità condizionate:

$$
\mathbb P(SR\mid S)=0.45,
$$

$$
\mathbb P(SS\mid S)=0.55.
$$

Le probabilità dei quattro percorsi terminali sono quindi:

| Percorso | Probabilità |
|---|---:|
| $MR$ | 0.3900 |
| $MP$ | 0.2600 |
| $SR$ | 0.1575 |
| $SS$ | 0.1925 |

Controllo obbligatorio:

$$
0.3900+0.2600+0.1575+0.1925=1.
$$

La struttura informativa è:

$$
(b,h)
\longrightarrow
\{M,S\}
\longrightarrow
(y_n,u_n,g_n)
\longrightarrow
\{MR,MP,SR,SS\}
\longrightarrow
(z_\ell,v_\ell,G_\ell).
$$

### Parametri e dati

La prima margin call è proporzionale all'esposizione LDI iniziale:

$$
a_n h.
$$

I coefficienti sono:

| Nodo | $a_n$ |
|---|---:|
| $M$ | 0.10 |
| $S$ | 0.22 |

La seconda margin call è proporzionale all'esposizione residua dopo il deleveraging intermedio:

$$
\beta_\ell(h-y_n).
$$

I coefficienti sono:

| Percorso | $\beta_\ell$ |
|---|---:|
| $MR$ | 0.00 |
| $MP$ | 0.10 |
| $SR$ | 0.05 |
| $SS$ | 0.20 |

Limiti operativi al primo adattamento:

$$
0\leq y_n\leq25,
$$

$$
0\leq u_n\leq4.
$$

Limiti operativi allo stadio terminale:

$$
0\leq z_\ell\leq10,
$$

$$
0\leq v_\ell\leq4.
$$

Il deleveraging complessivo lungo ciascun percorso non può superare:

$$
y_n+z_\ell\leq40.
$$

I costi unitari del deleveraging intermedio sono:

| Nodo | $\lambda_n$ |
|---|---:|
| $M$ | 0.025 |
| $S$ | 0.050 |

I costi unitari della liquidità aggiuntiva intermedia sono:

| Nodo | $\kappa_n$ |
|---|---:|
| $M$ | 0.020 |
| $S$ | 0.040 |

I costi unitari del deleveraging terminale sono:

| Percorso | $\mu_\ell$ |
|---|---:|
| $MR$ | 0.005 |
| $MP$ | 0.020 |
| $SR$ | 0.020 |
| $SS$ | 0.050 |

I costi unitari della liquidità aggiuntiva terminale sono:

| Percorso | $\eta_\ell$ |
|---|---:|
| $MR$ | 0.015 |
| $MP$ | 0.030 |
| $SR$ | 0.030 |
| $SS$ | 0.030 |

I coefficienti di costo hanno funzione didattica e rappresentano costi economici complessivi di aggiustamento, mobilitazione della liquidità e deleveraging; non devono essere interpretati come spread o commissioni storicamente osservati.

### Ipotesi

1. L'albero degli scenari è discreto e le probabilità sono note al tempo iniziale.
2. $b$ e $h$ devono essere scelti prima di osservare qualsiasi shock.
3. Le decisioni al nodo $M$ possono dipendere dall'osservazione di $M$, ma non possono dipendere dalla successiva realizzazione $MR$ o $MP$.
4. Le decisioni al nodo $S$ possono dipendere dall'osservazione di $S$, ma non possono dipendere dalla successiva realizzazione $SR$ o $SS$.
5. Le decisioni terminali possono dipendere dall'intero percorso osservato.
6. Una unità di esposizione deleveraged rende disponibile una unità di liquidità; l'eventuale perdita economica associata alla vendita o alla riduzione della posizione è rappresentata separatamente dai coefficienti di costo.
7. La liquidità aggiuntiva mobilitabile dal pension scheme è limitata, per rappresentare in forma stilizzata vincoli operativi e temporali.
8. Il limite su $z_\ell$ rappresenta la capacità limitata di deleveraging immediato nello stadio terminale.
9. Non vengono modellati esplicitamente prezzi dei gilt, duration, derivati specifici, repo haircuts o feedback endogeni tra vendite del fondo e prezzi di mercato.
10. Il modello non ricostruisce un singolo fondo pensione o LDI fund del 2022.
11. Tutte le quantità monetarie sono espresse in unità convenzionali su scala $A_0=100$.

### Formule vincolanti

Per il primo nodo osservato:

$$
b+u_n+y_n
=
a_n h+g_n,
\qquad
n\in\{M,S\}.
$$

Per ciascun percorso terminale $\ell$, con nodo padre $n(\ell)$:

$$
g_{n(\ell)}+v_\ell+z_\ell
=
\beta_\ell
\left(
h-y_{n(\ell)}
\right)
+
G_\ell.
$$

La funzione obiettivo del problema multistadio è:

$$
\max
\left\{
r_b b+r_h h
-
\sum_{n\in\{M,S\}}
p_n
\left(
\lambda_n y_n+\kappa_n u_n
\right)
-
\sum_{\ell}
p_\ell
\left(
\mu_\ell z_\ell+\eta_\ell v_\ell
\right)
\right\}.
$$

Il valore ottimo del problema multistadio corretto è indicato con

$$
z^{MS}.
$$

### Vincoli di non anticipatività

Nel modello a nodi i vincoli di non anticipatività sono incorporati nella definizione stessa delle variabili.

In una formulazione per percorsi equivalenti, devono valere almeno:

$$
y_{MR}=y_{MP},
\qquad
u_{MR}=u_{MP},
\qquad
g_{MR}=g_{MP},
$$

e:

$$
y_{SR}=y_{SS},
\qquad
u_{SR}=u_{SS},
\qquad
g_{SR}=g_{SS}.
$$

Le decisioni iniziali devono inoltre essere identiche su tutti i percorsi:

$$
b_{MR}=b_{MP}=b_{SR}=b_{SS},
$$

$$
h_{MR}=h_{MP}=h_{SR}=h_{SS}.
$$

### Rilassamento anticipativo diagnostico

Per mostrare l'effetto dei vincoli di non anticipatività si costruisce un secondo modello nel quale $b$ e $h$ restano decisioni iniziali comuni, ma le decisioni del nodo intermedio vengono illegittimamente rese specifiche del percorso terminale.

In particolare, vengono rimossi i vincoli:

$$
y_{MR}=y_{MP},
\qquad
y_{SR}=y_{SS},
$$

e le corrispondenti uguaglianze per $u$ e $g$.

Il valore del rilassamento anticipativo è indicato con

$$
z^{AR}.
$$

Deve risultare:

$$
z^{AR}\geq z^{MS}.
$$

La differenza

$$
\Delta_{NA}
=
z^{AR}-z^{MS}
$$

è utilizzata esclusivamente come misura diagnostica del vantaggio artificiale prodotto dalla violazione della non anticipatività. Non deve essere confusa con VSS o EVPI.

### Benchmark wait-and-see

Nel benchmark wait-and-see si assume che l'intero percorso terminale sia noto già al tempo iniziale. Per ogni percorso $\ell$ si risolve quindi un problema deterministico separato e si ottiene $z_\ell^{WS}$.

Il valore atteso con informazione perfetta è:

$$
z^{WS}
=
\sum_\ell p_\ell z_\ell^{WS}.
$$

Il valore atteso dell'informazione perfetta è:

$$
EVPI
=
z^{WS}-z^{MS}.
$$

Deve risultare:

$$
z^{MS}
\leq
z^{AR}
\leq
z^{WS},
$$

quando il rilassamento anticipativo mantiene comuni le decisioni iniziali $b$ e $h$.

### Quantità finali di interesse

1. $b^{MS}$ e $h^{MS}$;
2. $y_M,y_S,u_M,u_S,g_M,g_S$;
3. $z_\ell,v_\ell,G_\ell$ per i quattro percorsi;
4. $z^{MS}$;
5. valore e decisioni del rilassamento anticipativo;
6. $\Delta_{NA}$;
7. soluzioni wait-and-see dei quattro percorsi;
8. $z^{WS}$;
9. $EVPI$;
10. verifica dei vincoli di non anticipatività;
11. confronto economico tra buffer iniziale, deleveraging e liquidità aggiuntiva nei diversi rami.

## 5. Output richiesti

### Stime o risultati numerici

1. soluzione ottima del problema multistadio;
2. buffer iniziale ottimo;
3. esposizione LDI iniziale ottima;
4. deleveraging e liquidità aggiuntiva ai nodi $M$ e $S$;
5. decisioni terminali sui quattro percorsi;
6. valore $z^{MS}$;
7. valore $z^{AR}$;
8. differenza $\Delta_{NA}$;
9. quattro valori $z_\ell^{WS}$;
10. valore $z^{WS}$;
11. $EVPI$.

### Tabelle

**Tabella 1 — Albero degli scenari e parametri**

Probabilità, margin call, costi e limiti operativi.

**Tabella 2 — Soluzione multistadio**

Decisioni iniziali, decisioni ai nodi intermedi e decisioni terminali.

**Tabella 3 — Verifica della non anticipatività**

Confronto delle decisioni che devono coincidere nei percorsi con storia comune.

**Tabella 4 — Confronto dei benchmark informativi**

Colonne:

- multistadio corretto;
- rilassamento anticipativo;
- wait-and-see.

Righe:

- informazione disponibile;
- decisione iniziale;
- valore obiettivo;
- principali decisioni di adattamento.

**Tabella 5 — Valore dell'informazione**

$$
z^{MS},\quad
z^{AR},\quad
\Delta_{NA},\quad
z^{WS},\quad
EVPI.
$$

### Grafici

**Figura 1 — Albero degli scenari**

Rappresentazione dell'albero $M/S$ e dei quattro percorsi terminali, con probabilità e coefficienti di margin call.

**Figura 2 — Deleveraging per nodo e percorso**

Confronto tra:

- deleveraging intermedio;
- deleveraging terminale;
- deleveraging complessivo.

**Figura 3 — Confronto multistadio e rilassamento anticipativo**

Grafico che evidenzi, in particolare nel ramo $S$, la differenza tra la decisione comune imposta dalla non anticipatività e le decisioni illegittimamente differenziate nel rilassamento anticipativo.

### Controlli

1. verifica della somma delle probabilità dei nodi iniziali;
2. verifica delle probabilità condizionate;
3. verifica della somma delle probabilità dei quattro percorsi;
4. verifica $b+h=100$;
5. verifica $h\geq50$;
6. verifica dei limiti su $y_n,u_n,z_\ell,v_\ell$;
7. verifica $y_n+z_\ell\leq40$;
8. verifica dei bilanci di liquidità al primo stadio;
9. verifica dei bilanci terminali;
10. verifica della non negatività;
11. verifica dello status ottimo del solver;
12. verifica esplicita della non anticipatività;
13. verifica che il rilassamento anticipativo mantenga comuni $b$ e $h$;
14. verifica
$$
z^{AR}\geq z^{MS};
$$
15. verifica
$$
z^{WS}\geq z^{AR};
$$
16. verifica
$$
EVPI\geq0.
$$

## 6. Flusso logico-teorico risolutivo atteso

| Passo | Finalità risolutiva | Formula, definizione, proprietà o teorema | Applicazione nel caso | Output o controllo collegato |
|---:|---|---|---|---|
| 1 | Ricostruire l'albero informativo e classificare le decisioni | Programmazione stocastica multistadio; probabilità condizionate e di percorso | Distinguere decisioni iniziali, ai nodi $M/S$ e terminali | Albero corretto; probabilità dei quattro percorsi pari a uno |
| 2 | Formulare i vincoli dinamici e di non anticipatività | Bilanci di liquidità; decisioni adattate alla filtrazione disponibile | Margin call, deleveraging, liquidità aggiuntiva e decisioni comuni sui rami con storia condivisa | Forma estesa corretta; controlli di non anticipatività |
| 3 | Risolvere il problema multistadio corretto | Massimizzazione del rendimento iniziale al netto dei costi attesi di adattamento | Scelta di $b,h$ e ricorso nodo per nodo | Soluzione $MS$, controlli di fattibilità e interpretazione |
| 4 | Costruire il rilassamento anticipativo | Rimozione selettiva dei vincoli di non anticipatività | Consentire alle decisioni intermedie di dipendere illegittimamente dal ramo futuro | $z^{AR}$ e $\Delta_{NA}$; verifica $z^{AR}\geq z^{MS}$ |
| 5 | Costruire il benchmark wait-and-see | Informazione perfetta sull'intero percorso | Risolvere separatamente i quattro problemi deterministici | $z_\ell^{WS}$, $z^{WS}$ ed $EVPI$ |
| 6 | Interpretare economicamente il valore dell'adattamento e dell'informazione | Confronto $z^{MS}\leq z^{AR}\leq z^{WS}$ | Collegare buffer, margin call, deleveraging e informazione disponibile | Tabelle, grafici e commento sui vincoli informativi e sui limiti del modello |

## 7. Scomposizione attesa in tappe

| Tappa | Regime | Input | Operazione | Output | Controllo | Uso successivo |
|---:|:---:|---|---|---|---|---|
| 1 | A | Scheda Caso, Capitoli 14–15 | Ricostruire albero, probabilità, variabili e struttura informativa | Schema teorico del problema | Distinzione corretta tra storia osservata e futuro non osservato | Formulazione del modello |
| 2 | B | Albero e parametri | Implementare il modello multistadio corretto con variabili a nodo | Soluzione $MS$ | Status solver, bilanci, bounds | Analisi della soluzione |
| 3 | C | Output $MS$ | Verificare fattibilità, non anticipatività e significato economico delle decisioni | Tabelle di controllo | Uguaglianze tra decisioni con storia comune | Rilassamento anticipativo |
| 4 | B | Modello $MS$ | Costruire il rilassamento anticipativo mantenendo comuni $b,h$ | $z^{AR}$ e decisioni anticipate | $z^{AR}\geq z^{MS}$ | Misura diagnostica |
| 5 | B | Quattro percorsi | Risolvere i quattro problemi wait-and-see | $z_\ell^{WS},z^{WS},EVPI$ | $z^{WS}\geq z^{AR}$ | Confronto informativo |
| 6 | C | Tutti gli output | Costruire tabelle, grafici e interpretazione finale | Sintesi economico-finanziaria | Coerenza tra numeri, informazione e decisioni | Conclusione notebook |

## 8. Mappa tra prompt e notebook

| Prompt | Regime | Tappa | Celle o output prodotti | Decisione o controllo richiesto |
|---:|:---:|---:|---|---|
| Prompt zero | — | — | Nessuna cella | Inizializzazione del contesto IA |
| Prompt 1 | — | — | Cella Markdown iniziale | Fedeltà alla Scheda Caso |
| Prompt 2 | A | preliminare | Cella Markdown: Flusso logico-teorico | Completezza del ragionamento |
| Prompt 3 | A | preliminare | Cella Markdown: scomposizione in tappe | Coerenza input-output |
| Prompt tappa 1 | A | 1 | Cella Markdown con albero e struttura informativa | Corretta lettura della non anticipatività |
| Prompt tappa 2 | B | 2 | Celle codice del modello $MS$ | Corretta forma solver |
| Prompt tappa 3 | C | 3 | Celle di controllo e tabelle $MS$ | Bilanci e non anticipatività |
| Prompt tappa 4 | B | 4 | Celle del rilassamento anticipativo | Rimozione selettiva e non globale dei vincoli |
| Prompt tappa 5 | B | 5 | Celle wait-and-see ed EVPI | Corretta gestione delle probabilità di percorso |
| Prompt conclusivo | C | 6 | Tabelle finali, grafici e commento | Completezza, controlli e limiti |

## 9. Struttura attesa del notebook

Ordine previsto:

1. cella Markdown iniziale prodotta dal Prompt 1;
2. cella Markdown con Flusso logico-teorico risolutivo;
3. cella Markdown con scomposizione in tappe;
4. import delle librerie;
5. definizione dei nodi e dei percorsi;
6. definizione delle probabilità condizionate e delle probabilità dei percorsi;
7. controlli sulle probabilità;
8. definizione dei parametri economici e operativi;
9. rappresentazione tabellare dell'albero;
10. costruzione del modello multistadio corretto;
11. soluzione con `scipy.optimize.linprog(method="highs")`;
12. estrazione di $b^{MS},h^{MS}$;
13. estrazione delle decisioni ai nodi $M,S$;
14. estrazione delle decisioni terminali;
15. verifica dei bilanci;
16. verifica dei bounds;
17. verifica esplicita della non anticipatività;
18. Tabella 2 — soluzione multistadio;
19. costruzione del rilassamento anticipativo;
20. soluzione del rilassamento e calcolo di $\Delta_{NA}$;
21. Tabella 3 — verifica della non anticipatività;
22. costruzione dei quattro problemi wait-and-see;
23. calcolo di $z^{WS}$;
24. calcolo di $EVPI$;
25. Tabella 4 — confronto dei benchmark informativi;
26. Tabella 5 — valore dell'informazione;
27. Figura 1 — albero degli scenari;
28. Figura 2 — deleveraging per nodo e percorso;
29. Figura 3 — confronto multistadio/anticipativo;
30. cella Markdown conclusiva con interpretazione e limiti.

L'implementazione deve privilegiare strutture trasparenti: dizionari per nodi e percorsi, array NumPy, DataFrame Pandas e `scipy.optimize.linprog(method="highs")`.

Non è richiesto costruire classi Python, algoritmi di decomposizione o un framework general-purpose di programmazione stocastica.

## 10. Calibrazione docente

### Ordine di grandezza atteso dei risultati

Con i parametri assegnati, salvo differenze dovute alle tolleranze del solver, la soluzione multistadio corretta attesa è:

$$
b^{MS}
=
9.0909,
$$

$$
h^{MS}
=
90.9091.
$$

Al nodo moderato:

$$
y_M=0,
\qquad
u_M=0,
\qquad
g_M=0.
$$

Al nodo severo:

$$
y_S
\approx
9.2424,
$$

$$
u_S=4,
$$

$$
g_S
\approx
2.3333.
$$

Decisioni terminali:

$$
z_{MR}=0,
\qquad
v_{MR}=0,
$$

$$
z_{MP}
\approx
9.0909,
\qquad
v_{MP}=0,
$$

$$
z_{SR}
=
1.7500,
\qquad
v_{SR}=0,
$$

$$
z_{SS}
=
10.0000,
\qquad
v_{SS}=4.
$$

Il valore multistadio atteso è circa:

$$
z^{MS}
\approx
3.79194.
$$

Nel rilassamento anticipativo:

$$
z^{AR}
\approx
3.81864.
$$

Pertanto:

$$
\Delta_{NA}
=
z^{AR}-z^{MS}
\approx
0.02670.
$$

Nel ramo severo il rilassamento anticipativo consente, illegittimamente, decisioni intermedie differenti:

$$
y_{SR}
\approx
6.9091,
$$

$$
y_{SS}
\approx
17.5758,
$$

mentre nel modello corretto deve esistere un'unica decisione $y_S$ prima di conoscere se il seguito sarà $SR$ oppure $SS$.

Per i quattro problemi wait-and-see sono attesi valori circa pari a:

$$
z_{MR}^{WS}
=
4.2700,
$$

$$
z_{MP}^{WS}
=
4.0820,
$$

$$
z_{SR}^{WS}
\approx
3.78689,
$$

$$
z_{SS}^{WS}
\approx
3.46479.
$$

Il valore atteso wait-and-see è:

$$
z^{WS}
\approx
3.99003.
$$

L'EVPI atteso è:

$$
EVPI
=
z^{WS}-z^{MS}
\approx
0.19809.
$$

Deve risultare:

$$
3.79194
<
3.81864
<
3.99003.
$$

### Errori o ambiguità prevedibili

1. confondere probabilità condizionate e probabilità dei percorsi;
2. utilizzare le probabilità condizionate direttamente nella funzione obiettivo terminale;
3. permettere a $b$ o $h$ di dipendere dal percorso;
4. permettere a $y_M$ di essere diverso tra $MR$ e $MP$ nel modello corretto;
5. permettere a $y_S$ di essere diverso tra $SR$ e $SS$ nel modello corretto;
6. imporre invece la stessa decisione terminale a percorsi ormai distinti;
7. applicare la seconda margin call a $h$ anziché all'esposizione residua $h-y_n$;
8. dimenticare che $g_n$ è nodo-specifica e deve essere riportata allo stadio successivo;
9. confondere il rilassamento anticipativo con un modello economicamente implementabile;
10. confondere $\Delta_{NA}$ con VSS;
11. confondere $z^{AR}$ con il wait-and-see;
12. calcolare $z^{WS}$ come media semplice anziché media ponderata con le probabilità dei percorsi;
13. interpretare i coefficienti di costo come dati storici osservati;
14. interpretare il buffer ottimo come raccomandazione operativa per un fondo pensione reale.

### Controlli minimi di validazione

Devono essere verificati esplicitamente:

$$
\sum_n p_n=1,
$$

$$
\sum_\ell p_\ell=1,
$$

$$
b+h=100,
$$

$$
h\geq50,
$$

tutti i bilanci di liquidità,

tutti i bounds,

i vincoli di deleveraging complessivo,

la non anticipatività ai nodi $M$ e $S$,

$$
z^{AR}\geq z^{MS},
$$

$$
z^{WS}\geq z^{AR},
$$

e:

$$
EVPI\geq0.
$$

### Limiti interpretativi

Il caso:

- non ricostruisce quantitativamente un fondo LDI specifico;
- non modella direttamente il prezzo dei gilt;
- non rappresenta esplicitamente duration e convexity;
- non distingue derivati sui tassi, repo e gilt fisici;
- non modella haircuts o collateral agreement reali;
- non rappresenta endogenamente l'impatto delle vendite sui prezzi;
- non riproduce la spirale di fire sale in equilibrio generale;
- non include l'intervento della Bank of England come nodo decisionale;
- assegna probabilità e costi in modo esogeno;
- utilizza un albero molto piccolo;
- rappresenta la mobilitazione di liquidità del pension scheme con un semplice limite quantitativo;
- interpreta i costi di aggiustamento in forma lineare.

Questi limiti devono essere esplicitamente richiamati nella conclusione del notebook.

## 11. Uso dell'IA e tracciato

- **Prompt obbligatori:** Prompt zero; Prompt 1; Prompt 2; Prompt 3; prompt di tappa; prompt conclusivo di verifica in Regime C.
- **Numero minimo e massimo di prompt:** 9–11, conteggiando Prompt zero e Prompt 1.
- **Usi ammessi dell'IA:** chiarimento dell'albero informativo; verifica delle probabilità di percorso; supporto alla costruzione della forma solver; verifica dei vincoli di non anticipatività; traduzione del modello in Python; controllo di output già prodotti; revisione di tabelle e grafici; individuazione di errori; verifica finale di completezza.
- **Usi non ammessi:** modifica dell'albero o dei parametri della Scheda Caso; introduzione autonoma di nuovi scenari; eliminazione dei vincoli di non anticipatività dal modello principale; sostituzione del problema con simulazioni Monte Carlo non richieste; delega globale del notebook; modifica delle definizioni di $z^{MS}$, $z^{AR}$, $\Delta_{NA}$, $z^{WS}$ o $EVPI$; interpretazioni storiche non supportate dalle fonti indicate.

Nel TakeHome lo studente deve dimostrare autonomia maggiore rispetto al Caso Aula. In particolare, la costruzione dell'albero, la verifica delle probabilità e l'identificazione dei vincoli di non anticipatività devono emergere chiaramente dal tracciato IA e dal notebook.

## 12. Valutazione

### Criteri per il notebook

1. corretta rappresentazione dell'albero;
2. corretto calcolo delle probabilità dei percorsi;
3. corretta classificazione temporale delle decisioni;
4. corretta formulazione dei bilanci;
5. corretta implementazione della non anticipatività;
6. corretto utilizzo del solver;
7. corretta costruzione del rilassamento anticipativo;
8. corretta costruzione del benchmark wait-and-see;
9. corretto calcolo di $\Delta_{NA}$ ed $EVPI$;
10. qualità dei controlli;
11. leggibilità del codice;
12. qualità delle tabelle;
13. significatività dei grafici;
14. interpretazione economico-finanziaria;
15. dichiarazione dei limiti.

### Criteri per il tracciato IA

1. capacità di ricostruire autonomamente la struttura informativa;
2. contributo iniziale dello studente nei prompt in Regime A;
3. specificità dei prompt in Regime B;
4. uso del Regime C su output o dubbi effettivi;
5. capacità di identificare il rischio di anticipazione illegittima;
6. capacità di verificare criticamente le risposte dell'IA;
7. assenza di delega globale;
8. coerenza tra tracciato e notebook finale.

### Peso dei controlli e dell'interpretazione

Nel TakeHome deve avere peso elevato la capacità dello studente di spiegare:

- perché $y_M$ deve essere comune a $MR$ e $MP$;
- perché $y_S$ deve essere comune a $SR$ e $SS$;
- perché il rilassamento anticipativo produce un valore superiore ma non implementabile;
- perché il wait-and-see dispone di informazione ancora maggiore del rilassamento anticipativo;
- come il buffer iniziale riduce la necessità di vendite o di liquidità aggiuntiva;
- perché una limitazione della capacità di deleveraging terminale rende economicamente rilevanti le decisioni prese al nodo intermedio;
- perché il caso LDI riguarda principalmente un problema di liquidità e collateral sotto stress e non può essere letto semplicemente come insolvenza economica del pension scheme.

Risultati numerici corretti ma ottenuti violando la struttura informativa devono essere considerati sostanzialmente errati.

## 13. Relazione con l'altro caso della lezione

Il Caso Aula SVB–ALM e il Caso TakeHome UK LDI 2022 condividono la stessa struttura metodologica di fondo: una decisione iniziale deve essere assunta prima che l'incertezza sia completamente rivelata e le decisioni successive servono ad adattarsi agli scenari osservati.

Nel Caso Aula:

- il decisore è una banca;
- la decisione iniziale riguarda la composizione dell'attivo;
- gli scenari sono rappresentati in una struttura a due stadi;
- il ricorso consiste principalmente nel funding di emergenza;
- il focus è su soluzione stocastica, Expected Value, wait-and-see, VSS ed EVPI.

Nel Caso TakeHome:

- il decisore è un fondo pensione/investitore istituzionale con strategia LDI;
- la decisione iniziale riguarda buffer di liquidità ed esposizione LDI;
- l'incertezza si rivela progressivamente su un albero a tre stadi;
- il ricorso consiste in mobilitazione di liquidità e deleveraging;
- il focus è sulla non anticipatività, sul valore dell'adattamento progressivo, sul rilassamento anticipativo e sull'informazione perfetta.

Il TakeHome non costituisce quindi una variazione parametrica del Caso Aula. Cambiano il soggetto finanziario, il meccanismo di stress, la struttura temporale dell'informazione e il problema computazionale principale.

La domanda metodologica comune resta:

> Quanto conviene sacrificare oggi rendimento o capacità di investimento per preservare possibilità di adattamento quando le condizioni future sono incerte?
