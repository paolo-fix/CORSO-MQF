# Valutazione TakeHome Lezione 07 Ferrari

Data: 22 novembre 2026.

**Risultato: 85/100.** Valutazione individuale della coppia di file con suffisso `Ferrari`.

## Riferimenti e criterio di attribuzione

Si applicano esclusivamente `00_MasterPlan/MQF_Project_Guidelines.md` (??14.10 e 15.8-15.12), `04_Codice/Lez07/Lezione_07_Scheda_Caso_TakeHome.md` (??3-8) e `04_Codice/Lez07/Lezione_07_Scheda_Costruzione_Caso_TakeHome.md` (??7,12,15,16,18).

I massimi delle sei aree sono quelli normativi. I punti entro ciascuna area costituiscono un giudizio motivato: non sono decurtazioni automatiche stabilite dalle Guidelines. Non si applicano soglie di sufficienza, conversioni in trentesimi o un prezzo-obiettivo. La qualit? della risposta IA non ? confusa con il contributo iniziale dello studente, e un dubbio poi respinto pu? comunque documentare un utile processo critico.

## Materiali e verifica

- Notebook: [Lezione_07_Notebook_TakeHome_Ferrari.ipynb](Lezione_07_Notebook_TakeHome_Ferrari.ipynb), 14 celle, delle quali 5 di codice.
- Tracciato: [Lezione_07_Tracciato_TakeHome_Ferrari.pdf](Lezione_07_Tracciato_TakeHome_Ferrari.pdf), 29 pagine; presenti Prompt zero, Prompt 1, Prompt 2 e Prompt 3.

Sono stati esaminati contributi iniziali, risposte e revisioni pertinenti nel PDF, tutte le celle del notebook, codice e output incorporati. Le pagine centrali del PDF e i grafici sono stati controllati anche visivamente. Le cinque celle sono state eseguite in ordine in ambiente Python con backend grafico non interattivo, mantenendo la funzione display disponibile come in Jupyter. Le prime prove in Python semplice richiedevano questa predisposizione: la disponibilit? di display non ? stata trattata come errore degli studenti. I file originali sono invariati.

SHA256 notebook: `c2b32f2ddd5cc9406d9fe983fdf1e8fba8805b43d671ed38b8f0582e57998a79`.

## Punteggi

| Area | Punti | Massimo |
|---|---:|---:|
| Prompt 2 e flusso logico teorico | 25 | 30 |
| Prompt 3 e scomposizione input output | 13 | 15 |
| Notebook e output computazionali | 20 | 20 |
| Prompt di tappa e regimi IA | 12 | 15 |
| Verifiche logiche e controlli numerici | 12 | 15 |
| Interpretazione finanziaria finale | 3 | 5 |
| **Totale** | **85** | **100** |

## 1 Prompt 2 e flusso logico teorico

**25/30.** La proposta iniziale ? presente alle pp.8-9 del PDF e individua modelli dei fattori, dipendenza, discretizzazioni e relativi domini, fixing con esclusione di S0, payoff, sconto stocastico e aggregazione Monte Carlo. ? un contributo personale specifico, non una richiesta generica di soluzione.

Il flusso finale nella cella 2 ? coerente nelle formule. Parte della formalizzazione viene per? fornita dall'IA: costruzione esplicita degli shock, probabilit? di esercizio e somma di Riemann sinistra. Il contributo iniziale non sviluppa altrettanto bene il collegamento con tutti i controlli. Restano nel testo IA etichette imprecise, come ?riflessione positiva? per il CIR e ?soluzione esatta? per il passo del sottostante: le formule usate sono quelle prescritte, ma l'intero modello con tasso stocastico resta discretizzato. Si riconosce una buona impostazione autonoma senza equipararla alla completezza teorica massima.

## 2 Prompt 3 e scomposizione input output

**13/15.** Alle pp.10-11 la proposta specifica parametri, output tabellari e grafici, correlazione, positivit?, fixing, controllo della media, payoff e attualizzazione; distingue inoltre diagnostica Monte Carlo e raffinamento della griglia. ? pi? dettagliata di un elenco nominale di tappe.

La seconda tappa ? molto aggregata e l'IA la suddivide. La proposta non assegna esplicitamente il grafico dei valori attualizzati e il controllo V=D H, poi inseriti nella scomposizione finale della cella 3. Le dipendenze operative sono riconoscibili, ma input, operazione, output e controllo non sono sempre separati sistematicamente nella proposta iniziale.

## 3 Notebook e output computazionali

**20/20.** Le celle di codice 5, 7, 9, 11 e 13 si eseguono in ordine senza errori nell'ambiente di verifica predisposto per le funzioni Jupyter. Sono presenti le quattro tabelle e i cinque grafici prescritti; alcuni grafici sono riuniti in pannelli della stessa figura. Non si confonde il numero di figure incorporate con il numero di grafici richiesti.

Sono rispettati parametri, shock correlati, CIR con max solo sotto radice, drift r-q, fixing 21,42,...,252 senza S0 e sconto tramite r[:, :N] per replica. Prezzo 255,153870; SE 1,844978; IC 95% [251,537714; 258,770026]; esercizio sotto Q 45,938%. I risultati principali coincidono con quelli salvati. La vista completa e quella positiva dei valori attualizzati sono entrambe presenti. Il grafico di convergenza utilizza media e SE dei sottocampioni correnti in modo coerente.

## 4 Prompt di tappa e regimi IA

**12/15.** Il PDF di 29 pagine contiene Prompt zero, Prompt 1, proposte iniziali dei Prompt 2 e 3, cinque tappe B e una verifica C approfondita sul significato dell'intervallo di confidenza (pp.22-26). Lo studente formula il dubbio, insiste sul punto non compreso e infine dichiara ?Ho compreso, grazie? prima di procedere. La correzione della rappresentazione grafica viene recepita.

Il dubbio iniziale confonde la distribuzione dei payoff con la distribuzione dello stimatore della media; non viene trattato come una critica corretta al calcolo numerico. ? per? positivo che sia esposto e affrontato, anzich? nascosto. L'accoglimento IA riguarda soprattutto la leggibilit? del grafico: l'IC non richiedeva una correzione. La comprensione conclusiva ? dichiarata ma non riformulata autonomamente. Le validazioni ordinarie di flusso e tappe sono poco esplicite. Il commento finale ? fornito dallo studente e richiesto in Markdown: la formattazione non ? equiparata a delega del ragionamento.

## 5 Verifiche logiche e controlli numerici

**12/15.** I controlli 1-7 sono sostanzialmente coperti; correlazione empirica -0,249577, sottostante positivo e nessun tasso negativo osservato. La diagnostica richiesta per M=1000,5000,10000,50000 ? presente. Il rapporto SE(1000)/SE(50000)=7,0457 ? confrontato con sqrt(50)=7,0711.

La griglia fine N=504 mantiene i dodici fixing e produce 256,778220 contro 255,153870 della base, differenza circa 0,6366%. Tuttavia il messaggio ?Stabilit? confermata? ? stampato incondizionatamente: non esiste nel codice una soglia effettivamente verificata n? un confronto quantitativo con il SE della differenza. La differenza ? compatibile con la scala dell'errore Monte Carlo, ma il confronto tra due simulazioni con shock nuovi non isola il bias temporale. Non si richiedono obbligatoriamente shock accoppiati, non prescritti dalla Scheda: si limita il credito per la forza della conclusione dichiarata.

Il seed garantisce la riesecuzione ordinata, confermata dal valutatore, ma nella consegna non ? svolto un secondo confronto esplicito di riproducibilit?. Queste riserve giustificano il mancato massimo nell'area controlli, senza sottrazioni ulteriori fuori rubrica.

## 6 Interpretazione finanziaria finale

**3/5.** La cella 14, corrispondente al testo studentesco alle pp.28-29, collega correttamente r attorno al 2,2% e q=2,5% alla debole tendenza negativa del sottostante e alla frequenza di payoff nulli; menziona il dubbio statistico affrontato. Il riferimento a theta come livello medio ? una lettura approssimata pertinente, non una formula esatta del prezzo.

Il commento non utilizza prezzo, SE e IC per una lettura finanziaria del risultato, non sviluppa la differenza fra incertezza Monte Carlo ed errore di modello e non ricorda la natura risk-neutral e non operativa della valutazione. Strike prossimo a S0 e drift contenuto non determinano da soli la probabilit? di esercizio: contano anche media asiatica e volatilit?. Interpretazione pertinente ma incompleta.

## Giudizio conclusivo

Consegna completa e corretta nel calcolo principale, con proposte iniziali articolate e una verifica statistica affrontata esplicitamente. Per una valutazione pi? alta occorrono maggiore precisione nella validazione della griglia e un commento conclusivo che usi prezzo, incertezza e limiti del modello.

**Valutazione individuale: 85/100.**
