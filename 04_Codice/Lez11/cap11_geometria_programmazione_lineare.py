from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

# Lo script si trova in <radice progetto>/04_Codice/Lez11.
# Costruire il percorso a partire da __file__ evita dipendenze dal PC in uso.
project_dir = Path(__file__).resolve().parents[2]
out_dir = Path(r"E:\Didattica\MQF\graphics")
out_dir.mkdir(parents=True, exist_ok=True)

png_path = out_dir / "cap11_geometria_programmazione_lineare.png"
svg_path = out_dir / "cap11_geometria_programmazione_lineare.svg"

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
    "axis_label": 16.0,
    "tick_label": 16.0,
    "vertex_label": 16.0,
    "region_label": 14.0,
    "legend": 16,
}

# Interlinea per categoria.
LINE_SPACINGS: dict[str, float] = {
    "axis_label": 1.00,
    "tick_label": 1.00,
    "vertex_label": 1.00,
    "region_label": 1.05,
    "legend": 1.00,
}

plt.rcParams["font.family"] = FONT_FAMILY


def font_size(category: str) -> float:
    return FONT_SIZES[category] * FONT_SCALE


def line_spacing(category: str) -> float:
    return LINE_SPACINGS[category] * LINE_SPACING_SCALE


# ============================================================
# Parametri e geometria
# ============================================================

A0 = 10.0
Q_min = 3.0
B_max = 4.0

x1 = np.linspace(0, 11, 400)
x2_budget = A0 - x1

vertices = np.array([
    [Q_min, 0.0],
    [A0, 0.0],
    [A0 - B_max, B_max],
    [Q_min, B_max],
])

fig, ax = plt.subplots(figsize=(8.6, 5.8))
ax.plot(x1, x2_budget, linewidth=2, label=r"$x_1+x_2\leq 10$")
ax.axvline(Q_min, linewidth=2, linestyle="--", label=r"$x_1 \geq 3$")
ax.axhline(B_max, linewidth=2, linestyle="-.", label=r"$x_2 \leq 4$")

ax.fill(vertices[:, 0], vertices[:, 1], alpha=0.2, label="Regione ammissibile")
closed = np.vstack([vertices, vertices[0]])
ax.plot(closed[:, 0], closed[:, 1], linewidth=1.5)

for (xv, yv), label in zip(vertices, ["A", "B", "C", "D"]):
    ax.scatter([xv], [yv], s=35)
    ax.annotate(
        label,
        (xv, yv),
        xytext=(6, 6),
        textcoords="offset points",
        fontsize=font_size("vertex_label"),
        linespacing=line_spacing("vertex_label")
    )

ax.text(
    5.0,
    2.0,
    "Regione\nammissibile",
    ha="center",
    va="center",
    fontsize=font_size("region_label"),
    linespacing=line_spacing("region_label")
)
ax.set_xlim(0, 11)
ax.set_ylim(0, 7)
ax.set_xlabel(
    r"$x_1$: attività liquide",
    fontsize=font_size("axis_label"),
    linespacing=line_spacing("axis_label")
)
ax.set_ylabel(
    r"$x_2$: titoli a lunga scadenza",
    fontsize=font_size("axis_label"),
    linespacing=line_spacing("axis_label")
)
ax.tick_params(axis="both", labelsize=font_size("tick_label"))
ax.grid(True, alpha=0.25)
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
# plt.show()
plt.close(fig)

print("File salvati:")
print(png_path)
print(svg_path)
