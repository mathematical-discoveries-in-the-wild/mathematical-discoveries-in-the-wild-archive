#!/usr/bin/env python3
"""Finite consistency checks for the sharp degree-one example.

This script is supplementary evidence only; the packet proof is algebraic.
"""

from itertools import product

import numpy as np


I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
PAULIS = (I, X, Y, Z)


def kron_all(matrices):
    out = np.array([[1.0 + 0.0j]])
    for matrix in matrices:
        out = np.kron(out, matrix)
    return out


def pauli_coefficients(operator, qubits, tolerance=1e-10):
    scale = 2**qubits
    coefficients = {}
    for word in product(range(4), repeat=qubits):
        pauli = kron_all(PAULIS[index] for index in word)
        coefficient = np.trace(pauli.conj().T @ operator) / scale
        if abs(coefficient) > tolerance:
            coefficients[word] = coefficient
    return coefficients


def main():
    q = (X + Y + Z) / np.sqrt(3)
    u = (np.kron(q, I) + 1j * np.kron(I, q)) / np.sqrt(2)
    assert np.allclose(q.conj().T @ q, I)
    assert np.allclose(u.conj().T @ u, np.eye(4))

    coefficients = pauli_coefficients(u, 2)
    degree = max(sum(index != 0 for index in word) for word in coefficients)
    ell1 = sum(abs(value) for value in coefficients.values())
    ell2_sq = sum(abs(value) ** 2 for value in coefficients.values())

    assert len(coefficients) == 6
    assert degree == 1
    assert np.isclose(ell1, np.sqrt(6))
    assert np.isclose(ell2_sq, 1)

    base_values = np.array(list(coefficients.values()))
    for d in range(1, 5):
        tensor_values = base_values
        for _ in range(d - 1):
            tensor_values = np.kron(tensor_values, base_values)
        assert np.isclose(np.sum(np.abs(tensor_values)), 6 ** (d / 2))
        assert np.isclose(np.sum(np.abs(tensor_values) ** 2), 1)

    print("verified: U_star is unitary, degree one, and has Pauli ell_1 = sqrt(6)")
    print("verified: tensor-power ell_1 norms equal 6^(d/2) for d=1,2,3,4")


if __name__ == "__main__":
    main()
