from fractions import Fraction


def norm_upper_for_swapped_test_vector(delta: Fraction) -> Fraction:
    # For U e1 = a e2, U e2 = b e1 with |a|=|b|=1, the third
    # defining functional is bounded by delta + 1/2.
    return max(delta, Fraction(1), delta + Fraction(1, 2))


def main() -> None:
    delta = Fraction(1, 8)
    original_norm = max(Fraction(1), delta, Fraction(1) + delta / 2)
    swapped_upper = norm_upper_for_swapped_test_vector(delta)
    assert original_norm == Fraction(17, 16)
    assert swapped_upper == Fraction(1)
    assert original_norm > swapped_upper
    print("verified diamond isometric-swap obstruction")


if __name__ == "__main__":
    main()
