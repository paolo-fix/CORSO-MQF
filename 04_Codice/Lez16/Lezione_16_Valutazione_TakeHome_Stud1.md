# Valutazione dello studente 1 — Lezione 16, take-home: nuova consegna

Data: 10 ottobre 2026.

**Valutazione proposta: 67/100.** La nuova consegna implementa correttamente SP, il problema deterministico medio e WS, e documenta un intervento autonomo significativo contro una modifica del modello introdotta dall'IA. La correzione finale rimane però incompleta: alla decisione EV inammissibile viene attribuito un valore economico finito, da cui un VSS negativo. Due controlli finali restituiscono esplicitamente `False`, senza successiva correzione prima della convalida. Manca inoltre l'interpretazione finale autonoma.

Questa valutazione riguarda la **nuova traccia two-stage** «UK LDI 2022 — Buffer di liquidità, margin call e valore dell'informazione». La [valutazione precedente](Lezione_16_Valutazione_TakeHome_Stud1.md) riguarda una diversa formulazione multistadio e viene conservata. I due punteggi non misurano semplicemente il miglioramento o peggioramento della stessa soluzione.

## Fonti, criteri e verifiche

Si applica la griglia della sezione 15.11 delle [Guidelines](../../00_MasterPlan/MQF_Project_Guidelines.md): 30, 15, 20, 15, 15 e 5 punti. I punteggi parziali sono giudizi motivati entro questi pesi, non detrazioni automatiche prescritte. L'equivalente puramente lineare è **20,1/30**, senza assumere una regola istituzionale di conversione o arrotondamento.

Sono stati verificati i contenuti presenti su GitHub, repository `paolo-fix/CORSO-MQF`, ramo `main`, e la corrispondenza con i file locali:

| Documento | Identificativo Git del contenuto |
|---|---|
| Guidelines | `c97461e513ef986d964e5fc92568d7cd14942c0c` |
| [Nuova Scheda Caso](Lezione_16_Scheda_Caso_TakeHome.md) | `eb8fa6c0b70d3b32fdfc82f3c60bd6322b5a4a83` |
| [Nuova Scheda Costruzione](Lezione_16_Scheda_Costruzione_Caso_TakeHome.md) | `732811b7232df0a9db2433344c7118ce65e33f3c` |
| [Nuovo notebook](Lezione_16_Notebook_TakeHome_Stud1.ipynb) | `8dd6ccabb961befe56ecca60da861a2fcabb6602` |
| [Nuovo tracciato DOCX](Lezione_16_Tracciato_TakeHome_Stud1.docx) | `ea7a3081a51d026b97f64ed965ead2f6dc32c670` |

Per il DOCX, il connettore GitHub ha restituito l'identificativo ma non il contenuto binario: è stata letta la copia locale, il cui hash Git coincide esattamente. Il documento contiene 25 interventi utente, inclusa l'apertura con il titolo; non contiene immagini incorporate. La lettura è avvenuta direttamente dal DOCX, senza dipendere dal link alla conversazione online.

Il notebook contiene 17 celle, delle quali 7 di codice. La numerazione delle celle qui citata parte da 1. Le sette celle sono state eseguite in ordine in un processo Python pulito: **tutti gli output standard coincidono esattamente con quelli salvati**, compresi il VSS negativo e i controlli falliti. I tre grafici incorporati sono stati ispezionati. La riesecuzione non termina con eccezioni; questo non implica correttezza dei risultati. Gli avvisi del backend grafico non interattivo non sono difetti della consegna; il warning sulla sequenza `\l` nella stringa del titolo è un dettaglio tecnico secondario.

Una formulazione indipendente ridotta, con variabili `h=x2`, `e_s,f_s`, eliminazione di `x1=100-h` e del residuo `g_s`, conferma gli ottimi e l'inammissibilità della rivalutazione EV nello scenario E. Essa impone `(1+alpha_s)*h-e_s-beta_s*f_s <= 100`, `50 <= h <= 100`, `e_s <= 4`, `f_s <= 25`. Il vincolo `f_s <= h` è automaticamente soddisfatto in questo dominio. I controlli del valutatore non sono attribuiti allo studente. Notebook, tracciato e schede non sono stati modificati.

## Griglia numerica

| Area | Massimo | Assegnato | Motivazione sintetica |
|---|---:|---:|---|
| Prompt 2 — Flusso logico-teorico | 30 | **24** | Proposta personale pertinente, distinzione EV/rivalutazione e WS; formalizzazione prevalentemente affidata all'IA e fattibilità del ricorso non sviluppata inizialmente. |
| Prompt 3 — Scomposizione input-output | 15 | **13** | Sequenza coerente, rivalutazione a decisione fissata e controlli previsti; gestione degli esiti inammissibili e traduzione dei controlli non pienamente governate. |
| Notebook e output computazionali | 20 | **12** | SP, problema medio e WS corretti; valore rivalutato EV e VSS errati, con propagazione a tabella e grafico dei benchmark. |
| Prompt e regimi A/B/C | 15 | **11** | Intervento C autonomo e fondato, rimozione di deficit e penalità; revisione incompleta e superamento dell'intervallo di prompt esplicitamente comunicato. |
| Verifiche logiche e controlli numerici | 15 | **7** | Controlli parziali e diagnosi critica pertinente; residuali non validati esplicitamente e due esiti finali negativi lasciati irrisolti. |
| Interpretazione critica finale | 5 | **0** | Nessuna conclusione autonoma sui risultati effettivi e sui limiti del modello. |
| **Totale** | **100** | **67** | |

Si distingue l'errore nel prodotto, cioè il calcolo scorretto di EV/VSS, dalla responsabilità verificativa, cioè la convalida nonostante gli avvisi osservabili. Non si applicano penalità fisse ripetute per ogni tabella o figura in cui lo stesso errore si propaga. L'intervento C è valorizzato anche se non risolve integralmente il problema.

## 1. Questione preliminare: incoerenza della calibrazione docente

La sezione 10 della nuova Scheda Costruzione riporta `x_SP=(25,75)`, `z_SP=3,7375`, `x_EV=(16,25;83,75)`, `z_EV=3,5445833` e `z_WS=4,43125`. **Questi valori non risultano dalla Scheda Caso vincolante e dai parametri effettivamente assegnati.**

La verifica indipendente restituisce invece `x_SP=(20,80)`, `z_SP=3,944`, `x_EV=(0,100)` e `z_WS=4,506428571`. Anche il solo piano `(25,75)`, rivalutato correttamente con i dati assegnati, dà `3,893333333`, non `3,7375`: il rendimento iniziale è 4 e il ricorso nello scenario E costa `0,08*(5/0,75)`, ponderato con probabilità 0,2.

Inoltre, i parametri della Scheda Caso rendono la decisione media inammissibile nello scenario estremo. La traccia richiede un valore rivalutato e un grafico dei benchmark senza esplicitare la gestione di questo caso. È una criticità della progettazione/calibrazione del materiale docente, da distinguere dal lavoro dello studente.

**Non vengono penalizzati né i risultati SP e WS corretti ma diversi dalla calibrazione docente, né l'emergere dell'inammissibilità di EV.** Non si pretende un VSS finito che i dati non consentono. Si valuta invece la scelta, presente nel notebook finale, di costruire comunque un valore finito utilizzando ricorsi che non soddisfano il bilancio. La specifica vincolante non autorizza a cambiare parametri o a introdurre una penalità per ottenere i risultati attesi dalla Scheda Costruzione.

## 2. Prompt 2 — 24/30

Nel quarto intervento lo studente propone sette passaggi: separazione delle decisioni iniziali dai ricorsi; scenari e parametri; bilanci e bounds; SP; problema medio seguito dalla rivalutazione negli scenari originali; WS; confronto dei benchmark. Chiede all'IA di verificare e completare senza codice e senza modificare il modello. Nel quinto intervento propone di compattare il flusso in sei passaggi.

La proposta è specifica e ordinata. Distingue già il problema medio dalla valutazione della decisione sotto incertezza, evitando una confusione concettuale frequente. Non è una richiesta generica di costruire l'intero flusso. La tabella finale della cella 2 collega formulazione, output e controlli.

La formalizzazione personale rimane però soprattutto verbale: le equazioni, le formule dei valori e l'individuazione del dominio di fattibilità del ricorso sono esplicitate dall'IA. Non viene inizialmente discussa la possibilità che `x_EV` non disponga di ricorso ammissibile. Non si addebita allo studente il mancato ottenimento di un benchmark finito, ma non è documentato pieno controllo delle condizioni sotto cui le formule producono valori reali finiti.

Il successivo intervento C dimostra una comprensione effettiva del vincolo di bilancio e dell'effetto delle variabili aggiunte sul dominio ammissibile. Questa evidenza sostiene il giudizio positivo sul contributo teorico. I riferimenti ai «Controlli 4.x» nella tabella sono imprecisi rispetto alla numerazione 7.x della nuova Scheda Caso; il contenuto dei controlli resta riconoscibile e il refuso non è trattato come errore matematico.

## 3. Prompt 3 — 13/15

Nel sesto intervento lo studente propone sette tappe coerenti con il flusso. Distingue costruzione dei vincoli, ottimizzazione SP, ottimizzazione media, rivalutazione a `x_EV` fissata, problemi WS separati e sintesi dei risultati. Inserisce esplicitamente coerenza dei dati, ordinamento dei benchmark e non negatività degli indicatori.

La proposta rende osservabili il contributo personale e i collegamenti tra le operazioni. La scomposizione viene convalidata prima del codice. La tabella della cella 3 identifica correttamente gli output da utilizzare nelle tappe successive, ma non prevede un percorso esplicito per un sottoproblema inammissibile. Inoltre, nella consegna alcuni controlli promessi dalla tabella, come residuali entro tolleranza e rispetto di tutti i limiti, non diventano verifiche effettive complete. La proposta operativa è buona; la sua realizzazione e validazione non raggiungono la stessa completezza.

## 4. Notebook e risultati — 12/20

### Parti corrette

La formulazione finale SP usa le 11 variabili previste, senza deficit aggiuntivi e senza penalità M. La decisione iniziale è comune ai tre scenari; i ricorsi sono distinti. Bilanci, bounds, pesi probabilistici, vincolo minimo LDI e `f_s <= x2` sono implementati correttamente. Il solver è controllato prima dell'estrazione delle soluzioni SP, EV e WS.

Il problema medio usa le quattro medie prescritte e viene tenuto distinto dalla rivalutazione. WS risolve tre problemi con decisioni iniziali specifiche e ne pondera correttamente i valori.

| Quantità | Risultato verificato |
|---|---:|
| `x_SP` | **(20; 80)** |
| Rendimento iniziale SP | 4,2 |
| Costo atteso di ricorso SP | 0,256 |
| `z_SP` | **3,944000** |
| `alpha_bar` | 0,205 |
| `beta_bar` | 0,920 |
| `kappa_bar` | 0,052 |
| `lambda_bar` | 0,0275 |
| `x_EV` | **(0; 100)** |
| Ottimo del problema medio | **4,387228261** |
| `z_WS` | **4,506428571** |
| `EVPI` | **0,562428571** |

I ricorsi SP sono:

| Scenario | Margin call | `e` | `f` | `g` | Costo di ricorso |
|---|---:|---:|---:|---:|---:|
| N | 8 | 0 | 0 | 12 | 0 |
| S | 20 | 0 | 0 | 0 | 0 |
| E | 32 | 0 | 16 | 0 | 1,28 |

I risultati WS sono:

| Scenario | Buffer | Esposizione LDI | Valore WS |
|---|---:|---:|---:|
| N | 0 | 100 | 4,95 |
| S | 20 | 80 | 4,2 |
| E | 28,571429 | 71,428571 | 3,857143 |

### Errore nella rivalutazione EV: cella 13

Con `x_EV=(0,100)`, i ricorsi ottimi sono ammissibili in N (`e=0,f=10,g=0`, costo 0,05) e S (`e=2,5,f=25,g=0`, costo 0,9). Nello scenario E:

`margin call = 0,40*100 = 40`;

`liquidità massima = 0 + 4 + 0,75*25 = 22,75`.

Mancano **17,25 unità**. Non esiste una terna ammissibile `e,f,g` che soddisfi il bilancio. Il solver lo rileva correttamente con stato di inammissibilità.

Il codice finale intercetta il fallimento, inserisce manualmente `e=4,f=25,g=0` e calcola un costo di 2,48. Questi valori descrivono la capacità massima disponibile, **non una soluzione di ricorso ammissibile**: il residuo del bilancio è `22,75-40=-17,25`.

La variabile `z_ev_valid` viene inizialmente posta a `-np.inf`. La riga successiva sostituisce però questo esito con un valore finito ottenuto usando i costi delle righe tabellari, inclusa quella inammissibile:

`z_EV = 5 - (0,5*0,05 + 0,3*0,9 + 0,2*2,48) = 4,209`.

Ne deriva `VSS = 3,944 - 4,209 = -0,265`. **Né 4,209 né -0,265 sono benchmark validi per il modello assegnato.** La dicitura «Inammissibile» nella tabella è corretta ma non rende valido il valore aggregato costruito subito dopo.

La gestione corretta, senza cambiare modello, è dichiarare la politica EV non ammissibile negli scenari originali e il suo valore non disponibile come risultato economico finito. Adottando esplicitamente la convenzione della funzione valore estesa per un problema di massimizzazione, si ha `Q_E(x_EV)=-infinito`, quindi `z_EV=-infinito` e `VSS=+infinito`. Questa è una convenzione matematica per l'inammissibilità, non un guadagno monetario finito né una nuova penalità economica. Si può anche presentare VSS come non finitamente valutabile, motivando l'esito.

### Output

Le cinque tabelle e i tre grafici sono presenti; vengono esposti anche parametri medi, valore del problema medio e soluzioni WS. Le prime due figure sono leggibili e corrette. La terza visualizza il falso valore 4,209 come prestazione della politica EV e mostra una barra EV superiore a SP, mentre il titolo dichiara l'ordinamento opposto. L'errore della rivalutazione si propaga quindi alla Tabella 5 e alla Figura 3; non è un difetto di disegno del grafico, ma del dato rappresentato.

Nella tabella di rivalutazione manca inoltre il contributo economico scenario-specifico richiesto: sono esposti i costi. Per E tale contributo non potrebbe comunque essere presentato come valore finito ammissibile. Mancano le brevi interpretazioni dei grafici richieste dalla Scheda Caso; la carenza interpretativa è considerata nell'ultima area.

## 5. Prompt e regimi — 11/15

Il contesto e i vincoli sono fissati con Prompt zero e Scheda Caso. Sono presenti proposte personali per Prompt 2 e Prompt 3, sviluppo per tappe, una correzione tecnica del `KeyError` e un confronto esplicito sulla gestione dell'inammissibilità. I prompt brevi di avanzamento sono ammissibili perché collegati a un contesto già definito.

La parte più significativa è il ventiduesimo intervento. Lo studente confronta notebook e Scheda Caso, identifica l'aggiunta di `d_s` e M e spiega perché una variabile che consente di coprire un deficit pagando una penalità cambia l'insieme ammissibile. Chiede un esito esplicito di accoglimento o rigetto, vieta nuove ipotesi e richiede soltanto celle sostitutive e indicazioni di riesecuzione. Si tratta di una critica teorico-modellistica fondata, di maggior valore rispetto alla sola segnalazione di un errore di sintassi.

La risposta IA accoglie la criticità e il notebook finale elimina effettivamente `d_s` e M: questo miglioramento va riconosciuto. Non si penalizza automaticamente l'errore iniziale dell'IA come se fosse rimasto integralmente nel modello finale. Tuttavia, il ritorno alla specifica non viene verificato fino in fondo: rimane il calcolo sostitutivo finito per lo scenario inammissibile.

Alla richiesta di riesecuzione, intervento 23, l'IA dichiara di avere svolto un controllo «mentalmente», ma afferma anche una convergenza in 0,01 secondi e una soluzione SP `(2,25;97,75)` «o combinazione analoga», poi rassicura che VSS è positivo e tutti gli ordinamenti risultano `True`. Non è una prova di esecuzione. La soluzione citata non è neppure ammissibile in E: la capacità massima è `2,25+22,75=25`, contro una margin call di 39,1. Il notebook restituisce invece `(20,80)` e due `False`. La convalida finale non riconcilia questi elementi. L'errore numerico della risposta IA non viene trasferito nella soluzione SP del notebook; rileva qui la debolezza della validazione della rassicurazione ricevuta.

Diversamente dalla vecchia traccia, la **nuova Scheda Caso comunica esplicitamente il limite di 9–11 prompt**. Il tracciato contiene 25 interventi, o 24 escludendo l'apertura con il titolo. Il limite è superato anche con questa esclusione. Il conteggio comprende debugging, ripartenza e revisione, e la correzione C resta meritoria; il superamento è considerato moderatamente nel giudizio organizzativo dell'area, senza inventare una detrazione per ogni messaggio né un tetto al voto non previsto dalle Guidelines.

## 6. Verifiche e controlli — 7/15

Sono effettivi i controlli sulla somma delle probabilità, su alcuni parametri di primo stadio, sulle dimensioni delle matrici e sul successo dei solver SP, medio e WS. La costruzione dei sottoproblemi EV mantiene correttamente fissa la decisione iniziale e consente di rilevare l'inammissibilità di E. L'intervento critico autonomo sul deficit aggiunto è un punto positivo sostanziale.

La verifica finale rimane però insufficiente:

1. Nella cella 7 si dichiarano validati i vincoli controllando soprattutto forme delle matrici e numero di bounds. Questo verifica la struttura, non l'ammissibilità numerica della soluzione.
2. Nella cella 9 vengono calcolati `res_eq` e `max_res_eq`, ma non sono esposti né confrontati con una tolleranza tramite un controllo. Mancano verifiche numeriche esplicite complete dei bounds e dei bilanci delle soluzioni estratte, richieste dalla sezione 7 della traccia.
3. Nella cella 13 qualsiasi insuccesso del solver entra nel ramo etichettato come inammissibilità, senza distinguere `status == 2` da altri possibili fallimenti. Nel caso concreto lo stato è realmente di inammissibilità, ma la gestione generale non è rigorosa.
4. La cella 17 verifica le disuguaglianze mediante booleani e stampa **`z_EV <= z_SP: False`** e **`VSS >= 0: False`**. Un controllo osservabile esiste: non va descritto come assente. È però lasciato senza indagine o correzione, nonostante la Scheda Caso richieda espressamente di investigare le violazioni prima dell'interpretazione finale.

Non è obbligatorio risolvere questo problema soltanto con un `assert`: è necessario gestire l'esito e impedire che un benchmark non valido venga presentato come conclusione verificata. La frase finale dello studente «Valido ... tutto il tracciato e il relativo notebook» non trova riscontro negli stessi output salvati.

L'assenza di ricorso ammissibile non è un errore di esecuzione da nascondere. Il controllo avrebbe dovuto fermare il calcolo di un VSS finito e motivare l'esito. La distinzione fra notebook che termina e notebook matematicamente validato è il principale obiettivo formativo ancora da consolidare.

## 7. Interpretazione finale — 0/5

Il notebook termina con la cella dei grafici; non contiene una conclusione autonoma che discuta buffer, ricorso, inammissibilità della politica EV, valore dell'informazione e limiti del modello. Anche le brevi letture economiche dei singoli grafici non sono presenti. Le descrizioni delle tappe spiegano la procedura, ma non sostituiscono un commento dei risultati effettivi.

La critica dello studente alla variabile `d_s` è un contributo autonomo importante, già riconosciuto nelle aree teorica, dei regimi e dei controlli. Non costituisce tuttavia la conclusione finanziaria richiesta. Non si contesta una conclusione finale delegata all'IA: in questa nuova consegna la conclusione manca. La convalida generale della Fase 8 non la sostituisce.

## Indicazioni formative e nota al docente

Per completare il lavoro occorre preservare l'inammissibilità rilevata in E, evitando il calcolo sostitutivo `z_EV=4,209`. La tabella dovrebbe riportare l'assenza di una soluzione ammissibile, distinguendo eventuali quantità diagnostiche di capacità massima dai ricorsi ottimi. Il confronto grafico dovrebbe segnalare che EV non ha un valore finito ammissibile, senza disegnare una barra numerica arbitraria o tentare di rappresentare l'infinito come valore finito.

Il buffer SP di 20 copre la margin call nello scenario S. In E la margin call è 32: le 12 unità mancanti vengono ottenute liquidando 16 unità di esposizione, con efficacia 0,75 e costo 1,28. L'obiettivo è quindi `4,2 - 0,2*1,28 = 3,944`. Per ogni scenario il costo del deleveraging per unità di liquidità, `lambda_s/beta_s`, è inferiore a `kappa_s`; nella soluzione SP non occorre liquidità esterna, poiché la capacità di deleveraging è sufficiente.

L'assenza di buffer della politica media è compatibile con lo scenario medio, ma non con E. Con i limiti assegnati, la fattibilità in E richiede almeno `x1 >= 12,321429`, ottenuto da `x1 + 22,75 >= 0,4*(100-x1)`. Questo è un controllo diagnostico sul modello esistente, non un nuovo vincolo da aggiungere surrettiziamente al problema medio. SP sceglie un buffer maggiore per ottimizzare il rendimento netto atteso. WS può adattare anche il primo stadio allo scenario noto anticipatamente e dà un EVPI finito di 0,562429.

La conclusione autonoma dovrebbe collegare questi numeri al compromesso rendimento/liquidità e ricordare che probabilità, costi, efficacia delle liquidazioni e limiti operativi sono stilizzati ed esogeni. Il modello non rappresenta feedback dei prezzi, dinamiche intraday o una calibrazione storica di un fondo LDI.

**Nota al docente:** la calibrazione della Scheda Costruzione va riconciliata con i parametri della Scheda Caso prima di un nuovo utilizzo. Se si desidera un VSS finito, occorre una revisione esplicita della progettazione del caso; non spetta allo studente modificare di propria iniziativa dati o ricorso. Se si conservano questi parametri, è opportuno rendere esplicita nella consegna la possibilità di inammissibilità della politica EV e la modalità di esposizione del benchmark.

Il **67/100** valuta la consegna osservata, riconoscendo la criticità della calibrazione docente e il merito dell'intervento C, senza attribuire credito anticipato alle correzioni qui suggerite.
