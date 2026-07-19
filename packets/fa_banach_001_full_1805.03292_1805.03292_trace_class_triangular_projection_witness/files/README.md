# Full Result: Trace-Class Operator with Non-Trace-Class Triangular Projection

## Source Question

- Source paper: Alice Barbara Tumpach, *Banach Poisson-Lie groups and
  Bruhat-Poisson structure of the restricted Grassmannian*, arXiv:1805.03292.
- Location: page 9, Remark 1.14, after the definition of triangular
  truncations.
- Question: whether there exists a trace-class operator whose triangular
  projection is not trace class.

## Answer

Yes. Let `H` be an infinite-dimensional separable Hilbert space with a fixed
ordered orthonormal basis, and let `T_-` be the entrywise triangular truncation
used in the source paper. There is an operator `A in S_1(H)` such that the
formal triangular truncation `T_-(A)` is not in `S_1(H)`.

The construction is a block direct sum. The source-cited theorem says that
triangular truncation is unbounded on the trace class. This forces the norms of
the finite-dimensional triangular projections on `S_1^n` to be unbounded.
Choose finite blocks `B_k` with `||B_k||_1 <= 2^{-k}` but
`||T_- B_k||_1 >= 1`, place them on disjoint consecutive diagonal blocks, and
set `A = direct_sum B_k`. Then `A` is trace class, while the compressions of
`T_-(A)` to the first `N` blocks have trace norm at least `N`.

## Files

- `main.tex`: full solution packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_problem_crop.png`: crop of Remark 1.14 on page 9.
- `code/render_open_problem_crop.py`: script used to regenerate the crop.

## Review Focus

The key point for review is the finite-dimensional witness lemma: if the
finite triangular projections on `S_1^n` were uniformly bounded, density of
finite-rank operators would extend triangular truncation to a bounded operator
on all of `S_1(H)`, contradicting the unboundedness theorem cited in the
source. Once that lemma is accepted, the block-sum construction is immediate.

The packet does not address the separate broad problem about integrating
Banach Lie bialgebras into Banach Poisson-Lie groups.
