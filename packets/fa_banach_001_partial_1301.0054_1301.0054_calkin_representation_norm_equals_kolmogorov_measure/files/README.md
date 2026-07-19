# Partial Packet: Exact Norm of the BCAP-Free Calkin Representation

- status: candidate partial result, likely valid
- run: `fa_banach_001`
- source arXiv id: `1301.0054`
- source paper: March T. Boedihardjo and William B. Johnson, *On Mean Ergodic Convergence in the Calkin Algebras*
- target: Remark 1 after Theorem 2.1 asks whether the theorem is true without assuming that `X` has the BCAP.

## Claim

For every infinite-dimensional Banach space `X` and every `T in B(X)`, the
Boedihardjo--Johnson ultrapower representation satisfies

```text
||hat T|| = inf_E ||Q_E T||,
```

where `E` ranges over finite-dimensional subspaces of `X` and
`Q_E : X -> X/E` is the quotient map.

Thus the representation is exactly isometric for the Kolmogorov
noncompactness seminorm on operators. In particular it is injective modulo
compact operators for every Banach space, recovering and sharpening the prior
lane-5 partial packet.

## Scope

This is still a partial result for the original question. It does not prove
that the representation is bounded below for the essential norm without BCAP.
Instead, it gives the sharp reduction:

```text
Theorem 2.1 without BCAP is equivalent to a uniform estimate
||T||_e <= C_X inf_E ||Q_E T||
for all T in B(X).
```

The `L_p(0,1)` isometry question in Remark 2 becomes the special question
whether `||T||_e = inf_E ||Q_E T||` for all operators on that `L_p` space.

## Files

- `main.tex`: proof packet
- `solution_packet.pdf`: rendered packet
- `source_paper.pdf`: local copy of arXiv:1301.0054
- `figures/theorem_context_crop.png`: Theorem 2.1 and construction context
- `figures/open_problem_crop.png`: source remarks containing the open questions

## Verification

Human review should focus on the upper bound in the norm formula. The only
point to check is that if `(x_alpha^*)` has weak-star ultralimit zero, then for
each finite-dimensional `F subset X`, the restrictions `x_alpha^*|_F` converge
to zero in norm along the ultrafilter. This lets one perturb `x_alpha^*` by a
small amount into `F^\perp`, and then take the infimum over `F`.
