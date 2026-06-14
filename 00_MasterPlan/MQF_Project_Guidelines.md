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

Ogni applicazione deve essere costruita intorno a un caso identificabile. Il caso deve specificare:

1. il contesto finanziario o probabilistico;
2. la domanda quantitativa da affrontare;
3. i dati disponibili, se presenti, oppure la procedura di generazione dei dati simulati;
4. i parametri del modello;
5. le grandezze da calcolare;
6. gli output numerici e grafici attesi;
7. il prodotto computazionale finale.

Per ogni lezione applicativa devono essere predisposti almeno i seguenti materiali:

1. una traccia del caso;
2. un notebook o script Python semi-strutturato;
3. eventuali file dati;
4. una lista di parametri iniziali;
5. una sequenza di tappe operative;
6. controlli intermedi;
7. output numerici attesi;
8. grafici o tabelle da produrre;
9. indicazioni per la discussione in aula;
10. una o due estensioni take-home.

Il notebook o script deve evitare che gli studenti partano da un file vuoto. La struttura consigliata e':

1. intestazione della lezione e descrizione del caso;
2. importazione delle librerie;
3. definizione dei dati e dei parametri;
4. funzioni ausiliarie;
5. implementazione del modello base;
6. controlli intermedi;
7. output numerici;
8. grafici;
9. analisi di sensibilita';
10. blocchi da completare da parte degli studenti;
11. domande di interpretazione;
12. estensione take-home.

I blocchi destinati allo sviluppo autonomo devono essere chiaramente segnalati. Possono essere usate formule del tipo:

```python
# TODO 1: completare la funzione
# TODO 2: verificare il controllo numerico
# TODO 3: produrre il grafico richiesto
# TODO 4: interpretare il risultato
```

Criteri comuni per il codice Python:

1. codice ben commentato;
2. separazione tra dati, parametri, funzioni e output;
3. nomi delle variabili coerenti con la notazione matematica;
4. preferenza per codice leggibile rispetto a codice eccessivamente compatto;
5. controlli intermedi espliciti;
6. grafici leggibili e interpretabili;
7. interpretazione dei risultati dopo ogni blocco computazionale rilevante;
8. possibilita' di modificare parametri, scenari e target;
9. riproducibilita' dell'esecuzione;
10. tracciabilita' del passaggio dalla formula matematica all'algoritmo.

Gli strumenti Python introdotti in ciascuna lezione devono essere selezionati in funzione del modello. Non devono essere presentati come argomenti indipendenti di programmazione. A seconda della lezione, possono essere introdotti:

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

Ogni lezione applicativa deve concludersi con un prodotto finale osservabile. La lezione applicativa non deve concludersi genericamente con la scrittura di codice, ma con la comprensione di che cosa il codice permette di calcolare e di come tale calcolo modifichi o rafforzi l'interpretazione del modello teorico.

## 15. Uso controllato dell'IA generativa

L'uso di strumenti di intelligenza artificiale generativa puo' essere previsto come supporto controllato.

L'IA puo' essere utilizzata per:

1. spiegare messaggi di errore;
2. correggere errori sintattici o locali;
3. proporre una funzione Python coerente con una formula data;
4. commentare un blocco di codice;
5. migliorare la leggibilita' del codice;
6. confrontare due implementazioni alternative.

Non e' invece appropriato delegare all'IA:

1. la formulazione matematica del modello;
2. la scelta delle ipotesi;
3. la definizione delle variabili decisionali;
4. la selezione delle misure di rischio;
5. l'interpretazione economico-finanziaria dei risultati;
6. la verifica finale della correttezza.

Quando l'IA viene utilizzata dagli studenti, il docente puo' richiedere che siano esplicitati il prompt utilizzato, la risposta ricevuta e la verifica effettuata. L'obiettivo e' sviluppare un uso critico dello strumento, non sostituire la comprensione del modello.

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
