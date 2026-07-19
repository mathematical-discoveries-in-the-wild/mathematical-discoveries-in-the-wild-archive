# Conditional Counterexample Packet

## Status

`conditional_counterexample_likely_valid`, strengthened on 2026-06-16.

The original Q-point dependency has been reduced to a broader nonvacuity-relative statement:

- ZFC reduction: if an `epsilon`-strong measure has a finite-block partition whose bounded-per-block ideal has measure strictly below one half, the source paper's own `C(K_P)` sequence gives a counterexample to Question 2.
- Relative counterexample: if there exists a normalized `eta`-strong Q-measure, then for every `0 < epsilon < eta/2` there is an `epsilon`-strong Q-measure for which Question 2 fails.
- In particular, if any strong Q-measure exists, then Question 2 has a negative answer for every `0 < epsilon < 1/2`.

This strictly subsumes the previous Q-point packet, since a Q-point ultrafilter gives a strong Q-measure.  It does not prove a full ZFC counterexample, because the source paper proves models with no measure `Q+(omega)` ideals; in those models there are no `epsilon`-strong Q-measures at all.

## Source

Antonio Aviles, Gonzalo Martinez-Cervantes, Alejandro Poveda, Luis Saenz, *A Banach space with \(L\)-orthogonal sequences but without \(L\)-orthogonal elements*, arXiv:2501.06537.

Question 2 asks whether an \(\varepsilon\)-strong \(Q\)-measure \(\mu\) and an \(L\)-orthogonal sequence \((x_n)\) always satisfy
\[
\|x+\mu\text{-}\lim(x_n)\|\ge \|x\|+\varepsilon\|\mu\text{-}\lim(x_n)\|
\]
for \(x\in X\).

## Result

Let \(\sigma\) be a normalized \(\eta\)-strong \(Q\)-measure and fix \(0<\varepsilon<\eta/2\).  Choose \(t\) with \(\varepsilon/\eta<t<1/2\), choose a block partition \(\mathcal P=(P_m)\) with \(|P_m|\to\infty\), and let \(\lambda\) be block density along a free ultrafilter:
\[
\lambda(A)=\lim_{m\to\mathcal V}\frac{|A\cap P_m|}{|P_m|}.
\]
Then
\[
\mu=t\sigma+(1-t)\lambda
\]
is \(\varepsilon\)-strong, but every \(I\in\mathcal I_{\mathcal P}\) has \(\mu(I)\le t<1/2\).  The source Lemma 4.6 forces the canonical \(C(K_{\mathcal P})\) \(\mu\)-limit close to the constant function, and \(x=-1\) violates the proposed lower bound.

## ZFC Barrier

The source paper proves it is consistent with ZFC that there are no \(Q^+(\omega)\)-measures, and Corollary 3.15 identifies Laver, Mathias, and Miller models with no measure \(Q^+(\omega)\)-ideals.  Since every \(\varepsilon\)-strong \(Q\)-measure is automatically a \(Q^+(\omega)\)-measure, there cannot be a ZFC construction of a fixed \(\varepsilon\)-strong counterexample measure in all models.  A same-parameter absolute counterexample would need a new theorem extracting the non-fit/block-smallness condition from the particular \(\varepsilon\)-strong measure assumed in Question 2.

## Files

- `main.tex` / `solution_packet.pdf`: formal packet.
- `source_paper.pdf`: local copy of arXiv:2501.06537.
- `figures/open_problem_crop.png`: crop of Question 2 from the source PDF.
- `code/check_scalar_inequality.py`: scalar sanity check for the final contradiction.

## Human Review Recommendation

Review the new dilution step \( \mu=t\sigma+(1-t)\lambda \), the normalization of the source \(\eta\)-strong measure, and the application of source Lemma 4.6 with \(\delta\in(t,1/2)\).  The remaining limitation is conceptual rather than a proof gap: the result does not settle the same-parameter case starting from an arbitrary \(\varepsilon\)-strong measure.
