from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# Capitolo 2 - Densita' uniforme dell'esempio sul rendimento
# ============================================================
#
# Questo script genera il grafico della densita' uniforme
# dell'esempio:
#
#   f_R(r) = 10    per -0.04 <= r <= 0.06
#            0     altrove
#
# e mette in evidenza l'area corrispondente a
#
#   P(a <= R <= b)
#
# ------------------------------------------------------------
# CORREZIONI RISPETTO ALLA VERSIONE PRECEDENTE
# ------------------------------------------------------------
#
# 1. Rimossa la duplicazione delle etichette sull'asse orizzontale:
#    - non si usano piu' sia ax.text(...) sia xticklabels
#      per gli stessi punti;
#    - le etichette compaiono solo una volta, come tick labels.
#
# 2. Font aumentati:
#    - titolo assente, ma etichette e annotazioni principali
#      sono aumentate circa del 160%.
#
# 3. Area evidenziata:
#    - ora l'area e' quella compresa tra
#         a = 0.01  e  b = 0.05
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
# 3. Estremi del supporto della uniforme:
#       modificare alpha e beta
#
# 4. Intervallo evidenziato:
#       modificare a e b
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

output_name = "cap2_densita_uniforme_rendimento_area_01_05"


# ------------------------------------------------------------
# Parametri della distribuzione uniforme
# ------------------------------------------------------------

alpha = -0.04
beta = 0.06

# Altezza della densita'
density_height = 1.0 / (beta - alpha)   # = 10


# ------------------------------------------------------------
# Intervallo [a,b] da evidenziare
# ------------------------------------------------------------
#
# In questa versione:
#   a = 1%
#   b = 5%

a = 0.01
b = 0.05


# ------------------------------------------------------------
# Parametri grafici
# ------------------------------------------------------------

figure_width = 9.0
figure_height = 5.4
png_dpi = 300

# Font ingranditi
axis_label_fontsize = 18
tick_fontsize = 16
annotation_fontsize = 20   # circa 160% rispetto a un 12-13 standard

xlabel = r"$r$"
ylabel = r"$f_R(r)$"


# ------------------------------------------------------------
# Dominio del grafico
# ------------------------------------------------------------

x_min = -0.07
x_max = 0.09
num_points = 1200


# ------------------------------------------------------------
# Definizione della densita'
# ------------------------------------------------------------

def pdf(x):
    """
    Densita' uniforme su [alpha, beta].
    """
    y = np.zeros_like(x, dtype=float)
    y[(x >= alpha) & (x <= beta)] = density_height
    return y


# ------------------------------------------------------------
# Calcolo della probabilita' evidenziata
# ------------------------------------------------------------

def probability_on_interval(a, b, alpha, beta):
    """
    Calcola la probabilita' P(a <= R <= b)
    nel caso uniforme su [alpha, beta].
    """
    left = max(a, alpha)
    right = min(b, beta)

    if right <= left:
        return 0.0

    return (right - left) * density_height


# ------------------------------------------------------------
# Costruzione dei dati
# ------------------------------------------------------------

x = np.linspace(x_min, x_max, num_points)
y = pdf(x)

fill_left = max(a, alpha)
fill_right = min(b, beta)

mask = (x >= fill_left) & (x <= fill_right)
x_fill = x[mask]
y_fill = y[mask]

prob_value = probability_on_interval(a, b, alpha, beta)


# ------------------------------------------------------------
# Creazione del grafico
# ------------------------------------------------------------

fig, ax = plt.subplots(figsize=(figure_width, figure_height))

# Densita'
ax.plot(x, y, linewidth=2.6)

# Area evidenziata
if fill_right > fill_left:
    ax.fill_between(x_fill, y_fill, alpha=0.35)

# Verticali del supporto della densita'
ax.axvline(alpha, linestyle="--", linewidth=1.6)
ax.axvline(beta, linestyle="--", linewidth=1.6)

# Verticali dell'intervallo [a,b]
ax.axvline(a, linestyle=":", linewidth=2.0)
ax.axvline(b, linestyle=":", linewidth=2.0)

# Etichetta della densita'
# Posizionata in alto a destra, piu' distante dal testo dell'area
ax.text(
    0.82,
    0.86,
    r"$f_R(r)=10$",
    transform=ax.transAxes,
    fontsize=annotation_fontsize,
    ha="center",
    va="center",
)

# Formula dell'area
ax.text(
    0.52,
    0.92,
    r"$\mathrm{P}(0.01\leq R\leq 0.05)=\int_{0.01}^{0.05} f_R(r)\,dr$",
    transform=ax.transAxes,
    fontsize=annotation_fontsize,
    ha="center",
    va="center",
)

# Valore numerico dell'area
ax.text(
    0.52,
    0.84,
    r"$\mathrm{P}(0.01\leq R\leq 0.05)=0.40$",
    transform=ax.transAxes,
    fontsize=annotation_fontsize,
    ha="center",
    va="center",
)

# Assi
ax.set_xlim(x_min, x_max)
ax.set_ylim(0, density_height * 1.20)

ax.set_xlabel(xlabel, fontsize=axis_label_fontsize)
ax.set_ylabel(ylabel, fontsize=axis_label_fontsize)

# Tick dell'asse x:
# niente annotazioni duplicate, una sola etichetta per punto
x_ticks = [alpha, a, b, beta]
x_labels = [r"$-0.04$", r"$a=0.01$", r"$b=0.05$", r"$0.06$"]
ax.set_xticks(x_ticks)
ax.set_xticklabels(x_labels, fontsize=tick_fontsize)

# Tick dell'asse y
ax.set_yticks([0, density_height])
ax.set_yticklabels([r"$0$", r"$10$"], fontsize=tick_fontsize)

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
print(f"Probabilita' evidenziata: {prob_value:.4f}")