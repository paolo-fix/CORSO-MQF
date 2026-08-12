# Scheda Costruzione Caso Applicativo

Documento interno di progettazione docente.  
**Lezione 7 — caso take-home.**

## 1. Identificazione del caso

- **Lezione:** 7 — Applicazione in Python: traiettorie, simulazione e pricing Monte Carlo
- **Tipo di caso:** take-home
- **Titolo:** *Pricing Monte Carlo di una call asiatica sull'EURO STOXX 50 con tasso di interesse stocastico*
- **Destinatari:** studenti del secondo anno della Laurea Magistrale in Banca e Risk Management
- **Uso previsto:** lavoro autonomo successivo alla lezione applicativa, sviluppato mediante notebook Jupyter e uso documentato dell'IA secondo il protocollo MQF.
- **Data di riferimento del caso:** 27 luglio 2026.

Il caso consolida operativamente:

- dinamiche moltiplicative di tipo GBM per un indice azionario;
- presenza di dividend yield nel drift risk-neutral;
- processo CIR per il tasso nominale;
- simulazione di diffusioni correlate;
- costruzione di un payoff path-dependent;
- attualizzazione scenario per scenario;
- stima e diagnostica Monte Carlo.

Il caso deve essere metodologicamente confrontabile con il caso aula sull'inflation-linked bond, senza costituirne una variazione parametrica.

---

## 2. Contesto e motivazione

### Contesto di mercato

Il sottostante scelto è l'**EURO STOXX 50**, uno dei principali benchmark azionari dell'area euro e sottostante di un mercato molto liquido di futures e opzioni vanilla presso Eurex.

La data di riferimento è il **27 luglio 2026**. In quella seduta l'indice si colloca nell'area di 6.300 punti; il valore di chiusura utilizzato come condizione iniziale è:

$$S_0=6\,286.35.$$

Il livello è storicamente elevato rispetto al range osservato nei dodici mesi precedenti, che in luglio 2026 si estendeva approssimativamente da 5.155 a 6.431 punti. Il caso è quindi collocato in una fase di mercato in cui l'indice si trova vicino alla parte alta del range annuale.

Per lo strike si sceglie:

$$K=6\,300,$$

quindi un livello sostanzialmente at-the-money. La scelta è anche coerente con la griglia degli strike delle opzioni EURO STOXX 50 quotate su Eurex: per scadenze residue tra 6 e 12 mesi gli strike standard sono distanziati di 50 punti.

Il livello iniziale del tasso viene ancorato all'**€STR** del 27 luglio 2026:

$$r_0=0.02185.$$

Il dato si colloca in un contesto monetario particolare. L'11 giugno 2026 la BCE aveva aumentato di 25 punti base i tassi ufficiali, portando il tasso sui depositi al 2,25%, a fronte delle pressioni inflazionistiche derivanti dallo shock energetico legato al conflitto in Medio Oriente. Il 23 luglio 2026 la BCE aveva poi lasciato invariati i tassi. Il valore di €STR utilizzato nel caso è quindi coerente con il nuovo livello della politica monetaria dell'estate 2026.

Per tenere conto dei dividendi dell'indice si introduce un dividend yield continuo costante:

$$q=0.025.$$

Il valore è una proxy di mercato arrotondata: un ETF fisico che replica l'EURO STOXX 50 riportava a fine luglio 2026 un trailing dividend distribution yield vicino al 2,5%.

Per la volatilità del sottostante si assume:

$$\sigma_S=0.18.$$

Il valore non è una calibrazione della volatilità implicita a un anno. È una proxy market-consistent: all'inizio di luglio 2026 i future VSTOXX sulle scadenze estive quotavano valori nell'area 17--19 punti. Il parametro 18% rende quindi il caso coerente con l'ordine di grandezza della volatilità azionaria osservabile in quel periodo, senza introdurre una calibrazione di superficie non ancora trattata nel corso.

### Chi utilizza opzioni asiatiche e perché

Le opzioni asiatiche sono contratti path-dependent il cui payoff dipende dalla media dei prezzi osservati durante un intervallo, anziché da un singolo fixing terminale.

Il loro utilizzo è particolarmente diffuso nei mercati delle commodity, dove il prezzo economico di acquisti o vendite ricorrenti è spesso una media di più fixing. Le average-price options consentono quindi di allineare meglio il payoff del derivato all'esposizione economica effettiva e, per effetto dell'averaging, tendono a essere meno sensibili a picchi isolati del prezzo.

In ambito azionario, strutture di tipo Asian compaiono soprattutto nel mercato **OTC** e nei prodotti strutturati o assicurativi equity-linked. L'averaging può essere utilizzato da:

- banche e intermediari che strutturano prodotti equity-linked;
- investitori istituzionali;
- compagnie di assicurazione;
- gestori che desiderano un payoff indicizzato a una performance media piuttosto che al solo fixing finale.

Nel caso didattico si assume che un intermediario debba valutare una **call asiatica OTC sull'EURO STOXX 50**. Non si afferma che tale contratto sia quotato su Eurex: Eurex viene utilizzata come riferimento per il mercato liquido delle opzioni vanilla sullo stesso indice e per la plausibilità dello strike.

La scelta dell'opzione asiatica consente di mostrare in modo finanziariamente realistico perché una traiettoria simulata può essere necessaria anche quando il payoff finale è unico.

---

## 3. Domanda quantitativa e obiettivo didattico

**Domanda quantitativa**

Qual è il valore corrente di una call asiatica a media aritmetica sull'EURO STOXX 50 quando il livello dell'indice e il tasso nominale evolvono congiuntamente in modo stocastico? Come si passa dalle traiettorie simulate dei fattori di rischio al prezzo medio, al payoff e quindi al prezzo Monte Carlo?

**Obiettivo didattico**

Lo studente deve costruire autonomamente la catena:

$$\text{fattori stocastici}\rightarrow\text{shock correlati}\rightarrow\text{traiettorie}\rightarrow\text{statistiche terminali}\rightarrow\text{media del sottostante}\rightarrow\text{probabilità di esercizio}\rightarrow\text{payoff}\rightarrow\text{attualizzazione}\rightarrow\text{prezzo Monte Carlo}\rightarrow\text{errore Monte Carlo}.$$

Il caso deve consolidare soprattutto quattro passaggi concettuali:

1. distinguere valore terminale del sottostante e funzionale dell'intera traiettoria;
2. comprendere che il payoff deve essere costruito scenario per scenario prima dell'aggregazione Monte Carlo;
3. utilizzare la traiettoria del tasso, e non un unico tasso terminale, per costruire il fattore di sconto;
4. distinguere parametri osservati o market-consistent da parametri modellistici assegnati a fini didattici.

---

## 4. Specifica teorico-matematica

### Grandezze e variabili

Si considerano:

- $S_t$: livello dell'EURO STOXX 50;
- $r_t$: tasso nominale istantaneo privo di rischio;
- $q$: dividend yield continuo;
- $A_T$: media aritmetica dei livelli dell'indice osservati alle date di fixing;
- $K$: strike dell'opzione;
- $H_T$: payoff dell'opzione;
- $D(0,T)$: fattore di sconto stocastico;
- $V^{(s)}$: valore attualizzato del payoff nello scenario $s$;
- $T$: scadenza;
- $t_1,\ldots,t_m=T$: date di fixing.

### Dinamica del sottostante

Le dinamiche sono assegnate direttamente ai fini della valutazione sotto la misura di pricing utilizzata nel caso.

Il sottostante segue una dinamica moltiplicativa di tipo GBM con short rate stocastico e dividend yield continuo:

$$dS_t=(r_t-q)S_t\,dt+\sigma_S S_t\,dW_t^{(S)}.$$

### Dinamica del tasso nominale

Il tasso segue un processo CIR:

$$dr_t=\kappa_r(\theta_r-r_t)\,dt+\sigma_r\sqrt{r_t}\,dW_t^{(r)}.$$

I parametri devono soddisfare:

$$\kappa_r>0,\qquad \theta_r>0,\qquad \sigma_r>0,$$

e la calibrazione didattica viene scelta in modo da soddisfare la condizione di Feller:

$$2\kappa_r\theta_r\geq\sigma_r^2.$$

### Correlazione

Gli shock browniani soddisfano:

$$dW_t^{(S)}\,dW_t^{(r)}=\rho\,dt.$$

Operativamente, a partire da due normali standard indipendenti $Z_{1,k}$ e $Z_{2,k}$:

$$Z_{S,k}=Z_{1,k},$$

$$Z_{r,k}=\rho Z_{1,k}+\sqrt{1-\rho^2}\,Z_{2,k}.$$

### Media asiatica

Si considera una call asiatica a media aritmetica con $m=12$ fixing mensili:

$$A_T=\frac{1}{m}\sum_{j=1}^{m}S_{t_j}.$$

Il valore iniziale $S_0$ non entra nella media.

### Payoff

Il payoff a scadenza è:

$$H_T=\max(A_T-K,0).$$

Per lo scenario simulato $s$:

$$H_T^{(s)}=\max(A_T^{(s)}-K,0).$$

### Fattore di sconto

Il fattore di sconto scenario-specifico è:

$$D(0,T)=\exp\left(-\int_0^T r_u\,du\right).$$

### Valore attualizzato per scenario

Per ogni traiettoria:

$$V^{(s)}=D^{(s)}(0,T)H_T^{(s)}.$$

### Stima Monte Carlo

Con $M$ simulazioni:

$$\widehat V_M=\frac{1}{M}\sum_{s=1}^{M}V^{(s)}.$$

L'errore standard Monte Carlo è:

$$SE(\widehat V_M)=\frac{s_V}{\sqrt{M}},$$

dove $s_V$ è la deviazione standard campionaria dei valori attualizzati.

### Parametri e dati

**Contratto e mercato**

- data di riferimento: 27 luglio 2026;
- sottostante: EURO STOXX 50;
- $S_0=6\,286.35$;
- $K=6\,300$;
- $T=1$ anno;
- fixing mensili: $m=12$;
- $q=0.025$;
- $\sigma_S=0.18$.

**Tasso CIR**

- $r_0=0.02185$;
- $\kappa_r=1.25$;
- $\theta_r=0.0220$;
- $\sigma_r=0.040$.

La condizione di Feller è soddisfatta:

$$2(1.25)(0.0220)=0.055>0.0016=(0.040)^2.$$

**Dipendenza**

- $\rho=-0.25$.

La correlazione è un parametro modellistico didattico: non viene presentata come stima empirica o calibrazione di mercato.

**Simulazione**

- orizzonte: 1 anno;
- griglia principale: giornaliera, $\Delta t=1/252$;
- fixing mensili ai passi $21,42,\ldots,252$;
- $M=50\,000$ traiettorie;
- seed: 12345.

### Natura dei parametri

La scheda docente deve distinguere:

- **dato osservato:** $S_0$, $r_0$;
- **proxy di mercato arrotondata:** $q$, $\sigma_S$;
- **scelta contrattuale coerente con il mercato:** $K$, $T$, calendario dei fixing;
- **parametri modellistici didattici:** $\kappa_r$, $\theta_r$, $\sigma_r$, $\rho$;
- **parametri computazionali:** $\Delta t$, $M$, seed.

### Convenzione numerica

Per il CIR deve essere utilizzata la stessa convenzione numerica discussa e validata nel caso aula.

Il take-home non deve introdurre autonomamente una diversa tecnica di simulazione del CIR. Eventuali correzioni della discretizzazione devono essere esplicitate e motivate.

Per il sottostante è opportuno utilizzare una discretizzazione logaritmica coerente con la struttura moltiplicativa:

$$S_{t+\Delta t}=S_t\exp\left[\left(r_t-q-\frac{1}{2}\sigma_S^2\right)\Delta t+\sigma_S\sqrt{\Delta t}\,Z_S\right].$$

### Ipotesi

1. le dinamiche assegnate sono utilizzate direttamente ai fini del pricing;
2. i parametri del CIR e la correlazione non sono calibrati;
3. il dividend yield è costante;
4. la volatilità azionaria è costante;
5. non sono considerati rischio di credito, liquidità o costi di transazione;
6. i fixing sono equidistanti e mensili;
7. strike e calendario sono assegnati;
8. indice e tasso sono simulati sulla stessa griglia;
9. la stessa convenzione numerica per il CIR adottata nel caso aula deve essere mantenuta;
10. il caso non richiede formule chiuse di pricing.

### Quantità finali di interesse — ordine operativo

1. media e deviazione standard simulate di $S_T$ e $r_T$;
2. media e deviazione standard simulate del prezzo medio $A_T$;
3. probabilità simulata di esercizio, $\widehat{\mathbb P}(A_T>K)$;
4. valore medio del payoff non attualizzato $H_T$;
5. prezzo Monte Carlo della call asiatica $\widehat V_M$;
6. errore standard Monte Carlo e intervallo di confidenza al 95% del prezzo.

---

## 5. Output richiesti

### Stime o risultati numerici

Gli output numerici devono seguire l'ordine operativo del caso:

1. media e deviazione standard di $S_T$ e $r_T$;
2. media e deviazione standard di $A_T$;
3. $\widehat{\mathbb P}(A_T>K)$;
4. valore medio di $H_T$;
5. $\widehat V_M$;
6. errore standard Monte Carlo e intervallo di confidenza al 95%.

### Tabelle

**Tabella 1 — parametri del modello e natura del dato**

Contratto, dati di mercato, proxy, CIR, correlazione e simulazione.

**Tabella 2 — statistiche dei fattori e della media asiatica**

- media e deviazione standard di $S_T$;
- media e deviazione standard di $r_T$;
- media e deviazione standard di $A_T$.

**Tabella 3 — payoff e pricing**

- probabilità di esercizio;
- payoff medio;
- prezzo Monte Carlo;
- errore standard;
- intervallo di confidenza.

**Tabella 4 — diagnostica Monte Carlo**

Per $M=1\,000,\ 5\,000,\ 10\,000,\ 50\,000$, riportare prezzo ed errore standard.

**Tabella 5 — controllo della correlazione**

Confrontare $\rho$ teorico e correlazione empirica degli shock.

### Grafici

1. alcune traiettorie simulate di $S_t$;
2. alcune traiettorie simulate di $r_t$;
3. distribuzione di $A_T$ con evidenza dello strike $K$;
4. distribuzione dei payoff attualizzati $V^{(s)}$;
5. convergenza della stima Monte Carlo al crescere di $M$.

### Controlli

1. correlazione empirica degli shock prossima a $\rho$;
2. positività di $S_t$;
3. monitoraggio di eventuali valori negativi di $r_t$ prodotti dalla discretizzazione;
4. per ciascuna traiettoria, $\min_jS_{t_j}\leq A_T\leq\max_jS_{t_j}$;
5. $H_T\geq0$;
6. $D(0,T)>0$;
7. payoff nullo quando $A_T\leq K$;
8. errore standard decrescente approssimativamente come $1/\sqrt M$;
9. stabilità del prezzo rispetto alla griglia temporale;
10. replicabilità con seed fissato.

---

## 6. Flusso logico-teorico risolutivo atteso

| Passo | Finalità risolutiva | Formula, definizione, proprietà o teorema | Applicazione nel caso | Output o controllo collegato |
|---:|---|---|---|---|
| 1 | Identificare i fattori di rischio | GBM con dividendi e CIR | specificare $S_t$ e $r_t$ | parametri e condizioni iniziali |
| 2 | Costruire la dipendenza | correlazione tra Browniani | generare shock correlati | correlazione empirica |
| 3 | Generare le traiettorie | discretizzazione delle SDE | simulare $S_t$ e $r_t$ | traiettorie e statistiche terminali |
| 4 | Verificare i fattori simulati | momenti empirici | analizzare $S_T$ e $r_T$ | media e deviazione standard |
| 5 | Identificare le osservazioni contrattuali | date di fixing | selezionare $S_{t_j}$ | controllo calendario |
| 6 | Costruire la variabile path-dependent | media aritmetica | calcolare $A_T$ | media, deviazione standard e distribuzione |
| 7 | Identificare l'esercizio | $A_T>K$ | stimare frequenza di esercizio | probabilità di esercizio |
| 8 | Costruire il payoff | $(A_T-K)^+$ | calcolare $H_T$ | payoff medio |
| 9 | Costruire l'attualizzazione | $\exp(-\int r_tdt)$ | calcolare $D(0,T)$ | controllo discount factor |
| 10 | Valutare ogni scenario | $D(0,T)H_T$ | calcolare $V^{(s)}$ | distribuzione dei valori |
| 11 | Aggregare Monte Carlo | media e SE | stimare il prezzo | prezzo, SE e IC |
| 12 | Validare | convergenza e discretizzazione | variare $M$ e $\Delta t$ | diagnostica |
| 13 | Interpretare | path-dependence e dipendenza tra fattori | collegare traiettorie, payoff e prezzo | conclusione finanziaria |

---

## 7. Scomposizione attesa in tappe

| Tappa | Regime | Input | Operazione | Output | Controllo | Uso successivo |
|---:|:---:|---|---|---|---|---|
| 1 | A | Scheda Caso | ricostruire modello e struttura del payoff | mappa teorica | nessuna modifica alla specifica | base risolutiva |
| 2 | B | parametri, griglia, seed | predisporre ambiente numerico | parametri e calendario | coerenza temporale | simulazione |
| 3 | B | $\rho$, normali indipendenti | generare shock correlati | shock $Z_S,Z_r$ | correlazione empirica | processi |
| 4 | B | shock e parametri | simulare $S_t$ e $r_t$ | traiettorie | positività e controllo CIR | statistiche terminali |
| 5 | B | traiettorie | calcolare statistiche di $S_T$ e $r_T$ | media e deviazione standard | coerenza numerica | fixing |
| 6 | B | traiettorie $S_t$ | estrarre fixing e calcolare media | $A_T$ e statistiche | min/max della traiettoria | esercizio |
| 7 | B | $A_T,K$ | stimare esercizio e payoff | probabilità, $H_T$ | non negatività | pricing |
| 8 | B | traiettorie $r_t$ | costruire fattore di sconto | $D(0,T)$ | positività | pricing |
| 9 | B | payoff e discount factor | attualizzare e aggregare | $V^{(s)},\widehat V_M,SE$ | coerenza dimensionale | validazione |
| 10 | C | risultati | verificare convergenza e griglia | tabelle diagnostiche | stabilità | interpretazione |
| 11 | C | output validati | interpretare risultati | commento finale | coerenza finanziaria | consegna |

---

## 8. Mappa tra prompt e notebook

| Prompt | Regime | Tappa | Celle o output prodotti | Decisione o controllo richiesto |
|---|:---:|:---:|---|---|
| Prompt zero | — | — | inizializzazione della chat | rispetto del protocollo |
| Prompt 1 | — | — | cella Markdown iniziale | fedeltà alla Scheda Caso |
| Prompt 2 | A | 1 | Flusso logico-teorico | valutazione della proposta iniziale dello studente |
| Prompt 3 | — | 1–11 | scomposizione input-output | coerenza tra tappe |
| prompt di tappa | B | 2–9 | Markdown, codice e output | controlli intermedi |
| prompt di verifica | C | 10–11 | diagnostica e interpretazione | validazione critica |

La sequenza concreta dei prompt dovrà essere calibrata dopo la validazione del notebook docente.

---

## 9. Struttura attesa del notebook

1. titolo, data di riferimento e inquadramento del caso;
2. breve contesto dell'EURO STOXX 50 e natura dell'opzione asiatica;
3. specificazione del contratto;
4. specificazione delle dinamiche di $S_t$ e $r_t$;
5. parametri, natura dei dati e griglia temporale;
6. calendario dei fixing;
7. generazione degli shock correlati;
8. simulazione delle traiettorie;
9. controlli preliminari sui processi;
10. statistiche terminali di $S_T$ e $r_T$;
11. estrazione dei fixing;
12. costruzione e statistiche di $A_T$;
13. probabilità di esercizio;
14. costruzione e media del payoff;
15. costruzione del fattore di sconto;
16. valore attualizzato scenario per scenario;
17. pricing Monte Carlo;
18. errore standard e intervallo di confidenza;
19. diagnostica della convergenza;
20. controllo della discretizzazione;
21. interpretazione finanziaria finale.

---

## 10. Calibrazione docente

### Benchmark preliminare

La calibrazione definitiva deve essere validata mediante notebook docente dopo l'adozione della convenzione numerica CIR del caso aula.

Con i parametri proposti ci si attende:

- un contratto prossimo all'at-the-money all'origine;
- una probabilità di esercizio non estrema;
- una distribuzione di $A_T$ sufficientemente dispersa attorno allo strike;
- tassi concentrati attorno a valori prossimi al 2%;
- un effetto della correlazione sul pricing visibile ma secondario rispetto alla volatilità azionaria;
- un errore Monte Carlo chiaramente decrescente al crescere di $M$.

Il benchmark numerico definitivo non deve essere comunicato preventivamente agli studenti.

### Errori o ambiguità prevedibili

1. utilizzare $S_T$ al posto di $A_T$;
2. includere $S_0$ nella media senza che sia una data di fixing;
3. mediare tutti i punti della griglia anziché i soli fixing;
4. confondere media aritmetica e geometrica;
5. dimenticare il dividend yield $q$ nel drift;
6. trattare $q=2,5\%$ come dato esatto dell'indice anziché come proxy;
7. costruire il payoff sulla media delle traiettorie anziché scenario per scenario;
8. calcolare prima il payoff medio e poi applicare il massimo;
9. attualizzare con $r_T$;
10. utilizzare un tasso medio comune a tutte le traiettorie;
11. dimenticare la correlazione;
12. trattare $\rho=-0.25$ come correlazione empiricamente calibrata;
13. imporre implicitamente correlazione perfetta usando lo stesso shock;
14. trattare eventuali valori CIR negativi da discretizzazione come proprietà del modello;
15. trascurare l'errore Monte Carlo;
16. presentare il contratto Asian come opzione quotata su Eurex;
17. presentare la simulazione come una formula esatta di pricing.

### Limiti interpretativi

Il caso non rappresenta un modello completo di mercato:

- volatilità azionaria costante;
- dividend yield costante;
- short rate a un fattore;
- correlazione costante;
- parametri CIR non calibrati;
- nessuna superficie di volatilità;
- contratto Asian OTC stilizzato;
- nessun rischio di credito o liquidità.

L'obiettivo è il consolidamento della simulazione e del pricing path-dependent.

---

## 11. Uso dell'IA e tracciato

### Prompt obbligatori

- Prompt zero;
- Prompt 1;
- Prompt 2;
- Prompt 3;
- prompt di tappa;
- almeno un momento esplicito di verifica critica in Regime C.

### Usi ammessi dell'IA

- chiarimento teorico del problema;
- verifica della differenza tra $S_T$ e $A_T$;
- chiarimento della funzione del dividend yield;
- costruzione controllata di singole tappe Python;
- verifica del calendario dei fixing;
- controllo della correlazione;
- diagnostica degli output;
- revisione di codice già prodotto;
- supporto all'interpretazione finale.

### Usi non ammessi

- produrre il notebook completo in un unico passaggio;
- sostituire autonomamente il modello;
- cambiare strike, parametri, calendario o payoff;
- trasformare l'opzione asiatica in una call europea;
- eliminare il dividend yield;
- modificare il metodo CIR senza motivazione;
- introdurre formule chiuse o modelli non previsti;
- eliminare output o controlli richiesti.

---

## 12. Valutazione

### Criteri per il notebook

- correttezza della simulazione congiunta;
- corretta inclusione del dividend yield;
- corretta costruzione delle date di fixing;
- corretta definizione di $A_T$;
- corretta costruzione del payoff;
- corretta attualizzazione scenario per scenario;
- pricing Monte Carlo;
- misura dell'errore di simulazione;
- qualità dei controlli;
- leggibilità del notebook;
- interpretazione finanziaria;
- corretta distinzione tra dati osservati, proxy e parametri didattici.

### Criteri per il tracciato IA

- qualità del contributo iniziale dello studente;
- corretta identificazione della path-dependence;
- capacità di scomporre il problema;
- uso appropriato dei regimi A, B e C;
- capacità di verificare il codice suggerito;
- presenza di controlli autonomi;
- capacità di correggere eventuali errori dell'IA;
- coerenza tra chat e notebook consegnato.

Il risultato numerico del prezzo non deve essere sufficiente per una valutazione elevata.

---

## 13. Relazione con l'altro caso della lezione

La coppia condivide la stessa architettura generale:

$$\text{due fattori stocastici}\rightarrow\text{shock correlati}\rightarrow\text{traiettorie}\rightarrow\text{funzionale della traiettoria}\rightarrow\text{cash flow/payoff}\rightarrow\text{attualizzazione}\rightarrow\text{Monte Carlo}.$$

### Caso aula

- inflazione: OU;
- tasso nominale: CIR;
- funzionale della traiettoria: inflazione cumulata;
- prodotto: inflation-linked bond;
- output finanziari: cedole indicizzate e capitale protetto.

### Caso take-home

- sottostante: EURO STOXX 50;
- dinamica: GBM con dividend yield;
- tasso nominale: CIR;
- funzionale della traiettoria: media aritmetica dei fixing;
- prodotto: call asiatica OTC;
- output finanziario: payoff opzionale path-dependent.

La struttura computazionale comune rende trasferibili metodo e controlli, ma non la soluzione.

---

### Fonti di calibrazione e contesto per il docente

- Eurex, specifiche delle EURO STOXX 50 Index Options (OESX): sottostante, mercato delle opzioni vanilla e griglia degli strike.
- BCE, €STR con data di riferimento 27 luglio 2026 e decisioni di politica monetaria dell'11 giugno e del 23 luglio 2026.
- iShares / BlackRock, ETF EURO STOXX 50: trailing dividend distribution yield di fine luglio 2026, utilizzato come proxy del dividend yield.
- Eurex, VSTOXX futures: livelli delle scadenze estive 2026 utilizzati come riferimento per l'ordine di grandezza della volatilità.
- CME Group, materiale sulle Average Price Options: utilizzo delle opzioni asiatiche per esposizioni basate su prezzi medi.
- Letteratura su equity-linked securities e Asian-style options: utilizzo dell'averaging in prodotti strutturati e assicurativi.
