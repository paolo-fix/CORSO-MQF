# MQF — Stato di Avanzamento

## Snapshot al 2026-06-13

|  |  |
|---|---|
| **Ultima cosa completata** | Revisione dell'architettura del corso a partire dalla Lezione 4: nuova applicazione Python iniziale, processi stocastici sdoppiati, rimozione dell'applicazione autonoma sugli alberi binomiali, introduzione del Goal Programming. |
| **Materiale didattico completato** | Cap. 01–03 del manuale; slides Lez. 01–03; esercizi e grafici collegati ai primi tre capitoli. |
| **Lavoro in corso** | Riallineamento dei documenti di coordinamento: Master Plan, Guidelines, Notazione, Stato Avanzamento, registri e nomi file. |
| **Prossima priorità** | Cap. 04 — Applicazione in Python: probabilità, variabili casuali e condizionamento. |

---

## Stato per lezione

Legenda: `✓` completato · `bozza` in lavorazione · `traccia` struttura presente, contenuto da scrivere · `—` non iniziato · `n.a.` non applicabile per questa lezione

| Lez. | Tipo | Titolo | Capitolo manuale | Slides | Esercizi | Grafici | Python/Notebook |
|---:|:---:|---|:---:|:---:|:---:|:---:|:---:|
| 1 | P | Elementi di probabilità | ✓ | ✓ | ✓ | ✓ | n.a. |
| 2 | P | Variabili casuali | ✓ | ✓ | ✓ | ✓ | n.a. |
| 3 | P | Valori attesi condizionati | ✓ | ✓ | ✓ | ✓ | n.a. |
| 4 | C | Applicazione in Python: probabilità, variabili casuali e condizionamento | traccia | — | — | — | traccia |
| 5 | P | Processi stocastici in tempo discreto | traccia | — | — | — | n.a. |
| 6 | P | Processi stocastici in tempo continuo | traccia | — | — | — | n.a. |
| 7 | C | Applicazione in Python: traiettorie, simulazione e pricing Monte Carlo | traccia | — | — | — | — |
| 8 | P | Catene di Markov | traccia | — | — | — | n.a. |
| 9 | P | Catene di Markov e misure di rischio | traccia | — | — | — | n.a. |
| 10 | C | Applicazione in Python: rischio di credito | traccia | — | — | — | — |
| 11 | P | Programmazione lineare | traccia | — | — | — | n.a. |
| 12 | P | Goal Programming | traccia | — | — | — | n.a. |
| 13 | C | Applicazione in Python: Asset Allocation e ALM | traccia | — | — | — | — |
| 14 | P | Programmazione stocastica a due stadi | traccia | — | — | — | n.a. |
| 15 | P | Programmazione stocastica multistadio | traccia | — | — | — | n.a. |
| 16 | C | Applicazione in Python: programmazione stocastica | traccia | — | — | — | — |

---

## Nomi file di riferimento

### Manuale

```text
/01_Manuale
  MQF_Manuale_Master.tex

  /Capitoli
    MQF_Cap_01_Probabilita.tex
    MQF_Cap_02_Variabili_Casuali.tex
    MQF_Cap_03_Valori_Attesi_Condizionati.tex
    MQF_Cap_04_Python_Probabilita_Condizionamento.tex
    MQF_Cap_05_Processi_Stocastici_Tempo_Discreto.tex
    MQF_Cap_06_Processi_Stocastici_Tempo_Continuo.tex
    MQF_Cap_07_Python_Traiettorie_Pricing.tex
    MQF_Cap_08_Catene_Markov.tex
    MQF_Cap_09_Markov_Misure_Rischio.tex
    MQF_Cap_10_Python_Rischio_Credito.tex
    MQF_Cap_11_Programmazione_Lineare.tex
    MQF_Cap_12_Goal_Programming.tex
    MQF_Cap_13_Python_Asset_Allocation_ALM.tex
    MQF_Cap_14_Programmazione_Stocastica_Due_Stadi.tex
    MQF_Cap_15_Programmazione_Stocastica_Multistadio.tex
    MQF_Cap_16_Python_Programmazione_Stocastica.tex
```

### Slides

```text
/02_Slides
  Slides_Lez_01_Elementi_probabilita.tex
  Slides_Lez_02_Variabili_Casuali.tex
  Slides_Lez_03_Valori_attesi_condizionati.tex
  Slides_Lez_04_Python_Probabilita_Condizionamento.tex
  Slides_Lez_05_Processi_Stocastici_Tempo_Discreto.tex
  Slides_Lez_06_Processi_Stocastici_Tempo_Continuo.tex
  Slides_Lez_07_Python_Traiettorie_Pricing.tex
  Slides_Lez_08_Catene_Markov.tex
  Slides_Lez_09_Markov_Misure_Rischio.tex
  Slides_Lez_10_Python_Rischio_Credito.tex
  Slides_Lez_11_Programmazione_Lineare.tex
  Slides_Lez_12_Goal_Programming.tex
  Slides_Lez_13_Python_Asset_Allocation_ALM.tex
  Slides_Lez_14_Programmazione_Stocastica_Due_Stadi.tex
  Slides_Lez_15_Programmazione_Stocastica_Multistadio.tex
  Slides_Lez_16_Python_Programmazione_Stocastica.tex
```

### Python

```text
/03_Python
  MQF_Python_01_Probabilita_Condizionamento.py
  MQF_Python_02_Traiettorie_Pricing.py
  MQF_Python_03_Rischio_Credito.py
  MQF_Python_04_Asset_Allocation_ALM.py
  MQF_Python_05_Programmazione_Stocastica.py
```

---

## Note sui grafici delle Lezioni 1–3

I grafici sono presenti nella cartella `01_Manuale/graphics/`.

Grafici disponibili verificati:

- Cap. 01: `Cap01_Eserc_a.png`;
- Cap. 02: `cap2_cdf_rendimento_discreto`, `cap2_densita_uniforme_rendimento_area_01_05`, `cap2_es3_densita_cdf_affiancati`, `cap2_es4_perdita_normale_quantile_coda`, `cap2_funzione_shortfall_zero`, `cap2_normale_coda_sinistra_quantile_05`, `cap2_probabilita_area_sotto_densita`;
- Cap. 03: `Figura_3_1`, `Figura_3_2`, `Figura_3_3`, `Figura_3_4`.

Nota: la convenzione `Cap0X_` è applicata sistematicamente dal Cap. 01 in poi solo in parte. I grafici del Cap. 02 e del Cap. 03 usano nomi descrittivi; occorre decidere se rinominarli o registrarli come eccezioni stabili nelle Guidelines.

---

## Questioni aperte operative

1. **Convenzione nomi grafici** — i grafici Cap. 02 e Cap. 03 non seguono integralmente la convenzione `Cap0X_`. Decidere se rinominarli o dichiarare l'eccezione nelle Guidelines.

2. **Template LaTeX manuale** — da consolidare prima della scrittura piena del Cap. 04. I Cap. 01--03 usano shell non del tutto omogenei; verificare se mantenere la differenza o stabilire un template unico.

3. **Riallineamento nomi file pubblicati** — verificare che i file effettivamente presenti sul sito coincidano con i nomi definitivi del nuovo piano, in particolare per Cap. 07, Cap. 14 e Cap. 15.

4. **File master LaTeX** — verificare che `MQF_Manuale_Master.tex` e gli eventuali file master delle slides includano i nuovi nomi dei capitoli e delle lezioni.

5. **Notazione** — verificare, nello sviluppo dei Capitoli 5--7 e 12--13, la coerenza delle nuove notazioni per martingale, GBM, OU, CIR, correlazione, Eulero--Maruyama e Goal Programming.

6. **Librerie Python ammesse** — da decidere prima della scrittura definitiva del notebook della Lezione 4. Per la prima applicazione è plausibile limitarsi a `numpy`, `pandas` e `matplotlib`; le librerie di ottimizzazione saranno valutate per le applicazioni successive.

7. **Formato applicazioni Python** — il notebook Jupyter è confermato come formato principale delle lezioni applicative. Resta da decidere se esportare sistematicamente anche script `.py`.

8. **Dataset e simulazioni** — per la Lezione 4 si adotta una simulazione controllata con parametri stilizzati. Non è previsto l'uso di dati reali nella prima versione del caso aula.

9. **Pacchetto materiali applicativi** — dopo la prima implementazione completa della Lezione 4 occorre verificare se la lista dei materiali previsti per ogni applicazione sia troppo ampia e quali elementi possano essere accorpati.

10. **Prompt virtuosi** — la procedura distingue prompt zero, prompt breve di tappa e prompt autosufficiente. Dopo la Lezione 4 occorre valutare se questa distinzione debba essere mantenuta integralmente anche nelle successive applicazioni Python.

11. **Tracciato IA studenti** — resta da calibrare il numero minimo e massimo di prompt ammessi per il take-home della Lezione 4.

12. **Rubrica di valutazione** — la struttura generale è stata definita nelle Guidelines; resta da costruire la rubrica specifica per il take-home della Lezione 4.

13. **Lezione 7** — definire il livello di integrazione tra simulazione di GBM/OU/processi correlati, pricing di opzioni asiatiche e sistema OU--CIR per obbligazioni indicizzate all'inflazione.

14. **Goal Programming e ALM** — stabilire il caso applicativo specifico della Lezione 13: asset allocation multicriterio pura, liability matching, oppure formulazione integrata di Asset Liability Management.

15. **Programmazione stocastica** — precisare se la Lezione 16 userà un caso semplificato di asset allocation multistadio o un modello più ricco con vincoli di portafoglio e passività.

16. **Rimozione residui vecchia architettura** — verificare che non restino riferimenti alla vecchia applicazione autonoma sugli alberi binomiali, alla dualità LP come lezione autonoma o alla CVaR via PL come applicazione principale della Lezione 13.
