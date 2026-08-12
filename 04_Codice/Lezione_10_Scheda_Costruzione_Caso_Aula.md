# Lezione 10 — Scheda Costruzione Caso Aula

## 1. Identificazione del caso

* **Lezione:** 10 — Applicazione in Python: rischio di credito
* **Tipo di caso:** Aula
* **Titolo:** Lehman Brothers 2008: migrazione del rating, distribuzione delle perdite e rischio di coda
* **Destinatari:** studenti del secondo anno della Laurea Magistrale in Banca e Risk Management
* **Uso previsto:** caso applicativo guidato per consolidare mediante Python i contenuti dei Capitoli 8 e 9, con particolare riferimento a catene di Markov, migrazioni di rating, default, distribuzioni di perdita, VaR e CVaR.

## 2. Contesto e motivazione

Il caso è ambientato nel **giugno 2008**, alcuni mesi prima del fallimento di Lehman Brothers Holdings Inc.

Dopo il 31 maggio 2008 Standard & Poor's ridusse il rating dei senior long-term borrowings di Lehman da A+ ad A; nello stesso periodo Fitch ridusse il rating da AA- ad A+. Lehman dichiarava inoltre che ulteriori downgrade avrebbero potuto determinare richieste aggiuntive di collateral nell'ambito di contratti derivati e secured funding arrangements. Il successivo esito storico è noto: il 15 settembre 2008 Lehman Brothers Holdings presentò domanda di protezione ai sensi del Chapter 11.

Il caso viene però deliberatamente formulato **ex ante**. Lo studente assume il punto di vista di una funzione di risk management che, nel giugno 2008, deve valutare il rischio di credito associato a un'esposizione senior unsecured verso Lehman.

La cronologia reale svolge esclusivamente una funzione di contestualizzazione. La matrice di transizione, i valori associati agli stati e gli altri parametri numerici utilizzati nell'esercizio sono **dati didattici calibrati**, non stime storiche della dinamica effettiva del merito creditizio di Lehman.

La scelta del caso consente di rendere operativa una distinzione centrale del Capitolo 9: il rischio di credito non coincide con il solo evento di default. Una posizione può subire perdite rilevanti anche quando l'emittente sopravvive, se il deterioramento del rating produce una diminuzione del valore di mercato dell'esposizione.

## 3. Domanda quantitativa e obiettivo didattico

**Domanda quantitativa**

Nel giugno 2008, quale distribuzione delle perdite a un anno può essere associata a un'esposizione senior unsecured  verso Lehman Brothers (e.g. obbligazioni non garantite di Lehman Brothers in portafoglio) se l'evoluzione del merito creditizio viene rappresentata mediante una catena di Markov? Quale rischio emerge dalla perdita attesa, dal VaR e dal CVaR e quale ruolo svolgono rispettivamente migrazione del rating e default?

**Obiettivo didattico**

Lo studente deve essere in grado di trasformare una matrice di transizione tra stati creditizi in una distribuzione monetaria delle perdite, verificando esplicitamente la successione logica

\[
P
\longrightarrow
P^h
\longrightarrow
\pi_h
\longrightarrow
L_h
\longrightarrow
\mathbb{E}[L_h],\ \operatorname{VaR}_\alpha(L_h),\ \operatorname{CVaR}_\alpha(L_h).
\]

L'obiettivo non è prevedere il fallimento di Lehman, ma comprendere come un modello markoviano possa tradurre differenti possibili traiettorie del rating in una distribuzione di rischio finanziario.

## 4. Specifica teorico-matematica

### Grandezze e variabili

Si considera un'esposizione senior unsecured con valore iniziale normalizzato pari a

\[
V_0=100.
\]

Il processo creditizio è

\[
\{X_t\}_{t=0}^{4},
\]

dove ogni periodo corrisponde a un trimestre.

Lo spazio degli stati è

\[
\mathcal{I}=\{\mathrm{A},\mathrm{BBB},\mathrm{BB/B},\mathrm{CCC},\mathrm{D}\},
\]

dove $D$ rappresenta il default ed è uno stato assorbente.

Lo stato iniziale è

\[
X_0=A.
\]

### Parametri e dati

La matrice trimestrale di transizione didattica è

\[
P=
\begin{pmatrix}
0.800 & 0.150 & 0.040 & 0.009 & 0.001\\
0.050 & 0.750 & 0.130 & 0.050 & 0.020\\
0.010 & 0.080 & 0.680 & 0.170 & 0.060\\
0.000 & 0.020 & 0.080 & 0.650 & 0.250\\
0.000 & 0.000 & 0.000 & 0.000 & 1.000
\end{pmatrix}.
\]

I valori dell'esposizione all'orizzonte annuale, condizionatamente allo stato finale, sono fissati in:

| Stato finale | $A$ | $BBB$ | $BB/B$ | $CCC$ | $D$ |
| ------------ | --: | ----: | -----: | ----: | --: |
| Valore $V_h$ | 100 |    96 |     86 |    60 |  10 |

Le corrispondenti perdite sono quindi

\[
L_h=V_0-V_h,
\]

ossia

| Stato finale  | $A$ | $BBB$ | $BB/B$ | $CCC$ | $D$ |
| ------------- | --: | ----: | -----: | ----: | --: |
| Perdita $L_h$ |   0 |     4 |     14 |    40 |  90 |

Il valore $10$ nello stato di default corrisponde a un recovery value didattico del $10\%$. Non deve essere presentato come recovery storico effettivo dei titoli Lehman.

### Ipotesi

1. La catena è omogenea nell'orizzonte dei quattro trimestri.
2. Lo stato corrente sintetizza l'informazione rilevante per la distribuzione dello stato successivo.
3. Il default è assorbente.
4. La matrice $P$ è assegnata e non deve essere stimata dagli studenti.
5. I valori $V_h$ associati agli stati finali sono assegnati.
6. Il rischio viene valutato sotto probabilità fisiche.
7. Nel caso base non viene modellata dipendenza da fattori sistemici né da altri emittenti.
8. Il modello descrive il rischio di una singola esposizione; l'estensione a un portafoglio viene utilizzata solo come sviluppo finale controllato.

### Formule vincolanti

Distribuzione iniziale:

\[
\pi_0=(1,0,0,0,0).
\]

Distribuzione dopo $h$ trimestri:

\[
\pi_h=\pi_0P^h.
\]

Probabilità cumulativa di default entro $h$:

\[
\operatorname{PD}^{\mathrm{cum}}(h)=(P^h)_{A,D}.
\]

Perdita associata allo stato $j$:

\[
L(j)=V_0-V(j).
\]

Perdita attesa:

\[
\mathbb{E}[L_h]=\sum_{j\in\mathcal{I}}
L(j)\Pr(X_h=j).
\]

Il VaR e il CVaR devono essere calcolati sulla distribuzione discreta di $L_h$, secondo le definizioni adottate nel Capitolo 9.

### Quantità finali di interesse

* distribuzioni $\pi_1,\ldots,\pi_4$;
* probabilità cumulativa di default ai differenti orizzonti;
* distribuzione annuale della perdita;
* perdita attesa;
* $\operatorname{VaR}_{0.90}$;
* $\operatorname{CVaR}_{0.90}$;
* $\operatorname{VaR}_{0.95}$;
* $\operatorname{CVaR}_{0.95}$;
* contributo qualitativo di migrazione e default alla forma della distribuzione.

## 5. Output richiesti

### Risultati numerici

1. Verifica che $P$ sia una matrice stocastica.
2. Calcolo di $P^2,P^3,P^4$.
3. Calcolo di $\pi_h$, $h=1,\ldots,4$.
4. Term structure trimestrale della probabilità cumulativa di default.
5. Distribuzione discreta delle perdite a un anno.
6. Perdita attesa.
7. VaR e CVaR ai livelli $90\%$ e $95\%$.

### Tabelle

**Tabella 1 — Evoluzione delle probabilità di stato**

Righe: trimestre $h$.
Colonne: $A,BBB,BB/B,CCC,D$.

**Tabella 2 — Distribuzione annuale della perdita**

Stato, probabilità, valore finale, perdita.

**Tabella 3 — Misure sintetiche**

Perdita attesa, VaR e CVaR ai livelli richiesti.

### Grafici

1. Evoluzione trimestrale delle probabilità dei cinque stati.
2. Distribuzione discreta della perdita a un anno.
3. Probabilità cumulativa di default in funzione dell'orizzonte.

### Controlli

* tutte le righe di $P$ devono sommare a uno;
* tutte le componenti di $\pi_h$ devono essere non negative e sommare a uno;
* la probabilità cumulativa di default deve essere non decrescente;
* la perdita nello stato $D$ deve essere la massima perdita prevista;
* la distribuzione empirica ottenuta mediante simulazione deve risultare coerente con la distribuzione teorica derivata da $\pi_4$.

## 6. Flusso logico-teorico risolutivo atteso

| Passo | Finalità risolutiva                             | Strumento teorico                 | Applicazione nel caso                                  | Output o controllo         |
| ----: | ----------------------------------------------- | --------------------------------- | ------------------------------------------------------ | -------------------------- |
|     1 | Validare la rappresentazione creditizia         | Matrice di transizione            | Verifica di non negatività e somme di riga             | Matrice $P$ validata       |
|     2 | Determinare la distribuzione futura dei rating  | Potenze di $P$ e $\pi_h=\pi_0P^h$ | Evoluzione trimestrale da $A$                          | $\pi_1,\ldots,\pi_4$       |
|     3 | Isolare il rischio di default                   | Stato assorbente                  | Lettura della colonna $D$ di $P^h$                     | $\operatorname{PD}^{\mathrm{cum}}(h)$              |
|     4 | Passare dagli stati alle conseguenze economiche | Mappa stato-valore                | Associazione di $V(j)$ a ciascun rating                | Distribuzione dei valori   |
|     5 | Costruire la variabile di perdita               | $L=V_0-V_h$                       | Trasformazione dei valori in perdite                   | Distribuzione di $L$       |
|     6 | Misurare il rischio                             | Valore atteso, VaR, CVaR          | Applicazione alla distribuzione discreta               | Misure di rischio          |
|     7 | Verificare numericamente il modello             | Simulazione Monte Carlo           | Simulazione di traiettorie markoviane                  | Confronto teorico/empirico |
|     8 | Interpretare criticamente                       | Limiti del modello                | Distinzione migrazione/default e ipotesi di omogeneità | Interpretazione finale     |

## 7. Scomposizione attesa in tappe

| Tappa | Regime | Input                   | Operazione                                               | Output                     | Controllo                     | Uso successivo             |
| ----: | :----: | ----------------------- | -------------------------------------------------------- | -------------------------- | ----------------------------- | -------------------------- |
|     1 |    A   | Scheda Caso             | Identificare stati, variabili, ipotesi e quantità finali | Specifica teorica ordinata | Coerenza con Scheda Caso      | Costruzione computazionale |
|     2 |    B   | $P,\pi_0$               | Implementare matrice e verificarla                       | Oggetti Python validati    | Somme di riga                 | Calcolo multi-periodale    |
|     3 |    B   | $P,\pi_0$               | Calcolare $P^h$ e $\pi_h$                                | Evoluzione degli stati     | Somma di $\pi_h$              | Analisi default            |
|     4 |    B   | $\pi_h$                 | Estrarre $\operatorname{PD}^{\mathrm{cum}}(h)$                                   | Term structure di default  | Monotonicità                  | Costruzione della perdita  |
|     5 |   A/B  | $\pi_4,V(j)$            | Esplicitare e implementare la mappa stato-perdita        | Distribuzione di $L$       | Probabilità totale = 1        | Misure di rischio          |
|     6 |    B   | Distribuzione di $L$    | Calcolare EL, VaR, CVaR                                  | Tabella misure             | Coerenza ordinamento quantili | Interpretazione            |
|     7 |    B   | $P$, numero simulazioni | Simulare traiettorie                                     | Distribuzione empirica     | Confronto con $\pi_4$         | Validazione                |
|     8 |    C   | Notebook completo       | Formulare e verificare una criticità                     | Criticità accolta/respinta | Coerenza teorica              | Notebook definitivo        |
|     9 |    C   | Output finali           | Verifica conclusiva e interpretazione                    | Giudizio finanziario       | Coerenza con Scheda Caso      | Chiusura                   |

## 8. Mappa tra prompt e notebook

|            Prompt | Regime | Tappa | Celle o output prodotti                        | Decisione o controllo richiesto           |
| ----------------: | :----: | ----: | ---------------------------------------------- | ----------------------------------------- |
|          Prompt 1 |    —   |     — | Cella Markdown iniziale con specifica del caso | Acquisizione vincolante della Scheda Caso |
|          Prompt 2 |    A   |     1 | Flusso logico-teorico                          | Validazione docente                       |
|          Prompt 3 |    A   |   1–9 | Scomposizione in tappe                         | Validazione docente                       |
|    Prompt tappa 1 |    A   |     1 | Markdown teorico                               | Correttezza degli oggetti teorici         |
|    Prompt tappa 2 |    B   |     2 | Markdown + codice                              | Validazione matrice                       |
|    Prompt tappa 3 |    B   |     3 | Codice + tabella                               | Coerenza $P^h$ e $\pi_h$                  |
|    Prompt tappa 4 |    B   |     4 | Codice + grafico                               | Monotonicità della PD cumulativa          |
|    Prompt tappa 5 |   A/B  |     5 | Markdown + codice + tabella                    | Coerenza stato-valore-perdita             |
|    Prompt tappa 6 |    B   |     6 | Codice + tabella                               | Corretta implementazione di VaR/CVaR      |
|    Prompt tappa 7 |    B   |     7 | Codice + output Monte Carlo                    | Confronto teorico/empirico                |
|   Prompt verifica |    C   |     8 | Eventuale sostituzione delle celle coinvolte   | Criticità accolta o respinta              |
| Prompt conclusivo |    C   |     9 | Verifica finale                                | Coerenza notebook/Scheda Caso             |

## 9. Struttura attesa del notebook

1. **Markdown — Presentazione del caso e domanda quantitativa.**
2. **Markdown — Specifica teorico-matematica.**
3. **Codice — Definizione degli stati e della matrice $P$.**
4. **Codice — Controlli sulla matrice di transizione.**
5. **Markdown — Distribuzione iniziale e orizzonte temporale.**
6. **Codice — Calcolo di $P^h$ e $\pi_h$.**
7. **Output — Tabella delle probabilità di stato.**
8. **Codice — Term structure del default.**
9. **Output — Grafico della probabilità cumulativa di default.**
10. **Markdown — Passaggio dagli stati ai valori economici.**
11. **Codice — Costruzione della distribuzione della perdita.**
12. **Output — Tabella e grafico della distribuzione di $L$.**
13. **Markdown — Definizione delle misure di rischio utilizzate.**
14. **Codice — Perdita attesa, VaR e CVaR.**
15. **Output — Tabella delle misure di rischio.**
16. **Markdown — Simulazione della catena.**
17. **Codice — Monte Carlo delle traiettorie trimestrali.**
18. **Output — Frequenze empiriche degli stati finali.**
19. **Codice — Confronto distribuzione teorica/empirica.**
20. **Markdown — Verifica critica.**
21. **Markdown — Interpretazione finanziaria finale dello studente.**

## 10. Calibrazione docente

### Ordine di grandezza atteso dei risultati

Con la calibrazione assegnata, la distribuzione teorica dopo quattro trimestri è approssimativamente

\[
\pi_4=
(0.440,\ 0.300,\ 0.138,\ 0.070,\ 0.052).
\]

La probabilità cumulativa di default a un anno è quindi circa

\[
5.2\%.
\]

La perdita attesa su valore iniziale $100$ è approssimativamente

\[
\mathbb{E}[L_4]\simeq 10.6.
\]

La calibrazione è intenzionalmente costruita in modo che la distribuzione presenti una coda fortemente discreta:

\[
\operatorname{VaR}_{0.90}\approx40,
\qquad
\operatorname{CVaR}_{0.90}\approx65.8,
\]

mentre

\[
\operatorname{VaR}_{0.95}=90,
\qquad
\operatorname{CVaR}_{0.95}=90.
\]

Il salto tra il VaR al $90\%$ e quello al $95\%$ è didatticamente desiderato: rende evidente la sensibilità del VaR discreto alla massa di probabilità associata allo stato di default.

### Errori o ambiguità prevedibili

1. Interpretare $P^4$ come matrice ottenuta moltiplicando per quattro le probabilità annuali.
2. Confondere probabilità di default nel quarto trimestre con probabilità cumulativa di default entro un anno.
3. Considerare soltanto lo stato $D$ come generatore di perdita.
4. Confondere rating con valore monetario dell'esposizione.
5. Calcolare il VaR utilizzando direttamente i rating anziché la variabile $L$.
6. Applicare formule per distribuzioni continue a una distribuzione discreta senza verificarne il significato.
7. Interpretare i risultati simulati come più “corretti” di quelli teorici.
8. Presentare la matrice didattica come matrice storicamente stimata per Lehman.
9. Leggere il successivo default effettivo di Lehman come prova ex post della bontà del modello.
10. Trascurare l'ipotesi di omogeneità proprio nel contesto di una crisi finanziaria caratterizzata da rapido cambiamento strutturale.

### Controlli minimi di validazione

* somme delle righe di $P$;
* somma delle probabilità di ogni $\pi_h$;
* assorbimento dello stato $D$;
* monotonicità di $\operatorname{PD}^{\mathrm{cum}}(h)$;
* ordinamento economicamente plausibile dei valori $V(j)$;
* corrispondenza uno-a-uno tra stati, valori e perdite;
* convergenza delle frequenze Monte Carlo verso $\pi_4$ entro una tolleranza ragionevole;
* riproducibilità della simulazione mediante seed fissato.

### Limiti interpretativi

La catena omogenea è una rappresentazione intenzionalmente semplificata. Il periodo 2008 è precisamente un contesto nel quale l'ipotesi di stabilità delle probabilità di transizione può risultare fragile.

La matrice non incorpora:

* variazioni endogene della liquidità;
* effetti di funding;
* contagio tra intermediari;
* dipendenza sistemica;
* cambiamenti nelle probabilità di transizione dovuti al peggioramento macro-finanziario;
* variazioni stocastiche dei recovery rates;
* differenza tra probabilità fisiche e risk-neutral.

Il caso deve quindi concludersi sottolineando che un modello quantitativo coerente può essere internamente corretto e, nello stesso tempo, dipendere da ipotesi che diventano particolarmente fragili durante una crisi.

## 11. Uso dell'IA e tracciato

### Prompt obbligatori

* Prompt zero;
* Prompt 1;
* Prompt 2;
* Prompt 3;
* prompt delle singole tappe;
* almeno una verifica in Regime C;
* verifica conclusiva della coerenza notebook/Scheda Caso;
* verifica conclusiva dell'interpretazione.

### Numero minimo e massimo di prompt

Da definire definitivamente dopo la calibrazione della successione micro delle tappe.

Indicazione preliminare docente:

\[
10 \leq N_{\text{prompt}}\leq 16.
\]

### Usi ammessi dell'IA

* ordinamento delle premesse teoriche dopo un contributo iniziale dello studente;
* produzione del codice Python a partire da una specifica validata;
* costruzione tecnica di tabelle e grafici;
* controllo della coerenza tra formule e implementazione;
* verifica critica di dubbi formulati dallo studente;
* identificazione di possibili errori nel notebook.

### Usi non ammessi

* modifica autonoma della matrice $P$;
* modifica dei valori associati agli stati;
* sostituzione degli stati assegnati;
* introduzione autonoma di modelli di credito non trattati nei Capitoli 8–9;
* stima di una “vera” probabilità di default di Lehman;
* modifica dell'orizzonte temporale;
* produzione dell'interpretazione finanziaria finale al posto dello studente;
* sostituzione della specifica didattica con dati recuperati autonomamente dalla cronaca finanziaria.

## 12. Valutazione

### Criteri per il notebook

* correttezza della rappresentazione della catena;
* correttezza del passaggio $P\rightarrow P^h\rightarrow\pi_h$;
* distinzione fra probabilità cumulativa e marginale di default;
* corretta costruzione della variabile di perdita;
* corretta implementazione di perdita attesa, VaR e CVaR;
* qualità dei controlli;
* coerenza tra soluzione teorica e simulazione;
* chiarezza e leggibilità degli output;
* interpretazione finanziaria dei risultati.

### Criteri per il tracciato IA

* presenza di un contributo autonomo dello studente nei prompt di Regime A;
* corretta distinzione tra Regimi A, B e C;
* capacità di fornire all'IA specifiche teoriche già validate;
* assenza di delega all'IA delle scelte modellistiche vincolanti;
* qualità delle verifiche critiche;
* eventuale capacità di respingere una proposta dell'IA incoerente con la Scheda Caso.

### Peso dei controlli e dell'interpretazione

Il valore didattico principale non risiede nella complessità del codice, ma nel controllo dell'intera catena

\[
\text{modello}
\rightarrow
\text{implementazione}
\rightarrow
\text{output}
\rightarrow
\text{validazione}
\rightarrow
\text{interpretazione}.
\]

Particolare peso deve quindi essere attribuito alla corretta costruzione della distribuzione di perdita, ai controlli teorico-numerici e alla capacità di discutere criticamente le ipotesi del modello.

## 13. Relazione con l'altro caso della lezione

Il caso take-home sarà ambientato nella crisi di **China Evergrande del 2021**.

I due casi saranno isomorfi sul piano metodologico:

\[
\text{stato creditizio iniziale}
\rightarrow
\text{matrice di transizione}
\rightarrow
\text{distribuzioni future}
\rightarrow
\text{default}
\rightarrow
\text{valore dell'esposizione}
\rightarrow
\text{perdita}
\rightarrow
\operatorname{VaR}/\operatorname{CVaR}
\rightarrow
\text{verifica critica}.
\]

Non dovranno tuttavia costituire una semplice variazione parametrica.

Il caso Lehman sarà costruito intorno a una **investment bank statunitense durante la crisi finanziaria del 2008**, con particolare enfasi sulla rapidità del deterioramento del merito creditizio e sulla fragilità dell'ipotesi di omogeneità temporale.

Il caso Evergrande dovrà invece sfruttare la diversa natura dell'emittente, del settore immobiliare cinese e della sequenza di deterioramento creditizio, introducendo una diversa struttura dell'esposizione e una diversa calibrazione degli stati e delle perdite.

L'isomorfismo riguarderà quindi il metodo quantitativo e la struttura del processo risolutivo, non il contesto economico né i dati del problema.
