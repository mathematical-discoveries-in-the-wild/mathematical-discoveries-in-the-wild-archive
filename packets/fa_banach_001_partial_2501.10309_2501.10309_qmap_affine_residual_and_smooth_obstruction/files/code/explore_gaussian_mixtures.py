"""Search two-component Gaussian mixtures for entropy-power nonconcavity.

This is numerical exploration only. It evaluates mixture densities on an
adaptive uniform grid and checks midpoint concavity on a lambda grid.
"""

from __future__ import annotations

import math
import numpy as np


def normalize(weights: np.ndarray) -> np.ndarray:
    return weights / weights.sum()


def convolved_mixture(lam, wu, mu, su, wv, mv, sv):
    weights = np.outer(wu, wv).ravel()
    means = (
        math.sqrt(lam) * mu[:, None]
        + math.sqrt(1.0 - lam) * mv[None, :]
    ).ravel()
    variances = (
        lam * su[:, None] ** 2
        + (1.0 - lam) * sv[None, :] ** 2
    ).ravel()
    return weights, means, np.sqrt(variances)


def entropy_power(params, lam, points=40001):
    wu, mu, su, wv, mv, sv = params
    weights, means, sigmas = convolved_mixture(
        lam, wu, mu, su, wv, mv, sv
    )
    lo = float(np.min(means - 10.0 * sigmas))
    hi = float(np.max(means + 10.0 * sigmas))
    x = np.linspace(lo, hi, points)
    z = (x[:, None] - means[None, :]) / sigmas[None, :]
    density = np.sum(
        weights[None, :]
        * np.exp(-0.5 * z * z)
        / (math.sqrt(2.0 * math.pi) * sigmas[None, :]),
        axis=1,
    )
    mass = np.trapz(density, x)
    density = density / mass
    entropy = -np.trapz(density * np.log(np.maximum(density, 1e-300)), x)
    return math.exp(2.0 * entropy)


def random_params(rng):
    wu = normalize(rng.uniform(0.05, 1.0, 2))
    wv = normalize(rng.uniform(0.05, 1.0, 2))
    mu = np.sort(rng.uniform(-5.0, 5.0, 2))
    mv = np.sort(rng.uniform(-5.0, 5.0, 2))
    su = np.exp(rng.uniform(math.log(0.08), math.log(2.0), 2))
    sv = np.exp(rng.uniform(math.log(0.08), math.log(2.0), 2))
    return wu, mu, su, wv, mv, sv


def main(seed=20260719, trials=250, grid_size=31):
    rng = np.random.default_rng(seed)
    lambdas = np.linspace(0.0, 1.0, grid_size)
    best = None
    for trial in range(trials):
        params = random_params(rng)
        values = np.array(
            [entropy_power(params, lam, points=12001) for lam in lambdas]
        )
        # Positive second difference violates midpoint concavity.
        second = values[:-2] - 2.0 * values[1:-1] + values[2:]
        idx = int(np.argmax(second))
        scale = float(np.max(values))
        score = float(second[idx] / scale)
        if best is None or score > best[0]:
            best = (score, trial, idx, params, values[idx : idx + 3])
        if score > 2e-4:
            break

    score, trial, idx, params, vals = best
    print(f"best_relative_second_difference={score:.9g}")
    print(f"trial={trial}")
    print(f"lambda_triple={lambdas[idx:idx+3].tolist()}")
    print(f"values={vals.tolist()}")
    names = ("wu", "mu", "su", "wv", "mv", "sv")
    for name, value in zip(names, params):
        print(f"{name}={value.tolist()}")

    print("simple_symmetric_search")
    simple_best = None
    locations = (0.75, 1.0, 1.5, 2.0, 3.0, 4.0)
    sigmas = (0.1, 0.2, 0.35, 0.5, 0.75, 1.0, 1.5)
    for au in locations:
        for av in locations:
            for su0 in sigmas:
                for sv0 in sigmas:
                    simple = (
                        np.array([0.5, 0.5]),
                        np.array([-au, au]),
                        np.array([su0, su0]),
                        np.array([0.5, 0.5]),
                        np.array([-av, av]),
                        np.array([sv0, sv0]),
                    )
                    values = np.array(
                        [entropy_power(simple, lam, points=8001) for lam in lambdas]
                    )
                    second = values[:-2] - 2.0 * values[1:-1] + values[2:]
                    idx = int(np.argmax(second))
                    score = float(second[idx] / np.max(values))
                    if simple_best is None or score > simple_best[0]:
                        simple_best = (
                            score, idx, au, av, su0, sv0, values[idx : idx + 3]
                        )
    score, idx, au, av, su0, sv0, vals = simple_best
    print(f"simple_relative_second_difference={score:.9g}")
    print(f"simple_lambda_triple={lambdas[idx:idx+3].tolist()}")
    print(f"simple_values={vals.tolist()}")
    print(f"simple_parameters=au:{au},av:{av},su:{su0},sv:{sv0}")


if __name__ == "__main__":
    main()
