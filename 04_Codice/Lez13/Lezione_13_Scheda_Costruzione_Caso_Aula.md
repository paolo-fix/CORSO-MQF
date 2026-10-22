# Scheda Costruzione Caso Applicativo

Documento interno di progettazione docente. Compilazione riferita al **Caso Aula** della Lezione 13.

## 1. Identificazione del caso

- **Lezione:** 13 — Applicazione in Python: programmazione lineare e ALM deterministico
- **Tipo di caso:** Aula
- **Titolo:** **Silicon Valley Bank 2023 — piano ALM, sensitività e scenari di stress**
- **Destinatari:** studenti del secondo anno del Corso di Laurea Magistrale in Finanza e Risk Management
- **Uso previsto:** caso applicativo guidato per tradurre in Python il modello di programmazione lineare e ALM deterministico sviluppato nei Capitoli 11 e 12, validarne la soluzione mediante solver e studiare come il piano ottimo reagisce a variazioni del fabbisogno di liquidità, della capacità massima di funding e del costo del funding.

## 2. Contesto e motivazione

Il caso riprende il modello SVB stilizzato sviluppato nei Capitoli 11 e 12 e ne costituisce l'estensione computazionale.

Il riferimento finanziario è la crisi di Silicon Valley Bank del marzo 2023, nella quale l'interazione fra struttura dell'attivo, rialzo dei tassi, concentrazione della raccolta, deflussi di depositi e capacità di reperire liquidità rese centrale non soltanto l'ammontare complessivo delle risorse disponibili, ma soprattutto la loro distribuzione temporale.

Il caso non costituisce una ricostruzione del bilancio storico di SVB. La calibrazione è didattica e utilizza il modello già introdotto nel Capitolo 12. Il riferimento storico serve a motivare economicamente tre possibili fonti di tensione:

1. aumento dei fabbisogni di liquidità, rappresentato dal parametro $\theta$;
2. riduzione della capacità massima di funding, rappresentata dal parametro $\phi$;
3. aumento del costo del funding, rappresentato dal parametro $\psi$.

La struttura dell'analisi è articolata in quattro momenti distinti:

1. **benchmark:** implementazione e validazione del modello del Capitolo 12;
2. **sensitività univariata:** variazione separata di $\theta$, $\phi$ e $\psi$;
3. **frontiera di fattibilità:** approfondimento specifico dell'effetto di $\theta$;
4. **scenario analysis:** variazione congiunta di $\theta$, $\phi$ e $\psi$ in tre scenari economicamente coerenti.

La sequenza didattica è:

$$
\text{modello teorico}
\longrightarrow
\text{forma solver}
\longrightarrow
\text{benchmark}
\longrightarrow
\text{sensitività}
\longrightarrow
\text{frontiera}
\longrightarrow
\text{scenari}.
$$

L'obiettivo non è soltanto osservare come cambia il valore ottimo, ma comprendere come cambia la politica ottima: composizione dell'attivo, uso del funding, giacenze di liquidità, vincoli attivi e valori marginali.

## 3. Domanda quantitativa e funzione didattica

**Domanda quantitativa:**  
dato il modello ALM deterministico di Silicon Valley Bank sviluppato nei Capitoli 11 e 12, come si traduce correttamente il problema nella forma richiesta da un solver di programmazione lineare e come cambiano il valore ottimo e il piano ALM al variare, separatamente e congiuntamente, del fabbisogno di liquidità, della capacità massima di funding e del costo del funding? Fino a quale livello di aumento dei fabbisogni iniziali il problema resta ammissibile?

**Obiettivo didattico:**  
portare lo studente a:

1. tradurre un modello ALM deterministico in vettori, matrici, uguaglianze, disuguaglianze e bounds compatibili con un solver di programmazione lineare;
2. distinguere la formulazione economico-finanziaria del problema dalla sua rappresentazione computazionale;
3. gestire correttamente il passaggio dalla massimizzazione della funzione obiettivo alla convenzione di minimizzazione utilizzata dal solver;
4. risolvere e validare numericamente la configurazione benchmark;
5. interpretare residuali, slack, bounds attivi e valori marginali;
6. costruire una funzione parametrica di soluzione dipendente da $\theta$, $\phi$ e $\psi$;
7. distinguere tra sensitività univariata, stress test di fattibilità e scenario analysis multivariata;
8. analizzare non soltanto il valore ottimo $\Pi^*$, ma anche la composizione ottima dell'attivo, le giacenze di liquidità e l'utilizzo del funding;
9. riconoscere eventuali cambiamenti di regime nella soluzione del programma lineare;
10. collegare gli output computazionali alla logica economico-finanziaria dell'Asset--Liability Management.

**Collegamento con le lezioni teoriche precedenti:**  
il caso utilizza direttamente i risultati sviluppati nei Capitoli 11 e 12.

Dal Capitolo 11 riprende:

- la formulazione di un problema di programmazione lineare;
- la distinzione tra funzione obiettivo, vincoli e bounds;
- la nozione di regione ammissibile;
- il ruolo dei vincoli attivi;
- la sensitività locale della soluzione;
- la dualità e l'interpretazione economica dei valori marginali.

Dal Capitolo 12 riprende:

- la distinzione tra liquidità aggregata e liquidità disponibile alle diverse scadenze;
- la matrice dei cash flow degli attivi;
- i bilanci temporali di liquidità;
- le giacenze trasferite tra date successive;
- il ricorso a funding esterno e il relativo rimborso;
- i vincoli di capacità del funding;
- l'interpretazione dei valori marginali associati ai bilanci temporali e ai vincoli di liquidità.

Il Capitolo 13 costituisce il riferimento computazionale immediato: non introduce una nuova classe di modelli, ma rende operativo il modello ALM deterministico costruito nei capitoli precedenti traducendolo nella forma richiesta da `scipy.optimize.linprog`.

**Concetti teorici da rendere osservabili:**  
il caso deve rendere operativamente osservabili:

1. la corrispondenza tra formulazione economico-finanziaria e forma matriciale del programma lineare;
2. la distinzione tra vincoli di uguaglianza, vincoli di disuguaglianza e bounds;
3. la fattibilità della soluzione e il significato dei residuali;
4. il significato degli slack e l'identificazione dei vincoli attivi;
5. il ruolo dei bounds attivi sulle variabili;
6. l'interpretazione dei valori marginali restituiti dal solver;
7. la dipendenza della soluzione ottima dai parametri del modello;
8. la differenza tra variazione locale della soluzione, sensitività su griglia e cambiamento di regime;
9. il passaggio da soluzione ammissibile a problema non ammissibile;
10. la differenza tra sensitività univariata e scenario analysis con variazione congiunta dei driver.

**Funzione della procedura computazionale:**  
il ricorso a Python e al solver è necessario perché il caso richiede di risolvere ripetutamente lo stesso programma lineare al variare dei parametri $\theta$, $\phi$ e $\psi$.

La procedura computazionale deve consentire di:

1. costruire in modo riproducibile la forma solver del modello;
2. risolvere la configurazione benchmark;
3. verificare automaticamente fattibilità, residuali, slack e bounds attivi;
4. estrarre i valori marginali restituiti dal solver;
5. risolvere il modello lungo griglie parametrizzate;
6. confrontare sistematicamente le diverse configurazioni;
7. individuare la frontiera di fattibilità rispetto a $\theta$;
8. analizzare scenari nei quali i tre driver cambiano congiuntamente.

La funzione computazionale non deve sostituire l'interpretazione teorica: serve a rendere osservabili, confrontabili e verificabili proprietà del modello già definite nella specifica matematica.

**Ruolo dell'informazione, degli scenari e dei vincoli:**  
il caso è interamente deterministico. Non sono presenti variabili casuali né scenari probabilistici.

Per ciascuna configurazione di $(\theta,\phi,\psi)$, coefficienti, cash flow, fabbisogni e capacità di funding sono considerati noti.

I tre parametri svolgono ruoli distinti:

- $\theta$ modifica i fabbisogni di liquidità delle prime due date;
- $\phi$ modifica la capacità massima di funding;
- $\psi$ modifica il costo del funding e, di conseguenza, anche l'ammontare da rimborsare alla data successiva.

Le sensitività univariate modificano un solo parametro alla volta, mantenendo gli altri al valore benchmark.

La scenario analysis modifica invece congiuntamente $\theta$, $\phi$ e $\psi$ secondo configurazioni assegnate. Tali configurazioni non rappresentano stati aleatori e non hanno probabilità associate.

I vincoli svolgono una funzione centrale nell'interpretazione economica del caso: i bilanci temporali garantiscono la disponibilità di liquidità alle diverse date; il limite prudenziale e il limite di concentrazione restringono la composizione dell'attivo; i bounds sul funding rappresentano la capacità massima di reperire risorse esterne. L'analisi degli slack, dei bounds attivi e dei valori marginali deve permettere di identificare quali restrizioni determinano effettivamente il piano ALM ottimo nelle diverse configurazioni.

## 4. Specifica teorico-matematica

### Grandezze e variabili

- $x_j$, $j=1,\ldots,4$: ammontare inizialmente allocato nelle quattro classi di attivo:
  1. cassa e riserve;
  2. titoli a breve scadenza;
  3. titoli a lunga scadenza;
  4. prestiti e impieghi meno liquidi;

- $g_t$, $t=1,\ldots,4$: giacenza di liquidità immediatamente successiva al soddisfacimento del fabbisogno alla data $t$;

- $u_t$, $t=1,2,3$: funding esterno raccolto alla data $t$, disponibile immediatamente e da rimborsare alla data successiva;

- $c_j$: coefficiente di redditività dell'attivo $j$;

- $\ell_j$: perdita unitaria sotto stress associata all'attivo $j$;

- $a_{tj}$: quota di una unità dell'attivo $j$ resa liquida alla data $t$;

- $d_t$: fabbisogno di liquidità benchmark alla data $t$;

- $r_t^g$: rendimento della giacenza trasferita dalla data $t$ alla data $t+1$;

- $r_t^u$: costo benchmark del funding raccolto alla data $t$;

- $\bar u_t$: capacità benchmark di funding alla data $t$;

- $\theta$: moltiplicatore dei fabbisogni di liquidità delle prime due date;

- $\phi$: moltiplicatore della capacità massima di funding;

- $\psi$: moltiplicatore del costo del funding.

### Eventi, informazione, stati o scenari

Il caso è deterministico e non prevede variabili casuali, stati informativi aleatori o probabilità associate agli scenari.

La configurazione benchmark è:

$$
(\theta,\phi,\psi)=(1,1,1).
$$

La sensitività rispetto a $\theta$, mantenendo $\phi=1$ e $\psi=1$, utilizza:

$$
\theta\in\{1.00,1.01,\ldots,1.10\}.
$$

La sensitività rispetto a $\phi$, mantenendo $\theta=1$ e $\psi=1$, utilizza:

$$
\phi\in\{0.50,0.60,0.70,0.80,0.90,1.00,1.10,1.20,1.30,1.40,1.50\}.
$$

La sensitività rispetto a $\psi$, mantenendo $\theta=1$ e $\phi=1$, utilizza:

$$
\psi\in\{0.50,0.75,1.00,1.25,1.50,1.75,2.00\}.
$$

Gli scenari congiunti assegnati sono:

- scenario Standard:

$$
(\theta,\phi,\psi)=(1.00,1.00,1.00);
$$

- scenario Mediamente critico:

$$
(\theta,\phi,\psi)=(1.03,0.90,1.25);
$$

- scenario Critico:

$$
(\theta,\phi,\psi)=(1.06,0.70,1.50).
$$

Gli scenari rappresentano configurazioni deterministiche dei parametri e non eventi ai quali siano associate probabilità.

### Parametri e dati

Le risorse iniziali sono:

$$
A_0=100.
$$

Il vettore dei coefficienti di redditività è:

$$
c'=(0.010,0.025,0.040,0.050).
$$

Il vettore delle perdite unitarie sotto stress è:

$$
\ell'=(0,0.02,0.15,0.08).
$$

La matrice dei cash flow è:

$$
A^{\mathrm{CF}}
=
\begin{pmatrix}
1.00 & 0.65 & 0.05 & 0.05\\
0.00 & 0.35 & 0.10 & 0.15\\
0.00 & 0.00 & 0.25 & 0.30\\
0.00 & 0.00 & 0.60 & 0.50
\end{pmatrix}.
$$

Le righe corrispondono alle date $t=1,\ldots,4$ e le colonne, nell'ordine, alle variabili $(x_1,x_2,x_3,x_4)$.

I fabbisogni benchmark sono:

$$
d'=(30,30,22,15).
$$

I rendimenti delle giacenze sono:

$$
{r^g}'=(0.005,0.006,0.007).
$$

I costi benchmark del funding sono:

$$
{r^u}'=(0.015,0.020,0.025).
$$

Le capacità benchmark di funding sono:

$$
\bar u'=(10,8,6).
$$

Il limite prudenziale è:

$$
K=7.
$$

Il limite ai titoli a lunga scadenza è:

$$
x_3\leq30.
$$

### Ipotesi modellistiche

Il caso assume:

1. orizzonte deterministico a quattro date;
2. coefficienti, cash flow e fabbisogni noti per ogni configurazione parametrica;
3. divisibilità delle quantità;
4. assenza di costi fissi;
5. linearità della funzione obiettivo e dei vincoli per ciascuna configurazione assegnata di $\theta$, $\phi$ e $\psi$;
6. funding disponibile soltanto entro i limiti assegnati;
7. effetto di $\theta$ limitato ai fabbisogni delle prime due date;
8. variazione proporzionale della capacità massima di funding con $\phi$;
9. variazione proporzionale del costo del funding con $\psi$;
10. variazione di un solo parametro alla volta nelle sensitività univariate;
11. variazione congiunta dei tre parametri nella scenario analysis;
12. assenza di probabilità associate agli scenari;
13. natura stilizzata e didattica del caso, che non costituisce una ricostruzione quantitativa del bilancio storico di Silicon Valley Bank.

### Formule vincolanti

I fabbisogni parametrizzati sono:

$$
d(\theta)
=
(30\theta,30\theta,22,15)'.
$$

La capacità massima di funding è:

$$
\bar u_t(\phi)
=
\phi\bar u_t.
$$

Il costo del funding è:

$$
r_t^u(\psi)
=
\psi r_t^u.
$$

La funzione obiettivo è:

$$
\max_{x,g,u}
\Pi(x,g,u;\psi)
=
c'x
+
\sum_{t=1}^{3}r_t^g g_t
-
\sum_{t=1}^{3}\psi r_t^u u_t.
$$

Il vincolo sulle risorse iniziali è:

$$
\sum_{j=1}^{4}x_j=A_0.
$$

Il primo bilancio temporale è:

$$
a_1'x+u_1-g_1=d_1(\theta).
$$

I bilanci intermedi, per $t=2,3$, sono:

$$
a_t'x
+
(1+r_{t-1}^g)g_{t-1}
+
u_t
-
(1+\psi r_{t-1}^u)u_{t-1}
-
g_t
=
d_t(\theta).
$$

Il bilancio terminale è:

$$
a_4'x
+
(1+r_3^g)g_3
-
(1+\psi r_3^u)u_3
-
g_4
=
d_4.
$$

Il vincolo prudenziale è:

$$
\ell'x\leq K.
$$

Il limite di concentrazione è:

$$
x_3\leq30.
$$

I limiti di funding sono:

$$
0\leq u_t\leq\phi\bar u_t,
\qquad
t=1,2,3.
$$

Le condizioni di non negatività sono:

$$
x_j\geq0,
\qquad
j=1,\ldots,4,
$$

e:

$$
g_t\geq0,
\qquad
t=1,\ldots,4.
$$

### Quantità teoriche da stimare o calcolare

Devono essere determinate:

1. la soluzione ottima benchmark $x^*$, $g^*$ e $u^*$;
2. il valore ottimo $\Pi^*$;
3. i residuali dei vincoli di uguaglianza;
4. gli slack dei vincoli di disuguaglianza;
5. i bounds attivi;
6. i principali valori marginali restituiti dal solver;
7. l'evoluzione di $\Pi^*$ lungo le griglie di $\theta$, $\phi$ e $\psi$;
8. l'evoluzione di $x^*$, $g^*$ e $u^*$ lungo le tre griglie;
9. il rapporto di utilizzo della capacità di funding:

$$
\rho_t^u(p)
=
\frac{u_t^*(p)}{\bar u_t(p)};
$$

10. la variazione del valore ottimo rispetto al benchmark:

$$
\Delta\Pi^*(p)
=
\Pi^*(p)-\Pi^*(1);
$$

11. la variazione percentuale del valore ottimo:

$$
\Delta_{\%}\Pi^*(p)
=
100
\left[
\frac{\Pi^*(p)}{\Pi^*(1)}-1
\right];
$$

12. le variazioni delle componenti ottime:

$$
\Delta x_j^*(p)
=
x_j^*(p)-x_j^*(1),
$$

$$
\Delta g_t^*(p)
=
g_t^*(p)-g_t^*(1),
$$

$$
\Delta u_t^*(p)
=
u_t^*(p)-u_t^*(1);
$$

13. l'ultimo valore ammissibile della griglia di $\theta$;
14. il primo valore non ammissibile della stessa griglia;
15. un intervallo raffinato contenente $\theta_{\mathrm{crit}}$;
16. le soluzioni ottime nei tre scenari congiunti;
17. la perdita di valore di ciascuno scenario rispetto allo scenario Standard.

### Proprietà teoriche da verificare

Il caso deve verificare esplicitamente:

1. la fattibilità numerica della soluzione benchmark;
2. la soddisfazione dei bilanci temporali di liquidità;
3. la coerenza tra residuali numerici e vincoli di uguaglianza;
4. la coerenza tra slack e stato attivo o non attivo dei vincoli di disuguaglianza;
5. la coerenza tra valore delle variabili e bounds attivi;
6. il rispetto dei limiti di funding:

$$
u_t^*\leq\phi\bar u_t;
$$

7. il rispetto del vincolo prudenziale:

$$
\ell'x^*\leq K;
$$

8. il rispetto del limite di concentrazione:

$$
x_3^*\leq30;
$$

9. la coerenza dei valori marginali con i vincoli e i bilanci ai quali si riferiscono;
10. la corretta distinzione tra configurazioni ammissibili e non ammissibili;
11. la coerenza tra variazioni parametriche, eventuali cambiamenti dei vincoli attivi e modifiche della soluzione ottima;
12. la distinzione tra sensitività univariata e variazione congiunta dei parametri negli scenari.

### Soglie, target o vincoli rilevanti

Le principali soglie e condizioni di ammissibilità sono:

- risorse iniziali:

$$
\sum_{j=1}^{4}x_j=100;
$$

- limite prudenziale:

$$
\ell'x\leq7;
$$

- limite di concentrazione:

$$
x_3\leq30;
$$

- capacità massime benchmark di funding:

$$
\bar u'=(10,8,6),
$$

modificate mediante $\phi$;

- non negatività di $x$, $g$ e $u$;

- frontiera di fattibilità rispetto a $\theta$, individuata attraverso il passaggio tra l'ultimo valore ammissibile e il primo valore non ammissibile e successivamente raffinata.

### Quantità finali di interesse

Le quantità finali da utilizzare nell'interpretazione sono:

1. valore ottimo e composizione del piano ALM benchmark;
2. struttura delle giacenze e del funding;
3. vincoli e bounds attivi;
4. valori marginali economicamente informativi;
5. risposta del piano ottimo a variazioni di $\theta$, $\phi$ e $\psi$;
6. cambiamenti di regime nella soluzione;
7. grado di utilizzo della capacità di funding;
8. frontiera di fattibilità rispetto allo stress sui fabbisogni;
9. confronto tra gli scenari Standard, Mediamente critico e Critico.

### Limiti del modello

Il modello:

1. è deterministico;
2. non attribuisce probabilità agli scenari;
3. assume coefficienti e cash flow noti;
4. mantiene invariata la struttura del modello all'interno di ciascuna analisi parametrica;
5. non rappresenta costi fissi, non linearità o altre frizioni non previste dalla specifica;
6. utilizza una calibrazione didattica e stilizzata;
7. non costituisce una ricostruzione storica del bilancio di Silicon Valley Bank;
8. non consente di interpretare $\theta_{\mathrm{crit}}$ come stima empirica della soglia effettiva di deflusso di SVB;
9. consente di interpretare i risultati soltanto nell'ambito delle ipotesi, dei parametri e dei vincoli esplicitamente assegnati.

## 5. Output richiesti

Gli output devono avere una funzione informativa, diagnostica o interpretativa esplicita e devono essere collegati alle quantità teoriche definite nella specifica del caso.

Devono essere costruiti esclusivamente a partire da configurazioni per le quali il solver restituisce una soluzione valida.

### Stime o risultati numerici

Devono essere prodotti almeno i seguenti risultati:

1. soluzione ottima benchmark:
   - $x^*$;
   - $g^*$;
   - $u^*$;

2. valore ottimo benchmark:

$$
\Pi^*;
$$

3. residuali dei vincoli di uguaglianza;

4. slack dei vincoli di disuguaglianza;

5. bounds attivi;

6. principali valori marginali restituiti dal solver;

7. risultati delle sensitività univariate rispetto a:

$$
\theta,
\qquad
\phi,
\qquad
\psi;
$$

8. variazioni assolute del valore ottimo:

$$
\Delta\Pi^*(p)
=
\Pi^*(p)-\Pi^*(1);
$$

9. variazioni percentuali del valore ottimo:

$$
\Delta_{\%}\Pi^*(p)
=
100
\left[
\frac{\Pi^*(p)}{\Pi^*(1)}-1
\right];
$$

10. variazioni delle componenti della soluzione:

$$
\Delta x_j^*(p)
=
x_j^*(p)-x_j^*(1),
$$

$$
\Delta g_t^*(p)
=
g_t^*(p)-g_t^*(1),
$$

$$
\Delta u_t^*(p)
=
u_t^*(p)-u_t^*(1);
$$

11. rapporto di utilizzo della capacità di funding:

$$
\rho_t^u(p)
=
\frac{u_t^*(p)}{\bar u_t(p)};
$$

12. stato di fattibilità per ciascuna configurazione parametrica;

13. principali vincoli e bounds attivi nelle diverse configurazioni;

14. ultimo valore ammissibile e primo valore non ammissibile della griglia di $\theta$;

15. intervallo raffinato contenente:

$$
\theta_{\mathrm{crit}};
$$

16. soluzioni ottime nei tre scenari congiunti;

17. perdita di valore degli scenari Mediamente critico e Critico rispetto allo scenario Standard:

$$
L_s
=
\Pi_{\mathrm{Standard}}^*
-
\Pi_s^*.
$$

### Tabelle

Devono essere prodotte le seguenti tabelle.

1. **Tabella 1 — Parametri benchmark**

   Deve riportare almeno:

   - $A_0$;
   - $c$;
   - $\ell$;
   - $d$;
   - $r^g$;
   - $r^u$;
   - $\bar u$;
   - $K$;
   - limite su $x_3$.

   La funzione della tabella è rendere verificabile la configurazione benchmark utilizzata dal solver.

2. **Tabella 2 — Soluzione benchmark**

   Deve riportare:

   - $x_1^*,\ldots,x_4^*$;
   - $g_1^*,\ldots,g_4^*$;
   - $u_1^*,u_2^*,u_3^*$;
   - $\Pi^*$.

   La funzione della tabella è sintetizzare il piano ALM ottimo benchmark.

3. **Tabella 3 — Verifica dei bilanci temporali**

   Per ciascuna data deve riportare almeno:

   - cash flow degli attivi;
   - giacenza proveniente dalla data precedente, quando presente;
   - funding raccolto, quando presente;
   - rimborso del funding precedente, quando presente;
   - fabbisogno;
   - giacenza finale;
   - residuo dell'uguaglianza.

   La funzione della tabella è verificare direttamente i bilanci temporali di liquidità.

4. **Tabella 4 — Vincoli, bounds e slack benchmark**

   Per ciascun vincolo o bound rilevante deve riportare:

   - valore assunto;
   - limite;
   - slack o distanza dal bound;
   - stato attivo / non attivo.

   La funzione della tabella è rendere osservabile quali restrizioni risultano determinanti nel benchmark.

5. **Tabella 5 — Valori marginali benchmark**

   Deve riportare almeno i valori marginali economicamente informativi relativi:

   - ai bilanci temporali;
   - ai limiti di funding;
   - agli altri vincoli rilevanti quando il solver ne fornisce un marginale interpretabile.

   La funzione della tabella è collegare la soluzione numerica all'interpretazione marginale dei vincoli.

6. **Tabella 6 — Sensitività a $\theta$**

   Per ciascun valore della griglia deve riportare almeno:

   - $\theta$;
   - stato del solver;
   - fattibilità;
   - $\Pi^*$;
   - $\Delta\Pi^*$;
   - $\Delta_{\%}\Pi^*$;
   - $x^*$;
   - $g^*$;
   - $u^*$;
   - rapporti di utilizzo della capacità di funding;
   - principali vincoli attivi.

   La funzione della tabella è rendere osservabile come cambia il piano ALM quando aumenta il fabbisogno di liquidità iniziale.

7. **Tabella 7 — Sensitività a $\phi$**

   Deve avere struttura analoga alla Tabella 6, sostituendo $\theta$ con $\phi$ e mettendo in evidenza il ruolo della capacità disponibile di funding.

8. **Tabella 8 — Sensitività a $\psi$**

   Deve avere struttura analoga alla Tabella 6, sostituendo $\theta$ con $\psi$ e mettendo in evidenza l'effetto del costo del funding sul valore ottimo e sul ricorso al funding.

9. **Tabella 9 — Raffinamento della frontiera di fattibilità**

   Deve riportare:

   - valori raffinati di $\theta$;
   - stato del solver;
   - fattibilità.

   La funzione della tabella è individuare un intervallo ristretto contenente:

$$
\theta_{\mathrm{crit}}.
$$

10. **Tabella 10 — Confronto degli scenari**

   Deve confrontare Standard, Mediamente critico e Critico riportando almeno:

   - $\theta$;
   - $\phi$;
   - $\psi$;
   - fattibilità;
   - $\Pi^*$;
   - perdita rispetto allo Standard;
   - $x^*$;
   - $g^*$;
   - $u^*$;
   - principali vincoli attivi;
   - utilizzo relativo della capacità di funding.

   La funzione della tabella è confrontare configurazioni nelle quali i tre driver cambiano congiuntamente.

### Grafici

Devono essere prodotti i seguenti grafici.

1. **Figura 1 — Valore ottimo e sensitività a $\theta$**

   Rappresentare:

$$
\theta
\longmapsto
\Pi^*(\theta).
$$

   Devono essere rappresentati soltanto i punti corrispondenti a configurazioni ammissibili.

2. **Figura 2 — Variazione del valore ottimo rispetto a $\theta$**

   Rappresentare:

$$
\theta
\longmapsto
\Delta\Pi^*(\theta)
$$

   oppure la corrispondente variazione percentuale.

3. **Figura 3 — Composizione ottima dell'attivo rispetto a $\theta$**

   Rappresentare:

$$
x_1^*(\theta),\ldots,x_4^*(\theta).
$$

4. **Figura 4 — Variazioni dell'asset allocation rispetto al benchmark**

   Rappresentare:

$$
\Delta x_j^*(\theta).
$$

5. **Figura 5 — Funding ottimo e utilizzo della capacità rispetto a $\theta$**

   Rappresentare $u_t^*(\theta)$ e/o:

$$
\frac{u_t^*(\theta)}{\bar u_t}.
$$

6. **Figura 6 — Giacenze ottime rispetto a $\theta$**

   Rappresentare:

$$
g_1^*(\theta),\ldots,g_4^*(\theta).
$$

7. **Figura 7 — Sensitività a $\phi$**

   Rappresentare almeno:

$$
\phi
\longmapsto
\Pi^*(\phi)
$$

   e il comportamento del funding rispetto alla capacità disponibile.

8. **Figura 8 — Sensitività a $\psi$**

   Rappresentare almeno:

$$
\psi
\longmapsto
\Pi^*(\psi)
$$

   e l'evoluzione del funding ottimo.

9. **Figura 9 — Valori marginali**

   Rappresentare i valori marginali dei bilanci temporali e/o dei limiti di funding più informativi lungo almeno una delle griglie.

10. **Figura 10 — Mappa dei principali vincoli attivi**

   Rendere visibile il cambiamento dello stato attivo / non attivo dei principali vincoli almeno lungo la sensitività a $\theta$.

11. **Figura 11 — Valore ottimo nei tre scenari**

   Confrontare:

$$
\Pi_{\mathrm{Standard}}^*,
\qquad
\Pi_{\mathrm{Medio}}^*,
\qquad
\Pi_{\mathrm{Critico}}^*.
$$

12. **Figura 12 — Composizione ottima dell'attivo nei tre scenari**

   Confrontare:

$$
x_1^*,x_2^*,x_3^*,x_4^*.
$$

13. **Figura 13 — Funding nei tre scenari**

   Confrontare:

$$
u_1^*,u_2^*,u_3^*.
$$

14. **Figura 14 — Profilo temporale delle giacenze nei tre scenari**

   Per ogni scenario rappresentare:

$$
t
\longmapsto
g_t^*,
\qquad
t=1,\ldots,4.
$$

I grafici devono essere prodotti come output delle rispettive celle del notebook e devono essere rigenerabili mediante riesecuzione delle celle.

Non è richiesta automaticamente l'esportazione in file esterni.

### Controlli

Devono essere previsti ed eseguiti almeno i seguenti controlli.

#### Controlli numerici

1. verifica dei residuali dei vincoli di uguaglianza;
2. verifica degli slack delle disuguaglianze;
3. verifica dei bounds attivi;
4. controllo del vincolo prudenziale:

$$
\ell'x^*\leq7;
$$

5. controllo del limite:

$$
x_3^*\leq30;
$$

6. controllo dei limiti di funding:

$$
0\leq u_t^*\leq\phi\bar u_t;
$$

7. controllo della non negatività di tutte le variabili;
8. verifica dello stato di fattibilità per ogni configurazione parametrica e per ogni scenario.

#### Controlli logici e teorici

1. verifica che nelle sensitività univariate vari un solo parametro alla volta;
2. verifica della corretta distinzione tra sensitività univariata, stress test di fattibilità e scenario analysis;
3. verifica della coerenza tra slack, bounds e classificazione attivo / non attivo;
4. verifica della coerenza tra variazioni dei parametri, cambiamenti dei vincoli attivi e modifiche della soluzione ottima;
5. verifica della corretta interpretazione economica dei principali valori marginali;
6. verifica che $\theta_{\mathrm{crit}}$ sia interpretato esclusivamente come frontiera di fattibilità del modello stilizzato.

#### Controlli computazionali

1. verifica della corretta costruzione di $A_{\mathrm{eq}}$, $b_{\mathrm{eq}}$, $A_{\mathrm{ub}}$, $b_{\mathrm{ub}}$ e dei bounds;
2. verifica della corretta trasformazione della funzione obiettivo nella convenzione utilizzata da `scipy.optimize.linprog`;
3. verifica della corretta dipendenza dei fabbisogni da $\theta$;
4. verifica della corretta dipendenza della capacità di funding da $\phi$;
5. verifica che $\psi$ modifichi coerentemente sia il costo del funding nella funzione obiettivo sia il rimborso del funding nei bilanci temporali;
6. verifica mediante perturbazione numerica di almeno un valore marginale;
7. esclusione dall'analisi economica delle configurazioni per le quali il solver segnala non ammissibilità;
8. verifica che tabelle e grafici siano generati esclusivamente a partire da risultati di esecuzioni valide;
9. verifica della riproducibilità degli output mediante riesecuzione ordinata del notebook.

### Funzione interpretativa degli output

Gli output devono consentire allo studente di discutere, sulla base dei risultati numerici già validati:

1. come cambia il piano ALM al variare dei fabbisogni di liquidità;
2. quando la capacità di funding diventa una risorsa scarsa;
3. come il costo del funding modifica la convenienza del suo utilizzo;
4. quali vincoli e bounds determinano il piano ottimo nelle diverse configurazioni;
5. come cambiano composizione dell'attivo, giacenze, funding e valore ottimo;
6. quando si verifica un cambiamento di regime nella soluzione;
7. dove si colloca la frontiera di fattibilità rispetto a $\theta$;
8. come differiscono gli scenari Standard, Mediamente critico e Critico.

L'interpretazione finale resta responsabilità dello studente e deve basarsi esclusivamente su output già validati.

## 6. Flusso logico-teorico risolutivo atteso

Il Flusso logico-teorico deve ricostruire, in forma sintetica, la sequenza concettuale necessaria per passare dalla specifica ALM alla soluzione computazionale e alla successiva interpretazione.

Il Flusso non deve replicare la granularità delle celle del notebook. Deve individuare pochi snodi teorico-operativi, ciascuno dei quali può successivamente articolarsi in più operazioni computazionali.

La sequenza deve precedere la scomposizione operativa in tappe e deve rendere esplicito il collegamento tra:

$$
\text{modello teorico}
\longrightarrow
\text{forma solver}
\longrightarrow
\text{benchmark}
\longrightarrow
\text{analisi parametrica}
\longrightarrow
\text{scenari}
\longrightarrow
\text{interpretazione}.
$$

| Passo | Finalità risolutiva | Formula teorico-matematica / definizione / proprietà | Applicazione nel caso | Output o controllo collegato |
|---:|---|---|---|---|
| 1 | Ricostruire il modello ALM e tradurlo nella forma richiesta dal solver | Programmazione lineare; funzione obiettivo; uguaglianze; disuguaglianze; bounds; equivalenza tra $\max\Pi$ e $\min F=-\Pi$ | Identificare $x$, $g$, $u$ e costruire ordinamento delle variabili, vettore obiettivo, $A_{\mathrm{eq}}$, $b_{\mathrm{eq}}$, $A_{\mathrm{ub}}$, $b_{\mathrm{ub}}$ e bounds | Struttura solver completa; controlli dimensionali, dei coefficienti e dei segni |
| 2 | Risolvere e validare il benchmark, collegando diagnostica e valori marginali | Ammissibilità; ottimalità; residuali; slack; vincoli e bounds attivi; dualità e sensitività locale | Risolvere $(\theta,\phi,\psi)=(1,1,1)$, ricostruire $\Pi^*$, verificare i vincoli e associare i marginali agli oggetti corretti; verificare numericamente almeno un marginale | $x^*$, $g^*$, $u^*$, $\Pi^*$; tabelle benchmark; controllo marginale--perturbazione |
| 3 | Costruire la versione parametrica del modello senza modificarne la struttura | Analisi parametrica di termini noti, bounds e coefficienti | Introdurre $\theta$, $\phi$ e $\psi$ esclusivamente negli elementi previsti dalla Scheda Caso e verificare la riproduzione del benchmark | Funzione solver parametrica; controllo in $(1,1,1)$ |
| 4 | Analizzare lo stress sui fabbisogni e la frontiera di fattibilità | Comparative statics; insieme ammissibile parametrico; passaggio feasible / infeasible | Variare $\theta$ con $\phi=\psi=1$, analizzare soluzione e vincoli attivi, individuare ultimo valore ammissibile e primo non ammissibile e raffinare l'intervallo | Sensitività a $\theta$; tabelle e grafici; intervallo contenente $\theta_{\mathrm{crit}}$ |
| 5 | Analizzare il ruolo della capacità disponibile di funding | Bounds parametrizzati; scarsità di una risorsa vincolata | Variare $\phi$ con $\theta=\psi=1$ modificando esclusivamente i limiti superiori del funding | Sensitività a $\phi$; utilizzo della capacità; bounds attivi; variazioni di $\Pi^*$, $x^*$, $g^*$ e $u^*$ |
| 6 | Analizzare il ruolo del costo del funding | Modifica parametrica dei coefficienti economici e dei rimborsi | Variare $\psi$ con $\theta=\phi=1$ applicandolo sia alla funzione obiettivo sia ai rimborsi del funding | Sensitività a $\psi$; valore ottimo; funding; controllo della doppia applicazione di $\psi$ |
| 7 | Confrontare le sensitività e analizzare gli scenari congiunti | Comparative statics; cambiamenti di regime; scenario analysis deterministica | Confrontare gli effetti separati di $\theta$, $\phi$ e $\psi$ e risolvere Standard, Mediamente critico e Critico | Sintesi comparativa; tabella e grafici degli scenari; perdita rispetto allo Standard |
| 8 | Verificare la coerenza complessiva e delimitare l'interpretazione | Coerenza modello--solver--output; validità locale dei marginali; limiti del modello deterministico | Controllare completezza, riproducibilità, uso esclusivo di risultati validi e distinzione tra risultati del modello e fatti storici | Controlli conclusivi; elementi quantitativi per l'interpretazione finale; richiamo dei limiti del modello |

### 6.1 Logica della sequenza

Il flusso deve rispettare il seguente ordine concettuale:

$$
\text{specifica economica e forma solver}
\longrightarrow
\text{benchmark e diagnostica}
\longrightarrow
\text{marginali}
\longrightarrow
\text{parametrizzazione}
$$

$$
\longrightarrow
\text{sensitività e frontiera}
\longrightarrow
\text{confronto dei driver}
\longrightarrow
\text{scenari}
\longrightarrow
\text{controlli conclusivi}.
$$

La verifica dei valori marginali deve precedere l'analisi parametrica, perché lo studente deve comprenderne e validarne il significato locale prima di utilizzarli nell'interpretazione delle configurazioni successive.

La frontiera di fattibilità rispetto a $\theta$ deve essere ricercata immediatamente dopo la relativa sensitività, poiché deriva direttamente dal passaggio tra configurazioni ammissibili e non ammissibili osservato lungo la stessa griglia.

### 6.2 Relazione con la scomposizione in tappe

La successiva scomposizione operativa deve derivare dal Flusso logico-teorico.

In particolare:

- il Passo 1 alimenta la **Tappa 1 — Traduzione del modello nella forma solver**;
- il Passo 2 alimenta la **Tappa 2 — Benchmark, diagnostica e valori marginali**;
- i Passi 3–4 alimentano la **Tappa 3 — Solver parametrico, sensitività a $\theta$ e frontiera di fattibilità**;
- i Passi 5–6 alimentano la **Tappa 4 — Sensitività a $\phi$ e a $\psi$**;
- il Passo 7 alimenta la **Tappa 5 — Confronto delle sensitività e scenario analysis**;
- il Passo 8 alimenta la **Tappa 6 — Controlli conclusivi e predisposizione dell'interpretazione**.

La corrispondenza non implica che ciascun passo teorico o ciascuna tappa debba coincidere con una singola cella del notebook. Il Flusso definisce l'ordine concettuale; le tappe raggruppano blocchi operativi coerenti; le celle costituiscono la loro articolazione concreta.

## 7. Scomposizione attesa in tappe

La scomposizione operativa deve derivare dal Flusso logico-teorico risolutivo e deve mantenere visibile, per ciascuna tappa, il collegamento tra input disponibili, oggetti teorici, operazione computazionale, output prodotto, controllo associato e utilizzo successivo.

Le tappe devono costituire **blocchi operativi ampi** e non coincidere con singole operazioni, tabelle, grafici o celle del notebook.

Il Regime IA indicato nella tabella rappresenta il regime prevalente della tappa ordinaria.

Il Regime C non costituisce una tappa programmata del percorso. Può essere attivato soltanto quando lo studente individua una criticità specifica nel materiale prodotto e formula una richiesta mirata di verifica.

| Tappa | Titolo | Obiettivo | Input | Regime IA prevalente | Prompt virtuoso di riferimento | Oggetti teorici coinvolti | Operazione | Output | Controllo | Uso successivo |
|---:|---|---|---|:---:|---|---|---|---|---|---|
| 1 | Traduzione del modello nella forma solver | Trasformare la specifica economico-finanziaria in una struttura compatibile con il solver senza modificarne il contenuto | Scheda Caso; parametri benchmark; formule del modello | A/B | Ricostruire l'ordinamento delle variabili e verificare la traduzione di obiettivo, uguaglianze, disuguaglianze e bounds | Programmazione lineare; bilanci temporali; vincoli; bounds; trasformazione massimo/minimo | Definire ordinamento, vettore obiettivo, $A_{\mathrm{eq}}$, $b_{\mathrm{eq}}$, $A_{\mathrm{ub}}$, $b_{\mathrm{ub}}$ e bounds | Struttura solver completa del benchmark | Coerenza dimensionale; coefficienti; segni; ordinamento delle variabili | Benchmark |
| 2 | Benchmark, diagnostica e valori marginali | Risolvere il benchmark e validare congiuntamente soluzione, vincoli e sensitività locale | Struttura solver della Tappa 1; $(\theta,\phi,\psi)=(1,1,1)$ | B | Risolvere il benchmark, costruire la diagnostica e verificare numericamente almeno un marginale | Ammissibilità; ottimalità; residuali; slack; bounds attivi; dualità; sensitività locale | Eseguire `linprog`; ricostruire $\Pi^*$; estrarre $x^*$, $g^*$, $u^*$; costruire tabelle diagnostiche; associare i marginali; eseguire una perturbazione controllata | Tabelle benchmark; residuali; slack; bounds attivi; marginali; verifica perturbativa | Stato solver; bilanci; vincolo prudenziale; limite su $x_3$; bounds funding; non negatività; segno e validità locale del marginale | Parametrizzazione |
| 3 | Solver parametrico, sensitività a $\theta$ e frontiera di fattibilità | Generalizzare il benchmark e analizzare lo stress sui fabbisogni fino alla perdita di fattibilità | Benchmark validato; definizioni di $\theta$, $\phi$, $\psi$; griglia di $\theta$ | A/B | Costruire la funzione parametrica, verificarla nel benchmark, eseguire la griglia di $\theta$ e raffinare il bracket feasible / infeasible | Analisi parametrica; comparative statics; insieme ammissibile parametrico; vincoli attivi | Implementare `solve`; riprodurre il benchmark; eseguire la griglia di $\theta$; raccogliere risultati; individuare ultimo ammissibile e primo non ammissibile; raffinare l'intervallo | Funzione parametrica; Tabella 6; Figure 1–6, 9–10; Tabella 9; intervallo contenente $\theta_{\mathrm{crit}}$ | Corretta azione dei tre driver nella funzione; unico parametro variato nella sensitività; stato solver; esclusione dei risultati non validi; raffinamento basato sulla fattibilità | Sensitività agli altri driver |
| 4 | Sensitività a $\phi$ e a $\psi$ | Analizzare separatamente capacità disponibile e costo del funding | Funzione parametrica validata; griglie di $\phi$ e $\psi$ | B | Risolvere separatamente le due griglie e costruire gli output richiesti | Bounds parametrizzati; costo e rimborso del funding; comparative statics | Variare $\phi$ con $\theta=\psi=1$; variare $\psi$ con $\theta=\phi=1$; raccogliere risultati, vincoli attivi e utilizzo del funding | Tabelle 7–8; Figure 7–8; output quantitativi per il confronto dei driver | Unico parametro variato; $\phi$ applicato solo ai bounds; $\psi$ applicato sia all'obiettivo sia ai rimborsi; uso esclusivo di soluzioni valide | Confronto dei driver e scenari |
| 5 | Confronto delle sensitività e scenario analysis | Mettere in relazione le tre comparative statics e analizzare le configurazioni con variazione congiunta | Risultati delle Tappe 3–4; tre scenari assegnati | A/B | Confrontare $\theta$, $\phi$, $\psi$ senza confonderli con gli scenari e risolvere Standard, Mediamente critico e Critico | Comparative statics; cambiamenti di regime; scenario analysis deterministica | Collegare variazioni di soluzione e vincoli attivi; risolvere le tre configurazioni; calcolare la perdita rispetto allo Standard | Sintesi comparativa; Tabella 10; Figure 11–14 | Distinzione tra sensitività e scenari; parametri esatti; stato solver; Standard uguale al benchmark; uso esclusivo di risultati validi | Controllo conclusivo |
| 6 | Controlli conclusivi e predisposizione dell'interpretazione | Verificare la coerenza complessiva del notebook e predisporre gli elementi quantitativi per il commento finale | Tutti gli output precedenti | A | Riesaminare Scheda Caso, formule, risultati, tabelle, grafici e controlli prima dell'interpretazione | Coerenza globale; limiti del modello; interpretazione economico-finanziaria | Eseguire la checklist finale, verificare completezza e riproducibilità e delimitare il significato dei risultati | Sintesi quantitativa validata e base per il commento finale | Completezza; riproducibilità; coerenza Scheda Caso--notebook; rispetto dei limiti interpretativi | Chiusura del notebook |

### Eventuale attivazione del Regime C

Il Regime C non deve essere incorporato preventivamente nella sequenza delle tappe.

Può essere utilizzato, dopo una qualsiasi tappa, soltanto se lo studente individua una criticità specifica, ad esempio:

- un residuale inatteso;
- un segno apparentemente incoerente;
- un valore marginale che non coincide con la verifica perturbativa;
- una configurazione dichiarata ammissibile o non ammissibile in modo inatteso;
- una possibile incoerenza tra formula, codice e output;
- una possibile incoerenza tra tabella, grafico e risultato numerico.

In tal caso il prompt in Regime C deve indicare:

1. la tappa interessata;
2. la criticità specifica osservata;
3. gli elementi quantitativi che motivano il dubbio.

L'esito deve essere classificato come **criticità respinta** oppure **criticità accolta**.

Un eventuale intervento in Regime C non modifica la numerazione ordinaria delle tappe.

## 8. Sequenza docente dei prompt e mappa prompt-notebook

### 8.1 Sequenza docente dei prompt virtuosi

La sequenza ordinaria dei prompt è:

1. Prompt zero;
2. Prompt 1;
3. Prompt 2;
4. Prompt 3;
5. prompt di tappa derivati dalla scomposizione operativa validata.

Il Regime C non costituisce una fase obbligatoria né una tappa programmata del lavoro.

Può essere attivato soltanto quando lo studente individua una criticità specifica in una parte del notebook, in un output, in un controllo o nell'interpretazione di un risultato e formula una richiesta mirata di verifica.

La sequenza ordinaria è quindi:

$$
\text{Prompt zero}
\longrightarrow
\text{Prompt 1}
\longrightarrow
\text{Prompt 2}
\longrightarrow
\text{Prompt 3}
\longrightarrow
\text{prompt di tappa}.
$$

L'eventuale intervento in Regime C si inserisce soltanto nel punto in cui emerge una criticità specifica e non modifica la struttura ordinaria del percorso.

### 8.2 Funzione dei prompt iniziali

**Prompt zero**

Funzione:
- inizializzare il contesto;
- acquisire le regole generali;
- fissare il significato dei Regimi A, B e C;
- richiamare i vincoli sul ruolo dell'IA.

Non produce direttamente una cella del notebook.

**Prompt 1**

Funzione:
- acquisire integralmente la Scheda Caso come specifica vincolante;
- produrre esclusivamente la cella Markdown iniziale di inquadramento.

La cella deve:
- sintetizzare titolo, contesto e domanda quantitativa;
- riportare le quantità da stimare o calcolare;
- riportare gli output richiesti;
- riportare i controlli richiesti;
- dichiarare che la Scheda Caso non può essere modificata.

Non deve contenere:
- codice;
- soluzione;
- Flusso logico-teorico risolutivo;
- tappe operative;
- risultati numerici;
- interpretazioni conclusive.

**Prompt 2 — Regime A**

Funzione:
- costruire il Flusso logico-teorico risolutivo.

Lo studente deve proporre una prima sequenza teorico-logica.

L'IA può:
- verificare;
- completare;
- correggere;
- ordinare.

L'output deve essere una sola cella Markdown contenente il Flusso logico-teorico risolutivo, articolato in un numero contenuto di passi e comunque non superiore a otto.

**Prompt 3 — Regime A/B**

Funzione:
- trasformare il Flusso logico-teorico validato nella scomposizione operativa in tappe.

Lo studente deve proporre una prima articolazione delle tappe.

L'IA può:
- verificarla;
- completarla;
- ordinarla;
- associare a ciascuna tappa il regime IA prevalente.

La scomposizione deve utilizzare blocchi operativi ampi e comunque non più di sei tappe.

Non deve ancora sviluppare integralmente il codice delle singole tappe.

L'output deve essere una sola cella Markdown contenente la scomposizione operativa validata.

### 8.3 Prompt di tappa

I prompt di tappa devono essere costruiti a partire dalla Sezione 7 e devono indicare almeno:

1. numero e titolo della tappa;
2. obiettivo;
3. input disponibili;
4. oggetti teorici coinvolti;
5. operazione richiesta;
6. output atteso;
7. controllo da svolgere;
8. uso dell'output nella tappa successiva;
9. regime IA prevalente.

Il Regime A deve essere utilizzato quando la funzione principale della tappa è teorico-modellistica o interpretativa.

Il Regime B deve essere utilizzato quando una struttura già definita deve essere tradotta in codice o in una procedura computazionale.

Una stessa tappa può richiedere più interazioni e più celle Markdown o Python. L'accorpamento delle operazioni in una stessa tappa non implica che esse debbano essere svolte in un'unica risposta IA o in un'unica cella.

### 8.4 Mappa prompt-notebook

| Prompt | Regime | Tappa o fase | Funzione del prompt | Celle o output prodotti | Decisione o controllo richiesto |
|---:|:---:|---|---|---|---|
| Prompt zero | — | Inizializzazione | Acquisire regole generali, struttura del lavoro e disciplina dei Regimi IA | Nessuna cella obbligatoria | Verifica dell'acquisizione delle regole |
| Prompt 1 | — | Inquadramento | Acquisire la Scheda Caso e produrre la cella Markdown iniziale | Cella Markdown iniziale | Fedeltà integrale alla Scheda Caso; assenza di soluzione o suggerimenti risolutivi |
| Prompt 2 | A | Flusso teorico | Costruire e ordinare il Flusso logico-teorico risolutivo a partire dal contributo iniziale dello studente | Cella Markdown con il Flusso in massimo 8 passi | Completezza teorica; ordine logico; copertura di output e controlli |
| Prompt 3 | A/B | Scomposizione operativa | Tradurre il Flusso validato nella sequenza di tappe input-output | Cella Markdown con massimo 6 tappe | Coerenza con il Flusso; copertura di output e controlli; correttezza dei Regimi IA |
| Prompt di tappa 1 | A/B | Tappa 1 — Forma solver | Costruire ordinamento delle variabili e struttura matriciale del benchmark | Celle Markdown e codice per parametri, vettore obiettivo, matrici e bounds | Dimensioni; coefficienti; segni; corrispondenza con la Scheda Caso |
| Prompt di tappa 2 | B | Tappa 2 — Benchmark, diagnostica e marginali | Risolvere il benchmark, validarlo e verificare almeno un marginale | Celle codice, output diagnostici e breve Markdown di interpretazione locale | Stato solver; vincoli; residuali; slack; bounds; verifica perturbativa; segno max/min |
| Prompt di tappa 3 | A/B | Tappa 3 — Solver parametrico, $\theta$ e frontiera | Costruire la funzione parametrica, riprodurre il benchmark, eseguire la sensitività a $\theta$ e raffinare la frontiera | Celle Markdown/codice, DataFrame, figure e tabella di raffinamento | Azione corretta dei driver; unico parametro variato; esclusione dei punti non validi; bracket feasible / infeasible |
| Prompt di tappa 4 | B | Tappa 4 — Sensitività a $\phi$ e $\psi$ | Analizzare separatamente capacità e costo del funding | DataFrame, figure e controlli relativi alle due griglie | $\phi$ solo sui bounds; $\psi$ su obiettivo e rimborsi; stato solver |
| Prompt di tappa 5 | A/B | Tappa 5 — Confronto delle sensitività e scenari | Confrontare i driver e risolvere le tre configurazioni congiunte | Markdown di sintesi; tabella e grafici di scenario | Distinzione sensitività/scenari; parametri esatti; Standard = benchmark; risultati validi |
| Prompt di tappa 6 | A | Tappa 6 — Controlli conclusivi | Verificare completezza e coerenza del notebook e predisporre gli elementi quantitativi per l'interpretazione finale | Celle di controllo e Markdown conclusivo | Coerenza Scheda Caso--notebook; riproducibilità; completezza degli output; limiti del modello |

### 8.5 Eventuale Prompt in Regime C

Un Prompt C può essere attivato soltanto se lo studente identifica una criticità specifica.

Non deve essere previsto automaticamente un «Prompt C finale» né deve essere richiesto un numero minimo di interventi in Regime C.

Il Prompt C deve indicare:

1. tappa interessata;
2. cella, output o controllo interessato;
3. criticità osservata;
4. ragionamento che motiva il dubbio.

L'IA deve verificare esclusivamente la criticità indicata e classificare l'esito come:

- **criticità respinta**;
- **criticità accolta**.

Se la criticità è respinta, non devono essere proposte modifiche al notebook.

Se la criticità è accolta, devono essere proposte soltanto le correzioni necessarie alla parte interessata, senza modificare autonomamente la Scheda Caso.

### 8.6 Regole di coerenza della sequenza

La sequenza dei prompt deve rispettare le seguenti condizioni:

1. il Prompt 2 precede sempre il Prompt 3;
2. il Prompt 3 precede i prompt operativi di tappa;
3. il Flusso logico-teorico deve contenere non più di otto passi;
4. la scomposizione operativa deve contenere non più di sei tappe;
5. le tappe devono derivare dal Flusso logico-teorico validato;
6. nessun prompt può modificare variabili, parametri, formule, griglie, scenari, output o controlli fissati dalla Scheda Caso;
7. ogni prompt di tappa deve essere riconducibile a una tappa della Sezione 7;
8. tutti gli output e tutti i controlli della Scheda Caso devono risultare coperti dalla sequenza complessiva;
9. l'IA non deve produrre in un unico passaggio l'intero notebook;
10. ogni output computazionale deve essere validato prima di essere utilizzato nelle operazioni successive;
11. l'interpretazione finanziaria finale resta responsabilità dello studente;
12. il Regime C resta eventuale e subordinato all'individuazione autonoma di una criticità specifica.

## 9. Struttura attesa del notebook

Il notebook deve riflettere la sequenza logico-operativa validata nelle Sezioni 6 e 7.

La struttura deve rendere riconoscibile il percorso:

$$
\text{inquadramento}
\longrightarrow
\text{Flusso logico-teorico}
\longrightarrow
\text{tappe operative}
\longrightarrow
\text{forma solver}
$$

$$
\longrightarrow
\text{benchmark e diagnostica}
\longrightarrow
\text{solver parametrico}
\longrightarrow
\text{sensitività e frontiera}
\longrightarrow
\text{scenari}
$$

$$
\longrightarrow
\text{controlli conclusivi}
\longrightarrow
\text{interpretazione finale}.
$$

La struttura del notebook non deve replicare meccanicamente il numero dei passi del Flusso o delle operazioni elementari. Ciascuna delle sei tappe può articolarsi in più celle Markdown, codice e output.

### 9.1 Sequenza delle celle e degli output

La sequenza attesa è la seguente.

1. **Cella Markdown iniziale — Prompt 1**
   - titolo;
   - contesto;
   - domanda quantitativa;
   - quantità da calcolare;
   - output richiesti;
   - controlli richiesti;
   - richiamo alla natura vincolante della Scheda Caso.

2. **Cella Markdown — Prompt 2**
   - Flusso logico-teorico risolutivo validato in massimo otto passi.

3. **Cella Markdown — Prompt 3**
   - scomposizione operativa validata in massimo sei tappe.

4. **Tappa 1 — Traduzione del modello nella forma solver**
   - cella Markdown con obiettivo, input, oggetti teorici, output e controllo;
   - celle codice per importazioni e parametri benchmark;
   - **Tabella 1 — Benchmark e parametri principali**;
   - ordinamento dichiarato e invariato delle variabili;
   - celle codice per vettore obiettivo, $A_{\mathrm{eq}}$, $b_{\mathrm{eq}}$, $A_{\mathrm{ub}}$, $b_{\mathrm{ub}}$ e bounds;
   - controlli dimensionali, dei coefficienti e dei segni;
   - breve richiamo alla trasformazione $\max\Pi\leftrightarrow\min(-\Pi)$.

5. **Tappa 2 — Benchmark, diagnostica e valori marginali**
   - cella Markdown introduttiva;
   - soluzione benchmark in $(1,1,1)$;
   - Tabella 2 — Soluzione benchmark;
   - Tabella 3 — Verifica dei bilanci temporali;
   - Tabella 4 — Vincoli, bounds e slack benchmark;
   - Tabella 5 — Valori marginali benchmark;
   - verifica perturbativa di almeno un marginale;
   - breve Markdown di interpretazione locale del marginale verificato.

6. **Tappa 3 — Solver parametrico, sensitività a $\theta$ e frontiera**
   - cella Markdown con definizione dei tre driver e funzione della tappa;
   - funzione $\operatorname{solve}(\theta,\phi,\psi)$;
   - verifica della riproduzione del benchmark;
   - esecuzione della griglia di $\theta$;
   - Tabella 6 — Sensitività a $\theta$;
   - Figure 1–6 e, lungo una griglia informativa, Figure 9–10;
   - identificazione dell'ultimo valore ammissibile e del primo non ammissibile;
   - raffinamento della frontiera;
   - Tabella 9 — Raffinamento della frontiera;
   - Markdown con l'intervallo contenente $\theta_{\mathrm{crit}}$.

7. **Tappa 4 — Sensitività a $\phi$ e a $\psi$**
   - cella Markdown introduttiva che distingue capacità e costo del funding;
   - esecuzione della griglia di $\phi$;
   - Tabella 7 e Figura 7;
   - esecuzione della griglia di $\psi$;
   - Tabella 8 e Figura 8;
   - controlli specifici sulla corretta azione dei due parametri.

8. **Tappa 5 — Confronto delle sensitività e scenario analysis**
   - cella Markdown di confronto tra $\theta$, $\phi$ e $\psi$;
   - collegamento tra variazioni della soluzione e cambiamenti di vincoli o bounds attivi;
   - cella Markdown con Standard, Mediamente critico e Critico;
   - risoluzione delle tre configurazioni;
   - Tabella 10 — Confronto degli scenari;
   - Figure 11–14.

9. **Tappa 6 — Controlli conclusivi e predisposizione dell'interpretazione**
   - cella Markdown e/o codice con checklist conclusiva;
   - verifica della formulazione solver;
   - verifica del benchmark e dei marginali;
   - verifica delle sensitività e della frontiera;
   - verifica degli scenari;
   - verifica dell'uso esclusivo di risultati validi;
   - verifica della riproducibilità;
   - cella Markdown con gli elementi quantitativi necessari all'interpretazione economico-finanziaria;
   - cella Markdown finale dello studente per il commento autonomo.

Gli output delle celle codice costituiscono parte integrante della sequenza e non richiedono una numerazione autonoma delle celle.

### 9.2 Corrispondenza con le tappe operative

La struttura deve mantenere riconoscibile la seguente corrispondenza:

- **Tappa 1 — Traduzione del modello nella forma solver:** costruzione e validazione della forma computazionale;

- **Tappa 2 — Benchmark, diagnostica e valori marginali:** soluzione benchmark, tabelle diagnostiche e verifica perturbativa;

- **Tappa 3 — Solver parametrico, sensitività a $\theta$ e frontiera:** funzione parametrica, stress sui fabbisogni e localizzazione di $\theta_{\mathrm{crit}}$;

- **Tappa 4 — Sensitività a $\phi$ e a $\psi$:** capacità e costo del funding analizzati separatamente;

- **Tappa 5 — Confronto delle sensitività e scenario analysis:** sintesi dei driver e variazione congiunta negli scenari assegnati;

- **Tappa 6 — Controlli conclusivi e predisposizione dell'interpretazione:** validazione globale e base quantitativa per il commento finale.

La numerosità delle celle è indicativa e deve essere determinata dalla leggibilità del notebook e dalla necessità di mantenere visibile la sequenza:

$$
\text{operazione}
\longrightarrow
\text{output}
\longrightarrow
\text{controllo}
\longrightarrow
\text{uso successivo}.
$$

Una singola tappa può quindi contenere più coppie o blocchi di celle Markdown/Python.

### 9.3 Regole di costruzione del notebook

Il notebook deve rispettare le seguenti regole:

1. essere eseguibile sequenzialmente dall'inizio alla fine;

2. non dipendere da oggetti prodotti in esecuzioni precedenti non riproducibili;

3. non contenere celle errate duplicate o versioni alternative non utilizzate;

4. mantenere invariato l'ordinamento delle variabili dopo che è stato dichiarato;

5. generare tabelle e grafici direttamente dagli oggetti prodotti dal solver;

6. non inserire manualmente nelle celle successive valori numerici della soluzione;

7. verificare sempre lo stato del solver prima di utilizzare:

$$
x^*,
\qquad
g^*,
\qquad
u^*,
\qquad
\Pi^*;
$$

8. non utilizzare risultati provenienti da configurazioni non ammissibili;

9. distinguere chiaramente:
   - sensitività univariata;
   - frontiera di fattibilità;
   - scenario analysis;

10. applicare $\psi$ coerentemente sia alla funzione obiettivo sia ai rimborsi del funding;

11. collocare la ricerca della frontiera di fattibilità immediatamente dopo la sensitività a $\theta$ e all'interno della stessa tappa operativa;

12. produrre tutti gli output richiesti dalla Scheda Caso;

13. eseguire i controlli previsti nel punto in cui diventano necessari e prima dell'interpretazione conclusiva;

14. mantenere coerenti notazione matematica e nomi delle variabili computazionali;

15. non prevedere automaticamente directory di output o esportazioni esterne;

16. utilizzare le celle Markdown per introdurre e collegare i blocchi operativi, evitando di trasformare ogni singola operazione in una tappa autonoma.

### 9.4 Funzione delle celle Markdown

Le celle Markdown devono essere utilizzate per rendere riconoscibile:

1. obiettivo della tappa;

2. input disponibili;

3. oggetti teorici coinvolti;

4. operazioni da svolgere all'interno della tappa;

5. output attesi;

6. controlli associati;

7. collegamento con la tappa successiva;

8. interpretazioni locali necessarie alla comprensione degli output.

Le celle Markdown non devono duplicare estensivamente il manuale o le slides.

Una tappa può contenere più celle Markdown quando servono a separare momenti logicamente distinti, ad esempio benchmark e verifica perturbativa, oppure sensitività a $\theta$ e raffinamento della frontiera.

### 9.5 Funzione delle celle di controllo

I controlli non devono essere concentrati esclusivamente alla fine.

Devono comparire nel punto in cui diventano necessari:

- controllo dimensionale dopo la costruzione della forma solver;

- residuali, slack e bounds dopo la soluzione benchmark;

- verifica dei marginali prima della parametrizzazione;

- controllo della riproduzione del benchmark dopo la costruzione della funzione parametrica;

- stato del solver durante ciascuna griglia;

- controllo feasible / infeasible durante la ricerca di $\theta_{\mathrm{crit}}$;

- controllo della doppia azione di $\psi$ durante la relativa sensitività;

- coerenza dei parametri durante la scenario analysis;

- controllo complessivo prima dell'interpretazione finale.

Il notebook deve quindi rendere visibile la sequenza:

$$
\text{operazione}
\longrightarrow
\text{output}
\longrightarrow
\text{controllo}
\longrightarrow
\text{uso successivo}.
$$

## 10. Criteri di validazione del notebook

Il notebook del Caso Aula è considerato valido se implementa integralmente la Scheda Caso senza modificarne il modello, produce tutti gli output richiesti, esegue i controlli previsti ed è riproducibile mediante esecuzione sequenziale dall'inizio alla fine.

### 10.1 Fedeltà alla specifica del caso

Il notebook deve:

1. utilizzare esclusivamente le variabili, i parametri, le formule, le griglie e gli scenari definiti nella Scheda Caso;

2. mantenere invariato l'ordinamento delle variabili una volta dichiarato;

3. rispettare la specifica:

$$
d(\theta)
=
(30\theta,30\theta,22,15)';
$$

4. rispettare la parametrizzazione della capacità di funding:

$$
\bar u_t(\phi)
=
\phi\bar u_t;
$$

5. rispettare la parametrizzazione del costo del funding:

$$
r_t^u(\psi)
=
\psi r_t^u;
$$

6. applicare $\psi$ coerentemente sia alla funzione obiettivo sia al rimborso del funding nei bilanci temporali;

7. utilizzare esattamente le griglie parametriche assegnate;

8. utilizzare esattamente le configurazioni Standard, Mediamente critico e Critico previste dalla Scheda Caso;

9. non introdurre parametri, vincoli, scenari o modifiche del modello non autorizzati.

### 10.2 Validazione della forma solver

La traduzione computazionale è considerata valida se:

1. il vettore decisionale contiene correttamente le variabili:

$$
x_1,\ldots,x_4,
\qquad
g_1,\ldots,g_4,
\qquad
u_1,u_2,u_3;
$$

2. le dimensioni del vettore obiettivo, di $A_{\mathrm{eq}}$, $b_{\mathrm{eq}}$, $A_{\mathrm{ub}}$, $b_{\mathrm{ub}}$ e dei bounds sono reciprocamente compatibili;

3. il passaggio dal problema economico di massimizzazione alla convenzione di minimizzazione di `scipy.optimize.linprog` è effettuato correttamente;

4. i quattro bilanci temporali sono tradotti senza omissioni o errori di indice;

5. il vincolo prudenziale:

$$
\ell'x\leq7
$$

è codificato correttamente;

6. il limite:

$$
x_3\leq30
$$

è codificato correttamente;

7. i bounds del funding rispettano:

$$
0\leq u_t\leq\phi\bar u_t;
$$

8. le condizioni di non negatività di $x$ e $g$ sono correttamente rappresentate;

9. la forma solver può essere ricostruita direttamente dalle formule della Scheda Caso.

### 10.3 Validazione del benchmark

Il benchmark è considerato validato se:

1. il solver restituisce uno stato di ottimizzazione valido per:

$$
(\theta,\phi,\psi)
=
(1,1,1);
$$

2. il vettore $x^*$ soddisfa il vincolo sulle risorse iniziali;

3. tutti i bilanci temporali risultano soddisfatti entro una tolleranza numerica dichiarata;

4. il vincolo prudenziale è rispettato;

5. il limite su $x_3$ è rispettato;

6. tutti i bounds del funding sono rispettati;

7. tutte le variabili soddisfano le condizioni di non negatività;

8. slack e classificazione attivo / non attivo risultano coerenti;

9. i bounds attivi sono identificati correttamente;

10. il valore economico della funzione obiettivo è ricostruito correttamente a partire dalla soluzione del problema trasformato;

11. i principali valori marginali restituiti dal solver sono associati al corretto vincolo o bilancio;

12. almeno un valore marginale è verificato mediante una piccola perturbazione numerica del relativo termine noto o limite.

### 10.4 Validazione della funzione parametrica

La funzione solver parametrica è considerata valida se:

1. nel punto:

$$
(\theta,\phi,\psi)
=
(1,1,1)
$$

riproduce la soluzione benchmark entro la tolleranza numerica adottata;

2. una variazione di $\theta$ modifica esclusivamente i fabbisogni delle prime due date;

3. una variazione di $\phi$ modifica esclusivamente la capacità massima di funding;

4. una variazione di $\psi$ modifica correttamente sia i costi nella funzione obiettivo sia i rimborsi del funding;

5. nessuna variazione parametrica altera accidentalmente coefficienti che devono restare invariati;

6. lo stato del solver viene controllato prima di utilizzare i valori della soluzione.

### 10.5 Validazione delle sensitività univariate

Ciascuna sensitività è considerata valida se:

1. varia un solo parametro alla volta;

2. gli altri due parametri restano pari ai valori benchmark;

3. viene utilizzata integralmente la griglia assegnata;

4. per ogni punto viene registrato almeno lo stato del solver e la fattibilità;

5. valori di $x^*$, $g^*$, $u^*$ e $\Pi^*$ vengono utilizzati soltanto quando la soluzione è valida;

6. le variazioni rispetto al benchmark sono calcolate coerentemente;

7. i rapporti di utilizzo della capacità di funding utilizzano il denominatore corretto;

8. i cambiamenti della soluzione vengono confrontati con gli eventuali cambiamenti dei vincoli e dei bounds attivi;

9. grafici e tabelle non collegano né interpretano artificialmente configurazioni ammissibili e non ammissibili;

10. le interpretazioni dei valori marginali restano locali e coerenti con la configurazione considerata.

### 10.6 Validazione della frontiera di fattibilità

La ricerca di $\theta_{\mathrm{crit}}$ è considerata valida se:

1. sulla griglia iniziale viene identificato l'ultimo valore ammissibile di $\theta$;

2. viene identificato il primo valore successivo non ammissibile;

3. il raffinamento viene effettuato esclusivamente nell'intervallo così determinato;

4. lo stato di fattibilità deriva dall'esito del solver e non dall'andamento del valore obiettivo o di una singola variabile;

5. nelle configurazioni non ammissibili non vengono interpretati eventuali valori presenti negli oggetti del solver;

6. il risultato finale viene espresso come intervallo raffinato contenente:

$$
\theta_{\mathrm{crit}};
$$

7. $\theta_{\mathrm{crit}}$ viene interpretato esclusivamente come frontiera di fattibilità del modello stilizzato.

### 10.7 Validazione della scenario analysis

La scenario analysis è considerata valida se:

1. utilizza esattamente le tre configurazioni assegnate;

2. i tre parametri vengono modificati congiuntamente secondo ciascuno scenario;

3. lo scenario Standard riproduce il benchmark;

4. lo stato del solver viene controllato separatamente per ogni scenario;

5. soltanto gli scenari con soluzione valida vengono utilizzati nell'analisi numerica ed economica;

6. la perdita rispetto allo scenario Standard è calcolata come:

$$
L_s
=
\Pi_{\mathrm{Standard}}^*
-
\Pi_s^*;
$$

7. la scenario analysis resta distinta dalle sensitività univariate e non viene interpretata come analisi probabilistica.

### 10.8 Validazione degli output

Gli output sono considerati validi se:

1. tutti i risultati numerici richiesti nella Scheda Caso sono presenti;

2. tutte le tabelle richieste sono presenti e costruite a partire dagli oggetti effettivamente prodotti dal solver;

3. tutti i grafici richiesti sono presenti;

4. tabelle e grafici utilizzano esclusivamente risultati validi;

5. nessun valore della soluzione è inserito manualmente nelle celle successive;

6. titoli, etichette e grandezze rappresentate consentono di identificare chiaramente parametro, variabile o scenario;

7. gli output hanno una funzione informativa, diagnostica o interpretativa riconoscibile;

8. le figure relative alla perdita di fattibilità non rappresentano come continue regioni nelle quali il problema non possiede una soluzione valida;

9. gli output possono essere rigenerati mediante riesecuzione delle celle;

10. non sono richieste esportazioni in file esterni salvo indicazione esplicita del docente.

### 10.9 Validazione della struttura del notebook

Il notebook deve:

1. seguire una sequenza coerente con il Flusso logico-teorico risolutivo e con la scomposizione in tappe validata;

2. mantenere distinguibili:
   - definizione del modello;
   - soluzione benchmark;
   - diagnostica;
   - verifica dei marginali;
   - parametrizzazione;
   - sensitività;
   - frontiera di fattibilità;
   - scenari;
   - controlli conclusivi;

3. integrare celle Markdown e codice in modo da rendere tracciabile il passaggio dalla formulazione teorica all'operazione computazionale;

4. non contenere celle errate duplicate o versioni alternative non utilizzate;

5. essere eseguibile sequenzialmente dall'inizio alla fine;

6. non dipendere da oggetti prodotti da esecuzioni precedenti non riproducibili;

7. mantenere coerenti notazione matematica e nomi delle variabili computazionali;

8. utilizzare gli output delle tappe precedenti come input delle successive in modo tracciabile.

### 10.10 Validazione dell'uso dell'IA

Quando l'IA è utilizzata, il notebook e il relativo tracciato devono risultare coerenti con il protocollo previsto.

In particolare:

1. Prompt zero, Prompt 1, Prompt 2 e Prompt 3 devono precedere i prompt operativi di tappa;

2. il Flusso logico-teorico deve essere validato prima della scomposizione in tappe;

3. la scomposizione in tappe deve essere validata prima dello sviluppo operativo;

4. i prompt di tappa devono essere riconducibili alle tappe approvate;

5. il Regime A non deve produrre codice Python;

6. il Regime B deve tradurre in codice strutture già definite e validate;

7. il Regime C non deve essere attivato automaticamente;

8. un eventuale Regime C deve partire da una criticità specifica individuata dallo studente;

9. l'IA non deve modificare autonomamente la Scheda Caso;

10. la risposta dell'IA deve essere verificata prima di essere incorporata nel notebook.

### 10.11 Criteri specifici del Caso Aula

Oltre ai criteri generali, il notebook del Caso Aula è considerato valido soltanto se:

1. riproduce correttamente il benchmark del modello SVB;

2. rende osservabile il passaggio tra formulazione economico-finanziaria e forma solver;

3. permette di distinguere chiaramente gli effetti di $\theta$, $\phi$ e $\psi$;

4. verifica esplicitamente che $\psi$ agisca sia sul costo del funding sia sul rimborso intertemporale;

5. individua correttamente la perdita di fattibilità rispetto a $\theta$;

6. raffina l'intervallo contenente $\theta_{\mathrm{crit}}$;

7. rende leggibili i cambiamenti della soluzione e dei vincoli attivi lungo le analisi parametriche;

8. distingue esplicitamente sensitività univariata, stress test di fattibilità e scenario analysis;

9. produce tutti gli output previsti nella Scheda Caso;

10. conclude con controlli complessivi coerenti con i limiti del modello.

Un notebook che restituisca semplicemente `success=True` nel benchmark ma non soddisfi i controlli, gli output e i criteri precedenti non è considerato validato.


## 11. Calibrazione docente

La presente sezione contiene informazioni interne di calibrazione e validazione preventiva del Caso Aula.

Tali informazioni servono al docente per verificare che il caso sia numericamente non banale, coerente con gli obiettivi didattici e capace di produrre output interpretabili.

I valori numerici riportati in questa sezione non devono essere trasferiti nella Scheda Caso destinata agli studenti.

### 11.1 Ordini di grandezza attesi

Nel benchmark:

$$
(\theta,\phi,\psi)
=
(1,1,1),
$$

la soluzione attesa, a tolleranza numerica, è:

$$
x^*
\approx
(0,\;51.920,\;0,\;48.080)',
$$

$$
g^*
\approx
(6.152,\;1.567,\;0,\;2.890)',
$$

$$
u^*
\approx
(0,\;0,\;6)',
$$

e:

$$
\Pi^*
\approx
3.5922.
$$

Il limite:

$$
u_3\leq6
$$

deve risultare attivo nel benchmark.

I residuali dei bilanci temporali devono risultare prossimi a zero entro la tolleranza numerica adottata.

### 11.2 Relazioni qualitative attese

La calibrazione deve produrre almeno le seguenti relazioni qualitative.

1. All'aumentare di $\theta$, il piano ottimo deve progressivamente adattarsi a fabbisogni di liquidità più elevati nelle prime due date.

2. L'aumento di $\theta$ deve tendere a deteriorare il valore ottimo:

$$
\Pi^*(\theta),
$$

salvo eventuali tratti locali associati a cambiamenti della base ottima.

3. L'aumento dello stress sui fabbisogni deve rendere maggiormente rilevante la disponibilità di attività che generano liquidità nelle prime date.

4. La sensitività rispetto a $\phi$ deve evidenziare almeno:
   - una regione nella quale la capacità di funding è economicamente scarsa;
   - una regione nella quale ulteriore capacità non modifica più la soluzione ottima.

5. La sensitività rispetto a $\psi$ deve rendere osservabile come il maggiore costo del funding ne modifica la convenienza economica e, quando rilevante, il livello ottimo di utilizzo.

6. Lungo le griglie parametriche possono verificarsi cambiamenti dei vincoli e dei bounds attivi. Tali cambiamenti devono essere coerenti con eventuali cambiamenti di pendenza o di composizione della soluzione.

7. Le sensitività univariate devono produrre una lettura diversa dalla scenario analysis con variazione congiunta dei tre driver.

### 11.3 Calibrazione della frontiera di fattibilità

Con la calibrazione prevista, il problema deve risultare ancora ammissibile per:

$$
\theta=1.05
$$

e deve perdere la fattibilità prima di:

$$
\theta=1.07.
$$

Il controllo docente più fine colloca la frontiera approssimativamente attorno a:

$$
\theta_{\mathrm{crit}}
\simeq
1.061.
$$

Tale valore costituisce esclusivamente una calibrazione interna docente.

Non deve essere comunicato preventivamente agli studenti e non deve comparire nella Scheda Caso.

Nel lavoro dello studente, la frontiera deve essere ricostruita autonomamente mediante:

1. individuazione dell'ultimo valore ammissibile sulla griglia iniziale;
2. individuazione del primo valore non ammissibile;
3. raffinamento dell'intervallo così ottenuto.

Il risultato dello studente non deve essere valutato sulla coincidenza meccanica con il valore interno:

$$
1.061,
$$

ma sulla corretta procedura di individuazione della frontiera, sulla coerenza numerica e sulla precisione compatibile con il raffinamento richiesto.

### 11.4 Calibrazione degli scenari

Prima dell'utilizzo definitivo del caso devono essere validate mediante solver le tre configurazioni:

**Standard**

$$
(\theta,\phi,\psi)
=
(1.00,1.00,1.00);
$$

**Mediamente critico**

$$
(\theta,\phi,\psi)
=
(1.03,0.90,1.25);
$$

**Critico**

$$
(\theta,\phi,\psi)
=
(1.06,0.70,1.50).
$$

Lo scenario Standard deve coincidere con il benchmark.

Gli scenari Mediamente critico e Critico devono produrre configurazioni economicamente distinguibili e sufficientemente informative da rendere osservabili:

1. la variazione del valore ottimo;
2. la ricomposizione dell'attivo;
3. la variazione delle giacenze;
4. la variazione dell'utilizzo del funding;
5. eventuali modifiche dei vincoli e dei bounds attivi.

Gli scenari non devono essere calibrati in modo da produrre differenze puramente cosmetiche.

### 11.5 Errori o ambiguità prevedibili

Gli errori più probabili sono:

1. dimenticare che `scipy.optimize.linprog` risolve un problema di minimizzazione;

2. modificare erroneamente i segni dei vincoli quando si trasforma la funzione obiettivo;

3. confondere redditività dell'attivo e cash flow disponibile alle singole date;

4. dimenticare il rimborso del funding raccolto nella data precedente;

5. collocare il rimborso del funding nella data errata;

6. dimenticare la variabile terminale $g_4$;

7. confondere vincoli di uguaglianza, disuguaglianze e bounds;

8. duplicare un bound come vincolo esplicito senza comprenderne la funzione;

9. interpretare direttamente il segno dei marginali del problema trasformato senza tenere conto della convenzione massimo/minimo;

10. trattare un valore marginale come valido globalmente lungo una griglia parametrica;

11. modificare contemporaneamente più parametri durante una sensitività univariata;

12. applicare $\phi$ al funding effettivamente utilizzato anziché alle capacità:

$$
\bar u_t;
$$

13. applicare $\psi$ soltanto alla funzione obiettivo e non al rimborso del funding nei bilanci temporali;

14. confondere variazione assoluta e variazione percentuale di $\Pi^*$;

15. interpretare cambiamenti di pendenza senza verificare se sia cambiato l'insieme dei vincoli attivi;

16. utilizzare o interpretare `res.x` quando il solver dichiara il problema non ammissibile;

17. collegare graficamente configurazioni ammissibili e non ammissibili;

18. confondere lo scenario Critico con la frontiera di fattibilità rispetto a $\theta$;

19. interpretare $\theta$, $\phi$ e $\psi$ come stime storiche effettive riferite a Silicon Valley Bank;

20. confondere una variazione della capacità di funding con una variazione del funding effettivamente utilizzato;

21. interpretare uno slack nullo come sufficiente, da solo, per attribuire rilevanza economica a un marginale.

### 11.6 Controlli minimi di calibrazione

Prima di considerare il caso pronto per l'utilizzo didattico, il docente deve verificare almeno:

1. riproduzione del benchmark previsto;

2. errore massimo dei bilanci temporali inferiore alla tolleranza numerica adottata;

3. rispetto di tutti i bounds;

4. rispetto del vincolo prudenziale;

5. rispetto del limite di concentrazione:

$$
x_3\leq30;
$$

6. coerenza tra slack e classificazione dei vincoli attivi;

7. corretta identificazione dei bounds attivi;

8. verifica numerica di almeno un valore marginale;

9. corretta interpretazione del segno dei valori marginali rispetto al problema economico originario;

10. riproduzione del benchmark mediante la funzione parametrica nel punto:

$$
(\theta,\phi,\psi)
=
(1,1,1);
$$

11. variazione di un solo parametro alla volta nelle sensitività univariate;

12. corretta applicazione di $\psi$ sia alla funzione obiettivo sia ai rimborsi del funding;

13. separazione tra configurazioni ammissibili e non ammissibili prima della produzione di tabelle e grafici;

14. corretto raffinamento dell'intervallo attorno alla frontiera di $\theta$;

15. coerenza tra variazioni della soluzione, cambiamenti di pendenza e insieme dei vincoli attivi;

16. validità numerica delle tre configurazioni della scenario analysis;

17. riproducibilità integrale del notebook mediante esecuzione sequenziale.

### 11.7 Limiti interpretativi da preservare

La calibrazione deve mantenere visibili i seguenti limiti.

1. Il modello è deterministico.

2. Ogni configurazione parametrica è considerata nota al tempo iniziale.

3. Il comportamento dei depositanti non è modellato endogenamente.

4. Non sono modellati fire sales o feedback tra vendite e prezzi.

5. Lo stress non modifica endogenamente il valore di mercato degli attivi.

6. La capacità di funding è esogena.

7. Il costo del funding è parametrico e non dipende endogenamente dalla quantità raccolta.

8. $\theta$, $\phi$ e $\psi$ non sono variabili casuali.

9. I tre scenari non costituiscono una distribuzione probabilistica.

10. Non vengono assegnate probabilità agli scenari.

11. Non viene effettuata ottimizzazione stocastica.

12. Le decisioni non sono adattive rispetto a informazione progressivamente osservata.

13. Le estensioni stocastiche e adattive appartengono alle lezioni successive.

14. I coefficienti numerici non devono essere interpretati come dati storici effettivi di Silicon Valley Bank.

15. Il valore:

$$
\theta_{\mathrm{crit}}
$$

non deve essere interpretato come una stima empirica della soglia storica di deflusso di SVB.

### 11.8 Segnali di possibile cattiva calibrazione

Il caso deve essere riesaminato se emerge una delle seguenti situazioni:

1. il benchmark risulta non ammissibile;

2. il benchmark presenta residuali incompatibili con la tolleranza numerica adottata;

3. nessun vincolo o bound risulta economicamente informativo;

4. tutte le sensitività producono soluzioni praticamente identiche;

5. una variazione sostanziale di $\phi$ non produce mai alcun effetto sul funding o sulla soluzione;

6. una variazione sostanziale di $\psi$ non produce alcun effetto economicamente interpretabile;

7. la perdita di fattibilità rispetto a $\theta$ cade fuori dalla griglia prevista;

8. la regione di transizione feasible / infeasible non può essere raffinata in modo informativo;

9. gli scenari Mediamente critico e Critico producono risultati quasi indistinguibili dallo Standard;

10. lo scenario Critico risulta talmente estremo da impedire qualsiasi confronto economicamente utile;

11. le variazioni della soluzione risultano dominate da artefatti numerici anziché da cambiamenti economicamente leggibili dei vincoli;

12. la calibrazione rende immediatamente evidente allo studente un risultato che dovrebbe invece emergere dall'analisi.

La calibrazione finale deve garantire un caso numericamente stabile, non banale, interpretabile e coerente con la progressione didattica della Lezione 13.

## 12. Uso dell'IA e tracciato

### 12.1 Uso documentato dell'IA previsto

L'uso documentato dell'IA è previsto.

L'IA deve essere utilizzata come supporto controllato alla costruzione del ragionamento, alla traduzione computazionale e alla verifica degli output.

Non deve sostituire:

1. la Scheda Caso;
2. le decisioni modellistiche già fissate;
3. il contributo iniziale dello studente nei passaggi valutativi;
4. la validazione degli output;
5. l'interpretazione finanziaria finale.

### 12.2 Prompt obbligatori

La sequenza obbligatoria comprende:

1. Prompt zero;
2. Prompt 1;
3. Prompt 2;
4. Prompt 3;
5. prompt di tappa necessari a sviluppare la scomposizione operativa validata.

Il Regime C non costituisce un prompt obbligatorio.

Un eventuale Prompt C può essere aggiunto soltanto quando lo studente individua una criticità specifica da verificare.

La sequenza ordinaria è quindi:

$$
\text{Prompt zero}
\longrightarrow
\text{Prompt 1}
\longrightarrow
\text{Prompt 2}
\longrightarrow
\text{Prompt 3}
\longrightarrow
\text{prompt di tappa}.
$$

### 12.3 Numero dei prompt

Il numero complessivo dei prompt non deve essere fissato artificialmente a priori.

Deve derivare dalla scomposizione operativa validata e dal numero di interazioni effettivamente necessarie per:

1. sviluppare le tappe previste;
2. produrre gli output richiesti;
3. eseguire i controlli;
4. correggere eventuali errori ordinari all'interno dei Regimi A o B.

Un eventuale Prompt C si aggiunge alla sequenza soltanto in presenza di una criticità specifica individuata dallo studente.

Non è richiesto un numero minimo di Prompt C.

Non deve essere introdotto un Prompt C puramente formale allo scopo di soddisfare un requisito quantitativo.

### 12.4 Regimi IA utilizzati

I regimi ordinariamente utilizzati sono:

- **Regime A — Ricognizione teorico-modellistica**;
- **Regime B — Traduzione operativa in codice**.

Il **Regime C — Verifica di una criticità specifica** è eventuale.

#### Regime A

Il Regime A deve essere utilizzato quando occorre:

1. chiarire la struttura teorico-finanziaria del problema;
2. ordinare i passaggi logici;
3. collegare formule, output e controlli;
4. interpretare localmente un risultato già prodotto;
5. confrontare sensitività, vincoli attivi e cambiamenti della soluzione.

Il Regime A non deve produrre codice Python.

#### Regime B

Il Regime B deve essere utilizzato quando una struttura già fissata deve essere tradotta in codice.

Può riguardare:

1. costruzione delle matrici;
2. implementazione del solver;
3. calcolo di residuali e slack;
4. costruzione della funzione parametrica;
5. esecuzione delle griglie;
6. produzione di DataFrame;
7. produzione dei grafici;
8. controlli numerici;
9. raffinamento della frontiera di fattibilità;
10. scenario analysis.

Il Regime B non può modificare la specifica teorica del caso.

#### Regime C

Il Regime C può essere attivato soltanto quando lo studente identifica una possibile criticità specifica.

Il prompt deve contenere:

1. tappa interessata;
2. cella, formula, output o controllo interessato;
3. criticità osservata;
4. ragionamento che motiva il dubbio.

L'IA deve classificare l'esito come:

- **criticità respinta**;
- **criticità accolta**.

Il Regime C non può essere utilizzato per richiedere:

- una revisione generica dell'intero notebook;
- una nuova soluzione del caso;
- un'interpretazione finale delegata all'IA;
- modifiche autonome della Scheda Caso.

### 12.5 Usi ammessi dell'IA

Sono ammessi:

1. verifica della traduzione fra formulazione teorica e struttura solver;

2. controllo dell'ordinamento delle variabili;

3. controllo delle dimensioni di vettori e matrici;

4. supporto alla costruzione di codice Python per una tappa già definita;

5. costruzione della funzione parametrica in:

$$
(\theta,\phi,\psi);
$$

6. supporto alla gestione dei DataFrame;

7. costruzione dei grafici richiesti;

8. spiegazione tecnica degli oggetti restituiti da `scipy.optimize.linprog`;

9. supporto alla verifica di residuali, slack e bounds attivi;

10. supporto alla verifica numerica di un valore marginale;

11. controllo della corretta applicazione di $\theta$, $\phi$ e $\psi$;

12. supporto alla gestione delle configurazioni non ammissibili;

13. supporto al raffinamento della frontiera di fattibilità;

14. confronto tra output numerici, tabelle e grafici;

15. revisione di codice dopo che sia stato identificato un errore o un malfunzionamento;

16. supporto alla verifica della coerenza fra variazioni della soluzione e variazioni dei vincoli attivi;

17. supporto alla revisione critica di una specifica interpretazione già formulata dallo studente.

### 12.6 Usi non ammessi dell'IA

Non sono ammessi:

1. chiedere all'IA di risolvere integralmente il caso in un unico prompt;

2. delegare all'IA la formulazione del modello;

3. modificare variabili, formule, parametri, vincoli o scenari fissati dalla Scheda Caso;

4. introdurre autonomamente nuovi parametri;

5. modificare le griglie assegnate senza esplicita autorizzazione;

6. modificare le tre configurazioni di scenario;

7. chiedere un notebook completo senza passare attraverso Flusso logico-teorico e scomposizione in tappe;

8. chiedere direttamente all'IA il valore di:

$$
\theta_{\mathrm{crit}};
$$

9. accettare valori marginali senza verificarne almeno un caso mediante perturbazione numerica;

10. accettare automaticamente interpretazioni dei valori marginali;

11. interpretare automaticamente grafici e tabelle senza confronto con la soluzione numerica e con i vincoli attivi;

12. utilizzare l'IA per attribuire valore storico ai parametri stilizzati del modello;

13. utilizzare il Regime C per una revisione generica del lavoro;

14. chiedere all'IA di scrivere autonomamente l'interpretazione finanziaria finale da consegnare come contributo dello studente.

### 12.7 Criteri di validazione delle risposte IA

Ogni risposta dell'IA deve essere verificata prima di essere incorporata nel notebook.

La validazione deve controllare almeno:

1. coerenza con il Regime richiesto;

2. coerenza con la Scheda Caso;

3. utilizzo esclusivo degli input disponibili nella tappa;

4. rispetto delle variabili e della notazione fissate;

5. assenza di modifiche non autorizzate al modello;

6. assenza di nuovi parametri, vincoli o scenari non previsti;

7. correttezza della traduzione computazionale quando pertinente;

8. pertinenza degli output proposti;

9. presenza dei controlli richiesti dalla tappa;

10. utilità dell'output prodotto per la tappa successiva;

11. coerenza fra codice, output numerici e formule;

12. assenza di interpretazioni che eccedano il perimetro del modello.

Se la risposta è in Regime C deve essere inoltre verificato che:

1. la criticità sia stata formulata prima dallo studente;

2. l'IA abbia verificato esclusivamente la criticità indicata;

3. l'esito sia classificato come **criticità respinta** oppure **criticità accolta**;

4. in caso di criticità respinta non siano state introdotte modifiche arbitrarie;

5. in caso di criticità accolta la correzione sia limitata alla parte effettivamente interessata.

### 12.8 Tracciato IA richiesto

Il tracciato IA è richiesto.

La modalità ordinaria di consegna è la stampa PDF della chat dedicata al caso.

La chat deve essere utilizzata esclusivamente per il lavoro relativo al Caso Aula.

Non deve contenere:

1. conversazioni estranee;
2. materiale personale;
3. prove casuali non pertinenti;
4. richieste riferite ad altri casi;
5. messaggi che rendano ambiguo il tracciato del processo.

### 12.9 Sequenza osservabile richiesta nel tracciato

Il tracciato deve rendere osservabile la sequenza:

$$
\text{Prompt zero}
\longrightarrow
\text{Prompt 1}
\longrightarrow
\text{Prompt 2}
\longrightarrow
\text{Prompt 3}
\longrightarrow
\text{prompt di tappa effettivamente utilizzati}.
$$

Quando presente, un eventuale Prompt C deve essere collocato nel punto in cui la criticità è effettivamente emersa.

Il tracciato deve permettere di ricostruire:

1. il contributo iniziale dello studente;
2. la risposta dell'IA;
3. la decisione dello studente di accettare, correggere, ridurre o rifiutare la risposta;
4. la traduzione nel notebook;
5. l'output prodotto;
6. il controllo effettuato;
7. il passaggio alla tappa successiva.

### 12.10 Elementi del tracciato oggetto di valutazione

Sono oggetto di valutazione:

1. contributo autonomo dello studente nel Prompt 2;

2. contributo autonomo dello studente nel Prompt 3;

3. capacità di formulare prompt di tappa coerenti con la scomposizione validata;

4. corretta distinzione tra Regime A e Regime B;

5. specificità degli input forniti all'IA;

6. chiarezza dell'output richiesto;

7. presenza dei controlli all'interno dei prompt di tappa;

8. capacità di verificare criticamente le risposte IA;

9. capacità di non delegare all'IA decisioni già fissate dalla Scheda Caso;

10. coerenza fra conversazione, notebook e output prodotti;

11. eventuale qualità dell'attivazione del Regime C quando sia emersa una criticità reale.

L'assenza di un Prompt C non costituisce penalizzazione quando non è emersa alcuna criticità specifica che ne giustificasse l'utilizzo.

### 12.11 Responsabilità dello studente

Restano responsabilità dello studente:

1. validare il Flusso logico-teorico;

2. validare la scomposizione in tappe;

3. controllare il codice prodotto dall'IA;

4. eseguire il notebook;

5. verificare gli output;

6. eseguire i controlli previsti;

7. riconoscere eventuali anomalie;

8. decidere se una risposta IA debba essere accettata, modificata o respinta;

9. formulare eventuali criticità da verificare in Regime C;

10. redigere l'interpretazione finanziaria finale.

L'uso dell'IA deve restare tracciabile, controllato e subordinato alla struttura teorica e operativa definita dal caso.

## 13. Valutazione

La valutazione deve considerare congiuntamente:

1. correttezza della formulazione quantitativa;
2. qualità della traduzione computazionale;
3. completezza e validità degli output;
4. qualità dei controlli;
5. uso documentato e consapevole dell'IA;
6. coerenza dell'interpretazione finale.

L'ottenimento di una soluzione numerica non è sufficiente, da solo, per considerare corretto il lavoro.

### 13.1 Criteri per il notebook

Il notebook deve essere valutato almeno rispetto ai seguenti aspetti.

1. **Corretta costruzione della forma solver**
   - ordinamento delle variabili;
   - vettore obiettivo;
   - uguaglianze;
   - disuguaglianze;
   - bounds.

2. **Fedeltà alla Scheda Caso**
   - nessuna modifica non autorizzata a variabili, formule, parametri, griglie o scenari;
   - corretta implementazione di $\theta$, $\phi$ e $\psi$.

3. **Riproduzione del benchmark**
   - stato valido del solver;
   - soluzione coerente;
   - corretta ricostruzione di $\Pi^*$.

4. **Controlli numerici**
   - residuali;
   - slack;
   - bounds attivi;
   - rispetto del vincolo prudenziale;
   - rispetto del limite su $x_3$;
   - rispetto dei limiti sul funding;
   - non negatività.

5. **Interpretazione dei valori marginali**
   - corretta associazione ai vincoli;
   - attenzione alla trasformazione massimo/minimo;
   - verifica numerica di almeno un marginale.

6. **Qualità della funzione parametrica**
   - riproduzione del benchmark;
   - corretta azione separata di $\theta$, $\phi$, $\psi$;
   - assenza di modifiche accidentali alla struttura del modello.

7. **Sensitività univariate**
   - corretta esecuzione delle tre griglie;
   - variazione di un solo parametro alla volta;
   - corretta gestione delle configurazioni non ammissibili;
   - qualità delle tabelle e dei grafici.

8. **Frontiera di fattibilità**
   - corretta individuazione dell'ultimo valore ammissibile;
   - corretta individuazione del primo valore non ammissibile;
   - raffinamento coerente;
   - interpretazione corretta di $\theta_{\mathrm{crit}}$.

9. **Scenario analysis**
   - utilizzo esatto delle configurazioni assegnate;
   - confronto coerente tra Standard, Mediamente critico e Critico;
   - corretta lettura della perdita di valore e delle modifiche del piano ALM.

10. **Coerenza tra soluzione e vincoli attivi**
    - lettura congiunta di variazioni di $x^*$, $g^*$, $u^*$, $\Pi^*$;
    - confronto con slack, bounds e valori marginali;
    - riconoscimento dei cambiamenti di regime.

11. **Qualità degli output**
    - completezza;
    - leggibilità;
    - pertinenza;
    - coerenza con le quantità richieste;
    - assenza di grafici o tabelle puramente decorativi.

12. **Riproducibilità**
    - esecuzione sequenziale dall'inizio alla fine;
    - assenza di dipendenze nascoste;
    - assenza di valori inseriti manualmente.

### 13.2 Criteri per il tracciato IA

Il tracciato IA deve essere valutato almeno rispetto a:

1. presenza e corretto utilizzo di Prompt zero, Prompt 1, Prompt 2 e Prompt 3;

2. contributo autonomo dello studente nella costruzione del Flusso logico-teorico risolutivo;

3. contributo autonomo dello studente nella scomposizione in tappe;

4. qualità dei prompt di tappa;

5. corretta distinzione tra Regime A e Regime B;

6. capacità di fornire all'IA input completi ma non ridondanti;

7. esplicitazione di output e controlli richiesti;

8. capacità di verificare criticamente le risposte dell'IA;

9. capacità di accettare, modificare o rifiutare una risposta motivando la scelta;

10. assenza di delega all'IA delle decisioni già fissate dalla Scheda Caso;

11. coerenza tra tracciato IA e notebook finale;

12. eventuale corretto utilizzo del Regime C, quando effettivamente giustificato da una criticità specifica.

L'assenza di un intervento in Regime C non costituisce una carenza quando non emerge una criticità specifica.

### 13.3 Peso dei controlli e dell'interpretazione

La valutazione deve attribuire rilievo elevato alla correttezza dei controlli e alla capacità di leggere gli output.

Non è sufficiente ottenere:

```text
success = True
```

dal solver.

Lo studente deve mostrare di sapere verificare:

1. bilanci temporali;
2. vincoli;
3. bounds;
4. residuali;
5. slack;
6. valori marginali;
7. fattibilità;
8. coerenza tra output numerici e rappresentazioni grafiche;
9. relazione tra cambiamenti della soluzione e cambiamenti dei vincoli attivi.

L'interpretazione deve distinguere esplicitamente:

- sensitività univariata;
- stress test di fattibilità;
- scenario analysis.

### 13.4 Elementi particolarmente rilevanti nel Caso Aula

Nel Caso Aula SVB assumono particolare rilievo valutativo:

1. corretta traduzione del modello ALM del Capitolo 12 nella forma solver;

2. verifica della doppia azione di $\psi$:
   - costo del funding nella funzione obiettivo;
   - rimborso del funding nei bilanci temporali;

3. corretta identificazione della frontiera di fattibilità rispetto a $\theta$;

4. distinzione tra ultimo valore ammissibile, primo valore non ammissibile e intervallo raffinato contenente $\theta_{\mathrm{crit}}$;

5. lettura dei bounds di funding attivi;

6. confronto tra effetti di $\theta$, $\phi$ e $\psi$;

7. coerenza tra scenario analysis e struttura deterministica del modello;

8. capacità di non attribuire significato storico ai parametri stilizzati.

### 13.5 Errori che devono incidere significativamente sulla valutazione

Devono incidere in modo rilevante:

1. modifica non autorizzata della Scheda Caso;

2. errore nella forma solver;

3. mancato rimborso del funding;

4. errata applicazione di $\psi$;

5. utilizzo di risultati provenienti da configurazioni non ammissibili;

6. mancata verifica dei vincoli;

7. assenza di controlli numerici;

8. interpretazione errata dei valori marginali;

9. confusione tra sensitività e scenario analysis;

10. uso di $\theta_{\mathrm{crit}}$ come dato fornito anziché come quantità da determinare;

11. notebook non riproducibile;

12. delega all'IA dell'intera soluzione o dell'interpretazione finale.

### 13.6 Qualità attesa dell'interpretazione finale

L'interpretazione finale dello studente deve:

1. basarsi su risultati numericamente validati;

2. collegare il valore ottimo alla composizione dell'attivo, alle giacenze e al funding;

3. discutere quali vincoli risultino economicamente rilevanti;

4. distinguere effetti locali e cambiamenti di regime;

5. discutere la perdita di fattibilità rispetto a $\theta$;

6. confrontare le tre sensitività senza confonderne il significato economico;

7. confrontare gli scenari assegnati;

8. richiamare i limiti del modello;

9. evitare inferenze storiche non giustificate dai dati stilizzati.

La qualità dell'interpretazione deve essere valutata sulla coerenza con gli output e con i limiti dichiarati, non sulla lunghezza del commento.

## 14. Rubrica sintetica

Per il Caso Aula la valutazione deve riflettere la funzione didattica guidata dell'esercizio.

La rubrica assume come riferimento una valutazione complessiva su 100 punti.

| Area | Peso | Criteri principali |
|---|---:|---|
| Formulazione del modello e forma solver | 20 | corretta traduzione del modello ALM; ordinamento delle variabili; costruzione di funzione obiettivo, uguaglianze, disuguaglianze e bounds; coerenza dimensionale |
| Soluzione benchmark e diagnostica | 15 | correttezza della soluzione benchmark; residuali; slack; bounds attivi; rispetto dei vincoli; corretta ricostruzione di $\Pi^*$ |
| Valori marginali e controlli teorico-numerici | 10 | corretta associazione dei marginali ai vincoli; gestione del passaggio massimo/minimo; verifica numerica di almeno un marginale; interpretazione locale |
| Sensitività univariate | 15 | corretta parametrizzazione di $\theta$, $\phi$ e $\psi$; variazione di un solo parametro alla volta; qualità di tabelle e grafici; gestione della fattibilità |
| Frontiera di fattibilità rispetto a $\theta$ | 10 | corretta identificazione dell'ultimo valore ammissibile e del primo non ammissibile; raffinamento dell'intervallo; corretta interpretazione di $\theta_{\mathrm{crit}}$ |
| Scenario analysis | 10 | corretta implementazione di Standard, Mediamente critico e Critico; confronto tra soluzioni; perdita di valore; coerenza con i vincoli attivi |
| Notebook e riproducibilità | 10 | struttura lineare; eseguibilità dall'inizio alla fine; assenza di valori inseriti manualmente; coerenza tra celle Markdown, codice e output |
| Uso documentato dell'IA | 5 | corretto uso di Prompt zero, Prompt 1, Prompt 2, Prompt 3 e prompt di tappa; distinzione tra Regime A e B; capacità di validare le risposte IA; eventuale uso appropriato del Regime C |
| Interpretazione finanziaria finale | 5 | coerenza con gli output; collegamento tra soluzione, funding, liquidità e vincoli; consapevolezza dei limiti del modello |

**Totale: 100 punti.**

### 14.1 Criteri trasversali

Indipendentemente dall'area della rubrica, devono essere considerati criteri trasversali:

1. fedeltà alla Scheda Caso;

2. correttezza matematica;

3. coerenza tra formulazione teorica e implementazione computazionale;

4. qualità dei controlli;

5. uso esclusivo di risultati solver validi;

6. chiarezza nella distinzione tra:
   - benchmark;
   - sensitività;
   - frontiera di fattibilità;
   - scenario analysis;

7. riproducibilità;

8. coerenza tra risultati numerici, tabelle, grafici e interpretazione.

### 14.2 Errori sostanziali

Sono considerati errori sostanziali, tali da incidere significativamente sulla valutazione:

1. modifica non autorizzata del modello;

2. errore nella costruzione dei bilanci temporali;

3. omissione del rimborso del funding;

4. errata trasformazione della funzione obiettivo per il solver;

5. errata applicazione di $\theta$, $\phi$ o $\psi$;

6. utilizzo di `res.x` in configurazioni non ammissibili;

7. mancata verifica dei vincoli;

8. mancata distinzione tra slack e bounds attivi;

9. interpretazione dei marginali senza controllo della convenzione massimo/minimo;

10. confusione tra sensitività univariata e scenario analysis;

11. utilizzo di $\theta_{\mathrm{crit}}$ come dato anziché come quantità da determinare;

12. notebook non riproducibile;

13. produzione di output non coerenti con la Scheda Caso;

14. interpretazione storica dei parametri stilizzati.

### 14.3 Uso dell'IA nella valutazione

L'uso dell'IA non viene valutato in base al numero di prompt utilizzati.

La valutazione riguarda invece:

1. qualità del contributo iniziale dello studente;

2. coerenza dei prompt con la tappa;

3. capacità di utilizzare correttamente il Regime A e il Regime B;

4. capacità di verificare le risposte dell'IA;

5. capacità di correggere o rifiutare risposte incoerenti;

6. assenza di delega all'IA delle decisioni modellistiche già fissate;

7. coerenza tra tracciato IA e notebook finale.

L'eventuale assenza di un Prompt in Regime C non comporta penalizzazione.

Un Prompt C è valutato soltanto quando è stato effettivamente attivato e deve essere giudicato sulla qualità della criticità formulata e della successiva verifica.

### 14.4 Interpretazione del punteggio

La rubrica non deve essere applicata in modo puramente meccanico.

In particolare:

- una soluzione numericamente corretta ma priva di controlli non può ottenere una valutazione elevata;

- un notebook formalmente completo ma non riproducibile deve essere penalizzato;

- grafici e tabelle corretti ma non collegati all'interpretazione non compensano errori nella formulazione del modello;

- un uso esteso dell'IA non costituisce elemento premiante di per sé;

- la qualità del lavoro dipende dalla capacità di collegare:

$$
\text{modello}
\longrightarrow
\text{solver}
\longrightarrow
\text{output}
\longrightarrow
\text{controlli}
\longrightarrow
\text{interpretazione}.
$$

## 15. Esito atteso e calibrazione qualitativa del caso

### 15.1 Esito atteso

Se il caso è correttamente costruito e risolto, deve emergere in modo osservabile che la programmazione lineare consente di collegare:

$$
\text{struttura dell'attivo}
\longrightarrow
\text{profilo temporale della liquidità}
\longrightarrow
\text{uso del funding}
\longrightarrow
\text{vincoli attivi}
\longrightarrow
\text{valore ottimo}.
$$

Lo studente deve poter osservare che il problema ALM non è determinato soltanto dall'ammontare complessivo delle risorse disponibili, ma dalla loro collocazione temporale e dalla capacità di adattare la composizione del portafoglio ai fabbisogni previsti.

Il caso deve inoltre rendere evidente la differenza tra:

1. soluzione benchmark;
2. sensitività univariata;
3. stress test di fattibilità;
4. scenario analysis con variazione congiunta dei driver.

### 15.2 Relazioni qualitative attese

Gli output devono rendere osservabili almeno le seguenti relazioni.

1. Un aumento di $\theta$ deve aumentare la pressione sui bilanci di liquidità delle prime due date e richiedere una ricomposizione del piano ALM.

2. La ricomposizione può interessare:
   - asset allocation;
   - giacenze;
   - ricorso al funding;
   - insieme dei vincoli e dei bounds attivi.

3. Il valore ottimo:

$$
\Pi^*
$$

deve riflettere il costo economico dell'adattamento a condizioni di liquidità più stringenti.

4. Una riduzione di $\phi$ deve rendere più scarsa la capacità disponibile di funding e può modificare la politica ottima anche quando il funding effettivamente utilizzato non coincide con la capacità massima.

5. Un aumento di $\psi$ deve rendere il funding economicamente meno conveniente e deve essere leggibile sia nella funzione obiettivo sia nella dinamica dei rimborsi.

6. I cambiamenti della soluzione non devono essere interpretati separatamente dai cambiamenti dei vincoli e dei bounds attivi.

7. I valori marginali devono risultare informativi localmente, ma non devono essere utilizzati meccanicamente oltre il regime nel quale la struttura della soluzione resta invariata.

8. L'aumento di $\theta$ deve condurre, oltre una certa regione, alla perdita di fattibilità del problema.

9. La frontiera di fattibilità deve emergere come proprietà del modello e non come parametro assegnato.

10. Gli scenari congiunti devono produrre una lettura diversa da quella ottenuta modificando un solo parametro alla volta.

### 15.3 Funzione didattica degli output

Gli output devono rendere operativamente osservabili i seguenti concetti.

1. **Forma solver del programma lineare**

   Lo studente deve vedere come una formulazione economico-finanziaria venga tradotta in:

$$
c,
\qquad
A_{\mathrm{eq}},
\qquad
b_{\mathrm{eq}},
\qquad
A_{\mathrm{ub}},
\qquad
b_{\mathrm{ub}},
\qquad
\text{bounds}.
$$

2. **Fattibilità**

   Lo stato del solver e i residuali devono rendere evidente la distinzione tra una soluzione ottima valida e una configurazione non ammissibile.

3. **Vincoli attivi e slack**

   Le tabelle diagnostiche devono mostrare quali restrizioni incidono effettivamente sul piano ottimo.

4. **Bounds attivi**

   Deve risultare osservabile che anche i bounds sulle variabili possono essere economicamente rilevanti e devono essere distinti dalle disuguaglianze esplicite.

5. **Valori marginali**

   I marginali devono collegare i vincoli del problema alla variazione locale del valore ottimo.

6. **Comparative statics**

   Le sensitività devono mostrare come una stessa struttura ottimizzativa reagisca quando cambia un parametro assegnato.

7. **Cambiamenti di regime**

   I cambiamenti di pendenza, soluzione o vincoli attivi devono rendere evidente la natura piecewise-linear della risposta del programma lineare.

8. **Frontiera di fattibilità**

   La sensitività rispetto a $\theta$ deve mostrare che l'insieme ammissibile può scomparire quando i fabbisogni superano la capacità del sistema di soddisfarli.

9. **Scenario analysis**

   Gli scenari devono mostrare l'effetto combinato di più driver senza introdurre un'interpretazione probabilistica.

### 15.4 Relazioni che non devono essere imposte artificialmente

La calibrazione non deve imporre a priori:

1. monotonicità perfettamente regolare di tutte le variabili decisionali;

2. variazioni lineari della soluzione lungo le griglie;

3. identità dei vincoli attivi in tutte le configurazioni;

4. saturazione permanente della capacità di funding;

5. utilizzo positivo del funding in ogni configurazione;

6. un ordine fisso delle componenti dell'asset allocation;

7. un determinato marginale come economicamente dominante in tutte le configurazioni;

8. differenze artificialmente elevate tra gli scenari.

Le proprietà devono emergere dal modello e dalla calibrazione, non essere incorporate forzatamente negli output.

### 15.5 Possibili segnali di cattiva calibrazione

Costituiscono segnali di possibile cattiva calibrazione:

1. benchmark non ammissibile;

2. benchmark dominato da soluzioni degeneri prive di contenuto economico;

3. residuali incompatibili con la tolleranza numerica adottata;

4. sensitività a $\theta$ quasi priva di effetti sulla soluzione;

5. sensitività a $\phi$ completamente irrilevante su tutta la griglia;

6. sensitività a $\psi$ priva di effetti osservabili sul funding o sul valore ottimo;

7. assenza di qualsiasi cambiamento nei vincoli o nei bounds attivi lungo le griglie;

8. perdita di fattibilità già al benchmark;

9. perdita di fattibilità fuori dall'intervallo previsto dalla griglia di $\theta$;

10. impossibilità di individuare un intervallo utile per il raffinamento di $\theta_{\mathrm{crit}}$;

11. scenari Mediamente critico e Critico quasi indistinguibili dallo Standard;

12. scenario Critico non interpretabile perché eccessivamente distante dal benchmark;

13. risultati dominati da artefatti numerici;

14. grafici sostanzialmente piatti o privi di contenuto informativo;

15. output così complessi da impedire una lettura chiara dei principali meccanismi del modello.

### 15.6 Criterio qualitativo finale

La calibrazione è considerata soddisfacente se il caso consente allo studente di osservare con chiarezza che:

$$
\text{una variazione dei parametri}
\not\Rightarrow
\text{solo una variazione di } \Pi^*,
$$

ma può determinare anche:

$$
\text{ricomposizione dell'attivo},
\qquad
\text{variazione delle giacenze},
\qquad
\text{variazione del funding},
$$

$$
\text{cambiamento dei vincoli attivi},
\qquad
\text{variazione dei valori marginali},
\qquad
\text{perdita di fattibilità}.
$$

Il caso deve quindi risultare:

1. numericamente stabile;
2. non banale;
3. economicamente interpretabile;
4. coerente con i Capitoli 11 e 12;
5. coerente con la funzione computazionale della Lezione 13;
6. sufficientemente ricco da motivare sensitività, frontiera di fattibilità e scenario analysis;
7. sufficientemente delimitato da non anticipare i contenuti stocastici delle lezioni successive.

## 16. Relazione con l'altro caso della lezione

Il Caso Aula Silicon Valley Bank e il Caso TakeHome First Republic Bank devono essere metodologicamente comparabili, ma non devono ridursi a una semplice variazione parametrica dello stesso problema.

La relazione fra i due casi deve mostrare continuità degli strumenti quantitativi e differenza della struttura economico-finanziaria.

### 16.1 Concetti teorici comuni

I due casi consolidano i seguenti concetti:

1. formulazione di un problema di programmazione lineare;

2. distinzione tra:
   - funzione obiettivo;
   - uguaglianze;
   - disuguaglianze;
   - bounds;

3. rappresentazione temporale dei cash flow degli attivi;

4. bilanci di liquidità multiperiodali;

5. utilizzo di giacenze trasferite tra date successive;

6. utilizzo di funding esterno e relativo rimborso;

7. fattibilità del piano ALM;

8. residuali dei vincoli di uguaglianza;

9. slack dei vincoli di disuguaglianza;

10. vincoli e bounds attivi;

11. valori marginali e loro interpretazione locale;

12. sensitività parametrica;

13. cambiamenti della soluzione ottima al variare dei parametri;

14. scenario analysis deterministica;

15. distinzione tra risultati del modello e interpretazione del caso storico.

### 16.2 Strumenti computazionali comuni

Entrambi i casi utilizzano:

1. Python in ambiente Jupyter / VS Code;

2. `scipy.optimize.linprog`;

3. costruzione esplicita di:
   - vettore della funzione obiettivo;
   - $A_{\mathrm{eq}}$;
   - $b_{\mathrm{eq}}$;
   - $A_{\mathrm{ub}}$;
   - $b_{\mathrm{ub}}$;
   - bounds;

4. funzioni solver parametrizzate;

5. DataFrame per organizzare le analisi di sensitività;

6. grafici prodotti a partire dagli output del solver;

7. controlli numerici su residuali, slack e bounds;

8. lettura dei valori marginali restituiti dal solver;

9. verifica dello stato del solver prima dell'utilizzo dei risultati;

10. riesecuzione sequenziale e riproducibile del notebook.

### 16.3 Output comparabili

I due casi devono produrre tipologie di output comparabili:

1. soluzione benchmark;

2. valore ottimo;

3. composizione ottima dell'attivo;

4. giacenze di liquidità;

5. funding utilizzato;

6. residuali;

7. slack;

8. vincoli e bounds attivi;

9. valori marginali economicamente informativi;

10. sensitività univariate;

11. stato di fattibilità lungo le griglie;

12. tabelle comparative;

13. grafici della soluzione parametrica;

14. scenario analysis con configurazioni congiunte;

15. interpretazione economico-finanziaria finale.

La comparabilità riguarda la funzione metodologica degli output, non l'identità del loro contenuto numerico.

### 16.4 Controlli comparabili

Entrambi i casi devono prevedere:

1. controllo dimensionale di vettori e matrici;

2. verifica della trasformazione massimo/minimo;

3. verifica indipendente dei bilanci temporali;

4. controllo dei vincoli di portafoglio;

5. controllo dei bounds del funding;

6. controllo della non negatività;

7. verifica della coerenza tra slack e stato attivo / non attivo;

8. verifica dei bounds attivi;

9. verifica numerica di almeno un valore marginale;

10. controllo della funzione parametrica nel benchmark;

11. verifica che nelle sensitività univariate vari un solo parametro alla volta;

12. esclusione delle configurazioni non ammissibili dall'interpretazione economica;

13. produzione di grafici e tabelle esclusivamente da risultati solver validi;

14. controllo conclusivo di riproducibilità.

### 16.5 Elementi metodologici comuni

La struttura metodologica deve restare comune:

$$
\text{Scheda Caso}
\longrightarrow
\text{Flusso logico-teorico}
\longrightarrow
\text{tappe}
\longrightarrow
\text{notebook}
$$

$$
\longrightarrow
\text{output}
\longrightarrow
\text{controlli}
\longrightarrow
\text{interpretazione finale}.
$$

Anche il protocollo IA deve essere comparabile:

$$
\text{Prompt zero}
\longrightarrow
\text{Prompt 1}
\longrightarrow
\text{Prompt 2}
\longrightarrow
\text{Prompt 3}
\longrightarrow
\text{prompt di tappa}.
$$

L'eventuale Regime C resta subordinato, in entrambi i casi, all'individuazione di una criticità specifica da parte dello studente.

### 16.6 Elementi distintivi del Caso TakeHome rispetto al Caso Aula

Il Caso TakeHome deve essere autonomo rispetto al Caso Aula almeno nelle seguenti dimensioni.

#### Numero e composizione delle classi di attivo

Nel Caso Aula SVB:

- quattro classi di attivo.

Nel Caso TakeHome First Republic:

- cinque classi di attivo;
- maggiore peso di attività creditizie a lunga durata.

#### Struttura dei fabbisogni

Nel Caso Aula lo stress principale riguarda l'aumento dei fabbisogni delle prime due date attraverso:

$$
\theta.
$$

Nel Caso TakeHome sono presenti due ondate distinte:

- prima data, governata da $\alpha$;
- quarta data, governata da $\beta$.

#### Struttura dei vincoli

Nel Caso Aula compare il limite:

$$
x_3\leq30.
$$

Nel Caso TakeHome compare invece il vincolo strutturale:

$$
x_3+x_4\geq35,
$$

oltre al limite:

$$
x_5\leq35.
$$

Il vincolo legacy introduce una rigidità che non è presente nel Caso Aula e richiede una traduzione specifica nella forma solver.

#### Driver parametrici

Nel Caso Aula:

$$
(\theta,\phi,\psi)
$$

consentono di analizzare:

1. fabbisogno;
2. capacità di funding;
3. costo del funding.

Nel Caso TakeHome:

$$
(\alpha,\beta,\phi)
$$

consentono di analizzare:

1. prima ondata di deflussi;
2. seconda ondata di deflussi;
3. capacità di funding.

Il costo del funding resta invariato nel TakeHome.

#### Linea interpretativa

Nel Caso Aula la linea interpretativa principale è:

$$
\text{implementare}
\longrightarrow
\text{validare}
\longrightarrow
\text{parametrizzare}
\longrightarrow
\text{analizzare}.
$$

Nel Caso TakeHome deve prevalere:

$$
\text{riconoscere}
\longrightarrow
\text{riformulare}
\longrightarrow
\text{trasferire il metodo}.
$$

### 16.7 Differenza della responsabilità didattica

Nel Caso Aula il docente:

1. guida la lettura del problema;

2. governa il ritmo delle tappe;

3. discute gli errori più rilevanti;

4. seleziona gli output da interpretare;

5. sostiene la verifica del collegamento con i Capitoli 11 e 12.

Lo studente deve comunque:

1. contribuire al Flusso logico-teorico;

2. contribuire alla scomposizione in tappe;

3. validare le risposte IA;

4. eseguire i controlli;

5. interpretare gli output.

Nel Caso TakeHome aumenta invece la responsabilità dello studente nella:

1. riformulazione autonoma del nuovo problema;

2. costruzione del nuovo benchmark;

3. gestione del vincolo legacy;

4. distinzione fra prima e seconda ondata;

5. verifica della corretta trasposizione del metodo appreso in aula.

### 16.8 Ruolo dell'IA nei due casi

L'IA può assistere entrambi i casi nella traduzione computazionale e nei controlli.

Non deve però:

1. trasformare automaticamente il Caso Aula nel TakeHome mediante semplice sostituzione dei coefficienti;

2. decidere autonomamente come modificare il modello;

3. eliminare o modificare il vincolo legacy;

4. costruire il TakeHome come replica meccanica delle analisi di SVB.

Nel Caso TakeHome deve risultare particolarmente evidente la capacità dello studente di riconoscere:

- quali elementi metodologici sono trasferibili;
- quali elementi devono invece essere riformulati.

### 16.9 Criterio conclusivo di comparabilità

La coppia di casi è considerata ben costruita se:

$$
\text{metodo comune}
\qquad\text{e}\qquad
\text{problema finanziario differente}
$$

sono entrambi chiaramente riconoscibili.

Il Caso TakeHome non deve apparire come:

$$
\text{Caso Aula}
+
\text{nuovi coefficienti}.
$$

Deve invece rappresentare un'applicazione autonoma dello stesso quadro quantitativo a una diversa struttura ALM.

La relazione didattica finale deve essere:

$$
\text{Caso Aula SVB:}
\quad
\text{apprendere e consolidare il metodo},
$$

$$
\text{Caso TakeHome First Republic:}
\quad
\text{trasferire autonomamente il metodo}.
$$
