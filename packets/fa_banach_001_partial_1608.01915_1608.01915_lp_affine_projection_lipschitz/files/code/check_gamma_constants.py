"""Numerical sanity check for the ell_p affine-projection packet.

This is not part of the proof. It samples the explicit upper bound

  (E A_1^{2p})^{1/p} / (2 E Z_1^2)

that appears in the packet, where Z is uniform on B_p^n and A_1 is the
coordinate slice half-width.
"""

import math


def ratio(p: float, n: int) -> float:
    log_ea = (
        math.lgamma(3 + 1 / p)
        + math.lgamma(1 + n / p)
        - math.lgamma(1 + 1 / p)
        - math.lgamma(3 + n / p)
    )
    log_sigma2 = (
        math.lgamma(3 / p)
        + math.lgamma(1 + n / p)
        - math.lgamma(1 / p)
        - math.lgamma(1 + (n + 2) / p)
    )
    return 0.5 * math.exp(log_ea / p - log_sigma2)


if __name__ == "__main__":
    for p in [1, 1.2, 1.5, 2, 3, 5, 10, 50]:
        values = [ratio(p, n) for n in [1, 2, 3, 5, 10, 30, 100, 1000]]
        print(f"p={p:>4}: max_sample={max(values):.6f}, n=1000={values[-1]:.6f}")
