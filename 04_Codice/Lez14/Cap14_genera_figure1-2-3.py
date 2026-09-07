from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch

# ============================================================
# PERCORSO E PARAMETRI DI SALVATAGGIO
# ============================================================

# La destinazione non dipende dalla cartella dalla quale si esegue lo script.
OUTPUT_DIR = Path(r"E:\Didattica\MQF\graphics")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

PNG_DPI = 300
SAVE_BBOX = "tight"
SAVE_PAD_INCHES = 0.04

# ============================================================
# TIPOGRAFIA: tutti i controlli sono raccolti qui
# ============================================================

FONT_FAMILY = "DejaVu Sans"

# Moltiplicatori globali: 1.10 aumenta tutto del 10%; 0.90 riduce del 10%.
FONT_SCALE = 1.00
LINE_SPACING_SCALE = 1.00

FONT_SIZES: dict[str, float] = {
    "time_label": 19.0,
    "node_label": 16.0,
    "probability_label": 16.0,
    "stage_label": 14.5,
    "annotation": 15.0,
    "two_stage_note": 14.0,
    "math": 16.0,
}

LINE_SPACINGS: dict[str, float] = {
    "time_label": 1.00,
    "node_label": 1.00,
    "probability_label": 1.00,
    "stage_label": 1.00,
    "annotation": 1.00,
    "two_stage_note": 1.15,
    "math": 1.00,
}

plt.rcParams["font.family"] = FONT_FAMILY


def font_size(category: str) -> float:
    """Restituisce il font della categoria, corretto con la scala globale."""
    return FONT_SIZES[category] * FONT_SCALE


def line_spacing(category: str) -> float:
    """Restituisce l'interlinea, corretta con la scala globale."""
    return LINE_SPACINGS[category] * LINE_SPACING_SCALE


# ============================================================
# PARAMETRI GRAFICI MODIFICABILI
# ============================================================

# Colori:
# nessun colore specifico viene imposto; si usano i default Matplotlib.
COLORS = {}

FIG_SIZES = {
    "fig14_1": (10.0, 4.6),
    "fig14_2": (9.5, 5.4),
    "fig14_3": (12.5, 7.5),
}

POS14_1 = {
    "x": (0.16, 0.50),
    "xi": (0.50, 0.50),
    "y": (0.84, 0.50),
}

# Controlli specifici della figura 14.1.
FIG14_1_BOX_WIDTHS = {
    "x": 0.20,
    "xi": 0.20,
    "y": 0.23,
}
FIG14_1_BOX_HEIGHT = 0.16
FIG14_1_HEADER_Y = 0.76
FIG14_1_NOTE_Y = 0.18
FIG14_1_ARROW_GAP = 0.012

POS14_2 = {
    "root": (0.16, 0.50),
    "leaves_x": 0.78,
    "leaves_y": [0.80, 0.62, 0.38, 0.20],
}

# Controlli specifici della figura 14.2.
FIG14_2_ROOT_WIDTH = 0.20
FIG14_2_ROOT_HEIGHT = 0.13
FIG14_2_LEAF_WIDTH = 0.15
FIG14_2_LEAF_HEIGHT = 0.11
FIG14_2_ARROW_GAP = 0.010
# Posizione della probabilità lungo la freccia: 0 = origine, 1 = destinazione.
FIG14_2_LABEL_FRACTION = 0.52

# Aspetto del fondo applicato alle probabilità p_s.
# Il padding è proporzionale alla dimensione del font:
# 0.10 = stretto, 0.20 = medio, 0.30 = ampio.
FIG14_2_LABEL_PADDING = 0.28
FIG14_2_LABEL_FACE_COLOR = "white"
FIG14_2_LABEL_EDGE_COLOR = "none"
FIG14_2_LABEL_BOX_STYLE = "square"

FIG14_2_FORMULA_Y = 0.07

# Controlli delle probabilità sulla traiettoria evidenziata (figura 14.3).
FIG14_3_PATH_LABEL_OFFSET_Y = 0.025
FIG14_3_PATH_LABEL_PADDING = 0.24
FIG14_3_PATH_LABEL_FACE_COLOR = "white"
FIG14_3_PATH_LABEL_EDGE_COLOR = "none"
FIG14_3_PATH_LABEL_BOX_STYLE = "square"

# Righe in fondo alla figura 14.3.
# Le coordinate sono frazioni dell'altezza degli assi (0 = fondo, 1 = cima).
FIG14_3_BOTTOM_NOTE_Y = -0.005
# Distanza fra le posizioni verticali delle due righe: aumentare per separarle.
FIG14_3_BOTTOM_ROWS_GAP = 0.075
FIG14_3_BOTTOM_FORMULA_Y = FIG14_3_BOTTOM_NOTE_Y + FIG14_3_BOTTOM_ROWS_GAP

def save_figure(fig, stem: str) -> tuple[Path, Path]:
    """Salva una figura in PNG e SVG, quindi comunica le destinazioni."""
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


def add_box(
    ax,
    center,
    text,
    width=0.19,
    height=0.15,
    font_category="math",
):
    """Aggiunge un box con una categoria tipografica controllabile."""
    x, y = center
    patch = FancyBboxPatch(
        (x - width/2, y - height/2),
        width, height,
        boxstyle="round,pad=0.015",
        linewidth=1.2,
        fill=False,
    )
    ax.add_patch(patch)
    ax.text(
        x, y, text,
        ha="center", va="center",
        fontsize=font_size(font_category),
        linespacing=line_spacing(font_category),
    )


def add_arrow(ax, start, end, lw=1.5):
    ax.annotate(
        "",
        xy=end, xytext=start,
        arrowprops=dict(arrowstyle="->", linewidth=lw),
    )

# ============================================================
# FIGURA 14.1 — struttura informativa del problema a due stadi
# ============================================================

fig, ax = plt.subplots(figsize=FIG_SIZES["fig14_1"])
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

# Ogni intestazione è spezzata su due righe e allineata al proprio box.
two_stage_nodes = (
    ("x", r"$x$", "decisione di\nprimo stadio"),
    ("xi", r"$\xi$", "rivelazione\ndell'incertezza"),
    ("y", r"$y(x,\xi)$", "decisione di\nrecourse"),
)

for key, box_text, header_text in two_stage_nodes:
    center = POS14_1[key]
    add_box(
        ax,
        center,
        box_text,
        width=FIG14_1_BOX_WIDTHS[key],
        height=FIG14_1_BOX_HEIGHT,
    )
    ax.text(
        center[0], FIG14_1_HEADER_Y, header_text,
        ha="center", va="center",
        fontsize=font_size("stage_label"),
        linespacing=line_spacing("stage_label"),
    )

# Le frecce partono e terminano in funzione dei bordi dei box.
for left_key, right_key in (("x", "xi"), ("xi", "y")):
    left_x, common_y = POS14_1[left_key]
    right_x, _ = POS14_1[right_key]
    start = (
        left_x + FIG14_1_BOX_WIDTHS[left_key] / 2 + FIG14_1_ARROW_GAP,
        common_y,
    )
    end = (
        right_x - FIG14_1_BOX_WIDTHS[right_key] / 2 - FIG14_1_ARROW_GAP,
        common_y,
    )
    add_arrow(ax, start, end)

ax.text(
    0.50, FIG14_1_NOTE_Y,
    r"$x$ è scelta prima di conoscere $\xi$;" "\n"
    r"$y(x,\xi)$ è scelta dopo l'osservazione di $\xi$.",
    ha="center", va="center",
    fontsize=font_size("two_stage_note"),
    linespacing=line_spacing("two_stage_note"),
)

save_figure(fig, "Cap14_struttura_two_stage")

# ============================================================
# FIGURA 14.2 — rappresentazione discreta mediante scenari
# ============================================================

fig, ax = plt.subplots(figsize=FIG_SIZES["fig14_2"])
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

root = POS14_2["root"]
add_box(
    ax, root, "incertezza",
    width=FIG14_2_ROOT_WIDTH,
    height=FIG14_2_ROOT_HEIGHT,
    font_category="annotation",
)

leaf_labels = [
    ("scenario 1", r"$p_1$"),
    ("scenario 2", r"$p_2$"),
    (r"$\vdots$", r"$\vdots$"),
    ("scenario N", r"$p_N$"),
]

for y, (xi_label, p_label) in zip(POS14_2["leaves_y"], leaf_labels):
    leaf_center = (POS14_2["leaves_x"], y)
    add_box(
        ax,
        leaf_center,
        xi_label,
        width=FIG14_2_LEAF_WIDTH,
        height=FIG14_2_LEAF_HEIGHT,
    )

    arrow_start = (
        root[0] + FIG14_2_ROOT_WIDTH / 2 + FIG14_2_ARROW_GAP,
        root[1],
    )
    arrow_end = (
        leaf_center[0] - FIG14_2_LEAF_WIDTH / 2 - FIG14_2_ARROW_GAP,
        leaf_center[1],
    )
    add_arrow(ax, arrow_start, arrow_end)

    # La label è centrata sulla propria freccia; il piccolo fondo bianco
    # evita che il segmento attraversi il testo e rende univoco l'abbinamento.
    label_x = arrow_start[0] + FIG14_2_LABEL_FRACTION * (
        arrow_end[0] - arrow_start[0]
    )
    label_y = arrow_start[1] + FIG14_2_LABEL_FRACTION * (
        arrow_end[1] - arrow_start[1]
    )
    ax.text(
        label_x, label_y,
        p_label,
        ha="center", va="center",
        fontsize=font_size("probability_label"),
        linespacing=line_spacing("probability_label"),
        bbox={
            "facecolor": FIG14_2_LABEL_FACE_COLOR,
            "edgecolor": FIG14_2_LABEL_EDGE_COLOR,
            # Il padding va specificato nel boxstyle: un attributo "pad"
            # separato non modifica il margine del riquadro di testo.
            "boxstyle": (
                f"{FIG14_2_LABEL_BOX_STYLE},pad={FIG14_2_LABEL_PADDING}"
            ),
        },
        zorder=3,
    )

ax.text(
    0.50, FIG14_2_FORMULA_Y,
    "insieme finito di scenari con probabilità associate",
    ha="center", va="center",
    fontsize=font_size("annotation"),
    linespacing=line_spacing("annotation"),
)

ax.text(
    0.50, 0.015,
    r"$N$ = numero totale di scenari",
    ha="center", va="center",
    fontsize=font_size("annotation"),
    linespacing=line_spacing("annotation"),
)

save_figure(fig, "Cap14_rappresentazione_scenari")

# ============================================================
# FIGURA 14.3 — albero Markoviano a più periodi
# Catena a 8 stati, T=4.
# La figura mostra gli otto stati a ciascuna data e una traiettoria
# completa. Le transizioni non appartenenti alla traiettoria sono
# rese schematicamente per non compromettere la leggibilità.
# ============================================================

fig, ax = plt.subplots(figsize=FIG_SIZES["fig14_3"])
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

time_x = [0.08, 0.29, 0.50, 0.71, 0.92]
for t, x in enumerate(time_x):
    ax.text(
        x, 0.95, rf"$t={t}$",
        ha="center", va="center",
        fontsize=font_size("time_label"),
        linespacing=line_spacing("time_label"),
    )

root = (time_x[0], 0.50)
ax.add_patch(Circle(root, 0.024, fill=False, linewidth=1.2))
ax.text(
    root[0], root[1], r"$z_{i_0}$",
    ha="center", va="center",
    fontsize=font_size("node_label"),
    linespacing=line_spacing("node_label"),
)

ys = [0.84, 0.74, 0.64, 0.54, 0.44, 0.34, 0.24, 0.14]
future_nodes = {}

for t in range(1, 5):
    x = time_x[t]
    for i, y in enumerate(ys, start=1):
        future_nodes[(t, i)] = (x, y)
        ax.add_patch(Circle((x, y), 0.020, fill=False, linewidth=1.0))
        ax.text(
            x, y, rf"$z_{i}$",
            ha="center", va="center",
            fontsize=font_size("node_label"),
            linespacing=line_spacing("node_label"),
        )

# Tutti gli otto possibili stati al primo passo
for i in range(1, 9):
    add_arrow(
        ax,
        (root[0] + 0.025, root[1]),
        (time_x[1] - 0.025, ys[i-1]),
        lw=0.8
    )

# Tra periodi successivi si rappresentano alcune transizioni,
# sufficienti a rendere visibile la struttura Markoviana.
representative_pairs = [
    (1, 1), (1, 4),
    (2, 2), (2, 5),
    (3, 3), (3, 6),
    (4, 4), (4, 7),
    (5, 5), (5, 8),
    (6, 2), (6, 6),
    (7, 3), (7, 7),
    (8, 4), (8, 8),
]

for t in range(1, 4):
    for i, j in representative_pairs:
        start = future_nodes[(t, i)]
        end = future_nodes[(t+1, j)]
        add_arrow(
            ax,
            (start[0] + 0.022, start[1]),
            (end[0] - 0.022, end[1]),
            lw=0.55
        )

# Una traiettoria completa
path_indices = [2, 5, 3, 7]
path_points = [root] + [
    future_nodes[(t, idx)]
    for t, idx in enumerate(path_indices, start=1)
]

for a, b in zip(path_points[:-1], path_points[1:]):
    add_arrow(
        ax,
        (a[0] + 0.024, a[1]),
        (b[0] - 0.024, b[1]),
        lw=2.6
    )

prob_labels = [
    r"$p_{i_0\,i_1^s}$",
    r"$p_{i_1^s\,i_2^s}$",
    r"$p_{i_2^s\,i_3^s}$",
    r"$p_{i_3^s\,i_4^s}$",
]

for (a, b), lab in zip(zip(path_points[:-1], path_points[1:]), prob_labels):
    xm = (a[0] + b[0]) / 2
    ym = (a[1] + b[1]) / 2
    ax.text(
        xm, ym + FIG14_3_PATH_LABEL_OFFSET_Y, lab,
        ha="center", va="center",
        fontsize=font_size("probability_label"),
        linespacing=line_spacing("probability_label"),
        bbox={
            "facecolor": FIG14_3_PATH_LABEL_FACE_COLOR,
            "edgecolor": FIG14_3_PATH_LABEL_EDGE_COLOR,
            "boxstyle": (
                f"{FIG14_3_PATH_LABEL_BOX_STYLE},"
                f"pad={FIG14_3_PATH_LABEL_PADDING}"
            ),
        },
        zorder=4,
    )

ax.text(
    0.50, FIG14_3_BOTTOM_FORMULA_Y,
    r"$\xi_s=(Z_1^s,Z_2^s,Z_3^s,Z_4^s)$"
    r"$\qquad$"
    r"$p_s=p_{i_0i_1^s}p_{i_1^si_2^s}p_{i_2^si_3^s}p_{i_3^si_4^s}$",
    ha="center", va="center",
    fontsize=font_size("math"),
    linespacing=line_spacing("math"),
)

ax.text(
    0.50, FIG14_3_BOTTOM_NOTE_Y,
    "I nodi intermedi rappresentano stati del processo, non stadi decisionali.",
    ha="center", va="bottom",
    fontsize=font_size("annotation"),
    linespacing=line_spacing("annotation"),
)

save_figure(fig, "Cap14_albero_markoviano_scenari")

print("Salvataggio completato: 3 figure, 6 file generati.")
print(f"Cartella di destinazione: {OUTPUT_DIR.resolve()}")
