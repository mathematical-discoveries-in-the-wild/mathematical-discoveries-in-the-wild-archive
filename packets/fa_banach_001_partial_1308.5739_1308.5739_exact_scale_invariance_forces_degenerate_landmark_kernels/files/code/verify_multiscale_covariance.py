#!/usr/bin/env python3
"""Identity checks for adaptive and augmented scale-covariant Hamiltonians."""

import math

import numpy as np


def kernel(alpha, scale, displacement):
    ratio = displacement / scale
    return scale**alpha * math.exp(-(ratio * ratio))


def derivative_x(alpha, scale, displacement):
    ratio = displacement / scale
    return scale ** (alpha - 1) * (-2.0 * ratio) * math.exp(-(ratio * ratio))


def derivative_scale(alpha, scale, displacement):
    ratio = displacement / scale
    return (
        scale ** (alpha - 1)
        * (alpha + 2.0 * ratio * ratio)
        * math.exp(-(ratio * ratio))
    )


def vector_field(alpha, beta, q, scale, p, pi):
    landmarks = len(q)
    qdot = np.zeros(landmarks)
    pdot = np.zeros(landmarks)
    scale_derivative = 0.0
    for a in range(landmarks):
        for b in range(landmarks):
            displacement = q[a] - q[b]
            qdot[a] += kernel(alpha, scale, displacement) * p[b]
            pdot[a] -= p[a] * p[b] * derivative_x(
                alpha, scale, displacement
            )
            scale_derivative += (
                0.5
                * p[a]
                * p[b]
                * derivative_scale(alpha, scale, displacement)
            )
    scaledot = beta * scale**alpha * pi
    pidot = -scale_derivative
    pidot -= 0.5 * beta * alpha * scale ** (alpha - 1) * pi * pi
    return qdot, scaledot, pdot, pidot


def gram(alpha, scale, q):
    return np.array(
        [
            [kernel(alpha, scale, q[a] - q[b]) for b in range(len(q))]
            for a in range(len(q))
        ]
    )


def rms_scale(q):
    centered = q - np.mean(q)
    return math.sqrt(float(np.mean(centered * centered)))


def adaptive_vector_field(alpha, q, p):
    landmarks = len(q)
    scale = rms_scale(q)
    centered = q - np.mean(q)
    scale_gradient = centered / (landmarks * scale)
    matrix = gram(alpha, scale, q)
    qdot = matrix @ p
    pdot = np.zeros(landmarks)
    for k in range(landmarks):
        h_gradient = 0.0
        for a in range(landmarks):
            for b in range(landmarks):
                displacement = q[a] - q[b]
                displacement_gradient = float(a == k) - float(b == k)
                kernel_gradient = derivative_x(
                    alpha, scale, displacement
                ) * displacement_gradient
                kernel_gradient += derivative_scale(
                    alpha, scale, displacement
                ) * scale_gradient[k]
                h_gradient += 0.5 * p[a] * p[b] * kernel_gradient
        pdot[k] = -h_gradient
    return qdot, pdot, scale, np.linalg.eigvalsh(matrix)


def check_case(alpha, dilation):
    beta = 1.7
    q = np.array([-1.2, 0.35, 2.1])
    scale = 0.8
    p = np.array([0.7, -1.1, 0.25])
    pi = -0.45
    original = vector_field(alpha, beta, q, scale, p, pi)

    momentum_factor = dilation ** (1.0 - alpha)
    transformed = vector_field(
        alpha,
        beta,
        dilation * q,
        dilation * scale,
        momentum_factor * p,
        momentum_factor * pi,
    )
    expected = (
        dilation * original[0],
        dilation * original[1],
        momentum_factor * original[2],
        momentum_factor * original[3],
    )
    for actual, target in zip(transformed, expected):
        np.testing.assert_allclose(actual, target, rtol=2e-13, atol=2e-13)

    eigenvalues = np.linalg.eigvalsh(gram(alpha, scale, q))
    assert eigenvalues[0] > 0.0
    print(
        f"alpha={alpha:4.1f}, lambda={dilation:3.1f}: "
        f"covariance passed; Gram min eigenvalue={eigenvalues[0]:.8f}"
    )


def check_adaptive_case(alpha, dilation):
    q = np.array([-1.2, 0.35, 2.1])
    p = np.array([0.7, -1.1, 0.25])
    original = adaptive_vector_field(alpha, q, p)
    momentum_factor = dilation ** (1.0 - alpha)
    transformed = adaptive_vector_field(
        alpha, dilation * q, momentum_factor * p
    )
    np.testing.assert_allclose(
        transformed[0], dilation * original[0], rtol=2e-13, atol=2e-13
    )
    np.testing.assert_allclose(
        transformed[1], momentum_factor * original[1], rtol=2e-13, atol=2e-13
    )
    np.testing.assert_allclose(
        transformed[2], dilation * original[2], rtol=2e-13, atol=2e-13
    )
    assert transformed[3][0] > 0.0
    print(
        f"adaptive alpha={alpha:4.1f}, lambda={dilation:3.1f}: "
        f"covariance passed; scaled rho={transformed[2]:.8f}"
    )


if __name__ == "__main__":
    for exponent in (-1.5, 0.0, 1.0, 2.0, 3.25):
        for factor in (0.4, 1.8, 3.0):
            check_case(exponent, factor)
            check_adaptive_case(exponent, factor)
    print("ALL AUGMENTED AND ADAPTIVE SCALE-COVARIANCE CHECKS PASSED")
