from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# ============================================================
# PERCORSO E PARAMETRI DI SALVATAGGIO
# ============================================================

OUTPUT_DIR = Path(r"E:\Didattica\MQF\graphics")
OUTPUT_STEM = "Cap15_albero_ternario_non_anticipativita"

PNG_DPI = 300
SAVE_BBOX = "tight"
SAVE_PAD_INCHES = 0.04

# ============================================================
# TIPOGRAFIA E COLORI
# ============================================================

FONT_FAMILY = "DejaVu Sans"
FONT_SCALE = 1.00  # Scala globale: 1.10 aumenta tutti i testi del 10%.
LINE_SPACING_SCALE = 1.00  # Moltiplicatore delle interlinee dei testi multilinea.
plt.rcParams["font.family"] = FONT_FAMILY
# Testi SVG convertiti in tracciati: stesso aspetto anche senza il font installato.
plt.rcParams["svg.fonttype"] = "path"

FONT_SIZES = {
    "title": 19.0,
    "label": 16,
    "annotation": 15,
    "axis": 15,
    "footer": 14,
}

LINE_SPACINGS = {
    "title": 1.15,
    "label": 1.20,
    "annotation": 1.25,
    "axis": 1.00,
    "footer": 1.30,
}


def text_style(category):
    """Font e interlinea condivisi da tutti i testi della categoria."""
    return dict(fontsize=FONT_SIZES[category] * FONT_SCALE,
                linespacing=LINE_SPACINGS[category] * LINE_SPACING_SCALE)


# Dimensioni in pollici; margini come frazioni della figura.
# Formato calibrato sulle coordinate dell'albero e delle annotazioni.
# Ridurre solo il primo valore comprime orizzontalmente testi e bande;
# per una versione piu' stretta vanno ricalibrate anche le posizioni x.
FIG_SIZE = (12.0, 7.2)
PLOT_MARGINS = dict(left=0.05, right=0.98, bottom=0.15, top=0.84)
X_LIMITS = (-0.40, 3.35)
Y_LIMITS = (-3.95, 4.00)
TITLE_Y = 0.97  # Quota del titolo nella figura.
COLOR_NOTE_Y = 0.90  # Nota sui colori, sopra l'albero.
FOOTER_Y = 0.045  # Nota finale, separata dalla riga delle date.

# Date: x in coordinate dei dati, y in frazioni dell'altezza degli assi.
TIME_LABEL_Y = -0.06  # Diminuire per allontanare tutte le date dall'albero.
CONTINUATION_X = 2.62
CONTINUATION_DOTS_Y = -0.005

# Offset delle etichette dei nodi in punti tipografici (indipendenti dagli assi).
STATE_LABEL_OFFSET = (-10, 32)
ROOT_LABEL_OFFSET = (0, 20)
# Posizioni assolute delle due spiegazioni in coordinate dei dati.
U1_NOTE_POSITION = (0.02, 3.30)
U2_NOTE_POSITION = (2.55, -2.00)
NOTE_ARROW_WIDTH = 1.2
NOTE_ARROW_CURVATURE = 0.0
NODE_SIZE = 170
HIGHLIGHT_NODE_SIZE = 260
FAN_DX = 0.34
FAN_DY = 0.18

COL_STRUCT = "#2A4B7C"
COL_ACCENT = "#C24D2C"
COL_MUTED = "#7A7A7A"

# Bande di sfondo (una per ciascun valore di Z_1), a indicare i gruppi
# entro cui u_1^s deve essere costante.
BAND_COLORS = ["#DCE6F5", "#FBE7DE", "#E4EFE0"]

# ============================================================
# STRUTTURA DELL'ALBERO
# ============================================================

# Illustra l'Esercizio "Una catena a tre stati" (Sez. 5, catena omogenea a
# tre stati esogeni, T=4): albero ternario, disegnato per intero fino alla
# profondita' 2 (9 nodi) e troncato con "..." verso t=3,4 (|S|=3^4=81).
# A differenza della Fig. "albero generico", qui non si evidenziano un
# nodo n e il suo antenato in astratto: si mostrano invece gli elementi
# dell'esercizio, cioe' i raggruppamenti di scenari imposti dalla
# misurabilita' di u_1^s e u_2^s (punto (ii) dell'esercizio).

N_LEAVES = 9
LEAF_STEP = 0.85

leaf_ys = [(j - (N_LEAVES - 1) / 2) * LEAF_STEP for j in range(N_LEAVES)]
positions = {
    2: [(2, y) for y in leaf_ys],
    1: [(1, leaf_ys[3 * i + 1]) for i in range(3)],
}
positions[0] = [(0, sum(y for _, y in positions[1]) / 3)]


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


# ============================================================
# FIGURA
# ============================================================

fig, ax = plt.subplots(figsize=FIG_SIZE)
fig.subplots_adjust(**PLOT_MARGINS)
ax.set_xlim(*X_LIMITS)
ax.set_ylim(*Y_LIMITS)
ax.axis("off")

root_x, root_y = positions[0][0]

# bande di sfondo: un ramo di profondita' 1 = un valore di Z_1 = un
# gruppo entro cui u_1^s e' costante. Ciascuna banda parte dal proprio
# nodo di profondita' 1 (non dalla radice, comune a tutti gli scenari e
# priva di un valore di Z_1 assegnato), cosi' da restare aderente ai rami
# che deve evidenziare senza invadere i rami vicini. La banda e' a forma
# di imbuto: si allarga da un punto (il nodo Z_1) alla piena larghezza
# gia' in corrispondenza dei tre figli (x=2), non oltre, cosi' da
# racchiuderli visibilmente tutti e tre; da x=2 in poi prosegue a
# larghezza costante fino al troncamento.
NODE_X = 2  # ascissa dei nodi di profondita' 2
for i in range(3):
    branch_x, branch_y = positions[1][i]
    child_ys = [positions[2][3 * i + k][1] for k in range(3)]
    # il margine deve allargare la banda OLTRE i figli estremi, non
    # restringerla verso il centro: minimo - margine, massimo + margine.
    y_lo = min(child_ys) - LEAF_STEP / 2
    y_hi = max(child_ys) + LEAF_STEP / 2
    assert y_lo < min(child_ys) and y_hi > max(child_ys)
    poly = Polygon(
        [(branch_x, branch_y), (NODE_X, y_hi), (2.85, y_hi), (2.85, y_lo), (NODE_X, y_lo)],
        closed=True, facecolor=BAND_COLORS[i], edgecolor="none",
        zorder=0, alpha=0.9,
    )
    ax.add_patch(poly)

# rami
for d in range(2):
    parents = positions[d]
    children = positions[d + 1]
    for i, (px, py) in enumerate(parents):
        for (cx, cy) in children[3 * i: 3 * i + 3]:
            ax.plot([px, cx], [py, cy], color=COL_MUTED, lw=1.3, zorder=1)

# troncamento verso t=3,4: da ciascuno dei 9 nodi, un piccolo ventaglio di
# 3 trattini corti (27 in tutto) accenna all'ulteriore diramazione ternaria
# verso t=3, senza disegnarla per intero.
for (x, y) in positions[2]:
    for dy in (FAN_DY, 0.0, -FAN_DY):
        ax.plot([x, x + FAN_DX], [y, y + dy], color=COL_MUTED, lw=0.9,
                linestyle=(0, (1, 1.2)), zorder=1)

# nodo di esempio per u_2: un SINGOLO nodo a t=2 fissa (Z_1,Z_2), quindi
# tutti gli scenari che vi proseguono oltre (verso t=3,4, non disegnati)
# condividono lo stesso u_2^s. Non e' un raggruppamento fra i tre fratelli
# a t=2 (quelli hanno Z_2 diverso, quindi u_2^s diverso): e' un solo nodo
# e la sua continuazione tratteggiata.
u2_node = positions[2][1]   # nodo centrale del ramo Z_1=z_1

# nodi
for d in (0, 1, 2):
    for (x, y) in positions[d]:
        ax.scatter([x], [y], s=NODE_SIZE, color=COL_STRUCT, zorder=3,
                   edgecolor="white", linewidth=1.0)

# etichette Z_1=z_j sui nodi di profondita' 1 (z_3, il ramo di esempio
# evidenziato in rosso poco sotto, viene escluso qui ed etichettato la')
for i, (x, y) in enumerate(positions[1]):
    if i == 2:
        continue
    ax.annotate(f"$Z_1=z_{{{i + 1}}}$", xy=(x, y),
                xytext=STATE_LABEL_OFFSET, textcoords="offset points",
                ha="right", va="bottom", **text_style("annotation"), color=COL_STRUCT)

ax.annotate(r"$x$" + "\n(radice)", xy=(root_x, root_y),
            xytext=ROOT_LABEL_OFFSET, textcoords="offset points",
            ha="center", va="bottom", **text_style("label"), color=COL_STRUCT)

for d in (0, 1, 2):
    ax.text(d, TIME_LABEL_Y, f"$t={d}$", transform=ax.get_xaxis_transform(),
            ha="center", va="top", **text_style("axis"), color=COL_MUTED)
ax.text(CONTINUATION_X, TIME_LABEL_Y, r"$t=3,4$",
        transform=ax.get_xaxis_transform(), ha="center", va="top",
        **text_style("axis"), color=COL_MUTED)
ax.text(CONTINUATION_X, CONTINUATION_DOTS_Y, r"$\cdots$",
        transform=ax.get_xaxis_transform(), ha="center", va="center",
        **text_style("axis"), color=COL_MUTED)

# evidenzia il nodo di esempio e ricolora il suo ventaglio di continuazione
ax.scatter([u2_node[0]], [u2_node[1]], s=HIGHLIGHT_NODE_SIZE, facecolor="none",
           edgecolor=COL_ACCENT, linewidth=2.2, zorder=4)
for dy in (FAN_DY, 0.0, -FAN_DY):
    ax.plot([u2_node[0], u2_node[0] + FAN_DX], [u2_node[1], u2_node[1] + dy],
            color=COL_ACCENT, lw=1.4, linestyle=(0, (1, 1.2)), zorder=4)
ax.annotate(
    "Fissa $(Z_1,Z_2)$:\nchi qui prosegue\ncondivide $u_2^s$",
    xy=(u2_node[0] + 0.08, u2_node[1]), xytext=U2_NOTE_POSITION,
    ha="left", va="bottom", **text_style("annotation"), color=COL_ACCENT,
    arrowprops=dict(arrowstyle="-", color=COL_ACCENT, lw=NOTE_ARROW_WIDTH,
                     connectionstyle=f"arc3,rad={NOTE_ARROW_CURVATURE}"),
)

# per analogia, evidenzia anche il nodo Z_1=z_3: fissa gia' Z_1 da solo,
# quindi tutti i suoi discendenti (l'intera banda verde) condividono u_1^s.
# La sua etichetta "Z_1=z_3" (esclusa dal ciclo sopra) diventa rossa e si
# collega al nodo con una linea di indicazione, come per il nodo (Z_1,Z_2).
z3_node = positions[1][2]
ax.scatter([z3_node[0]], [z3_node[1]], s=HIGHLIGHT_NODE_SIZE, facecolor="none",
           edgecolor=COL_ACCENT, linewidth=2.2, zorder=4)
ax.annotate(
    "$Z_1=z_3$: fissa $Z_1$\nChi discende da qui\ncondivide $u_1^s$",
    xy=(z3_node[0] - 0.06, z3_node[1] + 0.10), xytext=U1_NOTE_POSITION,
    ha="left", va="bottom", **text_style("annotation"), color=COL_ACCENT,
    arrowprops=dict(arrowstyle="-", color=COL_ACCENT, lw=NOTE_ARROW_WIDTH,
                     connectionstyle=f"arc3,rad={NOTE_ARROW_CURVATURE}"),
)

fig.text(0.50, COLOR_NOTE_Y, "stesso colore $\\Rightarrow$ stesso $u_1^s$ (dipende solo da $Z_1$)",
         ha="center", va="center", **text_style("annotation"), color=COL_MUTED)

fig.text(0.50, FOOTER_Y,
         r"$|\mathcal{S}|=3^4=81$; albero rappresentato fino a $t=2$, con prosecuzione verso $t=3,4$.",
         ha="center", va="bottom", **text_style("footer"), color=COL_MUTED)

fig.suptitle("Esercizio: catena omogenea a tre stati ($T=4$)",
             y=TITLE_Y, **text_style("title"), color=COL_STRUCT)

save_figure(fig, OUTPUT_STEM)
