"""Symbolic and numerical checks for the Plucker ell-p (AC2) counterexample.

The symbolic assertions check the displayed algebra in the proof packet.  The
numerical bisection is only a sanity check; the proof needs no numerical root.
"""

from __future__ import annotations

import math

import sympy as sp


def skew(z: tuple[sp.Expr, ...]) -> sp.Matrix:
    """Return the 4 by 4 skew matrix in (12,13,14,23,24,34) order."""
    z12, z13, z14, z23, z24, z34 = z
    return sp.Matrix(
        [
            [0, z12, z13, z14],
            [-z12, 0, z23, z24],
            [-z13, -z23, 0, z34],
            [-z14, -z24, -z34, 0],
        ]
    )


def symbolic_checks() -> None:
    a, b, t = sp.symbols("a b t", positive=True)
    alpha, beta, theta = sp.symbols("alpha beta theta", positive=True)
    lam = sp.symbols("lambda")

    x = (a, -t, t, t, t, -b)
    y = (b, -t, t, t, t, -a)
    phix = (alpha, -theta, theta, theta, theta, -beta)
    phiy = (beta, -theta, theta, theta, theta, -alpha)

    plucker_x = sp.expand(x[0] * x[5] - x[1] * x[4] + x[2] * x[3])
    plucker_y = sp.expand(y[0] * y[5] - y[1] * y[4] + y[2] * y[3])
    relation = {t**2: a * b / 2}
    assert sp.expand(plucker_x).subs(relation) == 0
    assert sp.expand(plucker_y).subs(relation) == 0
    norm_sq = sum(v**2 for v in x)
    norm_reduced = sp.expand(norm_sq.subs(relation).subs(b, 1 - a))
    assert sp.simplify(norm_reduced - 1) == 0

    bx = skew(phix) * skew(x).T
    by = skew(phiy) * skew(y).T

    d1 = alpha * a + 2 * theta * t
    d2 = beta * b + 2 * theta * t
    r = alpha * t + theta * b
    s = beta * t + theta * a
    expected_x = sp.Matrix(
        [[d1, 0, -r, -r], [0, d1, -r, r], [-s, -s, d2, 0], [-s, s, 0, d2]]
    )
    expected_y = sp.Matrix(
        [[d2, 0, -s, -s], [0, d2, -s, s], [-r, -r, d1, 0], [-r, r, 0, d1]]
    )
    assert bx == expected_x
    assert by == expected_y

    d = (alpha * a + beta * b) / 2 + 2 * theta * t
    c = ((alpha + beta) * t + theta) / 2  # uses a+b=1
    average = ((bx + by) / 2).subs(b, 1 - a)
    target = sp.Matrix(
        [[d, 0, -c, -c], [0, d, -c, c], [-c, -c, d, 0], [-c, c, 0, d]]
    ).subs(b, 1 - a)
    assert sp.simplify(average - target) == sp.zeros(4)
    charpoly = sp.factor((target - lam * sp.eye(4)).det())
    expected_charpoly = (((lam - d) ** 2 - 2 * c**2) ** 2).subs(b, 1 - a)
    assert sp.simplify(charpoly - expected_charpoly) == 0


def smaller_eigenvalue(p: float, a: float = 0.8, b: float = 0.2) -> float:
    t = math.sqrt(a * b / 2.0)
    q = p - 1.0
    alpha, beta, theta = a**q, b**q, t**q
    d = (alpha * a + beta * b) / 2.0 + 2.0 * theta * t
    c = ((alpha + beta) * t + theta) / 2.0
    return d - math.sqrt(2.0) * c


def bisect_root(lo: float = 1.0, hi: float = 2.0, steps: int = 100) -> float:
    assert smaller_eigenvalue(lo) < 0 < smaller_eigenvalue(hi)
    for _ in range(steps):
        mid = (lo + hi) / 2.0
        if smaller_eigenvalue(mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


if __name__ == "__main__":
    symbolic_checks()
    root = bisect_root()
    print("symbolic checks: passed")
    print(f"p0 (a=4/5,b=1/5): {root:.16f}")
    print(f"D(1): {smaller_eigenvalue(1.0):.16e}")
    print(f"D(p0): {smaller_eigenvalue(root):.16e}")
    print(f"D(2): {smaller_eigenvalue(2.0):.16e}")
