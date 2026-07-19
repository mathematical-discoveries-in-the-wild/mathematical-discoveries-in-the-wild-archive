# Counterexample packet: operator-norm Toeplitz upgrade

Source paper: Siarhei Finski, *Bernstein-Markov measures and Toeplitz theory*, arXiv:2506.01610.

## Claim

Remark 1.6 asks whether, in the Bernstein-Markov setting of the paper, one can obtain the analogue of Theorem 1.5 with the normalized Schatten norm replaced by the operator norm.

This packet gives a negative answer. In the paper's own circle model
`X = P^1`, `L = O(1)`, and `mu` equal to Lebesgue measure on a great circle,
Definition 1.3 recovers finite Toeplitz matrices. For the real continuous
symbol

```text
h(e^{i theta}) = e^{i theta} + e^{-i theta} = 2 cos(theta),
```

the matrices satisfy

```text
|| T_N[h] T_N[h] - T_N[h^2] || = 1
```

for every `N >= 2`, while the normalized Schatten `p`-norm is
`(2/N)^{1/p}` and hence tends to zero. Thus Theorem 1.5 is sharp with respect
to the normalized Schatten topology: the general Bernstein-Markov hypothesis
does not force the operator-norm product formula.

## Mechanism

In the Fourier basis, `T_N[h]` is the truncated shift plus its adjoint. The
failure of multiplicativity is exactly the sum of the two boundary projections.
These projections disappear in normalized Schatten norm but remain visible in
operator norm.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered PDF.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_problem_crop.png`: crop of Theorem 1.5 and Remark 1.6.

## Status

`counterexample_likely_valid`. The packet disproves the operator-norm analogue
in the full Bernstein-Markov setting. It does not address possible additional
regularity hypotheses on the measure, and it does not settle the separate
`L^\infty`-symbol analogue mentioned in the same remark.
