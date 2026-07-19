"""Check the scalar formula used in the solution packet.

For the real one-dimensional space R, the unit sphere is {-1, 1}.
For 0 < d < 2 the only admissible pair in the definition of U_R(d; a)
is the antipodal pair.  The exact formula is

    U_R(d; a) = min(2a, 2).

This script samples values of a and compares the formula against a
grid maximization of ||1+z| - |-1+z|| over |z| <= a.
"""

from __future__ import annotations


def exact_scalar_modulus(a: float) -> float:
    return min(2.0 * a, 2.0)


def grid_scalar_modulus(a: float, steps: int = 200_000) -> float:
    best = 0.0
    for i in range(steps + 1):
        z = -a + (2.0 * a * i / steps)
        value = abs(abs(1.0 + z) - abs(-1.0 + z))
        if value > best:
            best = value
    return best


def main() -> None:
    samples = [0.01, 0.05, 0.125, 0.5, 0.9, 1.0, 1.5, 3.0]
    worst = 0.0
    for a in samples:
        exact = exact_scalar_modulus(a)
        grid = grid_scalar_modulus(a)
        error = abs(exact - grid)
        worst = max(worst, error)
        print(f"a={a:>5g} exact={exact:.12g} grid={grid:.12g} error={error:.3e}")

    print(f"worst error: {worst:.3e}")
    print("status:", "ok" if worst < 1e-9 else "check failed")


if __name__ == "__main__":
    main()
