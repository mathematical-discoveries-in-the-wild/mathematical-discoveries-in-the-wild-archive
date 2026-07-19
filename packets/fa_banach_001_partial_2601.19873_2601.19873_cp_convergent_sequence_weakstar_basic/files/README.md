# Weak-Star Basic Sequences In `C_p(K)'`: Exact Reduction

Run: `fa_banach_001`  
Source: arXiv:2601.19873, Jerzy Kakol, Manuel Lopez-Pellicer, Wieslaw Sliwa, "On weak*-basic sequences in duals and biduals of spaces C(X) and Quojections"  
Source target: Problem 12  
Upgrade processed: `2026-06-22`

Status: `stronger_partial_result (Problem 12 reduced exactly to the infinite-dimensional metrizable quotient problem for C_p(K); convergent-sequence, non-Efimov, and fsJNP positive regions recorded)`

## Classification

This is a stronger partial/reduction packet, not a full solution.

Problem 12 asks whether `C_p(K)'` admits a weak-star basic sequence for every infinite compact space `K`. The upgraded packet proves that this is equivalent to the older problem of whether `C_p(K)` has an infinite-dimensional metrizable quotient. That reduction is exact, and the same equivalence is recorded for arbitrary infinite Tychonoff spaces.

The full compact-space question remains open here because the metrizable-quotient problem remains open in the remaining separable Efimov region.

## Upgraded Claim

For every infinite compact Hausdorff space `K`, the following are equivalent:

- `C_p(K)'` contains a weak-star basic sequence;
- `C_p(K)` has an infinite-dimensional metrizable quotient;
- `C_p(K)` has an infinite-dimensional metrizable quotient with a Schauder basis;
- `C_p(K)'` contains an infinite-dimensional weak-star closed linear subspace of countable Hamel dimension.

Consequences:

- positive for compacta with a nontrivial convergent sequence;
- positive for compacta containing a copy of `beta N`;
- positive for compacta with the finitely supported Josefson-Nissenzweig property;
- any counterexample must be an Efimov compactum with no infinite-dimensional metrizable `C_p(K)` quotient.

## What Changed

The previous active packet proved only the explicit convergent-sequence subcase using

```text
mu_n = delta_{x_n} - delta_x.
```

The supplied report keeps that proof, but adds the exact reduction to metrizable quotients, a sequential norm-rigidity lemma in the no-fsJNP case, transfer/restriction principles, and the non-Efimov/fsJNP positive regions.

## Evidence And History

- `evidence/supplied_report_2026_06_22_cp_weakstar_basic/`: supplied TeX/PDF report.
- `history/previous_packet_2026_06_22_before_metrizable_quotient_reduction/`: previous active README, TeX, PDF, and ledger snapshot.

The duplicate check found the existing active packet and registry row, but those only recorded the convergent-sequence subcase and novelty caveat. They did not record the exact metrizable-quotient equivalence, so the upgrade was incorporated.

## Files

- `main.tex`: upgraded packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_problem_crop.png`: source crop showing Problem 12.

## Human Review Focus

1. Check the reverse implication from weak-star basic sequence to metrizable quotient, especially the use of fsJNP versus no-fsJNP norm rigidity.
2. Check that closure is always taken in the relative dual `Delta(K)=C_p(K)'`, not in the full Banach dual `C(K)^*`.
3. Verify the quotient-topology lemma for weak spaces and its countable-Hamel-dimension criterion.
4. Keep the final status as a reduction: the compact-space problem is equivalent to the metrizable-quotient problem, not solved outright.
