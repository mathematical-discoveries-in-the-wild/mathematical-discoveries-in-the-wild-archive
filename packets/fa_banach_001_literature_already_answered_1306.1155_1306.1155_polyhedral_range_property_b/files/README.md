# Literature-Already-Answered Packet: Polyhedral Subcase of Property B

Run: `fa_banach_001`

Result type: `literature_already_answered`

Status note: this is a literature-known proper subcase of Martin's Question 9,
not an answer to the full finite-dimensional problem and not a new partial
result from this run.

## Source Problem

- Miguel Martin, *Norm-attaining compact operators*, arXiv:1306.1155.
- Local PDF: `source_paper.pdf`.
- Evidence images:
  - `figures/open_problem_crop.png` (page 4, Question 9).
  - `figures/open_problem_continuation_crop.png` (page 5, comment that the problem is open even for the two-dimensional real Hilbert space).

Question 9 asks whether, for every finite-dimensional space `Y` and every
Banach space `X`, `NA(X,Y)` is dense in `L(X,Y)`.

## Supporting Literature

- Vladimir Kadets, Gines Lopez, Miguel Martin, Dirk Werner, *Norm attaining
  operators of finite rank*, arXiv:1905.08272.
- Local PDF: `supporting_paper_1905.08272.pdf`.
- Evidence images:
  - `figures/supporting_polyhedral_known_crop.png` (page 1, recalling
    Lindenstrauss's examples with property `B`, including finite-dimensional
    polyhedral spaces).
  - `figures/supporting_full_problem_open_crop.png` (page 2, stating that
    whether all finite-dimensional Banach spaces have property `B` is a major
    open question).

## Literature Status

The real finite-dimensional polyhedral subcase is already known in the
literature. The 2019 supporting paper recalls that Lindenstrauss showed
finite-dimensional polyhedral spaces have property `B`.

Equivalently, every real finite-dimensional polyhedral Banach space has
Lindenstrauss property `B`: for every real Banach space `X`,
norm-attaining operators `X -> Y` are dense in `L(X,Y)`.

This does not answer Martin's full Question 9, since the supporting paper also
states that the all finite-dimensional problem remains a major open question.

## Proof Idea

For polyhedral `Y`, the dual unit ball has finitely many extreme points.
Thus the norm of an operator `T:X -> Y` is the maximum of finitely many
scalar norms `||phi T||`. Choose a dual extreme point `phi_0` at which this
maximum is attained. Because the dual ball is a polytope, `phi_0` can be
exposed by a vector `y_0 in S_Y`, and all other non-opposite extreme
functionals see `y_0` with modulus strictly less than one.

Now slightly enlarge the scalar functional `phi_0 T`, approximate that
enlarged scalar functional by a norm-attaining functional using the
Bishop-Phelps theorem, and correct `T` only in the `y_0` direction. The
finite exposure gap keeps every other dual extreme coordinate strictly
below the corrected `phi_0` coordinate, so the corrected vector-valued
operator attains its full norm.

## Limitations

- This is a known proper subcase for real polyhedral finite-dimensional ranges
  only.
- It does not address smooth finite-dimensional ranges, especially the
  two-dimensional real Hilbert space mentioned in the source paper.
- It should not be counted as a new partial result from this run.

## Files

- `README.md`: this packet summary.
- `main.tex`: literature-status/proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source paper.
- `supporting_paper_1905.08272.pdf`: supporting literature source.
- `figures/open_problem_crop.png`: source Question 9 crop.
- `figures/open_problem_continuation_crop.png`: source continuation crop.
- `figures/supporting_polyhedral_known_crop.png`: supporting known-subcase crop.
- `figures/supporting_full_problem_open_crop.png`: supporting full-problem-open crop.
- `tmp/`: LaTeX build intermediates.

## Human Review Recommendation

Treat this as duplicate/literature-known status for the polyhedral subcase only.
The packet should not be used as evidence that the full finite-dimensional
property `B` problem is solved.
