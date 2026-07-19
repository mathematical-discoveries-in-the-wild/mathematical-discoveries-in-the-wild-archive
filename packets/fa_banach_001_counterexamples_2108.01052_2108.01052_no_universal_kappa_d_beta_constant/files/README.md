# Full negative answer to arXiv:2108.01052, Question 1

Status: `candidate_counterexample_likely_valid`.

Question 1 asks whether a universal constant `D` satisfies
`kappa_d(T) <= D beta(T)`.

For `c > 1`, set

`E = ell_1 direct_sum_infinity ell_2`

and let `J:ell_1 -> ell_2` be the formal inclusion. Define

`T_c(x,y) = (x, y - c Jx)`.

The inclusion `J` is strictly singular, hence the off-diagonal map
`S_c(x,y)=(0,cJx)` is strictly singular. The source paper's perturbation
inequality therefore gives

`kappa_d(T_c) = kappa_d(I) = 1`.

But the normalized disjoint vectors

`u_n = (c^{-1} e_n, e_n)`

satisfy `||T_c u_n|| = c^{-1}`, so `beta(T_c) <= c^{-1}`. Since `T_c` is
invertible, `beta(T_c) > 0`; in fact `beta(T_c) >= 1/(1+c)`. Thus

`kappa_d(T_c) / beta(T_c) >= c`,

which rules out every universal `D`.

The domain is an order-continuous atomic Banach lattice, and every `T_c` is
an isomorphism.

Files:

- `main.tex`: complete proof and source alignment.
- `solution_packet.pdf`: compiled proof packet.
- `verification_report.md`: adversarial step audit.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: source question.
