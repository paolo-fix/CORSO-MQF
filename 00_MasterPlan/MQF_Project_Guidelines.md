# Metodi Quantitativi per la Finanza — Linee guida di progetto

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

La struttura standard di un capitolo con applicazione Python e':

1. obiettivi della lezione;
2. motivazione finanziaria;
3. formulazione matematica del problema computazionale;
4. descrizione dell'algoritmo;
5. codice Python commentato;
6. output numerici;
7. grafici;
8. interpretazione economico-finanziaria dei risultati;
9. esercizi di modifica del codice;
10. sintesi finale.

Le dimostrazioni devono essere selettive. Devono essere incluse quando rafforzano la comprensione dei meccanismi quantitativi, ma non devono trasformare il corso in un corso astratto di probabilita' o ottimizzazione.

## 10. Slides delle lezioni

Le slides devono essere uno strumento di lezione, non una versione compressa del manuale.

Per ogni lezione teorica, la struttura orientativa e':

1. motivazione e obiettivi;
2. concetti teorici essenziali;
3. esempi numerici guidati;
4. grafici esplicativi;
5. esercizi da svolgere in aula;
6. sintesi conclusiva.

Per ogni lezione Python, la struttura orientativa e':

1. problema finanziario o quantitativo;
2. formulazione matematica;
3. schema algoritmico;
4. blocchi essenziali di codice;
5. output numerici;
6. grafici;
7. interpretazione dei risultati;
8. esercizi di modifica del codice.

Le slides devono essere concise, visivamente ordinate e orientate alla discussione in aula. Le formule devono essere presenti, ma non in quantita' tale da rendere le slides equivalenti a pagine di manuale.

## 11. Notazione matematica

La notazione matematica deve essere coerente in tutto il progetto. Il riferimento principale e' il file:

```text
MQF_Notazione.tex
```

Le convenzioni generali includono:

- `(Omega, F, P)` per lo spazio di probabilita';
- `X, Y, Z` per variabili casuali;
- `E[X]`, `Var(X)`, `Cov(X,Y)` per valore atteso, varianza e covarianza;
- `F_t` per la filtrazione in tempo discreto;
- `S_t` per il prezzo di un'attivita' finanziaria al tempo `t`;
- `r` per il tasso privo di rischio su un periodo;
- `Q` per la misura risk-neutral, quando introdotta;
- `x` per variabili decisionali;
- `xi` o `s` per incertezza, scenari o stati, a seconda del contesto.

Nel materiale LaTeX questi simboli devono essere scritti con la notazione matematica corretta, ad esempio `\Omega`, `\mathcal{F}`, `\mathbb{P}`, `\mathbb{E}`, `\mathbb{Q}`, `\mathcal{F}_t`.

Salvo diversa indicazione, il corso lavora prevalentemente in tempo discreto:

```text
t = 0, 1, ..., T.
```

Ogni nuova notazione introdotta in un capitolo deve essere registrata o verificata rispetto a `MQF_Notazione.tex`.

## 12. Esercizi in aula

Ogni lezione teorica deve includere almeno due esercizi in aula:

1. un esercizio di calcolo, derivazione o formulazione;
2. un esercizio di interpretazione finanziaria.

Quando utile, va aggiunto un esercizio grafico.

Le lezioni Python devono includere almeno:

1. un esercizio di modifica del codice;
2. un esercizio di interpretazione dell'output;
3. un eventuale esercizio di sensibilita' rispetto ai parametri.

Gli esercizi devono essere coerenti con il livello degli studenti. Devono essere sufficientemente tecnici da consolidare il metodo, ma non cosi' lunghi da diventare mini-progetti separati durante la lezione.

## 13. Grafici didattici

I grafici sono parte integrante del progetto. Devono essere usati per spiegare concetti, non solo per illustrare risultati.

Grafici ricorrenti previsti:

1. diagrammi di Venn e alberi probabilistici;
2. funzioni di massa, densita' e ripartizione;
3. quantili e code di distribuzione;
4. alberi informativi;
5. traiettorie simulate di processi stocastici;
6. ventagli di scenari;
7. grafi di catene di Markov;
8. heatmap di matrici di transizione;
9. distribuzioni di perdita con VaR e CVaR;
10. alberi binomiali dei prezzi e dei payoff;
11. regioni ammissibili di problemi di programmazione lineare;
12. rette di livello e interpretazione geometrica dell'ottimo;
13. diagrammi primal-dual e prezzi ombra;
14. alberi degli scenari nella programmazione stocastica;
15. confronti tra soluzioni SP, EV e WS;
16. visualizzazioni di EVPI e VSS.

Per compatibilita' tecnica, i grafici possono essere generati in Python e inclusi come immagini nei documenti LaTeX. L'uso di grafici direttamente in LaTeX deve essere valutato caso per caso.

## 14. Applicazioni Python

Sono previste cinque applicazioni Python:

| Applicazione | Lezione | Tema | Output computazionale |
|---:|---:|---|---|
| 1 | 5 | Processi stocastici e valori attesi condizionati | Simulazioni, stime condizionate, grafici di traiettorie |
| 2 | 8 | Rischio di credito | Matrici di transizione, default probability, VaR, CVaR |
| 3 | 10 | Pricing di opzioni e obbligazioni | Alberi binomiali, backward induction, sensibilita' |
| 4 | 13 | Programmazione lineare e CVaR | Formulazione PL, soluzione numerica, confronto VaR-CVaR |
| 5 | 16 | Programmazione stocastica | Scenari, recourse, EVPI, VSS |

Criteri comuni per il codice Python:

1. codice ben commentato;
2. separazione tra dati, parametri, funzioni e output;
3. nomi delle variabili coerenti con la notazione matematica;
4. uso di grafici leggibili;
5. interpretazione dei risultati dopo ogni blocco computazionale;
6. esercizi di modifica del codice;
7. preferenza per codice didatticamente trasparente rispetto a codice eccessivamente compatto.

Quando si scrive codice Python, occorre privilegiare chiarezza, replicabilita' e tracciabilita' del passaggio dalla formula matematica all'algoritmo.

## 15. Stato di avanzamento da mantenere aggiornato

Il progetto deve mantenere un registro di avanzamento per aree:

| Area | Stato iniziale | Nota |
|---|---|---|
| Struttura delle 16 lezioni | Bozza consolidata | Derivata dal syllabus e uniformata nei titoli |
| Notazione generale | Documento iniziale creato | Da aggiornare durante lo sviluppo |
| Manuale | Non iniziato | Da scrivere capitolo per capitolo |
| Slides | Non iniziate | Da produrre dopo lo schema dettagliato di ciascuna lezione |
| Esercizi teorici | Bozza iniziale | Da sviluppare lezione per lezione |
| Applicazioni Python | Bozza iniziale | Cinque applicazioni previste |
| Grafici | Bozza iniziale | Da validare e produrre progressivamente |
| Compatibilita' SWP 5.5 | Da verificare | Evitare pacchetti LaTeX moderni non necessari |

Ogni volta che una lezione viene sviluppata, occorre aggiornare il master plan o il registro decisionale con:

1. titolo definitivo;
2. obiettivi didattici;
3. notazione introdotta;
4. formule principali;
5. esercizi prodotti;
6. grafici previsti o prodotti;
7. collegamenti Python;
8. questioni aperte.

## 16. Metodo di lavoro nelle future chat ChatGPT

Per evitare chat eccessivamente lunghe, il progetto deve essere sviluppato in modo modulare.

Questa linea guida deve essere usata come contesto iniziale nelle nuove chat. Ogni nuova chat dovrebbe essere dedicata a un compito specifico, ad esempio:

- Lezione 1 — Manuale;
- Lezione 1 — Slides;
- Lezione 1 — Esercizi;
- Applicazione Python 1;
- Registro dei grafici;
- Revisione della notazione;
- Template del manuale;
- Template delle slides.

All'inizio di ogni nuova chat, e' consigliabile incollare o allegare:

1. questo file `MQF_Project_Guidelines.md`;
2. il file `MQF_Master_Plan.tex`, se rilevante;
3. il file `MQF_Notazione.tex`, se la chat riguarda contenuti matematici;
4. eventuali file gia' prodotti per la lezione specifica.

La richiesta iniziale nelle nuove chat dovrebbe indicare chiaramente:

1. quale lezione o materiale si intende sviluppare;
2. se il prodotto richiesto e' manuale, slides, esercizi, codice Python o revisione;
3. il livello di dettaglio atteso;
4. eventuali vincoli aggiuntivi.

## 17. Prompt operativo consigliato per nuove chat

Il seguente testo puo' essere usato come prompt iniziale nelle future chat.

```text
Sto sviluppando il corso universitario "Metodi Quantitativi per la Finanza".
Il corso e' destinato a studenti del quinto anno di Banca e Risk Management.
Gli studenti hanno livello medio di metodi quantitativi e statistici, e buon livello di teoria finanziaria.
Il materiale deve essere in italiano, con registro accademico e tecnico.
Il manuale e le slides devono essere scritti in LaTeX compatibile con Scientific Workplace 5.5.
La notazione matematica deve essere coerente con il file MQF_Notazione.tex.
Il progetto segue le linee guida del file MQF_Project_Guidelines.md e il piano del file MQF_Master_Plan.tex.

In questa chat lavoriamo su:
[INDICARE QUI: Lezione X / Manuale / Slides / Esercizi / Python / Revisione].

Obiettivo della chat:
[DESCRIVERE IL RISULTATO ATTESO].
```

## 18. Criteri di qualita'

Ogni output prodotto nel progetto deve essere verificato rispetto ai seguenti criteri:

1. coerenza con l'architettura generale del corso;
2. coerenza con la notazione stabilita;
3. compatibilita' con Scientific Workplace 5.5 quando il materiale e' in LaTeX;
4. chiarezza della motivazione finanziaria;
5. correttezza matematica;
6. presenza di esempi o esercizi adeguati;
7. uso ragionato dei grafici;
8. continuita' con le lezioni precedenti e successive;
9. distinzione chiara tra teoria, applicazione e interpretazione;
10. utilita' didattica per studenti del quinto anno.

## 19. Questioni aperte

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
