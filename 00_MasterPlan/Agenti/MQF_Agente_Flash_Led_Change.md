# MQF - Agente Flash Led Change

## Scopo

L'agente Flash Led Change e' un audit differenziale mirato. Non aggiorna
direttamente `MQF_Stato_Avanzamento.md`; misura invece quanto il progetto
corrente si sia allontanato da cio' che lo Stato di Avanzamento dichiara.

Quando il cambiamento supera una soglia critica, l'agente segnala
l'opportunita' di lanciare l'agente Stato di Avanzamento.

Il suo compito e' rispondere alla domanda:

```text
Le novita' accumulate sono abbastanza importanti da giustificare una revisione
intelligente dello stato del progetto?
```

## Relazione con l'agente Stato di Avanzamento

Flash Led Change non sostituisce l'agente Stato di Avanzamento.

- Flash Led Change misura il segnale differenziale rispetto allo Stato.
- Stato di Avanzamento legge, interpreta, verifica e aggiorna.

Il primo deve essere piu' rapido del secondo, ma non meccanico: deve leggere
quanto basta per evitare falsi allarmi e falsi silenzi. Il secondo resta la
revisione completa, accurata e argomentata.

## Fonti di segnale

L'agente puo' osservare:

- `git status --short`;
- `git diff --stat`;
- `git diff --name-only`;
- `git log` dei commit successivi allo snapshot corrente dello Stato di
  Avanzamento;
- `git show --stat --name-only` dei commit candidati;
- differenze rispetto all'ultimo commit;
- differenze rispetto a `MQF_Stato_Avanzamento.md`;
- modifiche a manuale, slides, codice, grafici, templates, Guidelines e Master
  Plan;
- nuovi file non tracciati;
- output tecnici recenti, se disponibili, come PDF compilati, figure generate o
  script aggiunti.

L'agente non deve basarsi solo sul numero di file modificati o sullo stato del
worktree. Un worktree pulito non implica che lo Stato di Avanzamento sia
aggiornato: le novita' rilevanti possono essere gia' state salvate in commit
recenti.

La baseline principale non e' l'ultimo commit, ma il contenuto corrente di
`MQF_Stato_Avanzamento.md`: cio' che lo Stato dichiara gia' realizzato,
parziale, aperto o prioritario.

## Procedura obbligatoria

Ogni esecuzione di Flash Led Change deve seguire questa sequenza minima:

1. leggere `MQF_Stato_Avanzamento.md`;
2. individuare lo snapshot dichiarato nello Stato;
3. leggere `git status --short --untracked-files=all`;
4. leggere i commit successivi allo snapshot o comunque i commit recenti non
   ancora riflessi nello Stato;
5. selezionare i file candidati per rilevanza didattica o progettuale;
6. leggere nel merito i file candidati, almeno tramite struttura, sezioni,
   esercizi, figure, prompt, istruzioni, output e riferimenti;
7. confrontare cio' che i file mostrano con cio' che lo Stato dichiara;
8. stimare solo la novita' non assorbita dallo Stato.

Se il worktree e' pulito, Flash deve comunque controllare la cronologia recente.
Se trova commit come "completato capitolo", "aggiornate istruzioni",
"predisposte slides", "aggiunti esercizi" o simili, deve leggerli come segnali
forti e confrontarli con lo Stato.

## Antifalso allarme e antifalso silenzio

Flash deve evitare due errori:

- falso allarme: dare punteggio alto a modifiche gia' pienamente assorbite
  nello Stato;
- falso silenzio: dare punteggio basso solo perche' non ci sono modifiche non
  committate.

Il caso-guida e':

```text
Worktree pulito, ma commit recenti completano Capitolo 9 e aggiornano
Istruzioni Studente / Prompt 1, mentre lo Stato dichiara ancora Lezione 9 come
traccia.
```

In questo caso Flash deve dare soglia alta, perche' esiste lavoro concluso non
registrato nello Stato.

## Indicatore FLC

L'indicatore FLC misura la rilevanza del cambiamento su scala 0-100.

La rilevanza non coincide con il numero di file modificati. Per MQF, una novita'
e' rilevante soprattutto quando segnala:

- molto lavoro gia' concluso;
- molto lavoro nuovo generato;
- rischio di dover rifare lavoro;
- cambiamento di priorita', sequenza o struttura didattica;
- perdita di coerenza fra stato, Master Plan, Guidelines e materiali.

La formula operativa e':

```text
FLC = min(100, L_concluso + L_generato + R_rilavorazione
               + I_didattico + C_coerenza + U_urgenza)
```

Il calcolo non deve essere meccanico. Le componenti servono a guidare il
giudizio; il punteggio finale deve essere normalizzato chiedendosi quante ore o
giornate di lavoro rappresenta il segnale.

Indicativamente:

- `0-24`: meno di un'ora di lavoro o nessun rischio rilevante;
- `25-44`: poche ore di lavoro, ma senza impatto strategico;
- `45-64`: mezza giornata circa o rischio di disallineamento circoscritto;
- `65-84`: una giornata o piu' di lavoro concluso/generato, oppure rischio di
  rilavorazione significativo;
- `85-100`: piu' giornate di lavoro, cambio progettuale, o rischio concreto di
  proseguire su una base superata.

## Componenti dell'indicatore

### L_concluso: lavoro concluso non ancora registrato

Misura quanto lavoro significativo sembra essere stato completato dopo l'ultimo
aggiornamento dello stato.

- 0 punti: nessun lavoro concluso.
- 10 punti: piccoli completamenti locali.
- 20 punti: completata una parte riconoscibile, come esercizi, figure o una
  sezione.
- 30 punti: completata una componente didattica importante, come slides,
  capitolo, pacchetto codice o materiali studente.
- 40 punti: completata o ristrutturata una lezione intera.

Un commit gia' acquisito nel repository puo' contribuire a `L_concluso` se il
suo contenuto non e' ancora rappresentato nello Stato di Avanzamento.

### L_generato: lavoro nuovo reso necessario

Misura quanto lavoro futuro e' stato creato da una modifica recente.

- 0 punti: nessun lavoro aggiuntivo.
- 10 punti: controlli o rifiniture locali.
- 20 punti: nuove verifiche tecniche, compilazioni, figure o riferimenti da
  riallineare.
- 30 punti: aggiornamenti necessari su piu' componenti, per esempio manuale,
  slides, Master Plan e Guidelines.
- 40 punti: nuova catena di lavoro sostanziale, come una lezione da ripensare,
  un caso applicativo da completare o materiali studente da ricostruire.

### R_rilavorazione: rischio di lavoro da rifare

Misura il rischio che procedere senza aggiornare lo stato provochi errori,
duplicazioni o scelte basate su informazioni vecchie.

- 0 punti: rischio nullo.
- 10 punti: rischio locale e facilmente correggibile.
- 20 punti: rischio di duplicare controlli o perdere una decisione recente.
- 30 punti: rischio di costruire nuovo materiale su una struttura superata.
- 40 punti: rischio di dover rifare una parte consistente del progetto.

### I_didattico: impatto sugli obiettivi formativi

Misura se la modifica cambia cio' che lo studente deve fare, capire o
consegnare.

- 0 punti: nessun impatto didattico.
- 10 punti: chiarimento locale.
- 20 punti: nuovi esempi, esercizi, figure o passaggi concettuali.
- 30 punti: modifica alla struttura di una lezione o alla progressione degli
  obiettivi.
- 40 punti: cambio di impostazione didattica, valutazione, take-home, prompt o
  ruolo dell'IA.

### C_coerenza: rischio di disallineamento progettuale

Misura quanto le novita' possono rendere incoerenti Stato, Master Plan,
Guidelines, manuale, slides, codice e materiali studente.

- 0 punti: nessun disallineamento.
- 10 punti: disallineamento descrittivo locale.
- 20 punti: una componente principale non e' piu' allineata allo stato.
- 30 punti: piu' componenti raccontano versioni diverse della stessa lezione.
- 40 punti: Master Plan o Guidelines sono superati rispetto al lavoro svolto.

Se una lezione e' indicata come `traccia` nello Stato ma il capitolo corrente
risulta sostanzialmente sviluppato, `C_coerenza` deve essere alto anche in
assenza di modifiche non committate.

### U_urgenza: costo di rimandare l'aggiornamento

Misura quanto diventa costoso aspettare.

- 0 punti: l'aggiornamento puo' attendere.
- 10 punti: conviene aggiornare entro fine sessione.
- 20 punti: conviene aggiornare prima del prossimo blocco di lavoro.
- 30 punti: conviene aggiornare prima di compilare, pubblicare o fare commit.
- 40 punti: conviene fermarsi e aggiornare subito.

## Lettura dell'indicatore

L'indicatore deve essere interpretato come costo-opportunita':

```text
Quanto costa non aggiornare lo stato adesso?
```

Un FLC alto puo' derivare da due casi molto diversi:

- molto lavoro concluso che merita di essere registrato;
- molto lavoro futuro o rischio di rilavorazione che conviene governare subito.

Il report deve quindi indicare sempre se il segnale e' soprattutto:

- `lavoro concluso`;
- `lavoro generato`;
- `rischio di rilavorazione`;
- `disallineamento progettuale`;
- `urgenza operativa`.

## Soglie

- `0-24`: nessuna azione. Il cambiamento e' ordinario.
- `25-44`: segnale debole. Annotare mentalmente; non serve ancora aggiornare.
- `45-64`: soglia di attenzione. Suggerire una verifica mirata.
- `65-84`: soglia critica. Raccomandare di lanciare l'agente Stato di
  Avanzamento sulla componente coinvolta.
- `85-100`: soglia urgente. Raccomandare aggiornamento prima di proseguire con
  nuove modifiche, per evitare perdita di coerenza.

La soglia iniziale consigliata per MQF e' `65`.

## Output dell'agente

L'agente deve produrre un report breve:

```text
FLC: 72/100 - soglia critica superata.
Segnale dominante: lavoro concluso + disallineamento progettuale.
Stima lavoro-tempo: circa una giornata di lavoro gia' incorporata nei materiali
e non ancora riflessa stabilmente nello stato.
Motivo: nuove slides Lez. 8, modifiche al capitolo, figura nuova, Master Plan
da riallineare.
Componente consigliata: Lezione 8.
Azione consigliata: lanciare Agente Stato di Avanzamento su Lezione 8.
```

Il report deve distinguere:

- componenti coinvolte;
- tipo di novita';
- se la novita' e' nel worktree o in commit recenti gia' acquisiti;
- cosa e' gia' assorbito dallo Stato e cosa non lo e';
- rischio di disallineamento;
- azione consigliata.

## Regole operative

Flash Led Change puo' essere eseguito spesso, anche dopo sessioni brevi.

Non deve:

- modificare file;
- decidere lo stato finale di una lezione;
- sostituire la lettura dei materiali;
- proporre aggiornamenti granulari allo stato.

Deve:

- essere rapido;
- segnalare quando il cambiamento e' diventato significativo;
- evitare falsi allarmi per modifiche puramente tecniche o ausiliarie;
- evitare falsi silenzi quando il worktree e' pulito ma la cronologia recente
  contiene lavoro non registrato nello Stato;
- privilegiare il rischio didattico e progettuale rispetto al conteggio dei
  file.

## Comandi di attivazione

Esempi:

- "Usa Flash Led Change."
- "Controlla se le novita' superano la soglia FLC."
- "Misura il cambiamento dall'ultimo stato di avanzamento."
- "Prima di lavorare ancora, dimmi se devo aggiornare lo stato."

## Regola semi-automatica

L'agente puo' essere usato in due modalita':

### A. Attivazione su richiesta

L'utente chiede esplicitamente:

```text
Usa Flash Led Change.
```

In questo caso l'agente calcola subito il segnale e produce un report breve.

La prima implementazione manuale e':

```powershell
conda run -n quick_env python github-publish-client/flash_led_change.py
```

Lo script si trova in `github-publish-client/`, accanto agli strumenti
operativi di pubblicazione del progetto. Per impostazione predefinita stampa
solo il report e restituisce exit code 0 anche quando la soglia e' superata.

### B. Attivazione periodica all'apertura del progetto

Ogni due giorni, al primo avvio del lavoro in VS Code su questo progetto, puo'
partire un controllo automatico leggero.

La logica consigliata e':

1. VS Code apre la cartella del progetto.
2. Un task automatico esegue uno script leggero.
3. Lo script legge una piccola memoria locale, per esempio
   `.agents/flash_led_change_state.json`.
4. Se l'ultimo controllo e' piu' vecchio di due giorni, calcola un pre-segnale
   FLC.
5. Se il pre-segnale supera la soglia, produce un avviso.
6. Se il pre-segnale e' sotto soglia, aggiorna solo la data dell'ultimo
   controllo e non disturba l'utente.

L'avviso puo' essere realizzato in modo progressivo:

- livello minimo: messaggio chiaro nel terminale del task;
- livello intermedio: generazione di un report Markdown in
  `.agents/reports/flash_led_change_last.md`;
- livello avanzato: warning nel pannello Problems di VS Code tramite problem
  matcher;
- livello massimo: estensione VS Code dedicata o integrazione esterna, da
  valutare solo se serve davvero.

La prima versione consigliata e' il livello intermedio: terminale + report
Markdown. E' semplice, tracciabile e non invasiva.

Lo script automatico non deve mai modificare `MQF_Stato_Avanzamento.md`. Deve
solo segnalare:

```text
Flash Led Change: soglia superata.
Suggerimento: lanciare l'agente Stato di Avanzamento su ...
```

## Evoluzione possibile

In una fase successiva l'indicatore puo' diventare uno script Python che legge:

- `git diff --name-only`;
- `git diff --stat`;
- mappa dei file rispetto alle lezioni;
- timestamp o commit dell'ultimo aggiornamento dello stato;
- parole chiave come "TODO", "Da fare", "Aperture residue", "Compilazione",
  "Guidelines", "Master Plan".

Per ora la versione consigliata e' semi-automatica: l'agente calcola il segnale
quando viene invocato e propone, se serve, l'esecuzione dell'agente Stato di
Avanzamento.
