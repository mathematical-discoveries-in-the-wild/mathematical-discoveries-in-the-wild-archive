# Conditional Packet: WC Cutoffs and the Summable-Fusion Reduction

Status: `conditional_summable_fusion_reduction`

Run: `fa_banach_001`

Source problem: Beanland--Causey--Freeman--Wallis, arXiv:1507.06285,
Question 9.3.

## Source Question

Question 9.3 asks for which ordinals `xi` the fixed cutoff class

```text
{ A : X -> Y : WC(A,X,Y) <= xi }
```

is an operator ideal, where `WC` is the weak-compactness tree index built
from domination of the summing basis of `c_0`.

## Current Status

This is not a full solution. The upgraded packet records the strongest
conditional state from the supplied report:

- all finite cutoffs are already settled by the separate finite-rank packet;
- the source paper proves that `WC <= omega` is the super weakly compact
  ideal and that `WC < omega_1` is an ideal;
- successor levels fail whenever an operator realizes the exact successor
  `WC` value;
- the natural positive candidate levels are `omega^{omega^eta}`;
- at those levels, ideality follows from the explicit tree-Ramsey
  `summable fusion` property `SF(lambda)`.

The remaining gap is combinatorial, not an analytic Banach-space estimate:
the literature supplies fixed-mesh pair stabilization at the relevant
ordinals, but the proof needs rank-preserving stabilization with a
prescribed summable sequence of errors.

## What This Upgrade Adds

Compared with the previous conditional packet, this upgrade adds:

- exact triangular-array characterization of finite `WC` nodes;
- a sharp summable-error perturbation lemma;
- an explicit finite-dimensional obstruction showing fixed mesh is not
  enough;
- a difference-sequence reformulation and convex-block stability;
- direct-sum ordinal lower bounds and a successor-level nonideality
  criterion;
- uniform finite localization and finite splitting principles;
- the summable-fusion property `SF(lambda)`;
- a conditional theorem: if `SF(lambda)` holds, then
  `{A : WC(A) <= lambda}` is an operator ideal.

The previous James-to-wide-(s) bridge is preserved as an alternative
possible completion route, but it is no longer the only or main dependency.

## Files

- `main.tex`: upgraded conditional packet source.
- `solution_packet.pdf`: compiled packet.
- `source_paper.pdf`: local copy of arXiv:1507.06285.
- `supporting_paper_1508.02065.pdf`: Causey's James-index paper.
- `supporting_paper_math_9610209.pdf`: Rosenthal's wide-(s) paper.
- `figures/open_problem_crop.png`: crop of the source WC definition.
- `figures/question_crop.png`: crop of Question 9.3 from the source.
- `evidence/supplied_wc_index_full_push_2026_06_22/`: supplied report.
- `history/previous_james_bridge_packet_2026_06_22/`: previous active
  conditional packet.

## Human Review

Recommended checks:

- verify the exact triangular criterion and summable-error lemma;
- verify the fixed-error obstruction really blocks fixed-mesh arguments;
- verify that the proof of the conditional ideal theorem uses only
  `SF(lambda)` as an unproved dependency;
- compare the stated pair-Ramsey/fixed-mesh input with Causey--Doebele and
  Causey's extended-pair stabilization.
