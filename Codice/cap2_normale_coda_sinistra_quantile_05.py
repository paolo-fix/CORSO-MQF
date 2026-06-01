from pathlib import Path
import math

import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# Capitolo 2 - Coda sinistra e quantile di una normale
# ============================================================
#
# Questo script genera un grafico della densita' normale
# del rendimento R e mette in evidenza:
#
#   - la coda sinistra di probabilita' alpha
#   - il quantile q_alpha(R)
#
# Nel caso illustrato:
#
#   R ~ N(mu, sigma^2)
#   mu = 0.008
#   sigma = 0.035
#   alpha = 0.05
#
# Il grafico e' pensato per la Sezione 2.8 (probabilita' di
# coda e quantili) oppure per l'esempio normale della Sezione 2.13.
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
# 3. Parametri della normale:
#       modificare mu e sigma
#
# 4. Livello di coda:
#       modificare alpha
#
# 5. Quantile normale standard:
#       modificare z_alpha
#       (se si usa un alpha diverso)
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


# ------------------------------------------------------------
# Nome base dei file di output
# ------------------------------------------------------------

output_name = "Cap02_normale_coda_sinistra_quantile_05"


# ------------------------------------------------------------
# Parametri della distribuzione normale
# ------------------------------------------------------------

mu = 0.008
sigma = 0.035

# Livello di coda
alpha = 0.05

# Quantile della normale standard:
# P(Z <= z_alpha) = alpha
#
# Per alpha = 0.05:
z_alpha = -1.645

# Quantile della variabile R
q_alpha = mu + sigma * z_alpha


# ------------------------------------------------------------
# Parametri grafici
# ------------------------------------------------------------

figure_width = 9.0
figure_height = 5.6
png_dpi = 300

axis_label_fontsize = 18
tick_fontsize = 15
annotation_fontsize = 19


# ------------------------------------------------------------
# Dominio del grafico
# ------------------------------------------------------------
#
# Si usa un intervallo centrato in media, sufficientemente ampio
# per mostrare bene la coda.

x_min = mu - 4.0 * sigma
x_max = mu + 4.0 * sigma
num_points = 1400


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


# ------------------------------------------------------------
# Costruzione dei dati
# ------------------------------------------------------------

x = np.linspace(x_min, x_max, num_points)
y = normal_pdf(x, mu, sigma)

# Area di coda sinistra: x <= q_alpha
mask = x <= q_alpha
x_tail = x[mask]
y_tail = y[mask]


# ------------------------------------------------------------
# Creazione del grafico
# ------------------------------------------------------------

fig, ax = plt.subplots(figsize=(figure_width, figure_height))

# Curva della densita'
ax.plot(x, y, linewidth=2.6)

# Area della coda sinistra
ax.fill_between(x_tail, y_tail, alpha=0.35)

# Linea verticale nel quantile q_alpha
ax.axvline(q_alpha, linestyle="--", linewidth=2.0)

# Eventuale linea verticale nella media
ax.axvline(mu, linestyle=":", linewidth=1.6)

# Etichette principali
ax.text(
    0.50,
    0.93,
    r"$R\sim\mathcal{N}(0.008,\ 0.035^2)$",
    transform=ax.transAxes,
    fontsize=annotation_fontsize,
    ha="center",
    va="center",
)

ax.text(
    0.24,
    0.72,
    r"$\mathrm{P}(R\leq q_{0.05}(R))=0.05$",
    transform=ax.transAxes,
    fontsize=annotation_fontsize,
    ha="center",
    va="center",
)

ax.text(
    0.70,
    0.80,
    r"$q_{0.05}(R)=\mu+\sigma z_{0.05}\simeq -0.0496$",
    transform=ax.transAxes,
    fontsize=annotation_fontsize,
    ha="center",
    va="center",
)

# Etichette puntuali sull'asse x

# Assi
ax.set_xlim(x_min, x_max)
ax.set_ylim(0, max(y) * 1.18)

ax.set_xlabel(r"$r$", fontsize=axis_label_fontsize)
ax.set_ylabel(r"$f_R(r)$", fontsize=axis_label_fontsize)

# Tick principali
ax.set_xticks([q_alpha, mu])
ax.set_xticklabels(
    [r"$q_{0.05}(R)$", r"$\mu$"],
    fontsize=tick_fontsize,
)

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
print(f"Quantile q_alpha(R): {q_alpha:.6f}")
