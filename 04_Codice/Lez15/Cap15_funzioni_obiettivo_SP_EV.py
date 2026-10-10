from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# PERCORSI DI OUTPUT
# ============================================================

# Cambia soltanto questa riga per inviare entrambe le figure altrove.
OUTPUT_DIR = Path(r"E:\Didattica\MQF\graphics")
# Nomi dei file, senza estensione: vengono creati sia PNG sia SVG.
OUTPUT_SP_STEM = "Cap15_funzione_obiettivo_SP"
OUTPUT_EV_STEM = "Cap15_funzione_obiettivo_EV"
# Qualità PNG e ritaglio/margine comune ai due formati.
PNG_DPI = 300
SAVE_BBOX = "tight"
SAVE_PAD_INCHES = 0.05

# ============================================================
# TIPOGRAFIA
# ============================================================

# Famiglia globale; FONT_SCALE aumenta/riduce tutte le dimensioni insieme.
FONT_FAMILY = "DejaVu Sans"
FONT_SCALE = 1.00
# LINE_SPACING_SCALE compatta o amplia tutte le interlinee insieme.
LINE_SPACING_SCALE = 1.00

# Dimensioni per categoria: modifica qui, non dentro i blocchi SP/EV sotto.
FONT_SIZES = {
    "title": 19.0,
    "axis_label": 17.0,
    "tick_label": 15.0,
    "annotation": 14,
    "legend": 14,
}

# Interlinea per categoria: ha effetto soprattutto su titoli e annotazioni multilinea.
LINE_SPACINGS = {
    "title": 1.00,
    "axis_label": 1.00,
    "tick_label": 1.00,
    "annotation": 1.5,
    "legend": 1.00,
}

plt.rcParams["font.family"] = FONT_FAMILY
plt.rcParams["mathtext.fontset"] = "dejavusans"
plt.rcParams["svg.fonttype"] = "none"


def font_size(category):
    return FONT_SIZES[category] * FONT_SCALE


def line_spacing(category):
    return LINE_SPACINGS[category] * LINE_SPACING_SCALE


def text_style(category):
    return {
        "fontsize": font_size(category),
        "linespacing": line_spacing(category),
    }


def save_figure(fig, stem):
    """Salva PNG e SVG e comunica chiaramente le destinazioni."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    png_path = OUTPUT_DIR / f"{stem}.png"
    svg_path = OUTPUT_DIR / f"{stem}.svg"
    fig.savefig(
        png_path,
        dpi=PNG_DPI,
        bbox_inches=SAVE_BBOX,
        pad_inches=SAVE_PAD_INCHES,
        facecolor="white",
    )
    fig.savefig(
        svg_path,
        bbox_inches=SAVE_BBOX,
        pad_inches=SAVE_PAD_INCHES,
        facecolor="white",
    )
    plt.close(fig)

    print("Figure salvate:")
    print(f"  PNG: {png_path}")
    print(f"  SVG: {svg_path}")

# ============================================================
# CONFIGURAZIONE GRAFICA COMUNE
# ============================================================

# Dimensione della tela in pollici e stile dei principali elementi grafici.
FIG_SIZE = (9.2, 5.8)
LINEWIDTH = 2.4
GUIDE_LINEWIDTH = 1.2
MARKER_SIZE = 55
# Numero di punti con cui sono tracciati i tratti lineari delle due funzioni.
N_GRID = 501
# Intervallo dei valori ammissibili di x_2 usato per entrambe le curve.
X2_MIN = 0.0
X2_MAX = 10.0
# Limiti orizzontali e trasparenza della griglia comuni alle due figure.
X_LIM = (-0.5, 10.5)
GRID_ALPHA = 0.20

# ============================================================
# DATI E CONTROLLI DELLA FIGURA SP
# ============================================================

# I primi quattro parametri definiscono la funzione spezzata Pi^SP(x_2).
SP_BREAK_X = 4.0
SP_LEFT_INTERCEPT = 0.10
SP_LEFT_SLOPE = 0.04
SP_RIGHT_INTERCEPT = 0.30
SP_RIGHT_SLOPE = -0.01
# Posizioni (x, y) dell'annotazione dell'ottimo e dell'etichetta del breakpoint.
SP_ANNOTATION_POS = (5.15, 0.278)
SP_BREAK_LABEL_POS = (SP_BREAK_X, 0.113)
# Limiti verticali e posizione della legenda della figura SP.
SP_Y_LIM = (0.09, 0.29)
SP_LEGEND_LOC = "upper right"

# ============================================================
# DATI E CONTROLLI DELLA FIGURA EV
# ============================================================

# I parametri definiscono la funzione spezzata Pi^EV(x_2).
EV_BREAK_X = 20.0 / 3.0
EV_LEFT_INTERCEPT = 0.10
EV_LEFT_SLOPE = 0.04
EV_RIGHT_INTERCEPT = 0.32
EV_RIGHT_SLOPE = 0.007
# Posizioni (x, y) dell'annotazione dell'ottimo e dell'etichetta del breakpoint.
EV_ANNOTATION_POS = (7.7, 0.345)
EV_BREAK_LABEL_POS = (EV_BREAK_X, 0.113)
# Limiti verticali e posizione della legenda della figura EV.
EV_Y_LIM = (0.085, 0.44)
EV_LEGEND_LOC = "upper left"

# ============================================================
# COSTRUZIONE DELLE DUE FUNZIONI
# ============================================================

x2 = np.linspace(X2_MIN, X2_MAX, N_GRID)

pi_sp = np.where(
    x2 <= SP_BREAK_X,
    SP_LEFT_INTERCEPT + SP_LEFT_SLOPE * x2,
    SP_RIGHT_INTERCEPT + SP_RIGHT_SLOPE * x2,
)

pi_ev = np.where(
    x2 <= EV_BREAK_X,
    EV_LEFT_INTERCEPT + EV_LEFT_SLOPE * x2,
    EV_RIGHT_INTERCEPT + EV_RIGHT_SLOPE * x2,
)

# Coordinate degli ottimi, calcolate dai parametri: non modificare a mano.
SP_OPTIMUM = (
    SP_BREAK_X,
    SP_LEFT_INTERCEPT + SP_LEFT_SLOPE * SP_BREAK_X,
)
EV_OPTIMUM = (
    X2_MAX,
    EV_RIGHT_INTERCEPT + EV_RIGHT_SLOPE * X2_MAX,
)

# ============================================================
# FIGURA SP
# ============================================================

fig, ax = plt.subplots(figsize=FIG_SIZE)

ax.plot(x2, pi_sp, linewidth=LINEWIDTH, label=r"$\Pi^{SP}(x_2)$")
# Guida verticale e punto di massimo: controllati dai parametri SP sopra.
ax.axvline(SP_BREAK_X, linestyle="--", linewidth=GUIDE_LINEWIDTH)
ax.scatter([SP_OPTIMUM[0]], [SP_OPTIMUM[1]], s=MARKER_SIZE, zorder=3)

# Freccia dell'ottimo: modifica SP_ANNOTATION_POS per spostare il testo.
ax.annotate(
    r"$x_2^{SP}=4$" "\n" r"$z^{SP}=0.26$",
    xy=SP_OPTIMUM,
    xytext=SP_ANNOTATION_POS,
    ha="left",
    va="top",
    arrowprops={"arrowstyle": "->", "shrinkA": 2, "shrinkB": 10},
    **text_style("annotation"),
)

ax.text(
    *SP_BREAK_LABEL_POS,
    r"$x_2=4$",
    ha="center",
    va="bottom",
    **text_style("annotation"),
)

ax.set_title(
    r"Funzione obiettivo stocastica $\Pi^{SP}(x_2)$",
    **text_style("title"),
    pad=10,
)
ax.set_xlabel(
    r"Investimento $x_2$ nei titoli meno liquidi (milioni di euro)",
    **text_style("axis_label"),
)
ax.set_ylabel(
    r"Valore della funzione obiettivo (milioni di euro)",
    **text_style("axis_label"),
)
ax.set_xlim(*X_LIM)
ax.set_ylim(*SP_Y_LIM)
ax.tick_params(labelsize=font_size("tick_label"))
ax.grid(alpha=GRID_ALPHA)
legend = ax.legend(frameon=False, fontsize=font_size("legend"), loc=SP_LEGEND_LOC)
for legend_text in legend.get_texts():
    legend_text.set_linespacing(line_spacing("legend"))

fig.tight_layout()
save_figure(fig, OUTPUT_SP_STEM)

# ============================================================
# FIGURA EV
# ============================================================

fig, ax = plt.subplots(figsize=FIG_SIZE)

ax.plot(x2, pi_ev, linewidth=LINEWIDTH, label=r"$\Pi^{EV}(x_2)$")
# Guida verticale e punto di massimo: controllati dai parametri EV sopra.
ax.axvline(EV_BREAK_X, linestyle="--", linewidth=GUIDE_LINEWIDTH)
ax.scatter([EV_OPTIMUM[0]], [EV_OPTIMUM[1]], s=MARKER_SIZE, zorder=3)

# Freccia dell'ottimo: modifica EV_ANNOTATION_POS per spostare il testo.
ax.annotate(
    r"$x_2^{EV}=10$" "\n" r"$\Pi^{EV}(10)=0.39$",
    xy=EV_OPTIMUM,
    xytext=EV_ANNOTATION_POS,
    ha="left",
    va="center",
    arrowprops={"arrowstyle": "->", "shrinkA": 2, "shrinkB": 10},
    **text_style("annotation"),
)

ax.text(
    *EV_BREAK_LABEL_POS,
    r"$x_2=20/3$",
    ha="center",
    va="bottom",
    **text_style("annotation"),
)

ax.set_title(
    r"Funzione obiettivo del problema medio $\Pi^{EV}(x_2)$",
    **text_style("title"),
    pad=10,
)
ax.set_xlabel(
    r"Investimento $x_2$ nei titoli meno liquidi (milioni di euro)",
    **text_style("axis_label"),
)
ax.set_ylabel(
    r"Valore della funzione obiettivo (milioni di euro)",
    **text_style("axis_label"),
)
ax.set_xlim(*X_LIM)
ax.set_ylim(*EV_Y_LIM)
ax.tick_params(labelsize=font_size("tick_label"))
ax.grid(alpha=GRID_ALPHA)
legend = ax.legend(frameon=False, fontsize=font_size("legend"), loc=EV_LEGEND_LOC)
for legend_text in legend.get_texts():
    legend_text.set_linespacing(line_spacing("legend"))

fig.tight_layout()
save_figure(fig, OUTPUT_EV_STEM)
