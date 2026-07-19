from fractions import Fraction


def next_power_of_two(n):
    value = 1
    while value < n:
        value *= 2
    return value


def sylvester(order):
    if order < 1 or order & (order - 1):
        raise ValueError("order must be a power of two")
    matrix = [[1]]
    while len(matrix) < order:
        top = [row + row for row in matrix]
        bottom = [row + [-entry for entry in row] for row in matrix]
        matrix = top + bottom
    return matrix


def frame_operator_from_first_columns(n):
    N = next_power_of_two(n)
    H = sylvester(N)
    op = []
    for k in range(n):
        row = []
        for i in range(n):
            total = sum(H[r][i] * H[r][k] for r in range(N))
            row.append(Fraction(total, n))
        op.append(row)
    target = [
        [Fraction(N, n) if i == k else Fraction(0, 1) for i in range(n)]
        for k in range(n)
    ]
    return N, op, target


def check_normalizations(n):
    N = next_power_of_two(n)
    H = sylvester(N)
    for r in range(N):
        x_norm = sum(Fraction(abs(H[r][i]), n) for i in range(n))
        x_star_norm = max(abs(H[r][i]) for i in range(n))
        pairing = sum(Fraction(H[r][i] * H[r][i], n) for i in range(n))
        assert x_norm == 1
        assert x_star_norm == 1
        assert pairing == 1


def main():
    for n in range(2, 21):
        N, op, target = frame_operator_from_first_columns(n)
        check_normalizations(n)
        assert op == target
        print(f"n={n:2d}, N={N:2d}: frame operator = ({N}/{n}) I")
    print("All Sylvester checks passed.")


if __name__ == "__main__":
    main()
