# MQF - Stato di avanzamento

## Funzione del documento

Questo file è l'unica fonte per lo stato corrente del progetto. Registra ciò che è stato realizzato, ciò che è in lavorazione, le prossime priorità e le questioni operative aperte.

Il Master Plan definisce l'architettura didattica e i contenuti previsti. Le Guidelines definiscono le regole stabili. Il Registro decisionale conserva le decisioni progettuali e le relative motivazioni.

## Snapshot al 2026-08-23

|  |  |
|---|---|
| **Ultima attività completata** | Sviluppo del Capitolo 12 e delle slides della Lezione 12 su dualità e ALM deterministico, con esercizi, grafici, codice sorgente delle figure e raccordo con la Lezione 13; aggiornamento dei promemoria delle Lezioni 11-12. |
| **Materiale sviluppato** | Capitoli 1-6, 8-9 e 11-12 del manuale; slides delle Lezioni 1, 2, 3, 5, 6, 8, 9, 11 e 12; pacchetto applicativo della Lezione 4; schede e notebook parziali della Lezione 7; schede caso della Lezione 10; grafici collegati ai Capitoli 1-6, 8-9 e 11-12. |
| **Lavoro in corso** | Chiusura delle tarature editoriali e tecniche delle Lezioni 9, 11 e 12; completamento dei pacchetti applicativi delle Lezioni 7 e 10; riallineamento puntuale dei template IA. |
| **Prossima priorità** | Predisporre il pacchetto applicativo della Lezione 13 su programmazione lineare e ALM deterministico, archiviando prima il codice solver di validazione dei casi delle Lezioni 11-12. |

---

## Stato per lezione

Legenda: `sviluppato` = contenuto sostanziale presente; `parziale` = componente presente ma incompleta; `traccia` = solo struttura iniziale; `-` = non iniziato; `n.a.` = non applicabile.

| Lez. | Tipo | Titolo sintetico | Manuale | Slides | Esercizi/materiali operativi | Grafici | Python/Notebook |
|---:|:---:|---|:---:|:---:|:---:|:---:|:---:|
| 1 | P | Elementi di probabilità | sviluppato | sviluppato | sviluppato | sviluppato | n.a. |
| 2 | P | Variabili casuali | sviluppato | sviluppato | sviluppato | sviluppato | n.a. |
| 3 | P | Valori attesi condizionati | sviluppato | sviluppato | sviluppato | sviluppato | n.a. |
| 4 | C | Python: probabilità e condizionamento | sviluppato | - | sviluppato | sviluppato | sviluppato |
| 5 | P | Processi stocastici in tempo discreto | sviluppato | sviluppato | sviluppato | sviluppato | n.a. |
| 6 | P | Processi stocastici in tempo continuo | sviluppato | sviluppato | parziale | sviluppato | n.a. |
| 7 | C | Traiettorie, simulazione e pricing | traccia | - | parziale | - | parziale |
| 8 | P | Catene di Markov | sviluppato | sviluppato | sviluppato | sviluppato | n.a. |
| 9 | P | Markov e misure di rischio | sviluppato | sviluppato | sviluppato | sviluppato | n.a. |
| 10 | C | Python: rischio di credito | traccia | - | parziale | - | - |
| 11 | P | Programmazione lineare | sviluppato | sviluppato | sviluppato | sviluppato | n.a. |
| 12 | P | Dualità e ALM deterministico | sviluppato | sviluppato | sviluppato | sviluppato | n.a. |
| 13 | C | Python: programmazione lineare e ALM deterministico | traccia | - | - | - | - |
| 14 | P | Programmazione stocastica a due stadi | traccia | - | - | - | n.a. |
| 15 | P | Programmazione stocastica multistadio | traccia | - | - | - | n.a. |
| 16 | C | Python: programmazione stocastica | traccia | - | - | - | - |

---

## Verifica 2026-07-17 - Lezione 6

Le slides `Slides_Lez_06_Processi_Stocastici_Tempo_Continuo.tex` sono
sviluppate e compilabili. La struttura copre il passaggio dal tempo discreto al
moto browniano, le SDE, GBM, processi OU/CIR, shock correlati,
discretizzazione di Eulero--Maruyama e raccordo con Python. Sono presenti
figure coerenti con il Capitolo 6, esercizi in aula e una scansione temporale
interna.

La compilazione genera il PDF senza errori bloccanti. Restano alcuni warning
tipografici, in particolare overfull verticali nelle parti finali su
correlazione e discretizzazione; si tratta di taratura locale delle slides, non
di predisposizione mancante.

---

## Aggiornamento 2026-07-16 - Lezione 8

La Lezione 8 sulle catene di Markov è passata da traccia a sviluppo avanzato.
Il materiale disponibile comprende il capitolo del manuale, le slides di
lezione, un insieme di grafici dedicati e lo script sorgente per il grafo del
mercato elettrico.

### Completato

- Predisposte le slides `Slides_Lez_08_Catene_Markov.tex`, con 32 slides di
  lezione e 5 slides di back-up. La struttura è stata calibrata per una lezione
  di 120 minuti, con due esercizi in aula e contenuti tecnici di supporto
  collocati in back-up.
- Integrati nelle slides due esercizi collegati agli esercizi proposti del
  Capitolo 8: dinamica a più passi della catena e catena di rating con default.
- Prodotti i grafici `Cap08_*`, inclusi il grafo del mercato elettrico, il grafo
  rating-default, l'evoluzione delle probabilità di stato e il confronto con la
  distribuzione stazionaria.
- Archiviato lo script `04_Codice/Lez08/Cap08_grafo_mercato_elettrico.py` per la
  generazione del grafo del mercato elettrico.
- Inserita nel Capitolo 8 la figura del grafo del mercato elettrico e corretti
  il refuso su `proprietà congiunta` e il blocco fuori posto sulla lettura della
  matrice.
- Allineato il Master Plan rimuovendo la heatmap della matrice di transizione
  dai grafici previsti della Lezione 8 e aggiornando il riferimento alla lettura
  del grafo nella catena di rating.

### Aperture residue

- Verificare la coerenza puntuale tra la consegna dell'Esercizio B nelle slides
  e il testo dell'esercizio proposto 2 nel Capitolo 8.
- Verificare se nelle Guidelines restano ulteriori riferimenti testuali, oltre
  alla tabella delle 16 lezioni, da riallineare alla numerazione corrente.
- Compilare le slides con le figure definitive e verificare larghezze,
  leggibilità delle matrici, coerenza degli arrotondamenti e tempi degli
  esercizi.
- Non prevedere un take-home per la Lezione 8: le estensioni devono restare nel
  perimetro degli esercizi proposti del capitolo.

---

## Verifica 2026-08-23 - Lezione 9 e template IA

La Lezione 9 su catene di Markov e misure di rischio dispone del capitolo del
manuale e delle slides sviluppati. I due materiali coprono il passaggio dalle
transizioni di rating alla distribuzione di perdita, alle misure VaR e CVaR,
al CDS, alla copertura e al raccordo con la Lezione 10.

### Completato

- Completato `MQF_Cap_09_Markov_Misure_Rischio.tex`, con obiettivi, sezioni
  teoriche, applicazioni integrate e raccordo con la Lezione 10.
- Inseriti 3 esercizi svolti e 6 esercizi proposti, con sezioni etichettate
  `sec:cap09-esercizi-svolti` e `sec:cap09-esercizi-proposti`.
- Predisposte le slides `Slides_Lez_09_Catene_Markov_e_misure_di_rischio.tex`,
  con 41 pagine complessive, due esercizi in aula e materiale di back-up.
- Prodotti e collegati i grafici `Cap09_*` sulla funzione di ripartizione,
  distribuzioni di perdita, VaR/CVaR, term structure di default, posizione
  coperta e tranche creditizia.
- Verificata in data 2026-08-23 la compilazione autonoma delle slides: il PDF viene
  generato senza errori bloccanti e tutte le figure referenziate sono presenti.
- Aggiornati `MQF_Istruzioni_Studente_Uso_Virtuoso_IA_Casi_Applicativi.md` e
  `MQF_Template_Prompt_1.md`: il Prompt 1 è separato in parte variabile
  Scheda Caso e parte fissa, acquisisce la Scheda Caso come specifica
  vincolante e produce la cella Markdown iniziale del notebook.

### Aperture residue

- Tarare localmente alcune formule e tabelle del Capitolo 9 e quattro frame
  delle slides che producono overfull, senza compromettere la generazione dei
  PDF.
- Riallineare i template IA: il Prompt 3 è indicato come `Regime A/B` mentre le
  Istruzioni Studente lo prescrivono in Regime A; il template di tappa in
  Regime A vieta il codice ma ammette una cella Python eventuale.

---

## Verifica 2026-08-23 - Lezioni applicative 7 e 10

La Lezione 7 dispone di schede di costruzione e Schede Caso per aula e
take-home, oltre a cinque notebook di prova o soluzione studente. La struttura
dei casi copre gli obiettivi del Master Plan: simulazione con fattori correlati,
pricing Monte Carlo, errore di stima, controlli e interpretazione. Il capitolo
del manuale resta però un placeholder e non esistono slides.

L'ispezione tecnica dei notebook mostra tre notebook eseguiti con output e
senza errori memorizzati, un notebook con un errore memorizzato e un notebook
costituito da una sola cella Markdown. Per questo il materiale operativo e la
componente Python sono classificati `parziale`, non `sviluppato`.

La Lezione 10 dispone di Schede Caso e schede di costruzione per aula e
take-home, coerenti con simulazione di migrazioni creditizie, rischio sistemico
comune, perdite di portafoglio, VaR e CVaR. Mancano ancora notebook o script,
tracciati IA e output grafici. Il capitolo del manuale è inoltre un placeholder
con il titolo storico non più coerente `Pricing di opzioni e obbligazioni`.
Pertanto i materiali operativi sono `parziale`, mentre manuale e Python non
superano rispettivamente `traccia` e `-`.

---

## Verifica 2026-08-23 - Lezioni 11 e 12

Le Lezioni 11 e 12 sono passate da traccia a contenuto sostanziale. Il blocco
copre formulazione e geometria della programmazione lineare, dualità,
complementarietà e prezzi ombra, quindi estende il caso SVB ai cash flow
temporali, ai bilanci di liquidità, alle giacenze, al funding e all'ALM
deterministico. L'architettura è coerente con Master Plan e Guidelines: la
dualità è introdotta nella Lezione 11 e consolidata nella Lezione 12, che non è
più dedicata alla Goal Programming.

### Completato

- Inclusi nel master e sviluppati i Capitoli 11 e 12, con obiettivi espliciti,
  casi guida, limiti dei modelli, sintesi e sezioni di esercizi etichettate.
- Il Capitolo 11 contiene 4 esercizi svolti e 6 proposti; il Capitolo 12
  contiene 3 esercizi svolti e 5 proposti.
- Predisposte slides coerenti con la selezione didattica dei capitoli: 40
  pagine per la Lezione 11 e 47 per la Lezione 12, con esercizi in aula e
  materiale di back-up nella Lezione 12.
- Prodotti e collegati grafici dedicati `Cap11_*` e `Cap12_*`; gli script
  sorgente delle figure sono archiviati in `04_Codice/Lez11/` e
  `04_Codice/Lez12/`.
- Verificata in data 2026-08-23 la compilazione autonoma di entrambi i deck: i PDF
  vengono generati senza errori bloccanti. La compilazione temporanea del
  manuale completo genera un PDF di 547 pagine e include entrambi i capitoli.

### Aperture residue

- Archiviare il codice `scipy.optimize.linprog(method="highs")` usato per la
  validazione numerica dei casi LP e ALM: nel repository sono presenti gli
  script grafici, ma non uno script solver riproducibile, richiesto dalle
  Guidelines.
- Chiudere gli overfull locali delle slides e del manuale. La compilazione del
  manuale in directory temporanea lascia inoltre riferimenti del Capitolo 12
  non risolti pur trovando le relative label nel file ausiliario; serve una
  compilazione finale nel workflow ordinario del progetto.
- Correggere il magic comment della Lezione 12, che usa
  `Slides_Lez_12_Dualita_ALM_Deterministico.tex` mentre il nome su disco usa
  `Slides_Lez_12_Dualita_alm_deterministico.tex`.

---

## Conformità degli esercizi nei capitoli teorici sviluppati

Lo standard di riferimento è definito nella Sezione 9.1.1 delle Guidelines; il modello operativo è collegato dal Catalogo dei template.

| Capitolo | Esercizi svolti | Esercizi proposti | Stato strutturale | Intervento residuo |
|---:|---:|---:|---|---|
| 1 | 2 | 3 | sezioni presenti e soluzioni uniformate | aggiungere etichette alle due sezioni |
| 2 | 4 | 10 | conforme nella struttura e nelle etichette | nessun intervento urgente |
| 3 | 4 | 8 | sezioni presenti e soluzioni uniformate | aggiungere etichette alle due sezioni |
| 5 | 4 | 6 | modello editoriale di riferimento | anteporre `cap5-` alle etichette storiche |
| 6 | 5 | 0 | esercizi svolti uniformati | aggiungere gli esercizi proposti e le etichette di sezione |
| 8 | 0 | 4 | esercizi proposti presenti e utilizzati come base per le slides | verificare allineamento puntuale tra consegne del capitolo e formulazione nelle slides |
| 9 | 3 | 6 | sezioni esercizi presenti e label coerenti | taratura tipografica locale di formule e tabelle |
| 11 | 4 | 6 | sezioni esercizi presenti, label coerenti e raccordo con il caso SVB | archiviare il codice solver di validazione e completare la taratura tipografica |
| 12 | 3 | 5 | sezioni esercizi presenti, label coerenti e raccordo con il caso ALM | archiviare il codice solver e chiudere warning e riferimenti della compilazione finale |

Il Capitolo 4 è applicativo e segue la struttura laboratoriale prevista dalle Guidelines; non rientra nel conteggio degli esercizi teorici.

---

## Stato delle componenti trasversali

| Componente | Stato | Nota operativa |
|---|:---:|---|
| Architettura documentale | consolidata | Master Plan, Guidelines, Stato di avanzamento e Registro decisionale hanno funzioni distinte e non sovrapposte. |
| Standard degli esercizi | consolidato | La struttura editoriale è definita nelle Guidelines e resa operativa dal template LaTeX; resta da completarne l'applicazione ai capitoli indicati sopra. |
| Sistema dei template | parziale | I template sono organizzati per formato nativo e censiti nel catalogo centrale; Prompt 1 e Prompt 2 separano parte variabile e parte fissa, ma restano incongruenze operative fra Prompt 3, prompt di tappa e Istruzioni Studente. |
| Compatibilità Scientific WorkPlace 5.5 | in verifica | Si mantiene un'impostazione LaTeX conservativa; le tabelle vengono gestite singolarmente con l'ambiente `tabular`. |
| Nomenclatura di file, figure ed etichette | parziale | La convenzione aggiornata è applicata ai nuovi materiali; alcuni elementi storici richiedono ancora riallineamento. |

---

## Questioni operative aperte

1. Completare gli esercizi proposti del Capitolo 6 secondo il nuovo standard.
2. Uniformare le etichette di sezione: nei Capitoli 1 e 3 mancano o non sono
   uniformi le label degli esercizi; nel Capitolo 6 vanno aggiunte insieme agli
   esercizi proposti; nel Capitolo 5 le label storiche vanno prefissate con
   `cap5-`.
3. Gestire singolarmente le tabelle che producono righe fuori margine, mantenendo l'ambiente standard `tabular` per la compatibilità con Scientific WorkPlace 5.5.
4. Predisporre le slides della Lezione 4.
5. Completare il pacchetto della Lezione 7: notebook canonico docente/studente, tracciati IA, rimozione dell'errore memorizzato e sostituzione del notebook take-home ancora vuoto.
6. Completare il pacchetto della Lezione 10: capitolo coerente con il titolo corrente, notebook o script, tracciati IA, output numerici e grafici.
7. Chiudere le aperture residue della Lezione 8: confronto esercizio B, verifica Guidelines e compilazione slides.
8. Tarare gli overfull delle Lezioni 9, 11 e 12 e completare la compilazione finale del manuale; correggere anche il magic comment delle slides della Lezione 12.
9. Archiviare uno script solver riproducibile per la validazione numerica dei casi delle Lezioni 11-12, coerente con `scipy.optimize.linprog(method="highs")`.
10. Riallineare Prompt 3 e prompt di tappa alle Istruzioni Studente e alle Guidelines, eliminando le incongruenze su Regime A/B e produzione di codice in Regime A.
11. Predisporre il caso e il pacchetto applicativo della Lezione 13 utilizzando il solver già stabilito nelle Guidelines e raccordandolo al modello ALM della Lezione 12.
12. Verificare la notazione nello sviluppo delle Lezioni 7, 10 e 13 e aggiornare la corrispondenza Python quando i relativi script saranno definitivi.
13. Riallineare progressivamente i nomi dei file ancora non conformi alla nomenclatura definitiva del Master Plan.

---

## Regola di aggiornamento

Aggiornare questo file quando cambia lo stato effettivo di una lezione o di uno dei suoi prodotti. Non trasferire gli indicatori di avanzamento nel Master Plan o nelle Guidelines.

Quando una questione produce una scelta progettuale stabile, registrare la decisione e la motivazione nel Registro decisionale; in questo file deve restare soltanto il suo eventuale stato di attuazione.
