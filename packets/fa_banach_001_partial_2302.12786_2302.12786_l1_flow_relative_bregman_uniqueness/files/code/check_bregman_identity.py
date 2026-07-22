"""Numerical regression checks for the relative-Bregman identity.

This is a sign/algebra check only, not a proof.
"""

from __future__ import annotations

import numpy as np


EPSILON = 0.7
SAMPLES = 10_000
SEED = 230212786


def f(x: np.ndarray) -> float:
    return 0.5 * float(x @ x) + EPSILON * float(np.logaddexp(x, -x).sum() - len(x) * np.log(2.0))


def grad_f(x: np.ndarray) -> np.ndarray:
    return x + EPSILON * np.tanh(x)


def hess_f(x: np.ndarray) -> np.ndarray:
    return np.diag(1.0 + EPSILON / np.cosh(x) ** 2)


def bregman(a: np.ndarray, b: np.ndarray) -> float:
    return f(a) - f(b) - float(grad_f(b) @ (a - b))


def main() -> None:
    rng = np.random.default_rng(SEED)
    max_identity_error = 0.0
    max_remainder_ratio = 0.0
    step = 1.0e-6

    # A valid global Lipschitz constant for the diagonal Hessian is 2*epsilon.
    k_bound = 2.0 * EPSILON

    for _ in range(SAMPLES):
        a, b, adot, bdot = rng.normal(size=(4, 4))
        finite_difference = (
            bregman(a + step * adot, b + step * bdot)
            - bregman(a - step * adot, b - step * bdot)
        ) / (2.0 * step)

        remainder = grad_f(a) - grad_f(b) - hess_f(b) @ (a - b)
        identity_rhs = float((grad_f(a) - grad_f(b)) @ (adot - bdot) + remainder @ bdot)
        max_identity_error = max(max_identity_error, abs(finite_difference - identity_rhs))

        delta_sq = float((a - b) @ (a - b))
        if delta_sq > 1.0e-14:
            ratio = float(np.linalg.norm(remainder) / (0.5 * k_bound * delta_sq))
            max_remainder_ratio = max(max_remainder_ratio, ratio)

    print(f"seed={SEED} samples={SAMPLES}")
    print(f"max_identity_error={max_identity_error:.3e}")
    print(f"max_taylor_bound_ratio={max_remainder_ratio:.6f}")
    if max_identity_error > 1.0e-7:
        raise SystemExit("identity regression failed")
    if max_remainder_ratio > 1.0 + 1.0e-10:
        raise SystemExit("Taylor remainder regression failed")
    print("PASS")


if __name__ == "__main__":
    main()
