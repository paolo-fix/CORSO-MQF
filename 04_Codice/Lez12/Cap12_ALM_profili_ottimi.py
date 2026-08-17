from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

OUTPUT_DIR = Path(r"E:\Didattica\MQF\graphics")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

png_path = OUTPUT_DIR / "Cap12_ALM_profili_ottimi.png"
svg_path = OUTPUT_DIR / "Cap12_ALM_profili_ottimi.svg"

# ============================================================
# TIPOGRAFIA: tutti i controlli sono raccolti qui
# ============================================================

FONT_FAMILY = "DejaVu Sans"  # Carattere usato in tutta la figura.

# Moltiplicatori globali: 1.10 aumenta tutto del 10%; 0.90 riduce del 10%.
FONT_SCALE = 1.00
LINE_SPACING_SCALE = 1.00

# Dimensioni dei caratteri per categoria.
FONT_SIZES: dict[str, float] = {
    "axis_label": 14.0,
    "tick_label": 13.0,
    "total_label": 11.5,
    "group_label": 11.5,
    "annotation": 11.5,
    "legend": 11.0,
}

# Interlinea per categoria.
LINE_SPACINGS: dict[str, float] = {
    "axis_label": 1.00,
    "tick_label": 1.00,
    "total_label": 1.00,
    "group_label": 1.00,
    "annotation": 1.00,
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
# COLORI DELLE RISORSE E DEGLI IMPIEGHI
# ============================================================

# Scala di azzurri, dal più chiaro al più scuro, per le risorse R.
RESOURCE_COLORS = ("#C6DBEF", "#6BAED6", "#2171B5")

# Scala di rosa, dal più chiaro al più scuro, per gli impieghi I.
USE_COLORS = ("#FDD0D7", "#F768A1", "#AE017E")


# ============================================================
# DIMENSIONI E POSIZIONI DEL GRAFICO
# ============================================================

FIGSIZE = (9.8, 5.4)  # Dimensioni della figura in pollici.
Y_AXIS_MAX = 40.5     # Limite superiore dell'asse verticale.

BAR_WIDTH = 0.32       # Larghezza di ciascuna barra.
PAIR_OFFSET = 0.18     # Distanza di R e I dal centro di ogni data.
TOTAL_LABEL_OFFSET = 0.55  # Distanza dei totali dalla sommità delle barre.
GROUP_LABEL_Y = 0.70       # Altezza delle lettere R e I dentro le barre.

ANNOTATION_X = 0.01  # Posizione orizzontale della nota R/I negli assi.
ANNOTATION_Y = 0.98  # Posizione verticale della nota R/I negli assi.

# Margini della figura espressi come frazioni di larghezza e altezza.
SUBPLOT_LEFT = 0.09
SUBPLOT_RIGHT = 0.99
SUBPLOT_TOP = 0.98
SUBPLOT_BOTTOM = 0.24


# ============================================================
# POSIZIONE E DIMENSIONI DELLA LEGENDA
# ============================================================

# La coppia (x, y) usa coordinate relative agli assi:
# (0, 0) è l'angolo in basso a sinistra; (1, 1) quello in alto a destra.
LEGEND_LOC = "upper center"          # Parte della legenda agganciata alla posizione (x, y).
LEGEND_BBOX = (0.50, -0.13)          # Posizione: x cresce verso destra, y verso l'alto.
LEGEND_NCOL = 3                       # Numero di colonne in cui disporre le voci.
LEGEND_FRAME = False                  # Mostra o nasconde il bordo della legenda.
LEGEND_HANDLELENGTH = 1.8             # Lunghezza dei simboli accanto alle voci.
LEGEND_COLUMNSPACING = 1.15           # Distanza orizzontale tra le colonne.
LEGEND_LABELSPACING = 0.45            # Distanza verticale tra le righe.
LEGEND_ORDER = (0, 3, 1, 4, 2, 5)    # Prima riga R azzurre, seconda riga I rosa.

# ============================================================
# DATI DELLA SOLUZIONE OTTIMA
# ============================================================

t = np.array([1, 2, 3, 4], dtype=float)

cash_flow_attivi = np.array([
    36.1518102942,
    25.3839367647,
    14.4240948529,
    24.0401580881,
])

giacenza_ereditata = np.array([
    0.0,
    6.1825693414,
    1.5759051430,
    0.0,
])

nuovo_funding = np.array([
    0.0,
    0.0,
    6.0,
    0.0,
])

fabbisogni = np.array([
    30.0,
    30.0,
    22.0,
    15.0,
])

rimborso_funding = np.array([
    0.0,
    0.0,
    0.0,
    6.15,
])

giacenza_finale = np.array([
    6.1518102942,
    1.5665061105,
    0.0,
    2.8901580881,
])

x_risorse = t - PAIR_OFFSET
x_impieghi = t + PAIR_OFFSET

# ============================================================
# COSTRUZIONE DEL GRAFICO
# ============================================================

fig, ax = plt.subplots(figsize=FIGSIZE)

ax.bar(
    x_risorse,
    cash_flow_attivi,
    width=BAR_WIDTH,
    color=RESOURCE_COLORS[0],
    label="Cash flow attivi",
)

ax.bar(
    x_risorse,
    giacenza_ereditata,
    width=BAR_WIDTH,
    bottom=cash_flow_attivi,
    color=RESOURCE_COLORS[1],
    label="Giacenza ereditata",
)

ax.bar(
    x_risorse,
    nuovo_funding,
    width=BAR_WIDTH,
    bottom=cash_flow_attivi + giacenza_ereditata,
    color=RESOURCE_COLORS[2],
    label="Nuovo funding",
)

ax.bar(
    x_impieghi,
    fabbisogni,
    width=BAR_WIDTH,
    color=USE_COLORS[0],
    label="Fabbisogno",
)

ax.bar(
    x_impieghi,
    rimborso_funding,
    width=BAR_WIDTH,
    bottom=fabbisogni,
    color=USE_COLORS[1],
    label="Rimborso funding",
)

ax.bar(
    x_impieghi,
    giacenza_finale,
    width=BAR_WIDTH,
    bottom=fabbisogni + rimborso_funding,
    color=USE_COLORS[2],
    label="Giacenza finale",
)

tot_risorse = cash_flow_attivi + giacenza_ereditata + nuovo_funding
tot_impieghi = fabbisogni + rimborso_funding + giacenza_finale

for xr, xi, tr, ti in zip(x_risorse, x_impieghi, tot_risorse, tot_impieghi):
    ax.text(
        xr,
        tr + TOTAL_LABEL_OFFSET,
        f"{tr:.1f}",
        ha="center",
        va="bottom",
        fontsize=font_size("total_label"),
        linespacing=line_spacing("total_label"),
    )
    ax.text(
        xi,
        ti + TOTAL_LABEL_OFFSET,
        f"{ti:.1f}",
        ha="center",
        va="bottom",
        fontsize=font_size("total_label"),
        linespacing=line_spacing("total_label"),
    )

for xr, xi in zip(x_risorse, x_impieghi):
    ax.text(
        xr,
        GROUP_LABEL_Y,
        "R",
        ha="center",
        va="center",
        fontsize=font_size("group_label"),
        linespacing=line_spacing("group_label"),
        fontweight="bold",
        color=RESOURCE_COLORS[2],
    )
    ax.text(
        xi,
        GROUP_LABEL_Y,
        "I",
        ha="center",
        va="center",
        fontsize=font_size("group_label"),
        linespacing=line_spacing("group_label"),
        fontweight="bold",
        color=USE_COLORS[2],
    )

ax.set_xticks(t)
ax.set_xticklabels([r"$t=1$", r"$t=2$", r"$t=3$", r"$t=4$"])
ax.set_ylabel(
    "Unità monetarie",
    fontsize=font_size("axis_label"),
    linespacing=line_spacing("axis_label"),
)
ax.tick_params(axis="both", labelsize=font_size("tick_label"))
ax.set_ylim(0, Y_AXIS_MAX)

legend_handles, legend_labels = ax.get_legend_handles_labels()
legend = ax.legend(
    [legend_handles[i] for i in LEGEND_ORDER],
    [legend_labels[i] for i in LEGEND_ORDER],
    loc=LEGEND_LOC,
    bbox_to_anchor=LEGEND_BBOX,
    ncol=LEGEND_NCOL,
    frameon=LEGEND_FRAME,
    fontsize=font_size("legend"),
    handlelength=LEGEND_HANDLELENGTH,
    columnspacing=LEGEND_COLUMNSPACING,
    labelspacing=LEGEND_LABELSPACING,
)
for legend_text in legend.get_texts():
    legend_text.set_linespacing(line_spacing("legend"))

ax.text(
    ANNOTATION_X,
    ANNOTATION_Y,
    "R = risorse disponibili; I = impieghi della liquidità",
    transform=ax.transAxes,
    ha="left",
    va="top",
    fontsize=font_size("annotation"),
    linespacing=line_spacing("annotation"),
)

fig.subplots_adjust(
    left=SUBPLOT_LEFT,
    right=SUBPLOT_RIGHT,
    top=SUBPLOT_TOP,
    bottom=SUBPLOT_BOTTOM,
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
