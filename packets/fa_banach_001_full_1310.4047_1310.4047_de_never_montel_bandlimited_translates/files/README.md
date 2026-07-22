# Full negative answer: `D_E` is never Montel

**Status:** claimed full solution, likely valid, pending human review.

This packet answers Remark 6 of Pavel Dimovski, Stevan Pilipović, and Jasson
Vindas, *New distribution spaces associated to translation-invariant Banach
spaces* ([arXiv:1310.4047](https://arxiv.org/abs/1310.4047)). Under all of the
source paper's hypotheses, the associated Fréchet space `D_E` is not Montel.

The construction takes a nonzero band-limited Schwartz function `phi` and the
normalized translates

```text
g_x = T_x phi / ||T_x phi||_E.
```

Fourier cutoffs express every derivative of `phi` as a fixed
`L^1_omega`-convolution of `phi`. The convolution-module estimate therefore
makes `{g_x}` bounded in every `D_E` seminorm. The inverse translation estimate
shows that the normalization grows at most polynomially, while Schwartz
correlations decay faster than any polynomial. Hence `g_x -> 0` in `S'` as
`|x| -> infinity`, although `||g_x||_E = 1`. No sequence tending to infinity
can have a `D_E`-convergent subsequence.

The packet includes Debrouwere's later paper
([arXiv:1901.10041](https://arxiv.org/abs/1901.10041)), which proves the result
for solid TIBDs and explicitly states that the general case was still open.
A bounded search through 22 July 2026 found no later general resolution.
Novelty confidence is moderate to high, not exhaustive.

## Files

- `solution_packet.pdf` - typeset proof and review notes
- `main.tex` - LaTeX source
- `VERIFICATION.md` - proof audit and novelty-search record
- `source_paper.pdf` - arXiv:1310.4047
- `supporting_paper_1901.10041.pdf` - later partial result and status evidence
- `figures/open_problem_crop.png` - Remark 6 on source-paper page 17
- `code/crop_source_evidence.py` - reproducible crop helper

The separate barreledness question in source Remark 7 remains untouched.
