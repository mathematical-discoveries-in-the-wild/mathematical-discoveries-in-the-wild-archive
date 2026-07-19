from fractions import Fraction


def add_outer(matrix, x, f):
    for row in range(len(x)):
        for col in range(len(f)):
            matrix[row][col] += x[row] * f[col]


def assert_pair_is_norming(x, f):
    assert sum(abs(value) for value in x) == 1
    assert max(abs(value) for value in f) == 1
    assert sum(a * b for a, b in zip(x, f)) == 1


def base_pairs_n_ge_3(n, k):
    assert n >= 3
    assert 0 <= k <= n - 1
    beta = Fraction(n - k, 2 * n * (n - 2))
    alpha = 1 - (n - 1) * beta
    pairs = []

    for j in range(n):
        x = [-beta for _ in range(n)]
        f = [-Fraction(1) for _ in range(n)]
        x[j] = alpha
        f[j] = Fraction(1)
        pairs.append((x, f))

    for _ in range(k):
        x = [Fraction(1, n) for _ in range(n)]
        f = [Fraction(1) for _ in range(n)]
        pairs.append((x, f))

    return pairs


def seed_pairs_n_2(length):
    assert length in (2, 3)
    if length == 2:
        return [
            ([Fraction(1), Fraction(0)], [Fraction(1), Fraction(0)]),
            ([Fraction(0), Fraction(1)], [Fraction(0), Fraction(1)]),
        ]
    return [
        ([Fraction(1), Fraction(0)], [Fraction(1), Fraction(0)]),
        ([Fraction(1, 4), Fraction(3, 4)], [Fraction(1), Fraction(1)]),
        ([-Fraction(1, 4), Fraction(3, 4)], [-Fraction(1), Fraction(1)]),
    ]


def construct_pairs(n, N):
    assert N >= n >= 1
    if n == 1:
        return [([Fraction(1)], [Fraction(1)]) for _ in range(N)]

    if n == 2:
        if N % 2 == 0:
            pairs = []
            for _ in range(N // 2):
                pairs.extend(seed_pairs_n_2(2))
            return pairs
        pairs = seed_pairs_n_2(3)
        for _ in range((N - 3) // 2):
            pairs.extend(seed_pairs_n_2(2))
        return pairs

    q, r = divmod(N, n)
    pairs = []
    if r == 0:
        for _ in range(q):
            pairs.extend(base_pairs_n_ge_3(n, 0))
    else:
        for _ in range(q - 1):
            pairs.extend(base_pairs_n_ge_3(n, 0))
        pairs.extend(base_pairs_n_ge_3(n, r))
    return pairs


def frame_operator(n, pairs):
    matrix = [[Fraction(0) for _ in range(n)] for __ in range(n)]
    for x, f in pairs:
        assert_pair_is_norming(x, f)
        add_outer(matrix, x, f)
    return matrix


def target_operator(n, N):
    return [
        [Fraction(N, n) if row == col else Fraction(0) for col in range(n)]
        for row in range(n)
    ]


def main():
    checked = 0
    for n in range(1, 11):
        for N in range(n, 4 * n + 8):
            pairs = construct_pairs(n, N)
            assert len(pairs) == N
            assert frame_operator(n, pairs) == target_operator(n, N)
            checked += 1
    print(f"Checked {checked} exact cases: 1 <= n <= 10, n <= N <= 4n+7.")
    print("All normalization, pairing, and frame-operator checks passed.")


if __name__ == "__main__":
    main()
