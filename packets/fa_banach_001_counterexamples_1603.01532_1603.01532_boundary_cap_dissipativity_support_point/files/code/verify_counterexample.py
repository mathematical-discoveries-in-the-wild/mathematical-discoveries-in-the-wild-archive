#!/usr/bin/env python3
"""Deterministic checks and figure for the Question 3.10 counterexample."""

from __future__ import annotations

import argparse
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def phi(z1: complex, z2: complex, c: float) -> np.ndarray:
    return np.array([z1 + c * z2**2, z2], dtype=complex)


def generator(z1: complex, z2: complex, c: float) -> np.ndarray:
    return np.array([-z1 + c * z2**2, -z2], dtype=complex)


def pde_residual(z1: complex, z2: complex, c: float) -> float:
    g = generator(z1, z2, c)
    dphi_g = np.array([g[0] + 2.0 * c * z2 * g[1], g[1]])
    return float(np.max(np.abs(dphi_g + phi(z1, z2, c))))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--figure", type=Path, required=True)
    args = parser.parse_args()

    c = 3.0 * math.sqrt(3.0) / 2.0
    y = np.linspace(0.0, 1.0, 200_001)
    x = np.sqrt(np.maximum(0.0, 1.0 - y * y))
    xy2 = x * y * y
    worst_boundary = -1.0 + c * xy2

    cap = y <= 0.25
    max_xy2 = float(np.max(xy2))
    cap_sup = float(np.max(worst_boundary[cap]))
    exact_max_xy2 = 2.0 / (3.0 * math.sqrt(3.0))
    conservative_cap_bound = -1.0 + c / 16.0

    samples = [
        (0.2 + 0.1j, -0.3 + 0.25j),
        (-0.4 + 0.2j, 0.1 - 0.35j),
        (1.0 / math.sqrt(3.0), math.sqrt(2.0 / 3.0)),
    ]
    max_pde_residual = max(pde_residual(z1, z2, c) for z1, z2 in samples)

    # The degree-two coefficient kernel has total mass one.
    t = np.linspace(0.0, 30.0, 1_000_001)
    coefficient_kernel_mass = float(np.trapz(np.exp(-t), t))

    assert abs(max_xy2 - exact_max_xy2) < 2e-10
    assert abs(c * exact_max_xy2 - 1.0) < 1e-14
    assert cap_sup < -0.75
    assert conservative_cap_bound < -0.75
    assert max_pde_residual < 1e-14
    assert abs(coefficient_kernel_mass - 1.0) < 1e-8

    args.figure.parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(8.2, 4.8))
    ax.plot(y, worst_boundary, color="#245985", linewidth=2.4,
            label=r"worst boundary value $-1+c s^2\sqrt{1-s^2}$")
    ax.axvspan(0.0, 0.25, color="#71a95a", alpha=0.24,
               label=r"cap $|\zeta_2|\leq 1/4$")
    ax.axhline(-0.75, color="#b7352d", linestyle="--", linewidth=1.8,
               label=r"chosen threshold $-a=-3/4$")
    ax.axhline(0.0, color="black", linewidth=0.8)
    ax.set_xlabel(r"$s=|\zeta_2|$")
    ax.set_ylabel("largest dissipativity expression at fixed s")
    ax.set_title("Boundary dissipation of the extremal quadratic shear")
    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(-1.05, 0.08)
    ax.grid(alpha=0.2)
    ax.legend(loc="lower right", frameon=True)
    fig.tight_layout()
    fig.savefig(args.figure, dpi=180)
    plt.close(fig)

    print(f"c={c:.15f}")
    print(f"max_sampled_xy2={max_xy2:.15f}")
    print(f"exact_max_xy2={exact_max_xy2:.15f}")
    print(f"c_times_exact_max={c * exact_max_xy2:.15f}")
    print(f"sampled_cap_sup={cap_sup:.15f}")
    print(f"conservative_cap_bound={conservative_cap_bound:.15f}")
    print(f"max_pde_residual={max_pde_residual:.3e}")
    print(f"coefficient_kernel_mass={coefficient_kernel_mass:.12f}")
    print(f"figure={args.figure}")
    print("PASS")


if __name__ == "__main__":
    main()
