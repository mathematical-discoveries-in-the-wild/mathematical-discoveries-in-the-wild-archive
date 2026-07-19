# Conditional Reduction: Schur Tensor Counterexample Implies `CC o L < L_msc`

Status: `conditional_reduction_likely_valid`

Source problem paper: G. Botelho and E. R. Torres, *Hyper-ideals of
multilinear operators*, arXiv:1504.00520.

Supporting status source: J. Rodriguez, *On weak compactness in projective
tensor products*, arXiv:2206.08651.

## Target

The source paper introduces the closed hyper-ideal `L_msc` of multilinearly
sequentially continuous multilinear operators and proves
`CC o L subset L_msc`, where `CC` is the ideal of completely continuous
linear operators and `CC o L` is the associated composition hyper-ideal.

Open Question 2 asks whether this inclusion is proper:

```text
We conjecture that CC o L subsetneqq L_msc.
```

The same source explains that a positive answer to the equality
`CC o L = L_msc` would be expected to imply a positive answer to the
long-standing Schur-property question for projective tensor products.

## Conditional Result

If there are Schur Banach spaces `E_1,...,E_n`, `n >= 2`, such that

```text
E_1 \widehat{\otimes}_pi ... \widehat{\otimes}_pi E_n
```

does not have the Schur property, then Open Question 2 has an affirmative
answer:

```text
CC o L subsetneqq L_msc.
```

The separating operator is the canonical tensor map

```text
sigma:E_1 x ... x E_n -> E_1 \widehat{\otimes}_pi ... \widehat{\otimes}_pi E_n,
sigma(x_1,...,x_n)=x_1 \otimes ... \otimes x_n.
```

It belongs to `L_msc`, but not to `CC o L`.

## Conditional Dependencies

The only unproved external dependency is the existence of a negative example
to the Schur-property preservation problem for projective tensor products:
Schur spaces whose projective tensor product fails Schur.

This dependency is not currently claimed as solved here. Rodriguez
arXiv:2206.08651 still describes preservation of the Schur property by
projective tensor products as an open problem. The conditional packet records
the exact implication from such a future or known counterexample to the
hyper-ideal conjecture.

## Proof Summary

For a multilinear operator `A:E_1 x ... x E_n -> F`, membership in
`CC o L` is equivalent to complete continuity of its linearization
`\widetilde A` on the projective tensor product. One direction follows from
factoring `A=u o B` with `u` completely continuous; the other follows from
`A=\widetilde A o sigma`.

If all `E_i` have the Schur property, then any weakly convergent sequence of
elementary tensors in the projective tensor product converges in projective
norm. The zero-limit case is proved by normalizing the factors and using the
Schur property to select functionals on successive subsequences; the nonzero
case is reduced to the zero-limit case by decomposing around rank-one
projections onto the limit factors.

Therefore the canonical tensor map `sigma` is multilinearly sequentially
continuous. But its linearization is the identity on the projective tensor
product. If that tensor product lacks the Schur property, the identity is not
completely continuous. Hence `sigma` is in `L_msc` but not in `CC o L`.

## Evidence

- `source_paper.pdf`: local copy of arXiv:1504.00520.
- `figures/open_problem_crop.png`: crop of Open Question 2 in the source PDF.
- `supporting_paper_2206.08651.pdf`: local copy of arXiv:2206.08651, whose
  introduction records that Schur preservation under projective tensor
  products still appears open as of 2022.
- `solution_packet.pdf`: full conditional proof note built from `main.tex`.

## Search Bounds

Before promotion, cheap run indexes were searched for `1504.00520`,
`hyper-ideals`, `multilinearly sequentially continuous`, `CC o L`, and
projective tensor Schur phrases. No prior packet or attempt for this exact
conditional reduction was found.

Local parsed arXiv sources were searched for `Schur property` with
`projective tensor`, `multilinearly sequentially continuous`, and related
Botelho--Rueda/Gonzalez--Gutierrez phrases. The 2022 Rodriguez paper records
the Schur projective-tensor problem as open. A bounded web search on
2026-06-16 for the same phrases did not identify a later exact solution.

## Human Review Notes

Recommended review focus:

- Verify the lemma that elementary tensors over Schur factors are
  Schur-sequential inside the projective tensor product.
- Verify the equivalence `A in CC o L` iff the projective-tensor
  linearization of `A` is completely continuous.
- Treat the result strictly as conditional: it becomes a full answer to Open
  Question 2 only after a negative Schur tensor-product example is available.
