from pathlib import Path

import matplotlib.pyplot as plt

# ============================================================
# PERCORSO E PARAMETRI DI SALVATAGGIO
# ============================================================

OUTPUT_DIR = Path(r"E:\Didattica\MQF\graphics")
OUTPUT_STEM = "Cap15_probabilita_nodo"

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
    "node": 11.5,
    "annotation": 10.5,
}

COL_STRUCT = "#2A4B7C"
COL_ACCENT = "#C24D2C"
COL_MUTED = "#7A7A7A"

# ============================================================
# DATI DELL'ESEMPIO
# ============================================================

ROOT = (0, 0)
MID = [(1, 1.2), (1, -1.2)]
LEAVES = [(2, 1.8), (2, 0.6), (2, -0.6), (2, -1.8)]
PROBS_LEAF = [0.15, 0.25, 0.30, 0.30]


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

fig, ax = plt.subplots(figsize=(8.5, 5.6))
ax.set_xlim(-0.4, 2.6)
ax.set_ylim(-3.2, 3.2)
ax.axis("off")

ax.scatter(*ROOT, s=190, color=COL_STRUCT, zorder=3, edgecolor="white")
ax.text(ROOT[0] - 0.05, ROOT[1] + 0.35, "radice", ha="center",
        fontsize=FONT_SIZES["annotation"], color=COL_MUTED)

for (px, py) in MID:
    ax.plot([ROOT[0], px], [ROOT[1], py], color=COL_MUTED, lw=1.3, zorder=1)

node_A = MID[0]
ax.scatter(*node_A, s=260, facecolor="none", edgecolor=COL_ACCENT, linewidth=2.2, zorder=4)
ax.scatter(*MID[1], s=190, color=COL_STRUCT, zorder=3, edgecolor="white")
ax.text(node_A[0] - 0.02, node_A[1] + 0.32, "$n$",
        fontsize=FONT_SIZES["node"], color=COL_ACCENT, fontweight="bold")

for i, (lx, ly) in enumerate(LEAVES):
    parent = MID[0] if i < 2 else MID[1]
    ax.plot([parent[0], lx], [parent[1], ly], color=COL_MUTED, lw=1.1, zorder=1)
    col = COL_ACCENT if i < 2 else COL_MUTED
    ax.scatter([lx], [ly], s=150, color=col, zorder=3, edgecolor="white")
    ax.text(lx + 0.15, ly, f"$s_{{{i + 1}}}$   $p_{{s_{{{i + 1}}}}}={PROBS_LEAF[i]:.2f}$",
            va="center", fontsize=FONT_SIZES["annotation"],
            color=(COL_ACCENT if i < 2 else COL_MUTED))

p_n = PROBS_LEAF[0] + PROBS_LEAF[1]
ax.text(1.0, 2.6,
        r"$p_n = p_{s_1}+p_{s_2} = %.2f$" % p_n
        + "\n(probabilità marginale: somma sugli scenari che passano per $n$)",
        ha="center", fontsize=FONT_SIZES["annotation"], color=COL_ACCENT)

ax.text(2.0, -2.7,
        r"$p_{s_1}=%.2f \neq p_n$" % PROBS_LEAF[0]
        + "\n(probabilità dell'intera traiettoria $s_1$)",
        ha="center", fontsize=FONT_SIZES["annotation"], color=COL_MUTED)

ax.set_title("Probabilità di nodo: marginale ($p_n$) vs traiettoria completa ($p_s$)",
             fontsize=FONT_SIZES["title"], color=COL_STRUCT, pad=14)

save_figure(fig, OUTPUT_STEM)
