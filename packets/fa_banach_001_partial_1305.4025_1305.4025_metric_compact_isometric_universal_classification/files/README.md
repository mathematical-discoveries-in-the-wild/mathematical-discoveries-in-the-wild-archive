# Partial Result: Metric compacta whose C(K) is isometrically universal

Status: partial_result_likely_valid

Source paper: Florent Baudier, "A topological obstruction for small-distortion embeddability into spaces of continuous functions on countable compact metric spaces", arXiv:1305.4025.

## Result

For compact metric \(K\), the Banach space \(C(K)\) is an isometric universal Banach space for the class of separable Banach spaces if and only if \(K\) is uncountable.

Moreover, if \(K\) is uncountable compact metric, then
\[
c_{C(K)}(\mathrm{SEP})=c_{C(K)}(\mathcal{SEP})=1.
\]

This answers the isometric-universal clause in Question 2 of the source for compact metric spaces, and gives the uncountable side of the \(c=1\) classification. It does not settle whether a countable compact metric \(K\) of high Cantor-Bendixson rank can satisfy \(c_{C(K)}(\mathrm{SEP})=1\) in the almost-isometric sense.

## Proof Sketch

If \(K\) is uncountable compact metric, then \(K\) contains a closed Cantor subset \(F\). There is a continuous surjection \(F\to[0,1]\), so pullback embeds \(C([0,1])\) linearly isometrically into \(C(F)\). The Borsuk-Dugundji extension theorem embeds \(C(F)\) linearly isometrically into \(C(K)\). Hence \(C(K)\) contains a linear isometric copy of \(C([0,1])\), and Banach-Mazur universality gives all separable Banach spaces; separable metric spaces follow by applying Banach-Mazur to the Lipschitz-free space.

If \(K\) is countable compact metric, then every regular Borel measure on \(K\) is atomic and \(C(K)^*\cong \ell_1(K)\) is separable. Therefore every closed subspace of \(C(K)\) has separable dual, so \(C(K)\) cannot contain a linear copy of \(\ell_1\). If \(\ell_1\) embedded isometrically as a metric space into \(C(K)\), the Godefroy-Kalton theorem would force a linear isometric copy of \(\ell_1\), contradiction.

## Files

- `source_paper.pdf`: arXiv:1305.4025.
- `figures/open_problem_crop.png`: crop of the source questions.
- `main.tex` / `solution_packet.pdf`: proof packet.

Ledger record: `runs/fa_banach_001/ledger/results/1305.4025_metric_compact_isometric_universal_classification.json`.
