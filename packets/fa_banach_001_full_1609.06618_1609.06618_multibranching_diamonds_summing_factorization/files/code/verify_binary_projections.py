#!/usr/bin/env python3
"""Exhaustively verify the binary-projection lemma at finite depths.

Vertices born at a refinement step are addressed by the parent-edge address
and their local arm label.  Replacing each arm label by one bit of an injective
binary code gives the canonical projection to a binary diamond.
"""

from __future__ import annotations

import argparse
from collections import deque
from dataclasses import dataclass
from typing import Optional


Vertex = tuple
EdgeAddress = tuple[tuple[int, int], ...]


@dataclass
class Diamond:
    vertices: list[Vertex]
    index: dict[Vertex, int]
    adjacency: list[list[int]]
    final_edges: list[tuple[int, int]]
    labels: Optional[list[list[int]]] = None


def build_diamond(n: int, k: int, with_binary_labels: bool = False) -> Diamond:
    if with_binary_labels and k != 2:
        raise ValueError("Hamming labels are implemented only for k=2")

    dimension = 2**n
    bottom: Vertex = ("B",)
    top: Vertex = ("T",)
    vertices = [bottom, top]
    index = {bottom: 0, top: 1}
    labels = ([([0] * dimension), ([1] * dimension)]
              if with_binary_labels else None)
    initial_support = tuple(range(dimension)) if with_binary_labels else None
    edges: list[tuple[Vertex, Vertex, EdgeAddress, Optional[tuple[int, ...]]]] = [
        (bottom, top, (), initial_support)
    ]

    for _ in range(n):
        new_edges = []
        for u, v, address, support in edges:
            for arm in range(k):
                midpoint: Vertex = ("M", address, arm)
                index[midpoint] = len(vertices)
                vertices.append(midpoint)

                lower_support = upper_support = None
                if labels is not None:
                    assert support is not None
                    half = len(support) // 2
                    chunks = (support[:half], support[half:])
                    z = labels[index[u]].copy()
                    for coordinate in chunks[arm]:
                        z[coordinate] = labels[index[v]][coordinate]
                    labels.append(z)
                    lower_support = tuple(
                        coordinate for coordinate in support
                        if labels[index[u]][coordinate] != z[coordinate]
                    )
                    upper_support = tuple(
                        coordinate for coordinate in support
                        if z[coordinate] != labels[index[v]][coordinate]
                    )

                new_edges.append(
                    (u, midpoint, address + ((arm, 0),), lower_support)
                )
                new_edges.append(
                    (midpoint, v, address + ((arm, 1),), upper_support)
                )
        edges = new_edges

    adjacency = [[] for _ in vertices]
    final_edges = []
    for u, v, _, _ in edges:
        ui, vi = index[u], index[v]
        adjacency[ui].append(vi)
        adjacency[vi].append(ui)
        final_edges.append((ui, vi))

    return Diamond(vertices, index, adjacency, final_edges, labels)


def all_pairs_distances(adjacency: list[list[int]]) -> list[list[int]]:
    output = []
    for source in range(len(adjacency)):
        distances = [-1] * len(adjacency)
        distances[source] = 0
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v in adjacency[u]:
                if distances[v] == -1:
                    distances[v] = distances[u] + 1
                    queue.append(v)
        output.append(distances)
    return output


def binary_codes(k: int) -> list[tuple[int, ...]]:
    width = max(1, (k - 1).bit_length())
    return [tuple(int(bit) for bit in f"{arm:0{width}b}") for arm in range(k)]


def project_descriptor(vertex: Vertex, codes: list[tuple[int, ...]], bit: int) -> Vertex:
    if vertex[0] != "M":
        return vertex
    _, address, arm = vertex
    projected_address = tuple((codes[parent_arm][bit], side)
                              for parent_arm, side in address)
    return ("M", projected_address, codes[arm][bit])


def verify(k: int, max_n: int) -> None:
    codes = binary_codes(k)
    width = len(codes[0])
    print(f"k={k}, code width={width}, codes={codes}")

    for n in range(1, max_n + 1):
        source = build_diamond(n, k)
        binary = build_diamond(n, 2, with_binary_labels=True)
        assert binary.labels is not None
        source_distances = all_pairs_distances(source.adjacency)
        binary_distances = all_pairs_distances(binary.adjacency)

        projections = []
        for bit in range(width):
            projections.append([
                binary.index[project_descriptor(vertex, codes, bit)]
                for vertex in source.vertices
            ])

        binary_edge_set = {
            (min(u, v), max(u, v)) for u, v in binary.final_edges
        }
        for u, v in source.final_edges:
            for projection in projections:
                image_edge = (min(projection[u], projection[v]),
                              max(projection[u], projection[v]))
                assert image_edge in binary_edge_set

        min_l1_ratio = float("inf")
        min_summing_ratio = float("inf")
        for u in range(len(source.vertices)):
            unscaled_u = sum(
                (binary.labels[projection[u]] for projection in projections),
                [],
            )
            for v in range(u + 1, len(source.vertices)):
                distance = source_distances[u][v]
                image_distances = [
                    binary_distances[projection[u]][projection[v]]
                    for projection in projections
                ]
                assert all(image <= distance for image in image_distances)
                assert max(image_distances) == distance

                unscaled_v = sum(
                    (binary.labels[projection[v]] for projection in projections),
                    [],
                )
                difference = [a - b for a, b in zip(unscaled_u, unscaled_v)]
                l1_unscaled = sum(abs(value) for value in difference)
                assert l1_unscaled <= width * distance
                partial = 0
                summing_unscaled = 0
                for value in difference:
                    partial += value
                    summing_unscaled = max(summing_unscaled, abs(partial))
                min_l1_ratio = min(
                    min_l1_ratio, l1_unscaled / (width * distance)
                )
                min_summing_ratio = min(
                    min_summing_ratio, summing_unscaled / (width * distance)
                )

        print(
            f"n={n}: vertices={len(source.vertices)}, "
            f"all pairs pass; min ||F(x)-F(y)||_1/d={min_l1_ratio:.8f}; "
            f"min ||F(x)-F(y)||_s/d={min_summing_ratio:.8f}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", type=int, default=3)
    parser.add_argument("--max-n", type=int, default=4)
    args = parser.parse_args()
    if args.k < 2:
        parser.error("k must be at least 2")
    verify(args.k, args.max_n)


if __name__ == "__main__":
    main()

