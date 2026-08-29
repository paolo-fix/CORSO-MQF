from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# ============================================================
# PERCORSO E PARAMETRI DI SALVATAGGIO
# ============================================================

# Destinazione indipendente dalla cartella dalla quale si esegue lo script.
OUTPUT_DIR = Path(r"E:\Didattica\MQF\graphics")
OUTPUT_STEM = "Cap15_fattibilita_ricorso"

PNG_DPI = 300
SAVE_BBOX = "tight"
SAVE_PAD_INCHES = 0.04

# ============================================================
# DATI DEL PROBLEMA: controlli economici
# ============================================================

# Risorse iniziali e fabbisogno di liquidità.
A0 = 10.0
D = 8.0

# Cash flow unitari dei due attivi nei due scenari:
# attivo 1 più liquido; attivo 2 meno liquido.
A11, A12 = 1.0, 0.6   # scenario ordinario
A21, A22 = 1.0, 0.2   # scenario avverso

# Capacità massima di funding nei due scenari.
U_BAR_1 = 1.0
U_BAR_2 = 2.0

# Dominio e precisione della griglia per la decisione x.
X_MIN = 0.0
X_MAX = A0
N_GRID = 501

# ============================================================
# TIPOGRAFIA: tutti i controlli sono raccolti qui
# ============================================================

FONT_FAMILY = "DejaVu Sans"
FONT_SCALE = 1.00
LINE_SPACING_SCALE = 1.00

FONT_SIZES = {
    "title": 19.0,
    "axis_label": 15.0,
    "tick_label": 14.0,
    "legend": 13,
    "threshold_label": 13,
    "annotation": 14,
}

LINE_SPACINGS = {
    "title": 1.00,
    "axis_label": 1.00,
    "tick_label": 1.00,
    "legend": 1.05,
    "threshold_label": 1.05,
    "annotation": 1.15,
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

FIG_SIZE = (9.8, 6.2)
X_LIMITS = (X_MIN, X_MAX)
Y_LIMITS = (0.0, 6.1)

COLORS = {
    "scenario_1": "#4C78A8",
    "scenario_2": "#D95F02",
    "capacity_1": "#72A6C9",
    "capacity_2": "#E39A63",
    "feasible": "#2F6B4F",
}

MIN_FUNDING_LINEWIDTH = 2.2
CAPACITY_LINEWIDTH = 1.8
CAPACITY_LINESTYLE = "--"
THRESHOLD_LINEWIDTH = 1.3
THRESHOLD_LINESTYLE = ":"

GRID_VISIBLE = True
GRID_ALPHA = 0.28
GRID_LINESTYLE = "--"

LEGEND_LOC = "upper right"
LEGEND_NCOL = 1
LEGEND_FRAMEON = True
LEGEND_FRAMEALPHA = 0.92
LEGEND_HANDLELENGTH = 2.2
LEGEND_BORDERPAD = 0.55
LEGEND_LABELSPACING = 0.50

# Posizione delle annotazioni in coordinate dei dati.
THRESHOLD_LABEL_X_OFFSET = 0.12
THRESHOLD_LABEL_TOP_Y = 5.55
FEASIBLE_NOTE_X = 7.25
FEASIBLE_NOTE_Y = 3.35

# Margini di tight_layout: sinistra, basso, destra, alto.
TIGHT_LAYOUT_RECT = (0.00, 0.00, 1.00, 1.00)


# ============================================================
# FUNZIONI DI CALCOLO E SALVATAGGIO
# ============================================================

def feasibility_threshold(a_liquid, a_illiquid, funding_capacity):
    """Calcola la minima quota x che rende ammissibile il recourse."""
    slope = a_liquid - a_illiquid
    if slope <= 0:
        raise ValueError(
            "Il cash flow dell'attivo 1 deve superare quello dell'attivo 2."
        )

    threshold = (
        D - funding_capacity - a_illiquid * A0
    ) / slope
    return float(np.clip(threshold, X_MIN, X_MAX))


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


# ============================================================
# CALCOLI
# ============================================================

x = np.linspace(X_MIN, X_MAX, N_GRID)
x_2 = A0 - x

liquidity_1 = A11 * x + A12 * x_2
liquidity_2 = A21 * x + A22 * x_2

u_min_1 = np.maximum(0.0, D - liquidity_1)
u_min_2 = np.maximum(0.0, D - liquidity_2)

# Le soglie sono ricavate dai dati e si aggiornano automaticamente.
x_feas_1 = feasibility_threshold(A11, A12, U_BAR_1)
x_feas_2 = feasibility_threshold(A21, A22, U_BAR_2)
x_feas_all = max(x_feas_1, x_feas_2)

# ============================================================
# FIGURA
# ============================================================

fig, ax = plt.subplots(figsize=FIG_SIZE)

ax.plot(
    x,
    u_min_1,
    color=COLORS["scenario_1"],
    linewidth=MIN_FUNDING_LINEWIDTH,
    label=r"$u_1^{\min}(x)$: scenario ordinario",
)
ax.plot(
    x,
    u_min_2,
    color=COLORS["scenario_2"],
    linewidth=MIN_FUNDING_LINEWIDTH,
    label=r"$u_2^{\min}(x)$: scenario avverso",
)
ax.axhline(
    U_BAR_1,
    color=COLORS["capacity_1"],
    linewidth=CAPACITY_LINEWIDTH,
    linestyle=CAPACITY_LINESTYLE,
    label=rf"$\bar u_1={U_BAR_1:g}$",
)
ax.axhline(
    U_BAR_2,
    color=COLORS["capacity_2"],
    linewidth=CAPACITY_LINEWIDTH,
    linestyle=CAPACITY_LINESTYLE,
    label=rf"$\bar u_2={U_BAR_2:g}$",
)

ax.axvline(
    x_feas_1,
    color=COLORS["scenario_1"],
    linewidth=THRESHOLD_LINEWIDTH,
    linestyle=THRESHOLD_LINESTYLE,
)
ax.axvline(
    x_feas_2,
    color=COLORS["scenario_2"],
    linewidth=THRESHOLD_LINEWIDTH,
    linestyle=THRESHOLD_LINESTYLE,
)

ax.text(
    x_feas_1 + THRESHOLD_LABEL_X_OFFSET,
    THRESHOLD_LABEL_TOP_Y,
    rf"$x={x_feas_1:g}$: fattibilità nello scenario 1",
    rotation=90,
    ha="left",
    va="top",
    fontsize=font_size("threshold_label"),
    linespacing=line_spacing("threshold_label"),
    color=COLORS["scenario_1"],
)
ax.text(
    x_feas_2 + THRESHOLD_LABEL_X_OFFSET,
    THRESHOLD_LABEL_TOP_Y,
    rf"$x={x_feas_2:g}$: fattibilità in tutti gli scenari",
    rotation=90,
    ha="left",
    va="top",
    fontsize=font_size("threshold_label"),
    linespacing=line_spacing("threshold_label"),
    color=COLORS["scenario_2"],
)

ax.text(
    FEASIBLE_NOTE_X,
    FEASIBLE_NOTE_Y,
    "Recourse ammissibile in entrambi gli scenari\n"
    rf"per $x\geq {x_feas_all:g}$",
    ha="center",
    va="center",
    fontsize=font_size("annotation"),
    linespacing=line_spacing("annotation"),
    color=COLORS["feasible"],
)

ax.set_xlim(*X_LIMITS)
ax.set_ylim(*Y_LIMITS)
ax.set_xlabel(
    r"Allocazione iniziale nell'attivo più liquido $x$",
    fontsize=font_size("axis_label"),
)
ax.set_ylabel(
    "Funding minimo richiesto",
    fontsize=font_size("axis_label"),
)
ax.set_title(
    "Fattibilità del recourse e capacità massima di funding",
    fontsize=font_size("title"),
)
ax.tick_params(axis="both", labelsize=font_size("tick_label"))

ax.legend(
    loc=LEGEND_LOC,
    ncol=LEGEND_NCOL,
    frameon=LEGEND_FRAMEON,
    framealpha=LEGEND_FRAMEALPHA,
    fontsize=font_size("legend"),
    handlelength=LEGEND_HANDLELENGTH,
    borderpad=LEGEND_BORDERPAD,
    labelspacing=LEGEND_LABELSPACING,
)
ax.grid(
    GRID_VISIBLE,
    alpha=GRID_ALPHA,
    linestyle=GRID_LINESTYLE,
)

fig.tight_layout(rect=TIGHT_LAYOUT_RECT)
save_figure(fig, OUTPUT_STEM)
