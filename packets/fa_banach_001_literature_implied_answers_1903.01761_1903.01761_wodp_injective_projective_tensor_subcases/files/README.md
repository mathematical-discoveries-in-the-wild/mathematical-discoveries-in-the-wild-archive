# 1903.01761 Daugavet tensor product question: WODP and transfinite subcases

Status: `literature_implied_answer` (partial subcases/status update; the full
Werner/RTV question remains open)

## Source Question

- Source paper: Abraham Rueda Zoca, Pedro Tradacete, and Ignacio Villanueva,
  "Daugavet property in tensor product spaces", arXiv:1903.01761.
- Location: Introduction, Question 1 / `questiondproyect`.
- Question: if Banach spaces \(X\) and \(Y\) both have the Daugavet property,
  must \(X\widehat{\otimes}_\varepsilon Y\) and
  \(X\widehat{\otimes}_\pi Y\) have the Daugavet property?

## Supporting Literature

- Miguel Martin and Abraham Rueda Zoca, "Daugavet property in projective
  symmetric tensor products of Banach spaces", arXiv:2010.15936, Banach
  J. Math. Anal. 16 (2022), article 35.
  - Location: Section 5, Theorem 5.4 / `theorem:WODP`.
  - Result: if \(X\) and \(Y\) have the weak operator Daugavet property
    (WODP), then \(X\widehat{\otimes}_\pi Y\) has WODP, hence the Daugavet
    property.
- Abraham Rueda Zoca, "Weak operator Daugavet property and weakly open sets in
  tensor product spaces", arXiv:2407.21585.
  - Location: Theorem `theo:daugainjective`.
  - Result: if \(X^*\) and \(Y^*\) have WODP, then
    \(X\widehat{\otimes}_\varepsilon Y\) has the Daugavet property.
  - The same paper says this improves the \(L_1(\mu)\widehat{\otimes}_\varepsilon
    L_1(\nu)\) theorem from arXiv:1903.01761.
- Antonio Aviles, Johann Langemets, Miguel Martin, and Abraham Rueda Zoca,
  "Transfinite Daugavet property", arXiv:2604.14102.
  - Location: Section "Tensor products", Theorem `theo:tensorprolargeDP`.
  - Result: for an infinite cardinal \(\kappa\), if injective Banach spaces
    \(X\) and \(Y\) have the \(\kappa\)-Daugavet property, then
    \(X\widehat{\otimes}_\pi Y\) has the \(\kappa\)-Daugavet property; likewise
    for the \(\kappa\)-perfect Daugavet property.

## Identification

The 1903 source asks the broad two-sided Daugavet tensor-product question after
noting that the "or" version is false. The later WODP theorem of
Martin--Rueda Zoca gives a direct positive projective-tensor subcase: WODP is
stronger than the Daugavet property and stable under projective tensor
products, so pairs of WODP spaces satisfy the projective half of the source
question.

The 2024 WODP paper gives a direct positive injective-tensor subcase under a
dual WODP hypothesis. This is not merely the source paper's \(L_1\)-space
result: the supporting paper explicitly states that its theorem improves the
source Theorem 1.1.

The 2026 transfinite paper gives an additional projective-tensor stability
result under injectivity plus a transfinite strengthening of the Daugavet
property. Since \(\kappa\)-Daugavet implies the ordinary finite-test Daugavet
property, this supplies another scoped positive projective subcase, but it is
stronger than ordinary Daugavet and therefore does not close the original
question for arbitrary Daugavet factors.

## Scope Limitations

This packet is not a full answer to Question 1 of arXiv:1903.01761. It records
known positive subcases:

- projective tensor product for WODP factors;
- injective tensor product when both duals have WODP;
- projective tensor product for injective factors with a transfinite Daugavet
  strengthening.

The following remain outside the packet:

- arbitrary Daugavet spaces \(X,Y\) for \(X\widehat{\otimes}_\pi Y\);
- arbitrary Daugavet spaces \(X,Y\) for \(X\widehat{\otimes}_\varepsilon Y\);
- whether every Daugavet space has WODP or ODP.

## Search Evidence

- Run indexes were searched for `1903.01761`, `Daugavet property`, `tensor
  product`, `projective tensor`, `injective tensor`, `WODP`, and `weak operator
  Daugavet`; no existing packet covered this status update.
- Local source search found arXiv:2010.15936, arXiv:2407.21585, and
  arXiv:2604.14102 as the decisive later sources.
- The source and supporting TeX files were checked around Question 1, the WODP
  projective theorem, the WODP injective theorem, and the transfinite tensor
  theorem.

## Local Files

- `source_paper.pdf`: arXiv:1903.01761.
- `supporting_paper_2010.15936.pdf`: projective WODP theorem.
- `supporting_paper_2407.21585.pdf`: injective dual-WODP theorem.
- `supporting_paper_2604.14102.pdf`: transfinite/injective-factor theorem.
- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note, if LaTeX rendering succeeds.

## Human Review Recommendation

Verify that the theorem labels above match the cited source locations and that
the scope line stays partial. In particular, do not read this packet as a
solution of the unrestricted "both Daugavet factors" problem.
