"""Verify the rank calculation for a homogeneous Ramsey four-set."""

from __future__ import annotations


def canonical(labels: list[int]) -> tuple[int, ...]:
    names: dict[int, int] = {}
    out: list[int] = []
    for label in labels:
        if label not in names:
            names[label] = len(names)
        out.append(names[label])
    return tuple(out)


def join(x: tuple[int, ...], y: tuple[int, ...]) -> tuple[int, ...]:
    parent = list(range(len(x)))

    def find(a: int) -> int:
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a: int, b: int) -> None:
        a, b = find(a), find(b)
        if a != b:
            parent[b] = a

    for partition in (x, y):
        first: dict[int, int] = {}
        for i, label in enumerate(partition):
            if label in first:
                union(i, first[label])
            else:
                first[label] = i
    return canonical([find(i) for i in range(len(x))])


def meet(x: tuple[int, ...], y: tuple[int, ...]) -> tuple[int, ...]:
    pairs = [(x[i], y[i]) for i in range(len(x))]
    names: dict[tuple[int, int], int] = {}
    return tuple(names.setdefault(pair, len(names)) for pair in pairs)


def rank(x: tuple[int, ...]) -> int:
    return len(x) - len(set(x))


def verify(testers: list[tuple[int, ...]], four: tuple[int, int, int, int]) -> None:
    n = len(testers[0])
    a, b, c, d = four
    y_labels = list(range(n))
    y_labels[b] = y_labels[a]
    y_labels[d] = y_labels[c]
    y = canonical(y_labels)
    assert rank(y) == 2

    for x in testers:
        relations = {x[u] == x[v] for j, u in enumerate(four) for v in four[j + 1 :]}
        assert len(relations) == 1, "the supplied four-set is not homogeneous"
        gap = rank(x) + rank(y) - rank(join(x, y)) - rank(meet(x, y))
        assert gap == 0


if __name__ == "__main__":
    demo_testers = [
        (0, 0, 0, 0, 1, 2, 3, 4),
        (0, 1, 2, 3, 0, 1, 2, 3),
        (0, 1, 2, 3, 4, 4, 5, 5),
    ]
    verify(demo_testers, (0, 1, 2, 3))
    print("Ramsey witness rank identities verified")

