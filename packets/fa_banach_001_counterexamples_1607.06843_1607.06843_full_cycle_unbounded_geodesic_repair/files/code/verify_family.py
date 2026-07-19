"""Verify the unbounded-distance genus-one counterexample family.

This script checks exact cycle formulas and the K_{m,m} crossing pattern for
m <= 50.  It also exhaustively enumerates all geodesic permutations for the
small cases m=1,2 and computes their true nearest Cayley distances.
"""

from itertools import permutations


def compose(left, right):
    return tuple(left[right[i]] for i in range(len(left)))


def inverse(pi):
    out = [0] * len(pi)
    for i, image in enumerate(pi):
        out[image] = i
    return tuple(out)


def cycle_count(pi):
    seen = set()
    total = 0
    for start in range(len(pi)):
        if start in seen:
            continue
        total += 1
        point = start
        while point not in seen:
            seen.add(point)
            point = pi[point]
    return total


def cayley_distance(left, right):
    return len(left) - cycle_count(compose(inverse(left), right))


def family(m):
    size = 4 * m
    alpha = list(range(size))
    a_pairs = []
    b_pairs = []
    for i in range(1, m + 1):
        x, y = i - 1, 3 * m - i
        alpha[x], alpha[y] = y, x
        a_pairs.append((x, y))
    for j in range(1, m + 1):
        x, y = m + j - 1, 4 * m - j
        alpha[x], alpha[y] = y, x
        b_pairs.append((x, y))
    gamma = tuple(range(1, size)) + (0,)
    return tuple(alpha), gamma, a_pairs, b_pairs


def crosses(first, second):
    a, c = sorted(first)
    b, d = sorted(second)
    return (a < b < c < d) or (b < a < d < c)


def defect(alpha, gamma):
    size = len(alpha)
    excess = (
        cayley_distance(tuple(range(size)), alpha)
        + cayley_distance(alpha, gamma)
        - cayley_distance(tuple(range(size)), gamma)
    )
    assert excess % 2 == 0
    return excess // 2


def is_geodesic(pi, gamma):
    identity = tuple(range(len(pi)))
    return (
        cayley_distance(identity, pi) + cayley_distance(pi, gamma)
        == cayley_distance(identity, gamma)
    )


def check_symbolic_range():
    for m in range(1, 51):
        alpha, gamma, a_pairs, b_pairs = family(m)
        assert cycle_count(alpha) == 2 * m
        assert cycle_count(compose(alpha, gamma)) == 2 * m - 1
        assert defect(alpha, gamma) == 1
        assert all(crosses(a_pair, b_pair) for a_pair in a_pairs for b_pair in b_pairs)
        assert all(not crosses(a_pairs[i], a_pairs[j]) for i in range(m) for j in range(i))
        assert all(not crosses(b_pairs[i], b_pairs[j]) for i in range(m) for j in range(i))


def exhaustive_small_cases():
    answers = {}
    for m in (1, 2):
        alpha, gamma, _, _ = family(m)
        best = len(alpha)
        geodesic_count = 0
        for pi in permutations(range(len(alpha))):
            if not is_geodesic(pi, gamma):
                continue
            geodesic_count += 1
            best = min(best, cayley_distance(alpha, pi))
        answers[m] = (geodesic_count, best)
    assert answers == {1: (14, 1), 2: (1430, 2)}
    return answers


if __name__ == "__main__":
    check_symbolic_range()
    small = exhaustive_small_cases()
    print("exact formulas and crossing pattern verified for 1 <= m <= 50")
    for m, (count, distance) in small.items():
        print(f"m={m}: geodesic_count={count}, nearest_distance={distance}")

