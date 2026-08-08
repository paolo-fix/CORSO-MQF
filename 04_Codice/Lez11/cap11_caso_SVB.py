from pathlib import Path
import textwrap
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# ============================================================
# Percorso di output
# Modifica se vuoi salvare in una cartella diversa
# ============================================================

out_dir = Path(r"E:\Didattica\MQF\graphics")
out_dir.mkdir(parents=True, exist_ok=True)

png_path = out_dir / "Cap11_SVB_meccanismo_fragilita.png"
svg_path = out_dir / "Cap11_SVB_meccanismo_fragilita.svg"

# ============================================================
# TIPOGRAFIA: tutti i controlli sono raccolti qui
# ============================================================

# Cambia il carattere di tutto il grafico.
FONT_FAMILY = "Aptos Narrow"  # "DejaVu Sans" "Aptos Narrow" "Arial" "Times New Roman"

# Moltiplicatori globali: 1.10 aumenta tutto del 10%; 0.90 riduce del 10%.
FONT_SCALE = 1.00
LINE_SPACING_SCALE = 1.00

# Dimensioni massime per categoria. I testi delle caselle troppo lunghi
# vengono ridotti automaticamente, senza modificare le caselle.
FONT_SIZES: dict[str, float] = {
    "title": 22.0,
    "column_header": 18.0,
    "box": 20.0,
    "arrow_label": 13,
    "decision": 16,
    "note": 8.0,
}

# Interlinea per categoria.
LINE_SPACINGS: dict[str, float] = {
    "title": 1.00,
    "column_header": 1.00,
    "box": 0.96,
    "arrow_label": 1.00,
    "decision": 1.00,
    "note": 1.00,
}

plt.rcParams["font.family"] = FONT_FAMILY


def font_size(category: str) -> float:
    return FONT_SIZES[category] * FONT_SCALE


def line_spacing(category: str) -> float:
    return LINE_SPACINGS[category] * LINE_SPACING_SCALE


# ============================================================
# Impostazioni grafiche di base
# ============================================================

cycle = plt.rcParams["axes.prop_cycle"].by_key()["color"]
c_struct, c_shock, c_mech, c_out = cycle[:4]

fig, ax = plt.subplots(figsize=(15.6, 7.7))
ax.set_xlim(0, 15.6)
ax.set_ylim(0, 7.7)
ax.axis("off")

# ============================================================
# Funzioni di supporto
# ============================================================

box_texts = []


def add_box(
    x, y, w, h, text, edge,
    alpha=0.10, wrap=26
):
    patch = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.025,rounding_size=0.08",
        linewidth=1.6,
        edgecolor=edge,
        facecolor=edge,
        alpha=alpha,
        zorder=2
    )
    ax.add_patch(patch)

    label = ax.text(
        x + w / 2,
        y + h / 2,
        "\n".join(textwrap.wrap(text, width=wrap)),
        ha="center",
        va="center",
        fontsize=font_size("box"),
        fontweight="bold",
        linespacing=line_spacing("box"),
        zorder=3
    )
    box_texts.append((label, x, y, w, h))


def fit_box_texts(pad_x=0.07, pad_y=0.10):
    """Riduce solo i testi che non rientrano nelle rispettive caselle."""
    fig.canvas.draw()

    for label, x, y, w, h in box_texts:
        x0, y0 = ax.transData.transform((x, y))
        x1, y1 = ax.transData.transform((x + w, y + h))
        max_width = abs(x1 - x0) * (1 - 2 * pad_x)
        max_height = abs(y1 - y0) * (1 - 2 * pad_y)

        # L'ingombro del testo è misurato in pixel. Il font viene ridotto
        # proporzionalmente finché larghezza e altezza restano nel box.
        for _ in range(8):
            bbox = label.get_window_extent()
            scale = min(max_width / bbox.width, max_height / bbox.height)
            if scale >= 1:
                break
            label.set_fontsize(label.get_fontsize() * scale * 0.98)

def add_arrow(x1, y1, x2, y2, label=None, rad=0.0, lw=1.5, label_shift=0.12):
    arr = FancyArrowPatch(
        (x1, y1), (x2, y2),
        arrowstyle="-|>",
        mutation_scale=13,
        linewidth=lw,
        color="black",
        connectionstyle=f"arc3,rad={rad}",
        zorder=1
    )
    ax.add_patch(arr)

    if label:
        mx = (x1 + x2) / 2
        my = (y1 + y2) / 2
        ax.text(
            mx,
            my + label_shift,
            label,
            ha="center",
            va="bottom",
            fontsize=font_size("arrow_label"),
            linespacing=line_spacing("arrow_label"),
            bbox=dict(facecolor="white", edgecolor="none", pad=1.2),
            zorder=4
        )

# ============================================================
# Titolo e intestazioni di colonna
# ============================================================

ax.text(
    7.8, 7.35,
    "Meccanismo di fragilità nel caso Silicon Valley Bank",
    ha="center",
    va="center",
    fontsize=font_size("title"),
    fontweight="bold",
    linespacing=line_spacing("title")
)

for x, txt in [
    (1.75, "Vulnerabilità costruite\nprima dello shock"),
    (5.15, "Shock esterni"),
    (8.55, "Pressione sul bilancio"),
    (11.75, "Amplificazione"),
    (14.45, "Esito"),
]:
    ax.text(
        x, 6.72, txt,
        ha="center",
        va="center",
        fontsize=font_size("column_header"),
        fontweight="bold",
        linespacing=line_spacing("column_header")
    )

# ============================================================
# Colonna 1: vulnerabilità pre-shock
# ============================================================

add_box(
    0.25, 4.92, 3.00, 1.02,
    "Elevata esposizione a titoli a lunga scadenza",
    c_struct, wrap=28
)

add_box(
    0.25, 3.15, 3.00, 1.18,
    "Raccolta concentrata e in larga parte non assicurata",
    c_struct, wrap=28
)

add_box(
    0.25, 1.45, 3.00, 1.08,
    "Buffer di liquidità limitato rispetto a deflussi estremi",
    c_struct, wrap=28
)

# ============================================================
# Colonna 2: shock esterni
# ============================================================

add_box(
    3.85, 4.98, 2.60, 0.94,
    "Rapido aumento dei tassi di interesse",
    c_shock, wrap=24
)

add_box(
    3.85, 3.08, 2.60, 1.15,
    "Rallentamento del settore tecnologico e utilizzo dei depositi",
    c_shock, wrap=24
)

# ============================================================
# Colonna 3: pressione sul bilancio
# ============================================================

add_box(
    6.95, 4.88, 2.95, 1.10,
    "Riduzione del valore di mercato dei titoli",
    c_mech, wrap=27
)

add_box(
    6.95, 3.02, 2.95, 1.12,
    "Deflussi di depositi e crescente fabbisogno di cassa",
    c_mech, wrap=27
)

add_box(
    7.05, 1.30, 2.85, 1.08,
    "Necessità di liquidare attività in condizioni sfavorevoli",
    c_mech, wrap=26
)

# ============================================================
# Colonna 4: amplificazione
# ============================================================

add_box(
    10.45, 4.40, 2.55, 1.35,
    "Vendita di titoli con perdite e annuncio di aumento di capitale",
    c_mech, wrap=23
)

add_box(
    10.45, 2.45, 2.55, 1.05,
    "Perdita di fiducia e accelerazione dei prelievi",
    c_mech, wrap=23
)

# ============================================================
# Colonna 5: esito
# ============================================================

add_box(
    13.55, 3.10, 1.80, 1.55,
    "Crisi di liquidità e chiusura della banca",
    c_out, alpha=0.14, wrap=17
)

# ============================================================
# Frecce principali
# ============================================================

add_arrow(3.25, 5.43, 3.85, 5.43)
add_arrow(6.45, 5.43, 6.95, 5.43)

add_arrow(3.25, 3.74, 3.85, 3.63)
add_arrow(6.45, 3.63, 6.95, 3.58)

# Connessioni interne verso la necessità di liquidare
add_arrow(8.42, 4.88, 8.48, 2.38, rad=0.04)
add_arrow(8.45, 3.02, 8.48, 2.38, rad=-0.03)

# Buffer di liquidità limitato -> necessità di liquidare
add_arrow(
    3.25, 1.99, 7.05, 1.82,
    label="minore capacità di assorbire i deflussi",
    label_shift=0.06
)

# Necessità di liquidare -> vendita con perdite
add_arrow(9.90, 1.82, 11.40, 4.40, rad=-0.18)

# Vendita con perdite -> perdita di fiducia
add_arrow(11.72, 4.40, 11.72, 3.50)

# Perdita di fiducia -> crisi finale
add_arrow(13.00, 2.98, 13.55, 3.82)

# Retroazione: nuovi deflussi -> pressione sul bilancio
add_arrow(
    11.00, 2.45, 9.90, 3.32,
    label="retroazione: nuovi deflussi",
    rad=0.33,
    lw=1.3,
    label_shift=-0.20
)

# ============================================================
# Riquadro inferiore: leve ex ante
# ============================================================

decision = FancyBboxPatch(
    (0.25, 0.35), 4.25, 0.66,
    boxstyle="round,pad=0.02,rounding_size=0.06",
    linewidth=1.4,
    edgecolor=c_struct,
    facecolor="white",
    linestyle="--",
    zorder=2
)
ax.add_patch(decision)

ax.text(
    2.375, 0.68,
    "Leve ex ante: composizione dell’attivo,\nbuffer di liquidità e limiti di concentrazione",
    ha="center",
    va="center",
    fontsize=font_size("decision"),
    fontweight="bold",
    linespacing=line_spacing("decision"),
    zorder=3
)

# Nota finale
# ax.text(
#     15.30, 0.48,
#     "Schema interpretativo:\nnon rappresenta una ricostruzione causale esaustiva.",
#     ha="right",
#     va="bottom",
#     fontsize=font_size("note"),
#     linespacing=line_spacing("note"),
#     style="italic"
# )

# ============================================================
# Salvataggio
# ============================================================

fig.tight_layout(pad=0.7)
fit_box_texts()
fig.savefig(png_path, dpi=220, bbox_inches="tight")
fig.savefig(svg_path, bbox_inches="tight")
plt.close(fig)

print("Figura salvata in:")
print(png_path)
print(svg_path)
