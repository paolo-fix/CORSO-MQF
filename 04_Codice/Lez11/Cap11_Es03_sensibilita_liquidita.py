from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

out_dir = Path(r"E:\Didattica\MQF\graphics")
out_dir.mkdir(parents=True, exist_ok=True)

png_path = out_dir / "Cap11_Es03_sensibilita_liquidita.png"
svg_path = out_dir / "Cap11_Es03_sensibilita_liquidita.svg"

# ============================================================
# TIPOGRAFIA: tutti i controlli sono raccolti qui
# ============================================================

FONT_FAMILY = "DejaVu Sans"
FONT_SCALE = 1.00
LINE_SPACING_SCALE = 1.00

FONT_SIZES: dict[str, float] = {
    "title": 19.0,
    "axis_label": 13.0,
    "tick_label": 12.0,
    "point_label": 13.0,
    "delta_label": 13,
    "sensitivity_label": 13,
}

LINE_SPACINGS: dict[str, float] = {
    "title": 1.00,
    "axis_label": 1.00,
    "tick_label": 1.00,
    "point_label": 1.05,
    "delta_label": 1.00,
    "sensitivity_label": 1.15,
}

plt.rcParams["font.family"] = FONT_FAMILY


def font_size(category: str) -> float:
    return FONT_SIZES[category] * FONT_SCALE


def line_spacing(category: str) -> float:
    return LINE_SPACINGS[category] * LINE_SPACING_SCALE


# ============================================================
# Dati
# ============================================================

Q = np.array([55, 56, 57, 58, 59, 60], dtype=float)

lambda_Q = 0.0350746268656716
z55 = 3.764925373134328
z = z55 - lambda_Q * (Q - 55)

Q57 = 57
z57 = z55 - lambda_Q * (Q57 - 55)
z60 = z55 - lambda_Q * (60 - 55)

fig, ax = plt.subplots(figsize=(9.2, 6.0))

line_color = "#2c7fb8"
annotation_color = "#444444"

ax.plot(Q, z, marker="o", linewidth=2.2, color=line_color, zorder=3)

# Etichette dei punti chiave: offset in punti, indipendenti dalla scala degli assi.
for q, zz, offset, ha, va, txt in [
    (55, z55, (8, 10), "left", "bottom",
     r"$Q=55,\; z^*(55)\approx 3.7649$"),
    (57, z57, (8, 10), "left", "bottom",
     r"$Q=57,\; z^*(57)\approx 3.6948$"),
    (60, z60, (-8, -10), "right", "top",
     r"$Q=60,\; z^*(60)\approx 3.5896$"),
]:
    ax.scatter(q, zz, s=52, color=line_color, zorder=4)
    ax.annotate(
        txt,
        xy=(q, zz),
        xytext=offset,
        textcoords="offset points",
        ha=ha,
        va=va,
        fontsize=font_size("point_label"),
        linespacing=line_spacing("point_label"),
        bbox=dict(facecolor="white", edgecolor="none", alpha=0.78, pad=1.2),
        zorder=5
    )

# Variazione orizzontale del requisito di liquidità.
yq = z57 - 0.035
ax.annotate(
    "",
    xy=(57, yq),
    xytext=(55, yq),
    arrowprops=dict(arrowstyle="<->", linewidth=1.4, color=annotation_color)
)
ax.text(
    56,
    yq - 0.008,
    r"$\Delta Q=2$",
    ha="center",
    va="top",
    fontsize=font_size("delta_label"),
    linespacing=line_spacing("delta_label"),
    color=annotation_color
)

# Variazione verticale del valore ottimo, con guide tratteggiate.
xv = 57.28
ax.plot([55, xv], [z55, z55], linestyle=":", linewidth=1.0,
        color=annotation_color, alpha=0.65, zorder=1)
ax.plot([57, xv], [z57, z57], linestyle=":", linewidth=1.0,
        color=annotation_color, alpha=0.65, zorder=1)
ax.annotate(
    "",
    xy=(xv, z55),
    xytext=(xv, z57),
    arrowprops=dict(arrowstyle="<->", linewidth=1.4, color=annotation_color)
)
ax.text(
    xv + 0.09,
    (z55 + z57) / 2,
    r"$\Delta z^*\approx -0.0701$",
    va="center",
    ha="left",
    fontsize=font_size("delta_label"),
    linespacing=line_spacing("delta_label"),
    color=annotation_color
)

# Formula di sensibilità in posizione stabile nel riquadro nord-est.
ax.text(
    0.97,
    0.93,
    r"Nel tratto $55\leq Q\leq 60$:" "\n"
    r"$\dfrac{dz^*}{dQ}=-\lambda_Q^*\approx -0.0351$",
    transform=ax.transAxes,
    ha="right",
    va="top",
    fontsize=font_size("sensitivity_label"),
    linespacing=line_spacing("sensitivity_label"),
    bbox=dict(
        boxstyle="round,pad=0.35",
        facecolor="white",
        edgecolor="#777777",
        alpha=0.95
    )
)

ax.set_xlabel(
    r"Requisito minimo di liquidità $Q$",
    fontsize=font_size("axis_label"),
    linespacing=line_spacing("axis_label")
)
ax.set_ylabel(
    r"Valore ottimo $z^*(Q)$",
    fontsize=font_size("axis_label"),
    linespacing=line_spacing("axis_label")
)
ax.set_title(
    "Sensibilità locale del valore ottimo al requisito di liquidità",
    fontsize=font_size("title"),
    linespacing=line_spacing("title")
)
ax.tick_params(axis="both", labelsize=font_size("tick_label"))
ax.grid(True, alpha=0.3)

ax.set_xlim(54.65, 60.35)
ax.set_ylim(3.55, 3.80)

fig.tight_layout()
fig.savefig(png_path, dpi=300, bbox_inches="tight")
fig.savefig(svg_path, bbox_inches="tight")
plt.close(fig)

print(png_path)
print(svg_path)
