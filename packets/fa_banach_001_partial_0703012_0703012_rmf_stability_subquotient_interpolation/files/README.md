# RMF stability and quantitative partial progress

Status: `candidate_partial_likely_valid`.

Source paper: Tuomas Hytonen, Alan McIntosh, and Pierre Portal, *Kato's square
root problem in Banach spaces*, arXiv:math/0703012.

Extracted question: after defining the Rademacher maximal function property
(RMF), the source asks whether every UMD Banach space has RMF. A positive
answer would remove the extra RMF hypothesis from the Banach-valued Kato
square-root theorem.

Strengthened packet result: the full UMD-to-RMF problem remains open, but the
active packet now records a stronger partial landscape:

- RMF is preserved by closed subspaces, quotients, and complex interpolation,
  with the quotient and interpolation arguments repaired explicitly.
- RMF is preserved by Bochner `L^q` formation and by finite representability
  with uniform constants.
- The full UMD-to-RMF question is equivalent to a quantitative
  finite-dimensional uniformity problem for UMD constants versus RMF constants.
- Every UMD space has truncated RMF constants growing at most like `N^delta`
  for some `delta < 1/2`.
- A type/martingale-cotype criterion gives RMF under the condition
  `q_0 < 2t/(2-t)`.

What remains open: the packet does not prove that every UMD space has RMF and
does not construct a UMD counterexample. The main remaining obstruction is the
anticipative nature of the pointwise RMF supremum: the optimizing coefficient
vector may depend on the terminal sample point, outside the predictable scope
of the usual UMD Stein/martingale-transform inequalities.

Evidence and history:

- `evidence/supplied_umd_rmf_final_attempt_2026_06_22/`: supplied TeX/PDF
  reports.
- `history/previous_stability_packet_2026_06_14/`: earlier partial packet.

Files:

- `main.tex` / `solution_packet.pdf`: consolidated strengthened partial packet.
- `source_paper.pdf`: local copy of arXiv:math/0703012.
- `figures/open_problem_crop.png`: crop of the source open-question paragraph
  from PDF page 8.

Human-review focus: check the Bochner quotient lifting lemma, the one-sided
Rademacher interpolation embedding, the finite-representability/locality
argument, and the type/variation route to the RMF sufficient criterion.
