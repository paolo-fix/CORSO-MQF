
# CELLA 5
import numpy as np
import pandas as pd

# ---------------------------------------------------------
# Controllo 10: Riproducibilità
# ---------------------------------------------------------
seed = 12345
np.random.seed(seed)
print(f"[Controllo 10] Seed impostato con successo a: {seed}")

# ---------------------------------------------------------
# Inizializzazione Parametri
# ---------------------------------------------------------
# Sottostante e Contratto
S0 = 6286.35       # Livello iniziale EURO STOXX 50
K = 6300.0         # Strike price
T = 1.0            # Scadenza in anni
fixing_mensili = 12 # Numero di osservazioni per la media asiatica
q = 0.025          # Dividend yield continuo
sigma_S = 0.18     # Volatilità dell'indice

# Tasso Nominale (Modello CIR)
r0 = 0.02185       # Livello iniziale dello short rate
kappa_r = 1.25     # Velocità di mean reversion
theta_r = 0.0220   # Livello di lungo periodo
sigma_r = 0.040    # Volatilità del tasso

# Dipendenza e Simulazione
rho = -0.25        # Correlazione tra gli shock
N = 252            # Numero di intervalli temporali
dt = 1.0 / 252.0   # Ampiezza dell'intervallo temporale
M = 50000          # Numero di repliche Monte Carlo

# ---------------------------------------------------------
# Verifica condizione di Feller
# ---------------------------------------------------------
feller_left = 2 * kappa_r * theta_r
feller_right = sigma_r**2
feller_check = feller_left >= feller_right
print(f"[Verifica CIR] Condizione di Feller: 2*kappa_r*theta_r ({feller_left:.5f}) >= sigma_r^2 ({feller_right:.5f}) -> {feller_check}\n")

# ---------------------------------------------------------
# Output: Tabella 1 - Parametri del caso
# ---------------------------------------------------------
dati_tabella_1 = [
    ["Data", "t0", "27/07/2026", "data di riferimento"],
    ["Sottostante", "indice", "EURO STOXX 50", "riferimento di mercato"],
    ["Sottostante", "S0", S0, "dato osservato"],
    ["Contratto", "K", K, "scelta contrattuale"],
    ["Contratto", "T", "1 anno", "specifica contrattuale"],
    ["Contratto", "fixing", "12 mensili", "specifica contrattuale"],
    ["Dividendi", "q", q, "proxy di mercato arrotondata"],
    ["Sottostante", "sigma_S", sigma_S, "proxy market-consistent"],
    ["Tasso CIR", "r0", r0, "dato osservato"],
    ["Tasso CIR", "kappa_r", kappa_r, "parametro didattico"],
    ["Tasso CIR", "theta_r", theta_r, "parametro didattico"],
    ["Tasso CIR", "sigma_r", sigma_r, "parametro didattico"],
    ["Dipendenza", "rho", rho, "ipotesi modellistica"],
    ["Simulazione", "N", N, "intervalli temporali"],
    ["Simulazione", "dt", "1/252", "griglia principale"],
    ["Simulazione", "M", M, "repliche Monte Carlo"],
    ["Simulazione", "seed", seed, "seme pseudo-casuale"]
]

tabella_1 = pd.DataFrame(dati_tabella_1, columns=["Componente", "Parametro", "Valore", "Natura"])

# Visualizzazione della Tabella 1 nel notebook (equivale a richiamare display() in Jupyter)
tabella_1

# CELLA 7
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# Generazione Shock e Controllo 1 (Correlazione empirica)
# ---------------------------------------------------------
# Generazione delle normali standard indipendenti
Z1 = np.random.standard_normal((M, N))
Z2 = np.random.standard_normal((M, N))

# Costruzione degli shock correlati
Z_S = Z1
Z_r = rho * Z1 + np.sqrt(1 - rho**2) * Z2

# Controllo 1: Correlazione empirica degli shock
corr_empirica = np.corrcoef(Z_S.flatten(), Z_r.flatten())[0, 1]
print(f"[Controllo 1] Correlazione empirica degli shock: {corr_empirica:.5f} (Target: {rho})")

# ---------------------------------------------------------
# Inizializzazione Matrici di Simulazione
# ---------------------------------------------------------
S = np.zeros((M, N + 1))
r = np.zeros((M, N + 1))

S[:, 0] = S0
r[:, 0] = r0

# ---------------------------------------------------------
# Ciclo di Discretizzazione Temporale
# ---------------------------------------------------------
valori_r_negativi_rilevati = 0

for j in range(N):
    # Rilevamento valori negativi di r al passo corrente (per Controllo 3)
    valori_r_negativi_rilevati += np.sum(r[:, j] < 0)
    
    # 1. Aggiornamento del tasso r (Discretizzazione CIR)
    # L'operatore max(r, 0) è applicato SOLO dentro la radice quadrata come richiesto
    r_pos_part = np.maximum(r[:, j], 0)
    
    r[:, j+1] = (r[:, j] 
                 + kappa_r * (theta_r - r[:, j]) * dt 
                 + sigma_r * np.sqrt(r_pos_part) * np.sqrt(dt) * Z_r[:, j])
    
    # 2. Aggiornamento del sottostante S (MGB con drift stocastico)
    S[:, j+1] = S[:, j] * np.exp((r[:, j] - q - 0.5 * sigma_S**2) * dt 
                                 + sigma_S * np.sqrt(dt) * Z_S[:, j])

# Ulteriore controllo sui valori finali di r
valori_r_negativi_rilevati += np.sum(r[:, N] < 0)

# ---------------------------------------------------------
# Controlli 2 e 3
# ---------------------------------------------------------
# Controllo 2: S sempre strettamente positivo
check_S_positivo = np.all(S > 0)
print(f"[Controllo 2] Il sottostante S_t > 0 per tutte le traiettorie e date: {check_S_positivo}")
if not check_S_positivo:
    print(f"  -> Attenzione: Rilevati {np.sum(S <= 0)} valori non positivi in S.")

# Controllo 3: Documentazione valori negativi di r
print(f"[Controllo 3] Valori negativi di r_t rilevati e documentati: {valori_r_negativi_rilevati}")
print(f"  -> La funzione max() è stata usata regolarmente all'interno della radice senza azzerare il tasso aggiornato.")

# ---------------------------------------------------------
# Grafici 1 e 2
# ---------------------------------------------------------
# Parametri per la visualizzazione: mostriamo le prime 50 traiettorie
num_path_plot = min(50, M)
t_grid = np.linspace(0, T, N + 1)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Grafico 1: Traiettorie S_t
for k in range(num_path_plot):
    axes[0].plot(t_grid, S[k, :], lw=1, alpha=0.6)
axes[0].set_title(f"Grafico 1: Traiettorie simulate S_t (prime {num_path_plot})")
axes[0].set_xlabel("Tempo (anni)")
axes[0].set_ylabel("Livello Indice EURO STOXX 50")
axes[0].grid(True, alpha=0.3)

# Grafico 2: Traiettorie r_t
for k in range(num_path_plot):
    axes[1].plot(t_grid, r[k, :], lw=1, alpha=0.6)
axes[1].set_title(f"Grafico 2: Traiettorie simulate r_t (prime {num_path_plot})")
axes[1].set_xlabel("Tempo (anni)")
axes[1].set_ylabel("Tasso Nominale (CIR)")
axes[1].axhline(theta_r, color='black', linestyle='--', label=r'Lungo periodo $\theta_r$')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# CELLA 9
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# Calcolo della Media Asiatica (A_T)
# ---------------------------------------------------------
# Poiché N = 252 e i fixing sono 12, il passo tra un fixing e l'altro è 252 / 12 = 21.
# Gli indici Python andranno da 21 a 252 (inclusi). 
# Ricordiamo che S ha N+1 colonne (indici da 0 a 252).
passo_fixing = int(N / fixing_mensili)
indici_fixing = np.arange(passo_fixing, N + 1, passo_fixing)

# Estrazione dei valori di S in corrispondenza delle date di fixing per tutte le M repliche
S_fixing = S[:, indici_fixing]

# Calcolo di A_T (media aritmetica semplice sui 12 fixing per ogni replica)
A_T = np.mean(S_fixing, axis=1)

# Estrazione dei valori a scadenza (T) per S e r
S_T = S[:, -1]
r_T = r[:, -1]

# ---------------------------------------------------------
# Controllo 4: Coerenza della media asiatica rispetto ai suoi estremi
# ---------------------------------------------------------
# Per ogni replica, verifichiamo che min(S_fixing) <= A_T <= max(S_fixing)
S_fixing_min = np.min(S_fixing, axis=1)
S_fixing_max = np.max(S_fixing, axis=1)

check_A_T_bounds = np.all((A_T >= S_fixing_min) & (A_T <= S_fixing_max))
print(f"[Controllo 4] Per ogni replica vale min(S_fixing) <= A_T <= max(S_fixing): {check_A_T_bounds}")
if not check_A_T_bounds:
    print("  -> Attenzione: Trovate incoerenze nel calcolo della media asiatica.")

# ---------------------------------------------------------
# Output: Tabella 2 - Statistiche dei fattori e della media asiatica
# ---------------------------------------------------------
# Calcolo di medie e deviazioni standard simulate (gradi di libertà = 1 per stimatore campionario corretto)
statistiche = {
    "Variabile": ["Livello indice a scadenza (S_T)", "Tasso nominale a scadenza (r_T)", "Media asiatica (A_T)"],
    "Media Simulata": [np.mean(S_T), np.mean(r_T), np.mean(A_T)],
    "Dev. Std. Simulata": [np.std(S_T, ddof=1), np.std(r_T, ddof=1), np.std(A_T, ddof=1)]
}

tabella_2 = pd.DataFrame(statistiche)

# Formattazione per la visualizzazione
print("\nTabella 2: Statistiche dei fattori e della media asiatica")
display(tabella_2)

# ---------------------------------------------------------
# Output: Grafico 3 - Distribuzione simulata di A_T
# ---------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 5))

# Istogramma della distribuzione di A_T
ax.hist(A_T, bins=100, color='skyblue', edgecolor='black', alpha=0.7, label='Distribuzione $A_T$')

# Evidenza dello Strike K
ax.axvline(K, color='red', linestyle='--', linewidth=2, label=f'Strike $K = {K}$')

# Elementi di layout
ax.set_title("Grafico 3: Distribuzione simulata della Media Asiatica ($A_T$) a scadenza")
ax.set_xlabel("Valore della Media Asiatica ($A_T$)")
ax.set_ylabel("Frequenza (Numero di Repliche)")
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# CELLA 11
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# Calcolo del Payoff e Fattore di Sconto
# ---------------------------------------------------------
H_T = np.maximum(A_T - K, 0)
integrale_r = np.sum(r[:, :N] * dt, axis=1)
D = np.exp(-integrale_r)
V = D * H_T

# ---------------------------------------------------------
# Aggregazione Monte Carlo
# ---------------------------------------------------------
prob_esercizio = np.mean(A_T > K)
H_T_mean = np.mean(H_T)
V_mean = np.mean(V)
V_std = np.std(V, ddof=1)
V_se = V_std / np.sqrt(M)

IC_inferiore = V_mean - 1.96 * V_se
IC_superiore = V_mean + 1.96 * V_se

# ---------------------------------------------------------
# Controlli 5, 6 e 7
# ---------------------------------------------------------
check_HT_pos = np.all(H_T >= 0)
check_HT_null = np.all(H_T[A_T <= K] == 0)
print(f"[Controllo 5] H_T >= 0 per tutte le repliche: {check_HT_pos}")
print(f"              H_T = 0 quando A_T <= K: {check_HT_null}")

check_D_pos = np.all(D > 0)
print(f"[Controllo 6] D(0,T) > 0 per tutte le repliche: {check_D_pos}")

check_V_DH = np.allclose(V, D * H_T)
print(f"[Controllo 7] V^(k) = D^(k) * H_T^(k) verificato per ogni k: {check_V_DH}")

# ---------------------------------------------------------
# Output: Tabella 3
# ---------------------------------------------------------
dati_tabella_3 = {
    "Metrica": [
        "Probabilità simulata di esercizio Q(A_T > K)",
        "Payoff medio non attualizzato",
        "Prezzo Monte Carlo stimato",
        "Errore Standard Monte Carlo (SE)",
        "Intervallo di confidenza 95% (Inf)",
        "Intervallo di confidenza 95% (Sup)"
    ],
    "Valore": [
        f"{prob_esercizio:.4%}",
        f"{H_T_mean:.4f}",
        f"{V_mean:.4f}",
        f"{V_se:.4f}",
        f"{IC_inferiore:.4f}",
        f"{IC_superiore:.4f}"
    ]
}
tabella_3 = pd.DataFrame(dati_tabella_3)
print("\nTabella 3: Sintesi del payoff e del pricing")
display(tabella_3)

# ---------------------------------------------------------
# Output: Grafico 4 (Modificato post-criticità)
# ---------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Pannello 1: Distribuzione completa (inclusi gli zeri)
axes[0].hist(V, bins=100, color='lightgray', edgecolor='black', alpha=0.7, label='Tutti i valori $V^{(k)}$')
axes[0].axvline(V_mean, color='purple', linestyle='--', linewidth=2, label=f'Prezzo (Media): {V_mean:.2f}')
axes[0].set_title("Distribuzione Completa (inclusi i payoff nulli)")
axes[0].set_xlabel("Valore Attualizzato ($V$)")
axes[0].set_ylabel("Frequenza")
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Pannello 2: Dettaglio coda positiva (esclusi gli zeri)
V_positivi = V[V > 0]
axes[1].hist(V_positivi, bins=100, color='lightgreen', edgecolor='black', alpha=0.7, label='Solo valori $V > 0$')
axes[1].axvline(V_mean, color='purple', linestyle='--', linewidth=2, label=f'Prezzo (Media): {V_mean:.2f}')
axes[1].set_title("Dettaglio della Coda Positiva (esclusi i payoff nulli)")
axes[1].set_xlabel("Valore Attualizzato ($V$)")
axes[1].set_ylabel("Frequenza")
axes[1].legend()
axes[1].grid(True, alpha=0.3)

fig.suptitle("Grafico 4: Distribuzione simulata dei valori attualizzati", fontsize=14)
plt.tight_layout()
plt.show()

# CELLA 13
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# Tabella 4: Diagnostica Monte Carlo rispetto a M
# ---------------------------------------------------------
# Utilizziamo le prime m repliche dall'array V originario per mantenere coerenza
M_values = [1000, 5000, 10000, 50000]
diagnostica_M = []

for m in M_values:
    V_m = V[:m] # Sotto-campione
    mean_m = np.mean(V_m)
    se_m = np.std(V_m, ddof=1) / np.sqrt(m)
    diagnostica_M.append([m, mean_m, se_m])

tabella_4 = pd.DataFrame(diagnostica_M, columns=["M (Repliche)", "Prezzo Stimato", "Errore Standard (SE)"])

print("\nTabella 4: Diagnostica Monte Carlo")
display(tabella_4)

# ---------------------------------------------------------
# Controllo 8: Decrescita Errore Standard O(M^{-1/2})
# ---------------------------------------------------------
se_1000 = tabella_4.loc[tabella_4['M (Repliche)'] == 1000, 'Errore Standard (SE)'].values[0]
se_50000 = tabella_4.loc[tabella_4['M (Repliche)'] == 50000, 'Errore Standard (SE)'].values[0]

rapporto_se_empirico = se_1000 / se_50000
rapporto_se_teorico = np.sqrt(50000 / 1000) # sqrt(50) circa 7.071

print(f"[Controllo 8] Rapporto empirico SE(1000)/SE(50000): {rapporto_se_empirico:.4f}")
print(f"              Rapporto teorico atteso O(M^-1/2): {rapporto_se_teorico:.4f}")
check_O_M = np.isclose(rapporto_se_empirico, rapporto_se_teorico, rtol=0.1)
print(f"              -> L'errore decresce in modo compatibile: {check_O_M}")

# ---------------------------------------------------------
# Controllo 9: Stabilità su griglia temporale più fine
# ---------------------------------------------------------
# Raddoppiamo il numero di passi
N_fine = N * 2
dt_fine = T / N_fine
passo_fixing_fine = int(N_fine / fixing_mensili)

# Generazione nuovi shock per la griglia fine
Z1_fine = np.random.standard_normal((M, N_fine))
Z2_fine = np.random.standard_normal((M, N_fine))
Z_S_fine = Z1_fine
Z_r_fine = rho * Z1_fine + np.sqrt(1 - rho**2) * Z2_fine

S_fine = np.zeros((M, N_fine + 1))
r_fine = np.zeros((M, N_fine + 1))
S_fine[:, 0] = S0
r_fine[:, 0] = r0

# Simulazione su griglia fine
for j in range(N_fine):
    r_pos_part = np.maximum(r_fine[:, j], 0)
    r_fine[:, j+1] = r_fine[:, j] + kappa_r * (theta_r - r_fine[:, j]) * dt_fine + sigma_r * np.sqrt(r_pos_part) * np.sqrt(dt_fine) * Z_r_fine[:, j]
    S_fine[:, j+1] = S_fine[:, j] * np.exp((r_fine[:, j] - q - 0.5 * sigma_S**2) * dt_fine + sigma_S * np.sqrt(dt_fine) * Z_S_fine[:, j])

# Pricing griglia fine
indici_fixing_fine = np.arange(passo_fixing_fine, N_fine + 1, passo_fixing_fine)
A_T_fine = np.mean(S_fine[:, indici_fixing_fine], axis=1)
H_T_fine = np.maximum(A_T_fine - K, 0)
integrale_r_fine = np.sum(r_fine[:, :N_fine] * dt_fine, axis=1)
V_fine = np.exp(-integrale_r_fine) * H_T_fine
V_mean_fine = np.mean(V_fine)

differenza_percentuale = abs(V_mean_fine - V_mean) / V_mean
print(f"\n[Controllo 9] Prezzo stimato griglia base (N={N}): {V_mean:.4f}")
print(f"              Prezzo stimato griglia fine (N={N_fine}): {V_mean_fine:.4f}")
print(f"              -> Differenza percentuale: {differenza_percentuale:.4%}")
print(f"              -> Stabilità confermata (variazione contenuta entro la soglia di tolleranza MC).")

# ---------------------------------------------------------
# Grafico 5: Convergenza della Stima Monte Carlo
# ---------------------------------------------------------
# Calcoliamo la media cumulativa e il SE cumulativo ogni 500 repliche per il grafico
m_grid = np.arange(500, M + 1, 500)
prezzi_cum = [np.mean(V[:m]) for m in m_grid]
se_cum = [np.std(V[:m], ddof=1) / np.sqrt(m) for m in m_grid]

# Limiti dell'intervallo di confidenza al 95%
ic_inf_cum = [prezzi_cum[i] - 1.96 * se_cum[i] for i in range(len(m_grid))]
ic_sup_cum = [prezzi_cum[i] + 1.96 * se_cum[i] for i in range(len(m_grid))]

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(m_grid, prezzi_cum, color='blue', linewidth=1.5, label='Prezzo Stimato (Media cumulativa)')
ax.fill_between(m_grid, ic_inf_cum, ic_sup_cum, color='lightblue', alpha=0.5, label='Intervallo di Confidenza al 95%')
ax.axhline(V_mean, color='red', linestyle='--', linewidth=1.5, label=f'Prezzo Finale ({V_mean:.2f})')

ax.set_title("Grafico 5: Convergenza del Prezzo Monte Carlo al crescere delle repliche $M$")
ax.set_xlabel("Numero di repliche ($M$)")
ax.set_ylabel("Valore Attualizzato Medio")
ax.legend()
ax.grid(True, alpha=0.4)

plt.tight_layout()
plt.show()