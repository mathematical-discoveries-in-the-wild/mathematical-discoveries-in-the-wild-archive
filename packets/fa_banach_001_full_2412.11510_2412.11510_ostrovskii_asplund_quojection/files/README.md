# Full positive answer to the final quojection problem of arXiv:2412.11510

Status: claimed full solution, likely valid, for human review.

## Result

Kakol--Leiderman's final quojection problem asks whether there exists a
quojection Frechet lcs `E` which is Asplund, is not a countable product of
Banach spaces, and contains no infinite-dimensional Banach subspaces.

The answer is yes:

> Ostrovskii's original "very twisted" quojection can be chosen so that every
> Banach level in the defining projective spectrum is Asplund. Consequently the
> resulting quojection is Asplund by Kakol--Leiderman's quojection criterion.

## Packet contents

- `main.tex` and `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: Kakol--Leiderman, arXiv:2412.11510.
- `supporting_paper_ostrovskii_9403209.pdf`: Ostrovskii, arXiv:math/9403209.
- `supporting_source_ostrovskii_9403209.tex`: TeX source used to inspect the
  construction.

## Proof summary

Ostrovskii constructs a projective sequence `(F_n, R_n)` such that the maps
`R_n:F_{n+1}->F_n` are quotient maps and the Banach spaces `F_j,F_k` have no
common infinite-dimensional subspace when `j != k`. Metafune--Moscatelli's
criterion then gives a twisted quojection with no infinite-dimensional Banach
subspaces.

The source paper observes that the same criterion would solve its Problem 4.6
if the `F_n` were Asplund. They are. Start with `F_1=ell_{q_1}`. Recursively,
`F_n=X**`, where `X` is a Bellenot--James `J(q_n,F_{n-1})` space and
`X**/X` is isometric to `F_{n-1}`. If `F_{n-1}` is separable Asplund, then
`X` and `X**/X` are separable, so `X**` is separable. Hence `X*` is separable,
so `X` is Asplund. Since Asplund Banach spaces are closed under extensions,
`X**` is Asplund. This induction makes every `F_n` Asplund.

Kakol--Leiderman's Theorem 4.2 says that a quojection is Asplund iff all its
defining Banach spaces are Asplund. Therefore Ostrovskii's quojection is the
desired positive example.

## Novelty check

Local run indexes were searched for `2412.11510`, the title, `Asplund spaces`,
`finest locally convex`, `quojection`, `Ostrovskii`, and the exact final
problem phrase. No existing packet or attempt for this target was found.

Web/literature searches on 2026-06-19 for the source title, the final
quojection problem, and Ostrovskii's "Quojections without Banach subspaces"
found the source paper and Ostrovskii's construction, but no explicit published
answer to the Asplund-strengthened problem.

## Human review recommendation

Review the induction proving the Ostrovskii Banach levels are Asplund. The key
standard facts used are: separability is a three-space property for Banach
spaces; if a dual Banach space is separable then its predual is separable; and
the class of Asplund Banach spaces is closed under extensions.
