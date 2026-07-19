# Sigma-Compact AM-Space Persistence Under Nonlinear Order Isomorphisms

Result type: `partial`

Status: candidate partial result, likely valid pending human review.

## Source

- Denny H. Leung and Wee-Kee Tang, *Persistence of Banach lattices under
  nonlinear order isomorphisms*, arXiv:1507.02759.
- Source question: introduction after Theorem 1, page 2.
- Local source PDF: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

## Exact Target

The paper asks whether every Banach lattice that is nonlinearly order
isomorphic to an AM-space must be linearly lattice isomorphic to an AM-space.

The source proves this when the target AM-space is a closed ideal in `C(K)`
with `C(K)` separable. This packet extends the same positive conclusion to
AM-spaces of the form `C_0(L)` for locally compact sigma-compact `L`.

## Claimed Partial Result

Let `L` be locally compact Hausdorff and sigma-compact. If a Banach lattice
`E` is order isomorphic to `C_0(L)`, then `E` is lattice isomorphic to an
AM-space.

Equivalently, the source question has an affirmative answer for all
sigma-compact locally compact AM-space targets.

## Proof Summary

Use the Cartwright-Lotz criterion: a Banach lattice is lattice isomorphic to
an AM-space iff every disjoint norm-null sequence is order bounded in the
bidual.

Let `T:E -> C_0(L)` be an order isomorphism with `T0=0`. For a disjoint
norm-null sequence `(x_n)` in `E`, the functions `f_n=T|x_n|` are disjoint
positive functions in `C_0(L)`.

The usual summable-subsequence argument from the source shows `(f_n)` is
bounded. A second summable-subsequence argument shows the family `(f_n)` is
uniformly vanishing at infinity. Since `L` is sigma-compact, choose a compact
exhaustion `K_n` and build a positive `h in C_0(L)` that is large on `K_1`
and decays on each annulus `K_n \ K_{n-1}`. This `h` dominates every `f_n`.
Then `T^{-1}h` order-bounds `|x_n|` in `E`, so Cartwright-Lotz applies.

## Novelty Check

Cheap run indexes were searched for `1507.02759`, the source title, nonlinear
order isomorphism, AM-space, and sigma-compact terms. No exact duplicate packet
was found. Bounded web searches for the exact source question and
`order isomorphic AM-space sigma-compact` found the source arXiv page but no
later direct answer to this subcase.

## Limitations

This does not solve the full AM-space question. The proof uses sigma-compactness
to construct a single `C_0` envelope for the image of each disjoint norm-null
sequence. The arbitrary locally compact, non-sigma-compact case remains open
in this packet.

## Human Review Notes

Check the envelope lemma for bounded disjoint families in `C_0(L)` that are
uniformly vanishing at infinity, and the use of Cartwright-Lotz. The result
order-bounds the tested sequence in `E` itself, which is stronger than the
bidual order-bound required by the criterion.
