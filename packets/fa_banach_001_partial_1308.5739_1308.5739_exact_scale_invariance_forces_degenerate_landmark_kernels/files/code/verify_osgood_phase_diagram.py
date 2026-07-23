#!/usr/bin/env python3
"""High-precision checks for the adaptive rough-kernel collision theorem."""

from __future__ import annotations

import mpmath as mp


mp.mp.dps = 80


def dot(x: list[mp.mpf], y: list[mp.mpf]) -> mp.mpf:
    return mp.fsum(a * b for a, b in zip(x, y))


def norm(x: list[mp.mpf]) -> mp.mpf:
    return mp.sqrt(dot(x, x))


def sub(x: list[mp.mpf], y: list[mp.mpf]) -> list[mp.mpf]:
    return [a - b for a, b in zip(x, y)]


def configuration(n: int, d: int, eps: mp.mpf) -> list[list[mp.mpf]]:
    e = [mp.mpf(1)] + [mp.mpf(0)] * (d - 1)
    q = [[-eps * x for x in e], [eps * x for x in e]]
    for j in range(3, n + 1):
        q.append(
            [
                mp.mpf(j - 1)
                + mp.mpf(k + 1) / mp.mpf(7)
                + mp.mpf((j + 2 * k) % 3) / mp.mpf(11)
                for k in range(d)
            ]
        )
    return q


def rms_scale(q: list[list[mp.mpf]]) -> mp.mpf:
    n = len(q)
    d = len(q[0])
    mean = [mp.fsum(q[i][k] for i in range(n)) / n for k in range(d)]
    return mp.sqrt(
        mp.fsum(dot(sub(x, mean), sub(x, mean)) for x in q) / n
    )


def gram(q: list[list[mp.mpf]], beta: mp.mpf) -> tuple[mp.matrix, mp.mpf]:
    n = len(q)
    rho = rms_scale(q)
    k = mp.matrix(n)
    for i in range(n):
        for j in range(n):
            t = norm(sub(q[i], q[j])) / rho
            k[i, j] = mp.exp(-(t**beta))
    return k, rho


def collision_blocks(
    n: int, d: int, beta: mp.mpf, eps: mp.mpf
) -> tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf]:
    q = configuration(n, d, eps)
    k, rho = gram(q, beta)

    # Columns are u=(e1-e2)/sqrt(2), w=(e1+e2)/sqrt(2), e3,...,eN.
    t = mp.eye(n)
    root2 = mp.sqrt(2)
    t[0, 0], t[1, 0] = 1 / root2, -1 / root2
    t[0, 1], t[1, 1] = 1 / root2, 1 / root2
    for row in range(2, n):
        t[row, row] = 1
    kb = t.T * k * t
    a = kb[0, 0]
    b = kb[1:n, 0]
    c = kb[1:n, 1:n]
    schur = a - (b.T * c**-1 * b)[0]

    # The collision velocity is -sqrt(2)u. Its exact metric norm is
    # 2/(rho^2 S), where S is the Schur complement.
    velocity = mp.matrix(n, 1)
    velocity[0], velocity[1] = -1, 1
    speed_sq_direct = (velocity.T * k**-1 * velocity)[0] / rho**2
    speed_sq_schur = 2 / (rho**2 * schur)
    return a, schur, speed_sq_direct, speed_sq_schur


def assert_close(x: mp.mpf, y: mp.mpf, tol: mp.mpf, label: str) -> None:
    rel = abs(x - y) / max(mp.mpf(1), abs(x), abs(y))
    if rel > tol:
        raise AssertionError(f"{label}: relative error {mp.nstr(rel, 12)}")


def main() -> None:
    betas = [mp.mpf("0.5"), mp.mpf("1.0"), mp.mpf("1.5"), mp.mpf("1.9")]
    cases = [(3, 1), (4, 2), (6, 3), (8, 4)]
    eps1, eps2 = mp.mpf("1e-12"), mp.mpf("1e-18")
    tol = mp.mpf("1e-42")

    checks = 0
    for n, d in cases:
        for beta in betas:
            a1, s1, direct1, schur1 = collision_blocks(n, d, beta, eps1)
            a2, s2, direct2, schur2 = collision_blocks(n, d, beta, eps2)
            if not (a1 > 0 and s1 > 0 and a2 > 0 and s2 > 0):
                raise AssertionError("positive Schur complement failed")
            assert_close(direct1, schur1, tol, "inverse/Schur identity eps1")
            assert_close(direct2, schur2, tol, "inverse/Schur identity eps2")

            ratio = s2 / a2
            if abs(ratio - 1) > mp.mpf("2e-3"):
                raise AssertionError(
                    f"S/a not tending to 1: N={n}, d={d}, beta={beta}, "
                    f"ratio={mp.nstr(ratio, 12)}"
                )
            slope = mp.log(s2 / s1) / mp.log(eps2 / eps1)
            if abs(slope - beta) > mp.mpf("2e-3"):
                raise AssertionError(
                    f"wrong Schur exponent: N={n}, d={d}, beta={beta}, "
                    f"slope={mp.nstr(slope, 12)}"
                )

            scaled_speed = mp.sqrt(direct2) * eps2 ** (beta / 2)
            if not (scaled_speed > 0 and mp.isfinite(scaled_speed)):
                raise AssertionError("scaled speed did not approach a finite constant")

            print(
                f"N={n}, d={d}, beta={mp.nstr(beta, 3)}: "
                f"S/a={mp.nstr(ratio, 10)}, "
                f"log-slope={mp.nstr(slope, 10)}, "
                f"scaled-speed={mp.nstr(scaled_speed, 10)}"
            )
            checks += 1

    cutoff = mp.mpf("1e-30")
    for beta in betas:
        exponent = 1 - beta / 2
        integral = (1 - cutoff**exponent) / exponent
        numerical = mp.quad(lambda x: x ** (-beta / 2), [cutoff, 1])
        assert_close(integral, numerical, mp.mpf("1e-35"), "model integral")
    beta_two_truncation = mp.quad(lambda x: 1 / x, [cutoff, 1])
    assert_close(
        beta_two_truncation,
        -mp.log(cutoff),
        mp.mpf("1e-55"),
        "beta=2 logarithmic divergence",
    )

    print(f"rough collision cases checked: {checks}")
    print("ALL OSGOOD PHASE-DIAGRAM CHECKS PASSED")


if __name__ == "__main__":
    main()
