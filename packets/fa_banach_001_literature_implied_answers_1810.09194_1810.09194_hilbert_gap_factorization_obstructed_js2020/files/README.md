# Literature-Implied Partial Subcase: Hilbert-Gap Factorization Fails

Status: `literature_implied_answer (partial subcase)`.

Source problem: Martin Mathieu and Pedro Tradacete, "Strictly singular multiplication operators on `L(X)`", arXiv:1810.09194.  Remark 6.11 asks whether every strictly singular operator on `L_p[0,1]`, `1<p<infty`, `p != 2`, is approximately `(ell_r,ell_s)`-factorizable for some `r<s`, and also asks a finite-dimensional-sum variant.

Supporting theorem: William B. Johnson and Gideon Schechtman, "The number of closed ideals in `L(L_p)`", arXiv:2003.11414.  In the introduction and Remark 6 they state/prove that the closed Hilbert-factorization ideal `overline{Gamma_2}(L_p)` does not contain all strictly singular operators on `L_p`, for every `1<p != 2<infty`.

Implication recorded here: for every `1<p != 2<infty`, there is a strictly singular operator on `L_p` which is not approximately factorizable through the Hilbert-gap pair:
- `(ell_p, ell_2)` when `1<p<2`;
- `(ell_2, ell_p)` when `2<p<infty`.

Reason: any operator approximately factorizable through one of these pairs is a norm limit of operators factoring through the Hilbert space `ell_2`, hence belongs to `overline{Gamma_2}(L_p)`.

Scope limitation: this does **not** answer the full Mathieu-Tradacete question, because it does not rule out approximate factorization through some other non-Hilbert pair `ell_r -> ell_s`.  It rules out the most natural upgrade of the DFJP/Johnson factorization route via the Hilbert exponent.

Files:
- `source_paper.pdf`: arXiv:1810.09194.
- `supporting_paper_2003.11414.pdf`: arXiv:2003.11414.
- `solution_packet.pdf`: compact status note.
- `figures/open_problem_crop.png`: source Remark 6.11 crop reused from the prior 1810.09194 packet.

Ledger: `runs/fa_banach_001/ledger/results/1810.09194_hilbert_gap_factorization_obstructed_js2020.json`.
