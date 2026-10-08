# Valutazione del take-home della lezione 13 - Studente 1

Data della valutazione: 8 ottobre 2026.

**Valutazione proposta: 67/100**, equivalente a **20,1/30** mediante conversione lineare, senza arrotondamenti aggiuntivi.

Il nucleo del modello ALM è corretto, riproducibile e coerente con la calibrazione docente. Il notebook risolve correttamente benchmark, sensitività e scenari e presenta tutte le quattordici figure richieste. Il punteggio è limitato da un controllo del marginale legacy che fallisce senza essere corretto, da tabelle incomplete rispetto alla Scheda Caso, da controlli conclusivi soltanto parziali e dall'assenza di un'interpretazione finale autonoma.

## Fonti GitHub e metodo

La valutazione è stata rifatta utilizzando esclusivamente file recuperati direttamente dal branch main del repository GitHub [paolo-fix/CORSO-MQF](https://github.com/paolo-fix/CORSO-MQF):

| Fonte | SHA del blob GitHub |
|---|---|
| [Guidelines](https://github.com/paolo-fix/CORSO-MQF/blob/main/00_MasterPlan/MQF_Project_Guidelines.md) | c97461e513ef986d964e5fc92568d7cd14942c0c |
| [Scheda Caso TakeHome](https://github.com/paolo-fix/CORSO-MQF/blob/main/04_Codice/Lez13/Lezione_13_Scheda_Caso_TakeHome.md) | 8eb5b6b04a479e235ebff2add8539a3dd6fa4506 |
| [Scheda Costruzione Caso TakeHome](https://github.com/paolo-fix/CORSO-MQF/blob/main/04_Codice/Lez13/Lezione_13_Scheda_Costruzione_Caso_TakeHome.md) | 75c131c67315e3aa42a6df07f924a0ed1cd5f27e |
| [Notebook TakeHome Studente 1](https://github.com/paolo-fix/CORSO-MQF/blob/main/04_Codice/Lez13/Lezione_13_Notebook_TakeHome_Stud1.ipynb) | 1b7e502a73b7e298a290e194479f3ac45aaae058 |
| [Tracciato IA DOCX Studente 1](https://github.com/paolo-fix/CORSO-MQF/blob/main/04_Codice/Lez13/Lezione_13_Tracciato_TakeHome_Stud1.docx) | a21a60791fd563cbf160b676f45b81373c036b60 |

Il DOCX è stato scaricato da GitHub come contenuto binario Base64 e analizzato estraendo il testo e i collegamenti dal pacchetto OOXML. Contiene 18 interventi utente e la sequenza completa delle risposte. Non contiene immagini incorporate da cui dipendano ulteriori evidenze. Il collegamento alla conversazione Gemini presente nel documento non è risultato apribile dagli strumenti browser disponibili; la trascrizione completa è però già contenuta nel DOCX GitHub e il mancato accesso al collegamento non incide sul punteggio.

Il notebook GitHub contiene 15 celle, di cui 6 di codice. È stato rieseguito integralmente in una copia temporanea con backend grafico non interattivo. L'esecuzione termina senza errori. I valori rigenerati coincidono con quelli salvati; le differenze testuali nelle ultime celle dipendono soltanto dagli identificativi temporanei degli oggetti Styler e dai warning del backend. Sono state ispezionate le cinque immagini incorporate, che contengono tutte le quattordici figure numerate.

Il renderer DOCX non ha potuto produrre le pagine PNG perché nell'ambiente mancava il modulo pdf2image. La valutazione riguarda tuttavia il contenuto metodologico del tracciato, che è stato estratto integralmente e verificato strutturalmente. Non vengono formulate conclusioni sull'impaginazione del DOCX.

I sei massimi sono quelli della sezione 15.11 delle Guidelines. I punteggi entro ciascuna area sono giudizi motivati e non detrazioni automatiche. Le verifiche aggiuntive del valutatore non sono attribuite allo studente.

## Griglia numerica

| Area delle Guidelines | Massimo | Assegnato | Motivazione sintetica |
|---|---:|---:|---|
| Prompt 2 - Flusso logico-teorico risolutivo | 30 | **23** | Contributo iniziale concreto; formalizzazione, dualità e raccordo puntuale con output e controlli sono sviluppati soprattutto dall'IA e convalidati con verifica limitata. |
| Prompt 3 - Scomposizione input-output | 15 | **12** | Buona proposta personale in sei tappe; il dettaglio sistematico di input, output, controlli e collegamenti è fornito prevalentemente dall'IA. |
| Notebook Jupyter e output computazionali | 20 | **14** | Modello primale corretto e riproducibile, benchmark e scenari validi, figure complete; tabelle 6-10 incomplete e rappresentazione parziale di vincoli attivi e marginali. |
| Prompt e uso dei regimi A/B/C | 15 | **11** | Sequenza controllata e dubbio sostanziale in Regime C; la correzione ricevuta non viene verificata sino in fondo e la validazione finale ignora criticità visibili. |
| Verifiche logiche e controlli numerici | 15 | **7** | Residuali, vincoli primali, riproducibilità e stato del solver sono controllati; il test richiesto del marginale legacy fallisce per il segno e non viene risolto. |
| Interpretazione critica finale | 5 | **0** | Non è presente un'interpretazione autonoma conclusiva; compare soltanto una validazione generale. |
| **Totale** | **100** | **67** | |

La completezza degli output è valutata nell'area notebook; l'efficacia dei test nell'area controlli; il governo della correzione nell'area prompt e regimi. L'assenza della conclusione è valutata soltanto nell'ultima area, evitando doppie penalizzazioni.

## 1. Prompt 2 - Flusso logico-teorico

Nel quarto intervento lo studente propone una sequenza personale non vuota: variabili, funzione obiettivo, vincoli, trasformazione per il solver, benchmark, funzione parametrica, tre sensitività, confronto temporale, scenari e interpretazione. La richiesta delimita correttamente il Regime A: chiede verifica, completamento e ordinamento, esclude il codice e vieta modifiche al modello.

Il contributo resta però prevalentemente descrittivo. Non formalizza i quattro bilanci temporali, la traduzione del vincolo legacy, i rapporti di utilizzo, il trattamento delle configurazioni non ammissibili e il significato dei marginali. Questi elementi sono introdotti dall'IA. La proposta personale di compattamento consiste nella sola frase “compatterei il flusso logico-teorico in 6 tappe”; il raccordo concreto da dieci a sei tappe viene costruito dall'assistente e poi convalidato.

La tabella finale della cella 2 è complessivamente coerente, ma usa la relazione generica λ_i = ∂Π*/∂b_i senza distinguere il termine noto codificato dal parametro naturale. La distinzione è essenziale per il legacy, scritto come -(x3+x4) ≤ -35: il segno rispetto al termine noto del solver non coincide con quello rispetto alla soglia naturale 35. L'imprecisione riappare nel controllo numerico.

## 2. Prompt 3 - Scomposizione input-output

Il settimo intervento contiene una proposta operativa pertinente in sei tappe: impostazione, benchmark e controlli, funzione parametrica, sensitività, confronto fra ondate e scenari. Lo studente collega il benchmark a residuali, slack e vincoli attivi e prevede che la funzione parametrica riproduca il punto (1,1,1).

La tabella dettagliata di input, operazione, output, controllo e uso successivo viene però costruita dall'IA. La convalida non discute la concreta produzione di tutti gli output promessi. La tabella approvata prevede variazioni di tutte le componenti, marginali lungo le griglie e verifica dei 27 controlli, mentre il notebook finale non rende osservabili tali elementi in modo completo.

La scomposizione afferma inoltre di escludere i punti non ammissibili “dai grafici e dalle tabelle”. L'esclusione è corretta per i grafici, non per le tabelle: la Scheda richiede stato e fattibilità per ogni punto. Il codice finale conserva opportunamente le righe non ammissibili con valori NaN, ma la formulazione approvata resta imprecisa.

## 3. Notebook e output computazionali

### Correttezza del nucleo

Il vettore è ordinato correttamente come (x1,...,x5,g1,...,g4,u1,u2,u3). Funzione obiettivo, cinque uguaglianze, prudenziale, legacy, limite su x5, capacità di funding e non negatività sono implementati correttamente. La funzione parametrica modifica soltanto d1 con alpha, d4 con beta e le capacità con phi. res.x è letto soltanto dopo il controllo di successo; nei punti non ottimi vengono restituiti NaN.

Il benchmark coincide con la calibrazione docente:

| Quantità | Valore verificato |
|---|---|
| x* | (0; 36,1905; 0; 35; 28,8095) |
| g* | (0; 1,7967; 6,9485; 4,0140) |
| u* | (2,0357; 0; 0) |
| Π* | 3,8257 |

Il prudenziale e il legacy sono attivi. Le tre configurazioni di scenario sono ammissibili:

| Scenario | Π* | Perdita sullo Standard | u* |
|---|---:|---:|---|
| Standard | 3,8257 | 0,0000 | (2,0357; 0; 0) |
| Mediamente critico | 3,7976 | 0,0281 | (2,9957; 0; 0) |
| Critico | 3,7518 | 0,0739 | (3,0000; 0; 0) |

Le griglie assegnate sono rispettate. Alpha e beta sono ammissibili fino a 1,10 e non ammissibili a 1,15, coerentemente con la calibrazione docente. Phi mostra la saturazione di u1 per capacità basse e un plateau oltre la regione di scarsità.

### Output incompleti

| Requisito | Evidenza nel notebook | Valutazione |
|---|---|---|
| Tabelle 6-8: g, Delta x, Delta g, Delta u, vincoli attivi e marginali | Il DataFrame interno calcola livelli e variazioni, ma le tabelle mostrano soltanto Π, Delta Π, livelli di x e u e rapporti di funding. | Output richiesto non esposto. |
| Stato solver nelle Tabelle 6-8 | È mostrato solo il booleano success; messaggio e codice status non sono visualizzati. | Copertura parziale. |
| Tabella 9: confronto su Π, x, g, u, vincoli e fattibilità | Sono riportati Π, u1, u3, solo il legacy e la fattibilità. | Mancano composizione completa, giacenze, u2 e quadro dei vincoli. |
| Tabella 10: Π, perdita, x, g, u, vincoli, utilizzo e marginali | Sono presenti Π, perdita, x, u, rapporti e alcuni vincoli. | Mancano tutte le g e i marginali di scenario. |
| Bounds attivi benchmark | La Tabella 4 riporta soltanto le sei righe di A_ub. | Mancano i bounds inferiori attivi di x1, x3, g1, u2 e u3. |
| Figura 9: Π(phi) e funding rispetto alla capacità | Mostra soltanto Π(phi). | Manca la componente funding/capacità. |
| Figura 10: marginali o principali vincoli attivi | Mostra legacy, prudenziale e limite x5. | Omette il limite di u1, attivo proprio nella regione di capacità scarsa. |

Le quattordici figure sono comunque tutte presenti, numerate, leggibili e coerenti con i dati. La Figura 14 usa correttamente le date sull'asse orizzontale e una curva per scenario.

## 4. Prompt, regimi e governo dell'IA

Il tracciato documenta Prompt zero, Prompt 1, contributi iniziali nei Prompt 2 e 3, validazioni prima del codice e sviluppo progressivo. I prompt brevi “Tappa 2”, “Tappa 3” e successivi sono collegati a un contesto già fissato e non equivalgono automaticamente a delega globale.

È particolarmente positivo l'intervento 16 in Regime C. Lo studente osserva autonomamente che x è deciso a t=0 e non può essere “ricomposto successivamente” dopo lo shock. La criticità è reale, viene accolta e il testo della Tappa 5 è sostituito nel notebook.

Il ciclo critico non viene però chiuso completamente. Il testo sostitutivo non usa il principale riscontro numerico: lungo beta la soluzione e Π* restano invariati fino a 1,10 perché l'aumento del fabbisogno terminale riduce innanzitutto g4, che non entra nell'obiettivo. Il testo afferma inoltre che il funding precedente deve essere rimborsato “entro t=3”, mentre u3 è rimborsato nel bilancio di t=4. Lo studente accetta la risposta senza confrontarla con tabelle e bilanci e poi dichiara tutto consistente.

I 18 interventi superano l'indicazione orientativa di 9-10 prompt della Scheda Costruzione. Non si applica una detrazione automatica: l'intervallo non è riportato nella Scheda Caso destinata allo studente e gli interventi comprendono conferme, richieste di formato e una verifica motivata.

## 5. Verifiche logiche e controlli numerici

Sono effettivi e positivi: stato del solver, residuali delle cinque uguaglianze, controlli indipendenti di prudenziale, legacy e x5, slack delle sei disuguaglianze, riproduzione del benchmark, isolamento dei parametri, esclusione degli infeasible dai grafici e monotonia delle perdite di scenario.

Il limite principale è la verifica del marginale legacy:

| Grandezza | Valore |
|---|---:|
| Marginale teorico riportato | +0,004887 |
| Marginale empirico aumentando la soglia da 35 a 35,001 | -0,004887 |
| Errore assoluto | 9,77e-03 |

Il risultato non verifica il marginale: ne mostra il segno opposto. Il duale +0,004887 è riferito al termine noto codificato b_ub=-35, mentre la perturbazione aumenta la soglia naturale L=35 e quindi diminuisce b_ub. Rispetto a L il marginale corretto è -0,004887; rispetto a b_ub è +0,004887. Occorre dichiarare la variabile perturbata e applicare la catena dei segni. Il notebook mostra il fallimento ma non contiene un assert, una classificazione dell'esito o una correzione.

Ulteriori limiti:

- la “verifica completa” finale controlla soltanto quattro proprietà degli scenari, non i 27 punti della Scheda;
- la classificazione dei vincoli attivi esclude bounds inferiori e, lungo phi, il limite di u1;
- success=False è descritto sempre come inammissibilità; nei punti assegnati è vero, ma la funzione generale dovrebbe distinguere gli status;
- non viene confrontata la struttura delle tabelle promessa nel Markdown con quella effettivamente visualizzata;
- la validazione finale non reagisce all'errore non nullo del test marginale.

Il merito per la criticità sulla ricomposizione di x resta riconosciuto, ma non compensa la mancata verifica numerica richiesta esplicitamente.

## 6. Interpretazione critica finale

Il tracciato termina con una dichiarazione di coerenza e validazione complessiva. Non compare un'interpretazione quantitativo-finanziaria autonoma che colleghi la diversa risposta ad alpha e beta, il ruolo di g4 nella neutralità locale di beta, la saturazione di u1, il cambio del prudenziale nello scenario Critico, la ricomposizione fra x2 e x5 e i limiti deterministici del modello.

La conclusione richiesta è quindi assente. Non si afferma che sia stata delegata all'IA: non è stata prodotta.

## Restituzione allo studente

La formulazione primale, la funzione parametrica e i risultati numerici principali sono solidi. È positivo avere individuato autonomamente l'errore sulla presunta ricomposizione successiva dell'attivo. Per completare il lavoro occorre correggere e spiegare il segno del marginale legacy, rendere visibili nelle Tabelle 6-10 tutti i livelli e le variazioni richieste, includere bounds e capacità di funding fra i vincoli attivi, completare la Figura 9 e scrivere un'interpretazione finale autonoma fondata sui risultati effettivi, in particolare sul ruolo di g4 nello shock terminale.
