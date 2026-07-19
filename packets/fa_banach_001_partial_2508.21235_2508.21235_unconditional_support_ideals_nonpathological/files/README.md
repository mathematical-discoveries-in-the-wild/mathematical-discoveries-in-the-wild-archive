# Critical Ideals of Ideal Schauder Systems: Stronger Partial Package

Status: `strong_partial_reduction_likely_valid`

Source paper: Adam Kwela and Jaroslaw Swaczyna, *Zoo of ideal Schauder bases*, arXiv:2508.21235.

Open question: Question 11.2 asks whether every analytic `P`-ideal can be represented as a critical ideal `CR(X,a)` for some Banach space `X` and biorthogonal system `a`.

## Current Packet

The active packet is a strengthened partial result and reduction package. It does not solve Question 11.2.

It contains:

- A repaired proof of the previous unconditional-support obstruction: ideals of positive weighted subseries over an unconditional basis are non-pathological.
- The observation that this unconditional-support theorem is subsumed by the Borodulin-Nadzieja-Farkas-Plebanek characterization of Banach-representable ideals.
- A residual-projection reformulation using `R_n = I - S_n`.
- An exact statistical strong-operator/Katetov criterion for non-pathology.
- A regular-matrix averaging formulation.
- A bounded-positive-subset criterion: if every positive set contains a positive subset on which `||R_n||` is bounded, then the critical ideal is non-pathological.
- A rapid-plus dual-filter corollary using the filter-dependent uniform boundedness theorem.
- A necessary reciprocal-norm divergence condition on every positive set.

## Main Remaining Obstruction

The unresolved core is a statistical strong-operator selection problem for an unbounded nested family of residual projections:

```text
R_n R_m = R_max(n,m).
```

An affirmative selection theorem would imply that every analytic `P`-ideal critical ideal is non-pathological, hence pathological analytic `P`-ideals could not answer Question 11.2 positively. A realization of a pathological analytic `P`-ideal would conversely produce a counterexample to this selection principle.

## Files

- `main.tex`: active strengthened partial/reduction packet.
- `solution_packet.pdf`: rendered active packet.
- `source_paper.pdf`: local copy of arXiv:2508.21235.
- `figures/open_problem_crop.png`: full-width crop of Question 11.2.
- `code/make_open_problem_crop.py`: reproducible crop script from the previous packet.
- `history/previous_unconditional_support_packet_2026_06_19/`: previous active partial packet.
- `evidence/supplied_critical_ideals_best_result_2026_06_19/`: supplied external TeX/PDF note used for this strengthened version.

## Human Review Focus

The unconditional-support theorem is now presented as a repaired and contextualized special case, not as a new characterization. The main review burden is on the operator-theoretic reductions: the Katetov/statistical SOT equivalence, the regular-matrix averaging step, the rapid-plus uniform-boundedness corollary, and the Kadets-Manskova reciprocal-norm translation.

