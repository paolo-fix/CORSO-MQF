from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


# ============================================================
# Capitolo 2 - Funzione di ripartizione di una v.c. discreta
# ============================================================
#
# Questo script genera il grafico della funzione di ripartizione
# di una variabile casuale discreta.
#
# Output:
#   - file PNG, utile per l'inclusione in Scientific Workplace / LaTeX
#   - file SVG, utile come formato vettoriale/editabile
#
# ------------------------------------------------------------
# COME CREARE UNA NUOVA VERSIONE DEL GRAFICO
# ------------------------------------------------------------
#
# 1. Modificare la lista x_values:
#       valori assunti dalla variabile casuale X.
#
# 2. Modificare la lista p_values:
#       probabilita' corrispondenti ai valori di x_values.
#
#    Le due liste devono avere la stessa lunghezza.
#    Le probabilita' devono essere non negative e sommare a 1.
#
# 3. Modificare output_name:
#       nome base dei file prodotti, senza estensione.
#
# 4. Se necessario, modificare output_dir:
#       cartella in cui salvare i grafici.
#
# ============================================================


# ------------------------------------------------------------
# Cartella di salvataggio dei grafici
# ------------------------------------------------------------

output_dir = Path(
    r"E:\Didattica\MQF\Github\CORSO-MQF\01_Manuale\graphics"
)

output_dir.mkdir(parents=True, exist_ok=True)


# ------------------------------------------------------------
# Specificazione della distribuzione discreta
# ------------------------------------------------------------
#
# Esempio del Capitolo 2:
#
#   X = -0.04 con probabilita' 0.25
#   X =  0.01 con probabilita' 0.50
#   X =  0.06 con probabilita' 0.25
#
# Per creare un'altra distribuzione, modificare solo x_values,
# p_values e output_name.

x_values = [-0.04, 0.01, 0.06]
p_values = [0.25, 0.50, 0.25]

output_name = "Cap02_cdf_rendimento_discreto"


# ------------------------------------------------------------
# Parametri grafici modificabili
# ------------------------------------------------------------

figure_width = 7.2
figure_height = 4.4

png_dpi = 300

xlabel = r"$x$"
ylabel = r"$F_X(x)=\mathrm{P}(X\leq x)$"

# Margine orizzontale automatico intorno ai valori di X.
# Aumentare questo parametro se il grafico appare troppo compresso.
x_padding_factor = 0.25


# ------------------------------------------------------------
# Funzione di utilita'
# ------------------------------------------------------------

def plot_discrete_cdf(
    x_values,
    p_values,
    output_dir,
    output_name,
    figure_width=7.2,
    figure_height=4.4,
    png_dpi=300,
    xlabel=r"$x$",
    ylabel=r"$F_X(x)=\mathrm{P}(X\leq x)$",
    x_padding_factor=0.25,
):
    """
    Genera il grafico della funzione di ripartizione di una
    variabile casuale discreta.

    Parametri
    ---------
    x_values : list of float
        Valori assunti dalla variabile casuale X.

    p_values : list of float
        Probabilita' associate ai valori di X.

    output_dir : pathlib.Path
        Cartella di salvataggio dei grafici.

    output_name : str
        Nome base dei file di output, senza estensione.

    Note
    ----
    La funzione di ripartizione viene disegnata come funzione
    a gradini, continua da destra.

    I punti pieni rappresentano il valore di F_X nel punto di salto.
    I punti vuoti rappresentano il limite sinistro.
    """

    x_values = np.asarray(x_values, dtype=float)
    p_values = np.asarray(p_values, dtype=float)

    # Controlli elementari sulla distribuzione
    if x_values.ndim != 1 or p_values.ndim != 1:
        raise ValueError("x_values e p_values devono essere liste monodimensionali.")

    if len(x_values) != len(p_values):
        raise ValueError("x_values e p_values devono avere la stessa lunghezza.")

    if len(x_values) == 0:
        raise ValueError("La distribuzione deve contenere almeno un valore.")

    if np.any(p_values < 0):
        raise ValueError("Le probabilita' devono essere non negative.")

    if not np.isclose(np.sum(p_values), 1.0):
        raise ValueError("Le probabilita' devono sommare a 1.")

    # Ordinamento dei valori di X
    order = np.argsort(x_values)
    x_values = x_values[order]
    p_values = p_values[order]

    # Se ci fossero valori duplicati, le probabilita' vengono aggregate.
    unique_x = []
    unique_p = []

    for x, p in zip(x_values, p_values):
        if unique_x and np.isclose(x, unique_x[-1]):
            unique_p[-1] += p
        else:
            unique_x.append(x)
            unique_p.append(p)

    x_values = np.asarray(unique_x, dtype=float)
    p_values = np.asarray(unique_p, dtype=float)

    cdf_values = np.cumsum(p_values)
    cdf_left_values = np.concatenate(([0.0], cdf_values[:-1]))

    # Limiti orizzontali del grafico
    x_range = x_values[-1] - x_values[0]
    if np.isclose(x_range, 0.0):
        x_range = 1.0

    x_padding = x_padding_factor * x_range
    x_min = x_values[0] - x_padding
    x_max = x_values[-1] + x_padding

    fig, ax = plt.subplots(figsize=(figure_width, figure_height))

    # Segmento iniziale: F_X(x)=0 per x < primo valore
    ax.hlines(
        y=0.0,
        xmin=x_min,
        xmax=x_values[0],
        linewidth=1.8,
    )

    # Segmenti orizzontali della funzione di ripartizione
    for i, x in enumerate(x_values):
        y = cdf_values[i]
        xmin = x
        xmax = x_values[i + 1] if i < len(x_values) - 1 else x_max

        ax.hlines(
            y=y,
            xmin=xmin,
            xmax=xmax,
            linewidth=1.8,
        )

    # Punti pieni: valore della funzione nel punto di salto
    ax.plot(
        x_values,
        cdf_values,
        marker="o",
        linestyle="None",
        markersize=6,
    )

    # Punti vuoti: limite sinistro della funzione nel punto di salto
    ax.plot(
        x_values,
        cdf_left_values,
        marker="o",
        linestyle="None",
        markersize=6,
        markerfacecolor="none",
    )

    # Linee verticali tratteggiate nei punti di salto
    for x in x_values:
        ax.axvline(
            x=x,
            linestyle="--",
            linewidth=0.8,
            alpha=0.6,
        )

    # Assi e griglia
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(-0.05, 1.05)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    ax.set_xticks(x_values)
    ax.set_xticklabels([f"${x:.2f}$" for x in x_values])

    y_ticks = sorted(set([0.0, 1.0] + list(cdf_left_values) + list(cdf_values)))
    ax.set_yticks(y_ticks)
    ax.set_yticklabels([f"${y:.2f}$" if y not in (0.0, 1.0) else f"${int(y)}$" for y in y_ticks])

    ax.grid(True, linewidth=0.5, alpha=0.4)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.tight_layout()

    png_path = output_dir / f"{output_name}.png"
    svg_path = output_dir / f"{output_name}.svg"

    fig.savefig(png_path, dpi=png_dpi, bbox_inches="tight")
    fig.savefig(svg_path, bbox_inches="tight")

    plt.close(fig)

    print(f"Creato file PNG: {png_path}")
    print(f"Creato file SVG: {svg_path}")


# ------------------------------------------------------------
# Esecuzione dello script
# ------------------------------------------------------------

if __name__ == "__main__":
    plot_discrete_cdf(
        x_values=x_values,
        p_values=p_values,
        output_dir=output_dir,
        output_name=output_name,
        figure_width=figure_width,
        figure_height=figure_height,
        png_dpi=png_dpi,
        xlabel=xlabel,
        ylabel=ylabel,
        x_padding_factor=x_padding_factor,
    )
