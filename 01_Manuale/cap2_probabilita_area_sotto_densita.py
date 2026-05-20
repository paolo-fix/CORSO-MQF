from pathlib import Path
import math

import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# Capitolo 2 - Probabilita' come area sotto una densita'
# ============================================================
#
# Questo script genera un grafico illustrativo del fatto che
#
#   P(a < X <= b) = \int_a^b f_X(x) dx
#
# Il grafico mostra:
#   - la curva della densita' f_X(x),
#   - le rette verticali x = a e x = b,
#   - l'area sottesa alla densita' nell'intervallo [a,b].
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
#    modificare output_dir.
#
# 2. Nome dei file:
#    modificare output_name.
#
# 3. Intervallo di probabilita':
#    modificare i valori di a e b.
#
# 4. Densita':
#    modificare la funzione pdf(x).
#    In questo esempio viene usata una densita' normale.
#
# 5. Dominio del grafico:
#    modificare x_min, x_max e num_points.
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
# Nome dei file di output
# ------------------------------------------------------------

output_name = "cap2_probabilita_area_sotto_densita"


# ------------------------------------------------------------
# Parametri della densita' normale di esempio
# ------------------------------------------------------------
#
# Questa parte puo' essere modificata se si vuole usare
# una distribuzione normale con media e deviazione standard
# diverse.
#
# Se in futuro si vuole usare un'altra densita', e' sufficiente
# sostituire la funzione pdf(x) definita piu' sotto.

mu = 0.0
sigma = 1.0


# ------------------------------------------------------------
# Intervallo [a,b] di cui si vuole rappresentare la probabilita'
# ------------------------------------------------------------

a = -0.8
b = 1.2


# ------------------------------------------------------------
# Dominio del grafico
# ------------------------------------------------------------

x_min = -3.5
x_max = 3.5
num_points = 1000


# ------------------------------------------------------------
# Parametri grafici
# ------------------------------------------------------------

figure_width = 8.0
figure_height = 4.8
png_dpi = 300

xlabel = r"$x$"
ylabel = r"$f_X(x)$"


# ------------------------------------------------------------
# Definizione della densita'
# ------------------------------------------------------------
#
# Funzione di densita' normale:
#
#   f_X(x) = 1 / (sigma * sqrt(2*pi)) * exp(-(x-mu)^2 / (2*sigma^2))
#
# Per rappresentare una densita' diversa, sostituire questa
# funzione con la densita' desiderata.

def pdf(x):
    return (
        1.0 / (sigma * math.sqrt(2.0 * math.pi))
        * np.exp(-((x - mu) ** 2) / (2.0 * sigma ** 2))
    )


# ------------------------------------------------------------
# Calcolo dei punti del grafico
# ------------------------------------------------------------

x = np.linspace(x_min, x_max, num_points)
y = pdf(x)

# Selezione dei punti compresi tra a e b
mask = (x >= a) & (x <= b)
x_fill = x[mask]
y_fill = y[mask]


# ------------------------------------------------------------
# Creazione del grafico
# ------------------------------------------------------------

fig, ax = plt.subplots(figsize=(figure_width, figure_height))

# Curva della densita'
ax.plot(x, y, linewidth=2.0, label=r"$f_X(x)$")

# Area sotto la densita' tra a e b
ax.fill_between(x_fill, y_fill, alpha=0.35)

# Rette verticali nei punti a e b
ax.axvline(a, linestyle="--", linewidth=1.2)
ax.axvline(b, linestyle="--", linewidth=1.2)

# Etichette sull'asse x
ax.text(a, -0.015, r"$a$", ha="center", va="top")
ax.text(b, -0.015, r"$b$", ha="center", va="top")

# Etichetta della formula all'interno del grafico
formula_text = r"$\mathrm{P}(a<X\leq b)=\int_a^b f_X(x)\,dx$"
ax.text(
    0.50,
    0.88,
    formula_text,
    transform=ax.transAxes,
    ha="center",
    va="center",
)

# Etichetta della densita' in prossimita' del picco
peak_y = pdf(mu)
ax.text(mu + 0.15, peak_y + 0.02, r"$f_X(x)$")

# Impostazioni degli assi
ax.set_xlim(x_min, x_max)
ax.set_ylim(0, max(y) * 1.15)

ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)

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