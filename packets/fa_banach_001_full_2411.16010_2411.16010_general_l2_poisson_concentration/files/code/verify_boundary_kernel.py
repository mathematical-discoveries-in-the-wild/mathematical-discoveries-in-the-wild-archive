"""Independent numerical checks for the boundary-kernel sharpness family."""

from __future__ import annotations

import mpmath as mp


mp.mp.dps = 40


def angular_mean(r: mp.mpf) -> mp.mpf:
    integrand = lambda theta: (
        (1 + r * mp.cos(theta)) ** 2
        / (1 + 2 * r * mp.cos(theta) + r**2)
    )
    return mp.quad(integrand, [0, 2 * mp.pi]) / (2 * mp.pi)


def transformed_mass(rho: mp.mpf, s: mp.mpf) -> mp.mpf:
    radius_sq = s / (s + mp.pi)
    radius = mp.sqrt(radius_sq)

    def angular_integral(r: mp.mpf) -> mp.mpf:
        def density(theta: mp.mpf) -> mp.mpf:
            w = r * mp.e ** (1j * theta)
            x = mp.re(w)
            numerator = (1 - r**2) * (1 + rho**2 + 2 * rho * x) ** 2
            denominator = (1 + rho**2) * abs(1 + rho * w) ** 2
            # D_rho dmu = D_rho * r dr dtheta / (1-r^2)^2.
            return numerator / denominator * r / (1 - r**2) ** 2

        return mp.quad(density, [0, 2 * mp.pi])

    return mp.quad(angular_integral, [0, radius])


def limiting_mass(s: mp.mpf) -> mp.mpf:
    return mp.pi * (mp.log(1 + s / mp.pi) + s / (s + mp.pi))


def main() -> None:
    for r in (mp.mpf("0"), mp.mpf("0.2"), mp.mpf("0.6"), mp.mpf("0.9")):
        numerical = angular_mean(r)
        exact = 1 - r**2 / 2
        print(
            "angular",
            mp.nstr(r, 5),
            mp.nstr(numerical, 18),
            mp.nstr(exact, 18),
            mp.nstr(abs(numerical - exact), 5),
        )

    for s in (mp.mpf("0.01"), mp.mpf("0.5"), mp.mpf("3"), mp.mpf("20")):
        target = limiting_mass(s)
        analytic = mp.pi * mp.log(1 + s / mp.pi)
        print(
            "s",
            mp.nstr(s, 5),
            "limit",
            mp.nstr(target, 18),
            "analytic",
            mp.nstr(analytic, 18),
            "ratio",
            mp.nstr(target / analytic, 18),
        )
        for rho in (mp.mpf("0.9"), mp.mpf("0.99"), mp.mpf("0.999")):
            mass = transformed_mass(rho, s)
            print(
                " rho",
                mp.nstr(rho, 5),
                "mass",
                mp.nstr(mass, 18),
                "error",
                mp.nstr(abs(mass - target), 8),
            )


if __name__ == "__main__":
    main()
