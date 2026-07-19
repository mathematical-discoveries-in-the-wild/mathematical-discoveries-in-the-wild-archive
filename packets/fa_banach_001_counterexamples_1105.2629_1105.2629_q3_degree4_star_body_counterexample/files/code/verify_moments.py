"""Verify the exact moment arithmetic in the 1105.2629 Question 3 packet."""

from fractions import Fraction


def poly_mul(p, q):
    out = [Fraction(0) for _ in range(len(p) + len(q) - 1)]
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


def poly_pow(p, n):
    out = [Fraction(1)]
    for _ in range(n):
        out = poly_mul(out, p)
    return out


def sphere_z_moment(power):
    """Average of z**power over S^2 with normalized surface measure."""
    if power % 2:
        return Fraction(0)
    return Fraction(1, power + 1)


def avg_poly(poly):
    return sum(c * sphere_z_moment(i) for i, c in enumerate(poly))


def binom_coeff(alpha, j):
    out = Fraction(1)
    for i in range(j):
        out *= alpha - i
    for i in range(1, j + 1):
        out /= i
    return out


def series_power_one_plus(c, moments, alpha, order):
    coeffs = [Fraction(0) for _ in range(order + 1)]
    coeffs[0] = Fraction(1)
    for j in range(1, order + 1):
        coeffs[j] = binom_coeff(alpha, j) * (c**j) * moments[j]
    return coeffs


def series_mul(a, b, order):
    out = [Fraction(0) for _ in range(order + 1)]
    for i, x in enumerate(a[: order + 1]):
        for j, y in enumerate(b[: order + 1 - i]):
            out[i + j] += x * y
    return out


def main():
    # P4(z) = (35 z^4 - 30 z^2 + 3) / 8.
    p4 = [Fraction(3, 8), Fraction(0), Fraction(-30, 8), Fraction(0), Fraction(35, 8)]
    moments = [Fraction(1)]
    for n in range(1, 5):
        moments.append(avg_poly(poly_pow(p4, n)))

    assert moments[1] == 0
    assert moments[2] == Fraction(1, 9)
    assert moments[3] == Fraction(18, 1001)
    assert moments[4] == Fraction(529, 17017)

    # A(eps) = E(1 + eps P4)^3.
    a_coeffs = [
        Fraction(1),
        3 * moments[1],
        3 * moments[2],
        moments[3],
    ]
    assert a_coeffs == [Fraction(1), Fraction(0), Fraction(1, 3), Fraction(18, 1001)]

    # B(eps) = E(1 + (8/3) eps P4)^(3/2), to cubic order.
    b_coeffs = series_power_one_plus(Fraction(8, 3), moments, Fraction(3, 2), 3)
    assert b_coeffs[:4] == [
        Fraction(1),
        Fraction(0),
        Fraction(8, 27),
        Fraction(-64, 3003),
    ]

    # A(eps)^(-1/2) B(eps), to cubic order.
    # Since A = 1 + a2 e^2 + a3 e^3, A^-1/2 has this cubic truncation.
    a_inv_sqrt = [Fraction(1), Fraction(0), -Fraction(1, 2) * a_coeffs[2], -Fraction(1, 2) * a_coeffs[3]]
    ratio_coeffs = series_mul(a_inv_sqrt, b_coeffs, 3)
    assert ratio_coeffs[:4] == [
        Fraction(1),
        Fraction(0),
        Fraction(7, 54),
        Fraction(-1, 33),
    ]

    print("moments:", moments[1:5])
    print("A coefficients through eps^3:", a_coeffs)
    print("B coefficients through eps^3:", b_coeffs[:4])
    print("ratio coefficients through eps^3:", ratio_coeffs[:4])


if __name__ == "__main__":
    main()
