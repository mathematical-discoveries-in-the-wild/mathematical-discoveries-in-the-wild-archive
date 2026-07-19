# Literature Answer: A New Complemented Subspace of `C(beta omega x beta omega)`

Status: `literature_already_answered`

Source/open-problem paper: Jakub Kakol, Witold Marciszewski, Damian Sobota,
and Lyubomyr Zdomskyy, *On complementability of `c_0` in spaces
`C(K x L)`*, arXiv:2206.03794.

Supporting answer paper: Grzegorz Plebanek, Jakub Rondos, and Damian Sobota,
*Complemented subspaces of Banach spaces `C(K x L)`*, arXiv:2405.19120.

## Question Identified

At the end of the Introduction, arXiv:2206.03794 asks whether
`C(beta N x beta N)` has a complemented infinite-dimensional subspace not
isomorphic to any of:

`C(beta N x beta N)`, `C(beta N)`, `c_0`,
`c_0 + C(beta N)`, or `c_0(C(beta N))`.

## Answer Located

The later paper arXiv:2405.19120 explicitly revisits this Alspach--Galego /
Candido question. Its abstract and Corollary 1.4 state that
`C(beta omega x beta omega)` contains complemented copies of
`C([0,1]^kappa)` for every `1 <= kappa <= c`. Taking `kappa=1` gives a
complemented subspace isomorphic to `C[0,1]`.

This is outside the five listed isomorphism classes. The spaces
`C(beta N x beta N)`, `C(beta N)`, `c_0 + C(beta N)`, and `c_0(C(beta N))` are
nonseparable, while `C[0,1]` is separable. The remaining listed separable space
is `c_0`, and `C[0,1]` is not isomorphic to `c_0` because their duals are not
both separable: `c_0^* = ell_1` is separable, whereas `C[0,1]^*` is
nonseparable.

## Scope Notes

This gives a positive answer to the existence question from arXiv:2206.03794.
It does not classify all complemented subspaces of `C(beta omega x beta omega)`.

Local files:

- `supporting_paper_2405.19120.pdf`: local copy of the supporting paper.
- `source_tex/source_2206.03794.tex`: parsed TeX for the source paper.
- `source_tex/supporting_2405.19120.tex`: parsed TeX for the supporting paper.
- `main.tex` / `solution_packet.pdf`: compact status note.

The local cache for arXiv:2206.03794 contains source TeX but no source PDF.
