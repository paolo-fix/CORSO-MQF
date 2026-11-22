# Sintesi delle valutazioni TakeHome Lezione 07

Data: 22 novembre 2026. Tre valutazioni individuali, ciascuna riferita esclusivamente alla propria coppia notebook e tracciato IA. Riferimenti: Guidelines, Scheda Caso e Scheda Costruzione Caso TakeHome Lez07.

| Area | Massimo | Ferrari | Ghislandi | Zani |
|---|---:|---:|---:|---:|
| Prompt 2 e flusso logico teorico | 30 | 25 | 23 | 22 |
| Prompt 3 e scomposizione input output | 15 | 13 | 11 | 9 |
| Notebook e output computazionali | 20 | 20 | 18 | 15 |
| Prompt di tappa e regimi IA | 15 | 12 | 14 | 11 |
| Verifiche logiche e controlli numerici | 15 | 12 | 13 | 8 |
| Interpretazione finanziaria finale | 5 | 3 | 1 | 3 |
| **Totale** | **100** | **85** | **80** | **68** |

I punteggi interni alle aree sono giudizi motivati, non una formula automatica di decurtazione. Non si introduce una conversione in trentesimi n? una soglia di sufficienza.

## Risultati e differenze rilevanti

Tutti e tre i codici eseguiti ordinatamente producono prezzo 255,153870, SE 1,844978 e probabilit? di esercizio sotto Q 45,938%. Non si impone questa stima come prezzo-obiettivo: la coincidenza discende dalla stessa implementazione numerica e dallo stesso seed.

- **Ferrari 85/100:** quattro tabelle e cinque grafici richiesti presenti; contributi iniziali articolati e confronto esplicito sul significato dell'IC. Il messaggio di stabilit? della griglia ? per? incondizionato e l'interpretazione finale ? breve.
- **Ghislandi 80/100:** pacchetto completo, revisioni critiche su specifica e seed, riproducibilit? esplicitamente verificata. Le bande del grafico cumulativo sono centrate sul prezzo finale, non sulle medie cumulative cui sono attribuite, e il commento conclusivo ? quasi soltanto una valutazione dell'interazione IA.
- **Zani 68/100:** codice principale corretto, ma mancano Tabella 4, Grafico 5 e controlli 8-9; il prezzo salvato 260,1725 differisce da quello riprodotto 255,153870. Non si attribuisce una causa non provata alla discrepanza. Il PDF comprende i prompt iniziali e termina dopo pricing e commento, senza l'esecuzione della Tappa 6 prevista nella mappa.

Per Ferrari la griglia fine produce 256,778220 (differenza 1,624350); per Ghislandi 255,355991 (differenza 0,202121). I due confronti usano generazioni casuali diverse: n? la maggiore n? la minore differenza isolano da sole il bias temporale. ? valutata la qualit? del controllo, non la vicinanza a un risultato numerico prestabilito.

## Resoconti individuali

- [Ferrari: 85/100](Lezione_07_Valutazione_TakeHome_Ferrari.md).
- [Ghislandi: 80/100](Lezione_07_Valutazione_TakeHome_Ghislandi.md).
- [Zani: 68/100](Lezione_07_Valutazione_TakeHome_Zani.md).
