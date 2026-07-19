"""Small checks for the uniformly discrete metric used in the packet.

The metric is d(v_k, v_n) = 1 + 1/max(k, n) for k != n.
For q1 < q2 < q3 < q4, the crossing matching
{v_q1 v_q3, v_q2 v_q4} is strictly lighter than
{v_q1 v_q2, v_q3 v_q4}.
"""

from itertools import combinations


def d(i: int, j: int) -> float:
    if i == j:
        return 0.0
    return 1.0 + 1.0 / max(i, j)


def check_metric(n: int = 40) -> bool:
    for i, j, k in combinations(range(1, n + 1), 3):
        triples = [(i, j, k), (i, k, j), (j, k, i)]
        for a, b, c in triples:
            if d(a, b) > d(a, c) + d(c, b) + 1e-12:
                raise AssertionError((a, b, c, d(a, b), d(a, c) + d(c, b)))
    return True


def check_crossing(n: int = 40) -> bool:
    for q1, q2, q3, q4 in combinations(range(1, n + 1), 4):
        original = d(q1, q2) + d(q3, q4)
        crossed = d(q1, q3) + d(q2, q4)
        if not crossed < original:
            raise AssertionError((q1, q2, q3, q4, crossed, original))
    return True


if __name__ == "__main__":
    print("metric", check_metric())
    print("crossing_improvement", check_crossing())
