from pathlib import Path

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
plt.rcParams["font.family"] = FONT_FAMILY

FONT_SIZES = {
    "title": 19,
    "node": 16.0,
    "annotation": 15.0,
}

COL_STRUCT = "#2A4B7C"
COL_ACCENT = "#C24D2C"
COL_MUTED = "#7A7A7A"
COL_BG_BOX = "#EDF1F7"
COL_BG_ACCENT = "#F7E9E4"

# ============================================================
# CONTROLLI DI LAYOUT (regolabili a mano, in ordine dal basso verso l'alto)
# ============================================================

APEX_GAP = 0.40            # spazio fra la cima del box del vincolo e la
                            # "canalina" tratteggiata orizzontale
ANNOTATION_GAP = 0.40      # spazio fra la canalina e il sottotitolo
TITLE_GAP = 0.35           # spazio fra il sottotitolo e il titolo
TOP_MARGIN = 0.25          # spazio fra il titolo e il bordo superiore del
                            # canvas
# tutti e quattro nella stessa unita' (quella del disegno, non punti):
# si possono confrontare e sommare direttamente fra loro.


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


def add_box(ax, x, y, w, h, text, face, edge, fontsize):
    patch = FancyBboxPatch((x, y), w, h,
                            boxstyle="round,pad=0.03,rounding_size=0.10",
                            linewidth=1.6, edgecolor=edge, facecolor=face, zorder=2)
    ax.add_patch(patch)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=fontsize, color=edge, zorder=3, linespacing=1.25)
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

# Griglia dei box: dimensioni uniformi, ricalcolate per il font piu' grande
# (il testo piu' lungo, "ambiente esogeno", va esplicitamente su due righe
# cosi' la larghezza del box non dipende dal punto esatto a cui e' tarato
# il font).
BOX_W, BOX_H = 2.3, 1.4
GAP_X, GAP_Y = 0.9, 0.9

col_x0 = 0.4                          # X_t, Z_t
col_x1 = col_x0 + BOX_W + GAP_X       # kappa_t, d_t
col_x2 = col_x1 + BOX_W + GAP_X       # (g_t,u_t)
col_x3 = col_x2 + BOX_W + GAP_X       # X_{t+1}

row_y_bottom = 1.2                    # Z_t, d_t
row_y_top = row_y_bottom + BOX_H + GAP_Y     # X_t, kappa_t
row_y_mid = (row_y_bottom + row_y_top) / 2   # (g_t,u_t), X_{t+1}, centrata

# altezza del canvas ricavata dai controlli di layout sopra, cosi' i box
# restano della stessa dimensione qualunque valore diano a APEX_GAP,
# ANNOTATION_GAP, TOP_MARGIN: cambia solo lo spazio bianco in alto.
BOX_C_H = 0.8
box_c_bottom = row_y_top + BOX_H + 0.3   # gap fra kappa_t e il box del vincolo
box_c_top = box_c_bottom + BOX_C_H       # cima del box del vincolo
y_apex = box_c_top + APEX_GAP
y_annotation = y_apex + ANNOTATION_GAP
y_title = y_annotation + TITLE_GAP
ylim_top = y_title + TOP_MARGIN

fig, ax = plt.subplots(figsize=(12.7, ylim_top))
ax.set_xlim(0, col_x3 + BOX_W + 0.4)
ax.set_ylim(0, ylim_top)
ax.axis("off")

b_x0 = add_box(ax, col_x0, row_y_top, BOX_W, BOX_H, r"$X_t$" + "\n(stato interno)",
               COL_BG_BOX, COL_STRUCT, FONT_SIZES["node"])
b_z = add_box(ax, col_x0, row_y_bottom, BOX_W, BOX_H,
              r"$Z_t$" + "\n(ambiente\nesogeno)",
              COL_BG_BOX, COL_STRUCT, FONT_SIZES["node"])
b_k = add_box(ax, col_x1, row_y_top, BOX_W, BOX_H, r"$\kappa_t$" + "\n(solidità)",
              COL_BG_BOX, COL_STRUCT, FONT_SIZES["node"])
b_d = add_box(ax, col_x1, row_y_bottom, BOX_W, BOX_H, r"$d_t$" + "\n(fabbisogno)",
              COL_BG_BOX, COL_STRUCT, FONT_SIZES["node"])
b_u = add_box(ax, col_x2, row_y_mid, BOX_W, BOX_H, r"$(g_t,u_t)$" + "\n(decisioni)",
              COL_BG_BOX, COL_STRUCT, FONT_SIZES["node"])
b_x = add_box(ax, col_x3, row_y_mid, BOX_W, BOX_H, r"$X_{t+1}$" + "\n(stato interno)",
              COL_BG_BOX, COL_STRUCT, FONT_SIZES["node"])
b_c = add_box(ax, col_x1, box_c_bottom, BOX_W, BOX_C_H,
              r"$\kappa_t\geq\kappa_{\min}$",
              COL_BG_ACCENT, COL_ACCENT, FONT_SIZES["annotation"])

# X_t (stato ereditato dalla data precedente) e Z_t (nuova osservazione
# esogena) sono i due ingressi noti a inizio periodo: insieme determinano
# kappa_t = kappa_0 + beta'X_t - h_Z(Z_t); Z_t da solo determina d_t. Ogni
# freccia qui corrisponde a un'equazione scritta nel testo. Il passo va da
# X_t a X_{t+1}: e' una catena lineare (X_0->X_1->X_2->...), non un ciclo,
# quindi non c'e' alcuna freccia di ritorno da disegnare.
add_arrow(ax, b_x0, b_k, side1="right", side2="left")
add_arrow(ax, b_z, b_k, side1="top", side2="bottom")
add_arrow(ax, b_z, b_d, side1="right", side2="left")
add_arrow(ax, b_d, b_u, side1="right", side2="bottom")
add_arrow(ax, b_k, b_c, side1="top", side2="bottom", color=COL_ACCENT)
add_arrow(ax, b_u, b_x, side1="right", side2="left")

# X_t entra anche direttamente nella dinamica dello stato,
# X_{t+1}=A X_t+B u_t+alpha (non solo attraverso kappa_t): la tracciamo
# come collegamento tratteggiato, passando sopra tutte le caselle per non
# tagliare (g_t,u_t), d_t o il vincolo di solidita'.
x0_top = (b_x0[0] + b_x0[2] / 2, b_x0[1] + b_x0[3])   # sommita' di X_t
x1_top = (b_x[0] + b_x[2] / 2, b_x[1] + b_x[3])       # sommita' di X_{t+1}
# y_apex e' gia' calcolato sopra, insieme agli altri controlli di layout

dyn_path = MplPath(
    [(x0_top[0], x0_top[1]), (x0_top[0], y_apex),
     (x1_top[0], y_apex), (x1_top[0], x1_top[1])],
    [MplPath.MOVETO, MplPath.LINETO, MplPath.LINETO, MplPath.LINETO],
)
dyn_arrow = FancyArrowPatch(path=dyn_path, arrowstyle="-|>", mutation_scale=14,
                             color=COL_STRUCT, lw=1.4, linestyle="--", zorder=1,
                             joinstyle="round")
ax.add_patch(dyn_arrow)
ax.text((x0_top[0] + x1_top[0]) / 2, y_annotation,
        r"$X_t$ entra anche direttamente nella dinamica: $X_{t+1}=AX_t+Bu_t+\alpha$",
        fontsize=FONT_SIZES["annotation"], color=COL_STRUCT, ha="center")

# Titolo come testo normale (non ax.set_title), nella stessa unita' di
# misura del sottotitolo, cosi' i due si posizionano con controlli
# omogenei (TITLE_GAP, ANNOTATION_GAP) invece di unita' diverse.
ax.text((col_x0 + col_x3 + BOX_W) / 2, y_title,
        "Schema causale del caso guida SVB--ALM",
        fontsize=FONT_SIZES["title"], color=COL_STRUCT, ha="center", va="bottom")

save_figure(fig, OUTPUT_STEM)
