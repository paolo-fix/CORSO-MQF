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

OU_PARAMETERS = {
    "x0": 1.2,       # Valore iniziale X_0, allineato agli esempi BM e GBM.
    "theta": 0.5,    # Livello medio di lungo periodo.
    "kappa": 1.5,    # Velocita' di ritorno verso theta.
    "sigma": 0.25,   # Volatilita' degli shock stocastici.
    "T": 2.0,        # Orizzonte temporale.
    "n_steps": 500,  # Numero di passi temporali.
    "n_paths": 8,    # Numero di traiettorie mostrate nel grafico.
    "seed": 42,      # Seme casuale: cambiarlo genera altre traiettorie.
}


# ============================================================
# OUTPUT DA PRODURRE
# ============================================================
#
# Aggiungere o togliere percorsi in questa lista per controllare
# i file salvati. L'estensione decide il formato: .png, .svg, ecc.

OUTPUT_FILES = [
    "./graphics/Cap06_OU_mean_reversion.png",
    "./graphics/Cap06_OU_mean_reversion.svg",
]


# ============================================================
# SIMULAZIONE DEL PROCESSO DI ORNSTEIN-UHLENBECK
# ============================================================


def simulate_ou_paths(
    x0: float,
    theta: float,
    kappa: float,
    sigma: float,
    T: float,
    n_steps: int,
    n_paths: int,
    seed: int,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Simulate paths of an Ornstein-Uhlenbeck process with Euler-Maruyama.

    Model:

        dX_t = kappa * (theta - X_t) dt + sigma dW_t

    Parameters
    ----------
    x0
        Initial value X_0.
    theta
        Long-run mean. Larger or smaller values move the horizontal
        mean-reversion level in the plot.
    kappa
        Mean-reversion speed. Larger values pull the paths toward theta
        more quickly.
    sigma
        Volatility parameter. Larger values produce more dispersed paths.
    T
        Final time horizon.
    n_steps
        Number of time steps used in the Euler-Maruyama discretization.
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
    x = np.empty((n_steps + 1, n_paths))
    x[0, :] = x0

    for i in range(n_steps):
        z = rng.standard_normal(n_paths)
        x[i + 1, :] = (
            x[i, :]
            + kappa * (theta - x[i, :]) * dt
            + sigma * sqrt_dt * z
        )

    return t_grid, x


# ============================================================
# COSTRUZIONE E SALVATAGGIO DEL GRAFICO
# ============================================================


def plot_ou_mean_reversion(
    output_paths: str | list[str] | tuple[str, ...],
    x0: float,
    theta: float,
    kappa: float,
    sigma: float,
    T: float,
    n_steps: int,
    n_paths: int,
    seed: int,
) -> None:
    """
    Build and save the OU mean-reversion figure.

    The same figure can be written to one or more output files. The file
    extension controls the format, for example ``.png`` or ``.svg``.
    """
    t_grid, x = simulate_ou_paths(
        x0=x0,
        theta=theta,
        kappa=kappa,
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
        ax.plot(t_grid, x[:, j], linewidth=1.2)

    ax.axhline(theta, linestyle="--", linewidth=1.5, label=r"$\theta$")

    ax.set_xlabel("Tempo")
    ax.set_ylabel(r"$X_t$")
    ax.set_title("Processo di Ornstein-Uhlenbeck: traiettorie e mean reversion")
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
    plot_ou_mean_reversion(OUTPUT_FILES, **OU_PARAMETERS)

    for output_file in OUTPUT_FILES:
        print(f"Figura salvata in: {output_file}")
