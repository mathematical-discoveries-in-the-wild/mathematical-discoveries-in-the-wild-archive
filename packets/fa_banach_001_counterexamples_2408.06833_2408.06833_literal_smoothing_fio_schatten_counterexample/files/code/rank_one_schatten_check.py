import numpy as np


def main() -> None:
    u = np.array([1.0, 2.0, -1.0, 0.5])
    v = np.array([2.0, -1.0, 0.0, 3.0])
    matrix = np.outer(u, v)
    singular_values = np.linalg.svd(matrix, compute_uv=False)
    expected = np.linalg.norm(u) * np.linalg.norm(v)
    print("singular values:", np.array2string(singular_values, precision=12))
    print("expected nonzero singular value:", expected)
    for r in [0.5, 1.0, 1.7, 2.0, 3.3]:
        schatten_sum = float(np.sum(singular_values**r))
        print(f"r={r}: sum s_j^r = {schatten_sum}")
    assert np.allclose(singular_values[0], expected)
    assert np.allclose(singular_values[1:], 0.0)


if __name__ == "__main__":
    main()
