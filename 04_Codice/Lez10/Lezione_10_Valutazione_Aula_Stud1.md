# Valutazione dello studente 1 sul caso aula della lezione 10

Data della valutazione: 29 settembre 2026.

**Valutazione proposta: 72/100.** Il lavoro presenta un impianto computazionale sostanzialmente corretto e contributi iniziali pertinenti dello studente. La qualità della verifica è disomogenea e manca una vera interpretazione economico-finanziaria conclusiva. Il risultato non giustifica pertanto una valutazione di eccellenza.

Si applicano i sei pesi della sezione 15.11 delle [Guidelines](../../00_MasterPlan/MQF_Project_Guidelines.md), come richiesto dal docente anche per questo caso aula. La griglia è formulata nelle Guidelines con riferimento ai take-home: l'applicazione al caso aula è qui esplicita. I punteggi interni alle sei aree sono giudizi motivati del valutatore; le Guidelines non stabiliscono detrazioni automatiche per ciascun difetto. L'eventuale conversione lineare è **21,6/30**, senza applicare regole di arrotondamento non previste.

## Materiali ed evidenze

- [Scheda Caso Aula](Lezione_10_Scheda_Caso_Aula.md), assunta come specifica vincolante.
- [Notebook dello studente](Lezione_10_Notebook_Aula_Stud1.ipynb), composto da 15 celle, di cui 6 di codice; numerazione delle celle in questa relazione a partire da 1.
- [Tracciato IA in Word](Lezione_10_Tracciato_Aula_Stud1.docx), contenente l'esportazione della conversazione, inclusi i prompt dello studente e le risposte IA.
- [Rinvio al tracciato condiviso](Lezione_10_Tracciato_Aula_Stud1.md): <https://share.gemini.google/9t7cvvReRUxr>.
- [Scheda Costruzione Caso Aula](Lezione_10_Scheda_Costruzione_Caso_Aula.md), per i criteri metodologici pertinenti, e [Capitolo 9](../../01_Manuale/Capitoli/MQF_Cap_09_Markov_Misure_Rischio.tex), per la convenzione del CVaR discreto.

Il link condiviso è stato contattato e reindirizza a una pagina Gemini; l'accesso HTTP disponibile ha restituito l'involucro della pagina, senza il testo della conversazione. La valutazione del processo si basa quindi sull'esportazione locale Word, che contiene il percorso di lavoro fino alla validazione finale. Non si afferma di avere verificato l'identità tra l'esportazione e la versione attualmente pubblicata sul web. Il limite tecnico di accesso al link non determina alcuna penalizzazione.

La Scheda Costruzione presenta nella sezione 13 un richiamo a Lehman Brothers incoerente con il caso Evergrande assegnato. Questo refuso del materiale docente non è imputato allo studente e non modifica la specifica di valutazione.

## Punteggi per area

| Area delle Guidelines | Massimo | Assegnato | Motivazione sintetica |
|---|---:|---:|---|
| Prompt 2 — Flusso logico-teorico risolutivo | 30 | **23** | Contributo iniziale concreto e ordinato; formalizzazione e alcuni collegamenti decisivi sono completati dall'IA, con validazione dello studente poco argomentata. |
| Prompt 3 — Scomposizione input-output | 15 | **11** | Proposta iniziale presente e pertinente, con riuso degli stessi scenari; input, output intermedi e controlli non sono ancora esplicitati sistematicamente dallo studente. |
| Notebook Jupyter e output computazionali | 20 | **17** | Esecuzione riuscita, risultati riprodotti, parametri e meccanismo delle perdite corretti, quattro tabelle e tre figure; convenzione del CVaR da correggere e distribuzione delle differenze non esposta. |
| Prompt e uso dei regimi A/B/C | 15 | **12** | Contesto e vincoli fissati, validazioni anteriori al codice, uso pertinente del Regime C; documentazione delle verifiche sulle singole tappe e chiusura metodologica incomplete. |
| Verifiche logiche e controlli numerici | 15 | **9** | Controlli effettivi su diversi vincoli e buona correzione dimensionale; alcune verifiche sono tautologiche, dichiarative o troppo circoscritte. |
| Interpretazione critica finale | 5 | **0** | Non è presente un commento autonomo che interpreti risultati, politica di concentrazione e limiti del modello. |
| **Totale** | **100** | **72** | |

Le criticità del codice incidono nell'area del prodotto; la debolezza delle verifiche incide nell'area del controllo. L'assenza dell'interpretazione è valutata nella sua area specifica, senza ulteriori detrazioni automatiche nelle altre aree.

## Motivazione analitica

### Prompt 2

Lo studente propone una sequenza teorica non vuota: regime sistemico, migrazioni condizionate, default assorbente, distinzione tra perdite da migrazione e da default, aggregazione, distribuzione Monte Carlo, misure di rischio, concentrazione e confronto tra scenari con e senza crisi. Chiede espressamente di verificare, completare e ordinare la proposta, senza codice e senza cambiare modello. Sono evidenze positive del contributo personale osservabile, senza inferenze sulla storia privata del lavoro.

Nella proposta iniziale non sono però formalizzati il regime preciso della LGD, la riallocazione proporzionale, il confronto a traiettorie identiche e le definizioni operative delle misure di coda. Questi elementi vengono esplicitati dall'IA. La richiesta successiva di compattare il flusso in sei tappe è una scelta organizzativa dello studente, ma il raggruppamento concreto è elaborato dall'IA. La validazione «Valido la tua proposta» non documenta una verifica puntuale delle integrazioni.

Il flusso finale della cella 2 è coerente nell'impianto, ma la tappa sulle misure di rischio ne elenca i nomi senza fissarne le convenzioni. La prima risposta IA al Prompt 2 identifica inoltre il CVaR con la media condizionata sopra il VaR, senza la cautela necessaria per distribuzioni discrete; tale convenzione passa poi nel codice. Il rilievo non penalizza l'errore dell'IA in sé, ma il suo recepimento senza correzione.

### Prompt 3

Lo studente propone sei passaggi operativi, distingue simulazione e valorizzazione, e indica esplicitamente di ricalcolare le perdite del portafoglio limitato sugli stessi scenari. Chiede una tabella con input, operazione, output, controllo e uso successivo: il collegamento con il flusso teorico è riconoscibile.

La proposta personale resta tuttavia descrittiva. I controlli sono concentrati alla fine e gli oggetti intermedi non sono identificati puntualmente. La tabella dettagliata della cella 3 è prodotta dall'IA e convalidata senza motivazione analitica. Il punteggio riconosce la buona base iniziale, senza attribuire integralmente allo studente il dettaglio introdotto dall'assistente.

### Notebook e output

Le sei celle di codice sono state eseguite in sequenza in un processo Python pulito, con backend grafico non interattivo. Non si sono verificati errori; gli assert sono passati e le tabelle numeriche coincidono con gli output salvati alla precisione esposta. Le tre immagini incorporate sono state ispezionate: sono leggibili e pertinenti. La figura 2 potrebbe usare una scala verticale più adatta alla coda, ma resta interpretabile.

Sono corretti i parametri, la composizione dei portafogli, il totale di 200 milioni, la riduzione di Evergrande a 20 milioni, la riallocazione BBB/BB e l'impiego delle stesse traiettorie. La simulazione conserva M0,...,M3 e usa Mt per la transizione creditizia t→t+1. Il tempo di primo default e la LGD al regime M_(tau-1) sono implementati correttamente; le perdite da migrazione si applicano soltanto ai non-default.

La cella 11 costruisce `delta_L_sim`: il campione empirico delle differenze esiste, ma non viene esposto mediante una distribuzione, una tabella o una sintesi adeguata oltre alla media. Non si tratta quindi di un calcolo mancante, bensì di una restituzione incompleta dell'output richiesto. Non si impone una quarta figura come requisito autonomo: la Scheda Caso ne richiede tre.

La cella 13 usa `np.percentile` con interpolazione predefinita e `mean(loss_vec[loss_vec >= var_alpha])`. Nel caso discreto, quest'ultima espressione include tutta la massa al quantile e non garantisce una coda di probabilità esattamente 1-alpha. Il Capitolo 9 distingue esplicitamente questa media condizionata dal CVaR. Con 50.000 osservazioni, per i livelli assegnati, il CVaR empirico coerente si ottiene mediando rispettivamente le peggiori 2.500 e 500 perdite ordinate.

| Misura | Notebook base | CVaR corretto base | Notebook limite | CVaR corretto limite |
|---|---:|---:|---:|---:|
| CVaR 95%, milioni USD | 69,037542 | 69,044556 | 63,225760 | 63,228954 |
| CVaR 99%, milioni USD | 79,636240 | 79,636240 | 73,446910 | 73,456771 |

L'impatto numerico è piccolo su questo campione, ma la distinzione teorica è rilevante. Anche il VaR empirico andrebbe allineato al quantile inverso della funzione di ripartizione: il VaR 99% base è 74,7200, contro 74,7201 prodotto dall'interpolazione. Non è un errore sostanziale della simulazione del rischio di credito.

### Uso dei regimi e qualità del tracciato

Sono presenti Prompt zero, Scheda Caso nel Prompt 1, proposta teorica, proposta operativa, validazioni esplicite, sei richieste progressive di implementazione e una verifica critica in Regime C. Il codice arriva dopo la convalida della specifica e della scomposizione. Il notebook recepisce la sostituzione della Tappa 5 richiesta dopo la correzione delle unità.

I prompt «Tappa 3», «Tappa 4» e analoghi sono brevi ma legati al contesto già fissato: la sezione 15.9 ammette espressamente questa forma dopo il Prompt zero. Non sono trattati come deleghe generiche dell'intero caso. Rimane poco documentata l'analisi degli output effettivi dopo ciascuna tappa: il passaggio successivo indica prosecuzione, non dimostra da solo una verifica.

Il tracciato contiene 19 interventi utente, contando apertura, conferme e richieste di formato. L'intervallo 11–15 compare nella Scheda Costruzione come indicazione preliminare, ma non nella Scheda Caso consegnata. Non si applica una penalizzazione automatica per il conteggio, anche perché non tutti gli interventi costituiscono prompt metodologici autonomi.

### Controlli

La criticità formulata dallo studente sulle unità della varianza è pertinente e ha valore didattico: lo studente distingue un possibile errore di etichetta da un errore di calcolo e chiede una verifica circoscritta. La correzione a `(M$)^2` è presente nel notebook finale. Si riconosce quindi un uso effettivo del Regime C.

Il report finale con 17 esiti `True` sovrastima però la forza di alcune verifiche:

- **Controllo 6, cella 9:** `ctrl_6 = True` non è un test. Le estrazioni indipendenti sono giustificate dalla struttura del generatore e del codice, che è corretta; il booleano non costituisce una verifica aggiuntiva.
- **Controllo 15, cella 9:** controlla soltanto che i primi tre scenari partano da S. L'array `expected_M_head` non viene usato. Non verifica la riproducibilità dichiarata.
- **Controlli 8 e 10, cella 11:** verificano un solo caso in default e un solo caso senza default, entrambi sul portafoglio base. Non giustificano da soli le affermazioni generali stampate.
- **Controllo 13, cella 11:** controlla dimensioni degli array; il riuso delle traiettorie è effettivo nelle chiamate alle funzioni, ma non viene provato dal test dimensionale.
- **Controllo 14:** ricalcola la medesima somma utilizzata per costruire il totale; utile contro modifiche accidentali, poco indipendente come verifica del modello.
- **Controllo 16, cella 13:** confronta 25.000 e 50.000 osservazioni, ma soltanto per media e VaR 95% del portafoglio base. È un controllo reale, tuttavia non copre CVaR, livello 99% e portafoglio limitato.
- **Controllo 17:** verifica ordinamenti necessari delle misure, ma tali disuguaglianze non certificano la corretta convenzione del CVaR.

La riesecuzione indipendente del valutatore con lo stesso seed ha restituito array M, X e tau identici. Questo conferma che il codice è riproducibile, ma non trasforma retroattivamente il controllo 15 dello studente in una prova adeguata.

### Interpretazione finale

Il notebook termina con il report dei controlli. Nel tracciato lo studente conclude che i risultati sono consistenti e valida tutto il lavoro, ma non interpreta quantitativamente gli esiti. Non discute la riduzione delle misure di coda, la persistenza del rischio sistemico, l'assenza di miglioramento in ogni singolo scenario o i limiti della calibrazione didattica.

Non vi è evidenza di un'interpretazione finale delegata all'IA: l'interpretazione semplicemente manca. La dichiarazione di validazione non soddisfa il criterio delle Guidelines e non consente di assegnare punti nell'area dedicata.

## Risultati verificati dal valutatore

| Quantità | Portafoglio base | Portafoglio limite | Differenza limite meno base |
|---|---:|---:|---:|
| Perdita media, milioni USD | 26,2337 | 24,9138 | -1,3199 |
| Varianza, milioni USD al quadrato | 276,6052 | 225,6674 | -50,9379 |
| Deviazione standard, milioni USD | 16,6315 | 15,0222 | -1,6092 |
| VaR 95% del notebook, milioni USD | 60,2700 | 55,2400 | -5,0300 |
| VaR 99% del notebook, milioni USD | 74,7201 | 68,5164 | -6,2037 |

La probabilità simulata di raggiungere C in M0,...,M3 è 0,37146, coerente con il valore esatto 0,371112 ottenuto dalla sottomatrice di Q sugli stati N e S. I default medi sono 5,34604. Le perdite medie base con e senza ingresso in C sono rispettivamente circa 40,9945 e 17,5103 milioni.

La riduzione media della perdita è circa il 5,03%; quella del VaR 95% è circa l'8,35%. Il portafoglio limitato presenta però una perdita maggiore nel 52,506% delle repliche. Le misure aggregate migliorano grazie alla dimensione delle riduzioni negli scenari sfavorevoli, non perché la politica riduca la perdita in ogni scenario. Questo dato, calcolato dal valutatore, è un esempio di analisi che avrebbe potuto sostenere la conclusione dello studente: non gli viene attribuito come lavoro svolto.

## Restituzione allo studente

Il contributo iniziale e la costruzione del modello sono buoni. Per migliorare il lavoro occorre formalizzare le convenzioni di VaR e CVaR, rendere i controlli coerenti con ciò che dichiarano di verificare, presentare la distribuzione delle differenze di perdita e scrivere una conclusione autonoma fondata sui risultati e sui limiti del caso. La correzione delle unità della varianza è un esempio positivo del tipo di controllo critico da estendere al resto del notebook.
