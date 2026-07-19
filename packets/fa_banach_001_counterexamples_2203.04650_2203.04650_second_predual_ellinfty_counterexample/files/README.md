# Counterexample Packet: Second Predual Does Not Force Samples Into `U`

Run: `fa_banach_001`

Agent: `agent_lane_08`

Result type: `counterexample`

Status: likely valid, scoped negative answer.

## Source Problem

- Yury Korolev, Jonas Latz, Carola-Bibiane Schoenlieb, *Gaussian random fields
  on non-separable Banach spaces*, arXiv:2203.04650.
- Local PDF: `source_paper.pdf`.
- Extracted question: Outlook, "Second preduals", local build PDF page 14.
- Evidence crop: `figures/open_problem_crop.png`.

The paper asks whether, in cases where the Banach target `U` has a second
predual, one can strengthen the bounded-pairing / weak-star-completion
conclusions and prove that the Gaussian sample `theta` belongs to `U` with
probability one.

## Result

The second-predual hypothesis alone is not sufficient. For
`U = ell_infty = c_0^{**}` there is a positive nuclear covariance kernel
`c in U hat tensor_pi U` with summable eigenvalues such that all scalar
predual pairings are finite almost surely, but the formal Gaussian sample is
not an element of `U` almost surely.

The same obstruction transfers to every Banach space isomorphic to `ell_infty`.
In particular, it applies to the `Lip(X^alpha)` cases covered by the source
paper's Theorem 8.49 whenever that theorem identifies `Lip(X^alpha)` with
`ell_infty`.

## Main Files

- `main.tex`: formal proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source paper PDF, locally built from the arXiv source.
- `figures/open_problem_crop.png`: source question crop.
- `code/finite_subset_growth_demo.py`: simulation illustrating the finite-subset
  supremum mechanism.
- `tmp/`: LaTeX build intermediates.

## Scope Limits

This does not refute a more restrictive theorem for special covariance kernels
such as the exponential kernels studied later in the source paper. It refutes
the broad strengthening "second predual implies `theta in U`" for arbitrary
positive nuclear covariance kernels in the paper's Banach-space framework.

## Human Review Recommendation

Review as a genuine scoped counterexample. The key point to check is that the
constructed kernel is a legitimate positive element of the symmetric projective
tensor product and that the finite-subset coordinates force the sample outside
`ell_infty` almost surely.
