# Scaletta Capitoli 14-15 - Programmazione Stocastica (I e II)

*Documento di lavoro per la progettazione dei capitoli. Non e' un file normativo (Master Plan, Notazione, Guidelines): raccoglie e mantiene aggiornata la struttura concordata di Cap.14-15, in vista della stesura del testo pieno e del successivo aggiornamento dei file normativi.*

## Principio strutturale del gruppo Cap.14-16

Il gruppo Cap.14-15-16 ha per scopo la presentazione del **metodo matematico** della programmazione stocastica (PS). Il caso guida SVB-ALM e' un'**istanza** del metodo, non il suo motore: ogni sezione teorica deve poter essere letta e capita senza il caso guida, che compare sempre *dopo* l'enunciato generale, mai prima. Cap.14 gia' rispetta questo schema (si veda "Il programma lineare stocastico a due stadi" seguito da "Identificazione dei coefficienti nel caso SVB-ALM" al suo interno); Cap.15 va costruito con lo stesso schema.

Ripartizione dei tre capitoli: Cap.14 introduce il modello a due stadi; Cap.15 lo estende al multistadio e presenta il quadro istituzionale della PS (generazione/riduzione degli scenari, panorama dei metodi di ottimizzazione); Cap.16 implementa in Python il caso guida e sviluppa per intero un metodo di ottimizzazione multistadio.

## Cap.14 - Programmazione Stocastica I (esistente, per riferimento)

Struttura attuale (invariata, solo per contesto):

1. Dal piano deterministico alla decisione sotto incertezza
2. Stadi decisionali e struttura dell'informazione
3. Scenari e rappresentazione discreta dell'incertezza
4. Dalla legge probabilistica agli scenari: il caso Markoviano
5. La funzione di ricorso
6. Il programma lineare stocastico a due stadi
7. Forma estesa e non anticipativita'
8. Esercizi svolti
9. Esercizi proposti
10. Sintesi finale

## Cap.15 - Programmazione Stocastica II (scaletta aggiornata)

### Sez. 1 (esistente, invariata) - Fattibilita' del ricorso

Ricorso ammissibile, completo, relativamente completo; esempio a due scenari sulla capacita' di funding (figura Cap15_fattibilita_ricorso.png gia' presente). Nessuna modifica.

### Sez. 2 (esistente, con una riga di raccordo in chiusura) - Proprieta' della funzione di ricorso

Dipendenza di Q_s(x) da x; proposizione di concavita'/linearita' a tratti nel caso lineare; esempio unidimensionale (due classi di attivo, A_0=10.000). Aggiungere solo, in chiusura, una riga che anticipa: questa proprieta' si estendera' alla funzione di valore multistadio Q_{t+1}(X_t,Z_t) (Sez.5). Nessun'altra modifica.

### Sez. 3 (nuova) - Perche' il modello a due stadi non basta

**Tier:** sviluppo pieno, essenziale ma sintetico.

3.1 Il criterio operativo per assegnare uno stadio (Birge-Louveaux: una decisione appartiene a uno stadio se e' quello il momento in cui va effettivamente implementata) - enunciato in generale, nessun riferimento a SVB.
3.2 Conseguenza generale: ogni decisione intermedia deve essere misurabile rispetto alla propria storia osservata, non rispetto a quella terminale. Il modello a due stadi resta valido come dispositivo di valutazione della decisione iniziale, non come piano operativo per le decisioni intermedie.
3.3 Esercizio svolto: costruzione incrementale 2 stadi -> 3 stadi -> 4 stadi con T=4, notazione SVB-ALM usata come illustrazione (non come "il" problema della banca). Mostra che l'unica differenza fra le versioni e' la misurabilita' di u_1 (poi u_2, poi u_3): F_4 (libero per scenario) vs F_t (vincolato per nodo). Esempio numerico minimo: due valori di Z_1, due proseguimenti, 4 scenari totali.

**Notazione introdotta:** F_t (storia osservata fino a t), misurabilita' di una decisione rispetto a F_t.
**Formula chiave:** per ogni coppia di scenari s,s' con storia comune fino a t, u_t^s = u_t^{s'}.
**Esercizi:** 1 svolto (la costruzione 2->3->4 stadi sopra), 1 proposto (dato un quinto scenario, verificare quali vincoli di non anticipativita' si aggiungono).

### Sez. 4 (nuova) - Due letture dello stesso problema: programmazione stocastica e programmazione dinamica

**Tier:** sviluppo pieno ma conciso, puramente teorico/istituzionale.

Distinzione PS/DSP (Birge-Louveaux, Sez.2.10b): la PS generale indicizza le decisioni sui nodi di un albero senza assumere uno stato a bassa dimensione; la DSP/MDP assume uno stato Markoviano sufficiente e risolve per ricorsione all'indietro. Introduzione dello **stato aumentato (X_t,Z_t)** come scelta di sovrapporre la lettura DSP al problema PS - motivata dal fatto che il numero di traiettorie possibili cresce fino a 8^4=4096 su T=4. SVB-ALM compare solo come esempio di "quando conviene lo stato aumentato", nessun calcolo qui.

**Notazione introdotta:** stato aumentato (X_t,Z_t), funzione di valore Q_{t+1}(X_t,Z_t).
**Esercizi:** nessuno specifico (sezione di inquadramento).

### Sez. 5 (nuova, portante) - Il programma stocastico multistadio: formulazione generale e istanza SVB-ALM

**Tier:** sviluppo pieno - e' la sezione cardine del capitolo.

**5.1 Formulazione generale.** Nodi n, antenato a(n), probabilita' di nodo p_n, decisioni astratte u_n. Non anticipativita' in forma implicita (variabile per nodo) ed esplicita (vincolo di uguaglianza fra scenari a storia comune) - richiamando la notazione gia' in Notazione.tex (x_{s,t}=x_{s',t}). Forma estesa generale (convenzione di massimo, coerente con Sez.2):
```
max  c'x + somma_n p_n q_n' u_n
s.v. T_1 x + W_1 u_(n1) = h_1
     B_n u_(a(n)) + A_n u_n = h_n   per ogni nodo n
```
Forma ricorsiva generale a piu' livelli, con Q_{t+1}(X_t,Z_t) come funzione di valore (collegamento esplicito a Sez.2 e Sez.4).

**5.2 Identificazione dei coefficienti nel caso SVB-ALM** (stesso titolo/stessa logica gia' usata in Cap.14). Qui, e solo qui, la formulazione generale diventa concreta: T=4, decisione a ogni data (u_1,u_2,u_3,u_4, ciascuna F_t-misurabile - il modello pieno, non l'ibrido a 3 stadi della Sez.3 che li' resta un gradino didattico), bilancio di liquidita' L_t^s ricorsivo, fabbisogno D_t^s=d(Z_t^s), costo/rendimento di funding r_t^u(Z_t^s). Confronto esplicito e formale col modello a due stadi di Cap.14: stessa funzione obiettivo, stessi vincoli operativi, un solo vincolo di non anticipativita' aggiuntivo per ciascun u_t intermedio.

**Notazione introdotta:** u_n (decisione di nodo, forma generale); nella istanza SVB-ALM, L_t^s, D_t^s, r_t^u(Z_t^s) (se non gia' tutti presenti in Notazione - da verificare puntualmente in sede di stesura).
**Formule principali:** le due forme sopra (generale e istanza), piu' la ricorsione a piu' livelli.
**Figure:** albero multistadio generico con nodi e antenati; confronto grafico "ventaglio" (2 stadi) vs "albero" (multistadio) sullo stesso insieme di scenari.
**Esercizi:** 1 svolto (istanziare la forma generale sul caso SVB-ALM per T=2, verificando che si ottiene esattamente il modello di Cap.14), 1 proposto (istanziare per un caso ridotto a 3 stati esogeni).

### Sez. 6 (nuova) - Un esempio di generazione di scenari: la catena a 8 stati per il caso guida

**Tier:** sviluppo pieno (e' l'istanza concreta, esplicitamente presentata come tale).

Richiamo di Z_t=(Z_t^R,Z_t^C,Z_t^F); costruzione di una matrice P 8x8 omogenea, irriducibile, con righe deterministiche e probabilistiche, tale da generare un numero contenuto di traiettorie su T=4 (non le 8^4=4096 del caso generale). Tabella della P proposta; conteggio esplicito delle traiettorie sopravviventi.

**Figure:** grafo della catena a 8 stati con transizioni deterministiche/probabilistiche evidenziate; albero delle traiettorie sopravviventi su T=4.
**Esercizi:** 1 svolto (calcolo delle probabilita' di traiettoria sulla P data), 1 svolto (verifica di irriducibilita'/ricorrenza), 1 proposto (modificare una riga di P e ricontare le traiettorie).

### Sez. 7 (nuova) - Generazione e riduzione degli scenari

**Tier:** panorama, solo manuale (non in slide/lezione).

Alberi di scenari: generazione via simulazione + riduzione (richiamo di Fast Forward Selection, riformulato senza riferimento al caso Alcoa, uscito dal corso); cenno a metodi di moment-matching (Hoyland-Wallace); nota su vincolo di assenza di arbitraggio per alberi finanziari.

**Esercizi:** 1 proposto, facoltativo.

### Sez. 8 (nuova) - Panorama dei metodi di ottimizzazione multistadio

**Tier:** breve cenno.

Un paragrafo ciascuno, senza sviluppo: forma estesa diretta; L-shaped/Benders (richiamo, si appoggia alla convessita' di Sez.2); Nested Decomposition; SDDP; Progressive Hedging. Annuncio esplicito che uno di questi sara' sviluppato per intero in Cap.16.

**Esercizi:** nessuno (rimandati a Cap.16).

### Sez. 9 (nuova) - Sintesi e raccordo con Cap.16

Breve, un paragrafo: cosa il capitolo ha stabilito, cosa Cap.16 implementera'.

## Punti aperti / decisioni in sospeso

- **Segno EVPI/VSS.** La scheda Master Plan di Lezione 15 riporta la forma da minimizzazione (z^WS <= z^SP <= z^EV). Il caso SVB-ALM e' un problema di massimo: va corretto in z^WS >= z^SP >= z^EV, EVPI = z^WS - z^SP, VSS = z^SP - z^EV, quando si aggiorna la scheda.
- **Caso Alcoa.** Deciso a voce di rimuoverlo dal corso; non ancora rimosso dalla scheda di Lezione 14 nel Master Plan.
- **Terminologia hazard-decision/decision-hazard.** Esclusa dal manuale per scelta esplicita (specialistica, non necessaria qui); resta documentata nella nota di approfondimento personale.
- **Nota di approfondimento.** I dettagli teorici completi non riportati nel manuale (hazard-decision/decision-hazard, la disuguaglianza di valore, la ricorsione a piu' livelli in forma dettagliata) sono raccolti nel progetto Claude, doc `claude/Note_Fondamenti_2stadi_vs_multistadio.md`.
- **Aggiornamento Notazione.tex e Master Plan.** Da fare dopo la stesura del testo pieno di Cap.15, non prima (per evitare di fissare simboli prima di aver visto se servono davvero nella prosa).

## Fonti principali

- Birge, Louveaux, *Introduction to Stochastic Programming* (Springer), Sez. 2.5, 2.10b, 3.4, Cap. 6.1, Cap. 10 - file locale in `03_Common`.
- Shapiro, Dentcheva, Ruszczynski, *Lectures on Stochastic Programming*, Sez. 1.2.3, 1.4.2.
- Downward, Dowson, Baucke, "The policy graph decomposition of multistage stochastic programming problems".
- Kopa, "Multistage Stochastic Programs: Basic Formulations" (note, Univ. Carlo di Praga).
