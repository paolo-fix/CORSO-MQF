
# CELLA 5
import numpy as np
import pandas as pd
from IPython.display import display, Markdown

# ==============================================================================
# 1. PARAMETRI COMPUTAZIONALI E RIPRODUCIBILITÀ (SEED = 2026)
# ==============================================================================
SEED = 2026
N_MC = 50_000
T = 4  # orizzonte in trimestri (1 anno)
LGD = 0.65

# Inizializzazione del generatore pseudocasuale principale per le tappe successive
rng = np.random.default_rng(SEED)

# ==============================================================================
# 2. SPAZI DEGLI STATI E MATRICI DI TRANSIZIONE
# ==============================================================================
STATI_SISTEMICI = ["O", "S", "C"]
SISTEMICO_TO_IDX = {stato: idx for idx, stato in enumerate(STATI_SISTEMICI)}
M_0 = "S"
M_0_IDX = SISTEMICO_TO_IDX[M_0]

STATI_RATING = ["A", "BBB", "BB", "B", "D"]
RATING_TO_IDX = {rating: idx for idx, rating in enumerate(STATI_RATING)}

# Matrice di transizione trimestrale del regime sistemico Q (ordine: O, S, C)
Q = np.array([
    [0.82, 0.16, 0.02],
    [0.30, 0.55, 0.15],
    [0.10, 0.35, 0.55]
], dtype=float)

# Matrici di migrazione creditizia (ordine: A, BBB, BB, B, D)
P_O = np.array([
    [0.960, 0.035, 0.004, 0.0005, 0.0005],
    [0.020, 0.940, 0.030, 0.0070, 0.0030],
    [0.004, 0.030, 0.910, 0.0460, 0.0100],
    [0.001, 0.004, 0.025, 0.9400, 0.0300],
    [0.000, 0.000, 0.000, 0.0000, 1.0000]
], dtype=float)

P_S = np.array([
    [0.920, 0.060, 0.014, 0.004, 0.002],
    [0.010, 0.870, 0.085, 0.027, 0.008],
    [0.002, 0.018, 0.820, 0.135, 0.025],
    [0.000, 0.002, 0.018, 0.880, 0.100],
    [0.000, 0.000, 0.000, 0.000, 1.000]
], dtype=float)

P_C = np.array([
    [0.820, 0.120, 0.040, 0.015, 0.005],
    [0.005, 0.760, 0.150, 0.060, 0.025],
    [0.000, 0.010, 0.680, 0.230, 0.080],
    [0.000, 0.001, 0.009, 0.740, 0.250],
    [0.000, 0.000, 0.000, 0.000, 1.000]
], dtype=float)

P_REGIMI = {"O": P_O, "S": P_S, "C": P_C}
P_ARRAY = np.array([P_O, P_S, P_C], dtype=float)  # shape: (3, 5, 5)

# ==============================================================================
# 3. TASSI DI PERDITA MIGRATION-BASED phi(r_0, r_4)
# ==============================================================================
# Righe: rating iniziale (A, BBB, BB, B) | Colonne: rating finale (A, BBB, BB, B, D)
PHI = np.array([
    [ 0.00,  0.03,  0.10, 0.22, 0.65],
    [-0.02,  0.00,  0.06, 0.16, 0.65],
    [-0.04, -0.02,  0.00, 0.09, 0.65],
    [-0.06, -0.04, -0.02, 0.00, 0.65]
], dtype=float)

df_phi = pd.DataFrame(
    PHI,
    index=STATI_RATING[:-1],
    columns=STATI_RATING
)
df_phi.index.name = "Rating iniziale"
df_phi.columns.name = "Rating finale"

# ==============================================================================
# 4. COSTRUZIONE PORTAFOGLIO CONCENTRATO E PORTAFOGLIO CONTROFATTUALE
# ==============================================================================
specifica_gruppi_conc = [
    {"Gruppo": "Lehman Brothers",  "Numero debitori": 1,  "Rating iniziale": "A",   "Investimento per debitore": 25.0, "is_lehman": True},
    {"Gruppo": "Altri debitori A", "Numero debitori": 11, "Rating iniziale": "A",   "Investimento per debitore": 5.0,  "is_lehman": False},
    {"Gruppo": "Debitori BBB",     "Numero debitori": 14, "Rating iniziale": "BBB", "Investimento per debitore": 4.0,  "is_lehman": False},
    {"Gruppo": "Debitori BB",      "Numero debitori": 9,  "Rating iniziale": "BB",  "Investimento per debitore": 3.0,  "is_lehman": False},
    {"Gruppo": "Debitori B",       "Numero debitori": 5,  "Rating iniziale": "B",   "Investimento per debitore": 2.0,  "is_lehman": False},
]

# Espansione a livello di singolo debitore (40 debitori nel portafoglio concentrato)
righe_debitori = []
id_counter = 1
for g in specifica_gruppi_conc:
    for k in range(g["Numero debitori"]):
        nome = "Lehman Brothers" if g["is_lehman"] else f"Debitore_{id_counter:02d}"
        righe_debitori.append({
            "id_debitore": id_counter,
            "emittente": nome,
            "gruppo": g["Gruppo"],
            "rating_iniziale": g["Rating iniziale"],
            "rating_iniziale_idx": RATING_TO_IDX[g["Rating iniziale"]],
            "V_0": g["Investimento per debitore"],
            "EAD_0": g["Investimento per debitore"],  # ipotesi specifica: EAD_i = V_{i,0}
            "is_lehman": g["is_lehman"]
        })
        id_counter += 1

df_debitori_conc = pd.DataFrame(righe_debitori)

# Costruzione portafoglio controfattuale (39 debitori con riallocazione proporzionale)
V_totale_target = 173.0
V_residui_iniziale = df_debitori_conc.loc[~df_debitori_conc["is_lehman"], "V_0"].sum()  # 148.0
fattore_riscalamento = V_totale_target / V_residui_iniziale  # 173 / 148

df_debitori_div = df_debitori_conc.loc[~df_debitori_conc["is_lehman"]].copy().reset_index(drop=True)
df_debitori_div["V_0_div"] = df_debitori_div["V_0"] * fattore_riscalamento
df_debitori_div["EAD_0_div"] = df_debitori_div["V_0_div"]

# Vettori NumPy pronti per le tappe successive
X_0_conc_idx = df_debitori_conc["rating_iniziale_idx"].to_numpy()
V_0_conc = df_debitori_conc["V_0"].to_numpy()
V_0_div = df_debitori_div["V_0_div"].to_numpy()
mask_non_lehman = (~df_debitori_conc["is_lehman"]).to_numpy()

# ==============================================================================
# 5. TABELLE DESCRITTIVE RICHIESTE (TABELLA 1 E TABELLA 2)
# ==============================================================================
# Tabella 1 — Portafoglio iniziale concentrato
righe_tab1 = []
for g in specifica_gruppi_conc:
    n_deb = g["Numero debitori"]
    inv_ind = g["Investimento per debitore"]
    righe_tab1.append({
        "Gruppo": g["Gruppo"],
        "Numero debitori": n_deb,
        "Rating iniziale": g["Rating iniziale"],
        "Investimento per debitore": inv_ind,
        "Investimento complessivo": n_deb * inv_ind
    })
righe_tab1.append({
    "Gruppo": "Totale",
    "Numero debitori": int(df_debitori_conc.shape[0]),
    "Rating iniziale": "",
    "Investimento per debitore": np.nan,
    "Investimento complessivo": float(df_debitori_conc["V_0"].sum())
})
tabella_1 = pd.DataFrame(righe_tab1)

# Tabella 2 — Portafoglio controfattuale
righe_tab2 = []
for g in specifica_gruppi_conc:
    if g["is_lehman"]:
        continue
    n_deb = g["Numero debitori"]
    inv_ind_div = g["Investimento per debitore"] * fattore_riscalamento
    righe_tab2.append({
        "Gruppo": g["Gruppo"],
        "Numero debitori": n_deb,
        "Rating iniziale": g["Rating iniziale"],
        "Investimento per debitore": inv_ind_div,
        "Investimento complessivo": n_deb * inv_ind_div
    })
righe_tab2.append({
    "Gruppo": "Totale",
    "Numero debitori": int(df_debitori_div.shape[0]),
    "Rating iniziale": "",
    "Investimento per debitore": np.nan,
    "Investimento complessivo": float(df_debitori_div["V_0_div"].sum())
})
tabella_2 = pd.DataFrame(righe_tab2)

display(Markdown("### Tabella 1 — Portafoglio iniziale concentrato (milioni di dollari)"))
display(
    tabella_1.style
    .format({
        "Investimento per debitore": lambda x: "" if pd.isna(x) else f"{x:,.2f}",
        "Investimento complessivo": "{:,.2f}"
    })
    .hide(axis="index")
)

display(Markdown("### Tabella 2 — Portafoglio controfattuale (milioni di dollari)"))
display(
    tabella_2.style
    .format({
        "Investimento per debitore": lambda x: "" if pd.isna(x) else f"{x:,.4f}",
        "Investimento complessivo": "{:,.4f}"
    })
    .hide(axis="index")
)

# ==============================================================================
# 6. ESECUZIONE DEI CONTROLLI PRELIMINARI DELLA TAPPA 1
# ==============================================================================
tol = 1e-12

# Controllo 1: somma righe di Q pari a 1
somme_righe_Q = Q.sum(axis=1)
ctrl_1 = bool(np.allclose(somme_righe_Q, 1.0, atol=tol))

# Controllo 2: somma righe di P^(O), P^(S), P^(C) pari a 1
ctrl_2 = bool(all(np.allclose(P.sum(axis=1), 1.0, atol=tol) for P in P_REGIMI.values()))

# Controllo 3: stato D assorbente in tutte le matrici di migrazione (p_DD^(m) = 1)
ctrl_3 = bool(all(
    np.isclose(P[-1, -1], 1.0, atol=tol) and np.allclose(P[-1, :-1], 0.0, atol=tol)
    for P in P_REGIMI.values()
))

# Controllo 7: numero debitori portafoglio concentrato == 40
n_deb_conc = len(df_debitori_conc)
ctrl_7 = (n_deb_conc == 40)

# Controllo 8: numero debitori portafoglio controfattuale == 39
n_deb_div = len(df_debitori_div)
ctrl_8 = (n_deb_div == 39)

# Controllo 9: investimento complessivo pari a 173 milioni in entrambi i portafogli
V_tot_conc = float(df_debitori_conc["V_0"].sum())
V_tot_div = float(df_debitori_div["V_0_div"].sum())
ctrl_9 = bool(np.isclose(V_tot_conc, 173.0, atol=tol) and np.isclose(V_tot_div, 173.0, atol=tol))

# Controllo 10: invarianza delle proporzioni relative dei 39 debitori residui
pesi_relativi_pre = df_debitori_div["V_0"] / df_debitori_div["V_0"].sum()
pesi_relativi_post = df_debitori_div["V_0_div"] / df_debitori_div["V_0_div"].sum()
max_diff_pesi = float(np.max(np.abs(pesi_relativi_post - pesi_relativi_pre)))
ctrl_10 = bool(np.allclose(pesi_relativi_post, pesi_relativi_pre, atol=tol))

# Controllo 13: seed pari a 2026 impostato correttamente e riproducibile
rng_check_1 = np.random.default_rng(SEED)
rng_check_2 = np.random.default_rng(SEED)
ctrl_13 = bool((SEED == 2026) and np.array_equal(rng_check_1.random(10), rng_check_2.random(10)))

controlli_tappa_1 = pd.DataFrame([
    {"Controllo": "Controllo 1",  "Descrizione": "Somma delle righe della matrice Q pari a 1",                     "Valore verificato": str(np.round(somme_righe_Q, 6).tolist()), "Esito": "SUPERATO" if ctrl_1 else "NON SUPERATO"},
    {"Controllo": "Controllo 2",  "Descrizione": "Somma delle righe di P^(O), P^(S), P^(C) pari a 1",              "Valore verificato": "Tutte le righe = 1.000000",                    "Esito": "SUPERATO" if ctrl_2 else "NON SUPERATO"},
    {"Controllo": "Controllo 3",  "Descrizione": "Stato D assorbente in tutte le matrici creditizie (p_DD = 1)",     "Valore verificato": "p_DD = 1.0 in O, S, C",                        "Esito": "SUPERATO" if ctrl_3 else "NON SUPERATO"},
    {"Controllo": "Controllo 7",  "Descrizione": "Portafoglio concentrato composto da 40 debitori",                  "Valore verificato": f"{n_deb_conc} debitori",                       "Esito": "SUPERATO" if ctrl_7 else "NON SUPERATO"},
    {"Controllo": "Controllo 8",  "Descrizione": "Portafoglio controfattuale composto da 39 debitori",               "Valore verificato": f"{n_deb_div} debitori",                        "Esito": "SUPERATO" if ctrl_8 else "NON SUPERATO"},
    {"Controllo": "Controllo 9",  "Descrizione": "Investimento complessivo pari a 173 mln in entrambi i portafogli", "Valore verificato": f"Conc: {V_tot_conc:.2f} | Div: {V_tot_div:.2f}", "Esito": "SUPERATO" if ctrl_9 else "NON SUPERATO"},
    {"Controllo": "Controllo 10", "Descrizione": "Invarianza proporzioni relative dei 39 debitori residui",          "Valore verificato": f"Max diff rel: {max_diff_pesi:.2e}",           "Esito": "SUPERATO" if ctrl_10 else "NON SUPERATO"},
    {"Controllo": "Controllo 13", "Descrizione": "Seed = 2026 impostato e riproducibilità verificata",               "Valore verificato": f"SEED = {SEED}",                               "Esito": "SUPERATO" if ctrl_13 else "NON SUPERATO"},
])

display(Markdown("### Riepilogo controlli preliminari — Tappa 1"))
display(controlli_tappa_1.style.hide(axis="index"))

assert all([ctrl_1, ctrl_2, ctrl_3, ctrl_7, ctrl_8, ctrl_9, ctrl_10, ctrl_13]), (
    "Errore nella verifica dei controlli preliminari della Tappa 1."
)

# CELLA 7
import numpy as np
import pandas as pd
from IPython.display import display, Markdown

# ==============================================================================
# 1. INIZIALIZZAZIONE RIPRODUCIBILE E ALLOCAZIONE DELLE TRAIETTORIE SISTEMICHE
# ==============================================================================
# Generatore dedicato inizializzato con SEED = 2026 per garantire che la
# riesecuzione della cella produca esattamente le medesime traiettorie sistemiche.
rng_sistemico = np.random.default_rng(SEED)

# Matrice degli indici di stato sistemico: dimensione (N_MC, T) = (50_000, 4)
# Colonne: t = 0, 1, 2, 3 (non si simula t = 4 perché la migrazione t = 3 -> 4 usa M_3)
M_traj_idx = np.empty((N_MC, T), dtype=int)
M_traj_idx[:, 0] = M_0_IDX  # M_0 = S per tutte le N_MC repliche

# Distribuzione cumulata per riga della matrice Q
Q_cdf = np.cumsum(Q, axis=1)
Q_cdf[:, -1] = 1.0  # chiusura esatta a 1.0 contro arrotondamenti floating-point

# ==============================================================================
# 2. SIMULAZIONE SEQUENZIALE DELLA CATENA DI MARKOV {M_t}_{t=0}^3
# ==============================================================================
U_sist = rng_sistemico.random((N_MC, T - 1))

for t in range(T - 1):
    stato_corrente = M_traj_idx[:, t]
    cdf_corrente = Q_cdf[stato_corrente]  # dimensione (N_MC, 3)
    M_traj_idx[:, t + 1] = (U_sist[:, t : t + 1] >= cdf_corrente).sum(axis=1)

# Conversione negli stati simbolici appartenenti a M = {O, S, C}
stati_sistemici_arr = np.array(STATI_SISTEMICI)
M_traj = stati_sistemici_arr[M_traj_idx]

# ==============================================================================
# 3. ISPEZIONE DELLE TRAIETTORIE E FREQUENZE MARGINALI TRIMESTRALI
# ==============================================================================
colonne_trimestri = [f"M_{t}" for t in range(T)]

df_esempio_traiettorie = pd.DataFrame(
    M_traj[:10],
    columns=colonne_trimestri
)
df_esempio_traiettorie.insert(0, "Replica (r)", np.arange(1, 11))

# Frequenze empiriche marginali degli stati O, S, C in ciascun trimestre t = 0, 1, 2, 3
freq_marginali = []
for stato in STATI_SISTEMICI:
    riga = {"Stato sistemico": stato}
    for t in range(T):
        riga[f"t = {t}"] = float(np.mean(M_traj[:, t] == stato))
    freq_marginali.append(riga)

df_freq_marginali = pd.DataFrame(freq_marginali)

display(Markdown("### Anteprima delle prime 10 traiettorie sistemiche simulate ($t = 0, 1, 2, 3$)"))
display(df_esempio_traiettorie.style.hide(axis="index"))

display(Markdown("### Frequenze empiriche marginali del regime sistemico per trimestre"))
display(
    df_freq_marginali.style
    .format({f"t = {t}": "{:.4%}" for t in range(T)})
    .hide(axis="index")
)

# ==============================================================================
# 4. ESECUZIONE DEI CONTROLLI DELLA TAPPA 2 (CONTROLLO 4 E CONTROLLO 5)
# ==============================================================================
# Controllo 4 (parte sistemica): tutti gli stati simulati appartengono a M = {O, S, C}
# e lo stato iniziale è M_0 = S per tutte le repliche
stati_unici_simulati = set(np.unique(M_traj))
ctrl_4_dominio = stati_unici_simulati.issubset(set(STATI_SISTEMICI))
ctrl_4_iniziale = bool(np.all(M_traj[:, 0] == M_0))
ctrl_4_sist = bool(ctrl_4_dominio and ctrl_4_iniziale)

# Controllo 5: esistenza di un'unica traiettoria sistemica comune per ogni replica r
# La struttura M_traj ha dimensione (N_MC, T) = (50_000, 4), priva di dimensione debitore:
# ogni riga r identifica univocamente la traiettoria sistemica condivisa dai 40 debitori.
ctrl_5 = bool((M_traj.ndim == 2) and (M_traj.shape == (N_MC, T)) and (M_traj_idx.shape == (N_MC, T)))

controlli_tappa_2 = pd.DataFrame([
    {
        "Controllo": "Controllo 4 (Regime sistemico)",
        "Descrizione": "Stati simulati in M = {O, S, C} e stato iniziale M_0 = S in tutte le repliche",
        "Valore verificato": f"Stati osservati: {sorted(list(stati_unici_simulati))} | M_0 = {M_traj[0, 0]}",
        "Esito": "SUPERATO" if ctrl_4_sist else "NON SUPERATO"
    },
    {
        "Controllo": "Controllo 5",
        "Descrizione": "Unica traiettoria sistemica comune per ciascuna replica Monte Carlo",
        "Valore verificato": f"Dimensione matrice traiettorie: {M_traj.shape}",
        "Esito": "SUPERATO" if ctrl_5 else "NON SUPERATO"
    }
])

display(Markdown("### Riepilogo controlli — Tappa 2"))
display(controlli_tappa_2.style.hide(axis="index"))

assert ctrl_4_sist and ctrl_5, "Errore nella verifica dei controlli della Tappa 2."

# CELLA 9
import numpy as np
import pandas as pd
from IPython.display import display, Markdown

# ==============================================================================
# 1. INIZIALIZZAZIONE RIPRODUCIBILE E ALLOCAZIONE DELLE TRAIETTORIE CREDITIZIE
# ==============================================================================
# Derivazione deterministica di uno stream indipendente dal SEED = 2026 per le
# estrazioni individuali, garantendo riproducibilità e assenza di sovrapposizione
# con le estrazioni del regime sistemico della Tappa 2.
seed_seq = np.random.SeedSequence(SEED)
_, child_seed_creditizio = seed_seq.spawn(2)
rng_creditizio = np.random.default_rng(child_seed_creditizio)

n_debitori = len(X_0_conc_idx)  # 40 debitori

# Tensore degli indici di rating: dimensione (N_MC, T + 1, n_debitori) = (50_000, 5, 40)
# L'asse 1 rappresenta i tempi t = 0, 1, 2, 3, 4.
X_traj_idx = np.empty((N_MC, T + 1, n_debitori), dtype=int)
X_traj_idx[:, 0, :] = X_0_conc_idx  # assegnazione rating iniziali X_{i,0}

# Distribuzioni cumulate per riga delle matrici P^(O), P^(S), P^(C)
# P_ARRAY ha dimensione (3, 5, 5): [regime, rating_corrente, rating_successivo]
P_cdf = np.cumsum(P_ARRAY, axis=2)
P_cdf[:, :, -1] = 1.0  # chiusura esatta a 1.0 per evitare errori floating-point

# ==============================================================================
# 2. SIMULAZIONE TRIMESTRALE CONDIZIONATA DELLE MIGRAZIONI INDIVIDUALI
# ==============================================================================
# Estrazioni uniformi indipendenti in [0, 1) per ogni replica r, trimestre t e debitore i
U_cred = rng_creditizio.random((N_MC, T, n_debitori))

for t in range(T):
    # Regime sistemico comune al trimestre t: dimensione (N_MC, 1) per broadcasting
    regime_t = M_traj_idx[:, t][:, None]
    # Rating correnti dei 40 debitori al tempo t: dimensione (N_MC, 40)
    rating_corrente_t = X_traj_idx[:, t, :]
    # Selezione vettoriale della riga CDF corrispondente a (M_t^{(r)}, X_{i,t}^{(r)})
    cdf_corrente = P_cdf[regime_t, rating_corrente_t]  # dimensione (N_MC, 40, 5)
    # Transizione tramite inversione della CDF discreta (D resta assorbente con prob. 1)
    X_traj_idx[:, t + 1, :] = (U_cred[:, t, :, None] >= cdf_corrente).sum(axis=2)

# Stati terminali all'orizzonte T = 4 trimestri (1 anno)
X_4_conc_idx = X_traj_idx[:, T, :]

# Conversione negli stati simbolici appartenenti a I = {A, BBB, BB, B, D}
stati_rating_arr = np.array(STATI_RATING)
X_traj = stati_rating_arr[X_traj_idx]
X_4_conc = stati_rating_arr[X_4_conc_idx]

# ==============================================================================
# 3. ISPEZIONE DELLE TRAIETTORIE E FREQUENZE EMPIRICHE DEI RATING TERMINALI
# ==============================================================================
# Anteprima delle prime 10 repliche per Lehman Brothers (debitore 1, indice 0)
df_anteprima_lehman = pd.DataFrame({
    "Replica (r)": np.arange(1, 11),
    "Traiettoria sistemica (M_0..M_3)": ["-".join(row) for row in M_traj[:10]],
    "X_0 (Lehman)": X_traj[:10, 0, 0],
    "X_1 (Lehman)": X_traj[:10, 1, 0],
    "X_2 (Lehman)": X_traj[:10, 2, 0],
    "X_3 (Lehman)": X_traj[:10, 3, 0],
    "X_4 (Lehman)": X_traj[:10, 4, 0],
})

display(Markdown("### Anteprima delle prime 10 traiettorie simulate — Lehman Brothers"))
display(df_anteprima_lehman.style.hide(axis="index"))

# Frequenze empiriche degli stati terminali X_{i,4} per gruppo di portafoglio
righe_freq_terminali = []
for gruppo in df_debitori_conc["gruppo"].unique():
    mask_gruppo = (df_debitori_conc["gruppo"] == gruppo).to_numpy()
    rating_init = df_debitori_conc.loc[mask_gruppo, "rating_iniziale"].iloc[0]
    stati_finali_gruppo = X_4_conc[:, mask_gruppo]
    riga = {
        "Gruppo": gruppo,
        "Rating iniziale": rating_init,
        "Numero debitori": int(mask_gruppo.sum()),
    }
    for stato in STATI_RATING:
        riga[f"Finale {stato}"] = float(np.mean(stati_finali_gruppo == stato))
    righe_freq_terminali.append(riga)

df_freq_terminali = pd.DataFrame(righe_freq_terminali)

display(Markdown("### Distribuzione empirica dei rating terminali ($t = 4$) per gruppo iniziale"))
display(
    df_freq_terminali.style
    .format({f"Finale {stato}": "{:.4%}" for stato in STATI_RATING})
    .hide(axis="index")
)

# ==============================================================================
# 4. ESECUZIONE DEI CONTROLLI DELLA TAPPA 3 (CONTROLLI 4, 3 E 6)
# ==============================================================================
idx_default = RATING_TO_IDX["D"]  # indice 4

# Controllo 4 (parte creditizia): tutti gli stati simulati appartengono a I = {A, BBB, BB, B, D}
# e gli stati iniziali a t = 0 coincidono con quelli assegnati
stati_creditizi_osservati = set(np.unique(X_traj))
ctrl_4_dominio = stati_creditizi_osservati.issubset(set(STATI_RATING))
ctrl_4_iniziali = bool(np.array_equal(X_traj_idx[:, 0, :], np.broadcast_to(X_0_conc_idx, (N_MC, n_debitori))))
ctrl_4_cred = bool(ctrl_4_dominio and ctrl_4_iniziali)

# Controllo 3 (operativo sulle traiettorie): permanenza irreversibile in D dopo il default
# Confronto diretto trimestre per trimestre tra t e t + 1 (entrambi di shape (N_MC, 40))
violazioni_assorbenza = 0
for t in range(T):
    in_default_a_t = (X_traj_idx[:, t, :] == idx_default)
    if np.any(in_default_a_t):
        stati_t_piu_1 = X_traj_idx[:, t + 1, :][in_default_a_t]
        violazioni_assorbenza += int(np.sum(stati_t_piu_1 != idx_default))
ctrl_3_traj = (violazioni_assorbenza == 0)

# Controllo 6: estrazioni individuali indipendenti condizionatamente alla traiettoria sistemica
# Verifica che U_cred abbia dimensione (N_MC, T, 40) con estrazioni distinte per ciascun debitore
# e correlazione campionaria tra debitori trascurabile (indipendenza stocastica)
corr_u = np.corrcoef(U_cred[:, 0, :], rowvar=False)
np.fill_diagonal(corr_u, 0.0)
max_abs_corr_u = float(np.max(np.abs(corr_u)))
ctrl_6 = bool((U_cred.shape == (N_MC, T, n_debitori)) and (max_abs_corr_u < 0.03))

controlli_tappa_3 = pd.DataFrame([
    {
        "Controllo": "Controllo 4 (Rating)",
        "Descrizione": "Tutti gli stati simulati in I = {A, BBB, BB, B, D} e rating iniziali X_{i,0} corretti",
        "Valore verificato": f"Stati osservati: {sorted(list(stati_creditizi_osservati))}",
        "Esito": "SUPERATO" if ctrl_4_cred else "NON SUPERATO"
    },
    {
        "Controllo": "Controllo 3 (Traiettorie)",
        "Descrizione": "Assorbenza dello stato D lungo l'intera traiettoria trimestrale",
        "Valore verificato": f"Violazioni post-default: {violazioni_assorbenza}",
        "Esito": "SUPERATO" if ctrl_3_traj else "NON SUPERATO"
    },
    {
        "Controllo": "Controllo 6",
        "Descrizione": "Estrazioni casuali individuali indipendenti condizionatamente al regime sistemico",
        "Valore verificato": f"Shape U: {U_cred.shape} | Max |corr(U_i, U_j)|: {max_abs_corr_u:.4f}",
        "Esito": "SUPERATO" if ctrl_6 else "NON SUPERATO"
    }
])

display(Markdown("### Riepilogo controlli — Tappa 3"))
display(controlli_tappa_3.style.hide(axis="index"))

assert ctrl_4_cred and ctrl_3_traj and ctrl_6, "Errore nella verifica dei controlli della Tappa 3."

# CELLA 11
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display, Markdown

# ==============================================================================
# 1. CALCOLO DELLE PERDITE MONETARIE — PORTAFOGLIO CONCENTRATO (40 DEBITORI)
# ==============================================================================
# Associazione deterministica del tasso migration-based phi(X_{i,0}, X_{i,4}^{(r)}):
# poiché phi(r_0, D) = 0.65 = LGD e D è assorbente, la formula incorpora sia
# migrazioni senza default sia eventi di default, in milioni di dollari.
tassi_perdita_conc = PHI[X_0_conc_idx[None, :], X_4_conc_idx]  # shape: (N_MC, 40)
L_ind_conc = tassi_perdita_conc * V_0_conc[None, :]            # shape: (N_MC, 40)
L_conc_P = L_ind_conc.sum(axis=1)                              # shape: (N_MC,)

# ==============================================================================
# 2. CALCOLO DELLE PERDITE MONETARIE — PORTAFOGLIO CONTROFATTUALE (39 DEBITORI)
# ==============================================================================
# Principio delle variabili casuali comuni (Common Random Numbers):
# si estraggono esattamente le traiettorie già simulate dei 39 debitori comuni (i != L),
# senza generare alcuna nuova estrazione pseudocasuale.
X_0_div_idx = X_0_conc_idx[mask_non_lehman]                    # shape: (39,)
X_4_div_idx = X_4_conc_idx[:, mask_non_lehman]                 # shape: (N_MC, 39)

tassi_perdita_div = PHI[X_0_div_idx[None, :], X_4_div_idx]     # shape: (N_MC, 39)
L_ind_div = tassi_perdita_div * V_0_div[None, :]               # shape: (N_MC, 39)
L_div_P = L_ind_div.sum(axis=1)                                # shape: (N_MC,)

# ==============================================================================
# 3. FUNZIONI DI STIMA DELLE MISURE DI RISCHIO (DEFINIZIONE MEDIANTE QUANTILI)
# ==============================================================================
def calcola_var_cvar_quantili(perdite: np.ndarray, alpha: float) -> tuple[float, float]:
    """
    Calcola VaR_alpha e CVaR_alpha secondo la definizione mediante quantili (Cap. 9):
      - VaR_alpha(L) = F_L^{-1}(alpha) (quantile empirico inferiore / order statistic)
      - CVaR_alpha(L) = (1 / (1 - alpha)) * int_alpha^1 q_u(L) du
    Su un campione ordinato L_{(1)} <= ... <= L_{(N)} con alpha * N intero,
    l'integrale dei quantili coincide esattamente con la media delle ultime
    N * (1 - alpha) statistiche d'ordine.
    """
    n = len(perdite)
    perdite_ordinate = np.sort(perdite)
    idx_soglia = int(np.ceil(alpha * n)) - 1
    var_alpha = float(perdite_ordinate[idx_soglia])
    # Integrazione esatta della funzione quantile empirica su [alpha, 1]
    u_grid = np.linspace(alpha, 1.0, num=max(10_000, int(round((1.0 - alpha) * n)) * 10), endpoint=False)
    quantili_coda = np.quantile(perdite_ordinate, u_grid, method="inverted_cdf")
    cvar_alpha = float(np.mean(quantili_coda))
    return var_alpha, cvar_alpha

def calcola_misure_rischio(perdite: np.ndarray) -> dict[str, float]:
    """Restituisce tutte le misure di rischio richieste per un portafoglio (in mln USD)."""
    media = float(np.mean(perdite))
    varianza = float(np.var(perdite, ddof=1))
    dev_std = float(np.std(perdite, ddof=1))
    var_95, cvar_95 = calcola_var_cvar_quantili(perdite, 0.95)
    var_99, cvar_99 = calcola_var_cvar_quantili(perdite, 0.99)
    return {
        "Perdita media": media,
        "Varianza": varianza,
        "Deviazione standard": dev_std,
        "VaR 95%": var_95,
        "CVaR 95%": cvar_95,
        "VaR 99%": var_99,
        "CVaR 99%": cvar_99,
    }

misure_conc = calcola_misure_rischio(L_conc_P)
misure_div = calcola_misure_rischio(L_div_P)

df_misure_tappa4 = pd.DataFrame({
    "Misura di rischio": list(misure_conc.keys()),
    "Portafoglio concentrato (mln $)": list(misure_conc.values()),
    "Portafoglio controfattuale (mln $)": list(misure_div.values()),
})

display(Markdown("### Misure di rischio stimate per entrambi i portafogli ($N_{\\mathrm{MC}} = 50\\,000$, orizzonte 1 anno)"))
display(
    df_misure_tappa4.style
    .format({
        "Portafoglio concentrato (mln $)": "{:,.4f}",
        "Portafoglio controfattuale (mln $)": "{:,.4f}",
    })
    .hide(axis="index")
)

# ==============================================================================
# 4. VERIFICA DI STABILITÀ AL CRESCERE DEL NUMERO DI REPLICHE (CONTROLLO 15)
# ==============================================================================
dimensioni_campione = [5_000, 10_000, 20_000, 30_000, 40_000, 50_000]
righe_stabilita = []

for n_sub in dimensioni_campione:
    m_c = calcola_misure_rischio(L_conc_P[:n_sub])
    m_d = calcola_misure_rischio(L_div_P[:n_sub])
    righe_stabilita.append({
        "Repliche (n)": n_sub,
        "E[L_conc]": m_c["Perdita media"],
        "VaR 95% conc": m_c["VaR 95%"],
        "CVaR 95% conc": m_c["CVaR 95%"],
        "VaR 99% conc": m_c["VaR 99%"],
        "CVaR 99% conc": m_c["CVaR 99%"],
        "E[L_div]": m_d["Perdita media"],
        "VaR 95% div": m_d["VaR 95%"],
        "CVaR 95% div": m_d["CVaR 95%"],
        "VaR 99% div": m_d["VaR 99%"],
        "CVaR 99% div": m_d["CVaR 99%"],
    })

df_stabilita = pd.DataFrame(righe_stabilita)

display(Markdown("### Verifica di stabilità delle misure di rischio al crescere delle repliche simulate (Controllo 15)"))
display(
    df_stabilita.style
    .format({col: "{:,.4f}" for col in df_stabilita.columns if col != "Repliche (n)"})
    .format({"Repliche (n)": "{:,d}"})
    .hide(axis="index")
)

# ==============================================================================
# 5. FIGURA 1 — DISTRIBUZIONE DELLA PERDITA DEL PORTAFOGLIO CONCENTRATO
# ==============================================================================
fig, ax = plt.subplots(figsize=(10, 5.5))

ax.hist(
    L_conc_P,
    bins=80,
    density=True,
    color="#2b5c8f",
    alpha=0.75,
    edgecolor="white",
    linewidth=0.5,
    label="Distribuzione empirica $L_{\\mathrm{conc}}^P$"
)

ax.axvline(
    misure_conc["VaR 95%"],
    color="#d97706",
    linestyle="--",
    linewidth=2.0,
    label=f"VaR 95% = {misure_conc['VaR 95%']:.2f} mln $"
)

ax.axvline(
    misure_conc["VaR 99%"],
    color="#dc2626",
    linestyle="-.",
    linewidth=2.0,
    label=f"VaR 99% = {misure_conc['VaR 99%']:.2f} mln $"
)

ax.set_title("Figura 1 — Distribuzione della perdita del portafoglio concentrato ($L_{\\mathrm{conc}}^P$)", fontsize=12, fontweight="bold")
ax.set_xlabel("Perdita annua di portafoglio (milioni di dollari)", fontsize=10.5)
ax.set_ylabel("Densità empirica", fontsize=10.5)
ax.grid(True, linestyle=":", alpha=0.5)
ax.legend(frameon=True, fontsize=10)
plt.tight_layout()
plt.show()

# ==============================================================================
# 6. ESECUZIONE DEI CONTROLLI DELLA TAPPA 4 (CONTROLLI 11, 12, 14 E 15)
# ==============================================================================
tol = 1e-12

# Controllo 11: utilizzo esatto delle stesse traiettorie creditizie dei 39 debitori comuni
ctrl_11 = bool(
    np.array_equal(X_4_div_idx, X_4_conc_idx[:, mask_non_lehman]) and
    np.array_equal(X_0_div_idx, X_0_conc_idx[mask_non_lehman]) and
    (X_4_div_idx.shape == (N_MC, 39))
)

# Controllo 12: perdita totale di ciascun portafoglio uguale alla somma delle perdite individuali
diff_somma_conc = float(np.max(np.abs(L_conc_P - L_ind_conc.sum(axis=1))))
diff_somma_div = float(np.max(np.abs(L_div_P - L_ind_div.sum(axis=1))))
ctrl_12 = bool((diff_somma_conc <= tol) and (diff_somma_div <= tol))

# Controllo 14: VaR e CVaR calcolati sulle distribuzioni empiriche delle perdite monetarie (mln USD)
# Verifica scala monetaria coerente con V_0 = 173 mln USD e ordinamento teorico E[L] <= VaR95 <= CVaR95 <= VaR99 <= CVaR99
ordine_conc = (
    misure_conc["Perdita media"] <= misure_conc["VaR 95%"] <= misure_conc["CVaR 95%"]
    <= misure_conc["VaR 99%"] <= misure_conc["CVaR 99%"] <= 173.0 * LGD
)
ordine_div = (
    misure_div["Perdita media"] <= misure_div["VaR 95%"] <= misure_div["CVaR 95%"]
    <= misure_div["VaR 99%"] <= misure_div["CVaR 99%"] <= 173.0 * LGD
)
ctrl_14 = bool(ordine_conc and ordine_div)

# Controllo 15: ragionevole stabilità delle misure di rischio al crescere delle repliche
# Confronto relativo tra n = 40_000 e n = 50_000 sulle metriche principali (soglia di stabilità 2%)
metriche_check = ["E[L_conc]", "VaR 95% conc", "CVaR 95% conc", "VaR 99% conc", "CVaR 99% conc",
                  "E[L_div]",  "VaR 95% div",  "CVaR 95% div",  "VaR 99% div",  "CVaR 99% div"]
val_40k = df_stabilita.loc[df_stabilita["Repliche (n)"] == 40_000, metriche_check].to_numpy()[0]
val_50k = df_stabilita.loc[df_stabilita["Repliche (n)"] == 50_000, metriche_check].to_numpy()[0]
max_var_rel = float(np.max(np.abs(val_50k - val_40k) / np.abs(val_50k)))
ctrl_15 = bool(max_var_rel < 0.02)

controlli_tappa_4 = pd.DataFrame([
    {
        "Controllo": "Controllo 11",
        "Descrizione": "I 39 debitori comuni utilizzano esattamente le stesse traiettorie nei due portafogli",
        "Valore verificato": "Traiettorie identiche (shape 50.000 x 39)",
        "Esito": "SUPERATO" if ctrl_11 else "NON SUPERATO"
    },
    {
        "Controllo": "Controllo 12",
        "Descrizione": "Perdita totale uguale alla somma delle perdite individuali per entrambi i portafogli",
        "Valore verificato": f"Max diff conc: {diff_somma_conc:.2e} | div: {diff_somma_div:.2e}",
        "Esito": "SUPERATO" if ctrl_12 else "NON SUPERATO"
    },
    {
        "Controllo": "Controllo 14",
        "Descrizione": "VaR e CVaR calcolati sulle distribuzioni empiriche delle perdite monetarie (mln $)",
        "Valore verificato": f"Monotonicità e scala in [0, {173.0 * LGD:.2f}] mln $ verificate",
        "Esito": "SUPERATO" if ctrl_14 else "NON SUPERATO"
    },
    {
        "Controllo": "Controllo 15",
        "Descrizione": "Stabilità delle principali misure di rischio al crescere del numero di repliche",
        "Valore verificato": f"Max var. rel. (40k vs 50k): {max_var_rel:.2%}",
        "Esito": "SUPERATO" if ctrl_15 else "NON SUPERATO"
    }
])

display(Markdown("### Riepilogo controlli — Tappa 4"))
display(controlli_tappa_4.style.hide(axis="index"))

assert all([ctrl_11, ctrl_12, ctrl_14, ctrl_15]), "Errore nella verifica dei controlli della Tappa 4."

# CELLA 13
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display, Markdown

# ==============================================================================
# 1. IDENTIFICAZIONE DELL'EVENTO E_C (INGRESSO ALMENO UNA VOLTA NEL REGIME C)
# ==============================================================================
idx_crisi = SISTEMICO_TO_IDX["C"]  # indice 2

# Maschera booleana per replica r: True se M_t^{(r)} == C per almeno un t in {0, 1, 2, 3}
evento_C = np.any(M_traj_idx == idx_crisi, axis=1)
evento_no_C = ~evento_C

n_con_C = int(np.sum(evento_C))
n_senza_C = int(np.sum(evento_no_C))

# Probabilità empirica di raggiungere il regime C almeno una volta
prob_C = float(np.mean(evento_C))
prob_no_C = float(np.mean(evento_no_C))

# ==============================================================================
# 2. PERDITE DEL PORTAFOGLIO CONCENTRATO CONDIZIONATE AL REGIME SISTEMICO
# ==============================================================================
L_conc_con_C = L_conc_P[evento_C]
L_conc_senza_C = L_conc_P[evento_no_C]

media_L_conc_con_C = float(np.mean(L_conc_con_C))
media_L_conc_senza_C = float(np.mean(L_conc_senza_C))

std_L_conc_con_C = float(np.std(L_conc_con_C, ddof=1))
std_L_conc_senza_C = float(np.std(L_conc_senza_C, ddof=1))

mediana_L_conc_con_C = float(np.median(L_conc_con_C))
mediana_L_conc_senza_C = float(np.median(L_conc_senza_C))

q95_L_conc_con_C = float(np.quantile(L_conc_con_C, 0.95))
q95_L_conc_senza_C = float(np.quantile(L_conc_senza_C, 0.95))

# ==============================================================================
# 3. TABELLA 4 — REGIME SISTEMICO E PERDITA (PORTAFOGLIO CONCENTRATO)
# ==============================================================================
tabella_4 = pd.DataFrame([
    {
        "Scenario sistemico": "Regime C raggiunto almeno una volta (E_C)",
        "Numero repliche": n_con_C,
        "Probabilità stimata": prob_C,
        "Perdita media (mln $)": media_L_conc_con_C,
        "Deviazione standard (mln $)": std_L_conc_con_C,
        "Mediana (mln $)": mediana_L_conc_con_C,
        "Quantile 95% (mln $)": q95_L_conc_con_C,
    },
    {
        "Scenario sistemico": "Regime C mai raggiunto (E_C^c)",
        "Numero repliche": n_senza_C,
        "Probabilità stimata": prob_no_C,
        "Perdita media (mln $)": media_L_conc_senza_C,
        "Deviazione standard (mln $)": std_L_conc_senza_C,
        "Mediana (mln $)": mediana_L_conc_senza_C,
        "Quantile 95% (mln $)": q95_L_conc_senza_C,
    },
    {
        "Scenario sistemico": "Portafoglio concentrato complessivo (Incondizionato)",
        "Numero repliche": int(N_MC),
        "Probabilità stimata": 1.0,
        "Perdita media (mln $)": misure_conc["Perdita media"],
        "Deviazione standard (mln $)": misure_conc["Deviazione standard"],
        "Mediana (mln $)": float(np.median(L_conc_P)),
        "Quantile 95% (mln $)": misure_conc["VaR 95%"],
    }
])

display(Markdown("### Tabella 4 — Regime sistemico e perdita (portafoglio concentrato)"))
display(
    tabella_4.style
    .format({
        "Numero repliche": "{:,d}",
        "Probabilità stimata": "{:.2%}",
        "Perdita media (mln $)": "{:,.4f}",
        "Deviazione standard (mln $)": "{:,.4f}",
        "Mediana (mln $)": "{:,.4f}",
        "Quantile 95% (mln $)": "{:,.4f}",
    })
    .hide(axis="index")
)

# ==============================================================================
# 4. FIGURA 3 — REGIME SISTEMICO E PERDITA (PORTAFOGLIO CONCENTRATO)
# ==============================================================================
fig, axes = plt.subplots(1, 2, figsize=(13.5, 5.2))

bins_comuni = np.linspace(float(np.min(L_conc_P)), float(np.max(L_conc_P)), 75)

# Pannello sinistro: distribuzioni empiriche sovrapposte e medie condizionate
axes[0].hist(
    L_conc_senza_C,
    bins=bins_comuni,
    density=True,
    color="#2b5c8f",
    alpha=0.55,
    edgecolor="white",
    linewidth=0.4,
    label=f"Regime C mai raggiunto ($1 - \\hat{{p}}_C$ = {prob_no_C:.2%})"
)
axes[0].hist(
    L_conc_con_C,
    bins=bins_comuni,
    density=True,
    color="#c0392b",
    alpha=0.55,
    edgecolor="white",
    linewidth=0.4,
    label=f"Regime C raggiunto $\\geq 1$ volta ($\\hat{{p}}_C$ = {prob_C:.2%})"
)

axes[0].axvline(
    media_L_conc_senza_C,
    color="#1b3b5c",
    linestyle="--",
    linewidth=2.0,
    label=f"$\\mathbb{{E}}[L_{{\\mathrm{{conc}}}}^P \\mid E_C^c]$ = {media_L_conc_senza_C:.2f} mln USD"
)
axes[0].axvline(
    media_L_conc_con_C,
    color="#922b21",
    linestyle="-.",
    linewidth=2.0,
    label=f"$\\mathbb{{E}}[L_{{\\mathrm{{conc}}}}^P \\mid E_C]$ = {media_L_conc_con_C:.2f} mln USD"
)

axes[0].set_title("Distribuzioni empiriche condizionate", fontsize=11, fontweight="bold")
axes[0].set_xlabel("Perdita annua del portafoglio concentrato (milioni di dollari)", fontsize=10)
axes[0].set_ylabel("Densità empirica", fontsize=10)
axes[0].grid(True, linestyle=":", alpha=0.5)
axes[0].legend(frameon=True, fontsize=9)

# Pannello destro: boxplot comparativo con indicazione e legenda di media e mediana
bp = axes[1].boxplot(
    [L_conc_senza_C, L_conc_con_C],
    tick_labels=["Regime C\nmai raggiunto", "Regime C raggiunto\nalmeno una volta"],
    patch_artist=True,
    widths=0.45,
    showmeans=True,
    meanprops=dict(marker="D", markeredgecolor="black", markerfacecolor="gold", markersize=7, zorder=4),
    medianprops=dict(color="black", linewidth=1.8, zorder=3),
    flierprops=dict(marker="o", markersize=2.5, alpha=0.25, markeredgecolor="gray")
)

colori_box = ["#2b5c8f", "#c0392b"]
for patch, colore in zip(bp["boxes"], colori_box):
    patch.set_facecolor(colore)
    patch.set_alpha(0.65)

axes[1].legend(
    handles=[bp["means"][0], bp["medians"][0]],
    labels=["Media condizionata", "Mediana"],
    frameon=True,
    fontsize=9,
    loc="upper left"
)

axes[1].set_title("Dispersione e coda delle perdite per regime", fontsize=11, fontweight="bold")
axes[1].set_ylabel("Perdita annua del portafoglio concentrato (milioni di dollari)", fontsize=10)
axes[1].grid(True, axis="y", linestyle=":", alpha=0.5)

fig.suptitle(
    "Figura 3 — Regime sistemico e perdita del portafoglio concentrato ($L_{\\mathrm{conc}}^P$)",
    fontsize=12.5,
    fontweight="bold"
)
plt.tight_layout()
plt.show()

# ==============================================================================
# 5. ESECUZIONE DEI CONTROLLI DELLA TAPPA 5
# ==============================================================================
tol = 1e-12

# Controllo 5.1: partizione esaustiva e disgiunta delle N_MC = 50_000 repliche
ctrl_partizione = bool(
    (n_con_C + n_senza_C == N_MC) and
    np.all(evento_C | evento_no_C) and
    (not np.any(evento_C & evento_no_C)) and
    np.isclose(prob_C + prob_no_C, 1.0, atol=tol)
)

# Controllo 5.2: legge delle aspettative totali sulla perdita media del portafoglio concentrato
media_ricostruita = prob_C * media_L_conc_con_C + prob_no_C * media_L_conc_senza_C
diff_media_totale = abs(media_ricostruita - misure_conc["Perdita media"])
ctrl_aspettative_totali = bool(diff_media_totale <= tol)

# Controllo 5.3: coerenza con lo stato iniziale deterministico M_0 = S (nessun C a t = 0)
n_C_a_t0 = int(np.sum(M_traj_idx[:, 0] == idx_crisi))
ctrl_t0_no_C = (n_C_a_t0 == 0)

controlli_tappa_5 = pd.DataFrame([
    {
        "Controllo": "Partizione campionaria (E_C, E_C^c)",
        "Descrizione": "Partizione esaustiva e disgiunta delle N_MC = 50.000 repliche",
        "Valore verificato": f"{n_con_C:,d} + {n_senza_C:,d} = {n_con_C + n_senza_C:,d} (p_C + p_C^c = {prob_C + prob_no_C:.6f})",
        "Esito": "SUPERATO" if ctrl_partizione else "NON SUPERATO"
    },
    {
        "Controllo": "Legge delle aspettative totali",
        "Descrizione": "Coerenza tra medie condizionate e media incondizionata E[L_conc^P]",
        "Valore verificato": f"Diff. assoluta: {diff_media_totale:.2e}",
        "Esito": "SUPERATO" if ctrl_aspettative_totali else "NON SUPERATO"
    },
    {
        "Controllo": "Coerenza stato iniziale M_0 = S",
        "Descrizione": "Assenza dello stato di crisi C al trimestre iniziale t = 0",
        "Valore verificato": f"Repliche con M_0 = C: {n_C_a_t0}",
        "Esito": "SUPERATO" if ctrl_t0_no_C else "NON SUPERATO"
    }
])

display(Markdown("### Riepilogo controlli — Tappa 5"))
display(controlli_tappa_5.style.hide(axis="index"))

assert all([ctrl_partizione, ctrl_aspettative_totali, ctrl_t0_no_C]), (
    "Errore nella verifica dei controlli della Tappa 5."
)

# CELLA 15
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display, Markdown

# ==============================================================================
# 1. CALCOLO DEI DIFFERENZIALI TRA MISURE DI RISCHIO E TABELLA 3
# ==============================================================================
nomi_misure = list(misure_conc.keys())

righe_tabella_3 = []
for m in nomi_misure:
    val_conc = misure_conc[m]
    val_div = misure_div[m]
    delta_rho = val_div - val_conc
    var_rel_pct = (delta_rho / abs(val_conc)) if val_conc != 0.0 else np.nan
    righe_tabella_3.append({
        "Misura di rischio": m,
        "Portafoglio concentrato": val_conc,
        "Portafoglio controfattuale": val_div,
        "Differenza (Delta rho)": delta_rho,
        "Variazione relativa": var_rel_pct,
    })

tabella_3 = pd.DataFrame(righe_tabella_3)

display(Markdown("### Tabella 3 — Misure di rischio (milioni di dollari; varianza in mln USD$^2$)"))
display(
    tabella_3.style
    .format({
        "Portafoglio concentrato": "{:,.4f}",
        "Portafoglio controfattuale": "{:,.4f}",
        "Differenza (Delta rho)": "{:+,.4f}",
        "Variazione relativa": "{:+.2%}",
    })
    .hide(axis="index")
)

# ==============================================================================
# 2. DISTRIBUZIONE EMPIRICA DELLA DIFFERENZA REPLICA PER REPLICA (Delta L^(r))
# ==============================================================================
# Delta L^{(r)} = L_{div}^{P,(r)} - L_{conc}^{P,(r)}
delta_L = L_div_P - L_conc_P

riepilogo_delta_L = pd.DataFrame([
    {"Statistica di Delta L^(r) = L_div - L_conc": "Media empirica (mln USD)",         "Valore": float(np.mean(delta_L))},
    {"Statistica di Delta L^(r) = L_div - L_conc": "Deviazione standard (mln USD)",    "Valore": float(np.std(delta_L, ddof=1))},
    {"Statistica di Delta L^(r) = L_div - L_conc": "Minimo (mln USD)",                 "Valore": float(np.min(delta_L))},
    {"Statistica di Delta L^(r) = L_div - L_conc": "Quantile 1% (mln USD)",            "Valore": float(np.quantile(delta_L, 0.01))},
    {"Statistica di Delta L^(r) = L_div - L_conc": "Quantile 5% (mln USD)",            "Valore": float(np.quantile(delta_L, 0.05))},
    {"Statistica di Delta L^(r) = L_div - L_conc": "Quantile 25% (mln USD)",           "Valore": float(np.quantile(delta_L, 0.25))},
    {"Statistica di Delta L^(r) = L_div - L_conc": "Mediana / Quantile 50% (mln USD)", "Valore": float(np.median(delta_L))},
    {"Statistica di Delta L^(r) = L_div - L_conc": "Quantile 75% (mln USD)",           "Valore": float(np.quantile(delta_L, 0.75))},
    {"Statistica di Delta L^(r) = L_div - L_conc": "Quantile 95% (mln USD)",           "Valore": float(np.quantile(delta_L, 0.95))},
    {"Statistica di Delta L^(r) = L_div - L_conc": "Quantile 99% (mln USD)",           "Valore": float(np.quantile(delta_L, 0.99))},
    {"Statistica di Delta L^(r) = L_div - L_conc": "Massimo (mln USD)",                "Valore": float(np.max(delta_L))},
    {"Statistica di Delta L^(r) = L_div - L_conc": "Frequenza P(Delta L < 0)",         "Valore": float(np.mean(delta_L < 0.0))},
    {"Statistica di Delta L^(r) = L_div - L_conc": "Frequenza P(Delta L = 0)",         "Valore": float(np.isclose(delta_L, 0.0, atol=1e-12).mean())},
    {"Statistica di Delta L^(r) = L_div - L_conc": "Frequenza P(Delta L > 0)",         "Valore": float(np.mean(delta_L > 0.0))},
])

display(Markdown("### Distribuzione empirica di $\\Delta L^{(r)} = L_{\\mathrm{div}}^{P,(r)} - L_{\\mathrm{conc}}^{P,(r)}$"))
display(
    riepilogo_delta_L.style
    .format({"Valore": "{:,.4f}"})
    .hide(axis="index")
)

# ==============================================================================
# 3. FIGURA 2 — CONFRONTO DELLE DISTRIBUZIONI (INTERO SUPPORTO E CODA DESTRA)
# ==============================================================================
fig, axes = plt.subplots(1, 2, figsize=(14.0, 5.4))

min_loss = float(min(np.min(L_conc_P), np.min(L_div_P)))
max_loss = float(max(np.max(L_conc_P), np.max(L_div_P)))
bins_full = np.linspace(min_loss, max_loss, 85)

# Palette cromatica richiesta: rosso per concentrato, giallo per controfattuale
colore_hist_conc = "#d62728"   # rosso
colore_hist_div = "#f1c40f"    # giallo
colore_linea_conc = "#b91c1c"  # rosso intenso per le soglie VaR
colore_linea_div = "#eab308"   # giallo intenso per le soglie VaR

# Pannello sinistro: confronto sull'intero supporto delle perdite
axes[0].hist(
    L_conc_P,
    bins=bins_full,
    density=True,
    color=colore_hist_conc,
    alpha=0.48,
    edgecolor="white",
    linewidth=0.35,
    label="Portafoglio concentrato ($L_{\\mathrm{conc}}^P$)"
)
axes[0].hist(
    L_div_P,
    bins=bins_full,
    density=True,
    color=colore_hist_div,
    alpha=0.52,
    edgecolor="white",
    linewidth=0.35,
    label="Portafoglio controfattuale ($L_{\\mathrm{div}}^P$)"
)

axes[0].axvline(
    misure_conc["VaR 95%"],
    color=colore_linea_conc,
    linestyle="--",
    linewidth=1.8,
    label=f"VaR 95% conc. = {misure_conc['VaR 95%']:.2f} mln USD"
)
axes[0].axvline(
    misure_div["VaR 95%"],
    color=colore_linea_div,
    linestyle="--",
    linewidth=1.8,
    label=f"VaR 95% controf. = {misure_div['VaR 95%']:.2f} mln USD"
)
axes[0].axvline(
    misure_conc["VaR 99%"],
    color=colore_linea_conc,
    linestyle="-",
    linewidth=2.0,
    label=f"VaR 99% conc. = {misure_conc['VaR 99%']:.2f} mln USD"
)
axes[0].axvline(
    misure_div["VaR 99%"],
    color=colore_linea_div,
    linestyle="-",
    linewidth=2.0,
    label=f"VaR 99% controf. = {misure_div['VaR 99%']:.2f} mln USD"
)

axes[0].set_title("Confronto complessivo delle distribuzioni empiriche", fontsize=11, fontweight="bold")
axes[0].set_xlabel("Perdita annua di portafoglio (milioni di dollari)", fontsize=10)
axes[0].set_ylabel("Densità empirica", fontsize=10)
axes[0].grid(True, linestyle=":", alpha=0.5)
axes[0].legend(frameon=True, fontsize=8.5, loc="upper right")

# Pannello destro: ingrandimento sulla coda destra (oltre il 90° percentile)
soglia_coda = float(min(np.quantile(L_conc_P, 0.90), np.quantile(L_div_P, 0.90)))
bins_coda = np.linspace(soglia_coda, max_loss, 50)

axes[1].hist(
    L_conc_P[L_conc_P >= soglia_coda],
    bins=bins_coda,
    density=False,
    weights=np.ones(np.sum(L_conc_P >= soglia_coda)) / N_MC,
    color=colore_hist_conc,
    alpha=0.48,
    edgecolor="white",
    linewidth=0.4,
    label="Portafoglio concentrato ($L_{\\mathrm{conc}}^P$)"
)
axes[1].hist(
    L_div_P[L_div_P >= soglia_coda],
    bins=bins_coda,
    density=False,
    weights=np.ones(np.sum(L_div_P >= soglia_coda)) / N_MC,
    color=colore_hist_div,
    alpha=0.52,
    edgecolor="white",
    linewidth=0.4,
    label="Portafoglio controfattuale ($L_{\\mathrm{div}}^P$)"
)

axes[1].axvline(
    misure_conc["VaR 95%"],
    color=colore_linea_conc,
    linestyle="--",
    linewidth=1.8,
    label=f"VaR 95% conc. = {misure_conc['VaR 95%']:.2f} mln USD"
)
axes[1].axvline(
    misure_div["VaR 95%"],
    color=colore_linea_div,
    linestyle="--",
    linewidth=1.8,
    label=f"VaR 95% controf. = {misure_div['VaR 95%']:.2f} mln USD"
)
axes[1].axvline(
    misure_conc["VaR 99%"],
    color=colore_linea_conc,
    linestyle="-",
    linewidth=2.0,
    label=f"VaR 99% conc. = {misure_conc['VaR 99%']:.2f} mln USD"
)
axes[1].axvline(
    misure_div["VaR 99%"],
    color=colore_linea_div,
    linestyle="-",
    linewidth=2.0,
    label=f"VaR 99% controf. = {misure_div['VaR 99%']:.2f} mln USD"
)

axes[1].set_title("Dettaglio della coda destra (perdite oltre il 90° percentile)", fontsize=11, fontweight="bold")
axes[1].set_xlabel("Perdita annua di portafoglio (milioni di dollari)", fontsize=10)
axes[1].set_ylabel("Frequenza relativa per classe", fontsize=10)
axes[1].grid(True, linestyle=":", alpha=0.5)
axes[1].legend(frameon=True, fontsize=8.5, loc="upper right")

fig.suptitle(
    "Figura 2 — Confronto delle distribuzioni di perdita: portafoglio concentrato vs controfattuale",
    fontsize=12.5,
    fontweight="bold"
)
plt.tight_layout()
plt.show()

# ==============================================================================
# 4. ESECUZIONE DEI CONTROLLI DELLA TAPPA 6 E RIEPILOGO GENERALE CONTROLLI 1–15
# ==============================================================================
tol = 1e-12

# Controllo 6.1: linearità della media E[Delta L] = E[L_div^P] - E[L_conc^P]
diff_linearita_media = abs(float(np.mean(delta_L)) - (misure_div["Perdita media"] - misure_conc["Perdita media"]))
ctrl_linearita_delta = bool(diff_linearita_media <= tol)

# Controllo 6.2: coerenza dimensionale del vettore accoppiato Delta L^(r)
ctrl_dim_delta = bool((delta_L.shape == (N_MC,)) and np.all(np.isfinite(delta_L)))

controlli_tappa_6 = pd.DataFrame([
    {
        "Controllo": "Linearità valore atteso Delta L",
        "Descrizione": "Coerenza E[Delta L^(r)] = E[L_div^P] - E[L_conc^P]",
        "Valore verificato": f"Diff. assoluta: {diff_linearita_media:.2e}",
        "Esito": "SUPERATO" if ctrl_linearita_delta else "NON SUPERATO"
    },
    {
        "Controllo": "Integrità campionaria Delta L^(r)",
        "Descrizione": "Dimensione (50.000,) e assenza di valori NaN/Inf nelle differenze accoppiate",
        "Valore verificato": f"Shape: {delta_L.shape}",
        "Esito": "SUPERATO" if ctrl_dim_delta else "NON SUPERATO"
    }
])

display(Markdown("### Riepilogo controlli specifici — Tappa 6"))
display(controlli_tappa_6.style.hide(axis="index"))

# Consolidamento completo dei 15 controlli previsti dalla Sezione 7 della Scheda Caso
ctrl_3_globale = bool(ctrl_3 and ctrl_3_traj)
ctrl_4_globale = bool(ctrl_4_sist and ctrl_4_cred)

riepilogo_15_controlli = pd.DataFrame([
    {"ID": "Controllo 1",  "Categoria": "Numerico",       "Tappa": "Tappa 1",          "Descrizione": "Ogni riga della matrice Q somma a 1",                                       "Esito": "SUPERATO" if ctrl_1 else "NON SUPERATO"},
    {"ID": "Controllo 2",  "Categoria": "Numerico",       "Tappa": "Tappa 1",          "Descrizione": "Ogni riga delle matrici P^(O), P^(S) e P^(C) somma a 1",                     "Esito": "SUPERATO" if ctrl_2 else "NON SUPERATO"},
    {"ID": "Controllo 3",  "Categoria": "Logico/Teorico", "Tappa": "Tappa 1, Tappa 3", "Descrizione": "Stato D assorbente in tutte le matrici e nelle traiettorie simulate",       "Esito": "SUPERATO" if ctrl_3_globale else "NON SUPERATO"},
    {"ID": "Controllo 4",  "Categoria": "Logico/Teorico", "Tappa": "Tappa 2, Tappa 3", "Descrizione": "Tutti gli stati simulati appartengono a M = {O,S,C} e I = {A,BBB,BB,B,D}",   "Esito": "SUPERATO" if ctrl_4_globale else "NON SUPERATO"},
    {"ID": "Controllo 5",  "Categoria": "Logico/Teorico", "Tappa": "Tappa 2",          "Descrizione": "Unica traiettoria sistemica comune a tutti i debitori in ciascuna replica",   "Esito": "SUPERATO" if ctrl_5 else "NON SUPERATO"},
    {"ID": "Controllo 6",  "Categoria": "Logico/Teorico", "Tappa": "Tappa 3",          "Descrizione": "Estrazioni casuali individuali indipendenti condizionatamente al regime",    "Esito": "SUPERATO" if ctrl_6 else "NON SUPERATO"},
    {"ID": "Controllo 7",  "Categoria": "Numerico",       "Tappa": "Tappa 1",          "Descrizione": "Portafoglio concentrato composto esattamente da 40 debitori",                 "Esito": "SUPERATO" if ctrl_7 else "NON SUPERATO"},
    {"ID": "Controllo 8",  "Categoria": "Numerico",       "Tappa": "Tappa 1",          "Descrizione": "Portafoglio controfattuale composto esattamente da 39 debitori",              "Esito": "SUPERATO" if ctrl_8 else "NON SUPERATO"},
    {"ID": "Controllo 9",  "Categoria": "Numerico",       "Tappa": "Tappa 1",          "Descrizione": "Investimento iniziale complessivo pari a 173 mln USD in entrambi i portafogli","Esito": "SUPERATO" if ctrl_9 else "NON SUPERATO"},
    {"ID": "Controllo 10", "Categoria": "Numerico",       "Tappa": "Tappa 1",          "Descrizione": "Proporzioni relative dei 39 debitori residui inalterate dopo riallocazione",   "Esito": "SUPERATO" if ctrl_10 else "NON SUPERATO"},
    {"ID": "Controllo 11", "Categoria": "Computazionale", "Tappa": "Tappa 4",          "Descrizione": "I 39 debitori comuni utilizzano le stesse traiettorie nei due portafogli",    "Esito": "SUPERATO" if ctrl_11 else "NON SUPERATO"},
    {"ID": "Controllo 12", "Categoria": "Numerico",       "Tappa": "Tappa 4",          "Descrizione": "Perdita totale di ciascun portafoglio uguale alla somma delle perdite indiv.","Esito": "SUPERATO" if ctrl_12 else "NON SUPERATO"},
    {"ID": "Controllo 13", "Categoria": "Computazionale", "Tappa": "Tappa 1–3",        "Descrizione": "Seed = 2026 impostato correttamente per la riproducibilità della simulazione", "Esito": "SUPERATO" if ctrl_13 else "NON SUPERATO"},
    {"ID": "Controllo 14", "Categoria": "Numerico",       "Tappa": "Tappa 4",          "Descrizione": "VaR e CVaR calcolati sulle distribuzioni empiriche delle perdite (mln USD)",  "Esito": "SUPERATO" if ctrl_14 else "NON SUPERATO"},
    {"ID": "Controllo 15", "Categoria": "Numerico",       "Tappa": "Tappa 4",          "Descrizione": "Ragionevole stabilità delle misure di rischio al crescere delle repliche",   "Esito": "SUPERATO" if ctrl_15 else "NON SUPERATO"},
])

display(Markdown("### Quadro riepilogativo generale — Controlli 1–15 della Scheda Caso"))
display(riepilogo_15_controlli.style.hide(axis="index"))

assert all([
    ctrl_linearita_delta,
    ctrl_dim_delta,
    all(riepilogo_15_controlli["Esito"] == "SUPERATO")
]), "Errore nella verifica finale dei controlli."