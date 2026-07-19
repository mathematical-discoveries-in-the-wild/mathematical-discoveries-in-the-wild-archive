# 1602.07090: ASQ Passes To Symmetric Injective Tensor Powers

Status: `candidate_full_solution_likely_valid`

Source paper: Johann Langemets, Vegard Lima, and Abraham Rueda Zoca,
*Almost square and octahedral norms in tensor products of Banach spaces*,
arXiv:1602.07090.

Open question solved: Section 4, Question 4.3 asks whether
`\widehat{\otimes}_{\varepsilon,s,N}X` is ASQ for every `N in N` whenever
`X` is ASQ.

Candidate answer: yes. For every ASQ Banach space `X` and every `N >= 1`,
the injective symmetric tensor product
`\widehat{\otimes}_{\varepsilon,s,N}X` is ASQ.

Core mechanism: approximate finitely many target tensors by finite symmetric
tensors supported in a finite-dimensional subspace `E`. The ASQ
finite-dimensional extension theorem gives `y in S_X` such that
`E + span{y}` is almost an `ell_infty` sum. Dualizing gives
`||x^*|_E|| + |x^*(y)| <= 1 + delta` for every `x^* in B_{X^*}`. This
turns the injective symmetric norm estimate into the scalar bound
`r^N + s^N <= (r+s)^N`, proving that `u_i +/- y^N` has norm at most
`1 + epsilon` for all finitely many `u_i`.

Novelty check: local run indexes and target-pool scans found no prior packet
for arXiv:1602.07090 or this symmetric injective ASQ question. Web searches on
2026-06-19 for exact phrases around "injective symmetric tensor product",
"almost square", "ASQ", and arXiv:1602.07090 only surfaced the source paper,
not a later explicit answer. Novelty is therefore plausible but still marked
for human literature review.

Files:

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:1602.07090.
- `figures/open_problem_crop.png`: crop of Question 4.3.
- `code/scalar_bound_verifier.py`: optional audit of the scalar inequality.

Human review recommendation: check the dualization step from the ASQ
finite-dimensional extension theorem and the passage from finite symmetric
tensors to the completed tensor product. These are the only substantive points.
