# Corrected partial for strongly Rosenthal compacta

Source: Glasner--Megrelishvili, *Representations of dynamical systems on
Banach spaces not containing ell_1*, arXiv:0803.2320.

Status: `corrected_partial_previous_claim_invalid`.

This packet replaces the previous active packet
`0803.2320_separable_strongly_rosenthal_admissible`. The previous packet
claimed a proof that every separable strongly Rosenthal compactum is
admissible. The audit found that proof invalid.

## Corrected Outcome

The original open question is not solved here. The active result is a corrected
partial:

- a compact metrizable example shows that a pointwise-convergent sequence in
  `B_1(X)` can still be equivalent, in supremum norm, to the `ell_1`
  unit-vector basis;
- the proposed graph-coordinate family need not be Rosenthal;
- the proposed quotient of the representing Banach space does not collapse
  fibers, and the annihilator calculation used the wrong closure;
- the valid replacement embeds the target compactum into
  `E^*`, where `E` is the norm-closed span of the graph evaluation functionals
  inside `V^*`;
- this does not prove admissibility, because it does not identify `E` as the
  dual of a separable Rosenthal Banach space.

## Files

- `main.tex`: corrected audit packet.
- `solution_packet.pdf`: compiled corrected packet.
- `source_paper.pdf`: local copy of arXiv:0803.2320.
- `figures/open_problem_crop.png`: source-paper screenshot of the relevant
  strongly Rosenthal/admissible question.
- `history/invalid_previous_packet_2026_06_18/`: previous active packet,
  preserved only as provenance and not to be cited as valid.
- `evidence/audit_verdict_2026_06_18.md`: user-supplied audit verdict used for
  this correction.

## Human Review Focus

Review the explicit `ell_1` pointwise-null example, the weak-star versus
norm-closure distinction in the annihilator identity, and the replacement
embedding into `E^*`. The key limitation is whether `E` can be represented as
the dual of a separable Rosenthal space; without that, Theorem 6.16 of the
source cannot be applied.
