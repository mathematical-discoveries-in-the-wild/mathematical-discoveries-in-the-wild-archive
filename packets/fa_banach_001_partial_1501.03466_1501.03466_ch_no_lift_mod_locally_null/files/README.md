# Partial packet: CH obstruction to lifting modulo locally null operators

Status: claimed partial result, likely valid, needs human review.

Source target: Piotr Koszmider and Cristobal Rodriguez-Porras,
*On automorphisms of the Banach space `ell_infty/c_0`*, arXiv:1501.03466.

Open problem addressed: Problem 7.1 asks whether it is consistent, possibly
from PFA or OCA+MA, that every automorphism of `ell_infty/c_0` can be written
as `[R] + S`, where `[R]` is induced by an operator on `ell_infty` and `S` is
locally null.

Partial result: any automorphism with such a decomposition is somewhere
trivial. Therefore, under CH, Problem 7.1 has a negative answer, because the
source paper proves under CH that there is an automorphism of `ell_infty/c_0`
which is nowhere trivial.

This does not settle the intended PFA/OCA+MA consistency question; it records
that the proposed lifting-modulo-locally-null property implies the later
somewhere-triviality problem and fails in the CH model supplied by the source.

Files:
- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:1501.03466.
- `figures/open_problem_crop.png`: source crop for Problem 7.1.
- `figures/source_corollary_4_9_crop.png`: source crop for the liftable
  isomorphic embedding corollary.
- `figures/source_ch_theorem_6_9_crop.png`: source crop for the CH
  nowhere-trivial automorphism theorem.

Review recommendation: verify the localization step from `S` locally null to
`[R]` agreeing with `T` on an infinite coordinate subspace, and the use of
Corollary 4.9 after identifying `ell_infty(A)/c_0(A)` with `ell_infty/c_0`.
