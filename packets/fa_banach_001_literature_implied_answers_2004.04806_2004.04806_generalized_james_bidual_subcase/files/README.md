# Literature-Implied Partial Subcase: Generalized James Targets

Source paper: Florent P. Baudier, Gilles Lancien, Pavlos Motakis, and
Thomas Schlumprecht, *Coarse and Lipschitz universality*,
arXiv:2004.04806.

Supporting paper: Stephen Jackson, Cory Krause, and Bunyamin Sari,
*On coarse geometry of separable dual Banach spaces*, arXiv:2501.01561.

Result type: `literature_implied_answer (partial subcase)`.

Status: literature-implied partial subcase, pending human review.

## Original Problem

Problem 5.15 asks whether, if `X=c_0` or a related separable Banach space with
nonseparable bidual and no `ell_1` spreading-model obstruction coarsely embeds
into a Banach space `Y`, it follows that `Y**` is nonseparable.

This packet records only the target-space subcase `Y = J(e_i)`, a generalized
James space over an unconditional basis.

## Supporting Identification

Jackson--Krause--Sari prove that, for every unconditional basis `(e_i)`,
`c_0` coarsely embeds into the generalized James space `J(e_i)` if and only if
`c_0` linearly embeds into `J(e_i)`.

If a Banach space `Y` contains a linear copy of `c_0`, then `Y**` contains a
linear copy of `c_0** = ell_infty`, by passing the embedding to its second
adjoint. Hence `Y**` is nonseparable.

Therefore Problem 5.15 has an affirmative answer in the target-space subcase
where `X=c_0` and `Y` is a generalized James space `J(e_i)`.

## Files

- `main.tex`: self-contained LaTeX packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2004.04806.
- `supporting_paper_2501.01561.pdf`: local copy of arXiv:2501.01561.
- `figures/open_problem_crop.png`: crop of Problem 5.15 from the source paper.
- `figures/open_problem_context_crop.png`: context crop from the preceding page.
- `figures/supporting_theorem_crop.png`: crop of Theorem 29 from the supporting paper.
- `tmp/`: LaTeX build intermediates.

## Literature Check

The run indexes were searched for `2004.04806`, `2501.01561`, generalized
James-space keywords, `c_0 coarsely embeds`, and the `Y**` nonseparability
phrasing. No prior packet or attempt for this subcase was found. Web search on
June 14, 2026 for exact phrases from Problem 5.15 found only the source paper.

## Human Review

Recommended check: verify that Theorem 29 of arXiv:2501.01561 applies to the
intended generalized James space notation `J(e_i)`, and that the second-adjoint
argument indeed gives an isomorphic `ell_infty` copy in `J(e_i)**` whenever
`c_0` linearly embeds into `J(e_i)`. The full Problem 5.15 remains open.
