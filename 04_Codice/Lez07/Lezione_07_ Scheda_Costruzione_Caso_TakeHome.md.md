# Scheda Costruzione Caso Applicativo

Documento interno di progettazione docente.  
**Lezione 7 — caso take-home.**

## 1. Identificazione del caso

- **Lezione:** 7 — Applicazione in Python: traiettorie, simulazione e pricing Monte Carlo
- **Tipo di caso:** take-home
- **Titolo:** *Path-dependence e tassi stocastici: pricing Monte Carlo di un'opzione asiatica*
- **Destinatari:** studenti del secondo anno della Laurea Magistrale in Banca e Risk Management
- **Uso previsto:** lavoro autonomo successivo alla lezione applicativa, sviluppato mediante notebook Jupyter e uso documentato dell'IA secondo il protocollo MQF.

Il caso consolida operativamente:

- dinamiche moltiplicative di tipo GBM per prezzi azionari;
- processo CIR per il tasso nominale;
- simulazione di diffusioni correlate;
- costruzione di un payoff path-dependent;
- attualizzazione scenario per scenario;
- stima e diagnostica Monte Carlo.

Il caso deve essere metodologicamente confrontabile con il caso aula sull'inflation-linked bond, senza costituirne una variazione parametrica.

---

## 2. Contesto e motivazione

Un intermediario finanziario deve valutare una call asiatica a media aritmetica scritta su un titolo azionario.

A differenza di una call europea ordinaria, il payoff non dipende soltanto dal prezzo terminale del sottostante, ma dalla media dei prezzi osservati a un insieme prefissato di date. Il valore del contratto dipende quindi dall'intera traiettoria rilevante del prezzo azionario.

Si introduce inoltre un tasso nominale privo di rischio stocastico. Il problema richiede pertanto la simulazione congiunta di:

1. prezzo del sottostante;
2. short rate;
3. eventuale dipendenza tra i rispettivi shock.

La simulazione assume una funzione finanziaria diversa rispetto al caso aula:

- nel bond inflation-linked la traiettoria dell'inflazione genera il coefficiente di indicizzazione dei cash flow;
- nell'opzione asiatica la traiettoria del prezzo azionario entra direttamente nella costruzione del payoff.

In entrambi i casi, invece, la traiettoria del tasso determina il fattore di attualizzazione.

Il caso è costruito per rendere osservabile il concetto di **path-dependence** e per mostrare che il pricing Monte Carlo richiede una trasformazione coerente delle traiettorie simulate in una variabile finanziaria finale.

---

## 3. Domanda quantitativa e obiettivo didattico

**Domanda quantitativa**

Qual è il valore corrente di una call asiatica a media aritmetica quando il prezzo del sottostante e il tasso nominale evolvono congiuntamente in modo stocastico? Come si passa dalle traiettorie simulate dei fattori di rischio al payoff e quindi al prezzo Monte Carlo?

**Obiettivo didattico**

Lo studente deve costruire autonomamente la catena:

$$\text{fattori stocastici}\rightarrow\text{shock correlati}\rightarrow\text{traiettorie}\rightarrow\text{media del sottostante}\rightarrow\text{payoff}\rightarrow\text{attualizzazione}\rightarrow\text{prezzo Monte Carlo}\rightarrow\text{controlli}.$$

Il caso deve consolidare soprattutto tre passaggi concettuali:

1. distinguere valore terminale del sottostante e funzionale dell'intera traiettoria;
2. comprendere che il payoff deve essere costruito scenario per scenario prima dell'aggregazione Monte Carlo;
3. utilizzare la traiettoria del tasso, e non un unico tasso terminale, per costruire il fattore di sconto.

---

## 4. Specifica teorico-matematica

### Grandezze e variabili

Si considerano:

- $S_t$: prezzo del sottostante azionario;
- $r_t$: tasso nominale istantaneo privo di rischio;
- $A_T$: media aritmetica dei prezzi osservati alle date di fixing;
- $K$: strike dell'opzione;
- $H_T$: payoff dell'opzione;
- $D(0,T)$: fattore di sconto stocastico;
- $V^{(s)}$: valore attualizzato del payoff nello scenario $s$;
- $T$: scadenza;
- $t_1,\ldots,t_m=T$: date di fixing.

### Dinamica del sottostante

Le dinamiche sono assegnate direttamente ai fini della valutazione sotto la misura di pricing utilizzata nel caso.

Il sottostante segue una dinamica moltiplicativa di tipo GBM con short rate stocastico:

$$dS_t=r_tS_t\,dt+\sigma_S S_t\,dW_t^{(S)}.$$

Non vengono considerati dividendi.

La scelta mantiene la struttura moltiplicativa introdotta per il GBM nel Capitolo 6, mentre il drift incorpora il tasso privo di rischio simulato.

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

Si considera una call asiatica a media aritmetica con $m$ fixing:

$$A_T=\frac{1}{m}\sum_{j=1}^{m}S_{t_j}.$$

La media deve essere costruita utilizzando esclusivamente i prezzi osservati alle date contrattuali di fixing.

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

### Parametri e dati — calibrazione didattica proposta

**Contratto**

- $S_0=100$;
- $K=100$;
- $T=1$ anno;
- fixing mensili: $m=12$;
- nessun dividendo.

**Sottostante**

- $\sigma_S=0.20$.

**Tasso CIR**

- $r_0=0.030$;
- $\kappa_r=1.50$;
- $\theta_r=0.030$;
- $\sigma_r=0.10$.

La condizione di Feller è soddisfatta:

$$2(1.50)(0.030)=0.09>0.01=(0.10)^2.$$

**Dipendenza**

- $\rho=-0.30$.

**Simulazione**

- orizzonte: 1 anno;
- griglia principale: giornaliera, $\Delta t=1/252$;
- fixing mensili estratti dalla griglia;
- $M=50\,000$ traiettorie;
- seed: 12345.

### Convenzione numerica

Per il CIR deve essere utilizzata la stessa convenzione numerica discussa e validata nel caso aula.

Il take-home non deve introdurre autonomamente una diversa tecnica di simulazione del CIR. Eventuali correzioni della discretizzazione devono essere esplicitate e motivate.

Per il sottostante è opportuno utilizzare una discretizzazione logaritmica coerente con la struttura moltiplicativa del processo:

$$S_{t+\Delta t}=S_t\exp\left[\left(r_t-\frac{1}{2}\sigma_S^2\right)\Delta t+\sigma_S\sqrt{\Delta t}\,Z_S\right].$$

### Ipotesi

1. le dinamiche assegnate sono utilizzate direttamente ai fini del pricing;
2. i parametri sono costanti;
3. non si richiedono stima o calibrazione;
4. non sono considerati dividendi;
5. non sono considerati rischio di credito, liquidità o costi di transazione;
6. i fixing sono equidistanti e mensili;
7. strike e calendario sono assegnati;
8. prezzo azionario e tasso sono simulati sulla stessa griglia;
9. la stessa convenzione numerica per il CIR adottata nel caso aula deve essere mantenuta;
10. il caso non richiede formule chiuse di pricing.

### Quantità finali di interesse

- prezzo Monte Carlo della call asiatica;
- errore standard e intervallo di confidenza;
- media e deviazione standard di $A_T$;
- probabilità simulata di esercizio $\mathbb P(A_T>K)$;
- valore medio del payoff non attualizzato;
- distribuzione dei payoff attualizzati;
- statistiche terminali di $S_T$ e $r_T$;
- effetto della dipendenza tra sottostante e tasso sul pricing.

---

## 5. Output richiesti

### Stime o risultati numerici

1. $\widehat V_M$;
2. errore standard Monte Carlo;
3. intervallo di confidenza Monte Carlo al 95%;
4. $\widehat{\mathbb P}(A_T>K)$;
5. media e deviazione standard di $A_T$;
6. valore medio di $H_T$;
7. media e deviazione standard di $S_T$ e $r_T$.

### Tabelle

**Tabella 1 — parametri del modello**

Contratto, sottostante, CIR, correlazione e simulazione.

**Tabella 2 — risultati di pricing**

- prezzo;
- errore standard;
- intervallo di confidenza;
- probabilità di esercizio;
- payoff medio.

**Tabella 3 — diagnostica Monte Carlo**

Per:

$$M=1\,000,\ 5\,000,\ 10\,000,\ 50\,000,$$

riportare prezzo ed errore standard.

**Tabella 4 — controllo della correlazione**

Confrontare $\rho$ teorico e correlazione empirica degli shock.

### Grafici

1. alcune traiettorie simulate di $S_t$;
2. alcune traiettorie simulate di $r_t$;
3. distribuzione di $A_T$ con evidenza dello strike $K$;
4. distribuzione dei payoff attualizzati $V^{(s)}$;
5. convergenza della stima Monte Carlo al crescere di $M$.

Come nel caso aula, i grafici devono avere funzione interpretativa.

### Controlli

1. correlazione empirica degli shock prossima a $\rho$;
2. positività di $S_t$;
3. monitoraggio di eventuali valori negativi di $r_t$ prodotti dalla discretizzazione;
4. per ciascuna traiettoria:
   $$\min_jS_{t_j}\leq A_T\leq\max_jS_{t_j};$$
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
| 1 | Identificare i fattori di rischio | dinamica moltiplicativa e CIR | specificare $S_t$ e $r_t$ | parametri e condizioni iniziali |
| 2 | Costruire la dipendenza | correlazione tra Browniani | generare shock correlati | correlazione empirica |
| 3 | Generare le traiettorie | discretizzazione delle SDE | simulare $S_t$ e $r_t$ | grafici e statistiche |
| 4 | Identificare le osservazioni contrattuali | date di fixing | selezionare $S_{t_j}$ | controllo calendario |
| 5 | Costruire la variabile path-dependent | media aritmetica | calcolare $A_T$ | distribuzione di $A_T$ |
| 6 | Trasformare la media in payoff | $(A_T-K)^+$ | calcolare $H_T$ | probabilità di esercizio |
| 7 | Costruire l'attualizzazione | $\exp(-\int r_tdt)$ | calcolare $D(0,T)$ | controllo discount factor |
| 8 | Valutare ogni scenario | $D(0,T)H_T$ | calcolare $V^{(s)}$ | distribuzione dei valori |
| 9 | Aggregare Monte Carlo | media e SE | stimare il prezzo | prezzo e IC |
| 10 | Validare | convergenza e discretizzazione | variare $M$ e $\Delta t$ | diagnostica |
| 11 | Interpretare | path-dependence e dipendenza tra fattori | collegare traiettorie, payoff e prezzo | conclusione finanziaria |

---

## 7. Scomposizione attesa in tappe

| Tappa | Regime | Input | Operazione | Output | Controllo | Uso successivo |
|---:|:---:|---|---|---|---|---|
| 1 | A | Scheda Caso | ricostruire modello e struttura del payoff | mappa teorica | nessuna modifica alla specifica | base risolutiva |
| 2 | B | parametri, griglia, seed | predisporre ambiente numerico | parametri e calendario | coerenza temporale | simulazione |
| 3 | B | $\rho$, normali indipendenti | generare shock correlati | shock $Z_S,Z_r$ | correlazione empirica | processi |
| 4 | B | shock e parametri | simulare $S_t$ e $r_t$ | traiettorie | positività e CIR | fixing |
| 5 | B | traiettorie $S_t$ | estrarre fixing e calcolare media | $A_T$ | min/max della traiettoria | payoff |
| 6 | B | $A_T,K$ | costruire payoff | $H_T$ | non negatività | pricing |
| 7 | B | traiettorie $r_t$ | costruire fattore di sconto | $D(0,T)$ | positività | pricing |
| 8 | B | payoff e discount factor | attualizzare e aggregare | $V^{(s)},\widehat V_M,SE$ | coerenza dimensionale | validazione |
| 9 | C | risultati | verificare convergenza e griglia | tabelle diagnostiche | stabilità | interpretazione |
| 10 | C | output validati | interpretare risultati | commento finale | coerenza finanziaria | consegna |

---

## 8. Mappa tra prompt e notebook

| Prompt | Regime | Tappa | Celle o output prodotti | Decisione o controllo richiesto |
|---|:---:|:---:|---|---|
| Prompt zero | — | — | inizializzazione della chat | rispetto del protocollo |
| Prompt 1 | — | — | cella Markdown iniziale | fedeltà alla Scheda Caso |
| Prompt 2 | A | 1 | Flusso logico-teorico | valutazione della proposta iniziale dello studente |
| Prompt 3 | — | 1–10 | scomposizione input-output | coerenza tra tappe |
| prompt di tappa | B | 2–8 | Markdown, codice e output | controlli intermedi |
| prompt di verifica | C | 9–10 | diagnostica e interpretazione | validazione critica |

La sequenza concreta dei prompt dovrà essere calibrata dopo la validazione del notebook docente.

---

## 9. Struttura attesa del notebook

1. titolo e inquadramento del caso;
2. specificazione del contratto;
3. specificazione delle dinamiche di $S_t$ e $r_t$;
4. parametri e griglia temporale;
5. calendario dei fixing;
6. generazione degli shock correlati;
7. simulazione delle traiettorie;
8. controlli preliminari sui processi;
9. estrazione dei fixing;
10. costruzione di $A_T$;
11. costruzione del payoff;
12. costruzione del fattore di sconto;
13. valore attualizzato scenario per scenario;
14. pricing Monte Carlo;
15. errore standard e intervallo di confidenza;
16. diagnostica della convergenza;
17. controllo della discretizzazione;
18. interpretazione finanziaria finale.

Il notebook deve evidenziare con chiarezza la separazione tra:

- simulazione dei fattori;
- costruzione del payoff;
- attualizzazione;
- aggregazione Monte Carlo;
- validazione.

---

## 10. Calibrazione docente

### Ordine di grandezza atteso

Con la calibrazione proposta, la simulazione docente preliminare produce un prezzo nell'intorno di **5,6** per unità di contratto, con probabilità di esercizio prossima al **52%**.

Questi valori hanno esclusivamente funzione di benchmark interno e devono essere ricalcolati con la convenzione numerica definitiva utilizzata per il CIR.

Il benchmark non deve essere comunicato preventivamente agli studenti.

### Comportamenti attesi

La calibrazione deve produrre:

- una quota significativa sia di payoff nulli sia di payoff positivi;
- una distribuzione di $A_T$ sufficientemente dispersa attorno allo strike;
- tassi concentrati attorno al livello di lungo periodo;
- un effetto della correlazione sul prezzo osservabile ma non dominante;
- errore Monte Carlo chiaramente decrescente al crescere di $M$.

### Errori o ambiguità prevedibili

1. utilizzare $S_T$ al posto di $A_T$;
2. includere $S_0$ nella media senza che sia una data di fixing;
3. mediare tutti i punti della griglia anziché i soli fixing;
4. confondere media aritmetica e geometrica;
5. costruire il payoff sulla media delle traiettorie anziché scenario per scenario;
6. calcolare prima il payoff medio e poi applicare il massimo;
7. attualizzare con $r_T$;
8. utilizzare un tasso medio comune a tutte le traiettorie;
9. dimenticare la correlazione;
10. imporre implicitamente correlazione perfetta usando lo stesso shock;
11. trattare eventuali valori CIR negativi da discretizzazione come proprietà del modello;
12. modificare arbitrariamente la convenzione CIR adottata in aula;
13. trascurare l'errore Monte Carlo;
14. presentare la simulazione come una formula esatta di pricing.

### Controlli minimi di validazione

- calendario dei fixing;
- correlazione degli shock;
- positività di $S_t$;
- gestione coerente del CIR;
- relazione min--media--max per $A_T$;
- non negatività del payoff;
- coerenza payoff/esercizio;
- convergenza Monte Carlo;
- sensibilità alla griglia;
- replicabilità.

### Limiti interpretativi

Il caso non rappresenta un modello completo di mercato:

- volatilità azionaria costante;
- short rate a un fattore;
- correlazione costante;
- assenza di dividendi;
- parametri non calibrati;
- nessuna superficie di volatilità;
- nessun rischio di credito o liquidità;
- calendario di fixing semplificato.

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

### Numero di prompt

Da calibrare dopo la costruzione definitiva del notebook. Il numero deve essere sufficiente a rendere osservabile il processo di ragionamento, senza frammentare artificialmente il lavoro.

### Usi ammessi dell'IA

- chiarimento teorico del problema;
- verifica della differenza tra $S_T$ e $A_T$;
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
- modificare il metodo CIR senza motivazione;
- introdurre formule chiuse o modelli non previsti;
- eliminare output o controlli richiesti.

---

## 12. Valutazione

### Criteri per il notebook

- correttezza della simulazione congiunta;
- corretta costruzione delle date di fixing;
- corretta definizione di $A_T$;
- corretta costruzione del payoff;
- corretta attualizzazione scenario per scenario;
- pricing Monte Carlo;
- misura dell'errore di simulazione;
- qualità dei controlli;
- leggibilità del notebook;
- interpretazione finanziaria.

### Criteri per il tracciato IA

- qualità del contributo iniziale dello studente;
- corretta identificazione della path-dependence;
- capacità di scomporre il problema;
- uso appropriato dei regimi A, B e C;
- capacità di verificare il codice suggerito;
- presenza di controlli autonomi;
- capacità di correggere eventuali errori dell'IA;
- coerenza tra chat e notebook consegnato.

### Peso dei controlli e dell'interpretazione

Il risultato numerico del prezzo non deve essere sufficiente per una valutazione elevata.

Devono avere peso sostanziale:

- correttezza della costruzione del payoff;
- controlli;
- diagnostica Monte Carlo;
- interpretazione della path-dependence;
- qualità dell'interazione critica con l'IA.

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

- sottostante azionario: dinamica moltiplicativa di tipo GBM;
- tasso nominale: CIR;
- funzionale della traiettoria: media aritmetica dei fixing;
- prodotto: call asiatica;
- output finanziario: payoff opzionale path-dependent.

La struttura computazionale comune rende trasferibili metodo e controlli, ma non la soluzione.

Lo studente non può ottenere il take-home mediante semplice modifica dei parametri del notebook aula, perché deve ricostruire:

1. la variabile path-dependent;
2. il meccanismo di payoff;
3. il significato della traiettoria principale;
4. la relazione tra fattore simulato e valore finanziario.

Nel complesso, la coppia consente di utilizzare operativamente i tre modelli centrali del Capitolo 6:

- OU nel caso aula;
- GBM nel take-home;
- CIR in entrambi;

e di confrontare due forme profondamente diverse di dipendenza del valore finanziario dall'intera traiettoria.