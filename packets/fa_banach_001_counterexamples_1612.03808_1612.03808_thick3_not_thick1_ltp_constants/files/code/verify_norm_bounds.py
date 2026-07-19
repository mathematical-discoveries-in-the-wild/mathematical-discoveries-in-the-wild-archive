from itertools import permutations

import numpy as np
from scipy.optimize import linprog


POINTS = ["0", "z", "a", "b"]


def dist(p: str, q: str) -> float:
    if p == q:
        return 0.0
    if {p, q} == {"0", "z"}:
        return 2.0
    return 1.0


EDGES = [(p, q) for p in POINTS for q in POINTS if p != q]


def atom(point: str) -> np.ndarray:
    vector = np.zeros(len(POINTS))
    vector[POINTS.index(point)] = 1.0
    return vector


def molecule(p: str, q: str) -> np.ndarray:
    return (atom(p) - atom(q)) / dist(p, q)


def free_norm(vector: np.ndarray) -> float:
    c = np.array([dist(p, q) for p, q in EDGES], dtype=float)
    a_eq = np.zeros((len(POINTS), len(EDGES)))
    for j, (p, q) in enumerate(EDGES):
        a_eq[POINTS.index(p), j] = 1.0
        a_eq[POINTS.index(q), j] = -1.0
    res = linprog(c, A_eq=a_eq, b_eq=vector, bounds=(0, None), method="highs")
    if not res.success:
        raise RuntimeError(res.message)
    return float(res.fun)


def main() -> None:
    mu = molecule("0", "z")
    rows = []
    max_min = 0.0
    for p, q in permutations(POINTS, 2):
        m = molecule(p, q)
        plus = free_norm(mu + m)
        minus = free_norm(-mu + m)
        best = min(plus, minus)
        max_min = max(max_min, best)
        rows.append((p, q, plus, minus, best))

    print("p q ||mu+m_pq|| ||-mu+m_pq|| min")
    for p, q, plus, minus, best in rows:
        print(f"{p:>1} {q:>1} {plus:8.5f} {minus:10.5f} {best:8.5f}")
    print(f"max_min={max_min:.5f}")
    assert abs(max_min - 1.5) < 1e-9


if __name__ == "__main__":
    main()
