# MQF - Stato di avanzamento

## Funzione del documento

Questo file è l'unica fonte per lo stato corrente del progetto. Registra ciò che è stato realizzato, ciò che è in lavorazione, le prossime priorità e le questioni operative aperte.

Il Master Plan definisce l'architettura didattica e i contenuti previsti.
Le Guidelines definiscono le regole operative stabili. La Notazione definisce
le convenzioni matematiche. Le decisioni progettuali stabili e le relative
motivazioni sono recepite nel documento normativo pertinente.

## Snapshot al 2026-10-23

|  |  |
|---|---|
| **Ultima attività completata** | Completata la passata conclusiva di coerenza del blocco Capitoli/Lezioni 14--16, inclusa la verifica applicativa della Lezione 16. Il raccordo teorico tra Lezioni 14--15 e Capitoli 14--15 è stabilizzato: la Lezione 14 resta dedicata ai fondamenti della programmazione stocastica a due stadi; il Capitolo 15 amplia la trattazione al multistadio, mentre la Lezione 15 rimane deliberatamente nel framework two-stage per approfondire fattibilità del ricorso, funzione di ricorso, SP/EV/WS, VSS/EVPI e forma estesa. La Lezione 16 consolida computazionalmente lo stesso framework two-stage. Schede Costruzione, Schede Caso e notebook docente Aula/TakeHome della Lezione 16 sono stati riallineati e validati; nel Caso Aula il ricorso è relativamente completo, mentre nel TakeHome la capacità di ricorso è limitata e la non ammissibilità di $x^{EV}$ nello scenario estremo comporta la non definibilità standard di $z^{EV}$ e VSS. |
| **Materiale sviluppato** | Manuale: contenuto sostanziale per i Capitoli 1-16. Slides: contenuto sostanziale per le Lezioni 1-16. Pacchetti applicativi strutturati per le Lezioni 4, 7, 10, 13 e 16. Codice, notebook, script e asset grafici presenti lungo l'intero corso, inclusi i blocchi di programmazione lineare, ALM e programmazione stocastica. |
| **Lavoro in corso** | Prosegue la verifica conclusiva di coerenza orizzontale, verticale e incrociata nei blocchi del corso non ancora sottoposti a passata conclusiva. Il blocco Capitoli/Lezioni 1--4 ha completato la verifica sostanziale di coerenza; per la Lezione 4 risultano completati anche il riallineamento del pacchetto applicativo TakeHome, la produzione del notebook docente coerente con il protocollo dei prompt e la relativa esecuzione tecnica. Per le Lezioni 7, 10, 13 e 16 sono concluse sia la verifica di coerenza dei notebook docente Aula/TakeHome con le rispettive Schede Caso e Schede Costruzione sia la validazione tecnica con controllo degli output. Nel blocco 11--13 risultano verificati il raccordo programmazione lineare--dualità--ALM, la diversa scansione intenzionale tra Capitoli 11--12 e Lezioni 11--12, il raccordo teorico-computazionale tra ALM deterministico e Lezione 13, la coerenza conclusiva tra Capitolo 13, slides, Schede Costruzione e Schede Caso e la validazione dei notebook docente Aula/TakeHome. Il blocco 14--16 è concluso sul piano della coerenza interna, sia teorica sia applicativa. La compilazione di manuale e slides viene svolta ordinariamente a seguito delle modifiche e non costituisce un'attività residua autonoma. Resta da svolgere una verifica residuale di eventuali rinvii espliciti obsoleti a capitoli, lezioni, file e notebook, oltre alla verifica finale dei template e dei materiali operativi. |
| **Prossima priorità** | Completare le passate conclusive sui blocchi ancora aperti utilizzando la checklist di raccordo, senza riaprire i blocchi già verificati salvo nuove evidenze; svolgere una verifica residuale di eventuali rinvii espliciti obsoleti a capitoli, lezioni, file e notebook; completare il controllo di template IA e asset tecnici. |

---

## Stato per lezione

Legenda: `sviluppato` = contenuto sostanziale presente; `parziale` = componente presente ma incompleta o non ancora validata in modo conclusivo; `traccia` = solo struttura iniziale; `-` = non iniziato; `n.a.` = non applicabile.

La classificazione `sviluppato` non equivale a `chiuso`: in questa fase gran parte del corso è sviluppato con taratura o verifica conclusiva residua.

Alla data del 2026-10-23 nessuna lezione viene riclassificata automaticamente come `chiusa`. La classificazione richiede il completamento dei controlli di coerenza, compilabilità e, per le lezioni applicative, esecuzione e riproducibilità dei notebook; gli audit automatici restano strumenti di ricognizione e non costituiscono da soli certificazione di chiusura.

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

| Area | Note |
|---|---|
| Probabilità, variabili casuali e condizionamento | Raccordo conclusivo verificato tra Capitoli/Lezioni 1--4 e documenti normativi pertinenti: coerenti spazio di probabilità ed eventi, variabili casuali e distribuzioni, valore atteso condizionato e informazione, proprietà della torre e trasferimento computazionale nella Lezione 4. È stato inoltre riallineato il richiamo alla disuguaglianza condizionata di Jensen nella Lezione 3, esplicitando nelle slides l'integrabilità di $\varphi(X)$ in coerenza con il Capitolo 3. Le incoerenze sostanziali individuate nella passata sono state corrette; la verifica integrale successiva non ha evidenziato ulteriori incoerenze plateali. |
| Processi stocastici discreti e filtrazioni | Raccordo verificato tra Capitolo/Lezione 5 e Capitoli 1-4: coerenti informazione, filtrazioni, adattabilità, prevedibilità delle decisioni, martingale e ruolo strutturale del modello binomiale. |
| Processi stocastici continui | Raccordo verificato tra Capitoli/Lezioni 6-7: coerenti moto browniano, diffusioni geometriche, OU, CIR, correlazione, Eulero--Maruyama, distinzione tra scenari del modello e repliche Monte Carlo e passaggio dalla teoria alla simulazione e al pricing. |
| Catene di Markov | Raccordo verificato tra Capitolo/Lezione 8, Capitolo/Lezione 9 e Lezione 10: coerenti dinamica markoviana, stato di default assorbente, passaggio dalle probabilità alle perdite e trasferimento alla simulazione di portafoglio. |
| Misure di rischio | Raccordo verificato nel blocco 8--10. La Lezione 9 distingue Expected Loss, dispersione complessiva, unexpected loss, VaR, CVaR e capitale economico; il passaggio dalla distribuzione markoviana degli stati alla distribuzione monetaria delle perdite esplicita l'aggregazione delle probabilità per perdite coincidenti e il collegamento alle Expected Credit Loss. Il trasferimento alla Lezione 10 resta coerente con la simulazione di portafoglio e le misure di coda già verificate. |
| Modello binomiale | Controllo concluso nel blocco Capitoli/Lezioni 5--7. Il modello binomiale resta utilizzato come esempio strutturale di processo discreto e come palestra per traiettorie, filtrazioni, adattabilità e martingale. Il raccordo elementare con assenza di arbitraggio, misura risk-neutral e valutazione di un payoff nel Capitolo/Lezione 5 è funzionale alla lettura finanziaria delle martingale e non costituisce un modulo autonomo di pricing dei derivati. Nel Capitolo/Lezione 6 il richiamo al binomiale svolge esclusivamente la funzione di ponte concettuale dalla passeggiata aleatoria al moto browniano; nel Capitolo/Lezione 7 non emergono sviluppi ulteriori del modello binomiale. Non risultano quindi debordamenti rispetto alla funzione didattica assegnata. |
| Programmazione lineare e dualità | Raccordo conclusivo verificato nel blocco Capitoli/Lezioni 11--12. La scansione scientifica del Manuale mantiene nel Capitolo 11 formulazione primale, vincoli attivi, sensitivit\`a, problema duale, dualità debole e forte, complementarietà e prezzi impliciti; il Capitolo 12 utilizza tali strumenti per passare dal requisito aggregato ai bilanci intertemporali dell'ALM deterministico. La scansione didattica è deliberatamente diversa: la Lezione 11 si arresta alla sensitivit\`a e all'interpretazione dei prezzi ombra, mentre la costruzione formale del duale, la dualità debole e forte e la complementarietà sono svolte all'apertura della Lezione 12 e immediatamente raccordate all'ALM. Le slides 11--12 sono state riallineate e verificate; il Master Plan e le Guidelines registrano ora esplicitamente questa diversa scansione e chiariscono che la corrispondenza tra capitoli del Manuale e lezioni non è necessariamente uno-a-uno. La Notazione non ha richiesto modifiche. |
| Asset--Liability Management deterministico | Raccordo verificato tra Capitolo/Lezione 12 e Lezione 13. Il Capitolo 13 rende operativo, senza introdurre una nuova classe di modelli, l'ALM deterministico formulato nel Capitolo 12; mantiene le variabili di allocazione $x$, le giacenze $g$, il funding $u$, i bilanci temporali e la relativa interpretazione economica, traducendoli in vettore decisionale, funzione obiettivo, uguaglianze, disuguaglianze e bound per `scipy.optimize.linprog`. Le slides della Lezione 13 esplicitano la sequenza Lezione 11 $\rightarrow$ Lezione 12 $\rightarrow$ Lezione 13 e il passaggio da programmazione lineare ad ALM deterministico e quindi a implementazione e analisi computazionale. È stata completata la passata conclusiva di coerenza tra Capitolo 13, slides, Schede Costruzione Caso Aula/TakeHome e Schede Caso Aula/TakeHome: driver, struttura dei modelli, output, controlli, scenari, frontiera di fattibilità e vincolo legacy risultano allineati e non restano incoerenze sostanziali note nel pacchetto documentale. Sono stati inoltre ricostruiti e validati i notebook docente Aula e TakeHome secondo la nuova architettura di 8 passi e 6 tappe, con esecuzione integrale, verifica degli output, dei marginali, delle sensitività e degli scenari. La verifica applicativa della Lezione 13 è quindi conclusa. |
| Programmazione stocastica | Raccordo conclusivo verificato nel blocco Capitoli/Lezioni 14--16. La Lezione 14 introduce il framework two-stage, distinguendo decisione ex ante, scenari, ricorso, forma estesa e non anticipatività della decisione iniziale. Il Capitolo 15 amplia la trattazione alla programmazione stocastica multistadio, alla rivelazione progressiva dell'informazione e ai vincoli di non anticipatività tra nodi con storia comune; la Lezione 15, invece, rimane deliberatamente nel framework a due stadi e approfondisce fattibilità del ricorso, proprietà della funzione di ricorso, SP/EV/WS, VSS/EVPI e forma estesa. La Lezione 16 consolida sul piano computazionale lo stesso framework two-stage mediante una decisione iniziale unica $x$ comune agli scenari e ricorso scenario-specifico $y_s$; il Caso Aula utilizza una versione ridotta del SVB--ALM e presenta ricorso relativamente completo grazie al funding illimitato, mentre il Caso TakeHome UK LDI utilizza capacità di ricorso limitate e rende esplicita la dipendenza della fattibilità dalla decisione di primo stadio. Il Master Plan registra esplicitamente la diversa scansione tra Manuale e lezioni, sia nelle schede delle Lezioni 15--16 sia nel registro degli esercizi. Nel two-stage la non anticipatività della decisione iniziale è incorporata strutturalmente dall'unicità di $x$. Sono state completate la verifica di coerenza tra Schede Costruzione, Schede Caso e notebook docente Aula/TakeHome della Lezione 16 e la validazione dei relativi benchmark SP/EV/WS, VSS/EVPI e controlli di fattibilità. Non restano incoerenze sostanziali note nel blocco 14--16. |
| Corrispondenza Python | Per la Lezione 4 è stata verificata la coerenza tra Scheda Caso, Scheda Costruzione, protocollo dei prompt, notebook, output e controlli, inclusa la riproducibilità mediante riesecuzione completa. Il notebook docente TakeHome è stato ricostruito in modo esplicitamente conforme alla sequenza Prompt zero → Prompt 1 → Prompt 2 → Prompt 3 → prompt di tappa: Prompt zero resta nel tracciato IA; Prompt 1--3 generano le tre celle Markdown iniziali; le Tappe 1--5 sono organizzate come coppie Markdown → Python e la Tappa 6 contiene interpretazione critica e limiti. Il notebook è stato eseguito integralmente con esito positivo. Per la Lezione 7 i notebook docente Aula e TakeHome sono stati ricostruiti e validati direttamente sulle Schede Costruzione e Schede Caso correnti e sui documenti normativi: Prompt zero resta nel protocollo senza generare una cella quantitativa autonoma; Prompt 1, Prompt 2 e Prompt 3 producono le celle Markdown iniziali; le sei tappe sono sviluppate come moduli Markdown → Python. I Flussi logico-teorici mantengono integralmente la scansione delle Schede Costruzione, con 11 passi per l'Aula e 12 per il TakeHome, e le sei tappe input-output restano quelle canoniche. Entrambi i notebook sono stati rieseguiti integralmente con esito positivo, inclusi output, controlli, convenzione CIR, diagnostica Monte Carlo, controllo della discretizzazione e riproducibilità. Per la Lezione 10 i notebook docente Aula e TakeHome sono stati ricostruiti direttamente dalle Schede Costruzione Caso e dalle Schede Caso correnti, tenendo conto delle Guidelines e dei template canonici dei prompt. Entrambi seguono sei passi del Flusso logico-teorico e sei tappe input-output; hanno 22 celle ciascuno, 11 Markdown e 11 Python, in alternanza rigorosa. Sono stati rieseguiti integralmente senza errori. Il Caso Aula preserva la specifica Evergrande con tempo di primo default, LGD dipendente dal regime che governa la transizione verso il default e confronto mediante Common Random Numbers; il Caso TakeHome preserva la specifica Lehman con LGD costante e funzione di perdita migration-based sul rating finale, mantenendo identiche le traiettorie dei 39 debitori comuni. Per entrambi risultano verificati gli output numerici, le quattro tabelle, le tre figure, i controlli previsti, i seed assegnati, la stabilità empirica Monte Carlo e il calcolo di VaR/CVaR sulle perdite monetarie secondo la definizione quantile-based adottata nel Capitolo 9; i risultati sono stati inoltre confrontati con i benchmark indicativi delle rispettive Schede Costruzione. Per la Lezione 13 i notebook docente Aula e TakeHome sono stati ricostruiti sulle Schede Costruzione e Schede Caso aggiornate: entrambi adottano un Flusso in 8 passi e 6 tappe, Prompt zero non genera una cella autonoma, Prompt 1--3 costituiscono le tre celle Markdown iniziali e le sei tappe operative sono articolate in coppie Markdown → Python, con una cella Markdown finale destinata all'interpretazione autonoma. Entrambi contano 16 celle, 10 Markdown e 6 Python, e sono stati rieseguiti integralmente senza errori. Nel Caso Aula risultano verificati benchmark, 10 tabelle, 14 figure, marginali, sensitività a $\theta$, $\phi$, $\psi$, frontiera di fattibilità e scenari; nel TakeHome risultano verificati benchmark, 6 tabelle, 6 figure, sensitività ad $\alpha$, $\beta$, $\phi$, confronto delle due ondate, vincolo legacy e relazione $\partial\Pi^*/\partial L=m$, oltre agli scenari. Per la Lezione 16 i notebook docente Aula e TakeHome sono stati ricostruiti e validati rispetto alle Schede Costruzione e Schede Caso correnti. Entrambi mantengono il framework two-stage e una decisione iniziale unica comune agli scenari. Nel Caso Aula risultano verificati i benchmark $x^{SP}=(0,30,70,0)'$, $z^{SP}=3.4375$, $x^{EV}=(0,0,30,70)'$, $z^{EV}=3.3500$, $VSS=0.0875$, $z^{WS}=4.510625$ ed $EVPI=1.073125$, insieme a rendimento iniziale lordo, costo atteso del funding, cinque tabelle, due figure e controlli conclusivi. Nel TakeHome risultano verificati $x^{SP}=(20,80)'$, $z^{SP}=3.944000$, $x^{EV}=(0,100)'$, valore del problema medio pari a $4.387228$, inammissibilità di $x^{EV}$ nello scenario estremo, conseguente non definibilità standard di $z^{EV}$ e VSS, $z^{WS}=4.506429$ ed $EVPI=0.562429$, cinque tabelle, tre figure e controlli conclusivi. Le Lezioni applicative 4, 7, 10, 13 e 16 non rientrano più tra quelle per cui resta aperta la verifica di corrispondenza Python o la validazione tecnica dei notebook docente. |
| Rischio di credito e risk-neutral | Raccordo verificato tra Capitoli/Lezioni 8-10: coerenti distinzione tra misura fisica e misura risk-neutral, uso delle matrici di transizione, costruzione delle perdite, misure di rischio e simulazione Monte Carlo di portafoglio. |

---

## Verifica 2026-10-23 - Chiusura del blocco 14--16

È stata completata la verifica conclusiva del blocco Capitoli/Lezioni 14--16, inclusa la componente applicativa della Lezione 16.

### Evidenze verificate

- Il raccordo tra Capitolo/Lezione 14, Capitolo 15 e Lezione 15 è coerente con la scansione deliberata del corso: fondamenti two-stage nella Lezione 14; estensione multistadio nel Capitolo 15; approfondimento two-stage nella Lezione 15.
- La Lezione 16 resta esclusivamente two-stage e non implementa la rivelazione progressiva dell'informazione né vincoli di non anticipatività tra nodi intermedi.
- Scheda Costruzione e Scheda Caso Aula sono allineate sul caso SVB--ALM ridotto, sul funding illimitato e sul ricorso relativamente completo.
- Scheda Costruzione e Scheda Caso TakeHome sono allineate sul caso UK LDI 2022, sui limiti $e_s\leq4$, $f_s\leq25$, $f_s\leq x_2$ e sulla centralità della fattibilità del ricorso.
- Il notebook docente Aula è coerente con le due schede: implementa SP, EV con rivalutazione, WS, VSS ed EVPI e produce gli output e i controlli richiesti.
- Il notebook docente TakeHome è coerente con le due schede: mantiene $x^{EV}$ fissa durante la rivalutazione, riconosce l'inammissibilità nello scenario estremo e non attribuisce valori artificiali a $z^{EV}$ o VSS.
- I Flussi logico-teorici e le scomposizioni in tappe dei notebook docente sono stati riallineati alle rispettive Schede Costruzione; Prompt zero non genera una cella autonoma nei notebook docente.
- Le tabelle, i grafici e i benchmark numerici dei due notebook risultano coerenti con la calibrazione docente.

### Esito

Il blocco 14--16 è considerato stabilizzato sul piano della coerenza interna teorica, didattica e applicativa. Non restano incoerenze sostanziali note nel blocco; eventuali future riaperture dovranno derivare da nuove evidenze o da modifiche successive ai documenti normativi.

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

La compilazione del manuale e dei deck viene effettuata ordinariamente nel corso delle revisioni e delle modifiche e non è quindi registrata come verifica tecnica residua autonoma.

Restano da completare:

- una verifica visuale sistematica degli output grafici e degli eventuali problemi di impaginazione;
- una verifica residuale di eventuali rinvii espliciti obsoleti a capitoli, lezioni, file e notebook.

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
- Usare la `Checklist per il controllo di raccordo` per i controlli orizzontali, verticali e incrociati ancora aperti.
- Chiudere le incoerenze residue eventualmente individuate nei blocchi ancora in revisione prima di considerarne conclusa la verifica.
- Per le Lezioni applicative 4, 7, 10, 13 e 16 la verifica di coerenza dei notebook rispetto alle rispettive specifiche applicative e la validazione tecnica dei notebook docente risultano concluse.
- Il blocco 14--16 è stabilizzato sul piano del raccordo teorico, didattico e applicativo: il Capitolo 15 mantiene l'estensione multistadio, mentre le Lezioni 15 e 16 restano deliberatamente nel framework two-stage; nella Lezione 16 la non anticipatività è rappresentata mediante un'unica decisione iniziale comune agli scenari e ricorso scenario-specifico.
- La compilazione di manuale e deck viene svolta ordinariamente durante le revisioni e non costituisce un'attività aperta autonoma.
- Svolgere una verifica residuale di eventuali rinvii espliciti obsoleti a capitoli, lezioni, file e notebook.
- Riesaminare puntualmente i template IA rispetto alle Istruzioni Studente correnti, verificando coerenza dei Regimi A/B/C, del formato dei tracciati e dei materiali di valutazione.
- Implementare per le lezioni teoriche la `scaletta-promemoria` prevista dal Master Plan, attualmente non ancora realizzata come materiale operativo. In tale contesto, sostituire nel Master Plan il riferimento alla pagina `https://paolilla25.synology.me/github-publish/public/` con il repository GitHub pubblico `https://github.com/paolo-fix/CORSO-MQF`, definendo un criterio di accesso ai documenti che consenta di individuare e leggere senza ambiguità i materiali necessari anche quando sono collocati in cartelle e sottocartelle differenti della struttura del repository.