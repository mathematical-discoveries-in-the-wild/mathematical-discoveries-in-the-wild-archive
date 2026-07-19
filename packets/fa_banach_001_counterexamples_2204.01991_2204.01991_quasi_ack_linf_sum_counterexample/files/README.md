# Counterexample: Quasi-ACK `ell_infty` Sum Stability

Result type: `counterexample`

Status: counterexample likely valid pending human review.

Source paper:

- Geunsu Choi and Mingu Jung, "A generalized ACK structure and the denseness
  of norm attaining operators", arXiv:2204.01991.
- Source question: Remark 3.4 asks whether quasi-ACK structure and property
  quasi-beta are stable under `ell_infty`-sums; Remark 4.8 repeats the
  quasi-ACK family case.
- Local source PDF: `source_paper.pdf`.
- Open-problem evidence crop: `figures/open_problem_crop.png`.

## Upgrade Incorporated

The supplied report
`evidence/supplied_quasi_ack_linf_counterexample_2026_06_23/quasi_ack_linf_counterexample.tex`
promotes the previous partial packet to a negative answer for the unrestricted
real case. The old packet proved a positive uniform subcase: if all active
quasi-ACK rho-values are bounded away from `1`, then the `ell_infty`-sum has
ACK_r structure. That packet is preserved under
`history/previous_uniform_quasi_ack_linf_sum_2026_06_23/`.

## Claimed Counterexample

The packet constructs two-dimensional real regular-polygon spaces `X_n`.
Each `X_n` has property beta, hence quasi-ACK structure, with ACK constants
`rho_n = cos(pi/m_n)` tending to `1`. For
`Z = (oplus_n X_n)_{ell_infty}`, the proof identifies extreme points of
`B_{Z^*}` through ultrafilter fibers. Free ultrafilters see the Euclidean limit
of the polygon norms, and a localization consequence of the quasi-ACK axioms
contradicts the round geometry of that limit fiber.

Thus arbitrary `ell_infty`-sum stability fails for quasi-ACK structure and, by
property quasi-beta implying quasi-ACK structure, also for property
quasi-beta over the real field.

## Scope

This packet gives a real counterexample to the unrestricted source questions.
It does not claim a complex counterexample. The former uniform positive
subcase remains valid and explains the obstruction: the counterexample is
genuinely nonuniform, with constants tending to `1`.

## Files

- `main.tex`: consolidated counterexample packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2204.01991.
- `figures/open_problem_crop.png`: crop of Remark 3.4 and surrounding context.
- `evidence/supplied_quasi_ack_linf_counterexample_2026_06_23/`: supplied TeX
  report.
- `history/previous_uniform_quasi_ack_linf_sum_2026_06_23/`: previous active
  partial packet.
- `tmp/`: LaTeX build intermediates and rendered verification pages.

## Human Review Notes

Verifier focus:

- Check the extreme-point formula for the dual ball of the `ell_infty`-sum via
  ultrafilter support.
- Check that free ultrafilter fibers are the Euclidean limit of the polygonal
  norms.
- Check the localization inequality derived from quasi-ACK condition (iv)' and
  (v)'.
- Check the final angle estimates in the free and principal fiber cases.

No computational verification is needed.
