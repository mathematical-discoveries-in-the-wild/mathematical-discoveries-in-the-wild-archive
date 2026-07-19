# Strong partial packet: endpoint \(L^1\) inequality in nilpotency step two

Status: `strong_partial_step_two_complete_likely_valid`

Source paper: Seung-Yeon Ryoo, "Quantitative nonembeddability of groups of polynomial growth into uniformly convex spaces", arXiv:2207.11305.

Open question targeted: Questions 38/42 and Conjecture 43 ask for finite exponents in the endpoint \(L^1\) vertical-horizontal inequality for nonabelian nilpotent Lie groups.

## Current Result

The active packet verifies the previous Carnot-only proof and strengthens it:

- the subgroup \(H=\exp(\operatorname{span}\{a,b,[a,b]\})\) is closed because the exponential map of a simply connected nilpotent group is a diffeomorphism;
- Weil disintegration applies because \(H\) is closed and both \(G\) and \(H\) are unimodular;
- the Carnot grading assumption is unnecessary;
- every connected, simply connected, step-two nilpotent Lie group with any bracket-generating left-invariant Carnot--Caratheodory structure satisfies the endpoint inequality with \(q=4\) in every commutator direction;
- the constant is quantified by the commutator factorization gauge \(\kappa_W(z)\);
- all \(q\ge4\) follow by interpolation with the deterministic path bound.

Thus Ryoo's question is completely resolved in nilpotency step two. The packet also records the known sharper \(q=2\) transfer criterion through higher-dimensional Heisenberg subgroups.

## Why This Is Still Partial

This does not solve the higher-step endpoint problem. The packet isolates the obstruction: in higher step, a top-layer vector \(v=[a,w]\) may generate a Heisenberg subgroup with \(a\), \(w\), and \(v\), but the resulting estimate contains the derivative \(wf\), where \(w\) is nonhorizontal and not controlled directly by \(\int |\nabla_W f|\).

## Files

- `main.tex`: active verified proof packet.
- `solution_packet.pdf`: rendered active packet.
- `source_paper.pdf`: local copy of arXiv:2207.11305.
- `supporting_paper_2004.12522.pdf`: Naor--Young supporting theorem.
- `figures/open_problem_crop.png`: crop of the source question.
- `figures/supporting_h3_theorem_crop.png`: crop of the supporting Heisenberg theorem.
- `history/previous_carnot_packet_2026_06_18/`: previous active Carnot-only packet.
- `evidence/supplied_verified_note_2026_06_18/`: supplied verification/strengthening note.

## Human Review Recommendation

Review as a likely valid strong partial theorem. The key checks are the Heisenberg coset transfer, the \(\kappa_W\) homogeneity/balancing, the deterministic \(q=\infty\) path bound, and the stated obstruction to iterating the proof in higher step.
