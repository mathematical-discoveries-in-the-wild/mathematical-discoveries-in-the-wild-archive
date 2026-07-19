import math


def hs_partial(n: int) -> float:
    total = 0.0
    for i in range(1, n + 1):
        theta_i = 2.0 ** (-i)
        m_i = 2.0 ** (-4 * i)
        for j in range(1, n + 1):
            if i == j:
                continue
            theta_j = 2.0 ** (-j)
            m_j = 2.0 ** (-4 * j)
            denom = abs(1.0 - complex(math.cos(theta_j - theta_i), math.sin(theta_j - theta_i)))
            total += m_i * m_j / (denom * denom)
    return total


def main() -> None:
    for n in [10, 20, 40, 80, 160]:
        print(n, hs_partial(n))


if __name__ == "__main__":
    main()
