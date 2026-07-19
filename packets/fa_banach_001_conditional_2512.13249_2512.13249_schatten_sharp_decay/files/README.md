# Sharp Schatten Covering-Index Decay

Status: full result for the Schatten-class covering-index decay problem;
likely valid. Also records the optimal AUS exponent of `S_p`.

Source paper: Tomasz Kania and Natalia Maslany, *Raja's covering index of
`L_p` spaces*, arXiv:2512.13249.

Open problem context: the source paper proves lower bounds for
non-commutative `L_p(M,tau)` spaces and says that corresponding upper bounds
are not pursued. It then states that determining the precise optimal AUS
exponent and the sharp covering-index decay remains open even for Schatten
classes `S_p`.

Main result: if `H` is an infinite-dimensional Hilbert space and
`1 <= p < infinity`, then for every `n`,

`Theta_{S_p(H)}(n) <= n^{-1/p}`.

For `1 <= p < infinity`, the diagonal copy of `ell_p` is contractively
complemented in `S_p(H)`. Raja's/source-paper monotonicity for contractively
complemented subspaces gives `Theta_{ell_p}(n) <= Theta_{S_p(H)}(n)`, and
the known scalar estimate `Theta_{ell_p}(n) asymp n^{-1/p}` gives the lower
bound. Hence

`Theta_{S_p(H)}(n) asymp n^{-1/p}`.

The packet also notes the optimal AUS exponent: for `1 < p < infinity`,
`S_p(H)` has optimal AUS power exponent `min(p,2)`. The upper side is the
standard noncommutative Clarkson estimate already recalled in the source
paper; the obstruction to better exponents comes from subspaces: diagonal
`ell_p` when `p <= 2`, and an isometric Hilbert row/column subspace when
`p >= 2`.

Packet contents:

- `source_paper.pdf`: arXiv:2512.13249.
- `figures/noncommutative_schatten_gap_crop.png`: source passage saying the
  Schatten/noncommutative upper bounds are not pursued.
- `figures/open_problem_crop.png`: source passage stating that sharp
  covering-index decay remains open for Schatten classes.
- `code/make_open_problem_crops.py`: reproducible crop script.
- `history/partial_upper_bound/`: superseded upper-bound-only packet from
  the first push, kept for provenance.
- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `tmp/`: LaTeX build outputs.

Human review focus:

- Check the pinching/corner-compression covering for all `1 <= p < infinity`.
- Check the finite-codimensional rank-one tail argument proving
  `varrho(A_k) <= n^{-1/p}`.
- Check the diagonal conditional expectation monotonicity lower bound.
- Check the AUS exponent obstruction via `ell_p` and Hilbert subspaces,
  especially the inheritance of `q`-AUSability by subspaces.
