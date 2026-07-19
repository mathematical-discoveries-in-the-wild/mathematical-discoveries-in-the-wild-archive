"""Finite-dimensional sanity checks for the kernel-pairing packet.

This script is not part of the proof. It checks representative cyclic and
free-group-style finite-dimensional examples where the isometries are
non-orthogonal conjugates of rotations. The theorem in the packet proves the
full finite-dimensional statement.
"""

from __future__ import annotations

import itertools
import numpy as np


def nullspace(a: np.ndarray, tol: float = 1e-9) -> np.ndarray:
    _, s, vh = np.linalg.svd(a)
    return vh[(s > tol).sum() :].T


def rotation(theta: float) -> np.ndarray:
    return np.array(
        [[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]],
        dtype=float,
    )


def cyclic_kernel(t: np.ndarray, s_values: list[int]) -> np.ndarray:
    n = t.shape[0]
    idx = {s: i for i, s in enumerate(s_values)}

    def tp(k: int) -> np.ndarray:
        if k >= 0:
            return np.linalg.matrix_power(t, k)
        return np.linalg.matrix_power(np.linalg.inv(t), -k)

    rows = []
    for s in s_values:
        if -s in idx:
            row = np.zeros((n, len(s_values) * n))
            row[:, idx[s] * n : (idx[s] + 1) * n] = np.eye(n)
            row[:, idx[-s] * n : (idx[-s] + 1) * n] = tp(s)
            rows.append(row)
    for s in s_values:
        for u in s_values:
            r = u - s
            if r in idx:
                row = np.zeros((n, len(s_values) * n))
                row[:, idx[r] * n : (idx[r] + 1) * n] += tp(s)
                row[:, idx[u] * n : (idx[u] + 1) * n] -= np.eye(n)
                row[:, idx[s] * n : (idx[s] + 1) * n] += np.eye(n)
                rows.append(row)
    return nullspace(np.vstack(rows))


def reduced(word: tuple[int, ...]) -> tuple[int, ...]:
    stack: list[int] = []
    for letter in word:
        if stack and stack[-1] == -letter:
            stack.pop()
        else:
            stack.append(letter)
    return tuple(stack)


def inverse_word(word: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(-letter for letter in word[::-1])


def cocycle_operator(a: np.ndarray, b: np.ndarray, word: tuple[int, ...]) -> np.ndarray:
    n = a.shape[0]
    out = np.zeros((n, 2 * n))
    current = np.eye(n)
    inv_a = np.linalg.inv(a)
    inv_b = np.linalg.inv(b)
    for letter in word:
        if letter == 1:
            out[:, :n] += current
            current = current @ a
        elif letter == -1:
            out[:, :n] -= current @ inv_a
            current = current @ inv_a
        elif letter == 2:
            out[:, n:] += current
            current = current @ b
        elif letter == -2:
            out[:, n:] -= current @ inv_b
            current = current @ inv_b
    return out


def free_group_cocycle_matrix(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    words = set()
    for length in (1, 2):
        for word in itertools.product([1, -1, 2, -2], repeat=length):
            if reduced(word) == word:
                words.add(word)
    words |= {inverse_word(word) for word in words}
    ordered = sorted(words, key=lambda w: (len(w), w))
    return np.vstack([cocycle_operator(a, b, word) for word in ordered])


def assert_full_pairing_rank(k: np.ndarray, k_dual: np.ndarray) -> None:
    pairing = k.T @ k_dual
    rank = np.linalg.matrix_rank(pairing, tol=1e-8)
    expected = pairing.shape[0]
    if rank != expected:
        raise AssertionError(f"rank {rank}, expected {expected}")


def main() -> None:
    conjugators = [
        np.array([[1.0, 3.0], [0.2, 1.0]]),
        np.array([[1.0, 5.0], [0.0, 1.0]]),
        np.array([[2.0, 1.0], [1.0, 1.0]]),
    ]

    for p in conjugators:
        t = p @ rotation(0.7) @ np.linalg.inv(p)
        k = cyclic_kernel(t, [-2, -1, 1, 2])
        k_dual = cyclic_kernel(np.linalg.inv(t).T, [-2, -1, 1, 2])
        assert_full_pairing_rank(k, k_dual)

        a = p @ rotation(0.4) @ np.linalg.inv(p)
        b = p @ rotation(1.1) @ np.linalg.inv(p)
        k = free_group_cocycle_matrix(a, b)
        k_dual = free_group_cocycle_matrix(np.linalg.inv(a).T, np.linalg.inv(b).T)
        assert_full_pairing_rank(k, k_dual)

    print("finite-dimensional kernel-pairing sanity checks passed")


if __name__ == "__main__":
    main()
