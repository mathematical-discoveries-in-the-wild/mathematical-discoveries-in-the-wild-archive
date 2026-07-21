"""Exact n=5 check for the proposed common-coefficient Bell pattern."""

from math import factorial


def multinomial(parts: tuple[int, ...]) -> int:
    value = factorial(sum(parts))
    for part in parts:
        value //= factorial(part)
    return value


# Partitions of 4 into two positive parts, encoded by multiplicities of 1,2,3.
# 1+3 gives alpha_2 alpha_4; 2+2 gives alpha_3^2.
coeff_alpha2_alpha4 = multinomial((1, 0, 1))
coeff_alpha3_squared = multinomial((0, 2, 0))

assert coeff_alpha2_alpha4 == 2
assert coeff_alpha3_squared == 1

outer_factor = 5 * 6 // 2  # binomial(6,2)
assert outer_factor * coeff_alpha2_alpha4 == 30
assert outer_factor * coeff_alpha3_squared == 15

print("B^o_{4,2} = 2 alpha_2 alpha_4 + alpha_3^2")
print("n=5 coefficients after binomial(6,2): 30 and 15")
print("No single common m_2 can produce both coefficients.")

