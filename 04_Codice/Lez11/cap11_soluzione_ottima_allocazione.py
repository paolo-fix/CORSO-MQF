from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib import colormaps

# ============================================================
# Percorso di output
# ============================================================

out_dir = Path(r"E:\Didattica\MQF\graphics")
out_dir.mkdir(parents=True, exist_ok=True)

png_path = out_dir / "Cap11_soluzione_ottima_allocazione.png"
svg_path = out_dir / "Cap11_soluzione_ottima_allocazione.svg"

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
    "summary": 14.0,
    "axis_label": 16.0,
    "category_label": 14,
    "scale_tick": 14,
    "value_label": 14,
}

# Interlinea per categoria.
LINE_SPACINGS: dict[str, float] = {
    "title": 1.00,
    "summary": 1.25,
    "axis_label": 1.00,
    "category_label": 1.00,
    "scale_tick": 1.00,
    "value_label": 1.05,
}

plt.rcParams["font.family"] = FONT_FAMILY


def font_size(category: str) -> float:
    return FONT_SIZES[category] * FONT_SCALE


def line_spacing(category: str) -> float:
    return LINE_SPACINGS[category] * LINE_SPACING_SCALE


# ============================================================
# Dati: soluzione ottima della Sezione 11.7
# ============================================================

labels = [
    "Cassa e riserve",
    "Titoli a breve scadenza",
    "Titoli a lunga scadenza",
    "Prestiti e impieghi meno liquidi",
]

values = [0.000, 41.045, 20.896, 38.060]

total = sum(values)
shares = [100 * v / total if total > 0 else 0 for v in values]

# ============================================================
# Figura
# ============================================================

fig, ax = plt.subplots(figsize=(11.8, 6.6))

short_labels = [
    "Cassa e\nriserve",
    "Titoli a breve\nscadenza",
    "Titoli a lunga\nscadenza",
    "Prestiti e impieghi\nmeno liquidi",
]

# Tonalità azzurre ordinate per valore: il maggiore è il più scuro.
blue_map = colormaps["Blues"]
shade_levels = [0.88, 0.72, 0.56, 0.40]
ranked_indices = sorted(range(len(values)), key=values.__getitem__, reverse=True)
rank_by_index = {index: rank for rank, index in enumerate(ranked_indices)}
colors = [
    blue_map(shade_levels[rank_by_index[index]])
    for index in range(len(values))
]
x_positions = range(len(values))

bars = ax.bar(
    x_positions,
    values,
    width=0.64,
    color=colors,
    edgecolor="white",
    linewidth=1.2,
    zorder=3
)

# Valore e quota sopra ogni barra. Per il valore nullo viene tracciato
# un breve segmento sulla linea dello zero, così la categoria resta visibile.
for x, bar, value, share, color in zip(
    x_positions, bars, values, shares, colors
):
    if value == 0:
        ax.plot(
            [x - 0.20, x + 0.20], [0.25, 0.25],
            color=color, linewidth=4, solid_capstyle="round", zorder=4
        )
        label_y = 1.15
    else:
        label_y = bar.get_height() + 1.15

    ax.text(
        x,
        label_y,
        f"{share:.1f}%",
        ha="center",
        va="bottom",
        fontsize=font_size("value_label"),
        fontweight="bold",
        linespacing=line_spacing("value_label"),
        color="#174a70"
    )

# ============================================================
# Assi e titolo
# ============================================================

ax.set_ylim(0, 50)
ax.set_ylabel(
    "Unità monetarie allocate",
    fontsize=font_size("axis_label"),
    linespacing=line_spacing("axis_label")
)
ax.set_xticks(
    list(x_positions),
    short_labels,
    fontsize=font_size("category_label"),
    linespacing=line_spacing("category_label")
)
ax.tick_params(axis="y", labelsize=font_size("scale_tick"))

ax.set_title(
    "Composizione dell'attivo nella soluzione ottima",
    fontsize=font_size("title"),
    fontweight="bold",
    linespacing=line_spacing("title"),
    pad=48
)

ax.set_axisbelow(True)
ax.yaxis.grid(True, color="#d9d9d9", linewidth=0.8)
ax.xaxis.grid(False)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("#777777")
ax.spines["bottom"].set_color("#777777")

# ============================================================
# Annotazioni sintetiche
# ============================================================

summary_text = (
    #"$x^*=(0,\\ 41.045,\\ 20.896,\\ 38.060)$"
    "$z^*\\approx 3.765$\n"
    "Vincoli attivi: bilancio, liquidità, perdita"
)

ax.text(
    0.5,
    1.015,
    summary_text,
    transform=ax.transAxes,
    ha="center",
    va="bottom",
    fontsize=font_size("summary"),
    linespacing=line_spacing("summary"),
    color="#444444"
)

# ============================================================
# Salvataggio
# ============================================================

fig.tight_layout(pad=1.4)
fig.savefig(png_path, dpi=220, bbox_inches="tight")
fig.savefig(svg_path, bbox_inches="tight")
plt.close(fig)

print("Figura salvata in:")
print(png_path)
print(svg_path)
