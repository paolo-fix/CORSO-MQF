"""Composizione della coda peggiore del 5% sul caso guida della Lezione 9.

Usata nelle slide della Lezione 9 (slide sul punto di VaR).

Caso guida: rating iniziale X_0 = 2, orizzonte h = 1.
Perdite L_1 = -3, 0, 8, 60 con probabilita' 0.08, 0.75, 0.14, 0.03.
VaR_{0.95} = 8: della probabilita' 0.14 nel punto di VaR, solo 0.02 entra nella coda.
"""

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


# ============================================================
# DATI DEL PROBLEMA
# ============================================================

losses = np.array([-3.0, 0.0, 8.0, 60.0])
probabilities = np.array([0.08, 0.75, 0.14, 0.03])

alpha = 0.95
var_95 = 8.0

cdf_values = np.cumsum(probabilities)
cdf_at_var = cdf_values[losses == var_95][0]          # 0.97
tail_at_var = cdf_at_var - alpha                       # 0.02

tail_mass = np.where(losses > var_95, probabilities, 0.0)
tail_mass[losses == var_95] = tail_at_var
body_mass = probabilities - tail_mass


# ============================================================
# PERCORSO DI SALVATAGGIO
# ============================================================

# Lo script risiede in 04_Codice/Lez09: la cartella delle figure
# del repository e' ../../graphics.
output_dir = Path(__file__).resolve().parents[2] / "graphics"
output_dir.mkdir(parents=True, exist_ok=True)

file_stem = "Cap09_CVaR_probabilita_quantile_caso_guida"
png_path = output_dir / f"{file_stem}.png"

# Altezza d'uso nella slide: il PNG dichiara una risoluzione tale che la
# sua dimensione fisica coincida con quella d'uso, cosi' Scientific
# WorkPlace 5.5 lo importa al 100% senza ricampionarlo (Guidelines, sez. 8).
TARGET_HEIGHT_CM = 3.9


# ============================================================
# COSTRUZIONE DEL GRAFICO
# ============================================================

colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
body_color, tail_color = colors[0], colors[1]

fig, ax = plt.subplots(figsize=(10.0, 6.4))

bar_width = 2.0

ax.bar(losses, body_mass, width=bar_width, color=body_color,
       label="Probabilit\u00e0 fuori dalla coda peggiore")
ax.bar(losses, tail_mass, width=bar_width, bottom=body_mass,
       color=tail_color, label="Probabilit\u00e0 nella coda peggiore del 5%")

for x_value, p_value in zip(losses, probabilities):
    # L'etichetta nel punto di VaR e' spostata a sinistra della linea.
    x_text = x_value - 1.6 if x_value == var_95 else x_value
    ax.text(x_text, p_value + 0.02, f"{p_value:.2f}",
            ha="center", va="bottom", fontsize=12)

ax.axvline(var_95, color=body_color, linestyle="--", linewidth=1.5,
           label=f"VaR al 95% = {var_95:g}")

ax.annotate(
    f"{tail_at_var:.2f} della probabilit\u00e0 in L = {var_95:g}\nentra nella coda",
    xy=(var_95 + 0.3, probabilities[2] - 0.01),
    xytext=(24.0, 0.33),
    ha="center",
    fontsize=12,
    arrowprops={"arrowstyle": "->", "color": "black", "linewidth": 1.3},
)

ax.set_xlabel("Perdita L", fontsize=12)
ax.set_ylabel("Probabilità", fontsize=12)
ax.set_xticks(losses)
ax.set_xticklabels([f"{x:g}".replace("-", "\u2212") for x in losses])
ax.tick_params(labelsize=12)
ax.set_xlim(-8.0, 65.0)
ax.set_ylim(0.0, 0.86)
ax.grid(True, axis="y", alpha=0.3)

handles, labels = ax.get_legend_handles_labels()
wanted = [f"VaR al 95% = {var_95:g}", "Probabilit\u00e0 fuori dalla coda peggiore",
          "Probabilit\u00e0 nella coda peggiore del 5%"]
order = [labels.index(w) for w in wanted]
ax.legend([handles[i] for i in order], [labels[i] for i in order],
          loc="upper right", fontsize=12)

fig.tight_layout()
fig.savefig(png_path, dpi=250, bbox_inches="tight")
plt.close(fig)

# Risoluzione dichiarata = pixel / pollici d'uso (i pixel restano invariati).
with Image.open(png_path) as img:
    img.load()
    declared_dpi = img.height / (TARGET_HEIGHT_CM / 2.54)
    img.save(png_path, dpi=(declared_dpi, declared_dpi))

print("File salvato:", png_path)
