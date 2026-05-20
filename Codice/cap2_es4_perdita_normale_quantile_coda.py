from pathlib import Path
import math

import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# Capitolo 2 - Esercizio 4
# Densita' della perdita L e probabilita' di coda
# ============================================================
#
# Dati dell'esercizio:
#
#   R ~ N(0.006, 0.04^2)
#
# Perdita percentuale:
#
#   L = -R
#
# Quindi:
#
#   L ~ N(-0.006, 0.04^2)
#
# Il grafico rappresenta:
#   1. la densita' di L;
#   2. il quantile q_0.99(L);
#   3. la soglia 0.10;
#   4. l'area di coda destra P(L > 0.10).
#
# Output:
#   - file PNG
#   - file SVG
#
# ============================================================
# COME PERSONALIZZARE IL GRAFICO
# ============================================================
#
# 1. Cartella di salvataggio:
#       modificare output_dir
#
# 2. Nome dei file:
#       modificare output_name
#
# 3. Parametri della distribuzione di R:
#       modificare mu_R e sigma_R
#
# 4. Livello del quantile:
#       modificare alpha
#
# 5. Soglia di perdita da evidenziare:
#       modificare loss_threshold
#
# ============================================================


# ------------------------------------------------------------
# Cartella di salvataggio dei grafici
# ------------------------------------------------------------

output_dir = Path(
#    r"E:\Didattica\MQF\Github\CORSO-MQF\01_Manuale\graphics"
    r"E:\Didattica\MQF\graphics"
)
output_dir.mkdir(parents=True, exist_ok=True)

output_name = "cap2_es4_perdita_normale_quantile_coda"


# ------------------------------------------------------------
# Parametri del rendimento R
# ------------------------------------------------------------

mu_R = 0.006
sigma_R = 0.04

# Distribuzione della perdita L = -R
mu_L = -mu_R
sigma_L = sigma_R

# Livello del quantile richiesto
alpha = 0.99

# Quantile standard della normale:
# P(Z <= z_alpha) = alpha
z_alpha = 2.326

# Quantile della perdita
q_alpha_L = mu_L + sigma_L * z_alpha

# Soglia di perdita per cui calcolare la probabilita' di coda
loss_threshold = 0.10


# ------------------------------------------------------------
# Funzioni della normale
# ------------------------------------------------------------

def normal_pdf(x, mu, sigma):
    """
    Densita' della distribuzione normale N(mu, sigma^2).
    """
    return (
        1.0 / (sigma * math.sqrt(2.0 * math.pi))
        * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    )


def standard_normal_cdf(x):
    """
    Funzione di distribuzione della normale standard.
    Usa la funzione erf della libreria math.
    """
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def normal_cdf(x, mu, sigma):
    """
    Funzione di distribuzione della normale N(mu, sigma^2).
    """
    z = (x - mu) / sigma
    return standard_normal_cdf(z)


# ------------------------------------------------------------
# Calcoli numerici utili
# ------------------------------------------------------------

# Probabilita' di coda destra oltre la soglia loss_threshold
prob_tail = 1.0 - normal_cdf(loss_threshold, mu_L, sigma_L)

# Dominio del grafico
x_min = mu_L - 4.0 * sigma_L
x_max = max(loss_threshold, q_alpha_L) + 2.0 * sigma_L
num_points = 1600

x = np.linspace(x_min, x_max, num_points)
y = normal_pdf(x, mu_L, sigma_L)

# Area di coda destra: x >= loss_threshold
mask_tail = x >= loss_threshold
x_tail = x[mask_tail]
y_tail = y[mask_tail]


# ------------------------------------------------------------
# Parametri grafici
# ------------------------------------------------------------

figure_width = 9.2
figure_height = 5.8
png_dpi = 300

axis_label_fontsize = 18
tick_fontsize = 15
annotation_fontsize = 18


# ------------------------------------------------------------
# Creazione del grafico
# ------------------------------------------------------------

fig, ax = plt.subplots(figsize=(figure_width, figure_height))

# Curva della densita'
ax.plot(x, y, linewidth=2.6)

# Area di coda destra oltre 0.10
ax.fill_between(x_tail, y_tail, alpha=0.35)

# Verticale nel quantile q_0.99(L)
ax.axvline(q_alpha_L, linestyle="--", linewidth=2.0)

# Verticale nella soglia 0.10
ax.axvline(loss_threshold, linestyle=":", linewidth=2.2)

# Verticale nella media della perdita
ax.axvline(mu_L, linestyle="--", linewidth=1.3, alpha=0.7)

# Annotazioni principali
ax.text(
    0.50,
    0.93,
    r"$L=-R\sim\mathcal{N}(-0.006,\ 0.04^2)$",
    transform=ax.transAxes,
    fontsize=annotation_fontsize,
    ha="center",
    va="center",
)

ax.text(
    0.68,
    0.82,
    rf"$q_{{0.99}}(L)\simeq {q_alpha_L:.4f}$",
    transform=ax.transAxes,
    fontsize=annotation_fontsize,
    ha="center",
    va="center",
)

ax.text(
    0.72,
    0.70,
    rf"$\mathrm{{P}}(L>0.10)\simeq {prob_tail:.4f}$",
    transform=ax.transAxes,
    fontsize=annotation_fontsize,
    ha="center",
    va="center",
)

ax.text(
    0.33,
    0.60,
    r"$\mathrm{P}(L\leq q_{0.99}(L))=0.99$",
    transform=ax.transAxes,
    fontsize=annotation_fontsize,
    ha="center",
    va="center",
)

# Assi
ax.set_xlim(x_min, x_max)
ax.set_ylim(0, max(y) * 1.18)

ax.set_xlabel(r"$\ell$", fontsize=axis_label_fontsize)
ax.set_ylabel(r"$f_L(\ell)$", fontsize=axis_label_fontsize)

# Tick principali sull'asse x
ax.set_xticks([mu_L, q_alpha_L, loss_threshold])
ax.set_xticklabels(
    [r"$\mu_L$", r"$q_{0.99}(L)$", r"$0.10$"],
    fontsize=tick_fontsize,
)

ax.tick_params(axis="x", pad=10)
ax.tick_params(axis="y", labelsize=tick_fontsize)

# Griglia leggera
ax.grid(True, linewidth=0.5, alpha=0.4)

# Rimozione delle cornici superiore e destra
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

fig.tight_layout()


# ------------------------------------------------------------
# Salvataggio
# ------------------------------------------------------------

png_path = output_dir / f"{output_name}.png"
svg_path = output_dir / f"{output_name}.svg"

fig.savefig(png_path, dpi=png_dpi, bbox_inches="tight")
fig.savefig(svg_path, bbox_inches="tight")

plt.close(fig)

print(f"Creato file PNG: {png_path}")
print(f"Creato file SVG: {svg_path}")
print(f"q_0.99(L) = {q_alpha_L:.6f}")
print(f"P(L > 0.10) = {prob_tail:.6f}")