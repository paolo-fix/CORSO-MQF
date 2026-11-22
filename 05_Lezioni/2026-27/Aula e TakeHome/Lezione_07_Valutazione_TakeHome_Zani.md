# Valutazione TakeHome Lezione 07 Zani

Data: 22 novembre 2026.

**Risultato: 68/100.** Valutazione individuale della coppia di file con suffisso `Zani`.

## Riferimenti e criterio di attribuzione

Si applicano esclusivamente `00_MasterPlan/MQF_Project_Guidelines.md` (??14.10 e 15.8-15.12), `04_Codice/Lez07/Lezione_07_Scheda_Caso_TakeHome.md` (??3-8) e `04_Codice/Lez07/Lezione_07_Scheda_Costruzione_Caso_TakeHome.md` (??7,12,15,16,18).

I massimi delle sei aree sono quelli normativi. I punti entro ciascuna area costituiscono un giudizio motivato: non sono decurtazioni automatiche stabilite dalle Guidelines. Non si applicano soglie di sufficienza, conversioni in trentesimi o un prezzo-obiettivo. La qualit? della risposta IA non ? confusa con il contributo iniziale dello studente, e un dubbio poi respinto pu? comunque documentare un utile processo critico.

## Materiali e verifica

- Notebook: [Lezione_07_Notebook_TakeHome_Zani.ipynb](Lezione_07_Notebook_TakeHome_Zani.ipynb), 14 celle, delle quali 5 di codice.
- Tracciato: [Lezione_07_Tracciato_TakeHome_Zani.pdf](Lezione_07_Tracciato_TakeHome_Zani.pdf), 32 pagine; presenti Prompt zero, Prompt 1, Prompt 2 e Prompt 3.

Sono stati esaminati contributi iniziali, risposte e revisioni pertinenti nel PDF, tutte le celle del notebook, codice e output incorporati. Le pagine centrali del PDF e i grafici sono stati controllati anche visivamente. Le cinque celle sono state eseguite in ordine in ambiente Python con backend grafico non interattivo, mantenendo la funzione display disponibile come in Jupyter. Le prime prove in Python semplice richiedevano questa predisposizione: la disponibilit? di display non ? stata trattata come errore degli studenti. I file originali sono invariati.

SHA256 notebook: `be56b0a6a3b5a1b7f72b75e6af56f6b759125fde54cb6a9a65448d77fca71332`.

## Punteggi

| Area | Punti | Massimo |
|---|---:|---:|
| Prompt 2 e flusso logico teorico | 22 | 30 |
| Prompt 3 e scomposizione input output | 9 | 15 |
| Notebook e output computazionali | 15 | 20 |
| Prompt di tappa e regimi IA | 11 | 15 |
| Verifiche logiche e controlli numerici | 8 | 15 |
| Interpretazione finanziaria finale | 3 | 5 |
| **Totale** | **68** | **100** |

## 1 Prompt 2 e flusso logico teorico

**22/30.** Alle pp.11-12 la proposta iniziale richiama SDE accoppiate, drift stocastico, discretizzazioni, correlazione tramite Cholesky, simulazione, payoff e sconto. ? pertinente e non vuota.

Mancano per? nella proposta autonoma la media dei dodici fixing e l'esclusione di S0, la Riemann sinistra per replica e un'articolazione esplicita di aggregazione, errore standard e diagnostica. La correlazione va logicamente costruita prima dell'evoluzione delle traiettorie, come riordina l'IA. Il flusso finale nella cella 2 completa i contenuti, ma ci? non attribuisce retroattivamente allo studente tutti i dettagli della risposta assistita.

## 2 Prompt 3 e scomposizione input output

**9/15.** A p.13 sono proposti cinque blocchi: input, simulazione, valori per replica, aggregazione e controlli. La distinzione fra singola replica e media Monte Carlo ? riconoscibile.

La proposta non specifica sistematicamente output, controlli e dipendenze per ciascuna tappa, non alloca puntualmente tabelle e grafici e non isola i fixing. L'IA costruisce una mappa pi? completa in sei tappe (pp.13-15 e cella 3), aggiungendo media asiatica e diagnostica dedicata. Il credito dell'area riguarda la proposta iniziale e la mappa risultante; la mancata esecuzione della sesta tappa ? valutata nelle aree prodotto e controlli, non usata per una seconda penalit? sulla stessa omissione.

## 3 Notebook e output computazionali

**15/20.** Le celle di codice 5,7,9,11,13 si eseguono in ordine senza errori e implementano correttamente la parte principale: shock correlati, CIR con max soltanto sotto radice, drift r-q, fixing mensili senza S0, payoff e sconto Riemann sinistra per replica.

Il notebook consegnato termina dopo la Tappa 5 di pricing e il commento conclusivo. Mancano la Tabella 4 di diagnostica e il Grafico 5 di convergenza. La Tappa 6 ? prevista nella cella 3 ma non implementata; nel PDF di 32 pagine non compare una sua richiesta/esecuzione, e la conversazione passa dal pricing al commento finale (pp.28-32).

Gli output salvati della cella 13 riportano prezzo 260,1725 e IC [256,4768;263,8681]. La riesecuzione ordinata con seed 12345 produce invece prezzo 255,153870, SE 1,844978, IC [251,537714;258,770026], esercizio 45,938%. Anche i grafici salvati non coincidono con quelli degli altri due notebook, mentre i tre codici ordinati producono la stessa base. La causa non ? dimostrata: non si presume un modello alterato n? un comportamento scorretto. Si rileva l'incoerenza fra codice consegnato e output incorporati. Il prezzo salvato, preso isolatamente, non ? prova di una formula errata.

## 4 Prompt di tappa e regimi IA

**11/15.** Il PDF comprende inizializzazione, Scheda Caso, Prompt 2 e 3, cinque tappe B e un dubbio C su media asiatica e valore terminale (pp.24-25). Lo studente individua un risultato da comprendere, propone una possibile spiegazione legata al drift e chiede una verifica mirata. Il dubbio ? respinto e non vengono introdotte modifiche arbitrarie al modello.

Nel ragionamento iniziale compare un'imprecisione fra theta_r e il dividend yield q; la risposta distingue r-q, ma la frase secondo cui la media asiatica risulta maggiore del terminale deve essere intesa come confronto aggregato osservato, non come ordinamento garantito per ciascuna traiettoria. Il commento finale recepisce l'idea di drift contenuto.

Il processo non completa tutte le tappe della mappa validata e non rileva la discordanza degli output salvati. Le validazioni restano per lo pi? implicite. La richiesta finale contiene gi? il testo dello studente e viene semplicemente formattata: non viene penalizzata come delega integrale dell'interpretazione. Nessuna carenza ? imputata alla mancanza di prompt iniziali, che sono presenti.

## 5 Verifiche logiche e controlli numerici

**8/15.** I controlli 1-7 sono implementati: correlazione, positivit? del sottostante, diagnostica dei tassi negativi, media fra estremi dei fixing, payoff, sconto e prodotto per replica. La correlazione riprodotta ? -0,249577; i controlli di costruzione risultano soddisfatti.

Non vengono eseguiti i controlli 8 e 9: andamento del SE per M=1000,5000,10000,50000 e confronto con una griglia pi? fine. Non ? quindi documentata la robustezza numerica richiesta dalla specifica. Il Controllo 10 ? presentato come fissaggio del seed, ma gli output salvati non sono riprodotti dalla riesecuzione ordinata e manca un confronto esplicito di verifica.

Si distinguono le due dimensioni: l'area notebook valuta completezza e coerenza degli output; quest'area valuta le verifiche effettivamente svolte. Non si aggiungono decurtazioni esterne alla rubrica.

## 6 Interpretazione finanziaria finale

**3/5.** La cella 14, corrispondente al testo fornito alle pp.31-32, collega q vicino al livello medio del tasso a una crescita contenuta e una frequenza di esercizio prossima al 50%. ? un commento economico pertinente, fornito dallo studente.

La probabilit? di esercizio non segue per? dalla sola vicinanza tra drift e zero e strike e S0: rilevano distribuzione della media asiatica e volatilit?. Mancano lettura del prezzo e dell'IC, distinzione esplicita Q/probabilit? fisica, path-dependence e limiti del modello. Non sono discussi gli effetti dei controlli numerici mancanti. Si riconosce il nucleo corretto senza attribuire il massimo.

## Giudizio conclusivo

La costruzione principale del prezzo ? corretta nel codice rieseguito e il tracciato mostra contributi autonomi. La consegna resta incompleta nella diagnostica e presenta output salvati non coerenti con la riesecuzione. Sono carenze sostanziali del pacchetto, distinte dalla plausibilit? del prezzo isolato.

**Valutazione individuale: 68/100.**
