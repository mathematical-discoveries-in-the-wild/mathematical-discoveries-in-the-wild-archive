# Strong Partial Report: Banach-Valued Sobolev Extension Sets

Run: `fa_banach_001`

Result type: `partial`

Status: `strong_partial_result_likely_valid`

Source paper: Miguel Garcia-Bravo, Toni Ikonen, and Zheng Zhu,
*Extensions and approximations of Banach-valued Sobolev functions*,
arXiv:2208.12594.

## Source Question

Question 1.1 asks whether, for `1 < p < infinity` and a `p`-PI metric measure
space `Z`, every real-valued `W^{1,p}`-extension set `Omega subset Z` is
automatically a `V`-valued `W^{1,p}`-extension set for every Banach space `V`.

## Current Packet

This packet replaces the older finite-dimensional-only note with a stronger
bookkeeping report.

Verified content:

- The finite-dimensional coordinate-extension result is correct and now stated
  quantitatively.
- No Poincare, doubling, completeness, or measure-density hypothesis is needed
  for that finite-dimensional result.
- If a Euclidean scalar extension domain has a bounded linear scalar extension
  operator, then it extends to targets isomorphic to complemented subspaces of
  an `L^p` space.
- In particular, in the Euclidean setting this covers `L^p` targets, `ell^p`,
  and arbitrary Hilbert spaces.
- A concrete `c0`-valued Lipschitz map on an interval shows why finite-rank
  approximation/truncation does not by itself upgrade the finite-dimensional
  proof to `c0`.

Literature status recorded in the packet:

- No full proof or counterexample was found.
- A May 2026 paper by the same authors still identifies the Euclidean range
  `1 <= p < n` as open, so the full Question 1.1 should not be treated as
  solved.

## Files

- `main.tex`: active strengthened packet.
- `solution_packet.pdf`: rendered active packet.
- `source_paper.pdf`: local copy of arXiv:2208.12594.
- `figures/open_problem_crop.png`: screenshot crop of Question 1.1 and the
  componentwise-obstruction paragraph.
- `history/packet_before_strong_report_2026_06_19/`: previous active
  finite-dimensional-only packet.
- `evidence/supplied_banach_sobolev_extension_report_2026_06_19/`: supplied
  TeX/PDF report used to build this active packet.

## Human Review Recommendation

Review as a strong partial result, not as a full answer. The most important
checks are the quantitative finite-dimensional constants, the Sobolev--Fubini
identification for `L^p` targets, and the `c0` truncation obstruction.
