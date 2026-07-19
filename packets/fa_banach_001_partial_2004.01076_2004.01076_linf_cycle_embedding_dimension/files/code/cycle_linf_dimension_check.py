"""Finite checks for the cyclic metric ell_infty dimension packet.

This script is a sanity check, not a proof dependency.  It verifies the
landmark construction for small cycles and brute-forces integer-valued
1-Lipschitz coordinates to confirm the per-coordinate diameter-pair counts.
"""

from itertools import product


def d_cycle(m, i, j):
    k = abs(i - j) % m
    return min(k, m - k)


def landmark_embedding_ok(m):
    p = (m + 1) // 2
    landmarks = list(range(p))
    for i in range(m):
        for j in range(i + 1, m):
            lhs = max(abs(d_cycle(m, i, a) - d_cycle(m, j, a)) for a in landmarks)
            if lhs != d_cycle(m, i, j):
                return False, (i, j, lhs, d_cycle(m, i, j))
    return True, None


def diameter_pairs(m):
    q = m // 2
    seen = set()
    pairs = []
    for i in range(m):
        for j in ((i + q) % m,):
            pair = tuple(sorted((i, j)))
            if pair not in seen:
                seen.add(pair)
                pairs.append(pair)
    return pairs


def coordinate_witness_count(m, values):
    q = m // 2
    count = 0
    for i, j in diameter_pairs(m):
        if abs(values[i] - values[j]) == q:
            count += 1
    return count


def brute_coordinate_bound(m):
    # Integer-valued 1-Lipschitz functions with f(0)=0 and range in [-q,q].
    # This is enough for a finite sanity check of the extremal patterns.
    q = m // 2
    best = 0
    best_values = None
    for tail in product(range(-q, q + 1), repeat=m - 1):
        values = (0,) + tail
        ok = True
        for i in range(m):
            if abs(values[(i + 1) % m] - values[i]) > 1:
                ok = False
                break
        if not ok:
            continue
        count = coordinate_witness_count(m, values)
        if count > best:
            best = count
            best_values = values
    return best, best_values


def main():
    for m in range(2, 31):
        ok, detail = landmark_embedding_ok(m)
        if not ok:
            raise AssertionError((m, detail))
        print(f"S_{m}: landmark construction ok in ceil(m/2) coordinates")

    # Exhaustive enumeration grows as (2q+1)^(m-1), so keep it small.
    for m in range(2, 10):
        best, values = brute_coordinate_bound(m)
        expected = 1 if m % 2 == 0 else 2
        if m == 2:
            expected = 1
        assert best <= expected, (m, best, values)
        print(f"S_{m}: brute coordinate bound ok; max diameter pairs per coordinate = {best}; example={values}")


if __name__ == "__main__":
    main()
