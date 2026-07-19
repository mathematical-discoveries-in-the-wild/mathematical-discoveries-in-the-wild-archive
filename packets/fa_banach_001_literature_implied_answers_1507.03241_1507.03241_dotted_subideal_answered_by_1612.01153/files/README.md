# Literature Status: Dotted Subideal Inclusion From arXiv:1507.03241

Status: literature-implied answer.

Source paper: arXiv:1507.03241, Ben Wallis, *Closed ideals in $\mathcal{L}(X)$ and $\mathcal{L}(X^*)$ when $X$ contains certain copies of $\ell_p$ and $c_0$*.

Supporting paper: arXiv:1612.01153, D. Freeman, Th. Schlumprecht, and A. Zsak, *Closed ideals of operators between the classical sequence spaces*.

## Source Signal

In Section 5 of arXiv:1507.03241, Wallis records the then-known closed subideal diagram in
`L(ell_p,c_0)`, `1<p<infty`:

`{0} => K => [G_{I_{p,0}}] .> FSS --> L`.

The dotted arrow means that the inclusion was not known to be proper. The same section immediately proves a proper intermediate ideal only for the special range `1<p<2`, and by duality gives the analogous `L(ell_1,ell_q)` information for `q>2`.

## Later Answer

The later paper arXiv:1612.01153 identifies the remaining `L(ell_p,c_0)` problem and proves that for every `1<p<infty`, `L(ell_p,c_0)` has continuum many closed ideals. More precisely, Theorem 1 constructs continuum many closed ideals between `J^{I_{U,V}}` and `FSS`.

For `2<=p<infty`, the remark after the proof of Theorem 1 states that `J^{I_{ell_p,c_0}}` and `J^{I_{U,V}}` are identical. Therefore the dotted inclusion

`[G_{I_{p,0}}](ell_p,c_0) subset FSS(ell_p,c_0)`

is proper also in the complementary range `2<=p<infty`. Together with Wallis's same-paper result for `1<p<2`, this answers the dotted-inclusion question for all `1<p<infty`.

## Scope Notes

This is not a new result of the run. It is recorded as a later-literature implication because the supporting paper answers the exact dotted inclusion only after identifying `J^{I_{ell_p,c_0}}` with the `J^{I_{U,V}}` base ideal in the range `2<=p<infty`.

The packet does not claim to settle every open problem listed in arXiv:1612.01153, such as meet preservation for the lattice embedding or whether `FSS subset J^K` in Theorem 2.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note, if LaTeX rendering succeeds.
- `source_paper.pdf`: source paper arXiv:1507.03241, when available.
- `supporting_paper_1612.01153.pdf`: later supporting paper, when available.
