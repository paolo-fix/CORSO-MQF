from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# ============================================================
# PERCORSI DI OUTPUT — VERSIONE B COMPATTA
# ============================================================

OUTPUT_DIR = Path(r"E:\Didattica\MQF\graphics")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

png_path = OUTPUT_DIR / "Cap12_cashflow_attivi_fabbisogni_b.png"
svg_path = OUTPUT_DIR / "Cap12_cashflow_attivi_fabbisogni_b.svg"

# ============================================================
# TIPOGRAFIA: tutti i controlli sono raccolti qui
# ============================================================

FONT_FAMILY = "DejaVu Sans"

# Moltiplicatori globali: 1.10 aumenta tutto del 10%; 0.90 riduce del 10%.
FONT_SCALE = 1.00
LINE_SPACING_SCALE = 1.00

FONT_SIZES: dict[str, float] = {
    "title": 16.0,
    "axis_label": 13.5,
    "tick_label": 13.0,
    "value_label": 11.5,
    "annotation": 11.5,
    "legend": 11.0,
}

LINE_SPACINGS: dict[str, float] = {
    "title": 1.00,
    "axis_label": 1.00,
    "tick_label": 1.00,
    "value_label": 1.00,
    "annotation": 1.05,
    "legend": 1.00,
}

plt.rcParams["font.family"] = FONT_FAMILY


def font_size(category: str) -> float:
    """Restituisce il font della categoria, corretto con la scala globale."""
    return FONT_SIZES[category] * FONT_SCALE


def line_spacing(category: str) -> float:
    """Restituisce l'interlinea, corretta con la scala globale."""
    return LINE_SPACINGS[category] * LINE_SPACING_SCALE


# ============================================================
# DIMENSIONI E POSIZIONI DELLA VERSIONE COMPATTA
# ============================================================

FIGSIZE = (8.8, 4.0)  # Formato più largo e meno alto della versione originale.
Y_AXIS_MAX = 9.2

# Geometria orizzontale delle barre:
# - BAR_WIDTH controlla la larghezza di ogni barra;
# - BAR_GAP controlla lo spazio vuoto fra i bordi di due barre consecutive.
BAR_WIDTH = 0.34
BAR_GAP = 0.28
BAR_CENTER_SPACING = BAR_WIDTH + BAR_GAP  # Distanza fra i centri delle barre.

VALUE_LABEL_OFFSET = 0.22
TITLE_PAD = 8

ANNOTATION_X = 0.98
ANNOTATION_Y = 0.96
ANNOTATION_TEXT = (
    r"$\sum_t CF_t = \sum_t d_t = 20$"
    "\n"
    "ma alcuni periodi presentano deficit"
)

# Margini: lo spazio a destra è riservato alla legenda verticale.
SUBPLOT_LEFT = 0.08
SUBPLOT_RIGHT = 0.76
SUBPLOT_BOTTOM = 0.14
SUBPLOT_TOP = 0.88

# ============================================================
# COLORI E STILE DEL FABBISOGNO
# ============================================================

# Scala di azzurri, dal più chiaro al più scuro.
ASSET_COLORS = ("#C6DBEF", "#6BAED6", "#2171B5")

REQUIREMENT_COLOR = "#08306B"
REQUIREMENT_LINESTYLE = "--"
REQUIREMENT_LINEWIDTH = 2.0
REQUIREMENT_MARKER = "D"
REQUIREMENT_MARKER_SIZE = 5.5
REQUIREMENT_MARKER_FACE_COLOR = "#DEEBF7"

# ============================================================
# LEGENDA VERTICALE SUL LATO DESTRO
# ============================================================

# La coppia (x, y) usa coordinate relative agli assi.
LEGEND_LOC = "center left"            # Lato sinistro della legenda ancorato a (x, y).
LEGEND_BBOX_TO_ANCHOR = (1.02, 0.50)  # Legenda appena fuori dal bordo destro.
LEGEND_NCOL = 1                        # Una voce per riga.
LEGEND_HANDLELENGTH = 2.0
LEGEND_BORDERPAD = 0.55
LEGEND_LABELSPACING = 0.65
LEGEND_FRAME = True

# ============================================================
# DATI
# ============================================================

dates = np.array([1, 2, 3, 4])

# Coordinate orizzontali calcolate dai controlli BAR_WIDTH e BAR_GAP.
bar_positions = np.arange(dates.size, dtype=float) * BAR_CENTER_SPACING

cf_attivo_1 = np.array([3.0, 0.0, 2.0, 0.0])
cf_attivo_2 = np.array([2.0, 1.0, 2.0, 1.0])
cf_attivo_3 = np.array([2.0, 2.0, 2.0, 3.0])
fabbisogni = np.array([5.0, 5.0, 5.0, 5.0])

cf_totale = cf_attivo_1 + cf_attivo_2 + cf_attivo_3

# ============================================================
# COSTRUZIONE DEL GRAFICO
# ============================================================

fig, ax = plt.subplots(figsize=FIGSIZE)

ax.bar(
    bar_positions,
    cf_attivo_1,
    width=BAR_WIDTH,
    color=ASSET_COLORS[0],
    label="Attivo 1",
)
ax.bar(
    bar_positions,
    cf_attivo_2,
    width=BAR_WIDTH,
    bottom=cf_attivo_1,
    color=ASSET_COLORS[1],
    label="Attivo 2",
)
ax.bar(
    bar_positions,
    cf_attivo_3,
    width=BAR_WIDTH,
    bottom=cf_attivo_1 + cf_attivo_2,
    color=ASSET_COLORS[2],
    label="Attivo 3",
)

ax.plot(
    bar_positions,
    fabbisogni,
    color=REQUIREMENT_COLOR,
    linestyle=REQUIREMENT_LINESTYLE,
    linewidth=REQUIREMENT_LINEWIDTH,
    marker=REQUIREMENT_MARKER,
    markersize=REQUIREMENT_MARKER_SIZE,
    markerfacecolor=REQUIREMENT_MARKER_FACE_COLOR,
    markeredgecolor=REQUIREMENT_COLOR,
    label=r"Fabbisogno $d_t$",
)

for x, cft, dt in zip(bar_positions, cf_totale, fabbisogni):
    saldo = cft - dt
    testo = f"+{saldo:.0f}" if saldo > 0 else f"{saldo:.0f}"
    ax.text(
        x,
        max(cft, dt) + VALUE_LABEL_OFFSET,
        testo,
        ha="center",
        va="bottom",
        fontsize=font_size("value_label"),
        linespacing=line_spacing("value_label"),
    )

ax.set_xticks(bar_positions)
ax.set_xticklabels([rf"$t={i}$" for i in dates])

# La versione compatta omette intenzionalmente l'etichetta dell'asse x "Data".
ax.set_ylabel(
    "Unità monetarie",
    fontsize=font_size("axis_label"),
    linespacing=line_spacing("axis_label"),
)
ax.set_title(
    "Cash flow degli attivi e fabbisogni alle diverse date",
    fontsize=font_size("title"),
    linespacing=line_spacing("title"),
    pad=TITLE_PAD,
)
ax.tick_params(axis="both", labelsize=font_size("tick_label"))
ax.set_ylim(0, Y_AXIS_MAX)

ax.text(
    ANNOTATION_X,
    ANNOTATION_Y,
    ANNOTATION_TEXT,
    transform=ax.transAxes,
    ha="right",
    va="top",
    fontsize=font_size("annotation"),
    linespacing=line_spacing("annotation"),
)

legend = ax.legend(
    loc=LEGEND_LOC,
    bbox_to_anchor=LEGEND_BBOX_TO_ANCHOR,
    ncol=LEGEND_NCOL,
    frameon=LEGEND_FRAME,
    fontsize=font_size("legend"),
    handlelength=LEGEND_HANDLELENGTH,
    borderpad=LEGEND_BORDERPAD,
    labelspacing=LEGEND_LABELSPACING,
)
for legend_text in legend.get_texts():
    legend_text.set_linespacing(line_spacing("legend"))

fig.subplots_adjust(
    left=SUBPLOT_LEFT,
    right=SUBPLOT_RIGHT,
    bottom=SUBPLOT_BOTTOM,
    top=SUBPLOT_TOP,
)

fig.savefig(png_path, dpi=300, bbox_inches="tight", pad_inches=0.04)
fig.savefig(svg_path, bbox_inches="tight", pad_inches=0.04)

plt.close(fig)

print(f"Figura PNG salvata in: {png_path}")
print(f"Figura SVG salvata in: {svg_path}")
