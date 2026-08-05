from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

# Lo script si trova in <radice progetto>/04_Codice/Lez11.
# Costruire il percorso a partire da __file__ evita dipendenze dal PC in uso.
project_dir = Path(__file__).resolve().parents[2]
out_dir = project_dir / "graphics"
out_dir.mkdir(parents=True, exist_ok=True)

png_path = out_dir / "cap11_geometria_programmazione_lineare.png"
svg_path = out_dir / "cap11_geometria_programmazione_lineare.svg"

A0 = 10.0
Q_min = 3.0
B_max = 4.0

x1 = np.linspace(0, 11, 400)
x2_budget = A0 - x1

vertices = np.array([
    [Q_min, 0.0],
    [A0, 0.0],
    [A0 - B_max, B_max],
    [Q_min, B_max],
])

fig, ax = plt.subplots(figsize=(8.6, 5.8))
ax.plot(x1, x2_budget, linewidth=2, label=r"$x_1+x_2=A_0$")
ax.axvline(Q_min, linewidth=2, linestyle="--", label=r"$x_1=Q_{\min}$")
ax.axhline(B_max, linewidth=2, linestyle="-.", label=r"$x_2=B_{\max}$")

ax.fill(vertices[:, 0], vertices[:, 1], alpha=0.2, label="Regione ammissibile")
closed = np.vstack([vertices, vertices[0]])
ax.plot(closed[:, 0], closed[:, 1], linewidth=1.5)

for (xv, yv), label in zip(vertices, ["A", "B", "C", "D"]):
    ax.scatter([xv], [yv], s=35)
    ax.annotate(label, (xv, yv), xytext=(6, 6), textcoords="offset points")

ax.text(5.0, 2.0, "Regione\nammissibile", ha="center", va="center")
ax.set_xlim(0, 11)
ax.set_ylim(0, 7)
ax.set_xlabel(r"$x_1$: attività liquide")
ax.set_ylabel(r"$x_2$: titoli a lunga scadenza")
ax.grid(True, alpha=0.25)
ax.legend(loc="upper right", frameon=True)
fig.tight_layout()

fig.savefig(png_path, dpi=300, bbox_inches="tight")
fig.savefig(svg_path, bbox_inches="tight")
# plt.show()
plt.close(fig)

print("File salvati:")
print(png_path)
print(svg_path)
