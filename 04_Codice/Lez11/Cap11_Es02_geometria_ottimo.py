from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# ============================================================
# Cartella temporanea di controllo
# ============================================================

out_dir = Path(r"E:\Didattica\MQF\graphics")
out_dir.mkdir(parents=True, exist_ok=True)

png_path = out_dir / "Cap11_Es02_geometria_ottimo.png"
svg_path = out_dir / "Cap11_Es02_geometria_ottimo.svg"

# ============================================================
# TIPOGRAFIA: tutti i controlli sono raccolti qui
# ============================================================

# Cambia il carattere di tutto il grafico.
FONT_FAMILY = "DejaVu Sans"

# Moltiplicatori globali: 1.10 aumenta tutto del 10%; 0.90 riduce del 10%.
FONT_SCALE = 1.00
LINE_SPACING_SCALE = 1.00

# Dimensioni per categoria.
FONT_SIZES: dict[str, float] = {
    "title": 19.0,
    "axis_label": 15.0,
    "tick_label": 12.0,
    "vertex_label": 12.0,
    "optimum_label": 12.0,
    "direction_label": 12.0,
    "legend": 12.0,
}

# Interlinea per categoria.
LINE_SPACINGS: dict[str, float] = {
    "title": 1.00,
    "axis_label": 1.00,
    "tick_label": 1.00,
    "vertex_label": 1.00,
    "optimum_label": 1.00,
    "direction_label": 1.00,
    "legend": 1.00,
}

plt.rcParams["font.family"] = FONT_FAMILY


def font_size(category: str) -> float:
    return FONT_SIZES[category] * FONT_SCALE


def line_spacing(category: str) -> float:
    return LINE_SPACINGS[category] * LINE_SPACING_SCALE


# ============================================================
# Geometria della regione ammissibile
# ============================================================

A = (3, 0)
B = (10, 0)
C = (6, 4)
D = (3, 4)

vertices = np.array([A, B, C, D])

fig, ax = plt.subplots(figsize=(9.2, 6.8))

x = np.linspace(0, 11.5, 400)

# Vincoli
ax.plot(x, 10 - x, linewidth=1.8, label=r"$x_1+x_2=10$")
ax.axvline(3, linewidth=1.8, label=r"$x_1=3$")
ax.axhline(4, linewidth=1.8, label=r"$x_2=4$")

# Regione ammissibile
poly = Polygon(vertices, closed=True, alpha=0.18, label="Regione ammissibile")
ax.add_patch(poly)

# Vertici
for (xp, yp), name, dx, dy in [
    (A, "A=(3,0)", 0.10, 0.18),
    (B, "B=(10,0)", -0.90, 0.18),
    (C, "C=(6,4)", 0.12, 0.15),
    (D, "D=(3,4)", 0.10, 0.15),
]:
    ax.plot(xp, yp, marker="o")
    ax.text(
        xp + dx,
        yp + dy,
        name,
        fontsize=font_size("vertex_label"),
        linespacing=line_spacing("vertex_label")
    )

# Rette di livello rappresentative
y1 = (24 - 2 * x) / 3
mask1 = (y1 >= -0.5) & (y1 <= 6.2)
ax.plot(x[mask1], y1[mask1], linestyle="--", linewidth=1.8,
        label=r"$2x_1+3x_2=24$")

y2 = (30 - 3 * x) / 2
mask2 = (y2 >= -0.5) & (y2 <= 6.2)
ax.plot(x[mask2], y2[mask2], linestyle=":", linewidth=2.2,
        label=r"$3x_1+2x_2=30$")

# Evidenza dei due ottimi
ax.annotate(r"Ottimo per $z=2x_1+3x_2$",
            xy=C, xytext=(7.1, 4.9),
            arrowprops=dict(arrowstyle="->", linewidth=1.4),
            fontsize=font_size("optimum_label"),
            linespacing=line_spacing("optimum_label"))

ax.annotate(r"Ottimo per $\widetilde z=3x_1+2x_2$",
            xy=B, xytext=(7.0, 1.1),
            arrowprops=dict(arrowstyle="->", linewidth=1.4),
            fontsize=font_size("optimum_label"),
            linespacing=line_spacing("optimum_label"))

# Direzione di crescita delle funzioni obiettivo
ax.annotate("", xy=(8.6, 3.4), xytext=(7.7, 2.8),
            arrowprops=dict(arrowstyle="->", linewidth=1.2))
ax.text(
    8.65,
    3.45,
    r"$z \uparrow$",
    fontsize=font_size("direction_label"),
    linespacing=line_spacing("direction_label")
)

ax.annotate("", xy=(9.7, 2.0), xytext=(8.8, 1.4),
            arrowprops=dict(arrowstyle="->", linewidth=1.2))
ax.text(
    9.75,
    2.05,
    r"$\widetilde z \uparrow$",
    fontsize=font_size("direction_label"),
    linespacing=line_spacing("direction_label")
)

# Assi e rifiniture
ax.set_xlim(0, 11.5)
ax.set_ylim(0, 6.2)
ax.set_xlabel(
    r"$x_1$",
    fontsize=font_size("axis_label"),
    linespacing=line_spacing("axis_label")
)
ax.set_ylabel(
    r"$x_2$",
    fontsize=font_size("axis_label"),
    linespacing=line_spacing("axis_label")
)
ax.set_title(
    "Geometria del problema e cambiamento della soluzione ottima",
    fontsize=font_size("title"),
    linespacing=line_spacing("title")
)
ax.tick_params(axis="both", labelsize=font_size("tick_label"))
ax.grid(True, alpha=0.3)
legend = ax.legend(
    loc="upper right",
    frameon=True,
    fontsize=font_size("legend")
)
for legend_text in legend.get_texts():
    legend_text.set_linespacing(line_spacing("legend"))

fig.tight_layout()
fig.savefig(png_path, dpi=300, bbox_inches="tight")
fig.savefig(svg_path, bbox_inches="tight")
plt.close(fig)

print("Figura salvata in:")
print(png_path)
print(svg_path)
