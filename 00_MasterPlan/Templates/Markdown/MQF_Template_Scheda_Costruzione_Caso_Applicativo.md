# Template - Scheda Costruzione Caso Applicativo

Documento interno di progettazione docente. Compilare separatamente per il Caso Aula e per il Caso TakeHome.

## 1. Identificazione del caso

- **Lezione:** [numero e titolo]
- **Tipo di caso:** [Caso Aula / Caso TakeHome]
- **Titolo:** [titolo]
- **Destinatari:** [destinatari]
- **Uso previsto:** [uso didattico]

## 2. Contesto e motivazione

[Descrivere il contesto economico-finanziario, probabilistico o decisionale e la sua rilevanza didattica.]

## 3. Domanda quantitativa e funzione didattica

**Domanda quantitativa:**  
[formulare la domanda quantitativa centrale del caso]

**Obiettivo didattico:**  
[indicare che cosa lo studente deve comprendere, costruire, calcolare, verificare o interpretare]

**Collegamento con le lezioni teoriche precedenti:**  
[indicare i capitoli o le lezioni teoriche di riferimento e precisare quali concetti già introdotti vengono utilizzati nel caso]

**Concetti teorici da rendere osservabili:**  
[elencare le definizioni, proprietà, relazioni o risultati teorici che il caso deve rendere operativamente osservabili]

**Funzione della simulazione o della procedura computazionale:**  
[spiegare perché il ricorso a Python, alla simulazione, al solver o ad altra procedura computazionale è necessario o didatticamente utile nel caso]

**Ruolo dell'informazione, degli stati, degli scenari o dei vincoli:**  
[precisare quale struttura informativa, probabilistica, dinamica o decisionale governa il caso e quale funzione svolge nella soluzione]

## 4. Specifica teorico-matematica

- **Grandezze e variabili:** [elenco]
- **Eventi, informazione, stati o scenari:** [elenco]
- **Parametri e dati:** [elenco]
- **Ipotesi modellistiche:** [elenco]
- **Formule vincolanti:** [elenco]
- **Quantità teoriche da stimare o calcolare:** [elenco]
- **Proprietà teoriche da verificare:** [elenco delle identità, disuguaglianze, condizioni, proprietà o relazioni teoriche che devono essere controllate nel caso]
- **Soglie, target o vincoli rilevanti:** [elenco e significato economico-finanziario o probabilistico]
- **Quantità finali di interesse:** [elenco]
- **Limiti del modello:** [elenco]


## 5. Output richiesti

Gli output devono avere una funzione informativa, diagnostica o interpretativa esplicita e devono essere collegati alle quantità teoriche del caso.

### Stime o risultati numerici

Per ciascuna stima o risultato indicare, quando rilevante:

- quantità teorica o economico-finanziaria rappresentata;
- procedura computazionale utilizzata;
- unità di misura o scala;
- controllo numerico o logico associato;
- significato interpretativo.

[elenco delle stime o dei risultati numerici richiesti]

### Tabelle

Per ciascuna tabella indicare:

- quantità o oggetti rappresentati;
- funzione informativa o diagnostica;
- controllo associato;
- uso nella successiva analisi o interpretazione.

[elenco delle tabelle richieste]

### Grafici

Per ciascun grafico indicare:

- variabile o variabili rappresentate;
- confronto che il grafico deve rendere visibile;
- eventuali soglie, stati, scenari o target da evidenziare;
- domanda interpretativa associata;
- collegamento con il modello teorico.

[elenco dei grafici richiesti]

### Controlli

[elenco dei controlli numerici, logici, teorici, computazionali o interpretativi richiesti]

## 6. Flusso logico-teorico risolutivo atteso

| Passo | Finalità risolutiva | Formula, definizione, proprietà o teorema | Applicazione nel caso | Output o controllo collegato |
|---:|---|---|---|---|
| 1 | [finalità] | [strumento teorico] | [applicazione] | [output/controllo] |

## 7. Scomposizione attesa in tappe

| Tappa | Titolo | Obiettivo | Input | Regime IA prevalente | Prompt virtuoso di riferimento | Oggetti teorici coinvolti | Operazione | Output | Controllo | Uso successivo |
|---:|---|---|---|:---:|---|---|---|---|---|---|
| 1 | [titolo] | [obiettivo] | [input] | [A/B/C] | [prompt] | [oggetti teorici] | [operazione] | [output] | [controllo] | [uso] |

## 8. Sequenza docente dei prompt e mappa prompt-notebook

**Sequenza docente dei prompt virtuosi:**  
[indicare l'ordine previsto dei prompt, distinguendo Prompt zero, Prompt 1, Prompt 2, Prompt 3, prompt di tappa in Regime A/B ed eventuali Prompt C, attivati soltanto quando lo studente individua una criticità specifica da verificare]

La sequenza deve essere coerente con la Scheda Caso, con il Flusso logico-teorico risolutivo e con la scomposizione in tappe input-output. Per ciascun prompt deve essere chiaro quale funzione svolge, quale regime IA utilizza e quale elemento del notebook o del tracciato contribuisce a produrre o verificare.

| Prompt | Regime | Tappa o fase | Funzione del prompt | Celle o output prodotti | Decisione o controllo richiesto |
|---|:---:|---|---|---|---|
| [numero o nome] | [A/B/C/—] | [tappa o fase] | [funzione] | [celle/output] | [decisione/controllo] |

## 9. Struttura attesa del notebook

[Indicare l'ordine delle celle Markdown, delle celle codice, degli output e dei controlli.]

## 10. Criteri di validazione del notebook

Il notebook è considerato valido se:

1. implementa la specifica teorico-matematica senza modificarla;
2. utilizza esclusivamente gli input previsti dalla Scheda Caso;
3. rispetta la scomposizione in tappe input-output validata;
4. mantiene coerenti notazione matematica e nomi delle variabili computazionali;
5. produce tutti gli output richiesti;
6. esegue tutti i controlli numerici, logici e interpretativi previsti;
7. rende tracciabile il passaggio dalle formule alle procedure computazionali;
8. utilizza correttamente seed, parametri e convenzioni numeriche assegnate, quando previsti;
9. non utilizza risultati provenienti da esecuzioni non valide o da configurazioni non ammissibili;
10. contiene un'interpretazione finale coerente con gli output e con i limiti del modello.

**Criteri specifici del caso:**  
[aggiungere eventuali condizioni di validazione proprie del modello, della simulazione, del solver o degli output richiesti]


## 11. Calibrazione docente

- **Ordine di grandezza atteso dei risultati:** [indicazioni]
- **Errori o ambiguità prevedibili:** [elenco]
- **Controlli minimi di validazione:** [elenco]
- **Limiti interpretativi:** [elenco]

## 12. Uso dell'IA e tracciato

- **Uso documentato dell'IA previsto:** [sì / no]
- **Prompt obbligatori:** [Prompt zero, Prompt 1, Prompt 2, Prompt 3 e prompt di tappa necessari secondo la scomposizione operativa validata]
- **Numero dei prompt:** [determinato dalla scomposizione operativa validata; possono aggiungersi eventuali Prompt C soltanto in presenza di criticità specifiche individuate dallo studente]
- **Regimi IA utilizzati:** [A e/o B nelle tappe ordinarie; eventuale C soltanto quando lo studente individua una criticità specifica da verificare, indicando la tappa interessata]
- **Usi ammessi dell'IA:** [elenco]
- **Usi non ammessi dell'IA:** [elenco]
- **Criteri di validazione delle risposte IA:** [verificare almeno coerenza con il regime richiesto, coerenza con gli input disponibili, rispetto degli oggetti teorici già fissati, assenza di modifiche non autorizzate al modello, assenza di contenuti non ammessi, correttezza della traduzione computazionale quando pertinente, pertinenza dei controlli proposti e utilità dell'output per la tappa successiva]
- **Tracciato IA richiesto:** [sì / no]
- **Modalità di consegna del tracciato IA:** [ordinariamente stampa PDF della chat dedicata; indicare eventuali modalità diverse previste per il caso]
- **Sequenza osservabile richiesta nel tracciato:** [Prompt zero → Prompt 1 → Prompt 2 → Prompt 3 → prompt di tappa effettivamente utilizzati → eventuali Prompt C]
- **Elementi del tracciato oggetto di valutazione:** [contributo iniziale dello studente, prompt utilizzati, regime attribuito, risposte IA utilizzate, decisioni di accettazione/modifica/rifiuto/correzione, output prodotti, controlli svolti ed eventuali Prompt C attivati a partire da criticità specifiche individuate dallo studente]






## 13. Valutazione

- **Criteri per il notebook:** [elenco]
- **Criteri per il tracciato IA:** [elenco]
- **Peso dei controlli e dell'interpretazione:** [indicazioni]

## 14. Rubrica sintetica

Per i Casi TakeHome con uso documentato dell'IA, la rubrica assume come riferimento la seguente articolazione su 100 punti:

| Area | Peso | Criteri principali |
|---|---:|---|
| Prompt 2 — Flusso logico-teorico risolutivo | 30 | contributo iniziale dello studente, ordine logico, collegamento tra teoria, output e controlli |
| Prompt 3 — Scomposizione input-output | 15 | proposta operativa iniziale dello studente, coerenza delle tappe, collegamento input-output |
| Notebook Jupyter e output computazionali | 20 | correttezza del codice, tabelle, grafici, riproducibilità, coerenza degli output richiesti |
| Prompt di tappa e uso dei Regimi A/B; eventuale Regime C | 15 | qualità dei prompt, rispetto dei vincoli, contributo dello studente, uso appropriato dell'IA e, quando presente, qualità dell'attivazione del Regime C a partire da una criticità specifica |
| Verifiche logiche e controlli numerici | 15 | controlli su formule, simulazioni, vincoli, quantità teoriche e proprietà del modello |
| Interpretazione finanziaria finale | 5 | autonomia, coerenza con gli output, interpretazione finanziaria e consapevolezza dei limiti del modello |

**Totale:** 100 punti.

Per il Caso Aula, oppure per casi nei quali il tracciato IA non sia oggetto di valutazione, la rubrica può essere adattata alla funzione didattica del caso, mantenendo comunque coerenza con:
- obiettivi didattici;
- Flusso logico-teorico risolutivo;
- scomposizione in tappe;
- output richiesti;
- controlli;
- criteri di validazione del notebook;
- interpretazione finale.


## 15. Esito atteso e calibrazione qualitativa del caso

**Esito atteso:**  
[indicare quali caratteristiche qualitative devono emergere dagli output se il caso è correttamente costruito, senza fissare artificialmente risultati numerici predeterminati]

**Ordini di grandezza o relazioni attese:**  
[indicare eventuali intervalli plausibili, ordinamenti, segni, relazioni comparative o proprietà che dovrebbero risultare osservabili]

**Funzione didattica degli output:**  
[indicare quali concetti teorici, economico-finanziari o decisionali devono diventare osservabili attraverso i risultati]

**Possibili segnali di cattiva calibrazione:**
1. [segnale 1];
2. [segnale 2];
3. [segnale 3];
4. [ulteriori segnali].

La calibrazione deve garantire che il caso sia numericamente non banale, interpretabile e coerente con gli obiettivi didattici, senza trasformare l'esito atteso in un risultato da imporre al modello.

## 16. Relazione con l'altro caso della lezione

Il Caso Aula e il Caso TakeHome devono essere metodologicamente comparabili, ma non devono ridursi a una semplice variazione parametrica dello stesso problema.

Esplicitare:

1. **Concetti teorici comuni:** [quali concetti vengono consolidati in entrambi i casi]
2. **Strumenti computazionali comuni:** [quali procedure, librerie, metodi numerici o solver vengono utilizzati in entrambi i casi]
3. **Output comparabili:** [quali tipologie di stime, tabelle, grafici o risultati sono comuni]
4. **Controlli comparabili:** [quali controlli numerici, logici, teorici o interpretativi sono condivisi]
5. **Elementi metodologici comuni:** [quali passaggi della struttura Scheda Caso → Flusso logico-teorico → tappe → notebook → interpretazione restano invariati]
6. **Elementi distintivi del Caso TakeHome rispetto al Caso Aula:** [contesto, struttura del modello, formulazione finanziaria, dati, scenari, vincoli o linea risolutiva che rendono autonomo il secondo caso]
7. **Ripartizione delle responsabilità:** [indicare quali parti sono guidate dal docente, quali sono affidate allo studente e quali possono essere assistite dall'IA]

La relazione tra i due casi deve mostrare continuità metodologica senza duplicazione sostanziale del problema.
