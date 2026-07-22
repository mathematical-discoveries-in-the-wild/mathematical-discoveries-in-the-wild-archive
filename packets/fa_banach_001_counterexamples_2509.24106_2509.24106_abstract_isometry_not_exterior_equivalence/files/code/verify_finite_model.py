#!/usr/bin/env python3
"""Exact checks for the C_2 acting on C^3 counterexample."""

from itertools import product


# A permutation is stored as its action on {0,1,2}; composition is left after right.
IDENTITY = (0, 1, 2)
R = (1, 0, 2)  # (12)
Q = (0, 2, 1)  # (23)
T = (1, 2, 0)  # (123)


def compose(left, right):
    return tuple(left[right[i]] for i in range(3))


def inverse(perm):
    result = [None] * 3
    for i, image in enumerate(perm):
        result[image] = i
    return tuple(result)


def gamma(perm, vector):
    """The coordinate automorphism gamma^perm: e_i maps to e_perm(i)."""
    result = [0] * 3
    for i, value in enumerate(vector):
        result[perm[i]] = value
    return tuple(result)


def basis_a(i):
    return tuple(1 if j == i else 0 for j in range(3))


def pointwise(left, right):
    return tuple(a * b for a, b in zip(left, right))


def action(which, group_element, vector):
    if group_element == 0:
        return vector
    return gamma(R if which == "alpha" else Q, vector)


def crossed_basis_product(which, first, second):
    """Product of delta_g e_i and delta_h e_j, returned as (gh, A-vector)."""
    g, i = first
    h, j = second
    coefficient = pointwise(basis_a(i), action(which, g, basis_a(j)))
    return (g ^ h, coefficient)


def phi_basis(term):
    g, i = term
    return (g, T[i])


def phi_product(product_value):
    group_element, coefficient = product_value
    return (group_element, gamma(T, coefficient))


def rho_diagonal(vector):
    """rho=pi o phi^{-1}, with pi the faithful diagonal representation."""
    return gamma(inverse(T), vector)


def regular_coefficient_diagonal(which, coefficient_rep, group_x, vector):
    # Every element of C_2 is its own inverse.
    transformed = action(which, group_x, vector)
    return coefficient_rep(transformed)


def integrated_matrix(which, coefficient_rep, group_g, vector):
    """Matrix of pi(vector) u_g on l^p(C_2 x {0,1,2}); integer entries."""
    matrix = [[0 for _ in range(6)] for _ in range(6)]
    for x, coordinate in product(range(2), range(3)):
        diagonal = regular_coefficient_diagonal(
            which, coefficient_rep, x, vector
        )[coordinate]
        source_x = g_inverse_times_x(group_g, x)
        matrix[3 * x + coordinate][3 * source_x + coordinate] = diagonal
    return tuple(tuple(row) for row in matrix)


def g_inverse_times_x(g, x):
    return g ^ x


def main():
    assert compose(compose(T, R), inverse(T)) == Q
    assert R != Q
    assert gamma(R, basis_a(0)) != gamma(Q, basis_a(0))

    algebra_basis = list(product(range(2), range(3)))
    for first, second in product(algebra_basis, repeat=2):
        lhs = phi_product(crossed_basis_product("alpha", first, second))
        rhs = crossed_basis_product("beta", phi_basis(first), phi_basis(second))
        assert lhs == rhs, (first, second, lhs, rhs)

    pi_diagonal = lambda vector: vector
    for g, i in algebra_basis:
        alpha_matrix = integrated_matrix("alpha", pi_diagonal, g, basis_a(i))
        beta_matrix = integrated_matrix(
            "beta", rho_diagonal, g, gamma(T, basis_a(i))
        )
        assert alpha_matrix == beta_matrix, (g, i)

    print("PASS: q = t r t^{-1} and alpha != beta")
    print("PASS: Phi preserves all 36 algebraic basis products")
    print("PASS: all 6 regular integrated basis matrices intertwine exactly")


if __name__ == "__main__":
    main()
