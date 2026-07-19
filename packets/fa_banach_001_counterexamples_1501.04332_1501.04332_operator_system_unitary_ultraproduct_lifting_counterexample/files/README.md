# Counterexample Packet: Operator-system unitary ultraproduct lifting

Status: `counterexample_likely_valid`

Source paper: Isaac Goldbring and Martino Lupini, "Model-theoretic aspects of the Gurarij operator system", arXiv:1501.04332v3.

Target question: Question 5.6 asks whether, for operator systems \(X_i\) and an ultrafilter \(\mathcal U\), every unitary \(u\in\prod_{\mathcal U}X_i\) can be represented as \(u=(u_i)^\bullet\) with each \(u_i\) a unitary in \(X_i\).

Result: negative. For any free ultrafilter on \(\mathbb N\), set \(\varepsilon_n=1/(n+5)\) and
\[
X_n=\operatorname{span}\{1,z+\varepsilon_n z^2,z^{-1}+\varepsilon_n z^{-2}\}\subset C(\mathbb T).
\]
The element \(u=(z+\varepsilon_n z^2)^\bullet\in\prod_{\mathcal U}X_n\) is a unitary in the operator-space sense, because it equals \((z)^\bullet\) in the ambient C*-ultraproduct. However every unitary in each \(X_n\) is a scalar constant, and \(z+\varepsilon_nz^2\) stays at distance at least \(2-\varepsilon_n\) from scalar unitaries. Thus \(u\) has no representing family of unitaries in the factors.

Human review focus:
- Check the boundary lemma: the curve \(z+\varepsilon z^2\), \(0<\varepsilon<1/4\), is strictly convex, so each point is strongly exposed by a real affine functional from the operator system.
- Check the use of the \(n=1\) row part of the Blecher-Neal characterization to force a unitary in \(X_\varepsilon\) to have modulus one at every point of \(\mathbb T\).
- Check the Laurent-polynomial step: a Laurent polynomial in \(X_\varepsilon\) with constant modulus one on \(\mathbb T\) must be a scalar constant.

Files:
- `main.tex` / `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: arXiv:1501.04332 source paper.
- `supporting_paper_0805.2166.pdf`: Blecher-Neal metric characterization paper.
- `figures/open_problem_page_18.png`: rendered source page containing Questions 5.5 and 5.6.
- `code/verify_laurent_curve_checks.py`: lightweight symbolic/numeric sanity checks.
