# Scheda Costruzione Caso Applicativo

Documento interno di progettazione docente.  
**Lezione 7 — Caso Aula.**

## 1. Identificazione del caso

- **Lezione:** 7 — Applicazione in Python: simulazione di traiettorie e pricing
- **Tipo di caso:** Aula
- **Titolo:** *Inflazione e tassi stocastici: pricing Monte Carlo di un inflation-linked bond*
- **Destinatari:** studenti del secondo anno del Corso di Laurea Magistrale in Finanza e Risk Management
- **Uso previsto:** sviluppo guidato durante la lezione applicativa mediante notebook Jupyter e uso controllato dell'IA secondo il protocollo MQF.

Il caso consolida operativamente i contenuti dei Capitoli 5 e 6 e li trasferisce nel problema di valutazione sviluppato nel Capitolo 7:

- organizzazione di molte traiettorie simulate;
- distinzione tra dimensione temporale e dimensione Monte Carlo;
- processo Ornstein--Uhlenbeck per l'inflazione;
- processo CIR per il tasso nominale;
- simulazione con shock correlati;
- discretizzazione temporale;
- costruzione di quantità dipendenti dalla traiettoria;
- attualizzazione replica per replica;
- pricing e diagnostica Monte Carlo.

La Scheda Costruzione costituisce il documento docente a monte della Scheda Caso, del Flusso logico-teorico risolutivo, della scomposizione in tappe, della sequenza dei prompt e del notebook.

---

## 2. Contesto e motivazione

Un investitore deve valutare un'obbligazione i cui flussi dipendono dall'evoluzione futura dell'inflazione.

Le cedole sono indicizzate al livello dei prezzi. A scadenza il capitale rimborsato è anch'esso indicizzato, ma non può essere inferiore al valore facciale.

La valutazione dipende congiuntamente da due fattori stocastici:

1. il **tasso istantaneo di inflazione** $i_t$, che determina l'indicizzazione dei flussi;
2. il **tasso nominale istantaneo privo di rischio** $r_t$, che determina la loro attualizzazione.

Gli shock dei due fattori sono correlati.

Il caso non introduce nuovi modelli rispetto al Capitolo 6. La funzione didattica consiste nel mostrare come passare da modelli stocastici assegnati a una procedura quantitativa completa:

$
\text{modello}
\rightarrow
\text{shock}
\rightarrow
\text{traiettorie}
\rightarrow
\text{quantità contrattuali}
\rightarrow
\text{valore per replica}
\rightarrow
\text{stima Monte Carlo}
$.


Le dinamiche assegnate vengono utilizzate direttamente ai fini della valutazione. Non viene derivato un cambio di misura e non si afferma che i parametri costituiscano una calibrazione risk-neutral di mercato.

Il valore ottenuto deve pertanto essere interpretato come **risultato del modello assegnato**, non come quotazione teorica od osservabile di uno specifico inflation-linked bond di mercato.

---

## 3. Domanda quantitativa e obiettivo didattico

### Domanda quantitativa

**Qual è il valore corrente dell'inflation-linked bond ottenuto mediante simulazione Monte Carlo, e quale ruolo assumono l'indicizzazione, il rimborso protetto e la dipendenza tra inflazione e tasso nominale?**

La domanda non richiede una sensitivity analysis rispetto a $\rho$. La dipendenza tra i fattori entra nel modello attraverso gli shock correlati e deve essere correttamente preservata e verificata nella simulazione.

### Obiettivo didattico

Lo studente deve comprendere e costruire la catena

$$
\text{OU per }i_t
+
\text{CIR per }r_t
$$

$$
\downarrow
$$

$$
\text{shock correlati e traiettorie}
$$

$$
\downarrow
$$

$$
J_t,\;D(0,t)
$$

$$
\downarrow
$$

$$
\text{cedole e rimborso}
$$

$$
\downarrow
$$

$$
V^{(k)}
$$

$$
\downarrow
$$

$$
\widehat V_M
$$

$$
\downarrow
$$

$$
\text{diagnostica e interpretazione}.
$$


Il punto centrale è distinguere sempre:

- operazioni **lungo il tempo**, effettuate all'interno della stessa replica;
- operazioni **tra repliche**, utilizzate nell'aggregazione Monte Carlo.

---

## 4. Specifica teorico-matematica

### 4.1 Convenzione Monte Carlo

Il numero di repliche è indicato con $M$.

La singola replica è indicata con $k=1,\ldots,M$.

Una traiettoria simulata del processo $X$ nella replica $k$ è quindi rappresentata da
$X_{t_0}^{(k)},\ldots,X_{t_N}^{(k)}$.

Il termine **scenario** non deve essere utilizzato per indicare una replica Monte Carlo. Rimane utilizzabile nel normale significato economico o probabilistico, per esempio «scenario di deflazione».

### 4.2 Inflazione

Il tasso istantaneo di inflazione segue un processo Ornstein--Uhlenbeck:

$$
di_t = \kappa_i(\theta_i-i_t)\,dt
+
\sigma_i\,dW_t^{(i)}.
$$

I valori negativi di $i_t$ sono compatibili con il modello e rappresentano periodi di deflazione.

### 4.3 Tasso nominale

Il tasso nominale istantaneo privo di rischio segue un processo CIR:

$$
dr_t = \kappa_r(\theta_r-r_t)\,dt
+
\sigma_r\sqrt{r_t}\,dW_t^{(r)}.
$$

I parametri assegnati soddisfano la condizione di Feller:

$$
2\kappa_r\theta_r\geq\sigma_r^2.
$$

### 4.4 Convenzione numerica vincolante per il CIR

Sulla griglia temporale si utilizza

$$
r_{t_{j+1}}^{(k)}
=
r_{t_j}^{(k)}
+
\kappa_r
\left(
\theta_r-r_{t_j}^{(k)}
\right)\Delta t
+
\sigma_r
\sqrt{\max(r_{t_j}^{(k)},0)}
\sqrt{\Delta t}\,
Z_{r,j+1}^{(k)}.
$$

L'operatore

$$\max(r_{t_j}^{(k)},0)$$

deve agire **soltanto all'interno della radice quadrata**.

Il valore aggiornato $r_{t_{j+1}}^{(k)}$ non deve essere successivamente forzato a zero mediante un'operazione del tipo

```python
r_next = np.maximum(r_next_raw, 0.0)
```

Eventuali valori negativi prodotti dalla discretizzazione devono invece essere mantenuti, rilevati, conteggiati e interpretati come possibile anomalia numerica della discretizzazione.

Questa convenzione è vincolante anche come riferimento metodologico per il Caso TakeHome.

### 4.5 Dipendenza tra i fattori

Gli shock browniani soddisfano

$$
dW_t^{(i)}\,dW_t^{(r)}
=
\rho\,dt.
$$

A partire da due normali standard indipendenti si costruiscono, per ogni replica $k$ e intervallo temporale $j$,

$$
Z_{i,j}^{(k)}
=
Z_{1,j}^{(k)},
$$

$$
Z_{r,j}^{(k)}
=
\rho Z_{1,j}^{(k)}
+
\sqrt{1-\rho^2}\,
Z_{2,j}^{(k)}.
$$

Deve essere preservato l'allineamento tra i due fattori: gli shock e le traiettorie della stessa riga appartengono alla stessa replica.

La correlazione da verificare empiricamente è la correlazione degli **shock**, non quella dei livelli simulati di $i_t$ e $r_t$.

### 4.6 Indicizzazione

Sia $I_t$ il livello dell'indice dei prezzi. Il tasso $i_t$ ne rappresenta il tasso istantaneo di crescita:

$$
dI_t=I_t i_t\,dt.
$$

Il fattore cumulato di indicizzazione è

$$
J_t
=
\frac{I_t}{I_0}
=
\exp\left(
\int_0^t i_s\,ds
\right).
$$

Per la replica $k$,

$$
J_{t_j}^{(k)}
\approx
\exp\left(
\sum_{\ell=0}^{j-1}
i_{t_\ell}^{(k)}
\Delta t
\right).
$$

Per costruzione,

$$
J_0^{(k)}=1,
\qquad
J_{t_j}^{(k)}>0.
$$

### 4.7 Fattore di sconto

Il fattore di sconto è

$$
D(0,t)
=
\exp\left(
-\int_0^t r_s\,ds
\right).
$$

Per ogni replica,

$$
D^{(k)}(0,t_j)
\approx
\exp\left(
-\sum_{\ell=0}^{j-1}
r_{t_\ell}^{(k)}
\Delta t
\right).
$$

Il fattore di sconto deve quindi essere costruito utilizzando la traiettoria del tasso della **stessa replica**. Non deve essere sostituito da un tasso terminale o da una media trasversale tra repliche.

### 4.8 Flussi contrattuali

Il bond ha valore facciale $N$, scadenza $T$ e tasso cedolare annuo $c$.

Le cedole sono semestrali. Alla data $t_j$,

$$
C_{t_j}^{(k)}
=
\frac{c}{2}
N
J_{t_j}^{(k)}.
$$

Le cedole non sono protette contro la deflazione.

A scadenza il rimborso del capitale è

$$
R_T^{(k)}
=
N\max(J_T^{(k)},1).
$$

Deve pertanto valere, replica per replica,

$$
R_T^{(k)}\geq N.
$$

La decomposizione

$$
R_T^{(k)}
=
N+
N\max(J_T^{(k)}-1,0)
$$

può essere utilizzata a fini interpretativi, ma **non costituisce un output numerico obbligatorio autonomo** del Caso Aula.

### 4.9 Valore attuale per replica

Il valore attuale delle cedole nella replica $k$ è

$$
PV_C^{(k)}
=
\sum_{j=1}^{m}
D^{(k)}(0,t_j)
C_{t_j}^{(k)}.
$$

Il valore attuale del rimborso è

$$
PV_R^{(k)}
=
D^{(k)}(0,T)
R_T^{(k)}.
$$

Il valore complessivo è

$$
V^{(k)}
=
PV_C^{(k)}
+
PV_R^{(k)}.
$$

Tutti i flussi e i fattori di sconto devono quindi essere combinati **replica per replica prima di qualsiasi media Monte Carlo**.

### 4.10 Stima Monte Carlo

Il prezzo stimato è

$$
\widehat V_M
=
\frac{1}{M}
\sum_{k=1}^{M}
V^{(k)}.
$$

Indicando con $s_V$ la deviazione standard campionaria dei valori $V^{(k)}$,

$$
SE(\widehat V_M)
=
\frac{s_V}{\sqrt{M}}.
$$

L'intervallo di confidenza Monte Carlo approssimato al $95\%$ è

$$
\widehat V_M
\pm
1.96\,SE(\widehat V_M).
$$

La decomposizione del prezzo deve soddisfare

$$
\widehat V_M
=
\widehat{PV}_C
+
\widehat{PV}_R.
$$

### 4.11 Deflazione cumulata

La probabilità simulata di deflazione cumulata a scadenza è

$$
\widehat{\mathbb P}(J_T<1)
=
\frac{1}{M}
\sum_{k=1}^{M}
\mathbf 1_{\{J_T^{(k)}<1\}}.
$$

Essa coincide con la quota di repliche nelle quali il floor sul capitale risulta attivo.

---

## 5. Parametri assegnati

I parametri sono didattici e non costituiscono una calibrazione a dati di mercato.

| Componente | Parametro | Valore |
|---|---|---:|
| Contratto | $N$ | 100 |
| Contratto | $T$ | 5 anni |
| Contratto | $c$ | 1,5% annuo |
| Contratto | frequenza cedole | semestrale |
| Indice prezzi | $I_0$ | 100 |
| Inflazione OU | $i_0$ | 0,025 |
| Inflazione OU | $\kappa_i$ | 0,80 |
| Inflazione OU | $\theta_i$ | 0,020 |
| Inflazione OU | $\sigma_i$ | 0,015 |
| Tasso CIR | $r_0$ | 0,030 |
| Tasso CIR | $\kappa_r$ | 1,20 |
| Tasso CIR | $\theta_r$ | 0,030 |
| Tasso CIR | $\sigma_r$ | 0,10 |
| Dipendenza | $\rho$ | 0,25 |
| Simulazione | $\Delta t$ | 1/12 |
| Simulazione | $M$ | 50.000 |
| Simulazione | seed | 12345 |

La griglia principale è mensile:

$$
N_{\mathrm{step}}=60,
$$

con $61$ nodi inclusa la data iniziale.

Le dieci date semestrali di pagamento corrispondono ai passi

$$
6,12,\ldots,60.
$$

---

## 6. Quantità e output richiesti

La Scheda Costruzione deve riprodurre esattamente il perimetro quantitativo destinato alla Scheda Caso.

### 6.1 Quantità numeriche obbligatorie

Devono essere determinate:

1. prezzo Monte Carlo del bond;
2. errore standard Monte Carlo e intervallo di confidenza al $95\%$;
3. valore attuale medio delle cedole;
4. valore attuale atteso del rimborso del capitale;
5. probabilità simulata di deflazione cumulata a scadenza, $\widehat{\mathbb P}(J_T<1)$;
6. media e deviazione standard simulate di $i_T$, $r_T$ e $J_T$.

Non costituiscono output obbligatori aggiuntivi:

- una sensitivity analysis rispetto a $\rho$;
- il valore autonomo della protezione del capitale;
- una decomposizione obbligatoria del rimborso tra nominale e rivalutazione.

Tali elementi possono essere utilizzati dal docente come approfondimenti, purché restino esplicitamente distinti dalla consegna vincolante.

### 6.2 Tabelle obbligatorie

**Tabella 1 — Parametri del caso**

Contratto, OU, CIR, correlazione e simulazione.

**Tabella 2 — Sintesi del pricing**

Almeno:

- valore attuale medio delle cedole;
- valore attuale atteso del rimborso;
- prezzo complessivo.

**Tabella 3 — Diagnostica Monte Carlo**

Per

$$
M=1\,000,\;5\,000,\;10\,000,\;50\,000
$$

riportare almeno:

- prezzo stimato;
- errore standard.

**Tabella 4 — Statistiche terminali**

Media e deviazione standard di:

$$
i_T,\qquad r_T,\qquad J_T.
$$

### 6.3 Grafici obbligatori

Produrre almeno:

1. alcune traiettorie simulate di $i_t$;
2. alcune traiettorie simulate di $r_t$;
3. distribuzione simulata di $J_T$;
4. distribuzione dei valori attuali $V^{(k)}$;
5. grafico di convergenza della stima Monte Carlo al crescere di $M$.

Un grafico delle traiettorie di $J_t$ può essere utilizzato dal docente come diagnostica aggiuntiva, ma non è un output obbligatorio della Scheda Caso.

---

## 7. Controlli obbligatori

Il notebook deve verificare esplicitamente:

1. **correlazione degli shock**

$$
\widehat\rho\approx0.25;
$$

2. **positività del fattore di indicizzazione**

$$
J_{t_j}^{(k)}>0
$$

per ogni replica e data;

3. **floor sul capitale**

$$
R_T^{(k)}\geq N
$$

per ogni replica;

4. **anomalia numerica CIR**

rilevare, conteggiare e documentare gli eventuali valori

$$
r_{t_j}^{(k)}<0
$$

prodotti dalla discretizzazione, senza azzerare sistematicamente il valore aggiornato;

5. **decomposizione del prezzo**

$$
\widehat V_M
=
\widehat{PV}_C+\widehat{PV}_R;
$$

6. **precisione Monte Carlo**

verificare che l'errore standard diminuisca al crescere di $M$ in modo compatibile con

$$
O(M^{-1/2});
$$

7. **stabilità rispetto alla griglia temporale**

confrontare il prezzo principale, ottenuto con

$$
\Delta t=\frac1{12},
$$

con quello ottenuto su almeno una griglia più fine.

I primi cinque controlli verificano la coerenza della costruzione quantitativa. I controlli 6 e 7 riguardano invece due differenti fonti di approssimazione numerica:

$$
M
\longrightarrow
\text{errore Monte Carlo},
$$

$$
\Delta t
\longrightarrow
\text{errore di discretizzazione}.
$$

Aumentare $M$ non corregge l'errore di discretizzazione; raffinare la griglia non sostituisce un numero adeguato di repliche.

---

## 8. Flusso logico-teorico risolutivo atteso

Il Flusso logico-teorico deve precedere la scomposizione operativa del notebook. Non è una descrizione del codice: ricostruisce il percorso teorico necessario per passare dalla domanda quantitativa agli output richiesti.

| Passo | Finalità risolutiva | Formula teorico-matematica / definizione / proprietà | Applicazione nel caso | Output o controllo collegato |
|---:|---|---|---|---|
| 1 | Identificare i fattori di rischio | SDE OU e CIR | Definire $i_t$ e $r_t$ con condizioni iniziali e parametri assegnati | Parametri; verifica di Feller |
| 2 | Rappresentare la dipendenza | Correlazione fra Browniani | Costruire coppie di shock correlati all'interno della stessa replica | Correlazione empirica degli shock |
| 3 | Passare dal continuo alla griglia | Discretizzazione delle SDE | Simulare $i_t^{(k)}$ e $r_t^{(k)}$ sulle $M$ repliche | Traiettorie; statistiche terminali; diagnostica CIR |
| 4 | Trasformare l'inflazione in indicizzazione | $J_t=\exp(\int_0^t i_s\,ds)$ | Approssimare l'integrale lungo ogni traiettoria | $J_t^{(k)}$; $J_t>0$; $J_T$; deflazione cumulata |
| 5 | Costruire l'attualizzazione | $D(0,t)=\exp(-\int_0^t r_s\,ds)$ | Approssimare l'integrale del tasso nella stessa replica | Fattori $D^{(k)}(0,t)$ |
| 6 | Selezionare le date contrattuali | Date semestrali della griglia | Estrarre $J_{t_j}^{(k)}$ e $D^{(k)}(0,t_j)$ ai passi $6,12,\ldots,60$ | Coerenza calendario/griglia |
| 7 | Costruire i flussi | Cedola indicizzata e rimborso protetto | Calcolare $C_{t_j}^{(k)}$ e $R_T^{(k)}$ | Controllo $R_T^{(k)}\geq N$ |
| 8 | Costruire il valore per replica | Somma dei flussi attualizzati | Calcolare $PV_C^{(k)}$, $PV_R^{(k)}$, $V^{(k)}$ | Distribuzione dei valori; identità pathwise |
| 9 | Aggregare tra repliche | Media campionaria, deviazione standard, SE | Calcolare $\widehat V_M$, decomposizione e IC 95% | Tabelle di pricing |
| 10 | Valutare precisione e discretizzazione | $SE=O(M^{-1/2})$; confronto tra griglie | Variare $M$ e raffinare $\Delta t$ | Diagnostica Monte Carlo e stabilità temporale |
| 11 | Interpretare il risultato | Distinzione tra risultato del modello e valore di mercato | Collegare indicizzazione, floor, sconto e limiti del modello | Commento economico-finanziario conclusivo |

Il Flusso deve restare riconoscibile nella successiva costruzione del notebook.

---

## 9. Scomposizione attesa in tappe input-output

La scomposizione operativa viene costruita **dopo** il Flusso logico-teorico. Le undici unità concettuali precedenti vengono raccolte in sei tappe computazionali compatibili con il lavoro in aula.

| Tappa | Regime ordinario | Input | Operazione principale | Output essenziali | Controlli principali | Uso successivo |
|---:|:---:|---|---|---|---|---|
| 1 | B | Scheda Caso, parametri, $M$, $\Delta t$, seed, $\rho$ | Definire ambiente, parametri, griglia e date contrattuali; generare gli shock correlati | Tabella parametri; griglia; matrici $Z_i,Z_r$ | Feller; dimensioni; date semestrali; correlazione empirica | Simulazione fattori |
| 2 | B | Parametri e shock correlati | Simulare $i_t$ e $r_t$ con le convenzioni numeriche assegnate | Matrici delle traiettorie; statistiche di $i_T,r_T$ | Anomalie CIR; coerenza dimensionale | Quantità path-dependent |
| 3 | B | Traiettorie $i_t,r_t$ | Costruire cumulativamente $J_t$ e $D(0,t)$ | Matrici $J,D$; statistiche $J_T$; probabilità $J_T<1$ | $J_t>0$; allineamento replica per replica | Flussi contrattuali |
| 4 | B | $J,D$, date cedolari, $N,c,T$ | Costruire cedole, rimborso e valori attuali replica per replica | $PV_C^{(k)},PV_R^{(k)},V^{(k)}$ | $R_T^{(k)}\geq N$; identità $V^{(k)}=PV_C^{(k)}+PV_R^{(k)}$ | Aggregazione Monte Carlo |
| 5 | B | Campione $V^{(k)}$ e componenti di valore | Calcolare prezzo, SE, IC 95%, decomposizione e tabelle di sintesi | $\widehat V_M$; SE; IC; Tabelle 2 e 4 | Decomposizione del prezzo | Diagnostica finale |
| 6 | B | Procedura completa e output precedenti | Costruire diagnostica per diversi $M$, confronto della griglia, grafici obbligatori e interpretazione conclusiva | Tabella 3; cinque grafici; confronto $\Delta t$; conclusione | $1/\sqrt M$; stabilità temporale; coerenza complessiva; rieseguibilità | Chiusura del caso |

La Tappa 6 fa parte della soluzione ordinaria e **non costituisce di per sé Regime C**.

Il Regime C viene utilizzato soltanto se lo studente individua una criticità specifica in una formula, nel codice, in un output, in un controllo o in una bozza interpretativa.

---

## 10. Mappa tra prompt e notebook

| Prompt | Regime | Funzione | Prodotto nel notebook | Vincolo |
|---|:---:|---|---|---|
| Prompt zero | — | Inizializzare contesto, regole e regimi | Nessuna cella quantitativa obbligatoria | Rispetto del protocollo |
| Prompt 1 | — | Acquisire la Scheda Caso | Cella Markdown iniziale di inquadramento | Nessuna soluzione anticipata |
| Prompt 2 | A | Costruire il Flusso logico-teorico a partire dalla proposta dello studente | Una cella Markdown con tabella del Flusso | Contributo iniziale dello studente visibile |
| Prompt 3 | — | Trasformare il Flusso validato in tappe input-output | Una cella Markdown con le sei tappe | Contributo iniziale dello studente; nessun codice |
| Prompt Tappa 1 | B | Implementare la Tappa 1 validata | Markdown + codice + output + controllo | Non modificare Scheda Caso |
| Prompt Tappa 2 | B | Implementare la Tappa 2 validata | Markdown + codice + output + controllo | Convenzione CIR vincolante |
| Prompt Tappa 3 | B | Implementare la Tappa 3 validata | Markdown + codice + output + controllo | Operazioni lungo la stessa replica |
| Prompt Tappa 4 | B | Implementare la Tappa 4 validata | Markdown + codice + output + controllo | Valore costruito replica per replica |
| Prompt Tappa 5 | B | Implementare la Tappa 5 validata | Markdown + codice + tabelle + controllo | Aggregazione solo dopo la costruzione di $V^{(k)}$ |
| Prompt Tappa 6 | B | Completare diagnostica, grafici e interpretazione | Codice + output + Markdown conclusivo | Distinguere errori MC, discretizzazione e modello |
| Eventuale Prompt C | C | Verificare una criticità concreta individuata dallo studente | Eventuale sostituzione delle celle interessate | Non è obbligatorio e non può essere precompilato come verifica generica |

---

## 11. Struttura attesa del notebook

Il notebook deve rendere visibile sia il ragionamento sia la costruzione computazionale.

L'ordine atteso è:

1. **Titolo e inquadramento del caso** — Markdown derivato dal Prompt 1.
2. **Flusso logico-teorico risolutivo** — Markdown derivato dal Prompt 2.
3. **Scomposizione in sei tappe input-output** — Markdown derivato dal Prompt 3.
4. **Tappa 1 — setup, griglia e shock correlati.**
5. **Tappa 2 — simulazione congiunta di inflazione e tasso.**
6. **Tappa 3 — costruzione di $J_t$ e $D(0,t)$.**
7. **Tappa 4 — cash flow e valore attuale replica per replica.**
8. **Tappa 5 — prezzo Monte Carlo e statistiche di sintesi.**
9. **Tappa 6 — diagnostica Monte Carlo, controllo della griglia, grafici e interpretazione.**
10. **Limiti del modello e riproducibilità del notebook.**

Ogni tappa deve essere preceduta da una breve cella Markdown che chiarisca:

- input disponibili;
- operazione quantitativa;
- output attesi;
- controllo da eseguire;
- collegamento con la tappa successiva.

Il notebook non deve essere organizzato come una successione di blocchi di codice privi di raccordo teorico.

---

## 12. Criteri di validazione docente

### 12.1 Coerenza strutturale

Il notebook è strutturalmente coerente se:

- contiene il Flusso logico-teorico prima delle tappe;
- contiene la scomposizione input-output prima dell'implementazione;
- conserva la catena tra le sei tappe;
- non introduce output obbligatori non presenti nella Scheda Caso;
- non elimina output o controlli richiesti;
- utilizza $k=1,\ldots,M$ per le repliche Monte Carlo.

### 12.2 Coerenza computazionale

Devono essere verificati:

- forma degli array coerente con repliche sulle righe e tempo sulle colonne;
- corretto uso degli assi NumPy;
- allineamento degli shock dei due fattori nella stessa replica e nello stesso intervallo;
- corretta selezione dei passi cedolari;
- somme di Riemann costruite lungo la dimensione temporale;
- fattori di sconto costruiti replica per replica;
- assenza di aggregazioni premature tra repliche.

### 12.3 Convenzione CIR

È da considerare non coerente una soluzione che:

- sostituisca ogni nuovo valore negativo del CIR con zero;
- introduca una diversa tecnica di discretizzazione senza che la Scheda Caso sia stata modificata;
- elimini i valori negativi prima di poterli diagnosticare.

La protezione numerica

$$
\sqrt{\max(r_t,0)}
$$

riguarda esclusivamente il termine diffusivo.

### 12.4 Coerenza finanziaria

Devono essere rispettati:

$$
J_t^{(k)}>0,
$$

$$
R_T^{(k)}\geq N,
$$

$$
V^{(k)}
=
PV_C^{(k)}
+
PV_R^{(k)}.
$$

Cedole e capitale devono utilizzare l'indicizzazione della medesima replica; i relativi flussi devono essere attualizzati con il fattore di sconto costruito dalla medesima traiettoria del tasso.

### 12.5 Coerenza numerica

Devono essere tenuti distinti:

- errore Monte Carlo;
- errore di discretizzazione;
- errore di modello.

Una riduzione dell'errore standard all'aumentare di $M$ non dimostra la convergenza rispetto a $\Delta t$.

### 12.6 Riproducibilità

Il notebook deve poter essere eseguito integralmente dall'inizio in ambiente pulito.

Il seed principale è

$$
12345.
$$

Non devono esistere celle che dipendono da variabili prodotte da esecuzioni precedenti ma non ricostruite dal notebook corrente.

---

## 13. Errori o ambiguità prevedibili

1. confondere $i_t$ con il livello dell'indice dei prezzi $I_t$;
2. utilizzare $1+i_t$ come fattore di indicizzazione;
3. dimenticare la natura cumulativa di $J_t$;
4. confondere una replica Monte Carlo con uno scenario teorico;
5. utilizzare l'indice $s$ per le repliche invece di $k$;
6. confondere la correlazione degli shock con la correlazione dei livelli di $i_t$ e $r_t$;
7. generare processi indipendenti nonostante $\rho\neq0$;
8. utilizzare la stessa normale per entrambi i processi, ottenendo correlazione perfetta;
9. modificare il valore aggiornato del CIR imponendo artificialmente $r_t\geq0$;
10. interpretare valori CIR negativi dovuti alla discretizzazione come caratteristica economica del processo continuo;
11. applicare il floor alle cedole;
12. applicare il floor al tasso di inflazione;
13. utilizzare $r_T$ per scontare i flussi;
14. utilizzare un fattore di sconto comune ottenuto mediando i tassi tra repliche;
15. combinare $J_t$ di una replica con $D(0,t)$ di un'altra;
16. mediare le traiettorie prima di costruire i flussi;
17. confondere aggregazione lungo il tempo e aggregazione tra repliche;
18. presentare $\widehat V_M$ come valore numericamente esatto;
19. utilizzare il Regime C come fase ordinaria e obbligatoria del lavoro;
20. omettere Flusso logico-teorico e scomposizione in tappe passando direttamente dalla Scheda Caso al codice.

---

## 14. Ipotesi e limiti interpretativi

Ai fini del caso:

1. i parametri dei processi sono costanti e assegnati;
2. le dinamiche specificate vengono utilizzate direttamente ai fini della valutazione;
3. non viene derivato né richiesto un cambio di misura;
4. non vengono effettuate stima econometrica o calibrazione di mercato;
5. non sono considerati rischio di credito, liquidità o fiscalità;
6. l'indicizzazione non replica integralmente lag e convenzioni operative dei titoli inflation-linked reali;
7. l'indice dei prezzi viene costruito direttamente dall'integrazione del tasso istantaneo di inflazione;
8. i due processi sono simulati sulla medesima griglia;
9. la simulazione è una rappresentazione discretizzata di modelli formulati in tempo continuo.

L'interpretazione conclusiva deve distinguere esplicitamente:

$$
\text{risultato del modello}
\neq
\text{quotazione osservabile di mercato}.
$$

---

## 15. Uso dell'IA

### Usi ammessi

L'IA può essere utilizzata per:

- verificare e completare il Flusso logico-teorico proposto dallo studente;
- verificare la scomposizione operativa proposta dallo studente;
- tradurre in Python una singola tappa già validata;
- spiegare localmente codice e output;
- proporre o implementare i controlli previsti;
- verificare una criticità specifica;
- aiutare a formulare l'interpretazione di output già prodotti.

### Usi non ammessi

L'IA non deve:

- sostituire la Scheda Caso;
- modificare modello, parametri, contratto o controlli;
- produrre l'intero notebook in un'unica risposta;
- saltare il Flusso logico-teorico o la scomposizione in tappe;
- introdurre una diversa discretizzazione CIR;
- eliminare controlli perché il risultato appare plausibile;
- aggiungere autonomamente analisi di sensitività o output obbligatori;
- produrre interpretazioni non sostenute dagli output del notebook.

### Regime C

Il Regime C non costituisce una tappa programmata.

La sequenza è:

$$
\text{criticità individuata dallo studente}
\rightarrow
\text{Prompt C mirato}
\rightarrow
\text{verifica della risposta}
\rightarrow
\text{eventuale correzione delle celle}.
$$

In assenza di una criticità specifica non deve essere generato artificialmente un Prompt C.

---

## 16. Relazione con il Caso TakeHome

Caso Aula e Caso TakeHome condividono la stessa architettura metodologica:

$$
\text{fattori stocastici}
\rightarrow
\text{shock correlati}
\rightarrow
\text{traiettorie}
\rightarrow
\text{quantità path-dependent}
\rightarrow
\text{flussi/payoff}
\rightarrow
\text{attualizzazione per replica}
\rightarrow
\text{stima Monte Carlo}
\rightarrow
\text{diagnostica}
\rightarrow
\text{interpretazione}.
$$

Condividono inoltre:

- $M$ come numero di repliche Monte Carlo;
- $k$ come indice di replica;
- organizzazione matriciale repliche $\times$ tempo;
- costruzione di shock correlati;
- processo CIR con la medesima convenzione numerica;
- fattore di sconto costruito dalla traiettoria del tasso;
- valore finanziario costruito replica per replica;
- errore standard Monte Carlo;
- controllo della convergenza rispetto a $M$;
- controllo della discretizzazione;
- seed per la riproducibilità;
- sequenza Prompt zero → Prompt 1 → Prompt 2 → Prompt 3 → prompt di tappa;
- Regime C soltanto in presenza di una criticità specifica.

### Caso Aula

- primo fattore: inflazione OU;
- quantità path-dependent: $J_t$;
- prodotto: inflation-linked bond;
- flussi: cedole indicizzate e rimborso protetto;
- dinamiche assegnate utilizzate direttamente ai fini della valutazione.

### Caso TakeHome

- primo fattore: EURO STOXX 50 con diffusione geometrica e drift stocastico;
- quantità path-dependent: media aritmetica $A_T$;
- prodotto: call asiatica OTC;
- payoff: $(A_T-K)^+$;
- dinamiche assegnate esplicitamente sotto la misura risk-neutral $\mathbb Q$.

Il Caso TakeHome trasferisce quindi il **metodo**, non il codice né la soluzione del Caso Aula.

---

## 17. Esito atteso e calibrazione qualitativa

Prima dell'uso didattico il notebook docente deve essere rieseguito integralmente e validato.

Non deve essere imposto ex ante un prezzo-obiettivo.

La calibrazione qualitativa deve verificare che:

- il prezzo abbia ordine di grandezza finanziariamente plausibile rispetto al valore facciale;
- il livello delle cedole sia coerente con il tasso cedolare e con l'indicizzazione simulata;
- la probabilità di deflazione cumulata sia leggibile e interpretabile;
- il floor sul capitale abbia una funzione osservabile nel caso;
- gli shock presentino correlazione empirica compatibile con $\rho=0.25$;
- eventuali valori CIR negativi siano rilevati senza alterare silenziosamente le traiettorie;
- il prezzo mostri stabilità Monte Carlo al crescere di $M$;
- il raffinamento della griglia non produca variazioni economicamente rilevanti rispetto alla scala del problema;
- tabelle, grafici e commento conclusivo forniscano una lettura reciprocamente coerente degli stessi risultati.

Il notebook può essere considerato soluzione completa soltanto quando resta ricostruibile la sequenza

$$
\text{ipotesi}
\rightarrow
\text{simulazione}
\rightarrow
\text{quantità contrattuali}
\rightarrow
\text{flussi}
\rightarrow
\text{valore}
\rightarrow
\text{controlli}
\rightarrow
\text{interpretazione}.
$$