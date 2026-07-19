# Ferenczi--Galego Question 19 is answered by Cuellar-Carrera

Status: `literature_already_answered_with_adjacent_strengthening`

Run: `fa_banach_001`  
Agent: `agent_lane_07`  
Source target: arXiv `0704.1459`, Ferenczi--Galego, *Even infinite dimensional real Banach spaces*

## Literature Answer

Ferenczi--Galego Question 19 asks whether there exists a Banach space with exactly `omega` complex structures. This exact question is answered positively by Cuellar-Carrera, arXiv `1401.1781`, Corollary 9: for every limit ordinal `omega^2 <= gamma < omega_1`, the space `X_gamma(C)` has exactly countably infinitely many complex structures.

## Adjacent Strengthening Preserved Here

The packet also records a likely valid adjacent strengthening: Cuellar-Carrera's separable examples `X_gamma(C)` can be chosen even in the sense of Ferenczi--Galego. More precisely, for every limit ordinal `omega^2 <= gamma < omega_1`, the real Banach space `X_gamma(C)` is even and has exactly countably infinitely many complex structures.

This strengthening is retained as useful provenance, but the folder is classified as `literature_already_answered` because the original target question is already solved in the literature.

## Packet Files

- `main.tex` - proof packet.
- `solution_packet.pdf` - rendered packet.
- `source_paper.pdf` - Ferenczi--Galego source paper.
- `supporting_paper_1401.1781.pdf` - Cuellar-Carrera supporting paper.
- `figures/open_problem_crop.png` - source Question 19 crop.
- `figures/supporting_cuellar_crop.png` - supporting Corollary 9 / Proposition 10 crop.

## Proof Mechanism

The proof combines:

- Ferenczi--Galego's lifting criterion: a real space has no complex structures on its hyperplanes when the strictly singular ideal has the lifting property.
- Cuellar-Carrera's diagonal decomposition on `X_{omega_1}(C)`.
- The same initial-interval extension trick used in Cuellar-Carrera's proof of Corollary 9.

Given a real-linear `T` on `X_gamma(C)` with `T^2 + Id` strictly singular, extend it to `X_{omega_1}(C)` by `T P_I + i P^I`. Cuellar-Carrera's Remark 7 and diagonal decomposition produce an exact diagonal complex structure modulo strictly singular operators. Restricting the diagonal back to `X_gamma(C)` proves the lifting property there.

## Review Notes

Main reviewer focus for the adjacent strengthening: use Cuellar-Carrera's diagonal construction preceding Proposition 3, Proposition 3 itself, and Remark 7 for the modulo-strictly-singular square condition. The exact Question 19 literature answer does not depend on this strengthening.

Remaining open territory: this does not settle the direct-sum question for arbitrary even Banach spaces or the projection-total-incomparability questions in the Ferenczi--Galego paper.
