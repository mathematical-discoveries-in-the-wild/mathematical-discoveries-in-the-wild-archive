# Complementability in the Banach weighted-composition question

Status: `partial_result_likely_valid`

Source paper: L. Abadias, F. J. Gonzalez-Dona, and J. Oliva-Maza,
*Universality arising from invertible weighted composition operators*,
arXiv:2406.02330.

## Result

The source asks whether, for the Banach Hardy/Bergman spaces
`\mathcal B = H^p` or `\mathcal A_\sigma^p`, the eigenspace
`ker(uC_\psi-\lambda I)` is complemented and contains a subspace
isomorphic to `\mathcal B`.

This packet proves the complementability half: under the hypotheses of the
source question, `\lambda I-uC_\psi` has a bounded right inverse on
`\mathcal B`, hence `ker(uC_\psi-\lambda I)` is complemented.

The second half, whether the kernel contains a copy of `\mathcal B`, remains
open here.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2406.02330.
- `figures/banach_question_crop.png`: source crop containing Theorem 5.2 and the printed question.

## Verification

The proof uses only the source paper's Banach adaptation of the Hilbert range
space argument plus an explicit bounded splitting of
`\mathcal B = \mathcal B_{\mu,0} + \mathcal B_{0,\nu}`. Human review should
check that the inverses on the two range spaces are indeed bounded in the
Banach versions of the source proof; this follows from the same spectral
exclusion used to prove surjectivity.
