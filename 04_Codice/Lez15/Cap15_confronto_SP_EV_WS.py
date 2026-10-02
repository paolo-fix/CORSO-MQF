"""Confronto concettuale EV, SP e WS (Capitolo 15, sezione 15.6).

La figura illustra l'ordinamento per problemi di massimizzazione e
le definizioni di VSS ed EVPI. Le posizioni non sono valori stimati:
le distanze sono convenzionali e possono annullarsi.

Output: Cap15_confronto_SP_EV_WS.png (300 dpi) e .svg.
Requisiti: matplotlib.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

# ============================================================
# PERCORSI DI OUTPUT
# ============================================================
# Cartella definitiva delle figure del progetto MQF.
OUTPUT_DIR = Path(r"E:\Didattica\MQF\graphics")
OUTPUT_STEM = "Cap15_confronto_SP_EV_WS"
PNG_DPI = 300
SAVE_BBOX = "tight"
SAVE_PAD_INCHES = 0.08

# ============================================================
# TIPOGRAFIA
# ============================================================
FONT_FAMILY = "DejaVu Sans"
FONT_SCALE = 1.00
LINE_SPACING_SCALE = 1.00
FONT_SIZES = {
    "title": 19.0,
    "subtitle": 15.0,
    "benchmark": 17.0,
    "description": 13.0,
    "indicator": 16.0,
    "interpretation": 13.0,
    "annotation": 12.0,
}
LINE_SPACINGS = {k: 1.05 for k in FONT_SIZES}
LINE_SPACINGS["interpretation"] = 1.20

plt.rcParams["font.family"] = FONT_FAMILY
plt.rcParams["mathtext.fontset"] = "dejavusans"
plt.rcParams["svg.fonttype"] = "none"


def text_style(category):
    return {
        "fontsize": FONT_SIZES[category] * FONT_SCALE,
        "linespacing": LINE_SPACINGS[category] * LINE_SPACING_SCALE,
    }


# ============================================================
# GEOMETRIA: posizioni puramente illustrative (NON valori numerici)
# ============================================================
FIG_SIZE = (13.3, 5.0)
X_EV = 1.10
X_SP = 4.85
X_WS = 8.25
X_AXIS_END = 9.55
Y_AXIS = 1.80
Y_GAP = 2.88
Y_TOP_LABEL = 3.43
Y_MARKER_LABEL = 1.36
Y_DESCRIPTION = 0.95
Y_FOOTER = 0.25
MARKER_SIZE = 115
MARKER_EDGE_WIDTH = 1.8
LINE_WIDTH = 2.2
BRACKET_WIDTH = 1.7

# Palette conforme alle figure gia' sviluppate per il Capitolo 15.
COLORS = {
    "navy": "#2b4c7e",
    "terracotta": "#c0502e",
    "gray": "#6a6a6a",
    "light_gray": "#b3b3b3",
    "black": "#272727",
}


# ============================================================
# DISEGNO
# ============================================================
fig, ax = plt.subplots(figsize=FIG_SIZE)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")
ax.set_xlim(0.0, 10.0)
ax.set_ylim(-0.08, 4.47)
ax.axis("off")

ax.text(5.0, 4.20, "Confronto tra EV, SP e WS", ha="center",
        va="center", color=COLORS["navy"], fontweight="bold",
        **text_style("title"))
ax.text(5.0, 3.83,
        r"Problema di massimizzazione: $z^{EV}\leq z^{SP}\leq z^{WS}$",
        ha="center", va="center", color=COLORS["black"],
        **text_style("subtitle"))

# Asse qualitativo del valore ottimo, non graduato numericamente.
ax.add_patch(FancyArrowPatch((0.40, Y_AXIS), (X_AXIS_END, Y_AXIS),
                            arrowstyle="-|>", mutation_scale=19,
                            lw=LINE_WIDTH, color=COLORS["black"]))

# Tre benchmark.
for xpos, name, desc in (
    (X_EV, r"$z^{EV}$", "Decisione basata\nsui valori medi"),
    (X_SP, r"$z^{SP}$", "Soluzione\nstocastica"),
    (X_WS, r"$z^{WS}$", "Informazione\nperfetta"),
):
    ax.scatter([xpos], [Y_AXIS], s=MARKER_SIZE,
               c=COLORS["navy"], edgecolors="white",
               linewidths=MARKER_EDGE_WIDTH, zorder=5)
    ax.text(xpos, Y_MARKER_LABEL, name, color=COLORS["navy"],
            ha="center", va="center", **text_style("benchmark"))
    ax.text(xpos, Y_DESCRIPTION, desc, color=COLORS["black"],
            ha="center", va="top", **text_style("description"))

# Proiezioni verticali e intervalli: prima VSS, poi EVPI.
for xpos in (X_EV, X_SP, X_WS):
    ax.plot([xpos, xpos], [Y_AXIS + 0.12, Y_GAP + 0.02],
            ls=(0, (3, 4)), lw=1.1, color=COLORS["light_gray"])

for xmin, xmax, name, interpretation, color in (
    (X_EV, X_SP, r"$\mathrm{VSS}=z^{SP}-z^{EV}$",
     "Valore della scelta\nstocastica", COLORS["navy"]),
    (X_SP, X_WS, r"$\mathrm{EVPI}=z^{WS}-z^{SP}$",
     "Valore dell'informazione\nperfetta", COLORS["terracotta"]),
):
    ax.add_patch(FancyArrowPatch((xmin + 0.08, Y_GAP),
                                (xmax - 0.08, Y_GAP),
                                arrowstyle="<->", mutation_scale=15,
                                lw=BRACKET_WIDTH, color=color))
    middle = (xmin + xmax) / 2
    ax.text(middle, Y_TOP_LABEL, name, ha="center", va="center",
            color=color, **text_style("indicator"))
    ax.text(middle, Y_GAP - 0.27, interpretation, ha="center",
            va="top", color=color, **text_style("interpretation"))

ax.text(5.0, Y_FOOTER,
        "Schema qualitativo: distanze non in scala.",
        ha="center", va="center", color=COLORS["gray"],
        **text_style("annotation"))

# ============================================================
# SALVATAGGIO (PNG 300 dpi + SVG dallo stesso script)
# ============================================================
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
for extension in ("png", "svg"):
    target = OUTPUT_DIR / f"{OUTPUT_STEM}.{extension}"
    fig.savefig(target, dpi=PNG_DPI if extension == "png" else None,
                bbox_inches=SAVE_BBOX, pad_inches=SAVE_PAD_INCHES,
                facecolor="white")
    print(f"Creato: {target}")
plt.close(fig)
