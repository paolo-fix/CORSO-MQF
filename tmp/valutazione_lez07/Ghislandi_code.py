
# CELLA 5
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ====================================================================
# ASSEGNAZIONE PARAMETRI DELLA SCHEDA CASO
# ====================================================================

# Dati temporali e contrattuali
t_0 = "27/07/2026"
T = 1.0                # 1 anno
fixing_mensili = 12
K = 6300.0             # Strike

# Sottostante (EURO STOXX 50) e proxy
S_0 = 6286.35
q = 0.025              # Dividend yield continuo
sigma_S = 0.18         # Volatilità dell'indice

# Tasso (CIR)
r_0 = 0.02185
kappa_r = 1.25
theta_r = 0.0220
sigma_r = 0.040

# Dipendenza
rho = -0.25

# Parametri di Simulazione
N = 252                # Intervalli temporali
dt = 1.0 / 252.0       # Griglia principale
M = 50000              # Repliche Monte Carlo
seed_value = 12345     # Seme pseudo-casuale

# Impostazione del seed per la riproducibilità (Controllo 10)
np.random.seed(seed_value)

# ====================================================================
# OUTPUT: TABELLA 1 - PARAMETRI DEL CASO
# ====================================================================

dati_tabella_1 = [
    ["Data", "t_0", t_0, "data di riferimento"],
    ["Sottostante", "indice", "EURO STOXX 50", "riferimento di mercato"],
    ["Sottostante", "S_0", S_0, "dato osservato"],
    ["Contratto", "K", K, "scelta contrattuale"],
    ["Contratto", "T", f"{int(T)} anno", "specifica contrattuale"],
    ["Contratto", "fixing", f"{fixing_mensili} mensili", "specifica contrattuale"],
    ["Dividendi", "q", q, "proxy di mercato arrotondata"],
    ["Sottostante", "sigma_S", sigma_S, "proxy market-consistent"],
    ["Tasso CIR", "r_0", r_0, "dato osservato"],
    ["Tasso CIR", "kappa_r", kappa_r, "parametro didattico"],
    ["Tasso CIR", "theta_r", theta_r, "parametro didattico"],
    ["Tasso CIR", "sigma_r", sigma_r, "parametro didattico"],
    ["Dipendenza", "rho", rho, "ipotesi modellistica"],
    ["Simulazione", "N", N, "intervalli temporali"],
    ["Simulazione", "dt", "1/252", "griglia principale"],
    ["Simulazione", "M", M, "repliche Monte Carlo"],
    ["Simulazione", "seed", seed_value, "seme pseudo-casuale"]
]

tabella_1 = pd.DataFrame(dati_tabella_1, columns=["Componente", "Parametro", "Valore", "Natura"])

# Formattazione per la corretta visualizzazione nel notebook
tabella_1.style.set_caption("Tabella 1: Parametri del caso").hide(axis="index")

# CELLA 7
# ====================================================================
# SIMULAZIONE FATTORI (TASSO E INDICE)
# ====================================================================

np.random.seed(seed_value)

Z1 = np.random.standard_normal((M, N))
Z2 = np.random.standard_normal((M, N))

Z_S = Z1
Z_r = rho * Z1 + np.sqrt(1 - rho**2) * Z2

r = np.zeros((M, N + 1))
S = np.zeros((M, N + 1))

r[:, 0] = r_0
S[:, 0] = S_0

for j in range(N):
    r_old = r[:, j]
    S_old = S[:, j]
    
    r_new = r_old + kappa_r * (theta_r - r_old) * dt + \
            sigma_r * np.sqrt(np.maximum(r_old, 0)) * np.sqrt(dt) * Z_r[:, j]
    
    S_new = S_old * np.exp((r_old - q - 0.5 * sigma_S**2) * dt + sigma_S * np.sqrt(dt) * Z_S[:, j])
    
    r[:, j + 1] = r_new
    S[:, j + 1] = S_new

mean_S = np.mean(S, axis=0)

# ====================================================================
# CONTROLLI RICHIESTI
# ====================================================================

print("--- CONTROLLI TAPPA 2 ---")
corr_empirica = np.corrcoef(Z_S.flatten(), Z_r.flatten())[0, 1]
print(f"Controllo 1 - Correlazione empirica shock: {corr_empirica:.4f} (Attesa: {rho})")

s_minimo = np.min(S)
s_positivo = np.all(S > 0)
print(f"Controllo 2 - S_t > 0 per tutte le traiettorie e date: {s_positivo} (Minimo osservato: {s_minimo:.4f})")

num_negativi = np.sum(r < 0)
if num_negativi > 0:
    print(f"Controllo 3 - Valori negativi di r_t rilevati: {num_negativi} occorrenze.")
    print(f"              Valore minimo di r_t osservato: {np.min(r):.6f}")
else:
    print("Controllo 3 - Nessun valore negativo di r_t rilevato dalla discretizzazione.")

print("\nVerifica Media Sottostante:")
print(f"  Valore iniziale (S_0): {S_0:.2f}")
print(f"  Valore medio terminale (S_T): {mean_S[-1]:.2f}")
print("-------------------------\n")

# ====================================================================
# OUTPUT: GRAFICI DELLE TRAIETTORIE
# ====================================================================

num_plot = 100
time_grid = np.linspace(0, T, N + 1)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].plot(time_grid, S[:num_plot, :].T, lw=0.5, alpha=0.4)

# Modifica della linea e inserimento annotazioni
axes[0].plot(time_grid, mean_S, color='black', lw=1.2, label='Media empirica $S_t$')
axes[0].text(time_grid[0], mean_S[0] + 70, f"{mean_S[0]:.2f}", color='black', fontweight='bold', fontsize=9, ha='left')
axes[0].text(time_grid[-1], mean_S[-1] + 70, f"{mean_S[-1]:.2f}", color='black', fontweight='bold', fontsize=9, ha='right')

axes[0].set_title("Grafico 1: Traiettorie simulate di EURO STOXX 50 ($S_t$)")
axes[0].set_xlabel("Tempo (anni)")
axes[0].set_ylabel("Livello Indice")
axes[0].legend()
axes[0].grid(True, alpha=0.3)

axes[1].plot(time_grid, r[:num_plot, :].T, lw=0.5, alpha=0.4)
axes[1].set_title("Grafico 2: Traiettorie simulate del tasso nominale ($r_t$)")
axes[1].set_xlabel("Tempo (anni)")
axes[1].set_ylabel("Tasso di interesse")
axes[1].axhline(theta_r, color='black', linestyle='--', label=r'Livello di lungo periodo ($\theta_r$)')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# CELLA 9
# ====================================================================
# FIXING, PAYOFF E ATTUALIZZAZIONE
# ====================================================================

# 1. Individuazione delle date di fixing
# 12 fixing su 252 passi corrispondono a passi multipli di 21
passo_fixing = int(N / fixing_mensili)
indici_fixing = [h * passo_fixing for h in range(1, fixing_mensili + 1)]

# Estrazione dei valori di S_t ai fixing (matrice M x 12)
S_fixing = S[:, indici_fixing]

# 2. Calcolo Media Asiatica (A_T)
A_T = np.mean(S_fixing, axis=1)

# 3. Calcolo Payoff non attualizzato (H_T)
H_T = np.maximum(A_T - K, 0)

# 4. Attualizzazione
# L'integrale approssimato con Riemann sinistra richiede i valori da t_0 a t_{N-1}
# Estraiamo le prime N colonne della matrice r (indici da 0 a N-1)
integrale_r = np.sum(r[:, :N], axis=1) * dt
D_hat = np.exp(-integrale_r)

# Valore attualizzato della call asiatica (V)
V = D_hat * H_T

# ====================================================================
# CONTROLLI RICHIESTI
# ====================================================================

print("--- CONTROLLI TAPPA 3 ---")

# Controllo 4: Limiti della media asiatica
min_S_fixing = np.min(S_fixing, axis=1)
max_S_fixing = np.max(S_fixing, axis=1)
check_4 = np.all((A_T >= min_S_fixing) & (A_T <= max_S_fixing))
print(f"Controllo 4 - min(S_tau) <= A_T <= max(S_tau) per ogni replica: {check_4}")

# Controllo 5: Proprietà del payoff
check_5a = np.all(H_T >= 0)
check_5b = np.all(H_T[A_T <= K] == 0)
print(f"Controllo 5 - H_T >= 0 per ogni replica: {check_5a}")
print(f"              H_T nullo se A_T <= K: {check_5b}")

# Controllo 6: Costruzione fattore di sconto
check_6a = np.all(D_hat > 0)
num_passi_integrale = r[:, :N].shape[1]
print(f"Controllo 6 - D(0,T) > 0 per ogni replica: {check_6a}")
print(f"              L'integrale è stato calcolato su {num_passi_integrale} passi (da t_0 a t_251)")

# Controllo 7: Formula del valore attualizzato
check_7 = np.allclose(V, D_hat * H_T)
print(f"Controllo 7 - V^(k) = D^(k)(0,T) * H_T^(k) per ogni replica: {check_7}")

print("-------------------------\n")

# ====================================================================
# OUTPUT: GRAFICI DELLE DISTRIBUZIONI
# ====================================================================

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Grafico 3: Distribuzione simulata di A_T
axes[0].hist(A_T, bins=100, color='skyblue', edgecolor='black', alpha=0.7)
axes[0].axvline(K, color='red', linestyle='--', linewidth=2, label=f'Strike K = {K}')
axes[0].set_title("Grafico 3: Distribuzione simulata media asiatica ($A_T$)")
axes[0].set_xlabel("Livello della media $A_T$")
axes[0].set_ylabel("Frequenza (numero di repliche)")
axes[0].legend()
axes[0].grid(axis='y', alpha=0.3)

# Grafico 4a: Distribuzione di tutti i valori attualizzati V
axes[1].hist(V, bins=100, color='lightgreen', edgecolor='black', alpha=0.7)
axes[1].set_title("Grafico 4a: Tutti i valori attualizzati ($V^{(k)}$)")
axes[1].set_xlabel("Valore attualizzato $V^{(k)}$")
axes[1].set_ylabel("Frequenza (numero di repliche)")
axes[1].grid(axis='y', alpha=0.3)

# Grafico 4b: Distribuzione dei valori attualizzati strettamente positivi V > 0
V_positivi = V[V > 0]
axes[2].hist(V_positivi, bins=100, color='mediumseagreen', edgecolor='black', alpha=0.7)
axes[2].set_title("Grafico 4b: Valori attualizzati positivi ($V^{(k)} > 0$)")
axes[2].set_xlabel("Valore attualizzato $V^{(k)}$")
axes[2].set_ylabel("Frequenza (numero di repliche)")
axes[2].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()

# CELLA 11
# ====================================================================
# AGGREGAZIONE STATISTICA E PRICING
# ====================================================================

# 1. Estrazione dei valori terminali
S_T = S[:, -1]
r_T = r[:, -1]

# 2. Calcolo metriche per Tabella 2 (Statistiche di S_T, r_T, A_T)
# Utilizziamo ddof=1 per la deviazione standard campionaria non distorta
stats_S_T = (np.mean(S_T), np.std(S_T, ddof=1))
stats_r_T = (np.mean(r_T), np.std(r_T, ddof=1))
stats_A_T = (np.mean(A_T), np.std(A_T, ddof=1))

# Creazione Tabella 2
dati_tabella_2 = [
    ["Sottostante a scadenza (S_T)", stats_S_T[0], stats_S_T[1]],
    ["Tasso nominale a scadenza (r_T)", stats_r_T[0], stats_r_T[1]],
    ["Media asiatica (A_T)", stats_A_T[0], stats_A_T[1]]
]
tabella_2 = pd.DataFrame(dati_tabella_2, columns=["Variabile", "Media Simulata", "Deviazione Standard Simulata"])

# 3. Calcolo metriche per Tabella 3 (Pricing e Probabilità)
# Probabilità simulata di esercizio sotto Q
prob_esercizio = np.mean(A_T > K)

# Payoff medio
payoff_medio = np.mean(H_T)

# Prezzo Monte Carlo
V_M = np.mean(V)

# Errore Standard Monte Carlo
std_V = np.std(V, ddof=1)
SE_V = std_V / np.sqrt(M)

# Intervallo di confidenza al 95%
CI_lower = V_M - 1.96 * SE_V
CI_upper = V_M + 1.96 * SE_V
CI_str = f"[{CI_lower:.4f}, {CI_upper:.4f}]"

# Creazione Tabella 3
dati_tabella_3 = [
    ["Probabilità simulata di esercizio Q(A_T > K)", f"{prob_esercizio:.4%}"],
    ["Payoff medio non attualizzato (H_T)", f"{payoff_medio:.4f}"],
    ["Prezzo Monte Carlo della call asiatica (V_M)", f"{V_M:.4f}"],
    ["Errore standard Monte Carlo (SE)", f"{SE_V:.6f}"],
    ["Intervallo di confidenza al 95%", CI_str]
]
tabella_3 = pd.DataFrame(dati_tabella_3, columns=["Metrica", "Valore Stimato"])

# ====================================================================
# OUTPUT: TABELLE RISULTATI
# ====================================================================

# Per visualizzare correttamente due DataFrame in Jupyter uno di seguito all'altro, 
# si usa la funzione display() del modulo IPython.display. 
from IPython.display import display

print("OUTPUT RICHIESTO: TABELLA 2")
display(tabella_2.style.set_caption("Tabella 2: Statistiche dei fattori e della media asiatica").hide(axis="index").format({
    "Media Simulata": "{:.6f}",
    "Deviazione Standard Simulata": "{:.6f}"
}))

print("\nOUTPUT RICHIESTO: TABELLA 3")
display(tabella_3.style.set_caption("Tabella 3: Sintesi del payoff e del pricing").hide(axis="index"))

# CELLA 13
# ====================================================================
# DIAGNOSTICA E STABILITÀ
# ====================================================================

# Funzione incapsulata per rigenerare simulazioni e pricing
def esegui_simulazione_e_pricing(M_sim, N_sim, seed_val):
    # Fissaggio del seed per riproducibilità
    np.random.seed(seed_val)
    
    dt_sim = T / N_sim
    
    # 1. Shock
    Z1 = np.random.standard_normal((M_sim, N_sim))
    Z2 = np.random.standard_normal((M_sim, N_sim))
    Z_S = Z1
    Z_r = rho * Z1 + np.sqrt(1 - rho**2) * Z2
    
    # 2. Inizializzazione
    r_sim = np.zeros((M_sim, N_sim + 1))
    S_sim = np.zeros((M_sim, N_sim + 1))
    r_sim[:, 0] = r_0
    S_sim[:, 0] = S_0
    
    # 3. Loop temporale
    for j in range(N_sim):
        r_old = r_sim[:, j]
        S_old = S_sim[:, j]
        
        r_new = r_old + kappa_r * (theta_r - r_old) * dt_sim + \
                sigma_r * np.sqrt(np.maximum(r_old, 0)) * np.sqrt(dt_sim) * Z_r[:, j]
        
        S_new = S_old * np.exp((r_old - q - 0.5 * sigma_S**2) * dt_sim + sigma_S * np.sqrt(dt_sim) * Z_S[:, j])
        
        r_sim[:, j + 1] = r_new
        S_sim[:, j + 1] = S_new
        
    # 4. Fixing (adattamento dinamico alla griglia)
    passo_fix = int(N_sim / fixing_mensili)
    idx_fix = [h * passo_fix for h in range(1, fixing_mensili + 1)]
    
    S_fix = S_sim[:, idx_fix]
    A_T_sim = np.mean(S_fix, axis=1)
    H_T_sim = np.maximum(A_T_sim - K, 0)
    
    # 5. Attualizzazione
    integrale = np.sum(r_sim[:, :N_sim], axis=1) * dt_sim
    D_hat_sim = np.exp(-integrale)
    
    V_sim = D_hat_sim * H_T_sim
    
    prezzo_m = np.mean(V_sim)
    std_m = np.std(V_sim, ddof=1)
    se_m = std_m / np.sqrt(M_sim)
    
    return prezzo_m, se_m, std_m

# Analisi su diverse numerosità Monte Carlo
M_list = [1000, 5000, 10000, 50000]
risultati_diagnostica = []

for m_val in M_list:
    p_m, se_m, std_m = esegui_simulazione_e_pricing(m_val, N, seed_value)
    # Conserviamo anche la stima asintotica della deviazione standard per il Controllo 8
    proxy_costante = se_m * np.sqrt(m_val)
    risultati_diagnostica.append([m_val, p_m, se_m, proxy_costante])

# Creazione Tabella 4
tabella_4 = pd.DataFrame(risultati_diagnostica, columns=[
    "Repliche (M)", 
    "Prezzo Stimato", 
    "Errore Standard (SE)", 
    "SE * radice(M) (Proxy Dev. Std.)"
])

# Analisi di stabilità su griglia temporale raddoppiata (N=504, ovvero dt dimezzato)
N_fine = 504
prezzo_Nfine, se_Nfine, _ = esegui_simulazione_e_pricing(M, N_fine, seed_value)

# ====================================================================
# CONTROLLI RICHIESTI
# ====================================================================

print("--- CONTROLLI TAPPA 5 ---")

# Controllo 8: Decadimento O(M^{-1/2})
print("Controllo 8 - Decadimento Errore Standard in O(M^{-1/2}):")
for row in risultati_diagnostica:
    print(f"  M = {row[0]:5d} -> SE = {row[2]:.6f} | Costante asintotica [SE * sqrt(M)] = {row[3]:.4f}")
print("  (Il prodotto approssimativamente costante dimostra il decadimento con radice di M)")

# Controllo 9: Stabilità temporale
prezzo_riferimento = risultati_diagnostica[-1][1] # Prezzo per M=50.000, N=252
diff_assoluta = abs(prezzo_riferimento - prezzo_Nfine)
print(f"\nControllo 9 - Stabilità griglia temporale:")
print(f"  Prezzo con N=252: {prezzo_riferimento:.4f}")
print(f"  Prezzo con N=504: {prezzo_Nfine:.4f}")
print(f"  Differenza assoluta: {diff_assoluta:.4f}")

# Controllo 10: Riproducibilità
print(f"\nControllo 10 - Riproducibilità risultati:")
print(f"  Prezzo M=50.000 (ricavato ora):       {prezzo_riferimento:.4f}")
print(f"  Prezzo M=50.000 (Tappa 4 originale):  {V_M:.4f}")
check_repro = np.isclose(prezzo_riferimento, V_M)
print(f"  Risultati coincidenti tramite seed={seed_value}: {check_repro}")

print("-------------------------\n")

# ====================================================================
# OUTPUT: TABELLA E GRAFICO
# ====================================================================

from IPython.display import display

print("OUTPUT RICHIESTO: TABELLA 4")
display(tabella_4.style.set_caption("Tabella 4: Diagnostica Monte Carlo").hide(axis="index").format({
    "Prezzo Stimato": "{:.4f}",
    "Errore Standard (SE)": "{:.6f}",
    "SE * radice(M) (Proxy Dev. Std.)": "{:.4f}"
}))

# Grafico 5: Convergenza della stima Monte Carlo
# Utilizziamo le medie progressive del vettore V già calcolato in Tappa 3/4 per tracciare la curva completa in modo efficiente
M_grid = np.arange(1, M + 1)
running_mean = np.cumsum(V) / M_grid
running_SE = std_V / np.sqrt(M_grid)

# Tronchiamo i primi 100 valori per evitare che l'altissima volatilità iniziale distorca l'asse Y
start_idx = 100

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(M_grid[start_idx:], running_mean[start_idx:], color='blue', lw=1.5, label='Prezzo stimato cumulativo ($\widehat{V}_m$)')
ax.plot(M_grid[start_idx:], V_M + 1.96 * running_SE[start_idx:], color='red', linestyle='--', lw=1.2, label='Intervallo di confidenza al 95%')
ax.plot(M_grid[start_idx:], V_M - 1.96 * running_SE[start_idx:], color='red', linestyle='--', lw=1.2)
ax.axhline(V_M, color='black', linestyle='-', lw=1.5, alpha=0.7, label=f'Prezzo finale ($M=50.000$): {V_M:.4f}')

ax.set_title("Grafico 5: Convergenza della stima Monte Carlo al crescere di M")
ax.set_xlabel("Numero di repliche ($m$)")
ax.set_ylabel("Prezzo Stimato (Euro)")
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()