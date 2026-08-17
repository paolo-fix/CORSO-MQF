from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

# ============================================================
# PERCORSI DI OUTPUT
# ============================================================

OUTPUT_DIR = Path(r"E:\Didattica\MQF\graphics")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

png_path = OUTPUT_DIR / "Cap12_bilancio_intertemporale.png"
svg_path = OUTPUT_DIR / "Cap12_bilancio_intertemporale.svg"

# ============================================================
# TIPOGRAFIA: tutti i controlli sono raccolti qui
# ============================================================

FONT_FAMILY = "DejaVu Sans"  # Carattere usato in tutta la figura.

# Moltiplicatori globali: 1.10 aumenta tutto del 10%; 0.90 riduce del 10%.
FONT_SCALE = 1.00
LINE_SPACING_SCALE = 1.00

# Dimensioni dei caratteri per categoria.
FONT_SIZES: dict[str, float] = {
    "box_title": 20.0,
    "formula": 18,
    "transfer_formula": 16,
    "transfer_note": 16,
}

# Interlinea per categoria.
LINE_SPACINGS: dict[str, float] = {
    "box_title": 1.00,
    "formula": 1.30,
    "transfer_formula": 1.00,
    "transfer_note": 1.00,
}

plt.rcParams["font.family"] = FONT_FAMILY


def font_size(category: str) -> float:
    """Restituisce il font della categoria, corretto con la scala globale."""
    return FONT_SIZES[category] * FONT_SCALE


def line_spacing(category: str) -> float:
    """Restituisce l'interlinea, corretta con la scala globale."""
    return LINE_SPACINGS[category] * LINE_SPACING_SCALE


# ============================================================
# GEOMETRIA E STILE: parametri modificabili
# ============================================================

FIGSIZE = (13.2, 4.4)  # Dimensioni della figura in pollici.
AXIS_X_MAX = 13.2      # Estremo destro delle coordinate interne.
AXIS_Y_MAX = 4.4       # Estremo superiore delle coordinate interne.

LEFT_BOX_X = 0.32      # Posizione orizzontale del bilancio alla data t.
RIGHT_BOX_X = 7.73     # Posizione orizzontale del bilancio alla data t+1.
BOX_Y = 0.40           # Posizione verticale comune alle due caselle.
BOX_WIDTH = 4.5       # Larghezza delle caselle.
BOX_HEIGHT = 3.58      # Altezza delle caselle.
BOX_LINEWIDTH = 1.35   # Spessore dei bordi.
BOX_ROUNDING = 0.08    # Arrotondamento degli angoli.

BOX_TITLE_Y_OFFSET = 3.05  # Distanza del titolo dalla base della casella.
BOX_FORMULA_Y_OFFSET = 1.52  # Distanza delle formule dalla base della casella.

ARROW_START_X = LEFT_BOX_X + BOX_WIDTH + 0.14  # Inizio delle frecce.
ARROW_END_X = RIGHT_BOX_X - 0.14                # Fine delle frecce.
ARROW_LINEWIDTH = 1.35                          # Spessore delle frecce.
ARROW_MUTATION_SCALE = 15                       # Dimensione della punta.

UPPER_ARROW_Y = 2.78  # Collegamento relativo alla giacenza.
LOWER_ARROW_Y = 1.37  # Collegamento relativo al funding.
TRANSFER_FORMULA_OFFSET = 0.22  # Formula sopra ciascuna freccia.
TRANSFER_NOTE_OFFSET = -0.22    # Descrizione sotto ciascuna freccia.

TEXT_COLOR = "#111111"       # Colore dei testi principali.
SECONDARY_COLOR = "#303030"  # Colore delle descrizioni.
LINE_COLOR = "#111111"       # Colore di caselle e frecce.

# ============================================================
# TESTI DELLA FIGURA
# ============================================================

LEFT_TITLE = r"Bilancio alla data $t$"
RIGHT_TITLE = r"Bilancio alla data $t+1$"

LEFT_FORMULA = (
    r"$\sum_{j=1}^{n} a_{tj}x_j+(1+r_{t-1})g_{t-1}+u_t$"
    "\n"
    r"$=d_t+(1+\rho_{t-1})u_{t-1}+g_t$"
)

RIGHT_FORMULA = (
    r"$\sum_{j=1}^{n} a_{t+1,j}x_j+(1+r_t)g_t+u_{t+1}$"
    "\n"
    r"$=d_{t+1}+(1+\rho_t)u_t+g_{t+1}$"
)

# ============================================================
# FUNZIONI DI SUPPORTO
# ============================================================


def add_balance_box(x: float, title: str, formula: str) -> None:
    """Disegna una casella con il titolo e il bilancio di una data."""
    box = FancyBboxPatch(
        (x, BOX_Y),
        BOX_WIDTH,
        BOX_HEIGHT,
        boxstyle=f"round,pad=0.02,rounding_size={BOX_ROUNDING}",
        fill=False,
        edgecolor=LINE_COLOR,
        linewidth=BOX_LINEWIDTH,
    )
    ax.add_patch(box)

    ax.text(
        x + BOX_WIDTH / 2,
        BOX_Y + BOX_TITLE_Y_OFFSET,
        title,
        ha="center",
        va="center",
        fontsize=font_size("box_title"),
        linespacing=line_spacing("box_title"),
        fontweight="bold",
        color=TEXT_COLOR,
    )

    ax.text(
        x + BOX_WIDTH / 2,
        BOX_Y + BOX_FORMULA_Y_OFFSET,
        formula,
        ha="center",
        va="center",
        fontsize=font_size("formula"),
        linespacing=line_spacing("formula"),
        color=TEXT_COLOR,
    )


def add_transfer(y: float, formula: str, note: str) -> None:
    """Disegna una freccia e ne indica trasformazione e significato."""
    arrow = FancyArrowPatch(
        (ARROW_START_X, y),
        (ARROW_END_X, y),
        arrowstyle="->",
        mutation_scale=ARROW_MUTATION_SCALE,
        linewidth=ARROW_LINEWIDTH,
        color=LINE_COLOR,
    )
    ax.add_patch(arrow)

    center_x = (ARROW_START_X + ARROW_END_X) / 2
    ax.text(
        center_x,
        y + TRANSFER_FORMULA_OFFSET,
        formula,
        ha="center",
        va="center",
        fontsize=font_size("transfer_formula"),
        linespacing=line_spacing("transfer_formula"),
        color=TEXT_COLOR,
    )
    ax.text(
        center_x,
        y + TRANSFER_NOTE_OFFSET,
        note,
        ha="center",
        va="center",
        fontsize=font_size("transfer_note"),
        linespacing=line_spacing("transfer_note"),
        color=SECONDARY_COLOR,
    )


# ============================================================
# COSTRUZIONE DELLA FIGURA
# ============================================================

fig, ax = plt.subplots(figsize=FIGSIZE)
ax.set_xlim(0, AXIS_X_MAX)
ax.set_ylim(0, AXIS_Y_MAX)
ax.axis("off")

add_balance_box(LEFT_BOX_X, LEFT_TITLE, LEFT_FORMULA)
add_balance_box(RIGHT_BOX_X, RIGHT_TITLE, RIGHT_FORMULA)

add_transfer(
    UPPER_ARROW_Y,
    r"$g_t \mapsto (1+r_t)g_t$",
    "risorsa futura",
)
add_transfer(
    LOWER_ARROW_Y,
    r"$u_t \mapsto (1+\rho_t)u_t$",
    "obbligo futuro",
)

fig.tight_layout(pad=0.15)

fig.savefig(png_path, dpi=300, bbox_inches="tight")
fig.savefig(svg_path, bbox_inches="tight")

plt.close(fig)

print(f"Figura PNG salvata in: {png_path}")
print(f"Figura SVG salvata in: {svg_path}")
