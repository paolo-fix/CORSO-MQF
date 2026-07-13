# Lezione 04 - Prompt virtuosi docente

## Caso aula

**Titolo:** Perdita obbligazionaria condizionata a regimi di tasso  
**Notebook collegato:** `Lezione_04_Notebook_Docente.ipynb`  
**Scheda collegata:** `Lezione_04_Scheda_Caso_Aula.md`

Questo file riporta solo la **parte variabile** dei prompt usati per costruire il notebook docente.  
La parte fissa è quella prevista dalle istruzioni generali: Prompt zero, Prompt 1, regimi A/B/C, vincolo di non modificare la Scheda Caso e regole operative dell'uso virtuoso dell'IA.

I prompt sono scritti come blocchi Markdown, non come codice, in modo che il testo e le formule matematiche siano renderizzati correttamente.

## Corrispondenza tra prompt e notebook

| Prompt | Regime | Output nel notebook |
|---:|---|---|
| 1 | Prompt fisso | Cella Markdown iniziale di inquadramento |
| 2 | A | Flusso logico-teorico risolutivo |
| 3 | A | Scomposizione operativa in tappe |
| 4 | C | Validazione della scomposizione |
| 5 | B | Tappa 1: parametri e soglia implicita |
| 6 | B | Tappa 2: simulazione della partizione informativa |
| 7 | B | Tappa 3: simulazione degli shock e perdita |
| 8 | B | Tappa 4: analisi non condizionata |
| 9 | B | Tappa 5: analisi condizionata e valore atteso totale |
| 10 | C | Tappa 6: interpretazione critica e limiti |
| 11 | C | Controllo finale |

---

## Prompt 2 - Flusso logico-teorico risolutivo

> **Regime A.**
>
> Sulla base della Scheda Caso Aula, sto costruendo il Flusso logico-teorico risolutivo da inserire nel notebook docente.
>
> Secondo me la sequenza deve partire dalla perdita obbligazionaria $L$, collegarla allo shock di rendimento $\Delta y$ tramite
> $L = D V_0 \Delta y$, tradurre la soglia $\ell$ nella soglia implicita $\Delta y^\star$, introdurre la partizione $A_1,A_2,A_3$, specificare le distribuzioni condizionate e arrivare a media, probabilità di superamento soglia, quantili, medie condizionate e valore atteso condizionato rispetto alla sigma-algebra generata dalla partizione.
>
> Ti chiedo di verificare, completare e ordinare questa sequenza in una tabella del flusso logico-teorico.

---

## Prompt 3 - Scomposizione in tappe input-output

> **Regime A.**
>
> Ora vorrei trasformare il flusso teorico in una struttura operativa per il notebook.
>
> La mia ipotesi è articolare il lavoro in sei tappe: parametri e soglia implicita; simulazione della partizione informativa; simulazione degli shock condizionati e calcolo della perdita; analisi non condizionata; analisi condizionata e verifica del valore atteso totale; interpretazione critica e limiti.
>
> Ti chiedo di trasformare questa ipotesi in una tabella input-output, indicando per ogni tappa input, operazione, output, controllo e uso nella tappa successiva.

---

## Prompt 4 - Validazione della scomposizione

> **Regime C.**
>
> Prima di passare al codice voglio validare la scomposizione in tappe.
>
> Il mio dubbio è che qualche passaggio possa confondere oggetti diversi: gli eventi $A_1,A_2,A_3$ devono restare blocchi della partizione informativa; $\Delta y$ deve restare lo shock di rendimento; $L$ deve restare la perdita derivata; $\mathbb{E}[L\mid A_g]$ ed $\mathbb{E}[L\mid\mathcal{G}]$ devono essere distinti.
>
> Ti chiedo di segnalare solo eventuali mancanze o correzioni necessarie.

---

## Prompt 5 - Tappa 1: parametri e soglia implicita

> **Regime B.**
>
> Costruiamo la Tappa 1 del notebook docente: parametri finanziari e probabilistici del caso.
>
> Produci una cella Markdown sintetica e una cella Python che definisca $V_0$, $D$, $\ell$, $n$, `seed`, probabilità degli eventi $A_1,A_2,A_3$ e parametri $\mu_g,\sigma_g$. Calcola
> $\Delta y^\star = \ell/(D V_0)$.
>
> La cella deve produrre le tabelle dei parametri, degli eventi e dei parametri condizionati, con controlli su probabilità, positività dei parametri e volatilità. Le tabelle visualizzate devono evitare la notazione scientifica.

---

## Prompt 6 - Tappa 2: simulazione della partizione informativa

> **Regime B.**
>
> Costruiamo la Tappa 2: simulazione della partizione informativa.
>
> Assegna a ciascuna osservazione Monte Carlo uno degli eventi $A_1,A_2,A_3$ usando le probabilità della Scheda Caso. Produci frequenze assolute, frequenze relative, probabilità teoriche e scarti.
>
> Nel Markdown chiarisci che le etichette usate nel codice sono operative e non introducono una nuova variabile teorica.

---

## Prompt 7 - Tappa 3: shock condizionati e perdita

> **Regime B.**
>
> Costruiamo la Tappa 3: simulazione di $\Delta y$ condizionatamente all'evento e calcolo della perdita.
>
> Simula $\Delta y$ usando i parametri condizionati di $A_1,A_2,A_3$. Calcola $\Delta y$ in punti base, $\Delta V = -L$ e $L = D V_0 \Delta y$. Costruisci il dataset principale con evento, descrizione, $\Delta y$, punti base, $\Delta V$ e $L$.
>
> Inserisci controlli su dimensione del dataset, formula della perdita, coerenza dei segni e statistiche empiriche dello shock per evento.

---

## Prompt 8 - Tappa 4: analisi non condizionata

> **Regime B.**
>
> Costruiamo la Tappa 4: analisi non condizionata della perdita $L$.
>
> Calcola statistiche descrittive, quantili principali e probabilità empirica $\mathbb{P}(L>\ell)$. Produci istogramma dello shock, istogramma della perdita ed ECDF della perdita.
>
> Nei grafici monetari usa milioni di euro, evidenzia la soglia $\ell$ e inserisci la linea nera di riferimento a zero quando utile. Inserisci controlli su quantili, probabilità e posizione della media.

---

## Prompt 9 - Tappa 5: analisi condizionata e valore atteso totale

> **Regime B.**
>
> Costruiamo la Tappa 5: analisi condizionata per evento e verifica del valore atteso totale.
>
> Calcola frequenze, medie condizionate $\mathbb{E}[L\mid A_1]$, $\mathbb{E}[L\mid A_2]$, $\mathbb{E}[L\mid A_3]$, deviazioni standard, probabilità condizionate di superamento soglia e quantili condizionati. Costruisci nel dataset la colonna `E_L_cond_G_hat`, costante sui blocchi della partizione.
>
> Verifica la media ricomposta e produci il grafico delle medie condizionate e il confronto tra distribuzioni condizionate della perdita. Nel Markdown distingui $\mathbb{E}[L\mid A_g]$, $\mathbb{E}[L\mid\mathcal{G}]$ e media globale.

---

## Prompt 10 - Tappa 6: interpretazione critica e limiti

> **Regime C.**
>
> Ho preparato questa lettura dei risultati: $A_1$ può generare perdita media negativa perché una riduzione dei rendimenti aumenta il valore del portafoglio obbligazionario; $A_2$ è un regime intermedio; $A_3$ concentra perdita attesa più alta e maggiore dispersione.
>
> Vorrei anche chiarire che l'informazione di regime modifica la distribuzione rilevante ma non elimina l'incertezza, e che il modello resta didattico perché usa l'approssimazione lineare di duration e non considera convessità, curva dei rendimenti, credito, liquidità o dinamica multiperiodale.
>
> Ti chiedo di verificare se questa interpretazione è coerente e di segnalare solo correzioni o cautele necessarie.

---

## Prompt 11 - Controllo finale

> **Regime C.**
>
> Vorrei fare un controllo finale del notebook docente e del tracciato IA.
>
> Controlla che la Scheda Caso sia rispettata, che $A_1,A_2,A_3$ restino eventi della partizione, che $\Delta y$ e $L$ siano distinti, che $L = D V_0 \Delta y$ sia implementata correttamente e che la verifica del valore atteso totale sia presente.
>
> Controlla anche che tabelle e grafici siano leggibili, che i grafici monetari siano in milioni di euro e che i CSV restino numerici. Segnala solo errori, omissioni o correzioni prioritarie.
