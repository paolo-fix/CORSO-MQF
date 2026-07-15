# MQF - Catalogo dei template

## Funzione

Questo catalogo è il punto di ingresso unico per i modelli riutilizzabili del progetto MQF. Le Guidelines definiscono le regole; i file elencati qui contengono le strutture operative canoniche.

Ogni template usa il formato nativo del prodotto cui è destinato:

- `.tex` per contenuti da inserire nel manuale o nelle slides;
- `.md` per prompt, schede e documenti operativi;
- `.ipynb` per eventuali notebook base futuri;
- `.py` per eventuali strutture canoniche di script future.

Il formato del template dipende dal documento nel quale viene conservato e utilizzato, non dal formato dell'output richiesto all'IA.

## Template disponibili

| Ambito | Template | Destinazione | Fonte normativa |
|---|---|---|---|
| Manuale | [Sezioni degli esercizi](LaTeX/MQF_Template_Sezioni_Esercizi_Manuale.tex) | Capitoli teorici LaTeX | Guidelines 9.1.1 |
| Lezioni applicative | [Sviluppo della lezione applicativa](Markdown/MQF_Template_Sviluppo_Lezione_Applicativa.md) | Avvio della progettazione docente | Guidelines 12, 14 e 15 |
| Casi applicativi | [Scheda Costruzione Caso](Markdown/MQF_Template_Scheda_Costruzione_Caso_Applicativo.md) | Caso aula o take-home | Guidelines 14.2 |
| Prompt | [Prompt zero](Markdown/MQF_Template_Prompt_Zero.md) | Inizializzazione della chat | Guidelines 15.6 |
| Prompt | [Prompt 1](Markdown/MQF_Template_Prompt_1.md) | Acquisizione della Scheda Caso | Guidelines 15.6 |
| Prompt | [Prompt 2](Markdown/MQF_Template_Prompt_2.md) | Flusso logico-teorico | Guidelines 15.6 |
| Prompt | [Prompt 3](Markdown/MQF_Template_Prompt_3.md) | Scomposizione input-output | Guidelines 15.6 |
| Prompt di tappa | [Regime A](Markdown/MQF_Template_Prompt_Tappa_Regime_A.md) | Ricognizione teorico-modellistica | Guidelines 15.7 |
| Prompt di tappa | [Regime B](Markdown/MQF_Template_Prompt_Tappa_Regime_B.md) | Traduzione operativa in codice | Guidelines 15.7 |
| Prompt di tappa | [Regime C](Markdown/MQF_Template_Prompt_Tappa_Regime_C.md) | Verifica critica | Guidelines 15.7 |

## Regole di manutenzione

1. Il catalogo descrive e collega i template, ma non ne duplica il contenuto.
2. Un nuovo template deve essere aggiunto nel formato nativo appropriato e registrato in questa tabella.
3. Le istanze riferite a una singola lezione restano nella cartella della lezione e non vengono collocate tra i template.
4. Lo stato di consolidamento dei template appartiene a `MQF_Stato_Avanzamento.md`, non a questo catalogo.
5. Le modifiche normative devono essere recepite prima nelle Guidelines e poi nel template interessato.
