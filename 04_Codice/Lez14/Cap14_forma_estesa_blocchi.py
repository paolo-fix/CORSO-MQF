from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.path import Path as MplPath
from matplotlib.patches import FancyBboxPatch, PathPatch

# ============================================================
# PERCORSO E PARAMETRI DI SALVATAGGIO
# ============================================================

OUTPUT_DIR = Path(r"E:\Didattica\MQF\graphics")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

PNG_DPI = 300
SAVE_BBOX = "tight"
SAVE_PAD_INCHES = 0.04

# ============================================================
# TIPOGRAFIA: controlli raccolti in un unico punto
# ============================================================

FONT_FAMILY = "DejaVu Sans"
FONT_SCALE = 1.00
LINE_SPACING_SCALE = 1.00

FONT_SIZES = {
    "header": 16.0,
    "math": 17.0,
    "annotation": 14.0,
    "small": 14.0,
    "form_header": 16.0,
    "bottom_note": 15.0,
}

LINE_SPACINGS = {
    "header": 1.00,
    "math": 1.00,
    "annotation": 1.15,
    "small": 1.05,
    "form_header": 1.00,
    "bottom_note": 1.00,
}

plt.rcParams["font.family"] = FONT_FAMILY


def font_size(category):
    """Restituisce il font della categoria, corretto con la scala globale."""
    return FONT_SIZES[category] * FONT_SCALE


def line_spacing(category):
    """Restituisce l'interlinea, corretta con la scala globale."""
    return LINE_SPACINGS[category] * LINE_SPACING_SCALE


# ============================================================
# PARAMETRI GRAFICI MODIFICABILI
# ============================================================

FIG_SIZE = (13.5, 10.0)

BOX_LINEWIDTH = 1.4
BOX_ROUNDING_SIZE = 0.012
SEPARATOR_LINEWIDTH = 1.0
ARROW_LINEWIDTH = 1.5
# 0.000 porta la punta delle frecce esattamente sul bordo dei box.
ARROW_GAP = 0.000

# Blocco del primo stadio.
FIRST_CENTER = (0.17, 0.66)
FIRST_WIDTH = 0.22
FIRST_HEIGHT = 0.16
FIRST_NOTE_Y = 0.535

# Blocchi di scenario.
SCENARIO_X = 0.65
SCENARIO_YS = [0.86, 0.66, 0.40]
SCENARIO_WIDTH = 0.25
SCENARIO_HEIGHT = 0.17
SCENARIO_ELLIPSIS_Y = 0.525

# Punto comune dal quale si diramano le frecce.
BRANCH_POINT = (0.33, FIRST_CENTER[1])

# Parentesi e annotazione dei vincoli replicati.
BRACE_X = 0.815
BRACE_WIDTH = 0.012
BRACE_TOP = SCENARIO_YS[0] + SCENARIO_HEIGHT / 2
BRACE_BOTTOM = SCENARIO_YS[-1] - SCENARIO_HEIGHT / 2
BRACE_TEXT_X = 0.91

# Blocco della forma estesa.
FORM_CENTER = (0.50, 0.205)
FORM_WIDTH = 0.90
FORM_HEIGHT = 0.15
FORM_DIVIDER_X = 0.255
FORM_OBJECTIVE_OFFSET_Y = 0.035
FORM_CONSTRAINT_OFFSET_Y = -0.030

# Richiamo finale sulla non anticipatività.
BOTTOM_CENTER = (FORM_CENTER[0], 0.040)
BOTTOM_WIDTH = 0.72
BOTTOM_HEIGHT = 0.070


# ============================================================
# FUNZIONI GRAFICHE
# ============================================================

def add_box(ax, center, width, height, linewidth=BOX_LINEWIDTH):
    """Disegna un box arrotondato e restituisce la patch creata."""
    x, y = center
    patch = FancyBboxPatch(
        (x - width / 2, y - height / 2),
        width,
        height,
        # pad=0 mantiene esatte le dimensioni geometriche dichiarate:
        # le frecce possono quindi terminare precisamente sul bordo.
        boxstyle=f"round,pad=0,rounding_size={BOX_ROUNDING_SIZE}",
        linewidth=linewidth,
        facecolor="white",
        edgecolor="black",
    )
    ax.add_patch(patch)
    return patch


def add_arrow(ax, start, end, linewidth=ARROW_LINEWIDTH):
    """Disegna una freccia fra due punti espressi in coordinate degli assi."""
    ax.annotate(
        "",
        xy=end,
        xytext=start,
        arrowprops={"arrowstyle": "->", "linewidth": linewidth},
    )


def add_right_brace(ax, x, y_top, y_bottom, width, linewidth=1.3):
    """Disegna una parentesi graffa destra verticale mediante curve di Bézier."""
    y_mid = (y_top + y_bottom) / 2
    curve = min(0.055, (y_top - y_bottom) / 7)

    vertices = [
        (x - width, y_top),
        (x, y_top), (x, y_top), (x, y_top - curve),
        (x, y_mid + curve), (x, y_mid + curve), (x + width, y_mid),
        (x, y_mid - curve), (x, y_mid - curve), (x, y_bottom + curve),
        (x, y_bottom), (x, y_bottom), (x - width, y_bottom),
    ]
    codes = [MplPath.MOVETO] + [MplPath.CURVE4] * 12
    brace = PathPatch(
        MplPath(vertices, codes),
        fill=False,
        edgecolor="black",
        linewidth=linewidth,
        capstyle="round",
        joinstyle="round",
    )
    ax.add_patch(brace)


# ============================================================
# FIGURA 14.4 — forma estesa e struttura a blocchi
# ============================================================

fig, ax = plt.subplots(figsize=FIG_SIZE)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

# Primo stadio: intestazione, separatore e variabile comune.
add_box(ax, FIRST_CENTER, FIRST_WIDTH, FIRST_HEIGHT)
first_top = FIRST_CENTER[1] + FIRST_HEIGHT / 2
first_separator_y = first_top - 0.043

ax.text(
    FIRST_CENTER[0], first_top - 0.022, "primo stadio",
    ha="center", va="center",
    fontsize=font_size("header"),
    fontweight="bold",
    linespacing=line_spacing("header"),
)
ax.plot(
    [FIRST_CENTER[0] - FIRST_WIDTH / 2 + 0.010,
     FIRST_CENTER[0] + FIRST_WIDTH / 2 - 0.010],
    [first_separator_y, first_separator_y],
    color="black",
    linewidth=SEPARATOR_LINEWIDTH,
)
ax.text(
    FIRST_CENTER[0], FIRST_CENTER[1] - 0.022, r"$x$",
    ha="center", va="center",
    fontsize=font_size("math") + 7,
    linespacing=line_spacing("math"),
)
ax.text(
    FIRST_CENTER[0], FIRST_NOTE_Y,
    "decisione comune\na tutti gli scenari",
    ha="center", va="center",
    fontsize=font_size("annotation"),
    linespacing=line_spacing("annotation"),
)

# Collegamento dal primo stadio al punto di diramazione.
first_right = FIRST_CENTER[0] + FIRST_WIDTH / 2 + ARROW_GAP
ax.plot(
    [first_right, BRANCH_POINT[0]],
    [FIRST_CENTER[1], BRANCH_POINT[1]],
    color="black",
    linewidth=ARROW_LINEWIDTH,
)

# Blocchi dei vincoli di secondo stadio.
scenario_specs = [
    ("scenario 1", r"$y_1$", r"$T_1x+W_1y_1=h_1$", r"$y_1\in\mathcal{X}_1$"),
    ("scenario 2", r"$y_2$", r"$T_2x+W_2y_2=h_2$", r"$y_2\in\mathcal{X}_2$"),
    ("scenario $N$", r"$y_N$", r"$T_Nx+W_Ny_N=h_N$", r"$y_N\in\mathcal{X}_N$"),
]

for y, (title, y_label, constraint, admissible) in zip(
    SCENARIO_YS,
    scenario_specs,
):
    center = (SCENARIO_X, y)
    add_box(ax, center, SCENARIO_WIDTH, SCENARIO_HEIGHT)

    top = y + SCENARIO_HEIGHT / 2
    separator_y = top - 0.043
    ax.text(
        SCENARIO_X, top - 0.022, title,
        ha="center", va="center",
        fontsize=font_size("header"),
        fontweight="bold",
        linespacing=line_spacing("header"),
    )
    ax.plot(
        [SCENARIO_X - SCENARIO_WIDTH / 2 + 0.010,
         SCENARIO_X + SCENARIO_WIDTH / 2 - 0.010],
        [separator_y, separator_y],
        color="black",
        linewidth=SEPARATOR_LINEWIDTH,
    )
    ax.text(
        SCENARIO_X, y + 0.012, y_label,
        ha="center", va="center",
        fontsize=font_size("math"),
        linespacing=line_spacing("math"),
    )
    ax.text(
        SCENARIO_X, y - 0.025, constraint,
        ha="center", va="center",
        fontsize=font_size("math"),
        linespacing=line_spacing("math"),
    )
    ax.text(
        SCENARIO_X, y - 0.060, admissible,
        ha="center", va="center",
        fontsize=font_size("small"),
        linespacing=line_spacing("small"),
    )

    scenario_left = SCENARIO_X - SCENARIO_WIDTH / 2 - ARROW_GAP
    add_arrow(ax, BRANCH_POINT, (scenario_left, y))

# Scenari intermedi omessi.
ax.text(
    SCENARIO_X, SCENARIO_ELLIPSIS_Y, r"$\vdots$",
    ha="center", va="center",
    fontsize=font_size("math") + 7,
)

# Parentesi che raccoglie i vincoli replicati.
add_right_brace(
    ax,
    BRACE_X,
    BRACE_TOP,
    BRACE_BOTTOM,
    BRACE_WIDTH,
)
ax.text(
    BRACE_TEXT_X, (BRACE_TOP + BRACE_BOTTOM) / 2,
    "vincoli di\nsecondo stadio\nreplicati per\nscenario",
    ha="center", va="center",
    fontsize=font_size("annotation"),
    linespacing=line_spacing("annotation"),
)

# Forma estesa: un solo x e un blocco di vincoli per ogni scenario.
add_box(ax, FORM_CENTER, FORM_WIDTH, FORM_HEIGHT)
form_left = FORM_CENTER[0] - FORM_WIDTH / 2
form_right = FORM_CENTER[0] + FORM_WIDTH / 2
form_bottom = FORM_CENTER[1] - FORM_HEIGHT / 2
form_top = FORM_CENTER[1] + FORM_HEIGHT / 2

ax.plot(
    [FORM_DIVIDER_X, FORM_DIVIDER_X],
    [form_bottom + 0.012, form_top - 0.012],
    color="black",
    linewidth=SEPARATOR_LINEWIDTH,
)
ax.text(
    (form_left + FORM_DIVIDER_X) / 2,
    FORM_CENTER[1],
    "forma estesa",
    ha="center", va="center",
    fontsize=font_size("form_header"),
    fontweight="bold",
    linespacing=line_spacing("form_header"),
)
ax.text(
    (FORM_DIVIDER_X + form_right) / 2,
    FORM_CENTER[1] + FORM_OBJECTIVE_OFFSET_Y,
    r"$\max\quad c^{\prime}x+\sum_{s\in\mathcal{S}}p_s q_s^{\prime}y_s$",
    ha="center", va="center",
    fontsize=font_size("math") + 2,
    linespacing=line_spacing("math"),
)
ax.text(
    (FORM_DIVIDER_X + form_right) / 2,
    FORM_CENTER[1] + FORM_CONSTRAINT_OFFSET_Y,
    r"$x\in\mathcal{X},\quad T_sx+W_sy_s=h_s,\quad "
    r"y_s\in\mathcal{X}_s,\quad s\in\mathcal{S}$",
    ha="center", va="center",
    fontsize=font_size("math"),
    linespacing=line_spacing("math"),
)

# Richiamo finale collegato al blocco della forma estesa.
add_box(ax, BOTTOM_CENTER, BOTTOM_WIDTH, BOTTOM_HEIGHT)
add_arrow(
    ax,
    (FORM_CENTER[0], form_bottom - ARROW_GAP),
    (
        BOTTOM_CENTER[0],
        BOTTOM_CENTER[1] + BOTTOM_HEIGHT / 2 + ARROW_GAP,
    ),
)
ax.text(
    BOTTOM_CENTER[0], BOTTOM_CENTER[1],
    r"$\mathbf{Non\ anticipatività:}$ "
    r"$x$ è unico, mentre $y_s$ dipende dallo scenario.",
    ha="center", va="center",
    fontsize=font_size("bottom_note"),
    linespacing=line_spacing("bottom_note"),
)

# ============================================================
# SALVATAGGIO PNG + SVG
# ============================================================

stem = "Cap14_forma_estesa_blocchi_b"
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
