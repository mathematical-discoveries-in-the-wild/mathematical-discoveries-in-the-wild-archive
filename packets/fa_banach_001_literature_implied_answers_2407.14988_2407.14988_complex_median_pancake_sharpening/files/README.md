# 2407.14988 complex median pancake sharpening

status: `literature_implied_answer (complex median lemma sharpening; not main open problem)`

## Source

- Source paper: Feng, Wang, Zhou, "On the boundedness and Schatten class property of noncommutative martingale paraproducts and operator-valued commutators", arXiv:2407.14988.
- Source location: Theorem 1.9 / TeX label `divideS`, with the proof in Section 8. The theorem states that for a measurable complex-valued function on a finite-measure set there are two orthogonal lines whose four closed quadrants each capture at least `1/16` of the mass. The source later remarks that a simple-functions-plus-limit proof route is not clear to the authors.

## Supporting literature

- Fakhrutdinov and Musin, "Algorithms for orthogonal partitioning into four parts", arXiv:2511.20866v2.
- Supporting location: introduction and Theorem 1. The paper recalls the planar second pancake theorem: a finite-area planar mass can be cut by two perpendicular straight lines into four equal pieces, and proves an optimal linear-time finite-point version.

## Identification

The complex median lemma is exactly a planar orthogonal equipartition statement for the pushforward measure `b_#(mu|I)` on `C = R^2`. Applying the second pancake theorem, and using the closed-quadrant formulation to pass to arbitrary finite Borel measures by weak approximation, improves the source constant from `1/16` to the optimal `1/4`.

The supporting paper does not explicitly target arXiv:2407.14988; this is an agent-identified implication of the classical orthogonal equipartition theorem.

## Scope

This packet only sharpens the geometric complex-median lemma and supplies the missing limit route alluded to after the source proof. It does not settle the paper's main open noncommutative paraproduct boundedness problem, and it does not settle the low-`p` endpoint range for Theorem 1.6 when `n=1`.

## Files

- `main.tex`: compact LaTeX status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: local copy of arXiv:2407.14988.
- `supporting_paper_2511.20866.pdf`: local copy of arXiv:2511.20866.

## Ledger

Ledger record: `runs/fa_banach_001/ledger/results/2407.14988_complex_median_pancake_sharpening.json`.
