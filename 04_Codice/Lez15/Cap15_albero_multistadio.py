"""Figura 15.3. Albero a quattro stadi con decisioni adattate alla storia.

Tempi decisionali: 0, 1, 3, 4. Il tempo 2 e' informativo intermedio.
La figura aggrega (Z_2,Z_3) nelle etichette C_1 e C_2.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle


# Lo script salva le immagini in graphics/ se eseguito dal repository,
# altrimenti nella cartella che lo contiene.
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[1] if len(SCRIPT_DIR.parents) > 1 else SCRIPT_DIR
OUT_DIR = REPO_ROOT / "graphics" if (REPO_ROOT / "00_MasterPlan").is_dir() else SCRIPT_DIR
OUT_DIR.mkdir(parents=True, exist_ok=True)

BLU = "#2b4c7e"
ROSSO = "#c0502e"
GRIGIO = "#808080"
TESTO = "#303943"

# La scala verticale e' aumentata appositamente per separare
# le otto coppie di etichette terminali.
Y_TERMINALI = {
    ("A", 1, 1): 16.0,
    ("A", 1, 2): 14.0,
    ("A", 2, 1): 12.0,
    ("A", 2, 2): 10.0,
    ("B", 1, 1): 8.0,
    ("B", 1, 2): 6.0,
    ("B", 2, 1): 4.0,
    ("B", 2, 2): 2.0,
}
Y_STADIO_3 = {("A", 1): 15.0, ("A", 2): 11.0,
              ("B", 1): 7.0, ("B", 2): 3.0}
Y_STADIO_2 = {"A": 13.0, "B": 5.0}

X0, X1, X2, X3, X4 = 0.0, 2.4, 5.0, 8.3, 11.2
FIG_W, FIG_H = 19, 12.3


def edge(ax, p, q, highlighted=False):
    ax.plot([p[0], q[0]], [p[1], q[1]],
            color=ROSSO if highlighted else GRIGIO,
            lw=2.5 if highlighted else 1.25,
            zorder=2, solid_capstyle="round")


def node(ax, p, filled=True):
    ax.scatter([p[0]], [p[1]], s=95,
               facecolor=BLU if filled else "white",
               edgecolor=BLU, linewidth=1.5, zorder=5)


def label(ax, x, y, value, size=11.5, color=TESTO, **kwargs):
    ax.text(x, y, value, fontsize=size, color=color, zorder=6, **kwargs)


def main():
    plt.rcParams["font.family"] = "DejaVu Sans"
    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    fig.patch.set_facecolor("white")

    # Fasce di stadio; l'area terminale e' intenzionalmente piu' larga
    # per accogliere le etichette g_4 con l'intera storia informativa.
    bands = [
        (-0.9, 1.1, 1, r"$\mathcal{T}_1=\{0\}$", "decide $x$", "#eef2f8"),
        (1.1, 3.4, 2, r"$\mathcal{T}_2=\{1\}$", "osserva $Z_1$; decide $u_1$", "#f7f3ee"),
        (3.4, 9.8, 3, r"$\mathcal{T}_3=\{2,3\}$", "osserva $(Z_2,Z_3)$; decide $(u_2,u_3)$", "#eef2f8"),
        (9.8, 17.2, 4, r"$\mathcal{T}_4=\{4\}$", "osserva $Z_4$; decide $g_4$", "#f7f3ee"),
    ]
    for left, right, stage, times, desc, bg in bands:
        ax.add_patch(Rectangle((left, 0.8), right - left, 17.3,
                               color=bg, linewidth=0, zorder=0))
        mx = (left + right) / 2
        label(ax, mx, 19.85, f"Stadio {stage}", size=15.3, color=BLU,
              ha="center", va="center", fontweight="bold")
        label(ax, mx, 19.15, times, size=13.5, color=BLU,
              ha="center", va="center")
        label(ax, mx, 18.55, desc, size=10.7, color=TESTO,
              ha="center", va="center")
    for sep in (1.1, 3.4, 9.8):
        ax.plot([sep, sep], [0.8, 18.1], color=BLU, lw=0.8, ls=":", alpha=0.7)

    root = (X0, 9.0)
    node(ax, root)
    label(ax, X0, 9.48, r"$x$", size=14, color=BLU, ha="center")

    for a in ("A", "B"):
        p1 = (X1, Y_STADIO_2[a])
        p2 = (X2, Y_STADIO_2[a])
        edge(ax, root, p1, highlighted=(a == "A"))
        edge(ax, p1, p2, highlighted=(a == "A"))
        node(ax, p1)
        node(ax, p2, filled=False)

        # Realizzazione sempre sopra, decisione sempre sotto.
        label(ax, X1, p1[1] + 0.45, rf"$Z_1={a}$", size=12.6,
              color=BLU, ha="center", va="bottom")
        label(ax, X1, p1[1] - 0.45, rf"$u_1({a})$", size=12.6,
              color=BLU, ha="center", va="top")

        for c in (1, 2):
            p3 = (X3, Y_STADIO_3[(a, c)])
            selected = (a == "A" and c == 2)
            edge(ax, p2, p3, highlighted=selected)
            node(ax, p3)

            label(ax, X3, p3[1] + 0.53,
                  rf"$(Z_2,Z_3)=C_{c}$", size=12.2,
                  color=BLU, ha="center", va="bottom")
            # Componenti distinte, ma scelte insieme al termine di stadio 3.
            label(ax, X3, p3[1] - 0.50,
                  rf"$u_2({a},C_{c}),\ u_3({a},C_{c})$", size=11.6,
                  color=BLU, ha="center", va="top")

            for d in (1, 2):
                p4 = (X4, Y_TERMINALI[(a, c, d)])
                edge(ax, p3, p4, highlighted=selected and d == 1)
                node(ax, p4)
                # Etichette terminali a destra dei nodi (anziche' tra
                # gli archi): nessuna sovrapposizione fra gli otto rami.
                tx = X4 + 0.42
                label(ax, tx, p4[1] + 0.21, rf"$Z_4=D_{d}$",
                      size=11.0, color=BLU, ha="left", va="bottom")
                label(ax, tx, p4[1] - 0.20,
                      rf"$g_4({a},C_{c},D_{d})$",
                      size=11.0, color=BLU, ha="left", va="top")

    for xx, t in ((X0, 0), (X1, 1), (X2, 2), (X3, 3), (X4, 4)):
        label(ax, xx, 0.33, rf"$t={t}$", size=12.3,
              ha="center", va="center", color=TESTO)

    handles = [
        Line2D([], [], color=BLU, marker="o", linestyle="None", markersize=8,
               label="nodo decisionale"),
        Line2D([], [], color=BLU, marker="o", linestyle="None", markersize=8,
               markerfacecolor="white", label="nodo informativo intermedio"),
        Line2D([], [], color=ROSSO, lw=2.5,
               label="percorso evidenziato: $(A,C_2,D_1)$"),
    ]
    ax.legend(handles=handles, loc="lower center", bbox_to_anchor=(0.5, -0.07),
              ncol=3, frameon=False, fontsize=11)
    ax.set_title("Albero degli scenari a 4 stadi: informazioni e decisioni",
                 fontsize=17, color=BLU, pad=24)
    ax.set_xlim(-1.0, 17.3)
    ax.set_ylim(0.0, 20.5)
    ax.axis("off")
    fig.subplots_adjust(left=0.035, right=0.985, top=0.90, bottom=0.11)

    base = "Cap15_albero_multistadio"
    png = OUT_DIR / f"{base}.png"
    svg = OUT_DIR / f"{base}.svg"
    fig.savefig(png, dpi=220, bbox_inches="tight", facecolor="white")
    fig.savefig(svg, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"PNG: {png}\nSVG: {svg}")


if __name__ == "__main__":
    main()
