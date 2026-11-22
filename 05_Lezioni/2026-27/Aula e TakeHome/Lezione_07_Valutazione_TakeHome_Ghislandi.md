# Valutazione TakeHome Lezione 07 Ghislandi

Data: 22 novembre 2026.

**Risultato: 80/100.** Valutazione individuale della coppia di file con suffisso `Ghislandi`.

## Riferimenti e criterio di attribuzione

Si applicano esclusivamente `00_MasterPlan/MQF_Project_Guidelines.md` (??14.10 e 15.8-15.12), `04_Codice/Lez07/Lezione_07_Scheda_Caso_TakeHome.md` (??3-8) e `04_Codice/Lez07/Lezione_07_Scheda_Costruzione_Caso_TakeHome.md` (??7,12,15,16,18).

I massimi delle sei aree sono quelli normativi. I punti entro ciascuna area costituiscono un giudizio motivato: non sono decurtazioni automatiche stabilite dalle Guidelines. Non si applicano soglie di sufficienza, conversioni in trentesimi o un prezzo-obiettivo. La qualit? della risposta IA non ? confusa con il contributo iniziale dello studente, e un dubbio poi respinto pu? comunque documentare un utile processo critico.

## Materiali e verifica

- Notebook: [Lezione_07_Notebook_TakeHome_Ghislandi.ipynb](Lezione_07_Notebook_TakeHome_Ghislandi.ipynb), 14 celle, delle quali 5 di codice.
- Tracciato: [Lezione_07_Tracciato_TakeHome_Ghislandi.pdf](Lezione_07_Tracciato_TakeHome_Ghislandi.pdf), 51 pagine; presenti Prompt zero, Prompt 1, Prompt 2 e Prompt 3.

Sono stati esaminati contributi iniziali, risposte e revisioni pertinenti nel PDF, tutte le celle del notebook, codice e output incorporati. Le pagine centrali del PDF e i grafici sono stati controllati anche visivamente. Le cinque celle sono state eseguite in ordine in ambiente Python con backend grafico non interattivo, mantenendo la funzione display disponibile come in Jupyter. Le prime prove in Python semplice richiedevano questa predisposizione: la disponibilit? di display non ? stata trattata come errore degli studenti. I file originali sono invariati.

SHA256 notebook: `9d88f1df3d3ed65e041db1558f0c81ec1f09b842414509c79ce70c0c8058ad49`.

## Punteggi

| Area | Punti | Massimo |
|---|---:|---:|
| Prompt 2 e flusso logico teorico | 23 | 30 |
| Prompt 3 e scomposizione input output | 11 | 15 |
| Notebook e output computazionali | 18 | 20 |
| Prompt di tappa e regimi IA | 14 | 15 |
| Verifiche logiche e controlli numerici | 13 | 15 |
| Interpretazione finanziaria finale | 1 | 5 |
| **Totale** | **80** | **100** |

## 1 Prompt 2 e flusso logico teorico

**23/30.** Il contributo iniziale a p.9 individua dinamiche dei due fattori, discretizzazione Eulero e logaritmica, Riemann sinistra, fixing, correlazione, payoff, sconto e aggregazione. La sequenza ? specifica e pertinente.

La formulazione ?media dei valori finali del sottostante? ? per? ambigua rispetto alla media dei dodici fixing della singola traiettoria; viene corretta dall'IA. Sono integrate anche convenzione CIR e costruzione esplicita degli shock. Il flusso finale ? coerente, ma non tutte le precisazioni teoriche sono gi? presenti o motivate nella proposta autonoma. Il punteggio riconosce la buona architettura e distingue le integrazioni IA dal contributo iniziale.

## 2 Prompt 3 e scomposizione input output

**11/15.** La proposta a p.11 contiene cinque tappe sensate, richiama gli output e la diagnostica, ma concentra genericamente i controlli nell'ultima tappa e non mappa ogni tabella e grafico. L'IA distribuisce i controlli nelle tappe che producono le rispettive quantit? e separa meglio aggregazione e diagnostica.

Alle pp.13-15 lo studente rileva il riferimento non richiesto a Black-Scholes e chiede una tabella corretta. ? un intervento positivo sulla specifica: non implica che fosse stata effettivamente applicata una formula Black-Scholes, ma impedisce un'ambiguit? nella progettazione. Nella cella 3 la scomposizione finale risulta corretta. Resta parziale la distinzione sistematica dei campi input-output nella proposta iniziale.

## 3 Notebook e output computazionali

**18/20.** Le cinque celle di codice si eseguono in ordine e riproducono il prezzo salvato 255,153870, SE 1,844978 e probabilit? di esercizio sotto Q 45,938%. Le quattro tabelle e i cinque grafici sono presenti. Sono corretti modello, CIR, fixing, dividend yield e attualizzazione per replica; la visualizzazione di media empirica e valori positivi aggiunge informazione senza cambiare il problema.

Nel grafico 5 della cella 13 le bande etichettate ?Intervallo di confidenza al 95%? sono costruite come V_M finale +/- 1,96*std_V_finale/sqrt(m), mentre la curva ? la media cumulativa dei primi m valori. Non sono quindi gli IC delle rispettive stime cumulative: per quelli occorrerebbero media e deviazione dei sottocampioni correnti. ? possibile usarle come bande illustrative di scala, ma non con l'etichetta attribuita. L'IC finale tabellare resta corretto. La perdita di punti riguarda questo output, non il pricing principale.

## 4 Prompt di tappa e regimi IA

**14/15.** Il PDF di 51 pagine documenta la sequenza iniziale, cinque tappe B e otto richieste C. Lo studente controlla il rispetto della specifica (Black-Scholes, pp.13-15), affronta la riesecuzione con seed (pp.23-27), chiede media empirica istante per istante e annotazioni per interpretare il drift (pp.20-37), e conserva sia distribuzione totale sia dettaglio positivo dei valori attualizzati (pp.40-44).

La richiesta sul seed ? ricondotta dall'IA all'avanzamento del generatore dopo una riesecuzione isolata; la versione finale fissa il seed anche nella cella di simulazione. Non si interpreta la differenza visiva come prova di parametri modificati.

Il dubbio sulla media quasi rettilinea ? respinto alle pp.30-31 e la successiva richiesta di valori iniziale/finale rende la verifica pi? concreta. Gli interventi sono specifici, ma una parte consiste in preferenze grafiche: il numero elevato dei prompt non d? automaticamente pi? punti. Le validazioni ordinarie restano sintetiche; l'errata etichetta delle bande finali non ? individuata. Il commento conclusivo ? fornito interamente dallo studente, non generato al suo posto.

## 5 Verifiche logiche e controlli numerici

**13/15.** I controlli 1-7 sono presenti e coerenti; shock con correlazione -0,249577, positivit? del sottostante e diagnostica CIR corretta. La tabella al variare di M riporta SE*sqrt(M) compreso circa tra 411,23 e 421,37, coerente con il comportamento atteso. Il prezzo con N=504 ? 255,355991, differenza 0,202121 rispetto alla base. I fixing restano mensili.

? presente un confronto esplicito fra il prezzo rigenerato con seed 12345 e quello originario: coincidono. Il controllo di riproducibilit? ? dunque pi? documentato della sola impostazione del seed.

Il confronto fra griglie stampa la differenza ma non quantifica una tolleranza economica o statistica per concludere la stabilit?. Anche usando lo stesso seed, cambiando dimensione delle matrici non si ottiene automaticamente un accoppiamento coerente degli incrementi browniani fra le griglie. Il risultato ? un riscontro compatibile con la stabilit?, non una misura isolata del bias. Non si richiedono tecniche aggiuntive obbligatorie; si valuta la limitata interpretazione del controllo. Il difetto delle bande ? conteggiato nell'area output, senza una seconda decurtazione per la medesima formula.

## 6 Interpretazione finanziaria finale

**1/5.** La cella 14 coincide con il testo fornito a p.51: esprime soddisfazione per l'interazione IA e per i controlli, ma non interpreta economicamente prezzo, esercizio, averaging, sconto, misura Q o limiti del modello.

Il testo ? autonomo e questo viene riconosciuto. Non basta per? a soddisfare l'area di interpretazione finanziaria. Le osservazioni sul drift presenti nella chat sono valorizzate nel governo dell'interazione, ma non sostituiscono un commento finanziario conclusivo sviluppato nel notebook.

## Giudizio conclusivo

Consegna computazionalmente completa, con un governo attivo e documentato delle revisioni IA e una verifica esplicita della riproducibilit?. Pesano l?errata rappresentazione delle bande nel grafico di convergenza e soprattutto l?assenza di un?autentica interpretazione finanziaria finale.

**Valutazione individuale: 80/100.**
