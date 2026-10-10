# Valutazione dello studente 1 sul caso aula della lezione 13

Data della valutazione: 8 ottobre 2026.

**Valutazione proposta: 70/100.** Il modello ALM è implementato correttamente e il notebook riproduce i risultati consegnati. Il tracciato documenta contributi iniziali pertinenti e un intervento critico effettivo dello studente. La valutazione è limitata da incongruenze nella formulazione scritta, incompletezze negli output, una verifica insufficiente di marginali e vincoli attivi e dall'assenza di una vera interpretazione conclusiva.

Si applicano i sei pesi della sezione 15.11 delle [Guidelines](../../00_MasterPlan/MQF_Project_Guidelines.md), come richiesto dal docente per il caso aula. Le Guidelines presentano questa articolazione con riferimento ai take-home con IA: l'applicazione al caso aula è qui esplicita. I singoli punteggi sono giudizi motivati entro i pesi assegnati, non il risultato di detrazioni automatiche previste dalle Guidelines. L'equivalente puramente lineare è **21/30**; non si presume una diversa regola istituzionale di conversione.

## Materiali esaminati e metodo

Sono stati esaminati:

- [Scheda Caso Aula](Lezione_13_Scheda_Caso_Aula.md), specifica vincolante del caso Silicon Valley Bank 2023;
- [Scheda Costruzione Caso Aula](Lezione_13_Scheda_Costruzione_Caso_Aula.md), soprattutto le sezioni 11 e 12 sul processo e sulla valutazione;
- [Notebook Aula dello studente 1](Lezione_13_Notebook_Aula_Stud1.ipynb), 15 celle, di cui 6 di codice;
- [Tracciato IA in DOCX](Lezione_13_Tracciato_Aula_Stud1.docx), contenente 25 interventi utente, inclusi apertura, conferme, richieste di formato e correzioni;
- Guidelines, sezioni 15.9–15.11.

La numerazione delle celle riportata di seguito parte da 1. Il tracciato è stato letto direttamente dal DOCX; non è stato necessario accedere alla conversazione online. Non sono presenti immagini incorporate o formule OMML da cui dipendano evidenze ulteriori rispetto al testo estratto. La valutazione riguarda il caso aula: il notebook take-home presente nella stessa cartella non è incluso.

Le sei celle di codice sono state rieseguite in sequenza in un processo Python pulito, con NumPy 2.1.3, SciPy 1.15.3 e backend grafico non interattivo. Il testo degli output standard delle sei celle coincide esattamente con quello salvato nel notebook. Sono state inoltre ispezionate le otto immagini incorporate, che contengono i quattordici pannelli numerati. Le verifiche aggiuntive del valutatore non sono attribuite allo studente. Gli elaborati originali non sono stati modificati.

## Griglia numerica

| Area delle Guidelines | Massimo | Assegnato | Motivazione sintetica |
|---|---:|---:|---|
| Prompt 2 — Flusso logico-teorico risolutivo | 30 | **22** | Sequenza personale pertinente; formalizzazione poco sviluppata, integrazioni sostanziali dell'IA e incongruenze teoriche accettate nel flusso finale. |
| Prompt 3 — Scomposizione input-output | 15 | **12** | Proposta operativa coerente, con controlli e raffinamento; oggetti intermedi e collegamenti puntuali agli output sono precisati soprattutto dall'IA. |
| Notebook Jupyter e output computazionali | 20 | **15** | Modello corretto e riproducibile, benchmark, griglie, frontiera e scenari validi; output e rappresentazioni non interamente conformi alla specifica. |
| Prompt e uso dei regimi A/B/C | 15 | **12** | Contesto e vincoli fissati, approvazioni prima del codice, correzione fondata in Regime C; revisione successiva della risposta IA non sufficientemente documentata. |
| Verifiche logiche e controlli numerici | 15 | **9** | Bilanci, slack e perturbazione di A0 effettivi; verifica incompleta dei marginali, dei bounds attivi e della coerenza tra teoria, output e analisi parametrica. |
| Interpretazione critica finale | 5 | **0** | Manca un commento autonomo dei risultati, dei cambiamenti del piano ALM e dei limiti del modello. |
| **Totale** | **100** | **70** | |

La formulazione scritta è valutata nel flusso teorico; correttezza e completezza degli output nel notebook; l'adeguatezza delle verifiche nella relativa area. L'assenza della conclusione è valutata nell'ultima area, senza ulteriori detrazioni automatiche nelle altre.

## 1. Prompt 2 e contributo teorico

Il Prompt 2, riconoscibile nel tracciato dall'apertura «Regime A - Ricognizione teorico-modellistica», contiene sette passaggi proposti dallo studente. Identifica attivi, giacenze e funding; richiama il passaggio massimo/minimo; distingue i diversi vincoli; prevede benchmark, sensitività separate, frontiera di fattibilità e scenari congiunti. La richiesta di verificare, completare e ordinare senza codice è appropriata. Non è una richiesta generica di soluzione integrale.

Il contributo iniziale rimane però prevalentemente descrittivo: non formalizza i bilanci temporali, la dipendenza dei rimborsi da psi, i marginali economici e la loro verifica, né collega puntualmente formule e controlli. L'IA introduce il vettore a 11 componenti, la formalizzazione matriciale e il riferimento alla dualità. Lo studente propone il compattamento in sei tappe, ma lascia all'IA il raggruppamento concreto e convalida il risultato senza discutere le integrazioni.

Nel flusso finale, cella 2, restano due incongruenze rilevanti:

1. **Doppio cambio di segno.** Si scrive contemporaneamente “min -f'z” e “f = -c_Pi”. Con questa definizione di f, la minimizzazione corretta è “min f'z”, e il valore economico è “Pi = -f'z”. Anche la successiva espressione “Pi* = f'z*” è incoerente con la definizione adottata. Il problema ricompare nella cella 4. Il codice, invece, usa correttamente f negativo rispetto ai coefficienti economici e Pi* = -res.fun: la criticità è nella spiegazione teorica e nella sua mancata riconciliazione con l'implementazione.
2. **Dipendenza parametrica delle matrici.** La forma scritta colloca psi in b_eq(theta,psi), mentre psi modifica i coefficienti dei rimborsi, quindi A_eq(psi); b_eq dipende da theta. Nel codice, phi agisce sui bounds del funding e non sui due termini noti di A_ub, che restano K e 30. Il testo non descrive con precisione la forma solver effettivamente adottata.

Si riconosce la comprensione del percorso generale, ma non si attribuisce pieno controllo della formalizzazione finale. Gli errori introdotti dall'IA non sono penalizzati in quanto tali: rileva il fatto che siano stati validati e trasferiti nel notebook senza correzione.

## 2. Prompt 3 e scomposizione operativa

La proposta iniziale dello studente è concreta e ordinata: costruzione della forma solver, benchmark, controlli tramite residuali/slack/marginali, routine parametrica, raffinamento della frontiera e scenari. I controlli sono una tappa esplicita e precedono le analisi successive. Questo è un punto positivo sostanziale.

Gli input e gli output sono riconoscibili, ma non sono ancora specificati sistematicamente per ogni passaggio; mancano nella proposta personale il censimento completo delle dieci tabelle e quattordici figure e la gestione puntuale dei risultati non validi. La tabella dettagliata della cella 3 è elaborata dall'IA e approvata con «Convalido questa scomposizione». La validazione documenta una decisione, ma non una verifica analitica di tutti i collegamenti.

La dicitura “stima esatta della frontiera” nella tabella è inoltre eccessiva rispetto al metodo adottato, che individua un intervallo numerico. Non si richiede allo studente di produrre una soluzione analitica: occorre soltanto qualificare correttamente la precisione ottenuta.

## 3. Notebook e completezza degli output

### Risultati positivi

La funzione solve_alm, cella 5, implementa correttamente:

- l'ordinamento (x1,...,x4,g1,...,g4,u1,u2,u3);
- il segno della funzione obiettivo e il coefficiente nullo di g4;
- i cinque vincoli di uguaglianza e la corretta collocazione temporale di giacenze e rimborsi;
- il vincolo prudenziale, la concentrazione e i bounds del funding;
- theta sui primi due fabbisogni, phi sulle capacità e psi sia nell'obiettivo sia nei rimborsi.

Sono rispettate tutte le griglie e le tre configurazioni assegnate. Nelle sensitività e negli scenari res.x è letto soltanto dopo successo del solver. I valori non ammissibili sono sostituiti con NaN, e le curve di sensitività usano soltanto punti validi. Tutti e tre gli scenari assegnati risultano ammissibili: la denominazione “Critico” non implica, da sola, infeasibilità.

La Tabella 1 è presente nella cella Markdown 4; non va considerata assente perché non stampata dal codice. La correzione richiesta in Regime C è stata recepita nella cella 11: le Tabelle 6–8 includono ora g*, una sintesi dei vincoli attivi e una colonna di differenze finite. Le quattordici figure sono numerate e leggibili.

### Output incompleti o da correggere

| Requisito | Evidenza nel notebook | Valutazione |
|---|---|---|
| Marginali benchmark dei limiti di funding economicamente rilevanti, Tabella 5 | Il codice della cella 9 stampa soltanto i marginali delle uguaglianze. Le righe sul funding restano segnaposto nella tabella Markdown. | Manca il marginale del limite u3, attivo e con valore economico positivo. |
| Bounds attivi benchmark | La Tabella 4 considera prudenziale, concentrazione e bounds superiori di u. | Non sono censiti i bounds inferiori attivi di x1, x3, g3, u1, u2. |
| Variazioni di tutte le componenti nelle tre sensitività | Delta Pi e Delta % Pi presenti; Delta x calcolato e rappresentato soltanto lungo theta. | Mancano Delta g e Delta u nelle tre analisi e Delta x per phi e psi. I livelli disponibili permettono di ricavarli, ma non sostituiscono il calcolo richiesto. |
| Figura 7: Pi(phi) e funding rispetto alla capacità | Mostra soltanto Pi(phi). | La parte sul funding è disponibile in tabella, ma manca nel grafico richiesto. |
| Figura 8: Pi(psi) e funding ottimo | Mostra soltanto Pi(psi). | Manca la componente grafica sul funding. |
| Figura 10: principali vincoli attivi | Rappresenta soltanto i rapporti di utilizzo del funding. | È informativa per i limiti superiori di u, ma non descrive gli altri bounds attivi responsabili dei cambiamenti della soluzione. |
| Marginali degli scenari, quando rilevanti | La cella 15 non li estrae né li riporta. | Output incompleto, soprattutto per il confronto della scarsità di liquidità nei diversi scenari. |
| Figura 14: profilo temporale delle giacenze nei tre scenari | L'asse orizzontale contiene gli scenari e ogni curva una data. | I dati sono presenti, ma la figura confronta scenari a data fissata; per un profilo temporale servono le date sull'asse e una curva per scenario. |

Il funding rispetto a theta è rappresentato nella Figura 5 e il suo utilizzo nella Figura 10: si riconosce questa copertura complessiva, senza imporre che entrambe le informazioni occupino necessariamente lo stesso pannello. La Tabella 3 include correttamente i rimborsi nei fabbisogni aggregati, ma non li espone in una voce separata come richiesto dalla specifica: è una limitazione di presentazione, non un errore dei bilanci.

## 4. Prompt, regimi e correzioni

Il tracciato contiene Prompt zero, Scheda Caso nel Prompt 1, contributi iniziali, approvazioni prima del codice e costruzione progressiva per tappe. I prompt successivi brevi, come «Tappa 3», sono ammessi dalla sezione 15.9 quando collegati a un Prompt zero e a un contesto definito; non sono trattati come delega indiscriminata dell'intero caso.

Sono distinguibili due correzioni:

- **Errore tecnico di plotting:** lo studente riporta l'AttributeError dovuto a fontweight passato a plot. La correzione viene recepita e il notebook finale funziona. È un'azione appropriata, ma con valore valutativo inferiore a una verifica teorica.
- **Verifica sostanziale in Regime C:** lo studente osserva che le Tabelle 6–8 non espongono giacenze, vincoli attivi e marginali sufficienti, collega il dubbio alla specifica e chiede una revisione circoscritta della Tappa 4. La richiesta è pertinente e viene riconosciuta positivamente.

La revisione dell'IA non risolve però completamente il problema: sostituisce di fatto parte dell'informazione sui marginali con np.gradient su griglie ampie. Lo studente chiede chiarimenti sulla riesecuzione delle celle, ma non documenta una verifica della nuova colonna né delle omissioni residue. Il credito per aver individuato la criticità rimane; non può equivalere a una validazione completa della correzione.

I 25 interventi superano l'indicazione orientativa 9–10 della Scheda Costruzione, ma comprendono anche conferme e chiarimenti. Tale intervallo non è riportato nella Scheda Caso destinata allo studente. In accordo con la sezione 15.9 delle Guidelines, che richiede la comunicazione del limite agli studenti, non si applica una penalizzazione automatica per il numero dei messaggi. Non si applica neppure una penalità per il formato DOCX, espressamente indicato dal docente per questa valutazione.

## 5. Controlli e valori marginali

### Controlli effettivamente presenti

La cella 9 ricostruisce risorse e impieghi delle quattro date e mostra residuali trascurabili; presenta valori assunti e slack dei principali vincoli superiori. Dichiara una tolleranza di 10^-5 per l'attività dei vincoli e un riferimento a 10^-7 per i residuali nel testo. Queste due tolleranze hanno oggetti diversi e non costituiscono, da sole, una contraddizione.

Il test numerico su A0 con incremento 0,1 è reale: il rapporto incrementale 0,068418 circa coincide con il marginale economico restituito dal solver dopo il cambio di segno. Soddisfa la richiesta minima di verificare almeno un marginale. Il commento nel codice menziona anche il bilancio t=1, ma questo secondo test non viene eseguito; non era comunque necessario testare due marginali per soddisfare il minimo.

I parametri non variati restano fissi nelle tre sensitività. Lo Standard riproduce il benchmark. La frontiera è determinata tramite fattibilità, non tramite estrapolazione del valore obiettivo.

### Limiti delle verifiche

**Marginali locali e differenze sulla griglia.** Nella cella 11, np.gradient usa punti distanti e può attraversare cambiamenti della base ottima. I valori ottenuti sono approssimazioni di pendenze su una griglia, non automaticamente derivate locali o prezzi ombra. La verifica indipendente con perturbazioni di 10^-6 mostra:

| Parametro e punto | Colonna del notebook | Rapporto incrementale locale del valutatore |
|---|---:|---:|
| theta = 1,05 | -66,495662 | -15,589031 |
| theta = 1,06 | NaN | -455,571429 |
| phi = 1,20 | 0,017257 | 0,000000 |
| psi = 1,25 | -0,106019 | -0,150000 |
| psi = 1,50 | -0,031019 | 0,000000 |

A theta = 1,06, np.gradient incorpora il punto successivo non ammissibile e perde l'informazione locale nonostante il punto corrente sia valido. A phi = 1,20 e psi = 1,50 il valore locale è nullo, mentre la colonna risente dei punti precedenti in un diverso tratto della funzione. Non sono errori nella soluzione del problema primale, ma rendono inadeguata una lettura diretta della colonna come “valore marginale”. La Figura 9, invece, usa effettivi marginali delle uguaglianze con segno correttamente convertito: non va confusa con questa colonna.

**Funding e bounds inferiori.** Il marginale economico del bound superiore di u3 nel benchmark è circa 0,008834957; la verifica del valutatore aumentando il limite di 0,0001 lo conferma. Il notebook non lo riporta, pur essendo proprio il limite superiore attivo. Inoltre le etichette “Nessuno” nelle tabelle significano soltanto nessuno dei vincoli superiori selezionati: nello scenario Critico, per esempio, sono attivi i bounds inferiori di x3, x4, g4, u1, u2 e u3. Non documentano l'assenza di vincoli attivi in senso generale. Questa omissione impedisce un confronto completo tra cambiamenti della soluzione e cambiamenti dei vincoli, richiesto dal controllo 23.

**Robustezza dello stato del solver.** Il codice equipara success=False a non ammissibilità. Nei punti effettivamente assegnati tutti gli insuccessi sono status=2, quindi la conclusione è corretta. Una funzione più generale dovrebbe distinguere infeasibilità, illimitatezza e altri arresti. Non si considera questo limite come un errore di risultato nei casi eseguiti. Nel test perturbato di A0, invece, res.fun è letto senza un controllo preventivo di success, pur essendo l'esito effettivo ottimo.

**Frontiera.** I valori estremi individuati, 1,0610 ammissibile e 1,0611 non ammissibile, sono corretti. La notazione stampata (1,0610; 1,0611] non riflette l'informazione logica agli estremi: è preferibile riportare l'intervallo chiuso come contenimento numerico, specificando separatamente l'esito dei due estremi. La frase “incremento massimo +6,10%” va intesa come ultimo incremento verificato sulla griglia fine, non come soglia esatta. Il valore indipendente circa 6,108602% conferma comunque la bontà del raffinamento.

## 6. Interpretazione critica finale

Il notebook termina con tabelle e grafici degli scenari. Il tracciato si chiude con la dichiarazione che i risultati sono consistenti e con la validazione complessiva. Non compare una bozza autonoma di commento finanziario né una successiva revisione critica di tale bozza.

Le celle Markdown illustrano ciò che il codice deve fare e ricordano alcuni limiti del modello; non discutono i risultati ottenuti con un contributo conclusivo dello studente. Non viene spiegato, per esempio, perché l'aumento di theta modifichi drasticamente la composizione dell'attivo, perché oltre alcuni livelli di phi il valore smetta di crescere, o perché nello scenario Critico il funding ottimo sia nullo pur in presenza di stress.

Non si afferma che lo studente abbia delegato all'IA una conclusione: la conclusione richiesta è assente. La mera approvazione del lavoro non soddisfa il criterio da 5 punti delle Guidelines.

## 7. Risultati verificati e riscontri indipendenti

Il benchmark restituisce:

| Quantità | Valore |
|---|---|
| x* | (0; 51,919684; 0; 48,080316) |
| g* | (6,151810; 1,566506; 0; 2,890158) |
| u* | (0; 0; 6) |
| Pi* | 3,592165993 |
| Perdita prudenziale ell'x* | 4,884819 circa, inferiore a 7 |
| Marginale economico di A0 | 0,068418 circa |
| Marginale economico del limite superiore di u3, calcolato dal valutatore | 0,008834957 |

| Scenario | Pi* | Perdita rispetto allo Standard | Funding u* |
|---|---:|---:|---|
| Standard | 3,592166 | 0,000000 | (0; 0; 6) |
| Mediamente critico | 3,476367 | 0,115799 | (0; 0; 5,4) |
| Critico | 2,159921 | 1,432245 | (0; 0; 0) |

Sulla griglia theta l'ultimo valore ammissibile è 1,06 e il primo non ammissibile è 1,07. Il raffinamento individua 1,0610 e 1,0611. Un problema LP aggiuntivo del valutatore, che massimizza theta come dodicesima variabile mantenendo phi=psi=1, restituisce **theta_crit = 1,061086021** circa. Questa verifica non era richiesta allo studente e non sostituisce il suo procedimento, che è valido.

Sono state controllate 134 configurazioni conteggiate con le ripetizioni del benchmark nelle varie analisi: benchmark, tre griglie, griglia fine e scenari. Gli esiti sono 40 ottimi e 94 infeasibili. Per ogni soluzione ottima sono stati ricostruiti indipendentemente i bilanci finanziari, l'obiettivo economico, il vincolo prudenziale, la concentrazione, la non negatività e le capacità di funding. Il massimo residuo dei bilanci è circa 1,42 × 10^-14; il massimo scarto fra obiettivo ricalcolato e -res.fun è circa 8,88 × 10^-16. Ciò conferma la correttezza numerica del nucleo del modello, senza attestare che tutti questi controlli siano già documentati nell'elaborato dello studente.

## Restituzione allo studente

La costruzione del modello e la proposta operativa sono buone. È positivo aver individuato la mancanza di informazioni nelle tabelle e aver richiesto una correzione circoscritta. Per completare il lavoro occorre riconciliare notazione e codice, distinguere pendenze su griglia e marginali locali, includere i bounds inferiori e i marginali del funding, completare variazioni e grafici richiesti e scrivere una conclusione autonoma che colleghi risultati, vincoli e limiti del modello.
