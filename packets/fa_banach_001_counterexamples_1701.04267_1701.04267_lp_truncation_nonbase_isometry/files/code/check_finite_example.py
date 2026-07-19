from itertools import combinations


POINTS = ("a", "b", "c")
DIST = {
    ("a", "a"): 0.0,
    ("b", "b"): 0.0,
    ("c", "c"): 0.0,
    ("a", "b"): 2.0,
    ("b", "a"): 2.0,
    ("a", "c"): 2.5,
    ("c", "a"): 2.5,
    ("b", "c"): 3.0,
    ("c", "b"): 3.0,
}
TAU = {"a": "b", "b": "a", "c": "c"}


def subsets(points):
    pts = list(points)
    for r in range(len(pts) + 1):
        for combo in combinations(pts, r):
            yield set(combo)


def mass(p, subset):
    return sum(p[x] for x in subset)


def tv(p, q):
    return max(abs(mass(p, subset) - mass(q, subset)) for subset in subsets(POINTS))


def push(p):
    out = {x: 0.0 for x in POINTS}
    for x, px in p.items():
        out[TAU[x]] += px
    return out


def grid(denominator):
    for i in range(denominator + 1):
        for j in range(denominator + 1 - i):
            k = denominator - i - j
            yield {
                "a": i / denominator,
                "b": j / denominator,
                "c": k / denominator,
            }


def main():
    for x in POINTS:
        for y in POINTS:
            for z in POINTS:
                assert DIST[(x, z)] <= DIST[(x, y)] + DIST[(y, z)]

    assert DIST[("a", "c")] != DIST[(TAU["a"], TAU["c"])]

    for p in grid(8):
        for q in grid(8):
            assert abs(tv(p, q) - tv(push(p), push(q))) < 1e-12

    print("metric ok")
    print("tau is not a base-space isometry")
    print("tau push-forward preserves total variation on denominator-8 grid")
    print("because all nonzero distances exceed 1, Levy-Prokhorov = total variation")


if __name__ == "__main__":
    main()
