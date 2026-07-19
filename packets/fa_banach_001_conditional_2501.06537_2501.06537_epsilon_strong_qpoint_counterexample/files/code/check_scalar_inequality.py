"""Scalar sanity check for the dilution packet.

The proof uses:

1. eta-strong source measure, diluted by t, remains eps-strong when
   eps < t*eta.
2. t < delta < 1/2 makes the final contradiction
   2*delta*M < M < M + eps*M*(1 - 2*delta).
"""

samples = [
    # eta, eps, t, delta
    (1.00, 0.05, 0.10, 0.20),
    (1.00, 0.24, 0.30, 0.40),
    (0.60, 0.10, 0.20, 0.35),
    (0.20, 0.04, 0.45, 0.49),
]

for eta, eps, t, delta in samples:
    assert 0 < eta <= 1
    assert 0 < eps < t * eta
    assert 0 < t < delta < 0.5
    left = 2 * delta
    right = 1 + eps * (1 - 2 * delta)
    assert left < 1 < right
    print(
        f"eta={eta:.3f}, eps={eps:.3f}, t={t:.3f}, delta={delta:.3f}: "
        f"eps < t*eta={t * eta:.3f}; {left:.3f} < 1 < {right:.3f}"
    )
