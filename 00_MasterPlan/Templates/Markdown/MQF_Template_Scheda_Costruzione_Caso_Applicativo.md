# Template - Scheda Costruzione Caso Applicativo

Documento interno di progettazione docente. Compilare separatamente per il caso aula e per il caso take-home.

## 1. Identificazione del caso

- **Lezione:** [numero e titolo]
- **Tipo di caso:** [aula / take-home]
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

- **Stime o risultati numerici:** [elenco]
- **Tabelle:** [elenco]
- **Grafici:** [elenco]
- **Controlli:** [elenco]

## 6. Flusso logico-teorico risolutivo atteso

| Passo | Finalità risolutiva | Formula, definizione, proprietà o teorema | Applicazione nel caso | Output o controllo collegato |
|---:|---|---|---|---|
| 1 | [finalità] | [strumento teorico] | [applicazione] | [output/controllo] |

## 7. Scomposizione attesa in tappe

| Tappa | Regime | Input | Operazione | Output | Controllo | Uso successivo |
|---:|:---:|---|---|---|---|---|
| 1 | [A/B/C] | [input] | [operazione] | [output] | [controllo] | [uso] |

## 8. Sequenza docente dei prompt e mappa prompt-notebook

**Sequenza docente dei prompt virtuosi:**  
[indicare l'ordine previsto dei prompt, distinguendo Prompt zero, Prompt 1, Prompt 2, Prompt 3, prompt di tappa in Regime A/B/C ed eventuali verifiche conclusive]

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

- **Prompt obbligatori:** [elenco]
- **Numero minimo e massimo di prompt:** [intervallo]
- **Usi ammessi dell'IA:** [elenco]
- **Usi non ammessi:** [elenco]

## 13. Valutazione

- **Criteri per il notebook:** [elenco]
- **Criteri per il tracciato IA:** [elenco]
- **Peso dei controlli e dell'interpretazione:** [indicazioni]

## 14. Rubrica sintetica

| Area | Peso | Criteri principali |
|---|---:|---|
| Premesse teorico-matematiche | [peso] | [criteri] |
| Flusso logico-teorico risolutivo | [peso] | [criteri] |
| Scomposizione input-output | [peso] | [criteri] |
| Notebook e output computazionali | [peso] | [criteri] |
| Prompt e uso dei regimi A/B/C | [peso] | [criteri] |
| Controlli numerici, logici e interpretativi | [peso] | [criteri] |
| Interpretazione critica finale | [peso] | [criteri] |

**Totale:** [100 punti oppure altra scala prevista]

La rubrica deve essere adattata al caso specifico mantenendo coerenza con:
- gli obiettivi didattici;
- gli output richiesti;
- i controlli previsti;
- i criteri di validazione del notebook;
- i criteri di valutazione del tracciato IA, quando richiesto.


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

[Spiegare in che modo il caso aula e il caso take-home sono metodologicamente comparabili senza ridursi a una variazione parametrica.]
