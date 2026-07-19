# Partial solution packet: a shrinking-skeleton positive criterion for Problem 4.15

Status: `partial`, likely valid, human review recommended.

## Source problem

Source: A. J. Guirao, G. Martinez-Cervantes, and J. Rodriguez, "Completeness in the Mackey topology by norming subspaces", arXiv:1812.10669 / J. Math. Anal. Appl. 478 (2019), 776--789.

The packet addresses Problem 4.15:

> Is \(X^*\) fully Mackey complete whenever \(X\) is \(w^*\)-sequentially dense in \(X^{**}\)?

## Claimed result

This packet proves a structural positive criterion. If \(X\) contains no \(\ell_1\) and admits a bounded separable projectional skeleton \((P_s)\) which:

- captures every \(x^{**}\in X^{**}\), meaning \(P_s^{**}x^{**}=x^{**}\) for some \(s\);
- is shrinking along countable suprema, meaning the induced projections on the duals of the separable ranges converge in norm;

then \(X\) is \(w^*\)-sequentially dense in \(X^{**}\), and \(X^*\) is fully Mackey complete.

This abstracts the previous `ell_p`-sum proof: coordinate projections on \((\oplus_{\gamma\in\Gamma}E_\gamma)_{\ell_p}\), \(1<p<\infty\), have exactly this countable-support and shrinking-tail behavior.

## Key mechanism

For a norming closed \(Y\subset X^{**}\), the skeleton lets one recursively enlarge a separable range \(P_sX\). At each stage, weak-star metrizability of the dual ball of \(P_sX\) selects countably many elements of \(Y\) that norm that range. Bidual capture then moves those selected elements into a later skeleton range. The shrinking condition is the crucial extra ingredient: it lets norming estimates on the increasing ranges pass to the dual of the countable supremum range.

Once \(Y\cap P_s^{**}X^{**}\) is norming for \((P_sX)^*\), the source paper's separable theorem applies to \(P_sX\), and the resulting \(LK\) compact witness is also an \(LK\) witness in \(X^{**}\).

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source paper PDF.
- `figures/open_problem_crop.png`: crop of the source problem statement.

## Review focus

The main point to check is the abstract localization lemma, especially the use of the shrinking condition to pass from norming estimates on \(P_{s_n}X\) to the countable supremum range \(P_sX\). This is also the obstruction exposed for a full solution of Problem 4.15: weak-star sequential density alone gives separable weak-star closures, but it does not supply these shrinking projections.
