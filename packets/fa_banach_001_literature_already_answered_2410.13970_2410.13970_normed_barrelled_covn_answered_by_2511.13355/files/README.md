# Normed Barrelled Dimension Lower Bound Answered By arXiv:2511.13355

Status: literature_already_answered.

Source/open-problem paper: Will Brian and Christopher Stuart,
*Small-dimensional normed barrelled spaces*, arXiv:2410.13970.

Source question: Question 4.13 asks whether every barrelled subspace of an
infinite-dimensional Banach space has dimension at least `cov(N)`, and in
particular whether the minimal dimension `y` of an infinite-dimensional normed
barrelled space satisfies `cov(N) <= y`.

Supporting answer paper: Damian Sobota, *A small remark on small-dimensional
normed barrelled spaces*, arXiv:2511.13355.

Answer: yes. Theorem `thm:main` proves that if `A` is a subset of an
infinite-dimensional Banach space `E` and `span(A)` is barrelled, then
`|A| >= cov(N)`. Corollary `cor:covN` states the direct consequence that every
infinite-dimensional normed barrelled space has dimension at least `cov(N)`.
Corollary `cor:y_covN` records `max(b, cov(N)) <= y <= non(M)`.

Packet contents:

- `source_paper.pdf`: original arXiv:2410.13970 PDF.
- `supporting_paper_2511.13355.pdf`: supporting arXiv:2511.13355 PDF.
- `main.tex`: compact LaTeX status note.
- `solution_packet.pdf`: rendered status note.
- `tmp/`: LaTeX build outputs.

Scope:

This clears Question 4.13 of arXiv:2410.13970. It does not settle the later
question asked in arXiv:2511.13355, namely whether the minimal normed
barrelled-space dimension `y` equals `non(M)` in ZFC.
