"""Verify the finite residue calculation used in the packet.

The construction has deterministic residue weights modulo 3
    d_0 = 1/2, d_1 = 1, d_2 = 0.
After normalizing by the total density delta = (d_0+d_1+d_2)/3 = 1/2,
the Fourier-Bohr coefficient at lambda with lambda^3 = 1 is
    c(lambda) = (1/(3 delta)) * sum_r d_r lambda^r.
"""

from __future__ import annotations

import cmath
import math


weights = [0.5, 1.0, 0.0]
delta = sum(weights) / 3.0

for j in range(3):
    lam = cmath.exp(2j * math.pi * j / 3)
    coeff = sum(w * lam**r for r, w in enumerate(weights)) / (3.0 * delta)
    print(j, complex(round(coeff.real, 12), round(coeff.imag, 12)))

