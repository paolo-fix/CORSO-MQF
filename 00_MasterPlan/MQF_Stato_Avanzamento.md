# MQF - Stato di avanzamento

## Funzione del documento

Questo file è l'unica fonte per lo stato corrente del progetto. Registra ciò che è stato realizzato, ciò che è in lavorazione, le prossime priorità e le questioni operative aperte.

Il Master Plan definisce l'architettura didattica e i contenuti previsti. Le Guidelines definiscono le regole stabili. Il Registro decisionale conserva le decisioni progettuali e le relative motivazioni.

## Snapshot al 2026-07-15

|  |  |
|---|---|
| **Ultima attività completata** | Consolidamento dell'architettura dei template per formato nativo, con catalogo centrale, modelli LaTeX e Markdown e separazione tra regole normative, testi operativi e stato di attuazione. |
| **Materiale sviluppato** | Capitoli 1-6 del manuale; slides delle Lezioni 1, 2, 3 e 5; pacchetto applicativo della Lezione 4; grafici collegati ai Capitoli 1-6. |
| **Lavoro in corso** | Completamento dell'adeguamento dei capitoli già sviluppati al nuovo standard degli esercizi e verifica puntuale della compatibilità con Scientific WorkPlace 5.5. |
| **Prossima priorità** | Completare gli esercizi proposti del Capitolo 6 e normalizzare le etichette delle sezioni degli esercizi nei capitoli storici. |

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
| 6 | P | Processi stocastici in tempo continuo | sviluppato | - | parziale | sviluppato | n.a. |
| 7 | C | Traiettorie, simulazione e pricing | traccia | - | - | - | - |
| 8 | P | Catene di Markov | traccia | - | - | - | n.a. |
| 9 | P | Markov e misure di rischio | traccia | - | - | - | n.a. |
| 10 | C | Python: rischio di credito | traccia | - | - | - | - |
| 11 | P | Programmazione lineare | traccia | - | - | - | n.a. |
| 12 | P | Goal Programming | traccia | - | - | - | n.a. |
| 13 | C | Python: Asset Allocation e ALM | traccia | - | - | - | - |
| 14 | P | Programmazione stocastica a due stadi | traccia | - | - | - | n.a. |
| 15 | P | Programmazione stocastica multistadio | traccia | - | - | - | n.a. |
| 16 | C | Python: programmazione stocastica | traccia | - | - | - | - |

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

Il Capitolo 4 è applicativo e segue la struttura laboratoriale prevista dalle Guidelines; non rientra nel conteggio degli esercizi teorici.

---

## Stato delle componenti trasversali

| Componente | Stato | Nota operativa |
|---|:---:|---|
| Architettura documentale | consolidata | Master Plan, Guidelines, Stato di avanzamento e Registro decisionale hanno funzioni distinte e non sovrapposte. |
| Standard degli esercizi | consolidato | La struttura editoriale è definita nelle Guidelines e resa operativa dal template LaTeX; resta da completarne l'applicazione ai capitoli indicati sopra. |
| Sistema dei template | consolidato | I template sono organizzati per formato nativo e censiti nel catalogo centrale. |
| Compatibilità Scientific WorkPlace 5.5 | in verifica | Si mantiene un'impostazione LaTeX conservativa; le tabelle vengono gestite singolarmente con l'ambiente `tabular`. |
| Nomenclatura di file, figure ed etichette | parziale | La convenzione aggiornata è applicata ai nuovi materiali; alcuni elementi storici richiedono ancora riallineamento. |

---

## Questioni operative aperte

1. Completare gli esercizi proposti del Capitolo 6 secondo il nuovo standard.
2. Normalizzare le etichette di sezione nei Capitoli 1, 3 e 6 e le etichette storiche del Capitolo 5.
3. Gestire singolarmente le tabelle che producono righe fuori margine, mantenendo l'ambiente standard `tabular` per la compatibilità con Scientific WorkPlace 5.5.
4. Predisporre le slides delle Lezioni 4 e 6.
5. Verificare e integrare la notazione relativa a tempo continuo, SDE, processi OU/CIR, correlazione e Goal Programming.
6. Definire il livello di integrazione tra simulazione di GBM/OU/processi correlati, pricing di opzioni asiatiche e sistema OU-CIR nella Lezione 7.
7. Stabilire il caso applicativo della Lezione 13 e le librerie di ottimizzazione da utilizzare nelle Lezioni 13 e 16.
8. Riallineare progressivamente i nomi dei file ancora non conformi alla nomenclatura definitiva del Master Plan.

---

## Regola di aggiornamento

Aggiornare questo file quando cambia lo stato effettivo di una lezione o di uno dei suoi prodotti. Non trasferire gli indicatori di avanzamento nel Master Plan o nelle Guidelines.

Quando una questione produce una scelta progettuale stabile, registrare la decisione e la motivazione nel Registro decisionale; in questo file deve restare soltanto il suo eventuale stato di attuazione.
