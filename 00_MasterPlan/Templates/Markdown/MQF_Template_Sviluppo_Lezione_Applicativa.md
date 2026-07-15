# Template - Sviluppo di una lezione applicativa

Sto sviluppando una delle cinque lezioni applicative Python del corso magistrale MQF — Metodi Quantitativi per la Finanza.

La lezione applicativa deve essere sviluppata in modo coerente con la teoria dell’uso virtuoso dell’AI già definita nel progetto. In particolare, l’obiettivo non è insegnare Python come contenuto autonomo, ma usare Python e AI per rendere osservabili, simulabili e verificabili modelli quantitativi applicati alla finanza.

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
4. una successione di prompt virtuosi per il caso aula;
5. un notebook Jupyter in cui ogni tappa sia documentata da celle Markdown e celle codice;
6. una scheda di calibrazione docente per il caso take-home;
7. un template `.md` per il tracciato AI degli studenti;
8. una rubrica di valutazione del notebook e del tracciato AI.

La progettazione deve rispettare i tre regimi dell’interazione studente–AI:

**Regime A — Ricognizione teorico-modellistica.**
Lo studente, con supporto dell’AI, identifica grandezze economico-finanziarie, variabili casuali o decisionali, eventi, stati informativi, scenari, ipotesi, formule e quantità teoriche. L’AI non deve risolvere il problema né imporre il modello finale.

**Regime B — traduzione operativa in codice.**
Data una specifica teorica validata, l’AI può costruire l’apparato computazionale: simulazione, dataset, struttura delle celle, codice Python, tabelle, output numerici e implementazione tecnica dei grafici. L’AI non deve modificare variabili, eventi, formule, ipotesi o significato finanziario del problema.

**Regime C — Verifica e interpretazione critica.**
Lo studente verifica e interpreta. L’AI può intervenire solo come revisore critico di controlli, interpretazioni o discussioni già formulate dallo studente. L’AI non deve produrre l’interpretazione finale al posto dello studente.

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
3. regime prevalente A/B/C;
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
6. numero minimo e massimo di prompt ammessi per il tracciato studente;
7. criteri di valutazione.

La valutazione degli studenti deve basarsi congiuntamente su:

1. qualità delle premesse teorico-matematiche identificate;
2. corretta scomposizione in tappe;
3. coerenza degli input/output che collegano le tappe;
4. qualità degli output richiesti;
5. qualità e virtù dei prompt utilizzati;
6. rispetto dei regimi A/B/C;
7. capacità di verifica e interpretazione critica.

La valutazione non deve premiare la complessità autonoma del codice Python. Deve valutare la capacità dello studente di governare l’interazione con l’AI mantenendo controllo teorico, computazionale e interpretativo del problema quantitativo-finanziario.

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
5. potenziale didattico per l’uso virtuoso dell’AI.
