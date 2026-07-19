import math


def shear_norm(a: float) -> float:
    return (math.sqrt(a * a + 4.0) + abs(a)) / 2.0


def main() -> None:
    for eps in [1e-1, 1e-2, 1e-3, 1e-4]:
        m = 1.0 + eps
        eta = m - 1.0 / m
        norm = shear_norm(eta)
        lower_ratio = eta / (2.0 * eps)
        print(f"eps={eps:g}")
        print(f"  eta={eta:.16g}")
        print(f"  shear_norm(eta)={norm:.16g}, M={m:.16g}, diff={norm-m:.3g}")
        print(f"  K_eps lower ratio={lower_ratio:.16g}")
        assert abs(norm - m) < 1e-12

    upper = math.exp(math.sqrt(2.0)) / math.sqrt(2.0)
    print(f"optimized dyadic upper constant={upper:.16g}")
    assert upper < 3.0


if __name__ == "__main__":
    main()
