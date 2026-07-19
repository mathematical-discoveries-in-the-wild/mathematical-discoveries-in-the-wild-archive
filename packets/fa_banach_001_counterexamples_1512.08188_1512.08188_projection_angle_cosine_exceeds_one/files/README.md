# Counterexample packet: projection-angle cosine can exceed one

Status: likely valid counterexample, ready for human review.

Source target: Izhar Oppenheim, "Vanishing of cohomology with coefficients in representations on Banach spaces of groups acting on Buildings", arXiv:1512.08188v2.

The source defines a cosine for the angle between two Banach-space projections and remarks that it is unknown whether this quantity is always at most 1. The packet gives a two-dimensional Hilbert-space example with non-orthogonal projections for which the defined cosine is `sqrt(2)`. The same example also shows that the angle between the complementary projections need not be well defined, matching the paper's later warning about complement angles.

Main construction:

- Work on `R^2` with the Euclidean norm.
- Let `P_1(x,y)=(x,0)` and `P_2(x,y)=(x,x)`.
- Then `im(P_1) cap im(P_2)={0}`, so `P_{1,2}=0` is admissible.
- The source definition gives
  `cos(angle(P_1,P_2)) = max(||P_1 P_2||, ||P_2 P_1||) = sqrt(2) > 1`.

Files:

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of the source arXiv PDF.
- `figures/open_problem_crop.png`: crop of Remark 2.11.
- `figures/complement_angle_crop.png`: crop of Remark 3.11.
- `code/rank_two_projection_angle_check.py`: small numerical/algebraic check.
- `code/crop_source_remarks.py`: reproducible crop script.

Novelty check:

- Local lightweight indexes were searched for `1512.08188`, the paper title, `angle between projections`, `Friedrichs angle`, and related terms; no exact prior packet or attempt for this target was found.
- Bounded web searches on 2026-06-28 for exact phrases around `cos(angle(P_1,P_2)) <= 1`, Oppenheim projection angle cosine, and `1512.08188 angle between projections` found no separate literature answer beyond the arXiv source metadata.

Human-review recommendation: check that the source definition permits arbitrary bounded, non-orthogonal projections in Hilbert spaces. If yes, the counterexample is literal and requires no additional hypotheses.
