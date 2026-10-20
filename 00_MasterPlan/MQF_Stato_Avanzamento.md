# MQF - Stato di avanzamento

## Funzione del documento

Questo file è l'unica fonte per lo stato corrente del progetto. Registra ciò che è stato realizzato, ciò che è in lavorazione, le prossime priorità e le questioni operative aperte.

Il Master Plan definisce l'architettura didattica e i contenuti previsti.
Le Guidelines definiscono le regole operative stabili. La Notazione definisce
le convenzioni matematiche. Le decisioni progettuali stabili e le relative
motivazioni sono recepite nel documento normativo pertinente.

## Snapshot al 2026-10-20

|  |  |
|---|---|
| **Ultima attività completata** | Completata la passata conclusiva di coerenza sul pacchetto applicativo della Lezione 10, con verifica coordinata dei materiali Aula e TakeHome. Per il Caso Aula sono stati riallineati Scheda Costruzione, Scheda Caso e notebook su definizione del CVaR discreto, natura strutturale dei controlli su traiettoria sistemica e indipendenza condizionata, uso dei Common Random Numbers, controllo del seed 2027, stabilità Monte Carlo e verifica diretta di VaR/CVaR. Per il Caso TakeHome è stata eliminata dalla Scheda Costruzione una contaminazione da contenuti Aula, riallineando integralmente controlli, scomposizione in tappe, mappa prompt-notebook, struttura attesa del notebook e criteri di validazione ai parametri Lehman 2008: 40/39 debitori, investimento complessivo di 173 milioni, seed 2026, regimi $O,S,C$, LGD costante 0.65 e funzione di perdita $\varphi$ comprensiva del default. La rilettura integrale finale da GitHub della Scheda Costruzione TakeHome non ha evidenziato ulteriori incoerenze sostanziali. La verifica di coerenza del pacchetto Lezione 10 può quindi considerarsi conclusa, restando distinta dalla successiva validazione tecnica in ambiente pulito dei notebook. |
| **Materiale sviluppato** | Manuale: contenuto sostanziale per i Capitoli 1-16. Slides: contenuto sostanziale per le Lezioni 1-16. Pacchetti applicativi strutturati per le Lezioni 4, 7, 10, 13 e 16. Codice, notebook, script e asset grafici presenti lungo l'intero corso, inclusi i blocchi di programmazione lineare, ALM e programmazione stocastica. |
| **Lavoro in corso** | Prosegue la verifica conclusiva di coerenza orizzontale, verticale e incrociata nei blocchi del corso non ancora sottoposti a passata conclusiva. Il blocco Capitoli/Lezioni 1--4 ha completato la verifica sostanziale di coerenza; per la Lezione 4 è stata completata anche la passata conclusiva sul pacchetto applicativo TakeHome. Per la Lezione 10 è ora conclusa la verifica puntuale di coerenza del pacchetto applicativo Aula/TakeHome, inclusi Schede Caso, Schede Costruzione e notebook di riferimento. Restano da completare la validazione tecnica in ambiente pulito dei notebook applicativi delle Lezioni 7, 10, 13 e 16, la compilazione integrale dei sorgenti LaTeX, il controllo dei riferimenti incrociati e la verifica finale dei template e dei materiali operativi. |
| **Prossima priorità** | Completare le passate conclusive sui blocchi ancora aperti utilizzando il promemoria di raccordo come checklist, senza riaprire i blocchi già verificati salvo nuove evidenze; aggiornare progressivamente il promemoria eliminando i controlli già conclusi; eseguire la compilazione completa del manuale e dei 16 deck; proseguire la validazione tecnica dei notebook applicativi, completando la riesecuzione in ambiente pulito dei notebook delle Lezioni 7, 10, 13 e 16; completare il controllo di riferimenti incrociati, template IA, asset tecnici e scalette-promemoria. |

---

## Stato per lezione

Legenda: `sviluppato` = contenuto sostanziale presente; `parziale` = componente presente ma incompleta o non ancora validata in modo conclusivo; `traccia` = solo struttura iniziale; `-` = non iniziato; `n.a.` = non applicabile.

La classificazione `sviluppato` non equivale a `chiuso`: in questa fase gran parte del corso è sviluppata con taratura o verifica conclusiva residua.

Alla data del 2026-10-19 nessuna lezione viene riclassificata automaticamente come `chiusa`. La classificazione richiede il completamento dei controlli di coerenza, compilabilità e, per le lezioni applicative, esecuzione e riproducibilità dei notebook; gli audit automatici restano strumenti di ricognizione e non costituiscono da soli certificazione di chiusura.

| Lez. | Tipo | Titolo sintetico | Manuale | Slides | Esercizi/materiali operativi | Grafici | Python/Notebook |
|---:|:---:|---|:---:|:---:|:---:|:---:|:---:|
| 1 | P | Elementi di probabilità | sviluppato | sviluppato | sviluppato | sviluppato | n.a. |
| 2 | P | Variabili casuali | sviluppato | sviluppato | sviluppato | sviluppato | n.a. |
| 3 | P | Valori attesi condizionati | sviluppato | sviluppato | sviluppato | sviluppato | n.a. |
| 4 | C | Python: probabilità e condizionamento | sviluppato | sviluppato | sviluppato | sviluppato | sviluppato |
| 5 | P | Processi stocastici in tempo discreto | sviluppato | sviluppato | sviluppato | sviluppato | n.a. |
| 6 | P | Processi stocastici in tempo continuo | sviluppato | sviluppato | sviluppato | sviluppato | n.a. |
| 7 | C | Traiettorie, simulazione e pricing | sviluppato | sviluppato | sviluppato | sviluppato | sviluppato |
| 8 | P | Catene di Markov | sviluppato | sviluppato | sviluppato | sviluppato | n.a. |
| 9 | P | Markov e misure di rischio | sviluppato | sviluppato | sviluppato | sviluppato | n.a. |
| 10 | C | Python: rischio di credito | sviluppato | sviluppato | sviluppato | sviluppato | sviluppato |
| 11 | P | Programmazione lineare | sviluppato | sviluppato | sviluppato | sviluppato | n.a. |
| 12 | P | Dualità e ALM deterministico | sviluppato | sviluppato | sviluppato | sviluppato | n.a. |
| 13 | C | Python: programmazione lineare e ALM deterministico | sviluppato | sviluppato | sviluppato | sviluppato | sviluppato |
| 14 | P | Programmazione stocastica a due stadi | sviluppato | sviluppato | sviluppato | sviluppato | n.a. |
| 15 | P | Programmazione stocastica multistadio | sviluppato | sviluppato | sviluppato | sviluppato | n.a. |
| 16 | C | Python: programmazione stocastica | sviluppato | sviluppato | sviluppato | sviluppato | sviluppato |

---

## Promemoria per il controllo di raccordo

Questa sezione conserva una checklist operativa per il controllo orizzontale, verticale e incrociato dei materiali del corso. Non rappresenta lo stato ufficiale di avanzamento, sintetizzato nelle sezioni precedenti. Le note vengono aggiornate o eliminate quando il relativo controllo è stato completato.

| Area | Note |
|---|---|
| Probabilità, variabili casuali e condizionamento | Raccordo conclusivo verificato tra Capitoli/Lezioni 1--4 e documenti normativi pertinenti: coerenti spazio di probabilità ed eventi, variabili casuali e distribuzioni, valore atteso condizionato e informazione, proprietà della torre e trasferimento computazionale nella Lezione 4. È stato inoltre riallineato il richiamo alla disuguaglianza condizionata di Jensen nella Lezione 3, esplicitando nelle slides l'integrabilità di $\varphi(X)$ in coerenza con il Capitolo 3. Le incoerenze sostanziali individuate nella passata sono state corrette; la verifica integrale successiva non ha evidenziato ulteriori incoerenze plateali. |
| Processi stocastici discreti e filtrazioni | Raccordo verificato tra Capitolo/Lezione 5 e Capitoli 1-4: coerenti informazione, filtrazioni, adattabilità, prevedibilità delle decisioni, martingale e ruolo strutturale del modello binomiale. |
| Processi stocastici continui | Raccordo verificato tra Capitoli/Lezioni 6-7: coerenti moto browniano, diffusioni geometriche, OU, CIR, correlazione, Eulero--Maruyama, distinzione tra scenari del modello e repliche Monte Carlo e passaggio dalla teoria alla simulazione e al pricing. |
| Catene di Markov | Raccordo verificato tra Capitolo/Lezione 8, Capitolo/Lezione 9 e Lezione 10: coerenti dinamica markoviana, stato di default assorbente, passaggio dalle probabilità alle perdite e trasferimento alla simulazione di portafoglio. |
| Misure di rischio | Verificare il raccordo tra il blocco teorico delle misure di rischio e le applicazioni successive, evitando anticipazioni o sovrapposizioni non motivate. |
| Modello binomiale | Mantenuto come esempio strutturale di processo discreto, non come lezione autonoma di pricing; verificare che questa funzione resti coerente nei richiami successivi. |
| Programmazione lineare e dualità | Verificare la continuità tra Lezioni 11-12: formulazione primale, interpretazione economica dei vincoli e dualità devono preparare senza duplicazioni il passaggio all'ALM deterministico. |
| Asset--Liability Management deterministico | Verificare il raccordo tra Capitolo/Lezione 12 e l'implementazione Python della Lezione 13, con particolare attenzione a variabili, vincoli, unità di misura e interpretazione economica. |
| Programmazione stocastica | Verificare la progressione Lezioni 14-16: due stadi, EVPI/VSS, ricorso, multistadio, non anticipatività e implementazione Python devono restare distinti e progressivi. |
| Corrispondenza Python | Per la Lezione 4 è stata verificata la coerenza tra Scheda Caso, Scheda Costruzione, protocollo dei prompt, notebook, output e controlli, inclusa la riproducibilità mediante riesecuzione completa; la successiva passata sul pacchetto TakeHome ha inoltre riallineato in modo conclusivo output, tappe, prompt, struttura attesa del notebook e criteri di validazione. Per la Lezione 10 è ora conclusa la verifica puntuale di coerenza del pacchetto Aula/TakeHome: riallineati controlli, CVaR discreto, Common Random Numbers, seed, stabilità Monte Carlo, struttura delle tappe e corrispondenza tra Schede Caso, Schede Costruzione e notebook. Resta distinta e ancora da completare la validazione tecnica in ambiente pulito dei notebook della Lezione 10. La verifica conclusiva della corrispondenza Python resta invece aperta per le Lezioni applicative 7, 13 e 16, mantenendo distinta la funzione di regia delle slides dalla sequenza operativa di costruzione del notebook. |
| Rischio di credito e risk-neutral | Raccordo verificato tra Capitoli/Lezioni 8-10: coerenti distinzione tra misura fisica e misura risk-neutral, uso delle matrici di transizione, costruzione delle perdite, misure di rischio e simulazione Monte Carlo di portafoglio. |

---

## Verifica 2026-10-12 - Ricognizione generale del progetto

La ricognizione del repository mostra un passaggio di fase rispetto allo snapshot del 2026-09-15. Il progetto non è più caratterizzato dalla costruzione dei blocchi mancanti, ma dal controllo conclusivo di un impianto didattico ormai sostanzialmente completo.

### Evidenze verificate

- In `01_Manuale/Capitoli/` sono presenti i sedici capitoli previsti dal corso. I Capitoli 7, 10, 13, 15 e 16, che nel precedente registro risultavano assenti, in traccia o parziali, contengono ora sviluppo sostanziale coerente con la rispettiva funzione didattica.
- In `02_Slides/` sono presenti i sedici deck di lezione. In particolare risultano sviluppate anche le slides delle Lezioni 4, 7, 10, 13, 14, 15 e 16, mancanti nel precedente snapshot.
- Il Capitolo 6 contiene una sezione strutturata di esercizi svolti e una sezione di esercizi proposti con risultati per l'autovalutazione; il precedente stato `parziale` della componente `Esercizi/materiali operativi` non descrive più il materiale corrente ed è stato portato a `sviluppato`.
- La Lezione 7 dispone di capitolo, slides, Schede Caso Aula/TakeHome, schede di costruzione e più notebook di lavoro.
- La Lezione 10 dispone di capitolo sul rischio di credito, slides, Schede Caso Aula/TakeHome, schede di costruzione, notebook Aula/TakeHome e tracciati.
- La Lezione 13 dispone di capitolo sull'implementazione Python dell'ALM deterministico, slides, casi Aula/TakeHome, notebook, tracciati e valutazioni. Il capitolo rende esplicita la traduzione del modello in `scipy.optimize.linprog`.
- La Lezione 14 dispone ora anche delle slides; restano presenti gli script dedicati alla forma estesa e alla generazione delle figure.
- La Lezione 15 dispone di capitolo e slides sviluppati, di un insieme articolato di script su fattibilità del ricorso, SP/EV/WS, funzione di ricorso, alberi multistadio e non anticipatività, e degli asset grafici richiesti dai sorgenti nella cartella condivisa `graphics/`.
- La Lezione 16 dispone di capitolo e slides sviluppati, nonché del pacchetto applicativo con Caso Aula e TakeHome, notebook, tracciati e valutazioni.
- La Lezione 4, già sviluppata sul piano operativo, dispone ora anche di un deck autonomo e continua a costituire il riferimento metodologico per le lezioni applicative successive.
- Per le Lezioni applicative 4, 7, 10, 13 e 16 è stata verificata integralmente la presenza di figure nei rispettivi sorgenti LaTeX di capitolo e slides. Nei cinque capitoli non risultano comandi `\includegraphics`; nei cinque deck l'unica immagine stabilmente inclusa è il logo UniBS della copertina. I grafici prodotti in esecuzione dai notebook costituiscono output computazionali e non determinano quindi lo stato della colonna `Grafici` del registro. Per tutte e cinque le lezioni applicative la componente `Grafici` è classificata `sviluppato`.
- Per la Lezione 15 è stata verificata la presenza nella cartella condivisa `graphics/` di tutti gli asset richiamati dal Capitolo 15 e dalle relative slides; la componente `Grafici` è pertanto classificata `sviluppato`.
- `MQF_Project_Guidelines.md` è stato riallineato alla struttura corrente del corso e del repository: eliminati i residui della Goal Programming, corretti i nomi dei file delle Lezioni 12, 14 e 15, sostituiti i vecchi riferimenti a `/03_Python` e `/03_Codice` con `04_Codice`, aggiornata la struttura delle slides e corretta la disciplina degli asset grafici e degli output dei notebook.

### Variazioni principali rispetto al 2026-09-15

- Le slides passano da copertura parziale a copertura completa delle 16 lezioni.
- I Capitoli 7, 10, 13 e 16 passano da `traccia` a `sviluppato`.
- Il Capitolo 15 passa da `parziale` a `sviluppato`.
- La componente `Esercizi/materiali operativi` della Lezione 6 passa da `parziale` a `sviluppato`, sulla base della presenza corrente di esercizi svolti e proposti strutturati nel Capitolo 6.
- Le componenti Python/materiali operativi delle Lezioni 7, 10, 13 e 16 passano a `sviluppato`, sulla base della presenza di pacchetti strutturati e sostanziali.
- La componente `Grafici` delle Lezioni applicative 4, 7, 10, 13 e 16 è classificata `sviluppato`: capitoli e slides non prevedono figure didattiche esterne stabilmente incorporate, oltre al logo istituzionale delle copertine, mentre gli output grafici dei notebook sono parte della componente computazionale.
- La componente `Grafici` della Lezione 15 passa da `parziale` a `sviluppato`, sulla base della verifica degli asset effettivamente richiamati dai sorgenti e presenti nella cartella condivisa `graphics/`.
- Le Guidelines sono state riallineate all'architettura corrente del corso e alla struttura effettiva del repository.
- La fase progettuale dominante diventa la verifica conclusiva di coerenza, compilabilità, riproducibilità e qualità didattica.

### Verifiche tecniche ancora da completare

Lo script `tools/audit_stato_avanzamento.py` è stato eseguito con successo sulla copia locale del repository, utilizzando come data iniziale lo snapshot del 2026-10-12. Il report ha rilevato nuove evidenze per le Lezioni 1-6 e 10-16 e modifiche trasversali nei principali documenti normativi e nei template IA.

L'audit è uno strumento di ricognizione: segnala file modificati e materiali presenti, ma non assegna stati e non certifica da solo la qualità o la chiusura dei contenuti.

Restano da completare:

- la compilazione completa del manuale;
- la compilazione autonoma dei 16 deck;
- la riesecuzione integrale, in ambiente pulito, dei notebook delle Lezioni 7, 10, 13 e 16;
- la verifica della riproducibilità degli output, dei seed e delle dipendenze Python;
- una verifica visuale sistematica degli output grafici e degli eventuali problemi di impaginazione;
- il controllo conclusivo dei riferimenti incrociati e dei collegamenti tra documenti normativi, capitoli, slides e materiali applicativi.

L'output dell'audit contiene anche rumore tecnico che non deve essere interpretato come avanzamento didattico, tra cui file temporanei Word, directory `__pycache__`, file `synctex(busy)`, copie `_old` e cartelle storiche.

---

## Verifica 2026-10-16 - Audit dello stato di avanzamento

È stato eseguito `tools/audit_stato_avanzamento.py` sulla copia locale del repository. Lo script ha letto come riferimento lo snapshot del 2026-10-12 e ha prodotto una ricognizione delle modifiche Git, dei materiali presenti per le lezioni coinvolte e delle modifiche trasversali.

### Evidenze emerse dall'audit

- Nuove evidenze Git sono state rilevate per le Lezioni 1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15 e 16.
- Per le Lezioni 1-4 risultano modificati capitoli e/o slides; per la Lezione 4 è presente un pacchetto applicativo articolato con notebook, Schede Caso, schede di costruzione, tracciati e output.
- Per le Lezioni 5-6 risultano modifiche ai materiali teorici e sono presenti codice e asset grafici di supporto.
- Per la Lezione 10 risultano modifiche al capitolo e la presenza del pacchetto applicativo con notebook, Schede Caso, tracciati e valutazioni.
- Per le Lezioni 11-12 risultano modifiche a capitoli/slides e un insieme esteso di script e grafici di supporto alla programmazione lineare, dualità e ALM deterministico.
- Per la Lezione 13 risultano modifiche a capitolo e slides e la presenza del pacchetto applicativo strutturato.
- Per le Lezioni 14-16 risultano modifiche ai materiali teorici e applicativi, con script, grafici e pacchetti dedicati alla programmazione stocastica.
- Sono inoltre state rilevate modifiche trasversali a `MQF_Master_Plan.tex`, `MQF_Notazione.tex`, `MQF_Project_Guidelines.md`, `MQF_Stato_Avanzamento.md`, `MQF_Istruzioni_Studente_Uso_Virtuoso_IA_Casi_Applicativi.md` e ad alcuni template IA.

### Limiti dell'audit

L'audit non dimostra che ogni modifica sia corretta o conclusiva e non sostituisce il controllo qualitativo dei materiali. Inoltre, la ricognizione include file tecnici o storici che devono essere filtrati nella valutazione dello stato.

Il parser delle intestazioni LaTeX può troncare titoli contenenti comandi accentati con graffe; questa anomalia riguarda il report dello script e non costituisce evidenza di errore nei sorgenti LaTeX.

### Esito

L'audit conferma che il progetto è nella fase di verifica conclusiva di un impianto sostanzialmente completo. Le evidenze rilevate rafforzano la necessità di proseguire con il controllo di raccordo orizzontale, verticale e incrociato prima di attribuire eventuali stati di chiusura.

---

## Questioni operative aperte

- Completare il controllo integrato di coerenza tra Manuale, Slides, Master Plan, Notazione, Guidelines e Istruzioni Studente nei blocchi del corso per i quali la verifica conclusiva non è ancora stata chiusa.
- Usare il `Promemoria per il controllo di raccordo` come checklist per i controlli orizzontali, verticali e incrociati ancora aperti.
- Chiudere le incoerenze residue eventualmente individuate nei blocchi ancora in revisione prima di considerarne conclusa la verifica.
- Per le Lezioni 4 e 10 la verifica puntuale di coerenza tra architettura didattica, Scheda Caso, Scheda Costruzione, protocollo dei prompt, notebook, output e controlli è conclusa; completare la medesima verifica per le Lezioni applicative 7, 13 e 16, senza richiedere che la sequenza formale dei prompt sia riprodotta nelle slides.
- Eseguire una compilazione finale ordinaria del manuale e dei 16 deck per intercettare errori LaTeX, overfull, riferimenti irrisolti, figure mancanti, percorsi errati e incoerenze nei magic comment.
- Rieseguire i notebook delle Lezioni 7, 10, 13 e 16 in ambiente pulito, verificando assenza di errori, dipendenze, seed, riproducibilità degli output e funzionamento dei controlli.
- Riesaminare puntualmente i template IA rispetto alle Istruzioni Studente correnti, verificando coerenza dei Regimi A/B/C, del formato dei tracciati e dei materiali di valutazione.
- Verificare la copertura e l'allineamento delle scalette-promemoria previste dal Master Plan.


---

## Verifiche storiche sintetiche

- **2026-07-16/17** — sviluppate e verificate le Lezioni 8 e 6; per la Lezione 6 restavano allora tarature locali e il completamento dei materiali esercitativi. Il residuo esercitativo risulta successivamente chiuso nella versione corrente del Capitolo 6.
- **2026-08-23** — sviluppati Capitolo e slides della Lezione 9; sviluppato il blocco teorico delle Lezioni 11-12; verificati i primi materiali applicativi delle Lezioni 7 e 10; avviato il riallineamento dei template IA.
- **2026-09-15** — sviluppata la Lezione 14 sul modello stocastico a due stadi e avviato in forma avanzata il Capitolo 15.
- **2026-10-12** — ricognizione generale del repository: copertura sostanziale completa di manuale e slides; pacchetti applicativi strutturati per tutte le lezioni computazionali; passaggio alla fase di verifica conclusiva e chiusura. Verificata inoltre la componente grafica delle Lezioni applicative 4, 7, 10, 13 e 16, tutte classificate `sviluppato`; riallineate le Guidelines all'architettura corrente del corso e del repository; chiuso il residuo storico della Lezione 6 sugli esercizi/materiali operativi, ora classificati `sviluppato`.
- **2026-10-13** — verificata la componente grafica della Lezione 15: gli asset richiamati da Capitolo 15 e slides sono presenti nella cartella condivisa `graphics/`; la componente `Grafici` passa da `parziale` a `sviluppato`.
- **2026-10-16** — eseguito `tools/audit_stato_avanzamento.py` a partire dallo snapshot del 2026-10-12. Rilevate nuove evidenze per le Lezioni 1-6 e 10-16 e modifiche trasversali nei principali documenti normativi e nei template IA. Integrato nel registro un promemoria operativo per il controllo di raccordo orizzontale, verticale e incrociato. L'audit viene assunto come strumento di ricognizione e non come certificazione automatica di chiusura.
- **2026-10-18** — completata una nuova passata conclusiva sul blocco Capitoli/Lezioni 8-10 e sui documenti normativi. Verificati il raccordo tra catene di Markov, rischio di credito, misure di rischio e simulazione di portafoglio; chiusi residui terminologici nella distinzione tra scenari e repliche Monte Carlo; consolidata la distinzione tra misura fisica e misura risk-neutral. Le Guidelines sono state inoltre riallineate all'architettura effettiva delle lezioni applicative: la sequenza formale dei prompt resta normativa per notebook e tracciato IA ma non costituisce una sequenza obbligatoria delle slides; l'uso di `\subsection{...}` prima dei frame è facoltativo.
- **2026-10-19** — completata la passata conclusiva sul pacchetto TakeHome della Lezione 4. Riletti integralmente da GitHub la Scheda Caso e la Scheda Costruzione e verificati i raccordi con i documenti normativi pertinenti. Riallineati statistiche e grafici richiesti per $P_E$, $M$ e $S$, confronto tra distribuzioni condizionate dello shortfall, flusso logico-teorico, tappe input-output, prompt operativi, struttura attesa del notebook, criteri di validazione ed esito atteso. La verifica finale non ha evidenziato ulteriori incoerenze sostanziali. La Lezione 4 non rientra più tra i notebook applicativi ancora da rieseguire o validare tecnicamente; restano aperte le Lezioni 7, 10, 13 e 16.
- **2026-10-20** — completata la passata conclusiva di coerenza sul pacchetto applicativo della Lezione 10. Per il Caso Aula sono stati corretti e riallineati Scheda Costruzione, Scheda Caso e notebook su CVaR discreto, controlli strutturali della simulazione, Common Random Numbers, seed 2027, stabilità Monte Carlo e verifica diretta delle misure di coda. Per il Caso TakeHome è stata eliminata dalla Scheda Costruzione una contaminazione da contenuti Aula e sono state riscritte in modo coerente le sezioni sui controlli, sulla scomposizione in tappe, sulla mappa prompt-notebook, sulla struttura attesa del notebook e sui criteri di validazione. La rilettura integrale finale da GitHub ha confermato coerenza con il caso Lehman 2008: 40/39 debitori, 173 milioni di investimento complessivo, seed 2026, regimi $O,S,C$, LGD costante 0.65 e funzione di perdita $\varphi$ comprensiva del default. La verifica di coerenza del pacchetto Lezione 10 è conclusa; resta separatamente aperta la validazione tecnica dei notebook in ambiente pulito.
- **2026-10-20** — verificato il trattamento delle condizioni di integrabilità nei Capitoli e nelle Slides delle Lezioni 1-4. Riallineata la Lezione 3 al Capitolo 3 sulla disuguaglianza condizionata di Jensen, esplicitando nelle slides che $\varphi(X)$ deve essere integrabile; confermata invece come già corretta la formulazione della migliore previsione in $L^2$, senza necessità di ulteriori modifiche.
