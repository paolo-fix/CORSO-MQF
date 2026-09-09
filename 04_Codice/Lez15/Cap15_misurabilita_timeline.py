from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# ============================================================
# PERCORSO E PARAMETRI DI SALVATAGGIO
# ============================================================

OUTPUT_DIR = Path(r"E:\Didattica\MQF\graphics")
OUTPUT_STEM = "Cap15_misurabilita_timeline"

PNG_DPI = 300
SAVE_BBOX = "tight"
SAVE_PAD_INCHES = 0.04

# ============================================================
# TIPOGRAFIA E COLORI
# ============================================================

FONT_FAMILY = "DejaVu Sans"
plt.rcParams["font.family"] = FONT_FAMILY

FONT_SIZES = {
    "title": 15.0,
    "label": 12.5,
    "annotation": 10.5,
    "axis": 11.5,
}

COL_STRUCT = "#2A4B7C"
COL_ACCENT = "#C24D2C"
COL_MUTED = "#7A7A7A"

# ============================================================
# DATI: data di misurabilita' di u_1,u_2,u_3 per numero di stadi
# ============================================================

ROWS = ["2 stadi", "3 stadi", "4 stadi"]
SCHEDULE = {
    "2 stadi": {"u_1": 4, "u_2": 4, "u_3": 4},
    "3 stadi": {"u_1": 1, "u_2": 4, "u_3": 4},
    "4 stadi": {"u_1": 1, "u_2": 2, "u_3": 3},
}
COLORS = {"u_1": COL_STRUCT, "u_2": COL_ACCENT, "u_3": COL_MUTED}
OFFSETS = {"u_1": 0.18, "u_2": 0.0, "u_3": -0.18}


def save_figure(fig, stem):
    """Salva la figura in PNG e SVG e comunica le destinazioni effettive."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    png_path = OUTPUT_DIR / f"{stem}.png"
    svg_path = OUTPUT_DIR / f"{stem}.svg"
    fig.savefig(png_path, dpi=PNG_DPI, bbox_inches=SAVE_BBOX, pad_inches=SAVE_PAD_INCHES)
    fig.savefig(svg_path, bbox_inches=SAVE_BBOX, pad_inches=SAVE_PAD_INCHES)
    plt.close(fig)
    print(f"Figura PNG salvata in: {png_path.resolve()}")
    print(f"Figura SVG salvata in: {svg_path.resolve()}")
    return png_path, svg_path


# ============================================================
# FIGURA
# ============================================================

fig, ax = plt.subplots(figsize=(9.5, 4.6))

y_pos = {r: i for i, r in enumerate(ROWS)}

for r in ROWS:
    y = y_pos[r]
    ax.plot([0, 4], [y, y], color="#D8D8D8", lw=10, zorder=1, solid_capstyle="round")
    for u, t in SCHEDULE[r].items():
        ax.scatter([t], [y + OFFSETS[u]], s=170, color=COLORS[u], zorder=3,
                   edgecolor="white", linewidth=1.0)

ax.set_yticks([y_pos[r] for r in ROWS])
ax.set_yticklabels(ROWS, fontsize=FONT_SIZES["label"])
ax.set_xticks([0, 1, 2, 3, 4])
ax.set_xticklabels([f"$t={t}$" for t in range(5)], fontsize=FONT_SIZES["axis"])
ax.set_xlim(-0.3, 4.5)
ax.set_ylim(-0.7, 2.7)
for spine in ["top", "right", "left"]:
    ax.spines[spine].set_visible(False)
ax.tick_params(left=False)

legend_handles = [
    Line2D([0], [0], marker="o", color="none", markerfacecolor=COL_STRUCT,
           markersize=10, label=r"$u_1^s$"),
    Line2D([0], [0], marker="o", color="none", markerfacecolor=COL_ACCENT,
           markersize=10, label=r"$u_2^s$"),
    Line2D([0], [0], marker="o", color="none", markerfacecolor=COL_MUTED,
           markersize=10, label=r"$u_3^s$"),
]
ax.legend(handles=legend_handles, loc="upper center", bbox_to_anchor=(0.5, -0.16),
          ncol=3, frameon=False, fontsize=FONT_SIZES["annotation"])

ax.set_title("Misurabilità delle decisioni intermedie: dal due al quattro stadi",
             fontsize=FONT_SIZES["title"], color=COL_STRUCT, pad=14)

save_figure(fig, OUTPUT_STEM)
