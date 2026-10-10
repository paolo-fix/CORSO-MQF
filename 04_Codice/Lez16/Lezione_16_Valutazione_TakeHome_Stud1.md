# Valutazione dello studente 1 sul caso take-home della lezione 16

Data della valutazione: 10 ottobre 2026.

**Valutazione proposta: 77/100.** Il modello multistadio, il rilassamento anticipativo e il benchmark wait-and-see sono implementati correttamente e producono risultati riproducibili. Il tracciato mostra contributi iniziali pertinenti e un intervento autonomo significativo sulla verifica della non anticipatività, recepito nel notebook. La valutazione è limitata da un'esposizione non corretta dei costi di adattamento, da output incompleti o poco leggibili e, soprattutto, da una conclusione prodotta dall'IA e trasferita nel notebook con valori incompatibili con i risultati effettivi.

Si applica la griglia su 100 punti della sezione 15.11 delle [Guidelines](../../00_MasterPlan/MQF_Project_Guidelines.md), direttamente pertinente al take-home con uso documentato dell'IA. I punteggi sono giudizi motivati entro i pesi assegnati, non detrazioni automatiche stabilite dalle Guidelines. L'equivalente puramente lineare è **23,1/30**; non si presume una regola istituzionale di conversione o arrotondamento.

## Materiali esaminati e metodo

La valutazione riguarda esclusivamente il caso **UK LDI 2022 — Buffer di liquidità, margin call e non anticipatività**. Sono stati acquisiti da GitHub, repository `paolo-fix/CORSO-MQF`, ramo `main`, i seguenti materiali:

| Materiale | Identificativo Git del contenuto acquisito |
|---|---|
| Guidelines, in particolare §§ 15.6–15.12 | `c97461e513ef986d964e5fc92568d7cd14942c0c` |
| [Scheda Caso TakeHome](Lezione_16_Scheda_Caso_TakeHome.md) | `46efb0eaf1e04a78f7f063ef518086fd03964a15` |
| [Scheda Costruzione Caso TakeHome](Lezione_16_Scheda_Costruzione_Caso_TakeHome.md) | `7546cb67e29070719b8f86617f092e56b099af51` |
| [Notebook TakeHome dello studente 1](Lezione_16_Notebook_TakeHome_Stud1.ipynb) | `07399164f267020274d32501282807e6e5b467e9` |
| [Tracciato IA in DOCX](Lezione_16_Tracciato_TakeHome_Stud1.docx) | `36703da33e6cee48544693438725ccd8f180a5d9` |

I file locali esaminati coincidono con i contenuti acquisiti da GitHub; per i Markdown sono stati normalizzati i fine riga Windows. Il tracciato è stato letto direttamente dal DOCX, senza necessità di accedere alla conversazione online. Contiene 31 interventi utente, comprese apertura, conferme, richieste di formato e correzioni tecniche; non contiene immagini incorporate.

Il notebook comprende **16 celle, di cui 6 di codice**. La numerazione delle celle citata parte da 1. Le sei celle di codice sono state eseguite in ordine in un processo Python pulito, con NumPy 2.1.3, SciPy 1.15.3, pandas 2.2.3 e Matplotlib 3.10.0. Gli output standard coincidono esattamente con quelli salvati. È stata verificata anche la riproduzione esatta delle cinque tabelle HTML incorporate. I tre grafici salvati sono stati ispezionati visivamente. Gli avvisi di `plt.show()` durante la verifica dipendono dal backend non interattivo del valutatore.

Una formulazione indipendente per percorso, con eliminazione di `b`, `g` e `G` e uguaglianze informative esplicite, conferma i risultati dei tre modelli. In essa `b = 100 - h`, il residuo intermedio è `g = 100 - (1+a)h + u + y` e quello terminale è `G = 100 - (1+a+beta)h + u + (1+beta)y + z + v`. Sono imposte le rispettive non negatività e i limiti operativi. MS mantiene comuni `h` su tutti i percorsi e `y,u` sui percorsi con lo stesso padre; AR mantiene comune solo `h`; WS separa tutti i percorsi. Le verifiche aggiuntive del valutatore non sono attribuite allo studente. Gli elaborati originali non sono stati modificati.

## Griglia numerica

| Area delle Guidelines | Massimo | Assegnato | Motivazione sintetica |
|---|---:|---:|---|
| Prompt 2 — Flusso logico-teorico risolutivo | 30 | **24** | Proposta personale pertinente e ben ordinata, con struttura informativa e distinzione MS/AR/WS; formalizzazione e collegamenti puntuali ai controlli sviluppati soprattutto dall'IA. |
| Prompt 3 — Scomposizione input-output | 15 | **13** | Proposta operativa coerente, controllo dedicato e corretta costruzione dei benchmark; dettaglio dei prodotti intermedi e copertura degli output non pienamente governati. |
| Notebook Jupyter e output computazionali | 20 | **15** | Modelli e ottimi corretti e riproducibili; costi tabellari non coerentemente attribuiti, alcuni risultati non esposti e albero graficamente poco leggibile. |
| Prompt e uso dei regimi A/B/C | 15 | **13** | Sequenza controllata, validazioni prima del codice e intervento C autonomo con sostituzione delle celle; controllo del ruolo dell'IA non mantenuto nella fase conclusiva. |
| Verifiche logiche e controlli numerici | 15 | **12** | Controlli MS sostanziali, probabilità e gerarchia corrette; valida individuazione del controllo tautologico, ma verifica finale e copertura dei benchmark non complete. |
| Interpretazione critica finale | 5 | **0** | Testo generato dall'IA senza bozza autonoma documentata, con dati decisionali errati e senza discussione dei limiti del modello. |
| **Totale** | **100** | **77** | |

Il punteggio riconosce separatamente la correttezza del prodotto computazionale e il contributo osservabile dello studente. La correzione sulla non anticipatività è valorizzata; gli errori tecnici iniziali poi corretti non producono una penalizzazione automatica. Le carenze sono considerate nella loro area prevalente: costi e completezza degli output nel notebook, qualità delle verifiche nei controlli, autonomia e contenuto della conclusione nell'ultima area. Non sono applicate detrazioni fisse cumulative per il medesimo errore.

## 1. Prompt 2 e flusso teorico — 24/30

Il tredicesimo intervento utente, in Regime A, propone sette passaggi. Lo studente distingue le decisioni iniziali `b,h`, i due momenti di rivelazione dell'incertezza e le scelte disponibili nei nodi; introduce l'albero e le probabilità condizionate; richiama bilanci, margin call, limiti operativi e funzione obiettivo attesa. Prevede poi la soluzione rispettosa dell'informazione disponibile, il confronto con decisioni intermedie dipendenti dal percorso finale e il benchmark wait-and-see con EVPI.

Il contributo è specifico del caso e coglie il suo nodo concettuale: una decisione intermedia può dipendere dalla storia già osservata, ma non dal ramo terminale ancora ignoto. Non è una richiesta generica di risolvere il problema. L'ordine è coerente e lo studente chiede espressamente di verificare e completare senza codice, senza anticipare la scomposizione e senza cambiare modello.

La proposta rimane tuttavia in larga parte descrittiva. Non esplicita personalmente le formule delle probabilità di percorso, i due bilanci, i pesi distinti dei costi intermedi e terminali, la dipendenza della seconda margin call da `h-y`, né la formula di `Delta_NA` e l'intera gerarchia dei valori. Questi elementi sono sviluppati nella risposta IA e nella tabella finale della cella 2. La validazione successiva è generale, non accompagnata da una verifica analitica dei passaggi.

La tabella finale è sostanzialmente corretta e coerente con la Scheda Caso. L'intervento successivo in Regime C conferma che il tema della non anticipatività non è rimasto soltanto una formula riprodotta: lo studente distingue effettivamente l'incorporazione strutturale del vincolo dalla qualità del controllo presentato. Si riconosce quindi una buona comprensione della struttura, senza attribuire piena autonomia alla formalizzazione elaborata dall'IA.

## 2. Prompt 3 e scomposizione input-output — 13/15

Il sedicesimo intervento utente propone sei tappe: ricostruzione dell'albero; modello MS; controlli della soluzione; rilassamento AR con `b,h` ancora comuni; quattro problemi WS separati; organizzazione e confronto economico degli output.

È particolarmente positivo che i controlli costituiscano una tappa autonoma prima dei benchmark e che lo studente precisi personalmente quali decisioni devono restare comuni in AR. La richiesta di mantenere visibile il collegamento fra output di una tappa e input della successiva è appropriata. La proposta rende riconoscibili operazioni, risultati e scopi dei confronti.

Il dettaglio sistematico delle strutture dati, delle singole tabelle e delle verifiche è demandato alla risposta IA. La tabella accettata, cella 3, non esplicita `z_MS` tra gli input della tappa 4, pur utilizzandolo per `Delta_NA`; prevede i valori WS per percorso, che vengono calcolati ma non esposti negli output finali. La scomposizione è quindi ben impostata, ma la sua validazione non si traduce in un controllo completo delle dipendenze e della consegna dei risultati.

## 3. Notebook, correttezza e output — 15/20

### Formulazioni corrette

Il codice rispetta parametri, struttura temporale, bounds e bilanci della Scheda Caso. La seconda margin call è correttamente applicata all'esposizione residua `h-y`. I costi intermedi MS sono ponderati con le probabilità dei nodi e quelli terminali con le probabilità dei percorsi. Nel rilassamento, anche i costi intermedi specifici del percorso sono correttamente ponderati con le probabilità dei percorsi.

MS utilizza 20 variabili: due iniziali, tre per ciascuno dei due nodi intermedi e tre per ciascuno dei quattro terminali. AR utilizza 26 variabili, mantenendo un'unica coppia iniziale. WS risolve quattro problemi distinti di otto variabili ciascuno. Il solver è controllato prima di estrarre le soluzioni. Le probabilità WS sono applicate nell'aggregazione dei quattro valori, non impropriamente all'interno dei singoli problemi deterministici.

Nella cella 7 rimane un commento che parla di «18 variabili» e di 20 variabili «ridotte a 18 per eleganza»: è un refuso descrittivo, perché `len(var_names)` e le matrici effettive sono correttamente dimensionati a 20. Non viene confuso con un errore del modello.

### Risultati verificati

| Quantità | Valore |
|---|---:|
| Probabilità MR, MP, SR, SS | 0,39; 0,26; 0,1575; 0,1925 |
| Buffer `b_MS` | **9,090909** |
| Esposizione `h_MS` | **90,909091** |
| Rendimento iniziale lordo MS | 4,181818 |
| Costi intermedi attesi MS | 0,217742 |
| Costi terminali attesi MS | 0,172135 |
| Costi totali attesi MS | **0,389878** |
| `z_MS` | **3,791941** |
| `z_AR` | **3,818640** |
| `Delta_NA = z_AR - z_MS` | **0,026699** |
| `z_WS` | **3,990026** |
| `EVPI = z_WS - z_MS` | **0,198086** |

Le decisioni della soluzione MS sono:

| Nodo intermedio | Deleveraging `y` | Liquidità aggiuntiva `u` | Residuo `g` |
|---|---:|---:|---:|
| M | 0 | 0 | 0 |
| S | 9,242424 | 4 | 2,333333 |

| Percorso terminale | Deleveraging `z` | Liquidità aggiuntiva `v` | Residuo `G` |
|---|---:|---:|---:|
| MR | 0 | 0 | 0 |
| MP | 9,090909 | 0 | 0 |
| SR | 1,75 | 0 | 0 |
| SS | 10 | 4 | 0 |

In AR la coppia iniziale rimane `(9,090909; 90,909091)`, ma le decisioni intermedie sul ramo severo diventano:

| Percorso | `y_AR` | `u_AR` | `g_AR` |
|---|---:|---:|---:|
| SR | 6,909091 | 4 | 0 |
| SS | 17,575758 | 4 | 10,666667 |

Su MR e MP i tre ricorsi intermedi AR sono nulli. La differenziazione sul ramo S mostra l'anticipazione illegittima della seconda osservazione. Il confronto non modifica la decisione iniziale e non coincide con WS.

I risultati deterministici WS, calcolati correttamente nel dizionario `z_ws_path` ma non mostrati dal notebook, sono:

| Percorso | Buffer WS | Esposizione WS | Valore WS |
|---|---:|---:|---:|
| MR | 0 | 100 | 4,270000 |
| MP | 0 | 100 | 4,082000 |
| SR | 18,032787 | 81,967213 | 3,786885 |
| SS | 29,577465 | 70,422535 | 3,464789 |

È confermata la gerarchia `3,791941 < 3,818640 < 3,990026`. I risultati coincidono anche con i riferimenti numerici della Scheda Costruzione.

### Costi di adattamento nella Tabella 2

La cella 15 costruisce ogni riga di percorso sommando:

`p_n * (lambda_n*y_n + kappa_n*u_n) + p_l * (mu_l*z_l + eta_l*v_l)`.

La colonna denominata «Costo Adatt. Atteso (Tot)» mescola così un contributo dell'intero nodo con un contributo del singolo percorso. Lo stesso costo intermedio ponderato di S viene riportato sia su SR sia su SS. Le righe non rappresentano né costi condizionati al percorso, né contributi additivi al costo atteso complessivo.

| Percorso | Colonna consegnata | Contributo atteso correttamente attribuito al percorso |
|---|---:|---:|
| MR | 0 | 0 |
| MP | 0,047273 | 0,047273 |
| SR | 0,223255 | 0,103497 |
| SS | 0,337092 | 0,239108 |
| **Somma** | **0,607620** | **0,389878** |

Per una tabella additiva per percorso, il peso `p_l` deve moltiplicare tutti i costi sostenuti su quel percorso; in alternativa si possono presentare separatamente costi intermedi per nodo e terminali per percorso. Il notebook non usa la somma della colonna errata per calcolare `z_MS`: l'ottimo del solver è corretto. La criticità riguarda il prodotto tabellare e la possibilità di riconciliare i costi con l'obiettivo.

### Completezza e leggibilità

Le cinque tabelle e i tre grafici sono presenti, ma con alcune limitazioni:

- **Tabella 1:** mancano i limiti operativi richiesti, pur correttamente definiti nel codice e richiamati nelle celle teoriche.
- **Tabella 4:** il confronto è trasposto rispetto alla disposizione richiesta; la trasposizione, da sola, non è un problema sostanziale. Sono invece generiche le voci WS sulle decisioni iniziali e di adattamento, nonostante le soluzioni siano disponibili. Mancano negli output i quattro valori `z_l_WS`; per AR sono mostrati i quattro `y_l`, ma non un riepilogo completo dei ricorsi intermedi `u_l,g_l` richiesti fra le quantità da determinare. Si distingue quindi ciò che è calcolato da ciò che è effettivamente reso osservabile.
- **Figura 1:** le stringhe raw conservano `\n` come testo letterale anziché come a capo. I riquadri rimangono larghi, le etichette si sovrappongono ai rami e parte delle probabilità è coperta. L'albero è strutturalmente corretto, ma la sua leggibilità è compromessa.
- **Figure 2 e 3:** sono leggibili e coerenti con i risultati; mostrano bene il deleveraging terminale e la divergenza delle decisioni AR fra SR e SS.

## 4. Uso dell'IA e dei regimi — 13/15

Il Prompt zero definisce correttamente regimi, responsabilità e divieto di delegare la conclusione. La sequenza procede dalla Scheda Caso al flusso teorico, alla scomposizione validata e poi al codice per tappe. I prompt brevi «Tappa 2», «Tappa 3» e successivi sono ammissibili nel contesto già fissato, come previsto dalle Guidelines; non rappresentano automaticamente delega globale.

Lo studente segnala errori di formattazione, problemi di escape nelle stringhe del grafico e avvisi del codice. Questi interventi documentano attenzione all'esecuzione, ma hanno peso metodologico minore della revisione concettuale successiva. Non si addebitano allo studente gli errori linguistici iniziali dell'IA poi corretti.

Nel ventottesimo intervento, in Regime C, lo studente individua precisamente che il confronto di una variabile con se stessa è tautologico. Spiega anche che la scelta di variabili per nodo dovrebbe già incorporare la non anticipatività: è una distinzione corretta e autonoma. Chiede all'IA un esito esplicito, accoglimento o rigetto, e solo le celle sostitutive della tappa interessata, senza alterare modello e risultati. Il notebook contiene le celle sostitutive e il tracciato documenta la domanda sulla loro riesecuzione. Questo è un uso appropriato e sostanziale del Regime C.

Il controllo del ruolo dell'IA non rimane altrettanto saldo nella fase conclusiva. Alla semplice richiesta «Tappa 6» l'IA produce anche l'interpretazione finale, nonostante il Prompt zero ne riservi la responsabilità allo studente. Il testo viene trasferito nel notebook; alla successiva domanda se vada modificato, lo studente accetta la rassicurazione dell'IA e convalida tutto senza una propria bozza critica documentata. Il rilievo di processo è distinto dalla valutazione del contenuto della conclusione, discussa nell'ultima area.

La Scheda Costruzione indica un intervallo di 9–11 prompt, ma il limite non è riportato nella Scheda Caso consegnata né risulta una distinta comunicazione nel tracciato. Le Guidelines richiedono che tale vincolo sia comunicato: **non si applica una penalizzazione automatica per i 31 interventi**. Il DOCX è il formato indicato dal docente per l'esame del tracciato e non determina penalizzazioni.

## 5. Verifiche e controlli — 12/15

Sono presenti e superati i controlli sulle probabilità nodali, condizionate e di percorso; risorse e copertura minima; bounds e non negatività; bilanci intermedi e terminali MS; deleveraging complessivo; stato dei solver; unicità delle decisioni iniziali AR; gerarchia dei tre valori ed EVPI.

La verifica autonoma sul controllo tautologico è un punto di merito rilevante secondo le Guidelines: lo studente riconosce una debolezza metodologica della risposta IA, la segnala e ne recepisce una correzione mirata. Le celle 8 e 9 rendono ora esplicita la mappatura delle decisioni nodali sui percorsi, e la Tabella 3 confronta MR/MP e SR/SS.

Occorre però qualificare correttamente il risultato: anche dopo la correzione, i valori confrontati derivano dallo stesso oggetto nodale. La mappatura rende trasparente la proprietà garantita dalla formulazione; non costituisce un test indipendente capace di scoprire qualsiasi errore nella matrice del modello. Non si richiede di duplicare artificialmente le variabili né si considera violata la non anticipatività: l'ispezione delle matrici conferma che è correttamente incorporata. Il merito dello studente è aver individuato la distinzione e migliorato la documentazione, non aver riparato un modello anticipativo che prima fosse errato.

Rimangono alcuni limiti:

- I controlli dettagliati di ammissibilità e dei bilanci sono svolti per MS. AR e WS controllano il successo del solver e le relazioni tra obiettivi, ma non ripetono una verifica esplicita completa dei residuali e dei bounds delle rispettive soluzioni. I modelli risultano comunque ammissibili alla verifica indipendente.
- Il controllo 16 usa un'uguaglianza esatta per `b+h==A0` e la presenza delle chiavi `b,h`: la comunanza tra percorsi è garantita dalla struttura delle variabili, non dal solo test sulle chiavi. Una tolleranza numerica e una spiegazione strutturale renderebbero il controllo più preciso.
- Manca una riconciliazione autonoma del risultato economico con i costi presentati negli output e una revisione complessiva fra dati calcolati, grafici e conclusione. L'intervento C, pur valido, si concentra sulla tappa 3 e non dimostra il controllo di tutte le parti finali.

Il richiamo a «15 controlli» nella tappa 3 è impreciso rispetto agli identificativi 4–13 e 15 effettivamente elencati: è una questione descrittiva secondaria. La valutazione si basa sui controlli realmente eseguiti, non sul conteggio dichiarato. Le criticità specifiche dei costi e della conclusione sono valutate nelle rispettive aree, senza aggiungere qui detrazioni automatiche per gli stessi valori errati.

## 6. Interpretazione critica finale — 0/5

La conclusione è presente nella cella 16, ma non soddisfa il requisito delle Guidelines secondo cui deve essere scritta dallo studente e sottoposta all'IA solo per revisione critica. Il tracciato ne documenta la produzione da parte dell'IA nella risposta al ventisettesimo intervento, senza una precedente bozza personale. Il contenuto è stato trasferito nel notebook e poi convalidato. Il giudizio si fonda su questa sequenza osservabile, non su un'inferenza sullo stile del testo.

La conclusione contiene inoltre errori sostanziali:

| Grandezza MS | Affermazione nella conclusione | Risultato effettivo del notebook |
|---|---:|---:|
| Buffer `b` | 0 | **9,090909** |
| Esposizione `h` | 100 | **90,909091** |
| Deleveraging `y_M` | 10 | **0** |
| Deleveraging `y_S` | 25, massimo consentito | **9,242424**, inferiore a 25 |
| Residuo `g_S` | 7 | **2,333333** |

Queste discrepanze non dipendono da arrotondamenti e non sono introdotte dalla sostituzione della tappa 3. Alterano la spiegazione del ruolo del buffer e dei limiti effettivamente attivi. L'affermazione sul massimo deleveraging intermedio è smentita anche dalla Figura 2. Nella soluzione corretta si saturano `u_S=4`, `z_SS=10` e `v_SS=4`, mentre `y_S` non raggiunge 25.

Il testo descrive in termini generali AR, WS, `Delta_NA` ed EVPI in modo sostanzialmente corretto, ma non ne discute i valori ottenuti e non richiama i limiti del modello. La risposta IA al trentesimo intervento rassicura lo studente sulla validità della conclusione senza confrontarla con gli output; la convalida finale lascia gli errori nel prodotto consegnato.

Qui ricorre precisamente il caso previsto dalle Guidelines: l'errore IA non è penalizzato perché prodotto dall'IA, ma perché **accettato senza correzione e trasferito nell'interpretazione finale**. L'intervento autonomo sulla non anticipatività resta valorizzato nelle aree dei regimi e dei controlli; non sostituisce una conclusione finanziaria autonoma e coerente con i risultati.

## Indicazioni formative per completare il lavoro

Le indicazioni che seguono sono del valutatore e non sono attribuite allo studente ai fini del punteggio.

La conclusione dovrebbe partire dal buffer positivo. Con `b=9,090909` e `h=90,909091`, il buffer copre esattamente la prima margin call del nodo M, pari a `0,10*h`, senza deleveraging o liquidità aggiuntiva intermedia. Nel nodo S, invece, la prima margin call vale 20 e il bilancio è:

`9,090909 + 4 + 9,242424 = 20 + 2,333333`.

Il residuo viene riportato al secondo stadio. Sul percorso SS la seconda margin call è `0,20*(90,909091-9,242424)=16,333333`: la copertura combina residuo 2,333333, deleveraging terminale 10 e liquidità aggiuntiva 4. La capacità terminale limitata rende quindi economicamente rilevante la scelta intermedia, pur senza portare `y_S` al massimo di 25.

Nel modello MS la stessa scelta al nodo S deve servire sia SR sia SS. AR ottiene un vantaggio di 0,026699 differenziando prematuramente tali scelte, mentre mantiene comune l'allocazione iniziale. WS conosce già al tempo zero il percorso completo e può differenziare anche il buffer: il suo vantaggio rispetto a MS, 0,198086, è l'EVPI. `Delta_NA` è una diagnostica della violazione informativa e non va confusa con VSS o EVPI.

La riconciliazione economica corretta è:

`4,181818 - 0,217742 - 0,172135 = 3,791941`.

Occorre correggere la colonna dei costi, esporre i risultati WS per percorso e i ricorsi intermedi AR, completare i limiti nella Tabella 1, migliorare gli a capo e le sovrapposizioni nell'albero e riscrivere autonomamente il commento finale sui dati effettivi.

La lettura finanziaria deve restare entro le ipotesi del caso: probabilità e parametri esogeni, costi lineari, una unità di liquidità per unità di deleveraging, capacità di aggiustamento limitate e albero discreto molto piccolo. Il modello non rappresenta prezzi dei gilt, impatto delle vendite sui prezzi, contratti reali di collateral o interventi endogeni della Bank of England. Descrive un problema didattico di liquidità e margin call, non una ricostruzione storica di un fondo né una misura della sua insolvenza.

**Il punteggio di 77/100 riguarda il materiale consegnato**, senza attribuire credito anticipato alle integrazioni suggerite.
