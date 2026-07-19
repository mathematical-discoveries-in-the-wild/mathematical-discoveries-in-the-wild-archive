# Strengthened Partial Packet: Tail Localization for Question 6.17(2)

Run: `fa_banach_001`

Result type: `partial`

Status: `strong_partial_likely_valid`

## Source Problem

- W. Cuellar Carrera, N. de Rancourt, and V. Ferenczi,
  *Local Banach-space dichotomies and ergodic spaces*, arXiv:2005.06458.
- Local PDF: `source_paper.pdf`.
- Location: Question 6.17, PDF page 60; parsed source
  `data/parsed/arxiv_sources/2005.06458/main.tex`, lines 2871--2885.

The packet addresses the second part of Question 6.17:

> Does every non-Hilbertian space with unconditional FDD have a non-Hilbertian
> subspace with an unconditional basis?

## Result

The previous packet proved a sufficient finite-dimensional tail-witness
condition. The 2026-06-22 upgrade repairs the old uniformity argument, removes
the inaccurate property-(H) terminology, and proves the converse relative to a
fixed unconditional FDD.

For a UFDD `(E_n)`, the packet defines the tail-witness property: there is a
constant `lambda` such that every tail contains interval-supported
finite-dimensional subspaces with normalized `lambda`-unconditional bases and
arbitrarily large Banach-Mazur distance from Euclidean space.

The strengthened theorem says this tail-witness property is equivalent, for
the fixed UFDD, to the existence of a non-Hilbertian subspace with an
unconditional basis. Consequently the result is an exact localization of
Question 6.17(2), not a full solution of the original question.

The packet also records a hard-case reduction: after passing to a tail, any
counterexample must look like a non-Hilbertian Hilbertian sum
`(\oplus E_n)_2` of finite-dimensional spaces, with unbounded Euclidean
distortion in every tail but no uniformly unconditional non-Euclidean
interval witnesses for any fixed constant. It rules out bounded-dimensional
UFDDs, uniformly unconditional blocks, uniformly Euclidean blocks, and spaces
with type/cotype exponents away from `2`.

## Remaining Open

The full Question 6.17(2) remains open. The residual finite-dimensional
principle is whether every non-Hilbertian Hilbertian sum of finite-dimensional
spaces contains uniformly unconditional interval-supported subspaces with
Euclidean distortion tending to infinity.

## Files

- `main.tex`: strengthened partial-result packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source/open-problem paper.
- `figures/open_problem_crop.png`: crop of Question 6.17.
- `evidence/2026-06-22_q617_unconditional_fdd_report/`: supplied TeX/PDF
  upgrade report.
- `history/2026-06-22_previous_uniform_tail_property_h/`: previous active
  README, LaTeX, and rendered PDF.

## Human Review Recommendation

Check Lemma 4.1, the finite-rank avoidance lemma, since it drives the converse
from an arbitrary non-Hilbertian unconditional-basis subspace back into remote
finite intervals of the original UFDD. Also check the type-cotype corollary:
it uses finite representability plus finite interval approximation to produce
uniformly unconditional witnesses.
