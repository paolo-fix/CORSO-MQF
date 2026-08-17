from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

OUTPUT_DIR = Path(r"E:\Didattica\MQF\graphics")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ============================================================
# TIPOGRAFIA: tutti i controlli sono raccolti qui
# ============================================================

FONT_FAMILY = "DejaVu Sans"

# Moltiplicatori globali: 1.10 aumenta tutto del 10%; 0.90 riduce del 10%.
FONT_SCALE = 1.00
LINE_SPACING_SCALE = 1.00

FONT_SIZES: dict[str, float] = {
    "title": 18.0,
    "axis_label": 16.0,
    "tick_label": 16.0,
    "value_label": 14.0,
    "annotation": 13.5,
    "legend": 12.0,
}

LINE_SPACINGS: dict[str, float] = {
    "title": 1.00,
    "axis_label": 1.00,
    "tick_label": 1.00,
    "value_label": 1.00,
    "annotation": 1.10,
    "legend": 1.00,
}

plt.rcParams["font.family"] = FONT_FAMILY


def font_size(category: str) -> float:
    return FONT_SIZES[category] * FONT_SCALE


def line_spacing(category: str) -> float:
    return LINE_SPACINGS[category] * LINE_SPACING_SCALE


# ============================================================
# DIMENSIONI E POSIZIONE DEI TESTI SUPERIORI
# ============================================================

FIGSIZE = (9.2, 5.4)       # Dimensioni della figura in pollici.
Y_AXIS_MAX = 9.2           # Spazio verticale, compresa la fascia dell'annotazione.
TITLE_PAD = 12             # Distanza tra il titolo e il bordo superiore degli assi.
ANNOTATION_X = 0.98        # Posizione orizzontale dell'annotazione negli assi.
ANNOTATION_Y = 0.96        # Posizione verticale dell'annotazione negli assi.

ANNOTATION_TEXT = (
    r"$\sum_t CF_t = \sum_t d_t = 20$"
    "\n"
    "ma alcuni periodi presentano deficit"
)


# ============================================================
# COLORI E STILE DEL FABBISOGNO
# ============================================================

# Scala di azzurri, dal più chiaro al più scuro.
ASSET_COLORS = ("#C6DBEF", "#6BAED6", "#2171B5")

REQUIREMENT_COLOR = "#08306B"              # Colore della linea e del bordo dei rombi.
REQUIREMENT_LINESTYLE = "--"               # Linea tratteggiata.
REQUIREMENT_LINEWIDTH = 2.2                 # Spessore della linea.
REQUIREMENT_MARKER = "D"                   # Simbolo visualizzato alle singole date.
REQUIREMENT_MARKER_SIZE = 6.5               # Dimensione dei simboli.
REQUIREMENT_MARKER_FACE_COLOR = "#DEEBF7"  # Riempimento chiaro per migliorare il contrasto.


# ============================================================
# POSIZIONE E DIMENSIONI DELLA LEGENDA
# ============================================================

# La coppia (x, y) usa coordinate relative agli assi:
# (0, 0) è l'angolo in basso a sinistra; (1, 1) quello in alto a destra.
LEGEND_LOC = "upper center"           # Parte della legenda agganciata alla posizione (x, y).
LEGEND_BBOX_TO_ANCHOR = (0.50, -0.18) # Posizione: x cresce verso destra, y verso l'alto.
LEGEND_NCOL = 4                        # Numero di colonne in cui disporre le voci.
LEGEND_HANDLELENGTH = 2.2              # Lunghezza dei simboli grafici accanto alle voci.
LEGEND_BORDERPAD = 0.55                # Spazio interno tra contenuto e bordo della legenda.
LEGEND_LABELSPACING = 0.50             # Distanza verticale tra le diverse voci della legenda.


# ============================================================
# Dati
# ============================================================

t = np.array([1, 2, 3, 4])

cf_attivo_1 = np.array([3.0, 0.0, 2.0, 0.0])
cf_attivo_2 = np.array([2.0, 1.0, 2.0, 1.0])
cf_attivo_3 = np.array([2.0, 2.0, 2.0, 3.0])
fabbisogni = np.array([5.0, 5.0, 5.0, 5.0])

cf_totale = cf_attivo_1 + cf_attivo_2 + cf_attivo_3

fig, ax = plt.subplots(figsize=FIGSIZE)

ax.bar(t, cf_attivo_1, width=0.58, color=ASSET_COLORS[0], label="Attivo 1")
ax.bar(
    t,
    cf_attivo_2,
    width=0.58,
    bottom=cf_attivo_1,
    color=ASSET_COLORS[1],
    label="Attivo 2",
)
ax.bar(
    t,
    cf_attivo_3,
    width=0.58,
    bottom=cf_attivo_1 + cf_attivo_2,
    color=ASSET_COLORS[2],
    label="Attivo 3",
)

ax.plot(
    t,
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

for ti, cft, dt in zip(t, cf_totale, fabbisogni):
    saldo = cft - dt
    testo = f"+{saldo:.0f}" if saldo > 0 else f"{saldo:.0f}"
    ax.text(
        ti,
        max(cft, dt) + 0.25,
        testo,
        ha="center",
        va="bottom",
        fontsize=font_size("value_label"),
        linespacing=line_spacing("value_label"),
    )

ax.set_xticks(t)
ax.set_xticklabels([rf"$t={i}$" for i in t])
ax.set_xlabel(
    "Data",
    fontsize=font_size("axis_label"),
    linespacing=line_spacing("axis_label"),
)
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
    fontsize=font_size("legend"),
    handlelength=LEGEND_HANDLELENGTH,
    borderpad=LEGEND_BORDERPAD,
    labelspacing=LEGEND_LABELSPACING,
)
for legend_text in legend.get_texts():
    legend_text.set_linespacing(line_spacing("legend"))

fig.tight_layout()

png_path = OUTPUT_DIR / "Cap12_cashflow_attivi_fabbisogni.png"
svg_path = OUTPUT_DIR / "Cap12_cashflow_attivi_fabbisogni.svg"

fig.savefig(
    png_path,
    dpi=300,
    bbox_inches="tight",
)

fig.savefig(
    svg_path,
    bbox_inches="tight",
)

plt.close(fig)

print(f"Figura PNG salvata in: {png_path}")
print(f"Figura SVG salvata in: {svg_path}")
