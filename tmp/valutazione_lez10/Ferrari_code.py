
# CELLA 5
import numpy as np
import pandas as pd
from IPython.display import display, Markdown

# ==============================================================================
# 1. DEFINIZIONE DEGLI SPAZI DEGLI STATI E DELLO STATO SISTEMICO INIZIALE
# ==============================================================================
REGIME_STATES = ["O", "S", "C"]
regime_to_idx = {state: idx for idx, state in enumerate(REGIME_STATES)}

RATING_STATES = ["A", "BBB", "BB", "B", "D"]
rating_to_idx = {state: idx for idx, state in enumerate(RATING_STATES)}

# Stato iniziale del regime sistemico (giugno 2008: stress finanziario)
M0 = "S"
M0_idx = regime_to_idx[M0]

# ==============================================================================
# 2. MATRICE DI TRANSIZIONE DEL REGIME SISTEMICO (Q)
# ==============================================================================
# Ordine degli stati: (O, S, C)
Q = np.array([
    [0.82, 0.16, 0.02],
    [0.30, 0.55, 0.15],
    [0.10, 0.35, 0.55]
], dtype=float)

# ==============================================================================
# 3. MATRICI DI MIGRAZIONE CREDITIZIA CONDIZIONATE AL REGIME (P^(O), P^(S), P^(C))
# ==============================================================================
# Ordine degli stati: (A, BBB, BB, B, D)
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

P_matrices = {
    "O": P_O,
    "S": P_S,
    "C": P_C
}

# ==============================================================================
# 4. PARAMETRI DI PERDITA E MATRICE DEI TASSI MIGRATION-BASED phi(r_0, r_4)
# ==============================================================================
LGD = 0.65

# Righe: rating iniziale (A, BBB, BB, B, D); Colonne: rating finale (A, BBB, BB, B, D)
# La riga D (indice 4) è coerente con l'assorbenza di D e LGD = 0.65
phi = np.array([
    [ 0.00,  0.03,  0.10,  0.22, 0.65],  # A
    [-0.02,  0.00,  0.06,  0.16, 0.65],  # BBB
    [-0.04, -0.02,  0.00,  0.09, 0.65],  # BB
    [-0.06, -0.04, -0.02,  0.00, 0.65],  # B
    [ 0.00,  0.00,  0.00,  0.00, 0.65]   # D
], dtype=float)

# ==============================================================================
# 5. COSTRUZIONE DEL PORTAFOGLIO INIZIALE CONCENTRATO (40 DEBITORI)
# ==============================================================================
gruppi_conc = [
    {"Gruppo": "Lehman Brothers",  "Numero debitori": 1,  "Rating iniziale": "A",   "Investimento per debitore": 25.0},
    {"Gruppo": "Altri debitori A", "Numero debitori": 11, "Rating iniziale": "A",   "Investimento per debitore": 5.0},
    {"Gruppo": "Debitori BBB",     "Numero debitori": 14, "Rating iniziale": "BBB", "Investimento per debitore": 4.0},
    {"Gruppo": "Debitori BB",      "Numero debitori": 9,  "Rating iniziale": "BB",  "Investimento per debitore": 3.0},
    {"Gruppo": "Debitori B",       "Numero debitori": 5,  "Rating iniziale": "B",   "Investimento per debitore": 2.0},
]

# Vettori a livello di singolo debitore (indice 0 = Lehman Brothers; indici 1..39 = 39 debitori comuni)
X0_conc_labels = []
V0_conc_list = []
is_lehman_list = []

for g in gruppi_conc:
    n_deb = g["Numero debitori"]
    rating = g["Rating iniziale"]
    v_ind = g["Investimento per debitore"]
    X0_conc_labels.extend([rating] * n_deb)
    V0_conc_list.extend([v_ind] * n_deb)
    is_lehman_list.extend([g["Gruppo"] == "Lehman Brothers"] * n_deb)

X0_conc = np.array([rating_to_idx[r] for r in X0_conc_labels], dtype=int)
V0_conc = np.array(V0_conc_list, dtype=float)
is_lehman = np.array(is_lehman_list, dtype=bool)

# ==============================================================================
# 6. COSTRUZIONE DEL PORTAFOGLIO CONTROFATTUALE (39 DEBITORI)
# ==============================================================================
V_tot_conc = V0_conc.sum()
V_lehman = V0_conc[is_lehman].sum()
V_residui_39 = V0_conc[~is_lehman].sum()
fattore_riscalamento = V_tot_conc / V_residui_39  # 173 / 148

# Eliminazione di Lehman e riallocazione proporzionale sui 39 debitori comuni
X0_div = X0_conc[~is_lehman].copy()
V0_div = V0_conc[~is_lehman] * fattore_riscalamento

# ==============================================================================
# 7. PRODUZIONE TABELLA 1 E TABELLA 2
# ==============================================================================
df_tab1 = pd.DataFrame(gruppi_conc)
df_tab1["Investimento complessivo"] = df_tab1["Numero debitori"] * df_tab1["Investimento per debitore"]
riga_tot_1 = pd.DataFrame([{
    "Gruppo": "Totale",
    "Numero debitori": int(df_tab1["Numero debitori"].sum()),
    "Rating iniziale": "",
    "Investimento per debitore": np.nan,
    "Investimento complessivo": df_tab1["Investimento complessivo"].sum()
}])
tabella_1 = pd.concat([df_tab1, riga_tot_1], ignore_index=True)

gruppi_div = []
for g in gruppi_conc:
    if g["Gruppo"] == "Lehman Brothers":
        continue
    v_ind_div = g["Investimento per debitore"] * fattore_riscalamento
    gruppi_div.append({
        "Gruppo": g["Gruppo"],
        "Numero debitori": g["Numero debitori"],
        "Rating iniziale": g["Rating iniziale"],
        "Investimento per debitore": v_ind_div,
        "Investimento complessivo": g["Numero debitori"] * v_ind_div
    })

df_tab2 = pd.DataFrame(gruppi_div)
riga_tot_2 = pd.DataFrame([{
    "Gruppo": "Totale",
    "Numero debitori": int(df_tab2["Numero debitori"].sum()),
    "Rating iniziale": "",
    "Investimento per debitore": np.nan,
    "Investimento complessivo": df_tab2["Investimento complessivo"].sum()
}])
tabella_2 = pd.concat([df_tab2, riga_tot_2], ignore_index=True)

display(Markdown("### Tabella 1 — Portafoglio iniziale concentrato (importi in milioni di USD)"))
display(tabella_1.style.format({
    "Investimento per debitore": lambda x: "" if pd.isna(x) else f"{x:.2f}",
    "Investimento complessivo": "{:.2f}"
}).hide(axis="index"))

display(Markdown("### Tabella 2 — Portafoglio controfattuale (importi in milioni di USD)"))
display(tabella_2.style.format({
    "Investimento per debitore": lambda x: "" if pd.isna(x) else f"{x:.4f}",
    "Investimento complessivo": "{:.4f}"
}).hide(axis="index"))

# ==============================================================================
# 8. CONTROLLI NUMERICI E LOGICO-TEORICI DELLA TAPPA 1
# ==============================================================================
print("=" * 78)
print("VERIFICA DEI CONTROLLI DELLA TAPPA 1")
print("=" * 78)

# Controllo 1: Somma righe di Q pari a 1
row_sums_Q = Q.sum(axis=1)
ctrl_1 = np.allclose(row_sums_Q, 1.0, atol=1e-12)
assert ctrl_1, f"Controllo 1 fallito: somme righe Q = {row_sums_Q}"
print(f"[Controllo 1] Somma righe matrice Q == 1: {ctrl_1} | Somme: {np.round(row_sums_Q, 6)}")

# Controllo 2: Somma righe di P^(O), P^(S), P^(C) pari a 1
ctrl_2_details = {}
for regime, P in P_matrices.items():
    r_sums = P.sum(axis=1)
    ok = np.allclose(r_sums, 1.0, atol=1e-12)
    assert ok, f"Controllo 2 fallito per P^({regime}): somme righe = {r_sums}"
    ctrl_2_details[regime] = (ok, np.round(r_sums, 6))
print(f"[Controllo 2] Somma righe matrici P^(m) == 1: {all(v[0] for v in ctrl_2_details.values())}")
for regime, (ok, r_sums) in ctrl_2_details.items():
    print(f"   - P^({regime}): {ok} | Somme: {r_sums}")

# Controllo 3: Stato D assorbente in tutte le matrici di migrazione creditizia (p_DD^(m) = 1)
idx_D = rating_to_idx["D"]
ctrl_3_details = {}
for regime, P in P_matrices.items():
    p_dd = P[idx_D, idx_D]
    others_zero = np.allclose(P[idx_D, :idx_D], 0.0, atol=1e-12)
    ok = np.isclose(p_dd, 1.0, atol=1e-12) and others_zero
    assert ok, f"Controllo 3 fallito per P^({regime}): riga D = {P[idx_D]}"
    ctrl_3_details[regime] = p_dd
print(f"[Controllo 3] Stato D assorbente (p_DD^(m) == 1): {all(np.isclose(v, 1.0) for v in ctrl_3_details.values())} | Valori p_DD: {ctrl_3_details}")

# Controllo 7: Portafoglio concentrato con esattamente 40 debitori
n_deb_conc = len(V0_conc)
ctrl_7 = (n_deb_conc == 40) and (len(X0_conc) == 40)
assert ctrl_7, f"Controllo 7 fallito: trovati {n_deb_conc} debitori"
print(f"[Controllo 7] Numero debitori portafoglio concentrato == 40: {ctrl_7} (valore: {n_deb_conc})")

# Controllo 8: Portafoglio controfattuale con esattamente 39 debitori
n_deb_div = len(V0_div)
ctrl_8 = (n_deb_div == 39) and (len(X0_div) == 39)
assert ctrl_8, f"Controllo 8 fallito: trovati {n_deb_div} debitori"
print(f"[Controllo 8] Numero debitori portafoglio controfattuale == 39: {ctrl_8} (valore: {n_deb_div})")

# Controllo 9: Investimento iniziale complessivo pari a 173 milioni di USD in entrambi i portafogli
V_tot_div = V0_div.sum()
ctrl_9 = np.isclose(V_tot_conc, 173.0, atol=1e-12) and np.isclose(V_tot_div, 173.0, atol=1e-12)
assert ctrl_9, f"Controllo 9 fallito: V_conc={V_tot_conc}, V_div={V_tot_div}"
print(f"[Controllo 9] Investimento totale == 173 mln USD: {ctrl_9} (Conc: {V_tot_conc:.6f}, Div: {V_tot_div:.6f})")

# Controllo 10: Invarianza delle proporzioni relative dei 39 debitori residui
pesi_rel_conc_39 = V0_conc[~is_lehman] / V0_conc[~is_lehman].sum()
pesi_rel_div_39 = V0_div / V0_div.sum()
max_diff_pesi = np.max(np.abs(pesi_rel_conc_39 - pesi_rel_div_39))
ctrl_10 = np.allclose(pesi_rel_conc_39, pesi_rel_div_39, atol=1e-15)
assert ctrl_10, f"Controllo 10 fallito: max diff pesi = {max_diff_pesi}"
print(f"[Controllo 10] Invarianza proporzioni relative dei 39 debitori residui: {ctrl_10} (max diff: {max_diff_pesi:.2e})")
print("=" * 78)

# CELLA 7
# ==============================================================================
# 1. PARAMETRI COMPUTAZIONALI DELLA SIMULAZIONE MONTE CARLO
# ==============================================================================
N_MC = 50_000
SEED = 2026
T = 4  # Orizzonte in trimestri (1 anno)

n_deb_conc = len(X0_conc)  # 40 debitori
n_deb_div = len(X0_div)    # 39 debitori

# Matrici cumulative per il campionamento tramite inversione della CDF
Q_cdf = np.cumsum(Q, axis=1)
Q_cdf[:, -1] = 1.0  # Garantisce chiusura esatta a 1.0

# Stack tridimensionale delle matrici di transizione creditizia: shape (3, 5, 5)
# Indice 0 -> O, Indice 1 -> S, Indice 2 -> C
P_stack = np.stack([P_matrices[s] for s in REGIME_STATES], axis=0)
P_cdf_stack = np.cumsum(P_stack, axis=2)
P_cdf_stack[:, :, -1] = 1.0

# ==============================================================================
# 2. FUNZIONE DI SIMULAZIONE MONTE CARLO DELLE TRAIETTORIE
# ==============================================================================
def simula_traiettorie_mc(n_mc, t_horizon, seed, m0_idx, x0_conc, is_lehman_mask, q_cdf, p_cdf_stack):
    """
    Simula le traiettorie trimestrali del regime sistemico {M_t}_{t=0}^{T-1}
    e le traiettorie creditizie individuali {X_{i,t}}_{t=0}^{T} condizionate al regime.
    """
    # Flussi pseudocasuali separati e riproducibili derivati da seed = 2026
    ss = np.random.SeedSequence(seed)
    seed_sys, seed_cred = ss.spawn(2)
    rng_sys = np.random.default_rng(seed_sys)
    rng_cred = np.random.default_rng(seed_cred)

    # Estrazione delle uniformi indipendenti per il processo sistemico (n_mc, T-1)
    # e per i processi creditizi individuali (n_mc, T, 40)
    u_sys = rng_sys.random((n_mc, t_horizon - 1))
    u_cred = rng_cred.random((n_mc, t_horizon, len(x0_conc)))

    # --- A. Evoluzione del regime sistemico comune {M_t}_{t=0}^{3} ---
    # Ogni replica r = 0, ..., n_mc-1 evolve liberamente secondo Q a partire da M_0 = S
    m_paths = np.empty((n_mc, t_horizon), dtype=int)
    m_paths[:, 0] = m0_idx
    for t in range(t_horizon - 1):
        curr_m = m_paths[:, t]
        m_paths[:, t + 1] = (u_sys[:, t, None] >= q_cdf[curr_m]).sum(axis=1)

    # --- B. Evoluzione delle migrazioni creditizie individuali {X_{i,t}}_{t=0}^{4} ---
    x_paths_conc = np.empty((n_mc, t_horizon + 1, len(x0_conc)), dtype=int)
    x_paths_conc[:, 0, :] = x0_conc

    # Tracciamento esplicito dell'indice di matrice P^(m) usato da ogni debitore in (r, t)
    matrice_usata_idx = np.empty((n_mc, t_horizon, len(x0_conc)), dtype=int)

    for t in range(t_horizon):
        # A parità di replica r e trimestre t, tutti i 40 debitori condividono M_t^(r)
        regime_t = m_paths[:, t][:, None]  # shape (n_mc, 1) -> broadcast sui 40 debitori
        matrice_usata_idx[:, t, :] = regime_t

        curr_x = x_paths_conc[:, t, :]  # shape (n_mc, 40)
        cdf_rt = p_cdf_stack[regime_t, curr_x]  # shape (n_mc, 40, 5)
        x_paths_conc[:, t + 1, :] = (u_cred[:, t, :, None] >= cdf_rt).sum(axis=2)

    # --- C. Estrazione traiettorie terminali, portafoglio controfattuale ed evento C ---
    x_t_conc = x_paths_conc[:, t_horizon, :]

    # Condivisione esatta delle traiettorie dei 39 debitori comuni nel portafoglio controfattuale
    x_paths_div = x_paths_conc[:, :, ~is_lehman_mask].copy()
    x_t_div = x_t_conc[:, ~is_lehman_mask].copy()

    # Indicatore binario di ingresso nello stato C almeno una volta in t in {0, 1, 2, 3}
    idx_c = regime_to_idx["C"]
    in_c = np.any(m_paths == idx_c, axis=1)

    return m_paths, in_c, x_paths_conc, x_t_conc, x_paths_div, x_t_div, u_cred, matrice_usata_idx


# Esecuzione della simulazione principale con seed = 2026
(
    M_paths,
    in_regime_C,
    X_paths_conc,
    X_T_conc,
    X_paths_div,
    X_T_div,
    U_cred_draws,
    matrice_P_applicata
) = simula_traiettorie_mc(
    n_mc=N_MC,
    t_horizon=T,
    seed=SEED,
    m0_idx=M0_idx,
    x0_conc=X0_conc,
    is_lehman_mask=is_lehman,
    q_cdf=Q_cdf,
    p_cdf_stack=P_cdf_stack
)

# ==============================================================================
# 3. RIEPILOGO STRUTTURALE DEGLI OUTPUT DELLA TAPPA 2
# ==============================================================================
riepilogo_sim = pd.DataFrame([
    {"Oggetto": "M_paths",      "Dimensione": str(M_paths.shape),      "Tipo": str(M_paths.dtype),      "Descrizione": "Traiettorie trimestrali del regime sistemico (t = 0..3)"},
    {"Oggetto": "in_regime_C",  "Dimensione": str(in_regime_C.shape),  "Tipo": str(in_regime_C.dtype),  "Descrizione": "Indicatore booleano di ingresso nello stato C almeno una volta"},
    {"Oggetto": "X_paths_conc", "Dimensione": str(X_paths_conc.shape), "Tipo": str(X_paths_conc.dtype), "Descrizione": "Traiettorie trimestrali rating portafoglio concentrato (40 debitori)"},
    {"Oggetto": "X_T_conc",     "Dimensione": str(X_T_conc.shape),     "Tipo": str(X_T_conc.dtype),     "Descrizione": "Stati creditizi terminali a t = 4 portafoglio concentrato (40 debitori)"},
    {"Oggetto": "X_paths_div",  "Dimensione": str(X_paths_div.shape),  "Tipo": str(X_paths_div.dtype),  "Descrizione": "Traiettorie trimestrali rating portafoglio controfattuale (39 debitori)"},
    {"Oggetto": "X_T_div",      "Dimensione": str(X_T_div.shape),      "Tipo": str(X_T_div.dtype),      "Descrizione": "Stati creditizi terminali a t = 4 portafoglio controfattuale (39 debitori)"},
])

display(Markdown(f"### Riepilogo strutturale della simulazione Monte Carlo ($N_{{\\mathrm{{MC}}}} = {N_MC:,}$, $T = {T}$, $\\text{{seed}} = {SEED}$)"))
display(riepilogo_sim.style.hide(axis="index"))

# ==============================================================================
# 4. CONTROLLI LOGICI, TEORICI E COMPUTAZIONALI DELLA TAPPA 2
# ==============================================================================
print("=" * 78)
print("VERIFICA DEI CONTROLLI DELLA TAPPA 2")
print("=" * 78)

# Controllo 4: Appartenenza di tutti gli stati simulati a M = {O, S, C} e I = {A, BBB, BB, B, D}
valid_m_indices = set(range(len(REGIME_STATES)))
valid_i_indices = set(range(len(RATING_STATES)))

obs_m_indices = set(np.unique(M_paths))
obs_i_conc_indices = set(np.unique(X_paths_conc))
obs_i_div_indices = set(np.unique(X_paths_div))

init_m_ok = np.all(M_paths[:, 0] == M0_idx)
init_x_ok = np.array_equal(X_paths_conc[:, 0, :], np.broadcast_to(X0_conc, (N_MC, n_deb_conc)))
idx_D = rating_to_idx["D"]
default_mask = (X_paths_conc[:, :-1, :] == idx_D)
absorbing_sim_ok = np.all(X_paths_conc[:, 1:, :][default_mask] == idx_D)

ctrl_4 = (
    obs_m_indices.issubset(valid_m_indices)
    and obs_i_conc_indices.issubset(valid_i_indices)
    and obs_i_div_indices.issubset(valid_i_indices)
    and init_m_ok
    and init_x_ok
    and absorbing_sim_ok
)
assert ctrl_4, "Controllo 4 fallito: rilevati stati fuori dominio o violazioni strutturali."
print(f"[Controllo 4] Appartenenza stati simulati a M e I (e coerenza iniziale/assorbenza): {ctrl_4}")
print(f"   - Stati sistemici osservati: {[REGIME_STATES[k] for k in sorted(obs_m_indices)]}")
print(f"   - Stati creditizi osservati: {[RATING_STATES[k] for k in sorted(obs_i_conc_indices)]}")

# Controllo 5: Unicità della traiettoria sistemica comune e identità della matrice P^(M_t)
# per tutti i debitori a parità di replica r e trimestre t (con variabilità tra repliche)
diff_matrice_tra_debitori = np.max(np.abs(matrice_P_applicata - M_paths[:, :, None]))
n_traiettorie_distinte = len(np.unique(M_paths, axis=0))
ctrl_5 = (M_paths.shape == (N_MC, T)) and (diff_matrice_tra_debitori == 0) and (n_traiettorie_distinte > 1)
assert ctrl_5, "Controllo 5 fallito: i debitori non condividono la medesima traiettoria sistemica/matrice P."
print(f"[Controllo 5] Unicità traiettoria sistemica e matrice P^(M_t) comune in (r, t): {ctrl_5}")
print(f"   - Traiettorie sistemiche distinte osservate tra le {N_MC:,} repliche: {n_traiettorie_distinte} (su 27 possibili)")

# Controllo 6: Estrazioni casuali individuali e indipendenti condizionatamente al regime comune
diff_u_0_1 = np.max(np.abs(U_cred_draws[:, :, 0] - U_cred_draws[:, :, 1]))
corr_u_0_1 = np.corrcoef(U_cred_draws[:, 0, 0], U_cred_draws[:, 0, 1])[0, 1]

mask_ssss = np.all(M_paths == regime_to_idx["S"], axis=1)
def_cond_0 = (X_T_conc[mask_ssss, 0] == idx_D).astype(float)
def_cond_1 = (X_T_conc[mask_ssss, 1] == idx_D).astype(float)
corr_cond_def = np.corrcoef(def_cond_0, def_cond_1)[0, 1] if mask_ssss.sum() > 10 else 0.0

ctrl_6 = (
    (U_cred_draws.shape == (N_MC, T, n_deb_conc))
    and (diff_u_0_1 > 0.5)
    and (abs(corr_u_0_1) < 0.02)
    and (abs(corr_cond_def) < 0.03)
)
assert ctrl_6, f"Controllo 6 fallito: corr_u={corr_u_0_1:.4f}, corr_cond_def={corr_cond_def:.4f}"
print(f"[Controllo 6] Estrazioni individuali e indipendenza condizionata: {ctrl_6}")
print(f"   - Corr. estrazioni uniformi debitori (0,1) a t=0: {corr_u_0_1:.5f} | Corr. default condizionata a (S,S,S,S): {corr_cond_def:.5f}")

# Controllo 11: I 39 debitori comuni utilizzano esattamente le stesse traiettorie nei due portafogli
ctrl_11 = (
    np.array_equal(X_paths_conc[:, :, ~is_lehman], X_paths_div)
    and np.array_equal(X_T_conc[:, ~is_lehman], X_T_div)
)
assert ctrl_11, "Controllo 11 fallito: divergenza tra le traiettorie dei 39 debitori comuni."
print(f"[Controllo 11] Identità traiettorie dei 39 debitori comuni nei due portafogli: {ctrl_11}")

# Controllo 13: Corretta impostazione del seed = 2026 per la riproducibilità
M_check, _, _, X_T_conc_check, _, X_T_div_check, _, _ = simula_traiettorie_mc(
    n_mc=N_MC,
    t_horizon=T,
    seed=SEED,
    m0_idx=M0_idx,
    x0_conc=X0_conc,
    is_lehman_mask=is_lehman,
    q_cdf=Q_cdf,
    p_cdf_stack=P_cdf_stack
)
ctrl_13 = (
    (SEED == 2026)
    and np.array_equal(M_paths, M_check)
    and np.array_equal(X_T_conc, X_T_conc_check)
    and np.array_equal(X_T_div, X_T_div_check)
)
assert ctrl_13, "Controllo 13 fallito: la simulazione non è riproducibile con seed = 2026."
print(f"[Controllo 13] Riproducibilità esatta con seed == 2026: {ctrl_13}")
print("=" * 78)

# CELLA 9
import matplotlib.pyplot as plt

# ==============================================================================
# 1. DETERMINAZIONE DEI TASSI DI PERDITA MIGRATION-BASED phi(X_{i,0}, X_{i,4})
# ==============================================================================
# Indicizzazione vettoriale sulla matrice phi (righe = rating iniziale, colonne = rating finale)
phi_rate_conc = phi[X0_conc[None, :], X_T_conc]  # shape: (N_MC, 40)
phi_rate_div = phi[X0_div[None, :], X_T_div]     # shape: (N_MC, 39)

# ==============================================================================
# 2. CALCOLO DELLE PERDITE INDIVIDUALI E DI PORTAFOGLIO (IN MILIONI DI USD)
# ==============================================================================
# Perdite individuali per ciascuna replica r = 0, ..., N_MC - 1
L_ind_conc = V0_conc[None, :] * phi_rate_conc  # shape: (N_MC, 40)
L_ind_div = V0_div[None, :] * phi_rate_div     # shape: (N_MC, 39)

# Perdite complessive di portafoglio per replica (somma sulle posizioni)
L_conc = np.sum(L_ind_conc, axis=1)  # L_{conc}^{P,(r)}, shape: (N_MC,)
L_div = np.sum(L_ind_div, axis=1)    # L_{div}^{P,(r)},  shape: (N_MC,)

# Differenza replica per replica: Delta L^(r) = L_{div}^{P,(r)} - L_{conc}^{P,(r)}
Delta_L = L_div - L_conc             # shape: (N_MC,)

# ==============================================================================
# 3. RAPPRESENTAZIONE GRAFICA DELLE FREQUENZE EMPIRICHE SIMULATE
# ==============================================================================
# Nota: la linea verticale indica esclusivamente la collocazione grafica della media
# empirica, rimandando alla Tappa 4 la stima numerica esatta delle misure di sintesi.
fig, axes = plt.subplots(1, 3, figsize=(16, 4.6), dpi=110)

serie_distribuzioni = [
    (
        axes[0],
        L_conc,
        "Portafoglio concentrato ($L_{\\mathrm{conc}}^P$)",
        "Perdita di portafoglio (mln USD)",
        "#2b5c8f"
    ),
    (
        axes[1],
        L_div,
        "Portafoglio controfattuale ($L_{\\mathrm{div}}^P$)",
        "Perdita di portafoglio (mln USD)",
        "#2e7d6b"
    ),
    (
        axes[2],
        Delta_L,
        "Differenza replica per replica ($\\Delta L^{(r)}$)",
        "$L_{\\mathrm{div}}^{P,(r)} - L_{\\mathrm{conc}}^{P,(r)}$ (mln USD)",
        "#6a51a3"
    )
]

for ax, dati, titolo, xlabel, colore in serie_distribuzioni:
    pesi_rel = np.ones_like(dati) / len(dati)
    ax.hist(
        dati,
        bins=50,
        weights=pesi_rel,
        color=colore,
        alpha=0.78,
        edgecolor="white",
        linewidth=0.4
    )
    # Posizione qualitativa della media senza esporre il valore numerico
    ax.axvline(
        np.mean(dati),
        color="#c0392b",
        linestyle="--",
        linewidth=1.8,
        label="Media empirica"
    )
    if titolo.startswith("Differenza"):
        ax.axvline(0.0, color="#444444", linestyle=":", linewidth=1.2, label="Parità ($\\Delta L = 0$)")

    ax.set_title(titolo, fontsize=11, pad=10)
    ax.set_xlabel(xlabel, fontsize=9.5)
    ax.set_ylabel("Frequenza relativa empirica", fontsize=9.5)
    ax.grid(axis="y", linestyle="--", alpha=0.35)
    ax.legend(frameon=True, fontsize=8.8)

fig.suptitle(
    f"Distribuzioni empiriche simulate su $N_{{\\mathrm{{MC}}}} = {N_MC:,}$ repliche (collocazione grafica della media)",
    fontsize=12.5,
    y=1.02
)
plt.tight_layout()
plt.show()

# ==============================================================================
# 4. CONTROLLI NUMERICI E LOGICI DELLA TAPPA 3
# ==============================================================================
print("=" * 78)
print("VERIFICA DEI CONTROLLI DELLA TAPPA 3")
print("=" * 78)

# Controllo 12: La perdita totale di ciascun portafoglio coincide con la somma delle perdite individuali
somma_ind_conc = np.einsum("ri->r", L_ind_conc)
somma_ind_div = np.einsum("ri->r", L_ind_div)

max_err_conc = np.max(np.abs(L_conc - somma_ind_conc))
max_err_div = np.max(np.abs(L_div - somma_ind_div))

ctrl_12_conc = np.allclose(L_conc, somma_ind_conc, atol=1e-12) and (L_conc.shape == (N_MC,))
ctrl_12_div = np.allclose(L_div, somma_ind_div, atol=1e-12) and (L_div.shape == (N_MC,))
ctrl_12 = ctrl_12_conc and ctrl_12_div

assert ctrl_12, f"Controllo 12 fallito: max_err_conc={max_err_conc:.2e}, max_err_div={max_err_div:.2e}"
print(f"[Controllo 12] Coincidenza perdita totale con somma perdite individuali: {ctrl_12}")
print(f"   - Portafoglio concentrato (40 debitori): {ctrl_12_conc} | Max diff: {max_err_conc:.2e}")
print(f"   - Portafoglio controfattuale (39 debitori): {ctrl_12_div} | Max diff: {max_err_div:.2e}")

# Verifiche di coerenza strutturale della funzione di perdita migration-based (Passo 4):
# a) Per ogni debitore in default a t=4 (X_{i,4} = D), il tasso applicato è pari a LGD = 0.65
idx_D = rating_to_idx["D"]
mask_def_conc = (X_T_conc == idx_D)
lgd_ok = np.allclose(phi_rate_conc[mask_def_conc], LGD, atol=1e-12) if np.any(mask_def_conc) else True

# b) I 39 debitori comuni hanno identici tassi di perdita phi(X_{i,0}, X_{i,4}) nei due portafogli
phi_comuni_ok = np.allclose(phi_rate_conc[:, ~is_lehman], phi_rate_div, atol=1e-12)

assert lgd_ok and phi_comuni_ok, "Errore di coerenza nell'applicazione della mappa phi."
print(f"[Coerenza Passo 4] Tasso default == LGD ({LGD}): {lgd_ok} | Identità tassi phi dei 39 debitori comuni: {phi_comuni_ok}")
print("=" * 78)

# CELLA 11
# ==============================================================================
# 1. FUNZIONI DI STIMA EMPIRICA DELLE MISURE DI SINTESI E DI RISCHIO DI CODA
# ==============================================================================
def calcola_var_empirico(perdite: np.ndarray, alpha: float) -> float:
    """
    Calcola il Value at Risk empirico al livello alpha sulla distribuzione
    delle perdite monetarie (in milioni di USD).
    """
    return float(np.quantile(perdite, alpha))


def calcola_cvar_empirico(perdite: np.ndarray, alpha: float) -> float:
    """
    Calcola il Conditional Value at Risk empirico al livello alpha secondo la
    definizione mediante quantili:
        CVaR_alpha(L) = 1 / (1 - alpha) * int_alpha^1 VaR_u(L) du
    valutata esattamente sulle statistiche d'ordine superiori del campione simulato.
    """
    n = len(perdite)
    perdite_ordinate = np.sort(perdite)
    idx_inizio = int(np.ceil(alpha * n))
    return float(np.mean(perdite_ordinate[idx_inizio:]))


def calcola_misure_portafoglio(perdite: np.ndarray) -> dict:
    """
    Restituisce il dizionario completo delle misure di sintesi e di rischio
    (in milioni di USD) per un vettore di perdite simulate.
    """
    media = float(np.mean(perdite))
    varianza = float(np.var(perdite, ddof=1))
    dev_std = float(np.std(perdite, ddof=1))
    var_95 = calcola_var_empirico(perdite, 0.95)
    cvar_95 = calcola_cvar_empirico(perdite, 0.95)
    var_99 = calcola_var_empirico(perdite, 0.99)
    cvar_99 = calcola_cvar_empirico(perdite, 0.99)

    return {
        "Perdita media E[L^P]": media,
        "Varianza Var(L^P)": varianza,
        "Deviazione standard": dev_std,
        "VaR 95%": var_95,
        "CVaR 95%": cvar_95,
        "VaR 99%": var_99,
        "CVaR 99%": cvar_99,
    }


# ==============================================================================
# 2. STIMA DELLE MISURE DI RISCHIO E DELLE DIFFERENZE DELTA_RHO
# ==============================================================================
risk_conc = calcola_misure_portafoglio(L_conc)
risk_div = calcola_misure_portafoglio(L_div)

# Variazione per ciascuna misura di rischio: Delta rho = rho(L_div^P) - rho(L_conc^P)
delta_risk = {
    misura: risk_div[misura] - risk_conc[misura]
    for misura in risk_conc
}

# Esposizione esplicita delle soglie VaR e CVaR in memoria per le tappe successive
var_95_conc = risk_conc["VaR 95%"]
cvar_95_conc = risk_conc["CVaR 95%"]
var_99_conc = risk_conc["VaR 99%"]
cvar_99_conc = risk_conc["CVaR 99%"]

var_95_div = risk_div["VaR 95%"]
cvar_95_div = risk_div["CVaR 95%"]
var_99_div = risk_div["VaR 99%"]
cvar_99_div = risk_div["CVaR 99%"]

# ==============================================================================
# 3. PRODUZIONE TABELLA 3 — MISURE DI RISCHIO
# ==============================================================================
unita_misure = [
    "mln USD",
    "(mln USD)^2",
    "mln USD",
    "mln USD",
    "mln USD",
    "mln USD",
    "mln USD",
]

righe_tab3 = []
for (misura, val_conc), unita in zip(risk_conc.items(), unita_misure):
    val_div = risk_div[misura]
    diff = delta_risk[misura]
    var_pct = (diff / val_conc * 100.0) if abs(val_conc) > 1e-12 else np.nan
    righe_tab3.append({
        "Misura di rischio": misura,
        "Unità": unita,
        "Portafoglio concentrato": val_conc,
        "Portafoglio controfattuale": val_div,
        "Differenza (Div - Conc)": diff,
        "Variazione (%)": var_pct,
    })

tabella_3 = pd.DataFrame(righe_tab3)

display(Markdown("### Tabella 3 — Misure di rischio (portafoglio concentrato vs. portafoglio controfattuale)"))
display(tabella_3.style.format({
    "Portafoglio concentrato": "{:.4f}",
    "Portafoglio controfattuale": "{:.4f}",
    "Differenza (Div - Conc)": "{:+.4f}",
    "Variazione (%)": "{:+.2f}%"
}).hide(axis="index"))

# ==============================================================================
# 4. SINTESI NUMERICA DELLA DISTRIBUZIONE EMPIRICA DI DELTA L^(r)
# ==============================================================================
sintesi_delta_L = pd.DataFrame([
    {"Statistica": "Media campionaria E[Delta L]",        "Valore (mln USD)": float(np.mean(Delta_L))},
    {"Statistica": "Varianza campionaria Var(Delta L)",    "Valore (mln USD)": float(np.var(Delta_L, ddof=1))},
    {"Statistica": "Deviazione standard sigma(Delta L)",   "Valore (mln USD)": float(np.std(Delta_L, ddof=1))},
    {"Statistica": "Minimo osservato",                     "Valore (mln USD)": float(np.min(Delta_L))},
    {"Statistica": "Percentile 1% (q_0.01)",               "Valore (mln USD)": float(np.quantile(Delta_L, 0.01))},
    {"Statistica": "Percentile 5% (q_0.05)",               "Valore (mln USD)": float(np.quantile(Delta_L, 0.05))},
    {"Statistica": "Primo quartile (q_0.25)",              "Valore (mln USD)": float(np.quantile(Delta_L, 0.25))},
    {"Statistica": "Mediana (q_0.50)",                     "Valore (mln USD)": float(np.quantile(Delta_L, 0.50))},
    {"Statistica": "Terzo quartile (q_0.75)",              "Valore (mln USD)": float(np.quantile(Delta_L, 0.75))},
    {"Statistica": "Percentile 95% (q_0.95)",              "Valore (mln USD)": float(np.quantile(Delta_L, 0.95))},
    {"Statistica": "Percentile 99% (q_0.99)",              "Valore (mln USD)": float(np.quantile(Delta_L, 0.99))},
    {"Statistica": "Massimo osservato",                    "Valore (mln USD)": float(np.max(Delta_L))},
])

display(Markdown("### Sintesi numerica della distribuzione empirica di $\\Delta L^{(r)} = L_{\\mathrm{div}}^{P,(r)} - L_{\\mathrm{conc}}^{P,(r)}$"))
display(sintesi_delta_L.style.format({
    "Valore (mln USD)": "{:+.4f}"
}).hide(axis="index"))

# ==============================================================================
# 5. CONTROLLI NUMERICI DELLA TAPPA 4
# ==============================================================================
print("=" * 78)
print("VERIFICA DEI CONTROLLI DELLA TAPPA 4")
print("=" * 78)

# Controllo 14: VaR e CVaR calcolati sulle distribuzioni empiriche delle perdite
# monetarie espresse in milioni di dollari
# 1) Verifica monetaria: le perdite sono espresse in mln USD (scala coerente con V_0^P = 173 mln USD
#    e con la somma delle perdite individuali V_{i,0} * phi, non normalizzate su [0, 1])
scala_monetaria_conc = np.allclose(L_conc, np.sum(L_ind_conc, axis=1), atol=1e-12) and (np.max(L_conc) > 1.0)
scala_monetaria_div = np.allclose(L_div, np.sum(L_ind_div, axis=1), atol=1e-12) and (np.max(L_div) > 1.0)

# 2) Verifica di coerenza ordinale e appartenenza al supporto monetario per entrambi i portafogli
coerenza_conc = (
    (np.min(L_conc) <= var_95_conc <= cvar_95_conc <= np.max(L_conc))
    and (np.min(L_conc) <= var_99_conc <= cvar_99_conc <= np.max(L_conc))
    and (var_95_conc <= var_99_conc)
    and (cvar_95_conc <= cvar_99_conc)
)
coerenza_div = (
    (np.min(L_div) <= var_95_div <= cvar_95_div <= np.max(L_div))
    and (np.min(L_div) <= var_99_div <= cvar_99_div <= np.max(L_div))
    and (var_95_div <= var_99_div)
    and (cvar_95_div <= cvar_99_div)
)

# 3) Verifica dell'identità della variazione Delta rho = rho(L_div) - rho(L_conc)
coerenza_delta = all(
    np.isclose(delta_risk[k], risk_div[k] - risk_conc[k], atol=1e-12)
    for k in risk_conc
)

ctrl_14 = scala_monetaria_conc and scala_monetaria_div and coerenza_conc and coerenza_div and coerenza_delta
assert ctrl_14, "Controllo 14 fallito: incoerenza nella scala monetaria o nei quantili empirici."

print(f"[Controllo 14] VaR e CVaR calcolati su perdite monetarie empiriche (mln USD): {ctrl_14}")
print(f"   - Concentrato:    VaR_95 = {var_95_conc:.4f} <= CVaR_95 = {cvar_95_conc:.4f} | VaR_99 = {var_99_conc:.4f} <= CVaR_99 = {cvar_99_conc:.4f} mln USD")
print(f"   - Controfattuale: VaR_95 = {var_95_div:.4f} <= CVaR_95 = {cvar_95_div:.4f} | VaR_99 = {var_99_div:.4f} <= CVaR_99 = {cvar_99_div:.4f} mln USD")
print("=" * 78)

# CELLA 13
# ==============================================================================
# 1. PARTIZIONE DEL CAMPIONE IN BASE ALL'INGRESSO NEL REGIME DI CRISI C
# ==============================================================================
# Evento E_C = {esiste t in {0, 1, 2, 3} tale che M_t = C}
L_conc_in_C = L_conc[in_regime_C]     # Repliche con ingresso almeno una volta in C
L_conc_no_C = L_conc[~in_regime_C]    # Repliche senza mai ingresso in C

n_in_C = int(L_conc_in_C.size)
n_no_C = int(L_conc_no_C.size)

# Probabilità empiriche simulate
prob_regime_C = float(np.mean(in_regime_C))
prob_no_regime_C = float(np.mean(~in_regime_C))

# Perdite medie condizionate del portafoglio concentrato (in milioni di USD)
mean_L_conc_in_C = float(np.mean(L_conc_in_C))
mean_L_conc_no_C = float(np.mean(L_conc_no_C))
diff_mean_C = mean_L_conc_in_C - mean_L_conc_no_C

# Statistiche descrittive condizionate di supporto
std_L_conc_in_C = float(np.std(L_conc_in_C, ddof=1))
std_L_conc_no_C = float(np.std(L_conc_no_C, ddof=1))
med_L_conc_in_C = float(np.median(L_conc_in_C))
med_L_conc_no_C = float(np.median(L_conc_no_C))

# ==============================================================================
# 2. STIMA PUNTUALE DI P(E_C) E PRODUZIONE TABELLA 4 — REGIME SISTEMICO E PERDITA
# ==============================================================================
display(Markdown(
    f"### Probabilità simulata di ingresso almeno una volta nel regime $C$\n\n"
    f"- **Probabilità empirica $\\widehat{{\\mathbb{{P}}}}(E_C)$:** `{prob_regime_C:.6f}` (`{prob_regime_C * 100:.2f}%`, pari a `{n_in_C:,}` repliche su `{N_MC:,}`)\n"
    f"- **Probabilità complementare $\\widehat{{\\mathbb{{P}}}}(E_C^c)$:** `{prob_no_regime_C:.6f}` (`{prob_no_regime_C * 100:.2f}%`, pari a `{n_no_C:,}` repliche su `{N_MC:,}`)"
))

tabella_4 = pd.DataFrame([
    {
        "Indicatore": "Numero di repliche",
        "Unità": "conteggio",
        "Con ingresso in C (E_C)": f"{n_in_C:,}",
        "Senza ingresso in C (E_C^c)": f"{n_no_C:,}",
        "Differenza (Con C - Senza C)": f"{n_in_C - n_no_C:+,}"
    },
    {
        "Indicatore": "Frequenza relativa / Probabilità",
        "Unità": "%",
        "Con ingresso in C (E_C)": f"{prob_regime_C * 100:.2f}%",
        "Senza ingresso in C (E_C^c)": f"{prob_no_regime_C * 100:.2f}%",
        "Differenza (Con C - Senza C)": f"{(prob_regime_C - prob_no_regime_C) * 100:+.2f}%"
    },
    {
        "Indicatore": "Perdita media condizionata E[L_conc^P | .]",
        "Unità": "mln USD",
        "Con ingresso in C (E_C)": f"{mean_L_conc_in_C:.4f}",
        "Senza ingresso in C (E_C^c)": f"{mean_L_conc_no_C:.4f}",
        "Differenza (Con C - Senza C)": f"{diff_mean_C:+.4f}"
    },
    {
        "Indicatore": "Deviazione standard condizionata",
        "Unità": "mln USD",
        "Con ingresso in C (E_C)": f"{std_L_conc_in_C:.4f}",
        "Senza ingresso in C (E_C^c)": f"{std_L_conc_no_C:.4f}",
        "Differenza (Con C - Senza C)": f"{std_L_conc_in_C - std_L_conc_no_C:+.4f}"
    },
    {
        "Indicatore": "Mediana condizionata",
        "Unità": "mln USD",
        "Con ingresso in C (E_C)": f"{med_L_conc_in_C:.4f}",
        "Senza ingresso in C (E_C^c)": f"{med_L_conc_no_C:.4f}",
        "Differenza (Con C - Senza C)": f"{med_L_conc_in_C - med_L_conc_no_C:+.4f}"
    }
])

display(Markdown("### Tabella 4 — Regime sistemico e perdita (portafoglio concentrato)"))
display(tabella_4.style.hide(axis="index"))

# ==============================================================================
# 3. CONTROLLI NUMERICI E INTEGRATIVI DELLA TAPPA 5
# ==============================================================================
print("=" * 78)
print("VERIFICA DEI CONTROLLI DELLA TAPPA 5")
print("=" * 78)

# 1) Verifica di partizione completa ed esclusiva delle repliche Monte Carlo
partizione_ok = (n_in_C + n_no_C == N_MC) and np.isclose(prob_regime_C + prob_no_regime_C, 1.0, atol=1e-15)
assert partizione_ok, f"Partizione incompleta: n_in_C={n_in_C}, n_no_C={n_no_C}, N_MC={N_MC}"
print(f"[Controllo Partizione] n_in_C + n_no_C == N_MC ({N_MC:,}): {partizione_ok}")

# 2) Verifica della Legge delle Aspettative Totali sulla perdita media del portafoglio concentrato
media_ricomposta = prob_regime_C * mean_L_conc_in_C + prob_no_regime_C * mean_L_conc_no_C
media_incondizionata = risk_conc["Perdita media E[L^P]"]
err_ricomposizione = abs(media_ricomposta - media_incondizionata)
aspettative_totali_ok = np.isclose(media_ricomposta, media_incondizionata, atol=1e-12)
assert aspettative_totali_ok, f"Errore legge aspettative totali: diff={err_ricomposizione:.2e}"
print(f"[Controllo Aspettative Totali] Ricomposizione esatta di E[L_conc^P]: {aspettative_totali_ok} (diff: {err_ricomposizione:.2e})")

# 3) Controllo integrativo di coerenza markoviana: confronto tra probabilità simulata
#    e probabilità teorica esatta di raggiungere lo stato C almeno una volta da M_0 = S
idx_non_C = [regime_to_idx["O"], regime_to_idx["S"]]
Q_non_C = Q[np.ix_(idx_non_C, idx_non_C)]  # Sottomatrice 2x2 degli stati {O, S}
# Distribuzione iniziale su {O, S} a t = 0 dato M_0 = S
p0_non_C = np.array([1.0 if idx == M0_idx else 0.0 for idx in idx_non_C], dtype=float)
# Probabilità di restare sempre in {O, S} per t = 0, 1, 2, 3 (cioè per T - 1 = 3 passi)
prob_never_C_teor = float(p0_non_C @ np.linalg.matrix_power(Q_non_C, T - 1) @ np.ones(len(idx_non_C)))
prob_regime_C_teor = 1.0 - prob_never_C_teor

errore_std_mc = np.sqrt(prob_regime_C_teor * (1.0 - prob_regime_C_teor) / N_MC)
scarto_prob = abs(prob_regime_C - prob_regime_C_teor)
coerenza_markov_ok = scarto_prob < 4.0 * errore_std_mc
assert coerenza_markov_ok, (
    f"Scarto eccessivo tra P(E_C) simulata ({prob_regime_C:.5f}) e teorica ({prob_regime_C_teor:.5f})"
)

print(f"[Controllo Integrativo Markov] Coerenza tra P(E_C) simulata e teorica: {coerenza_markov_ok}")
print(f"   - P(E_C) simulata : {prob_regime_C:.6f} ({prob_regime_C * 100:.2f}%)")
print(f"   - P(E_C) teorica  : {prob_regime_C_teor:.6f} ({prob_regime_C_teor * 100:.2f}%)")
print(f"   - Scarto assoluto : {scarto_prob:.6f} (soglia 4*SE = {4.0 * errore_std_mc:.6f})")
print("=" * 78)

# CELLA 15
import matplotlib.pyplot as plt

# ==============================================================================
# 1. FIGURA 1 — DISTRIBUZIONE DELLA PERDITA DEL PORTAFOGLIO CONCENTRATO
# ==============================================================================
fig1, ax1 = plt.subplots(figsize=(10, 5), dpi=115)

pesi_conc = np.ones_like(L_conc) / len(L_conc)
ax1.hist(
    L_conc,
    bins=60,
    weights=pesi_conc,
    color="#2b5c8f",
    alpha=0.80,
    edgecolor="white",
    linewidth=0.45,
    label="Frequenza relativa empirica $L_{\\mathrm{conc}}^P$"
)

ax1.axvline(
    var_95_conc,
    color="#d95f02",
    linestyle="--",
    linewidth=2.0,
    label=f"$\\mathrm{{VaR}}_{{0.95}}(L_{{\\mathrm{{conc}}}}^P) = {var_95_conc:.4f}$ mln USD"
)
ax1.axvline(
    var_99_conc,
    color="#b2182b",
    linestyle="-.",
    linewidth=2.0,
    label=f"$\\mathrm{{VaR}}_{{0.99}}(L_{{\\mathrm{{conc}}}}^P) = {var_99_conc:.4f}$ mln USD"
)

ax1.set_title("Figura 1 — Distribuzione della perdita del portafoglio concentrato", fontsize=12.5, pad=12)
ax1.set_xlabel("Perdita di portafoglio a 1 anno (milioni di USD)", fontsize=10.5)
ax1.set_ylabel("Frequenza relativa empirica", fontsize=10.5)
ax1.grid(axis="y", linestyle="--", alpha=0.35)
ax1.legend(frameon=True, fontsize=9.5, loc="upper right")

plt.tight_layout()
plt.show()

# ==============================================================================
# 2. FIGURA 2 — CONFRONTO DELLE DISTRIBUZIONI (INTERO SUPPORTO E CODA DESTRA)
# ==============================================================================
fig2, (ax2_left, ax2_right) = plt.subplots(1, 2, figsize=(15, 5.2), dpi=115)

# Pannello sinistro: confronto sull'intero supporto con bin comuni
min_tot = min(L_conc.min(), L_div.min())
max_tot = max(L_conc.max(), L_div.max())
bins_comuni = np.linspace(min_tot, max_tot, 65)

ax2_left.hist(
    L_conc,
    bins=bins_comuni,
    weights=np.ones_like(L_conc) / len(L_conc),
    color="#2b5c8f",
    alpha=0.55,
    edgecolor="white",
    linewidth=0.35,
    label="Portafoglio concentrato ($L_{\\mathrm{conc}}^P$)"
)
ax2_left.hist(
    L_div,
    bins=bins_comuni,
    weights=np.ones_like(L_div) / len(L_div),
    color="#2e7d6b",
    alpha=0.55,
    edgecolor="white",
    linewidth=0.35,
    label="Portafoglio controfattuale ($L_{\\mathrm{div}}^P$)"
)

ax2_left.set_title("Distribuzioni empiriche complete", fontsize=11.5, pad=10)
ax2_left.set_xlabel("Perdita di portafoglio a 1 anno (milioni di USD)", fontsize=10)
ax2_left.set_ylabel("Frequenza relativa empirica", fontsize=10)
ax2_left.grid(axis="y", linestyle="--", alpha=0.35)
ax2_left.legend(frameon=True, fontsize=9)

# Pannello destro: focus sulla coda destra (oltre il 90° percentile)
soglia_coda = min(np.quantile(L_conc, 0.90), np.quantile(L_div, 0.90))
bins_coda = np.linspace(soglia_coda, max_tot, 45)

ax2_right.hist(
    L_conc[L_conc >= soglia_coda],
    bins=bins_coda,
    weights=np.ones(np.sum(L_conc >= soglia_coda)) / len(L_conc),
    color="#2b5c8f",
    alpha=0.55,
    edgecolor="white",
    linewidth=0.35,
    label="Concentrato ($L_{\\mathrm{conc}}^P$)"
)
ax2_right.hist(
    L_div[L_div >= soglia_coda],
    bins=bins_coda,
    weights=np.ones(np.sum(L_div >= soglia_coda)) / len(L_div),
    color="#2e7d6b",
    alpha=0.55,
    edgecolor="white",
    linewidth=0.35,
    label="Controfattuale ($L_{\\mathrm{div}}^P$)"
)

ax2_right.axvline(var_95_conc, color="#1f4e78", linestyle="--", linewidth=1.6, label=f"$\\mathrm{{VaR}}_{{0.95}}$ Conc ({var_95_conc:.2f})")
ax2_right.axvline(var_95_div, color="#1b5e20", linestyle="--", linewidth=1.6, label=f"$\\mathrm{{VaR}}_{{0.95}}$ Div ({var_95_div:.2f})")
ax2_right.axvline(var_99_conc, color="#1f4e78", linestyle=":", linewidth=2.0, label=f"$\\mathrm{{VaR}}_{{0.99}}$ Conc ({var_99_conc:.2f})")
ax2_right.axvline(var_99_div, color="#1b5e20", linestyle=":", linewidth=2.0, label=f"$\\mathrm{{VaR}}_{{0.99}}$ Div ({var_99_div:.2f})")

ax2_right.set_title("Focus sulla coda destra (perdite oltre il 90° percentile)", fontsize=11.5, pad=10)
ax2_right.set_xlabel("Perdita di portafoglio a 1 anno (milioni di USD)", fontsize=10)
ax2_right.set_ylabel("Frequenza relativa sul totale delle repliche", fontsize=10)
ax2_right.grid(axis="y", linestyle="--", alpha=0.35)
ax2_right.legend(frameon=True, fontsize=8.5, loc="upper right")

fig2.suptitle("Figura 2 — Confronto delle distribuzioni tra portafoglio concentrato e controfattuale", fontsize=12.5, y=1.02)
plt.tight_layout()
plt.show()

# ==============================================================================
# 3. FIGURA 3 — REGIME SISTEMICO E PERDITA (PORTAFOGLIO CONCENTRATO)
# ==============================================================================
fig3, (ax3_left, ax3_right) = plt.subplots(1, 2, figsize=(15, 5.2), dpi=115)

bins_regime = np.linspace(L_conc.min(), L_conc.max(), 55)

# Pannello sinistro: distribuzioni condizionate normalizzate all'interno di ciascun sottocampione
ax3_left.hist(
    L_conc_no_C,
    bins=bins_regime,
    weights=np.ones_like(L_conc_no_C) / len(L_conc_no_C),
    color="#3b7ea1",
    alpha=0.58,
    edgecolor="white",
    linewidth=0.35,
    label=f"Mai in regime $C$ ($E_C^c$, {prob_no_regime_C*100:.1f}% repliche)"
)
ax3_left.hist(
    L_conc_in_C,
    bins=bins_regime,
    weights=np.ones_like(L_conc_in_C) / len(L_conc_in_C),
    color="#c0392b",
    alpha=0.55,
    edgecolor="white",
    linewidth=0.35,
    label=f"Almeno una volta in $C$ ($E_C$, {prob_regime_C*100:.1f}% repliche)"
)

ax3_left.axvline(
    mean_L_conc_no_C,
    color="#1b4f72",
    linestyle="--",
    linewidth=1.9,
    label=f"Media senza $C$ = {mean_L_conc_no_C:.4f} mln USD"
)
ax3_left.axvline(
    mean_L_conc_in_C,
    color="#78281f",
    linestyle="-.",
    linewidth=1.9,
    label=f"Media con $C$ = {mean_L_conc_in_C:.4f} mln USD"
)

ax3_left.set_title("Distribuzioni condizionate all'ingresso nel regime $C$", fontsize=11.5, pad=10)
ax3_left.set_xlabel("Perdita portafoglio concentrato $L_{\\mathrm{conc}}^P$ (milioni di USD)", fontsize=10)
ax3_left.set_ylabel("Frequenza relativa condizionata", fontsize=10)
ax3_left.grid(axis="y", linestyle="--", alpha=0.35)
ax3_left.legend(frameon=True, fontsize=8.8, loc="upper right")

# Pannello destro: boxplot comparativo con indicazione delle medie condizionate
bp = ax3_right.boxplot(
    [L_conc_no_C, L_conc_in_C],
    tick_labels=[
        f"Senza ingresso in $C$\n(n = {n_no_C:,})",
        f"Con ingresso in $C$\n(n = {n_in_C:,})"
    ],
    patch_artist=True,
    widths=0.45,
    showmeans=True,
    meanprops={"marker": "D", "markerfacecolor": "#f1c40f", "markeredgecolor": "#222222", "markersize": 7},
    medianprops={"color": "#111111", "linewidth": 1.8},
    flierprops={"marker": "o", "markersize": 3, "alpha": 0.35}
)

for patch, col in zip(bp["boxes"], ["#3b7ea1", "#c0392b"]):
    patch.set_facecolor(col)
    patch.set_alpha(0.65)

ax3_right.set_title("Dispersione, mediana, media (rombo) e code per regime", fontsize=11.5, pad=10)
ax3_right.set_ylabel("Perdita portafoglio concentrato $L_{\\mathrm{conc}}^P$ (milioni di USD)", fontsize=10)
ax3_right.grid(axis="y", linestyle="--", alpha=0.35)

fig3.suptitle("Figura 3 — Regime sistemico e perdita (portafoglio concentrato)", fontsize=12.5, y=1.02)
plt.tight_layout()
plt.show()

# ==============================================================================
# 4. CONTROLLO 15 — STABILITÀ DELLE MISURE DI RISCHIO AL CRESCERE DELLE REPLICHE
# ==============================================================================
griglia_n = np.array([1_000, 2_500, 5_000, 10_000, 15_000, 20_000, 25_000, 30_000, 35_000, 40_000, 45_000, 50_000])

def calcola_traiettoria_convergenza(perdite: np.ndarray, griglia: np.ndarray) -> pd.DataFrame:
    """
    Calcola le principali misure di rischio su prefissi crescenti del campione simulato.
    """
    records = []
    for n in griglia:
        sub = perdite[:n]
        records.append({
            "N_repliche": int(n),
            "Media": float(np.mean(sub)),
            "Dev_std": float(np.std(sub, ddof=1)),
            "VaR_95": calcola_var_empirico(sub, 0.95),
            "CVaR_95": calcola_cvar_empirico(sub, 0.95),
            "VaR_99": calcola_var_empirico(sub, 0.99),
            "CVaR_99": calcola_cvar_empirico(sub, 0.99),
        })
    return pd.DataFrame(records)

conv_conc = calcola_traiettoria_convergenza(L_conc, griglia_n)
conv_div = calcola_traiettoria_convergenza(L_div, griglia_n)

# Grafico diagnostico di stabilità al crescere del numero di repliche
fig_stab, axes_stab = plt.subplots(2, 2, figsize=(14, 8), dpi=110)

pannelli_stab = [
    (axes_stab[0, 0], "Media", "Perdita media $\\widehat{\\mathbb{E}}[L^P]$"),
    (axes_stab[0, 1], "Dev_std", "Deviazione standard $\\widehat{\\sigma}(L^P)$"),
    (axes_stab[1, 0], "CVaR_95", "$\\widehat{\\mathrm{CVaR}}_{0.95}(L^P)$"),
    (axes_stab[1, 1], "CVaR_99", "$\\widehat{\\mathrm{CVaR}}_{0.99}(L^P)$"),
]

for ax, col_metrica, titolo_metrica in pannelli_stab:
    ax.plot(conv_conc["N_repliche"], conv_conc[col_metrica], marker="o", markersize=4, linewidth=1.7, color="#2b5c8f", label="Concentrato")
    ax.plot(conv_div["N_repliche"], conv_div[col_metrica], marker="s", markersize=4, linewidth=1.7, color="#2e7d6b", label="Controfattuale")
    ax.set_title(titolo_metrica, fontsize=11)
    ax.set_xlabel("Numero di repliche simulate ($n$)", fontsize=9.5)
    ax.set_ylabel("Milioni di USD", fontsize=9.5)
    ax.grid(True, linestyle="--", alpha=0.35)
    ax.legend(frameon=True, fontsize=9)

fig_stab.suptitle("Diagnostica Controllo 15 — Stabilità delle principali misure di rischio al crescere di $N_{\\mathrm{MC}}$", fontsize=12.5, y=1.01)
plt.tight_layout()
plt.show()

# Tabella sintetica di stabilità su checkpoint selezionati
checkpoint_visibili = [5_000, 10_000, 25_000, 40_000, 50_000]
tab_stab_conc = conv_conc[conv_conc["N_repliche"].isin(checkpoint_visibili)].copy()
tab_stab_conc.insert(0, "Portafoglio", "Concentrato")
tab_stab_div = conv_div[conv_div["N_repliche"].isin(checkpoint_visibili)].copy()
tab_stab_div.insert(0, "Portafoglio", "Controfattuale")
tabella_stabilita = pd.concat([tab_stab_conc, tab_stab_div], ignore_index=True)

display(Markdown("### Tabella diagnostica — Andamento delle misure di rischio al crescere delle repliche"))
display(tabella_stabilita.style.format({
    "N_repliche": "{:,}",
    "Media": "{:.4f}",
    "Dev_std": "{:.4f}",
    "VaR_95": "{:.4f}",
    "CVaR_95": "{:.4f}",
    "VaR_99": "{:.4f}",
    "CVaR_99": "{:.4f}",
}).hide(axis="index"))

# Verifica quantitativa del Controllo 15:
# Massima variazione relativa nell'ultimo tratto campione (n in {40_000, 45_000} rispetto a N_MC = 50_000)
metriche_controllo = ["Media", "Dev_std", "VaR_95", "CVaR_95", "VaR_99", "CVaR_99"]
max_var_rel_conc = {}
max_var_rel_div = {}

for m in metriche_controllo:
    val_fin_c = conv_conc.loc[conv_conc["N_repliche"] == N_MC, m].values[0]
    val_tail_c = conv_conc.loc[conv_conc["N_repliche"].isin([40_000, 45_000]), m].values
    max_var_rel_conc[m] = float(np.max(np.abs(val_tail_c - val_fin_c) / abs(val_fin_c)))

    val_fin_d = conv_div.loc[conv_div["N_repliche"] == N_MC, m].values[0]
    val_tail_d = conv_div.loc[conv_div["N_repliche"].isin([40_000, 45_000]), m].values
    max_var_rel_div[m] = float(np.max(np.abs(val_tail_d - val_fin_d) / abs(val_fin_d)))

soglia_stabilita = 0.05  # Variazione relativa massima < 5% nell'ultimo 20% delle repliche
ctrl_15_conc = all(v < soglia_stabilita for v in max_var_rel_conc.values())
ctrl_15_div = all(v < soglia_stabilita for v in max_var_rel_div.values())
ctrl_15 = ctrl_15_conc and ctrl_15_div

assert ctrl_15, f"Controllo 15 fallito: oscillazione eccessiva su n >= 40_000."

print("=" * 78)
print("VERIFICA DEI CONTROLLI DELLA TAPPA 6")
print("=" * 78)
print(f"[Controllo 15] Stabilità delle misure di rischio al crescere di N_MC: {ctrl_15}")
print("   - Max variazione relativa (n in {40k, 45k} vs 50k) — Concentrato:")
for m, v in max_var_rel_conc.items():
    print(f"       * {m:<8}: {v * 100:.3f}%")
print("   - Max variazione relativa (n in {40k, 45k} vs 50k) — Controfattuale:")
for m, v in max_var_rel_div.items():
    print(f"       * {m:<8}: {v * 100:.3f}%")
print("=" * 78)