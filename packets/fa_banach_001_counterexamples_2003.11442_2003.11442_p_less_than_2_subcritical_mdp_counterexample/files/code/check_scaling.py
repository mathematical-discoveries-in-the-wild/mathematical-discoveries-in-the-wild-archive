"""Sanity checks for the exponents in the p<2 MDP counterexample."""

from fractions import Fraction


def exponents(p: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    beta = Fraction(1, 1) / (4 - p)
    gaussian_big_jump_threshold = p / (2 * (4 - p))
    cost_ratio_power = (p - 2) / 4
    return beta, gaussian_big_jump_threshold, cost_ratio_power


def main() -> None:
    grid = [Fraction(1, 1), Fraction(6, 5), Fraction(3, 2), Fraction(19, 10), Fraction(199, 100)]
    for p in grid:
        beta, threshold, cost_power = exponents(p)
        assert threshold < beta < Fraction(1, 2)
        assert cost_power < 0
        print(
            f"p={float(p):.3f} beta={float(beta):.6f} "
            f"threshold={float(threshold):.6f} cost_power={float(cost_power):.6f}"
        )


if __name__ == "__main__":
    main()
