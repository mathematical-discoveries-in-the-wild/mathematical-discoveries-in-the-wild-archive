#!/usr/bin/env python3
"""Exact rational verification of the Conjecture 4.3 counterexample.

No numerical quadrature is used.  The Hardy H^4 norms are reduced by
Parseval to H^2 coefficient sums.
"""

from fractions import Fraction as F


def convolution(a, b):
    out = [F(0) for _ in range(len(a) + len(b) - 1)]
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return out


def dot(a, b):
    return sum((ai * bi for ai, bi in zip(a, b)), F(0))


# f(z) = 1/2 - 3z + 2z^3 - z^5.
f = [F(1, 2), F(-3), F(0), F(2), F(0), F(-1)]
f2 = convolution(f, f)

# Common diagonal contribution in ||(1 - uf)^2||_2^2 when u is inner.
s = dot(f, f)
t = dot(f2, f2)
common = F(1) + 4 * s + t
assert s == F(57, 4)
assert t == F(5697, 16)
assert common == F(6625, 16)

# For |c|=1 and x=Re(c), direct coefficient expansion gives
# ||1-cf||_4^4 = common - 2e^2 - 4(e+U)x + 4e^2 x^2,
# where e=f(0) and U=<f,f^2>.
e = f[0]
u = sum(
    (f[n] * f2[n] for n in range(len(f))),
    F(0),
)
assert u == F(113, 8)
quadratic_constant = common - 2 * e * e
quadratic_linear = -4 * (e + u)
quadratic_square = 4 * e * e
assert quadratic_constant == F(6617, 16)
assert quadratic_linear == F(-117, 2)
assert quadratic_square == F(1)

# Its derivative 2x-117/2 is negative throughout [-1,1], so x=1 is
# the exact global minimizer.
assert 2 * F(1) + quadratic_linear < 0
right_min = quadratic_constant + quadratic_linear + quadratic_square
assert right_min == F(5697, 16)

# J(z)=(z-a)/(1-az), a=1/4.  Its Taylor coefficients are
# j_0=-a and j_n=(1-a^2)a^(n-1) for n>=1.
a = F(1, 4)
j = [-a] + [(1 - a * a) * a ** (n - 1) for n in range(1, len(f))]
jf2 = convolution(j, f2)
mixed = sum(
    (f[n] * jf2[n] for n in range(len(f))),
    F(0),
)
assert mixed == F(353249, 16384)

jf_at_zero = (-a) * e
left = common - 4 * jf_at_zero + 2 * jf_at_zero**2 - 4 * mixed
assert left == F(1344927, 4096)

gap = right_min - left
assert gap == F(113505, 4096)
assert gap > 0

print(f"||1-Jf||_4^4 = {left}")
print(f"inf_|c|=1 ||1-cf||_4^4 = {right_min}")
print(f"strict reversed gap = {gap}")
print("PASS: Conjecture 4.3 is violated for every unimodular c.")
