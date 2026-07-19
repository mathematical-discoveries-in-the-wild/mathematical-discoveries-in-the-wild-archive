# Conditional reduction: the \(L^q\), \(p=1\) endpoint

Status: `conditional_reduction_likely_valid`

Source problem: Ivan S. Yaroslavtsev, *Local characteristics and tangency of vector-valued martingales*, arXiv:1907.11588, Remark 12.10.

Conditional result: For every `1<q<infinity`, the full \(L^q(S)\)-valued general-local characteristic-domination theorem at \(p=1\) follows from one endpoint square-function comparison:

\[
  \mathbb E\Big\|\Big(\sum_i |\xi_i|^2\Big)^{1/2}\Big\|_{L^q(S)}
  \le C_q
  \mathbb E\Big\|\Big(\sum_j |\eta_j|^2\Big)^{1/2}\Big\|_{L^q(S)}
\]

whenever the independent \(L^q(S)\)-valued variables \((\xi_i)\), \((\eta_j)\) have aggregate occurrence measures satisfying
\[
  \sum_i \mathbb P(\xi_i\in B)\le \sum_j \mathbb P(\eta_j\in B)
  \quad(B\subset L^q(S)\setminus\{0\}\text{ Borel}).
\]

What is proved unconditionally in the packet:

- Dirksen--Yaroslavtsev's \(p=1\) independent upper estimate and Yaroslavtsev's \(p=1\) Banach-function-space BDG theorem reduce the endpoint discrete problem to the square-function comparison above.
- The same reduction, combined with the existing total-compensator collapse from the \(1<p<\infty\) packet and the source decoupled-tangent theorem, promotes the discrete endpoint comparison to the full general-local martingale statement.
- The comparison is true in Hilbert spaces by the existing Laplace-transform packet and false in \(c_0\); finite-dimensional \(L^q\) simulations found no growing obstruction.

Limitation: The endpoint square-function comparison itself is not proved here. This packet is therefore deliberately conditional, not a claimed partial theorem.

Human review recommendation: First verify the proposition named "Conditional discrete \(p=1\) comparison" in `main.tex`, which is the clean reduction from the named square-function lemma to the discrete \(p=1\) comparison. Then attack the endpoint square-function lemma directly; it is now the isolated missing step for the \(L^q\), \(p=1\) endpoint.

Files:

- `main.tex`: conditional proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv:1907.11588.
- `supporting_paper_1707.00109.pdf`: Dirksen--Yaroslavtsev \(L^q\)-valued Burkholder--Rosenthal paper.
- `supporting_paper_1807.05573.pdf`: Yaroslavtsev BDG in UMD Banach spaces.
- `code/grouping_square_simulation.py`: finite regrouping sanity checks.
- `code/last_simulation_output.txt`: output from the recorded run.
