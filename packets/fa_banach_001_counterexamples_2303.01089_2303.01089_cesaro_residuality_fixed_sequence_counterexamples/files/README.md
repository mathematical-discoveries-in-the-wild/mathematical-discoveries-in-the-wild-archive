# Fixed-dynamics counterexamples to two Cesaro-residuality questions

Status: candidate_counterexample_likely_valid

Source: Catalin Badea and Sophie Grivaux, *Around Furstenberg's times p,
times q conjecture: times p-invariant measures with some large Fourier
coefficients*, Discrete Analysis 2024:10; arXiv:2303.01089.

## Result

Questions 5.6 and 5.9 are false as stated.

- In Question 5.6 take \(c_n=p^n\). Every \(T_p\)-invariant measure is
  fixed by every \(T_{c_n}\), so the Cesaro averages equal the original
  measure. Hence \(G''_{p,(c_n)}=\{\mathrm{Leb}\}\), not a residual subset
  of \(\mathcal P_p(\mathbb T)\).
- In Question 5.9 take \(A=B=2I_d\). Every \(T_A\)-invariant measure is
  fixed by every \(T_{B^n}\), so
  \(G''_{A,B}=\{\mathrm{Leb}_d\}\), again not residual.

In each ambient space, the invariant point mass at zero witnesses that the
Lebesgue singleton is not dense.

This is a literal-formulation result. It does not settle the substantive case
\(c_n=q^n\) with \(q\) multiplicatively independent from \(p\), nor a matrix
version with an independence or coprimality condition. It also does not
answer Questions 5.5 or 5.8.

## Files

- main.tex and solution_packet.pdf: self-contained proof and render.
- source_paper.pdf: published/arXiv v3 source paper.
- figures/: source-page crops showing the definitions and Questions 5.6
  and 5.9 on article pages 28--29.
- code/crop_open_questions.py: reproducible crop script.
- verification_report.md: line-by-line proof and scope audit.

## Novelty check

The cheap run indexes were searched for arXiv:2303.01089, the title,
Questions 5.6 and 5.9, Cesaro residuality, \(c_n=p^n\), and \(B=A\); no
prior result or attempt was found. Bounded web searches on 2026-07-22 used
the exact question numbers with the arXiv id, the authors with the \(G''\)
notation, and the terms \(c_n=p^n\), \(T_p\)-invariant, and Cesaro residual.
They found the source paper and journal page, but no later answer or
discussion of the fixed-point obstruction. Novelty confidence is moderate
because the argument is elementary and may amount to an unrecorded correction
of the printed quantifiers.

## Human review

Recommended verdict: likely valid literal counterexamples. Verify first that
the published Questions 5.6 and 5.9 impose no independence condition and that
residuality is taken in the full invariant-measure spaces.

