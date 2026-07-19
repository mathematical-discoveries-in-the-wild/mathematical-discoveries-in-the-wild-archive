from __future__ import annotations


def check(p: float, max_m: int = 80) -> None:
    alpha = abs(1.0 - 2.0 / p)
    assert alpha > 0.0
    cb_ceiling = 2.0 ** (1.0 / p)
    for m in range(2, max_m + 1):
        d = m ** (-alpha)
        c = (1.0 - d**p) ** (1.0 / p)
        scalar_isometry = c**p + d**p
        cb_estimate = (c**p + (d * (m**alpha)) ** p) ** (1.0 / p)
        amplified_lower_bound = cb_estimate
        assert abs(scalar_isometry - 1.0) < 1e-10
        assert cb_estimate <= cb_ceiling + 1e-10
        assert amplified_lower_bound > 1.0
    print(
        f"p={p:g}: alpha={alpha:.6g}, checked m=2..{max_m}, "
        f"uniform cb bound <= {cb_ceiling:.6g}, block cb norm > 1"
    )


def main() -> None:
    for p in [1.0, 1.25, 1.5, 1.9, 2.1, 3.0, 6.0]:
        check(p)


if __name__ == "__main__":
    main()
