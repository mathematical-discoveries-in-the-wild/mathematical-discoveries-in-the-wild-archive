#!/usr/bin/env python3
"""Directed-interval certificate for the density-two sech counterexample.

The script verifies the numerical inputs in the Poincare--Miranda proof.
It uses mpmath's interval context, evaluates symmetric partial sums through
n = TRUNCATION, adds explicit geometric tail bounds, and checks the face-sign
margins after preconditioning.
"""

from mpmath import iv


iv.dps = 80
TRUNCATION = 240


def sech(u):
    """Interval-safe hyperbolic secant without relying on iv.cosh."""
    eu = iv.exp(u)
    emu = iv.exp(-u)
    return 2 / (eu + emu)


def tanh(u):
    """Interval-safe hyperbolic tangent without relying on iv.tanh."""
    eu = iv.exp(u)
    emu = iv.exp(-u)
    return (eu - emu) / (eu + emu)


def symmetric_tail_power(r, first_n, power):
    """Bound sum_{n>=first_n} (n+1/2)^power r^(n+1/2)."""
    x = iv.mpf(first_n) + iv.mpf(1) / 2
    first = x**power * r**x
    ratio = r * ((x + 1) / x) ** power
    assert ratio < 1
    return first / (1 - ratio)


def finite_center_data():
    a0 = 1 / iv.sqrt(28)
    c0 = iv.mpf(15) / 28

    fr = iv.mpf(0)
    fi = iv.mpf(0)
    far = iv.mpf(0)
    fai = iv.mpf(0)
    fcr = iv.mpf(0)
    fci = iv.mpf(0)

    # The summand is even in x = k+1/2, hence the factor 2.
    for n in range(TRUNCATION + 1):
        x = iv.mpf(n) + iv.mpf(1) / 2
        u = iv.pi * a0 * x
        s = sech(u)
        t = tanh(u)
        phase = iv.pi * c0 * x * x
        co = iv.cos(phase)
        si = iv.sin(phase)

        fr += 2 * s * co
        fi += 2 * s * si

        da_amp = -iv.pi * x * s * t
        far += 2 * da_amp * co
        fai += 2 * da_amp * si

        dc_amp = iv.pi * x * x * s
        fcr += 2 * (-dc_amp * si)
        fci += 2 * dc_amp * co

    r = iv.exp(-iv.pi * a0)
    first_n = TRUNCATION + 1
    tail0 = 4 * symmetric_tail_power(r, first_n, 0)
    taila = 4 * iv.pi * symmetric_tail_power(r, first_n, 1)
    tailc = 4 * iv.pi * symmetric_tail_power(r, first_n, 2)
    unit = iv.mpf([-1, 1])

    return (
        fr + unit * tail0,
        fi + unit * tail0,
        far + unit * taila,
        fai + unit * taila,
        fcr + unit * tailc,
        fci + unit * tailc,
    )


def verify_hessian_bounds():
    # On the whole proof box a >= 0.188, so exp(-pi*a) < exp(-0.59) < 0.555.
    a0 = 1 / iv.sqrt(28)
    radius = iv.mpf(1) / 10**6
    assert a0 - radius > iv.mpf("0.188")
    assert iv.pi * iv.mpf("0.188") > iv.mpf("0.59")
    assert iv.exp(-iv.mpf("0.59")) < iv.mpf("0.555")

    # sech(pi*a*x) <= 2 exp(-pi*a*|x|), pi^2 < 10, and symmetry
    # reduce each derivative sum to 40 sum_{n>=0}(n+1/2)^k 0.555^(n+1/2).
    r = iv.mpf("0.555")
    cutoff = 400
    claimed = {2: iv.mpf(400), 3: iv.mpf(2100), 4: iv.mpf(14000)}
    for power, bound in claimed.items():
        partial = iv.mpf(0)
        for n in range(cutoff):
            x = iv.mpf(n) + iv.mpf(1) / 2
            partial += x**power * r**x
        total = partial + symmetric_tail_power(r, cutoff, power)
        assert 40 * total < bound
    return claimed


def main():
    fr, fi, far, fai, fcr, fci = finite_center_data()
    assert abs(fr) < iv.mpf("1e-40")
    assert abs(fi) < iv.mpf("1e-40")

    # Rational decimal preconditioner used in the proof packet.
    a11 = iv.mpf("0.07386071204")
    a12 = iv.mpf("-0.11010607132")
    a21 = iv.mpf("-0.01062523295")
    a22 = iv.mpf("-0.02565158148")

    # J = D(Re F, Im F)/D(a,c), and E = A J - I.
    e11 = a11 * far + a12 * fai - 1
    e12 = a11 * fcr + a12 * fci
    e21 = a21 * far + a22 * fai
    e22 = a21 * fcr + a22 * fci - 1
    for entry in (e11, e12, e21, e22):
        assert abs(entry) < iv.mpf("1e-9")

    bounds = verify_hessian_bounds()
    radius = iv.mpf("1e-6")
    scalar_remainder = (
        bounds[2] * radius**2
        + 2 * bounds[3] * radius**2
        + bounds[4] * radius**2
    ) / 2
    row1 = abs(a11) + abs(a12)
    row2 = abs(a21) + abs(a22)
    remainder1 = row1 * scalar_remainder
    remainder2 = row2 * scalar_remainder

    center1 = abs(a11) * abs(fr) + abs(a12) * abs(fi)
    center2 = abs(a21) * abs(fr) + abs(a22) * abs(fi)
    linear_error = 2 * iv.mpf("1e-9") * radius
    margin1 = radius - center1 - linear_error - remainder1
    margin2 = radius - center2 - linear_error - remainder2
    assert margin1 > 0
    assert margin2 > 0

    print("CERTIFIED")
    print("Re F(a0,c0):", fr)
    print("Im F(a0,c0):", fi)
    print("F_a:", far, fai)
    print("F_c:", fcr, fci)
    print("max |A J - I| < 1e-9")
    print("scalar Taylor remainder:", scalar_remainder)
    print("preconditioned row remainders:", remainder1, remainder2)
    print("strict face margins:", margin1, margin2)


if __name__ == "__main__":
    main()
