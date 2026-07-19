"""Exhaustively verify the obstruction for 2 <= n <= 4.

The proof in main.tex is uniform in n.  This script independently enumerates
S_{2n} for the first three cases, identifies the full interval [id, gamma],
and checks that its distance from alpha is exactly n.
"""

from itertools import permutations


def compose(sigma, tau):
    """Return sigma o tau for permutations stored as image tuples."""
    return tuple(sigma[tau[i]] for i in range(len(sigma)))


def inverse(sigma):
    result = [0] * len(sigma)
    for i, value in enumerate(sigma):
        result[value] = i
    return tuple(result)


def cycle_count(sigma):
    seen = set()
    count = 0
    for start in range(len(sigma)):
        if start in seen:
            continue
        count += 1
        point = start
        while point not in seen:
            seen.add(point)
            point = sigma[point]
    return count


def distance(sigma, tau):
    quotient = compose(inverse(sigma), tau)
    return len(sigma) - cycle_count(quotient)


def construction(n):
    size = 2 * n
    gamma = list(range(size))
    alpha = list(range(size))
    for i in range(n):
        gamma[i] = (i + 1) % n
        gamma[n + i] = n + (i + 1) % n
        partner = n + (-i % n)
        alpha[i] = partner
        alpha[partner] = i
    return tuple(alpha), tuple(gamma)


for n in range(2, 5):
    alpha, gamma = construction(n)
    identity = tuple(range(2 * n))
    excess = (
        distance(identity, alpha)
        + distance(alpha, gamma)
        - distance(identity, gamma)
    )
    interval = [
        pi
        for pi in permutations(range(2 * n))
        if distance(identity, pi) + distance(pi, gamma)
        == distance(identity, gamma)
    ]
    minimum = min(distance(alpha, pi) for pi in interval)
    assert excess == 2
    assert minimum == n
    print(f"n={n}: interval_size={len(interval)}, excess={excess}, min_distance={minimum}")
