# Sharpened Asplund Averaging for AUS/AUC Power Types

Result type: `partial`

Status: candidate partial result, likely valid pending human review.

Source paper:

- Stephen J. Dilworth, Denka Kutzarova, Gilles Lancien, Lovasoa N.
  Randrianarivony, "Equivalent norms with the property `(beta)` of
  Rolewicz", arXiv:1506.07978.
- Local source PDF: `source_paper.pdf`
- Open-question evidence crop: `figures/open_problem_crop.png`

## Claimed Contribution

Remark 4.4 of the source paper asks whether, if a reflexive Banach space
admits one equivalent AUS norm of power type `p` and another equivalent AUC
norm of power type `q`, one can find a single equivalent norm preserving both
power types together. Lemma 4.3 of the paper proves a simultaneous norm with
AUS power type `p` and AUC power type `4q`.

This packet proves a sharpened partial result: for every `r > 2q`, the same
hypotheses give an equivalent norm which is simultaneously AUS of power type
`p` and AUC of power type `r`.

The result does not answer the exact-preservation question, since the target
would be AUC power type `q`. It improves the exponent loss obtainable from the
paper's Asplund averaging scheme.

## Files

- `main.tex`: self-contained LaTeX packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of the original arXiv PDF.
- `figures/open_problem_crop.png`: full-width crop of Remark 4.4 on page 10.
- `tmp/`: LaTeX build intermediates and disposable render outputs.

## Verification Notes

No computational checker is involved. The proof is a renorming argument.

The key reviewer point is the tail estimate in the AUC part. For the norms
used in Lemma 4.3, every tail index `n >= n0` gives a uniform `t^q` gain once
`n0` is chosen of order `t^{-q}`. Summing these gains against weights
`n^{-theta}` gives `t^{q theta}`. Since the AUS estimate requires
`sum n^{1-theta}<infty`, one needs `theta>2`, yielding every exponent above
`2q`.

## Human Review Notes

Recommended focus:

- Check that the source paper's estimate
  `rho_{||.||_n}(t) <= C n t^p` is inherited unchanged with weights
  `n^{-theta}`.
- Check the AUC tail summation, especially the comparison
  `(1-1/n)N(x+y) >= ||x||_n + c t^q` for all `n >= n0`.
- Confirm whether the same improvement is already present in later literature.

Bounded novelty/status check performed: cheap run indexes, local parsed arXiv
sources for the exact phrase "preserve both power types" and AUS/AUC power-type
phrases, plus web searches for close variants. No exact later answer or this
tail-summed exponent improvement was found in that bounded search.
