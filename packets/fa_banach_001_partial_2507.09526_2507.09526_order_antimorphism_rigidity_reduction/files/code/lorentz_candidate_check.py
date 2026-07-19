"""Check a failed non-Hilbert Lorentz-cone inversion candidate.

The packet theorem is purely formal and does not use this script. This file
records an abandoned counterexample route: the Hilbert/Lorentz inversion formula
does not remain order reversing for the cone

    C = {(t, x): t > ||x||_3}

over l_3^2.
"""

from __future__ import annotations


def norm_p(x: tuple[float, ...], p: float) -> float:
    return sum(abs(a) ** p for a in x) ** (1.0 / p)


def sub(u: tuple[float, tuple[float, ...]], v: tuple[float, tuple[float, ...]]):
    return (u[0] - v[0], tuple(a - b for a, b in zip(u[1], v[1])))


def leq(u, v, p: float) -> tuple[bool, float]:
    """Return whether u <= v in the Lorentz-type cone and the order margin."""
    dt, dx = sub(v, u)
    margin = dt - norm_p(dx, p)
    return margin >= -1e-12, margin


def candidate_j(u, p: float):
    t, x = u
    n = norm_p(x, p)
    den = t * t - n * n
    return (t / den, tuple(-a / den for a in x))


def main() -> None:
    p = 3.0
    a = (2.138479320430561, (1.8731542822513139, 1.1110113078764292))
    b = (3.571582887109277, (1.2983431865747295, 2.3609495223285495))
    ja = candidate_j(a, p)
    jb = candidate_j(b, p)

    ab_ok, ab_margin = leq(a, b, p)
    reverse_ok, reverse_margin = leq(jb, ja, p)

    print(f"p={p}")
    print(f"a <= b: {ab_ok}, margin={ab_margin:.12g}")
    print(f"J(b) <= J(a): {reverse_ok}, margin={reverse_margin:.12g}")
    if ab_ok and not reverse_ok:
        print("The candidate formula is not order reversing for this non-Hilbert norm.")
    else:
        raise SystemExit("unexpected check result")


if __name__ == "__main__":
    main()
