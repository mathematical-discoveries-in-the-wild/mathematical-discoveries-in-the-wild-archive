import math

import numpy as np
from scipy.linalg import expm


sqrt3 = math.sqrt(3.0)
K = np.array(
    [
        [0.0, -1.0 / sqrt3, 1.0 / sqrt3],
        [1.0 / sqrt3, 0.0, -1.0 / sqrt3],
        [-1.0 / sqrt3, 1.0 / sqrt3, 0.0],
    ]
)
P = np.ones((3, 3)) / 3.0
H = np.eye(3) - P
B = -np.eye(3) + 4.0 * K


def resolvent_block(lam: float) -> np.ndarray:
    r = 1.0 + lam
    return (1.0 / r) * P + (r / (r * r + 16.0)) * H + (4.0 / (r * r + 16.0)) * K


def main() -> None:
    print("K^2 + H norm:", np.linalg.norm(K @ K + H))
    for lam in np.linspace(0.001, 1.0, 11):
        r_formula = resolvent_block(float(lam))
        r_direct = np.linalg.inv(lam * np.eye(3) - B)
        print(
            f"lambda={lam:.3f}",
            "min_entry=", float(r_formula.min()),
            "formula_error=", float(np.linalg.norm(r_formula - r_direct)),
        )
        assert r_formula.min() > 0
        assert np.linalg.norm(r_formula - r_direct) < 1e-10

    e1 = np.array([1.0, 0.0, 0.0])
    for n in range(6):
        t = (2 * n + 1) * math.pi / 4.0
        val = (expm(t * B) @ e1)[0]
        expected = -math.exp(-t) / 3.0
        print(f"n={n}", "t=", t, "first_coordinate=", val, "expected=", expected)
        assert val < 0
        assert abs(val - expected) < 1e-10

    print("verification passed")


if __name__ == "__main__":
    main()

