# Lezione 04 — Scheda Caso Take-Home

## 1. Identificazione del caso

- **Lezione:** Lezione 04 — Applicazione in Python: probabilità, variabili casuali e condizionamento
- **Tipo di caso:** take-home
- **Titolo:** Shortfall di margine condizionato a regimi del costo dell’energia
- **Contesto:** impresa manifatturiera energivora esposta all’incertezza del prezzo dell’energia
- **Uso previsto:** lavoro individuale da svolgere con notebook Python e interazione documentata con l’IA

Questa Scheda Caso è la specifica operativa del lavoro.

La Scheda Caso deve essere acquisita come vincolante prima di costruire:

1. il Flusso logico-teorico risolutivo;
2. la scomposizione in tappe input-output;
3. le singole celle del notebook;
4. gli output numerici e grafici;
5. l’interpretazione finale.

La Scheda Caso non è una soluzione del problema. Non contiene già svolti il Flusso logico-teorico risolutivo, la scomposizione operativa, il notebook o l’interpretazione finale.

---

## 2. Contesto economico-finanziario

Il caso è ispirato alla forte instabilità dei costi energetici osservata negli anni recenti nei mercati europei. Per molte imprese manifatturiere, in particolare nei settori energivori, il prezzo dell’energia rappresenta una fonte rilevante di rischio operativo.

Un aumento del prezzo unitario dell’energia può ridurre il margine operativo dell’impresa. Se il margine scende sotto una soglia minima desiderata, si genera uno shortfall di margine, cioè una carenza rispetto all’obiettivo economico fissato.

Il caso non ha l’obiettivo di stimare un modello storico dei prezzi energetici né di produrre una previsione di mercato. Utilizza una simulazione controllata per rendere osservabile il legame tra:

1. prezzo unitario dell’energia;
2. costo energetico totale;
3. margine operativo;
4. shortfall rispetto a una soglia minima;
5. regimi informativi del mercato energetico;
6. valori attesi condizionati.

---

## 3. Domanda quantitativa

Si considera un’impresa manifatturiera con fabbisogno energetico annuo pari a $Q_E$ MWh.

Il prezzo unitario dell’energia è indicato con $P_E$ ed è espresso in euro/MWh.

Il costo energetico totale è:

$$
C_E = Q_E P_E.
$$

La contribuzione operativa netta non energetica è indicata con $G_0$. Essa rappresenta il margine disponibile prima del costo energetico.

Il margine operativo dopo il costo energetico è:

$$
M = G_0 - Q_E P_E.
$$

L’impresa considera desiderabile mantenere un margine almeno pari a $m^\star$.

Lo shortfall di margine è definito come:

$$
S = (m^\star - M)^+.
$$

Poiché $M=G_0-Q_E P_E$, si ha:

$$
S = (m^\star - G_0 + Q_E P_E)^+.
$$

La domanda quantitativa è:

$$
\text{Qual è la distribuzione dello shortfall } S
\text{ e come cambia lo shortfall atteso condizionando sui diversi regimi energetici?}
$$

In particolare, si vogliono stimare:

$$
\mathbb{E}[S],
\qquad
\mathbb{P}(S>0),
\qquad
\mathbb{P}(S>s^\star),
\qquad
q_{\alpha}(S),
\qquad
\mathbb{E}[S\mid A_g],
\qquad
\mathbb{E}[S\mid\mathcal{G}].
$$

---

## 4. Obiettivo didattico

Il caso serve a consolidare, in forma computazionale, i concetti introdotti nelle lezioni teoriche precedenti:

1. spazio di probabilità;
2. eventi;
3. partizioni informative;
4. variabili casuali;
5. distribuzioni condizionate;
6. trasformazioni di variabili casuali;
7. parte positiva;
8. probabilità di superamento soglia;
9. quantili;
10. valore atteso condizionato rispetto a eventi;
11. valore atteso condizionato rispetto alla sigma-algebra generata da una partizione;
12. formula del valore atteso totale.

Dal punto di vista computazionale, il caso richiede una procedura Monte Carlo gerarchica in Python.

Dal punto di vista interpretativo, il caso deve mostrare che l’informazione di regime non elimina l’incertezza, ma modifica la distribuzione rilevante dello shortfall e lo shortfall atteso condizionato.

---

## 5. Grandezze e oggetti del caso

Le grandezze economico-finanziarie sono:

- $G_0$: contribuzione operativa netta non energetica;
- $Q_E$: fabbisogno energetico;
- $P_E$: prezzo unitario dell’energia;
- $C_E$: costo energetico totale;
- $M$: margine operativo dopo il costo energetico;
- $m^\star$: margine minimo desiderato;
- $S$: shortfall di margine;
- $s^\star$: soglia di shortfall severo.

Le relazioni di riferimento sono:

$$
C_E = Q_E P_E,
$$

$$
M = G_0 - C_E = G_0 - Q_E P_E,
$$

$$
S = (m^\star - M)^+.
$$

Sostituendo la formula del margine:

$$
S = (m^\star - G_0 + Q_E P_E)^+.
$$

Lo shortfall è sempre non negativo:

$$
S\geq 0.
$$

Quando $M\geq m^\star$, lo shortfall è nullo.  
Quando $M<m^\star$, lo shortfall misura la distanza monetaria tra il margine effettivo e il margine minimo desiderato.

---

## 6. Partizione informativa

Il caso parte direttamente da una partizione informativa dello spazio degli esiti. Non deve essere introdotta una variabile casuale discreta ausiliaria.

La partizione è:

$$
\Omega=A_1\cup A_2\cup A_3,
\qquad
A_i\cap A_j=\emptyset
\quad \text{per } i\neq j.
$$

Gli eventi $A_1,A_2,A_3$ rappresentano tre regimi informativi del mercato energetico.

| Evento | Descrizione | Interpretazione economica |
|---|---|---|
| $A_1$ | Normalizzazione energetica | prezzi energetici relativamente contenuti |
| $A_2$ | Tensione persistente | prezzi energetici elevati ma non estremi |
| $A_3$ | Shock energetico severo | prezzi molto elevati e più volatili |

La sigma-algebra informativa generata dalla partizione è:

$$
\mathcal{G}=\sigma(A_1,A_2,A_3).
$$

---

## 7. Distribuzioni condizionate

Il prezzo unitario dell’energia è una variabile casuale continua:

$$
P_E:\Omega\to\mathbb{R}.
$$

Condizionatamente all’evento informativo $A_g$, il prezzo unitario dell’energia segue una distribuzione normale:

$$
P_E\mid A_g \sim \mathcal{N}(\mu_g,\sigma_g^2),
\qquad g=1,2,3.
$$

La distribuzione non condizionata di $P_E$ deriva dalla combinazione tra:

1. probabilità dei regimi $A_g$;
2. distribuzioni condizionate $P_E\mid A_g$.

La simulazione Monte Carlo deve quindi seguire uno schema gerarchico:

1. estrarre il regime $A_g$ secondo le probabilità assegnate;
2. estrarre $P_E$ dalla distribuzione condizionata al regime estratto;
3. calcolare $C_E=Q_E P_E$;
4. calcolare $M=G_0-Q_E P_E$;
5. calcolare $S=(m^\star-M)^+$.

La distribuzione normale del prezzo energetico è una scelta didattica e semplificata. Nel notebook deve essere controllata l’eventuale presenza di valori simulati negativi di $P_E$. Se presenti, tali valori devono essere discussi come limite del modello, non eliminati senza motivazione.

---

## 8. Parametri del caso

I parametri sono stilizzati e hanno funzione didattica. Non sono stime storiche e non hanno finalità previsionali.

### Parametri economico-finanziari

| Grandezza | Valore | Unità | Significato |
|---|---:|---|---|
| $G_0$ | 8.000.000 | euro | contribuzione operativa netta non energetica |
| $Q_E$ | 50.000 | MWh | fabbisogno energetico |
| $m^\star$ | 2.000.000 | euro | margine minimo desiderato |
| $s^\star$ | 1.000.000 | euro | soglia di shortfall severo |
| $n$ | 50.000 | simulazioni | dimensione Monte Carlo |
| seed | 24680 | — | seme casuale |

### Probabilità degli eventi informativi

| Evento | Descrizione | Probabilità |
|---|---|---:|
| $A_1$ | Normalizzazione energetica | 0,35 |
| $A_2$ | Tensione persistente | 0,45 |
| $A_3$ | Shock energetico severo | 0,20 |

Le probabilità devono sommare a uno.

### Distribuzioni condizionate del prezzo dell’energia

| Evento | $\mu_g$ | $\sigma_g$ | Unità | Lettura economica |
|---|---:|---:|---|---|
| $A_1$ | 75 | 15 | euro/MWh | prezzi relativamente contenuti |
| $A_2$ | 115 | 25 | euro/MWh | prezzi elevati ma non estremi |
| $A_3$ | 170 | 45 | euro/MWh | prezzi molto elevati e più dispersi |

---

## 9. Soglie implicite del prezzo dell’energia

Lo shortfall è positivo quando il margine operativo scende sotto il margine minimo desiderato:

$$
S>0
\quad\Longleftrightarrow\quad
M<m^\star.
$$

Poiché:

$$
M=G_0-Q_E P_E,
$$

si ottiene:

$$
S>0
\quad\Longleftrightarrow\quad
P_E>\frac{G_0-m^\star}{Q_E}.
$$

Con i parametri assegnati:

$$
\frac{G_0-m^\star}{Q_E}
=
\frac{8.000.000-2.000.000}{50.000}
=
120.
$$

Quindi:

$$
S>0
\quad\Longleftrightarrow\quad
P_E>120.
$$

Lo shortfall supera la soglia severa $s^\star$ quando:

$$
S>s^\star.
$$

Dato che:

$$
S=(m^\star-G_0+Q_E P_E)^+,
$$

si ha:

$$
S>s^\star
\quad\Longleftrightarrow\quad
P_E>
\frac{G_0-m^\star+s^\star}{Q_E}.
$$

Con i parametri assegnati:

$$
\frac{G_0-m^\star+s^\star}{Q_E}
=
\frac{8.000.000-2.000.000+1.000.000}{50.000}
=
140.
$$

Quindi:

$$
S>s^\star
\quad\Longleftrightarrow\quad
P_E>140.
$$

Le due soglie implicite del prezzo dell’energia sono dunque:

| Evento di rischio | Soglia implicita su $P_E$ |
|---|---:|
| $S>0$ | 120 euro/MWh |
| $S>s^\star$ | 140 euro/MWh |

---

## 10. Quantità da stimare o calcolare

Le quantità non condizionate richieste sono:

$$
\mathbb{E}[S],
\qquad
\mathbb{P}(S>0),
\qquad
\mathbb{P}(S>s^\star),
\qquad
q_{\alpha}(S).
$$

Le quantità condizionate richieste sono:

$$
\mathbb{E}[S\mid A_g],
\qquad g=1,2,3.
$$

Il valore atteso condizionato rispetto alla sigma-algebra informativa è:

$$
\mathbb{E}[S\mid\mathcal{G}]
=
\sum_{g=1}^{3}
\mathbb{E}[S\mid A_g]\mathbf{1}_{A_g}.
$$

La proprietà da verificare è la formula del valore atteso totale:

$$
\mathbb{E}[S]
=
\sum_{g=1}^{3}
\mathbb{P}(A_g)\mathbb{E}[S\mid A_g].
$$

Nel notebook, la controparte empirica sarà:

$$
\widehat{\mathbb{E}}[S]
\approx
\sum_{g=1}^{3}
\widehat{\mathbb{P}}(A_g)
\widehat{\mathbb{E}}[S\mid A_g].
$$

Occorre distinguere chiaramente:

1. $\mathbb{E}[S\mid A_g]$, che è un numero;
2. $\mathbb{E}[S\mid\mathcal{G}]$, che è una variabile casuale costante sui blocchi della partizione;
3. $\mathbb{E}[S]$, che è il valore atteso non condizionato.

---

## 11. Output richiesti

### Tabelle

Devono essere prodotte almeno le seguenti tabelle:

1. tabella dei parametri economico-finanziari;
2. tabella degli eventi $A_1,A_2,A_3$ e delle probabilità;
3. tabella dei parametri condizionati $(\mu_g,\sigma_g)$;
4. tabella delle soglie implicite del prezzo dell’energia;
5. tabella delle frequenze simulate degli eventi;
6. tabella di controllo delle statistiche empiriche di $P_E\mid A_g$;
7. tabella descrittiva del prezzo dell’energia $P_E$;
8. tabella descrittiva del margine operativo $M$;
9. tabella descrittiva dello shortfall $S$:
   - media;
   - deviazione standard;
   - minimo;
   - massimo;
   - quantili principali;
10. tabella delle probabilità:
   - $\widehat{\mathbb{P}}(S>0)$;
   - $\widehat{\mathbb{P}}(S>s^\star)$;
11. tabella delle medie condizionate:
   - $\widehat{\mathbb{E}}[S\mid A_1]$;
   - $\widehat{\mathbb{E}}[S\mid A_2]$;
   - $\widehat{\mathbb{E}}[S\mid A_3]$;
12. tabella di verifica della formula del valore atteso totale.

È possibile aggiungere una tabella finale con evento simulato, $P_E$, $C_E$, $M$, $S$ e valore della variabile a gradini $\widehat{\mathbb{E}}[S\mid\mathcal{G}]$.

### Grafici

Devono essere prodotti grafici con funzione interpretativa, non puramente decorativa.

Sono richiesti almeno:

1. istogramma o densità empirica del prezzo dell’energia $P_E$;
2. istogramma o densità empirica del margine operativo $M$;
3. istogramma o densità empirica dello shortfall $S$;
4. grafico della distribuzione empirica di $S$ con evidenza della soglia $s^\star$;
5. grafico delle medie condizionate $\widehat{\mathbb{E}}[S\mid A_g]$;
6. confronto tra distribuzioni condizionate dello shortfall.

Sono facoltativi:

1. confronto tra distribuzioni condizionate del prezzo $P_E$;
2. grafico della massa in zero dello shortfall;
3. ECDF dello shortfall.

---

## 12. Controlli richiesti

### Controlli numerici

Il notebook deve verificare che:

1. le probabilità degli eventi sommino a uno;
2. le frequenze empiriche degli eventi siano coerenti con le probabilità teoriche;
3. ogni evento abbia numerosità sufficiente;
4. le medie e deviazioni standard empiriche di $P_E\mid A_g$ siano coerenti con $\mu_g,\sigma_g$;
5. sia controllata l’eventuale presenza di valori negativi di $P_E$;
6. il costo energetico rispetti la relazione $C_E=Q_E P_E$;
7. il margine rispetti la relazione $M=G_0-Q_E P_E$;
8. lo shortfall rispetti la relazione $S=(m^\star-M)^+$;
9. lo shortfall sia sempre non negativo;
10. la probabilità $\widehat{\mathbb{P}}(S>0)$ sia coerente con la soglia implicita $P_E>120$;
11. la probabilità $\widehat{\mathbb{P}}(S>s^\star)$ sia coerente con la soglia implicita $P_E>140$;
12. la media globale di $S$ coincida, salvo arrotondamenti, con la media pesata delle medie condizionate;
13. i quantili rispettino l’ordinamento atteso;
14. la media si collochi tra minimo e massimo campionario.

### Controlli logici

Il notebook deve mantenere distinte le seguenti nozioni:

1. gli eventi $A_1,A_2,A_3$ sono blocchi informativi della partizione, non valori del prezzo o dello shortfall;
2. $P_E$ è il fattore di rischio;
3. $C_E$ è il costo energetico derivato dal prezzo;
4. $M$ è il margine operativo dopo il costo energetico;
5. $S$ è lo shortfall di margine e non può essere negativo;
6. $\mathbb{E}[S\mid A_g]$ è un numero;
7. $\mathbb{E}[S\mid\mathcal{G}]$ è una variabile casuale costante sui blocchi della partizione;
8. la formula del valore atteso totale non implica che $\mathbb{E}[S]$ ed $\mathbb{E}[S\mid\mathcal{G}]$ coincidano come oggetti;
9. la verifica campionaria della media ricomposta deve essere distinta dalla proprietà teorica.

### Controlli interpretativi

L’interpretazione finale deve rispettare almeno questi punti:

1. l’evento $A_3$ deve essere letto come il regime con shortfall atteso maggiore;
2. l’evento $A_1$ può produrre shortfall nullo o molto contenuto in molte simulazioni;
3. l’evento $A_2$ rappresenta una situazione intermedia;
4. la massa in zero dello shortfall, se visibile, deve essere collegata alla definizione $S=(m^\star-M)^+$;
5. l’informazione della partizione non elimina l’incertezza, ma modifica la distribuzione condizionata rilevante;
6. la probabilità $\mathbb{P}(S>0)$ misura il rischio di non raggiungere il margine minimo;
7. la probabilità $\mathbb{P}(S>s^\star)$ misura il rischio di shortfall severo;
8. la simulazione non deve essere interpretata come previsione del prezzo dell’energia.

---

## 13. Ipotesi del modello

### Ipotesi principali

1. L’impresa è rappresentata da una contribuzione operativa netta non energetica $G_0$ e da un fabbisogno energetico $Q_E$.
2. L’unica fonte di incertezza modellata è il prezzo unitario dell’energia $P_E$.
3. Il costo energetico totale è proporzionale al prezzo unitario: $C_E=Q_E P_E$.
4. Il margine operativo è dato da $M=G_0-Q_E P_E$.
5. Lo shortfall è definito come $S=(m^\star-M)^+$.
6. L’informazione disponibile è rappresentata dalla partizione $\{A_1,A_2,A_3\}$.
7. Condizionatamente a ciascun evento $A_g$, il prezzo dell’energia segue una distribuzione normale.
8. Gli eventi $A_1,A_2,A_3$ costituiscono una partizione dello spazio degli esiti.
9. La simulazione Monte Carlo approssima quantità teoriche mediante frequenze e medie empiriche.

### Ipotesi semplificatrici

1. Non si modellano ricavi aleatori.
2. Non si modellano costi non energetici aleatori.
3. Non si considera elasticità della produzione rispetto al prezzo dell’energia.
4. Non si considera possibilità di trasferire i maggiori costi sui prezzi di vendita.
5. Non si considerano contratti di copertura energetica.
6. Non si considerano politiche di acquisto a termine.
7. Non si considera dinamica multiperiodale.
8. Non si stimano parametri da dati reali.
9. Non si impone positività al prezzo simulato mediante distribuzioni troncate.
10. Non si modellano correlazioni con altre variabili macroeconomiche.

---

## 14. Uso dell’IA e documentazione del lavoro

Per l’uso dell’IA lo studente deve fare riferimento al documento:

**Istruzioni per lo studente — Uso virtuoso dell’IA nei casi applicativi MQF**

In particolare, devono essere rispettati:

1. la sequenza obbligatoria Prompt zero, Prompt 1, Prompt 2, Prompt 3 e prompt di tappa;
2. la distinzione tra Regime A, Regime B e Regime C;
3. il vincolo che la Scheda Caso non deve essere modificata dall’IA;
4. la necessità di documentare l’interazione con l’IA mediante stampa PDF della chat;
5. l’obbligo di mantenere nella chat solo interazioni pertinenti al caso.

La presente Scheda Caso contiene la specifica vincolante del problema.  
Gli esempi di prompt, i criteri di uso dell’IA e la tabella indicativa di valutazione sono riportati nel documento di istruzioni per lo studente.