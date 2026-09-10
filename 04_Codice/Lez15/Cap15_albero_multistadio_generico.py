from pathlib import Path

import matplotlib.pyplot as plt

# ============================================================
# PERCORSO E PARAMETRI DI SALVATAGGIO
# ============================================================

OUTPUT_DIR = Path(r"E:\Didattica\MQF\graphics")
OUTPUT_STEM = "Cap15_albero_multistadio_generico"

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
    "node": 11.5,
    "annotation": 10.5,
    "axis": 11.5,
}

COL_STRUCT = "#2A4B7C"   # blu strutturale: nodi, rami
COL_ACCENT = "#C24D2C"   # arancio-rosso: evidenziazioni
COL_MUTED = "#7A7A7A"    # grigio: elementi secondari

# ============================================================
# STRUTTURA DELL'ALBERO
# ============================================================

# Albero del tutto generico e irregolare: il numero di figli varia da nodo
# a nodo (2 sotto la radice; poi 3 e 2), cosi' da non suggerire alcun caso
# specifico (binomiale, ternario, ...) ne' alcun orizzonte T particolare.
# Serve solo a fissare il vocabolario nodo, antenato, profondita'
# (Sez. 5.1, "Nodi, antenati e probabilita' di nodo").

ROOT = (0, 0.0)
NODE_A = (1, 1.5)     # nodo di profondita' 1, con 3 figli
NODE_B = (1, -1.8)    # nodo di profondita' 1, con 2 figli
CHILDREN_A = [(2, 2.6), (2, 1.5), (2, 0.4)]
CHILDREN_B = [(2, -1.0), (2, -2.6)]

# Nodo evidenziato n e relativo antenato a(n)
N_NODE = CHILDREN_A[1]
A_NODE = NODE_A


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

fig, ax = plt.subplots(figsize=(8.5, 5.8))
ax.set_xlim(-0.5, 2.7)
ax.set_ylim(-3.2, 3.2)
ax.axis("off")

edges = [(ROOT, NODE_A), (ROOT, NODE_B)]
for c in CHILDREN_A:
    edges.append((NODE_A, c))
for c in CHILDREN_B:
    edges.append((NODE_B, c))
for (p, c) in edges:
    ax.plot([p[0], c[0]], [p[1], c[1]], color=COL_MUTED, lw=1.3, zorder=1)

all_nodes = [ROOT, NODE_A, NODE_B] + CHILDREN_A + CHILDREN_B
for (x, y) in all_nodes:
    ax.scatter([x], [y], s=180, color=COL_STRUCT, zorder=3, edgecolor="white", linewidth=1.0)

ax.text(ROOT[0], ROOT[1] + 0.55, r"$x$" + "\n(radice, $t=0$)",
        ha="center", va="bottom", fontsize=FONT_SIZES["label"], color=COL_STRUCT)

for t, x in enumerate([0, 1, 2]):
    ax.text(x, -3.0, f"$t={t}$", ha="center", va="top",
            fontsize=FONT_SIZES["axis"], color=COL_MUTED)

# evidenzia il nodo n e il suo antenato a(n)
ax.scatter([N_NODE[0]], [N_NODE[1]], s=260, facecolor="none",
           edgecolor=COL_ACCENT, linewidth=2.2, zorder=4)
ax.text(N_NODE[0] + 0.10, N_NODE[1] + 0.30, "$n$",
        fontsize=FONT_SIZES["node"], color=COL_ACCENT, fontweight="bold")
ax.scatter([A_NODE[0]], [A_NODE[1]], s=260, facecolor="none",
           edgecolor=COL_ACCENT, linewidth=2.2, zorder=4)
ax.text(A_NODE[0] - 0.32, A_NODE[1] + 0.05, "$a(n)$",
        fontsize=FONT_SIZES["node"], color=COL_ACCENT, fontweight="bold")
ax.annotate("", xy=(N_NODE[0] - 0.08, N_NODE[1]), xytext=(A_NODE[0] + 0.08, A_NODE[1]),
            arrowprops=dict(arrowstyle="-", color=COL_ACCENT, lw=1.6,
                             connectionstyle="arc3,rad=0.15"), zorder=2)

ax.text(1, 2.95, "il numero di figli per nodo è arbitrario: qui 2, poi 3 e 2",
        ha="center", va="top", fontsize=FONT_SIZES["annotation"], color=COL_MUTED)

ax.set_title("Albero degli scenari: nodi, antenato e profondità",
             fontsize=FONT_SIZES["title"], color=COL_STRUCT, pad=12)

save_figure(fig, OUTPUT_STEM)
