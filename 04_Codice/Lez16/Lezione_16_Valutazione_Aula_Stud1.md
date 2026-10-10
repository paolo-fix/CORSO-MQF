# Valutazione dello studente 1 sul caso aula della lezione 16

Data della valutazione: 10 ottobre 2026.

**Valutazione proposta: 78/100.** Il notebook implementa correttamente il modello stocastico a due stadi e i confronti EV/EEV e WS. I risultati sono riproducibili. Il tracciato documenta contributi iniziali pertinenti e una domanda autonoma significativa in Regime C. Il lavoro rimane incompleto nella conclusione interpretativa; alcuni controlli sono dichiarati più estesamente di quanto venga effettivamente verificato, e la risposta IA conclusiva contiene numeri incompatibili con il notebook, non riconciliati dallo studente.

Si applicano i sei pesi della sezione 15.11 delle [Guidelines](../../00_MasterPlan/MQF_Project_Guidelines.md), come richiesto dal docente per il caso aula. La griglia è formulata nelle Guidelines per i take-home con IA: la sua applicazione al caso aula è qui esplicita. I punteggi sono giudizi motivati entro i pesi assegnati, non detrazioni automatiche previste dalle Guidelines. L'equivalente puramente lineare è **23,4/30**, senza presumere una regola istituzionale di conversione o arrotondamento.

## Materiali e metodo

Sono stati acquisiti da GitHub, repository `paolo-fix/CORSO-MQF`, ramo `main`, e confrontati con i file locali:

| Materiale | Identificativo Git del contenuto acquisito |
|---|---|
| Guidelines, soprattutto §§ 15.6–15.12 | `c97461e513ef986d964e5fc92568d7cd14942c0c` |
| [Scheda Caso Aula](Lezione_16_Scheda_Caso_Aula.md) | `ee0665101858480dbf38ac2c10fff19a22b38c0f` |
| [Scheda Costruzione Caso Aula](Lezione_16_Scheda_Costruzione_Caso_Aula.md) | `3132a106330a0ffd2cc4ead602a90fad96d8072b` |
| [Notebook dello studente 1](Lezione_16_Notebook_Aula_Stud1.ipynb) | `08030f47b5be9e06e08296a3a2f3cb35c42fc36e` |
| [Tracciato IA in DOCX](Lezione_16_Tracciato_Aula_Stud1.docx) | `856bc223e274c956705b91d949d4befd9a0ba7d7` |

Le Guidelines locali coincidono con quelle acquisite da GitHub dopo la normalizzazione dei fine riga Windows. Il tracciato è stato letto direttamente dal DOCX, che non contiene immagini incorporate. Sono riconoscibili 21 interventi utente, incluse apertura, conferme e richieste di formato o correzione.

Il notebook contiene 17 celle, di cui 7 di codice; la numerazione citata parte da 1. Le sette celle di codice sono state eseguite in ordine in un processo Python pulito con NumPy 2.1.3, SciPy 1.15.3, pandas 2.2.3 e Matplotlib 3.10.0. Tutti gli output standard coincidono esattamente con quelli salvati. I due grafici incorporati sono stati ispezionati visivamente. Gli avvisi prodotti da `plt.show()` dipendono esclusivamente dal backend non interattivo utilizzato per la verifica.

È stata inoltre costruita una formulazione indipendente, eliminando le variabili di liquidità residua e imponendo `alpha_s'x + u_s >= d_s`: conferma allocazioni e obiettivi di SP, EV e dei tre problemi WS. EEV è stato ricalcolato a decisione EV fissata. Queste verifiche del valutatore non sono attribuite allo studente. Gli elaborati originali non sono stati modificati; il take-home della stessa lezione è escluso dalla valutazione.

## Griglia numerica

| Area delle Guidelines | Massimo | Assegnato | Motivazione sintetica |
|---|---:|---:|---|
| Prompt 2 — Flusso logico-teorico risolutivo | 30 | **23** | Contributo personale pertinente e ordinato; formalizzazione limitata e distinzione EV/EEV non esplicitata nella proposta iniziale, poi correttamente recepita. |
| Prompt 3 — Scomposizione input-output | 15 | **12** | Sequenza operativa coerente, con rivalutazione EEV, WS separati e controlli; input, output e verifiche non sono dettagliati sistematicamente nella proposta personale. |
| Notebook Jupyter e output computazionali | 20 | **18** | Modello e risultati corretti, riproducibili, tabelle e grafici presenti; costo per scenario confuso nell'etichettatura con il contributo al costo atteso. |
| Prompt e uso dei regimi A/B/C | 15 | **13** | Contesto e vincoli fissati, validazioni prima del codice e domanda C autonoma; accoglimento della criticità non seguito da una chiusura operativa documentata. |
| Verifiche logiche e controlli numerici | 15 | **11** | Controlli sostanziali effettivi; alcune verifiche WS solo dichiarate, gestione dello stato solver migliorabile e mancata riconciliazione numerica della risposta IA conclusiva. |
| Interpretazione critica finale | 5 | **1** | Intuizione autonoma osservabile nel prompt C, ma manca il commento conclusivo richiesto, con lettura quantitativa completa e limiti del modello. |
| **Totale** | **100** | **78** | |

Le carenze sono collocate nella loro area prevalente: precisione degli output nel notebook, verifiche nell'area dei controlli, mancata conclusione nell'ultima area. Non si sommano detrazioni automatiche per il medesimo rilievo. La qualità intrinseca della risposta IA non costituisce un criterio autonomo di penalizzazione.

## 1. Prompt 2: contributo teorico e flusso finale — 23/30

Il quinto intervento utente, identificato come «Regime A - Ricognizione teorico-modellistica», contiene sei passaggi proposti dallo studente. La sequenza distingue la decisione iniziale dalle decisioni successive all'osservazione dello scenario; collega scenari, probabilità e coefficienti di liquidabilità al vincolo di liquidità; introduce rendimento e costo atteso del funding; prevede SP, soluzione sui valori medi e benchmark con conoscenza anticipata dello scenario. Chiede all'IA di verificare, completare e ordinare senza codice e senza cambiare modello.

Il contributo è specifico e non vuoto. La distinzione temporale del primo punto costituisce già un apporto alla non anticipatività: non sarebbe corretto attribuire interamente all'IA questo concetto solo perché la formulazione finale lo rende più esplicito.

La proposta rimane tuttavia prevalentemente descrittiva. Non scrive le equazioni di bilancio o dell'obiettivo, non esplicita le formule delle due metriche e non distingue chiaramente la soluzione del problema EV dalla sua rivalutazione a decisione fissata negli scenari originali. Il sesto punto associa genericamente il benchmark con informazione perfetta al calcolo di entrambe le metriche: occorre separare il confronto SP–EEV, che definisce VSS, dal confronto WS–SP, che definisce EVPI.

La tabella finale della cella 2 recepisce correttamente queste distinzioni e collega teoria, output e controlli. La conferma «Valido la tua proposta» non documenta da sola una verifica analitica, ma il successivo Prompt 3 riprende esplicitamente la rivalutazione di EV negli scenari: è un'evidenza positiva di recepimento dell'integrazione. La notazione sintetica `max_x`, che non elenca sempre i ricorsi fra le variabili ottimizzate, può essere resa più precisa; il resto della formulazione e il codice chiariscono correttamente il problema e non mostrano un errore sostanziale su questo punto.

## 2. Prompt 3: scomposizione operativa — 12/15

L'ottavo intervento utente propone sei tappe: dati e somma delle probabilità; SP e ricorsi; risultati economici; EV seguito dalla rivalutazione EEV; tre problemi WS separati; confronto mediante tabelle, grafici e ordinamento dei valori.

La proposta è coerente con il flusso teorico. In particolare, lo studente scrive di ricavare `x_EV` e poi valutarlo negli scenari originari per ottenere EEV e VSS: supera così l'ambiguità della prima proposta teorica. Sono riconoscibili gli oggetti che alimentano i passaggi successivi e i controlli non sono assenti.

La distinzione sistematica fra input, operazione, output, controllo e uso successivo è però sviluppata soprattutto nella tabella prodotta dall'IA e validata dallo studente. Nella proposta personale non vengono specificati per ciascuna soluzione i controlli di bilancio, bounds, non negatività e stato del solver, né vengono identificati puntualmente tutti gli output richiesti. Il giudizio è positivo, ma non di piena padronanza documentata della scomposizione.

## 3. Notebook e risultati — 18/20

Il modello rispetta dati, scenari e vincoli della Scheda Caso. SP usa un unico vettore `x` e ricorsi distinti per scenario; i segni della minimizzazione e i pesi probabilistici sono corretti. EV usa le medie ponderate prescritte. EEV mantiene fisso `x_EV` e calcola il deficit positivo: con funding illimitato, costo positivo e residuo non remunerato, questo restituisce il ricorso ottimo. WS risolve effettivamente tre problemi separati e ne pondera gli obiettivi.

### Risultati verificati

L'ordine delle allocazioni è cassa, titoli a breve, titoli a lunga, prestiti.

| Quantità | Valore |
|---|---:|
| `x_SP` | `(0; 30; 70; 0)` |
| Rendimento lordo SP | 3,550000 |
| Costo atteso funding SP | 0,112500 |
| `z_SP` | **3,437500** |
| `x_EV` | `(0; 0; 30; 70)` |
| `d_bar` | 27,500000 |
| `alpha_bar` | `(1; 0,9605; 0,76; 0,49)` |
| `kappa_bar` | 0,058500 |
| `z_EV`, problema sui parametri medi | 4,700000 |
| Costo atteso funding EEV | 1,350000 |
| `z_EEV`, rivalutazione negli scenari | **3,350000** |
| `x_WS`, scenari N e P | `(0; 0; 30; 70)` |
| `x_WS`, scenario R | `(0; 37,5; 62,5; 0)` |
| Obiettivi WS per N, P, R | `(4,7; 4,7; 3,4375)` |
| `z_WS` | **4,510625** |
| `VSS = z_SP - z_EEV` | **0,087500** |
| `EVPI = z_WS - z_SP` | **1,073125** |

È quindi verificato `3,35 <= 3,4375 <= 4,510625`. Il valore 4,7 del problema EV non va sostituito a EEV nella formula del VSS.

| Politica | Scenario | Liquidità dagli attivi | Funding `u` | Residuo `g` | Costo di scenario `kappa*u` | Contributo atteso `p*kappa*u` |
|---|---|---:|---:|---:|---:|---:|
| SP | N | 88,9 | 0 | 73,9 | 0 | 0 |
| SP | P | 77,5 | 0 | 42,5 | 0 | 0 |
| SP | R | 62 | 3 | 0 | 0,75 | 0,1125 |
| EV rivalutata | N | 67,5 | 0 | 52,5 | 0 | 0 |
| EV rivalutata | P | 49 | 0 | 14 | 0 | 0 |
| EV rivalutata | R | 29 | 36 | 0 | 9 | 1,35 |

Le cinque tabelle richieste sono riconoscibili, con i parametri medi esposti nella tappa EV e il confronto nella successiva tappa EEV. I due grafici sono leggibili e coerenti con i dati: il secondo mostra chiaramente funding 3 contro 36 nello scenario R.

La principale incompletezza negli output riguarda il **costo del funding per scenario**. Nella cella 7 la colonna «Costo funding scenario (p_s*k_s*u_s)» espone il contributo ponderato all'attesa, dichiarandone almeno la formula; manca il costo non ponderato richiesto per scenario. Nella cella 11 la stessa quantità ponderata è denominata semplicemente «Costo funding scenario», con maggiore ambiguità. Le somme attese e gli obiettivi sono corretti: il rilievo riguarda presentazione e distinzione economica delle grandezze, non la soluzione dell'ottimizzazione.

## 4. Prompt e regimi — 13/15

Il Prompt zero fissa contesto, fasi, limiti e responsabilità dello studente, incluso il divieto di delegare l'interpretazione finale. La Scheda Caso viene acquisita prima della costruzione del flusso e del codice. Lo studente valida flusso e scomposizione, procede per tappe e interviene su aspetti di formato e piccoli difetti tecnici. I prompt brevi di avanzamento sono ammissibili in questo contesto già fissato, secondo le Guidelines; non costituiscono di per sé delega globale.

Il diciannovesimo intervento, in Regime C, è particolarmente pertinente: parte dal VSS effettivamente ottenuto, 0,0875, e osserva che valori obiettivo vicini possono accompagnarsi ad allocazioni e fabbisogni di funding molto diversi nello scenario di run. Lo studente chiede di verificare il proprio ragionamento sugli output esistenti, senza cambiare modello né produrre una nuova soluzione. È un contributo autonomo sostanziale, non una generica richiesta di validazione.

Il passaggio successivo riconosce esplicitamente l'accoglimento della criticità e domanda quali celle debbano cambiare. La gestione dell'esito resta però incompleta: il tracciato termina con una validazione generale e il notebook non contiene un'elaborazione che chiuda la questione interpretativa sollevata. L'area dei regimi valuta questa mancata chiusura del processo; l'assenza della conclusione richiesta è valutata specificamente nell'ultima area.

La Scheda Costruzione indica 9–11 prompt, ma tale intervallo non compare nella Scheda Caso acquisita e non emerge una distinta comunicazione del limite allo studente. Poiché le Guidelines richiedono che il vincolo sia comunicato, **non si applica una penalizzazione automatica per i 21 interventi**. Il DOCX è il formato espressamente indicato dal docente per questa valutazione: nessuna penalizzazione per il formato.

## 5. Controlli e revisione critica — 11/15

Il notebook contiene verifiche effettive: somma delle probabilità; bilancio iniziale e bounds di SP ed EV; bilanci di liquidità e non negatività dei ricorsi SP ed EEV; successo dei solver; bilanci WS; VSS, EVPI e ordinamento dei valori. La non anticipatività SP, il mantenimento di `x_EV` e l'indipendenza dei problemi WS sono verificabili nella struttura del codice: non sarebbe corretto considerarli assenti solo perché accompagnati da semplici messaggi di conferma.

Restano tre limiti osservabili:

1. **Controlli WS sovradichiarati.** La cella 13 stampa il superamento dei controlli 2–6, ma dopo la soluzione verifica esplicitamente solo il bilancio di liquidità. Mancano i controlli numerici separati su somma delle allocazioni, limiti e non negatività. I vincoli sono correttamente imposti al solver e i risultati li rispettano: è una carenza di verifica esplicita, non un'inammissibilità della soluzione.
2. **Stato solver verificato dopo l'estrazione.** Nelle celle 7 e 9 si leggono `res.x` e `res.fun` prima di verificare `res.success`. Nella consegna tutte le risoluzioni riescono, ma il controllo andrebbe anticipato per evitare che un fallimento produca un errore prima del messaggio diagnostico. Nel problema EV manca inoltre un controllo esplicito del bilancio medio e dei ricorsi analogo a quello SP.
3. **Risposta IA conclusiva non riconciliata con gli output.** Alla domanda C l'IA risponde citando funding SP nello scenario R pari a **11,50**, costo **2,875** e riduzione rispetto a EEV di circa **68%**. Ripete il valore 11,50 nella risposta successiva. Il notebook e il grafico riportano invece **3**, costo **0,75** e riduzione **91,67%**. Lo studente non segnala la discrepanza e chiude con «Valido, quindi tutto il tracciato e il relativo notebook prodotti».

L'ultimo rilievo richiede una distinzione essenziale: **i numeri errati sono prodotti dall'IA e non vengono trasferiti nel notebook**. Non si attribuisce pertanto allo studente un errore computazionale o un'interpretazione finale scritta con quei numeri, né si applica una sanzione automatica per l'errore dell'IA. L'evidenza limita il giudizio sulla sostanzialità del controllo conclusivo dichiarato: nel materiale consegnato non risulta risolta una contraddizione direttamente verificabile con gli output.

Anche la spiegazione IA del VSS contenuto è incompleta: non basta richiamare il peso del 15% dello scenario R. Occorre confrontare il risparmio atteso sul funding con il rendimento lordo sacrificato. Questo approfondimento non risulta svolto dallo studente.

## 6. Interpretazione critica finale — 1/5

Il notebook termina con i grafici della cella 17. Manca il commento finale richiesto dalla sezione 6.3 della Scheda Caso. Le definizioni e le descrizioni metodologiche nelle celle precedenti non equivalgono a una lettura autonoma dei risultati ottenuti. La convalida generale della «Fase 8» nel tracciato non sostituisce tale commento.

Si riconosce **1 punto** per l'intuizione personale espressa nel prompt C: un VSS contenuto non implica identità delle allocazioni o dei fabbisogni per scenario. Non viene assegnato zero indistintamente a un lavoro che contiene questa evidenza autonoma. Mancano però la sua verifica quantitativa conclusiva, la discussione congiunta di VSS ed EVPI, la distinzione fra scelta implementabile e benchmark con informazione perfetta, e una valutazione dei limiti del modello.

L'offerta dell'IA di redigere il commento al posto dello studente è incompatibile con il ruolo stabilito dal Prompt zero, ma lo studente non la accetta chiedendo un testo sostitutivo: non si contesta quindi una delega della conclusione non documentata.

## Indicazioni formative per completare il lavoro

Le seguenti osservazioni sono del valutatore e non vengono attribuite allo studente ai fini del punteggio.

La conclusione dovrebbe partire dal confronto corretto:

`VSS = (3,55 - 4,70) + (1,35 - 0,1125) = -1,15 + 1,2375 = 0,0875`.

SP rinuncia a 1,15 di rendimento lordo e risparmia 1,2375 di costo atteso del funding. Il vantaggio atteso netto è quindi contenuto, mentre nello scenario R il funding passa da 36 a 3. Questo rende fondata l'osservazione dello studente sulla differenza fra una misura aggregata e il comportamento per scenario. Non rende il VSS una misura sbagliata: esso misura precisamente il vantaggio nell'obiettivo atteso del modello.

Il benchmark WS raggiunge 4,510625 scegliendo allocazioni diverse dopo aver conosciuto lo scenario; non è una politica iniziale implementabile con l'informazione disponibile. L'EVPI di 1,073125 misura il vantaggio teorico dell'informazione perfetta rispetto a SP, mentre il VSS confronta SP con la politica EV rivalutata. Il valore EV di 4,7 riguarda un diverso problema sui parametri medi e non rappresenta la prestazione attesa effettiva di quella politica.

La lettura finanziaria va limitata alle ipotesi assegnate: funding disponibile senza limite quantitativo, costo lineare, parametri e probabilità esogeni, due soli stadi e dati didattici su scala 100. Il modello descrive fabbisogni e costi di liquidità; non dimostra probabilità di insolvenza, capacità effettiva di reperire funding o dinamiche storiche di SVB. Il parametro kappa esprime un costo economico complessivo, non semplicemente un tasso di interesse di mercato.

Per completare l'elaborato occorre distinguere nelle tabelle `kappa*u` da `p*kappa*u`, rendere effettivi i controlli WS dichiarati, riconciliare la risposta IA con il funding corretto e scrivere un commento conclusivo autonomo. **Il giudizio di 78/100 riguarda esclusivamente il materiale consegnato**, senza attribuire credito anticipato a queste integrazioni.
