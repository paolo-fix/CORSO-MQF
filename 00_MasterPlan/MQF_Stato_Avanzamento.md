# MQF - Stato di avanzamento

## Funzione del documento

Questo file è l'unica fonte per lo stato corrente del progetto. Registra ciò che è stato realizzato, ciò che è in lavorazione, le prossime priorità e le questioni operative aperte.

Il Master Plan definisce l'architettura didattica e i contenuti previsti. Le Guidelines definiscono le regole stabili. Il Registro decisionale conserva le decisioni progettuali e le relative motivazioni.

## Snapshot al 2026-07-24

|  |  |
|---|---|
| **Ultima attività completata** | Completamento del Capitolo 9 su catene di Markov e misure di rischio, con esercizi, grafici dedicati e raccordo con la Lezione 10; aggiornamento delle Istruzioni Studente e del template Prompt 1. |
| **Materiale sviluppato** | Capitoli 1-6, 8 e 9 del manuale; slides delle Lezioni 1, 2, 3, 5, 6 e 8; pacchetto applicativo della Lezione 4; grafici collegati ai Capitoli 1-6, 8 e 9; Istruzioni Studente e template Prompt 1 aggiornati. |
| **Lavoro in corso** | Predisposizione delle slides della Lezione 9; chiusura delle aperture residue della Lezione 8; completamento dell'adeguamento dei capitoli già sviluppati allo standard degli esercizi. |
| **Prossima priorità** | Predisporre le slides della Lezione 9 e completare gli esercizi proposti del Capitolo 6. |

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
| 7 | C | Traiettorie, simulazione e pricing | traccia | - | - | - | - |
| 8 | P | Catene di Markov | sviluppato | sviluppato | sviluppato | sviluppato | n.a. |
| 9 | P | Markov e misure di rischio | sviluppato | - | sviluppato | sviluppato | n.a. |
| 10 | C | Python: rischio di credito | traccia | - | - | - | - |
| 11 | P | Programmazione lineare | traccia | - | - | - | n.a. |
| 12 | P | Goal Programming | traccia | - | - | - | n.a. |
| 13 | C | Python: Asset Allocation e ALM | traccia | - | - | - | - |
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

## Aggiornamento 2026-07-24 - Lezione 9 e Prompt 1

La Lezione 9 su catene di Markov e misure di rischio dispone ora del capitolo
del manuale sviluppato. Il capitolo è incluso nel master del manuale e copre il
passaggio dalle transizioni di rating alla costruzione della distribuzione di
perdita, alle misure VaR e CVaR, al CDS, alla copertura, al portafoglio e ai
limiti del modello.

### Completato

- Completato `MQF_Cap_09_Markov_Misure_Rischio.tex`, con obiettivi, sezioni
  teoriche, applicazioni integrate e raccordo con la Lezione 10.
- Inseriti 3 esercizi svolti e 6 esercizi proposti, con sezioni etichettate
  `sec:cap09-esercizi-svolti` e `sec:cap09-esercizi-proposti`.
- Prodotti e collegati i grafici `Cap09_*` sulla funzione di ripartizione,
  distribuzioni di perdita, VaR/CVaR, term structure di default, posizione
  coperta e tranche creditizia.
- Verificata la compilazione del manuale dopo correzione dei percorsi di due
  figure del Capitolo 9; il PDF viene generato senza errori bloccanti.
- Aggiornati `MQF_Istruzioni_Studente_Uso_Virtuoso_IA_Casi_Applicativi.md` e
  `MQF_Template_Prompt_1.md`: il Prompt 1 è separato in parte variabile
  Scheda Caso e parte fissa, acquisisce la Scheda Caso come specifica
  vincolante e produce la cella Markdown iniziale del notebook.

### Aperture residue

- Predisporre le slides della Lezione 9 a partire dal capitolo sviluppato.
- Tarare localmente alcune formule e tabelle del Capitolo 9 che producono
  overfull in compilazione, senza compromettere la generazione del PDF.
- Verificare l'allineamento progressivo dei template Prompt 2, Prompt 3 e
  prompt di tappa alla distinzione fra parte variabile dello studente e parte
  fissa per l'IA.

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

Il Capitolo 4 è applicativo e segue la struttura laboratoriale prevista dalle Guidelines; non rientra nel conteggio degli esercizi teorici.

---

## Stato delle componenti trasversali

| Componente | Stato | Nota operativa |
|---|:---:|---|
| Architettura documentale | consolidata | Master Plan, Guidelines, Stato di avanzamento e Registro decisionale hanno funzioni distinte e non sovrapposte. |
| Standard degli esercizi | consolidato | La struttura editoriale è definita nelle Guidelines e resa operativa dal template LaTeX; resta da completarne l'applicazione ai capitoli indicati sopra. |
| Sistema dei template | consolidato | I template sono organizzati per formato nativo e censiti nel catalogo centrale; Prompt 1 è aggiornato alla separazione tra Scheda Caso e istruzioni fisse per l'IA. |
| Compatibilità Scientific WorkPlace 5.5 | in verifica | Si mantiene un'impostazione LaTeX conservativa; le tabelle vengono gestite singolarmente con l'ambiente `tabular`. |
| Nomenclatura di file, figure ed etichette | parziale | La convenzione aggiornata è applicata ai nuovi materiali; alcuni elementi storici richiedono ancora riallineamento. |

---

## Questioni operative aperte

1. Completare gli esercizi proposti del Capitolo 6 secondo il nuovo standard.
2. Aggiungere etichette coerenti (\label{...}) di sezione. **Capitoli 1 e 3**
Hanno le sezioni esercizi, ma manca o non è uniforme la label delle sezioni. 
**Capitolo 6**
Ha esercizi svolti, ma va completato con esercizi proposti e relative etichette.
**Capitolo 5**
Ha già una struttura più completa, ma alcune etichette sono “storiche”, cioè nate prima della convenzione attuale. Per esempio potrebbero essere troppo generiche o non prefissate con cap5-.
3. Gestire singolarmente le tabelle che producono righe fuori margine, mantenendo l'ambiente standard `tabular` per la compatibilità con Scientific WorkPlace 5.5.
4. Predisporre le slides della Lezione 4.
5. Predisporre le slides della Lezione 9 a partire dal capitolo sviluppato.
6. Chiudere le aperture residue della Lezione 8: confronto esercizio B, verifica Guidelines e compilazione slides.
7. Verificare e integrare la notazione relativa a tempo continuo, SDE, processi OU/CIR, correlazione e Goal Programming.
8. Verificare l'allineamento dei template Prompt 2, Prompt 3 e prompt di tappa alla distinzione tra parte variabile dello studente e parte fissa per l'IA.
9. Definire il livello di integrazione tra simulazione di GBM/OU/processi correlati, pricing di opzioni asiatiche e sistema OU-CIR nella Lezione 7.
10. Stabilire il caso applicativo della Lezione 13 e le librerie di ottimizzazione da utilizzare nelle Lezioni 13 e 16.
11. Riallineare progressivamente i nomi dei file ancora non conformi alla nomenclatura definitiva del Master Plan.
12. Le istruzioni studente uso virtuoso IA casi applicativi vanno integrate nelle guideline.
13. Eliminare incoerenza di informazioni tra template dei prompt zero, 1, 2 e 3 e di regime e scheda costruzione caso applicativo (aula e take-home) da una parte e guideline dall'altra

---

## Regola di aggiornamento

Aggiornare questo file quando cambia lo stato effettivo di una lezione o di uno dei suoi prodotti. Non trasferire gli indicatori di avanzamento nel Master Plan o nelle Guidelines.

Quando una questione produce una scelta progettuale stabile, registrare la decisione e la motivazione nel Registro decisionale; in questo file deve restare soltanto il suo eventuale stato di attuazione.
