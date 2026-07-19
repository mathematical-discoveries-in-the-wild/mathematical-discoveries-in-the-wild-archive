# Literature implied answer: real-line Gaussian tail-space reverse Bernstein--Markov

Status: `literature_implied_answer (real-line subcase)`

Source/open-problem paper: Alexandros Eskenazis and Paata Ivanisvili, "Dimension independent Bernstein--Markov inequalities in Gauss space", arXiv:1808.01273v3; Journal of Approximation Theory 253 (2020), Article 105377.

Supporting paper: Alexandros Eskenazis and Paata Ivanisvili, "Sharp growth of the Ornstein--Uhlenbeck operator on Gaussian tail spaces", arXiv:2011.01359v2; Israel Journal of Mathematics 253 (2023), 469--485, DOI 10.1007/s11856-022-2373-8.

## Identification

Question 7 in arXiv:1808.01273 asks whether, for every \(1<p<\infty\), there is \(c_p>0\) such that every \(k\)-dimensional polynomial \(P\) supported on Hermite frequencies \(|\alpha|\ge d\) satisfies
\[
\|LP\|_{L^p(d\gamma_k)}\ge c_p d\,\|P\|_{L^p(d\gamma_k)}.
\]

The supporting paper arXiv:2011.01359 proves the corresponding assertion on the real line. In its introduction, Corollary 2 states that for every \(p\in(1,\infty)\) there is \(T_p<\infty\) such that, for every one-dimensional polynomial \(f\) in the \(d\)-tail space,
\[
d\|f\|_{L^p(d\gamma_1)}\le T_p\|Lf\|_{L^p(d\gamma_1)}.
\]
This is exactly Question 7 with \(k=1\), after moving constants across the inequality.

## Scope

This packet records only the real-line subcase \(k=1\) of Question 7. It does not answer:

- the full \(k\ge 1\) reverse Bernstein--Markov question for arbitrary multivariate Hermite-tail polynomials,
- Question 3 on the sharp \(\sqrt{\deg P}\) gradient Bernstein--Markov inequality,
- the source's linear upper bound question for \(\|LP\|_p\) in all dimensions.

The supporting authors knew the relation: arXiv:2011.01359 explicitly describes the result as an affirmative answer to the Gaussian analogue of the Mendel--Naor question on the real line and cites arXiv:1808.01273.

## Files

- `source_paper.pdf`: arXiv:1808.01273 source/open-problem paper.
- `supporting_paper_2011.01359.pdf`: supporting theorem paper.
- `main.tex` and `solution_packet.pdf`: compact status note.

## Search Evidence

Cheap indexes were searched for `1808.01273`, `Dimension independent Bernstein-Markov`, `Bernstein-Markov`, `Gaussian space`, and related terms. No exact prior packet for this source was present. Web searches for the reverse Bernstein--Markov/Gaussian tail-space phrases identified arXiv:2011.01359 and its published DOI as the decisive supporting source.
