"""Finite check for the parity-envelope packet.

The proof uses the four vertices of {-1,1}^3 with parity -1.  Their barycenter
is the origin and the parity average is -1, proving h(0) = -1 for the convex
envelope of epsilon_1 epsilon_2 epsilon_3.
"""

from itertools import product


def parity(vertex):
    value = 1
    for coordinate in vertex:
        value *= coordinate
    return value


vertices = list(product([-1, 1], repeat=3))
negative = [v for v in vertices if parity(v) == -1]

barycenter = tuple(sum(v[i] for v in negative) / len(negative) for i in range(3))
average_parity = sum(parity(v) for v in negative) / len(negative)

print("negative parity vertices:", negative)
print("barycenter:", barycenter)
print("average parity:", average_parity)

assert barycenter == (0.0, 0.0, 0.0)
assert average_parity == -1.0
