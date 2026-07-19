# Superseded Partial Packet: Non-Fin Ideals Obstruct the Tensor Isometry

This packet is superseded by the full classification packet:

`runs/fa_banach_001/solutions/full/2309.08076_tensor_canonical_onto_classification/`

The partial statement here missed the finite-dimensional positive exception.
The corrected full theorem is: the source's canonical map
`c_{0,I} \hat\otimes_\varepsilon X -> c_{0,I}(X)` is onto if and only if
`I = Fin` or `X` is finite-dimensional.

- status: candidate partial result, likely valid
- run: `fa_banach_001`
- source arXiv id: `2309.08076`
- source paper: Michael A. Rincon-Villamizar and Carlos Uzcategui Aylwin,
  *Banach spaces of I-convergent sequences*
- target passage: PDF page 13, Question 5.12, asking for which ideals `I`
  the source's injective-tensor isometry
  `c_{0,I} \hat\otimes_\varepsilon X -> c_{0,I}(X)` is onto.

## Claim

Let `X` be a Banach space containing no complemented copy of `c_0`. Then the
canonical isometry

```text
c_{0,I} \hat\otimes_\varepsilon X -> c_{0,I}(X)
```

is onto if and only if `I = Fin`.

In particular, for `X = ell_2`, Question 5.12 has the exact answer: only the
Frechet ideal `Fin` works.

## Mechanism

If `I != Fin`, choose an infinite set `A in I`. Then `I|A = P(A)`, so the
restriction coordinates are an `ell_infty(A)` block. If the global canonical
tensor map were onto, coordinate projection would force the canonical map
`ell_infty(A) \hat\otimes_\varepsilon X -> ell_infty(A,X)` to be onto. By
the Leung--Rabiger obstruction quoted in the source paper, that implies `X`
contains a complemented copy of `c_0`, contradiction.

## Files

- `main.tex`: full partial-result packet
- `solution_packet.pdf`: rendered packet
- `source_paper.pdf`: local copy of arXiv:2309.08076
- `figures/open_problem_crop.png`: crop of Question 5.12

## Novelty Check

Local index searches for `2309.08076`, `injective tensor`,
`c_{0,\mathcal I}`, `Leung`, and `c_{0,I}(X)` found only the distinct
`c_{0,WO}` Grothendieck packet for this arXiv id and no duplicate of this
tensor-product target.

Bounded web searches on 2026-06-29 for exact phrases from Question 5.12 and
the source title with `injective tensor` found no explicit later answer.

Human review should focus on whether Question 5.12 is being read as the
source's canonical isometry being onto, as indicated by Remark 5.11.
