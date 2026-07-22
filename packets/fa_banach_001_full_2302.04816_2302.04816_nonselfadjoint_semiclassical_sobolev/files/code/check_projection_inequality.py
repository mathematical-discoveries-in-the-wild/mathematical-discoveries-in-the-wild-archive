"""Numerically test the two finite-dimensional inequalities used in the proof.

This is only a regression check, not part of the proof.  Random oblique
idempotents are obtained by conjugating a coordinate projection by an
ill-conditioned invertible matrix.
"""

from __future__ import annotations

import numpy as np


def schatten(a: np.ndarray, p: float) -> float:
    singular = np.linalg.svd(a, compute_uv=False)
    if np.isinf(p):
        return float(singular[0])
    return float(np.sum(singular**p) ** (1.0 / p))


def random_unitary(rng: np.random.Generator, n: int) -> np.ndarray:
    z = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    q, r = np.linalg.qr(z)
    phases = np.diag(r)
    phases = phases / np.where(np.abs(phases) == 0, 1, np.abs(phases))
    return q @ np.diag(np.conj(phases))


def random_idempotent(
    rng: np.random.Generator, n: int, rank: int
) -> tuple[np.ndarray, np.ndarray]:
    u = random_unitary(rng, n)
    v = random_unitary(rng, n)
    # Singular values spread over four orders of magnitude to test obliqueness.
    scales = np.geomspace(1.0e-2, 1.0e2, n)
    s = u @ np.diag(scales) @ v.conj().T
    coordinate = np.zeros((n, n), dtype=complex)
    coordinate[:rank, :rank] = np.eye(rank)
    p = s @ coordinate @ np.linalg.inv(s)
    basis, _ = np.linalg.qr(s[:, :rank])
    q = basis @ basis.conj().T
    return p, q


def main() -> None:
    rng = np.random.default_rng(230204816)
    ps = (1.0, 1.5, 2.0, 3.0, np.inf)
    worst_range_ratio = 0.0
    worst_commutator_ratio = 0.0
    cases = 0

    for n in range(2, 9):
        for rank in range(1, n):
            for _ in range(25):
                p0, q0 = random_idempotent(rng, n, rank)
                unitary = random_unitary(rng, n)
                p1 = unitary @ p0 @ unitary.conj().T
                q1 = unitary @ q0 @ unitary.conj().T
                z = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
                h = z + z.conj().T

                for exponent in ps:
                    cp = 1.0 if np.isinf(exponent) else 2.0 ** (1.0 / exponent)
                    lhs = schatten(q1 - q0, exponent)
                    rhs = cp * schatten(p1 - p0, exponent)
                    if lhs > rhs * (1.0 + 2.0e-8):
                        raise AssertionError((n, rank, exponent, lhs, rhs))
                    worst_range_ratio = max(worst_range_ratio, lhs / max(rhs, 1e-300))

                    cq = h @ q0 - q0 @ h
                    cp_oblique = h @ p0 - p0 @ h
                    lhs = schatten(cq, exponent)
                    rhs = cp * schatten(cp_oblique, exponent)
                    if lhs > rhs * (1.0 + 2.0e-8):
                        raise AssertionError(("commutator", n, rank, exponent, lhs, rhs))
                    worst_commutator_ratio = max(
                        worst_commutator_ratio, lhs / max(rhs, 1e-300)
                    )
                    cases += 1

    print(f"passed {cases} norm/exponent cases")
    print(f"largest normalized range-difference ratio: {worst_range_ratio:.8f}")
    print(f"largest normalized commutator ratio: {worst_commutator_ratio:.8f}")


if __name__ == "__main__":
    main()
