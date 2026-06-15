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

GBM_PARAMETERS = {
    "s0": 1.2,       # Valore iniziale S_0, allineato agli esempi BM e OU.
    "m": 0.15,       # Drift logaritmico nella formula S_t = S_0 exp(m t + sigma W_t).
    "sigma": 0.2,    # Volatilita': aumenta o riduce la dispersione.
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
    "./graphics/Cap06_GBM_traiettorie.png",
    "./graphics/Cap06_GBM_traiettorie.svg",
]


# ============================================================
# SIMULAZIONE DEL MOTO BROWNIANO GEOMETRICO
# ============================================================


def simulate_gbm_paths(
    s0: float,
    m: float,
    sigma: float,
    T: float,
    n_steps: int,
    n_paths: int,
    seed: int,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Simulate paths of a geometric Brownian motion with the exact scheme.

    Model:

        S_t = S_0 * exp(m * t + sigma * W_t)

    Exact time-discretized form:

        S_{t+dt} = S_t * exp(m * dt + sigma * sqrt(dt) * Z),
        with Z ~ N(0, 1).

    Parameters
    ----------
    s0
        Initial value S_0. It must be positive.
    m
        Logarithmic drift parameter. Larger values increase the median path.
    sigma
        Volatility parameter. Larger values produce more dispersed paths.
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
    s = np.empty((n_steps + 1, n_paths))
    s[0, :] = s0

    drift = m * dt

    for i in range(n_steps):
        z = rng.standard_normal(n_paths)
        diffusion = sigma * sqrt_dt * z
        s[i + 1, :] = s[i, :] * np.exp(drift + diffusion)

    return t_grid, s


# ============================================================
# COSTRUZIONE E SALVATAGGIO DEL GRAFICO
# ============================================================


def plot_gbm_paths(
    output_paths: str | list[str] | tuple[str, ...],
    s0: float,
    m: float,
    sigma: float,
    T: float,
    n_steps: int,
    n_paths: int,
    seed: int,
) -> None:
    """
    Build and save the geometric Brownian motion paths figure.

    The same figure can be written to one or more output files. The file
    extension controls the format, for example ``.png`` or ``.svg``.
    """
    t_grid, s = simulate_gbm_paths(
        s0=s0,
        m=m,
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
        ax.plot(t_grid, s[:, j], linewidth=1.2)

    # Qui m e' il drift logaritmico nella rappresentazione
    # S_t = S_0 exp(m t + sigma W_t).
    # Poiche' W_t ~ N(0,t), il valore atteso e'
    # E[S_t] = S_0 exp((m + 0.5 sigma^2)t).
    expected_value = s0 * np.exp((m + 0.5 * sigma**2) * t_grid)
    ax.plot(
        t_grid,
        expected_value,
        color="black",
        linestyle="--",
        linewidth=1.6,
        label=r"$\mathbb{E}[S_t]=S_0 e^{(m+\frac{1}{2}\sigma^2)t}$",
    )

    ax.set_xlabel("Tempo")
    ax.set_ylabel(r"$S_t$")
    ax.set_title("Moto browniano geometrico: traiettorie simulate")
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
    plot_gbm_paths(OUTPUT_FILES, **GBM_PARAMETERS)

    for output_file in OUTPUT_FILES:
        print(f"Figura salvata in: {output_file}")
