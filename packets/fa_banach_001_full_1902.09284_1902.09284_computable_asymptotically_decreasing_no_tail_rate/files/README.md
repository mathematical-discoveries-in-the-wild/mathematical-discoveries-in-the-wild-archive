# A computable asymptotically decreasing sequence with no computable tail rate

Status: `candidate_full_solution_likely_valid`

This packet answers the computability conjecture in footnote 2 of Thomas
Powell, *A new metastable convergence criterion and an application in the
theory of uniformly convex Banach spaces*, arXiv:1902.09284, PDF pages 4--5.

Powell asks whether the example immediately preceding the footnote can be
strengthened so that the sequence itself is computable. The answer is yes.
Fix an effective enumeration of Turing machines. Put a rational spike of
height `2^{-e}` at a computably scheduled stage if and when machine `e`
halts, and put zero otherwise. The resulting uniformly computable rational
sequence converges to its infimum zero, hence is asymptotically decreasing.
If a computable function `phi(epsilon,N)` always returned a witness for the
full-tail condition (5), then `phi(2^{-(e+1)},0)` would decide whether machine
`e` ever halts.

The scope is exact but narrow. The result concerns the full-tail witness
`phi(epsilon,N)` described immediately before the footnote. It does not claim
noncomputability of the later finite-window functional
`Gamma(epsilon,g,N)` in equation (6).

Files:

- `solution_packet.pdf`: review packet.
- `main.tex`: packet source.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_context.png`, `figures/open_problem_continuation.png`,
  and `figures/open_problem_footnote.png`: source evidence from PDF pages 4--5.
- `code/crop_source.py`: reproducible crop script.

Human review should focus on the intended computability convention in the
footnote and the distinction between the full-tail witness and finite-window
metastability. Exact-phrase and close-variant searches performed on
2026-07-19 found no later answer; the halting-spike construction itself is a
standard computability mechanism, so the novelty claim is intentionally
conservative.
