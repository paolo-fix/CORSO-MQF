# Metodi Quantitativi per la Finanza — Linee guida di progetto

TEST CACHE 2026-05-30 17:45

## 1. Identificazione del progetto

Il progetto riguarda la predisposizione completa del materiale didattico per il corso universitario **Metodi Quantitativi per la Finanza**.

Il corso e' destinato a studenti del quinto anno del corso di laurea in **Banca e Risk Management**. Gli studenti hanno una preparazione mediamente solida nei metodi quantitativi e statistici, e una preparazione buona nella teoria finanziaria e nei modelli finanziari. Il materiale deve quindi mantenere un livello accademico rigoroso, evitando sia un approccio eccessivamente divulgativo sia un formalismo astratto non motivato dalle applicazioni finanziarie.

Il corso deve essere sviluppato in italiano. Il manuale, le slides e i materiali matematici devono essere scritti in LaTeX compatibile con **Scientific Workplace 5.5**. Questo documento, invece, e' scritto in Markdown per essere caricato su GitHub e usato come linea guida operativa nelle future chat dedicate allo sviluppo del progetto.

## 2. Formato consigliato per questo documento

Il formato piu' idoneo per queste linee guida e' **Markdown**, con estensione `.md`.

Le ragioni sono le seguenti:

1. Markdown e' nativamente leggibile su GitHub.
2. E' facilmente versionabile con Git.
3. E' leggibile anche come semplice file di testo.
4. Puo' essere copiato integralmente o parzialmente nelle nuove chat di ChatGPT.
5. Mantiene una struttura gerarchica chiara mediante titoli, elenchi e sezioni.
6. Evita la complessita' sintattica del LaTeX quando lo scopo non e' la compilazione tipografica, ma il coordinamento del progetto.

Il nome consigliato del file e':

```text
MQF_Project_Guidelines.md
```

Il file dovrebbe essere collocato nella cartella di progetto:

```text
/progetto/MQF_Project_Guidelines.md
```

## 3. Finalita' generale del corso

Il corso deve fornire agli studenti strumenti quantitativi per rappresentare l'incertezza, modellizzare fenomeni finanziari discreti, misurare il rischio e formulare problemi decisionali in presenza di vincoli e scenari.

La finalita' generale non e' presentare una raccolta eterogenea di tecniche matematiche, ma costruire un percorso unitario centrato su tre assi concettuali:

1. modellizzazione probabilistica dell'incertezza;
2. valutazione finanziaria in tempo discreto;
3. decisione quantitativa sotto rischio e sotto incertezza.

Ogni lezione deve contribuire esplicitamente a uno o piu' di questi assi. Le connessioni tra probabilita', processi stocastici, misure di rischio, pricing binomiale, programmazione lineare e programmazione stocastica devono essere rese chiare e ricorrenti.

## 4. Prodotti finali previsti

Il progetto prevede la costruzione dei seguenti prodotti finali:

1. un manuale del corso, articolato in 16 capitoli o unita' didattiche;
2. le slides delle 16 lezioni;
3. un insieme di esercizi teorici e numerici da svolgere in aula;
4. cinque applicazioni Python coerenti con il syllabus;
5. un registro dei grafici didattici;
6. un documento autonomo di notazione matematica;
7. eventuali materiali ausiliari, quali soluzioni degli esercizi, template LaTeX, script Python e figure.

I materiali devono essere progettati in modo modulare, cosi' da consentire lo sviluppo separato di singole lezioni, capitoli, slides o applicazioni computazionali senza perdere coerenza complessiva.

## 5. Architettura concettuale del corso

Il corso deve seguire una progressione logica fondata su dieci passaggi concettuali:

1. rappresentazione probabilistica dell'incertezza;
2. variabili casuali, distribuzioni e momenti;
3. informazione e valore atteso condizionato;
4. processi stocastici e scenari;
5. catene di Markov e rischio di credito;
6. misure di rischio;
7. alberi binomiali e pricing finanziario;
8. programmazione lineare e dualita';
9. CVaR come problema di ottimizzazione lineare;
10. programmazione stocastica e decisioni in presenza di scenari.

Questa progressione deve orientare la scrittura del manuale, delle slides e degli esercizi. In particolare, le lezioni iniziali di probabilita' non devono essere presentate come un richiamo isolato, ma come la base necessaria per i modelli finanziari successivi.

## 6. Struttura delle 16 lezioni

La struttura operativa del corso e' la seguente.

| Lezione | Tipo | Titolo definitivo | Tema centrale |
|---:|:---:|---|---|
| 1 | P | Elementi di teoria della probabilita' | Spazio di probabilita', eventi, probabilita' condizionata |
| 2 | P | Variabili casuali e distribuzioni | Variabili casuali, distribuzioni, momenti, quantili |
| 3 | P | Valori attesi condizionati e informazione | Condizionamento, partizioni, informazione |
| 4 | P | Processi stocastici, traiettorie e scenari | Processi in tempo discreto, simulazione, scenari |
| 5 | C | Applicazioni Python a processi stocastici e valori attesi condizionati | Simulazione e stima computazionale |
| 6 | P | Catene di Markov: definizioni e proprieta' | Stati, transizioni, matrice di transizione |
| 7 | P | Catene di Markov e misure di rischio | Evoluzione delle distribuzioni, VaR, CVaR |
| 8 | C | Applicazioni Python al rischio di credito | Transizioni di rating e rischio di default |
| 9 | P | Variabili casuali binomiali e alberi binomiali | Modello binomiale, payoff, probabilita' risk-neutral |
| 10 | C | Applicazioni Python al pricing di opzioni e obbligazioni | Pricing numerico in alberi discreti |
| 11 | P | Programmazione lineare | Formulazione, vincoli, regione ammissibile |
| 12 | P | Dualita' nella programmazione lineare | Problema duale, prezzi ombra, interpretazione economica |
| 13 | C | Applicazioni Python di programmazione lineare: calcolo del CVaR | CVaR come problema di programmazione lineare |
| 14 | P | Programmazione lineare stocastica I | Decisioni here-and-now, scenari, recourse |
| 15 | P | Programmazione lineare stocastica II | Valore dell'informazione, soluzioni EV, WS e SP |
| 16 | C | Applicazioni Python di programmazione stocastica | Implementazione di modelli stocastici discreti |

Legenda:

- P = lezione prevalentemente teorica;
- C = lezione con forte componente computazionale o applicativa.

## 7. Vincoli linguistici e stilistici

Tutti i materiali destinati agli studenti devono essere scritti in italiano, con registro accademico, tecnico e preciso.

Lo stile deve rispettare i seguenti criteri:

1. linguaggio scientifico chiaro e non divulgativo;
2. definizioni formulate con precisione;
3. notazione matematica coerente e stabile;
4. spiegazioni finanziarie esplicite, ma non semplificate eccessivamente;
5. attenzione alla distinzione tra ipotesi, definizioni, risultati e interpretazioni;
6. uso di esempi numerici per consolidare i concetti;
7. uso di grafici come strumenti esplicativi, non decorativi;
8. neutralita' nella presentazione dei modelli e dei loro limiti.

Quando si scrive in LaTeX per il manuale o per le slides, usare per le vocali accentate italiane la notazione del tipo:

```latex
\`{a}, \`{e}, \`{i}, \`{o}, \`{u}
```

salvo diversa indicazione tecnica.

## 8. Vincoli LaTeX e compatibilita' Scientific Workplace 5.5

Il manuale e le slides devono essere scritti in LaTeX compatibile con Scientific Workplace 5.5.

Criteri operativi:

1. usare una sintassi LaTeX prudente e standard;
2. evitare pacchetti moderni non necessari o potenzialmente incompatibili;
3. preferire ambienti standard per teoremi, definizioni, esempi ed esercizi;
4. mantenere formule leggibili e non eccessivamente annidate;
5. usare una struttura modulare con file separati per capitoli e lezioni;
6. valutare con attenzione l'uso di TikZ o PGFPlots, che potrebbero non essere la soluzione piu' robusta in Scientific Workplace 5.5;
7. quando opportuno, generare i grafici con Python e includerli come immagini.

La struttura consigliata del manuale e':

```text
/manuale
  MQF_Manuale_Master.tex
  MQF_Capitolo_01.tex
  MQF_Capitolo_02.tex
  ...
  MQF_Capitolo_16.tex
```

La struttura consigliata delle slides e':

```text
/slides
  MQF_Slides_01.tex
  MQF_Slides_02.tex
  ...
  MQF_Slides_16.tex
```

La struttura consigliata dei file Python e':

```text
/python
  MQF_Python_01_Processi_Stocastici.py
  MQF_Python_02_Rischio_Credito.py
  MQF_Python_03_Pricing.py
  MQF_Python_04_CVaR_PL.py
  MQF_Python_05_Programmazione_Stocastica.py
```

La struttura consigliata dei documenti di coordinamento e':

```text
/progetto
  MQF_Project_Guidelines.md
  MQF_Master_Plan.tex
  MQF_Notazione.tex
  MQF_Registro_Esercizi.tex
  MQF_Registro_Grafici.tex
  MQF_Registro_Decisioni.tex
```

## Aggiornamento delle sezioni operative sulle lezioni applicative

Le sezioni seguenti aggiornano le linee guida relative ai capitoli applicativi, alle slides, agli esercizi in aula e alle applicazioni Python, in modo da renderle coerenti con la nuova impostazione generale delle lezioni applicative definita nel Master Plan.

---

## 9. Manuale del corso

Il manuale deve essere il riferimento scientifico principale. Ogni capitolo deve essere autosufficiente, ma collegato agli altri capitoli.

La struttura standard di un capitolo teorico e':

1. obiettivi della lezione;
2. motivazione finanziaria;
3. definizioni e notazione;
4. risultati teorici principali;
5. esempi numerici;
6. interpretazioni grafiche;
7. applicazioni finanziarie;
8. esercizi svolti;
9. esercizi proposti;
10. sintesi finale.

La struttura standard di un capitolo con applicazione Python deve essere concepita in modo coerente con la natura laboratoriale della lezione. Il capitolo applicativo non deve limitarsi a presentare codice commentato, ma deve documentare il passaggio dalla formulazione matematica al prodotto computazionale finale.

La struttura orientativa di un capitolo applicativo e':

1. obiettivi della lezione applicativa;
2. presentazione del caso finanziario o probabilistico;
3. richiamo matematico-operativo del modello;
4. descrizione dei dati, dei parametri e degli output attesi;
5. strumenti Python necessari per la lezione;
6. struttura del notebook o dello script;
7. sviluppo guidato del codice;
8. tappe di sviluppo autonomo;
9. controlli numerici e logici intermedi;
10. output numerici e grafici;
11. interpretazione economico-finanziaria dei risultati;
12. estensioni take-home;
13. sintesi finale.

Nei capitoli applicativi il codice deve essere presentato come parte integrante della modellizzazione. Ogni blocco computazionale rilevante deve essere preceduto da una motivazione e seguito da un commento interpretativo. Il capitolo deve rendere esplicito che cosa viene calcolato, perche' viene calcolato e come il risultato si collega al modello teorico.

Le dimostrazioni devono essere selettive. Devono essere incluse quando rafforzano la comprensione dei meccanismi quantitativi, ma non devono trasformare il corso in un corso astratto di probabilita' o ottimizzazione.

---

## 10. Slides delle lezioni

Le slides devono essere uno strumento di lezione, non una versione compressa del manuale.

Per ogni lezione teorica, la struttura orientativa e':

1. motivazione e obiettivi;
2. concetti teorici essenziali;
3. esempi numerici guidati;
4. grafici esplicativi;
5. esercizi da svolgere in aula;
6. sintesi conclusiva.

Per ogni lezione applicativa Python, la struttura delle slides deve essere coerente con lo svolgimento in laboratorio informatico. Le slides devono guidare l'alternanza tra spiegazione, sviluppo del codice, lavoro autonomo degli studenti e discussione collettiva.

La struttura orientativa delle slides applicative e':

1. apertura del caso applicativo;
2. obiettivi computazionali della lezione;
3. dati disponibili, parametri e output attesi;
4. richiamo matematico-operativo;
5. strumenti Python necessari;
6. schema del notebook o dello script;
7. avvio guidato dello sviluppo del codice;
8. tappe operative per lo sviluppo autonomo;
9. controlli intermedi e output attesi;
10. grafici e tabelle da produrre;
11. discussione dei risultati e degli errori ricorrenti;
12. estensione take-home.

Le slides applicative non devono contenere codice esteso in misura eccessiva. Devono invece mostrare i blocchi essenziali, la logica del flusso computazionale, le formule da implementare, i controlli da effettuare e l'interpretazione degli output. Il codice completo o semi-completo deve essere fornito nel notebook o nello script associato alla lezione.

Le slides devono inoltre distinguere chiaramente:

1. che cosa viene spiegato dal docente;
2. che cosa viene sviluppato in modo guidato;
3. che cosa viene completato autonomamente dagli studenti;
4. che cosa viene discusso collettivamente;
5. che cosa viene lasciato come lavoro take-home.

---

## 12. Esercizi in aula

Ogni lezione teorica deve includere almeno due esercizi in aula:

1. un esercizio di calcolo, derivazione o formulazione;
2. un esercizio di interpretazione finanziaria.

Quando utile, va aggiunto un esercizio grafico.

Nelle lezioni applicative Python gli esercizi in aula devono essere organizzati come tappe operative di laboratorio. Ogni tappa deve avere:

1. un obiettivo intermedio esplicito;
2. un blocco di codice da completare, modificare o interpretare;
3. un output atteso, numerico o grafico;
4. almeno un controllo numerico o logico;
5. una breve interpretazione economico-finanziaria.

Le tappe operative devono essere progettate in modo progressivo. Una possibile struttura e':

1. verifica dei dati e dei parametri;
2. implementazione di una formula o funzione centrale;
3. produzione di un primo output numerico;
4. costruzione di un grafico o di una tabella;
5. analisi di sensibilita' rispetto a un parametro;
6. interpretazione del risultato;
7. estensione o variante del caso base.

Gli esercizi applicativi non devono essere mini-progetti indipendenti durante la lezione. Devono invece essere parti controllate di un percorso comune, in cui gli studenti completano alcune componenti del software mantenendo visibile il collegamento con il modello teorico.

Quando si prevede l'uso di strumenti di intelligenza artificiale generativa, l'esercizio deve specificare in modo chiaro quali usi sono ammessi. L'IA puo' essere impiegata per chiarire errori di codice, spiegare messaggi di errore, proporre una funzione locale o migliorare la leggibilita' di un blocco. Non deve invece sostituire la formulazione del modello, la scelta delle ipotesi o l'interpretazione dei risultati.

---

## 14. Applicazioni Python e lezioni applicative

Sono previste cinque applicazioni Python, corrispondenti alle lezioni applicative del corso.

| Applicazione | Lezione | Tema                                             | Output computazionale                                   |
| -----------: | ------: | ------------------------------------------------ | ------------------------------------------------------- |
|            1 |       5 | Processi stocastici e valori attesi condizionati | Simulazioni, stime condizionate, grafici di traiettorie |
|            2 |       8 | Rischio di credito                               | Matrici di transizione, default probability, VaR, CVaR  |
|            3 |      10 | Pricing di opzioni e obbligazioni                | Alberi binomiali, backward induction, sensibilita'      |
|            4 |      13 | Programmazione lineare e CVaR                    | Formulazione PL, soluzione numerica, confronto VaR-CVaR |
|            5 |      16 | Programmazione stocastica                        | Scenari, recourse, EVPI, VSS                            |

Le applicazioni Python devono essere concepite come laboratori di modellizzazione quantitativa. La finalita' principale non e' insegnare Python in modo autonomo, ma mostrare come un modello probabilistico, finanziario o ottimizzativo possa essere tradotto in una procedura computazionale controllabile, interpretabile e modificabile.

Ciascuna lezione applicativa ha durata complessiva di 2 ore e 15 minuti, con 15 minuti di pausa. Il tempo effettivo di lavoro e' quindi pari a circa 120 minuti. La scansione temporale orientativa e':

1. 10--15 minuti per l'introduzione del caso;
2. 10--15 minuti per il richiamo matematico-operativo;
3. 15--20 minuti per gli strumenti Python necessari;
4. 25--30 minuti per lo sviluppo guidato del codice;
5. 15 minuti di pausa;
6. 35--40 minuti per lo sviluppo autonomo assistito;
7. 15--20 minuti per la discussione collettiva;
8. 5--10 minuti per la chiusura e l'assegnazione take-home.

Ogni applicazione deve essere costruita intorno a un caso identificabile. Il caso deve specificare:

1. il contesto finanziario o probabilistico;
2. la domanda quantitativa da affrontare;
3. i dati disponibili;
4. i parametri del modello;
5. le grandezze da calcolare;
6. gli output numerici e grafici attesi;
7. il prodotto computazionale finale.

Per ogni lezione applicativa devono essere predisposti almeno i seguenti materiali:

1. una traccia del caso;
2. un notebook o script Python semi-strutturato;
3. eventuali file dati;
4. una lista di parametri iniziali;
5. una sequenza di tappe operative;
6. controlli intermedi;
7. output numerici attesi;
8. grafici o tabelle da produrre;
9. indicazioni per la discussione in aula;
10. una o due estensioni take-home.

Il notebook o script deve evitare che gli studenti partano da un file vuoto. La struttura consigliata e':

1. intestazione della lezione e descrizione del caso;
2. importazione delle librerie;
3. definizione dei dati e dei parametri;
4. funzioni ausiliarie;
5. implementazione del modello base;
6. controlli intermedi;
7. output numerici;
8. grafici;
9. analisi di sensibilita';
10. blocchi da completare da parte degli studenti;
11. domande di interpretazione;
12. estensione take-home.

I blocchi destinati allo sviluppo autonomo devono essere chiaramente segnalati. Possono essere usate formule del tipo:

```python
# TODO 1: completare la funzione
# TODO 2: verificare il controllo numerico
# TODO 3: produrre il grafico richiesto
# TODO 4: interpretare il risultato
```

Criteri comuni per il codice Python:

1. codice ben commentato;
2. separazione tra dati, parametri, funzioni e output;
3. nomi delle variabili coerenti con la notazione matematica;
4. preferenza per codice leggibile rispetto a codice eccessivamente compatto;
5. controlli intermedi espliciti;
6. grafici leggibili e interpretabili;
7. interpretazione dei risultati dopo ogni blocco computazionale rilevante;
8. possibilita' di modificare parametri e scenari;
9. riproducibilita' dell'esecuzione;
10. tracciabilita' del passaggio dalla formula matematica all'algoritmo.

Gli strumenti Python introdotti in ciascuna lezione devono essere selezionati in funzione del modello. Non devono essere presentati come argomenti indipendenti di programmazione. A seconda della lezione, possono essere introdotti:

1. array, vettori e matrici;
2. funzioni;
3. cicli temporali;
4. simulazione Monte Carlo elementare;
5. strutture dati per stati e scenari;
6. grafici;
7. calcolo di quantili e medie condizionate;
8. uso di solver di ottimizzazione;
9. rappresentazione di alberi binomiali;
10. analisi di sensibilita'.

L'uso di strumenti di intelligenza artificiale generativa puo' essere previsto come supporto controllato. L'IA puo' essere utilizzata per:

1. spiegare messaggi di errore;
2. correggere errori sintattici o locali;
3. proporre una funzione Python coerente con una formula data;
4. commentare un blocco di codice;
5. migliorare la leggibilita' del codice;
6. confrontare due implementazioni alternative.

Non e' invece appropriato delegare all'IA:

1. la formulazione matematica del modello;
2. la scelta delle ipotesi;
3. la definizione delle variabili decisionali;
4. la selezione delle misure di rischio;
5. l'interpretazione economico-finanziaria dei risultati;
6. la verifica finale della correttezza.

Quando l'IA viene utilizzata dagli studenti, il docente puo' richiedere che siano esplicitati il prompt utilizzato, la risposta ricevuta e la verifica effettuata. L'obiettivo e' sviluppare un uso critico dello strumento, non sostituire la comprensione del modello.

Ogni lezione applicativa deve concludersi con un prodotto finale osservabile. Esempi di prodotto finale sono:

1. un simulatore di traiettorie;
2. una procedura di stima condizionata;
3. una matrice di transizione analizzata numericamente;
4. una distribuzione di perdita con VaR e CVaR;
5. un algoritmo di backward induction;
6. una formulazione di programmazione lineare;
7. una tabella di confronto tra soluzioni;
8. un grafico interpretativo;
9. una misura quantitativa del rischio;
10. un confronto tra soluzioni SP, EV e WS.

La lezione applicativa non deve concludersi genericamente con la scrittura di codice, ma con la comprensione di che cosa il codice permette di calcolare e di come tale calcolo modifichi o rafforzi l'interpretazione del modello teorico.

---

## 15. Stato di avanzamento da mantenere aggiornato

Il progetto deve mantenere un registro di avanzamento per aree. Tale registro deve essere aggiornato periodicamente e non deve restare fissato allo stato iniziale del progetto.

| Area                       | Stato da monitorare                             | Nota                                                              |
| -------------------------- | ----------------------------------------------- | ----------------------------------------------------------------- |
| Struttura delle 16 lezioni | Consolidata, salvo revisioni locali             | Derivata dal syllabus e uniformata nei titoli                     |
| Notazione generale         | Documento attivo                                | Da verificare durante lo sviluppo di ogni capitolo e applicazione |
| Manuale                    | In sviluppo progressivo                         | Da aggiornare capitolo per capitolo                               |
| Slides                     | In sviluppo progressivo                         | Da produrre e revisionare lezione per lezione                     |
| Esercizi teorici           | In sviluppo progressivo                         | Da collegare a manuale e slides                                   |
| Applicazioni Python        | Da strutturare secondo il formato laboratoriale | Cinque applicazioni previste                                      |
| Notebook/script Python     | Da predisporre per ogni applicazione            | Devono includere parti guidate e parti da completare              |
| Dati applicativi           | Da definire o simulare                          | Devono essere coerenti con i casi didattici                       |
| Grafici                    | Da produrre progressivamente                    | Devono essere coerenti con manuale, slides e codice               |
| Uso dell'IA generativa     | Da regolamentare nei materiali applicativi      | Solo come supporto controllato                                    |
| Compatibilita' SWP 5.5     | Da verificare                                   | Evitare pacchetti LaTeX moderni non necessari                     |

Ogni volta che una lezione viene sviluppata, occorre aggiornare il Master Plan o il registro decisionale con:

1. titolo definitivo;
2. obiettivi didattici;
3. notazione introdotta;
4. formule principali;
5. esercizi prodotti;
6. grafici previsti o prodotti;
7. collegamenti Python;
8. materiali applicativi collegati;
9. eventuali dataset;
10. eventuali notebook o script;
11. questioni aperte.

Per le lezioni applicative, l'aggiornamento deve inoltre indicare:

1. caso applicativo;
2. prodotto computazionale finale;
3. strumenti Python introdotti;
4. tappe operative in aula;
5. estensione take-home;
6. criteri per l'eventuale uso dell'IA generativa.

---

## 19. Questioni aperte

Le principali questioni ancora aperte sono:

1. definire il titolo definitivo del manuale;
2. consolidare il template LaTeX del manuale;
3. consolidare il template LaTeX delle slides;
4. decidere se le soluzioni complete degli esercizi saranno incluse nel manuale o in un fascicolo separato;
5. definire il livello di dettaglio delle dimostrazioni;
6. decidere le librerie Python ammesse nelle applicazioni computazionali;
7. stabilire una strategia definitiva per la produzione dei grafici;
8. decidere se il materiale debba includere criteri di valutazione o prove d'esame;
9. definire il formato standard dei notebook o script applicativi;
10. definire il formato dei dataset didattici;
11. stabilire se le applicazioni Python saranno distribuite come `.py`, notebook Jupyter o entrambi;
12. definire una convenzione per i blocchi di codice da completare in aula;
13. stabilire regole esplicite per l'uso dell'IA generativa da parte degli studenti;
14. predisporre prompt standard per debugging, spiegazione del codice e completamento locale di funzioni;
15. definire il formato delle estensioni take-home;
16. decidere se le consegne take-home saranno solo formative o anche valutabili;
17. stabilire una rubrica minima per valutare codice, controlli numerici e interpretazione finanziaria.


Le principali questioni ancora aperte sono:

1. definire il titolo definitivo del manuale;
2. consolidare il template LaTeX del manuale;
3. consolidare il template LaTeX delle slides;
4. decidere se le soluzioni complete degli esercizi saranno incluse nel manuale o in un fascicolo separato;
5. definire il livello di dettaglio delle dimostrazioni;
6. decidere le librerie Python ammesse nelle applicazioni computazionali;
7. stabilire una strategia definitiva per la produzione dei grafici;
8. decidere se il materiale debba includere criteri di valutazione o prove d'esame.

## 20. Principio guida finale

Il corso deve essere rigoroso nella notazione, selettivo nelle dimostrazioni, applicativo nell'interpretazione e coerente nella progressione didattica.

La qualita' del progetto dipendera' soprattutto dalla capacita' di mantenere un legame costante tra formalizzazione matematica, interpretazione finanziaria, esercizi, grafici e implementazioni computazionali.
