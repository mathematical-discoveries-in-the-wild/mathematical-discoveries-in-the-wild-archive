from decimal import Decimal, getcontext

getcontext().prec = 80

p = 20
eps = Decimal("0.000001")
t = Decimal(9) / Decimal(20)

# Check lambda_X^-(1) < 1e-6 for x=(1,t)/A and tangent y=(t^19,-1)/B.
A = (Decimal(1) + t**p) ** (Decimal(1) / Decimal(p))
B = (Decimal(1) + t ** (p * (p - 1))) ** (Decimal(1) / Decimal(p))
c1 = (Decimal(1) - eps) / A + (t ** (p - 1)) / B
c2 = (Decimal(1) - eps) * t / A - Decimal(1) / B
norm20 = abs(c1) ** p + abs(c2) ** p
c1_start = Decimal(1) / A + (t ** (p - 1)) / B
c2_start = t / A - Decimal(1) / B
norm20_start = abs(c1_start) ** p + abs(c2_start) ** p

# Check the symmetric lambda^+ lower bound at r0 = (1-1e-6)/2.
r0 = (Decimal(1) - eps) / Decimal(2)
u0 = Decimal(2) ** (Decimal(-9) / Decimal(10))
sym_value = (u0 + r0) ** p + abs(u0 - r0) ** p

print("norm20_at_lambda_0 =", norm20_start)
print("norm20_at_lambda_0 > 1:", norm20_start > 1)
print("norm20_at_lambda_1e-6 =", norm20)
print("norm20_at_lambda_1e-6 < 1:", norm20 < 1)
print("symmetric_value_at_u0 =", sym_value)
print("symmetric_value_at_u0 > 2:", sym_value > 2)
print("2^(9/10) =", Decimal(2) ** (Decimal(9) / Decimal(10)))
