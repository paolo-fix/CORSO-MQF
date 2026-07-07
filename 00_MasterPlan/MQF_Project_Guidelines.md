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
| 1 | 4 | Probabilità, variabili casuali e condizionamento | Simulazioni, distribuzioni empiriche, momenti, quantili, stime condizionate |
| 2 | 7 | Traiettorie, simulazione e pricing Monte Carlo | Traiettorie GBM, OU, processi correlati, opzioni asiatiche, sistema OU--CIR |
| 3 | 10 | Rischio di credito | Matrici di transizione, simulazioni di rating, distribuzioni di perdita, VaR, CVaR |
| 4 | 13 | Asset Allocation e Asset Liability Management | Goal programming, allocazioni multicriterio, deviazioni da target, liability matching |
| 5 | 16 | Programmazione stocastica | Scenari, recourse, non anticipatività, confronto tra soluzioni deterministiche e stocastiche |

Le applicazioni Python devono essere concepite come laboratori di modellizzazione quantitativa. La finalità principale non è insegnare Python come contenuto autonomo, ma mostrare come un modello probabilistico, finanziario o ottimizzativo possa essere tradotto in una procedura computazionale controllabile, verificabile e interpretabile.

Ogni applicazione deve essere costruita intorno a un problema finanziario, probabilistico o decisionale identificabile. Il caso applicativo deve specificare:

1. il contesto finanziario, probabilistico o decisionale;
2. la domanda quantitativa da affrontare;
3. i dati disponibili, se presenti, oppure la procedura di generazione dei dati simulati;
4. i parametri del modello;
5. le grandezze da calcolare;
6. gli output numerici e grafici attesi;
7. i controlli numerici, logici e interpretativi;
8. il prodotto computazionale finale.

La lezione applicativa non deve concludersi genericamente con la scrittura di codice. Deve concludersi con un prodotto osservabile e interpretabile: una distribuzione simulata, una procedura di stima, un insieme di traiettorie, una distribuzione di perdita, una tabella di confronto, una soluzione ottimizzativa o un altro output coerente con il modello teorico.

---

### 14.1 Coppia caso aula / caso take-home

Per ciascuna lezione applicativa deve essere progettata una coppia di casi:

1. **caso aula**, sviluppato dal docente durante la lezione;
2. **caso take-home**, assegnato agli studenti come lavoro autonomo.

Il caso aula e il caso take-home non devono essere distinti da differenze strutturali nella procedura di costruzione. Entrambi devono essere progettati mediante la stessa architettura metodologica:

1. Scheda Costruzione Caso;
2. Scheda Caso;
3. Flusso logico-teorico risolutivo;
4. scomposizione in tappe input-output;
5. sequenza di prompt virtuosi;
6. notebook;
7. output numerici e grafici;
8. controlli;
9. interpretazione critica;
10. eventuale tracciato IA;
11. rubrica di valutazione.

La differenza tra caso aula e caso take-home riguarda il contesto finanziario, probabilistico o decisionale, e, se necessario, alcune scelte specifiche della linea risolutiva. Il caso take-home deve restare distinto dal caso aula, ma non deve richiedere una procedura metodologica diversa.

Il caso take-home non deve consistere in una semplice variazione parametrica del caso svolto in aula. Deve essere comparabile per struttura di lavoro, tipo di output, controlli richiesti e criteri di valutazione, ma collocato in un contesto diverso o in una formulazione finanziaria differenziata.

Per ogni coppia caso aula / caso take-home devono essere chiari:

1. quali concetti teorici vengono consolidati;
2. quali strumenti computazionali vengono utilizzati;
3. quali output devono essere prodotti;
4. quali controlli devono essere svolti;
5. quali elementi metodologici sono comuni ai due casi;
6. quali elementi distinguono il caso take-home dal caso aula;
7. quali parti sono svolte dal docente, quali dagli studenti e quali sono eventualmente assistite dall’IA.

---

### 14.2 Scheda Costruzione Caso

La precedente denominazione **“scheda docente di calibrazione”** è sostituita da **Scheda Costruzione Caso**.

La Scheda Costruzione Caso è il documento interno di progettazione del caso. Essa resta nelle mani del docente, ha funzione creativa primaria e deve essere redatta prima di tutte le altre fasi: prima della Scheda Caso, prima della scomposizione in tappe, prima della sequenza dei prompt e prima della costruzione del notebook.

La Scheda Costruzione Caso deve essere predisposta sia per il caso aula sia per il caso take-home. La sua funzione metodologica è la stessa nei due casi. La differenza riguarda soltanto l’uso didattico successivo dei materiali: nel caso aula il materiale sostiene lo sviluppo guidato in lezione; nel caso take-home sostiene la consegna assegnata agli studenti e la valutazione del notebook e del tracciato IA.

La Scheda Costruzione Caso deve contenere almeno:

1. identificazione della lezione e del tipo di caso;
2. titolo del caso;
3. contesto storico-finanziario, probabilistico o decisionale;
4. motivazione didattica del caso;
5. domanda quantitativa;
6. obiettivo didattico;
7. collegamento con le lezioni teoriche precedenti;
8. concetti teorici da rendere osservabili;
9. funzione della simulazione o della procedura computazionale;
10. ruolo dell’informazione, degli stati, degli scenari o dei vincoli;
11. grandezze economico-finanziarie;
12. variabili casuali o decisionali;
13. eventi, stati informativi o scenari;
14. formule principali;
15. quantità teoriche da stimare o calcolare;
16. proprietà teoriche da verificare;
17. parametri finanziari, probabilistici o computazionali;
18. soglie, target o vincoli rilevanti;
19. ipotesi modellistiche;
20. limiti del modello;
21. output richiesti: tabelle, grafici, stime, controlli;
22. Flusso logico-teorico risolutivo;
23. scomposizione attesa in tappe input-output;
24. sequenza docente dei prompt virtuosi, se l’uso dell’IA è previsto;
25. struttura attesa del notebook;
26. criteri di validazione del notebook;
27. criteri di valutazione del tracciato IA, se richiesto;
28. rubrica sintetica;
29. esito atteso e calibrazione qualitativa del caso.

La Scheda Costruzione Caso non deve essere confusa con la Scheda Caso. Essa può contenere informazioni non destinate direttamente agli studenti: scelte di progettazione, calibrazione qualitativa attesa, struttura dei prompt, criteri di validazione, criteri di valutazione e rubrica.

#### Flusso logico-teorico risolutivo

La Scheda Costruzione Caso deve includere una sezione dedicata al **Flusso logico-teorico risolutivo**.

Questa sezione costituisce il cuore intellettuale del caso. Il suo compito non è descrivere il codice, né anticipare la scomposizione operativa del notebook, ma ricostruire la sequenza dei richiami teorico-matematici necessari per passare dalla domanda quantitativa agli output richiesti.

Il flusso deve richiamare, nell’ordine logicamente utile alla soluzione:

1. definizioni matematiche rilevanti;
2. proprietà probabilistiche, finanziarie o ottimizzative;
3. teoremi o formule utilizzate;
4. collegamenti con le grandezze specifiche del caso;
5. output o controlli che discendono da ciascun passaggio teorico.

L’output obbligatorio della sezione è una tabella con la seguente struttura:

| Passo | Finalità risolutiva | Formula teorico-matematica / definizione / proprietà / teorema | Applicazione nel caso | Output o controllo collegato |
|---:|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |

La colonna **Passo** indica l’ordine logico ideale della soluzione.

La colonna **Finalità risolutiva** spiega perché quel richiamo teorico è necessario per procedere nella soluzione del caso.

La colonna **Formula teorico-matematica / definizione / proprietà / teorema** contiene il richiamo matematico essenziale, già introdotto nei capitoli teorici del corso o esplicitamente ammesso nella lezione applicativa.

La colonna **Applicazione nel caso** traduce il richiamo teorico negli oggetti specifici del caso: variabili, eventi, partizioni, distribuzioni, funzioni di perdita, vincoli, soglie o quantità da stimare.

La colonna **Output o controllo collegato** indica quale tabella, grafico, quantità numerica, verifica o controllo del notebook discende da quel passaggio teorico.

La sequenza del flusso logico-teorico deve guidare la successiva scomposizione in tappe input-output. Le tappe operative non devono nascere direttamente dal codice, ma dalla successione teorica fissata in questa tabella.

---

### 14.3 Scheda Caso

La precedente denominazione **“scheda macro”** è sostituita da **Scheda Caso**.

La Scheda Caso è il documento operativo derivato dalla Scheda Costruzione Caso. Essa contiene la descrizione del caso, il contesto, la domanda quantitativa, la specifica teorico-matematica essenziale, i parametri, le ipotesi, gli output richiesti e i controlli essenziali.

La Scheda Caso non contiene la progettazione docente interna: non contiene la rubrica completa, la calibrazione qualitativa attesa, la struttura dettagliata del notebook, né la sequenza docente completa dei prompt.

La Scheda Caso non deve contenere già svolto il Flusso logico-teorico risolutivo completo. Deve però fornire gli elementi necessari affinché docente e studenti possano ricostruirlo: contesto, domanda quantitativa, variabili, eventi, parametri, formule principali, quantità teoriche da stimare, output e controlli richiesti.

Per il caso aula, la Scheda Caso è input comune per docente e studenti. Per il caso take-home, la Scheda Caso è input operativo per gli studenti.

Nel lavoro con IA, la Scheda Caso costituisce il contenuto del **Prompt 1**, successivo al Prompt 0 di inizializzazione. Nel Prompt 1 l’IA deve solo acquisire la scheda come specifica vincolante e rispondere con una conferma minima. Non deve produrre sintesi, formule aggiuntive, codice, tappe operative, interpretazioni o suggerimenti.

La Scheda Caso deve indicare almeno:

1. titolo del caso;
2. tipo di caso: aula o take-home;
3. contesto finanziario, probabilistico o decisionale;
4. domanda quantitativa;
5. grandezze economico-finanziarie;
6. variabili casuali o decisionali;
7. eventi, stati informativi o scenari;
8. formule principali;
9. ipotesi modellistiche;
10. parametri;
11. soglie, target o vincoli;
12. quantità teoriche da stimare o calcolare;
13. output computazionali attesi;
14. controlli richiesti;
15. limiti del modello;
16. eventuale specifica congelata del caso.

La Scheda Caso non deve essere una soluzione del problema. Deve delimitare ciò che potrà essere sviluppato nel notebook e ciò che l’IA non potrà modificare.

---

### 14.4 Pacchetto dei materiali per ogni lezione applicativa

Per ogni lezione applicativa deve essere predisposto un pacchetto coerente di materiali. L’elenco seguente indica contenuti da produrre o rendere disponibili; non implica necessariamente file separati per ciascun elemento. Alcuni materiali possono essere documenti autonomi, altri possono essere sezioni interne del notebook, della scheda docente, della traccia take-home o del README della lezione.

#### Materiali principali

1. Scheda Costruzione Caso del caso aula;
2. Scheda Caso del caso aula;
3. notebook del caso aula;
4. Scheda Costruzione Caso del caso take-home;
5. Scheda Caso del caso take-home;
6. notebook del caso take-home, completo, semi-strutturato o da costruire progressivamente;
7. template del tracciato IA in formato Markdown, se il lavoro prevede uso documentato dell’IA;
8. rubrica di valutazione del notebook e del tracciato IA.

#### Sezioni o allegati obbligatori del pacchetto

1. lista dei parametri iniziali;
2. sequenza di tappe operative;
3. controlli intermedi;
4. output numerici attesi;
5. grafici o tabelle da produrre;
6. indicazioni per la discussione in aula;
7. successione di prompt virtuosi utilizzati o suggeriti;
8. criteri di validazione delle risposte IA, se l’IA è prevista.

#### Materiali eventuali

1. file dati;
2. file di configurazione dei parametri;
3. script Python esportati dal notebook;
4. figure generate dal notebook;
5. README della lezione applicativa.

Il README non è obbligatorio in ogni lezione, ma è consigliato quando il pacchetto contiene più file. Deve indicare almeno:

1. scopo della lezione applicativa;
2. elenco dei file;
3. ordine consigliato di utilizzo;
4. differenza tra materiali docente e materiali studente;
5. eventuali istruzioni per l’esecuzione del notebook;
6. eventuale ruolo del tracciato IA.

---

### 14.5 Procedura di sviluppo della lezione applicativa

La costruzione di una lezione applicativa deve seguire una procedura progressiva. L’ordine raccomandato è:

1. definizione della coppia caso aula / caso take-home;
2. redazione della Scheda Costruzione Caso del caso aula;
3. validazione della Scheda Costruzione Caso del caso aula;
4. derivazione della Scheda Caso del caso aula;
5. costruzione o validazione del Flusso logico-teorico risolutivo del caso aula;
6. scomposizione del caso aula in tappe input-output;
7. definizione della sequenza di prompt virtuosi per il caso aula, se l’IA è prevista;
8. costruzione iterativa del notebook del caso aula;
9. esecuzione e calibrazione degli output;
10. redazione della Scheda Costruzione Caso del caso take-home;
11. validazione della Scheda Costruzione Caso del caso take-home;
12. derivazione della Scheda Caso del caso take-home;
13. costruzione o validazione del Flusso logico-teorico risolutivo del caso take-home;
14. scomposizione del caso take-home in tappe input-output;
15. definizione della sequenza di prompt virtuosi per il caso take-home, se l’IA è prevista;
16. predisposizione del notebook del caso take-home, se previsto;
17. predisposizione del template del tracciato IA;
18. predisposizione della rubrica di valutazione.

Quando l’IA è usata nella costruzione o nello svolgimento della lezione, il processo non deve essere lineare nel senso:

```text
prompt
-> codice
-> risultato
```

Deve invece essere iterativo e controllato:

```text
Scheda Caso
-> Prompt 1: acquisizione non produttiva del caso
-> Prompt 2: costruzione del Flusso logico-teorico risolutivo
-> scomposizione in tappe
-> prompt di tappa
-> risposta IA
-> validazione docente o studente
-> cella Markdown e/o codice
-> esecuzione della cella
-> output osservabile
-> controllo
-> uso dell’output nella tappa successiva
```

La risposta dell’IA non deve essere copiata automaticamente nel notebook. Deve essere selezionata, corretta, ridotta o riformulata in funzione della specifica teorica del caso e dei vincoli didattici della lezione.

---

### 14.6 Notebook applicativo

Il notebook Jupyter è il formato ordinario delle lezioni applicative. Lo script Python può essere prodotto come materiale ausiliario o di esportazione, ma il notebook resta preferibile quando è necessario integrare testo, formule, codice, output, grafici e commenti interpretativi.

Il notebook non deve essere una semplice raccolta di celle di codice. Deve essere progettato come una catena di ragionamento quantitativo, in cui ogni blocco computazionale sia collegato a:

1. una domanda finanziaria, probabilistica o decisionale;
2. un oggetto teorico;
3. una formula o procedura;
4. un output;
5. un controllo;
6. una interpretazione.

La struttura consigliata del notebook è:

1. intestazione della lezione e descrizione del caso;
2. obiettivi applicativi;
3. premesse teorico-matematiche essenziali;
4. dati disponibili, parametri o procedura di simulazione;
5. librerie Python necessarie;
6. funzioni ausiliarie, se necessarie;
7. scomposizione del problema in tappe;
8. implementazione delle tappe;
9. controlli intermedi;
10. output numerici;
11. grafici e tabelle;
12. analisi di sensibilità, se appropriata;
13. interpretazione critica;
14. limiti del modello;
15. sintesi finale.

Quando il notebook viene costruito passo passo con supporto dell’IA, ogni prompt di tappa può richiedere simultaneamente:

1. una cella Markdown della tappa;
2. una cella codice Python, se prevista;
3. l’elenco degli output attesi;
4. il controllo da eseguire;
5. il collegamento con la tappa successiva.

La produzione simultanea di testo Markdown e codice Python è ammessa nel Regime B solo quando la specifica teorica della tappa è già stata fissata e validata. L’IA non deve modificare la struttura del caso, le variabili, le formule, gli stati informativi, gli scenari o il significato finanziario del problema.

Il notebook docente è il risultato validato del processo di sviluppo, non la trascrizione integrale della conversazione con l’IA. Il notebook studente può essere:

1. completo, se deve essere usato come materiale di studio;
2. semi-strutturato, se deve essere completato in aula o a casa;
3. parzialmente guidato, se alcune celle devono essere modificate, integrate o interpretate dagli studenti.

Il notebook deve evitare che gli studenti partano da un file vuoto, salvo scelta didattica esplicita. Le parti da completare, modificare o discutere devono essere chiaramente segnalate.

---

### 14.7 Tappe operative come moduli input/output

Le tappe operative devono essere progettate come moduli logici, non come celle isolate. Ogni tappa deve rendere esplicito il collegamento tra ciò che è già disponibile, ciò che viene trasformato e ciò che sarà utilizzato successivamente.

La struttura generale di una tappa è:

```text
input_k
-> operazione_k
-> output_k
-> uso in k+1
```

Per ciascuna tappa devono essere specificati:

1. input provenienti dalle tappe precedenti;
2. obiettivo della tappa;
3. regime IA prevalente, quando l’IA è prevista;
4. prompt virtuoso di riferimento, quando l’IA è prevista;
5. oggetti teorici coinvolti;
6. operazione computazionale richiesta;
7. output prodotto;
8. controllo numerico, logico o interpretativo;
9. uso dell’output nella tappa successiva.

Quando l’IA è utilizzata, la tappa deve essere letta anche come modulo di interazione controllata:

```text
input_k
-> prompt_k
-> risposta IA_k
-> validazione_k
-> cella notebook_k
-> output_k
-> controllo_k
-> uso in k+1
```

Una tappa può comprendere più celle:

1. cella Markdown di descrizione della tappa;
2. cella Markdown con input disponibili e output atteso;
3. cella codice per l’operazione computazionale;
4. cella codice o Markdown per il controllo;
5. cella Markdown per interpretazione locale o commento;
6. eventuale nota sul regime IA e sul prompt utilizzato.

Le tappe operative non devono essere mini-progetti indipendenti. Devono essere parti concatenate di un percorso comune, in cui ogni output rilevante contribuisce alla tappa successiva o al prodotto computazionale finale.

---

### 14.8 Criteri comuni per il codice Python

Il codice Python deve rispettare i seguenti criteri:

1. codice leggibile e ben commentato;
2. separazione tra dati, parametri, funzioni e output;
3. nomi delle variabili coerenti, per quanto possibile, con la notazione matematica;
4. preferenza per codice comprensibile rispetto a codice eccessivamente compatto;
5. controlli intermedi espliciti;
6. grafici leggibili e interpretabili;
7. interpretazione dei risultati dopo ogni blocco computazionale rilevante;
8. possibilità di modificare parametri, scenari e target;
9. riproducibilità dell’esecuzione;
10. tracciabilità del passaggio dalla formula matematica all’algoritmo.

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
10. analisi di sensibilità.

Quando possibile, il codice deve essere costruito in modo da permettere agli studenti di modificare parametri, soglie, scenari o target e osservare come cambiano gli output. Tuttavia, tali modifiche devono essere collegate a una domanda interpretativa e non ridursi a manipolazioni puramente tecniche.

---

### 14.9 Output numerici, grafici e prodotto finale osservabile

Ogni lezione applicativa deve concludersi con un prodotto finale osservabile. La lezione non deve concludersi genericamente con la scrittura di codice, ma con la comprensione di che cosa il codice permette di calcolare e di come tale calcolo modifichi o rafforzi l’interpretazione del modello teorico.

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

Gli output numerici devono essere accompagnati da controlli. Per ogni tabella o stima devono essere chiari:

1. la quantità teorica approssimata;
2. la procedura computazionale utilizzata;
3. l’unità di misura o la scala del risultato;
4. il controllo numerico o logico associato;
5. il significato economico-finanziario.

I grafici devono avere funzione diagnostica o interpretativa. Non devono essere output decorativi. Per ogni grafico devono essere esplicitati:

1. la variabile o le variabili rappresentate;
2. il confronto che il grafico deve rendere visibile;
3. eventuali soglie, stati, scenari o target da evidenziare;
4. la domanda interpretativa associata;
5. il collegamento con il modello teorico.

Quando il codice per il grafico viene prodotto con supporto dell’IA, lo studente o il docente devono comunque specificare le proprietà informative del grafico. L’IA può essere delegata alla realizzazione tecnica, ma non alla scelta del significato informativo del grafico.

---

### 14.10 Valutazione dei lavori take-home

Quando una lezione applicativa prevede un lavoro take-home, la valutazione deve riguardare congiuntamente:

1. notebook operativo;
2. output prodotti;
3. eventuale tracciato IA in formato Markdown;
4. interpretazione finale.

La valutazione non deve premiare la complessità autonoma del codice Python. Deve valutare la capacità dello studente di:

1. identificare correttamente le premesse teorico-matematiche;
2. scomporre il problema in tappe coerenti;
3. mantenere il legame input/output tra le tappe;
4. produrre output numerici, tabelle e grafici coerenti con il problema;
5. verificare gli output mediante controlli numerici, logici o interpretativi;
6. interpretare i risultati in modo proporzionato alle ipotesi del modello;
7. governare l’eventuale interazione con l’IA secondo i regimi definiti nella Sezione 15.

Il notebook e il tracciato IA, quando richiesto, devono essere coerenti tra loro. Output computazionali corretti ma ottenuti attraverso una delega opaca e non controllata non costituiscono uso virtuoso dell’IA. Allo stesso modo, prompt formalmente corretti ma non collegati agli output effettivi del notebook non sono sufficienti.

La rubrica di valutazione di ciascun caso take-home deve essere coerente con la scheda docente di calibrazione. I criteri minimi sono:

1. qualità delle premesse teorico-matematiche identificate;
2. correttezza della scomposizione in tappe;
3. coerenza degli input/output che collegano le tappe;
4. qualità degli output richiesti: stime, tabelle, grafici, controlli;
5. qualità e virtù degli input forniti all’IA, se il tracciato IA è richiesto;
6. rispetto dei regimi di interazione con l’IA, se l’IA è ammessa;
7. capacità di verifica e interpretazione critica.

---

### 14.11 Relazione con le slides e con il capitolo applicativo

La lezione applicativa deve essere coerente con il capitolo corrispondente del manuale e con le slides della lezione.

Il capitolo applicativo deve documentare il passaggio dalla formulazione teorica al prodotto computazionale finale. Deve spiegare il caso, la modellizzazione, la struttura del notebook, le quantità calcolate, i controlli e l’interpretazione.

Le slides devono orientare il lavoro in aula, selezionando i passaggi essenziali:

1. caso;
2. obiettivi;
3. formule operative;
4. tappe principali;
5. output attesi;
6. controlli;
7. interpretazione;
8. eventuale estensione take-home.

Il notebook contiene il codice completo o semi-completo e rappresenta il supporto operativo principale. Le slides non devono duplicare il notebook, ma devono aiutare lo studente a comprendere la logica del percorso e il ruolo delle singole tappe.

Quando l’IA è prevista nella lezione, la relazione tra slides, notebook e materiali IA deve essere chiara:

1. le slides introducono il ruolo controllato dell’IA;
2. il notebook mostra il risultato operativo validato;
3. il file dei prompt virtuosi documenta l’interazione metodologica;
4. il tracciato IA dello studente registra l’uso effettivo dello strumento;
5. la rubrica valuta la coerenza tra problema, input all’IA, output e interpretazione.

---

## 15. Uso virtuoso dell'IA generativa nelle lezioni applicative

L'uso di strumenti di intelligenza artificiale generativa può essere previsto nelle lezioni applicative come supporto controllato alla modellizzazione quantitativa. L'obiettivo non è insegnare l'IA come contenuto autonomo, né trasformare Python in un contenuto indipendente del corso. L'obiettivo è permettere agli studenti di osservare, simulare, verificare e interpretare modelli quantitativi applicati alla finanza.

Nel corso MQF, l'IA deve essere trattata come strumento di interazione metodologica. Essa può assistere lo studente nel passaggio dal problema economico-finanziario alla procedura computazionale, ma non deve sostituire la responsabilità dello studente nella definizione degli oggetti teorici, nella verifica degli output e nell'interpretazione finanziaria dei risultati.

L'uso virtuoso dell'IA non coincide con un uso minimo dello strumento. Uno studente può utilizzare l'IA in modo esteso e tuttavia corretto, se conserva il controllo della struttura teorica, delimita esplicitamente i compiti delegati, verifica gli output e formula autonomamente l'interpretazione finanziaria. L'uso improprio consiste invece nella delega opaca di passaggi che devono restare sotto responsabilità dello studente.

La Sezione 14 definisce l'architettura dei materiali applicativi e del notebook. La presente sezione definisce l'architettura dell'interazione con l'IA: regimi, prompt, validazione delle risposte, tracciato dello studente e criteri di valutazione.

---

### 15.1 Principio generale: l'IA come supporto, non come sostituto

L'IA può essere utilizzata nelle lezioni applicative per ridurre la frizione tecnica e per sostenere la traduzione operativa di un modello quantitativo in un notebook. Questa funzione è coerente con il corso, perché Python non costituisce un contenuto autonomo. Tuttavia, la riduzione della frizione tecnica non deve produrre perdita di controllo concettuale.

Lo studente non è valutato per la capacità di programmare autonomamente ogni parte del notebook. È valutato per la capacità di:

1. riconoscere gli oggetti teorici del problema;
2. distinguere variabili, eventi, stati, scenari, ipotesi e formule;
3. delimitare ciò che può essere delegato all'IA;
4. controllare che il codice prodotto corrisponda alla specifica teorica;
5. verificare gli output numerici e grafici;
6. interpretare i risultati in modo coerente con le ipotesi;
7. riconoscere i limiti del modello.

La formula generale dell'uso virtuoso dell'IA nelle lezioni applicative è:

```text
lo studente decide che cosa significa il problema;
l'IA aiuta a renderlo computabile;
lo studente verifica se il risultato è coerente;
lo studente interpreta il risultato sul piano finanziario.
```

---

### 15.2 Uso virtuoso e uso improprio

Si parla di uso virtuoso dell'IA quando lo studente formula richieste delimitate, coerenti con il problema assegnato e accompagnate da vincoli espliciti. Un prompt virtuoso non chiede all'IA di risolvere globalmente il problema, ma specifica il contesto, indica gli oggetti già definiti, chiarisce il compito e stabilisce che cosa non deve essere modificato.

Sono esempi di uso virtuoso:

1. chiedere all'IA di aiutare a distinguere variabili casuali, eventi, stati informativi, scenari, ipotesi e quantità teoriche, senza risolvere il problema;
2. chiedere all'IA di costruire una procedura Python coerente con una specifica teorica già validata;
3. chiedere all'IA di produrre il codice necessario per un grafico di cui lo studente ha già specificato le proprietà informative;
4. chiedere all'IA di segnalare ambiguità, errori logici o conclusioni troppo forti in una verifica o interpretazione già formulata dallo studente;
5. usare l'IA per correggere errori tecnici, migliorare la leggibilità del codice o organizzare output numerici e grafici, senza modificare il significato matematico-finanziario del problema.

Sono esempi di uso improprio:

1. chiedere all'IA di scegliere autonomamente il modello da utilizzare;
2. chiedere all'IA di definire variabili casuali, eventi, formule o ipotesi senza successiva validazione critica;
3. chiedere all'IA di risolvere direttamente l'intero caso applicativo;
4. chiedere all'IA di produrre l'interpretazione finanziaria finale;
5. accettare output numerici o grafici senza controllare la coerenza con la formula, con il codice e con il problema;
6. presentare come verifica autonoma una certificazione di correttezza prodotta dall'IA;
7. usare prompt privi di contesto, lasciando all'IA il compito di ricostruire il problema;
8. utilizzare codice generato dall'IA senza comprendere quali variabili, formule o ipotesi siano state implementate.

La distinzione tra uso virtuoso e uso improprio non riguarda quindi la presenza o assenza dell'IA, ma il controllo esercitato dallo studente sulla sequenza di lavoro.

---

### 15.3 I tre regimi dell'interazione studente--IA

L'interazione con l'IA nelle lezioni applicative deve essere organizzata secondo tre regimi. I regimi rappresentano tre funzioni diverse dello strumento e tre diversi livelli di responsabilità dello studente.

#### Regime A — Ricognizione teorico-modellistica

Nel Regime A, l'IA viene utilizzata per aiutare lo studente a riconoscere gli oggetti teorici coinvolti nel problema.

Lo studente può chiedere supporto per distinguere:

1. grandezze economico-finanziarie;
2. variabili casuali o decisionali;
3. eventi;
4. stati informativi;
5. scenari;
6. ipotesi;
7. formule candidate;
8. quantità teoriche da calcolare;
9. controparte empirica o computazionale delle quantità teoriche;
10. limiti del modello che dovranno essere considerati.

L'IA non deve risolvere il problema, scegliere autonomamente il modello finale o produrre direttamente la soluzione matematica completa. In questo regime, l'autonomia dello studente riguarda la costruzione del significato matematico del problema. L'IA può proporre una mappa concettuale, ma lo studente deve validarla, correggerla e trasformarla in una specifica teorica coerente.

Formula guida del Regime A:

> Aiutami a riconoscere gli oggetti teorici del problema, senza risolverlo.

#### Regime B — Traduzione operativa in codice

Nel Regime B, l'IA viene utilizzata per rendere computabile una specifica teorica già definita e validata. In questo regime, lo studente può delegare all'IA la costruzione dell'apparato computazionale, pur mantenendo il controllo sulla sostanza teorica del problema.

L'IA può essere utilizzata per:

1. costruire dataset simulati;
2. definire strutture dati;
3. scegliere nomi di variabili Python coerenti;
4. organizzare la sequenza delle celle;
5. scrivere codice Python;
6. produrre tabelle;
7. produrre output numerici;
8. implementare tecnicamente grafici;
9. inserire controlli computazionali;
10. migliorare leggibilità e modularità del codice.

Il vincolo fondamentale è che l'IA non deve modificare la sostanza matematica del problema. Variabili casuali, eventi, stati, scenari, formule e ipotesi devono restare quelli emersi e validati nel Regime A. L'IA può scegliere la forma computazionale più conveniente, ma non può cambiare ciò che deve essere calcolato.

Formula guida del Regime B:

> Data questa specifica teorica validata, costruisci l'apparato computazionale, senza modificarla.

Nel caso dei grafici, la distinzione tra contenuto informativo e realizzazione tecnica è essenziale. Lo studente deve specificare quale variabile rappresentare, quale confronto mostrare, quale soglia evidenziare e quale domanda interpretativa il grafico deve rendere visibile. L'IA può essere delegata alla realizzazione tecnica del grafico, ma non alla scelta del suo significato informativo.

#### Regime C — Verifica e interpretazione critica

Nel Regime C, l'IA viene utilizzata come revisore critico. Lo studente deve prima formulare un controllo, una verifica o un'interpretazione. Solo dopo può chiedere all'IA di segnalare errori, ambiguità, passaggi non giustificati, confusioni terminologiche o conclusioni troppo forti.

L'IA può aiutare a individuare:

1. incoerenze tra formula teorica e codice;
2. incoerenze tra codice e output;
3. controlli numerici mancanti;
4. controlli logici mancanti;
5. confusione tra quantità teorica e stima empirica;
6. interpretazioni finanziarie troppo forti;
7. limiti del modello non dichiarati;
8. affermazioni non supportate dagli output prodotti.

L'IA non deve produrre la conclusione finale al posto dello studente. In questo regime, l'autonomia dello studente è massima: l'IA non interpreta, ma critica un'interpretazione già proposta.

Formula guida del Regime C:

> Valuta criticamente la verifica e l'interpretazione che ho scritto, senza sostituirti a me.

---

### 15.4 Due scale di lavoro: macro e micro

I tre regimi operano su due scale diverse:

1. livello macro, relativo al problema complessivo;
2. livello micro, relativo alla singola tappa.

Al livello macro, i tre regimi servono a costruire il percorso risolutivo. L'obiettivo non è ancora produrre codice o risultati numerici, ma inquadrare il problema, generare un percorso, fissare le tappe principali e verificare che la sequenza sia logicamente coerente.

Al livello micro, i tre regimi servono invece a svolgere un passaggio specifico del percorso: specificare l'oggetto teorico locale, costruire la procedura computazionale corrispondente, controllare l'output e interpretarne il ruolo.

Al livello macro, la sequenza è:

1. Regime A: inquadramento teorico del problema complessivo;
2. Regime B: progettazione del percorso computazionale;
3. Regime C: revisione critica del percorso risolutivo.

Al livello micro, la sequenza è:

1. Regime A: specificazione teorica della tappa;
2. Regime B: operazionalizzazione computazionale della tappa;
3. Regime C: verifica e interpretazione locale della tappa.

Questa distinzione impedisce che l'IA passi direttamente dal testo del problema al codice completo. Prima si costruisce il percorso, poi si lavora sulle singole tappe.

---

### 15.5 Sequenza iterativa: dal prompt al notebook

Quando l'IA è utilizzata nello sviluppo di una lezione applicativa o nello svolgimento di un take-home, il processo non deve essere lineare nel senso:

```text
prompt -> codice -> risultato
```

La sequenza corretta è iterativa e controllata:

```text
tappa_k
-> prompt_k
-> risposta IA_k
-> validazione_k
-> cella notebook_k
-> output_k
-> controllo_k
-> uso in k+1
```

Questa sequenza significa che la risposta dell'IA non viene trasferita automaticamente nel notebook. Deve essere valutata, corretta, ridotta, riformulata o scartata. Solo dopo validazione può diventare parte del notebook, sotto forma di cella Markdown, cella codice, tabella, grafico o controllo.

La validazione può essere svolta dal docente, nel notebook docente, oppure dallo studente, nel lavoro take-home. In entrambi i casi devono essere chiari:

1. quale tappa si sta svolgendo;
2. quali input erano disponibili;
3. quale regime IA era ammesso;
4. quale prompt è stato utilizzato;
5. quale parte della risposta IA è stata accettata;
6. quale parte è stata modificata o rifiutata;
7. quale cella notebook è stata prodotta;
8. quale output è stato ottenuto;
9. quale controllo è stato svolto;
10. come l'output viene usato nella tappa successiva.

Quando il notebook viene costruito passo passo con supporto dell’IA, ogni prompt di tappa deve richiedere esplicitamente gli elementi da trasferire nel notebook:

1. cella Markdown della tappa;
2. cella codice, se prevista;
3. output attesi;
4. controllo da eseguire;
5. collegamento con la tappa successiva.

La sequenza dei prompt virtuosi deve essere tracciabile rispetto alla struttura del notebook. Ogni prompt rilevante deve poter essere collegato a una o più sezioni del notebook e deve chiarire quale parte del prodotto finale genera: cella Markdown, cella codice, tabella, grafico, controllo, interpretazione locale o revisione critica.

Nella scheda docente di calibrazione, il docente deve quindi predisporre una mappa esplicita tra prompt e notebook. Questa mappa ha doppia funzione: guida lo sviluppo del notebook docente e fornisce un riferimento per valutare la coerenza tra tracciato IA e notebook nei lavori take-home.

---

### 15.6 Prompt zero, Prompt 1, Prompt 2 e prompt di tappa

La qualità di un prompt dipende anche dalla quantità di contesto fornito all’IA. Un prompt di tappa formalmente corretto può produrre risposte deboli se viene usato in una chat nuova senza avere prima definito il contesto del corso, del caso e dei regimi di interazione.

Per le lezioni applicative che prevedono uso documentato dell’IA, la sequenza iniziale deve distinguere:

1. Prompt zero;
2. Prompt 1 — acquisizione della Scheda Caso;
3. Prompt 2 — costruzione del Flusso logico-teorico risolutivo;
4. prompt di tappa.

#### Prompt zero

Il Prompt zero è il prompt di contesto iniziale. Si usa una sola volta all’inizio di una nuova chat. Serve a definire il perimetro generale della conversazione.

Il Prompt zero generale non deve anticipare il contenuto del caso. Deve indicare:

1. corso e livello degli studenti;
2. obiettivo generale del lavoro applicativo;
3. distinzione tra notebook e tracciato IA;
4. regimi di interazione A, B e C;
5. regole operative generali;
6. divieto di anticipare caso, modello, variabili, dati, scenari, parametri o output;
7. richiesta di risposta minima di conferma.

Salvo diversa indicazione del docente, il Prompt zero deve essere non produttivo. Non deve chiedere all’IA di generare contenuti teorici, codice, formule, esempi, Schede Caso, scomposizioni, piani di lavoro o sintesi del caso.

Forma raccomandata della chiusura del Prompt zero generale:

```text
Per ora questo è solo un prompt di inizializzazione del contesto.
Non produrre contenuti teorici, codice, formule, esempi, schede, scomposizioni, piani di lavoro o sintesi del caso.
Rispondi soltanto confermando che hai compreso i vincoli generali e che attenderai il prossimo prompt.
```

#### Prompt 1 — acquisizione della Scheda Caso

Il Prompt 1 segue il Prompt zero e contiene la Scheda Caso.

La funzione del Prompt 1 è esclusivamente vincolante e non produttiva. Lo studente fornisce all’IA la Scheda Caso e chiede soltanto di acquisirla come specifica del lavoro.

L’IA deve rispondere con una conferma minima. Non deve produrre sintesi, formule aggiuntive, codice, scomposizioni, interpretazioni, controlli o suggerimenti.

Forma raccomandata del Prompt 1:

```text
Ti fornisco la Scheda Caso. Devi soltanto leggerla e acquisirla come specifica vincolante del lavoro.
Non devi produrre sintesi, formule aggiuntive, codice, tappe operative, interpretazioni, controlli o suggerimenti.
Rispondi soltanto “OK, scheda acquisita” se tutto è chiaro.
```

#### Prompt 2 — Flusso logico-teorico risolutivo

Il Prompt 2 è obbligatorio nei lavori applicativi con uso documentato dell’IA. Deve essere formulato in **Regime A**.

La finalità del Prompt 2 è costruire, con supporto dell’IA, il Flusso logico-teorico risolutivo del caso.

Il Prompt 2 deve contenere un contributo esplicito dello studente. Lo studente deve proporre una prima sequenza degli elementi teorici che ritiene necessari per la soluzione del caso: definizioni, proprietà, formule, teoremi, variabili, eventi, partizioni, quantità da stimare e controlli teorici.

L’IA può aiutare a verificare, completare e ordinare tale sequenza, ma non deve sostituire integralmente il lavoro dello studente. Il contributo iniziale dello studente deve restare visibile nel tracciato IA.

Forma raccomandata del Prompt 2:

```text
Regime A — Ricognizione teorico-modellistica.

Sulla base della Scheda Caso acquisita, devo costruire il Flusso logico-teorico risolutivo.
Secondo me gli elementi teorici necessari, nell’ordine logico utile alla soluzione, sono:

1. [parte proposta dallo studente]
2. [parte proposta dallo studente]
3. [parte proposta dallo studente]

Ti chiedo di aiutarmi a verificare, completare e ordinare questa sequenza teorica, senza scrivere codice e senza proporre ancora la scomposizione operativa del notebook.

L’output deve essere una tabella con le colonne:
Passo;
Finalità risolutiva;
Formula teorico-matematica / definizione / proprietà / teorema;
Applicazione nel caso;
Output o controllo collegato.

Devi segnalare chiaramente eventuali elementi teorici mancanti, ridondanti o fuori ordine rispetto alla soluzione del caso.
```

L’output obbligatorio del Prompt 2 è la tabella:

| Passo | Finalità risolutiva | Formula teorico-matematica / definizione / proprietà / teorema | Applicazione nel caso | Output o controllo collegato |
|---:|---|---|---|---|

Prompt generici del tipo “costruisci il flusso logico-teorico del caso” sono considerati deboli, perché non rendono osservabile il contributo teorico dello studente.

#### Prompt di tappa

Il prompt di tappa è utilizzabile solo dopo che sono stati acquisiti:

1. Prompt zero;
2. Scheda Caso tramite Prompt 1;
3. Flusso logico-teorico risolutivo tramite Prompt 2;
4. scomposizione in tappe validata.

Il prompt di tappa deve indicare almeno:

1. numero e titolo della tappa;
2. input disponibili;
3. regime richiesto;
4. compito della tappa;
5. vincoli specifici;
6. output atteso;
7. controllo da eseguire;
8. collegamento con la tappa successiva.

I prompt brevi di avanzamento, come “ok, tappa k”, sono ammissibili solo se il contesto, la Scheda Caso, il Flusso logico-teorico risolutivo e la scomposizione in tappe sono già stati fissati e validati nella stessa conversazione.

---

### 15.7 Grammatica del prompt virtuoso

Un prompt virtuoso deve rendere visibili il contesto, il regime dell'interazione e i limiti del compito assegnato all'IA. La struttura generale del prompt deve includere, quando rilevante, i seguenti elementi:

1. contesto del problema;
2. input disponibili;
3. oggetti teorici già definiti;
4. regime richiesto: A, B oppure C;
5. compito richiesto all'IA;
6. vincoli su ciò che l'IA non deve modificare o produrre;
7. output atteso;
8. controllo richiesto;
9. uso dell'output nella tappa successiva.

La grammatica minima è:

```text
Sto lavorando su [caso/problema].
La tappa corrente è [titolo tappa].
Gli input disponibili sono [input].
Il regime richiesto è [A/B/C].
Gli oggetti teorici già fissati sono [oggetti].
Devi svolgere [compito].
Non devi [vincoli negativi].
L'output atteso è [formato].
L'output sarà usato per [tappa successiva].
```

Nel Regime A, il prompt deve orientare la ricognizione teorica:

> Aiutami a distinguere grandezze, variabili, eventi, informazione, ipotesi e quantità teoriche. Non risolvere il problema, non scegliere il modello finale e non scrivere codice.

Nel Regime B, il prompt deve vincolare la costruzione computazionale:

> Data questa specifica teorica, costruisci il codice o l'output richiesto. Puoi scegliere la forma tecnica della procedura, ma non modificare variabili, eventi, formule, ipotesi o significato finanziario.

Nel Regime C, il prompt deve trasformare l'IA in revisore critico:

> Ho scritto questa verifica o interpretazione. Segnala errori, ambiguità e affermazioni troppo forti, ma non riscrivere il testo al posto mio.

Un prompt privo di contesto, di input e di vincoli tende a produrre risposte generiche. Un prompt troppo ampio, come “risolvi il problema”, trasferisce all'IA responsabilità che nel corso devono restare allo studente.

La portabilità contestuale è parte integrante della qualità del prompt. Un prompt formalmente corretto ma comprensibile solo all'interno della conversazione originaria non deve essere considerato pienamente virtuoso, se è destinato a essere riutilizzato dagli studenti o documentato come esempio didattico.

---

### 15.8 Validazione della risposta IA

Ogni risposta dell'IA deve essere validata prima di essere trasferita nel notebook o nel tracciato finale. La validazione non è un atto formale, ma un controllo sostanziale di coerenza.

La validazione deve considerare almeno:

1. coerenza con il regime richiesto;
2. coerenza con gli input disponibili;
3. rispetto degli oggetti teorici già fissati;
4. assenza di modifiche non autorizzate al modello;
5. assenza di contenuti non ancora trattati o non ammessi;
6. correttezza della traduzione computazionale, se il regime è B;
7. pertinenza dei controlli proposti, se il regime è C;
8. utilità dell'output per la tappa successiva.

Una risposta IA deve essere corretta o scartata quando:

1. cambia variabili, eventi, formule o ipotesi senza richiesta esplicita;
2. introduce modelli più avanzati non previsti dalla lezione;
3. produce codice non collegato alla specifica teorica;
4. interpreta risultati non ancora calcolati;
5. propone conclusioni finanziarie non supportate dagli output;
6. confonde quantità teoriche e stime empiriche;
7. sostituisce la verifica dello studente con una dichiarazione generica di correttezza.

Nel notebook docente, la validazione può rimanere implicita se il materiale finale è già pulito e coerente. Nel tracciato IA dello studente, invece, deve essere visibile almeno in forma sintetica: accettazione, modifica, rifiuto o correzione della risposta ottenuta.

---

### 15.9 Tracciato IA dello studente

Quando il lavoro take-home prevede uso documentato dell'IA, lo studente deve consegnare un tracciato dell'interazione in formato Markdown `.md`.

Il tracciato non deve essere valutato come prova forense dell'intera storia privata del lavoro svolto con strumenti IA. Deve essere valutato come artefatto metodologico: esso deve mostrare come lo studente ha organizzato l'assistenza dell'IA secondo una sequenza controllata di ricognizione teorico-modellistica, traduzione operativa in codice, verifica e interpretazione critica.

Il tracciato deve contenere:

1. identificazione del problema;
2. Prompt zero utilizzato, se previsto;
3. Prompt 1 con acquisizione della Scheda Caso;
4. conferma non produttiva dell’IA al Prompt 1;
5. Prompt 2 in Regime A per la costruzione del Flusso logico-teorico risolutivo;
6. contributo iniziale dello studente al Flusso logico-teorico risolutivo;
7. risposta IA utilizzata per verificare, completare o ordinare il flusso;
8. azione dello studente sulla risposta IA: accettazione, modifica, rifiuto o correzione;
9. tabella finale del Flusso logico-teorico risolutivo;
10. scomposizione del problema in tappe;
11. collegamenti input/output tra tappe;
12. prompt utilizzati;
13. regime attribuito a ciascun prompt;
14. risposta IA utilizzata, oppure sintesi fedele della parte effettivamente utilizzata;
15. azione dello studente: accettazione, modifica, rifiuto o correzione;
16. output prodotto;
17. controllo svolto;
18. interpretazione finale autonoma.

Se lo studente utilizza un prompt zero, esso deve essere riportato una sola volta all'inizio del tracciato. I prompt successivi possono essere più brevi, purché siano chiaramente collegati al contesto iniziale e alle tappe del lavoro.

Se lo studente non utilizza un prompt zero, ogni prompt di tappa deve essere sufficientemente autosufficiente. In questo caso il tracciato deve mostrare che l'IA ha ricevuto contesto, input, vincoli e output atteso in misura sufficiente.

I prompt dello studente devono essere riportati integralmente. Le risposte dell'IA possono essere sintetizzate se molto lunghe, ma la sintesi deve indicare chiaramente quale parte della risposta è stata effettivamente utilizzata.

Il numero di prompt deve rispettare l’intervallo stabilito dal docente per ciascun caso take-home. Tale intervallo viene indicato nella Scheda Costruzione Caso e deve essere comunicato agli studenti nella Scheda Caso o nella traccia del lavoro.

Un tracciato troppo breve tende a indicare una delega globale e non controllata. Un tracciato eccessivamente lungo tende a rendere difficile la valutazione e può indicare assenza di organizzazione. Il vincolo sul numero minimo e massimo di prompt ha quindi funzione didattica: obbliga lo studente a decomporre il problema senza produrre un materiale ingestibile.

---

### 15.10 Struttura consigliata del tracciato IA

Il tracciato IA dello studente deve avere una struttura stabile. La struttura consigliata è:

# Tracciato IA

## 1. Identificazione del caso

- Lezione:
- Titolo del caso:
- Obiettivo quantitativo:
- Output finale richiesto:

## 2. Prompt zero, se utilizzato

Riportare integralmente il Prompt zero.

## 3. Prompt 1 — Acquisizione della Scheda Caso

Riportare integralmente il Prompt 1 e allegare o richiamare la Scheda Caso fornita all’IA.

**Risposta IA attesa:** conferma minima di acquisizione.

**Controllo dello studente:** verificare che l’IA non abbia prodotto sintesi, codice, formule aggiuntive, tappe operative o suggerimenti.

## 4. Prompt 2 — Flusso logico-teorico risolutivo

**Regime:** A — Ricognizione teorico-modellistica.

**Contributo iniziale dello studente:**

Riportare la sequenza teorica proposta dallo studente prima dell’intervento dell’IA.

**Prompt utilizzato:**

Riportare integralmente il Prompt 2.

**Risposta IA utilizzata o sintesi fedele:**

Indicare quali parti della risposta IA sono state utilizzate per verificare, completare o ordinare il flusso.

**Azione dello studente:**

Accettazione / modifica / rifiuto / correzione.

**Flusso logico-teorico risolutivo finale:**

| Passo | Finalità risolutiva | Formula teorico-matematica / definizione / proprietà / teorema | Applicazione nel caso | Output o controllo collegato |
|---:|---|---|---|---|

## 5. Scomposizione in tappe

| Tappa | Input | Operazione | Output | Controllo | Uso successivo |
|---:|---|---|---|---|---|

## 6. Interazioni con l’IA per le tappe operative

### Tappa k — Titolo della tappa

**Regime:** A / B / C

**Input disponibili:**

...

**Prompt utilizzato:**

...

**Risposta IA utilizzata o sintesi fedele:**

...

**Azione dello studente:**

Accettazione / modifica / rifiuto / correzione.

**Output prodotto nel notebook:**

...

**Controllo svolto:**

...

**Uso dell’output nella tappa successiva:**

...

## 7. Interpretazione finale

Testo autonomo dello studente.

## 8. Limiti del modello

Discussione dei principali limiti teorici, computazionali o finanziari.

La struttura può essere adattata dal docente in funzione della specifica lezione applicativa, ma deve sempre rendere visibile la relazione tra Scheda Caso, Flusso logico-teorico risolutivo, prompt, risposta IA, decisione dello studente, notebook e output.

---

### 15.11 Valutazione del tracciato IA

La valutazione del tracciato IA riguarda il modo in cui lo studente ha utilizzato l’IA nel processo di costruzione del lavoro. Non riguarda la qualità intrinseca delle risposte prodotte dall’IA.

Il docente valuta quindi:

1. la qualità dei prompt formulati dallo studente;
2. la chiarezza dei vincoli imposti all’IA;
3. il rispetto dei regimi A/B/C;
4. il contributo teorico iniziale dello studente;
5. la capacità di verificare, correggere o selezionare criticamente le risposte IA;
6. la tracciabilità del passaggio da prompt a notebook;
7. la presenza di controlli numerici, logici e interpretativi;
8. l’autonomia dell’interpretazione finale.

Il tracciato IA è valutato come documento metodologico. Deve rendere visibile il processo seguito dallo studente: che cosa è stato chiesto all’IA, con quali vincoli, quale risposta è stata utilizzata, quale decisione è stata presa dallo studente, quale output è stato trasferito nel notebook e quale controllo è stato svolto.

#### Oggetto della valutazione

La valutazione deve concentrarsi sui seguenti elementi.

| Area | Cosa si valuta | Indicatori positivi |
|---|---|---|
| Prompt zero | Inizializzazione corretta del contesto | il prompt definisce corso, livello, regimi A/B/C, distinzione tra notebook e tracciato IA, e chiede una conferma non produttiva |
| Prompt 1 | Acquisizione della Scheda Caso | l’IA riceve la Scheda Caso come specifica vincolante e risponde solo con una conferma minima |
| Prompt 2 | Costruzione del Flusso logico-teorico risolutivo | lo studente propone una sequenza teorica iniziale e chiede all’IA di verificarla, completarla e ordinarla |
| Regime A | Ricognizione teorico-modellistica | l’IA è usata per chiarire oggetti teorici, formule, definizioni, proprietà e collegamenti logici, senza produrre codice |
| Regime B | Traduzione operativa in codice | l’IA traduce in Python una specifica già validata, senza modificare variabili, formule, scenari, parametri o output richiesti |
| Regime C | Verifica e interpretazione critica | l’IA è usata per controllare, correggere o criticare output e interpretazioni già formulate dallo studente |
| Validazione | Controllo delle risposte IA | lo studente segnala errori, omissioni, ambiguità o modifiche non autorizzate introdotte dall’IA |
| Collegamento al notebook | Tracciabilità del lavoro | ogni uso dell’IA è collegato a una sezione del notebook, a un output prodotto e a un controllo svolto |
| Interpretazione finale | Autonomia critica | l’interpretazione finale è scritta dallo studente e l’IA è usata solo per revisione critica, non per sostituzione |

#### Valutazione specifica del Prompt 2

Il Prompt 2 ha un ruolo centrale perché avvia la costruzione del Flusso logico-teorico risolutivo. La sua valutazione deve considerare il contributo iniziale dello studente.

Sono indicatori positivi:

1. proposta iniziale dello studente non vuota e non generica;
2. presenza di definizioni, proprietà, formule o teoremi pertinenti;
3. ordine logico almeno parzialmente motivato;
4. collegamento tra richiami teorici e quantità da stimare;
5. collegamento tra richiami teorici e output richiesti;
6. richiesta all’IA di verificare, completare e ordinare, non di sostituire integralmente;
7. correzione o selezione critica della risposta IA;
8. tabella finale coerente con la Scheda Caso.

Sono indicatori deboli:

1. Prompt 2 formulato come richiesta generica del tipo “costruisci il flusso logico-teorico del caso”;
2. assenza di contributo teorico iniziale dello studente;
3. elenco puramente nominale copiato dalla Scheda Caso;
4. confusione tra flusso logico-teorico e scomposizione operativa del notebook;
5. accettazione integrale della risposta IA senza controllo;
6. flusso finale non collegato agli output richiesti.

#### Criteri generali di qualità

Un tracciato IA è di buona qualità se mostra che lo studente ha usato l’IA come supporto controllato. In particolare, deve risultare chiaro che lo studente:

1. ha fornito all’IA un contesto adeguato;
2. ha delimitato il compito dell’IA;
3. ha dichiarato il regime di interazione;
4. ha formulato prompt specifici e verificabili;
5. ha costruito il Flusso logico-teorico con un contributo personale visibile;
6. ha validato la scomposizione in tappe;
7. ha usato l’IA per produrre o correggere codice solo dopo avere fissato la specifica teorica;
8. ha controllato gli output numerici e grafici;
9. ha corretto eventuali errori dell’IA;
10. ha mantenuto autonoma l’interpretazione finale.

#### Elementi penalizzanti

Sono elementi penalizzanti:

1. uso di prompt generici come “risolvi il caso” o “scrivi tutto il notebook”;
2. assenza del Prompt 1 di acquisizione non produttiva della Scheda Caso;
3. assenza del Prompt 2 o Prompt 2 privo di contributo iniziale dello studente;
4. mancata distinzione tra Regime A, Regime B e Regime C;
5. produzione di codice prima della validazione della specifica teorica;
6. modifica non autorizzata di variabili, formule, parametri, scenari o output richiesti;
7. assenza di controlli sulle risposte IA;
8. trasferimento nel notebook di risultati non verificati;
9. interpretazione finale generata dall’IA senza bozza autonoma dello studente;
10. tracciato non collegato in modo chiaro alle sezioni del notebook.

#### Uso degli errori dell’IA nella valutazione

Gli errori commessi dall’IA non penalizzano automaticamente lo studente. Diventano rilevanti solo in relazione al comportamento dello studente.

Un errore dell’IA è valutato positivamente se lo studente lo riconosce, lo segnala e lo corregge. Diventa invece elemento negativo se lo studente lo accetta senza controllo e lo trasferisce nel notebook o nell’interpretazione finale.

Pertanto, nella valutazione del tracciato IA, il punto centrale non è se l’IA abbia prodotto una risposta perfetta, ma se lo studente abbia mantenuto il controllo teorico, operativo e interpretativo del lavoro.

---

### 15.12 Rapporto tra notebook e tracciato IA

Il notebook e il tracciato IA sono artefatti distinti ma collegati.

Il notebook deve mostrare il prodotto computazionale validato:

1. celle Markdown;
2. celle codice;
3. output numerici;
4. tabelle;
5. grafici;
6. controlli;
7. interpretazioni locali e finali.

Il tracciato IA deve mostrare il processo metodologico che ha condotto, con eventuale supporto dell'IA, alla costruzione del notebook:

1. prompt;
2. regime;
3. risposta IA utilizzata;
4. decisione dello studente;
5. output collegato;
6. controllo;
7. uso nella tappa successiva.

Il notebook non deve diventare un archivio completo della conversazione con l'IA. Il tracciato IA non deve sostituire il notebook. Il primo documenta il prodotto operativo; il secondo documenta la qualità del governo dell'interazione con lo strumento.

Output computazionali corretti ma ottenuti attraverso una delega opaca e non controllata non costituiscono uso virtuoso dell'IA. Allo stesso modo, prompt formalmente ordinati ma non collegati agli output effettivi del notebook non sono sufficienti.

---

### 15.13 Responsabilità finale dello studente

La responsabilità dello studente resta distribuita su tre piani:

1. responsabilità teorico-modellistica nel Regime A;
2. responsabilità di controllo computazionale nel Regime B;
3. responsabilità verificativa e interpretativa nel Regime C.

L'IA può aiutare a produrre testo, codice, tabelle, grafici e controlli, ma non può assumere la responsabilità finale del significato quantitativo-finanziario del lavoro.

In particolare, lo studente deve essere in grado di spiegare:

1. perché le variabili utilizzate sono appropriate;
2. quali eventi, stati o scenari sono stati definiti;
3. quali formule sono state implementate;
4. quali output numerici sono stati prodotti;
5. quali controlli sono stati svolti;
6. quali limiti ha il modello;
7. quale interpretazione finanziaria è giustificata dagli output.

Un lavoro applicativo con IA è accettabile solo se, al termine, lo studente conserva la capacità di ricostruire il passaggio:

```text
ipotesi
-> modello
-> codice
-> output
-> controllo
-> interpretazione
```

La finalità didattica non è ridurre il lavoro dello studente, ma aumentare la qualità del suo controllo sul processo quantitativo.

---

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
6. decidere in modo stabile le librerie Python ammesse nelle applicazioni computazionali;
7. stabilire una strategia definitiva per la produzione, il salvataggio e il richiamo dei grafici;
8. decidere se il materiale debba includere criteri di valutazione formale o solo strumenti di autovalutazione e valutazione formativa;
9. verificare che i file master del manuale e delle slides recepiscano i nuovi nomi dei capitoli e delle lezioni;
10. verificare che la rimozione della lezione applicativa autonoma sugli alberi binomiali non lasci riferimenti residui nei capitoli, nelle slides o nei registri;
11. definire una convenzione stabile per i blocchi di codice da completare in aula e nei notebook studente;
12. calibrare, dopo lo sviluppo completo della Lezione 4, la dimensione effettiva del pacchetto dei materiali applicativi, verificando quali documenti debbano restare autonomi e quali possano essere incorporati nel notebook, nella scheda docente o nel README;
13. verificare, dopo la prima applicazione Python, se la distinzione tra prompt zero, prompt breve di tappa e prompt autosufficiente debba essere mantenuta per tutte le lezioni applicative o adattata in funzione della complessità del caso;
14. definire, per ciascuna applicazione successiva, il numero minimo e massimo di prompt ammessi nel tracciato IA dello studente;
15. precisare se le consegne take-home saranno solo formative, valutabili in itinere o integrate nella valutazione finale;
16. costruire rubriche specifiche per ciascun caso take-home, sulla base della rubrica generale definita nelle Sezioni 14 e 15;
17. verificare la coerenza tra notebook docente, notebook studente, tracciato IA e rubrica di valutazione dopo la prima implementazione completa della Lezione 4;
18. definire il livello di integrazione tra simulazione di GBM/OU/processi correlati, pricing di opzioni asiatiche e sistema OU--CIR nella Lezione 7;
19. stabilire il caso applicativo specifico della Lezione 13: asset allocation multicriterio pura, liability matching, oppure formulazione integrata di Asset Liability Management;
20. precisare se la Lezione 16 userà un caso semplificato di asset allocation multistadio o un modello più ricco con vincoli di portafoglio e passività.

## 18. Principio guida finale

Il corso deve essere rigoroso nella notazione, selettivo nelle dimostrazioni, applicativo nell'interpretazione e coerente nella progressione didattica.

La qualita' del progetto dipendera' soprattutto dalla capacita' di mantenere un legame costante tra formalizzazione matematica, interpretazione finanziaria, esercizi, grafici e implementazioni computazionali.
