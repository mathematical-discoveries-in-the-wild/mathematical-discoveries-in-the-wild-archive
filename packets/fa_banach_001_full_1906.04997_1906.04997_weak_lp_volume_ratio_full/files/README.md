# Exponential weak-\(\ell_p\) volume gap for every finite \(p\)

Status: candidate full solution, likely valid, pending human review.

Source: Anna Doležalová and Jan Vybíral, *On the volume of unit balls
of finite-dimensional Lorentz spaces*, arXiv:1906.04997, Journal of
Approximation Theory 255 (2020), 105407.

The source proves that
\[
R_{p,n}=\frac{\operatorname{vol}(B_{p,\infty}^n)}
{\operatorname{vol}(B_p^n)}
\]
grows exponentially for \(0<p\leq2\), and asks whether the same is true
for every \(0<p<\infty\).

This packet proves the stronger quantitative bound
\[
\liminf_{n\to\infty}R_{p,n}^{1/n}
\geq
\frac{(1+1/p)^{1+1/p}}{\Gamma(1+1/p)}
>1
\qquad(0<p<\infty).
\]

The proof constructs a probability density whose survival function lies
under the weak-\(\ell_p\) rank constraint.  A finite-bin type-class argument
turns its differential entropy into volume inside the rescaled weak ball.
The density is uniform up to the tangency point
\((p+1)^{1/p}\) and has the extremal Pareto tail \(p t^{-p-1}\)
afterwards.  Its entropy exceeds the normalized \(\ell_p\)-ball entropy by
exactly
\[
(1+1/p)\log(1+1/p)-\log\Gamma(1+1/p)>0.
\]

Files:

- `solution_packet.pdf`: rendered review packet.
- `main.tex`: complete proof.
- `VERIFICATION.md`: explicit mathematical, numerical, novelty, and render audit.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source-paper page 14.
- `code/verify_rates.py`: finite-dimensional numerical sanity checks.

Recommended reviewer focus: the cumulative-bin inequalities in the
type-volume lemma, the \(n^{1/p}\) scaling, and the entropy calculation.
