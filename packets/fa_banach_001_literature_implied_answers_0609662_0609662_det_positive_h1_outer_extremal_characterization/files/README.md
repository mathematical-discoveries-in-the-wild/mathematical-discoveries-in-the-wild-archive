# 0609662 determinant-positive H1 outer extremal characterization

Status: `literature_implied_answer (partial subcase)`

Source/open-problem paper:

- David P. Blecher and Louis E. Labuschagne, *Applications of the Fuglede-Kadison determinant: Szego's theorem and outers for noncommutative H^p*, arXiv:math/0609662.
- The final question, on PDF page 14, asks whether outers in `H^1` admit a characterization in terms of extremals, analogous to the de Leeuw-Rudin theorem.

Supporting paper/theorem:

- Turdebek N. Bekjan and Quanhua Xu, *Riesz and Szego type factorizations for noncommutative Hardy spaces*, arXiv:0705.1947.
- Corollary 4.11, on PDF page 11, proves that for a finite subdiagonal algebra `A`, `0 < p <= infinity`, and `h in H^p(A)` with Fuglede-Kadison determinant `Delta(h) > 0`, `h` is outer iff every `x in H^p(A)` with `|x|=|h|` satisfies `Delta(Phi(x)) <= Delta(Phi(h))`.

Identification:

Specializing Bekjan-Xu Corollary 4.11 to `p=1` gives an extremal characterization of the determinant-positive, or strongly outer, part of the source paper's `H^1` question.  The extremal quantity is the diagonal determinant `Delta(Phi(x))` over all analytic competitors with fixed modulus.  This is an agent-identified implication: Bekjan-Xu cite and extend the Blecher-Labuschagne outer theory, but they do not present Corollary 4.11 as a named answer to the final de Leeuw-Rudin question.

Scope limitations:

- This does not remove the hypothesis `Delta(h)>0`.
- It does not settle determinant-zero outers.
- It is not a literal de Leeuw-Rudin extreme-point theorem.
- It does not answer the separate question whether every outer in `H^1` is the square of an outer in `H^2`.

Files:

- `source_paper.pdf`: arXiv:math/0609662.
- `supporting_paper_0705.1947.pdf`: arXiv:0705.1947.
- `figures/open_problem_crop.png`: source question crop.
- `figures/supporting_answer_crop.png`: Bekjan-Xu Corollary 4.11 crop.
- `solution_packet.pdf`: compact status note.
- Ledger record: `runs/fa_banach_001/ledger/results/0609662_det_positive_h1_outer_extremal_characterization.json`.

Search evidence:

Local parsed-source search for the exact square-of-outer phrase and the de Leeuw-Rudin/extremal wording found the source paper and a Blecher-Labuschagne survey repetition, but no later full closure.  Local and arXiv web searches for the determinant/outer keywords identified Bekjan-Xu arXiv:0705.1947 as the decisive partial supporting source.
