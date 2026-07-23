# Arithmetic-mean counterexample to Conjecture 11

Status: candidate counterexample, likely valid, pending human review.

Source: Idan Attias and Aryeh Kontorovich, *Fat-Shattering Dimension
of \(k\)-fold Aggregations*, arXiv:2110.04763; JMLR 25 (2024), paper
144, 1-29.

Conjecture 11, read with its displayed universal quantification over
1-Lipschitz aggregation rules, predicts
\[
  \operatorname{fat}_\gamma(G(F_1,\ldots,F_k))
  \geq
  \frac{C\operatorname{Log}(k)}{\gamma^2}
  \sum_{i=1}^k R_i^2
\]
for every collection of \(R_i\)-bounded affine classes and every
1-Lipschitz aggregation \(G\).

This packet gives a symmetric counterexample.  Take all component classes
equal to
\[
  \mathcal A_R
  =
  \{x\mapsto\langle w,x\rangle+b:
    \|w\|\leq R,\ |b|\leq R\}
\]
on a Hilbert unit ball, and take \(G\) to be the arithmetic mean.  Then
\[
  G(\mathcal A_R,\ldots,\mathcal A_R)=\mathcal A_R
\]
exactly, while a self-contained Rademacher-sign argument gives
\[
  \operatorname{fat}_\gamma(\mathcal A_R)
  \leq 4R^2/\gamma^2.
\]
The left side is independent of \(k\), whereas the conjectured lower bound
is \(Ck\operatorname{Log}(k)R^2/\gamma^2\).

The example is robust to the convention that “1-Lipschitz” means either
Lipschitz constant at most one or optimal Lipschitz constant exactly one:
the arithmetic mean has optimal supremum-norm Lipschitz constant one.

Scope caveat: this refutes Conjecture 11 as formally written.  It does not
refute a possible intended conjecture restricted to the maximum aggregation,
nor the weaker statement that the upper bound of Theorem 3 is attained by
some aggregation rule.

Files:

- `solution_packet.pdf`: rendered review packet.
- `main.tex`: complete self-contained proof.
- `VERIFICATION.md`: mathematical, novelty, and render audit.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source page 15 containing Conjecture 11.

Recommended reviewer focus: confirm the quantifier intended in Conjecture 11.
Under the literal universal reading printed in the paper, the counterexample
is immediate and complete.
