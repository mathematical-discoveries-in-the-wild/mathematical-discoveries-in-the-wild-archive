import sympy as sp


s = sp.symbols("s")


def laurent_coeff(expr, power):
    return sp.expand(sp.apart(sp.cancel(expr), s)).coeff(s, power)


def matrix_coeff(M, power):
    return sp.Matrix([[laurent_coeff(M[i, j], power) for j in range(M.cols)] for i in range(M.rows)])


H0 = sp.diag(1, 1, -1, 0, 0)
V = sp.Matrix(
    [
        [0, -1, -1, 0, 1],
        [-1, 0, -1, 1, 1],
        [-1, -1, 1, 1, 1],
        [0, 1, 1, 0, 0],
        [1, 1, 1, 0, 1],
    ]
)

K = sp.diag(1, 1, -1)
Vhat = sp.Matrix([[0, -1, -1], [-1, 0, -1], [-1, -1, 1]])
v = sp.Matrix([[0, 1], [1, 1], [1, 1]])
S = sp.zeros(5)
S[:3, :3] = K.inv() * Vhat
S[:3, 3:5] = K.inv() * v

A_of_s = (H0 + s * V).inv() * V
P = matrix_coeff(A_of_s, -1)
Alambda = matrix_coeff(A_of_s, -2)
Alambda2 = matrix_coeff(A_of_s, -3)

chi = sp.Matrix([0, 1, 0, -2, 1])
Schi = S * chi
defect = (Alambda * S + sp.eye(5)) * chi


def main():
    print("det(H0+sV) =", sp.factor((H0 + s * V).det()))
    assert sp.factor((H0 + s * V).det()) == 3 * s**4 * (s - 1)
    assert H0 == H0.T
    assert V == V.T
    assert P * P == P
    assert Alambda**2 == Alambda2
    assert Alambda**3 == sp.zeros(5)
    assert P * chi == chi
    assert P * Schi == Schi
    assert Schi != sp.zeros(5, 1)
    assert defect != sp.zeros(5, 1)
    print("P =")
    print(P)
    print("A_lambda =")
    print(Alambda)
    print("chi =", list(chi))
    print("S chi =", list(Schi))
    print("(A_lambda S + I) chi =", list(defect))
    print("verification_passed")


if __name__ == "__main__":
    main()
