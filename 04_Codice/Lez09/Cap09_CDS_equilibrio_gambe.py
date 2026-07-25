import numpy as np
import matplotlib.pyplot as plt

# Valore attuale della gamba di protezione e coefficiente che lega
# lo spread del CDS al valore attuale della gamba dei premi.
pv_prot = 6.804
coeff_prem = 264.37

# Lo spread equo rende uguali le due gambe:
# pv_prot = coeff_prem * (b_star / 10_000).
# Il fattore 10_000 converte lo spread da punti base a valore decimale.
b_star = (pv_prot / coeff_prem) * 10000.0

# Le immagini sono salvate in questa cartella, che si trova FUORI dal repository.
# Quando si controlla il risultato, occorre quindi aprire i file presenti qui.
output_dir = r"E:\Didattica\MQF\graphics"

# Dimensioni dei caratteri, espresse in punti tipografici.
# Ogni elemento del grafico ha un proprio parametro: modificare, per esempio,
# LABEL_FONTSIZE non cambia automaticamente legenda, tacche o annotazione.
LABEL_FONTSIZE = 12
TITLE_FONTSIZE = 14
ANNOTATION_FONTSIZE = 14
LEGEND_FONTSIZE = 12
TICK_FONTSIZE = 12

# Valori di spread usati sull'asse orizzontale e corrispondente valore
# della gamba dei premi.
b = np.linspace(0.0, 450.0, 500)
pv_prem = coeff_prem * (b / 10000.0)

fig, ax = plt.subplots(figsize=(10, 6.25))

# La gamba di protezione non dipende dallo spread ed è quindi orizzontale;
# la gamba dei premi cresce invece linearmente con lo spread.
ax.plot(b, np.full_like(b, pv_prot), linewidth=2.2, label="Gamba di protezione")
ax.plot(b, pv_prem, linewidth=2.2, label="Gamba dei premi")

# Evidenzia il punto di equilibrio e traccia le sue proiezioni sugli assi.
ax.scatter([b_star], [pv_prot], s=110, zorder=5)
ax.axvline(b_star, linestyle="--", linewidth=1.2)
ax.axhline(pv_prot, linestyle="--", linewidth=1.0)

# Testo mostrato vicino al punto di equilibrio.
annotation = (
    "Spread equo $s^* \\approx " + f"{b_star:.1f}" + "$ pb\n"
    "$\\mathrm{PV}_{\\mathrm{prot}} = \\mathrm{PV}_{\\mathrm{prem}} = " + f"{pv_prot:.3f}" + "$"
)
ax.annotate(
    annotation,
    xy=(b_star, pv_prot),
    xytext=(b_star + 28, pv_prot + 1.6),
    arrowprops={"arrowstyle": "->", "linewidth": 1.2},
    fontsize=ANNOTATION_FONTSIZE,
)

ax.set_xlim(0, 450)
ax.set_ylim(0, 12)
ax.set_xlabel("Spread annuo del CDS (punti base)", fontsize=LABEL_FONTSIZE)
ax.set_ylabel("Valore attuale", fontsize=LABEL_FONTSIZE)
ax.set_title(
    "Determinazione dello spread equo del CDS",
    fontsize=TITLE_FONTSIZE,
)

# Legenda e numeri sugli assi richiedono impostazioni indipendenti.
ax.legend(loc="upper left", fontsize=LEGEND_FONTSIZE)
ax.grid(True, linewidth=0.5, alpha=0.35)
ax.tick_params(axis="both", labelsize=TICK_FONTSIZE)

# Sistema automaticamente i margini per evitare testi tagliati.
fig.tight_layout()

png_path = output_dir + r"\Cap09_CDS_equilibrio_gambe.png"
svg_path = output_dir + r"\Cap09_CDS_equilibrio_gambe.svg"

# Il DPI influenza la risoluzione in pixel del PNG, non la dimensione relativa
# dei caratteri nel grafico. L'SVG è invece un formato vettoriale.
fig.savefig(png_path, dpi=220, bbox_inches="tight")
fig.savefig(svg_path, bbox_inches="tight")
print(f"Grafico salvato in:\n- {png_path}\n- {svg_path}")
plt.show()
