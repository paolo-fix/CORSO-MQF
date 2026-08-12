# Scheda Costruzione Caso Applicativo

Documento interno di progettazione docente.  
**Lezione 7 — caso aula.**

## 1. Identificazione del caso

- **Lezione:** 7 — Applicazione in Python: simulazione di traiettorie e pricing
- **Tipo di caso:** aula
- **Titolo:** *Inflazione e tassi stocastici: pricing Monte Carlo di un inflation-linked bond*
- **Destinatari:** studenti del secondo anno della Laurea Magistrale in Banca e Risk Management
- **Uso previsto:** caso sviluppato progressivamente durante la lezione applicativa, con costruzione guidata del notebook e uso controllato dell'IA. Il caso consolida operativamente i processi OU e CIR, la simulazione di diffusioni correlate, la discretizzazione temporale e la stima Monte Carlo introdotti nei Capitoli 5 e 6.

---

## 2. Contesto e motivazione

Un investitore istituzionale deve valutare un'obbligazione il cui valore nominale e le cui cedole sono indicizzati all'evoluzione del livello generale dei prezzi. Il contratto protegge inoltre il capitale nominale a scadenza: in presenza di deflazione cumulata, il rimborso non può scendere sotto il valore facciale.

La valutazione richiede di rappresentare congiuntamente due fonti di rischio:

1. l'evoluzione futura dell'inflazione, che determina l'indicizzazione dei flussi;
2. l'evoluzione futura del tasso nominale privo di rischio, che determina l'attualizzazione dei flussi.

L'inflazione è modellata mediante un processo di Ornstein--Uhlenbeck, coerente con la possibilità economica di osservare anche valori negativi del tasso di inflazione. Il tasso nominale è modellato mediante un processo CIR, che introduce mean reversion e preserva strutturalmente la non negatività del processo continuo.

I due fattori sono collegati attraverso shock browniani correlati.

Il caso è ispirato alla struttura modellistica di Falbo, Paris e Pelizzari, *Pricing inflation-linked bonds*, ma viene deliberatamente semplificato per concentrare l'attività didattica sui contenuti dei Capitoli 5 e 6.

In particolare, **non** vengono affrontati:

- stima econometrica dei parametri;
- calibrazione a prezzi di mercato;
- premi per il rischio di inflazione e di tasso;
- derivazione del cambio di misura;
- regole effettive di indicizzazione dei TIPS basate sul CPI con lag temporale;
- interpolazione dell'indice di riferimento;
- formule chiuse di pricing.

Le dinamiche assegnate sono interpretate direttamente come dinamiche da utilizzare ai fini della valutazione.

---

## 3. Domanda quantitativa e obiettivo didattico

**Domanda quantitativa**

Dato un modello stocastico congiunto per inflazione e tasso nominale, quale valore corrente attribuire a un inflation-linked bond con cedole indicizzate e protezione del capitale nominale a scadenza? Come si modifica il valore del titolo al variare delle traiettorie simulate, della correlazione tra i fattori e della protezione del capitale?

**Obiettivo didattico**

Portare lo studente a costruire una catena quantitativa di simulazione Monte Carlo:

$$
\text{modelli stocastici}
\rightarrow
\text{shock correlati}
\rightarrow
\text{traiettorie}
\rightarrow
\text{indice dei prezzi}
\rightarrow
\text{cash flow}
\\
\rightarrow
\text{fattori di sconto}
\rightarrow
\text{valori attuali per scenario}
\rightarrow
\text{stima}.
$$

Il caso deve mostrare che la simulazione di un processo non è un obiettivo autonomo: le traiettorie acquistano significato finanziario solo quando vengono trasformate nei flussi contrattuali e nei fattori di attualizzazione che determinano il valore del prodotto.

---

## 4. Specifica teorico-matematica

### Grandezze e variabili

Si considerano:

- $i_t$: tasso istantaneo di inflazione;
- $r_t$: tasso nominale istantaneo privo di rischio;
- $I_t$: indice dei prezzi;
- $J_t=I_t/I_0$: coefficiente di indicizzazione cumulata;
- $D(0,t)$: fattore di sconto stocastico;
- $N$: valore facciale dell'obbligazione;
- $c$: tasso cedolare nominale annuo;
- $T$: scadenza;
- $t_1,\ldots,t_m=T$: date di pagamento delle cedole.

### Dinamica dell'inflazione

Il tasso di inflazione segue un processo OU:

$$
di_t
=
\kappa_i(\theta_i-i_t)\,dt
+
\sigma_i\,dW_t^{(i)}.
$$

Interpretazione dei parametri:

- $\kappa_i>0$: velocità di mean reversion;
- $\theta_i$: livello di lungo periodo;
- $\sigma_i>0$: volatilità dell'inflazione.

Il modello ammette $i_t<0$, consentendo scenari di deflazione.

### Dinamica del tasso nominale

Il tasso nominale segue un processo CIR:

$$
dr_t
=
\kappa_r(\theta_r-r_t)\,dt
+
\sigma_r\sqrt{r_t}\,dW_t^{(r)}.
$$

con

$$
\kappa_r>0,\qquad
\theta_r>0,\qquad
\sigma_r>0.
$$

Per la calibrazione didattica iniziale si scelgono parametri che soddisfano la condizione di Feller:

$$
2\kappa_r\theta_r\geq \sigma_r^2.
$$

### Correlazione

Gli shock browniani soddisfano:

$$
dW_t^{(i)}\,dW_t^{(r)}
=
\rho\,dt,
\qquad -1\leq\rho\leq1.
$$

Operativamente, a ogni passo temporale si generano due normali standard indipendenti $Z_{1,k}$ e $Z_{2,k}$ e si costruisce:

$$
Z_{i,k}=Z_{1,k},
$$

$$
Z_{r,k}
=
\rho Z_{1,k}
+
\sqrt{1-\rho^2}\,Z_{2,k}.
$$

### Indice dei prezzi

Ponendo $I_0$ uguale al livello iniziale dell'indice:

$$
I_t
=
I_0
\exp\left(
\int_0^t i_s\,ds
\right).
$$

Pertanto:

$$
J_t
=
\frac{I_t}{I_0}
=
\exp\left(
\int_0^t i_s\,ds
\right).
$$

Nel notebook l'integrale viene approssimato sulla stessa griglia utilizzata per simulare i processi.

### Fattore di sconto

Per ogni traiettoria:

$$
D(0,t)
=
\exp\left(
-\int_0^t r_s\,ds
\right).
$$

Anche questo integrale viene approssimato numericamente sulla griglia temporale.

### Cedole indicizzate

Per pagamenti semestrali, la cedola alla data $t_j$ è:

$$
C_{t_j}
=
\frac{c}{2}N J_{t_j}.
$$

Le cedole possono quindi diminuire in presenza di deflazione.

### Rimborso del capitale

A scadenza il capitale è protetto al valore nominale:

$$
R_T
=
N\max(J_T,1).
$$

Equivalentemente:

$$
R_T
=
N
+
N\max(J_T-1,0).
$$

Questa decomposizione permette di distinguere il valore nominale del capitale dalla componente di rivalutazione legata all'inflazione.

### Valore attuale per scenario

Per la traiettoria simulata $s$:

$$
V^{(s)}
=
\sum_{j=1}^{m}
D^{(s)}(0,t_j)C_{t_j}^{(s)}
+
D^{(s)}(0,T)R_T^{(s)}.
$$

### Stima Monte Carlo

Con $M$ traiettorie:

$$
\widehat V_M
=
\frac{1}{M}
\sum_{s=1}^{M}V^{(s)}.
$$

Deve essere inoltre calcolato l'errore standard Monte Carlo:

$$
SE(\widehat V_M)
=
\frac{s_V}{\sqrt{M}},
$$

dove $s_V$ è la deviazione standard campionaria dei valori attuali simulati.

### Parametri e dati — calibrazione didattica iniziale proposta

Il caso non utilizza dati di mercato. I parametri sono assegnati.

**Contratto**

- $N=100$;
- $T=5$ anni;
- cedole semestrali;
- $c=1.5\%$ annuo;
- $I_0=100$.

**Inflazione OU**

- $i_0=0.025$;
- $\kappa_i=0.80$;
- $\theta_i=0.020$;
- $\sigma_i=0.015$.

**Tasso CIR**

- $r_0=0.030$;
- $\kappa_r=1.20$;
- $\theta_r=0.030$;
- $\sigma_r=0.10$.

**Dipendenza**

- $\rho=0.25$.

**Simulazione**

- orizzonte: 5 anni;
- griglia iniziale: mensile, $\Delta t=1/12$;
- numero di traiettorie per l'analisi principale: $M=50\,000$;
- seed fissato per rendere replicabili i risultati.

I valori sono una calibrazione esclusivamente didattica e dovranno essere verificati numericamente prima della costruzione definitiva del notebook.

### Ipotesi

1. i parametri dei processi sono costanti;
2. le dinamiche assegnate vengono utilizzate direttamente per la valutazione;
3. non si effettuano stima o calibrazione;
4. non si introducono rischio di credito o rischio di liquidità;
5. il contratto non replica integralmente le convenzioni di un TIPS reale;
6. l'indicizzazione è contemporanea e non presenta publication lag;
7. l'indice dei prezzi deriva dall'integrazione del tasso istantaneo di inflazione;
8. coupon e capitale sono determinati dalla stessa misura di indicizzazione;
9. il capitale, ma non le cedole, è protetto contro la deflazione cumulata;
10. i processi sono simulati sulla medesima griglia temporale.

### Quantità finali di interesse

- prezzo Monte Carlo del bond;
- errore standard della stima;
- valore attuale atteso delle cedole;
- valore attuale atteso del capitale;
- valore della protezione del capitale;
- distribuzione dei valori attuali per scenario;
- distribuzione dell'indice $J_T$;
- probabilità simulata di $J_T<1$;
- effetti della correlazione tra inflazione e tasso nominale.

---

## 5. Output richiesti

### Stime o risultati numerici

1. prezzo Monte Carlo $\widehat V_M$;
2. errore standard Monte Carlo;
3. intervallo di confidenza Monte Carlo al 95%;
4. valore attuale medio delle cedole;
5. valore attuale medio del capitale;
6. valore della componente di rivalutazione/protezione;
7. probabilità simulata di deflazione cumulata a scadenza:

$$
\widehat{\mathbb P}(J_T<1);
$$

8. media e deviazione standard di $i_T$, $r_T$ e $J_T$.

### Tabelle

**Tabella 1 — parametri del modello**

Parametri OU, CIR, correlazione, contratto e simulazione.

**Tabella 2 — decomposizione del prezzo**

- cedole;
- capitale nominale;
- rivalutazione del capitale;
- prezzo totale.

**Tabella 3 — diagnostica Monte Carlo**

Per un insieme crescente di numerosità, ad esempio

$$
M=1\,000,\ 5\,000,\ 10\,000,\ 50\,000,
$$

riportare prezzo stimato ed errore standard.

### Grafici

1. alcune traiettorie simulate di $i_t$;
2. alcune traiettorie simulate di $r_t$;
3. alcune traiettorie dell'indice $J_t$;
4. distribuzione simulata di $J_T$;
5. distribuzione dei valori attuali $V^{(s)}$;
6. grafico di convergenza della stima Monte Carlo al crescere di $M$.

Non tutti i grafici devono necessariamente entrare nelle slides: la selezione definitiva avverrà dopo la validazione del notebook.

### Controlli

1. verificare che la correlazione empirica degli shock simulati sia prossima a $\rho$;
2. verificare la mean reversion dei due processi attraverso le traiettorie e le statistiche terminali;
3. monitorare l'eventuale produzione di valori negativi di $r_t$ dovuti alla discretizzazione numerica;
4. verificare che $J_t>0$ per costruzione;
5. verificare che il rimborso soddisfi sempre:

$$
R_T\geq N;
$$

6. verificare che l'errore standard Monte Carlo diminuisca approssimativamente secondo $1/\sqrt{M}$;
7. verificare la stabilità del prezzo rispetto a una griglia temporale più fine;
8. verificare la coerenza della decomposizione:

$$
\text{prezzo totale}
=
\text{PV cedole}
+
\text{PV capitale}.
$$

---

## 6. Flusso logico-teorico risolutivo atteso

| Passo | Finalità risolutiva | Formula, definizione, proprietà o teorema | Applicazione nel caso | Output o controllo collegato |
|---:|---|---|---|---|
| 1 | Definire i fattori di rischio | SDE OU e CIR | Specificare inflazione e tasso nominale | Parametri e condizioni iniziali |
| 2 | Introdurre la dipendenza | Correlazione fra moti browniani | Costruire shock normali correlati | Correlazione empirica degli shock |
| 3 | Generare le traiettorie | Discretizzazione delle SDE | Simulare $i_t$ e $r_t$ | Grafici e statistiche dei processi |
| 4 | Trasformare l'inflazione in indicizzazione | $J_t=\exp\left(\int_0^t i_s\,ds\right)$ | Costruire l'indice cumulato | Traiettorie e distribuzione di $J_T$ |
| 5 | Costruire l'attualizzazione | $D(0,t)=\exp\left(-\int_0^t r_s\,ds\right)$ | Calcolare fattori di sconto scenario per scenario | Controllo di coerenza dei fattori di sconto |
| 6 | Costruire i cash flow | Cedole indicizzate e capitale protetto | Applicare $J_{t_j}$ alle cedole e il floor al capitale | Tabella dei flussi di alcune traiettorie |
| 7 | Valutare ogni scenario | Somma dei cash flow attualizzati | Calcolare $V^{(s)}$ | Distribuzione dei valori attuali |
| 8 | Aggregare Monte Carlo | Media campionaria ed errore standard | Stimare il prezzo | Prezzo, SE e intervallo di confidenza |
| 9 | Decomporre economicamente il valore | $R_T=N+N(J_T-1)^+$ | Separare capitale nominale e rivalutazione | Decomposizione del prezzo |
| 10 | Validare numericamente | Convergenza Monte Carlo e discretizzazione | Variare $M$ e $\Delta t$ | Tabelle e grafico di convergenza |
| 11 | Interpretare | Relazione tra fattori, payoff e sconto | Collegare traiettorie e prezzo | Commento finanziario conclusivo |

---

## 7. Scomposizione attesa in tappe

La scomposizione seguente è ancora una **mappa docente preliminare**. La sequenza definitiva dei prompt deve essere definita soltanto dopo la validazione del flusso logico-teorico.

| Tappa | Regime | Input | Operazione | Output | Controllo | Uso successivo |
|---:|:---:|---|---|---|---|---|
| 1 | A | Scheda Caso | Ricostruire struttura finanziaria e modello | Mappa teorica del problema | Nessuna formula estranea alla scheda | Base concettuale |
| 2 | B | Parametri, griglia, seed | Preparare ambiente numerico | Celle iniziali del notebook | Coerenza unità temporali | Simulazione |
| 3 | B | $\rho$, normali indipendenti | Generare shock correlati | Matrici degli shock | Correlazione empirica | OU e CIR |
| 4 | B | Shock e parametri | Simulare OU e CIR | Matrici delle traiettorie | Mean reversion; criticità CIR | Indicizzazione e sconto |
| 5 | B | Traiettorie $i_t$ | Integrare inflazione | $J_t$ | Positività dell'indice | Cash flow |
| 6 | B | Traiettorie $r_t$ | Integrare tassi | $D(0,t)$ | Coerenza dei discount factor | Pricing |
| 7 | B | $J_t$, contratto | Costruire cedole e rimborso | Cash flow per scenario | Floor sul capitale | Valori attuali |
| 8 | B | Cash flow e discount factor | Attualizzare e aggregare | $V^{(s)}$, $\widehat V_M$, SE | Identità di decomposizione | Interpretazione |
| 9 | C | Risultati principali | Eseguire controlli di convergenza | Tabelle diagnostiche | $1/\sqrt M$, sensibilità a $\Delta t$ | Validazione |
| 10 | C | Output validati | Interpretare risultati | Commento economico-finanziario | Distinguere modello e realtà | Chiusura caso |

---

## 8. Mappa tra prompt e notebook

La numerazione esatta dei prompt non viene ancora fissata. La progettazione definitiva seguirà la validazione delle tappe.

La struttura attesa è:

| Prompt | Regime | Tappa | Celle o output prodotti | Decisione o controllo richiesto |
|---|:---:|:---:|---|---|
| Prompt zero | — | — | Inizializzazione dell'ambiente di lavoro con IA | Rispetto del protocollo |
| Prompt 1 | — | — | Cella Markdown iniziale di descrizione del caso | Fedeltà alla Scheda Caso |
| Prompt 2 | — | 1 | Flusso logico-teorico | Validazione docente/studente |
| Prompt 3 | — | 1–10 | Scomposizione in tappe | Coerenza input-output |
| da definire | A | 1 | Ricognizione teorico-modellistica | Comprensione del problema |
| da definire | B | 2–8 | Celle Markdown e codice | Output e controlli di ogni tappa |
| da definire | C | 9–10 | Diagnostica e interpretazione | Validazione critica |

---

## 9. Struttura attesa del notebook

1. **Titolo e inquadramento del caso** — Markdown.
2. **Specificazione del contratto** — Markdown.
3. **Specificazione dei processi OU e CIR** — Markdown.
4. **Parametri e impostazioni numeriche** — codice.
5. **Generazione degli shock correlati** — Markdown + codice + controllo.
6. **Simulazione di inflazione e tasso nominale** — Markdown + codice.
7. **Diagnostica delle traiettorie** — codice + grafici + commento.
8. **Costruzione dell'indice dei prezzi** — Markdown + codice.
9. **Costruzione dei fattori di sconto** — Markdown + codice.
10. **Costruzione dei cash flow indicizzati** — Markdown + codice.
11. **Applicazione del floor sul capitale** — Markdown + codice.
12. **Valore attuale scenario per scenario** — codice.
13. **Stima Monte Carlo del prezzo** — codice + tabella.
14. **Decomposizione del prezzo** — codice + tabella.
15. **Diagnostica Monte Carlo** — codice + tabella/grafico.
16. **Controllo della discretizzazione** — codice.
17. **Interpretazione finanziaria conclusiva** — Markdown.

Il notebook docente deve contenere tutti i controlli. Nelle slides verranno successivamente selezionati solo quelli essenziali alla conduzione dell'aula.

---

## 10. Calibrazione docente

### Ordine di grandezza atteso dei risultati

Prima della distribuzione del caso devono essere prodotti numericamente valori benchmark con seed fissato.

Non si deve fissare ex ante un prezzo-obiettivo arbitrario. La calibrazione deve invece verificare che:

- il prezzo sia finanziariamente plausibile rispetto al valore facciale;
- le cedole indicizzate abbiano ordine di grandezza coerente con $c$ e con l'inflazione simulata;
- la probabilità di deflazione cumulata non sia né praticamente nulla né dominante, in modo che il floor abbia una funzione didattica osservabile;
- il valore della protezione del capitale sia positivo ma non tale da dominare il valore complessivo;
- la distribuzione di $r_t$ resti compatibile con la natura del CIR;
- la correlazione scelta produca un effetto osservabile senza diventare il tema dominante del caso.

### Errori o ambiguità prevedibili

1. confondere tasso di inflazione $i_t$ e indice dei prezzi $I_t$;
2. usare direttamente $1+i_t$ come coefficiente di indicizzazione;
3. dimenticare che l'indicizzazione è cumulata;
4. confondere correlazione dei livelli dei processi con correlazione degli shock browniani;
5. generare due processi indipendenti nonostante $\rho\neq0$;
6. utilizzare la stessa normale per i due processi, imponendo implicitamente correlazione perfetta;
7. applicare il floor anche alle cedole;
8. applicare il floor al tasso di inflazione invece che al capitale;
9. attualizzare tutti i flussi con un unico tasso terminale;
10. usare $r_T$ al posto dell'integrale della traiettoria di $r_t$;
11. mediare prima i fattori e poi calcolare il payoff, invece di valutare scenario per scenario;
12. interpretare eventuali valori negativi generati dalla discretizzazione CIR come proprietà economica del processo continuo;
13. modificare arbitrariamente i valori negativi senza documentare la scelta numerica;
14. trascurare l'errore Monte Carlo e presentare la stima come valore esatto.

### Controlli minimi di validazione

- correlazione degli shock;
- positività di $J_t$;
- floor del capitale;
- eventuali violazioni numeriche della positività CIR;
- convergenza rispetto a $M$;
- sensibilità rispetto a $\Delta t$;
- identità della decomposizione del prezzo;
- replicabilità con seed fissato.

### Limiti interpretativi

Il prezzo ottenuto non deve essere presentato come quotazione teorica di un TIPS reale.

Il caso:

- non utilizza curve nominali osservate;
- non calibra i parametri;
- non tratta la struttura a termine;
- non incorpora publication lag e interpolazione CPI;
- non stima premi per il rischio;
- non include liquidità, fiscalità o credito sovrano;
- assume parametri costanti;
- utilizza una discretizzazione numerica dei processi continui.

L'obiettivo è comprendere la struttura quantitativa della valutazione mediante simulazione, non costruire un modello operativo di trading.

---

## 11. Uso dell'IA e tracciato

### Prompt obbligatori

- Prompt zero;
- Prompt 1;
- Prompt 2;
- Prompt 3;
- prompt di tappa coerenti con i regimi A, B e C.

La sequenza concreta viene definita dopo la validazione della presente scheda e della scomposizione definitiva.

### Numero minimo e massimo di prompt

Da determinare dopo la costruzione del notebook docente, in funzione del numero effettivo di tappe necessarie e dei tempi disponibili in aula.

### Usi ammessi dell'IA

- ricostruzione controllata del significato delle formule già fornite;
- proposta di traduzione operativa delle tappe in Python;
- generazione di codice locale per una tappa esplicitamente definita;
- spiegazione degli output;
- proposta di controlli numerici;
- identificazione di possibili errori;
- confronto critico tra risultato atteso e risultato ottenuto.

### Usi non ammessi

- sostituire la Scheda Caso con una formulazione autonoma del problema;
- cambiare il modello finanziario;
- introdurre processi o formule non richiesti;
- modificare silenziosamente parametri o ipotesi;
- produrre integralmente il notebook in un'unica risposta;
- eliminare controlli perché il risultato appare plausibile;
- fornire interpretazioni finanziarie non verificabili dai risultati prodotti.

---

## 12. Valutazione

Per il **caso aula** la presente sezione ha soprattutto funzione di progettazione e di preparazione alla successiva rubrica comune con il take-home.

### Criteri per il notebook

- corretta traduzione delle SDE;
- corretta costruzione degli shock correlati;
- coerenza della discretizzazione;
- corretta costruzione di $J_t$;
- corretta costruzione dei discount factor;
- corretta formulazione dei cash flow;
- applicazione corretta del floor;
- pricing scenario per scenario;
- corretta aggregazione Monte Carlo;
- presenza e qualità dei controlli;
- interpretazione finanziaria degli output;
- leggibilità e struttura del notebook.

### Criteri per il tracciato IA

- qualità del contributo iniziale dello studente;
- rispetto dei regimi di interazione;
- capacità di valutare criticamente le proposte dell'IA;
- presenza di richieste di controllo;
- correzione di eventuali errori dell'IA;
- assenza di delega integrale del problema;
- coerenza tra tracciato e notebook finale.

### Peso dei controlli e dell'interpretazione

I controlli numerici e l'interpretazione devono avere un peso sostanziale. La correttezza sintattica del codice, da sola, non costituisce evidenza sufficiente di comprensione del caso.

---

## 13. Relazione con l'altro caso della lezione

Il caso aula e il caso take-home condividono la medesima architettura quantitativa generale:

$$
\text{processi stocastici}
\rightarrow
\text{traiettorie correlate}
\rightarrow
\text{funzionale delle traiettorie}
\rightarrow
\text{cash flow/payoff}
\rightarrow
\text{attualizzazione}
\rightarrow
\text{stima Monte Carlo}
\rightarrow
\text{controlli}.
$$

Il **caso aula** utilizza:

$$
\text{OU per inflazione}
+
\text{CIR per tasso nominale}
$$

e trasforma le traiettorie nell'indicizzazione di cedole e capitale di un inflation-linked bond.

Il **caso take-home**, da sviluppare separatamente, utilizzerà:

$$
\text{GBM per il sottostante azionario}
+
\text{CIR per il tasso nominale}
$$

per valutare un'opzione asiatica con tasso di interesse stocastico.

La comparabilità metodologica è quindi elevata, ma i due casi non costituiscono variazioni parametriche dello stesso esercizio:

- cambia la natura del fattore principale;
- cambia il processo utilizzato;
- cambia il meccanismo che trasforma la traiettoria in payoff;
- cambia il significato finanziario della path-dependence;
- resta comune la logica di simulazione congiunta, attualizzazione scenario per scenario, aggregazione Monte Carlo e validazione.

Nel complesso, la coppia consente di utilizzare operativamente tutti e tre i principali modelli sviluppati nel Capitolo 6 — GBM, OU e CIR — senza forzarne artificialmente la presenza all'interno dello stesso prodotto finanziario.