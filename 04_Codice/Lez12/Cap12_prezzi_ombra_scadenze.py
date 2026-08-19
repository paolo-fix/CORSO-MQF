from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# ============================================================
# PERCORSI DI OUTPUT
# ============================================================

OUTPUT_DIR = Path(r"E:\Didattica\MQF\graphics")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

png_path = OUTPUT_DIR / "Cap12_prezzi_ombra_scadenze.png"
svg_path = OUTPUT_DIR / "Cap12_prezzi_ombra_scadenze.svg"

# ============================================================
# TIPOGRAFIA: tutti i controlli sono raccolti qui
# ============================================================

FONT_FAMILY = "DejaVu Sans"  # Carattere usato in tutta la figura.

# Moltiplicatori globali: 1.10 aumenta tutto del 10%; 0.90 riduce del 10%.
FONT_SCALE = 1.00
LINE_SPACING_SCALE = 1.00

# Dimensioni dei caratteri per categoria.
FONT_SIZES: dict[str, float] = {
    "axis_label": 16.0,
    "tick_label": 15.0,
    "value_label": 13,
    "annotation": 13,
}

# Interlinea per categoria.
LINE_SPACINGS: dict[str, float] = {
    "axis_label": 1.00,
    "tick_label": 1.00,
    "value_label": 1.00,
    "annotation": 1.00,
}

plt.rcParams["font.family"] = FONT_FAMILY


def font_size(category: str) -> float:
    """Restituisce il font della categoria, corretto con la scala globale."""
    return FONT_SIZES[category] * FONT_SCALE


def line_spacing(category: str) -> float:
    """Restituisce l'interlinea, corretta con la scala globale."""
    return LINE_SPACINGS[category] * LINE_SPACING_SCALE


# ============================================================
# COLORI DEL GRAFICO
# ============================================================

BAR_COLOR = "#6BAED6"       # Riempimento delle barre.
BAR_EDGE_COLOR = "#2171B5"  # Bordo delle barre.
TEXT_COLOR = "#111111"      # Testi e annotazioni.


# ============================================================
# DIMENSIONI E POSIZIONI DEL GRAFICO
# ============================================================

FIGSIZE = (8.8, 4.6)  # Dimensioni della figura in pollici.
Y_AXIS_MAX = 0.052    # Limite superiore dell'asse verticale.

BAR_WIDTH = 0.55          # Larghezza delle barre.
VALUE_LABEL_OFFSET = 0.0012  # Distanza dei valori dalla sommità delle barre.

CAP_ANNOTATION_XY = (3.22, 0.0351)       # Punto indicato dalla freccia.
CAP_ANNOTATION_TEXT_XY = (3.35, 0.044)   # Posizione del testo della freccia.
CAP_ARROW_LINEWIDTH = 1.0                # Spessore della freccia.

TERMINAL_NOTE_X = 3.63    # Posizione orizzontale della nota terminale.
TERMINAL_NOTE_Y = 0.0072  # Posizione verticale della nota terminale.
TERMINAL_NOTE_TEXT = r"$g_4^*>0$:" "\n" "margine terminale"

# Margini della figura espressi come frazioni di larghezza e altezza.
SUBPLOT_LEFT = 0.12
SUBPLOT_RIGHT = 0.98
SUBPLOT_BOTTOM = 0.16
SUBPLOT_TOP = 0.96

# ============================================================
# DATI DELLA SOLUZIONE OTTIMA
# ============================================================

t = np.array([1, 2, 3, 4], dtype=float)
lambda_t = np.array([
    0.0452381562,
    0.0400379664,
    0.0338349566,
    0.0,
])

# ============================================================
# COSTRUZIONE DEL GRAFICO
# ============================================================

fig, ax = plt.subplots(figsize=FIGSIZE)

bars = ax.bar(
    t,
    lambda_t,
    width=BAR_WIDTH,
    color=BAR_COLOR,
    edgecolor=BAR_EDGE_COLOR,
)

for bar, value in zip(bars, lambda_t):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        value + VALUE_LABEL_OFFSET,
        f"{value:.4f}",
        ha="center",
        va="bottom",
        fontsize=font_size("value_label"),
        linespacing=line_spacing("value_label"),
        color=TEXT_COLOR,
    )

ax.set_xticks(t)
ax.set_xticklabels([rf"$t={int(periodo)}$" for periodo in t])
ax.set_xlabel(
    "Data",
    fontsize=font_size("axis_label"),
    linespacing=line_spacing("axis_label"),
)
ax.set_ylabel(
    r"Valore marginale $\lambda_t^*$",
    fontsize=font_size("axis_label"),
    linespacing=line_spacing("axis_label"),
)
ax.tick_params(axis="both", labelsize=font_size("tick_label"))
ax.set_ylim(0, Y_AXIS_MAX)

ax.annotate(
    r"$u_3^*=\bar u_3$",
    xy=CAP_ANNOTATION_XY,
    xytext=CAP_ANNOTATION_TEXT_XY,
    arrowprops={
        "arrowstyle": "->",
        "linewidth": CAP_ARROW_LINEWIDTH,
        "color": TEXT_COLOR,
    },
    fontsize=font_size("annotation"),
    linespacing=line_spacing("annotation"),
    ha="left",
    color=TEXT_COLOR,
)

ax.text(
    TERMINAL_NOTE_X,
    TERMINAL_NOTE_Y,
    TERMINAL_NOTE_TEXT,
    ha="left",
    va="bottom",
    fontsize=font_size("annotation"),
    linespacing=line_spacing("annotation"),
    color=TEXT_COLOR,
)

fig.subplots_adjust(
    left=SUBPLOT_LEFT,
    right=SUBPLOT_RIGHT,
    bottom=SUBPLOT_BOTTOM,
    top=SUBPLOT_TOP,
)

fig.savefig(
    png_path,
    dpi=300,
    bbox_inches="tight",
    pad_inches=0.04,
)

fig.savefig(
    svg_path,
    bbox_inches="tight",
    pad_inches=0.04,
)

plt.close(fig)

print(f"Figura PNG salvata in: {png_path}")
print(f"Figura SVG salvata in: {svg_path}")
