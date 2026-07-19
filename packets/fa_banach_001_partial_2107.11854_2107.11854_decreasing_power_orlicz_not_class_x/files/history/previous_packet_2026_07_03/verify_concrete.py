"""Numerical sanity check for the decreasing-power Orlicz packet.

This checks the concrete parameters used in the packet:
p=1, q=2, epsilon=1/2, d=1/4, a=1/2, b=20.
It is not part of the proof; it only guards against sign mistakes.
"""

from math import isclose


p = 1.0
q = 2.0
eps = 0.5
d = 0.25
a = 0.5
b = 20.0


def M(x: float) -> float:
    if x <= 1.0:
        return x ** (q + 1.0) / (q + 1.0)
    return 1.0 / (q + 1.0) + (x ** (p + 1.0) - 1.0) / (p + 1.0)


low_ratio = (M(eps * a) - M(eps * d)) / (M(a) - M(d))
high_ratio = (M(eps * b) - M(eps * a)) / (M(b) - M(a))

lower_theta = (M(b) - M(a)) / (M(a) - M(d))
upper_theta = (M(eps * b) - M(eps * a)) / (M(eps * a) - M(eps * d))
theta = 0.5 * (lower_theta + upper_theta)

af = M(b) + theta * M(d)
ag = (1.0 + theta) * M(a)
B = 0.5 * (1.0 / af + 1.0 / ag)
C = theta * B

prefix_high_f = B * M(b) + C * M(d)
prefix_high_g = (B + C) * M(a)
prefix_low_f = B * M(eps * b) + C * M(eps * d)
prefix_low_g = (B + C) * M(eps * a)
T = (1.0 - prefix_low_f) / M(eps * d)
global_low_f = prefix_low_f + T * M(eps * d)
global_low_g = prefix_low_g + T * M(eps * d)

print(f"low ratio  = {low_ratio:.12f}")
print(f"high ratio = {high_ratio:.12f}")
print(f"theta interval = ({lower_theta:.12f}, {upper_theta:.12f})")
print(f"theta = {theta:.12f}")
print(f"B = {B:.12f}, C = {C:.12f}, T = {T:.12f}")
print(f"prefix high scale: f={prefix_high_f:.12f}, g={prefix_high_g:.12f}")
print(f"prefix low scale:  f={prefix_low_f:.12f}, g={prefix_low_g:.12f}")
print(f"global low scale:  f={global_low_f:.12f}, g={global_low_g:.12f}")

assert low_ratio < high_ratio
assert lower_theta < theta < upper_theta
assert prefix_high_f < 1.0 < prefix_high_g
assert prefix_low_f > prefix_low_g
assert T > 0
assert isclose(global_low_f, 1.0, rel_tol=0.0, abs_tol=1e-12)
assert global_low_g < 1.0
