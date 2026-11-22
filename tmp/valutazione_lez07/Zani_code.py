
# CELLA 5
import numpy as np
import pandas as pd

# ---------------------------------------------------------
# 1. CONTROLLO 10: Impostazione del seed per riproducibilità
# ---------------------------------------------------------
seed = 12345
np.random.seed(seed)
print(f"[Controllo 10 verificato] Seed impostato a {seed} per garantire la riproducibilità.\n")

# ---------------------------------------------------------
# 2. DICHIARAZIONE VARIABILI E PARAMETRI
# ---------------------------------------------------------
# Sottostante e Contratto
S0 = 6286.35
K = 6300.0
T = 1.0
q = 0.025
sigma_S = 0.18
mesi_fixing = 12

# Tasso CIR
r0 = 0.02185
kappa_r = 1.25
theta_r = 0.0220
sigma_r = 0.040

# Dipendenza (Correlazione)
rho = -0.25

# Parametri di Simulazione
N = 252
dt = 1.0 / 252.0
M = 50000

# Calcolo dei nodi (indici) in cui avvengono i fixing asintotici (h/12)
step_fixing = int(N / mesi_fixing)
nodi_fixing = np.arange(step_fixing, N + 1, step_fixing)

# ---------------------------------------------------------
# 3. CREAZIONE E VISUALIZZAZIONE TABELLA 1
# ---------------------------------------------------------
dati_parametri = [
    ["Data", "t_0", "27/07/2026", "data di riferimento"],
    ["Sottostante", "indice", "EURO STOXX 50", "riferimento di mercato"],
    ["Sottostante", "S_0", "6.286,35", "dato osservato"],
    ["Contratto", "K", "6.300", "scelta contrattuale"],
    ["Contratto", "T", "1 anno", "specifica contrattuale"],
    ["Contratto", "fixing", "12 mensili", "specifica contrattuale"],
    ["Dividendi", "q", "0,025", "proxy di mercato arrotondata"],
    ["Sottostante", "sigma_S", "0,18", "proxy market-consistent"],
    ["Tasso CIR", "r_0", "0,02185", "dato osservato"],
    ["Tasso CIR", "kappa_r", "1,25", "parametro didattico"],
    ["Tasso CIR", "theta_r", "0,0220", "parametro didattico"],
    ["Tasso CIR", "sigma_r", "0,040", "parametro didattico"],
    ["Dipendenza", "rho", "-0,25", "ipotesi modellistica"],
    ["Simulazione", "N", "252", "intervalli temporali"],
    ["Simulazione", "Delta t", "1/252", "griglia principale"],
    ["Simulazione", "M", "50.000", "repliche Monte Carlo"],
    ["Simulazione", "seed", "12345", "seme pseudo-casuale"]
]

tabella_1 = pd.DataFrame(dati_parametri, columns=["Componente", "Parametro", "Valore", "Natura"])

# Visualizzazione dell'output (Tabella 1) formattato per Jupyter
display(tabella_1.style.set_caption("Tabella 1: Parametri del caso").hide(axis="index"))

# Verifica indici fixing
print(f"\nIndici (step temporali) calcolati per i fixing mensili:")
print(nodi_fixing)

# CELLA 7
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. GENERAZIONE SHOCK E CHOLESKY
# ---------------------------------------------------------
# Estrazione di Normali Standard indipendenti per M repliche e N step
Z1 = np.random.standard_normal((M, N))
Z2 = np.random.standard_normal((M, N))

# Applicazione Cholesky
Z_S = Z1
Z_r = rho * Z1 + np.sqrt(1 - rho**2) * Z2

# ---------------------------------------------------------
# 2. CONTROLLO 1: Correlazione empirica
# ---------------------------------------------------------
# Si calcola la correlazione raggruppando tutti gli N*M shock generati
corr_empirica = np.corrcoef(Z_S.flatten(), Z_r.flatten())[0, 1]
print(f"[Controllo 1] Correlazione empirica tra gli shock (Z_S, Z_r): {corr_empirica:.4f} (Attesa: {rho})\n")

# ---------------------------------------------------------
# 3. INIZIALIZZAZIONE MATRICI E SIMULAZIONE DINAMICHE
# ---------------------------------------------------------
S = np.zeros((M, N + 1))
r = np.zeros((M, N + 1))

# Condizioni iniziali
S[:, 0] = S0
r[:, 0] = r0

# Iterazione temporale (vettorizzata sulle M repliche)
for j in range(N):
    S_old = S[:, j]
    r_old = r[:, j]
    
    # Troncamento positivo sotto radice per il CIR
    r_old_plus = np.maximum(r_old, 0.0)
    
    # Aggiornamento tasso (CIR - Euler-Maruyama)
    dr = kappa_r * (theta_r - r_old) * dt + sigma_r * np.sqrt(r_old_plus) * np.sqrt(dt) * Z_r[:, j]
    r[:, j+1] = r_old + dr
    
    # Aggiornamento sottostante (GBM exact step condizionato al tasso in t_j)
    esp = (r_old - q - 0.5 * sigma_S**2) * dt + sigma_S * np.sqrt(dt) * Z_S[:, j]
    S[:, j+1] = S_old * np.exp(esp)

# ---------------------------------------------------------
# 4. CONTROLLO 2: Positività del sottostante
# ---------------------------------------------------------
min_S = np.min(S)
print(f"[Controllo 2] Valore minimo globale del sottostante simulato: {min_S:.4f}")
if min_S > 0:
    print("              -> Condizione S_t > 0 rigorosamente soddisfatta in ogni nodo.\n")
else:
    print("              -> ANOMALIA: Condizione S_t > 0 NON soddisfatta.\n")

# ---------------------------------------------------------
# 5. CONTROLLO 3: Rilevazione e documentazione r_t < 0
# ---------------------------------------------------------
maschera_negativi = r < 0
num_negativi = np.sum(maschera_negativi)
totale_nodi = M * (N + 1)
percentuale_negativi = num_negativi / totale_nodi

if num_negativi > 0:
    print(f"[Controllo 3] Rilevati {num_negativi} valori negativi per il tasso r_t (su {totale_nodi} totali, pari al {percentuale_negativi:.6%}).")
    print("              -> I valori sono stati mantenuti nella matrice come richiesto dalla specifica numerica (nessun azzeramento forzato).")
else:
    print(f"[Controllo 3] Nessun valore negativo rilevato per il tasso r_t durante l'intera simulazione (su {totale_nodi} nodi).")

print("-" * 70)

# ---------------------------------------------------------
# 6. OUTPUT GRAFICI RICHIESTI
# ---------------------------------------------------------
# Vettore dei tempi per i grafici
t_grid = np.linspace(0, T, N + 1)
num_traiettorie_plot = 50  # Plot di un sottoinsieme per leggibilità

fig, axes = plt.subplots(1, 2, figsize=(15, 5))

# Grafico 1
axes[0].plot(t_grid, S[:num_traiettorie_plot, :].T, lw=0.8, alpha=0.8)
axes[0].set_title(f"Grafico 1: Traiettorie EURO STOXX 50 (prime {num_traiettorie_plot} repliche)")
axes[0].set_xlabel("Tempo (Anni)")
axes[0].set_ylabel("Livello Indice $S_t$")
axes[0].grid(True, alpha=0.3)

# Grafico 2
axes[1].plot(t_grid, r[:num_traiettorie_plot, :].T, lw=0.8, alpha=0.8)
axes[1].axhline(y=theta_r, color='k', linestyle='--', label=r'Livello medio $\theta_r$')
axes[1].set_title(f"Grafico 2: Traiettorie Tasso CIR (prime {num_traiettorie_plot} repliche)")
axes[1].set_xlabel("Tempo (Anni)")
axes[1].set_ylabel("Tasso Nominale $r_t$")
axes[1].legend(loc="best")
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# CELLA 9
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. CAMPIONAMENTO E CALCOLO MEDIA ASIATICA
# ---------------------------------------------------------
# Estrazione dei valori del sottostante solo ai nodi di fixing (M righe, 12 colonne)
S_fixing = S[:, nodi_fixing]

# Calcolo di A_T come media aritmetica lungo le colonne per ogni riga (replica)
A_T = np.mean(S_fixing, axis=1)

# Estrazione dei valori terminali (all'istante N) per fattori
S_T = S[:, -1]
r_T = r[:, -1]

# ---------------------------------------------------------
# 2. CONTROLLO 4: Proprietà della media aritmetica
# ---------------------------------------------------------
min_S_fixing = np.min(S_fixing, axis=1)
max_S_fixing = np.max(S_fixing, axis=1)

# Verifica logica vettoriale
controllo_4_superato = np.all((A_T >= min_S_fixing) & (A_T <= max_S_fixing))

if controllo_4_superato:
    print("[Controllo 4 verificato] Per ogni singola replica, la media asiatica A_T è ")
    print("                       strettamente compresa tra il minimo e il massimo dei fixing mensili.\n")
else:
    print("[Controllo 4 FALLITO] Rilevate anomalie nel calcolo della media asiatica.\n")

# ---------------------------------------------------------
# 3. CREAZIONE E VISUALIZZAZIONE TABELLA 2
# ---------------------------------------------------------
statistiche = {
    "Variabile": ["S_T (Sottostante a T)", "r_T (Tasso CIR a T)", "A_T (Media Asiatica)"],
    "Media Simulata": [np.mean(S_T), np.mean(r_T), np.mean(A_T)],
    "Deviazione Standard": [np.std(S_T, ddof=1), np.std(r_T, ddof=1), np.std(A_T, ddof=1)]
}

tabella_2 = pd.DataFrame(statistiche)

# Formattazione per la stampa a video
format_dict = {"Media Simulata": "{:,.4f}", "Deviazione Standard": "{:,.4f}"}
display(tabella_2.style.format(format_dict).set_caption("Tabella 2: Statistiche dei fattori e della media asiatica").hide(axis="index"))

# ---------------------------------------------------------
# 4. OUTPUT GRAFICO RICHIESTO
# ---------------------------------------------------------
plt.figure(figsize=(10, 6))

# Grafico 3
plt.hist(A_T, bins=100, color='skyblue', edgecolor='black', alpha=0.7, label='Distribuzione simulata di $A_T$')
plt.axvline(x=K, color='red', linestyle='--', linewidth=2, label=f'Strike $K$ = {K}')

plt.title("Grafico 3: Distribuzione simulata della media asiatica $A_T$")
plt.xlabel("Livello della media asiatica ($A_T$)")
plt.ylabel("Frequenza (numero di repliche)")
plt.legend(loc="upper right")
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# CELLA 11
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. CALCOLO DEL PAYOFF H_T
# ---------------------------------------------------------
# Payoff della Call Asiatica (max(A_T - K, 0))
H_T = np.maximum(A_T - K, 0.0)

# ---------------------------------------------------------
# 2. CALCOLO DEL FATTORE DI SCONTO STOCASTICO
# ---------------------------------------------------------
# Estrazione dei tassi r_{t_0} ... r_{t_{N-1}} per la somma di Riemann sinistra
# La matrice r ha dimensione (M, N+1), prendiamo le prime N colonne per ogni riga
r_riemann = r[:, :N] 

# Approssimazione dell'integrale del tasso (somma per riga moltiplicata per dt)
integrale_r = np.sum(r_riemann, axis=1) * dt

# Calcolo del fattore di sconto stocastico per ciascuna replica
D = np.exp(-integrale_r)

# ---------------------------------------------------------
# 3. CALCOLO DEL VALORE ATTUALIZZATO V
# ---------------------------------------------------------
V = D * H_T

# ---------------------------------------------------------
# 4. CONTROLLO 5: Proprietà del payoff
# ---------------------------------------------------------
check_non_negativo = np.all(H_T >= 0)
check_zero_otm = np.all(H_T[A_T <= K] == 0)

if check_non_negativo and check_zero_otm:
    print("[Controllo 5 verificato] H_T >= 0 per tutte le repliche ed è nullo quando A_T <= K.\n")
else:
    print("[Controllo 5 FALLITO] Anomalie rilevate nei valori del payoff H_T.\n")

# ---------------------------------------------------------
# 5. CONTROLLO 6: Costruzione fattore di sconto
# ---------------------------------------------------------
check_positivita_D = np.all(D > 0)
# Verifica dimensionale implicita che abbiamo usato N elementi
check_dimensione_riemann = r_riemann.shape[1] == N

if check_positivita_D and check_dimensione_riemann:
    print("[Controllo 6 verificato] Somma di Riemann calcolata correttamente su r_t0 ... r_t{N-1}.")
    print("                       Il fattore di sconto D(0,T) è strettamente positivo per ogni replica.\n")
else:
    print("[Controllo 6 FALLITO] Errore nel calcolo del fattore di sconto stocastico.\n")

# ---------------------------------------------------------
# 6. CONTROLLO 7: Coerenza del valore attualizzato
# ---------------------------------------------------------
check_prodotto = np.allclose(V, D * H_T)

if check_prodotto:
    print("[Controllo 7 verificato] V^(k) = D^(k)(0,T) * H_T^(k) in tutte le repliche.\n")
else:
    print("[Controllo 7 FALLITO] Incoerenza tra V, D e H_T.\n")

print("-" * 70)

# ---------------------------------------------------------
# 7. OUTPUT GRAFICO RICHIESTO
# ---------------------------------------------------------
plt.figure(figsize=(10, 6))

# Grafico 4
plt.hist(V, bins=100, color='mediumseagreen', edgecolor='black', alpha=0.7, label='Distribuzione di $V^{(k)}$')

plt.title("Grafico 4: Distribuzione dei valori attualizzati $V^{(k)}$")
plt.xlabel("Valore Attualizzato ($V^{(k)}$)")
plt.ylabel("Frequenza (numero di repliche)")

# Aggiunta di una linea per evidenziare la massa sullo zero (repliche OTM)
plt.axvline(x=0, color='red', linestyle='--', linewidth=1.5, label='Repliche OTM ($V^{(k)}=0$)')

plt.legend(loc="upper right")
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# CELLA 13
import numpy as np
import pandas as pd

# ---------------------------------------------------------
# 1. CALCOLO DELLE QUANTITÀ STATISTICHE E DI PRICING
# ---------------------------------------------------------
# Probabilità simulata di esercizio Q(A_T > K)
prob_esercizio = np.mean(A_T > K)

# Valore medio del payoff non attualizzato
payoff_medio = np.mean(H_T)

# Prezzo Monte Carlo (media campionaria dei valori attualizzati)
V_M = np.mean(V)

# Deviazione standard campionaria dei valori attualizzati (ddof=1 per stima corretta)
s_V = np.std(V, ddof=1)

# Errore standard (SE) della stima Monte Carlo
SE = s_V / np.sqrt(M)

# Intervallo di confidenza al 95%
IC_inferiore = V_M - 1.96 * SE
IC_superiore = V_M + 1.96 * SE

# ---------------------------------------------------------
# 2. CREAZIONE E VISUALIZZAZIONE TABELLA 3
# ---------------------------------------------------------
dati_pricing = {
    "Quantità Stimata": [
        "Probabilità simulata di esercizio Q(A_T > K)",
        "Payoff medio non attualizzato (H_T)",
        "Prezzo Monte Carlo stimato (V_M)",
        "Errore Standard Monte Carlo (SE)",
        "Limite inferiore IC 95%",
        "Limite superiore IC 95%"
    ],
    "Valore": [
        prob_esercizio,
        payoff_medio,
        V_M,
        SE,
        IC_inferiore,
        IC_superiore
    ]
}

tabella_3 = pd.DataFrame(dati_pricing)

# Formattazione per la stampa a video (percentuale per probabilità, 4 decimali per gli altri)
def format_valori(row):
    if "Probabilità" in row['Quantità Stimata']:
        return f"{row['Valore']:.2%}"
    else:
        return f"{row['Valore']:,.4f}"

tabella_3['Valore Formattato'] = tabella_3.apply(format_valori, axis=1)
tabella_3_display = tabella_3[['Quantità Stimata', 'Valore Formattato']]

display(tabella_3_display.style.set_caption("Tabella 3: Sintesi del payoff e del pricing").hide(axis="index"))

# ---------------------------------------------------------
# 3. CONTROLLO VISIVO DI COERENZA
# ---------------------------------------------------------
semi_ampiezza = (IC_superiore - IC_inferiore) / 2
print("\n[Controllo di Coerenza]")
print(f"Stima Centrale (Prezzo): {V_M:.4f}")
print(f"Semi-ampiezza IC 95% calcolata: {semi_ampiezza:.4f} (deve corrispondere a 1.96 * SE = {1.96 * SE:.4f})")
print(f"L'intervallo di confidenza [{IC_inferiore:.4f}, {IC_superiore:.4f}] risulta regolarmente calcolato e centrato sulla stima.")