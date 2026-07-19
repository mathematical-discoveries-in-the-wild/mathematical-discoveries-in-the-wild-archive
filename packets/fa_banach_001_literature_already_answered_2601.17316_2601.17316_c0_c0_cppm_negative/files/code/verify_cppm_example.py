from __future__ import annotations

from math import isclose


def partial_weight_sum(n: int) -> float:
    """Sum of 2^(1-j), j=2,...,n."""
    return sum(2.0 ** (1 - j) for j in range(2, n + 1))


def txn_norm(n: int) -> float:
    """Norm of T on x^(n)=e_1 + 1/2 sum_{j=2}^n e_j."""
    f_xn = 0.5 * partial_weight_sum(n)
    return max(abs(1.0 - f_xn), 0.5)


def main() -> None:
    print("Finite checks for the c0 CPPm counterexample mechanism")
    print("T x = x - f(x)e_1, K x = f(x)e_1, so T+K is the identity.")
    print()
    print("n    f(x^(n))        ||T x^(n)||_infty")
    for n in [2, 3, 4, 6, 8, 12, 20, 40]:
        f_xn = 0.5 * partial_weight_sum(n)
        print(f"{n:<4} {f_xn:<15.12f} {txn_norm(n):.12f}")

    assert all(txn_norm(n) >= 0.5 for n in range(2, 60))
    assert abs(txn_norm(60) - 0.5) < 1e-18

    # In finite truncations, K cancels the first-coordinate defect exactly.
    samples = [
        [1.0, 0.5, 0.5, 0.5],
        [-1.0, 0.3, -0.2, 0.1],
        [0.0, 1.0, -0.25, 0.125],
    ]
    for x in samples:
        weights = [0.0] + [2.0 ** (1 - j) for j in range(2, len(x) + 1)]
        f_x = sum(w * xj for w, xj in zip(weights, x))
        tx = x.copy()
        tx[0] -= f_x
        kx = [0.0 for _ in x]
        kx[0] = f_x
        t_plus_k = [a + b for a, b in zip(tx, kx)]
        assert all(isclose(a, b, rel_tol=0.0, abs_tol=1e-12) for a, b in zip(t_plus_k, x))

    print()
    print("The sequence ||T x^(n)|| decreases to 1/2, while T+K is exactly I in each finite check.")
    print("The non-attainment step is analytic: equality would force |x_j|=1/2 for all j>=2, not x in c0.")


if __name__ == "__main__":
    main()
