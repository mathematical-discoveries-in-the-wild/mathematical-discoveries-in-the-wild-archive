# Literature-Implied Answer: Optimal Uniform-POVM Reverse Holder Constant

Status: `literature_implied_answer (full source subquestion)`

Source paper: Guillaume Aubrun and Cecilia Lancien, "Zonoids and Sparsification of Quantum Measurements", arXiv:1309.6003.

Supporting theorem: Daniel Murawski, "Comparing moments of real log-concave random variables", arXiv:2211.05210, Theorem 1.3.

## Source Question

In Section 4.1, after Proposition 4.1 and equations (10)--(12), Aubrun--Lancien prove

```text
(1/sqrt(18)) ||Delta||_{2(1)} <= ||Delta||_{U_d} <= ||Delta||_{2(1)}
```

and say that this is a reverse Holder inequality, asking for the optimal constant in that inequality.

## Identification

For a standard complex Gaussian vector `g`, the source observes that

```text
||Delta||_{U_d} = E | <g, Delta g> |
||Delta||_{2(1)} = (E | <g, Delta g> |^2)^{1/2}.
```

After diagonalizing `Delta`, the scalar random variable is

```text
X_Delta = sum_j lambda_j E_j,
```

where `E_j` are independent exponential random variables of mean 1. This law is log-concave, since it is a linear image of the product exponential measure on the positive orthant.

Murawski's Theorem 1.3 says that, among all real log-concave random variables, the largest `L2/L1` ratio is attained by a shifted exponential distribution. Therefore the optimal constant in the Aubrun--Lancien inequality is obtained by optimizing `E-s`.

## Constant

Let `s0` be the unique positive solution of

```text
exp(s) = 2(s^2 - s + 1).
```

Numerically,

```text
s0 = 0.41504274311322024063...
```

Then the sharp lower constant is

```text
kappa = (s0 - 1 + 2 exp(-s0)) / sqrt(s0^2 - 2s0 + 2)
      = 0.63500423058334237014...
```

Equivalently, the optimal reverse Holder factor is

```text
kappa^{-1} = 1.5747926578085262810...
```

Thus for every dimension `d` and every Hermitian `Delta`,

```text
kappa ||Delta||_{2(1)} <= ||Delta||_{U_d} <= ||Delta||_{2(1)},
```

and `kappa` cannot be increased uniformly over all `d`.

Sharpness in the original matrix class follows by taking spectra

```text
(1, -s0/N, ..., -s0/N)
```

in dimension `N+1`. Then

```text
<g, Delta_N g> = E_0 - (s0/N)(E_1 + ... + E_N)
```

converges in `L1` and `L2` to `E_0 - s0`.

## Scope

This answers only the reverse-Holder optimal-constant subquestion in Section 4.1. It does not address the paper's separate questions about deterministic sparsification of the uniform POVM, removal of the logarithmic factor for arbitrary zonoid approximation, or whether the arbitrary-POVM sub-POVM sparsification theorem can be upgraded to a true POVM.

The supporting paper does not explicitly cite Aubrun--Lancien's POVM question; the relation is an agent-identified implication via log-concavity of Gaussian Hermitian quadratic forms.

## Search Notes

Local cheap indexes had no prior `1309.6003` packet. Web searches for direct phrases such as `"sqrt{18}" "uniform POVM" "optimal constant"` and `"Zonoids and sparsification" "optimal constant"` did not reveal a direct POVM-specific answer. The decisive later theorem found was Murawski arXiv:2211.05210 on moment comparison for real log-concave random variables.

