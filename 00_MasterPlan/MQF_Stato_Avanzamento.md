# MQF - Stato di avanzamento

## Funzione del documento

Questo file è l'unica fonte per lo stato corrente del progetto. Registra ciò che è stato realizzato, ciò che è in lavorazione, le prossime priorità e le questioni operative aperte.

Il Master Plan definisce l'architettura didattica e i contenuti previsti. Le Guidelines definiscono le regole stabili. Il Registro decisionale conserva le decisioni progettuali e le relative motivazioni.

## Snapshot al 2026-10-12

|  |  |
|---|---|
| **Ultima attività completata** | Estensione del progetto alla copertura sostanziale completa delle 16 lezioni: sono presenti i 16 capitoli del manuale e i 16 deck di slides. Le lezioni applicative 7, 10, 13 e 16 dispongono ora di capitolo, slides, Schede Caso Aula/TakeHome, schede di costruzione e notebook; per la Lezione 10 sono presenti anche i tracciati, mentre per le Lezioni 13 e 16 sono presenti tracciati e materiali di valutazione. |
| **Materiale sviluppato** | Manuale: contenuto sostanziale per i Capitoli 1-16. Slides: contenuto sostanziale per le Lezioni 1-16. Pacchetti applicativi strutturati per le Lezioni 4, 7, 10, 13 e 16. Codice e script di supporto presenti lungo l'intero corso, inclusi i blocchi sulla programmazione stocastica delle Lezioni 14-15. |
| **Lavoro in corso** | Verifica conclusiva di coerenza tra capitoli, slides, Master Plan, Notazione e materiali applicativi; taratura tipografica e controllo delle figure; verifica finale dei notebook e dei tracciati IA; verifica dei template IA; chiusura dei residui gi\`a noti della Lezione 6. |
| **Prossima priorit\`a** | Eseguire il controllo finale integrato del corso: compilazione completa del manuale e dei 16 deck, esecuzione/validazione dei notebook delle lezioni applicative, verifica puntuale degli asset grafici, dei riferimenti incrociati e delle scalette-promemoria previste dal Master Plan. |

---

## Stato per lezione

Legenda: `sviluppato` = contenuto sostanziale presente; `parziale` = componente presente ma incompleta o non ancora validata in modo conclusivo; `traccia` = solo struttura iniziale; `-` = non iniziato; `n.a.` = non applicabile.

La classificazione `sviluppato` non equivale a `chiuso`: in questa fase gran parte del corso \`e sviluppata con taratura o verifica conclusiva residua.

| Lez. | Tipo | Titolo sintetico | Manuale | Slides | Esercizi/materiali operativi | Grafici | Python/Notebook |
|---:|:---:|---|:---:|:---:|:---:|:---:|:---:|
| 1 | P | Elementi di probabilit\`a | sviluppato | sviluppato | sviluppato | sviluppato | n.a. |
| 2 | P | Variabili casuali | sviluppato | sviluppato | sviluppato | sviluppato | n.a. |
| 3 | P | Valori attesi condizionati | sviluppato | sviluppato | sviluppato | sviluppato | n.a. |
| 4 | C | Python: probabilit\`a e condizionamento | sviluppato | sviluppato | sviluppato | sviluppato | sviluppato |
| 5 | P | Processi stocastici in tempo discreto | sviluppato | sviluppato | sviluppato | sviluppato | n.a. |
| 6 | P | Processi stocastici in tempo continuo | sviluppato | sviluppato | parziale | sviluppato | n.a. |
| 7 | C | Traiettorie, simulazione e pricing | sviluppato | sviluppato | sviluppato | sviluppato | sviluppato |
| 8 | P | Catene di Markov | sviluppato | sviluppato | sviluppato | sviluppato | n.a. |
| 9 | P | Markov e misure di rischio | sviluppato | sviluppato | sviluppato | sviluppato | n.a. |
| 10 | C | Python: rischio di credito | sviluppato | sviluppato | sviluppato | sviluppato | sviluppato |
| 11 | P | Programmazione lineare | sviluppato | sviluppato | sviluppato | sviluppato | n.a. |
| 12 | P | Dualit\`a e ALM deterministico | sviluppato | sviluppato | sviluppato | sviluppato | n.a. |
| 13 | C | Python: programmazione lineare e ALM deterministico | sviluppato | sviluppato | sviluppato | sviluppato | sviluppato |
| 14 | P | Programmazione stocastica a due stadi | sviluppato | sviluppato | sviluppato | sviluppato | n.a. |
| 15 | P | Programmazione stocastica multistadio | sviluppato | sviluppato | sviluppato | parziale | n.a. |
| 16 | C | Python: programmazione stocastica | sviluppato | sviluppato | sviluppato | sviluppato | sviluppato |

---

## Verifica 2026-10-12 - Ricognizione generale del progetto

La ricognizione del repository mostra un passaggio di fase rispetto allo snapshot del 2026-09-15. Il progetto non \`e pi\`u caratterizzato dalla costruzione dei blocchi mancanti, ma dal controllo conclusivo di un impianto didattico ormai sostanzialmente completo.

### Evidenze verificate

- In `01_Manuale/Capitoli/` sono presenti i sedici capitoli previsti dal corso. I Capitoli 7, 10, 13, 15 e 16, che nel precedente registro risultavano assenti, in traccia o parziali, contengono ora sviluppo sostanziale coerente con la rispettiva funzione didattica.
- In `02_Slides/` sono presenti i sedici deck di lezione. In particolare risultano sviluppate anche le slides delle Lezioni 4, 7, 10, 13, 14, 15 e 16, mancanti nel precedente snapshot.
- La Lezione 7 dispone di capitolo, slides, Schede Caso Aula/TakeHome, schede di costruzione e pi\`u notebook di lavoro.
- La Lezione 10 dispone di capitolo sul rischio di credito, slides, Schede Caso Aula/TakeHome, schede di costruzione, notebook Aula/TakeHome e tracciati.
- La Lezione 13 dispone di capitolo sull'implementazione Python dell'ALM deterministico, slides, casi Aula/TakeHome, notebook, tracciati e valutazioni. Il capitolo rende esplicita la traduzione del modello in `scipy.optimize.linprog`.
- La Lezione 14 dispone ora anche delle slides; restano presenti gli script dedicati alla forma estesa e alla generazione delle figure.
- La Lezione 15 dispone di capitolo e slides sviluppati e di un insieme articolato di script su fattibilit\`a del ricorso, SP/EV/WS, funzione di ricorso, alberi multistadio e non anticipativit\`a.
- La Lezione 16 dispone di capitolo e slides sviluppati, nonch\'e del pacchetto applicativo con Caso Aula e TakeHome, notebook, tracciati e valutazioni.
- La Lezione 4, gi\`a sviluppata sul piano operativo, dispone ora anche di un deck autonomo e continua a costituire il riferimento metodologico per le lezioni applicative successive.
- Per le Lezioni applicative 4, 7, 10, 13 e 16 \`e stata verificata integralmente la presenza di figure nei rispettivi sorgenti LaTeX di capitolo e slides. Nei cinque capitoli non risultano comandi `\includegraphics`; nei cinque deck l'unica immagine stabilmente inclusa \`e il logo UniBS della copertina. I grafici prodotti in esecuzione dai notebook costituiscono output computazionali e non determinano quindi lo stato della colonna `Grafici` del registro. Per tutte e cinque le lezioni applicative la componente `Grafici` \`e classificata `sviluppato`.
- `MQF_Project_Guidelines.md` \`e stato riallineato alla struttura corrente del corso e del repository: eliminati i residui della Goal Programming, corretti i nomi dei file delle Lezioni 12, 14 e 15, sostituiti i vecchi riferimenti a `/03_Python` e `/03_Codice` con `04_Codice`, aggiornata la struttura delle slides e corretta la disciplina degli asset grafici e degli output dei notebook.

### Variazioni principali rispetto al 2026-09-15

- Le slides passano da copertura parziale a copertura completa delle 16 lezioni.
- I Capitoli 7, 10, 13 e 16 passano da `traccia` a `sviluppato`.
- Il Capitolo 15 passa da `parziale` a `sviluppato`.
- Le componenti Python/materiali operativi delle Lezioni 7, 10, 13 e 16 passano a `sviluppato`, sulla base della presenza di pacchetti strutturati e sostanziali.
- La componente `Grafici` delle Lezioni applicative 4, 7, 10, 13 e 16 \`e classificata `sviluppato`: capitoli e slides non prevedono figure didattiche esterne stabilmente incorporate, oltre al logo istituzionale delle copertine, mentre gli output grafici dei notebook sono parte della componente computazionale.
- Le Guidelines sono state riallineate all'architettura corrente del corso e alla struttura effettiva del repository.
- La fase progettuale dominante diventa la verifica conclusiva di coerenza, compilabilit\`a, riproducibilit\`a e qualit\`a didattica.

### Verifiche non svolte in questa sessione

Questa ricognizione \`e stata effettuata sul contenuto corrente del repository GitHub.

Non sono stati eseguiti in questa sessione:

- lo script locale `tools/audit_stato_avanzamento.py`;
- una compilazione completa del manuale;
- la compilazione autonoma di tutti i 16 deck;
- la riesecuzione integrale dei notebook;
- una verifica visuale sistematica di tutti gli output grafici.

Di conseguenza, `sviluppato` indica presenza di contenuto sostanziale e non certificazione conclusiva della compilazione o dell'esecuzione.

---

## Questioni operative aperte

- Chiudere il residuo della Lezione 6 sugli esercizi/materiali, gi\`a classificato `parziale` nelle verifiche precedenti.
- Eseguire una compilazione finale ordinaria del manuale e dei deck per intercettare overfull, riferimenti irrisolti, figure mancanti e incoerenze tra nomi file e magic comment.
- Rieseguire i notebook delle Lezioni 4, 7, 10, 13 e 16 in ambiente pulito, verificando assenza di errori, riproducibilit\`a degli output, seed, controlli e dipendenze.
- Verificare le figure e gli asset della Lezione 15; la componente grafica resta `parziale` fino a controllo conclusivo.
- Riesaminare puntualmente i template IA rispetto alle Istruzioni Studente correnti, verificando coerenza dei regimi A/B/C, del formato dei tracciati e dei materiali di valutazione.
- Verificare la copertura e l'allineamento delle scalette-promemoria delle lezioni teoriche previste dal Master Plan.

---

## Verifiche storiche sintetiche

- **2026-07-16/17** — sviluppate e verificate le Lezioni 8 e 6; per la Lezione 6 restano tarature locali e il completamento dei materiali esercitativi.
- **2026-08-23** — sviluppati Capitolo e slides della Lezione 9; sviluppato il blocco teorico delle Lezioni 11-12; verificati i primi materiali applicativi delle Lezioni 7 e 10; avviato il riallineamento dei template IA.
- **2026-09-15** — sviluppata la Lezione 14 sul modello stocastico a due stadi e avviato in forma avanzata il Capitolo 15.
- **2026-10-12** — ricognizione generale del repository: copertura sostanziale completa di manuale e slides; pacchetti applicativi strutturati per tutte le lezioni computazionali; passaggio alla fase di verifica conclusiva e chiusura. Verificata inoltre la componente grafica delle Lezioni applicative 4, 7, 10, 13 e 16, tutte classificate `sviluppato`; riallineate le Guidelines all'architettura corrente del corso e del repository.
