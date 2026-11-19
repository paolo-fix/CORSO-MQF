"""
Cap15_albero_scenari_stadi.py
Albero degli scenari a 4 stadi decisionali, T = 4:
  T_1={0} (x),  T_2={1} (u_1),  T_3={2,3} (u_2,u_3),  T_4={4} (g_4).
Esempio illustrativo: Z_1 in {A,B}; proseguimenti C_1,C_2 per (Z_2,Z_3);
proseguimenti D_1,D_2 per Z_4. Otto scenari.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

# ============================================================
# PERCORSI DI OUTPUT
# ============================================================

# Lo script si trova in <radice progetto>/04_Codice/Lez15.
# Costruire il percorso da __file__ evita dipendenze dal PC in uso.
out_dir = Path(r"E:\Didattica\MQF\graphics")

png_path = out_dir / "Cap15_albero_multistadio.png"
svg_path = out_dir / "Cap15_albero_multistadio.svg"

# ============================================================
# TIPOGRAFIA: tutti i controlli sono raccolti qui
# ============================================================

# Cambia il carattere di tutto il grafico.
FONT_FAMILY = "DejaVu Sans"

# Moltiplicatori globali: 1.10 aumenta tutto del 10%; 0.90 riduce del 10%.
FONT_SCALE = 1.00
LINE_SPACING_SCALE = 1.00

# Dimensioni per categoria.
FONT_SIZES: dict[str, float] = {
    "title": 19.0,
    "stage_title": 17.0,
    "stage_set": 15.0,
    "stage_description": 13,
    "node_label": 15.0,
    "scenario_label": 13,
    "intermediate_label": 13,
    "root_label": 17.0,
    "root_description": 13,
    "ancestor_label": 17.0,
    "ancestor_description": 13,
    "time_label": 15.0,
    "legend": 13.0,
}

# Interlinea per categoria.
LINE_SPACINGS: dict[str, float] = {
    "title": 1.00,
    "stage_title": 1.00,
    "stage_set": 1.00,
    "stage_description": 1.25,
    "node_label": 1.00,
    "scenario_label": 1.00,
    "intermediate_label": 1.00,
    "root_label": 1.00,
    "root_description": 1.00,
    "ancestor_label": 1.00,
    "ancestor_description": 1.20,
    "time_label": 1.00,
    "legend": 1.00,
}

plt.rcParams["font.family"] = FONT_FAMILY


def font_size(category: str) -> float:
    return FONT_SIZES[category] * FONT_SCALE


def line_spacing(category: str) -> float:
    return LINE_SPACINGS[category] * LINE_SPACING_SCALE


# ============================================================
# STRUTTURA DELL'ALBERO
# ============================================================

BLU, ROSSO, GRIGIO = "#2b4c7e", "#c0502e", "#8a8a8a"
DX = 2.0
X = lambda t: t * DX

# Lo Stadio 4 e i relativi rami occupano metà della larghezza originaria.
X_STADIO_4 = X(3) + DX / 2
FINE_STADIO_4 = 6.45 + (11.3 - 6.45) / 2

ymin, ymax = -5.6, 6.6
fig, ax = plt.subplots(figsize=(12.5, 7.6))

# ---- fasce degli stadi (intervalli contigui; nodo di stadio sul bordo destro) ----
bande = [
    (1, -1.0, 0.45, r"$\mathcal{T}_1=\{0\}$", "decide $x$", "#eef2f8"),
    (2, 0.45, 2.45, r"$\mathcal{T}_2=\{1\}$", "osserva $Z_1$\ndecide $u_1$", "#f7f3ee"),
    (3, 2.45, 6.45, r"$\mathcal{T}_3=\{2,3\}$", "osserva $(Z_2,Z_3)$\ndecide $(u_2,u_3)$", "#eef2f8"),
    (4, 6.45, FINE_STADIO_4, r"$\mathcal{T}_4=\{4\}$", "osserva $Z_4$\ndecide $g_4$", "#f7f3ee"),
]
for k, x0, x1, T, testo, col in bande:
    ax.add_patch(Rectangle((x0, ymin), x1 - x0, ymax - ymin, color=col, lw=0, zorder=0))
    xm = (x0 + x1) / 2
    ax.text(xm, ymax - 0.3, f"Stadio {k}", ha="center", va="top",
            fontsize=font_size("stage_title"), color=BLU, weight="bold",
            linespacing=line_spacing("stage_title"))
    ax.text(xm, ymax - 0.95, T, ha="center", va="top",
            fontsize=font_size("stage_set"), color=BLU,
            linespacing=line_spacing("stage_set"))
    ax.text(xm, ymax - 1.55, testo, ha="center", va="top",
            fontsize=font_size("stage_description"), color="#555",
            linespacing=line_spacing("stage_description"))
for xb in (0.45, 2.45, 6.45):
    ax.plot([xb, xb], [ymin, ymax], color=BLU, lw=1, ls=":", zorder=0.5)

def arco(p, q, rosso=False):
    ax.plot([p[0], q[0]], [p[1], q[1]], color=ROSSO if rosso else GRIGIO,
            lw=2.4 if rosso else 1.3, zorder=1)
def pieno(p):
    ax.scatter(*p, s=210, color=BLU, edgecolor="white", lw=1.5, zorder=3)
def vuoto(p):
    ax.scatter(*p, s=120, facecolor="white", edgecolor=BLU, lw=1.6, zorder=3)

yZ1 = {"A": 2.0, "B": -2.0}
yC = {("A", 1): 3.0, ("A", 2): 1.0, ("B", 1): -1.0, ("B", 2): -3.0}
n_path = ("A", 2)                              # n = nodo di stadio 3 (A, C_2)

root = (X(0), 0.0)
i = 0
for z in ("A", "B"):
    nz = (X(1), yZ1[z])
    arco(root, nz)
    for c in (1, 2):
        yc = yC[(z, c)]
        red = (z, c) == n_path
        p2, p3 = (X(2), yc), (X(3), yc)
        arco(nz, p2, red); arco(p2, p3, red)
        vuoto(p2)
        ax.text(p2[0] - 0.1, yc + 0.28, f"$C_{c}$",
                fontsize=font_size("intermediate_label"), color="#555", ha="right",
                linespacing=line_spacing("intermediate_label"))
        for d, dy in ((1, 0.5), (2, -0.5)):
            i += 1
            p4 = (X_STADIO_4, yc + dy)
            arco(p3, p4)
            pieno(p4)
            ax.text(p4[0] + 0.3, p4[1], f"$s_{i}=({z},C_{c},D_{d})$",
                    va="center", fontsize=font_size("scenario_label"), color=BLU,
                    linespacing=line_spacing("scenario_label"))
        pieno(p3)
    pieno(nz)
    ax.text(nz[0], nz[1] + (0.5 if z == "A" else -0.8),
            f"$Z_1={z},\\ u_1({z})$", ha="center",
            fontsize=font_size("node_label"), color=BLU,
            linespacing=line_spacing("node_label"))
pieno(root)
ax.text(root[0], root[1] + 0.5, "$x$", ha="center",
        fontsize=font_size("root_label"), color=BLU,
        linespacing=line_spacing("root_label"))
ax.text(root[0], root[1] - 0.75, "radice", ha="center",
        fontsize=font_size("root_description"), color="#555",
        linespacing=line_spacing("root_description"))

# antenato di stadio a(n) -> n  (n allo stadio 3, a(n) allo stadio 2)
a, n = (X(1), yZ1["A"]), (X(3), yC[n_path])
for p in (a, n):
    ax.scatter(*p, s=470, facecolor="none", edgecolor=ROSSO, lw=2.2, zorder=4)
ax.add_patch(FancyArrowPatch((a[0] + 0.15, a[1] - 0.25), (n[0] - 0.25, n[1] - 0.3),
             connectionstyle="arc3,rad=0.22", arrowstyle="-|>", mutation_scale=14,
             color=ROSSO, lw=1.8, ls="--", zorder=2))
ax.text(a[0] - 0.35, a[1] + 0.05, "$a(n)$", color=ROSSO,
        fontsize=font_size("ancestor_label"), ha="right", va="center",
        linespacing=line_spacing("ancestor_label"))
ax.text(n[0] + 0.1, n[1] - 0.45, "$n$", color=ROSSO,
        fontsize=font_size("ancestor_label"), ha="left",
        linespacing=line_spacing("ancestor_label"))
ax.text(X(3) - 0.1, n[1] + 0.35, "$(u_2,u_3)(n)$", color=ROSSO,
        fontsize=font_size("scenario_label"), ha="center",
        linespacing=line_spacing("scenario_label"))
ax.text(X(2.55), 0.22, "antenato di stadio:\nsalta il tempo intermedio $t=2$",
        color=ROSSO, fontsize=font_size("ancestor_description"), ha="center", va="top",
        linespacing=line_spacing("ancestor_description"))

for t in range(5):
    x_t = X_STADIO_4 if t == 4 else X(t)
    ax.text(x_t, ymin + 0.3, f"$t={t}$", ha="center", color="#555",
            fontsize=font_size("time_label"),
            linespacing=line_spacing("time_label"))

ax.scatter([], [], s=150, color=BLU, label="nodo di stadio (decisione), a $t_{k,n_k}$")
ax.scatter([], [], s=100, facecolor="white", edgecolor=BLU, lw=1.6,
           label="nodo informativo intermedio (nessuna decisione)")
legend = ax.legend(
    loc="lower center",
    bbox_to_anchor=(0.5, -0.09),
    ncol=2,
    frameon=False,
    fontsize=font_size("legend")
)
for legend_text in legend.get_texts():
    legend_text.set_linespacing(line_spacing("legend"))

ax.set_title("Albero degli scenari a 4 stadi: stadi, tempi e antenato",
             fontsize=font_size("title"), color=BLU, pad=10,
             linespacing=line_spacing("title"))
ax.set_xlim(-1.0, FINE_STADIO_4); ax.set_ylim(ymin, ymax)
ax.axis("off")
fig.tight_layout()
fig.savefig(png_path, dpi=300, bbox_inches="tight")
fig.savefig(svg_path, bbox_inches="tight")
plt.close(fig)

print("File salvati:")
print(png_path)
print(svg_path)
