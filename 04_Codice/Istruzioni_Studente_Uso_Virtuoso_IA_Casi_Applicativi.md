# Istruzioni per lo studente — Uso virtuoso dell’IA nei casi applicativi MQF

## 1. Scopo del documento

Questo documento spiega come svolgere un caso applicativo MQF utilizzando l’IA in modo corretto, controllato e valutabile.

L’obiettivo non è far risolvere il caso all’IA, ma usarla come supporto per:

1. chiarire il problema;
2. organizzare il ragionamento;
3. costruire codice coerente con la Scheda Caso;
4. verificare output, controlli e interpretazioni;
5. documentare il processo seguito.

Il lavoro resta responsabilità dello studente.

---

## 2. Materiali di partenza

Per ogni caso applicativo il docente fornisce:

1. Prompt zero;
2. Prompt 1, contenente la Scheda Caso;
3. Le presenti "Istruzioni" che forniscono:  
    - indicazioni sugli output richiesti
    - indicazioni sulla consegna;
    - pesi di valutazione, se diversi da quelli indicativi riportati in fondo a questo documento.

La Scheda Caso è la specifica vincolante del lavoro.

Durante lo svolgimento non devono essere modificati:

1. contesto del caso;
2. variabili;
3. eventi, stati o scenari;
4. formule principali;
5. parametri;
6. output richiesti;
7. controlli richiesti;
8. ipotesi del modello.

---

## 3. Che cosa devi consegnare

Per un caso applicativo con uso documentato dell’IA devi consegnare:

1. notebook Jupyter eseguibile;
2. stampa PDF della chat IA utilizzata per il lavoro;
3. eventuali file aggiuntivi richiesti dal docente.

La stampa PDF della chat IA costituisce il tracciato dell’interazione con l’IA.

La chat consegnata deve essere dedicata al caso. Non deve contenere messaggi personali, conversazioni estranee, prove casuali, domande non pertinenti o materiale non collegato al lavoro.

---

## 4. I tre regimi di interazione con l’IA

## 4.1 Regime A — Ricognizione teorico-modellistica

Il Regime A serve a chiarire il caso dal punto di vista teorico, finanziario e matematico.

L’oggetto principale del prompt deve essere:

1. la struttura del problema;
2. le variabili;
3. gli eventi o scenari;
4. le formule;
5. le quantità da stimare;
6. l’ordine logico della soluzione;
7. il collegamento tra teoria, output e controlli.

Il Regime A può occasionalmente includere piccoli calcoli, esempi numerici o frammenti di codice, quando servono a chiarire una proprietà teorica, una formula o una quantità del caso.

Tuttavia, il centro del prompt non deve essere la sintassi Python, ma il ragionamento teorico-finanziario-matematico.

Nel Regime A è importante che lo studente fornisca un contributo iniziale: ipotesi, dubbi, ordine logico, collegamenti teorici, proposte di lettura.

---

## 4.2 Regime B — Traduzione operativa in codice

Il Regime B serve a tradurre in Python una tappa già definita.

Lo standard del Regime B è una richiesta all’IA di scrivere codice per realizzare l’output previsto dalla tappa.

Il prompt deve indicare:

1. tappa da svolgere;
2. input disponibili;
3. formule da implementare;
4. output richiesto;
5. controlli da includere;
6. vincoli da rispettare.

L’IA può scrivere codice, ma non deve cambiare la Scheda Caso.

---

## 4.3 Regime C — Verifica e interpretazione critica

Il Regime C serve a verificare materiale già prodotto.

L’IA può essere usata per:

1. controllare un output;
2. individuare errori o ambiguità;
3. suggerire controlli aggiuntivi;
4. modificare codice già scritto;
5. correggere una cella Markdown;
6. rivedere una bozza interpretativa;
7. verificare la completezza finale del lavoro.

Il prompt in Regime C deve partire da un dubbio, da una verifica già svolta o da un output già prodotto.

L’IA può anche suggerire modifiche al testo Markdown o al codice, ma la richiesta deve essere motivata da una verifica, da un’anomalia o da un dubbio dello studente.

---

## 5. Sequenza obbligatoria dei prompt

La sequenza iniziale è:

1. Prompt zero;
2. Prompt 1;
3. Prompt 2;
4. Prompt 3;
5. prompt di tappa.

| Prompt | Chi lo fornisce | Funzione | Valutazione |
|---|---|---|---|
| Prompt zero | docente | inizializza contesto, regimi e regole generali | non valuta il contributo dello studente |
| Prompt 1 | docente | fornisce la Scheda Caso e chiede acquisizione non produttiva | non valuta il contributo dello studente |
| Prompt 2 | studente + IA | costruisce il Flusso logico-teorico risolutivo | valuta contributo iniziale dello studente, ordine logico, collegamento tra teoria, output e controlli |
| Prompt 3 | studente + IA | costruisce la scomposizione in tappe input-output | valuta la proposta operativa iniziale dello studente |
| Prompt di tappa | studente + IA | sviluppa, codifica o verifica singole tappe | valuta specificità, controlli e uso critico dell’IA |

---

## 6. Prompt zero

Il Prompt zero è fisso ed è fornito dal docente.

Serve a inizializzare la conversazione con l’IA.

Deve essere usato senza modificarlo, salvo istruzioni esplicite del docente.

---

## 7. Prompt 1 — Acquisizione della Scheda Caso

Il Prompt 1 è fornito dal docente e contiene la Scheda Caso.

È un prompt non produttivo.

L’IA deve soltanto acquisire la Scheda Caso come specifica vincolante e rispondere con una conferma minima.

Risposta attesa:

```text
OK, scheda acquisita.
```

Se l’IA produce sintesi, codice, formule aggiuntive, tappe operative o suggerimenti, lo studente deve riportarla al vincolo iniziale.

---

## 8. Prompt 2 — Flusso logico-teorico risolutivo

Il Prompt 2 è obbligatorio ed è in Regime A.

Serve a costruire il Flusso logico-teorico risolutivo.

Lo studente deve proporre una prima sequenza di elementi teorici. L’IA può completare, correggere e ordinare.

### Esempio di prompt virtuoso

```text
Regime A — Ricognizione teorico-modellistica.

Sulla base della Scheda Caso acquisita, devo costruire il Flusso logico-teorico risolutivo.

Secondo me la soluzione deve partire da questi elementi teorici:

1. identificazione della variabile finale da analizzare;
2. collegamento tra fattore di rischio e variabile finale;
3. definizione degli eventi o regimi informativi;
4. probabilità degli eventi;
5. distribuzioni condizionate;
6. simulazione coerente con la struttura condizionata;
7. stima delle quantità non condizionate;
8. stima delle quantità condizionate;
9. verifica della formula del valore atteso totale;
10. interpretazione del ruolo dell’informazione.

Ti chiedo di verificare, completare e ordinare questa sequenza.

Non proporre ancora la scomposizione in tappe.
Non modificare la Scheda Caso.

L’output deve essere una tabella con colonne:
Passo;
Finalità risolutiva;
Formula teorico-matematica / definizione / proprietà / teorema;
Applicazione nel caso;
Output o controllo collegato.
```

---

## 9. Prompt 3 — Scomposizione in tappe input-output

Il Prompt 3 è obbligatorio ed è in Regime A.

Serve a trasformare il Flusso logico-teorico in una sequenza operativa di tappe.

Lo studente deve proporre una prima ipotesi di tappe. L’IA può modificarla, integrarla e ordinarla.

### Esempio di prompt virtuoso

```text
Regime A — Ricognizione teorico-modellistica.

Ho costruito il Flusso logico-teorico risolutivo e devo trasformarlo in tappe operative.

Propongo questa prima ipotesi:

1. definire i parametri del caso e controllare che le probabilità degli eventi sommino a uno;
2. simulare i regimi informativi secondo le probabilità assegnate;
3. simulare la variabile di rischio condizionatamente al regime estratto;
4. costruire la variabile finale del caso applicando la formula prevista;
5. produrre statistiche e grafici non condizionati;
6. calcolare le medie condizionate per regime;
7. verificare la formula del valore atteso totale;
8. scrivere l’interpretazione finale e dichiarare i limiti.

Ti chiedo di verificare, modificare, integrare e ordinare questa proposta.

Per ogni tappa indica:
- titolo;
- input;
- operazione;
- output;
- controllo;
- uso nella tappa successiva;
- regime IA prevalente.

Non produrre risultati numerici.
Non modificare la Scheda Caso.
```

---

## 10. Libreria di prompt virtuosi

Gli esempi seguenti devono essere adattati al caso specifico.

Non devono essere copiati meccanicamente. Un prompt virtuoso deve sempre indicare:

1. che cosa è già stato fatto;
2. che cosa si sta chiedendo all’IA;
3. quali vincoli devono essere rispettati;
4. quale output si vuole ottenere;
5. quale controllo o dubbio guida la richiesta.

---

## 10.1 Prompt di tappa in Regime A — Chiarimento teorico

### Esempio A1 — Simulazione dei regimi informativi

```text
Regime A.

Sto per costruire la tappa in cui simulo i regimi informativi.

Secondo me l’input è dato dalle probabilità degli eventi e dal numero di simulazioni. L’output deve essere una sequenza simulata di eventi. Il controllo principale è confrontare le frequenze empiriche con le probabilità teoriche.

Ti chiedo di verificare se questa lettura è corretta e se manca qualche controllo teorico o logico.

Non modificare la Scheda Caso.
```

### Esempio A2 — Distribuzione condizionata

```text
Regime A.

Sto lavorando sulla tappa in cui devo simulare la variabile di rischio condizionatamente al regime estratto.

La mia idea è che, dopo avere simulato il regime, devo usare la distribuzione condizionata prevista per quel regime. Il controllo dovrebbe confrontare media e deviazione standard empiriche con i parametri teorici.

Ti chiedo di verificare se la logica è corretta e se l’output della tappa è ben definito.
```

### Esempio A3 — Trasformazione nella variabile finale

```text
Regime A.

Sto lavorando sulla tappa in cui trasformo la variabile di rischio nella variabile finale del caso.

Secondo me devo applicare la formula indicata nella Scheda Caso e poi controllare che il risultato abbia il segno e l’interpretazione corretta.

Ti chiedo di verificare se sto distinguendo correttamente fattore di rischio, variabile derivata e output finale.

Non cambiare la formula del caso.
```

### Esempio A4 — Valore atteso condizionato

```text
Regime A.

Devo calcolare le medie condizionate per regime.

Secondo me devo raggruppare le osservazioni in base agli eventi della partizione e calcolare una media per ciascun gruppo. Devo poi distinguere tra la media condizionata rispetto a un evento e il valore atteso condizionato rispetto alla sigma-algebra generata dalla partizione.

Ti chiedo di verificare se questa distinzione è corretta e come deve essere resa visibile nel notebook.
```

---

## 10.2 Prompt di tappa in Regime B — Codice Python

### Esempio B1 — Definizione dei parametri

```text
Regime B — Traduzione operativa in codice.

Devo implementare la tappa di definizione dei parametri.

Input:
- parametri della Scheda Caso;
- probabilità degli eventi;
- parametri delle distribuzioni condizionate;
- numero di simulazioni;
- seed.

Output richiesto:
- tabelle dei parametri;
- controllo che le probabilità sommino a uno;
- calcolo delle eventuali soglie implicite.

Scrivi una cella Markdown sintetica e una cella Python chiara.

Non modificare parametri, formule o probabilità.
```

### Esempio B2 — Simulazione gerarchica

```text
Regime B — Traduzione operativa in codice.

Devo implementare la simulazione gerarchica.

La logica è:
1. simulare prima il regime informativo;
2. simulare poi la variabile di rischio condizionatamente al regime;
3. produrre un dataset con regime simulato e variabile simulata.

Output richiesto:
- dataset simulato;
- tabella delle frequenze dei regimi;
- controllo delle statistiche empiriche per regime.

Scrivi codice Python chiaro e commentato.
Non introdurre nuovi oggetti teorici.
Non modificare la Scheda Caso.
```

### Esempio B3 — Calcolo della variabile finale

```text
Regime B — Traduzione operativa in codice.

Devo calcolare la variabile finale del caso usando la formula fissata nella Scheda Caso.

Input:
- dataset simulato;
- variabile di rischio;
- parametri necessari alla formula.

Output:
- nuova colonna nel dataset con la variabile finale;
- controlli sulla formula;
- controllo di dimensione;
- controllo logico sul segno o sulla parte positiva, se rilevante.

Scrivi una cella Markdown e una cella Python.
Non modificare la formula.
```

### Esempio B4 — Output non condizionati e condizionati

```text
Regime B — Traduzione operativa in codice.

Devo produrre gli output statistici richiesti.

Input:
- dataset finale;
- variabile finale del caso;
- eventi o regimi simulati;
- soglie richieste.

Output:
- statistiche non condizionate;
- quantili;
- probabilità di superamento soglia;
- medie condizionate per regime;
- verifica della formula del valore atteso totale;
- grafici essenziali.

Scrivi codice Python ordinato, con tabelle leggibili e controlli espliciti.
```

---

## 10.3 Prompt in Regime C — Verifica critica

I prompt in Regime C devono essere mirati. Non devono chiedere all’IA di verificare tutto il lavoro in modo generico.

Si tratta di prompt di iniziativa dello studente dovuti ad un risultato anomalo o da una possibile incoerenza connessa alle risposte e/o il codice scritti dall'IA.

### Esempio D1 — Frequenze simulate inattese

```text
Regime C — Verifica diagnostica.

Ho un dubbio sulla simulazione dei regimi.

Con n = 50.000, le frequenze empiriche degli eventi risultano abbastanza diverse dalle probabilità teoriche. Mi aspettavo scostamenti più piccoli.

Output osservato:
[inserire tabella delle frequenze]

Il mio dubbio è:
non capisco se lo scostamento sia compatibile con la variabilità Monte Carlo oppure se ci sia un errore nel modo in cui ho simulato gli eventi.

Ti chiedo di verificare:
1. se il confronto frequenze-probabilità è impostato correttamente;
2. se lo scostamento osservato è plausibile;
3. quali controlli aggiuntivi posso svolgere senza modificare la Scheda Caso.

Non riscrivere la simulazione da zero, salvo individuazione di un errore preciso.
```

### Esempio D2 — Segno inatteso della perdita

```text
Regime C — Verifica diagnostica.

Ho un dubbio sul segno della perdita.

In alcune simulazioni ottengo valori negativi di L. All’inizio pensavo che una perdita dovesse essere sempre positiva, ma la formula della Scheda Caso è L = D V0 Delta y.

Il mio dubbio è:
i valori negativi di L sono un errore oppure rappresentano un guadagno quando lo shock di rendimento è negativo?

Ti chiedo di verificare la coerenza teorica e interpretativa del segno di L.

Non modificare la formula.
Non proporre una trasformazione in parte positiva se non è prevista dalla Scheda Caso.
```

### Esempio D3 — Massa in zero inattesa nello shortfall

```text
Regime C — Verifica diagnostica.

Ho un dubbio sulla distribuzione dello shortfall S.

Nel grafico compare una massa molto visibile in zero. Non sono sicuro se sia un risultato atteso oppure un errore nel calcolo di S.

Output osservato:
[inserire descrizione del grafico o tabella]

Il mio dubbio è:
la massa in zero deriva correttamente dalla definizione S = (m* - M)^+ oppure indica che ho applicato male la formula?

Ti chiedo di verificare:
1. la coerenza della formula;
2. l’interpretazione della massa in zero;
3. quale controllo posso aggiungere nel notebook.

Non sostituire lo shortfall con una variabile diversa.
```

### Esempio D4 — Media ricomposta diversa dalla media globale

```text
Regime C — Verifica diagnostica.

Ho un problema nella verifica della formula del valore atteso totale.

La media globale della variabile finale non coincide con la media ricomposta usando frequenze empiriche e medie condizionate.

Output osservato:
- media globale: [inserire valore]
- media ricomposta: [inserire valore]
- differenza: [inserire valore]

Il mio dubbio è:
non capisco se la differenza sia dovuta ad arrotondamenti, a un errore di raggruppamento per regime o a una formula usata male.

Ti chiedo di aiutarmi a diagnosticare il problema.

Controlla in particolare:
1. se la ricomposizione deve usare probabilità teoriche o frequenze empiriche;
2. se le medie condizionate sono calcolate sugli stessi dati della media globale;
3. se il confronto è scritto correttamente nel notebook.

Non riscrivere tutto il codice: individua il possibile punto debole.
```

---

## 10.4 Prompt conclusivi in Regime C

Anche i prompt conclusivi devono essere mirati. Non devono essere liste universali da copiare.

Lo studente deve scegliere quale aspetto finale verificare.

### Esempio F1 — Verifica finale della coerenza tra notebook e Scheda Caso

```text
Regime C — Verifica finale mirata.

Voglio controllare la coerenza tra la Scheda Caso e il notebook finale.

Ti fornisco l’elenco delle sezioni del notebook:
[inserire elenco sezioni]

Ti fornisco gli output richiesti dalla Scheda Caso:
[inserire elenco output richiesti]

Ti chiedo di verificare se ogni output richiesto compare nel notebook e se mancano controlli essenziali.

Non valutare la qualità stilistica.
Non riscrivere il notebook.

Restituisci solo:
1. output presenti;
2. output mancanti;
3. controlli mancanti;
4. correzioni prioritarie.
```


### Esempio F3 — Verifica finale dell’interpretazione

```text
Regime C — Verifica finale mirata.

Mi sto ficalizzando solo l’interpretazione finale.

La mia interpretazione  finale è ... . Con riferimento ai grafici prodotti si conferma che... . Con riferimento ai risulti numerici si conferma che ... .

Ti chiedo di verificare se ho incluso gli elementi rilevanti ed eventualmente di modificare / integrare il testo della mia interpretazione.:

Non riscrivere l’intera conclusione.
Suggerisci solo modifiche puntuali.
```

---

## 11. Come preparare la stampa PDF della chat IA

La chat IA consegnata deve documentare l'intero processo di lavoro, inclusivo di tutti i prompt e le risposte dell'IA.

Deve contenere:

1. Prompt zero;
2. Prompt 1;
3. Prompt 2;
4. risposta IA al Prompt 2;
5. Prompt 3;
6. risposta IA al Prompt 3;
7. prompt di tappa e relative risposte IA;
8. eventuali prompt di verifica e relative risposte IA;
9. interpretazione finale o verifica dell’interpretazione.

Non deve contenere:

1. messaggi personali;
2. conversazioni non pertinenti;
3. richieste estranee al caso;
4. materiale non collegato al notebook.

Usa una chat dedicata esclusivamente al caso.

La consegna deve essere una stampa PDF della chat. Non è necessario riscrivere manualmente tutta l’interazione in un file separato, salvo istruzioni diverse del docente.

---

## 12. Errori da evitare

Evita di:

1. chiedere all’IA di “risolvere il caso”;
2. chiedere all’IA di scrivere direttamente tutto il notebook;
3. saltare Prompt 2 o Prompt 3;
4. formulare Prompt 2 senza contributo teorico iniziale;
5. formulare Prompt 3 senza proposta di tappe;
6. scrivere codice prima di avere chiarito la struttura del lavoro;
7. accettare senza controllo risposte IA;
8. modificare la Scheda Caso;
9. confondere quantità teoriche e stime empiriche;
10. delegare all’IA l’interpretazione finale.

---

## 13. Sintesi della valutazione

La valutazione considera:

1. correttezza teorica;
2. qualità del Flusso logico-teorico;
3. qualità della scomposizione in tappe;
4. notebook e output;
5. controlli numerici e logici;
6. uso dei regimi IA;
7. qualità della chat IA;
8. autonomia dell’interpretazione finale.

Il Prompt 2 è valutato per il contributo teorico iniziale dello studente.

Il Prompt 3 è valutato per la rilevanza e completezza della proposta iniziale di tappe.

I prompt in Regime C sono valutati su due dimensioni:

1. qualità ordinaria della verifica richiesta;
2. eventuale valore diagnostico, quando lo studente individua reali debolezze o errori emersi nel lavoro.

Il valore diagnostico è riconosciuto solo se la chat mostra:

1. criticità individuata dallo studente;
2. verifica richiesta all’IA;
3. riconoscimento o precisazione da parte dell’IA;
4. decisione finale dello studente;
5. correzione apportata.

---

## 14. Tabella indicativa di valutazione

I pesi sono indicativi e possono essere modificati dal docente per ciascun esercizio take-home.

| Area | Peso indicativo | Criteri principali |
|---|---:|---|
| **Prompt 2**. Flusso logico-teorico risolutivo | 30 | contributo iniziale dello studente, ordine logico, collegamento tra teoria, output e controlli |
| **Prompt 3**. Scomposizione input-output | 15 | proposta operativa iniziale dello studente  |
| **Notebook Jupyter** e output computazionali | 20 | codice corretto, tabelle, grafici, riproducibilità, output richiesti |
| Prompt e uso dei regimi A/B/C | 15 | qualità dei prompt, vincoli, contributo dello studente, uso appropriato dell’IA |
| Verifiche logiche, Controlli numerici | 15 | verifiche su probabilità, simulazioni, formule, quantità condizionate e proprietà teoriche |
| Interpretazione critica | 5 | autonomia, coerenza con output, ruolo dell’informazione, limiti del modello |

Totale: 100.