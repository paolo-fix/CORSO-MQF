import os
import numpy as np
import matplotlib.pyplot as plt


def simulate_ou_paths(
    x0: float,
    theta: float,
    kappa: float,
    sigma: float,
    T: float,
    n_steps: int,
    n_paths: int,
    seed: int = 42,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Simula traiettorie di un processo di Ornstein-Uhlenbeck con schema di Euler-Maruyama.

    dX_t = kappa * (theta - X_t) dt + sigma dW_t
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


def plot_ou_mean_reversion(
    output_path: str,
    x0: float = 1.2,
    theta: float = 0.5,
    kappa: float = 1.5,
    sigma: float = 0.25,
    T: float = 2.0,
    n_steps: int = 500,
    n_paths: int = 8,
    seed: int = 42,
) -> None:
    """
    Genera un grafico con più traiettorie OU e la linea del livello di lungo periodo theta.
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

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

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
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    output_file = "./graphics/Cap06_OU_mean_reversion.png"
    plot_ou_mean_reversion(output_file)
    print(f"Figura salvata in: {output_file}")