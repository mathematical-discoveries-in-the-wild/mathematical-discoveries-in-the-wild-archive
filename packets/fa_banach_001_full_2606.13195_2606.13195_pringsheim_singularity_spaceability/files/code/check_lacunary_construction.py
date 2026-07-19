import math


def block_indices(m: int, count: int) -> list[int]:
    return [2**m * (2 * j + 1) for j in range(count)]


def exponent_from_index(k: int) -> int:
    return 2**k


def main() -> None:
    blocks = {m: [exponent_from_index(k) for k in block_indices(m, 6)] for m in range(5)}
    all_exponents = [n for values in blocks.values() for n in values]
    assert len(all_exponents) == len(set(all_exponents))

    for m, values in blocks.items():
        ratios = [values[i + 1] / values[i] for i in range(len(values) - 1)]
        print(f"block {m}: first exponents={values[:3]}, min ratio={min(ratios):.1f}")
        assert min(ratios) >= 4

    master = sorted(all_exponents)
    master_ratios = [master[i + 1] / master[i] for i in range(len(master) - 1)]
    print("sample master minimum consecutive ratio:", min(master_ratios))
    assert min(master_ratios) >= 2

    for r in range(5):
        vals = [(n**r) * math.exp(-math.sqrt(n)) for n in master[-5:]]
        print(f"sample n^{r} exp(-sqrt(n)) tail max={max(vals):.3e}")

    for n in blocks[0][-3:]:
        root = math.exp(-math.sqrt(n) / n)
        print(f"|exp(-sqrt({n}))|^(1/{n}) = {root:.8f}")

    print("Finite sanity checks passed. The proof uses the full lacunary construction and Hadamard gap theorem.")


if __name__ == "__main__":
    main()
