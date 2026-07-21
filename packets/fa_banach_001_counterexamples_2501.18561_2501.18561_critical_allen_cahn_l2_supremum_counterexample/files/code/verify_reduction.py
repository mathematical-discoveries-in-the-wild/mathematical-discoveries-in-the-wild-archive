#!/usr/bin/env python3
"""Exact algebra checks for the critical Allen--Cahn counterexample.

This is a verifier for the displayed Itô identities and the elementary
occupation-integral scaling.  The small-ball probability argument itself is
proved in the packet and is not delegated to computation.
"""

import sympy as sp


def main() -> None:
    x, y, r, eps, k, h = sp.symbols("x y r eps k h", positive=True)

    # Lf for f(x)=1/x under dX=(X-X^3)dt+sqrt(2)X^2dW.
    f = 1 / x
    generator_f = sp.diff(f, x) * (x - x**3) + x**4 * sp.diff(f, x, 2)
    expected_y_drift = -1 / x + 3 * x
    assert sp.simplify(generator_f - expected_y_drift) == 0

    # After y=sqrt(2)r, (1/sqrt(2))(-y+3/y)=-r+3/(2r).
    radial_drift = sp.simplify((-y + 3 / y).subs(y, sp.sqrt(2) * r) / sp.sqrt(2))
    assert sp.simplify(radial_drift - (-r + sp.Rational(3, 2) / r)) == 0

    # Conversely, X=1/(sqrt(2)R) applied to the 4D radial OU generator.
    g = 1 / (sp.sqrt(2) * r)
    radial_generator_g = (
        sp.diff(g, r) * (-r + sp.Rational(3, 2) / r)
        + sp.Rational(1, 2) * sp.diff(g, r, 2)
    )
    expected_x_drift = g - g**3
    expected_diffusion_magnitude = sp.sqrt(2) * g**2
    assert sp.simplify(radial_generator_g - expected_x_drift) == 0
    assert sp.simplify(-sp.diff(g, r) - expected_diffusion_magnitude) == 0

    # If h0=sqrt(k) eps^2, the split upper bound for
    # integral_0^infinity min(1,k eps^4 h^-2) dh equals 2 sqrt(k) eps^2.
    h0 = sp.sqrt(k) * eps**2
    split_integral = h0 + sp.integrate(k * eps**4 / h**2, (h, h0, sp.oo))
    assert sp.simplify(split_integral - 2 * sp.sqrt(k) * eps**2) == 0

    print("PASS: reciprocal Itô generator identity")
    print("PASS: four-dimensional radial OU rescaling")
    print("PASS: reciprocal OU-to-scalar drift and diffusion")
    print("PASS: occupation-kernel integral is O(epsilon^2)")


if __name__ == "__main__":
    main()
