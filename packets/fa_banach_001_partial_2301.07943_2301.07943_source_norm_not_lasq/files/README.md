# Strengthened Partial Result: LASQ versus D2P

Source paper: Jose Rodriguez and Abraham Rueda Zoca, *On weakly almost square
Banach spaces*, arXiv:2301.07943.

Result type: `partial`

Status: `candidate_partial_likely_valid`, pending human review.

## Source Question

The source paper asks whether there exists a locally almost square (LASQ)
Banach space which fails the diameter two property (D2P). It then proves that
every Banach space containing a complemented copy of `c0` admits an equivalent
norm with slice-D2P, arbitrarily small relatively weakly open subsets of the
unit ball, and `(r,s)`-SQ for all `r,s < (1-epsilon)/(1+epsilon)`.

The full LASQ-versus-D2P question remains open in this packet.

## Upgraded Contribution

The supplied June 22 note strengthens the earlier June 15 obstruction packet.
It verifies the fixed-`epsilon` obstruction and sharpens it:

- The source fixed-`epsilon` ball satisfies a symmetric leakage inequality
  controlling second-coordinate mass near the faces `L = +/-1`.
- Every tree generator `+/- (x_alpha,0)`, not just the root, is quantitatively
  strongly extreme.
- The actual full norm constructed in the proof of the source Theorem 1.2 is
  not LASQ for any fixed `0 < epsilon < 1`.
- Two later LD2P-without-D2P candidate constructions are also not LASQ by
  explicit strong-extremity arguments.
- If `X` is LASQ and a basic weakly open subset of `B_X` is determined by a
  rank `r` operator, then its diameter is at least `2/(r+1)`.

## Why This Is Still Partial

The result rules out the source fixed-parameter route and several nearby
candidate constructions. It does not construct a LASQ space failing D2P, and it
does not prove that every LASQ space has D2P. The remaining bottleneck is the
net-LASQ mechanism: finding almost-square directions that are simultaneously
small under finitely many functionals.

## Files

- `source_paper.pdf`: original arXiv PDF.
- `figures/open_question_crop_page3.png`: crop containing the LASQ/D2P
  question.
- `figures/theorem_1_2_crop_page4.png`: crop containing the source theorem
  whose construction is being obstructed.
- `evidence/2026_06_22_lasq_d2p_research_note/`: supplied TeX/PDF report.
- `history/previous_root_obstruction_2026_06_15/`: previous active packet.
- `main.tex`: strengthened packet source.
- `solution_packet.pdf`: rendered strengthened packet.
- `tmp/`: LaTeX build intermediates and rendered verification pages.

## Duplicate Check

The run indexes were searched for `2301.07943`, `weakly almost square`,
`locally almost square`, `LASQ`, `WASQ`, `D2P`, and diameter-two phrases. The
only active exact packet was this one, and it did not yet contain the supplied
June 22 evidence, symmetric leakage theorem, all-tree-generator theorem, full
source-norm obstruction, later-candidate exclusions, or finite-rank lower bound.

Kalenda's separate arXiv:2505.12893 Schur-constant packet was checked because a
mixed Kalenda attachment was supplied. It is already recorded as
`human_verified_AHA` in the registry under
`human_verified/verified_AHA/2505.12893_p_schur_constant_optimal/`; the older
finite-sum packet is archived inside the full packet history.

## Human Review

Recommended checks: verify the symmetric leakage inequality on the generators
of the source ball, the `ell_infty`-sum LASQ lemma used to pass from the core
renorming to the full source norm, and the finite-rank lower bound over
extreme points of the finite-dimensional image `overline{T(B_X)}`.
