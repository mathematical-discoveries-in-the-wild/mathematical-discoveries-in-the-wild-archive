# Partial solution packet: absolute-sum stability for the real Lipschitz numerical index question

## Source

- Paper: Antonio Perez-Hernandez, *Lipschitz vs Linear Numerical Index in certain Banach spaces*
- arXiv: `2507.18208`
- Local source PDF: `source_paper.pdf`

## Classification

- Status: `partial`
- Target question: the real Banach-space conjecture/question asking whether
  `n_L(X)=n(X)` for every real Banach space.
- Packet claim: if `{X_gamma}` is any family of real Banach spaces satisfying
  `n_L(X_gamma)=n(X_gamma)` for every `gamma`, then the same equality holds
  for their `c0`-, `ell_1`-, and `ell_infty`-sums. In particular, it holds
  for arbitrary such sums of real separable spaces, and for arbitrary such
  sums of real dual spaces.

## Relation to existing run packets

This extends the earlier packet
`solutions/partial/2507.18208_c0_sum_lipschitz_numerical_index/`, which proved
the `c0`-sum of separable spaces case by direct coordinate reduction. The
present packet also covers `ell_1` and `ell_infty` sums, and allows summands
from any known equality class, including real dual spaces.

It is still not a full solution of the arbitrary real Banach-space question.

## Inputs

- Perez-Hernandez arXiv:2507.18208: `n_L(Y)=n(Y)` for every real separable
  Banach space and for every real dual Banach space.
- Wang--Huang--Tan, JMAA 2014 / arXiv:1211.5753: the Lipschitz numerical
  index of a `c0`-, `ell_1`-, or `ell_infty`-sum is the infimum of the
  Lipschitz numerical indices of the summands.
- Classical numerical-index formula: for `c0`-, `ell_1`-, and `ell_infty`
  sums, `n` is the infimum of the summand numerical indices.

## Files

- `main.tex`: LaTeX source for the packet.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: original source paper.
- `figures/open_question_page2_crop.png`: crop showing the central equality question.
- `figures/real_case_conjecture_page3_crop.png`: crop showing the real-case conjecture.
- `figures/separable_theorem_page4_crop.png`: crop showing the separable theorem used as a summand input.
- `tmp/`: LaTeX build output.

## Verification notes

The proof is a three-line combination once the external formulas are accepted:

```text
n_L(sum) = inf_gamma n_L(X_gamma)
         = inf_gamma n(X_gamma)
         = n(sum).
```

The main verifier focus is not algebraic but bibliographic: check that the
stability formulas are exactly for arbitrary families under the three sum
norms, and that the packet is not overstating the result beyond those sums.
