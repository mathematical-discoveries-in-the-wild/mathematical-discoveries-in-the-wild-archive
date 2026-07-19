# A \(c_0\)-vector outside the closed span in a variable-exponent sequential space

Status: candidate counterexample / full negative answer to the second open problem in arXiv:0905.0812.

Source paper: Jarno Talponen, "Constructions of sequential spaces", arXiv:0905.0812.

## Target Question

Talponen asks whether
\[
\ell^{p(\cdot)}\cap c_0
\]
always coincides with the closed linear span \([(e_n)]\subset \ell^{p(\cdot)}\). The question appears first in the introduction and is repeated in the final open-problem list on page 8.

## Result

The answer is negative. There is a map \(p:\mathbb N\to[2,\infty)\) and a vector
\[
x\in \ell^{p(\cdot)}\cap c_0
\]
such that \(x\notin [(e_n)]\).

## Proof Mechanism

Use consecutive blocks with rapidly increasing exponents. In block \(j\), put \(m_j=j^{j+1}\) coordinates all equal to \(c/j\), where \(0<c<1\), and use exponent \(r_j=j+1\) throughout the block. Each block has its own internal norm exactly \(c\), so infinitely many tails have norm at least \(c\). But when block \(j\) is appended after an accumulated norm at least \(1\), it increases the global norm by only a factor bounded by \((1+c^{r_j})^{1/r_j}\). The product of these factors converges.

Thus the vector is in the ambient space and tends coordinatewise to zero, but its tails do not vanish in norm. Since vectors in the closed span \([(e_n)]\) are exactly those whose coordinate tails vanish in norm, this separates \(\ell^{p(\cdot)}\cap c_0\) from \([(e_n)]\).

## Files

- `main.tex`: review packet with the theorem and proof.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: official arXiv PDF for arXiv:0905.0812.
- `figures/open_problem_crop.png`: crop of the final open-problem list from page 8.
- `code/block_counterexample_check.py`: finite-block recurrence check.

## Verification And Novelty Notes

Local cheap-index searches on `registry_index.tsv`, `solutions/index.tsv`, `attempts/index.tsv`, and `proof_gaps/index.tsv` found no existing packet for arXiv:0905.0812 or this equality question. A local exact-phrase search for the variable-exponent sequential-space question found only the active claim and target-pool rows.

Bounded web searches on 2026-06-15 for exact and near-exact phrases including `"Constructions of sequential spaces" Talponen "c_0" "[(e_n)]"`, `"ell^{p(\\cdot)}" "c_0" "[(e_n)]"`, and `"variable exponent sequential spaces" Talponen` surfaced the source paper but no later explicit answer. Novelty confidence should still be treated as medium until a human does a broader specialist literature check.

Human review should focus on:

- the indexing convention for the exponents \(p(k)\) across consecutive blocks;
- the assertion that \(Q_n\) is contractive by coordinatewise monotonicity of Talponen's norm;
- the equivalence \(y\in[(e_n)]\) iff \(\|Q_n y\|\to0\);
- the convergence of \(\prod_j (1+c^{j+1})^{1/(j+1)}\).
