#!/usr/bin/env python3
"""Explore higher radial-quadratic Weyl coefficients with exact arithmetic."""

from __future__ import annotations

import argparse
import time

import sympy as sp


def coefficient(dimension: int, order: int):
    a, b, c, w = sp.symbols("a b c w")
    d = sp.Integer(dimension)
    L = b + w**2
    K0 = 1 / L

    def da(F):
        return sp.diff(F, a) + sp.diff(F, w)

    def dx(F):
        return 2*d*da(F) + 4*a*da(da(F)) + 4*c*da(sp.diff(F, c)) + b*sp.diff(F, c, 2)

    def dxi(F):
        return 2*d*sp.diff(F, b) + 4*b*sp.diff(F, b, 2) + 4*c*sp.diff(F, b, c) + a*sp.diff(F, c, 2)

    def s2(F):
        hessian = 2*a*sp.diff(F, b) + 4*c**2*sp.diff(F, b, 2) + 4*a*c*sp.diff(F, b, c) + a**2*sp.diff(F, c, 2)
        return sp.Rational(1, 4)*dx(F) + sp.Rational(1, 2)*w*dxi(F) + hessian

    def s4(F):
        return sp.Rational(1, 16)*dxi(dxi(F))

    ks = [K0]
    for j in range(1, order + 1):
        older = ks[j - 2] if j >= 2 else 0
        ks.append(sp.factor(-K0*(s2(ks[j - 1]) + s4(older))))
    return (a, b, c, w, L), ks[-1]


def exact_c(dimension: int, order: int, mu: int):
    (a, b, c, w, L), K = coefficient(dimension, order)
    d = sp.Integer(dimension)
    mu = sp.Integer(mu)
    q = 3*order + 1
    numerator, denominator = sp.together(K).as_numer_denom()
    denominator_constant = sp.simplify(denominator / L**q)
    assert not denominator_constant.has(a, b, c, w)

    total = 0
    groups = {}
    contributing_symbol = {}
    polynomial = sp.Poly(sp.expand(numerator), a, b, c, w)
    # Average over the xi sphere before integrating radially.  At the top
    # critical dimension, apparently nonintegrable highest-degree monomials
    # cancel exactly under this average.
    averaged = {}
    for (pa, pb, pc, pw), raw in polynomial.terms():
        assert pc % 2 == 0
        k = pc // 2
        radial = pb + k
        coefficient_ = sp.Rational(raw) / denominator_constant
        angular = sp.rf(sp.Rational(1, 2), k) / sp.rf(d/2, k)
        key = (pa + k, radial, pw)
        averaged[key] = sp.simplify(averaged.get(key, 0) + coefficient_*angular)

    for (xp, radial, pw), coefficient_ in sorted(averaged.items()):
        if coefficient_ == 0:
            continue
        cp = pw + 2*radial + d - 2*q + 1
        if cp >= 0:
            # These are polynomial-in-z pieces after analytic continuation;
            # their contour integrals vanish before the radial trace is taken.
            continue
        gap = q - radial - d/2
        assert gap > 0, (xp, radial, pw, coefficient_, gap)
        xi = sp.pi**(d/2)*sp.gamma(radial+d/2)*sp.gamma(gap)/(sp.gamma(d/2)*sp.gamma(q))
        ell = -cp - 1
        contributing_symbol.setdefault((xp, ell), []).append((radial, pw, coefficient_))
        contour = (-1)**(-cp) / sp.factorial(ell)
        fder = (-1)**ell * sp.rf(mu, ell)
        xint = sp.pi**(d/2)*sp.gamma(xp+d/2)*sp.gamma(mu+ell-xp-d/2)/(sp.gamma(d/2)*sp.gamma(mu+ell))
        term = sp.simplify(-2*(2*sp.pi)**(-d)*coefficient_*xi*contour*fder*xint)
        total += term
        groups[(xp, ell)] = sp.simplify(groups.get((xp, ell), 0) + term)
    groups = {key: sp.factor(value) for key, value in sorted(groups.items()) if value != 0}
    return sp.factor(sp.simplify(total)), groups, len(polynomial.terms()), contributing_symbol


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("order", type=int)
    parser.add_argument("dimension", type=int)
    parser.add_argument("mu", type=int)
    parser.add_argument("--raw", action="store_true")
    args = parser.parse_args()
    start = time.monotonic()
    result, groups, terms, symbol = exact_c(args.dimension, args.order, args.mu)
    print(f"j={args.order}, d={args.dimension}, mu={args.mu}, numerator monomials={terms}")
    for key, value in groups.items():
        print(f"  {key}: {value}")
        if args.raw:
            for radial, pw, coefficient_ in symbol[key]:
                print(f"    radial={radial}, w-power={pw}, averaged coefficient={coefficient_}")
    print(f"TOTAL: {result}")
    print(f"sign: {sp.sign(result)}, elapsed: {time.monotonic()-start:.2f}s")


if __name__ == "__main__":
    main()
