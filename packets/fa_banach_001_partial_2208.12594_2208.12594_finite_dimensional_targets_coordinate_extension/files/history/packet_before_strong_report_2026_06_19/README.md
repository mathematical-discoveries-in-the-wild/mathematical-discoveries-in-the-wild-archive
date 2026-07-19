# Partial Result: Finite-Dimensional Targets for Banach-Valued Sobolev Extensions

Run: `fa_banach_001`

Result type: `partial`

Status: `partial_result_likely_valid`

Source paper: Miguel Garcia-Bravo, Toni Ikonen, and Zheng Zhu,
*Extensions and approximations of Banach-valued Sobolev functions*,
arXiv:2208.12594.

## Source Question

Question 1.1 of arXiv:2208.12594 asks whether, for `1 < p < infinity` and a
`p`-PI space `Z`, every real-valued `W^{1,p}`-extension set `Omega subset Z`
is automatically a `V`-valued `W^{1,p}`-extension set for every Banach space
`V`.

The source paper notes that the obvious componentwise strategy is problematic
for infinite-dimensional targets such as `ell^\infty`: even if one extends
coordinates, it is not clear that the resulting sequence-valued map is an
`L^p` function or has Sobolev regularity.

## Result

For finite-dimensional targets, the componentwise obstruction disappears.

If `Omega` is a real-valued `W^{1,p}`-extension set in a metric measure space
`Z`, then `Omega` is a `V`-valued `W^{1,p}`-extension set for every
finite-dimensional Banach space `V`.

The proof first treats `V = ell_\infty^n`. For
`u = (u_1,...,u_n)`, extend each coordinate by a fixed real-valued extension
operator. The vector extension has `L^p` norm controlled by the finite sum of
the coordinate norms, and the maximum of the coordinate upper gradients is an
upper gradient for the vector map. An arbitrary finite-dimensional `V` is then
handled by a linear isomorphism `V -> ell_\infty^n`.

## Scope

- This is a narrow finite-dimensional target subcase of Question 1.1.
- It does not address `c_0`, `ell^\infty`, arbitrary separable targets, or
  general infinite-dimensional Banach spaces.
- It does not provide a geometric characterization of real-valued extension
  sets.
- The source paper already proves stronger positive results under additional
  geometric hypotheses, and proves that `c_0` is a universal target if one
  assumes `c_0`-valued extendability. This packet records only the elementary
  finite-dimensional consequence from real-valued extendability.

## Evidence

- `source_paper.pdf`: local copy of arXiv:2208.12594.
- `figures/open_problem_crop.png`: screenshot crop of Question 1.1 and the
  componentwise-obstruction paragraph.
- `main.tex` / `solution_packet.pdf`: proof packet.

## Search Bounds

Before promotion, the cheap run indexes were searched for `2208.12594`,
`Banach-valued Sobolev`, `finite-dimensional target`, `componentwise
extension`, `real-valued extension set`, and related extension terms. No prior
packet for this target was found. A web/arXiv search on June 15, 2026 for
finite-dimensional Banach-valued Sobolev extension variants found the source
paper itself, but no separate later paper recording this exact finite-
dimensional target subcase.

## Human Review Recommendation

Review as a small, likely folklore partial theorem. The main technical point
to verify is that the source paper's Newton--Sobolev convention permits the
coordinatewise upper-gradient estimate exactly as used here; this is standard
and also follows from the source paper's Lipschitz postcomposition facts.
