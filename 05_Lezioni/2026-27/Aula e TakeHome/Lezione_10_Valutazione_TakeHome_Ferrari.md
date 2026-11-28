# Verifica TakeHome Lezione 10 Ferrari in attesa di tracciato completo

Data: 27 novembre 2026.

**Valutazione complessiva non ancora attribuita.** Il PDF disponibile di 47 pagine inizia con una precisazione sulla matrice di migrazione prima della Tappa 1 e non documenta Prompt zero, Prompt 1, Prompt 2 e Prompt 3. Il notebook contiene flusso e scomposizione finali, ma questi non sostituiscono i contributi iniziali e le validazioni del tracciato.

? stata richiesta un'esportazione completa, oppure una scelta esplicita del docente di valutare soltanto il materiale documentato. Non si presume che i prompt non siano stati svolti e non si assegna un punteggio definitivo penalizzando una possibile esportazione incompleta.

## Verifiche gi? completate

Le sei celle di codice 5,7,9,11,13,15 si eseguono ordinatamente senza errori. Sono presenti i due portafogli corretti, quattro tabelle, tre figure, distribuzione di Delta L e verifica di stabilit?. Il totale ? 173 milioni per ciascuna allocazione, con fattore 173/148 sui debitori residui e scenari accoppiati.

Le medie riprodotte sono 11,189577 e 12,254726 milioni; CVaR 99% rispettivamente 37,153220 e 36,914880. La funzione CVaR restituisce la media delle statistiche d'ordine superiori: ? esatta per le numerosit? e i livelli qui impiegati, per cui alpha*N ? intero. La formula andrebbe generalizzata con massa frazionaria se fosse usata su numerosit? arbitrarie, ma questo non rende errati i risultati richiesti.

Il PDF documenta una verifica sul controllo di riproducibilit? alla p.13 e un chiarimento sulla dipendenza delle distribuzioni alla p.25. I risultati finali e il seed sono riproducibili nella riesecuzione. Il commento finale ? fornito dallo studente e richiesto in Markdown nelle ultime pagine.

## Riserve gi? osservabili

La conclusione sullo stato C come causa di una distribuzione platicurtica non ? sostenuta da un calcolo della curtosi e non segue dalla sola riduzione visiva dell'asimmetria. ? invece corretto il richiamo all'aumento delle perdite condizionato alla crisi e al cambiamento di composizione del controfattuale. Questi aspetti saranno valutati nell'area interpretazione, senza anticipare il totale.

Il recupero del tracciato iniziale servir? a valutare soprattutto le due aree Prompt 2 e Prompt 3, che insieme valgono 45 punti. Non occorre ripetere il controllo computazionale se notebook e codice rimangono invariati.
