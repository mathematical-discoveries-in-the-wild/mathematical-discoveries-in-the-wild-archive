# Literature-Implied Partial Subcase: `H'_alpha(ell_1^4) < 16`

Status: `literature_implied_answer (partial subcase)`

Source paper: S. K. Mercourakis and G. Vassiliadis, *Antipodal Hadwiger numbers of finite-dimensional Banach spaces*, arXiv:1902.05593.

Source problem: in the final open-problem list, item 1(a) asks for better upper and lower bounds for `H'_alpha(ell_p^n)` and `H_alpha(ell_p^n)` when `n >= 4` and `1 <= p < 2`.

Supporting theorem: Tomasz Kobos and Marin Varivoda, *On the Banach-Mazur Distance in Small Dimensions*, arXiv:2305.06427, Theorem 3.1, proves
`d_BM(C_4,C_4^*) = 2`, equivalently `d(ell_infty^4, ell_1^4)=2`.

Implication recorded here: `H'_alpha(ell_1^4) < 16`, hence `H'_alpha(ell_1^4) <= 15`. If a strict antipodal Hadwiger set of size `16=2^4` existed in `ell_1^4`, the renorming theorem quoted in the source paper would produce an equivalent norm with a `16`-point equilateral set and Banach-Mazur distance `<2` from `ell_1^4`. The maximal equilateral-set characterization then identifies the renormed space with `ell_infty^4`, contradicting Kobos--Varivoda.

Scope limitation: this does not determine the exact value of `H'_alpha(ell_1^4)`, and it does not address `H_alpha(ell_1^4)` or the remaining `1<p<2` cases.

Files:
- `source_paper.pdf`: arXiv:1902.05593.
- `supporting_paper_2305.06427.pdf`: arXiv:2305.06427.
- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.

Ledger: `runs/fa_banach_001/ledger/results/1902.05593_l1_4_strict_antipodal_upper_bound_kobos_varivoda.json`.
