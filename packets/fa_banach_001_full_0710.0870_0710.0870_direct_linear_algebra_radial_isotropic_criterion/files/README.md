# Direct linear-algebra proof of the radial-isotropic criterion

Status: candidate full solution, likely valid.  The theorem itself is already proved in the source paper and in related Brascamp--Lieb/radial-isotropic literature; the claimed contribution here is a direct proof of the source's explicit "purely linear algebra" proof request.

Source: Eric A. Carlen and Dario Cordero-Erausquin, "Subadditivity of the Entropy and its Relation to Brascamp--Lieb Type Inequalities", arXiv:0710.0870.

Target passage: On PDF page 30, before Theorem 4.3, the authors state that the theorem concerns a problem in linear algebra and that they do not know a direct proof in a purely linear algebra context.  Theorem 4.3 characterizes when an invertible symmetric matrix `R` exists such that

```text
sum_j c_j (R a_j / |R a_j|) \otimes (R a_j / |R a_j|) = I.
```

Result: The packet gives a direct proof using the vector-matroid basis polytope, Cauchy--Binet, a log-sum-exp/log-det minimization for the relative-interior case, and recursive splitting along saturated rank inequalities for the boundary case.

Novelty notes: Web/literature search found close known formulations under radial isotropic position and Tyler's M-estimator, including the known subspace-condition criterion.  This packet should be reviewed as a clean direct proof/explanation of the Carlen--Cordero-Erausquin theorem, not as a claim that the radial-isotropic criterion is new.

Files:
- `main.tex`: solution packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local source PDF.
- `figures/open_problem_crop.png`: source crop of the direct-proof request and theorem.

