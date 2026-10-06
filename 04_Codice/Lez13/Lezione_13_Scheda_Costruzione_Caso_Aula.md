# Scheda Costruzione Caso Applicativo

Documento interno di progettazione docente. Compilazione riferita al **Caso Aula** della Lezione 13.

## 1. Identificazione del caso

- **Lezione:** 13 — Applicazione in Python: programmazione lineare e ALM deterministico
- **Tipo di caso:** Aula
- **Titolo:** **Silicon Valley Bank 2023 — piano ALM, sensitività e scenari di stress**
- **Destinatari:** studenti del V anno del corso di laurea magistrale in Banca e Risk Management
- **Uso previsto:** caso applicativo guidato per tradurre in Python il modello di programmazione lineare e ALM deterministico sviluppato nei Capitoli 11 e 12, validarne la soluzione mediante solver e studiare come il piano ottimo reagisce a variazioni del fabbisogno di liquidità, della capacità massima di funding e del costo del funding.

## 2. Contesto e motivazione

Il caso riprende il modello SVB stilizzato sviluppato nei Capitoli 11 e 12 e ne costituisce l'estensione computazionale.

Il riferimento finanziario è la crisi di Silicon Valley Bank del marzo 2023, nella quale l'interazione fra struttura dell'attivo, rialzo dei tassi, concentrazione della raccolta, deflussi di depositi e capacità di reperire liquidità rese centrale non soltanto l'ammontare complessivo delle risorse disponibili, ma soprattutto la loro distribuzione temporale.

Il caso non costituisce una ricostruzione del bilancio storico di SVB. La calibrazione è didattica e utilizza il modello già introdotto nel Capitolo 12. Il riferimento storico serve a motivare economicamente tre possibili fonti di tensione:

1. aumento dei fabbisogni di liquidità, rappresentato dal parametro $\theta$;
2. riduzione della capacità massima di funding, rappresentata dal parametro $\phi$;
3. aumento del costo del funding, rappresentato dal parametro $\psi$.

La struttura dell'analisi è articolata in quattro momenti distinti:

1. **benchmark:** implementazione e validazione del modello del Capitolo 12;
2. **sensitività univariata:** variazione separata di $\theta$, $\phi$ e $\psi$;
3. **frontiera di fattibilità:** approfondimento specifico dell'effetto di $\theta$;
4. **scenario analysis:** variazione congiunta di $\theta$, $\phi$ e $\psi$ in tre scenari economicamente coerenti.

La sequenza didattica è:

$$
\text{modello teorico}
\longrightarrow
\text{forma solver}
\longrightarrow
\text{benchmark}
\longrightarrow
\text{sensitività}
\longrightarrow
\text{frontiera}
\longrightarrow
\text{scenari}.
$$

L'obiettivo non è soltanto osservare come cambia il valore ottimo, ma comprendere come cambia la politica ottima: composizione dell'attivo, uso del funding, giacenze di liquidità, vincoli attivi e valori marginali.

## 3. Domanda quantitativa e obiettivo didattico

**Domanda quantitativa:** dato il modello ALM deterministico di SVB sviluppato nel Capitolo 12, come si traduce correttamente il problema in forma solver e come cambiano valore ottimo e piano ALM al variare separatamente e congiuntamente del fabbisogno di liquidità, della capacità massima di funding e del costo del funding? Fino a quale livello di aumento del fabbisogno il piano resta ammissibile?

**Obiettivo didattico:** portare lo studente a:

1. tradurre autonomamente un modello ALM in vettori e matrici compatibili con un solver di programmazione lineare;
2. distinguere funzione obiettivo, uguaglianze di bilancio, disuguaglianze e bounds;
3. gestire correttamente il passaggio da massimizzazione a minimizzazione richiesto dal solver;
4. validare numericamente la soluzione benchmark;
5. interpretare slack, vincoli attivi e valori marginali;
6. costruire una funzione parametrica di soluzione;
7. distinguere fra sensitività univariata, stress test di fattibilità e scenario analysis multivariata;
8. studiare non soltanto il valore ottimo $\Pi^*$, ma l'intero vettore della soluzione ottima;
9. riconoscere cambiamenti di regime nella soluzione del programma lineare;
10. collegare i risultati computazionali alla logica economico-finanziaria dell'ALM.

## 4. Specifica teorico-matematica

- **Grandezze e variabili:**
  - $x_j$, $j=1,\ldots,4$: ammontare inizialmente allocato nelle quattro classi di attivo:
    1. cassa e riserve;
    2. titoli a breve scadenza;
    3. titoli a lunga scadenza;
    4. prestiti e impieghi meno liquidi;
  - $g_t$, $t=1,\ldots,4$: giacenza di liquidità immediatamente successiva al soddisfacimento del fabbisogno alla data $t$;
  - $u_t$, $t=1,2,3$: funding esterno raccolto alla data $t$, disponibile immediatamente e da rimborsare alla data successiva;
  - $c_j$: coefficiente di redditività dell'attivo $j$;
  - $\ell_j$: perdita unitaria sotto stress associata all'attivo $j$;
  - $a_{tj}$: quota di una unità dell'attivo $j$ resa liquida alla data $t$;
  - $d_t$: fabbisogno di liquidità benchmark alla data $t$;
  - $r_t^g$: rendimento della giacenza fra $t$ e $t+1$;
  - $r_t^u$: costo benchmark del funding raccolto alla data $t$;
  - $\bar u_t$: capacità benchmark di funding alla data $t$;
  - $\theta$: moltiplicatore del fabbisogno di liquidità nelle prime due date;
  - $\phi$: moltiplicatore della capacità massima di funding;
  - $\psi$: moltiplicatore del costo del funding.

- **Eventi, informazione o scenari:**
  - benchmark:

    $$
    (\theta,\phi,\psi)=(1,1,1);
    $$

  - sensitività a $\theta$, con $\phi=1$ e $\psi=1$:

    $$
    \theta\in\{1.00,1.01,\ldots,1.10\};
    $$

  - sensitività a $\phi$, con $\theta=1$ e $\psi=1$:

    $$
    \phi\in\{0.50,0.60,0.70,0.80,0.90,1.00,1.10,1.20,1.30,1.40,1.50\};
    $$

  - sensitività a $\psi$, con $\theta=1$ e $\phi=1$:

    $$
    \psi\in\{0.50,0.75,1.00,1.25,1.50,1.75,2.00\};
    $$

  - scenario Standard:

    $$
    (\theta,\phi,\psi)=(1.00,1.00,1.00);
    $$

  - scenario Mediamente critico:

    $$
    (\theta,\phi,\psi)=(1.03,0.90,1.25);
    $$

  - scenario Critico:

    $$
    (\theta,\phi,\psi)=(1.06,0.70,1.50).
    $$

- **Parametri e dati:**
  - risorse iniziali:

    $$
    A_0=100;
    $$

  - redditività:

    $$
    c'=(0.010,0.025,0.040,0.050);
    $$

  - perdite sotto stress:

    $$
    \ell'=(0,0.02,0.15,0.08);
    $$

  - matrice dei cash flow:

    $$
    A^{\mathrm{CF}}=
    \begin{pmatrix}
    1.00 & 0.65 & 0.05 & 0.05\\
    0.00 & 0.35 & 0.10 & 0.15\\
    0.00 & 0.00 & 0.25 & 0.30\\
    0.00 & 0.00 & 0.60 & 0.50
    \end{pmatrix};
    $$

  - fabbisogni benchmark:

    $$
    d'=(30,30,22,15);
    $$

  - rendimenti delle giacenze:

    $$
    {r^g}'=(0.005,0.006,0.007);
    $$

  - costi benchmark del funding:

    $$
    {r^u}'=(0.015,0.020,0.025);
    $$

  - capacità benchmark di funding:

    $$
    \bar u'=(10,8,6);
    $$

  - limite prudenziale:

    $$
    K=7;
    $$

  - limite ai titoli a lunga scadenza:

    $$
    x_3\leq30.
    $$

- **Ipotesi:**
  - orizzonte deterministico a quattro date;
  - coefficienti e cash flow noti in ciascuna configurazione parametrica;
  - divisibilità delle quantità;
  - assenza di costi fissi;
  - linearità della funzione obiettivo e dei vincoli per ciascuna configurazione data di $\theta$, $\phi$ e $\psi$;
  - funding disponibile entro i limiti assegnati;
  - lo stress sul fabbisogno agisce soltanto sulle prime due date;
  - la capacità massima di funding varia proporzionalmente con $\phi$;
  - il costo del funding varia proporzionalmente con $\psi$;
  - nelle sensitività univariate varia un solo parametro alla volta;
  - nella scenario analysis i tre parametri variano congiuntamente;
  - gli scenari sono configurazioni deterministiche e non hanno probabilità associate;
  - il caso è stilizzato e non rappresenta una ricostruzione quantitativa del bilancio storico di SVB.

- **Formule vincolanti:**
  - fabbisogni:

    $$
    d(\theta)=(30\theta,30\theta,22,15)';
    $$

  - capacità massima di funding:

    $$
    \bar u_t(\phi)=\phi\bar u_t;
    $$

  - costo del funding:

    $$
    r_t^u(\psi)=\psi r_t^u;
    $$

  - funzione obiettivo:

    $$
    \max_{x,g,u}
    \Pi(x,g,u;\psi)
    =
    c'x
    +
    \sum_{t=1}^{3}r_t^g g_t
    -
    \sum_{t=1}^{3}\psi r_t^u u_t;
    $$

  - vincolo sulle risorse iniziali:

    $$
    \sum_{j=1}^{4}x_j=A_0;
    $$

  - primo bilancio temporale:

    $$
    a_1'x+u_1-g_1=d_1(\theta);
    $$

  - bilanci intermedi:

    $$
    a_t'x
    +(1+r_{t-1}^g)g_{t-1}
    +u_t
    -(1+\psi r_{t-1}^u)u_{t-1}
    -g_t
    =
    d_t(\theta),
    \qquad t=2,3;
    $$

  - bilancio terminale:

    $$
    a_4'x
    +(1+r_3^g)g_3
    -(1+\psi r_3^u)u_3
    -g_4
    =
    d_4;
    $$

  - vincolo prudenziale:

    $$
    \ell'x\leq K;
    $$

  - limite di concentrazione:

    $$
    x_3\leq30;
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
  - vincoli attivi;
  - valori marginali dei bilanci temporali e dei limiti di funding;
  - evoluzione di $\Pi^*$ lungo le tre griglie;
  - evoluzione di $x^*$, $g^*$ e $u^*$ lungo le tre griglie;
  - utilizzo relativo della capacità di funding:

    $$
    \rho_t^u(p)=\frac{u_t^*(p)}{\bar u_t(p)};
    $$

  - variazione del valore ottimo rispetto al benchmark:

    $$
    \Delta\Pi^*(p)=\Pi^*(p)-\Pi^*(1);
    $$

  - variazione percentuale del valore ottimo:

    $$
    \Delta_{\%}\Pi^*(p)
    =
    100\left[
    \frac{\Pi^*(p)}{\Pi^*(1)}-1
    \right];
    $$

  - variazioni delle componenti ottime:

    $$
    \Delta x_j^*(p)=x_j^*(p)-x_j^*(1),
    $$

    $$
    \Delta g_t^*(p)=g_t^*(p)-g_t^*(1),
    $$

    $$
    \Delta u_t^*(p)=u_t^*(p)-u_t^*(1);
    $$

  - ultimo valore ammissibile della griglia di $\theta$;
  - intervallo raffinato contenente $\theta_{\mathrm{crit}}$;
  - soluzioni ottime nei tre scenari;
  - perdita di valore di ciascuno scenario rispetto allo scenario Standard.

## 5. Output richiesti

- **Stime o risultati numerici:**
  1. soluzione ottima benchmark;
  2. valore della funzione obiettivo benchmark;
  3. slack, residuali e valori marginali benchmark;
  4. soluzioni lungo le tre griglie di sensitività;
  5. variazione assoluta e percentuale di $\Pi^*$;
  6. variazioni di $x^*$, $g^*$ e $u^*$;
  7. rapporto di utilizzo della capacità di funding;
  8. ultimo valore ammissibile della griglia di $\theta$;
  9. intervallo raffinato contenente $\theta_{\mathrm{crit}}$;
  10. soluzioni nei tre scenari;
  11. perdita di valore rispetto allo scenario Standard.

- **Tabelle:**
  1. tabella dei parametri benchmark;
  2. tabella della soluzione benchmark con $x_j^*$, $g_t^*$ e $u_t^*$;
  3. tabella di verifica dei quattro bilanci temporali;
  4. tabella dei vincoli con valore, limite, slack e stato attivo/non attivo;
  5. tabella dei principali valori marginali;
  6. DataFrame della sensitività a $\theta$;
  7. DataFrame della sensitività a $\phi$;
  8. DataFrame della sensitività a $\psi$;
  9. tabella di raffinamento della frontiera di fattibilità;
  10. tabella comparativa Standard / Mediamente critico / Critico.

  Ciascun DataFrame di sensitività deve contenere almeno:
  - valore del parametro;
  - stato del solver;
  - fattibilità;
  - $\Pi^*$;
  - $\Delta\Pi^*$;
  - $x_1^*,\ldots,x_4^*$;
  - $g_1^*,\ldots,g_4^*$;
  - $u_1^*,u_2^*,u_3^*$;
  - rapporti $u_t^*/\bar u_t$.

- **Grafici:**
  1. per ciascun parametro $p\in\{\theta,\phi,\psi\}$, grafico di $p\mapsto\Pi^*(p)$;
  2. per ciascun parametro, grafico di $p\mapsto\Delta\Pi^*(p)$ oppure $p\mapsto\Delta_{\%}\Pi^*(p)$;
  3. per ciascun parametro, grafico delle componenti $x_j^*(p)$;
  4. grafico delle variazioni $\Delta x_j^*(p)$ almeno per la sensitività a $\theta$ e, se informativo, anche per $\phi$ e $\psi$;
  5. per ciascun parametro, grafico delle componenti $u_t^*(p)$;
  6. per ciascun parametro, grafico del rapporto $u_t^*(p)/\bar u_t(p)$;
  7. per ciascun parametro, grafico delle giacenze $g_t^*(p)$;
  8. grafico dei valori marginali dei bilanci temporali, con particolare attenzione alla sensitività rispetto a $\theta$;
  9. grafico dei valori marginali dei limiti di funding quando economicamente informativi;
  10. mappa dei principali vincoli attivi lungo la griglia parametrica;
  11. per $\theta$, grafico del valore ottimo fino all'ultima soluzione ammissibile, con indicazione della regione di perdita di fattibilità;
  12. grafico a barre di $\Pi^*$ nei tre scenari;
  13. grafico della perdita di valore rispetto allo scenario Standard;
  14. grafico a barre, preferibilmente impilate, della composizione $x^*$ nei tre scenari;
  15. grafico del funding $u^*$ nei tre scenari;
  16. grafico del profilo temporale delle giacenze $g_t^*$ nei tre scenari;
  17. opzionalmente, misura sintetica della distanza della soluzione dal benchmark, ad esempio:

      $$
      D_x(p)
      =
      \sum_{j=1}^{4}
      \left|
      x_j^*(p)-x_j^*(1)
      \right|.
      $$

- **Controlli:**
  1. verifica dimensionale di vettori e matrici;
  2. verifica del segno della funzione obiettivo nella trasformazione massimo/minimo;
  3. verifica dello stato del solver;
  4. verifica indipendente delle uguaglianze mediante residuali;
  5. verifica indipendente di disuguaglianze e bounds;
  6. confronto della soluzione benchmark con il Capitolo 12;
  7. verifica della coerenza fra slack e classificazione del vincolo come attivo;
  8. verifica mediante perturbazione numerica di almeno un valore marginale;
  9. verifica della corretta dipendenza di $d$ da $\theta$;
  10. verifica della corretta dipendenza di $\bar u$ da $\phi$;
  11. verifica della corretta dipendenza di $r^u$ da $\psi$ sia nella funzione obiettivo sia nei rimborsi del funding;
  12. verifica che nelle sensitività univariate gli altri due parametri restino pari a 1;
  13. verifica che scenari infeasible non generino interpretazioni basate su valori non validi di `res.x`;
  14. verifica che il valore di soglia individuato sulla griglia non venga confuso con la frontiera raffinata;
  15. verifica che i valori marginali siano interpretati localmente;
  16. verifica della coerenza fra cambiamenti di pendenza, cambiamenti della soluzione e cambiamenti dei vincoli attivi;
  17. verifica che grafici e tabelle utilizzino esclusivamente risultati solver validi.

## 6. Flusso logico-teorico risolutivo atteso

| Passo | Finalità risolutiva | Formula, definizione, proprietà o teorema | Applicazione nel caso | Output o controllo collegato |
|---:|---|---|---|---|
| 1 | Ricostruire e tradurre il modello ALM | Struttura del programma lineare e forma matriciale per il solver | Identificare variabili, obiettivo, bilanci, vincoli e bounds; definire l'ordinamento delle variabili | Matrici e vettori del modello con controllo dimensionale |
| 2 | Risolvere e validare il benchmark | Ammissibilità, ottimalità, slack e valori marginali | Risolvere il caso $(\theta,\phi,\psi)=(1,1,1)$ e confrontarlo con il Capitolo 12 | Soluzione benchmark, residuali, vincoli attivi e marginals |
| 3 | Parametrizzare i tre driver di stress | Analisi parametrica di termini noti, bounds e coefficienti | Introdurre $\theta$, $\phi$ e $\psi$ nella funzione solver | Funzione generale di soluzione validata sul benchmark |
| 4 | Svolgere le sensitività univariate | Comparative statics numerica | Variare separatamente $\theta$, $\phi$ e $\psi$ sulle griglie assegnate | DataFrame, variazioni di $\Pi^*$, $x^*$, $g^*$, $u^*$, vincoli attivi e grafici |
| 5 | Individuare la frontiera di fattibilità | Insieme ammissibile parametrico | Raffinare l'analisi di $\theta$ nell'intorno del passaggio feasible / infeasible | Intervallo contenente $\theta_{\mathrm{crit}}$ |
| 6 | Confrontare gli scenari e interpretare | Scenario analysis deterministica | Risolvere Standard, Mediamente critico e Critico e confrontare le soluzioni ottime | Tabella e grafici di scenario; interpretazione economico-finanziaria finale |

## 7. Scomposizione attesa in tappe

| Tappa | Regime | Input | Operazione | Output | Controllo | Uso successivo |
|---:|:---:|---|---|---|---|---|
| 1 | A/B | Scheda Caso e modello teorico | Definire ordinamento delle variabili, parametri e matrici del benchmark | Struttura solver completa | Dimensioni, indici, coefficienti e segni | Risoluzione benchmark |
| 2 | B/C | Modello benchmark | Risolvere il LP e costruire la diagnostica | $x^*$, $g^*$, $u^*$, $\Pi^*$, residuali, slack e marginals | Confronto con Capitolo 12 e verifica di almeno un marginale | Validazione del modello |
| 3 | A/B | Modello validato | Costruire una funzione parametrica in $\theta$, $\phi$, $\psi$ | Solver parametrico riutilizzabile | Riproduzione del benchmark per $(1,1,1)$ | Analisi parametrica |
| 4 | B | Funzione parametrica e tre griglie | Eseguire le sensitività univariate e costruire tabelle e grafici | Tre DataFrame di sensitività e relativi grafici | Un solo parametro varia alla volta; gestione degli scenari infeasible | Lettura comparative statics |
| 5 | B/C | Risultati della sensitività a $\theta$ | Raffinare la ricerca della frontiera di fattibilità | Ultimo valore ammissibile, primo non ammissibile e intervallo per $\theta_{\mathrm{crit}}$ | Robustezza rispetto al passo della griglia | Stress test |
| 6 | B/C | Tre scenari congiunti | Risolvere e confrontare Standard, Mediamente critico e Critico | Tabella comparativa, grafici e commento finale | Coerenza tra parametri, soluzione ottima, vincoli attivi e interpretazione | Chiusura del caso |

## 8. Mappa tra prompt e notebook

| Prompt | Regime | Tappa | Celle o output prodotti | Decisione o controllo richiesto |
|---:|:---:|---:|---|---|
| 0 | — | — | Inizializzazione della chat | Applicazione delle regole generali |
| 1 | — | — | Cella Markdown iniziale | Fedeltà alla Scheda Caso |
| 2 | A | — | Flusso logico-teorico risolutivo | Correttezza dell'ordine logico |
| 3 | A | — | Scomposizione in tappe | Coerenza input / output / controlli |
| 4 | A/B | 1 | Definizione del modello | Ordinamento delle variabili e controllo delle matrici |
| 5 | B | 2 | Solver benchmark | Confronto con Capitolo 12 |
| 6 | B/C | 3–4 | Diagnostica e marginali | Residuali, slack e verifica mediante differenza finita |
| 7 | A/B | 5 | Funzione parametrica | Corretta azione di $\theta$, $\phi$ e $\psi$ |
| 8 | B | 6–8 | Tre sensitività, DataFrame e grafici | Isolamento corretto dei parametri |
| 9 | B/C | 9–10 | Frontiera e scenari | Fattibilità e confronto multivariato |
| 10, solo se necessario | C | 11 | Revisione critica finale | Solo criticità effettivamente emersa |

## 9. Struttura attesa del notebook

1. Cella Markdown iniziale prodotta dal Prompt 1.
2. Cella Markdown con il Flusso logico-teorico risolutivo.
3. Cella Markdown con la scomposizione in tappe.
4. Cella codice per l'importazione delle librerie.
5. Cella codice per la definizione dei parametri benchmark.
6. Cella Markdown con l'ordinamento delle variabili.
7. Cella codice per la costruzione delle matrici benchmark.
8. Cella codice per i controlli dimensionali.
9. Cella codice per la soluzione benchmark.
10. Output con stato del solver, valore ottimo e vettori $x^*$, $g^*$, $u^*$.
11. Cella Markdown di confronto con il Capitolo 12.
12. Cella codice per la ricostruzione dei bilanci.
13. Output con residuali.
14. Cella codice per slack, bounds attivi e valori marginali.
15. Output con tabella diagnostica.
16. Cella codice per la verifica di almeno un marginale mediante perturbazione.
17. Cella Markdown con interpretazione della verifica.
18. Cella Markdown per la definizione di $\theta$, $\phi$ e $\psi$.
19. Cella codice per la funzione solver parametrica.
20. Cella codice di test della funzione in $(1,1,1)$.
21. Cella codice per la sensitività a $\theta$.
22. Output DataFrame e grafici relativi a $\theta$.
23. Cella codice per la sensitività a $\phi$.
24. Output DataFrame e grafici relativi a $\phi$.
25. Cella codice per la sensitività a $\psi$.
26. Output DataFrame e grafici relativi a $\psi$.
27. Cella Markdown per l'identificazione dell'intervallo critico di $\theta$.
28. Cella codice per il raffinamento della frontiera.
29. Output con ultimo valore ammissibile e primo valore non ammissibile.
30. Cella Markdown con la definizione dei tre scenari.
31. Cella codice per la risoluzione degli scenari.
32. Output con tabella comparativa.
33. Celle codice / output con grafici di scenario.
34. Cella Markdown finale con interpretazione economico-finanziaria e limiti del modello.

Il notebook deve essere eseguibile sequenzialmente dall'inizio alla fine. Tutte le tabelle e tutti i grafici devono derivare dagli oggetti prodotti dal solver. Non devono essere inseriti manualmente valori della soluzione nelle celle successive.

## 10. Calibrazione docente

- **Ordine di grandezza atteso dei risultati:**
  - nel benchmark devono essere riprodotti, a tolleranza numerica:

    $$
    x^*\approx(0,51.920,0,48.080)',
    $$

    $$
    g^*\approx(6.152,1.567,0,2.890)',
    $$

    $$
    u^*\approx(0,0,6)',
    $$

    $$
    \Pi^*\approx3.5922;
    $$

  - il limite $u_3\leq6$ deve risultare attivo nel benchmark;
  - i residuali dei bilanci devono essere prossimi allo zero entro una tolleranza numerica appropriata;
  - aumentando $\theta$, la soluzione deve riallocare progressivamente il piano verso profili che rendono liquidità disponibile prima;
  - la funzione obiettivo deve deteriorarsi all'aumentare dello stress, salvo eventuali tratti locali associati a cambiamenti della base ottima;
  - la sensitività a $\phi$ deve evidenziare quando una capacità aggiuntiva di funding smette di modificare la soluzione;
  - la sensitività a $\psi$ deve evidenziare come cambia la convenienza economica del funding;
  - con la calibrazione prevista, il problema è ancora ammissibile per $\theta=1.05$ e perde la fattibilità prima di $\theta=1.07$;
  - il controllo docente più fine colloca la frontiera approssimativamente attorno a:

    $$
    \theta_{\mathrm{crit}}\simeq1.061;
    $$

  - tale valore è riservato alla calibrazione docente e non deve essere riportato nella Scheda Caso destinata agli studenti;
  - prima della pubblicazione della Scheda Caso studente devono essere validati nuovamente con il solver anche gli scenari Mediamente critico e Critico.

- **Errori o ambiguità prevedibili:**
  1. dimenticare che il solver minimizza;
  2. modificare erroneamente anche i segni dei vincoli;
  3. confondere rendimento dell'attivo e cash flow disponibile;
  4. dimenticare il rimborso del funding;
  5. collocare il rimborso nella data errata;
  6. dimenticare $g_4$;
  7. confondere uguaglianze e disuguaglianze;
  8. duplicare bounds e vincoli senza comprenderne la funzione;
  9. interpretare direttamente il segno dei marginals del problema trasformato;
  10. trattare un valore marginale come valido globalmente;
  11. modificare contemporaneamente più parametri durante una sensitività univariata;
  12. applicare $\phi$ ai valori di $u_t$ anziché alle capacità $\bar u_t$;
  13. applicare $\psi$ soltanto alla funzione obiettivo e non al rimborso del funding nei bilanci;
  14. confondere variazione assoluta e percentuale;
  15. interpretare cambiamenti di pendenza senza verificare i vincoli attivi;
  16. utilizzare `res.x` quando il solver dichiara il problema non ammissibile;
  17. collegare graficamente punti ammissibili e non ammissibili;
  18. confondere lo scenario Critico con la frontiera di fattibilità;
  19. interpretare $(\theta,\phi,\psi)$ come stime storiche effettive di SVB.

- **Controlli minimi di validazione:**
  1. riproduzione del benchmark del Capitolo 12;
  2. errore massimo dei bilanci temporali inferiore alla tolleranza scelta;
  3. rispetto di tutti i bounds;
  4. rispetto del vincolo prudenziale e del limite di concentrazione;
  5. coerenza slack / vincoli attivi;
  6. verifica numerica di almeno un valore marginale;
  7. test della funzione parametrica nel punto $(1,1,1)$;
  8. verifica che in ciascuna sensitività univariata restino fissi gli altri due parametri;
  9. separazione degli scenari feasible / infeasible prima della costruzione dei grafici;
  10. raffinamento della griglia attorno alla frontiera di $\theta$;
  11. coerenza fra cambiamenti della soluzione, cambiamenti di pendenza e insieme dei vincoli attivi;
  12. riproducibilità integrale del notebook.

- **Limiti interpretativi:**
  1. il modello è deterministico;
  2. ogni configurazione parametrica è trattata come nota al tempo iniziale;
  3. non è modellato il comportamento endogeno dei depositanti;
  4. non sono modellati fire sales o feedback prezzo-vendita;
  5. lo stress non modifica endogenamente il valore di mercato degli attivi;
  6. la capacità di funding è esogena;
  7. il costo del funding è parametrico e non dipende endogenamente dalla quantità raccolta;
  8. $\theta$, $\phi$ e $\psi$ non sono variabili casuali;
  9. i tre scenari non costituiscono una distribuzione probabilistica;
  10. non vengono assegnate probabilità agli scenari;
  11. non si effettua ottimizzazione stocastica;
  12. le decisioni non sono adattive rispetto a informazione progressiva;
  13. tali estensioni appartengono alle Lezioni 14–16;
  14. i coefficienti numerici non devono essere interpretati come dati storici effettivi di SVB.

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
  1. verifica della traduzione fra formulazione teorica e struttura matriciale;
  2. costruzione di codice Python per una tappa già definita;
  3. controllo di dimensioni, indici e segni;
  4. costruzione della funzione parametrica;
  5. supporto nella gestione dei DataFrame;
  6. costruzione dei grafici richiesti;
  7. spiegazione dell'output del solver;
  8. verifica di residuali, slack e valori marginali;
  9. revisione di codice a seguito di un errore identificato;
  10. controllo della coerenza fra grafici, tabelle e output numerici;
  11. revisione critica dell'interpretazione finale.

- **Usi non ammessi:**
  1. chiedere all'IA di risolvere integralmente il caso in un unico prompt;
  2. delegare all'IA la formulazione del modello;
  3. introdurre autonomamente nuovi parametri o scenari;
  4. modificare le griglie assegnate senza motivazione e senza approvazione;
  5. sostituire la Scheda Caso con una formulazione proposta dall'IA;
  6. chiedere un notebook completo senza passare attraverso flusso e tappe;
  7. chiedere direttamente all'IA il valore di $\theta_{\mathrm{crit}}$;
  8. accettare valori marginali o interpretazioni del solver senza controllo;
  9. interpretare automaticamente i grafici senza confronto con tabelle e vincoli;
  10. attribuire valore storico ai parametri stilizzati del caso.

## 12. Valutazione

- **Criteri per il notebook:**
  1. corretta costruzione della forma solver;
  2. leggibilità dell'ordinamento delle variabili;
  3. riproducibilità;
  4. riproduzione corretta del benchmark;
  5. presenza dei controlli numerici richiesti;
  6. corretta parametrizzazione di $\theta$, $\phi$ e $\psi$;
  7. costruzione corretta delle tre sensitività univariate;
  8. gestione corretta della fattibilità;
  9. qualità e completezza dei DataFrame;
  10. qualità e leggibilità dei grafici;
  11. capacità di leggere le variazioni della soluzione ottima;
  12. collegamento fra cambiamenti della soluzione e vincoli attivi;
  13. corretta costruzione della scenario analysis;
  14. coerenza fra risultati numerici e interpretazione.

- **Criteri per il tracciato IA:**
  1. contributo autonomo dello studente nei Prompt 2 e 3;
  2. distinzione corretta fra Regime A, B e C;
  3. specificità dei prompt di tappa;
  4. esplicitazione di input, output e controlli;
  5. presenza di verifiche critiche e non soltanto di richieste di generazione di codice;
  6. capacità di non delegare all'IA le decisioni modellistiche fissate dalla Scheda Caso;
  7. uso del Regime C fondato su criticità effettivamente osservate.

- **Peso dei controlli e dell'interpretazione:** deve essere attribuito rilievo elevato alla correttezza della costruzione del modello e ai controlli, non alla sola capacità di ottenere `success=True`. La lettura di residuali, slack, valori marginali, cambiamenti della soluzione ottima, vincoli attivi e perdita di fattibilità costituisce parte sostanziale dell'esercizio. La distinzione fra sensitività univariata, stress test e scenario analysis deve risultare esplicita nell'interpretazione finale.

## 13. Relazione con l'altro caso della lezione

Il Caso Aula SVB e il Caso TakeHome First Republic devono essere metodologicamente comparabili senza ridursi a una variazione parametrica dello stesso problema.

Nel Caso Aula SVB lo studente dispone:

- di un modello teorico già noto;
- di un benchmark verificabile;
- di una calibrazione strutturata;
- di tre driver di sensitività;
- di una frontiera di fattibilità riferita a $\theta$;
- di tre scenari congiunti.

Il percorso metodologico del Caso Aula è:

$$
\text{implementare}
\longrightarrow
\text{validare}
\longrightarrow
\text{parametrizzare}
\longrightarrow
\text{analizzare}
\longrightarrow
\text{interpretare}.
$$

Il Caso TakeHome First Republic deve invece richiedere:

$$
\text{riconoscere}
\longrightarrow
\text{riformulare}
\longrightarrow
\text{trasferire il metodo}.
$$

La diversità dovrà riguardare almeno una dimensione strutturale fra:

- profilo temporale dei cash flow degli attivi;
- struttura dei fabbisogni;
- accesso al funding;
- distribuzione temporale della scarsità.

Il Caso TakeHome non deve trasformarsi in una semplice replica delle tre griglie di SVB con coefficienti differenti.

La comparabilità deve riguardare il metodo di programmazione lineare e ALM; la differenza deve riguardare il problema finanziario che il metodo è chiamato a risolvere.
