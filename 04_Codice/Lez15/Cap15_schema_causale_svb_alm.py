from pathlib import Path
from typing import Literal, TypedDict

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.path import Path as MplPath

# ============================================================
# PERCORSO E PARAMETRI DI SALVATAGGIO
# ============================================================

OUTPUT_DIR = Path(r"E:\Didattica\MQF\graphics")
OUTPUT_STEM = "Cap15_schema_causale_svb_alm"

PNG_DPI = 300
SAVE_BBOX = "tight"
SAVE_PAD_INCHES = 0.04

# ============================================================
# TIPOGRAFIA E COLORI
# ============================================================

FONT_FAMILY = "DejaVu Sans"
FONT_SCALE = 1.00  # Scala globale: 1.10 aumenta tutti i testi del 10%.
LINE_SPACING_SCALE = 1.00  # Scala globale delle interlinee.

plt.rcParams["font.family"] = FONT_FAMILY
# Mantiene in SVG lo stesso aspetto tipografico anche su altri computer.
plt.rcParams["svg.fonttype"] = "path"

TextCategory = Literal["title", "node", "constraint", "annotation"]


class TextStyle(TypedDict):
    """Proprietà tipografiche riconosciute da Matplotlib e Pylance."""

    fontsize: float
    linespacing: float


FONT_SIZES: dict[TextCategory, float] = {
    "title": 19.0,
    "node": 14.5,
    "constraint": 14.5,  # Testo nel riquadro rosso del vincolo.
    "annotation": 14.5,
}

LINE_SPACINGS: dict[TextCategory, float] = {
    "title": 1.15,
    "node": 1.25,
    "constraint": 1.20,
    "annotation": 1.20,
}


def text_style(category: TextCategory) -> TextStyle:
    """Restituisce dimensione e interlinea della categoria richiesta."""
    return {
        "fontsize": FONT_SIZES[category] * FONT_SCALE,
        "linespacing": LINE_SPACINGS[category] * LINE_SPACING_SCALE,
    }


COL_STRUCT = "#2A4B7C"
COL_ACCENT = "#C24D2C"
COL_MUTED = "#7A7A7A"
COL_BG_BOX = "#EDF1F7"
COL_BG_ACCENT = "#F7E9E4"


def save_figure(fig, stem):
    """Salva la figura in PNG e SVG e comunica le destinazioni effettive."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    png_path = OUTPUT_DIR / f"{stem}.png"
    svg_path = OUTPUT_DIR / f"{stem}.svg"
    fig.savefig(png_path, dpi=PNG_DPI, bbox_inches=SAVE_BBOX, pad_inches=SAVE_PAD_INCHES)
    fig.savefig(svg_path, format="svg", bbox_inches=SAVE_BBOX, pad_inches=SAVE_PAD_INCHES)
    plt.close(fig)
    print(f"Figura PNG salvata in: {png_path.resolve()}")
    print(f"Figura SVG salvata in: {svg_path.resolve()}")
    print(f"Salvataggio completato (PNG + SVG). Destinazione: {OUTPUT_DIR.resolve()}")
    return png_path, svg_path


def add_box(ax, x, y, w, h, text, face, edge,
            text_category: TextCategory = "node"):
    """Disegna un box usando la categoria tipografica indicata."""
    patch = FancyBboxPatch((x, y), w, h,
                            boxstyle="round,pad=0.03,rounding_size=0.10",
                            linewidth=1.6, edgecolor=edge, facecolor=face, zorder=2)
    ax.add_patch(patch)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            color=edge, zorder=3, **text_style(text_category))
    return (x, y, w, h)


def add_arrow(ax, b1, b2, side1="right", side2="left", color=COL_STRUCT, style="-|>"):
    x1, y1, w1, h1 = b1
    x2, y2, w2, h2 = b2
    pts = {"right": (x1 + w1, y1 + h1 / 2), "left": (x2, y2 + h2 / 2),
           "top": (x1 + w1 / 2, y1 + h1), "bottom": (x2 + w2 / 2, y2)}
    arr = FancyArrowPatch(pts[side1], pts[side2], arrowstyle=style, mutation_scale=14,
                           color=color, lw=1.6, zorder=1, connectionstyle="arc3,rad=0.05")
    ax.add_patch(arr)


# ============================================================
# FIGURA
# ============================================================

fig, ax = plt.subplots(figsize=(11.5, 6.8))
ax.set_xlim(0, 11.5)
ax.set_ylim(0, 6.8)
ax.axis("off")

b_z = add_box(ax, 0.4, 2.4, 2.1, 1.2, r"$Z_t$" + "\n(ambiente\nesogeno)",
              COL_BG_BOX, COL_STRUCT)
b_k = add_box(ax, 3.3, 3.6, 2.1, 1.2, r"$\kappa_t$" + "\n(solidità)",
              COL_BG_BOX, COL_STRUCT)
b_d = add_box(ax, 3.3, 1.2, 2.1, 1.2, r"$d_t$" + "\n(fabbisogno)",
              COL_BG_BOX, COL_STRUCT)
b_u = add_box(ax, 6.2, 2.4, 2.3, 1.2, r"$(g_t,u_t)$" + "\n(decisioni)",
              COL_BG_BOX, COL_STRUCT)
b_x = add_box(ax, 9.1, 2.4, 2.1, 1.2, r"$X_{t+1}$" + "\n(stato interno)",
              COL_BG_BOX, COL_STRUCT)
b_c = add_box(ax, 3.3, 5.2, 2.1, 0.65, r"$\kappa_t\geq\kappa_{\min}$",
              COL_BG_ACCENT, COL_ACCENT, "constraint")

add_arrow(ax, b_z, b_k, side1="top", side2="left")
add_arrow(ax, b_z, b_d, side1="bottom", side2="left")
add_arrow(ax, b_d, b_u, side1="right", side2="bottom")
add_arrow(ax, b_k, b_c, side1="top", side2="bottom", color=COL_ACCENT)
add_arrow(ax, b_u, b_x, side1="right", side2="left")

# retroazione X_t -> kappa_{t+1}: percorso "a canalina" sopra tutte le caselle,
# cosi' da non tagliare mai attraverso (g_t,u_t), d_t o il vincolo di solidita'.
x_top_box, y_top_box = 10.15, 3.6      # sommita' di X_{t+1}
x_left_box, y_left_box = 3.3, 4.2      # lato sinistro di kappa_t
y_apex = 6.15                          # quota del tratto orizzontale, sopra b_c (top 5.85)
x_left_turn = 2.0                      # ascissa del tratto verticale di rientro

fb_path = MplPath(
    [(x_top_box, y_top_box), (x_top_box, y_apex),
     (x_left_turn, y_apex), (x_left_turn, y_left_box),
     (x_left_box, y_left_box)],
    [MplPath.MOVETO, MplPath.LINETO, MplPath.LINETO, MplPath.LINETO, MplPath.LINETO],
)
fb = FancyArrowPatch(path=fb_path, arrowstyle="-|>", mutation_scale=14,
                      color=COL_MUTED, lw=1.4, linestyle="--", zorder=1, joinstyle="round")
ax.add_patch(fb)
ax.text((x_top_box + x_left_turn) / 2, y_apex + 0.28,
        r"retroazione: $X_{t+1}$ alimenta $\kappa$",
        color=COL_MUTED, ha="center", va="bottom", **text_style("annotation"))

ax.set_title("Schema causale del caso guida SVB--ALM",
             color=COL_STRUCT, pad=14, **text_style("title"))

save_figure(fig, OUTPUT_STEM)
