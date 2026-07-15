# Metodi Quantitativi per la Finanza - Linee guida di progetto

## 1. Identificazione del progetto

Il progetto riguarda la predisposizione completa del materiale didattico per il corso universitario Metodi Quantitativi per la Finanza.
Il corso e' destinato a studenti del quinto anno del corso di laurea in Banca e Risk Management. Gli studenti hanno una preparazione mediamente solida nei metodi quantitativi e statistici, e una preparazione buona nella teoria finanziaria e nei modelli finanziari.
Il materiale deve quindi mantenere un livello accademico rigoroso, evitando sia un approccio eccessivamente divulgativo sia un formalismo astratto non motivato dalle applicazioni finanziarie.

Il corso deve essere sviluppato in italiano. Il manuale, le slides e i materiali matematici devono essere scritti in LaTeX compatibile con Scientific WorkPlace 5.5.
Questo documento, invece, e' scritto in Markdown per essere caricato su GitHub e usato come linea guida operativa nelle future chat dedicate allo sviluppo del progetto.

## 2. Funzione e formato delle guidelines

Queste guidelines hanno una funzione di coordinamento: definiscono l'impostazione didattica, i prodotti finali, i vincoli tecnici e le regole operative da rispettare nella produzione del materiale del corso.

Il formato piu' idoneo per questo documento e' Markdown, con estensione `.md`, perche':

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

Il manuale e le slides devono essere scritti in LaTeX compatibile con Scientific WorkPlace 5.5.

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
  MQF_Istruzioni_Studente_Uso_Virtuoso_IA_Casi_Applicativi.md
  MQF_Registro_Esercizi.tex
  MQF_Registro_Grafici.tex
  MQF_Registro_Decisioni.tex

  /Templates
    MQF_Catalogo_Template.md
    /LaTeX
    /Markdown
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

#### 9.1.1 Standard degli esercizi nei capitoli teorici

Ogni capitolo teorico deve contenere, prima della sintesi finale e in questo ordine, le sezioni `Esercizi svolti` ed `Esercizi proposti`. Il riferimento operativo e' il template LaTeX registrato in `Templates/MQF_Catalogo_Template.md`.

Si applicano le seguenti regole:

1. ogni esercizio usa l'ambiente standard `exercise`, gia' definito nel master del manuale;
2. il titolo facoltativo dell'esercizio deve essere breve, descrittivo e privo di formule inutilmente complesse;
3. ogni sezione e ogni esercizio deve avere un'etichetta univoca che includa il numero del capitolo, secondo forme quali `sec:cap08-esercizi-svolti` ed `ex:cap08-matrice-transizione`;
4. l'enunciato deve rendere espliciti dati, unita' di misura, ipotesi e oggetti matematici necessari;
5. le richieste multiple devono essere organizzate con `enumerate` e devono procedere, quando possibile, dal calcolo o dalla formulazione al controllo e all'interpretazione economico-finanziaria;
6. negli esercizi svolti la soluzione completa segue immediatamente l'ambiente `exercise`, introdotta da `\noindent` e `\textbf{Soluzione.}`; non si usa un ambiente `solution`;
7. la soluzione deve riprendere l'ordine e la numerazione delle richieste, motivare i passaggi essenziali e concludersi con un'interpretazione quando il contenuto lo consente;
8. negli esercizi proposti non si inserisce lo svolgimento completo; si riportano soltanto, quando utili, i risultati essenziali per l'autovalutazione, introdotti da `\textit{Risultati:}`;
9. gli esercizi proposti devono avere difficolta' progressiva e coprire sia la comprensione matematica sia il significato finanziario dei risultati;
10. come riferimento orientativo, un capitolo teorico contiene da tre a quattro esercizi svolti e da quattro a sei esercizi proposti; il numero puo' variare in funzione dell'estensione e della difficolta' del capitolo;
11. la sintassi deve restare prudente e compatibile con Scientific WorkPlace 5.5: ambienti LaTeX standard, formule leggibili e nessun pacchetto aggiuntivo introdotto soltanto per impaginare gli esercizi.

Lo standard disciplina la forma editoriale e didattica, ma non sostituisce il Registro degli esercizi del Master Plan, che definisce gli argomenti da coprire, ne' `MQF_Stato_Avanzamento.md`, che registra lo stato effettivo di realizzazione.

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

Le slides devono essere prodotte in LaTeX Beamer compatibile con Scientific WorkPlace 5.5, riutilizzando il preambolo ufficiale gia' adottato nelle lezioni precedenti. In particolare, vanno mantenuti la classe `beamer`, il tema `Madrid`, le macro matematiche ufficiali del progetto e la struttura dei frame compatibile con Scientific WorkPlace 5.5.

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
%*
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

Anche per le lezioni prevalentemente teoriche di tipo P, la durata effettiva al netto del break e' assunta pari a 2 ore, cioe' circa 120 minuti.

La progettazione delle slides deve quindi essere calibrata su tale durata, prevedendo:

1. un numero di slides compatibile con spiegazione, esempi e discussione;
2. almeno due momenti applicativi o esercizi in aula;
3. pause concettuali dopo blocchi definitori o tecnici;
4. equilibrio tra formule, testo, grafici e interpretazioni.

E' preferibile una sequenza di slides leggibile a una singola slide eccessivamente densa. Ogni slide deve avere un obiettivo didattico riconoscibile.

## 12. Slides delle lezioni applicative di tipo C

Le slides delle lezioni applicative di tipo C devono essere progettate come strumento di regia del laboratorio. La loro funzione non è anticipare integralmente il notebook, insegnare Python come contenuto autonomo o documentare tutta l'interazione con l'IA. La loro funzione è guidare docente e studenti nello svolgimento del caso aula: lettura della Scheda Caso, uso dei prompt, costruzione progressiva del notebook, esecuzione dei controlli, discussione degli output e assegnazione del take-home.

Nelle lezioni di tipo C gli studenti lavorano alla propria postazione, preferibilmente in ambiente VS Code/Jupyter. Il docente indica i prompt da utilizzare, li fa inserire materialmente dagli studenti, discute le risposte dell'IA, seleziona le parti utili, guida la costruzione delle celle del notebook e controlla gli output. Le slides devono sostenere questa sequenza operativa.

---

### 12.1 Ordine di produzione delle slides applicative

Le slides applicative devono essere prodotte dopo la soluzione del caso aula e dopo la validazione del notebook docente. Non devono essere progettate in astratto prima di avere osservato come il caso si sviluppa effettivamente attraverso prompt, risposte dell'IA, celle Markdown, codice, output e controlli.

L'ordine di produzione raccomandato è:

1. redazione della Scheda Costruzione Caso;
2. derivazione della Scheda Caso;
3. svolgimento del caso aula con Prompt zero, Prompt 1, Prompt 2, Prompt 3 e prompt di tappa;
4. costruzione e validazione del notebook docente;
5. selezione degli elementi utili alla conduzione della lezione;
6. costruzione delle slides applicative;
7. revisione della consegna take-home alla luce del caso aula svolto.

Questa sequenza è necessaria perché gli elementi davvero utili per le slides emergono durante la soluzione del caso: passaggi teorici da richiamare, istruzioni Python da spiegare, prompt da mostrare, controlli da enfatizzare, criticità dell'IA da discutere e output da interpretare.

---

### 12.2 Funzione delle slides durante la lezione

Durante la lezione applicativa, le slides devono aiutare il docente a governare il ritmo del laboratorio e devono aiutare gli studenti a capire che cosa stanno facendo nel notebook.

Ogni gruppo di slides deve chiarire:

1. quale parte del caso si sta affrontando;
2. quale prompt deve essere usato o quale tappa deve essere svolta;
3. quale cella del notebook si vuole costruire;
4. quale output deve essere prodotto;
5. quale controllo consente di validare l'output;
6. quale interpretazione locale o finale è richiesta.

Le slides non devono sostituire il notebook. Il notebook contiene il lavoro operativo validato; le slides guidano la sua costruzione in aula.

---

### 12.3 Contenuti da ricavare dal notebook docente

Il notebook docente validato è la fonte principale per costruire le slides della lezione applicativa. Dalla soluzione del caso aula devono essere estratti solo gli elementi necessari alla conduzione della lezione.

Gli elementi da considerare sono:

1. formule, definizioni o collegamenti teorici indispensabili per la tappa;
2. grandezze finanziarie, eventi, scenari, vincoli o variabili decisionali che strutturano il caso;
3. prompt che devono essere effettivamente inseriti dagli studenti;
4. frammenti di codice o istruzioni Python che richiedono spiegazione;
5. tabelle, grafici e output numerici con valore didattico;
6. controlli numerici, logici e interpretativi da svolgere in aula;
7. criticità emerse nella costruzione del notebook e utili alla discussione.

Le parti puramente esecutive restano nel notebook. Le risposte complete dell'IA restano nel tracciato IA. Le slides devono mostrare gli snodi che servono a condurre la lezione.

---

### 12.4 Piano generale delle slides applicative

Le slides di una lezione applicativa devono seguire un piano coerente con lo svolgimento effettivo del laboratorio.

La struttura di riferimento è:

1. apertura della lezione e collocazione del caso nel corso;
2. presentazione della Scheda Caso e della domanda quantitativa;
3. richiamo del protocollo di lavoro con IA, notebook e tracciato;
4. sequenza iniziale dei prompt: Prompt zero, Prompt 1, Prompt 2 e Prompt 3;
5. sviluppo guidato delle tappe del notebook;
6. controlli intermedi e discussione degli output;
7. verifica conclusiva del notebook e interpretazione finale;
8. assegnazione del caso take-home.

La struttura può essere adattata alla complessità del caso, ma deve mantenere il legame tra prompt, notebook, output e controlli.

---

### 12.5 Slides di tappa

La parte centrale della lezione applicativa è composta da slides di tappa. Ogni tappa deve corrispondere a un passaggio riconoscibile del notebook.

Una slide di tappa deve indicare, in forma sintetica:

1. input disponibili;
2. obiettivo della tappa;
3. prompt o regime IA utilizzato;
4. cella Markdown o cella code da costruire;
5. output atteso;
6. controllo da eseguire;
7. uso dell'output nella tappa successiva.

Quando una tappa è complessa, è preferibile separare la slide di orientamento, la slide con il prompt, la slide sul codice essenziale, la slide sull'output e la slide di controllo. Una slide troppo densa rallenta il laboratorio e rende difficile seguire la costruzione del notebook.

---

### 12.6 Prompt, codice e output nelle slides

I prompt devono comparire nelle slides solo quando servono alla conduzione dell'aula. Un prompt completo va inserito in slide quando deve essere copiato dagli studenti. Negli altri casi è sufficiente indicare regime, obiettivo del prompt, input disponibili, output atteso e vincoli principali.

Il codice Python deve comparire nelle slides solo quando serve a spiegare una scelta operativa non immediata. Non devono essere riportate intere celle già presenti nel notebook, salvo che il docente voglia discutere un passaggio specifico.

Gli output devono essere selezionati in base alla loro funzione didattica. Una tabella o un grafico entra nelle slides se aiuta a discutere una quantità teorica, un confronto, una soglia, un controllo o un'interpretazione. Gli output estesi restano nel notebook.

---

### 12.7 Gestione del tempo della lezione applicativa

Ciascuna lezione applicativa ha durata complessiva di 2 ore e 15 minuti, con 15 minuti di pausa. Il tempo effettivo di lavoro è quindi pari a circa 120 minuti.

Nella progettazione delle slides occorre stimare il tempo necessario per lo sviluppo del caso aula. Il tempo non coincide con la semplice esposizione del docente: include inserimento dei prompt, attesa delle risposte dell'IA, selezione delle risposte, costruzione delle celle, esecuzione del notebook, controllo degli output e discussione.

Per la Lezione 4, che introduce per la prima volta il protocollo applicativo con IA, una scansione realistica è:

1. 20--25 minuti per presentare il protocollo generale delle lezioni applicative;
2. 10 minuti per presentare la Scheda Caso aula;
3. 15--20 minuti per Prompt zero, Prompt 1, Prompt 2 e Prompt 3;
4. 45--50 minuti per sviluppare le tappe centrali del notebook;
5. 15 minuti per controlli, output finali e interpretazione;
6. 5--10 minuti per assegnare il take-home e richiamare le regole di consegna.

Nelle lezioni applicative successive, il protocollo generale deve essere richiamato brevemente. Il tempo recuperato deve essere destinato allo sviluppo del caso aula, ai controlli e alla discussione degli output.

---

### 12.8 Specificità della Lezione 4

La Lezione 4 ha una funzione diversa dalle altre lezioni applicative, perché introduce il metodo di lavoro che verrà riutilizzato nelle successive lezioni di tipo C.

Le slides della Lezione 4 devono quindi presentare in modo esplicito:

1. ruolo della Scheda Caso;
2. differenza tra notebook e tracciato IA;
3. funzione di Prompt zero, Prompt 1, Prompt 2 e Prompt 3;
4. distinzione tra Regime A, Regime B e Regime C;
5. modalità di lavoro in VS Code/Jupyter;
6. regole di consegna del take-home;
7. criteri generali di valutazione.

Nelle lezioni applicative successive questi elementi non devono essere ripetuti integralmente, ma solo richiamati quando servono a governare il caso specifico.

---

### 12.9 Controllo finale della progettazione delle slides

Prima di considerare definitive le slides di una lezione applicativa, occorre verificare che esse permettano al docente di condurre effettivamente il laboratorio.

La revisione finale deve rispondere a queste domande:

1. lo studente capisce quale caso sta risolvendo e perché;
2. la sequenza dei prompt è collocata nel punto giusto della lezione;
3. ogni tappa del notebook è collegata a un output e a un controllo;
4. il codice mostrato è essenziale e non duplica il notebook;
5. gli output scelti per le slides hanno una funzione interpretativa;
6. i tempi sono compatibili con 120 minuti effettivi;
7. il take-home è presentato come estensione coerente del caso aula.

Se una slide non aiuta a orientare il lavoro, introdurre un prompt, costruire una cella, discutere un output, eseguire un controllo o preparare il take-home, deve essere eliminata o spostata nel notebook o nei materiali operativi.



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

1. caso aula, sviluppato dal docente durante la lezione;
2. caso take-home, assegnato agli studenti come lavoro autonomo.

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

La Scheda Costruzione Caso è il documento interno di progettazione del caso. Essa resta nelle mani del docente, ha funzione creativa primaria e deve essere redatta prima di tutte le altre fasi: prima della Scheda Caso, prima della scomposizione in tappe, prima della sequenza dei prompt e prima della costruzione del notebook.

La Scheda Costruzione Caso deve essere predisposta sia per il caso aula sia per il caso take-home. La sua funzione metodologica è la stessa nei due casi. La differenza riguarda soltanto l’uso didattico successivo dei materiali: nel caso aula il materiale sostiene lo sviluppo guidato in lezione; nel caso take-home sostiene la consegna assegnata agli studenti e la valutazione del notebook e del tracciato IA.

La struttura operativa canonica e' conservata nel template Markdown registrato in `Templates/MQF_Catalogo_Template.md`. Le schede compilate per le singole lezioni sono istanze del template e restano nelle rispettive cartelle applicative.

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
25. mappa prompt--notebook, con indicazione degli elementi del notebook generati da ciascun prompt rilevante;
26. struttura attesa del notebook;
27. criteri di validazione del notebook;
28. criteri di valutazione del tracciato IA, se richiesto;
29. rubrica sintetica;
30. esito atteso e calibrazione qualitativa del caso.

La Scheda Costruzione Caso non deve essere confusa con la Scheda Caso. Essa può contenere informazioni non destinate direttamente agli studenti: scelte di progettazione, calibrazione qualitativa attesa, struttura dei prompt, criteri di validazione, criteri di valutazione e rubrica.

#### Flusso logico-teorico risolutivo

La Scheda Costruzione Caso deve includere una sezione dedicata al Flusso logico-teorico risolutivo.

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

La colonna Passo indica l’ordine logico ideale della soluzione.

La colonna Finalità risolutiva spiega perché quel richiamo teorico è necessario per procedere nella soluzione del caso.

La colonna Formula teorico-matematica / definizione / proprietà / teorema contiene il richiamo matematico essenziale, già introdotto nei capitoli teorici del corso o esplicitamente ammesso nella lezione applicativa.

La colonna Applicazione nel caso traduce il richiamo teorico negli oggetti specifici del caso: variabili, eventi, partizioni, distribuzioni, funzioni di perdita, vincoli, soglie o quantità da stimare.

La colonna Output o controllo collegato indica quale tabella, grafico, quantità numerica, verifica o controllo del notebook discende da quel passaggio teorico.

La sequenza del flusso logico-teorico deve guidare la successiva scomposizione in tappe input-output. Le tappe operative non devono nascere direttamente dal codice, ma dalla successione teorica fissata in questa tabella.

---

### 14.3 Scheda Caso

La Scheda Caso è il documento operativo derivato dalla Scheda Costruzione Caso. Essa contiene la descrizione del caso, il contesto, la domanda quantitativa, la specifica teorico-matematica essenziale, i parametri, le ipotesi, gli output richiesti e i controlli essenziali.

La Scheda Caso non contiene la progettazione docente interna: non contiene la rubrica completa, la calibrazione qualitativa attesa, la struttura dettagliata del notebook, né la sequenza docente completa dei prompt.

La Scheda Caso non deve contenere già svolto il Flusso logico-teorico risolutivo completo. Deve però fornire gli elementi necessari affinché docente e studenti possano ricostruirlo: contesto, domanda quantitativa, variabili, eventi, parametri, formule principali, quantità teoriche da stimare, output e controlli richiesti.

Per il caso aula, la Scheda Caso è input comune per docente e studenti. Per il caso take-home, la Scheda Caso è input operativo per gli studenti.

Nel lavoro con IA, la Scheda Caso costituisce il contenuto informativo del Prompt 1, successivo al Prompt zero di inizializzazione. La Scheda Caso resta la specifica vincolante del problema e non deve contenere istruzioni operative rivolte all'IA.

Il Prompt 1 concreto può però contenere, dopo la Scheda Caso, un'istruzione operativa esterna alla scheda: produrre una sola cella Markdown iniziale di inquadramento da inserire nel notebook. Questa cella deve sintetizzare il caso senza risolverlo. Non deve introdurre formule, variabili, parametri, ipotesi o output non presenti nella Scheda Caso; non deve produrre codice, flusso logico-teorico, scomposizione in tappe, risultati numerici, interpretazioni o suggerimenti risolutivi.

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
7. istruzioni per la consegna del tracciato IA, ordinariamente mediante stampa PDF della chat, se il lavoro prevede uso documentato dell’IA;
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
17. predisposizione delle istruzioni per la consegna del tracciato IA;
18. predisposizione della rubrica di valutazione.

Quando l’IA è usata nella costruzione o nello svolgimento della lezione, il processo non deve essere lineare nel senso:

```text
prompt
-> codice
-> risultato
```

Deve invece essere iterativo e controllato:

```text
Prompt zero: inizializzazione del contesto
-> Prompt 1: Scheda Caso e cella Markdown iniziale di inquadramento
-> Prompt 2: costruzione del Flusso logico-teorico risolutivo
-> Prompt 3: scomposizione in tappe input-output
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

La struttura consigliata del notebook, quando l'applicazione prevede uso documentato dell'IA, è:

1. cella Markdown iniziale di inquadramento prodotta dal Prompt 1;
2. cella Markdown con il Flusso logico-teorico risolutivo prodotto dal Prompt 2;
3. cella Markdown con la scomposizione in tappe input-output prodotta dal Prompt 3;
4. librerie Python necessarie;
5. dati disponibili, parametri o procedura di simulazione;
6. implementazione progressiva delle tappe;
7. controlli intermedi;
8. output numerici;
9. grafici e tabelle;
10. verifica conclusiva della coerenza tra notebook e Scheda Caso, se richiesta;
11. interpretazione critica finale dello studente;
12. verifica conclusiva dell'interpretazione, se richiesta;
13. limiti del modello e sintesi finale.

Quando l'applicazione non prevede uso documentato dell'IA, la stessa struttura può essere adattata mantenendo comunque il collegamento tra caso, flusso teorico, tappe, output, controlli e interpretazione.

Quando il notebook viene costruito passo passo con supporto dell’IA, ogni prompt di tappa può richiedere simultaneamente:

1. una cella Markdown della tappa;
2. una cella codice Python, se prevista;
3. l’elenco degli output attesi;
4. il controllo da eseguire;
5. il collegamento con la tappa successiva.

La produzione simultanea di testo Markdown e codice Python è ammessa nel Regime B solo quando la specifica teorica della tappa è già stata fissata e validata. L’IA non deve modificare la struttura del caso, le variabili, le formule, gli stati informativi, gli scenari o il significato finanziario del problema.

Il notebook finale deve restare pulito, lineare ed eseguibile. Non deve conservare celle errate duplicate. Se una criticità concettuale viene accolta in Regime C, le celle della tappa coinvolta devono essere sostituite con versioni corrette e informative. La traccia della verifica deve essere incorporata nelle celle sostitutive, non aggiunta come cella extra: devono risultare visibili la criticità individuata, l'origine della criticità nella risposta dell'IA e la modifica adottata.

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
3. tracciato IA, ordinariamente consegnato come stampa PDF della chat, quando richiesto;
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

La rubrica di valutazione di ciascun caso take-home deve essere coerente con la Scheda Costruzione Caso. I criteri minimi sono:

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

#### Regime C — Verifica critica

Nel Regime C, l'IA viene utilizzata come revisore critico di materiale già prodotto o di un dubbio già formulato dallo studente. Il Regime C non consiste in una richiesta generica di certificazione del lavoro. Deve partire da un risultato numerico anomalo, da un dubbio teorico o matematico, da una possibile incoerenza con la Scheda Caso, da un passaggio di codice non convincente, da una tabella o da un grafico da verificare.

Lo studente deve indicare:

1. la parte del notebook interessata;
2. il dubbio, l'anomalia o la possibile incoerenza;
3. il proprio ragionamento, cioè perché il risultato, la formula, il testo o il codice non convince;
4. il materiale da controllare.

La risposta dell'IA deve classificare l'esito della verifica in uno solo dei due casi:

1. criticità respinta, quando il dubbio dello studente non richiede modifiche al notebook;
2. criticità accolta, quando il dubbio segnala un errore, una incoerenza, una ambiguità o una debolezza effettiva.

Se la criticità è respinta, il notebook non viene modificato. La verifica resta documentata nel tracciato IA.

Se la criticità è accolta, il notebook viene corretto senza aggiungere celle extra di verifica. Le celle della tappa interessata vengono sostituite con versioni corrette e informative. La cella Markdown della tappa deve incorporare in modo sintetico:

1. la criticità individuata;
2. l'origine della criticità nella risposta dell'IA;
3. la modifica adottata.

Se è necessario correggere anche il codice, la nuova cella code sostituisce la precedente e può contenere solo commenti essenziali collegati alla correzione.

Gli errori puramente tecnici di codice, come errori di sintassi, librerie mancanti o warning segnalati dall'ambiente di sviluppo, vanno corretti sostituendo la cella errata. Non costituiscono però, di per sé, verifiche critiche di alto valore.

L'IA non deve produrre la conclusione finale al posto dello studente. Restano distinte le verifiche conclusive sul notebook e sull'interpretazione finale, quando previste.

Formula guida del Regime C:

> Ho individuato un dubbio o una possibile criticità. Verifica se la criticità è respinta o accolta. Se è accolta, produci le celle sostitutive della tappa, senza celle extra e senza modificare la Scheda Caso.

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

Nella Scheda Costruzione Caso, il docente deve quindi predisporre una mappa esplicita tra prompt e notebook. Questa mappa ha doppia funzione: guida lo sviluppo del notebook docente e fornisce un riferimento per valutare la coerenza tra tracciato IA e notebook nei lavori take-home.

Per il Regime C la sequenza è specifica:

```text
dubbio dello studente
-> Prompt C
-> risposta IA: criticità respinta oppure criticità accolta
-> se criticità respinta: nessuna modifica al notebook
-> se criticità accolta: sostituzione delle celle della tappa coinvolta
```

Il notebook documenta il prodotto corretto e validato; il tracciato IA documenta il processo di verifica che ha portato alla decisione.

---

### 15.6 Prompt zero, Prompt 1, Prompt 2, Prompt 3 e prompt di tappa

La qualità di un prompt dipende anche dalla quantità di contesto fornito all’IA. Un prompt di tappa formalmente corretto può produrre risposte deboli se viene usato in una chat nuova senza avere prima definito il contesto del corso, del caso e dei regimi di interazione.

Per le lezioni applicative che prevedono uso documentato dell’IA, la sequenza iniziale deve distinguere:

1. Prompt zero;
2. Prompt 1 — acquisizione della Scheda Caso e cella Markdown iniziale;
3. Prompt 2 — costruzione del Flusso logico-teorico risolutivo;
4. Prompt 3 — scomposizione in tappe input-output;
5. prompt di tappa.

#### Prompt zero

Il Prompt zero è il prompt di contesto iniziale. Si usa una sola volta all’inizio di una nuova chat. Serve a definire il perimetro generale della conversazione.

Il testo fisso canonico del Prompt zero e' conservato nel template Markdown registrato in `Templates/MQF_Catalogo_Template.md`. Deve essere riutilizzato senza riscritture locali; eventuali modifiche generali richiedono prima l'aggiornamento delle presenti Guidelines e poi del template.

#### Prompt 1 — Scheda Caso e cella Markdown iniziale

Il Prompt 1 segue il Prompt zero e contiene la Scheda Caso. È fornito dal docente e non richiede contributo autonomo dello studente.

La funzione del Prompt 1 è vincolante: l'IA deve acquisire la Scheda Caso come specifica del lavoro e non deve modificarla. Il Prompt 1 deve però chiedere anche una sola cella Markdown iniziale da inserire nel notebook. Questa cella ha funzione di inquadramento del caso, non di soluzione.

La cella Markdown iniziale deve sintetizzare:

1. titolo del caso;
2. contesto economico-finanziario, probabilistico o decisionale;
3. domanda quantitativa;
4. variabile finale di interesse;
5. informazione disponibile;
6. quantità principali da stimare;
7. output richiesti;
8. controlli principali;
9. vincolo che la Scheda Caso non deve essere modificata.

Il testo canonico del Prompt 1 e' conservato nel corrispondente template Markdown registrato nel Catalogo dei template. La Scheda Caso costituisce la parte variabile; le istruzioni successive costituiscono la parte fissa.

Se l'IA produce formule aggiuntive, codice, tappe operative, interpretazioni o suggerimenti risolutivi, lo studente deve riportarla al vincolo del Prompt 1.

#### Prompt 2 — Flusso logico-teorico risolutivo

Il Prompt 2 è obbligatorio nei lavori applicativi con uso documentato dell’IA. Deve essere formulato in Regime A.

La finalità del Prompt 2 è costruire, con supporto dell’IA, il Flusso logico-teorico risolutivo del caso.

Il Prompt 2 deve contenere un contributo esplicito dello studente. Lo studente deve proporre una prima sequenza degli elementi teorici che ritiene necessari per la soluzione del caso: definizioni, proprietà, formule, teoremi, variabili, eventi, partizioni, quantità da stimare e controlli teorici.

L’IA può aiutare a verificare, completare e ordinare tale sequenza, ma non deve sostituire integralmente il lavoro dello studente. Il contributo iniziale dello studente deve restare visibile nel tracciato IA.

Il testo canonico del Prompt 2 e' conservato nel corrispondente template Markdown. La proposta iniziale dello studente costituisce la parte variabile e non deve essere precompilata dal docente o dall'IA.

L’output obbligatorio del Prompt 2 è la tabella:

| Passo | Finalità risolutiva | Formula teorico-matematica / definizione / proprietà / teorema | Applicazione nel caso | Output o controllo collegato |
|---:|---|---|---|---|

Prompt generici del tipo “costruisci il flusso logico-teorico del caso” sono considerati deboli, perché non rendono osservabile il contributo teorico dello studente.

#### Prompt 3 — Scomposizione in tappe input-output

Il Prompt 3 è obbligatorio nei lavori applicativi con uso documentato dell'IA. Deve essere formulato dopo il Prompt 2.

La finalità del Prompt 3 è trasformare il Flusso logico-teorico risolutivo in una scomposizione operativa del notebook. Anche il Prompt 3 deve contenere un contributo esplicito dello studente: una proposta iniziale di tappe, con input, operazione, output e controllo.

L'IA può aiutare a verificare, completare e ordinare la scomposizione, ma non deve produrre direttamente il notebook e non deve modificare la Scheda Caso.

Il testo canonico del Prompt 3 e' conservato nel corrispondente template Markdown. La prima proposta di tappe costituisce la parte variabile e deve rendere visibile il contributo dello studente.

Prompt generici del tipo “dividi il problema in tappe” sono considerati deboli se non rendono visibile una proposta iniziale dello studente.

#### Prompt di tappa

Il prompt di tappa è utilizzabile solo dopo che sono stati acquisiti:

1. Prompt zero;
2. Scheda Caso e cella Markdown iniziale tramite Prompt 1;
3. Flusso logico-teorico risolutivo tramite Prompt 2;
4. scomposizione in tappe input-output tramite Prompt 3.

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

I testi canonici dei prompt di tappa in Regime A, B e C sono conservati in tre template Markdown distinti, registrati nel Catalogo dei template. La separazione evita di confondere il contributo teorico dello studente nei Regimi A e C con la richiesta tecnica semplificata propria del Regime B.

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

La grammatica minima e le formulazioni operative dei tre regimi sono rese concrete nei template dei prompt di tappa registrati nel Catalogo. Le presenti Guidelines restano la fonte dei vincoli; i template sono la fonte del testo riutilizzabile.

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

Nel Regime C, la validazione deve assumere una forma esplicita. La risposta dell'IA deve essere ricondotta a uno dei due esiti: criticità respinta oppure criticità accolta. Nel primo caso il notebook non viene modificato. Nel secondo caso il notebook viene aggiornato sostituendo le celle della tappa coinvolta con versioni corrette e informative, senza aggiungere celle extra di verifica.

Nel notebook docente, la validazione può rimanere implicita se il materiale finale è già pulito e coerente. Nel tracciato IA dello studente, invece, deve essere visibile almeno in forma sintetica: accettazione, modifica, rifiuto o correzione della risposta ottenuta.

---

### 15.9 Tracciato IA dello studente

Quando il lavoro take-home prevede uso documentato dell'IA, lo studente deve consegnare il tracciato dell'interazione. La forma ordinaria di consegna è la stampa PDF della chat IA dedicata al caso, salvo diversa indicazione del docente.

Il tracciato non deve essere valutato come prova forense dell'intera storia privata del lavoro svolto con strumenti IA. Deve essere valutato come artefatto metodologico: esso deve mostrare come lo studente ha organizzato l'assistenza dell'IA secondo una sequenza controllata di ricognizione teorico-modellistica, traduzione operativa in codice, verifica e interpretazione critica.

Il tracciato deve contenere:

1. identificazione del problema;
2. Prompt zero utilizzato;
3. Prompt 1 con Scheda Caso e produzione della cella Markdown iniziale del notebook;
4. Prompt 2 in Regime A per la costruzione del Flusso logico-teorico risolutivo;
5. contributo iniziale dello studente al Flusso logico-teorico risolutivo;
6. risposta IA utilizzata per verificare, completare o ordinare il flusso;
7. azione dello studente sulla risposta IA: accettazione, modifica, rifiuto o correzione;
8. tabella finale del Flusso logico-teorico risolutivo;
9. Prompt 3 per la scomposizione del problema in tappe input-output;
10. contributo iniziale dello studente alla scomposizione in tappe;
11. collegamenti input/output tra tappe;
12. prompt utilizzati;
13. regime attribuito a ciascun prompt;
14. risposta IA utilizzata;
15. azione dello studente: accettazione, modifica, rifiuto o correzione;
16. eventuali verifiche in Regime C, con esito criticità respinta oppure criticità accolta;
17. output prodotto;
18. controllo svolto;
19. verifiche conclusive, se richieste;
20. interpretazione finale autonoma.

Se lo studente utilizza un prompt zero, esso deve essere riportato una sola volta all'inizio del tracciato. I prompt successivi possono essere più brevi, purché siano chiaramente collegati al contesto iniziale e alle tappe del lavoro.

Se lo studente non utilizza un prompt zero, ogni prompt di tappa deve essere sufficientemente autosufficiente. In questo caso il tracciato deve mostrare che l'IA ha ricevuto contesto, input, vincoli e output atteso in misura sufficiente.

La chat consegnata in PDF deve essere dedicata al caso e non deve contenere conversazioni estranee. I prompt dello studente e le risposte dell'IA devono restare visibili nella sequenza effettiva di lavoro. Eventuali sintesi interne al notebook non sostituiscono il tracciato IA.

Il numero di prompt deve rispettare l’intervallo stabilito dal docente per ciascun caso take-home. Tale intervallo viene indicato nella Scheda Costruzione Caso e deve essere comunicato agli studenti nella Scheda Caso o nella traccia del lavoro.

Un tracciato troppo breve tende a indicare una delega globale e non controllata. Un tracciato eccessivamente lungo tende a rendere difficile la valutazione e può indicare assenza di organizzazione. Il vincolo sul numero minimo e massimo di prompt ha quindi funzione didattica: obbliga lo studente a decomporre il problema senza produrre un materiale ingestibile.

---

### 15.10 Struttura osservabile del tracciato IA

La consegna ordinaria del tracciato IA è la stampa PDF della chat. Non è quindi necessario trasformare la chat in un documento Markdown separato, salvo diversa indicazione del docente.

La chat deve tuttavia essere costruita in modo ordinato. Deve rendere osservabile la successione:

```text
Prompt zero
-> Prompt 1
-> Prompt 2
-> Prompt 3
-> prompt di tappa
-> eventuali prompt C
-> verifiche conclusive
```

Nel tracciato devono risultare riconoscibili:

1. il caso a cui la chat si riferisce;
2. il Prompt zero;
3. il Prompt 1 con la Scheda Caso e la cella Markdown iniziale prodotta dall'IA;
4. il Prompt 2 con il contributo teorico iniziale dello studente;
5. il Flusso logico-teorico risolutivo finale;
6. il Prompt 3 con la proposta iniziale di scomposizione dello studente;
7. la scomposizione input-output finale;
8. i prompt di tappa e il regime attribuito;
9. le risposte IA effettivamente utilizzate;
10. le decisioni dello studente: accettazione, modifica, rifiuto o correzione;
11. le verifiche in Regime C, quando presenti, con esito criticità respinta oppure criticità accolta;
12. le eventuali celle sostitutive prodotte in caso di criticità accolta;
13. le verifiche conclusive sul notebook e sull'interpretazione, quando richieste;
14. la relazione tra tracciato IA e notebook consegnato.

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
| Prompt 1 | Scheda Caso e cella Markdown iniziale | l’IA riceve la Scheda Caso come specifica vincolante e produce solo la cella Markdown iniziale di inquadramento, senza risolvere il caso |
| Prompt 2 | Costruzione del Flusso logico-teorico risolutivo | lo studente propone una sequenza teorica iniziale e chiede all’IA di verificarla, completarla e ordinarla |
| Prompt 3 | Scomposizione input-output | lo studente propone una prima scomposizione in tappe e chiede all’IA di verificarla, completarla e ordinarla |
| Regime A | Ricognizione teorico-modellistica | l’IA è usata per chiarire oggetti teorici, formule, definizioni, proprietà e collegamenti logici, senza produrre codice |
| Regime B | Traduzione operativa in codice | l’IA traduce in Python una specifica già validata, senza modificare variabili, formule, scenari, parametri o output richiesti |
| Regime C | Verifica critica | l’IA verifica un dubbio dello studente e classifica l’esito come criticità respinta oppure criticità accolta |
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

#### Valutazione specifica del Prompt 3

Il Prompt 3 ha il compito di tradurre il Flusso logico-teorico risolutivo in una scomposizione operativa del notebook. La sua valutazione deve considerare la qualità della proposta iniziale dello studente.

Sono indicatori positivi:

1. proposta iniziale di tappe non vuota e non puramente copiata dalla risposta dell'IA;
2. distinzione chiara tra input, operazione, output e controllo;
3. coerenza con il Flusso logico-teorico risolutivo;
4. collegamento tra tappe successive;
5. presenza di controlli numerici, logici o interpretativi;
6. richiesta all'IA di verificare, completare e ordinare, non di sostituire integralmente.

Sono indicatori deboli:

1. richiesta generica di costruire l'intero notebook;
2. scomposizione che nasce direttamente dal codice e non dal flusso teorico;
3. assenza di controlli;
4. tappe non collegate tra loro;
5. accettazione integrale della risposta IA senza selezione critica.

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
2. assenza del Prompt 1 con Scheda Caso e cella Markdown iniziale;
3. assenza del Prompt 2 o Prompt 2 privo di contributo iniziale dello studente;
4. assenza del Prompt 3 o Prompt 3 privo di proposta iniziale dello studente;
5. mancata distinzione tra Regime A, Regime B e Regime C;
6. produzione di codice prima della validazione della specifica teorica;
7. modifica non autorizzata di variabili, formule, parametri, scenari o output richiesti;
8. assenza di controlli sulle risposte IA;
9. trasferimento nel notebook di risultati non verificati;
10. interpretazione finale generata dall’IA senza bozza autonoma dello studente;
11. tracciato non collegato in modo chiaro alle sezioni del notebook.

#### Uso degli errori dell’IA nella valutazione

Gli errori commessi dall’IA non penalizzano automaticamente lo studente. Diventano rilevanti solo in relazione al comportamento dello studente.

Un errore dell’IA è valutato positivamente se lo studente lo riconosce, lo segnala e lo corregge. Diventa invece elemento negativo se lo studente lo accetta senza controllo e lo trasferisce nel notebook o nell’interpretazione finale.

Occorre distinguere gli errori puramente tecnici di codice dagli errori teorici, matematici, logici o interpretativi. I primi possono essere corretti sostituendo la cella errata e non hanno, di norma, alto valore valutativo. I secondi hanno valore didattico più elevato quando sono individuati dallo studente, verificati in Regime C e recepiti nel notebook mediante sostituzione delle celle della tappa coinvolta.

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

## 16. Gestione dello stato di avanzamento

L'unica fonte per lo stato corrente del progetto e' `MQF_Stato_Avanzamento.md`. Il file deve essere aggiornato periodicamente e ogni volta che cambia lo stato effettivo di una lezione, di un capitolo o di un prodotto didattico.

Le presenti Guidelines definiscono regole stabili e non devono contenere tabelle, conteggi o note sullo stato corrente. Il Master Plan definisce l'architettura didattica, i contenuti previsti e i registri tematici, ma non deve riportare indicatori quali completato, in lavorazione, bozza o da scrivere.

`MQF_Stato_Avanzamento.md` registra almeno:

1. stato del capitolo, delle slides, degli esercizi, dei grafici e degli eventuali materiali Python per ciascuna lezione;
2. ultima attivita' completata, lavoro in corso e prossima priorita';
3. scostamenti rispetto al Master Plan o alle Guidelines;
4. questioni operative ancora aperte;
5. verifiche di conformita' rilevanti, comprese la struttura degli esercizi e la compatibilita' con Scientific WorkPlace 5.5.

Il Registro decisionale resta distinto: documenta le decisioni progettuali e le loro motivazioni, non lo stato di esecuzione delle attivita'.

## 17. Principio guida finale

Il corso deve essere rigoroso nella notazione, selettivo nelle dimostrazioni, applicativo nell'interpretazione e coerente nella progressione didattica.

La qualita' del progetto dipendera' soprattutto dalla capacita' di mantenere un legame costante tra formalizzazione matematica, interpretazione finanziaria, esercizi, grafici e implementazioni computazionali.
