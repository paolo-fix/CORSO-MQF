# Metodi Quantitativi per la Finanza - Linee guida di progetto

## 1. Identificazione del progetto

Il progetto riguarda la predisposizione completa del materiale didattico per il corso universitario **Metodi Quantitativi per la Finanza**.
Il corso e' destinato a studenti del quinto anno del corso di laurea in **Banca e Risk Management**. Gli studenti hanno una preparazione mediamente solida nei metodi quantitativi e statistici, e una preparazione buona nella teoria finanziaria e nei modelli finanziari.
Il materiale deve quindi mantenere un livello accademico rigoroso, evitando sia un approccio eccessivamente divulgativo sia un formalismo astratto non motivato dalle applicazioni finanziarie.

Il corso deve essere sviluppato in italiano. Il manuale, le slides e i materiali matematici devono essere scritti in LaTeX compatibile con **Scientific WorkPlace 5.5**.
Questo documento, invece, e' scritto in Markdown per essere caricato su GitHub e usato come linea guida operativa nelle future chat dedicate allo sviluppo del progetto.

## 2. Funzione e formato delle guidelines

Queste guidelines hanno una funzione di coordinamento: definiscono l'impostazione didattica, i prodotti finali, i vincoli tecnici e le regole operative da rispettare nella produzione del materiale del corso.

Il formato piu' idoneo per questo documento e' **Markdown**, con estensione `.md`, perche':

1. e' nativamente leggibile su GitHub;
2. e' facilmente versionabile con Git;
3. e' leggibile anche come semplice file di testo;
4. puo' essere copiato integralmente o parzialmente nelle nuove chat di lavoro;
5. mantiene una struttura gerarchica chiara mediante titoli, elenchi e sezioni;
6. evita la complessita' sintattica del LaTeX quando lo scopo non e' la compilazione tipografica, ma il coordinamento del progetto.

Il nome del file e':

```text
MQF_Project_Guidelines.md
```

Il file e' collocato nella cartella:

```text
00_MasterPlan/MQF_Project_Guidelines.md
```

## 3. Finalita' generale del corso

Il corso deve fornire agli studenti strumenti quantitativi per rappresentare l'incertezza, modellizzare fenomeni finanziari discreti e continui, misurare il rischio e formulare problemi decisionali in presenza di vincoli, scenari e obiettivi multipli.

La finalita' generale non e' presentare una raccolta eterogenea di tecniche matematiche, ma costruire un percorso unitario centrato su tre assi concettuali:

1. modellizzazione probabilistica dell'incertezza;
2. processi stocastici, informazione e simulazione;
3. decisione quantitativa sotto rischio, sotto incertezza e in presenza di obiettivi multipli.

Ogni lezione deve contribuire esplicitamente a uno o piu' di questi assi. Le connessioni tra probabilita', variabili casuali, valori attesi condizionati, processi stocastici, catene di Markov, misure di rischio, programmazione lineare, goal programming e programmazione stocastica devono essere rese chiare e ricorrenti.

Il corso deve mantenere un equilibrio tra formalizzazione matematica, interpretazione finanziaria e implementazione computazionale. Le lezioni applicative in Python non devono essere considerate appendici tecniche, ma momenti di consolidamento operativo dei concetti introdotti nelle lezioni teoriche.

## 4. Architettura concettuale del corso

Il corso deve seguire una progressione logica fondata sui seguenti passaggi concettuali:

1. rappresentazione probabilistica dell'incertezza;
2. variabili casuali, distribuzioni e momenti;
3. informazione e valore atteso condizionato;
4. consolidamento computazionale in Python dei concetti probabilistici;
5. processi stocastici in tempo discreto, filtrazioni e martingale;
6. processi stocastici in tempo continuo, diffusioni e simulazione;
7. catene di Markov e rischio di credito;
8. misure di rischio in contesto markoviano;
9. programmazione lineare, con dualita' come contenuto essenziale;
10. goal programming e decisioni multicriterio;
11. asset allocation multicriterio e asset liability management;
12. programmazione stocastica e decisioni adattate agli scenari.

Questa progressione deve orientare la scrittura del manuale, delle slides, degli esercizi e delle applicazioni Python. In particolare, le lezioni iniziali di probabilita' non devono essere presentate come un richiamo isolato, ma come la base necessaria per i modelli finanziari successivi.

Il modello binomiale non costituisce piu' una lezione applicativa autonoma di pricing. Deve essere utilizzato, quando utile, come esempio strutturale di processo in tempo discreto, filtrazione, adattabilita' e martingala.

La dualita' nella programmazione lineare non scompare dal corso, ma viene ricondotta alla lezione introduttiva di programmazione lineare come contenuto essenziale per l'interpretazione economica dei vincoli e dei prezzi ombra. Non costituisce piu' una lezione autonoma.

Il goal programming assume invece un ruolo autonomo, come passaggio dalla programmazione lineare a obiettivo singolo alla formulazione di problemi con obiettivi multipli, target, deviazioni e trade-off. Tale passaggio prepara l'applicazione computazionale ad asset allocation multicriterio e asset liability management.

## 5. Prodotti finali previsti

Il progetto prevede la costruzione dei seguenti prodotti finali:

1. un manuale del corso, articolato in 16 capitoli o unita' didattiche;
2. le slides delle 16 lezioni;
3. un insieme di esercizi teorici e numerici da svolgere in aula;
4. cinque applicazioni Python coerenti con la nuova architettura del corso;
5. un registro dei grafici didattici;
6. un documento autonomo di notazione matematica;
7. eventuali materiali ausiliari, quali soluzioni degli esercizi, template LaTeX, script Python, notebook, dataset e figure.

I materiali devono essere progettati in modo modulare, cosi' da consentire lo sviluppo separato di singole lezioni, capitoli, slides o applicazioni computazionali senza perdere coerenza complessiva.

## 6. Struttura delle 16 lezioni

La struttura operativa del corso e' la seguente.

| Lezione | Tipo | Titolo definitivo | Tema centrale |
|---:|:---:|---|---|
| 1 | P | Elementi di probabilita' | Spazio di probabilita', eventi, probabilita' condizionata |
| 2 | P | Variabili casuali | Variabili casuali, distribuzioni, momenti, quantili |
| 3 | P | Valori attesi condizionati | Condizionamento, partizioni, informazione |
| 4 | C | Applicazione in Python: probabilita', variabili casuali e condizionamento | Simulazione, distribuzioni empiriche, momenti, quantili, valori attesi condizionati |
| 5 | P | Processi stocastici in tempo discreto | Processi, traiettorie, scenari, filtrazioni, adattabilita', martingale |
| 6 | P | Processi stocastici in tempo continuo | Moto browniano, diffusioni, GBM, OU, CIR, correlazione, discretizzazione |
| 7 | C | Applicazione in Python: traiettorie, simulazione e pricing Monte Carlo | GBM, OU, processi correlati, opzioni asiatiche, obbligazioni indicizzate |
| 8 | P | Catene di Markov | Stati, transizioni, matrice di transizione, distribuzioni stazionarie |
| 9 | P | Catene di Markov e misure di rischio | Transizioni di rating, distribuzioni di perdita, VaR, CVaR |
| 10 | C | Applicazione in Python: rischio di credito | Simulazione di catene di Markov, portafogli creditizi, misure di rischio |
| 11 | P | Programmazione lineare | Formulazione, regione ammissibile, soluzioni di base, dualita' essenziale |
| 12 | P | Goal Programming | Obiettivi multipli, target, deviazioni, priorita', trade-off |
| 13 | C | Applicazione in Python: Asset Allocation e Asset Liability Management | Asset allocation multicriterio, liability matching, goal programming |
| 14 | P | Programmazione stocastica a due stadi | Decisioni sotto incertezza, scenari, recourse, valore atteso |
| 15 | P | Programmazione stocastica multistadio | Alberi di scenari, informazione progressiva, non anticipativita' |
| 16 | C | Applicazione in Python: programmazione stocastica | Asset allocation sotto incertezza, scenari, vincoli di non anticipativita' |

Legenda:

1. `P` = lezione prevalentemente teorica;
2. `C` = lezione con forte componente computazionale o applicativa.

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

## 8. Vincoli LaTeX e compatibilita' Scientific WorkPlace 5.5

Il manuale e le slides devono essere scritti in LaTeX compatibile con **Scientific WorkPlace 5.5**.

Criteri operativi:

1. usare una sintassi LaTeX prudente e standard;
2. evitare pacchetti moderni non necessari o potenzialmente incompatibili;
3. preferire ambienti standard per teoremi, definizioni, esempi ed esercizi;
4. mantenere formule leggibili e non eccessivamente annidate;
5. usare una struttura modulare con file separati per capitoli e lezioni;
6. valutare con attenzione l'uso di TikZ o PGFPlots, che potrebbero non essere la soluzione piu' robusta in Scientific WorkPlace 5.5;
7. quando opportuno, generare i grafici con Python e includerli come immagini.

I nomi dei file devono essere esplicativi e coerenti con la struttura gia' adottata nel progetto. Non devono essere utilizzati nomi puramente numerici o sbrigativi.

La struttura consigliata del manuale e':

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

La struttura consigliata delle slides e':

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

La struttura consigliata dei file Python e':

```text
/03_Python
  MQF_Python_01_Probabilita_Condizionamento.py
  MQF_Python_02_Traiettorie_Pricing.py
  MQF_Python_03_Rischio_Credito.py
  MQF_Python_04_Asset_Allocation_ALM.py
  MQF_Python_05_Programmazione_Stocastica.py
```

La struttura consigliata dei documenti di coordinamento e':

```text
/00_MasterPlan
  MQF_Project_Guidelines.md
  MQF_Master_Plan.tex
  MQF_Notazione.tex
  MQF_Stato_Avanzamento.md
  MQF_Registro_Esercizi.tex
  MQF_Registro_Grafici.tex
  MQF_Registro_Decisioni.tex
```

Ogni modifica ai nomi dei file deve essere esplicita e deve essere riportata nel Master Plan, nelle Guidelines e, se necessario, nei file master LaTeX che includono i singoli capitoli o le singole lezioni.

### Gestione delle figure: struttura delle cartelle, percorsi relativi e convenzione dei nomi

Per tutte le figure del progetto si adotta una cartella grafica comune e una convenzione uniforme sia per il richiamo nei file LaTeX sia per il salvataggio tramite script Python.

Schema ad albero della struttura rilevante:

```text
Progetto_MQF/
|-- 01_Manuale/
|   |-- Capitoli/
|   |   |-- MQF_Cap_01_....tex
|   |   |-- MQF_Cap_02_....tex
|   |   `-- ...
|   `-- MQF_Manuale_Master.tex
|
|-- 02_Slides/
|   |-- Lezioni/
|   |   |-- MQF_Slides_Lez_01_....tex
|   |   |-- MQF_Slides_Lez_02_....tex
|   |   `-- ...
|   `-- MQF_Slides_Master.tex
|
|-- 03_Codice/
|   |-- script_01.py
|   |-- script_02.py
|   `-- ...
|
`-- graphics/
    |-- Cap06_OU_mean_reversion.png
    |-- Cap06_GBM_traiettorie.png
    `-- Lez07_MC_payoff_distribution.png
```

Regole operative:

1. Tutte le figure del progetto, incluse quelle generate con Python, devono essere salvate nella cartella comune `graphics/`.

2. Nei file LaTeX del Manuale e delle Slides, le figure devono essere richiamate mediante il percorso relativo:
   `../graphics/NomeFigura.ext`

3. Negli script Python, la cartella `03_Codice/` si trova allo stesso livello della cartella `graphics/`; di conseguenza, il salvataggio delle figure deve avvenire mediante il percorso relativo:
   `./graphics/NomeFigura.ext`

4. La convenzione di denominazione dei file grafici deve essere stabile, informativa e priva di spazi. Usare underscore `_` per separare le parole.

5. Per figure associate ai capitoli del manuale, usare la forma:
   `CapXX_descrizione.png`

6. Per figure associate principalmente a una lezione o a una slide, usare la forma:
   `LezXX_descrizione.png`

7. La parte descrittiva del nome file deve essere breve e semanticamente chiara. Esempi:

   * `Cap06_OU_mean_reversion.png`
   * `Cap06_GBM_traiettorie.png`
   * `Lez07_MC_payoff_distribution.png`

Esempi d'uso:

* in LaTeX: `\includegraphics[width=0.78\textwidth]{../graphics/Cap06_OU_mean_reversion.png}`
* in Python: `plt.savefig("./graphics/Cap06_OU_mean_reversion.png", dpi=300, bbox_inches="tight")`


## 9. Manuale del corso

Il manuale deve essere il riferimento scientifico principale. Ogni capitolo deve essere autosufficiente, ma collegato agli altri capitoli.

### 9.1 Capitoli teorici

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

Le dimostrazioni devono essere selettive. Devono essere incluse quando rafforzano la comprensione dei meccanismi quantitativi, ma non devono trasformare il corso in un corso astratto di probabilita' o ottimizzazione.

### 9.2 Capitoli applicativi

La struttura standard di un capitolo con applicazione Python deve essere concepita in modo coerente con la natura laboratoriale della lezione. Il capitolo applicativo non deve limitarsi a presentare codice commentato, ma deve documentare il passaggio dalla formulazione matematica al prodotto computazionale finale.

La struttura orientativa di un capitolo applicativo e':

1. obiettivi della lezione applicativa;
2. presentazione del caso finanziario o probabilistico;
3. richiamo matematico-operativo del modello;
4. descrizione dei dati, dei parametri e degli output attesi;
5. strumenti Python necessari per la lezione;
6. struttura del notebook o dello script;
7. sviluppo guidato del codice;
8. tappe di sviluppo autonomo;
9. controlli numerici e logici intermedi;
10. output numerici e grafici;
11. interpretazione economico-finanziaria dei risultati;
12. estensioni take-home;
13. sintesi finale.

Nei capitoli applicativi il codice deve essere presentato come parte integrante della modellizzazione. Ogni blocco computazionale rilevante deve essere preceduto da una motivazione e seguito da un commento interpretativo. Il capitolo deve rendere esplicito che cosa viene calcolato, perche' viene calcolato e come il risultato si collega al modello teorico.

## 10. Slides: principi comuni

Le slides del corso MQF devono essere uno strumento di lezione, non una versione compressa del manuale. Devono guidare l'esposizione in aula, selezionare i passaggi concettuali essenziali, rendere visibili le formule operative e favorire l'alternanza tra motivazione finanziaria, formalizzazione matematica, esempi, grafici, esercizi e interpretazione.

Le slides devono essere prodotte in **LaTeX Beamer compatibile con Scientific WorkPlace 5.5**, riutilizzando il preambolo ufficiale gia' adottato nelle lezioni precedenti. In particolare, vanno mantenuti la classe `beamer`, il tema `Madrid`, le macro matematiche ufficiali del progetto e la struttura dei frame compatibile con Scientific WorkPlace 5.5.

### 10.1 Struttura tecnica di ogni slide

Ogni slide deve rispettare la struttura standard seguente:

```latex
\subsection{Titolo della sottosezione}
%TCIMACRO{\TeXButton{BeginFrame}{\begin{frame}}}%
%BeginExpansion
\begin{frame}%
%EndExpansion

\QTR{frametitle}{Titolo della slide}

%TCIMACRO{\TeXButton{Transparency}{\setbeamercovered{transparent=20}}}%
%BeginExpansion
\setbeamercovered{transparent=20}%
%EndExpansion

Contenuto della slide
%TCIMACRO{\TeXButton{Transition: Box Out}{\transboxout}}%
%BeginExpansion
\transboxout%
%EndExpansion
%TCIMACRO{\TeXButton{EndFrame}{\end{frame}}}%
%BeginExpansion
\end{frame}%
%EndExpansion
%*********************************************
```

La struttura va mantenuta anche quando il contenuto della slide e' breve. Il codice deve essere direttamente integrabile nel file `.tex` della lezione.

### 10.2 Uso del preambolo e delle macro

Il preambolo delle lezioni precedenti viene riutilizzato. Non e' quindi necessario rigenerarlo a ogni slide, salvo richiesta esplicita.

Le nuove slides devono assumere disponibili le macro ufficiali, fra cui:

```latex
\R, \N, \E, \Prob, \Q, \F, \B, \G,
\Var, \Cov, \VaR, \CVaR
```

Le formule devono usare queste macro in modo coerente con la notazione ufficiale del progetto MQF. Ogni nuova notazione introdotta nelle slides deve essere coerente con il documento `MQF_Notazione.tex`.

### 10.3 Enumerazioni e liste

Per le enumerazioni progressive si usa `stepenumerate`, con numerazione esplicita nella forma:

```latex
\begin{stepenumerate}
\item [1.] Primo punto.

\item [2.] Secondo punto.

\item [3.] Terzo punto.
\end{stepenumerate}
```

Per liste non numerate si usa `stepitemize`.

Le liste devono rimanere sintetiche. Ogni punto deve contenere un'unita' concettuale chiara, evitando testi eccessivamente lunghi. Le enumerazioni non devono sostituire la spiegazione del docente: devono invece scandire i passaggi principali.

### 10.4 Enfasi tipografica

Le parole chiave della slide possono essere evidenziate con `\textbf{...}`, ma con parsimonia. Il grassetto va riservato a concetti strutturali, come:

```latex
\textbf{evento condizionante}, \textbf{distribuzione condizionata},
\textbf{sigma-algebra informativa}, \textbf{regole operative}.
```

Non si devono enfatizzare intere frasi, ne' sovraccaricare la slide con troppi termini in grassetto.

## Formattazione delle istruzioni operative nel Manuale

Nel Manuale, tutti i testi operativi che uno studente deve digitare o impartire a un sistema devono essere trattati come blocchi tecnici, non come formule matematiche e non come testo ordinario. La regola riguarda in particolare:

1. prompt rivolti a strumenti di IA generativa;
2. comandi da terminale o riga di comando;
3. istruzioni testuali da inserire in un'interfaccia;
4. comandi sintetici da copiare ed eseguire;
5. input operativi rivolti a un software.

La formattazione standard e' la seguente:

    \begin{quote}
    \small
    \noindent{\ttfamily\raggedright
    testo del comando o dell'istruzione.\par}
    \end{quote}

Non utilizzare display matematici del tipo `\[ \text{...} \]` per prompt, comandi o istruzioni operative. Tali elementi non sono formule matematiche, non devono essere confusi con il contenuto teorico e possono produrre problemi di impaginazione.

Per riferimenti brevi a nomi di librerie, funzioni, variabili Python, file o comandi isolati all'interno del testo, e' invece ammesso l'uso di `\texttt{...}`. Ad esempio: `\texttt{numpy}`, `\texttt{pandas}`, `\texttt{pip}`, `\texttt{losses}`.

### 10.5 Formule matematiche

Nel codice `.tex` delle slides si usa naturalmente il codice LaTeX. Nella chat di lavoro, invece, le formule matematiche vanno rese con la normale renderizzazione matematica in riga, salvo quando si sta producendo direttamente codice sorgente.

Nel sorgente delle slides le formule devono essere brevi e centrali rispetto al messaggio della slide. Le formule lunghe o tecniche vanno preferibilmente isolate in display math. Ogni formula rilevante deve essere accompagnata da una breve interpretazione: probabilistica, finanziaria, computazionale o geometrica, a seconda del contesto.

### 10.6 Commento finale della slide

Un commento conclusivo in fondo alla slide va inserito solo quando soddisfa entrambe le condizioni seguenti:

1. aggiunge un contenuto logico rilevante;
2. vi e' sufficiente spazio nella slide.

Non va inserita una frase conclusiva puramente ornamentale o ridondante. Quando presente, il commento deve chiarire il passaggio concettuale della slide, il significato operativo della formula oppure il collegamento con la slide successiva.

### 10.7 Pianificazione delle slides

Prima di produrre il sorgente LaTeX di una lezione, occorre predisporre uno storyboard sintetico delle slides. Lo storyboard deve indicare:

1. numero progressivo della slide;
2. titolo provvisorio;
3. funzione didattica della slide;
4. contenuto matematico o finanziario essenziale;
5. eventuale esempio, grafico, esercizio o riferimento al manuale.

La pianificazione deve essere compatibile con la successiva costruzione della scaletta-promemoria della lezione. Le slides devono quindi essere pensate per gruppi didatticamente omogenei, cosi' da poter associare a ciascun gruppo un tempo parziale, un tempo cumulato e contenuti essenziali.

### 10.8 Coerenza documentale

La costruzione delle slides deve sempre partire dalla lettura aggiornata di:

1. Master Plan;
2. Guidelines;
3. Notazione ufficiale;
4. capitolo corrispondente del Manuale;
5. eventuali figure, esercizi e materiali collegati.

La memoria delle conversazioni precedenti puo' servire solo da orientamento generale, ma non deve sostituire la lettura diretta dei file aggiornati quando si pianifica o si genera una nuova lezione.

## 11. Slides delle lezioni teoriche di tipo P

Per ogni lezione teorica di tipo P, la struttura orientativa e':

1. apertura e motivazione finanziaria;
2. obiettivi della lezione;
3. richiamo dei prerequisiti strettamente necessari;
4. definizioni e notazione;
5. formule operative e risultati principali;
6. esempi numerici guidati;
7. eventuali grafici esplicativi;
8. esercizi in aula;
9. interpretazione finanziaria;
10. sintesi conclusiva.

Una lezione teorica non deve essere costruita come successione uniforme di definizioni. Deve alternare passaggi concettuali, formule, esempi e interpretazioni.

La sequenza didattica consigliata e':

| Blocco | Funzione |
|---|---|
| Apertura | Motivare il problema e formulare la domanda guida |
| Formalizzazione | Introdurre definizioni, ipotesi e simboli |
| Meccanismo | Presentare il risultato principale o la formula operativa |
| Esempio | Consolidare il concetto con un calcolo guidato |
| Grafico | Visualizzare distribuzioni, eventi, traiettorie, regioni o funzioni |
| Esercizio | Verificare la comprensione in aula |
| Sintesi | Fissare il nucleo concettuale da ricordare |

Anche per le lezioni prevalentemente teoriche di tipo P, la durata effettiva al netto del break e' assunta pari a **2 ore**, cioe' circa **120 minuti**.

La progettazione delle slides deve quindi essere calibrata su tale durata, prevedendo:

1. un numero di slides compatibile con spiegazione, esempi e discussione;
2. almeno due momenti applicativi o esercizi in aula;
3. pause concettuali dopo blocchi definitori o tecnici;
4. equilibrio tra formule, testo, grafici e interpretazioni.

E' preferibile una sequenza di slides leggibile a una singola slide eccessivamente densa. Ogni slide deve avere un obiettivo didattico riconoscibile.

## 12. Slides delle lezioni computazionali di tipo C

Le lezioni computazionali di tipo C hanno natura laboratoriale. Le slides devono quindi guidare non soltanto l'esposizione del docente, ma anche lo sviluppo del codice, il lavoro autonomo degli studenti, la discussione degli output e l'assegnazione dell'estensione take-home.

Le slides computazionali non devono trasformarsi in una dispensa di programmazione. Devono invece mostrare come un modello probabilistico, finanziario o ottimizzativo viene tradotto in una procedura Python controllabile, verificabile e interpretabile.

### 12.1 Funzione delle slides computazionali

Per ogni lezione applicativa Python, le slides devono svolgere cinque funzioni principali:

1. introdurre il caso applicativo;
2. collegare il caso al modello matematico del corso;
3. presentare gli strumenti Python strettamente necessari;
4. guidare lo sviluppo del notebook o dello script;
5. organizzare il lavoro autonomo, la discussione e il take-home.

Le slides devono rendere chiaro agli studenti che il codice non e' un esercizio separato dalla teoria, ma una forma operativa della modellizzazione quantitativa.

### 12.2 Struttura orientativa delle slides computazionali

La struttura orientativa di una lezione computazionale e':

1. apertura del caso applicativo;
2. obiettivi computazionali della lezione;
3. dati disponibili, parametri e output attesi;
4. richiamo matematico-operativo;
5. strumenti Python necessari;
6. schema del notebook o dello script;
7. avvio guidato dello sviluppo del codice;
8. tappe operative per lo sviluppo autonomo;
9. controlli intermedi e output attesi;
10. grafici e tabelle da produrre;
11. discussione dei risultati e degli errori ricorrenti;
12. estensione take-home.

Questa struttura puo' essere adattata alla difficolta' specifica della lezione, ma deve sempre mantenere l'alternanza tra spiegazione, implementazione guidata, lavoro autonomo e interpretazione dei risultati.

### 12.3 Codice nelle slides

Le slides computazionali non devono contenere codice esteso in misura eccessiva. Devono invece mostrare:

1. blocchi essenziali;
2. struttura logica del programma;
3. formule da implementare;
4. passaggi algoritmici principali;
5. controlli numerici o logici;
6. output attesi;
7. interpretazione dei risultati.

Il codice completo o semi-completo deve essere fornito nel notebook o nello script associato alla lezione. Le slides devono orientare la lettura e l'uso di quel codice, non sostituirlo integralmente.

### 12.4 Distinzione tra attivita' del docente e attivita' degli studenti

Le slides computazionali devono distinguere chiaramente:

1. che cosa viene spiegato dal docente;
2. che cosa viene sviluppato in modo guidato;
3. che cosa viene completato autonomamente dagli studenti;
4. che cosa viene discusso collettivamente;
5. che cosa viene lasciato come lavoro take-home.

Questa distinzione puo' essere resa mediante titoli di slide, etichette operative o blocchi separati. Esempi di etichette utili sono:

```text
Sviluppo guidato
Tappa autonoma
Controllo intermedio
Discussione in aula
Estensione take-home
```

### 12.5 Tappe operative e controlli intermedi

Le parti affidate allo sviluppo autonomo devono essere organizzate in tappe verificabili. Ogni tappa deve indicare:

1. obiettivo intermedio;
2. blocco di codice da completare, modificare o interpretare;
3. output atteso;
4. controllo numerico o logico;
5. breve interpretazione economico-finanziaria.

Le slides devono rendere visibile il criterio di successo della tappa. Non basta chiedere agli studenti di "completare il codice"; occorre specificare che cosa deve essere prodotto e come verificarlo.

### 12.6 Uso dei grafici nelle slides computazionali

Nelle lezioni computazionali i grafici hanno una funzione diagnostica e interpretativa. Devono essere usati per rappresentare, quando opportuno:

1. traiettorie simulate;
2. distribuzioni empiriche;
3. evoluzione di stati, probabilita' o rating;
4. processi multivariati correlati;
5. regioni ammissibili;
6. funzioni obiettivo, deviazioni da target e trade-off;
7. perdite, quantili e misure di rischio;
8. confronti tra scenari o soluzioni.

Ogni grafico deve essere accompagnato da una domanda interpretativa o da un commento operativo. Un grafico non deve comparire come puro output decorativo.

### 12.7 Uso controllato dell'IA generativa

Quando previsto, l'uso dell'IA generativa deve essere presentato nelle slides come supporto controllato, non come sostituto della modellizzazione.

Le slides possono indicare usi ammessi, quali:

1. spiegare un messaggio di errore;
2. correggere un errore sintattico o locale;
3. proporre una funzione Python coerente con una formula data;
4. commentare un blocco di codice;
5. migliorare la leggibilita' del codice;
6. confrontare due implementazioni alternative.

Le slides devono anche chiarire che non e' appropriato delegare all'IA:

1. la formulazione matematica del modello;
2. la scelta delle ipotesi;
3. la definizione delle variabili decisionali;
4. la selezione delle misure di rischio;
5. l'interpretazione economico-finanziaria dei risultati;
6. la verifica finale della correttezza.

### 12.8 Durata e scansione delle lezioni computazionali

Ciascuna lezione computazionale ha durata complessiva di **2 ore e 15 minuti**, con **15 minuti di pausa**. Il tempo effettivo di lavoro e' quindi pari a circa **120 minuti**.

La scansione temporale di riferimento e':

1. 10--15 minuti per l'introduzione del caso;
2. 10--15 minuti per il richiamo matematico-operativo;
3. 15--20 minuti per gli strumenti Python necessari;
4. 25--30 minuti per lo sviluppo guidato del codice;
5. 15 minuti di pausa;
6. 35--40 minuti per lo sviluppo autonomo assistito;
7. 15--20 minuti per la discussione collettiva;
8. 5--10 minuti per la chiusura e l'assegnazione take-home.

Le slides devono essere progettate in modo coerente con questa scansione. In particolare, devono rendere evidente il passaggio dalla parte guidata alla parte autonoma e poi alla discussione collettiva.

### 12.9 Prodotto finale osservabile

Ogni lezione computazionale deve concludersi con un prodotto finale osservabile. Le slides devono esplicitare fin dall'inizio quale prodotto si intende costruire.

Esempi di prodotto finale sono:

1. una distribuzione empirica simulata;
2. una procedura di stima condizionata;
3. un simulatore di traiettorie;
4. una procedura Monte Carlo di pricing;
5. una matrice di transizione analizzata numericamente;
6. una distribuzione di perdita con VaR e CVaR;
7. una formulazione di goal programming;
8. una tabella di confronto tra soluzioni;
9. un grafico interpretativo;
10. un confronto tra soluzioni deterministiche e stocastiche.

La lezione computazionale non deve concludersi genericamente con la scrittura di codice, ma con la comprensione di che cosa il codice permette di calcolare e di come tale calcolo rafforzi l'interpretazione del modello teorico.

## 13. Esercizi in aula

Ogni lezione teorica deve includere almeno due esercizi in aula:

1. un esercizio di calcolo, derivazione o formulazione;
2. un esercizio di interpretazione finanziaria.

Quando utile, va aggiunto un esercizio grafico.

Nelle lezioni applicative Python gli esercizi in aula devono essere organizzati come tappe operative di laboratorio. Ogni tappa deve avere:

1. un obiettivo intermedio esplicito;
2. un blocco di codice da completare, modificare o interpretare;
3. un output atteso, numerico o grafico;
4. almeno un controllo numerico o logico;
5. una breve interpretazione economico-finanziaria.

Le tappe operative devono essere progettate in modo progressivo. Una possibile struttura e':

1. verifica dei dati e dei parametri;
2. implementazione di una formula o funzione centrale;
3. produzione di un primo output numerico;
4. costruzione di un grafico o di una tabella;
5. analisi di sensibilita' rispetto a un parametro;
6. interpretazione del risultato;
7. estensione o variante del caso base.

Gli esercizi applicativi non devono essere mini-progetti indipendenti durante la lezione. Devono invece essere parti controllate di un percorso comune, in cui gli studenti completano alcune componenti del software mantenendo visibile il collegamento con il modello teorico.

Quando si prevede l'uso di strumenti di intelligenza artificiale generativa, l'esercizio deve specificare in modo chiaro quali usi sono ammessi. L'IA puo' essere impiegata per chiarire errori di codice, spiegare messaggi di errore, proporre una funzione locale o migliorare la leggibilita' di un blocco. Non deve invece sostituire la formulazione del modello, la scelta delle ipotesi o l'interpretazione dei risultati.

## 14. Applicazioni Python e lezioni applicative

Sono previste cinque applicazioni Python, corrispondenti alle lezioni applicative del corso.

| Applicazione | Lezione | Tema | Output computazionale |
|---:|---:|---|---|
| 1 | 4 | Probabilita', variabili casuali e condizionamento | Simulazioni, distribuzioni empiriche, momenti, quantili, stime condizionate |
| 2 | 7 | Traiettorie, simulazione e pricing Monte Carlo | Traiettorie GBM, OU, processi correlati, opzioni asiatiche, sistema OU--CIR |
| 3 | 10 | Rischio di credito | Matrici di transizione, simulazioni di rating, distribuzioni di perdita, VaR, CVaR |
| 4 | 13 | Asset Allocation e Asset Liability Management | Goal programming, allocazioni multicriterio, deviazioni da target, liability matching |
| 5 | 16 | Programmazione stocastica | Scenari, recourse, non anticipativita', confronto tra soluzioni deterministiche e stocastiche |

Le applicazioni Python devono essere concepite come laboratori di modellizzazione quantitativa. La finalita' principale non e' insegnare Python in modo autonomo, ma mostrare come un modello probabilistico, finanziario o ottimizzativo possa essere tradotto in una procedura computazionale controllabile, interpretabile e modificabile.

Ogni applicazione deve essere costruita intorno a un problema finanziario o probabilistico identificabile. Il caso applicativo deve specificare:

1. il contesto finanziario o probabilistico;
2. la domanda quantitativa da affrontare;
3. i dati disponibili, se presenti, oppure la procedura di generazione dei dati simulati;
4. i parametri del modello;
5. le grandezze da calcolare;
6. gli output numerici e grafici attesi;
7. il prodotto computazionale finale.

### 14.1 Coppia caso aula / caso take-home

Per ciascuna lezione applicativa deve essere progettata una coppia di casi:

1. **caso aula**, sviluppato dal docente durante la lezione;
2. **caso take-home**, assegnato agli studenti come lavoro autonomo.

Il caso aula ha funzione dimostrativa. Deve mostrare come un problema quantitativo-finanziario venga trasformato in un percorso computazionale attraverso:

1. ricognizione delle premesse teorico-matematiche;
2. scomposizione del problema in tappe;
3. identificazione degli input e degli output di ciascuna tappa;
4. costruzione del notebook;
5. produzione di stime, tabelle, grafici e controlli;
6. interpretazione economico-finanziaria dei risultati;
7. uso virtuoso dell'IA generativa, quando previsto, secondo le regole della Sezione 15.

Il caso take-home deve essere distinto dal caso aula, ma metodologicamente comparabile. Non deve consistere in una semplice variazione parametrica del caso svolto in aula. Deve invece essere isomorfo sul piano metodologico: deve richiedere strumenti teorici analoghi, una struttura di tappe confrontabile e output dello stesso tipo generale, ma in un contesto finanziario o probabilistico diverso.

Per ogni coppia caso aula / caso take-home devono essere chiari:

1. quali concetti teorici vengono consolidati;
2. quali strumenti computazionali vengono utilizzati;
3. quali output devono essere prodotti;
4. quali controlli devono essere svolti;
5. quali elementi sono comuni ai due casi;
6. quali elementi distinguono il caso take-home dal caso aula.

### 14.2 Materiali da predisporre per ogni lezione applicativa

Per ogni lezione applicativa devono essere predisposti almeno i seguenti materiali:

1. traccia del caso aula;
2. notebook docente del caso aula;
3. eventuale successione di prompt virtuosi utilizzati nel caso aula;
4. traccia del caso take-home;
5. scheda docente di calibrazione del caso take-home;
6. notebook studente, completo o semi-strutturato;
7. eventuali file dati;
8. lista dei parametri iniziali;
9. sequenza di tappe operative;
10. controlli intermedi;
11. output numerici attesi;
12. grafici o tabelle da produrre;
13. indicazioni per la discussione in aula;
14. template del tracciato IA in formato Markdown, se il lavoro prevede uso documentato dell'IA;
15. rubrica di valutazione del notebook e del tracciato IA.

La scheda docente di calibrazione del caso take-home deve essere predisposta prima dell'assegnazione agli studenti. Essa deve contenere:

1. premesse teorico-matematiche necessarie;
2. scomposizione attesa del problema in tappe;
3. collegamenti input/output tra le tappe;
4. output richiesti: stime, tabelle, grafici, controlli;
5. successione di prompt docente di riferimento, se l'uso dell'IA e' previsto;
6. numero minimo e massimo di prompt ammessi nel tracciato dello studente, quando richiesto;
7. criteri di valutazione.

La scheda di calibrazione ha funzione interna di controllo didattico. Serve a verificare che il caso take-home sia risolvibile, coerente con il caso aula, adeguato al livello del corso e valutabile in modo non arbitrario.

### 14.3 Notebook applicativo

Il notebook Jupyter e' il formato ordinario delle lezioni applicative. Lo script Python puo' essere prodotto come materiale ausiliario o di esportazione, ma il notebook resta preferibile quando e' necessario integrare testo, formule, codice, output, grafici e commenti interpretativi.

Il notebook non deve essere una semplice raccolta di celle di codice. Deve essere progettato come catena di ragionamento quantitativo, in cui ogni blocco computazionale sia collegato a una domanda finanziaria, a una formula, a un output e a un controllo.

La struttura consigliata del notebook e':

1. intestazione della lezione e descrizione del caso;
2. obiettivi applicativi;
3. premesse teorico-matematiche essenziali;
4. dati disponibili, parametri o procedura di simulazione;
5. librerie Python necessarie;
6. funzioni ausiliarie;
7. scomposizione del problema in tappe;
8. implementazione delle tappe;
9. controlli intermedi;
10. output numerici;
11. grafici e tabelle;
12. analisi di sensibilita', se appropriata;
13. blocchi da completare da parte degli studenti;
14. domande di interpretazione;
15. sintesi finale;
16. indicazioni per il caso take-home, quando previsto.

Il notebook deve evitare che gli studenti partano da un file vuoto. Le parti da completare, modificare o discutere devono essere chiaramente segnalate. Possono essere usate formule del tipo:

```python
# TODO 1: completare la funzione
# TODO 2: verificare il controllo numerico
# TODO 3: produrre il grafico richiesto
# TODO 4: interpretare il risultato
```

Quando l'uso dell'IA e' previsto, il notebook puo' includere prompt virtuosi di riferimento. Tali prompt devono essere coerenti con la teoria dell'uso virtuoso dell'IA definita nella Sezione 15. I prompt non devono trasformare il notebook in una soluzione gia' delegata all'IA, ma devono mostrare come delimitare il compito richiesto allo strumento.

### 14.4 Tappe operative come moduli input/output

Le tappe operative devono essere progettate come moduli logici, non come celle isolate. Ogni tappa deve rendere esplicito il collegamento tra cio' che e' gia' disponibile, cio' che viene trasformato e cio' che sara' utilizzato successivamente.

La struttura generale di una tappa e':

```text
input_k -> operazione_k -> output_k -> uso in k+1
```

Per ciascuna tappa devono essere specificati:

1. input provenienti dalle tappe precedenti;
2. obiettivo della tappa;
3. oggetti teorici coinvolti;
4. operazione computazionale richiesta;
5. output prodotto;
6. controllo numerico, logico o interpretativo;
7. uso dell'output nella tappa successiva.

Una tappa didattica puo' comprendere piu' celle:

1. cella Markdown di descrizione della tappa;
2. cella Markdown con input disponibili e output atteso;
3. cella Markdown con eventuale regime IA prevalente e prompt virtuoso di riferimento;
4. cella codice per l'operazione computazionale;
5. cella codice o Markdown per il controllo;
6. cella Markdown per interpretazione o commento locale.

Questa struttura deve rendere visibile il passaggio:

```text
problema finanziario -> oggetto teorico -> procedura Python -> output -> controllo -> interpretazione
```

Le tappe operative non devono essere mini-progetti indipendenti. Devono essere parti concatenate di un percorso comune, in cui ogni output rilevante contribuisce alla tappa successiva o al prodotto computazionale finale.

### 14.5 Criteri comuni per il codice Python

Il codice Python deve rispettare i seguenti criteri:

1. codice leggibile e ben commentato;
2. separazione tra dati, parametri, funzioni e output;
3. nomi delle variabili coerenti, per quanto possibile, con la notazione matematica;
4. preferenza per codice comprensibile rispetto a codice eccessivamente compatto;
5. controlli intermedi espliciti;
6. grafici leggibili e interpretabili;
7. interpretazione dei risultati dopo ogni blocco computazionale rilevante;
8. possibilita' di modificare parametri, scenari e target;
9. riproducibilita' dell'esecuzione;
10. tracciabilita' del passaggio dalla formula matematica all'algoritmo.

Gli strumenti Python introdotti in ciascuna lezione devono essere selezionati in funzione del modello. Non devono essere presentati come argomenti indipendenti di programmazione.

A seconda della lezione, possono essere introdotti:

1. array, vettori e matrici;
2. funzioni;
3. simulazione Monte Carlo;
4. strutture dati per stati, scenari e traiettorie;
5. grafici;
6. calcolo di quantili e medie condizionate;
7. simulazione di processi stocastici discreti e continui;
8. uso di solver di ottimizzazione;
9. formulazione di problemi di goal programming;
10. analisi di sensibilita'.

Quando possibile, il codice deve essere costruito in modo da permettere agli studenti di modificare parametri, soglie, scenari o target e osservare come cambiano gli output. Tuttavia, tali modifiche devono essere collegate a una domanda interpretativa e non ridursi a manipolazioni puramente tecniche.

### 14.6 Output numerici, grafici e prodotto finale osservabile

Ogni lezione applicativa deve concludersi con un prodotto finale osservabile. La lezione non deve concludersi genericamente con la scrittura di codice, ma con la comprensione di che cosa il codice permette di calcolare e di come tale calcolo modifichi o rafforzi l'interpretazione del modello teorico.

Esempi di prodotto finale sono:

1. una distribuzione empirica simulata;
2. una procedura di stima condizionata;
3. un simulatore di traiettorie;
4. una procedura Monte Carlo di pricing;
5. una matrice di transizione analizzata numericamente;
6. una distribuzione di perdita con VaR e CVaR;
7. una formulazione di goal programming;
8. una tabella di confronto tra soluzioni;
9. un grafico interpretativo;
10. un confronto tra soluzioni deterministiche e stocastiche.

I grafici devono avere funzione diagnostica o interpretativa. Non devono essere output decorativi. Per ogni grafico devono essere esplicitati:

1. la variabile o le variabili rappresentate;
2. il confronto che il grafico deve rendere visibile;
3. eventuali soglie, stati, scenari o target da evidenziare;
4. la domanda interpretativa associata;
5. il collegamento con il modello teorico.

Quando il codice per il grafico viene prodotto con supporto dell'IA, lo studente o il docente devono comunque specificare le proprieta' informative del grafico. L'IA puo' essere delegata alla realizzazione tecnica, ma non alla scelta del significato informativo del grafico.

### 14.7 Valutazione dei lavori take-home

Quando una lezione applicativa prevede un lavoro take-home, la valutazione deve riguardare congiuntamente:

1. notebook operativo;
2. output prodotti;
3. eventuale tracciato IA in formato Markdown;
4. interpretazione finale.

La valutazione non deve premiare la complessita' autonoma del codice Python. Deve valutare la capacita' dello studente di:

1. identificare correttamente le premesse teorico-matematiche;
2. scomporre il problema in tappe coerenti;
3. mantenere il legame input/output tra le tappe;
4. produrre output numerici, tabelle e grafici coerenti con il problema;
5. verificare gli output mediante controlli numerici, logici o interpretativi;
6. interpretare i risultati in modo proporzionato alle ipotesi del modello;
7. governare l'eventuale interazione con l'IA secondo i regimi definiti nella Sezione 15.

Il notebook e il tracciato IA, quando richiesto, devono essere coerenti tra loro. Output computazionali corretti ma ottenuti attraverso una delega opaca e non controllata non costituiscono uso virtuoso dell'IA. Allo stesso modo, prompt formalmente corretti ma non collegati agli output effettivi del notebook non sono sufficienti.

La rubrica di valutazione di ciascun caso take-home deve essere coerente con la scheda docente di calibrazione. I criteri minimi sono:

1. qualita' delle premesse teorico-matematiche identificate;
2. correttezza della scomposizione in tappe;
3. coerenza degli input/output che collegano le tappe;
4. qualita' degli output richiesti: stime, tabelle, grafici, controlli;
5. qualita' e virtu' dei prompt utilizzati, se il tracciato IA e' richiesto;
6. capacita' di verifica e interpretazione critica.

### 14.8 Relazione con le slides e con il capitolo applicativo

La lezione applicativa deve essere coerente con il capitolo corrispondente del manuale e con le slides della lezione.

Il capitolo applicativo deve documentare il passaggio dalla formulazione teorica al prodotto computazionale finale. Le slides devono invece orientare il lavoro in aula, selezionando i passaggi essenziali: caso, obiettivi, formule operative, tappe principali, output attesi, controlli e interpretazione.

Il notebook contiene il codice completo o semi-completo e rappresenta il supporto operativo principale. Le slides non devono duplicare il notebook, ma devono aiutare lo studente a comprendere la logica del percorso e il ruolo delle singole tappe.

## 15. Uso virtuoso dell'IA generativa nelle lezioni applicative

L'uso di strumenti di intelligenza artificiale generativa puo' essere previsto nelle lezioni applicative come supporto controllato alla modellizzazione quantitativa. L'obiettivo non e' insegnare l'IA come contenuto autonomo, ne' trasformare Python in un contenuto indipendente del corso. L'obiettivo e' permettere agli studenti di osservare, simulare, verificare e interpretare modelli quantitativi applicati alla finanza.

Nel corso MQF, l'IA deve essere trattata come strumento di interazione metodologica. Essa puo' assistere lo studente nel passaggio dal problema economico-finanziario alla procedura computazionale, ma non deve sostituire la responsabilita' dello studente nella definizione degli oggetti teorici, nella verifica degli output e nell'interpretazione finanziaria dei risultati.

L'uso virtuoso dell'IA non coincide con un uso minimo dello strumento. Uno studente puo' utilizzare l'IA in modo esteso e tuttavia corretto, se conserva il controllo della struttura teorica, delimita esplicitamente i compiti delegati, verifica gli output e formula autonomamente l'interpretazione finanziaria. L'uso improprio consiste invece nella delega opaca di passaggi che devono restare sotto responsabilita' dello studente.

Le lezioni applicative devono quindi insegnare non soltanto a ottenere output computazionali, ma a governare l'interazione con l'IA secondo una sequenza metodologicamente controllata.

### 15.1 Uso virtuoso e uso improprio

Si parla di uso virtuoso dell'IA quando lo studente formula richieste delimitate, coerenti con il problema assegnato e accompagnate da vincoli espliciti. Un prompt virtuoso non chiede all'IA di risolvere globalmente il problema, ma specifica il contesto, indica gli oggetti gia' definiti, chiarisce il compito e stabilisce che cosa non deve essere modificato.

Sono esempi di uso virtuoso:

1. chiedere all'IA di aiutare a distinguere variabili casuali, eventi, stati informativi, scenari, ipotesi e quantita' teoriche, senza risolvere il problema;

2. chiedere all'IA di costruire una procedura Python coerente con una specifica teorica gia' validata;

3. chiedere all'IA di produrre il codice necessario per un grafico di cui lo studente ha gia' specificato le proprieta' informative;

4. chiedere all'IA di segnalare ambiguita', errori logici o conclusioni troppo forti in una verifica o interpretazione gia' formulata dallo studente;

5. usare l'IA per correggere errori tecnici, migliorare la leggibilita' del codice o organizzare output numerici e grafici, senza modificare il significato matematico-finanziario del problema.

Sono esempi di uso improprio:

1. chiedere all'IA di scegliere autonomamente il modello da utilizzare;

2. chiedere all'IA di definire variabili casuali, eventi, formule o ipotesi senza successiva validazione critica;

3. chiedere all'IA di risolvere direttamente l'intero caso applicativo;

4. chiedere all'IA di produrre l'interpretazione finanziaria finale;

5. accettare output numerici o grafici senza controllare la coerenza con la formula, con il codice e con il problema;

6. presentare come verifica autonoma una certificazione di correttezza prodotta dall'IA.

La distinzione tra uso virtuoso e uso improprio non riguarda quindi la presenza o assenza dell'IA, ma il controllo esercitato dallo studente sulla sequenza di lavoro.

### 15.2 I tre regimi dell'interazione studente-IA

L'interazione con l'IA nelle lezioni applicative deve essere organizzata secondo tre regimi. I regimi rappresentano tre funzioni diverse dello strumento e tre diversi livelli di responsabilita' dello studente.

#### Regime A - Ricognizione teorico-modellistica

Nel Regime A, l'IA viene utilizzata per aiutare lo studente a riconoscere gli oggetti teorici coinvolti nel problema.

Lo studente puo' chiedere supporto per distinguere:

1. grandezze economico-finanziarie;
2. variabili casuali o decisionali;
3. eventi;
4. stati informativi;
5. scenari;
6. ipotesi;
7. formule candidate;
8. quantita' teoriche da calcolare;
9. controparte empirica o computazionale delle quantita' teoriche;
10. limiti del modello che dovranno essere considerati.

L'IA non deve risolvere il problema, scegliere autonomamente il modello finale o produrre direttamente la soluzione matematica completa. In questo regime, l'autonomia dello studente riguarda la costruzione del significato matematico del problema. L'IA puo' proporre una mappa concettuale, ma lo studente deve validarla, correggerla e trasformarla in una specifica teorica coerente.

Formula guida del Regime A:

> Aiutami a riconoscere gli oggetti teorici del problema, senza risolverlo.

Esempio di prompt coerente con il Regime A:

> Sto lavorando su un problema di perdita di portafoglio condizionata a stati informativi di mercato. Aiutami a distinguere variabili casuali, eventi, informazione disponibile, quantita' teoriche e possibili stime empiriche. Non scegliere il modello finale, non scrivere codice e non risolvere il caso.

#### Regime B - Operazionalizzazione computazionale

Nel Regime B, l'IA viene utilizzata per rendere computabile una specifica teorica gia' definita e validata. In questo regime, lo studente puo' delegare all'IA la costruzione dell'apparato computazionale, pur mantenendo il controllo sulla sostanza teorica del problema.

L'IA puo' essere utilizzata per:

1. costruire dataset simulati;
2. definire strutture dati;
3. scegliere nomi di variabili Python coerenti;
4. organizzare la sequenza delle celle;
5. scrivere codice Python;
6. produrre tabelle;
7. produrre output numerici;
8. implementare tecnicamente grafici;
9. inserire controlli computazionali;
10. migliorare leggibilita' e modularita' del codice.

Il vincolo fondamentale e' che l'IA non deve modificare la sostanza matematica del problema. Variabili casuali, eventi, stati, scenari, formule e ipotesi devono restare quelli emersi e validati nel Regime A. L'IA puo' scegliere la forma computazionale piu' conveniente, ma non puo' cambiare cio' che deve essere calcolato.

Formula guida del Regime B:

> Data questa specifica teorica validata, costruisci l'apparato computazionale, senza modificarla.

Esempio di prompt coerente con il Regime B:

> Ho validato la seguente specifica teorica: L e' la perdita di portafoglio, S e' l'evento di stress, e la quantita' da stimare e' la media empirica di L condizionata a S. Costruisci una procedura Python coerente con questa specifica. Puoi scegliere struttura dati, nomi Python e forma dell'output. Non modificare la definizione di L, non cambiare l'evento S, non introdurre altre misure di rischio e non interpretare il risultato.

Nel caso dei grafici, la distinzione tra contenuto informativo e realizzazione tecnica e' essenziale. Lo studente deve specificare quale variabile rappresentare, quale confronto mostrare, quale soglia evidenziare e quale domanda interpretativa il grafico deve rendere visibile. L'IA puo' essere delegata alla realizzazione tecnica del grafico, ma non alla scelta del suo significato informativo.

#### Regime C - Verifica e interpretazione critica

Nel Regime C, l'IA viene utilizzata come revisore critico. Lo studente deve prima formulare un controllo, una verifica o un'interpretazione. Solo dopo puo' chiedere all'IA di segnalare errori, ambiguita', passaggi non giustificati, confusioni terminologiche o conclusioni troppo forti.

L'IA puo' aiutare a individuare:

1. incoerenze tra formula teorica e codice;
2. incoerenze tra codice e output;
3. controlli numerici mancanti;
4. controlli logici mancanti;
5. confusione tra quantita' teorica e stima empirica;
6. interpretazioni finanziarie troppo forti;
7. limiti del modello non dichiarati;
8. affermazioni non supportate dagli output prodotti.

L'IA non deve produrre la conclusione finale al posto dello studente. In questo regime, l'autonomia dello studente e' massima: l'IA non interpreta, ma critica un'interpretazione gia' proposta.

Formula guida del Regime C:

> Valuta criticamente la verifica e l'interpretazione che ho scritto, senza sostituirti a me.

Esempio di prompt coerente con il Regime C:

> Ho scritto questa interpretazione del risultato ottenuto. Segnala se distinguo correttamente quantita' teorica e stima empirica, se traggo conclusioni troppo forti e se sto trascurando limiti rilevanti del modello. Non riscrivere il testo al posto mio e non produrre una conclusione finale.

### 15.3 Due scale di lavoro

I tre regimi operano su due scale diverse: il livello del problema complessivo e il livello della singola tappa.

Al livello del problema complessivo, i tre regimi servono a costruire il percorso risolutivo. L'obiettivo non e' ancora produrre codice o risultati numerici, ma inquadrare il problema, generare un percorso, fissare le tappe principali e verificare che la sequenza sia logicamente coerente.

Al livello della singola tappa, i tre regimi servono invece a svolgere un passaggio specifico del percorso: specificare l'oggetto teorico locale, costruire la procedura computazionale corrispondente, controllare l'output e interpretarne il ruolo.

Al livello macro, la sequenza e':

1. Regime A: inquadramento teorico del problema complessivo;
2. Regime B: progettazione del percorso computazionale;
3. Regime C: revisione critica del percorso risolutivo.

Al livello micro, la sequenza e':

1. Regime A: specificazione teorica della tappa;
2. Regime B: operazionalizzazione computazionale della tappa;
3. Regime C: verifica e interpretazione locale della tappa.

Questa distinzione impedisce che l'IA passi direttamente dal testo del problema al codice completo. Prima si costruisce il percorso, poi si lavora sulle singole tappe.

### 15.4 La tappa come modulo input/output

Ogni tappa applicativa deve essere trattata come un modulo input/output. Una tappa non e' una semplice cella di codice, ma un passaggio logico che riceve alcuni oggetti, compie una trasformazione e produce nuovi oggetti da utilizzare successivamente.

La struttura generale di una tappa e' data dalla successione: input della tappa, operazione da svolgere, output prodotto e uso dell'output nella tappa successiva.

Per ogni tappa devono essere esplicitati:

1. input disponibili all'inizio della tappa;
2. obiettivo della tappa;
3. regime prevalente dell'interazione con l'IA, se previsto;
4. oggetti teorici coinvolti;
5. operazione computazionale richiesta;
6. output prodotto;
7. controllo numerico, logico o interpretativo;
8. uso dell'output nella tappa successiva.

Questa impostazione evita che il notebook diventi una successione di celle indipendenti. Ogni blocco computazionale deve avere una funzione nel percorso complessivo e deve produrre un oggetto utile per il seguito dell'analisi o per il prodotto finale.

Nel tracciato dell'interazione con l'IA, lo studente deve rendere visibile il collegamento tra tappe. Non e' sufficiente mostrare prompt isolati: occorre indicare quali input erano disponibili, quale output e' stato ottenuto e in che modo tale output viene riutilizzato.

### 15.5 Grammatica del prompt virtuoso

Un prompt virtuoso deve rendere visibili il contesto, il regime dell'interazione e i limiti del compito assegnato all'IA. La struttura generale del prompt deve includere, quando rilevante, i seguenti elementi:

1. contesto del problema;
2. input disponibili;
3. oggetti teorici gia' definiti;
4. regime richiesto: A, B oppure C;
5. compito richiesto all'IA;
6. vincoli su cio' che l'IA non deve modificare o produrre;
7. output atteso;
8. controllo richiesto;
9. uso dell'output nella tappa successiva.

Nel Regime A, il prompt deve orientare la ricognizione teorica. La forma raccomandata e':

> Aiutami a distinguere grandezze, variabili, eventi, informazione, ipotesi e quantita' teoriche. Non risolvere il problema, non scegliere il modello finale e non scrivere codice.

Nel Regime B, il prompt deve vincolare la costruzione computazionale. La forma raccomandata e':

> Data questa specifica teorica, costruisci il codice o l'output richiesto. Puoi scegliere la forma tecnica della procedura, ma non modificare variabili, eventi, formule, ipotesi o significato finanziario.

Nel Regime C, il prompt deve trasformare l'IA in revisore critico. La forma raccomandata e':

> Ho scritto questa verifica o interpretazione. Segnala errori, ambiguita' e affermazioni troppo forti, ma non riscrivere il testo al posto mio.

Un prompt privo di contesto, di input e di vincoli tende a produrre risposte generiche. Un prompt troppo ampio, come "risolvi il problema", trasferisce all'IA responsabilita' che nel corso devono restare allo studente. Un prompt virtuoso, invece, delimita l'interazione e permette di controllare se la risposta ottenuta e' coerente con il modello.

### 15.6 Tracciato IA dello studente

Quando il lavoro take-home prevede uso documentato dell'IA, lo studente deve consegnare un tracciato dell'interazione in formato Markdown `.md`.

Il tracciato non deve essere valutato come prova forense dell'intera storia privata del lavoro svolto con strumenti IA. Deve essere valutato come artefatto metodologico: esso deve mostrare come lo studente ha organizzato l'assistenza dell'IA secondo una sequenza controllata di ricognizione teorico-modellistica, operazionalizzazione computazionale, verifica e interpretazione critica.

Il tracciato deve contenere:

1. identificazione del problema;
2. premesse teorico-matematiche individuate;
3. scomposizione del problema in tappe;
4. collegamenti input/output tra tappe;
5. prompt utilizzati;
6. regime attribuito a ciascun prompt;
7. risposta IA utilizzata, oppure sintesi fedele della parte effettivamente utilizzata;
8. azione dello studente: accettazione, modifica, rifiuto o correzione;
9. output prodotto;
10. controllo svolto;
11. interpretazione finale.

I prompt dello studente devono essere riportati integralmente. Le risposte dell'IA possono essere sintetizzate se molto lunghe, ma la sintesi deve indicare chiaramente quale parte della risposta e' stata effettivamente utilizzata.

Il numero di prompt deve rispettare l'intervallo stabilito dal docente per ciascun caso take-home. Tale intervallo viene indicato nella scheda docente di calibrazione del caso e deve essere comunicato agli studenti nella traccia del lavoro.

Un tracciato troppo breve tende a indicare una delega globale e non controllata. Un tracciato eccessivamente lungo tende a rendere difficile la valutazione e puo' indicare assenza di organizzazione. Il vincolo sul numero minimo e massimo di prompt ha quindi funzione didattica: obbliga lo studente a decomporre il problema senza produrre un materiale ingestibile.

### 15.7 Valutazione del tracciato IA

La valutazione del tracciato IA deve concentrarsi sulla qualita' metodologica dell'interazione, non sulla presunta originalita' assoluta della conversazione. In un lavoro svolto a casa non e' realistico ricostruire tutta la storia privata dell'uso dell'IA. La valutazione deve riguardare il tracciato consegnato come artefatto osservabile.

Non e' penalizzato l'uso dell'IA per migliorare la formulazione dei prompt, per organizzare meglio la sequenza di lavoro o per chiarire come strutturare l'interazione. Cio' che deve essere valutato negativamente e' la delega non governata, generica, opaca o concettualmente vuota.

La valutazione del tracciato deve considerare almeno i seguenti criteri:

1. corretta distinzione dei regimi A, B e C;
2. qualita' delle premesse teorico-matematiche identificate;
3. corretta scomposizione del problema in tappe;
4. chiarezza del legame input/output tra tappe;
5. specificita' dei prompt;
6. presenza di vincoli espliciti posti all'IA;
7. coerenza tra prompt, output del notebook e interpretazione;
8. capacita' di correggere, restringere o rifiutare risposte IA troppo ampie;
9. presenza di controlli numerici, logici o interpretativi;
10. autonomia dell'interpretazione finale.

Sono indicatori di uso debole o improprio:

1. prompt globali del tipo "risolvi il problema";
2. passaggio immediato dal testo del problema al codice completo;
3. assenza di Regime A;
4. assenza di Regime C;
5. prompt privi di contesto e di vincoli;
6. IA che sceglie variabili, eventi, formule o ipotesi senza validazione;
7. IA che produce direttamente l'interpretazione finale;
8. output non coerenti con i prompt o con la traccia del problema;
9. controlli dichiarati ma non effettivamente collegati agli output;
10. tracciato formalmente ordinato ma povero di contenuto specifico.

Sono indicatori di uso virtuoso:

1. sequenza riconoscibile di ricognizione, operazionalizzazione e verifica;
2. prompt specifici e contestualizzati;
3. vincoli espliciti sul ruolo dell'IA;
4. collegamento tra oggetti teorici e oggetti computazionali;
5. tappe concatenate mediante input e output;
6. proprieta' informative dei grafici specificate dallo studente;
7. controlli numerici e logici espliciti;
8. revisione critica dell'interpretazione;
9. correzione di risposte IA troppo generiche o invasive;
10. coerenza tra tracciato IA, notebook e output finali.

### 15.8 Rapporto tra IA, Python e responsabilita' dello studente

Nelle lezioni applicative, l'IA puo' ridurre la frizione tecnica associata alla scrittura del codice Python. Questa funzione e' coerente con il corso, perche' Python non costituisce un contenuto autonomo. Tuttavia, la riduzione della frizione tecnica non deve trasformarsi in perdita di controllo concettuale.

Lo studente non e' valutato per la capacita' di programmare autonomamente ogni parte del notebook. E' valutato per la capacita' di:

1. riconoscere gli oggetti teorici del problema;
2. delimitare cio' che puo' essere delegato all'IA;
3. controllare che il codice prodotto corrisponda alla specifica teorica;
4. verificare gli output;
5. interpretare i risultati in modo coerente con le ipotesi;
6. riconoscere i limiti del modello.

La responsabilita' dello studente resta quindi distribuita su tre piani:

1. responsabilita' teorico-modellistica nel Regime A;
2. responsabilita' di controllo computazionale nel Regime B;
3. responsabilita' verificativa e interpretativa nel Regime C.

La formula generale dell'uso virtuoso dell'IA nelle lezioni applicative e':

lo studente decide che cosa significa il problema; l'IA aiuta a renderlo computabile; lo studente verifica se il risultato e' coerente e che cosa significa sul piano finanziario.

## 16. Stato di avanzamento da mantenere aggiornato

Il progetto deve mantenere un registro di avanzamento per aree. Tale registro deve essere aggiornato periodicamente e non deve restare fissato allo stato iniziale del progetto.

| Area | Stato da monitorare | Nota |
|---|---|---|
| Struttura delle 16 lezioni | Consolidata nella nuova architettura | Include nuova Lezione 4, processi sdoppiati, Goal Programming e rimozione dell'applicazione binomiale autonoma |
| Notazione generale | Documento attivo | Da verificare durante lo sviluppo di ogni capitolo e applicazione |
| Manuale | In sviluppo progressivo | Da aggiornare capitolo per capitolo, mantenendo nomi file esplicativi |
| Slides | In sviluppo progressivo | Da produrre e revisionare lezione per lezione |
| Esercizi teorici | In sviluppo progressivo | Da collegare a manuale e slides |
| Applicazioni Python | Da strutturare secondo il formato laboratoriale | Cinque applicazioni previste alle Lezioni 4, 7, 10, 13 e 16 |
| Notebook/script Python | Da predisporre per ogni applicazione | Devono includere parti guidate e parti da completare |
| Dati applicativi | Da definire o simulare | Devono essere coerenti con i casi didattici |
| Grafici | Da produrre progressivamente | Devono essere coerenti con manuale, slides e codice |
| Uso dell'IA generativa | Da regolamentare nei materiali applicativi | Solo come supporto controllato |
| Compatibilita' SWP 5.5 | Da verificare | Evitare pacchetti LaTeX moderni non necessari |

Ogni volta che una lezione viene sviluppata, occorre aggiornare il Master Plan o il registro decisionale con:

1. titolo definitivo;
2. obiettivi didattici;
3. notazione introdotta;
4. formule principali;
5. esercizi prodotti;
6. grafici previsti o prodotti;
7. collegamenti Python;
8. materiali applicativi collegati;
9. eventuali dataset;
10. eventuali notebook o script;
11. questioni aperte.

Per le lezioni applicative, l'aggiornamento deve inoltre indicare:

1. caso applicativo;
2. prodotto computazionale finale;
3. strumenti Python introdotti;
4. tappe operative in aula;
5. estensione take-home;
6. criteri per l'eventuale uso dell'IA generativa.

## 17. Questioni aperte

Le principali questioni ancora aperte sono:

1. consolidare il template LaTeX del manuale;
2. consolidare il template LaTeX delle slides;
3. decidere se le soluzioni complete degli esercizi saranno incluse nel manuale o in un fascicolo separato;
4. definire il livello di dettaglio delle dimostrazioni;
5. verificare la coerenza della notazione introdotta nei nuovi capitoli con il file `MQF_Notazione.tex`;
6. decidere le librerie Python ammesse nelle applicazioni computazionali;
7. stabilire una strategia definitiva per la produzione dei grafici;
8. decidere se il materiale debba includere criteri di valutazione o prove d'esame;
9. definire il formato standard dei notebook o script applicativi;
10. definire il formato dei dataset didattici;
11. stabilire se le applicazioni Python saranno distribuite come `.py`, notebook Jupyter o entrambi;
12. verificare che i file master del manuale e delle slides recepiscano i nuovi nomi dei capitoli e delle lezioni;
13. verificare che la rimozione della lezione applicativa sugli alberi binomiali non lasci riferimenti residui nei capitoli, nelle slides o nei registri;
14. definire una convenzione per i blocchi di codice da completare in aula;
15. stabilire regole esplicite per l'uso dell'IA generativa da parte degli studenti;
16. predisporre prompt standard per debugging, spiegazione del codice e completamento locale di funzioni;
17. definire il formato delle estensioni take-home;
18. decidere se le consegne take-home saranno solo formative o anche valutabili;
19. stabilire una rubrica minima per valutare codice, controlli numerici e interpretazione finanziaria.

## 18. Principio guida finale

Il corso deve essere rigoroso nella notazione, selettivo nelle dimostrazioni, applicativo nell'interpretazione e coerente nella progressione didattica.

La qualita' del progetto dipendera' soprattutto dalla capacita' di mantenere un legame costante tra formalizzazione matematica, interpretazione finanziaria, esercizi, grafici e implementazioni computazionali.
