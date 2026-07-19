"""Check the fixed numerical inequalities used in the packet.

The proof leaves only finite arithmetic for d in {3,4,5}.  This script works
with logarithms because the source value alpha(d)=d^{-10^11 log d} is tiny.
"""

import math


EPS = 0.2


def log_alpha(d: int) -> float:
    return -1e11 * (math.log(d) ** 2)


def max_log_poly_times_r(r: float) -> float:
    """Upper bound sup_{ell>=2} log(ell^2 r^ell), for 0<r<1."""
    assert 0 < r < 1
    critical = max(2, int(math.ceil(-2 / math.log(r))) + 5)
    return max(2 * math.log(ell) + ell * math.log(r) for ell in range(2, critical + 1))


def main() -> None:
    for d in (3, 4, 5):
        D = d - 1
        beta = ((D - EPS) ** 3) / D
        tau = (math.sqrt(D) + math.sqrt(beta)) / 2
        eta = tau + D / tau - 2 * math.sqrt(D)
        r = tau * tau / beta

        la = log_alpha(d)
        logL = math.log(24) - la

        # Negative term dominated by half of the positive term in the
        # nonbacktracking lower bound. This is a conservative log upper bound.
        log_neg_over_pos_at_ell2 = (
            0.5 * math.log(3)
            + 2.5 * math.log(d)
            - 1.5 * math.log(d - 2)
            + 0.5 * math.log(D)
            + 2 * la
            - 1.5 * math.log(24)
            + math.log(D / beta)
        )

        # If the lower and upper spectral estimates were compatible, this log
        # ratio would be nonnegative for some ell. It is safely negative.
        log_C_upper = 2 * math.log(4 * tau / (tau - 1))
        log_lower_const = 3 * logL + math.log(d - 2) - math.log(64) - 3 * math.log(d)
        worst_log_upper_over_lower = (
            log_C_upper - log_lower_const + max_log_poly_times_r(r)
        )

        print(f"d={d}")
        print(f"  beta={beta:.12g}, tau={tau:.12g}, eta={eta:.12g}, tau^2/beta={r:.12g}")
        print(f"  beta>D: {beta > D}")
        print(f"  log(negative/positive) upper bound at ell=2: {log_neg_over_pos_at_ell2:.3f}")
        print(f"  log(worst upper/lower contradiction ratio): {worst_log_upper_over_lower:.3f}")
        assert beta > D
        assert eta > 0
        assert r < 1
        assert log_neg_over_pos_at_ell2 < math.log(0.5)
        assert worst_log_upper_over_lower < 0

    print("all fixed degree-3,4,5 inequalities verified")


if __name__ == "__main__":
    main()
