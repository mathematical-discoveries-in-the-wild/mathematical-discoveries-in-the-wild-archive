from fractions import Fraction


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


one = [Fraction(1) for _ in range(8)]


def v(i, j):
    # Indices are 1-based.  The vector lies in the hyperplane sum x_i=0.
    out = [-Fraction(1, 4) for _ in range(8)]
    out[i - 1] += 1
    out[j - 1] += 1
    assert dot(out, one) == 0
    return out


edges = (
    [(1, j) for j in range(2, 9)]
    + [(2, j) for j in range(3, 9)]
    + [(3, 4), (3, 5)]
)
vectors = [v(i, j) for i, j in edges]

norms = {dot(x, x) for x in vectors}
off_diagonal_abs = {abs(dot(x, y)) for i, x in enumerate(vectors) for y in vectors[i + 1 :]}

assert len(vectors) == 15
assert rank(vectors) == 7
assert norms == {Fraction(3, 2)}
assert off_diagonal_abs == {Fraction(1, 2)}

n = Fraction(7)
d = Fraction(15)
bound = n / d + Fraction(28, 15)
assert bound == Fraction(7, 3)

print("selected lines:", len(vectors))
print("span rank:", rank(vectors))
print("norm squared:", next(iter(norms)))
print("absolute off-diagonal inner product:", next(iter(off_diagonal_abs)))
print("normalized absolute inner product:", Fraction(1, 2) / Fraction(3, 2))
print("KLL bound for (n,d)=(7,15):", bound)
