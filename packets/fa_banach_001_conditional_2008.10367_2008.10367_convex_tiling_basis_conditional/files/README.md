# Conditional packet: convex normal tilings for Schauder-basis spaces

- Status: `conditional_reduction`
- Source paper: arXiv:2008.10367, Robert Deville and Mar Jimenez-Sevilla, "Normal and starlike tilings in separable Banach spaces".
- Target question: whether every separable Banach space, finite or infinite dimensional, admits a `K`-normal convex tiling with `K` independent of the space and norm.
- Packet path: `runs/fa_banach_001/solutions/conditional/2008.10367_convex_tiling_basis_conditional/`

## Result

The packet proves the following conditional reduction.

If `X` has a Schauder basis with uniformly bounded partial-sum projections
`B = sup_k ||P_k||`, and the finite-dimensional initial spans
`V_k = span(e_1,...,e_k)` admit convex normal tilings with a uniform normality
constant `S`, then `X` admits a convex normal tiling.

Consequently, a positive solution of the finite-dimensional uniform
convex-normal tiling problem would imply a positive solution for every Banach
space with a monotone Schauder basis, with a universal constant depending only
on the finite-dimensional constant and on the fixed constants in the source
construction.

## Conditional Dependency

The unproved dependency is the finite-dimensional uniform convex-normal tiling
conjecture, or more locally the boundedness of the convex-normal tiling
constants of the basis initial spans `V_k`.

This packet does not prove the finite-dimensional conjecture and must not be
counted as a full solution of the source open problem.

## Verification

- Source PDF rendered locally from the arXiv TeX source.
- Open problem crop: `figures/open_problem_crop.png`.
- LaTeX packet: `main.tex`.
- Rendered packet: `solution_packet.pdf`.
- No computational proof code was used.

## Human Review Recommendation

Check the extension of Proposition 2.6 in the source paper from finitely many
layers to all layers under `sup_k ||P_k|| < infinity` and `sup_k tau(V_k) <
infinity`. The key point is that the proof of Proposition 2.6 only uses
finiteness to bound these two quantities.
