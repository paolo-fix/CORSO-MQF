# Valutazione del caso aula della lezione 10 — Studente 1

Data: 2 ottobre 2026.

**Valutazione proposta: 72/100.** Il lavoro presenta un contributo iniziale pertinente e un modello computazionale sostanzialmente corretto. Le verifiche documentate sono disomogenee e manca l'interpretazione critica finale autonoma.

## Materiali e criterio

La fonte del processo IA è esclusivamente [il tracciato DOCX](Lezione_10_Tracciato_Aula_Stud1.docx). Il PDF e il link web non sono utilizzati nella presente valutazione. Il prodotto computazionale è valutato attraverso [il notebook del caso aula](Lezione_10_Notebook_Aula_Stud1.ipynb). La specifica del caso è quella riportata nel Prompt 1 del DOCX.

Si applicano i sei pesi della [sezione 15.11 delle Guidelines](../../00_MasterPlan/MQF_Project_Guidelines.md), con le indicazioni sulla validazione e sul tracciato delle sezioni 15.8–15.10. La griglia numerica, presentata con riferimento ai take-home, è applicata a questo caso aula su richiesta del docente. I massimi derivano dalle Guidelines; i punteggi entro ciascuna area sono giudizi motivati, perché non sono previste detrazioni automatiche per ogni difetto.

La conversione puramente lineare è **21,6/30**; non si applicano arrotondamenti non prescritti. Si valuta il contributo osservabile dello studente, senza inferenze sull'intera storia privata del lavoro con IA.

## Punteggi

| Area | Massimo | Assegnato | Motivazione sintetica |
|---|---:|---:|---|
| Prompt 2 — Flusso logico-teorico risolutivo | 30 | **23** | Proposta personale concreta e ordinata; formalizzazione e collegamenti specifici completati dall'IA, con validazione poco argomentata. |
| Prompt 3 — Scomposizione input-output | 15 | **11** | Proposta operativa pertinente, con riuso degli scenari; input, output intermedi e controlli non ancora esplicitati sistematicamente dallo studente. |
| Notebook Jupyter e output computazionali | 20 | **17** | Modello corretto, esecuzione riuscita, tabelle e grafici presenti; convenzione del CVaR da correggere e distribuzione delle differenze non adeguatamente presentata. |
| Prompt e uso dei regimi A/B/C | 15 | **12** | Contesto e vincoli fissati, validazioni prima del codice, sviluppo progressivo e uso effettivo del Regime C; controlli delle risposte di tappa poco documentati. |
| Verifiche logiche e controlli numerici | 15 | **9** | Controlli effettivi su diversi vincoli e buona critica dimensionale; alcune verifiche sono dichiarative, troppo circoscritte o non dimostrano la proprietà annunciata. |
| Interpretazione critica finale | 5 | **0** | Nessuna conclusione autonoma quantitativa sul significato finanziario dei risultati e sui limiti del modello. |
| **Totale** | **100** | **72** | |

L'uso dell'IA non costituisce di per sé motivo di penalizzazione. I difetti del prodotto e quelli delle verifiche sono trattati nelle rispettive aree; l'assenza della conclusione è valutata nell'area dedicata.

## Evidenze e motivazioni

I riferimenti agli interventi indicano l'ordine dei 19 paragrafi del DOCX che iniziano con `User prompt:`. Le celle del notebook sono numerate a partire da 1.

### Prompt 2 — 23/30

Nell'intervento 5 lo studente propone regime sistemico, migrazioni condizionate, default assorbente, distinzione tra perdite da migrazione e default, aggregazione, distribuzione Monte Carlo, misure di rischio, concentrazione e confronto tra scenari con e senza crisi. Chiede all'IA di verificare, completare e ordinare la sequenza senza codice e senza cambiare modello. Il contributo è concreto e collegato alla domanda quantitativa, non una richiesta generica di soluzione.

La proposta resta prevalentemente descrittiva: non formalizza il regime preciso della LGD al primo default, la riallocazione proporzionale, il confronto a traiettorie identiche e le convenzioni delle misure di coda. Questi aspetti sono completati dall'IA. Nell'intervento 6 lo studente sceglie di compattare il flusso in sei tappe, ma il raggruppamento concreto è elaborato dall'assistente. La conferma dell'intervento 7, «Valido la tua proposta», è accettazione osservabile, senza verifica puntuale delle integrazioni. La tabella finale della cella 2 è coerente nell'impianto; non esplicita le convenzioni del CVaR.

### Prompt 3 — 11/15

Nell'intervento 9 lo studente distingue dati, simulazione, valorizzazione, misure di rischio, portafoglio limitato e output. Specifica di ricalcolare le perdite sugli stessi scenari simulati e richiede una tabella con input, operazione, output, controllo e uso successivo. Questi elementi soddisfano diversi indicatori positivi delle Guidelines.

La proposta personale non identifica però in modo sistematico gli oggetti intermedi e concentra i controlli alla fine. Il dettaglio della tabella input-output è introdotto dall'IA; l'intervento 10 convalida la scomposizione senza motivazione analitica. Il punteggio riconosce la base operativa personale, senza attribuire integralmente allo studente il dettaglio dell'assistente.

### Notebook e output — 17/20

Il notebook contiene 15 celle, 6 di codice. Le celle computazionali sono state rieseguite in sequenza: tutti gli assert passano. Sono corretti i parametri assegnati, la composizione dei due portafogli, il totale di 200 milioni, Evergrande a 20 milioni e la riallocazione proporzionale a BBB e BB. Le due valorizzazioni usano gli stessi array sistemici e creditizi.

La simulazione conserva M0,…,M3 e usa Mt per la transizione creditizia t→t+1. Il tempo di primo default e la LGD al regime M_(tau−1) sono implementati correttamente. Le perdite migration-based si applicano ai soli non-default. Sono presenti quattro tabelle e tre figure pertinenti, già verificate nella riesecuzione del medesimo notebook durante questa sessione.

La cella 11 calcola `delta_L_sim`, ma ne presenta solo la media. Il campione delle differenze esiste; manca una restituzione adeguata della distribuzione empirica richiesta nel Prompt 1. Non si impone una quarta figura come requisito autonomo.

La cella 13 definisce il CVaR come `mean(loss_vec[loss_vec >= var_alpha])`. Su una distribuzione discreta la formula può includere troppa massa al VaR: il CVaR deve considerare una coda di probabilità esattamente 1−alpha. Con 50.000 osservazioni, ai livelli assegnati, si ottiene mediando le peggiori 2.500 e 500 perdite ordinate. La differenza è teoricamente rilevante ma numericamente piccola in questo campione:

| CVaR, milioni USD | Notebook base | Corretto base | Notebook limite | Corretto limite |
|---|---:|---:|---:|---:|
| 95% | 69,037542 | 69,044556 | 63,225760 | 63,228954 |
| 99% | 79,636240 | 79,636240 | 73,446910 | 73,456771 |

Il VaR empirico con interpolazione predefinita andrebbe allineato al quantile inverso della funzione di ripartizione: il VaR 99% base è 74,7200, contro 74,7201 restituito dal notebook. Questi riscontri sono calcoli del valutatore già verificati sullo stesso notebook nella sessione; non sono attribuiti allo studente.

### Prompt e regimi — 12/15

Sono presenti Prompt zero, Scheda Caso nel Prompt 1, contributi iniziali ai Prompt 2 e 3, validazioni esplicite e sei richieste progressive di implementazione. Il codice arriva dopo la convalida della specifica e della scomposizione. I prompt brevi «Tappa 3», «Tappa 4» e analoghi sono collegati al contesto iniziale, come ammesso dalla sezione 15.9.

L'intervento 17 formula in Regime C una criticità specifica sulle unità della varianza, distingue errore di intestazione e possibile errore di calcolo, chiede un esito esplicito e celle sostitutive. Il notebook recepisce la correzione `(M$)^2`. È una buona evidenza di controllo dell'IA. Rimane poco documentata la verifica degli output effettivi di ciascuna tappa: la prosecuzione del lavoro non equivale da sola a controllo.

I 19 interventi includono identificazione del caso, conferme e richieste di formato. Non si applica una penalizzazione automatica per il loro numero: nel Prompt 1 non è comunicato un intervallo obbligatorio e non tutti gli interventi sono prompt metodologici autonomi.

### Verifiche — 9/15

La critica dimensionale della varianza è pertinente e ha valore didattico. Sono inoltre effettivi i controlli sulle somme delle righe, sull'assorbimento, sul primo ingresso in default e sui vincoli della riallocazione. Il report finale con 17 esiti `True` sovrastima però alcune verifiche:

- Cella 9, controllo 6: `ctrl_6 = True` è una dichiarazione; l'indipendenza delle estrazioni è giustificata dalla struttura del generatore, non dal booleano.
- Cella 9, controllo 15: verifica solo l'inizializzazione in S delle prime tre repliche; `expected_M_head` non è usato. Non prova la riproducibilità.
- Cella 11, controlli 8 e 10: verificano un solo debitore in default e un solo non-default, entrambi nel portafoglio base.
- Cella 11, controllo 13: verifica dimensioni degli array, che non dimostrano il riuso delle traiettorie. Il riuso è comunque corretto nel codice.
- Cella 11, controllo 14: ripete la somma già utilizzata per costruire il totale, con limitata indipendenza rispetto alla costruzione della perdita.
- Cella 13, controllo 16: confronta 25.000 e 50.000 osservazioni solo per media e VaR 95% base; non copre CVaR, livello 99% e portafoglio limitato.
- Cella 13, controllo 17: verifica ordinamenti necessari delle misure, che non garantiscono la corretta convenzione del CVaR.

La riproducibilità effettiva del codice è stata confermata dal valutatore nella sessione con una seconda simulazione a seed identico; questo non trasforma il controllo 15 dello studente in una prova adeguata.

### Interpretazione finale — 0/5

Nell'intervento 19 lo studente scrive: «Dopo una rilettura complessiva, trovo i risultati consistenti con le richieste del caso». Segue una validazione del lavoro. Questa è una dichiarazione sintetica di accettazione, non un'interpretazione finanziaria dei risultati. Il notebook termina con il report dei controlli.

Manca una discussione autonoma della riduzione delle misure di coda, del rischio sistemico residuo, del comportamento scenario per scenario e dei limiti della calibrazione didattica. Non si assume che l'interpretazione sia stata delegata all'IA: l'interpretazione manca nel materiale consegnato.

## Risultati e restituzione

La riesecuzione restituisce perdita media base di 26,233737 milioni e limite di 24,913819 milioni; VaR 95% rispettivamente 60,27 e 55,24 milioni. Le riduzioni sono circa il 5,03% per la media e l'8,35% per il VaR 95%. Sono risultati che avrebbero potuto sostenere una conclusione autonoma, senza confondere il miglioramento delle misure aggregate con una riduzione della perdita in ogni scenario.

Il contributo iniziale e la costruzione del modello sono buoni. Per migliorare il lavoro occorre formalizzare VaR e CVaR discreti, rendere i controlli coerenti con le proprietà dichiarate, presentare la distribuzione delle differenze e scrivere una conclusione autonoma fondata sui risultati e sui limiti del caso. Il rilievo sulle unità della varianza è un esempio positivo del controllo critico da estendere al resto del lavoro.
