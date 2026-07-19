# Literature status: uniformly convex targets in quantitative affine approximation

status: literature_already_answered

source_arxiv: 1510.00276

supporting_arxiv: 1608.01915

source_problem: Hytönen--Li--Naor, Question `Q:UC`

packet_verdict: positive answer already in later literature

## Summary

Question `Q:UC` in arXiv:1510.00276 asks whether the improved quantitative
affine-approximation bound proved there for UMD targets remains true under the
weaker and qualitatively optimal assumption that the target admits an
equivalent uniformly convex norm.

Hytönen--Naor, arXiv:1608.01915, explicitly answers that question positively.
Its Theorem 1 states that if `Y` admits an equivalent uniformly convex norm,
then for every `n`-dimensional Banach space `X` and every `epsilon in
(0,1/2]`,

```text
r^{X -> Y}(epsilon) >= exp(-1 / epsilon^{c n})
```

for some constant `c = c(Y)`. The paper states directly after the theorem that
this answers Question 8 of arXiv:1510.00276 positively.

## Evidence

- `source_paper.pdf`: original/open-question paper, arXiv:1510.00276.
- `supporting_paper_1608.01915.pdf`: later answer paper.
- `main.tex`: compact status note with source question and supporting theorem.
- `solution_packet.pdf`: rendered status note.

## Scope

This packet records only the positive literature answer to the uniformly
convex-target part of arXiv:1510.00276, Question `Q:UC`. It does not claim to
settle the broader sharp asymptotic problem for `r_n(epsilon)` in the Hilbert
case, nor the infinite-dimensional-domain question in the same source section.
The supporting paper itself still says that the best known Hilbert-to-Hilbert
bound for `r^{ell_2^n -> ell_2}(1/4)` has the same asymptotic form as the
general lower bound.

## Verification Notes

- Cheap-index searches for `1510.00276`, the paper title, `affine
  approximation`, `quantitative differentiation`, and `UMD targets` found no
  prior packet for this source paper.
- The only nearby registry hit was arXiv:1608.01915 Question 19 / `Q:proj
  lip`, a different affine-projection subproblem.
- The source arXiv v2 includes an `Added in proof` note pointing to the
  forthcoming work that became arXiv:1608.01915; the answer evidence used here
  is the separate later paper's Theorem 1 and explicit "answers Question 8"
  sentence.

Human-review recommendation: accept as a scoped literature-already-answered
packet for `Q:UC`, while leaving the other open questions from arXiv:1510.00276
available for future targeted attacks.
