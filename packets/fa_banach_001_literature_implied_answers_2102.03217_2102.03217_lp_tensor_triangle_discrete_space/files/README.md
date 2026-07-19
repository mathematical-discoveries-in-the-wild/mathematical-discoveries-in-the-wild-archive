# Literature-Implied Partial Answer: tensor-product `L^p` discrete spaces

Status: `literature_implied_answer (partial subcase)`

Source target: arXiv:2102.03217, Debrouwere-Prangoski, "Gabor frame characterisations of generalised modulation spaces", Problem 3.19.

Problem 3.19 asks for an explicit description of

```text
(L^{p1} \hat{\otimes}_tau L^{p2})^{B0}_d(Λ1 × Λ2)
```

for `tau = pi` or `epsilon` and `1 <= p1,p2 < infinity`.

Identified partial answer:

- For `tau = pi` and `1 <= p1 <= p2 <= 2`,
  `(L^{p1} \hat{\otimes}_pi L^{p2})^{B0}_d(Λ1 × Λ2)`
  is topologically `ell^1(Λ1; ell^{p2}(Λ2))`.
- For `tau = epsilon` and `2 <= p2 <= p1 < infinity`,
  `(L^{p1} \hat{\otimes}_epsilon L^{p2})^{B0}_d(Λ1 × Λ2)`
  is topologically `c_0(Λ1; ell^{p2}(Λ2))`.

This is not presented as an original new proof. It is an agent-identified implication of:

- the Gabor coefficient theorem in the source paper, especially Corollary 4.11;
- Feichtinger-Pilipovic-Prangoski, arXiv:2012.12295, Corollary 6.1 and Remark 6.2, identifying the corresponding tensor-product modulation spaces;
- the standard Gabor coefficient descriptions of `W(FL^p,L^1)` and `W(FL^p,L^\infty_0)`.

Remaining open: Problem 3.19 outside these exponent regions, and any sharper direct description avoiding the modulation-space/Gabor-frame reformulation.

Files:

- `main.tex` - compact status note.
- `solution_packet.pdf` - rendered note.
- `source_paper.pdf` - arXiv:2102.03217.
- `supporting_paper_2012.12295.pdf` - decisive supporting tensor-product modulation paper.
