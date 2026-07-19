"""Exact symbolic expansion for the nonlinear LW counterexample candidate."""

import sympy as sp


x, y, z, e = sp.symbols("x y z e", real=True)
variables = (x, y, z)

p1 = sp.Matrix((y + e*x*z, z - e*x*y))
p2 = sp.Matrix((z + e*x*y, x - e*y*z))
p3 = sp.Matrix((x + e*y*z, y - e*x*z))
maps = (p1, p2, p3)

omegas = []
for p in maps:
    jac = p.jacobian(variables)
    omegas.append(jac.row(0).T.cross(jac.row(1).T))

determinant = sp.factor(sp.Matrix.hstack(*omegas).det())
sum_squares = sp.factor(sum((p.dot(p) for p in maps), sp.Integer(0)))
excess = sp.factor(sum_squares - 2*(x*x + y*y + z*z))

# Near the origin the determinant is positive.  Expand through second order.
relative = sp.sqrt(determinant) * sp.exp(-excess/2)
series = sp.series(relative, e, 0, 3).removeO().expand()
linear = sp.expand(series.coeff(e, 1))
quadratic = sp.expand(series.coeff(e, 2))


def gaussian_expectation(poly):
    """Expectation for independent N(0,1/2) coordinates."""
    value = sp.Integer(0)
    expanded = sp.Poly(sp.expand(poly), x, y, z)
    for powers, coefficient in expanded.terms():
        moment = coefficient
        for power in powers:
            if power % 2:
                moment = 0
                break
            k = power // 2
            moment *= sp.factorial2(2*k - 1) / (2**k) if k else 1
        value += moment
    return sp.simplify(value)


print("omega_1", [sp.factor(v) for v in omegas[0]])
print("omega_2", [sp.factor(v) for v in omegas[1]])
print("omega_3", [sp.factor(v) for v in omegas[2]])
print("determinant", determinant)
print("excess", excess)
print("linear", sp.factor(linear))
print("quadratic", sp.factor(quadratic))
print("E_linear", gaussian_expectation(linear))
print("E_quadratic", gaussian_expectation(quadratic))
