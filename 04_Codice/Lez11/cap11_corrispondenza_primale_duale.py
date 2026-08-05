from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# Cartella di destinazione del progetto
out_dir = Path(r"E:\Didattica\MQF\graphics")
out_dir.mkdir(parents=True, exist_ok=True)

png_path = out_dir / "cap11_corrispondenza_primale_duale.png"
svg_path = out_dir / "cap11_corrispondenza_primale_duale.svg"

fig, ax = plt.subplots(figsize=(11.5, 5.5))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

# Titolo
ax.text(
    0.5, 0.96,
    "Corrispondenza tra problema primale e problema duale",
    ha="center", va="center", fontsize=18, fontweight="bold"
)

# Box principali
left_x, right_x = 0.06, 0.60
box_y, box_w, box_h = 0.14, 0.34, 0.72

left_box = FancyBboxPatch(
    (left_x, box_y), box_w, box_h,
    boxstyle="round,pad=0.02,rounding_size=0.02",
    linewidth=1.8, fill=False
)
right_box = FancyBboxPatch(
    (right_x, box_y), box_w, box_h,
    boxstyle="round,pad=0.02,rounding_size=0.02",
    linewidth=1.8, fill=False
)
ax.add_patch(left_box)
ax.add_patch(right_box)

# Intestazioni box
ax.text(left_x + box_w/2, 0.81, "PROBLEMA PRIMALE",
        ha="center", va="center", fontsize=15, fontweight="bold")
ax.text(right_x + box_w/2, 0.81, "PROBLEMA DUALE",
        ha="center", va="center", fontsize=15, fontweight="bold")

# Formule
ax.text(left_x + box_w/2, 0.70, r"$\min\; c'x$",
        ha="center", va="center", fontsize=17)
ax.text(left_x + box_w/2, 0.62, r"$Ax\geq b,\qquad x\geq 0$",
        ha="center", va="center", fontsize=17)

ax.text(right_x + box_w/2, 0.70, r"$\max\; b'\lambda$",
        ha="center", va="center", fontsize=17)
ax.text(right_x + box_w/2, 0.62, r"$A'\lambda\leq c,\qquad \lambda\geq 0$",
        ha="center", va="center", fontsize=17)

# Etichetta centrale
ax.text(0.5, 0.56, r"$A \longleftrightarrow A'$",
        ha="center", va="center", fontsize=17)

# Righe di corrispondenza
rows = [
    (0.48, r"$m$ vincoli", r"$m$ variabili duali"),
    (0.37, r"$n$ variabili", r"$n$ vincoli duali"),
    (0.26, r"$b$: termini noti", r"$b$: coefficienti dell'obiettivo"),
    (0.15, r"$c$: coefficienti dell'obiettivo", r"$c$: termini noti"),
]

for y, left_text, right_text in rows:
    ax.text(left_x + box_w/2, y, left_text,
            ha="center", va="center", fontsize=13.5)
    ax.text(right_x + box_w/2, y, right_text,
            ha="center", va="center", fontsize=13.5)

    arrow = FancyArrowPatch(
        (0.44, y), (0.56, y),
        arrowstyle="<->", mutation_scale=15, linewidth=1.5
    )
    ax.add_patch(arrow)

# Testo finale separato
#ax.text(
#    0.5, 0.055,
#    "Ogni vincolo primale genera una variabile duale;\n"
#    "ogni variabile primale genera un vincolo duale.",
#    ha="center", va="center", fontsize=12.5
#)

fig.subplots_adjust(left=0.03, right=0.97, bottom=-0.03, top=0.97)
fig.savefig(png_path, dpi=300, bbox_inches="tight")
fig.savefig(svg_path, bbox_inches="tight")
plt.show()

print(f"Salvato: {png_path}")
print(f"Salvato: {svg_path}")