# H-infinity Calculus Angle Equality: Literature-Implied Negative Answer

Status: `literature_implied_answer`

Source paper: N. J. Kalton and L. Weis, `The H^{infinity}-calculus and sums of
closed operators`, arXiv:math/0010155.

Supporting paper: N. J. Kalton, E. Lorist, and L. Weis, `Euclidean structures
and operator theory in Banach spaces`, arXiv:1912.09347.

## Source Question

In Section 4 of arXiv:math/0010155, after defining the sectorial angle
`omega(A)` and the bounded `H^infinity`-calculus angle `omega_H(A)`, Kalton and
Weis write:

> It is an open problem (cf. CDMY) whether `omega_H(A)=omega(A)` whenever `A`
> is `H^infinity`-sectorial.

This appears on page 16 of `source_paper.pdf`.

## Supporting Answer

The later paper arXiv:1912.09347 gives a negative answer after translating
notation. In Section 6.4 it records that counterexamples to
`omega_{H^infinity}(A)=omega(A)` were already known, and Theorem 6.4.4 gives a
particularly strong family: for every `p in (1,infinity) \\ {2}` and every
`sigma in (0,pi)`, there is a closed subspace `Y` of `L^p([0,1])` and a
sectorial operator `A` on `Y` such that `A` has a bounded `H^infinity`-calculus
and

```text
omega(A)=0,   omega_{H^infinity}(A)=sigma.
```

Thus the equality asked about in the 2000 paper fails, even on closed subspaces
of classical `L^p` spaces.

## Provenance

This is not an original lane result. The relation is agent-identified rather
than explicitly advertised as an answer to arXiv:math/0010155: the supporting
paper cites the older CDMY/Kalton counterexample lineage and gives a stronger
modern construction, but it does not present itself as resolving the exact
Kalton-Weis sentence from the source paper.

## Files

- `source_paper.pdf`: arXiv:math/0010155.
- `supporting_paper_1912.09347.pdf`: arXiv:1912.09347.
- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `tmp/`: LaTeX build intermediates.

## Scope

The packet only records the negative answer to the angle-equality question
`omega_H(A)=omega(A)` for all `H^infinity`-sectorial operators. It does not
claim novelty, and it does not address unrelated open problems in functional
calculus or maximal regularity.
