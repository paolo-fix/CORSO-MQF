# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# Progetto MQF - Capitolo 8: Catene di Markov
# Figura: Cap08_Grafo_mercato_elettrico.png
# Grafo orientato dei quattro regimi del mercato elettrico.
# Matrice di transizione (dal Capitolo 8):
#       depresso ordinario tensione crisi
#   P = [0.60    0.30      0.10     0.00]
#       [0.10    0.65      0.20     0.05]
#       [0.00    0.25      0.50     0.25]
#       [0.00    0.10      0.35     0.55]
# Stile: sobrio, coerente con l'impostazione didattica del manuale.
# Gli archi lunghi sono ancorati alle "spalle" dei nodi per non
# intersecare i cappi.
# ------------------------------------------------------------

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams["font.family"] = "serif"
plt.rcParams["mathtext.fontset"] = "cm"

DX = 3.4
node_x = [i * DX for i in range(4)]
node_y = 0.0
BOX_W, BOX_H = 2.05, 0.85
SH = 0.82            # scostamento orizzontale delle "spalle"
TOP = node_y + BOX_H / 2
BOT = node_y - BOX_H / 2

names = ["depresso", "ordinario", "tensione", "crisi"]
FACE = "#f5f5f0"
EDGE = "black"

fig, ax = plt.subplots(figsize=(11.0, 4.6))
ax.set_xlim(-1.5, node_x[-1] + 1.5)
ax.set_ylim(-2.15, 2.55)
ax.set_aspect("equal")
ax.axis("off")

node_patches = []
for k, (x, name) in enumerate(zip(node_x, names)):
    box = FancyBboxPatch(
        (x - BOX_W / 2, node_y - BOX_H / 2), BOX_W, BOX_H,
        boxstyle="round,pad=0.06,rounding_size=0.18",
        linewidth=1.4, edgecolor=EDGE, facecolor=FACE, zorder=3,
    )
    ax.add_patch(box)
    node_patches.append(box)
    ax.text(x, node_y + 0.13, str(k + 1), ha="center", va="center",
            fontsize=15, fontweight="bold", zorder=4)
    ax.text(x, node_y - 0.22, name, ha="center", va="center",
            fontsize=12.5, style="italic", zorder=4)

def lab(x, y, s, fs=12):
    ax.text(x, y, s, ha="center", va="center", fontsize=fs, zorder=6,
            bbox=dict(boxstyle="round,pad=0.13", facecolor="white",
                      edgecolor="none"))

def edge(i, j, rad, label, label_xy):
    """Arco adiacente: ancoraggio ai centri, ritagliato sui box."""
    arrow = FancyArrowPatch(
        (node_x[i], node_y), (node_x[j], node_y),
        connectionstyle=f"arc3,rad={rad}",
        arrowstyle="-|>", mutation_scale=16,
        linewidth=1.3, color=EDGE, zorder=2,
        patchA=node_patches[i], patchB=node_patches[j],
        shrinkA=2, shrinkB=2,
    )
    ax.add_patch(arrow)
    lab(label_xy[0], label_xy[1], label)

def edge_far(pA, pB, rad, label, label_xy):
    """Arco lungo: ancoraggio esplicito alle spalle dei box."""
    arrow = FancyArrowPatch(
        pA, pB,
        connectionstyle=f"arc3,rad={rad}",
        arrowstyle="-|>", mutation_scale=16,
        linewidth=1.3, color=EDGE, zorder=2,
    )
    ax.add_patch(arrow)
    lab(label_xy[0], label_xy[1], label)

def self_loop(i, label):
    x = node_x[i]
    y0 = TOP + 0.03
    arrow = FancyArrowPatch(
        (x - 0.42, y0), (x + 0.42, y0),
        connectionstyle="arc3,rad=2.0",
        arrowstyle="-|>", mutation_scale=14,
        linewidth=1.3, color=EDGE, zorder=2,
    )
    ax.add_patch(arrow)
    lab(x, y0 + 0.52, label, fs=11.5)

# cappi (elementi diagonali)
self_loop(0, "0.60")
self_loop(1, "0.65")
self_loop(2, "0.50")
self_loop(3, "0.55")

mid = lambda i, j: (node_x[i] + node_x[j]) / 2

# adiacenti in avanti (sopra)
edge(0, 1, -0.30, "0.30", (mid(0, 1), 0.53))
edge(1, 2, -0.30, "0.20", (mid(1, 2), 0.53))
edge(2, 3, -0.30, "0.25", (mid(2, 3), 0.53))

# lunghe in avanti (sopra, dalle spalle: scavalcano i cappi)
edge_far((node_x[0] + SH, TOP), (node_x[2] - SH, TOP), -0.59,
         "0.10", (mid(0, 2), 1.98))
edge_far((node_x[1] + SH, TOP), (node_x[3] - SH, TOP), -0.59,
         "0.05", (mid(1, 3), 1.98))

# adiacenti indietro (sotto)
edge(1, 0, -0.30, "0.10", (mid(0, 1), -0.53))
edge(2, 1, -0.30, "0.25", (mid(1, 2), -0.53))
edge(3, 2, -0.30, "0.35", (mid(2, 3), -0.53))

# lunga indietro (sotto, dalle spalle)
edge_far((node_x[3] - SH, BOT), (node_x[1] + SH, BOT), -0.41,
         "0.10", (mid(1, 3), -1.50))

fig.savefig("/home/claude/Cap08_Grafo_mercato_elettrico.png",
            dpi=300, bbox_inches="tight", facecolor="white")
print("figura salvata")
