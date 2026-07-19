# Partial solution packet: an `ell_p`-sum positive class for Problem 4.15

Status: `partial`, likely valid, human review recommended.

## Source problem

Source: A. J. Guirao, G. Martinez-Cervantes, and J. Rodriguez, "Completeness in the Mackey topology by norming subspaces", arXiv:1812.10669 / J. Math. Anal. Appl. 478 (2019), 776--789.

The packet addresses Problem 4.15:

> Is \(X^*\) fully Mackey complete whenever \(X\) is \(w^*\)-sequentially dense in \(X^{**}\)?

The result proves an affirmative answer for a broad nonseparable `ell_p`-sum class.

## Claimed result

Let \(1<p<\infty\), let \(\Gamma\) be any index set, and let \((E_\gamma)_{\gamma\in\Gamma}\) be separable Banach spaces containing no subspace isomorphic to \(\ell_1\). Put
\[
X=\left(\bigoplus_{\gamma\in\Gamma} E_\gamma\right)_{\ell_p}.
\]
Then \(X\) is \(w^*\)-sequentially dense in \(X^{**}\), and \(X^*\) is fully Mackey complete.

When \(\Gamma\) is uncountable and some \(E_\gamma\) is separable non-Asplund without \(\ell_1\), e.g. a James-tree type space, this gives a nonseparable non-Asplund positive class beyond the separable and Asplund cases listed in the source paper.

## Key mechanism

For a norming norm-closed \(Y\subset X^{**}\) and \(u\in X^{**}\setminus Y\), the support of \(u\) is countable. A localization lemma enlarges that support to a countable set \(A\subset\Gamma\) such that \(Y\cap X_A^{**}\) is still norming for \(X_A^*\). Since \(X_A\) is separable and contains no \(\ell_1\), the source paper implies \(X_A^*\) is fully Mackey complete. The `LK` witness in the countable sub-sum is then also an `LK` witness in \(X^{**}\).

The nontrivial point is the localization lemma: it uses the weak-star metrizability of \(B_{X_A^*}\) for countable \(A\), plus a countable recursive support-enlargement argument.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source paper PDF.
- `figures/open_problem_crop.png` and `figures/problem_4_15_crop.png`: source problem crops.

## Review focus

Please check the countable-support localization lemma, especially the passage from a norming subspace \(Y\subset X^{**}\) to a countable \(A\) for which \(Y\cap X_A^{**}\) remains norming for \(X_A^*\). This is the core new argument.
