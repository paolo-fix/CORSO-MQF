from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Patch


# ============================================================
# Cartella temporanea di controllo
# ============================================================

out_dir = Path(r"E:\Didattica\MQF\graphics")
out_dir.mkdir(parents=True, exist_ok=True)

png_path = out_dir / "Cap11_confronto_redditivita_resilienza.png"
svg_path = out_dir / "Cap11_confronto_redditivita_resilienza.svg"


# ============================================================
# Dati delle due politiche
# ============================================================

asset_classes = [
    "Cassa e riserve",
    "Titoli a breve scadenza",
    "Titoli a lunga scadenza",
    "Prestiti e impieghi meno liquidi",
]

policy_labels = [
    "Politica A\norientata alla redditività",
    "Politica B\nmaggiore resilienza",
]

policy_a = [0.000, 41.045, 20.896, 38.060]
policy_b = [10.000, 54.286, 30.000, 5.714]

data_by_asset = [
    [policy_a[0], policy_b[0]],
    [policy_a[1], policy_b[1]],
    [policy_a[2], policy_b[2]],
    [policy_a[3], policy_b[3]],
]


# ============================================================
# Scala cromatica
# Blu decrescente al diminuire della liquidabilità
# ============================================================

colors = [
    "#0B3C5D",  # Cassa e riserve
    "#1D70A2",  # Titoli a breve scadenza
    "#5FA8D3",  # Titoli a lunga scadenza
    "#A9D6E5",  # Prestiti e impieghi meno liquidi
]


# ============================================================
# Indicatori sintetici
# ============================================================

z_a = 3.7649
z_b = 2.9429

liquidity_a = 55.000
liquidity_b = 75.000

stress_loss_a = 7.000
stress_loss_b = 6.043


# ============================================================
# Costruzione della figura
# ============================================================

fig, ax = plt.subplots(figsize=(11.8, 6.0))

left_positions = [0.0, 0.0]
bar_objects = []

for asset, values, color in zip(
    asset_classes,
    data_by_asset,
    colors
):
    bars = ax.barh(
        policy_labels,
        values,
        left=left_positions,
        color=color,
        label=asset
    )

    bar_objects.append(bars)

    for row, (value, left) in enumerate(
        zip(values, left_positions)
    ):
        if value >= 4:
            text_color = (
                "white"
                if color in ("#0B3C5D", "#1D70A2")
                else "black"
            )

            ax.text(
                left + value / 2,
                row,
                f"{value:.1f}",
                ha="center",
                va="center",
                fontsize=9,
                fontweight="bold",
                color=text_color
            )

    left_positions = [
        left_positions[i] + values[i]
        for i in range(len(policy_labels))
    ]


# Indicazione esplicita della quota nulla di cassa
ax.text(
    0.8,
    0,
    "Cassa: 0",
    ha="left",
    va="center",
    fontsize=8.5
)


# ============================================================
# Assi, titolo e griglia
# ============================================================

ax.set_xlim(0, 100)

ax.set_xlabel(
    "Composizione dell'attivo",
    fontsize=10.5
)

ax.set_title(
    "Redditività e resilienza: confronto tra due politiche",
    fontsize=14
)

ax.grid(
    axis="x",
    alpha=0.30
)

ax.set_axisbelow(True)


# ============================================================
# Riquadro con gli indicatori
# ============================================================

summary_text = (
    "Politica A:  "
    f"$z^*={z_a:.4f}$   "
    f"liquidità={liquidity_a:.0f}   "
    f"perdita={stress_loss_a:.3f}\n"
    "Politica B:  "
    f"$z^*={z_b:.4f}$   "
    f"liquidità={liquidity_b:.0f}   "
    f"perdita={stress_loss_b:.3f}"
)

ax.text(
    0.5,
    -0.23,
    summary_text,
    transform=ax.transAxes,
    ha="center",
    va="top",
    fontsize=9.5,
    bbox={
        "boxstyle": "round,pad=0.35",
        "facecolor": "#EAF4F8",
        "edgecolor": "#7AAEC4"
    }
)


# ============================================================
# Legenda
# ============================================================

legend_handles = [
    Patch(
        facecolor=color,
        edgecolor=color,
        label=asset
    )
    for asset, color in zip(asset_classes, colors)
]

ax.legend(
    handles=legend_handles,
    loc="upper center",
    bbox_to_anchor=(0.5, -0.38),
    ncol=2,
    frameon=True
)


# ============================================================
# Salvataggio
# ============================================================

fig.tight_layout()

fig.savefig(
    png_path,
    dpi=300,
    bbox_inches="tight"
)

fig.savefig(
    svg_path,
    bbox_inches="tight"
)

plt.close(fig)

print("Figure salvate in:")
print(png_path)
print(svg_path)