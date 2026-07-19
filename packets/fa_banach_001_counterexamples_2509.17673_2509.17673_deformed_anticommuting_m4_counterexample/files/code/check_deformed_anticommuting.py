import numpy as np


def e(i, j):
    m = np.zeros((4, 4), dtype=complex)
    m[i - 1, j - 1] = 1
    return m


def algebra_generators(t):
    u = e(1, 3) + t * e(2, 4)
    v = e(1, 2) - t * e(3, 4)
    w = e(1, 4)
    return u, v, w


def main():
    t = 2.0
    u, v, w = algebra_generators(t)
    checks = {
        "u^2": np.linalg.norm(u @ u),
        "v^2": np.linalg.norm(v @ v),
        "uw": np.linalg.norm(u @ w),
        "wu": np.linalg.norm(w @ u),
        "vw": np.linalg.norm(v @ w),
        "wv": np.linalg.norm(w @ v),
        "uv + t w": np.linalg.norm(u @ v + t * w),
        "vu - t w": np.linalg.norm(v @ u - t * w),
        "uv + vu": np.linalg.norm(u @ v + v @ u),
    }
    for name, value in checks.items():
        print(f"{name}: {value:.3g}")

    x = u + v
    print("rank(u+v):", np.linalg.matrix_rank(x))
    print("singular values source u_1:", np.linalg.svd(algebra_generators(1.0)[0], compute_uv=False))
    print("singular values deformed u_2:", np.linalg.svd(u, compute_uv=False))

    # Ratio used in the proof: ||P_E x e_4|| / ||P_{Ce1} x|_E||.
    # For x = a u_t + b v_t + c w it equals t whenever (a,b) != (0,0).
    for a, b, c in [(1, 0, 0), (0, 1, 0), (1 + 2j, -3j, 5)]:
        x = a * u + b * v + c * w
        upper = np.linalg.norm(x[0, 1:3])
        lower = np.linalg.norm(x[1:3, 3])
        print(f"ratio for a={a}, b={b}, c={c}: {lower / upper:.12g}")


if __name__ == "__main__":
    main()
