from pathlib import Path

import matplotlib.pyplot as plt

# ============================================================
# PERCORSO E PARAMETRI DI SALVATAGGIO
# ============================================================

OUTPUT_DIR = Path(r"E:\Didattica\MQF\graphics")
OUTPUT_STEM = "Cap15_confronto_ventaglio_albero"

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

N_LEAVES = 8


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
# FIGURA: due pannelli, stesso insieme di scenari s_1..s_8
# ============================================================

fig, axes = plt.subplots(1, 2, figsize=(12.5, 5.5))

# --- pannello sinistro: ventaglio (Cap. 14) ---
ax = axes[0]
ax.set_xlim(-0.4, 3.4)
ax.set_ylim(-4.2, 4.2)
ax.axis("off")
ax.set_title("Modello a due stadi (\"ventaglio\")",
             fontsize=FONT_SIZES["title"], color=COL_STRUCT, pad=10)

root = (0, 0)
leaf_x = 3.0
ys = [(i - (N_LEAVES - 1) / 2) * (6.8 / N_LEAVES) for i in range(N_LEAVES)]
ax.scatter(*root, s=200, color=COL_STRUCT, zorder=3, edgecolor="white")
ax.text(root[0], 0.55, r"$x$", ha="center", fontsize=FONT_SIZES["label"], color=COL_STRUCT)
for i, y in enumerate(ys):
    ax.plot([root[0], leaf_x], [root[1], y], color=COL_MUTED, lw=1.1, zorder=1)
    ax.scatter([leaf_x], [y], s=140, color=COL_ACCENT, zorder=3, edgecolor="white")
    ax.text(leaf_x + 0.18, y, f"$s_{{{i + 1}}}$", va="center",
            fontsize=FONT_SIZES["annotation"], color=COL_ACCENT)
ax.text(root[0], -4.05, "$t=0$", ha="center", fontsize=FONT_SIZES["axis"], color=COL_MUTED)
ax.text(leaf_x, -4.05, "$t=T$ (intero scenario noto)", ha="center",
        fontsize=FONT_SIZES["axis"], color=COL_MUTED)

# --- pannello destro: albero genuino, stesso numero di foglie ---
ax = axes[1]
ax.set_xlim(-0.4, 3.4)
ax.set_ylim(-4.2, 4.2)
ax.axis("off")
ax.set_title("Modello multistadio (\"albero\")",
             fontsize=FONT_SIZES["title"], color=COL_STRUCT, pad=10)

depths = [0, 1, 2, 3]
positions = {0: [(0, 0.0)]}
for d in [1, 2, 3]:
    n = 2 ** d
    scale = 7.6
    ys_d = [(i - (n - 1) / 2) * (scale / n) for i in range(n)]
    positions[d] = [(d, y) for y in ys_d]

for d in range(3):
    parents = positions[d]
    children = positions[d + 1]
    for i, (px, py) in enumerate(parents):
        for (cx, cy) in (children[2 * i], children[2 * i + 1]):
            ax.plot([px, cx], [py, cy], color=COL_MUTED, lw=1.1, zorder=1)

for d in depths:
    for (x, y) in positions[d]:
        color = COL_ACCENT if d == 3 else COL_STRUCT
        size = 140 if d == 3 else 130
        ax.scatter([x], [y], s=size, color=color, zorder=3, edgecolor="white")

for d in depths:
    ax.text(d, -4.0, f"$t={d}$", ha="center", fontsize=FONT_SIZES["axis"], color=COL_MUTED)

ax.text(0, 0.55, r"$x$", ha="center", fontsize=FONT_SIZES["label"], color=COL_STRUCT)

fig.suptitle("Stesso insieme di scenari, due strutture informative diverse",
             fontsize=FONT_SIZES["title"] + 1, color=COL_STRUCT, y=1.02)

save_figure(fig, OUTPUT_STEM)
