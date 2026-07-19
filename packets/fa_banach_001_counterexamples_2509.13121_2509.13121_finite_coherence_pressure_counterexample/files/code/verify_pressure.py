"""Exact check for the finite-coherence pressure counterexample.

Model:
    H = R^2 with Euclidean norm.
    x_infty = 0.
    C1 = {e1, e2}.
    Delta = diam(C1) = sqrt(2).

For a k-tuple from C1, the inner infimum in Phi_k is zero as soon as
the tuple repeats a point, because coefficients 1/2 and -1/2 cancel on
the repeated entries.  Otherwise k is 1 or 2 and the infimum is computed
directly.
"""

from __future__ import annotations

from itertools import product
from math import sqrt


DELTA = sqrt(2.0)


def tuple_infimum(labels: tuple[int, ...]) -> float:
    """Return inf_{||a||_1=1} ||sum a_i y_i|| / Delta for labels in {0,1}."""
    if len(set(labels)) < len(labels):
        return 0.0
    if len(labels) == 1:
        return 1.0 / DELTA
    if set(labels) == {0, 1}:
        # Minimize sqrt(a^2+b^2)/sqrt(2) subject |a|+|b|=1.
        return (1.0 / sqrt(2.0)) / DELTA
    raise ValueError(f"unexpected tuple {labels!r}")


def phi(k: int) -> float:
    return max(tuple_infimum(t) for t in product((0, 1), repeat=k))


def main() -> None:
    print("C1 = {e1, e2}, Delta = sqrt(2), mutual coherence mu = 0")
    for k in range(1, 7):
        print(f"Phi_{k} = {phi(k):.12g}")
    print("P = inf_k Phi_k = 0, already because Phi_3 = 0.")


if __name__ == "__main__":
    main()
