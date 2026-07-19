# Full As-Stated Solution Packet: The Mixed Composition Inequality

Run: `fa_banach_001`

Status: `candidate_full_as_stated_second_alternative`

Model: `GPT5.6`

## Source Problem

- Vitali Milman and Liran Rotem, *Novel view on classical convexity theory*,
  arXiv:2005.11253v1 (2020).
- Source location: Problem 4.1, source PDF page 13.
- Local source: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

Problem 4.1 asks for which convex bodies `T` either of two composition
Brunn--Minkowski inequalities holds. This packet completely classifies the
second alternative exactly as printed. Its last right-hand term uses the
support composition `T circ K_2`, while the other two terms use the radial
composition `T odot (...)`.

## Result

Assume `T` is a full-dimensional convex body in `R^n` containing the origin.

- If `n >= 2`, the printed mixed inequality holds for every pair `K_1,K_2`
  if and only if `T` is a centered Euclidean ball `s B_2^n`.
- If `n = 1`, every interval containing the origin works, and equality always
  holds.

The proof is short. Substitute `K_1=tB_2^n` and `K_2=B_2^n`. Since
`T odot B_2^n=T`, the inequality forces `T` and
`conv{h_T(u)u : u in S^{n-1}}` to have the same volume. The former is
contained in the latter because `r_T <= h_T`, so the bodies are equal. Every
point `h_T(u)u` therefore lies in `T`, giving the reverse inequality and hence
`r_T=h_T` pointwise. In dimension at least two, a geodesic subdivision
argument forces this common radial/support function to be constant.

## Scope Warning

The asymmetry of the displayed source formula is essential. If the final
`T circ K_2` was a typographical error intended to read `T odot K_2`, this
packet does not solve that corrected symmetric radial-composition problem.
The first, all-`circ` alternative also remains open here.

## Verification

- The proof uses only the definitions in the source paper, elementary convex
  body facts, Hausdorff convergence, and the ordinary Brunn--Minkowski
  inequality for the converse.
- `code/numerical_reconnaissance.py` records the polygonal experiments that
  exposed the importance of the mixed final term. Run with
  `conda run --no-capture-output -n sandbox python code/numerical_reconnaissance.py`.
  Its default deterministic sweep checks 22,324 polygon pairs across support
  and radial modes and finds failures for several nonball multipliers. These
  approximate tests motivated the exact argument but are not used in the proof.
- The LaTeX log was checked for layout/reference warnings, and every rendered
  packet page was visually inspected.

## Novelty Check

On 19 July 2026 the run registry, solution, attempt, and proof-gap indexes were
searched for arXiv:2005.11253, the paper title, composition of convex bodies,
and the mixed radial/support inequality. A bounded arXiv search for the exact
paper and close phrases returned the source paper but no later answer to
Problem 4.1. Novelty confidence is therefore moderate, subject especially to
human confirmation that the printed mixed formula was intentional.

## Files

- `main.tex`, `solution_packet.pdf`: full proof packet.
- `source_paper.pdf`: official arXiv PDF.
- `figures/open_problem_crop.png`: full-width crop of Problem 4.1.
- `code/numerical_reconnaissance.py`: exploratory polygon computation.
- `tmp/`: build and rendered-page intermediates.

## Human Review Recommendation

Verify the one-line ball substitution, the implication from equality of the
nested bodies to `r_T=h_T`, and the scope distinction between the literal
mixed formula and the likely symmetric `odot` variant. Mathematically the
as-printed classification is complete.
