"""Numerical smoke check for the E_{1,beta}(it) asymptotic.

This script is not a proof.  It evaluates the exact incomplete-gamma
representation at high precision and checks the two asymptotic signatures
used in the proof packet.
"""

from __future__ import annotations

import mpmath as mp


mp.mp.dps = 70


def e_one_beta(beta: mp.mpf, t: int) -> mp.mpc:
    """Exact E_{1,beta}(i t) through the lower incomplete gamma."""
    z = mp.j * t
    return (
        1 / mp.gamma(beta)
        + z ** (1 - beta)
        * mp.exp(z)
        * mp.gammainc(beta, 0, z)
        / mp.gamma(beta)
    )


def main() -> None:
    for beta_text in ("0.2", "0.5", "0.8"):
        beta = mp.mpf(beta_text)
        coefficient = (1 - beta) / mp.gamma(beta)
        for t in (30, 100, 300):
            z = mp.j * t
            exact = e_one_beta(beta, t)
            leading = z ** (1 - beta) * mp.exp(z)
            modulus_ratio = abs(exact) / mp.mpf(t) ** (1 - beta)
            scaled_error = t * abs(exact - leading)

            # Loose thresholds deliberately test only the asymptotic regime.
            assert abs(modulus_ratio - 1) < mp.mpf("0.01")
            if t == 300:
                assert abs(scaled_error - coefficient) < mp.mpf("0.001")

            print(
                f"beta={beta_text} t={t:3d} "
                f"modulus_ratio={mp.nstr(modulus_ratio, 16)} "
                f"t_times_error={mp.nstr(scaled_error, 16)}"
            )

    print("all numerical smoke checks passed")


if __name__ == "__main__":
    main()
