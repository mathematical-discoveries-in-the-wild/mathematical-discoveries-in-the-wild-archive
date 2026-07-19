# Strong partial packet: endpoint \(L^1\) inequalities, step two and Cartan reductions

Status: `strong_partial_step_two_complete_cartan_reduction_likely_valid`

Source paper: Seung-Yeon Ryoo, "Quantitative nonembeddability of groups of polynomial growth into uniformly convex spaces", arXiv:2207.11305.

Open question targeted: Questions 38/42 and Conjecture 43 ask for finite exponents in the endpoint \(L^1\) vertical-horizontal inequality for nonabelian nilpotent Lie groups.

## Current Result

The active packet supersedes the previous step-two-only packet and records the
strongest current partial progress:

- the complete nilpotency-step-two theorem remains proved: every connected,
  simply connected, step-two nilpotent Lie group with any bracket-generating
  left-invariant Carnot--Caratheodory structure satisfies the endpoint inequality
  with \(q=4\) in every commutator direction;
- the constant is quantified by the commutator factorization gauge \(\kappa_W(z)\);
- strong and weak Lorentz mixed-bracket propagation are proved;
- finite weak scale exponents are shown to imply all larger strong exponents;
- the entire step-three problem is reduced to one weak estimate on the
  five-dimensional Cartan group;
- a noncentral weak Cartan seed would imply all strong step-three exponents above
  the propagated threshold;
- a rank-two weak seed on the free group \(F_{2,s}\) would propagate to arbitrary
  step;
- unconditional higher-step examples are recorded, including upper unitriangular
  groups.

Thus Ryoo's question is completely resolved in nilpotency step two and reduced to
very explicit weak-type targets in step three and beyond. The packet also records the
known sharper \(q=2\) transfer criterion through higher-dimensional Heisenberg
subgroups.

## Why This Is Still Partial

This does not solve the higher-step endpoint problem. The remaining universal
step-three target is a finite weak-type estimate for one top-layer direction on the
Cartan group. The packet explains why plain quotient lifting and Heisenberg slicing
do not close this estimate: they introduce nonhorizontal derivatives or require
multiscale cancellation that is not presently proved.

## Files

- `main.tex`: active verified proof packet.
- `solution_packet.pdf`: rendered active packet.
- `source_paper.pdf`: local copy of arXiv:2207.11305.
- `supporting_paper_2004.12522.pdf`: Naor--Young supporting theorem.
- `figures/open_problem_crop.png`: crop of the source question.
- `figures/supporting_h3_theorem_crop.png`: crop of the supporting Heisenberg theorem.
- `history/previous_carnot_packet_2026_06_18/`: previous Carnot-only packet.
- `history/previous_step_two_packet_2026_06_19/`: previous active step-two packet.
- `evidence/supplied_verified_note_2026_06_18/`: supplied step-two verification note.
- `evidence/supplied_final_endpoint_progress_2026_06_19/`: supplied stronger
  progress note now used as the active packet.

## Human Review Recommendation

Review as a likely valid strong partial theorem. The key checks are the Heisenberg
coset transfer, the \(\kappa_W\) homogeneity/balancing, the deterministic
\(q=\infty\) path bound, the Lorentz mixed-bracket propagation proof, the
weak-to-strong upgrade, the Cartan reduction, and the barrier analysis explaining why
the remaining weak Cartan estimate is still open.
