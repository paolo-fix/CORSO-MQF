from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# Capitolo 2 - Esercizio 3
# Densita' e funzione di distribuzione affiancate
# ============================================================
#
# Variabile di perdita L con densita'
#
#   f_L(l) = c (1 + l),   0 <= l <= 1
#            0,           altrove
#
# con c = 2/3.
#
# La figura contiene due pannelli affiancati:
#
#   (1) densita' f_L(l), con area di coda destra P(L > 0.6)
#   (2) funzione di distribuzione F_L(l), con evidenza del
#       quantile q_0.95(L)
#
# Output:
#   - PNG
#   - SVG
#
# ============================================================


# ------------------------------------------------------------
# Cartella di salvataggio
# ------------------------------------------------------------

output_dir = Path(
#    r"E:\Didattica\MQF\Github\CORSO-MQF\01_Manuale\graphics"
    r"E:\Didattica\MQF\graphics"
)
output_dir.mkdir(parents=True, exist_ok=True)


output_name = "Cap02_es3_densita_cdf_affiancati"


# ------------------------------------------------------------
# Parametri del problema
# ------------------------------------------------------------

c = 2.0 / 3.0

# Soglia per la probabilita' di coda
tail_threshold = 0.6

# Livello di quantile
alpha = 0.95

# Quantile teorico:
# risolve (2l + l^2)/3 = 0.95
q_alpha = -1.0 + np.sqrt(3.85)


# ------------------------------------------------------------
# Funzioni del problema
# ------------------------------------------------------------

def pdf_L(x):
    """
    Densita' di L.
    """
    y = np.zeros_like(x, dtype=float)
    mask = (x >= 0.0) & (x <= 1.0)
    y[mask] = c * (1.0 + x[mask])
    return y


def cdf_L(x):
    """
    Funzione di distribuzione di L.
    """
    x = np.asarray(x, dtype=float)
    y = np.zeros_like(x, dtype=float)

    mask_left = x < 0.0
    mask_mid = (x >= 0.0) & (x <= 1.0)
    mask_right = x > 1.0

    y[mask_left] = 0.0
    y[mask_mid] = (2.0 * x[mask_mid] + x[mask_mid] ** 2) / 3.0
    y[mask_right] = 1.0

    return y


# ------------------------------------------------------------
# Valori numerici utili
# ------------------------------------------------------------

prob_tail = 1.0 - (2.0 * tail_threshold + tail_threshold ** 2) / 3.0
# dovrebbe essere 0.48

# Griglia per i grafici
x = np.linspace(-0.05, 1.05, 1200)
y_pdf = pdf_L(x)
y_cdf = cdf_L(x)


# ------------------------------------------------------------
# Parametri grafici
# ------------------------------------------------------------

figure_width = 12.5
figure_height = 5.4
png_dpi = 300

title_fontsize = 17
axis_label_fontsize = 16
tick_fontsize = 13
annotation_fontsize = 15


# ------------------------------------------------------------
# Creazione figura con due pannelli affiancati
# ------------------------------------------------------------

fig, (ax1, ax2) = plt.subplots(
    1, 2, figsize=(figure_width, figure_height)
)

# ============================================================
# Pannello sinistro: densita'
# ============================================================

ax1.plot(x, y_pdf, linewidth=2.4)

# Area di coda destra: L > 0.6
mask_tail = (x >= tail_threshold) & (x <= 1.0)
ax1.fill_between(x[mask_tail], y_pdf[mask_tail], alpha=0.35)

# Verticale in l = 0.6
ax1.axvline(tail_threshold, linestyle="--", linewidth=1.8)

# Etichette e annotazioni
ax1.text(
    0.50,
    0.93,
    r"$f_L(\ell)=\frac{2}{3}(1+\ell),\quad 0\leq \ell\leq 1$",
    transform=ax1.transAxes,
    fontsize=annotation_fontsize,
    ha="center",
    va="center",
)

ax1.text(
    0.67,
    0.72,
    r"$\mathrm{P}(L>0.6)=0.48$",
    transform=ax1.transAxes,
    fontsize=annotation_fontsize,
    ha="center",
    va="center",
)

ax1.set_title("Densità della perdita", fontsize=title_fontsize)

ax1.set_xlim(-0.05, 1.05)
ax1.set_ylim(0, max(y_pdf) * 1.18)

ax1.set_xlabel(r"$\ell$", fontsize=axis_label_fontsize)
ax1.set_ylabel(r"$f_L(\ell)$", fontsize=axis_label_fontsize)

ax1.set_xticks([0.0, 0.6, 1.0])
ax1.set_xticklabels([r"$0$", r"$0.6$", r"$1$"], fontsize=tick_fontsize)
ax1.tick_params(axis="y", labelsize=tick_fontsize)

ax1.grid(True, linewidth=0.5, alpha=0.4)
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)


# ============================================================
# Pannello destro: funzione di distribuzione
# ============================================================

ax2.plot(x, y_cdf, linewidth=2.4)

# Retta orizzontale a livello alpha
ax2.axhline(alpha, linestyle="--", linewidth=1.6)

# Retta verticale nel quantile
ax2.axvline(q_alpha, linestyle="--", linewidth=1.8)

# Punto di intersezione
ax2.plot([q_alpha], [alpha], marker="o", markersize=6)

# Etichette e annotazioni
ax2.text(
    0.50,
    0.93,
    r"$F_L(\ell)=\frac{2\ell+\ell^2}{3},\quad 0\leq \ell\leq 1$",
    transform=ax2.transAxes,
    fontsize=annotation_fontsize,
    ha="center",
    va="center",
)

ax2.text(
    0.63,
    0.72,
    rf"$q_{{0.95}}(L)\simeq {q_alpha:.4f}$",
    transform=ax2.transAxes,
    fontsize=annotation_fontsize,
    ha="center",
    va="center",
)

ax2.text(
    0.25,
    0.55,
    r"$F_L(q_{0.95}(L))=0.95$",
    transform=ax2.transAxes,
    fontsize=annotation_fontsize,
    ha="center",
    va="center",
)

ax2.set_title("Funzione di distribuzione", fontsize=title_fontsize)

ax2.set_xlim(-0.05, 1.05)
ax2.set_ylim(-0.02, 1.02)

ax2.set_xlabel(r"$\ell$", fontsize=axis_label_fontsize)
ax2.set_ylabel(r"$F_L(\ell)$", fontsize=axis_label_fontsize)

ax2.set_xticks([0.0, q_alpha, 1.0])
ax2.set_xticklabels(
    [r"$0$", r"$q_{0.95}(L)$", r"$1$"],
    fontsize=tick_fontsize,
)

ax2.set_yticks([0.0, alpha, 1.0])
ax2.set_yticklabels(
    [r"$0$", r"$0.95$", r"$1$"],
    fontsize=tick_fontsize,
)

ax2.grid(True, linewidth=0.5, alpha=0.4)
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)


# ------------------------------------------------------------
# Layout e salvataggio
# ------------------------------------------------------------

fig.tight_layout()

png_path = output_dir / f"{output_name}.png"
svg_path = output_dir / f"{output_name}.svg"

fig.savefig(png_path, dpi=png_dpi, bbox_inches="tight")
fig.savefig(svg_path, bbox_inches="tight")

plt.close(fig)

print(f"Creato file PNG: {png_path}")
print(f"Creato file SVG: {svg_path}")
print(f"P(L > 0.6) = {prob_tail:.4f}")
print(f"q_0.95(L) = {q_alpha:.6f}")
