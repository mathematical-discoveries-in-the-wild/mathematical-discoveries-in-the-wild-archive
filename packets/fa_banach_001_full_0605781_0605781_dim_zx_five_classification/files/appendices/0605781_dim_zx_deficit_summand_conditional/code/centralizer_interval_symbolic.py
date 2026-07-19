"""Verifier for the centralizer-coupling interval proof.

This script is not the proof.  It stress-tests the two coarse triangular
weight bounds used in the proof note and then checks the resulting
centralizer families far beyond the previous run limits.
"""

from __future__ import annotations


def triangular(k: int) -> int:
    return k * (k - 1) // 2


def triangular_weights(max_n: int) -> list[int]:
    w = [10**9] * (max_n + 1)
    w[0] = 0
    for k in range(2, max_n + 3):
        t = triangular(k)
        if t > max_n:
            break
        for n in range(t, max_n + 1):
            candidate = w[n - t] + k
            if candidate < w[n]:
                w[n] = candidate
    return w


def cap(kind: str, m: int) -> int:
    if kind == "R":
        return triangular(m)
    if kind == "C":
        return m * m
    if kind == "H":
        return m * (2 * m + 1)
    raise ValueError(kind)


def interval_max_prefix(w: list[int], offset: int, max_cap: int) -> list[int]:
    result = [0] * (max_cap + 1)
    best = w[offset]
    for ell in range(max_cap + 1):
        if w[offset + ell] > best:
            best = w[offset + ell]
        result[ell] = best
    return result


def main() -> None:
    p_limit = 500
    m_limit = 500
    k_limit = 500
    max_n = max(
        triangular(2 * m_limit + 1) + 4,
        (k_limit * k_limit) + m_limit * m_limit,
        14 + triangular(m_limit),
    )
    w = triangular_weights(max_n)

    lemma1_failures = []
    for p in range(3, p_limit + 1):
        bound = triangular(p) + 4
        worst = max(range(bound + 1), key=lambda n: w[n])
        if w[worst] > 2 * p + 2:
            lemma1_failures.append((p, worst, w[worst], 2 * p + 2))
            break

    lemma2_failures = []
    for m in range(1, m_limit + 1):
        bound = m * m
        worst = max(range(bound + 1), key=lambda n: w[n])
        if w[worst] > 4 * m:
            lemma2_failures.append((m, worst, w[worst], 4 * m))
            break

    family_failures = []
    max_r_cap = cap("R", m_limit)
    max_h_cap = cap("H", m_limit)
    u2_prefix = interval_max_prefix(w, 4, max_h_cap)
    g2_prefix = interval_max_prefix(w, 14, max_r_cap)

    checked = 0
    for label, prefix, e, d, kind in [
        ("U2 real", u2_prefix, 4, 3, "R"),
        ("U2 quaternionic", u2_prefix, 4, 4, "H"),
        ("G2 real", g2_prefix, 7, 7, "R"),
    ]:
        for m in range(1, m_limit + 1):
            checked += 1
            c = cap(kind, m)
            lhs = prefix[c]
            rhs = e + d * m
            if lhs > rhs:
                family_failures.append((label, m, lhs, rhs))
                break

    # The complex SU(k)/U(k) families are verified by the symbolic bounds
    # in the proof note:
    #   SU(k): w(k^2-1+ell) <= 4k-4+4m <= 2k+2km.
    #   U(k):  w(k^2+ell)   <= 2k+1+4m <= 2k+2km.
    complex_failures = []
    for k in range(3, k_limit + 1):
        for m in range(1, m_limit + 1):
            if 4 * k - 4 + 4 * m > 2 * k + 2 * k * m:
                complex_failures.append(("SU", k, m))
                break
            if 2 * k + 1 + 4 * m > 2 * k + 2 * k * m:
                complex_failures.append(("U", k, m))
                break
        if complex_failures:
            break

    print(f"Lemma 1 failures: {lemma1_failures}")
    print(f"Lemma 2 failures: {lemma2_failures}")
    print(f"Real/quaternionic centralizer families checked exactly: {checked}")
    print(f"Centralizer failures: {family_failures}")
    print(f"Complex symbolic inequality failures: {complex_failures}")


if __name__ == "__main__":
    main()
