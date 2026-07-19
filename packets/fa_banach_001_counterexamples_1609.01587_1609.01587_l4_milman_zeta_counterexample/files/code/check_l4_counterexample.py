from decimal import Decimal, getcontext
from fractions import Fraction


def fourth_root(x: Decimal) -> Decimal:
    return x.sqrt().sqrt()


def main() -> None:
    getcontext().prec = 80

    rational_upper = Fraction(251, 250) ** 4 + Fraction(1, 3) ** 4
    beta_fourth = Fraction(17, 16)
    gap = beta_fourth - rational_upper

    print("rational upper bound for candidate fourth power:")
    print(rational_upper)
    print("beta fourth power:")
    print(beta_fourth)
    print("exact fourth-power gap:")
    print(gap)
    assert gap > 0

    s = Decimal(1) / Decimal(6)
    a = fourth_root(Decimal(1) - s**4)
    r = (s / a) ** 3
    c = fourth_root(Decimal(1) / (Decimal(1) + r**4))

    first = a + c * r / Decimal(2)
    second = s - c / Decimal(2)
    candidate = fourth_root(first**4 + abs(second) ** 4)
    beta = fourth_root(Decimal(17) / Decimal(16))

    print("candidate norm:")
    print(candidate)
    print("beta^- + 1:")
    print(beta)
    print("norm gap:")
    print(beta - candidate)
    assert candidate < beta


if __name__ == "__main__":
    main()
