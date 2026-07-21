# A locally factorisable map that is not quantum factorisable

Status: `counterexample_likely_valid`

Source: Alexandros Chatzinikolaou, Ivan G. Todorov, and Lyudmila Turowska, *Absolutely dilatable bimodule maps*, arXiv:2411.08086; International Mathematics Research Notices 2025, rnaf160.

## Result

Equation (28) in the source asks whether
`D_loc,D(H) subset D_q,D(H)` remains true when `H` is infinite-dimensional. It does not.

Take `H = ell^2(N_0)`, let `D = ell^infinity(N_0)` be the diagonal masa, and let `Phi` be the normal conditional expectation onto `D`. Averaging conjugation by
`diag(1,z,z^2,...)` over Haar measure on the circle gives an exact factorisation through the abelian ancilla `L^infinity(T)`, so `Phi` is locally factorisable.

If `Phi` had a finite-dimensional quantum ancilla, the type-preserving exactness statement for measurable Schur multipliers in the source would give unitaries `v_n` in one finite-dimensional tracial von Neumann algebra with
`tau(v_i^* v_j) = delta_ij`. These would form an infinite orthonormal set in the finite-dimensional Hilbert space `L^2(M,tau)`, a contradiction.

Thus
`D_loc,D(ell^2) \ D_q,D(ell^2)` is nonempty.

## Files

- `main.tex`: complete counterexample proof.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_problem_crop_part1.png` and `part2.png`: the two-page source question.
- `VERIFICATION.md`: proof, novelty, and render checks.

## Novelty and review

The local run indexes and bounded web searches through July 21, 2026 found the unchanged question in both arXiv:2411.08086 and the 2025 published version, but no later answer or correction using the diagonal expectation. Novelty confidence is moderate because the obstruction is elementary and may be known informally.

Recommended review status: likely valid counterexample. The decisive reviewer check is that the type-preserving exactness assertion in the proof of the source's Corollary 3.5 applies to the quantum class for the discrete masa.
