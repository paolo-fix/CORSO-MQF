# Scheda Costruzione Caso Applicativo

Documento interno di progettazione docente. Compilazione riferita al **Caso TakeHome** della Lezione 13.

## 1. Identificazione del caso

- **Lezione:** 13 — Applicazione in Python: programmazione lineare e ALM deterministico
- **Tipo di caso:** TakeHome
- **Titolo:** **First Republic Bank 2023 — due ondate di deposit run e vincoli di ristrutturazione del bilancio**
- **Destinatari:** studenti del V anno del corso di laurea magistrale in Banca e Risk Management
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

## 3. Domanda quantitativa e obiettivo didattico

**Domanda quantitativa:** dato un bilancio stilizzato di First Republic caratterizzato da attività a liquidità differenziata, una quota minima di attività legacy e due ondate di fabbisogno di liquidità, come si costruisce e si risolve il corrispondente programma lineare e come cambia il piano ottimo al variare dell'intensità della prima ondata di deflussi, della seconda ondata e della capacità disponibile di funding?

**Obiettivo didattico:** portare lo studente a:

1. riconoscere la struttura di un problema ALM già studiato in una configurazione finanziaria diversa;
2. riformulare autonomamente variabili, vincoli e matrice dei cash flow;
3. gestire una dimensione dell'attivo maggiore rispetto al Caso Aula;
4. introdurre e interpretare un vincolo strutturale su attività legacy;
5. costruire e validare una funzione solver parametrica;
6. distinguere gli effetti di due ondate di deposit run;
7. analizzare separatamente l'effetto della capacità di funding;
8. costruire scenari congiunti senza confonderli con una sensitività univariata;
9. interpretare variazioni di valore ottimo, composizione dell'attivo, giacenze, funding e vincoli attivi;
10. trasferire il metodo del Caso Aula senza riprodurne meccanicamente la struttura.

## 4. Specifica teorico-matematica

- **Grandezze e variabili:**
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
  - $r_t^g$: rendimento della giacenza fra $t$ e $t+1$;
  - $r_t^u$: costo del funding raccolto alla data $t$;
  - $\bar u_t$: capacità benchmark di funding alla data $t$;
  - $\alpha$: moltiplicatore dell'intensità della prima ondata di deflussi;
  - $\beta$: moltiplicatore dell'intensità della seconda ondata di deflussi;
  - $\phi$: moltiplicatore della capacità massima di funding.

- **Eventi, informazione o scenari:**
  - benchmark:

    $$
    (\alpha,\beta,\phi)=(1,1,1);
    $$

  - sensitività alla prima ondata, con $\beta=1$ e $\phi=1$:

    $$
    \alpha\in\{0.90,0.95,1.00,1.05,1.10,1.15\};
    $$

  - sensitività alla seconda ondata, con $\alpha=1$ e $\phi=1$:

    $$
    \beta\in\{0.90,0.95,1.00,1.05,1.10,1.15\};
    $$

  - sensitività alla capacità di funding, con $\alpha=1$ e $\beta=1$:

    $$
    \phi\in\{0.30,0.40,0.50,0.60,0.70,0.80,0.90,1.00,1.10,1.20,1.30\};
    $$

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

- **Parametri e dati:**
  - risorse iniziali:

    $$
    A_0=100;
    $$

  - redditività:

    $$
    c'=(0.008,0.022,0.035,0.045,0.050);
    $$

  - perdite sotto stress:

    $$
    \ell'=(0,0.015,0.060,0.100,0.120);
    $$

  - matrice dei cash flow:

    $$
    A^{\mathrm{CF}}
    =
    \begin{pmatrix}
    1.00 & 0.70 & 0.05 & 0.05 & 0.10\\
    0.00 & 0.30 & 0.10 & 0.15 & 0.20\\
    0.00 & 0.00 & 0.25 & 0.30 & 0.30\\
    0.00 & 0.00 & 0.60 & 0.50 & 0.40
    \end{pmatrix};
    $$

  - fabbisogni benchmark:

    $$
    d'=(32,18,14,32);
    $$

  - rendimenti delle giacenze:

    $$
    {r^g}'=(0.004,0.005,0.006);
    $$

  - costi del funding:

    $$
    {r^u}'=(0.018,0.025,0.040);
    $$

  - capacità benchmark di funding:

    $$
    \bar u'=(4,3,2);
    $$

  - limite prudenziale:

    $$
    K=7.5;
    $$

  - quota minima di attività legacy a lunga durata:

    $$
    x_3+x_4\geq35;
    $$

  - limite massimo agli altri prestiti:

    $$
    x_5\leq35.
    $$

- **Ipotesi:**
  - orizzonte deterministico a quattro date;
  - coefficienti e cash flow noti in ciascuna configurazione parametrica;
  - divisibilità delle quantità;
  - assenza di costi fissi;
  - linearità di funzione obiettivo e vincoli;
  - la prima ondata di deposit run influenza il fabbisogno della prima data;
  - la seconda ondata influenza il fabbisogno della quarta data;
  - i fabbisogni intermedi restano invariati;
  - la capacità massima di funding varia proporzionalmente con $\phi$;
  - il costo del funding resta invariato nelle sensitività e negli scenari principali;
  - il vincolo $x_3+x_4\geq35$ rappresenta una quota minima di attività legacy che non può essere ristrutturata istantaneamente;
  - nelle sensitività univariate varia un solo parametro alla volta;
  - gli scenari sono deterministici e non hanno probabilità associate;
  - il caso è stilizzato e non rappresenta una ricostruzione quantitativa del bilancio storico di First Republic.

- **Formule vincolanti:**
  - fabbisogni parametrizzati:

    $$
    d(\alpha,\beta)
    =
    (32\alpha,18,14,32\beta)';
    $$

  - capacità massima di funding:

    $$
    \bar u_t(\phi)=\phi\bar u_t;
    $$

  - funzione obiettivo:

    $$
    \max_{x,g,u}
    \Pi(x,g,u)
    =
    c'x
    +
    \sum_{t=1}^{3}r_t^g g_t
    -
    \sum_{t=1}^{3}r_t^u u_t;
    $$

  - risorse iniziali:

    $$
    \sum_{j=1}^{5}x_j=A_0;
    $$

  - primo bilancio:

    $$
    a_1'x+u_1-g_1=d_1(\alpha);
    $$

  - bilanci intermedi:

    $$
    a_t'x
    +(1+r_{t-1}^g)g_{t-1}
    +u_t
    -(1+r_{t-1}^u)u_{t-1}
    -g_t
    =
    d_t,
    \qquad t=2,3;
    $$

  - bilancio terminale:

    $$
    a_4'x
    +(1+r_3^g)g_3
    -(1+r_3^u)u_3
    -g_4
    =
    d_4(\beta);
    $$

  - vincolo prudenziale:

    $$
    \ell'x\leq K;
    $$

  - vincolo legacy:

    $$
    x_3+x_4\geq35;
    $$

  - limite agli altri prestiti:

    $$
    x_5\leq35;
    $$

  - capacità di funding:

    $$
    0\leq u_t\leq\phi\bar u_t,
    \qquad t=1,2,3;
    $$

  - non negatività:

    $$
    x_j\geq0,
    \qquad
    g_t\geq0.
    $$

- **Quantità finali di interesse:**
  - soluzione ottima benchmark $x^*$, $g^*$, $u^*$;
  - valore ottimo $\Pi^*$;
  - residuali dei vincoli di uguaglianza;
  - slack dei vincoli di disuguaglianza;
  - stato attivo / non attivo dei vincoli;
  - valori marginali dei bilanci temporali;
  - valore marginale della capacità di funding quando attiva;
  - evoluzione di $\Pi^*$ lungo le tre griglie;
  - evoluzione di $x^*$, $g^*$ e $u^*$ lungo le tre griglie;
  - variazione rispetto al benchmark:

    $$
    \Delta\Pi^*(p)
    =
    \Pi^*(p)-\Pi^*(1);
    $$

  - variazioni delle componenti ottime:

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

  - utilizzo relativo della capacità di funding:

    $$
    \rho_t^u(p)
    =
    \frac{u_t^*(p)}
    {\bar u_t(p)};
    $$

  - stato di fattibilità lungo le griglie di $\alpha$ e $\beta$;
  - soluzioni ottime nei tre scenari;
  - perdita di valore rispetto allo scenario Standard.

## 5. Output richiesti

- **Stime o risultati numerici:**
  1. soluzione ottima benchmark;
  2. valore della funzione obiettivo benchmark;
  3. residuali, slack e principali valori marginali;
  4. soluzioni lungo le griglie di $\alpha$, $\beta$ e $\phi$;
  5. variazioni di $\Pi^*$, $x^*$, $g^*$ e $u^*$ rispetto al benchmark;
  6. rapporti di utilizzo della capacità di funding;
  7. stato di fattibilità per ogni configurazione;
  8. soluzioni nei tre scenari;
  9. perdita di valore rispetto allo scenario Standard.

- **Tabelle:**
  1. tabella dei parametri benchmark;
  2. tabella della soluzione benchmark con $x_j^*$, $g_t^*$ e $u_t^*$;
  3. tabella di verifica dei quattro bilanci temporali;
  4. tabella dei vincoli con valore, limite, slack e stato attivo / non attivo;
  5. tabella dei principali valori marginali;
  6. DataFrame della sensitività ad $\alpha$;
  7. DataFrame della sensitività a $\beta$;
  8. DataFrame della sensitività a $\phi$;
  9. tabella comparativa Standard / Mediamente critico / Critico.

  Ciascun DataFrame di sensitività deve contenere almeno:
  - valore del parametro;
  - stato del solver;
  - fattibilità;
  - $\Pi^*$;
  - $\Delta\Pi^*$;
  - $x_1^*,\ldots,x_5^*$;
  - $g_1^*,\ldots,g_4^*$;
  - $u_1^*,u_2^*,u_3^*$;
  - rapporti $u_t^*/\bar u_t$.

- **Grafici:**
  1. per ciascun parametro $p\in\{\alpha,\beta,\phi\}$, grafico di $p\mapsto\Pi^*(p)$;
  2. per ciascun parametro, grafico di $p\mapsto\Delta\Pi^*(p)$;
  3. per ciascun parametro, grafico della composizione ottima dell'attivo $x_j^*(p)$;
  4. grafico delle variazioni $\Delta x_j^*(p)$ almeno per $\alpha$ e $\beta$;
  5. per ciascun parametro, grafico del funding $u_t^*(p)$;
  6. per ciascun parametro, grafico del rapporto $u_t^*(p)/\bar u_t(p)$;
  7. per ciascun parametro, grafico delle giacenze $g_t^*(p)$;
  8. grafico dei principali valori marginali dei bilanci temporali;
  9. mappa dei principali vincoli attivi lungo ciascuna griglia;
  10. grafico a barre di $\Pi^*$ nei tre scenari;
  11. grafico della perdita di valore rispetto allo scenario Standard;
  12. grafico a barre, preferibilmente impilate, della composizione $x^*$ nei tre scenari;
  13. grafico del funding $u^*$ nei tre scenari;
  14. grafico del profilo temporale delle giacenze $g_t^*$ nei tre scenari.

- **Controlli:**
  1. verifica dimensionale di vettori e matrici;
  2. verifica del segno della funzione obiettivo nella trasformazione massimo / minimo;
  3. verifica dello stato del solver;
  4. verifica indipendente delle uguaglianze mediante residuali;
  5. verifica indipendente di disuguaglianze e bounds;
  6. verifica del vincolo legacy $x_3+x_4\geq35$;
  7. verifica della coerenza fra slack e vincolo attivo;
  8. verifica mediante perturbazione numerica di almeno un valore marginale;
  9. verifica della corretta dipendenza di $d_1$ da $\alpha$;
  10. verifica della corretta dipendenza di $d_4$ da $\beta$;
  11. verifica della corretta dipendenza della capacità di funding da $\phi$;
  12. verifica che nelle sensitività univariate gli altri due parametri restino pari a 1;
  13. verifica che le configurazioni infeasible non vengano interpretate utilizzando valori non validi di `res.x`;
  14. verifica della coerenza fra cambiamenti di pendenza, cambiamenti della soluzione e cambiamenti dei vincoli attivi;
  15. verifica che grafici e tabelle utilizzino soltanto risultati solver validi.

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
