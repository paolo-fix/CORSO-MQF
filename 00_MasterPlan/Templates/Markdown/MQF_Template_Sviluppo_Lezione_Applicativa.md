# Template - Sviluppo di una lezione applicativa

Sto sviluppando una delle cinque lezioni applicative Python del corso magistrale MQF — Metodi Quantitativi per la Finanza.

La lezione applicativa deve essere sviluppata in modo coerente con la teoria dell’uso virtuoso dell’IA già definita nel progetto. In particolare, l’obiettivo non è insegnare Python come contenuto autonomo, ma usare Python e IA per rendere osservabili, simulabili e verificabili modelli quantitativi applicati alla finanza.

Prima di scrivere contenuti, leggi nel repository del progetto:

1. `00_MasterPlan/MQF_Master_Plan.tex`;
2. `00_MasterPlan/MQF_Project_Guidelines.md`;
3. `00_MasterPlan/MQF_Notazione.tex`;
4. `00_MasterPlan/MQF_Stato_Avanzamento.md`;
5. `00_MasterPlan/Templates/MQF_Catalogo_Template.md`;
6. il capitolo precedente e, se già disponibile, il capitolo della lezione applicativa in corso;
7. eventuali notebook o materiali già presenti nella cartella `04_Codice/LezNN/`.

Per questa lezione applicativa occorre progettare:

1. un caso da sviluppare in aula;
2. un caso take-home distinto ma metodologicamente comparabile;
3. una scomposizione del caso aula in tappe logiche;
4. la sequenza dei prompt del Caso Aula: Prompt zero, Prompt 1, Prompt 2, Prompt 3, prompt di tappa in Regime A/B ed eventuali Prompt C soltanto in presenza di criticità specifiche individuate dallo studente;
5. un notebook Jupyter in cui ogni tappa sia documentata da celle Markdown e celle codice;
6. una scheda di calibrazione docente per il caso take-home;
7. le istruzioni per la consegna del tracciato IA, ordinariamente mediante stampa PDF della chat dedicata;
8. una rubrica di valutazione del notebook e del tracciato IA.

La progettazione deve rispettare i Regimi A e B come modalità ordinarie di interazione studente–IA e prevedere il Regime C soltanto come modalità eventuale di verifica di una criticità specifica:

**Regime A — Ricognizione teorico-modellistica.**
Lo studente, con supporto dell’IA, identifica grandezze economico-finanziarie, variabili casuali o decisionali, eventi, stati informativi, scenari, ipotesi, formule e quantità teoriche. L’IA non deve risolvere il problema né imporre il modello finale.

**Regime B — traduzione operativa in codice.**
Data una specifica teorica validata, l’IA può costruire l’apparato computazionale: simulazione, dataset, struttura delle celle, codice Python, tabelle, output numerici e implementazione tecnica dei grafici. L’IA non deve modificare variabili, eventi, formule, ipotesi o significato finanziario del problema.

**Regime C — Verifica di una criticità specifica.**
Il Regime C può essere attivato soltanto quando lo studente individua un dubbio, un'anomalia o una possibile incoerenza specifica nel materiale già prodotto. L'IA verifica la criticità e ne classifica l'esito come criticità respinta oppure criticità accolta. L'IA non deve produrre l'interpretazione finale al posto dello studente.

La progettazione deve inoltre rispettare due scale di lavoro:

1. **livello macro**, relativo al problema complessivo: inquadramento teorico, percorso risolutivo, tappe principali, output finali;
2. **livello micro**, relativo alla singola tappa: input disponibili, operazione della tappa, output prodotto, uso dell’output nella tappa successiva.

Ogni tappa deve essere trattata come modulo input–output:

\[
\text{input}_k
\rightarrow
\text{operazione}_k
\rightarrow
\text{output}_k
\rightarrow
\text{uso in } k+1.
\]

Per ogni tappa occorre esplicitare:

1. input dalla tappa precedente;
2. obiettivo della tappa;
3. regime prevalente A/B; eventuale Regime C soltanto in presenza di una criticità specifica individuata dallo studente;
4. prompt virtuoso di riferimento;
5. oggetti teorici coinvolti;
6. operazione computazionale richiesta;
7. output prodotto;
8. controllo numerico, logico o interpretativo;
9. uso dell’output nella tappa successiva.

Il caso aula deve essere sufficientemente ricco da mostrare il metodo, ma non eccessivamente lungo. Il caso take-home deve essere distinto dal caso aula, ma isomorfo sul piano metodologico: deve richiedere strumenti teorici e passaggi analoghi, senza ridursi a una semplice variazione parametrica.

Per il caso take-home occorre produrre una scheda docente di calibrazione contenente:

1. premesse teorico-matematiche attese;
2. scomposizione attesa in tappe;
3. collegamenti input/output tra tappe;
4. output richiesti: stime, tabelle, grafici, controlli;
5. successione di prompt docente di riferimento;
6. sequenza dei prompt prevista dal caso, determinata dalla scomposizione operativa validata, con eventuali Prompt C soltanto in presenza di criticità specifiche individuate dallo studente;
7. criteri di valutazione.

La valutazione degli studenti deve basarsi congiuntamente su:

1. qualità delle premesse teorico-matematiche identificate;
2. corretta scomposizione in tappe;
3. coerenza degli input/output che collegano le tappe;
4. qualità degli output richiesti;
5. qualità e virtù dei prompt utilizzati;
6. uso appropriato dei Regimi A/B e, quando effettivamente attivato, del Regime C a partire da una criticità specifica individuata dallo studente;
7. qualità dei controlli conclusivi e autonomia dell'interpretazione finale dello studente.

La valutazione non deve premiare la complessità autonoma del codice Python. Deve valutare la capacità dello studente di governare l’interazione con l’IA mantenendo controllo teorico, computazionale e interpretativo del problema quantitativo-finanziario.

La lezione specifica da sviluppare è:

**Lezione [numero] — [titolo della lezione applicativa]**

Temi teorici collegati:
[elencare i temi teorici già trattati nel corso]

Obiettivo applicativo:
[descrivere l’obiettivo finanziario o quantitativo della lezione]

Prima attività richiesta:
proponi due possibili coppie “caso aula / caso take-home”, motivando per ciascuna:

1. coerenza con il programma;
2. livello di complessità;
3. oggetti teorici coinvolti;
4. output computazionali producibili;
5. potenziale didattico per l’uso virtuoso dell’IA.
