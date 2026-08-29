from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

# ============================================================
# PERCORSO E PARAMETRI DI SALVATAGGIO
# ============================================================

OUTPUT_DIR = Path(r"E:\Didattica\MQF\graphics")
OUTPUT_STEM = "Cap15_funzione_ricorso_piecewise"

PNG_DPI = 300
SAVE_BBOX = "tight"
SAVE_PAD_INCHES = 0.04

# ============================================================
# DATI DEL PROBLEMA: controlli economici
# ============================================================

# Le grandezze monetarie sono espresse direttamente in milioni di euro.
A0 = 10_000.0
LIQUIDITY_NEED = 6_000.0

# Coefficienti di liquidità nello scenario avverso.
A_LIQUID = 1.0
A_ILLIQUID = 0.2

# Costo unitario del funding: 3% dell'ammontare finanziato.
FUNDING_UNIT_COST = 0.03

X_MIN = 0.0
X_MAX = A0
N_GRID = 501
X_TICK_STEP = 2_000.0

# ============================================================
# TIPOGRAFIA: tutti i controlli sono raccolti qui
# ============================================================

FONT_FAMILY = "DejaVu Sans"
FONT_SCALE = 1.00
LINE_SPACING_SCALE = 1.00

FONT_SIZES = {
    "suptitle": 19.0,
    "panel_title": 17.0,
    "axis_label": 15,
    "tick_label": 13,
    "formula": 15,
    "annotation": 13,
    "footer": 13,
}

LINE_SPACINGS = {
    "suptitle": 1.00,
    "panel_title": 1.00,
    "axis_label": 1.00,
    "tick_label": 1.00,
    "formula": 1.05,
    "annotation": 1.15,
    "footer": 1.05,
}

plt.rcParams["font.family"] = FONT_FAMILY


def font_size(category):
    """Restituisce il font della categoria, corretto con la scala globale."""
    return FONT_SIZES[category] * FONT_SCALE


def line_spacing(category):
    """Restituisce l'interlinea, corretta con la scala globale."""
    return LINE_SPACINGS[category] * LINE_SPACING_SCALE


# ============================================================
# ASPETTO DELLA FIGURA: controlli grafici
# ============================================================

# Scala applicata soltanto alla larghezza complessiva della figura:
# 1.00 = larghezza originaria; valori inferiori comprimono gli assi x.
BASE_FIG_WIDTH = 15.5
FIG_HORIZONTAL_SCALE = 0.82
FIG_HEIGHT = 6.4
FIG_SIZE = (BASE_FIG_WIDTH * FIG_HORIZONTAL_SCALE, FIG_HEIGHT)
SUBPLOT_WSPACE = 0.12
X_LIMITS = (X_MIN, X_MAX)

# Margini verticali, proporzionali all'intervallo dei valori di Q.
Y_BOTTOM_MARGIN = 0.08
Y_TOP_MARGIN = 0.08

COLORS = {
    "recourse": "#2C7FB8",
    "breakpoint": "#1D4E89",
    "zero_axis": "#555555",
    "funding_region": "#F6D8D5",
    "annotation": "#222222",
}

RECOURSE_LINEWIDTH = 2.6
BREAKPOINT_LINEWIDTH = 1.4
BREAKPOINT_LINESTYLE = "--"
ZERO_AXIS_LINEWIDTH = 0.9
FUNDING_REGION_ALPHA = 0.42
MARKER_SIZE = 58

GRID_VISIBLE = True
GRID_ALPHA = 0.24
GRID_LINESTYLE = "--"

# Posizioni delle scritte interne: coordinate relative a ciascun pannello.
LEFT_FLAT_FORMULA_AXES = (0.73, 0.88)
LEFT_LINEAR_FORMULA_AXES = (0.25, 0.38)
LEFT_ANNOTATION_AXES = (0.63, 0.65)

RIGHT_FLAT_FORMULA_AXES = (0.27, 0.88)
RIGHT_LINEAR_FORMULA_AXES = (0.75, 0.38)
RIGHT_ANNOTATION_AXES = (0.07, 0.65)

# Fondo bianco delle formule e delle annotazioni.
TEXT_BBOX_FACE_COLOR = "white"
TEXT_BBOX_EDGE_COLOR = "none"
TEXT_BBOX_ALPHA = 0.90
TEXT_BBOX_PADDING = 0.14

FOOTER_Y = 0.025
TIGHT_LAYOUT_RECT = (0.00, 0.085, 1.00, 0.94)


# ============================================================
# FUNZIONI DI SUPPORTO
# ============================================================

def text_bbox():
    """Restituisce lo stile comune del fondo delle scritte interne."""
    return {
        "facecolor": TEXT_BBOX_FACE_COLOR,
        "edgecolor": TEXT_BBOX_EDGE_COLOR,
        "alpha": TEXT_BBOX_ALPHA,
        "boxstyle": f"square,pad={TEXT_BBOX_PADDING}",
    }


def affine_formula(intercept, slope, variable):
    """Costruisce una formula affine senza segni doppi o valori cablati."""
    return rf"$Q_2({variable})={intercept:g}{slope:+g}{variable}$"


def format_thousands(value, _position):
    """Formatta le migliaia con uno spazio sottile: 10 000 anziché 10000."""
    return f"{value:,.0f}".replace(",", "\u202f")


def format_math_thousands(value):
    """Formatta le migliaia per MathText: 5\\,000 anziché 5000."""
    return f"{value:,.0f}".replace(",", r"\,")


def save_figure(fig, stem):
    """Salva la figura in PNG e SVG e comunica le destinazioni effettive."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    png_path = OUTPUT_DIR / f"{stem}.png"
    svg_path = OUTPUT_DIR / f"{stem}.svg"

    fig.savefig(
        png_path,
        dpi=PNG_DPI,
        bbox_inches=SAVE_BBOX,
        pad_inches=SAVE_PAD_INCHES,
    )
    fig.savefig(
        svg_path,
        bbox_inches=SAVE_BBOX,
        pad_inches=SAVE_PAD_INCHES,
    )
    plt.close(fig)

    print(f"Figura PNG salvata in: {png_path.resolve()}")
    print(f"Figura SVG salvata in: {svg_path.resolve()}")
    return png_path, svg_path


def configure_panel(ax, title, x_label, y_limits):
    """Applica ai due pannelli la stessa configurazione grafica."""
    ax.set_xlim(*X_LIMITS)
    ax.set_ylim(*y_limits)
    ax.set_title(
        title,
        fontsize=font_size("panel_title"),
        pad=10,
    )
    ax.set_xlabel(x_label, fontsize=font_size("axis_label"))
    ax.set_xticks(np.arange(X_MIN, X_MAX + X_TICK_STEP, X_TICK_STEP))
    ax.xaxis.set_major_formatter(FuncFormatter(format_thousands))
    ax.tick_params(axis="both", labelsize=font_size("tick_label"))
    ax.axhline(
        0.0,
        color=COLORS["zero_axis"],
        linewidth=ZERO_AXIS_LINEWIDTH,
        zorder=0,
    )
    ax.grid(
        GRID_VISIBLE,
        alpha=GRID_ALPHA,
        linestyle=GRID_LINESTYLE,
    )


def add_formula(ax, position, formula):
    """Aggiunge una formula usando coordinate relative al pannello."""
    ax.text(
        *position,
        formula,
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=font_size("formula"),
        linespacing=line_spacing("formula"),
        bbox=text_bbox(),
        zorder=4,
    )


# ============================================================
# CALCOLI: DUE PARAMETRIZZAZIONI DELLO STESSO PORTAFOGLIO
# ============================================================

liquidity_slope = A_LIQUID - A_ILLIQUID
if liquidity_slope <= 0:
    raise ValueError("A_LIQUID deve essere maggiore di A_ILLIQUID.")
if FUNDING_UNIT_COST <= 0:
    raise ValueError("FUNDING_UNIT_COST deve essere strettamente positivo.")

x_1 = np.linspace(X_MIN, X_MAX, N_GRID)  # investimento nell'attivo liquido
x_2 = np.linspace(X_MIN, X_MAX, N_GRID)  # investimento nell'attivo illiquido

# Caso 1: x_1 cresce verso l'attivo più liquido.
liquidity_x1 = A_LIQUID * x_1 + A_ILLIQUID * (A0 - x_1)
u_star_x1 = np.maximum(0.0, LIQUIDITY_NEED - liquidity_x1)
q_x1 = -FUNDING_UNIT_COST * u_star_x1

# Caso 2: x_2 cresce verso l'attivo meno liquido.
liquidity_x2 = A_LIQUID * (A0 - x_2) + A_ILLIQUID * x_2
u_star_x2 = np.maximum(0.0, LIQUIDITY_NEED - liquidity_x2)
q_x2 = -FUNDING_UNIT_COST * u_star_x2

# Le soglie sono complementari: x_2 = A0 - x_1.
x1_break = (
    LIQUIDITY_NEED - A_ILLIQUID * A0
) / liquidity_slope
x2_break = A0 - x1_break

if not X_MIN <= x1_break <= X_MAX:
    raise ValueError("La soglia in x_1 è esterna al dominio.")
if not X_MIN <= x2_break <= X_MAX:
    raise ValueError("La soglia in x_2 è esterna al dominio.")

# Coefficienti dei due tratti non nulli.
left_intercept = -FUNDING_UNIT_COST * (
    LIQUIDITY_NEED - A_ILLIQUID * A0
)
left_slope = FUNDING_UNIT_COST * liquidity_slope
right_intercept = -left_intercept
right_slope = -left_slope
x1_break_text = format_math_thousands(x1_break)
x2_break_text = format_math_thousands(x2_break)

# Scala verticale comune e automatica, utile anche cambiando il costo unitario.
q_min = min(float(q_x1.min()), float(q_x2.min()))
q_span = max(abs(q_min), 1e-12)
Y_LIMITS = (
    q_min - Y_BOTTOM_MARGIN * q_span,
    Y_TOP_MARGIN * q_span,
)

# ============================================================
# FIGURA
# ============================================================

fig, (ax_left, ax_right) = plt.subplots(
    1,
    2,
    figsize=FIG_SIZE,
    sharey=True,
)

fig.suptitle(
    "Funzione di ricorso: due parametrizzazioni equivalenti",
    fontsize=font_size("suptitle"),
)

configure_panel(
    ax_left,
    "Variabile: investimento\n"
    r"nell'attivo più liquido $x_1$",
    r"Investimento nell'attivo più liquido $x_1$ (mln €)",
    Y_LIMITS,
)
configure_panel(
    ax_right,
    "Variabile: investimento\n"
    r"nell'attivo meno liquido $x_2$",
    r"Investimento nell'attivo meno liquido $x_2$ (mln €)",
    Y_LIMITS,
)

ax_left.set_ylabel(
    "Valore della funzione di ricorso (mln €)",
    fontsize=font_size("axis_label"),
)

# Regioni nelle quali il funding è necessario.
ax_left.axvspan(
    X_MIN,
    x1_break,
    color=COLORS["funding_region"],
    alpha=FUNDING_REGION_ALPHA,
    zorder=0,
)
ax_right.axvspan(
    x2_break,
    X_MAX,
    color=COLORS["funding_region"],
    alpha=FUNDING_REGION_ALPHA,
    zorder=0,
)

# Curve speculari della stessa funzione economica.
ax_left.plot(
    x_1,
    q_x1,
    color=COLORS["recourse"],
    linewidth=RECOURSE_LINEWIDTH,
    zorder=2,
)
ax_right.plot(
    x_2,
    q_x2,
    color=COLORS["recourse"],
    linewidth=RECOURSE_LINEWIDTH,
    zorder=2,
)

for ax, x_break in ((ax_left, x1_break), (ax_right, x2_break)):
    ax.axvline(
        x_break,
        color=COLORS["breakpoint"],
        linewidth=BREAKPOINT_LINEWIDTH,
        linestyle=BREAKPOINT_LINESTYLE,
        zorder=1,
    )
    ax.scatter(
        [x_break],
        [0.0],
        s=MARKER_SIZE,
        color=COLORS["recourse"],
        zorder=3,
    )

# Formule dei due tratti nel pannello x_1.
add_formula(
    ax_left,
    LEFT_LINEAR_FORMULA_AXES,
    affine_formula(left_intercept, left_slope, "x_1"),
)
add_formula(ax_left, LEFT_FLAT_FORMULA_AXES, r"$Q_2(x_1)=0$")

# Formule dei due tratti nel pannello x_2.
add_formula(ax_right, RIGHT_FLAT_FORMULA_AXES, r"$Q_2(x_2)=0$")
add_formula(
    ax_right,
    RIGHT_LINEAR_FORMULA_AXES,
    affine_formula(right_intercept, right_slope, "x_2"),
)

# Le due annotazioni chiariscono il significato opposto del movimento a destra.
ax_left.annotate(
    rf"per $x_1\geq{x1_break_text}$" "\n"
    r"il funding si annulla",
    xy=(x1_break, 0.0),
    xytext=LEFT_ANNOTATION_AXES,
    textcoords="axes fraction",
    ha="left",
    va="center",
    fontsize=font_size("annotation"),
    linespacing=line_spacing("annotation"),
    color=COLORS["annotation"],
    bbox=text_bbox(),
    arrowprops={
        "arrowstyle": "->",
        "color": COLORS["annotation"],
        "linewidth": 1.2,
    },
)
ax_right.annotate(
    rf"per $x_2>{x2_break_text}$" "\n"
    r"il funding diventa necessario",
    xy=(x2_break, 0.0),
    xytext=RIGHT_ANNOTATION_AXES,
    textcoords="axes fraction",
    ha="left",
    va="center",
    fontsize=font_size("annotation"),
    linespacing=line_spacing("annotation"),
    color=COLORS["annotation"],
    bbox=text_bbox(),
    arrowprops={
        "arrowstyle": "->",
        "color": COLORS["annotation"],
        "linewidth": 1.2,
    },
)

fig.text(
    0.50,
    FOOTER_Y,
    r"Unità monetaria: milioni di euro; $A_0=10\,000$ mln €." "\n"
    r"Poiché $x_2=A_0-x_1$, andare a destra in un pannello "
    r"equivale ad andare a sinistra nell'altro.",
    ha="center",
    va="center",
    fontsize=font_size("footer"),
    linespacing=line_spacing("footer"),
)

fig.tight_layout(rect=TIGHT_LAYOUT_RECT)
fig.subplots_adjust(wspace=SUBPLOT_WSPACE)
save_figure(fig, OUTPUT_STEM)
