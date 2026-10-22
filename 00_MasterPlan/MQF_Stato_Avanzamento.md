# MQF - Stato di avanzamento

## Funzione del documento

Questo file è l'unica fonte per lo stato corrente del progetto. Registra ciò che è stato realizzato, ciò che è in lavorazione, le prossime priorità e le questioni operative aperte.

Il Master Plan definisce l'architettura didattica e i contenuti previsti.
Le Guidelines definiscono le regole operative stabili. La Notazione definisce
le convenzioni matematiche. Le decisioni progettuali stabili e le relative
motivazioni sono recepite nel documento normativo pertinente.

## Snapshot al 2026-10-22

|  |  |
|---|---|
| **Ultima attività completata** | Ricostruiti, rieseguiti integralmente e validati i notebook docente del Caso Aula e del Caso TakeHome della Lezione 13, `Lezione_13_Notebook_Docente_Aula.ipynb` e `Lezione_13_Notebook_Docente_TakeHome.ipynb`, sulla base delle rispettive Schede Costruzione Caso aggiornate, delle Schede Caso e dei documenti normativi relativi alla produzione dei notebook e all'uso controllato dell'IA. Entrambe le Schede Costruzione adottano un Flusso logico-teorico in 8 passi e una scomposizione in 6 tappe input-output. Nei notebook Prompt zero resta nel protocollo e non genera una cella autonoma; Prompt 1, Prompt 2 e Prompt 3 producono le tre celle Markdown iniziali; le sei tappe operative sono organizzate come coppie Markdown → Python, seguite dalla cella Markdown destinata all'interpretazione autonoma dello studente. Entrambi i notebook presentano 16 celle, 10 Markdown e 6 Python, e sono stati eseguiti integralmente senza errori. Il Caso Aula SVB produce le 10 tabelle e le 14 figure richieste, verifica il benchmark, i valori marginali, le sensitività a $\theta$, $\phi$ e $\psi$, la doppia azione di $\psi$, la frontiera di fattibilità rispetto a $\theta$ e i tre scenari congiunti. Il Caso TakeHome First Republic produce le 6 tabelle e le 6 figure richieste, tratta separatamente $\alpha$ e $\beta$, analizza $\phi$, verifica esplicitamente il vincolo legacy e la relazione $\partial\Pi^*/\partial L=m$, e sviluppa la scenario analysis assegnata. I controlli conclusivi e le verifiche di riproducibilità risultano superati in entrambi i notebook. |
| **Materiale sviluppato** | Manuale: contenuto sostanziale per i Capitoli 1-16. Slides: contenuto sostanziale per le Lezioni 1-16. Pacchetti applicativi strutturati per le Lezioni 4, 7, 10, 13 e 16. Codice, notebook, script e asset grafici presenti lungo l'intero corso, inclusi i blocchi di programmazione lineare, ALM e programmazione stocastica. |
| **Lavoro in corso** | Prosegue la verifica conclusiva di coerenza orizzontale, verticale e incrociata nei blocchi del corso non ancora sottoposti a passata conclusiva. Il blocco Capitoli/Lezioni 1--4 ha completato la verifica sostanziale di coerenza; per la Lezione 4 risultano completati anche il riallineamento del pacchetto applicativo TakeHome, la produzione del notebook docente coerente con il protocollo dei prompt e la relativa esecuzione tecnica. Per le Lezioni 7, 10 e 13 sono concluse sia la verifica di coerenza dei notebook docente Aula/TakeHome con le rispettive Schede Caso e Schede Costruzione sia l'esecuzione tecnica con controllo degli output. Nel blocco 11--13 risultano quindi verificati il raccordo programmazione lineare--dualità--ALM, il raccordo teorico-computazionale tra ALM deterministico e Lezione 13, la coerenza conclusiva tra Capitolo 13, slides, Schede Costruzione e Schede Caso e la validazione dei notebook docente Aula/TakeHome. Nel blocco 14--16 il raccordo didattico è verificato; resta da recepire nel Master Plan la relativa precisazione redazionale. Restano inoltre da completare la verifica applicativa e la validazione tecnica dei notebook della Lezione 16, la compilazione integrale dei sorgenti LaTeX, il controllo dei riferimenti incrociati e la verifica finale dei template e dei materiali operativi. |
| **Prossima priorità** | Completare le passate conclusive sui blocchi ancora aperti utilizzando il promemoria di raccordo come checklist, senza riaprire i blocchi già verificati salvo nuove evidenze; recepire nel Master Plan la precisazione sulla funzione two-stage della Lezione 16 e sostituire nel Caso TakeHome l'espressione `adattamento progressivo` con una formulazione coerente con il ricorso scenario-specifico; completare per la Lezione 16 il controllo coordinato del pacchetto applicativo e la validazione tecnica dei notebook; eseguire la compilazione completa del manuale e dei 16 deck; completare il controllo di riferimenti incrociati, template IA, asset tecnici e scalette-promemoria. |

---

## Stato per lezione

Legenda: `sviluppato` = contenuto sostanziale presente; `parziale` = componente presente ma incompleta o non ancora validata in modo conclusivo; `traccia` = solo struttura iniziale; `-` = non iniziato; `n.a.` = non applicabile.

La classificazione `sviluppato` non equivale a `chiuso`: in questa fase gran parte del corso è sviluppata con taratura o verifica conclusiva residua.

Alla data del 2026-10-22 nessuna lezione viene riclassificata automaticamente come `chiusa`. La classificazione richiede il completamento dei controlli di coerenza, compilabilità e, per le lezioni applicative, esecuzione e riproducibilità dei notebook; gli audit automatici restano strumenti di ricognizione e non costituiscono da soli certificazione di chiusura.

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
| Misure di rischio | Raccordo verificato nel blocco 8--10. La Lezione 9 distingue Expected Loss, dispersione complessiva, unexpected loss, VaR, CVaR e capitale economico; il passaggio dalla distribuzione markoviana degli stati alla distribuzione monetaria delle perdite esplicita l'aggregazione delle probabilità per perdite coincidenti e il collegamento alle Expected Credit Loss. Il trasferimento alla Lezione 10 resta coerente con la simulazione di portafoglio e le misure di coda già verificate. |
| Modello binomiale | Mantenuto come esempio strutturale di processo discreto, non come lezione autonoma di pricing; verificare che questa funzione resti coerente nei richiami successivi. |
| Programmazione lineare e dualità | Raccordo verificato tra Lezioni 11--12. Il Capitolo 11 introduce formulazione primale, vincoli attivi, sensitività, problema duale, prezzi impliciti e complementarità; il Capitolo 12 riprende esplicitamente soluzione, requisito di liquidità e valore duale del caso guida e usa tali strumenti come punto di partenza per passare dal vincolo aggregato ai bilanci intertemporali. La dualità non viene duplicata come tema autonomo, ma utilizzata per interpretare il valore marginale della liquidità e dei vincoli temporali nell'ALM deterministico. |
| Asset--Liability Management deterministico | Raccordo verificato tra Capitolo/Lezione 12 e Lezione 13. Il Capitolo 13 rende operativo, senza introdurre una nuova classe di modelli, l'ALM deterministico formulato nel Capitolo 12; mantiene le variabili di allocazione $x$, le giacenze $g$, il funding $u$, i bilanci temporali e la relativa interpretazione economica, traducendoli in vettore decisionale, funzione obiettivo, uguaglianze, disuguaglianze e bound per `scipy.optimize.linprog`. Le slides della Lezione 13 esplicitano la sequenza Lezione 11 $\rightarrow$ Lezione 12 $\rightarrow$ Lezione 13 e il passaggio da programmazione lineare ad ALM deterministico e quindi a implementazione e analisi computazionale. È stata completata la passata conclusiva di coerenza tra Capitolo 13, slides, Schede Costruzione Caso Aula/TakeHome e Schede Caso Aula/TakeHome: driver, struttura dei modelli, output, controlli, scenari, frontiera di fattibilità e vincolo legacy risultano allineati e non restano incoerenze sostanziali note nel pacchetto documentale. Sono stati inoltre ricostruiti e validati i notebook docente Aula e TakeHome secondo la nuova architettura di 8 passi e 6 tappe, con esecuzione integrale, verifica degli output, dei marginali, delle sensitività e degli scenari. La verifica applicativa della Lezione 13 è quindi conclusa. |
| Programmazione stocastica | Raccordo didattico verificato tra Lezioni 14--16. La Lezione 14 introduce il modello a due stadi, distinguendo decisione ex ante, scenari e ricorso; la Lezione 15 sviluppa fattibilità del ricorso, SP/EV/WS, VSS/EVPI e amplia il quadro al multistadio, all'informazione progressiva e ai vincoli di non anticipatività tra nodi con storia comune. La Lezione 16 non costituisce l'implementazione completa del multistadio: consolida deliberatamente sul piano computazionale il framework two-stage mediante una decisione iniziale unica $x$ comune agli scenari e ricorso scenario-specifico $y_s$. Questa scelta risulta coerente con Master Plan, Guidelines, Capitolo 16, slides e Schede Caso Aula/TakeHome. Nel two-stage la non anticipatività della decisione iniziale è incorporata strutturalmente dall'unicità di $x$. Resta soltanto un micro-riallineamento redazionale del Master Plan: esplicitare tale funzione della Lezione 16 e sostituire nel Caso TakeHome l'espressione `adattamento progressivo`, che può suggerire impropriamente un modello multistadio. |
| Corrispondenza Python | Per la Lezione 4 è stata verificata la coerenza tra Scheda Caso, Scheda Costruzione, protocollo dei prompt, notebook, output e controlli, inclusa la riproducibilità mediante riesecuzione completa. Il notebook docente TakeHome è stato ricostruito in modo esplicitamente conforme alla sequenza Prompt zero → Prompt 1 → Prompt 2 → Prompt 3 → prompt di tappa: Prompt zero resta nel tracciato IA; Prompt 1--3 generano le tre celle Markdown iniziali; le Tappe 1--5 sono organizzate come coppie Markdown → Python e la Tappa 6 contiene interpretazione critica e limiti. Il notebook è stato eseguito integralmente con esito positivo. Per la Lezione 7 i notebook docente Aula e TakeHome sono stati ricostruiti e validati direttamente sulle Schede Costruzione e Schede Caso correnti e sui documenti normativi: Prompt zero resta nel protocollo senza generare una cella quantitativa autonoma; Prompt 1, Prompt 2 e Prompt 3 producono le celle Markdown iniziali; le sei tappe sono sviluppate come moduli Markdown → Python. I Flussi logico-teorici mantengono integralmente la scansione delle Schede Costruzione, con 11 passi per l'Aula e 12 per il TakeHome, e le sei tappe input-output restano quelle canoniche. Entrambi i notebook sono stati rieseguiti integralmente con esito positivo, inclusi output, controlli, convenzione CIR, diagnostica Monte Carlo, controllo della discretizzazione e riproducibilità. Per la Lezione 10 i notebook docente Aula e TakeHome sono stati ricostruiti direttamente dalle Schede Costruzione Caso e dalle Schede Caso correnti, tenendo conto delle Guidelines e dei template canonici dei prompt. Entrambi seguono sei passi del Flusso logico-teorico e sei tappe input-output; hanno 22 celle ciascuno, 11 Markdown e 11 Python, in alternanza rigorosa. Sono stati rieseguiti integralmente senza errori. Il Caso Aula preserva la specifica Evergrande con tempo di primo default, LGD dipendente dal regime che governa la transizione verso il default e confronto mediante Common Random Numbers; il Caso TakeHome preserva la specifica Lehman con LGD costante e funzione di perdita migration-based sul rating finale, mantenendo identiche le traiettorie dei 39 debitori comuni. Per entrambi risultano verificati gli output numerici, le quattro tabelle, le tre figure, i controlli previsti, i seed assegnati, la stabilità empirica Monte Carlo e il calcolo di VaR/CVaR sulle perdite monetarie secondo la definizione quantile-based adottata nel Capitolo 9; i risultati sono stati inoltre confrontati con i benchmark indicativi delle rispettive Schede Costruzione. Per la Lezione 13 i notebook docente Aula e TakeHome sono stati ricostruiti sulle Schede Costruzione e Schede Caso aggiornate: entrambi adottano un Flusso in 8 passi e 6 tappe, Prompt zero non genera una cella autonoma, Prompt 1--3 costituiscono le tre celle Markdown iniziali e le sei tappe operative sono articolate in coppie Markdown → Python, con una cella Markdown finale destinata all'interpretazione autonoma. Entrambi contano 16 celle, 10 Markdown e 6 Python, e sono stati rieseguiti integralmente senza errori. Nel Caso Aula risultano verificati benchmark, 10 tabelle, 14 figure, marginali, sensitività a $\theta$, $\phi$, $\psi$, frontiera di fattibilità e scenari; nel TakeHome risultano verificati benchmark, 6 tabelle, 6 figure, sensitività ad $\alpha$, $\beta$, $\phi$, confronto delle due ondate, vincolo legacy e relazione $\partial\Pi^*/\partial L=m$, oltre agli scenari. Le Lezioni 4, 7, 10 e 13 non rientrano più tra quelle per cui resta aperta la verifica di corrispondenza Python o la validazione tecnica dei notebook. La verifica conclusiva della corrispondenza Python resta quindi aperta per la sola Lezione 16, mantenendo distinta la funzione di regia delle slides dalla sequenza operativa di costruzione del notebook. |
| Rischio di credito e risk-neutral | Raccordo verificato tra Capitoli/Lezioni 8-10: coerenti distinzione tra misura fisica e misura risk-neutral, uso delle matrici di transizione, costruzione delle perdite, misure di rischio e simulazione Monte Carlo di portafoglio. |

---

## Verifica 2026-10-12 - Ricognizione generale del progetto

La ricognizione del repository mostra un passaggio di fase rispetto allo snapshot del 2026-09-15. Il progetto non è più caratterizzato dalla costruzione dei blocchi mancanti, ma dal controllo conclusivo di un impianto didattico ormai sostanzialmente completo.

### Evidenze verificate

- In `01_Manuale/Capitoli/` sono presenti i sedici capitoli previsti dal corso. I Capitoli 7, 10, 13, 15 e 16, che nel precedente registro risultavano assenti, in traccia o parziali, contengono ora sviluppo sostanziale coerente con la rispettiva funzione didattica.
- In `02_Slides/` sono presenti i sedici deck di lezione. In particolare risultano sviluppate anche le slides delle Lezioni 4, 7, 10, 13, 14, 15 e 16, mancanti nel precedente snapshot.
- Il Capitolo 6 contiene una sezione strutturata di esercizi svolti e una sezione di esercizi proposti con risultati per l'autovalutazione; il precedente stato `parziale` della componente `Esercizi/materiali operativi` non descrive più il materiale corrente ed è stato portato a `sviluppato`.
- La Lezione 7 dispone di capitolo, slides, Schede Caso Aula/TakeHome, schede di costruzione e più notebook di lavoro.
- La Lezione 10 dispone di capitolo sul rischio di credito, slides, Schede Caso Aula/TakeHome, schede di costruzione, notebook docente Aula/TakeHome e tracciati.
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
- la riesecuzione integrale, in ambiente pulito, dei notebook della Lezione 16;
- la verifica della riproducibilità degli output, dei seed e delle dipendenze Python per i notebook ancora aperti;
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
- Per la Lezione 10 risultano modifiche al capitolo e la presenza del pacchetto applicativo con notebook docente Aula/TakeHome, Schede Caso, tracciati e valutazioni.
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
- Per le Lezioni 4, 7, 10 e 13 la verifica di coerenza dei notebook rispetto alle rispettive specifiche applicative e la validazione tecnica dei notebook docente risultano concluse. Per la Lezione 16 restano aperti il controllo coordinato del pacchetto applicativo e la validazione tecnica dei notebook, senza richiedere che la sequenza formale dei prompt sia riprodotta nelle slides.
- Recepire nel Master Plan la precisazione architetturale relativa alla Lezione 16: il laboratorio applicativo consolida deliberatamente il framework two-stage; l'estensione multistadio e i vincoli di non anticipatività tra nodi intermedi restano contenuti teorici della Lezione 15. Nella stessa scheda sostituire l'espressione `adattamento progressivo` riferita al Caso TakeHome con una formulazione coerente con il ricorso scenario-specifico.
- Eseguire una compilazione finale ordinaria del manuale e dei 16 deck per intercettare errori LaTeX, overfull, riferimenti irrisolti, figure mancanti, percorsi errati e incoerenze nei magic comment.
- Rieseguire i notebook della Lezione 16 in ambiente pulito, verificando assenza di errori, dipendenze, seed, riproducibilità degli output e funzionamento dei controlli.
- Riesaminare puntualmente i template IA rispetto alle Istruzioni Studente correnti, verificando coerenza dei Regimi A/B/C, del formato dei tracciati e dei materiali di valutazione.
- Verificare la copertura e l'allineamento delle scalette-promemoria previste dal Master Plan.