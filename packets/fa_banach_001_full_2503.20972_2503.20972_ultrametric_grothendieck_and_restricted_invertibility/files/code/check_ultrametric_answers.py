"""Deterministic arithmetic audit for the two answers to arXiv:2503.20972."""

from fractions import Fraction
from itertools import product


def valuation(n: int, p: int) -> int:
    """Return v_p(n) for a nonzero integer."""
    assert n
    n = abs(n)
    out = 0
    while n % p == 0:
        n //= p
        out += 1
    return out


def p_abs(x: Fraction, p: int) -> Fraction:
    if x == 0:
        return Fraction(0)
    exponent = valuation(x.numerator, p) - valuation(x.denominator, p)
    return Fraction(1, p**exponent) if exponent >= 0 else Fraction(p ** (-exponent))


def sup_norm(vector: tuple[Fraction, ...], p: int) -> Fraction:
    return max((p_abs(x, p) for x in vector), default=Fraction(0))


def inner(left: tuple[Fraction, ...], right: tuple[Fraction, ...]) -> Fraction:
    return sum((x * y for x, y in zip(left, right)), Fraction(0))


def check_grothendieck(p: int) -> None:
    # Every entry is p-adically integral, hence has absolute value at most one.
    matrix = ((Fraction(1), Fraction(p)), (Fraction(p**2), Fraction(-1)))
    scalars = tuple(Fraction(x) for x in (-p, -1, 0, 1, p))
    for s in product(scalars, repeat=2):
        for t in product(scalars, repeat=2):
            value = sum(
                (matrix[j][k] * s[j] * t[k] for j in range(2) for k in range(2)),
                Fraction(0),
            )
            assert p_abs(value, p) <= sup_norm(s, p) * sup_norm(t, p)

    vectors = tuple(product(scalars, repeat=2))
    for u in product(vectors, repeat=2):
        for v in product(vectors, repeat=2):
            value = sum(
                (
                    matrix[j][k] * inner(u[j], v[k])
                    for j in range(2)
                    for k in range(2)
                ),
                Fraction(0),
            )
            rhs = max(sup_norm(x, p) for x in u) * max(sup_norm(x, p) for x in v)
            assert p_abs(value, p) <= rhs

    # The one-dimensional sharpness example has ratio exactly one.
    assert p_abs(Fraction(1), p) == Fraction(1)


def identical_column_map(x: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    return (sum(x, Fraction(0)),) + (Fraction(0),) * (len(x) - 1)


def check_restricted_invertibility_counterexample(p: int, dimension: int = 4) -> None:
    scalars = tuple(Fraction(x) for x in (-p, -1, 0, 1, p))
    for x in product(scalars, repeat=dimension):
        assert sup_norm(identical_column_map(x), p) <= sup_norm(x, p)

    e1 = (Fraction(1),) + (Fraction(0),) * (dimension - 1)
    assert sup_norm(identical_column_map(e1), p) == sup_norm(e1, p) == 1

    cancellation = (Fraction(1), Fraction(-1)) + (Fraction(0),) * (dimension - 2)
    assert identical_column_map(cancellation) == (Fraction(0),) * dimension
    assert sup_norm(cancellation, p) == 1


def main() -> None:
    for prime in (2, 3, 5):
        check_grothendieck(prime)
        check_restricted_invertibility_counterexample(prime)
    print("ultrametric Grothendieck and restricted-invertibility audits: PASS")


if __name__ == "__main__":
    main()
