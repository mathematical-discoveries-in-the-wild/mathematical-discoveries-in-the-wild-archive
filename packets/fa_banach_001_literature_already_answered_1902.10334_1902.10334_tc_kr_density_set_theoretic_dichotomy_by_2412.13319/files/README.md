# Literature Already Answered: Set-Theoretic Dichotomy for TC/KR Density

Run: `fa_banach_001`

Status: `literature_already_answered_by_2412.13319`

## Source Problem

- Sofiya Ostrovska and Mikhail I. Ostrovskii,
  *Generalized transportation cost spaces*, arXiv:1902.10334.
- Source location: Theorem 1.13 and Remark 1.14, PDF page 11;
  parsed source `data/parsed/arxiv_sources/1902.10334/source.tex`,
  lines 680--746.

The source proves that, for Polish metric spaces, finitely supported
transportation problems `TP(M)` are dense in the Kantorovich-Rubinstein
measure space. Remark 1.14 says that the authors do not know how to prove an
analogue for general metric spaces.

## Supporting Literature

- Lucas Maciel Raad,
  *A Characterization of Borel Measures which Induce Lipschitz-Free Space
  Elements*, arXiv:2412.13319, v4 dated 2025-11-23.
- Decisive statements: Theorem 3.6 and Corollary 3.7, with Theorem 2.16.

Raad does not explicitly cite this Ostrovska-Ostrovskii remark in the local
packet. However, his theorem gives the exact characterization needed for the
source question: the completion of `TP(M)` is the Lipschitz-free space `F(M)`,
and a finite signed measure with finite first moment is approximable by
finitely supported transportation problems exactly when its integration
functional lies in `F(M)`.

## Implied Answer

Let `kappa_rvm` denote the least real-valued measurable cardinal, if it exists.
The general-metric analogue has the following sharp set-theoretic form.

- If there is no nontrivial measure on the weight of `M` (in particular if
  `w(M) < kappa_rvm`, or if no real-valued measurable cardinal exists), every
  finite Borel measure on `M` is concentrated on a separable subset. Then the
  Polish theorem applies after passing to the completion of that separable
  support, so `TP(M)` is dense in the KR measure space for `M`.
- If the weight of `M` carries a nontrivial measure (in particular, under the
  existence of a real-valued measurable cardinal, for metric spaces of weight
  at least `kappa_rvm`), Raad's Corollary 3.7 gives a finite-first-moment Borel
  measure whose integration functional is not in `F(M)`. Equivalently,
  `mu - mu(M) delta_0` is a KR measure element that cannot be approximated by
  `TP(M)`, even in the weaker Lipschitz-dual norm.

Thus the unrestricted general case is not a plain ZFC theorem in the naive
form. It is true below the real-valued-measurable threshold, and it fails above
that threshold if such a cardinal exists.

## Files

- `main.tex`: compact status note and proof bridge.
- `solution_packet.pdf`: rendered note.
- `source_paper.pdf`: source arXiv:1902.10334 PDF.
- `supporting_paper_2412.13319.pdf`: Raad supporting paper.
- `figures/open_problem_crop.png`: source page containing Remark 1.14.
- `figures/supporting_answer_page-08.png` through
  `figures/supporting_answer_page-10.png`: rendered supporting pages containing
  Theorem 3.6 and Corollary 3.7.
- `history/1902.10334_tight_measure_tc_kr_density_partial_2026_06_16/`:
  previous active tight-measure partial packet, now absorbed as a special case.

## Verification

The packet was checked against the source theorem/remark and against Raad's
Theorem 2.16, Theorem 3.6, and Corollary 3.7. The LaTeX note was compiled with
`latexmk`, rendered with `pdftoppm`, and visually inspected.
