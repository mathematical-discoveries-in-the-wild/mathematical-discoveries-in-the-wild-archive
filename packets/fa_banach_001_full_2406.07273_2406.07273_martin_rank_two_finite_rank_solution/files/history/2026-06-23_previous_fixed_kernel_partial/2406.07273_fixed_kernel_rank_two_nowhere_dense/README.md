# Fixed-Kernel Obstruction for Rank-Two Operators on Martin's Space

Result type: `partial`

Status: candidate partial result, likely valid pending human review.

Source paper:

- Miguel Martin, "A Banach space whose set of norm-attaining functionals is
  algebraically trivial", arXiv:2406.07273.
- Local source PDF: `source_paper.pdf`.
- Open-problem evidence crop: `figures/open_problem_crop.png`.

## Source Problem

Open Problem 7 asks whether the constructed smooth renorming `X` of `c0`,
whose scalar norm-attaining functionals contain no non-trivial cones, satisfies
that `NA(X, ell_2^2)` contains a rank-two operator.

## Claimed Contribution

Let `X` be Martin's space and let `M` be any closed codimension-two subspace.
Inside the finite-dimensional fibre

```text
L_M = { T : X -> ell_2^2 : M subset ker T },
```

the norm-attaining operators form a nowhere dense subset. Equivalently, every
rank-two norm-attaining operator with kernel `M`, if one exists, can be
arbitrarily closely perturbed without changing its kernel so that it no longer
attains its norm.

This does not solve Open Problem 7. It shows that no fixed quotient/kernel can
support a robust positive answer.

## Files

- `main.tex`: self-contained LaTeX packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2406.07273.
- `figures/open_problem_crop.png`: screenshot crop of Open Problem 7.
- `tmp/`: LaTeX build intermediates and rendered page image used for cropping.

## Proof Ingredients

- Martin's Proposition 2.4: for every codimension-two `M`, the set
  `q_M(B_X) cap S_{X/M}` contains at most two antipodal pairs.
- Martin's space is smooth, hence every two-dimensional quotient `X/M` is
  smooth.
- In a smooth two-dimensional domain `E`, for each fixed `e in S_E`, the set
  of operators `A:E -> ell_2^2` whose norm is attained at `e` is closed
  nowhere dense.

## Human Review Notes

Verifier focus:

- Check the finite-dimensional perturbation lemma for `F_e`.
- Check that smoothness passes from Martin's `X` to the quotient `X/M` via
  strict convexity of `X^*`.
- Check that the theorem is correctly limited to fixed-kernel fibres and does
  not claim non-existence or non-density when kernels vary.

No computational verification is needed; the argument is purely analytic.
