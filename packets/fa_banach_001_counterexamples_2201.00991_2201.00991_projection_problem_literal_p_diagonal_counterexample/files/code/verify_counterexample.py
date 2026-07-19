"""Verify the arithmetic in the 2201.00991 projection-problem counterexample."""

from fractions import Fraction


def main() -> None:
    target = Fraction(1, 2)
    epsilon = Fraction(1, 2)
    lower = (1 - epsilon) * target
    upper = (1 + epsilon) * target
    diagonal = [Fraction(3, 5), Fraction(2, 5)]

    print(f"target n/d = {target}")
    print(f"epsilon interval = [{lower}, {upper}]")
    for idx, value in enumerate(diagonal, start=1):
        print(f"k={idx}: value={value}, in interval={lower <= value <= upper}")
    print("conclusion would require every displayed P-diagonal value to equal 1/2")
    print("contradictions:", [value != target for value in diagonal])


if __name__ == "__main__":
    main()
