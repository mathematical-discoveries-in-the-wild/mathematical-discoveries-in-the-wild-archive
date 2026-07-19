"""Numerically sample the finite block ratio for the packet.

This is only a sanity check. The packet proof uses compactness/calculus.
"""

import math


def sample(eps=0.25, samples=400_000):
    best = float("inf")
    best_data = None
    kappa = eps + math.sqrt(1.0 - eps * eps)
    for j in (0, 1):
        for k in range(samples):
            theta = 2.0 * math.pi * k / samples
            x = math.cos(theta)
            y = math.sin(theta)
            sig = 1.0 if x + y > 1e-12 else -1.0 if x + y < -1e-12 else 0.0
            norm = 1.0 + eps * abs(x + y)
            if j == 0:
                dist = kappa * abs(y)
                g = (x + eps * sig) / (1.0 + eps)
            else:
                dist = kappa * abs(x)
                g = (y + eps * sig) / (1.0 + eps)
            if abs(g) < 1e-10:
                continue
            ratio = (norm - dist) / (norm * g * g)
            if ratio < best:
                best = ratio
                best_data = (j, theta, x, y, norm, dist, g, ratio)
    return best, best_data


if __name__ == "__main__":
    best, data = sample()
    print(f"best sampled ratio: {best:.12f}")
    print("attained near:", data)
