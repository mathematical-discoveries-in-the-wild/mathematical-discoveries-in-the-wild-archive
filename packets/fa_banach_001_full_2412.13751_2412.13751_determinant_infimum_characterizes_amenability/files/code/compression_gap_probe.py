"""Finite-dimensional checks for the compression-gap proof.

This is evidence only.  The packet proves the inequalities for arbitrary
Hilbert spaces by resolvents, Schur complements, and a Sylvester estimate.
"""

from __future__ import annotations

import numpy as np


def hermitian_log(a: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh(a)
    return (vectors * np.log(values)) @ vectors.conj().T


def random_compression_checks(rng: np.random.Generator, trials: int = 300) -> float:
    smallest_margin = np.inf
    for _ in range(trials):
        n = int(rng.integers(3, 15))
        rank = int(rng.integers(1, n))
        x = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
        b = x.conj().T @ x + float(rng.uniform(0.1, 2.0)) * np.eye(n)
        a = b[:rank, :rank]
        lhs = np.trace(hermitian_log(a)).real
        lhs -= np.trace(hermitian_log(b)[:rank, :rank]).real
        leakage = np.linalg.norm(b[rank:, :rank], "fro") ** 2
        rhs = leakage / (2.0 * np.linalg.norm(b, 2) ** 2)
        margin = lhs - rhs
        if margin < -2e-9:
            raise AssertionError((n, rank, lhs, rhs, margin))
        smallest_margin = min(smallest_margin, margin)
    return float(smallest_margin)


def sylvester_checks(rng: np.random.Generator, trials: int = 300) -> float:
    smallest_ratio = np.inf
    for _ in range(trials):
        n = int(rng.integers(3, 15))
        rank = int(rng.integers(1, n))
        x = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
        t_op = x.conj().T @ x + float(rng.uniform(0.2, 1.5)) * np.eye(n)
        alpha = float(np.linalg.eigvalsh(t_op)[0])
        y = t_op[rank:, :rank]
        z = (t_op @ t_op)[rank:, :rank]
        denominator = 2.0 * alpha * np.linalg.norm(y, "fro")
        if denominator > 1e-12:
            ratio = np.linalg.norm(z, "fro") / denominator
            if ratio < 1.0 - 2e-9:
                raise AssertionError((n, rank, ratio))
            smallest_ratio = min(smallest_ratio, ratio)
    return float(smallest_ratio)


def cyclic_boundary_check(n: int = 41) -> tuple[float, int, float, float]:
    # Right translations by +1 and -1 on a large cyclic model.  The chosen F
    # does not wrap, so the cyclic calculation equals the Z calculation.
    shift = np.roll(np.eye(n), 1, axis=0)
    h = shift + shift.conj().T
    f_size = 13
    leakage = np.linalg.norm(h[f_size:, :f_size], "fro") ** 2
    directed_boundary = 2
    if abs(leakage - directed_boundary) > 1e-12:
        raise AssertionError((leakage, directed_boundary))
    t = 0.15
    t_op = np.eye(n) + t * h
    b = t_op @ t_op
    log_finite_det = np.linalg.slogdet(b[:f_size, :f_size])[1] / f_size
    log_fk_det = np.linalg.slogdet(b)[1] / n
    determinant_gap = float(log_finite_det - log_fk_det)
    constant = 2 * t**2 * (1 - 2 * t) ** 2 / (1 + 2 * t) ** 4
    lower_bound = float(constant * directed_boundary / f_size)
    if determinant_gap < lower_bound - 2e-10:
        raise AssertionError((determinant_gap, lower_bound))
    return float(leakage), directed_boundary, determinant_gap, lower_bound


def main() -> None:
    rng = np.random.default_rng(241213751)
    compression_margin = random_compression_checks(rng)
    sylvester_ratio = sylvester_checks(rng)
    leakage, boundary, determinant_gap, lower_bound = cyclic_boundary_check()
    print("random compression trials: 300")
    print(f"smallest lhs-rhs margin: {compression_margin:.6e}")
    print("random Sylvester trials: 300")
    print(f"smallest observed ratio to lower bound: {sylvester_ratio:.6f}")
    print(f"cyclic/Z boundary check: leakage={leakage:g}, boundary={boundary}")
    print(
        "cyclic determinant check: "
        f"gap={determinant_gap:.6e}, lower_bound={lower_bound:.6e}"
    )
    print("all checks passed")


if __name__ == "__main__":
    main()
