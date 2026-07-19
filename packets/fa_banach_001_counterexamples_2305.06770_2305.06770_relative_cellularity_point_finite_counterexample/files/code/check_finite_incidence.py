"""Finite incidence sanity checks for the Psi-space counterexample.

This does not prove the infinite theorem.  It verifies the finite pattern used
in the construction: U_i = {i} union {p_{ij}: j != i} is point-finite, and a
linearly ordered countable subfamily can be thinned to pairwise disjoint basic
neighbourhoods by deleting the earlier intersection points.
"""

from itertools import combinations


def main() -> None:
    n = 8
    points = {("a", i) for i in range(n)}
    points.update({("p", min(i, j), max(i, j)) for i, j in combinations(range(n), 2)})

    U = {}
    for i in range(n):
        U[i] = {("a", i)}
        U[i].update({("p", min(i, j), max(i, j)) for j in range(n) if j != i})

    multiplicities = {x: sum(x in U[i] for i in range(n)) for x in points}
    assert max(multiplicities.values()) == 2
    assert all(("a", i) in U[i] for i in range(n))

    # Delete p_{ij} from the larger-indexed neighbourhood.  This is the finite
    # analogue of the countable cellular lower-bound family.
    V = {}
    for i in range(n):
        delete = {("p", j, i) for j in range(i)}
        V[i] = U[i] - delete

    for i, j in combinations(range(n), 2):
        assert V[i].isdisjoint(V[j])

    print(f"checked {n} indices, {len(points)} points, max multiplicity 2")


if __name__ == "__main__":
    main()
