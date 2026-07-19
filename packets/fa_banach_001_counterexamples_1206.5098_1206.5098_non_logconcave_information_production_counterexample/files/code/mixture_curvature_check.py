"""Sanity check for the Gaussian-mixture curvature counterexample.

This script numerically evaluates

    int ((log h_s)''(x))^2 h_s(x) dx

where h_s is the symmetric two-Gaussian mixture with means +/-a and common
variance s^2.  The formal packet proves strict failure by an analytic limiting
argument; these numbers are only a reproducibility check.
"""

import mpmath as mp


def lhs(a: mp.mpf, sigma: mp.mpf) -> mp.mpf:
    s = mp.sqrt(1 + a * a * sigma * sigma)
    normal = 1 / (mp.sqrt(2 * mp.pi) * s)

    def h(x):
        return normal * mp.e ** (-(x * x + a * a) / (2 * s * s)) * mp.cosh(
            a * x / (s * s)
        )

    def curvature(x):
        z = a * x / (s * s)
        return -1 / (s * s) + (a * a / (s**4)) / (mp.cosh(z) ** 2)

    return mp.quad(lambda x: curvature(x) ** 2 * h(x), [-mp.inf, mp.inf])


def main() -> None:
    mp.mp.dps = 50
    a = mp.mpf(5) / 2
    for sigma_text in ["0", "0.01", "0.02", "0.05"]:
        sigma = mp.mpf(sigma_text)
        value = lhs(a, sigma)
        print(f"a={a}, sigma={sigma}: lhs={value}, lhs-1={value - 1}")


if __name__ == "__main__":
    main()
