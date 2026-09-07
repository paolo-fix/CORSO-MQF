from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# ============================================================
# PERCORSI DI OUTPUT
# ============================================================

# Cartella graphics del progetto.
out_dir = Path(r"E:\Didattica\MQF\graphics")
out_dir.mkdir(parents=True, exist_ok=True)

png_path = out_dir / "cap11_corrispondenza_primale_duale.png"
svg_path = out_dir / "cap11_corrispondenza_primale_duale.svg"

# ============================================================
# TIPOGRAFIA: tutti i controlli sono raccolti qui
# ============================================================

FONT_FAMILY = "DejaVu Sans"  # Carattere usato in tutta la figura.

# Moltiplicatori globali: 1.10 aumenta tutto del 10%; 0.90 riduce del 10%.
FONT_SCALE = 1.00
LINE_SPACING_SCALE = 1.00

# Dimensioni dei caratteri per categoria.
FONT_SIZES: dict[str, float] = {
    "title": 19.0,
    "box_header": 16.0,
    "formula": 17.0,
    "central_label": 17.0,
    "row_label": 15.0,
}

# Interlinea per categoria.
LINE_SPACINGS: dict[str, float] = {
    "title": 1.00,
    "box_header": 1.00,
    "formula": 1.00,
    "central_label": 1.00,
    "row_label": 1.00,
}

plt.rcParams["font.family"] = FONT_FAMILY


def font_size(category: str) -> float:
    """Restituisce il font della categoria, corretto con la scala globale."""
    return FONT_SIZES[category] * FONT_SCALE


def line_spacing(category: str) -> float:
    """Restituisce l'interlinea, corretta con la scala globale."""
    return LINE_SPACINGS[category] * LINE_SPACING_SCALE


# ============================================================
# DIMENSIONI, POSIZIONI E STILE
# ============================================================

FIGSIZE = (11.5, 4.2)  # Dimensioni della figura in pollici.
AXIS_X_LIMITS = (0.0, 1.0)
AXIS_Y_LIMITS = (0.0, 1.0)

TITLE_X = 0.50  # Posizione orizzontale del titolo.
TITLE_Y = 0.94  # Posizione verticale del titolo.

LEFT_BOX_X = 0.06   # Posizione orizzontale del box primale.
RIGHT_BOX_X = 0.60  # Posizione orizzontale del box duale.
BOX_Y = 0.10        # Posizione verticale comune ai due box.
BOX_WIDTH = 0.34    # Larghezza dei box.
BOX_HEIGHT = 0.74   # Altezza dei box.
BOX_LINEWIDTH = 1.2
BOX_ROUNDING = 0.02

BOX_HEADER_Y = 0.78       # Altezza delle intestazioni dei box.
OBJECTIVE_Y = 0.67        # Altezza delle funzioni obiettivo.
CONSTRAINTS_Y = 0.59      # Altezza dei vincoli.
CENTRAL_LABEL_Y = 0.52    # Altezza della corrispondenza A ↔ A'.
ROW_Y_POSITIONS = (0.43, 0.35, 0.27, 0.19)

ARROW_START_X = 0.44      # Inizio delle frecce di corrispondenza.
ARROW_END_X = 0.56        # Fine delle frecce di corrispondenza.
ARROW_LINEWIDTH = 1.2
ARROW_MUTATION_SCALE = 15

TEXT_COLOR = "#111111"  # Colore di testi e formule.
LINE_COLOR = "#111111"  # Colore di box e frecce.

# Margini della figura espressi come frazioni di larghezza e altezza.
SUBPLOT_LEFT = 0.03
SUBPLOT_RIGHT = 0.97
SUBPLOT_BOTTOM = -0.03
SUBPLOT_TOP = 0.97

# True apre anche la finestra interattiva; False salva e chiude la figura.
SHOW_FIGURE = False

# ============================================================
# CONTENUTI DELLE CORRISPONDENZE
# ============================================================

ROWS = (
    (r"$m$ vincoli", r"$m$ variabili duali"),
    (r"$n$ variabili", r"$n$ vincoli duali"),
    (r"$b$: termini noti", r"$b$: coefficienti dell'obiettivo"),
    (r"$c$: coefficienti dell'obiettivo", r"$c$: termini noti"),
)

# ============================================================
# FUNZIONI DI SUPPORTO
# ============================================================


def add_box(x: float) -> None:
    """Disegna uno dei due box principali."""
    box = FancyBboxPatch(
        (x, BOX_Y),
        BOX_WIDTH,
        BOX_HEIGHT,
        boxstyle=f"round,pad=0.02,rounding_size={BOX_ROUNDING}",
        linewidth=BOX_LINEWIDTH,
        edgecolor=LINE_COLOR,
        fill=False,
    )
    ax.add_patch(box)


def add_centered_text(
    x: float,
    y: float,
    text: str,
    category: str,
    *,
    bold: bool = False,
) -> None:
    """Aggiunge testo centrato usando una categoria tipografica."""
    ax.text(
        x,
        y,
        text,
        ha="center",
        va="center",
        fontsize=font_size(category),
        linespacing=line_spacing(category),
        fontweight="bold" if bold else "normal",
        color=TEXT_COLOR,
    )


# ============================================================
# COSTRUZIONE DELLA FIGURA
# ============================================================

fig, ax = plt.subplots(figsize=FIGSIZE)
ax.set_xlim(*AXIS_X_LIMITS)
ax.set_ylim(*AXIS_Y_LIMITS)
ax.axis("off")

left_center_x = LEFT_BOX_X + BOX_WIDTH / 2
right_center_x = RIGHT_BOX_X + BOX_WIDTH / 2

add_centered_text(
    TITLE_X,
    TITLE_Y,
    "Corrispondenza tra problema primale e problema duale",
    "title",
    bold=True,
)

add_box(LEFT_BOX_X)
add_box(RIGHT_BOX_X)

add_centered_text(left_center_x, BOX_HEADER_Y, "PROBLEMA PRIMALE", "box_header", bold=True)
add_centered_text(right_center_x, BOX_HEADER_Y, "PROBLEMA DUALE", "box_header", bold=True)

add_centered_text(left_center_x, OBJECTIVE_Y, r"$\min\; c'x$", "formula")
add_centered_text(left_center_x, CONSTRAINTS_Y, r"$Ax\geq b,\qquad x\geq 0$", "formula")
add_centered_text(right_center_x, OBJECTIVE_Y, r"$\max\; b'\lambda$", "formula")
add_centered_text(
    right_center_x,
    CONSTRAINTS_Y,
    r"$A'\lambda\leq c,\qquad \lambda\geq 0$",
    "formula",
)

add_centered_text(TITLE_X, CENTRAL_LABEL_Y, r"$A \longleftrightarrow A'$", "central_label")

for y, (left_text, right_text) in zip(ROW_Y_POSITIONS, ROWS):
    add_centered_text(left_center_x, y, left_text, "row_label")
    add_centered_text(right_center_x, y, right_text, "row_label")

    arrow = FancyArrowPatch(
        (ARROW_START_X, y),
        (ARROW_END_X, y),
        arrowstyle="<->",
        mutation_scale=ARROW_MUTATION_SCALE,
        linewidth=ARROW_LINEWIDTH,
        color=LINE_COLOR,
    )
    ax.add_patch(arrow)

fig.subplots_adjust(
    left=SUBPLOT_LEFT,
    right=SUBPLOT_RIGHT,
    bottom=SUBPLOT_BOTTOM,
    top=SUBPLOT_TOP,
)
fig.savefig(png_path, dpi=300, bbox_inches="tight")
fig.savefig(svg_path, bbox_inches="tight")

if SHOW_FIGURE:
    plt.show()
else:
    plt.close(fig)

print(f"Figura PNG salvata in: {png_path}")
print(f"Figura SVG salvata in: {svg_path}")
