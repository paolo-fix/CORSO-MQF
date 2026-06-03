# =============================================================
# Cap04_Figura_4_2_filtrazione.py
# Progetto MQF - Capitolo 4: Processi stocastici
# Figura 4.2: Filtrazione naturale sull'albero binomiale
#   S0=100, u=1.1, d=0.9, T=3
#
# Output: E:\Didattica\MQF\Github\CORSO-MQF\graphics\Cap04_Figura_4_2.png
#
# Dipendenze: matplotlib
# Esecuzione: python Cap04_Figura_4_2_filtrazione.py
# =============================================================

import os
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch

# ------------------------------------------------------------
# Parametri del modello
# ------------------------------------------------------------
S0 = 100.0
u  = 1.1
d  = 0.9
T  = 3

# ------------------------------------------------------------
# Percorso di output
# ------------------------------------------------------------
OUTPUT_DIR = r"E:\Didattica\MQF\Github\CORSO-MQF\graphics"
OUTPUT     = os.path.join(OUTPUT_DIR, "Cap04_Figura_4_2.png")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ------------------------------------------------------------
# Geometria dell'albero (coerente con Figura 4.1)
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
COLOR_LABEL     = '#444444'
COLOR_ARROW     = '#999999'
RADIUS         = 0.33
LW_ARROW       = 2.6
FONT_NODE      = 22    # aggiustato manualmente
FONT_LABEL_BOX = 18
FONT_AXIS      = 24
FONT_SIGMA     = 18
FONT_LEGEND    = 20

# Palette colori per i blocchi informativi
PALETTES = {
    0: {0: '#E8EAF6'},
    1: {1: '#D6EAF8',  0: '#FDEBD0'},
    2: {2: '#D5F5E3',  1: '#FCF3CF',  0: '#FADBD8'},
    3: {3: '#EBF5FB',  2: '#EAFAF1',  1: '#FEF9E7',  0: '#FDEDEC'},
}

# Etichette degli insiemi informativi sopra ogni box
SIGMA_LABELS = {
    (0, 0): r'$\mathcal{F}_0$: $\Omega$',
    (1, 1): r'$A_u$',
    (1, 0): r'$A_d$',
    (2, 2): r'$A_{uu}$',
    (2, 1): r'$A_{ud}$',
    (2, 0): r'$A_{dd}$',
    (3, 3): r'$\{uuu\}$',
    (3, 2): r'$\{uu\!d\}$',
    (3, 1): r'$\{u\!dd\}$',
    (3, 0): r'$\{ddd\}$',
}

BOX_W = 0.72
BOX_H = 0.68

# ------------------------------------------------------------
# Box colorati (sfondo informativo)
# ------------------------------------------------------------
for (t, k), (x, y, v) in nodes.items():
    color = PALETTES[t][k]
    box = FancyBboxPatch(
        (x - BOX_W / 2, y - BOX_H / 2), BOX_W, BOX_H,
        boxstyle='round,pad=0.04',
        facecolor=color, edgecolor='#AAAAAA',
        lw=0.9, zorder=1, alpha=0.88)
    ax.add_patch(box)

# ------------------------------------------------------------
# Archi
# ------------------------------------------------------------
for t in range(T):
    for k in range(t + 1):
        x0, y0, _ = nodes[(t,   k)]
        xu, yu, _ = nodes[(t+1, k+1)]
        xd, yd, _ = nodes[(t+1, k  )]
        for xy_end in [(xu, yu), (xd, yd)]:
            ax.annotate('', xy=xy_end, xytext=(x0, y0),
                arrowprops=dict(arrowstyle='-|>', color=COLOR_ARROW,
                    lw=LW_ARROW, mutation_scale=16,
                    shrinkA=RADIUS*72, shrinkB=RADIUS*72))

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
# Etichette insiemi informativi (sopra ogni box)
# ------------------------------------------------------------
for (t, k), label in SIGMA_LABELS.items():
    x, y, _ = nodes[(t, k)]
    ax.text(x, y + BOX_H / 2 + 0.18, label,
            ha='center', va='bottom',
            fontsize=FONT_LABEL_BOX, color='#333333', zorder=5)

# ------------------------------------------------------------
# Asse dei tempi e nomi sigma-algebre
# ------------------------------------------------------------
y_min  = min(y for _, y, _ in nodes.values())
y_axis = y_min - 0.80

for t in range(T + 1):
    x_t = nodes[(t, 0)][0]
    ax.text(x_t, y_axis, f'$t={t}$', ha='center', va='top',
            fontsize=FONT_AXIS, color=COLOR_LABEL)

sigma_names = [
    r'$\mathcal{F}_0 = \{\emptyset,\Omega\}$',
    r'$\mathcal{F}_1 = \sigma(S_1)$',
    r'$\mathcal{F}_2 = \sigma(S_1,S_2)$',
    r'$\mathcal{F}_3 = \sigma(S_1,S_2,S_3)$',
]
for t, name in enumerate(sigma_names):
    x_t = nodes[(t, 0)][0]
    ax.text(x_t, y_axis - 0.55, name, ha='center', va='top',
            fontsize=FONT_SIGMA, color='#555555', style='italic')

ax.axhline(y=y_axis + 0.22, color='#CCCCCC', lw=0.9,
           xmin=0.0, xmax=1.0, clip_on=False)

# ------------------------------------------------------------
# Legenda: a destra dell'albero, centrata verticalmente
# ------------------------------------------------------------
legend_patches = [
    mpatches.Patch(color=PALETTES[0][0], ec='#AAAAAA',
                   label=r'$\mathcal{F}_0$: blocco $\Omega$'),
    mpatches.Patch(color=PALETTES[1][1], ec='#AAAAAA',
                   label=r'$\mathcal{F}_1$: blocco $A_u$'),
    mpatches.Patch(color=PALETTES[1][0], ec='#AAAAAA',
                   label=r'$\mathcal{F}_1$: blocco $A_d$'),
    mpatches.Patch(color=PALETTES[2][2], ec='#AAAAAA',
                   label=r'$\mathcal{F}_2$: blocco $A_{uu}$'),
    mpatches.Patch(color=PALETTES[2][1], ec='#AAAAAA',
                   label=r'$\mathcal{F}_2$: blocco $A_{ud}$'),
    mpatches.Patch(color=PALETTES[2][0], ec='#AAAAAA',
                   label=r'$\mathcal{F}_2$: blocco $A_{dd}$'),
]
y_center = (max(y for _, y, _ in nodes.values()) + y_min) / 2
x_leg    = nodes[(T, 0)][0] + 0.90
ax.legend(
    handles=legend_patches,
    loc='center left',
    bbox_to_anchor=(x_leg, y_center),
    bbox_transform=ax.transData,
    fontsize=FONT_LEGEND,
    framealpha=0.97,
    edgecolor='#BBBBBB',
    ncol=1,
    handlelength=2.2,
    handleheight=1.4,
    borderpad=1.0,
    labelspacing=0.8,
    title='Insiemi informativi',
    title_fontsize=FONT_LEGEND,
)

# ------------------------------------------------------------
# Margini e salvataggio
# ------------------------------------------------------------
x_max = nodes[(T, 0)][0]
ax.set_xlim(-0.70, x_max + 5.2)
ax.set_ylim(y_axis - 0.90, max(y for _, y, _ in nodes.values()) + 0.85)

plt.tight_layout()
plt.savefig(OUTPUT, dpi=200, bbox_inches='tight', facecolor='white')
plt.close()
print(f'Figura salvata in: {OUTPUT}')
