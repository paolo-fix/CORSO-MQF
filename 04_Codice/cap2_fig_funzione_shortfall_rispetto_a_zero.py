from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# Capitolo 2 - Funzione di perdita positiva g(r)=(-r)^+
# ============================================================
#
# Questo script rappresenta la funzione
#
#   g(r) = (-r)^+
#
# cioe'
#
#   g(r) = -r   se r < 0
#   g(r) =  0   se r >= 0
#
# Interpretazione:
#   se r e' un rendimento, g(r) misura la perdita positiva
#   associata ai soli rendimenti negativi.
#
# Output:
#   - PNG per inclusione nel manuale
#   - SVG come formato vettoriale/editabile
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
# Nome base dei file prodotti
# ------------------------------------------------------------

output_name = "Cap02_funzione_shortfall_zero"


# ------------------------------------------------------------
# Dominio del grafico
# ------------------------------------------------------------
#
# L'intervallo e' scelto in coerenza con l'esempio del rendimento
# uniforme su [-0.04,0.06], ma con un piccolo margine grafico.

r_min = -0.06
r_max = 0.08
num_points = 1000


# ------------------------------------------------------------
# Definizione della funzione g(r)=(-r)^+
# ------------------------------------------------------------

def g_positive_loss(r):
    """
    Calcola g(r)=(-r)^+.

    Per r < 0 restituisce -r.
    Per r >= 0 restituisce 0.
    """
    return np.maximum(-r, 0.0)


# ------------------------------------------------------------
# Parametri grafici
# ------------------------------------------------------------

figure_width = 8.5
figure_height = 5.2
png_dpi = 300

axis_label_fontsize = 18
tick_fontsize = 15
annotation_fontsize = 18


# ------------------------------------------------------------
# Costruzione dei dati
# ------------------------------------------------------------

r = np.linspace(r_min, r_max, num_points)
g = g_positive_loss(r)


# ------------------------------------------------------------
# Creazione del grafico
# ------------------------------------------------------------

fig, ax = plt.subplots(figsize=(figure_width, figure_height))

# Funzione g(r)
ax.plot(r, g, linewidth=2.6)

# Linea verticale in r=0, punto di cambio di regime
ax.axvline(0.0, linestyle="--", linewidth=1.4)

# Asse orizzontale
ax.axhline(0.0, linewidth=1.0)


# Annotazioni
ax.text(
    -0.038,
    0.045,
    r"$g(r)=-r$",
    fontsize=annotation_fontsize,
    ha="center",
)

ax.text(
    0.043,
    0.007,
    r"$g(r)=0$",
    fontsize=annotation_fontsize,
    ha="center",
)

ax.text(
    -0.032,
    0.012,
    r"$r<0$",
    fontsize=annotation_fontsize,
    ha="center",
)

ax.text(
    0.038,
    0.012,
    r"$r\geq 0$",
    fontsize=annotation_fontsize,
    ha="center",
)

# Etichetta della funzione
ax.text(
    0.50,
    0.92,
    r"$g(r)=(-r)^+$",
    transform=ax.transAxes,
    fontsize=annotation_fontsize + 2,
    ha="center",
    va="center",
)

# Assi
ax.set_xlim(r_min, r_max)
ax.set_ylim(-0.003, max(g) * 1.18)

ax.set_xlabel(r"$r$", fontsize=axis_label_fontsize)
ax.set_ylabel(r"$g(r)$", fontsize=axis_label_fontsize)

# Tick principali
ax.set_xticks([-0.04, 0.0, 0.06])
ax.set_xticklabels([r"$-0.04$", r"$0$", r"$0.06$"], fontsize=tick_fontsize)

ax.set_yticks([0.0, 0.04, 0.06])
ax.set_yticklabels([r"$0$", r"$0.04$", r"$0.06$"], fontsize=tick_fontsize)

# Griglia leggera
ax.grid(True, linewidth=0.5, alpha=0.4)

# Rimozione cornici superiore e destra
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
