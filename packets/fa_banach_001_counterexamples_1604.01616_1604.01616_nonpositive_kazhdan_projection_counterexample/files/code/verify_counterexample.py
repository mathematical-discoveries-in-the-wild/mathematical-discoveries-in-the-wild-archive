from fractions import Fraction


def eval_poly(coeffs, z):
    return sum(c * (z ** n) for n, c in coeffs.items())


def main() -> None:
    # p(u) = -2 u^2 + 5 u - 2.
    p = {2: Fraction(-2), 1: Fraction(5), 0: Fraction(-2)}
    assert sum(p.values()) == 1
    assert eval_poly(p, Fraction(1)) == 1
    assert eval_poly(p, Fraction(2)) == 0
    assert eval_poly(p, Fraction(1, 2)) == 0

    # Pointwise obstruction for positive probability measures on Z.
    for n in range(-20, 21):
        assert Fraction(2) ** n + Fraction(2) ** (-n) >= 2

    print("verified polynomial values and positive-moment obstruction")


if __name__ == "__main__":
    main()
