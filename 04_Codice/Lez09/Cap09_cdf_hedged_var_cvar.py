from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

# Per mantenere il testo come testo nel file SVG,
# anziché convertirlo in curve vettoriali, decommentare
# la riga seguente.
# plt.rcParams["svg.fonttype"] = "none"


# ============================================================
# DATI DEL PROBLEMA
# ============================================================

losses = np.array([-1.0, 2.0, 10.0])
probabilities = np.array([0.08, 0.78, 0.14])
cdf_values = np.cumsum(probabilities)

alpha = 0.95
var_95 = 10.0
cvar_95 = 10.0


# ============================================================
# PERCORSO DI SALVATAGGIO
# ============================================================

output_dir = Path(
    r"E:\Didattica\MQF\graphics"
)
output_dir.mkdir(parents=True, exist_ok=True)

file_stem = "Cap09_cdf_hedged_var_cvar"

png_path = output_dir / f"{file_stem}.png"
svg_path = output_dir / f"{file_stem}.svg"


# ============================================================
# COSTRUZIONE DEL GRAFICO
# ============================================================

fig, ax = plt.subplots(figsize=(9.2, 5.8))

x_left = -3.0
x_right = 12.0

# Tutti i tratti della CDF utilizzano il primo colore
# del ciclo standard di Matplotlib.
cdf_color = plt.rcParams["axes.prop_cycle"].by_key()["color"][0]

horizontal_segments = [
    (x_left, losses[0], 0.00),
    (losses[0], losses[1], 0.08),
    (losses[1], losses[2], 0.86),
    (losses[2], x_right, 1.00),
]

for x_start, x_end, y_value in horizontal_segments:
    ax.plot(
        [x_start, x_end],
        [y_value, y_value],
        color=cdf_color,
        linewidth=2.2,
    )

# Le discontinuità sono indicate da segmenti verticali
# tratteggiati, che non fanno parte del grafico della CDF.
vertical_guides = [
    (losses[0], 0.00, 0.08),
    (losses[1], 0.08, 0.86),
    (losses[2], 0.86, 1.00),
]

for x_value, y_lower, y_upper in vertical_guides:
    ax.plot(
        [x_value, x_value],
        [y_lower, y_upper],
        color=cdf_color,
        linestyle="--",
        linewidth=1.2,
        alpha=0.75,
    )

ax.scatter(
    losses,
    cdf_values,
    color=cdf_color,
    zorder=4,
)

ax.axhline(
    alpha,
    color="0.35",
    linestyle="--",
    linewidth=1.2,
)

ax.plot(
    [var_95, var_95],
    [0.00, alpha],
    color="0.35",
    linestyle="--",
    linewidth=1.2,
)

ax.annotate(
    "",
    xy=(10.25, 1.00),
    xytext=(10.25, 0.95),
    arrowprops={
        "arrowstyle": "<->",
        "color": "0.25",
        "linewidth": 1.2,
    },
)

ax.text(
    10.38,
    0.975,
    "coda del 5%\ninteramente associata\na $L^{\\mathrm{hedged}}=10$",
    fontsize=10,
    va="center",
)

ax.text(
    -2.6,
    0.91,
    r"$\alpha=0.95$",
    fontsize=11,
)

# VaR e CVaR sono valori sull'asse delle perdite.
ax.annotate(
    r"$\operatorname{VaR}^{\mathbb{P}}_{0.95}"
    r"(L^{\mathrm{hedged}})=10$",
    xy=(10.0, 0.0),
    xytext=(3.1, 0.57),
    arrowprops={
        "arrowstyle": "->",
        "color": "0.15",
        "linewidth": 1.2,
        "connectionstyle": "arc3,rad=-0.10",
    },
    fontsize=11,
)

ax.annotate(
    r"$\operatorname{CVaR}^{\mathbb{P}}_{0.95}"
    r"(L^{\mathrm{hedged}})=10$",
    xy=(10.0, 0.0),
    xytext=(3.1, 0.31),
    arrowprops={
        "arrowstyle": "->",
        "color": "0.15",
        "linewidth": 1.2,
        "connectionstyle": "arc3,rad=0.10",
    },
    fontsize=11,
)

ax.set_xlabel(r"Perdita $L^{\mathrm{hedged}}$")
ax.set_ylabel(
    r"$F_{L^{\mathrm{hedged}}\mid 2}(\ell)$"
)
ax.set_title(
    "Posizione coperta: funzione di ripartizione, VaR e CVaR"
)

ax.set_xlim(x_left, x_right)
ax.set_ylim(-0.02, 1.05)
ax.set_xticks([-1, 2, 10])
ax.set_yticks([0.00, 0.08, 0.50, 0.86, 0.95, 1.00])
ax.grid(True, alpha=0.3)

fig.tight_layout()

fig.savefig(
    png_path,
    dpi=220,
    bbox_inches="tight",
)

fig.savefig(
    svg_path,
    bbox_inches="tight",
)

plt.close(fig)

print("File salvati:")
print(png_path)
print(svg_path)
