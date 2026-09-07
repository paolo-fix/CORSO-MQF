from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

OUTPUT_DIR = Path(r"E:\\Didattica\\MQF\\graphics")

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
    "annotation": 14.0,
    "legend": 12.0,
}

# Interlinea per categoria.
LINE_SPACINGS: dict[str, float] = {
    "title": 1.00,
    "axis_label": 1.00,
    "tick_label": 1.00,
    "annotation": 1.00,
    "legend": 1.00,
}

plt.rcParams["font.family"] = FONT_FAMILY


def font_size(category: str) -> float:
    return FONT_SIZES[category] * FONT_SCALE


def line_spacing(category: str) -> float:
    return LINE_SPACINGS[category] * LINE_SPACING_SCALE


# ============================================================
# STILE DEL FABBISOGNO INIZIALE
# ============================================================

REQUIREMENT_COLOR = "#17365D"       # Blu scuro
REQUIREMENT_LINESTYLE = "--"        # Segmento tratteggiato
REQUIREMENT_LINEWIDTH = 2.5
REQUIREMENT_HALF_LENGTH = 0.34       # Semilunghezza in coordinate dell'asse x


# ============================================================
# POSIZIONE E DIMENSIONI DELLA LEGENDA
# ============================================================

# La coppia (x, y) usa coordinate relative agli assi:
# (0, 0) è l'angolo in basso a sinistra; (1, 1) quello in alto a destra.
LEGEND_LOC = "upper center"          # Parte della legenda agganciata alla posizione (x, y).
LEGEND_BBOX_TO_ANCHOR = (0.60, 1.0) # Posizione: x cresce verso destra, y verso l'alto.
LEGEND_NCOL = 1                       # Numero di colonne in cui disporre le voci.
LEGEND_HANDLELENGTH = 2.2             # Lunghezza dei simboli grafici accanto alle voci.
LEGEND_BORDERPAD = 0.55               # Spazio interno tra contenuto e bordo della legenda.
LEGEND_LABELSPACING = 0.50            # Distanza verticale tra le diverse voci della legenda.


# ============================================================
# Dati
# ============================================================

t = np.array([1, 2, 3])
portafoglio_a = np.array([6.0, 2.0, 2.0])
portafoglio_b = np.array([1.0, 2.0, 7.0])
d1 = 5.0
width = 0.34

fig, ax = plt.subplots(figsize=(9.0, 5.2))

ax.bar(
    t - width / 2,
    portafoglio_a,
    width=width,
    label="Portafoglio A: liquidità anticipata",
)

ax.bar(
    t + width / 2,
    portafoglio_b,
    width=width,
    label="Portafoglio B: liquidità posticipata",
)

# Il fabbisogno è riferito soltanto alla prima data.
ax.hlines(
    y=d1,
    xmin=t[0] - REQUIREMENT_HALF_LENGTH,
    xmax=t[0] + REQUIREMENT_HALF_LENGTH,
    colors=REQUIREMENT_COLOR,
    linestyles=REQUIREMENT_LINESTYLE,
    linewidth=REQUIREMENT_LINEWIDTH,
    zorder=4,
    label=r"Fabbisogno iniziale $d_1=5$",
)

ax.set_xticks(t)
ax.set_xticklabels([r"$t=1$", r"$t=2$", r"$t=3$"])
ax.set_xlabel(
    "Data",
    fontsize=font_size("axis_label"),
    linespacing=line_spacing("axis_label"),
)
ax.set_ylabel(
    "Cash flow disponibile",
    fontsize=font_size("axis_label"),
    linespacing=line_spacing("axis_label"),
)
ax.set_title(
    "Stessa liquidità complessiva, diversa distribuzione temporale",
    fontsize=font_size("title"),
    linespacing=line_spacing("title"),
)
ax.tick_params(axis="both", labelsize=font_size("tick_label"))

ax.text(
    0.02,
    0.95,
    r"$\sum_t CF_t^A=10$    e    $\sum_t CF_t^B=10$",
    transform=ax.transAxes,
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
ax.set_ylim(0, 8.2)
fig.tight_layout()

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

png_path = OUTPUT_DIR / "Cap12_liquidita_aggregata_temporale.png"
svg_path = OUTPUT_DIR / "Cap12_liquidita_aggregata_temporale.svg"

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
