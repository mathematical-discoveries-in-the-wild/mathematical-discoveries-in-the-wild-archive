from fractions import Fraction
from itertools import combinations
from math import isqrt


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def rank(matrix):
    a = [row[:] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if a[i][c] != 0), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        pv = a[r][c]
        a[r] = [x / pv for x in a[r]]
        for i in range(rows):
            if i != r and a[i][c] != 0:
                factor = a[i][c]
                a[i] = [x - factor * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def is_square_fraction(x):
    return (
        x >= 0
        and isqrt(x.numerator) ** 2 == x.numerator
        and isqrt(x.denominator) ** 2 == x.denominator
    )


def sqrt_fraction(x):
    assert is_square_fraction(x)
    return Fraction(isqrt(x.numerator), isqrt(x.denominator))


def kll_radicand(n, d):
    n = Fraction(n)
    d = Fraction(d)
    return (d - 1) * (n / d) * (1 - n / d)


def kll_value_is(target, n, d):
    radicand = kll_radicand(n, d)
    return is_square_fraction(radicand) and Fraction(n, d) + sqrt_fraction(radicand) == target


def e7_vector(i, j):
    out = [-Fraction(1, 4) for _ in range(8)]
    out[i - 1] += 1
    out[j - 1] += 1
    assert sum(out) == 0
    return out


def verify_e7_interval():
    all_edges = list(combinations(range(1, 9), 2))
    basis_edges = [(1, j) for j in range(2, 9)]
    remaining_edges = [edge for edge in all_edges if edge not in basis_edges]

    for d in range(7, 29):
        edges = basis_edges + remaining_edges[: d - 7]
        vectors = [e7_vector(i, j) for i, j in edges]
        norms = {dot(x, x) for x in vectors}
        off_abs = {
            abs(dot(x, y))
            for idx, x in enumerate(vectors)
            for y in vectors[idx + 1 :]
        }
        assert len(edges) == d
        assert rank(vectors) == 7
        assert norms == {Fraction(3, 2)}
        assert off_abs == {Fraction(1, 2)}

    assert kll_value_is(Fraction(7, 3), 7, 15)
    print("E7 spanning interval verified: Pi(7,d) is KLL-exact for 7 <= d <= 28")
    print("E7 special case: d=15 gives KLL value 7/3")


def verify_kll_seven_thirds_candidates(search_limit=1000):
    target = Fraction(7, 3)
    candidates = []
    for n in range(1, search_limit + 1):
        den = 9 * n - 49
        if den == 0:
            continue
        num = n * (9 * n - 33)
        if num % den == 0:
            d = num // den
            if d >= n and kll_value_is(target, n, d):
                candidates.append((n, d))

    assert candidates == [(7, 15), (49, 51)]
    print("KLL-bound equation B(n,d)=7/3 has integer candidates:", candidates)


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True


def legendre_symbol(a, p):
    a %= p
    if a == 0:
        return 0
    value = pow(a, (p - 1) // 2, p)
    return 1 if value == 1 else -1


def paley_conference_prime(p):
    assert is_prime(p) and p % 4 == 1
    size = p + 1
    c = [[0 for _ in range(size)] for _ in range(size)]

    # Index 0 represents infinity; indices 1..p represent field elements 0..p-1.
    for idx in range(1, size):
        c[0][idx] = 1
        c[idx][0] = 1
    for x in range(p):
        for y in range(p):
            if x != y:
                c[x + 1][y + 1] = legendre_symbol(x - y, p)
    return c


def matmul(a, b):
    rows = len(a)
    cols = len(b[0])
    inner = len(b)
    return [
        [sum(a[i][k] * b[k][j] for k in range(inner)) for j in range(cols)]
        for i in range(rows)
    ]


class Quadratic:
    """Exact arithmetic in Q(sqrt(q)) for one fixed q."""

    q = 0

    def __init__(self, a=0, b=0):
        self.a = Fraction(a)
        self.b = Fraction(b)

    def __add__(self, other):
        other = as_quadratic(other)
        return Quadratic(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        other = as_quadratic(other)
        return Quadratic(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        other = as_quadratic(other)
        return Quadratic(
            self.a * other.a + Quadratic.q * self.b * other.b,
            self.a * other.b + self.b * other.a,
        )

    def __truediv__(self, other):
        other = as_quadratic(other)
        den = other.a * other.a - Quadratic.q * other.b * other.b
        return self * Quadratic(other.a / den, -other.b / den)

    def __eq__(self, other):
        other = as_quadratic(other)
        return self.a == other.a and self.b == other.b


def as_quadratic(value):
    if isinstance(value, Quadratic):
        return value
    return Quadratic(value, 0)


def rank_quadratic(matrix):
    a = [[as_quadratic(x) for x in row] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    zero = Quadratic(0, 0)
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if a[i][c] != zero), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        pv = a[r][c]
        a[r] = [x / pv for x in a[r]]
        for i in range(rows):
            if i != r and a[i][c] != zero:
                factor = a[i][c]
                a[i] = [x - factor * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def verify_paley_prime_cases(limit=100):
    checked = []
    for p in range(5, limit + 1):
        if not is_prime(p) or p % 4 != 1:
            continue
        c = paley_conference_prime(p)
        size = p + 1
        assert all(c[i][i] == 0 for i in range(size))
        assert all(c[i][j] == c[j][i] for i in range(size) for j in range(size))
        assert all(abs(c[i][j]) == 1 for i in range(size) for j in range(size) if i != j)

        c2 = matmul(c, c)
        for i in range(size):
            for j in range(size):
                assert c2[i][j] == (p if i == j else 0)

        checked.append((p, (p + 1) // 2, p + 1))

    assert checked
    assert (97, 49, 98) in checked
    assert kll_value_is(Fraction(7, 3), 49, 51)
    print("Paley prime conference matrices verified up to q <=", limit)
    for q, n, d in checked[:8]:
        print(f"  q={q}: n={n}, d={d}, endpoint KLL value=(1+sqrt({q}))/2")
    if len(checked) > 8:
        print(f"  ... {len(checked) - 8} additional prime cases checked")


def verify_paley_q97_spanning_certificate():
    q = 97
    Quadratic.q = q
    c = paley_conference_prime(q)
    selected = list(range(51))

    # A scalar multiple of the Gram matrix of the positive eigenspace is C+sqrt(q)I.
    gram = [
        [
            Quadratic(c[i][j], 1 if i == j else 0)
            for j in selected
        ]
        for i in selected
    ]
    assert rank_quadratic(gram) == 49
    print("Paley q=97 certificate: the first 51 lines have Gram rank 49")
    print("  therefore they span R^49 and certify Pi(49,51)=7/3")


def verify_thirds_ladder_examples():
    examples = {
        Fraction(4, 3): [(2, 3)],
        Fraction(5, 3): [(5, 6)],
        Fraction(2, 1): [(5, 10)],
        Fraction(7, 3): [(7, 15), (49, 51)],
        Fraction(3, 1): [(13, 26), (15, 25), (21, 28), (27, 33), (45, 50)],
    }
    for value, pairs in examples.items():
        for n, d in pairs:
            assert kll_value_is(value, n, d), (value, n, d)
    print("sample spanning-thirds KLL values verified")


if __name__ == "__main__":
    verify_e7_interval()
    verify_kll_seven_thirds_candidates()
    verify_paley_prime_cases()
    verify_paley_q97_spanning_certificate()
    verify_thirds_ladder_examples()
