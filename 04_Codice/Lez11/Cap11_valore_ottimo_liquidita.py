from pathlib import Path
import matplotlib.pyplot as plt

# ============================================================
# Cartella temporanea di controllo
# ============================================================

out_dir = Path(r"E:\Didattica\MQF\graphics")
out_dir.mkdir(parents=True, exist_ok=True)

png_path = out_dir / "Cap11_valore_ottimo_liquidita.png"
svg_path = out_dir / "Cap11_valore_ottimo_liquidita.svg"

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
    "axis_label": 16.0,
    "tick_label": 16.0,
    "point_label": 14,
    "slope_label": 14.0,
}

# Interlinea per categoria.
LINE_SPACINGS: dict[str, float] = {
    "title": 1.00,
    "axis_label": 1.00,
    "tick_label": 1.00,
    "point_label": 1.00,
    "slope_label": 1.10,
}

plt.rcParams["font.family"] = FONT_FAMILY


def font_size(category: str) -> float:
    return FONT_SIZES[category] * FONT_SCALE


def line_spacing(category: str) -> float:
    return LINE_SPACINGS[category] * LINE_SPACING_SCALE


# ============================================================
# Dati della Sezione 11.8
# ============================================================

Q = [55, 60, 65, 70, 75, 80, 90]
z = [3.7649, 3.5896, 3.4142, 3.2357, 3.0571, 2.8750, 2.5000]

# ============================================================
# Figura
# ============================================================

fig, ax = plt.subplots(figsize=(9.4, 5.6))

ax.plot(Q, z, marker="o", linewidth=2)

ax.set_title(
    "Valore ottimo e requisito minimo di liquidità",
    fontsize=font_size("title"),
    linespacing=line_spacing("title")
)
ax.set_xlabel(
    "Requisito minimo di liquidità $Q$",
    fontsize=font_size("axis_label"),
    linespacing=line_spacing("axis_label")
)
ax.set_ylabel(
    "Valore ottimo $z^*(Q)$",
    fontsize=font_size("axis_label"),
    linespacing=line_spacing("axis_label")
)
ax.tick_params(axis="both", labelsize=font_size("tick_label"))

# Griglia leggera
ax.grid(True, alpha=0.4)

# Etichette solo su alcuni punti chiave
selected_points = [0, 2, 4, 6]
for i in selected_points:
    ax.annotate(
        f"({Q[i]}, {z[i]:.4f})",
        (Q[i], z[i]),
        textcoords="offset points",
        xytext=(0, 8),
        ha="center",
        fontsize=font_size("point_label"),
        linespacing=line_spacing("point_label")
    )

# Evidenziazione del tratto iniziale
ax.plot(Q[:2], z[:2], linewidth=3)

# Costo marginale iniziale tra 55 e 60
slope_55_60 = (z[1] - z[0]) / (Q[1] - Q[0])

mid_q = (Q[0] + Q[1]) / 2
mid_z = (z[0] + z[1]) / 2

annotation_text = (
    "Costo marginale locale della liquidità\n"
    f"pendenza ≈ {slope_55_60:.4f}"
)

ax.annotate(
    annotation_text,
    xy=(mid_q, mid_z),
    xycoords="data",
    xytext=(0.97, 0.94),
    textcoords="axes fraction",
    ha="right",
    va="top",
    fontsize=font_size("slope_label"),
    linespacing=line_spacing("slope_label"),
    bbox=dict(
        boxstyle="round,pad=0.30",
        facecolor="white",
        edgecolor="#777777"
    ),
    arrowprops=dict(
        arrowstyle="->",
        color="#555555",
        linewidth=1.0
    )
)

# Margini del grafico
ax.set_xlim(54, 91)
ax.set_ylim(2.45, 3.82)

fig.tight_layout()
fig.savefig(png_path, dpi=220, bbox_inches="tight")
fig.savefig(svg_path, bbox_inches="tight")
plt.close(fig)

print("Figura salvata in:")
print(png_path)
print(svg_path)
