# Valutazione del take-home della lezione 10 — Studente 1

Data: 2 ottobre 2026.

**Valutazione proposta: 61/100**, equivalente a **18,3/30** mediante conversione lineare, senza arrotondamenti aggiuntivi.

Il lavoro presenta contributi iniziali pertinenti e un motore di simulazione sostanzialmente corretto. Il prodotto consegnato contiene però tabelle Markdown e commenti incompatibili con i risultati computazionali. Lo studente individua questa incoerenza, ma accetta una risposta IA che la interpreta erroneamente e non la risolve. Manca inoltre una conclusione autonoma.

## Fonti e metodo

- [Guidelines](../../00_MasterPlan/MQF_Project_Guidelines.md), sezione 15.11 per la griglia numerica e sezioni 15.8–15.10 per validazione e tracciato.
- [Tracciato IA DOCX](Lezione_10_Tracciato_TakeHome_Stud1.docx), fonte esclusiva dell'interazione IA.
- [Notebook take-home](Lezione_10_Notebook_TakeHome_Stud1.ipynb), per codice, output e commenti consegnati.

Le Guidelines, il DOCX e il PDF sono leggibili; il PDF è di 56 pagine. La sua leggibilità è stata verificata, ma il suo contenuto non è utilizzato per assegnare i punteggi. La specifica vincolante è la Scheda Caso riportata nel Prompt 1 del DOCX: Lehman Brothers 2008, 40 debitori, investimento totale 173 milioni, eliminazione di Lehman e riallocazione proporzionale sui 39 debitori residui.

I sei massimi sono quelli delle Guidelines. I punteggi entro ogni area sono giudizi motivati del valutatore: le Guidelines non prescrivono detrazioni automatiche per ogni difetto. Non si penalizza l'uso dell'IA in quanto tale e non si formulano inferenze sulla storia privata del lavoro.

## Griglia numerica

| Area | Massimo | Assegnato | Motivazione sintetica |
|---|---:|---:|---|
| Prompt 2 — Flusso logico-teorico risolutivo | 30 | **22** | Contributo pertinente, inclusa la dipendenza condizionata; proposta descrittiva e validazione delle integrazioni poco argomentata. |
| Prompt 3 — Scomposizione input-output | 15 | **12** | Buona proposta operativa, scenari comuni espliciti e attenzione a verifiche e limiti; oggetti intermedi e controlli dettagliati introdotti dall'IA. |
| Notebook Jupyter e output computazionali | 20 | **11** | Codice eseguibile e modello sostanzialmente corretto, ma tabelle e commenti finali contraddicono i risultati; CVaR discreto e unità della varianza da correggere. |
| Prompt e uso dei regimi A/B/C | 15 | **10** | Sequenza ordinata, sviluppo progressivo e criticità specifica in Regime C; accettata una falsa diagnosi senza verificare l'esito della correzione. |
| Verifiche logiche e controlli numerici | 15 | **6** | Controlli reali sui vincoli e rilevazione di un'incoerenza; verifiche dichiarative e mancato controllo del disallineamento finale tra codice e Markdown. |
| Interpretazione critica finale | 5 | **0** | Nessuna conclusione autonoma dello studente; i commenti finanziari presenti sono prodotti dall'IA e alcuni sono errati. |
| **Totale** | **100** | **61** | |

Le contraddizioni nel prodotto incidono sul notebook; l'inefficacia della verifica incide sui controlli; l'accettazione della risposta errata riguarda il governo dell'interazione IA. Sono aspetti distinti, senza detrazioni automatiche duplicate. Il punteggio finale non è derivato dalla valutazione del caso aula.

## Motivazione analitica

I riferimenti agli interventi indicano l'ordine dei 25 paragrafi DOCX che iniziano con `User prompt:`. Le celle del notebook sono numerate a partire da 1.

### Prompt 2 — 22/30

Nell'intervento 5 lo studente propone regime sistemico markoviano, migrazioni governate dal regime corrente, indipendenza condizionata e dipendenza dovuta al fattore comune, simulazione, perdite terminali, distribuzione empirica, misure di rischio e confronto senza Lehman. Chiede verifica, completamento e ordinamento senza codice e senza cambio del modello. È un contributo concreto e riconoscibile.

La proposta non formalizza però la funzione di perdita, il fattore di riallocazione 173/148, il confronto a scenari identici, l'analisi condizionata alla crisi e le convenzioni di VaR e CVaR. I dettagli sono completati dall'IA. Lo studente sceglie il compattamento in sei tappe, ma convalida la proposta senza una verifica teorica puntuale.

Nella tabella finale della cella 2, l'indipendenza è scritta come fattorizzazione condizionata al solo regime corrente Mt. La specifica assume invece indipendenza condizionatamente alla traiettoria del regime comune; per gli stati creditizi accumulati il solo Mt non è generalmente sufficiente. Il codice usa correttamente la traiettoria comune, ma la formalizzazione resta imprecisa.

### Prompt 3 — 12/15

L'intervento 9 contiene una proposta operativa strutturata: dati e portafogli, simulazione dei quattro trimestri, conversione degli stati finali in perdite, aggregazione sugli stessi scenari, distribuzioni e misure di rischio, confronto con e senza crisi, verifiche e interpretazione con attenzione ai limiti. È particolarmente positivo il riuso esplicito degli scenari comuni.

Input, output e controlli non sono ancora identificati sistematicamente nella proposta personale. La tabella dettagliata viene costruita dall'IA e convalidata nell'intervento 10 senza selezione motivata. Il punteggio riconosce la buona base operativa senza attribuire allo studente tutto il dettaglio dell'assistente.

### Notebook e output — 11/20

Il notebook contiene 21 celle, di cui 6 di codice. La riesecuzione integrale in sequenza con backend grafico non interattivo termina senza errori. Tutti i 15 booleani di controllo risultano veri, ma questo non certifica tutte le proprietà dichiarate.

Sono corretti matrici, portafogli, capitale totale, riallocazione proporzionale e uso delle stesse traiettorie per i 39 debitori comuni. La simulazione usa M0,…,M3 per le quattro transizioni creditizie, mantiene il default assorbente e valorizza le perdite dal rating terminale, come appropriato con LGD costante 0,65. Sono presenti quattro tabelle Markdown, le tre figure richieste e un grafico aggiuntivo della distribuzione delle differenze. Le quattro figure rigenerate sono state ispezionate e sono pertinenti; in alcune figure le etichette inferiori risultano parzialmente tagliate nel rendering locale.

Il difetto principale è il disallineamento del testo con i calcoli:

| Quantità | Markdown consegnato | Riesecuzione |
|---|---:|---:|
| Media concentrato, milioni USD | 8,3079 | 11,1698 |
| Media controfattuale, milioni USD | 8,3079 | 12,2469 |
| Media della differenza, milioni USD | 0,0000 | 1,0772 |
| Varianza concentrato, milioni USD al quadrato | 148,6512 | 47,8501 |
| Varianza controfattuale, milioni USD al quadrato | 102,1482 | 53,0557 |
| VaR 99% concentrato, milioni USD | 48,7182 | 32,6500 |
| VaR 99% controfattuale, milioni USD | 44,2023 | 33,8403 |
| Probabilità di ingresso in C | 36,68% | 29,712% |
| Quota scenari di beneficio | 13,12% | 10,334% |
| Quota scenari di parità | 70,93% | 0,014% |
| Quota scenari di peggioramento | 15,95% | 89,652% |

Le celle 15, 18 e 21 contengono numeri non allineati. La cella 18 afferma invarianza della media e abbattimento della dispersione e del rischio di coda; i risultati effettivi mostrano invece aumenti delle misure riportate. Gli output salvati delle celle 14 e 20 confermano rispettivamente la probabilità 0,2971 e la differenza media 1,0772: non è una discrepanza introdotta soltanto dalla riesecuzione del valutatore.

La cella 17 costruisce `df_tabella_3` correttamente dai vettori simulati, ma non lo stampa; la tabella visibile successiva è trascritta in Markdown con valori diversi. La Tappa 6 sostitutiva conserva il corretto calcolo `delta_L = L_div - L_conc`, mentre la cella Markdown sostitutiva conserva valori errati.

La conservazione del capitale non implica uguaglianza della perdita attesa: Lehman ha rating A, mentre il capitale viene riallocato a un insieme con rating diversi. Un benchmark indipendente, ottenuto enumerando le 27 traiettorie sistemiche e propagando le probabilità di rating, restituisce medie esatte del modello pari a 11,185464 e 12,253505 milioni, differenza +1,068040 milioni. La probabilità esatta di crisi è 0,299295. Questi risultati corroborano il codice e confutano l'invarianza della media; sono calcoli del valutatore, non lavoro attribuito allo studente.

La cella 17 usa inoltre `mean(L[L >= VaR])` per il CVaR, formula non generale per distribuzioni discrete. La media delle peggiori 2.500 e 500 osservazioni dà:

| Misura, milioni USD | Codice concentrato | CVaR corretto concentrato | Codice controfattuale | CVaR corretto controfattuale |
|---|---:|---:|---:|---:|
| CVaR 95% | 29,698297 | 29,702080 | 31,089135 | 31,090859 |
| CVaR 99% | 36,858423 | 36,866840 | 36,956237 | 36,956237 |

L'impatto numerico è limitato, ma la convenzione teorica va precisata. Le intestazioni della Tabella 3 attribuiscono inoltre M$ anche alla varianza, che richiede (M$)^2.

### Prompt e regimi — 10/15

Il tracciato mostra Prompt zero, acquisizione della specifica, contributi iniziali, convalide prima del codice e sviluppo progressivo. Lo studente chiede di eseguire il codice prima di ricevere le celle dei risultati e comunica più volte «Esiti ok». È un'organizzazione positiva, sebbene queste conferme non forniscano gli output numerici all'IA e non dimostrino un confronto analitico.

L'intervento 24 è una buona richiesta in Regime C: segnala concretamente medie uguali nella Tabella 3, differenza di circa 1,08 nell'output e frequenze incompatibili con il Markdown; distingue possibili errori di calcolo, esecuzione e aggiornamento del testo. Chiede diagnosi e celle sostitutive senza cambiare la specifica.

La risposta IA accoglie la criticità, ma assume erroneamente che le medie debbano coincidere e attribuisce senza prova il valore 1,08 a vettori non aggiornati. Lo studente recepisce questa risposta e valida tutto nell'intervento 25, senza documentare il confronto dopo la sostituzione. L'errore dell'IA non è penalizzato automaticamente: rileva la mancata verifica e il suo trasferimento nel prodotto finale, come previsto dalle Guidelines.

Non si applica una detrazione automatica per i 25 interventi: includono conferme e richieste di formato, e il Prompt 1 non comunica un intervallo obbligatorio.

### Verifiche — 6/15

Sono reali i controlli sulle matrici, sul default assorbente, sulle dimensioni dei portafogli, sul capitale e sulle proporzioni. L'accoppiamento degli scenari è effettivo. La rilevazione autonoma del disallineamento merita riconoscimento.

Restano debolezze sostanziali:

- Cella 8: `chk_6 = True` e `chk_13 = True` sono dichiarazioni, non verifiche rispettivamente dell'indipendenza e della riproducibilità. La struttura del generatore e il seed sostengono il codice, ma non sostituiscono una prova di ripetizione.
- Cella 8: il controllo della forma di M non dimostra da solo l'unicità del regime applicato a tutti i debitori; il codice la rispetta comunque.
- Cella 11: il controllo di additività ripete la somma usata per costruire il totale, con limitata indipendenza.
- Cella 17: `L.max() > 1` non prova che la variabile abbia unità monetarie; il calcolo è monetario per la sua costruzione, non per il test.
- Cella 17: la stabilità è verificata solo sul VaR 99% concentrato, con soglia di 1 milione; non copre le principali misure di entrambi i portafogli.
- Manca il confronto sistematico tra output e tabelle Markdown, anche dopo la criticità segnalata.
- Manca il controllo elementare `mean(delta_L) = mean(L_div) - mean(L_conc)` confrontato con i valori esposti. L'identità è rispettata dal codice e smentisce il Markdown.

La formula matematica evocata dall'IA nella diagnosi è corretta; sono errate le medie assunte come premise e la conclusione di invarianza. Lo studente non completa il ciclo di verifica.

### Interpretazione finale — 0/5

Nell'intervento 25 lo studente dichiara i risultati consistenti e valida il lavoro, ma non propone un'interpretazione quantitativa autonoma. I commenti finanziari delle celle 15, 18 e 21 provengono dalle risposte IA e non soddisfano il requisito di una conclusione scritta dallo studente. Alcuni sono anche incompatibili con i risultati effettivi.

## Restituzione allo studente

La struttura del modello e la proposta operativa sono buone. La segnalazione dell'incoerenza è pertinente, ma deve essere seguita da una verifica della risposta ricevuta: il codice non conferma l'invarianza della media né la riduzione del rischio riportate nel testo. Occorre aggiornare le tabelle dagli output effettivi, correggere unità e CVaR discreto, rendere i controlli coerenti con ciò che dichiarano e formulare una conclusione autonoma sul cambiamento della composizione per rating e sul rischio sistemico residuo.
