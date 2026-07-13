import os

import matplotlib.pyplot as plt
import numpy as np


# ============================================================
# PARAMETRI DA MODIFICARE
# ============================================================

CORRELATION_PARAMETERS = {
    "T": 2.0,
    "n_steps": 500,
    "seed_1": 1,
    "seed_2": 127,
    "rho_values": [0.0, 0.45],
}


OUTPUT_FILES = {
    0.0: "./graphics/Cap06_correlazione_traiettorie_rho0.png",
    0.45: "./graphics/Cap06_correlazione_traiettorie_rho_m045.png",
}


# ============================================================
# SIMULAZIONE DI DUE BROWNIANI CORRELATI
# ============================================================


def generate_base_shocks(
    n_steps: int,
    seed_1: int,
    seed_2: int,
) -> tuple[np.ndarray, np.ndarray]:
    """Generate two independent standard-normal shock sequences."""
    rng_1 = np.random.default_rng(seed_1)
    rng_2 = np.random.default_rng(seed_2)
    z1 = rng_1.standard_normal(n_steps)
    z2 = rng_2.standard_normal(n_steps)
    return z1, z2


def correlate_shocks(
    z1: np.ndarray,
    z2: np.ndarray,
    rho: float,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Build shocks with target instantaneous correlation rho.

    In the two-dimensional case:

        eps_1 = z_1
        eps_2 = rho z_1 + sqrt(1-rho^2) z_2
    """
    if not -1.0 <= rho <= 1.0:
        raise ValueError("rho must be between -1 and 1.")

    eps1 = z1
    eps2 = rho * z1 + np.sqrt(1.0 - rho**2) * z2
    return eps1, eps2


def simulate_correlated_brownian_paths(
    T: float,
    n_steps: int,
    seed_1: int,
    seed_2: int,
    rho: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, float]:
    """Simulate two Brownian paths driven by correlated increments."""
    z1, z2 = generate_base_shocks(
        n_steps=n_steps,
        seed_1=seed_1,
        seed_2=seed_2,
    )
    eps1, eps2 = correlate_shocks(z1=z1, z2=z2, rho=rho)

    dt = T / n_steps
    sqrt_dt = np.sqrt(dt)

    t_grid = np.linspace(0.0, T, n_steps + 1)
    w1 = np.concatenate(([0.0], np.cumsum(sqrt_dt * eps1)))
    w2 = np.concatenate(([0.0], np.cumsum(sqrt_dt * eps2)))

    empirical_corr = float(np.corrcoef(eps1, eps2)[0, 1])
    return t_grid, w1, w2, empirical_corr


# ============================================================
# COSTRUZIONE E SALVATAGGIO DEL GRAFICO
# ============================================================


def plot_correlated_paths(
    output_path: str,
    T: float,
    n_steps: int,
    seed_1: int,
    seed_2: int,
    rho: float,
) -> float:
    """Build and save the figure for one target correlation."""
    t_grid, w1, w2, empirical_corr = simulate_correlated_brownian_paths(
        T=T,
        n_steps=n_steps,
        seed_1=seed_1,
        seed_2=seed_2,
        rho=rho,
    )

    fig, ax = plt.subplots(figsize=(9, 5.5))

    ax.plot(t_grid, w1, linewidth=1.5, label=r"$W_{1,t}$")
    ax.plot(t_grid, w2, linewidth=1.5, label=r"$W_{2,t}$")
    ax.axhline(0.0, color="black", linestyle="--", linewidth=1.0, alpha=0.7)

    ax.set_xlabel("Tempo")
    ax.set_ylabel("Livello del processo")
    ax.set_title(
        rf"Due fattori browniani simulati: $\rho={rho:.2f}$ "
        rf"(corr. empirica incrementi = {empirical_corr:.2f})"
    )
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()

    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)

    return empirical_corr


# ============================================================
# ESECUZIONE DELLO SCRIPT
# ============================================================


if __name__ == "__main__":
    for rho_value in CORRELATION_PARAMETERS["rho_values"]:
        empirical = plot_correlated_paths(
            output_path=OUTPUT_FILES[rho_value],
            T=CORRELATION_PARAMETERS["T"],
            n_steps=CORRELATION_PARAMETERS["n_steps"],
            seed_1=CORRELATION_PARAMETERS["seed_1"],
            seed_2=CORRELATION_PARAMETERS["seed_2"],
            rho=rho_value,
        )
        print(
            "Figura salvata in: "
            f"{OUTPUT_FILES[rho_value]} | rho target={rho_value:.2f} "
            f"| corr empirica incrementi={empirical:.4f}"
        )
