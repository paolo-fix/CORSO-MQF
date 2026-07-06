import os

import matplotlib.pyplot as plt
import numpy as np


# ============================================================
# PARAMETRI DA MODIFICARE
# ============================================================
#
# Per personalizzare la figura, cambiare solo i valori in questo
# dizionario. Le funzioni piu' sotto ricevono questi valori come input:
# i numeri nelle funzioni non sono quindi un secondo punto di controllo.

BROWNIAN_PARAMETERS = {
    "x0": 1.2,       # Valore iniziale X_0, allineato agli esempi OU e GBM.
    "sigma": 0.25,   # Volatilita': aumenta o riduce la dispersione.
    "T": 2.0,        # Orizzonte temporale.
    "n_steps": 500,  # Numero di passi temporali.
    "n_paths": 8,    # Numero di traiettorie mostrate nel grafico.
    "seed": 52,      # Seme casuale: cambiarlo genera altre traiettorie.
}


# ============================================================
# OUTPUT DA PRODURRE
# ============================================================
#
# Aggiungere o togliere percorsi in questa lista per controllare
# i file salvati. L'estensione decide il formato: .png, .svg, ecc.

OUTPUT_FILES = [
    "./graphics/Cap06_Brownian_traiettorie.png",
    "./graphics/Cap06_Brownian_traiettorie.svg",
]


# ============================================================
# SIMULAZIONE DEL MOTO BROWNIANO TRASLATO
# ============================================================


def simulate_brownian_paths(
    x0: float,
    sigma: float,
    T: float,
    n_steps: int,
    n_paths: int,
    seed: int,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Simulate paths of a shifted scaled Brownian motion.

    Model:

        X_t = x0 + sigma * W_t

    Incremental form:

        X_{t+dt} = X_t + sigma * sqrt(dt) * Z,
        with Z ~ N(0, 1).

    Parameters
    ----------
    x0
        Initial value X_0, aligned with the OU and GBM examples.
    sigma
        Volatility scale. Larger values produce more dispersed paths.
    T
        Final time horizon.
    n_steps
        Number of time steps used in the discretization.
    n_paths
        Number of simulated paths.
    seed
        Random seed. Change it to obtain a different, but reproducible,
        simulation.
    """
    rng = np.random.default_rng(seed)

    dt = T / n_steps
    sqrt_dt = np.sqrt(dt)

    t_grid = np.linspace(0.0, T, n_steps + 1)
    w = np.empty((n_steps + 1, n_paths))
    w[0, :] = x0

    for i in range(n_steps):
        z = rng.standard_normal(n_paths)
        w[i + 1, :] = w[i, :] + sigma * sqrt_dt * z

    return t_grid, w


# ============================================================
# COSTRUZIONE E SALVATAGGIO DEL GRAFICO
# ============================================================


def plot_brownian_paths(
    output_paths: str | list[str] | tuple[str, ...],
    x0: float,
    sigma: float,
    T: float,
    n_steps: int,
    n_paths: int,
    seed: int,
) -> None:
    """
    Build and save the Brownian paths figure.

    The same figure can be written to one or more output files. The file
    extension controls the format, for example ``.png`` or ``.svg``.
    """
    t_grid, w = simulate_brownian_paths(
        x0=x0,
        sigma=sigma,
        T=T,
        n_steps=n_steps,
        n_paths=n_paths,
        seed=seed,
    )

    if isinstance(output_paths, str):
        output_paths = [output_paths]

    fig, ax = plt.subplots(figsize=(9, 5.5))

    for j in range(n_paths):
        ax.plot(t_grid, w[:, j], linewidth=1.2)

    ax.axhline(x0, linestyle="--", linewidth=1.2, label=r"$X_0$")

    ax.set_xlabel("Tempo")
    ax.set_ylabel(r"$X_t$")
    ax.set_title("Moto browniano: traiettorie simulate")
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()

    for output_path in output_paths:
        output_dir = os.path.dirname(output_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        plt.savefig(output_path, dpi=300, bbox_inches="tight")

    plt.close(fig)


# ============================================================
# ESECUZIONE DELLO SCRIPT
# ============================================================


if __name__ == "__main__":
    plot_brownian_paths(OUTPUT_FILES, **BROWNIAN_PARAMETERS)

    for output_file in OUTPUT_FILES:
        print(f"Figura salvata in: {output_file}")
