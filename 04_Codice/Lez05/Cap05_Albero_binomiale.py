# =============================================================
# Cap05_Albero_binomiale.py
# Progetto MQF - Capitolo 5: Processi stocastici a tempo discreto
# Figura 4.1: Albero binomiale completo
#   S0=100, u=1.1, d=0.9, p=0.6, T=3
#
# Output: E:\Didattica\MQF\Github\CORSO-MQF\graphics\Cap05_Figura_4_1.png
#
# Dipendenze: matplotlib
# Esecuzione: python Cap05_Albero_binomiale.py
# =============================================================

import os
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# ------------------------------------------------------------
# Parametri del modello
# ------------------------------------------------------------
S0 = 100.0
u  = 1.1
d  = 0.9
p  = 0.6
T  = 3

# ------------------------------------------------------------
# Percorso di output
# ------------------------------------------------------------
OUTPUT_DIR = r"E:\Didattica\MQF\Github\CORSO-MQF\graphics"
OUTPUT     = os.path.join(OUTPUT_DIR, "Cap05_Figura_4_1.png")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ------------------------------------------------------------
# Geometria dell'albero
# XSCALE: spaziatura orizzontale tra periodi
# YSCALE: spaziatura verticale tra nodi
# ------------------------------------------------------------
XSCALE = 1.5
YSCALE = 1.6

def node_value(t, k):
    return S0 * (u ** k) * (d ** (t - k))

def node_pos(t, k):
    return float(t * XSCALE), float((k - t / 2.0) * YSCALE)

nodes = {}
for t in range(T + 1):
    for k in range(t + 1):
        x, y = node_pos(t, k)
        nodes[(t, k)] = (x, y, node_value(t, k))

# ------------------------------------------------------------
# Stile grafico (font grandi per proiezione in aula)
# ------------------------------------------------------------
matplotlib.rcParams.update({'font.family': 'serif', 'font.size': 26})

fig, ax = plt.subplots(figsize=(18, 11))
ax.set_aspect('equal')
ax.axis('off')

COLOR_NODE_EDGE = '#1C2833'
COLOR_VALUE     = '#1C1C1C'
COLOR_LABEL     = '#555555'
COLOR_UP        = '#1A5276'    # blu scuro  - rialzo
COLOR_DN        = '#7FB3D3'    # azzurro chiaro - ribasso
COLOR_PROB_UP   = '#1A5276'
COLOR_PROB_DN   = '#2E86C1'
RADIUS         = 0.33
LW_ARROW       = 2.6
FONT_NODE      = 26
FONT_PROB      = 22
FONT_AXIS      = 24
FONT_TERMINAL  = 22

# ------------------------------------------------------------
# Archi e probabilita'
# ------------------------------------------------------------
for t in range(T):
    for k in range(t + 1):
        x0, y0, _ = nodes[(t,   k)]
        xu, yu, _ = nodes[(t+1, k+1)]
        xd, yd, _ = nodes[(t+1, k  )]

        # Arco rialzo
        ax.annotate('', xy=(xu, yu), xytext=(x0, y0),
            arrowprops=dict(arrowstyle='-|>', color=COLOR_UP,
                lw=LW_ARROW, mutation_scale=16,
                shrinkA=RADIUS*72, shrinkB=RADIUS*72))
        mx  = (x0 + xu) / 2 - 0.12
        my  = (y0 + yu) / 2 + 0.20
        ax.text(mx, my, f'$p={p}$', ha='right', va='bottom',
                fontsize=FONT_PROB, color=COLOR_PROB_UP, fontstyle='italic')

        # Arco ribasso
        ax.annotate('', xy=(xd, yd), xytext=(x0, y0),
            arrowprops=dict(arrowstyle='-|>', color=COLOR_DN,
                lw=LW_ARROW, mutation_scale=16,
                shrinkA=RADIUS*72, shrinkB=RADIUS*72))
        mx2 = (x0 + xd) / 2 - 0.12
        my2 = (y0 + yd) / 2 - 0.20
        ax.text(mx2, my2, f'$1-p={1-p}$', ha='right', va='top',
                fontsize=FONT_PROB, color=COLOR_PROB_DN, fontstyle='italic')

# ------------------------------------------------------------
# Nodi
# ------------------------------------------------------------
for (t, k), (x, y, v) in nodes.items():
    circle = plt.Circle((x, y), RADIUS, color='white',
                         ec=COLOR_NODE_EDGE, lw=2.2, zorder=3)
    ax.add_patch(circle)
    ax.text(x, y, f'{v:.1f}', ha='center', va='center',
            fontsize=FONT_NODE, color=COLOR_VALUE,
            fontweight='bold', zorder=4)

# ------------------------------------------------------------
# Etichette traiettorie terminali
# ------------------------------------------------------------
terminal_labels = {
    (3, 3): 'uuu',
    (3, 2): 'uu·d',
    (3, 1): 'u·dd',
    (3, 0): 'ddd',
}
for (t, k), label in terminal_labels.items():
    x, y, _ = nodes[(t, k)]
    ax.text(x + 0.45, y, label, ha='left', va='center',
            fontsize=FONT_TERMINAL, color='#888888', fontstyle='italic')

# ------------------------------------------------------------
# Asse dei tempi
# ------------------------------------------------------------
y_min  = min(y for _, y, _ in nodes.values())
y_axis = y_min - 0.75
for t in range(T + 1):
    x_t = nodes[(t, 0)][0]
    ax.text(x_t, y_axis, f'$t={t}$', ha='center', va='top',
            fontsize=FONT_AXIS, color=COLOR_LABEL)
ax.axhline(y=y_axis + 0.20, color='#CCCCCC', lw=0.9,
           xmin=0.0, xmax=1.0, clip_on=False)

# ------------------------------------------------------------
# Legenda: nel quadrante nord-ovest della figura, in posizione compatta
# ------------------------------------------------------------
patch_up = mpatches.Patch(color=COLOR_UP,  label=f'Rialzo      $u = {u}$')
patch_dn = mpatches.Patch(color=COLOR_DN,  label=f'Ribasso   $d = {d}$')
x_leg = nodes[(0, 0)][0] - 0.75
y_leg = max(y for _, y, _ in nodes.values()) + 0.28
ax.legend(
    handles=[patch_up, patch_dn],
    loc='upper left',
    bbox_to_anchor=(x_leg, y_leg),
    bbox_transform=ax.transData,
    fontsize=18,
    framealpha=0.97,
    edgecolor='#BBBBBB',
    ncol=1,
    handlelength=1.6,
    handleheight=0.95,
    borderpad=0.65,
    labelspacing=0.65,
    columnspacing=0.8,
)

# ------------------------------------------------------------
# Margini e salvataggio
# ------------------------------------------------------------
x_max = nodes[(T, 0)][0]
ax.set_xlim(-0.65, x_max + 3.8)
ax.set_ylim(y_axis - 0.40, max(y for _, y, _ in nodes.values()) + 0.70)

plt.tight_layout()
plt.savefig(OUTPUT, dpi=200, bbox_inches='tight', facecolor='white')
plt.close()
print(f'Figura salvata in: {OUTPUT}')
