# Corrected Partial Packet: Simultaneous AUS/AUC Power Types

Run: `fa_banach_001`

Result type: `partial`

Status: `corrected_strong_partial_likely_valid`

## Source Problem

- S. J. Dilworth, D. Kutzarova, G. Lancien, and N. L. Randrianarivony,
  *Equivalent norms with the property (beta) of Rolewicz*, arXiv:1506.07978.
- Local source PDF: `source_paper.pdf`.
- Open-question evidence crop: `figures/open_problem_crop.png`.
- Location: Remark 4.4 on PDF page 10.

Remark 4.4 asks whether, if a reflexive Banach space admits an equivalent AUS
norm of power type `p` and, possibly under another equivalent norm, an
equivalent AUC norm of power type `q`, it must admit a single equivalent norm
with both original power types `p` and `q`.

## Upgrade Verdict

The previous packet claimed a common `p`-AUS and `r`-AUC norm for every
`r > 2q`. The 2026-06-22 audit finds that the proof used an unsupported
smoothness scaling estimate when `p > 2`: for the mixed norm associated to
`N^* + eps M^*`, the generally justified bound is of order
`eps^{-(p-1)} t^p`, not `eps^{-1} t^p`.

The old `r > 2q` conclusion is still justified by that argument when
`p <= 2`, but not for arbitrary `p`.

## Active Result

The corrected general theorem is:

- For every reflexive Banach space with separate `p`-AUS and `q`-AUC
  renormings, there is one equivalent norm which is `p`-AUS and `r`-AUC for
  every `r > pq`.

The packet also proves a barrier for positive linear Asplund averages built
from `N^* + eps_n M^*`: the method cannot reach a uniform endpoint gain of
order `t^{pq}`, let alone the exact `t^q` endpoint.

Finally, the exact endpoint has a positive answer for separable reflexive
spaces, by combining Odell-Schlumprecht tree estimates with their exact
tree-to-FDD embedding theorem and restricting the resulting FDD norm.

## Remaining Open

The exact endpoint for arbitrary nonseparable reflexive spaces remains open in
this packet. No published full answer or counterexample was located in the
bounded search recorded in `main.tex`.

## Files

- `main.tex`: corrected audit and partial-result packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of the original arXiv PDF.
- `figures/open_problem_crop.png`: full-width crop of Remark 4.4 on page 10.
- `evidence/2026-06-22_simultaneous_aus_auc_report/`: supplied TeX/PDF
  upgrade report.
- `history/2026-06-22_previous_gt_2q_packet/`: previous active README, LaTeX,
  and rendered PDF for the superseded `r > 2q` claim.

## Human Review Notes

Recommended focus:

- Check Lemma 3.1, especially the dependence
  `rho_{L_eps}(t) <= C eps^{-(p-1)} t^p`.
- Check the corrected averaging proof for `r > pq`.
- Check the deduction of the exact separable endpoint from
  Odell-Schlumprecht Proposition 3.3 and Theorem 4.1(e).
- Treat the old `r > 2q` packet as superseded except in the `p <= 2` range
  where the audit explains why its estimate remains justified.
