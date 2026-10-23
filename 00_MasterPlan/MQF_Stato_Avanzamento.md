# MQF - Stato di avanzamento

## Funzione del documento

Questo file è l'unica fonte per lo stato corrente del progetto. Registra ciò che è stato realizzato, ciò che è in lavorazione, le prossime priorità e le questioni operative aperte.

Il Master Plan definisce l'architettura didattica e i contenuti previsti.
Le Guidelines definiscono le regole operative stabili. La Notazione definisce
le convenzioni matematiche. Le decisioni progettuali stabili e le relative
motivazioni sono recepite nel documento normativo pertinente.

## Snapshot al 2026-10-24

|  |  |
|---|---|
| **Ultima attività completata** | Completata la verifica residuale dei rinvii espliciti obsoleti a capitoli, lezioni, file, notebook e percorsi. La passata ha riguardato le slides delle Lezioni 1--16, i materiali applicativi e operativi delle Lezioni 4, 7, 10, 13 e 16, i template dei prompt e le Istruzioni Studente, nonché Master Plan, Guidelines, Notazione e Stato di avanzamento. Sono stati corretti i residui individuati nella Lezione 13 relativi alla scansione dualità--sensitività e i riferimenti alla calibrazione docente del Caso TakeHome, ricondotta alla Scheda Costruzione Caso TakeHome. Il controllo residuale dei rinvii espliciti è pertanto concluso. |
| **Materiale sviluppato** | Manuale: contenuto sostanziale per i Capitoli 1-16. Slides: contenuto sostanziale per le Lezioni 1-16. Pacchetti applicativi strutturati per le Lezioni 4, 7, 10, 13 e 16. Codice, notebook, script e asset grafici presenti lungo l'intero corso, inclusi i blocchi di programmazione lineare, ALM e programmazione stocastica. |
| **Lavoro in corso** | La verifica conclusiva di coerenza è completata, con lo stesso trattamento metodologico, per tutti e cinque i blocchi del corso: Capitoli/Lezioni 1--4, 5--7, 8--10, 11--13 e 14--16. Per le Lezioni applicative 4, 7, 10, 13 e 16 risultano inoltre concluse la verifica di coerenza dei notebook docente Aula/TakeHome con le rispettive Schede Caso e Schede Costruzione e la validazione tecnica con controllo degli output. La compilazione di manuale e slides viene svolta ordinariamente a seguito delle modifiche e non costituisce un'attività residua autonoma. La verifica residuale dei rinvii espliciti obsoleti a capitoli, lezioni, file, notebook e percorsi è conclusa. Restano da completare la verifica finale dei template IA e degli asset tecnici. |
| **Prossima priorità** | Completare il controllo dei template IA e degli asset tecnici; implementare la scaletta-promemoria per le lezioni teoriche e aggiornare nel Master Plan il riferimento alla pagina pubblica del progetto. |

---

## Stato per lezione

Legenda: `sviluppato` = contenuto sostanziale presente; `parziale` = componente presente ma incompleta o non ancora validata in modo conclusivo; `traccia` = solo struttura iniziale; `-` = non iniziato; `n.a.` = non applicabile.

La classificazione `sviluppato` non equivale a `chiuso`: in questa fase gran parte del corso è sviluppato con taratura o verifica conclusiva residua.

Alla data del 2026-10-24 nessuna lezione viene riclassificata automaticamente come `chiusa`. La classificazione richiede il completamento dei controlli di coerenza, compilabilità e, per le lezioni applicative, esecuzione e riproducibilità dei notebook; gli audit automatici restano strumenti di ricognizione e non costituiscono da soli certificazione di chiusura.

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
| 15 | P | Soluzione e valore dell'informazione | sviluppato | sviluppato | sviluppato | sviluppato | n.a. |
| 16 | C | Python: programmazione stocastica | sviluppato | sviluppato | sviluppato | sviluppato | sviluppato |

---

## Checklist per il controllo di raccordo

Questa sezione conserva una checklist operativa per il controllo orizzontale, verticale e incrociato dei materiali del corso. Non rappresenta lo stato ufficiale di avanzamento, sintetizzato nelle sezioni precedenti. Le note vengono aggiornate o eliminate quando il relativo controllo è stato completato.

Ai fini dello stato complessivo del progetto, i blocchi Capitoli/Lezioni 1--4, 5--7, 8--10, 11--13 e 14--16 sono tutti classificati uniformemente come **verifica conclusiva di coerenza completata**. Le formulazioni più specifiche riportate nelle note della checklist descrivono il contenuto dei controlli svolti e non indicano livelli differenti di completamento.

| Area | Note |
|---|---|
| Probabilità, variabili casuali e condizionamento | Raccordo conclusivo verificato tra Capitoli/Lezioni 1--4 e documenti normativi pertinenti: coerenti spazio di probabilità ed eventi, variabili casuali e distribuzioni, valore atteso condizionato e informazione, proprietà della torre e trasferimento computazionale nella Lezione 4. È stato inoltre riallineato il richiamo alla disuguaglianza condizionata di Jensen nella Lezione 3, esplicitando nelle slides l'integrabilità di $\varphi(X)$ in coerenza con il Capitolo 3. Le incoerenze sostanziali individuate nella passata sono state corrette; la verifica integrale successiva non ha evidenziato ulteriori incoerenze plateali. |
| Processi stocastici discreti e filtrazioni | Raccordo verificato tra Capitolo/Lezione 5 e Capitoli 1-4: coerenti informazione, filtrazioni, adattabilità, prevedibilità delle decisioni, martingale e ruolo strutturale del modello binomiale. |
| Processi stocastici continui | Raccordo verificato tra Capitoli/Lezioni 6-7: coerenti moto browniano, diffusioni geometriche, OU, CIR, correlazione, Eulero--Maruyama, distinzione tra scenari del modello e repliche Monte Carlo e passaggio dalla teoria alla simulazione e al pricing. |
| Catene di Markov | Raccordo verificato tra Capitolo/Lezione 8, Capitolo/Lezione 9 e Lezione 10: coerenti dinamica markoviana, stato di default assorbente, passaggio dalle probabilità alle perdite e trasferimento alla simulazione di portafoglio. |
| Misure di rischio | Raccordo verificato nel blocco 8--10. La Lezione 9 distingue Expected Loss, dispersione complessiva, unexpected loss, VaR, CVaR e capitale economico; il passaggio dalla distribuzione markoviana degli stati alla distribuzione monetaria delle perdite esplicita l'aggregazione delle probabilità per perdite coincidenti e il collegamento alle Expected Credit Loss. Il trasferimento alla Lezione 10 resta coerente con la simulazione di portafoglio e le misure di coda già verificate. |
| Modello binomiale | Controllo concluso nel blocco Capitoli/Lezioni 5--7. Il modello binomiale resta utilizzato come esempio strutturale di processo discreto e come palestra per traiettorie, filtrazioni, adattabilità e martingale. Il raccordo elementare con assenza di arbitraggio, misura risk-neutral e valutazione di un payoff nel Capitolo/Lezione 5 è funzionale alla lettura finanziaria delle martingale e non costituisce un modulo autonomo di pricing dei derivati. Nel Capitolo/Lezione 6 il richiamo al binomiale svolge esclusivamente la funzione di ponte concettuale dalla passeggiata aleatoria al moto browniano; nel Capitolo/Lezione 7 non emergono sviluppi ulteriori del modello binomiale. Non risultano quindi debordamenti rispetto alla funzione didattica assegnata. |
| Programmazione lineare e dualità | Raccordo conclusivo verificato nel blocco Capitoli/Lezioni 11--12. La scansione scientifica del Manuale mantiene nel Capitolo 11 formulazione primale, vincoli attivi, sensitività, problema duale, dualità debole e forte, complementarietà e prezzi impliciti; il Capitolo 12 utilizza tali strumenti per passare dal requisito aggregato ai bilanci intertemporali dell'ALM deterministico. La scansione didattica è deliberatamente diversa: la Lezione 11 si arresta alla sensitività e all'interpretazione dei prezzi ombra, mentre la costruzione formale del duale, la dualità debole e forte e la complementarietà sono svolte all'apertura della Lezione 12 e immediatamente raccordate all'ALM. Le slides 11--12 sono state riallineate e verificate; il Master Plan e le Guidelines registrano ora esplicitamente questa diversa scansione e chiariscono che la corrispondenza tra capitoli del Manuale e lezioni non è necessariamente uno-a-uno. La Notazione non ha richiesto modifiche. |
| Asset--Liability Management deterministico | Raccordo verificato tra Capitolo/Lezione 12 e Lezione 13. Il Capitolo 13 rende operativo, senza introdurre una nuova classe di modelli, l'ALM deterministico formulato nel Capitolo 12; mantiene le variabili di allocazione $x$, le giacenze $g$, il funding $u$, i bilanci temporali e la relativa interpretazione economica, traducendoli in vettore decisionale, funzione obiettivo, uguaglianze, disuguaglianze e bound per `scipy.optimize.linprog`. Le slides della Lezione 13 esplicitano la sequenza Lezione 11 $\rightarrow$ Lezione 12 $\rightarrow$ Lezione 13 e il passaggio da programmazione lineare ad ALM deterministico e quindi a implementazione e analisi computazionale. È stata completata la passata conclusiva di coerenza tra Capitolo 13, slides, Schede Costruzione Caso Aula/TakeHome e Schede Caso Aula/TakeHome: driver, struttura dei modelli, output, controlli, scenari, frontiera di fattibilità e vincolo legacy risultano allineati e non restano incoerenze sostanziali note nel pacchetto documentale. Sono stati inoltre ricostruiti e validati i notebook docente Aula e TakeHome secondo la nuova architettura di 8 passi e 6 tappe, con esecuzione integrale, verifica degli output, dei marginali, delle sensitività e degli scenari. La verifica applicativa della Lezione 13 è quindi conclusa. |
| Programmazione stocastica | Raccordo conclusivo verificato nel blocco Capitoli/Lezioni 14--16. La Lezione 14 introduce il framework two-stage, distinguendo decisione ex ante, scenari, ricorso, forma estesa e non anticipatività della decisione iniziale. Il Capitolo 15 amplia la trattazione alla programmazione stocastica multistadio, alla rivelazione progressiva dell'informazione e ai vincoli di non anticipatività tra nodi con storia comune; la Lezione 15, invece, rimane deliberatamente nel framework a due stadi e approfondisce fattibilità del ricorso, proprietà della funzione di ricorso, SP/EV/WS, VSS/EVPI e forma estesa. La Lezione 16 consolida sul piano computazionale lo stesso framework two-stage mediante una decisione iniziale unica $x$ comune agli scenari e ricorso scenario-specifico $y_s$; il Caso Aula utilizza una versione ridotta del SVB--ALM e presenta ricorso relativamente completo grazie al funding illimitato, mentre il Caso TakeHome UK LDI utilizza capacità di ricorso limitate e rende esplicita la dipendenza della fattibilità dalla decisione di primo stadio. Il Master Plan registra esplicitamente la diversa scansione tra Manuale e lezioni, sia nelle schede delle Lezioni 15--16 sia nel registro degli esercizi. Nel two-stage la non anticipatività della decisione iniziale è incorporata strutturalmente dall'unicità di $x$. Sono state completate la verifica di coerenza tra Schede Costruzione, Schede Caso e notebook docente Aula/TakeHome della Lezione 16, la validazione tecnica dei notebook, la verifica degli output e il controllo di riproducibilità. Il blocco 14--16 è quindi stabilizzato sul piano teorico, didattico e applicativo. |

---

## Verifiche tecniche ancora da completare

La compilazione del manuale e dei deck viene effettuata ordinariamente nel corso delle revisioni e delle modifiche e non è quindi registrata come verifica tecnica residua autonoma.

Resta da completare:

- una verifica visuale sistematica degli output grafici e degli eventuali problemi di impaginazione.

L'output dell'audit contiene anche rumore tecnico che non deve essere interpretato come avanzamento didattico, tra cui file temporanei Word, directory `__pycache__`, file `synctex(busy)`, copie `_old` e cartelle storiche.

---

## Questioni operative aperte

- Per le Lezioni applicative 4, 7, 10, 13 e 16 la verifica di coerenza dei notebook rispetto alle rispettive specifiche applicative e la validazione tecnica dei notebook docente risultano concluse.
- Il blocco 14--16 è stabilizzato sul piano del raccordo teorico, didattico e applicativo: il Capitolo 15 mantiene l'estensione multistadio, mentre le Lezioni 15 e 16 restano deliberatamente nel framework two-stage; nella Lezione 16 la non anticipatività è rappresentata mediante un'unica decisione iniziale comune agli scenari e ricorso scenario-specifico.
- La compilazione di manuale e deck viene svolta ordinariamente durante le revisioni e non costituisce un'attività aperta autonoma.
- Riesaminare puntualmente i template IA rispetto alle Istruzioni Studente correnti, verificando coerenza dei Regimi A/B/C, del formato dei tracciati e dei materiali di valutazione.
- Implementare per le lezioni teoriche la `scaletta-promemoria` prevista dal Master Plan, attualmente non ancora realizzata come materiale operativo. In tale contesto, sostituire nel Master Plan il riferimento alla pagina `https://paolilla25.synology.me/github-publish/public/` con il repository GitHub pubblico `https://github.com/paolo-fix/CORSO-MQF`, definendo un criterio di accesso ai documenti che consenta di individuare e leggere senza ambiguità i materiali necessari anche quando sono collocati in cartelle e sottocartelle differenti della struttura del repository.
