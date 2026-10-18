# Istruzioni per lo studente — Uso virtuoso dell’IA nei casi applicativi MQF

<style>
.prompt-docente {
  font-family: Consolas, "Courier New", monospace;
  white-space: pre-wrap;
  background: #f6f8fa;
  border: 1px solid #d0d7de;
  border-radius: 6px;
  padding: 0.9em 1em;
  line-height: 1.45;
}
</style>


## 1. Scopo del documento

Questo documento spiega come svolgere un caso applicativo MQF utilizzando l’IA in modo corretto, controllato e valutabile.

L’obiettivo non è far risolvere il caso all’IA, ma usarla come supporto per:

1. chiarire il problema;
2. organizzare il ragionamento;
3. costruire codice coerente con la Scheda Caso;
4. supportare l'esecuzione dei controlli previsti e, quando emerga una criticità specifica individuata dallo studente, verificarla in modo mirato;
5. documentare il processo seguito.

Il lavoro resta responsabilità dello studente.

---

## 2. Materiali di partenza

Per ogni caso applicativo il docente fornisce:

1. Prompt zero;
2. Prompt 1, contenente integralmente la Scheda Caso e le istruzioni fisse per produrre la cella Markdown iniziale del Jupyter Notebook;
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

Il Jupyter Notebook deve aprirsi con la cella Markdown iniziale prodotta in risposta al Prompt 1 e verificata dallo studente.

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

Il Regime A può occasionalmente includere piccoli calcoli o esempi numerici, quando servono a chiarire una proprietà teorica, una formula o una quantità del caso, ma non deve includere codice Python. La traduzione della specifica teorica in codice appartiene al Regime B.

Nel Regime A è importante che lo studente fornisca un contributo iniziale: ipotesi, dubbi, ordine logico, collegamenti teorici, proposte di lettura.

---

## 4.2 Regime B — Traduzione operativa in codice

Il Regime B serve a tradurre in Python una tappa già definita.

Lo standard del Regime B è una richiesta all’IA di scrivere codice per realizzare l’output previsto dalla tappa.

Il prompt deve indicare:

1. numero e titolo della tappa da svolgere;
2. input disponibili;
3. formule, relazioni o procedure da implementare;
4. output richiesto;
5. controlli da includere;
6. uso dell'output nella tappa successiva o nel prodotto finale;
7. vincoli da rispettare.

L’IA può scrivere codice, ma non deve cambiare la Scheda Caso.

---

## 4.3 Regime C — Verifica di una criticità specifica

Il Regime C serve a verificare una possibile criticità già individuata dallo studente nel materiale prodotto.

Può essere attivato quando lo studente rileva, per esempio:

1. un risultato numerico anomalo;
2. un dubbio teorico o matematico;
3. una possibile incoerenza con la Scheda Caso;
4. un problema nel codice o in un controllo;
5. una possibile incoerenza tra formule, output e interpretazione.

Il prompt deve indicare con precisione:

1. la parte del notebook interessata;
2. la criticità individuata;
3. il ragionamento che motiva il dubbio.

L'IA deve verificare la criticità senza modificare autonomamente la Scheda Caso e deve classificare l'esito come **criticità respinta** oppure **criticità accolta**.

Se la criticità è accolta, l'IA può proporre la correzione necessaria della parte interessata. Se è respinta, non deve proporre modifiche al notebook.

Il Regime C non è una tappa obbligatoria del lavoro e non deve essere utilizzato per chiedere una verifica generica dell'intero notebook o per delegare all'IA l'interpretazione finale.

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
| Prompt 1 | docente | fornisce integralmente la Scheda Caso come specifica vincolante e richiede la cella Markdown iniziale di inquadramento | non valuta il contributo dello studente |
| Prompt 2 | studente + IA | costruisce il Flusso logico-teorico risolutivo | valuta contributo iniziale dello studente, ordine logico, collegamento tra teoria, output e controlli |
| Prompt 3 | studente + IA | costruisce la scomposizione in tappe input-output | valuta la proposta operativa iniziale dello studente |
| Prompt di tappa | studente + IA | sviluppa le singole tappe in Regime A e/o B secondo la scomposizione operativa validata | valuta specificità del contributo dello studente, coerenza con la tappa, controlli previsti e uso appropriato dell’IA |

---

## 6. Prompt zero

Il Prompt zero è fisso ed è fornito dal docente.

Serve a inizializzare la conversazione con l’IA.

Deve essere usato senza modificarlo, salvo istruzioni esplicite del docente.

---

## 7. Prompt 1 — Scheda Caso e cella Markdown iniziale

Il Prompt 1 è fornito integralmente dal docente e contiene:

1. la Scheda Caso, che costituisce la parte variabile riferita allo specifico caso;
2. le istruzioni fisse che disciplinano la risposta dell’IA.

Il Prompt 1 è produttivo, perché genera la prima cella Markdown del Jupyter Notebook, ma non è valutativo: non richiede un contributo autonomo dello studente.

L’IA deve acquisire la Scheda Caso come specifica vincolante e non deve modificarne contenuti, variabili, formule, parametri, output, controlli o ipotesi.

La risposta deve consistere in una sola cella Markdown iniziale che:

1. inquadra titolo, contesto, domanda quantitativa, variabile finale e informazione disponibile;
2. presenta separatamente le quantità da stimare o calcolare;
3. riporta tutti gli output richiesti conservando categorie e numerazione della Scheda Caso;
4. dedica una voce distinta a ciascuna tabella e a ciascuna figura;
5. riporta i controlli richiesti conservando categorie e numerazione;
6. esplicita che la Scheda Caso costituisce la specifica vincolante del lavoro e non deve essere modificata.

La cella non deve contenere codice, Flusso logico-teorico risolutivo, tappe operative, risultati numerici, conclusioni, interpretazioni, o suggerimenti risolutivi.

La risposta dell'IA deve contenere soltanto la cella Markdown pronta da inserire nel notebook, senza testo introduttivo, commenti esterni o contenuti aggiuntivi.

Prima di inserirla nel notebook, lo studente deve verificare che la cella:

1. sia fedele alla Scheda Caso;
2. non ometta quantità, tabelle, figure o controlli richiesti;
3. non introduca contenuti estranei;
4. rispetti la struttura Markdown prevista.

Se questi vincoli non sono rispettati, lo studente deve chiedere all’IA una correzione prima di proseguire con Prompt 2.

---

## 8. Prompt 2 — Flusso logico-teorico risolutivo

Il Prompt 2 è obbligatorio ed è in Regime A.

Serve a costruire il Flusso logico-teorico risolutivo.

Lo studente deve proporre una prima sequenza di elementi teorici. L’IA può completare, correggere e ordinare.

La risposta dell'IA a questo prompt (titolo e tabella del flusso) alimenta una nuova cella Markdown del notebook. 

Prima di procedere con il Prompt 3, lo studente deve validare il Flusso logico-teorico risolutivo ottenuto, verificandone la coerenza con la Scheda Caso, la completezza degli elementi teorici, l'ordine logico dei passaggi e il collegamento con output e controlli richiesti.

### Esempio di prompt virtuoso

<pre class="prompt-docente">
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

L’output deve essere una sola cella Markdown, con un titolo sintetico coerente con la funzione del Prompt 2 e una tabella con le colonne:
Passo;
Finalità risolutiva;
Formula teorico-matematica / definizione / proprietà / teorema;
Applicazione nel caso;
Output o controllo collegato.
</pre>

---

## 9. Prompt 3 — Scomposizione in tappe input-output

Il Prompt 3 è obbligatorio e opera in Regime A/B: parte dal Flusso logico-teorico già validato e lo traduce in una scomposizione operativa delle tappe, senza sviluppare ancora il codice delle singole tappe.

Serve a trasformare il Flusso logico-teorico in una sequenza operativa di tappe.

Lo studente deve proporre una prima ipotesi di tappe, indicando per ciascuna almeno obiettivo, input disponibili, operazione prevista, output atteso e controllo principale. L’IA può verificare, completare e ordinare la proposta.

La risposta dell'IA a questo prompt (titolo, tabella con scomposizione in tappe) alimenta una nuova cella Markdown del notebook.

Prima di procedere con i prompt di tappa, lo studente deve validare la scomposizione ottenuta, verificando che:

1. tutte le tappe siano coerenti con il Flusso logico-teorico risolutivo già validato;
2. ogni tappa abbia input, operazione, output e controllo chiaramente identificati;
3. tutti gli output e i controlli richiesti dalla Scheda Caso siano coperti;
4. sia visibile il collegamento tra gli output di ciascuna tappa e gli input delle tappe successive;
5. il regime IA prevalente assegnato a ciascuna tappa sia coerente con la funzione della tappa.

### Esempio di prompt virtuoso

<pre class="prompt-docente">
Regime A/B — Scomposizione input-output.

Ho costruito il Flusso logico-teorico risolutivo e devo trasformarlo in tappe operative.

Propongo questa prima ipotesi:

1. definire i parametri del caso e controllare che le probabilità degli eventi sommino a uno;
2. simulare i regimi informativi secondo le probabilità assegnate;
3. simulare la variabile di rischio condizionatamente al regime estratto;
4. costruire la variabile finale del caso applicando la formula prevista;
5. produrre statistiche e grafici non condizionati;
6. calcolare le medie condizionate per regime;
7. verificare la formula del valore atteso totale;
8. eseguire i controlli conclusivi e predisporre gli elementi quantitativi necessari all'interpretazione finale, che resta responsabilità dello studente.

Ti chiedo di verificare, modificare, integrare e ordinare questa proposta.

La scomposizione deve:
- rispettare l'ordine logico del Flusso logico-teorico risolutivo già validato;
- rendere ogni tappa riconducibile ad almeno un passaggio del flusso;
- coprire tutti gli output e tutti i controlli richiesti dalla Scheda Caso;
- mantenere visibile il collegamento tra gli output di ciascuna tappa e gli input della tappa successiva.

L'output deve essere una sola cella Markdown, con un titolo sintetico e una tabella.
    
Per ogni tappa, indica:
- titolo;
- obiettivo;
- input;
- oggetti teorici coinvolti;
- operazione;
- output;
- controllo;
- uso nella tappa successiva;
- regime IA prevalente.

Non scrivere codice.
Non produrre direttamente le celle delle singole tappe del notebook.
Non produrre risultati numerici, tabelle di risultati o grafici.
Non modificare la Scheda Caso.
Non modificare il Flusso logico-teorico risolutivo già validato.

Se rilevi una possibile incoerenza tra il flusso e la scomposizione proposta, segnalala esplicitamente senza correggere autonomamente il flusso.

Se un output o un controllo richiesto dalla Scheda Caso non risulta associato ad alcuna tappa, segnalalo esplicitamente.
    
</pre>

---

## 10. Libreria di "Prompt di tappa" virtuosi

A seguito del Prompt 3, inizia una successione di prompt di tappa in Regime A e/o B, coerenti con la scomposizione operativa validata. Eventuali Prompt C possono essere aggiunti soltanto quando lo studente individua una criticità specifica da verificare.

Gli esempi seguenti devono essere adattati al caso specifico.

Non devono essere copiati meccanicamente. Un prompt virtuoso deve sempre indicare:

1. che cosa è già stato fatto;
2. che cosa si sta chiedendo all’IA;
3. quali vincoli devono essere rispettati;
4. quale output si vuole ottenere;
5. quale controllo è previsto dalla tappa ed eventuali dubbi specifici dello studente.

---

## 10.1 Prompt di tappa in Regime A — Chiarimento teorico

Lo scopo delle tappe in regime A è la "comprensione" degli aspetti del caso. Per il Regime A la parte variabile deve mostrare un ragionamento iniziale dello studente alla base della interrogazione. L’IA deve ricevere istruzioni abbastanza precise.


<pre class="prompt-docente">
Regime A — Ricognizione teorico-modellistica.

PARTE VARIABILE — contributo iniziale dello studente

Sto lavorando sulla Tappa [numero] — [titolo della tappa].

Per questa tappa dispongo dei seguenti input:
- [input 1];
- [input 2];
- [ulteriori input].

Secondo me, per questa tappa sono rilevanti i seguenti elementi teorici:
- [variabili, eventi, distribuzioni, formule o proprietà];
- [quantità da stimare o calcolare];
- [output atteso];
- [controllo logico o numerico previsto].

Il mio ragionamento è il seguente:
[descrivere sinteticamente l'ordine logico dei passaggi].

Ho questi dubbi o punti da verificare:
[indicare eventuali dubbi, alternative o aspetti da chiarire].

PARTE FISSA — istruzioni per l'IA

Ti chiedo di verificare, completare e ordinare questo ragionamento limitatamente alla tappa corrente.

Non devi:
- risolvere l'intero problema;
- scegliere un modello diverso da quello fissato nella Scheda Caso;
- modificare variabili, formule, ipotesi, parametri, output o controlli previsti;
- scrivere codice;
- anticipare le tappe successive.

Devi:
- segnalare eventuali elementi teorici mancanti, ridondanti o fuori ordine;
- correggere eventuali confusioni teoriche;
- chiarire il collegamento tra input, oggetti teorici, output e controllo della tappa.

L'output deve essere una sola cella Markdown della tappa che contenga, in forma sintetica:
1. obiettivo della tappa;
2. input disponibili;
3. oggetti teorici coinvolti;
4. passaggio logico da svolgere;
5. output atteso;
6. controllo da eseguire;
7. uso dell'output nella tappa successiva, se rilevante.
</pre>


### Esempio A1 — Simulazione dei regimi informativi

<pre class="prompt-docente">
Regime A.

PARTE VARIABILE — contributo iniziale dello studente

Sto lavorando sulla Tappa [numero] — Simulazione dei regimi informativi.

Secondo me l’input è dato dalle probabilità degli eventi e dal numero di simulazioni. L’output deve essere una sequenza simulata di eventi. Il controllo principale è confrontare le frequenze empiriche con le probabilità teoriche.

PARTE FISSA — istruzioni per l'IA

Ti chiedo di verificare se questa lettura è corretta e se manca qualche controllo teorico o logico. L'output deve essere una cella Markdown della tappa che chiarisca:

1. obiettivo della tappa;
2. input disponibili;
3. oggetti teorici coinvolti;
4. passaggio logico da svolgere;
5. output atteso;
6. controllo da eseguire;
7. uso dell'output nella tappa successiva, se rilevante.

Non modificare la Scheda Caso.
</pre>

### Esempio A2 — Distribuzione condizionata

<pre class="prompt-docente">
Regime A.

PARTE VARIABILE — contributo iniziale dello studente

Sto lavorando sulla Tappa [numero] — Distribuzione condizionata.

La mia idea è che, dopo avere simulato il regime, devo usare la distribuzione condizionata prevista per quel regime. Il controllo dovrebbe confrontare media e deviazione standard empiriche con i parametri teorici.

PARTE FISSA — istruzioni per l'IA

Ti chiedo di verificare se la logica è corretta e se l’output della tappa è ben definito. L'output deve essere una cella Markdown della tappa che chiarisca:

1. obiettivo della tappa;
2. input disponibili;
3. oggetti teorici coinvolti;
4. passaggio logico da svolgere;
5. output atteso;
6. controllo da eseguire;
7. uso dell'output nella tappa successiva, se rilevante.
</pre>

### Esempio A3 — Trasformazione nella variabile finale

<pre class="prompt-docente">
Regime A.

PARTE VARIABILE — contributo iniziale dello studente

Sto lavorando sulla Tappa [numero] — Trasformazione nella variabile finale.

Secondo me devo applicare la formula indicata nella Scheda Caso e poi controllare che il risultato abbia il segno e l’interpretazione corretta.

PARTE FISSA — istruzioni per l'IA

Ti chiedo di verificare se sto distinguendo correttamente fattore di rischio, variabile derivata e output finale.
L'output deve essere una cella Markdown della tappa che chiarisca:

1. obiettivo della tappa;
2. input disponibili;
3. oggetti teorici coinvolti;
4. passaggio logico da svolgere;
5. output atteso;
6. controllo da eseguire;
7. uso dell'output nella tappa successiva, se rilevante.

Non cambiare la formula del caso.
</pre>

### Esempio A4 — Valore atteso condizionato

<pre class="prompt-docente">
Regime A.

PARTE VARIABILE — contributo iniziale dello studente

Sto lavorando sulla Tappa [numero] — Valore atteso condizionato.

Secondo me devo raggruppare le osservazioni in base agli eventi della partizione e calcolare una media per ciascun gruppo. Devo poi distinguere tra la media condizionata rispetto a un evento e il valore atteso condizionato rispetto alla sigma-algebra generata dalla partizione.

PARTE FISSA — istruzioni per l'IA

Ti chiedo di verificare se questa distinzione è corretta e come deve essere resa visibile nel notebook.
L'output deve essere una cella Markdown della tappa che chiarisca:

1. obiettivo della tappa;
2. input disponibili;
3. oggetti teorici coinvolti;
4. passaggio logico da svolgere;
5. output atteso;
6. controllo da eseguire;
7. uso dell'output nella tappa successiva, se rilevante.
</pre>

---

## 10.2 Prompt di tappa in Regime B — Codice Python

### Esempio B1 — Definizione dei parametri

<pre class="prompt-docente">
Regime B — Traduzione operativa in codice.

Sto lavorando sulla Tappa [numero] — Definizione dei parametri.

Per questa tappa dispongo dei seguenti input:
- parametri della Scheda Caso;
- probabilità degli eventi;
- parametri delle distribuzioni condizionate;
- numero di simulazioni;
- seed.

Le procedure da implementare sono:
- organizzare i parametri in strutture dati leggibili;
- verificare la coerenza delle probabilità;
- calcolare eventuali soglie implicite previste dalla Scheda Caso.

L'output richiesto è:
- tabella dei parametri;
- eventuali soglie implicite previste dal caso.

I controlli da includere sono:
- verifica che le probabilità sommino a uno;
- verifica della coerenza dei parametri con la Scheda Caso.

L'output della tappa sarà utilizzato successivamente come input per le procedure di simulazione.

I vincoli da rispettare sono:
- non modificare parametri, formule o probabilità;
- non introdurre quantità non previste dalla Scheda Caso.

Produci:
- una cella Markdown che riporti separatamente la copia fedele della richiesta dello studente e una sintesi logica degli input, delle operazioni, degli output, dei controlli e dell'uso successivo della tappa;
- una cella Python chiara e verificabile.
</pre>


### Esempio B2 — Simulazione gerarchica

<pre class="prompt-docente">
Regime B — Traduzione operativa in codice.

Sto lavorando sulla Tappa [numero] — Simulazione gerarchica.

Per questa tappa dispongo dei seguenti input:
- probabilità dei regimi informativi;
- parametri delle distribuzioni condizionate;
- numero di simulazioni;
- seed.

Le procedure da implementare sono:
1. simulare il regime informativo;
2. simulare la variabile di rischio condizionatamente al regime estratto;
3. costruire un dataset contenente regime simulato e variabile simulata.

L'output richiesto è:
- dataset simulato;
- tabella delle frequenze empiriche dei regimi;
- statistiche empiriche della variabile di rischio per regime.

I controlli da includere sono:
- confronto tra frequenze empiriche e probabilità teoriche;
- confronto tra statistiche empiriche per regime e parametri teorici assegnati.

L'output della tappa sarà utilizzato successivamente per costruire la variabile finale del caso.

I vincoli da rispettare sono:
- non introdurre nuovi oggetti teorici;
- non modificare la Scheda Caso;
- utilizzare soltanto le distribuzioni e i parametri già fissati.

Produci:
- una cella Markdown che riporti separatamente la copia fedele della richiesta dello studente e una sintesi logica degli input, delle operazioni, degli output, dei controlli e dell'uso successivo della tappa;
- una cella Python chiara e commentata.
</pre>

### Esempio B3 — Calcolo della variabile finale

<pre class="prompt-docente">
Regime B — Traduzione operativa in codice.

Sto lavorando sulla Tappa [numero] — Calcolo della variabile finale.

Per questa tappa dispongo dei seguenti input:
- dataset simulato;
- variabile di rischio;
- parametri necessari alla formula fissata nella Scheda Caso.

La procedura da implementare è:
- applicare la formula prevista dalla Scheda Caso per costruire la variabile finale.

L'output richiesto è:
- nuova colonna del dataset contenente la variabile finale.

I controlli da includere sono:
- controllo della corretta applicazione della formula;
- controllo dimensionale;
- controllo del segno o della parte positiva, quando previsto dalla Scheda Caso.

L'output della tappa sarà utilizzato successivamente per produrre statistiche, tabelle, grafici e quantità condizionate richieste dal caso.

I vincoli da rispettare sono:
- non modificare la formula;
- non modificare il significato economico-finanziario della variabile finale;
- non introdurre trasformazioni non previste dalla Scheda Caso.

Produci:
- una cella Markdown che riporti separatamente la copia fedele della richiesta dello studente e una sintesi logica degli input, dell'operazione, dell'output, dei controlli e dell'uso successivo della tappa;
- una cella Python chiara e verificabile.
</pre>

### Esempio B4 — Output non condizionati e condizionati

<pre class="prompt-docente">
Regime B — Traduzione operativa in codice.

Sto lavorando sulla Tappa [numero] — Output non condizionati e condizionati.

Per questa tappa dispongo dei seguenti input:
- dataset finale;
- variabile finale del caso;
- eventi o regimi simulati;
- soglie richieste.

Le procedure da implementare sono:
- calcolare le statistiche non condizionate richieste;
- calcolare quantili e probabilità di superamento delle soglie;
- calcolare le medie condizionate per regime;
- verificare la formula del valore atteso totale;
- produrre i grafici essenziali previsti dalla Scheda Caso.

L'output richiesto è:
- statistiche non condizionate;
- quantili;
- probabilità di superamento soglia;
- medie condizionate per regime;
- verifica numerica della formula del valore atteso totale;
- grafici essenziali.

I controlli da includere sono:
- coerenza tra quantità non condizionate e condizionate;
- verifica della formula del valore atteso totale;
- coerenza degli output con le quantità richieste dalla Scheda Caso.

L'output della tappa sarà utilizzato successivamente per i controlli conclusivi e per l'interpretazione finale dello studente.

I vincoli da rispettare sono:
- non introdurre statistiche o grafici non richiesti senza motivazione;
- non modificare le definizioni delle quantità teoriche;
- non produrre l'interpretazione finale al posto dello studente.

Produci:
- una cella Markdown che riporti separatamente la copia fedele della richiesta dello studente e una sintesi logica degli input, delle operazioni, degli output, dei controlli e dell'uso successivo della tappa;
- una cella Python ordinata, con tabelle leggibili e controlli espliciti.
</pre>

---

## 10.3 Prompt in Regime C — Verifica di una criticità specifica

Il Regime C si attiva soltanto quando lo studente individua una criticità specifica da verificare. Il prompt deve quindi essere mirato e non deve chiedere all'IA di controllare genericamente l'intero lavoro.

Devi usare un prompt in Regime C quando, durante la costruzione del notebook, individui:

1. un risultato numerico anomalo;
2. un dubbio teorico o matematico;
3. una possibile incoerenza con la Scheda Caso;
4. una formulazione Markdown poco chiara o non coerente;
5. un passaggio di codice che produce output non convincenti;
6. una specifica incoerenza tra l'interpretazione proposta dallo studente e i risultati numerici, i grafici, le ipotesi o i limiti del modello.

Il tuo compito non è correggere direttamente il notebook, ma formulare chiaramente il dubbio e chiedere all'IA di verificarlo.

Nel prompt devi indicare:

1. quale tappa, formula, output, grafico, tabella o cella è interessata;
2. quale dubbio hai individuato;
3. perché pensi che possa esserci un problema;
4. quale materiale deve essere controllato;
5. che l'IA deve classificare l'esito della verifica come:
   - **criticità respinta**;
   - **criticità accolta**.

Se la criticità è respinta, il notebook non viene modificato. La verifica resta documentata solo nel tracciato IA.

Se la criticità è accolta, il notebook viene corretto, ma deve rimanere pulito. Non devi conservare celle errate, celle duplicate o celle aggiuntive di verifica. Le celle della tappa interessata devono essere sostituite con versioni corrette e più informative.

In particolare, la nuova cella Markdown della tappa deve includere al proprio interno, in forma sintetica:

1. criticità individuata;
2. origine della criticità;
3. modifica adottata.

Se è necessario modificare anche il codice, la nuova cella code deve sostituire quella precedente. Il codice può contenere brevi commenti che segnalano la modifica adottata, ma non deve mantenere la versione errata.

La valutazione terrà conto del fatto che:
1. il dubbio deve essere formulato dallo studente;
2. la verifica deve essere documentata nella chat IA;
3. se la criticità è accolta, la modifica deve risultare visibile nelle celle corrette del notebook;
4. il notebook finale deve restare lineare, eseguibile e composto solo dalle celle previste per Prompt 1, Prompt 2, Prompt 3, tappe operative, controlli conclusivi e interpretazione finale.

### Schema di prompt C

<pre class="prompt-docente">
Regime C — Verifica di una criticità specifica.

Sto lavorando sulla seguente parte del notebook:

[indicare Prompt 2, Prompt 3 oppure la tappa interessata. Inserire formula, output, tabella, grafico, testo Markdown o codice interessato]

Ho individuato questo dubbio / possibile problema:

[descrivere il dubbio, l'anomalia o l'incoerenza]

Il mio ragionamento è:

[spiegare perché il risultato, la formula, il testo o il codice non mi convince]

Ti chiedo di verificare criticamente il problema e di classificare l'esito della verifica in uno solo dei due casi:

1. criticità respinta;
2. criticità accolta.

Se la criticità è respinta:
- spiegami perché il dubbio non richiede modifiche;
- non proporre modifiche al notebook.

Se la criticità è accolta:
- spiegami come si è generata la criticità, indicando quale passaggio, assunzione, formula, scelta di codice o interpretazione l’ha prodotta e perché non è coerente con la Scheda Caso, con la teoria, con la logica della tappa o con gli output attesi;
- produci la versione sostitutiva della cella Markdown della tappa, includendo nella cella:
  1. criticità individuata;
  2. origine della criticità;
  3. modifica adottata;
- produci, se necessario, la versione sostitutiva della cella code;
- non proporre celle extra;
- non mantenere la versione errata;
- non modificare la Scheda Caso.
</pre>


### Esempio C1 — Frequenze simulate inattese

<pre class="prompt-docente">
Regime C — Verifica di una criticità specifica.

PARTE VARIABILE — da adattare da parte dello studente

Sto lavorando sulla seguente parte del notebook:
Tappa di simulazione dei regimi informativi, Tabella delle frequenze empiriche dei regimi e le probabilità teoriche

Ho individuato questo dubbio / possibile problema:
con n = [inserire numero di simulazioni], le frequenze empiriche degli eventi risultano abbastanza diverse dalle probabilità teoriche. Mi aspettavo scostamenti più piccoli.

Il mio ragionamento è:
se la simulazione dei regimi è costruita correttamente, le frequenze empiriche dovrebbero essere vicine alle probabilità teoriche, salvo normale variabilità Monte Carlo. Non capisco se lo scostamento osservato sia plausibile oppure se derivi da un errore nella simulazione, nella lettura dei parametri o nel conteggio dei regimi.


PARTE FISSA — istruzioni per l'IA

Ti chiedo di verificare criticamente il problema.

Classifica l'esito della verifica in uno solo dei due casi:

1. criticità respinta;
2. criticità accolta.

Se la criticità è respinta:
- spiegami perché il dubbio non richiede modifiche;
- non proporre modifiche al notebook.

Se la criticità è accolta:
- spiegami come si è generata la criticità, indicando quale passaggio, assunzione, formula, scelta di codice o interpretazione l'ha prodotta e perché non è coerente con la Scheda Caso, con la teoria, con la logica della tappa o con gli output attesi;
- produci la versione sostitutiva della cella Markdown della tappa, includendo nella cella:
  1. criticità individuata;
  2. origine della criticità;
  3. modifica adottata;
- produci, se necessario, la versione sostitutiva della cella code;
- inserisci nella cella code solo commenti essenziali collegati alla correzione;
- non proporre celle extra;
- non mantenere la versione errata;
- non modificare la Scheda Caso.
</pre>

### Esempio C2 — Segno inatteso della perdita

<pre class="prompt-docente">
Regime C — Verifica di una criticità specifica.

PARTE VARIABILE — da adattare da parte dello studente

Sto lavorando sulla seguente parte del notebook:
Tappa di trasformazione dello shock di rendimento nella perdita del portafoglio obbligazionario; formula usata nel notebook, riepilogo statistico in cui compaiono valori negativi di L

Ho individuato questo dubbio / possibile problema:
in alcune simulazioni ottengo valori negativi della perdita L. All'inizio pensavo che una perdita dovesse essere sempre positiva.

Il mio ragionamento è:
la Scheda Caso definisce la perdita mediante la formula L = D V0 Delta y. Se Delta y è negativo, allora anche L risulta negativo. Non capisco se questo sia un errore di segno nel codice oppure se vada interpretato come guadagno del portafoglio quando lo shock di rendimento è negativo.


PARTE FISSA — istruzioni per l'IA

Ti chiedo di verificare criticamente il problema.

Classifica l'esito della verifica in uno solo dei due casi:

1. criticità respinta;
2. criticità accolta.

Se la criticità è respinta:
- spiegami perché il dubbio non richiede modifiche;
- non proporre modifiche al notebook.

Se la criticità è accolta:
- spiegami come si è generata la criticità, indicando quale passaggio, assunzione, formula, scelta di codice o interpretazione l'ha prodotta e perché non è coerente con la Scheda Caso, con la teoria, con la logica della tappa o con gli output attesi;
- produci la versione sostitutiva della cella Markdown della tappa, includendo nella cella:
  1. criticità individuata;
  2. origine della criticità;
  3. modifica adottata;
- produci, se necessario, la versione sostitutiva della cella code;
- inserisci nella cella code solo commenti essenziali collegati alla correzione;
- non proporre celle extra;
- non mantenere la versione errata;
- non modificare la Scheda Caso;
- non proporre una trasformazione in parte positiva se non è prevista dalla Scheda Caso.
</pre>

---
<!--
## 10.4 Prompt conclusivi in Regime C

Anche i prompt conclusivi devono essere mirati. Non devono essere liste universali da copiare.

Lo studente deve scegliere quale aspetto finale verificare.

### Esempio F1 — Verifica finale della coerenza tra notebook e Scheda Caso

<pre class="prompt-docente">
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
</pre>


### Esempio F3 — Verifica finale dell’interpretazione

<pre class="prompt-docente">
Regime C — Verifica finale mirata.

Mi sto focalizzando solo sull’interpretazione finale.

La mia interpretazione finale è ... . Con riferimento ai grafici prodotti si conferma che... . Con riferimento ai risultati numerici si conferma che ... .

Ti chiedo di verificare se ho incluso gli elementi rilevanti ed eventualmente di modificare / integrare il testo della mia interpretazione.:

Non riscrivere l’intera conclusione.
Suggerisci solo modifiche puntuali.
</pre>
-->
---

## 11. Come preparare la stampa PDF della chat IA

La chat IA consegnata deve documentare l'intero processo di lavoro, inclusivo di tutti i prompt e le risposte dell'IA.

Deve contenere:

1. Prompt zero e relativa risposta;
2. Prompt 1 completo, inclusivo della Scheda Caso e delle istruzioni fisse;
3. risposta IA al Prompt 1, contenente la cella Markdown iniziale;
4. Prompt 2;
5. risposta IA al Prompt 2;
6. Prompt 3;
7. risposta IA al Prompt 3;
8. prompt di tappa e relative risposte IA;
9. eventuali prompt di verifica e relative risposte IA;
10. interpretazione finale o verifica dell’interpretazione.

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

Gli eventuali prompt in Regime C sono valutati soltanto quando vengono effettivamente attivati a partire da una criticità specifica individuata dallo studente.

La loro valutazione considera:

1. precisione con cui la criticità è stata individuata e formulata;
2. qualità del ragionamento iniziale dello studente;
3. appropriatezza della verifica richiesta all'IA;
4. capacità di recepire correttamente l'esito della verifica, distinguendo tra criticità respinta e criticità accolta.

L'assenza di prompt in Regime C non costituisce di per sé una carenza del lavoro.

---

## 14. Tabella indicativa di valutazione

I pesi sono indicativi e possono essere modificati dal docente per ciascun esercizio take-home.

| Area | Peso indicativo | Criteri principali |
|---|---:|---|
| **Prompt 2**. Flusso logico-teorico risolutivo | 30 | contributo iniziale dello studente, ordine logico, collegamento tra teoria, output e controlli |
| **Prompt 3**. Scomposizione input-output | 15 | proposta operativa iniziale dello studente  |
| **Notebook Jupyter** e output computazionali | 20 | codice corretto, tabelle, grafici, riproducibilità, output richiesti |
| Prompt di tappa e uso dei Regimi A/B; eventuale Regime C | 15 | qualità dei prompt, rispetto dei vincoli, contributo dello studente, uso appropriato dell’IA e, quando presente, qualità dell’attivazione del Regime C a partire da una criticità specifica |
| Verifiche logiche, Controlli numerici | 15 | verifiche su probabilità, simulazioni, formule, quantità condizionate e proprietà teoriche |
| Interpretazione finanziaria finale | 5 | autonomia, coerenza con gli output, ruolo dell’informazione e consapevolezza dei limiti del modello |

Totale: 100.

