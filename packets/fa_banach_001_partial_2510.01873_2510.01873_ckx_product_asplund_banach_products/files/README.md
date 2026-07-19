# Partial Result: Bound-Covering Subcases for the `C_k(X)` Asplund Product Problem

Status: `partial_result_likely_valid`

Source/open-problem paper: M. Fabian, J. Kakol, A. Leiderman,
*Asplund spaces `C_k(X)` beyond Banach spaces*, arXiv:2510.01873.

Supporting papers:

- J. Kakol and A. Leiderman, *On the product of Weak Asplund locally convex
  spaces*, arXiv:2412.10221.
- J. Kakol and A. Leiderman, *Asplund locally convex spaces and the finest
  locally convex topology*, arXiv:2412.11510.

## Target

Problem 3.4 of the source paper asks whether, whenever `C_k(X)` is Asplund,
the product `C_k(X) x E` is Asplund for every Asplund locally convex space
`E`. This packet does not solve the full problem: taking `X` to be a singleton
would include the open question whether `E x R` is Asplund for every Asplund
lcs `E`.

## Result

Let `X` be Tychonoff and assume that `C_k(X)` is Asplund. Let `E` be a
bound-covering locally convex space with a directed defining family of
continuous seminorms such that every Banach quotient level `E_p` is Asplund.
Then

`C_k(X) x E`

is an Asplund locally convex space.

Concrete consequences include:

- `E = prod_alpha E_alpha` for any family of Asplund Banach spaces.
- `E` equal to the zero-basepoint Sigma-product of such a family.
- `E` with a weak topology.
- every Asplund quojection, in particular every reflexive quojection.

## Proof Intuition

The source paper proves the case where `E` is a single Asplund Banach space by
forcing a continuous convex function on `C_k(X)` to factor through one compact
restriction map `C_k(X) -> C(L)`. The same idea works whenever the `E`
coordinate has open Banach quotient maps: local boundedness is witnessed by one
compact `L` and one quotient seminorm `p`, and convexity forces constancy on
the kernel of

`(f,e) -> (f|_L, q_p(e))`.

The function therefore factors through `C(L) x E_p`, a Banach Asplund space.
Its dense `G_delta` set of Frechet differentiability points pulls back to the
original lcs.

## Evidence

- `source_paper.pdf`: local copy of arXiv:2510.01873.
- `supporting_paper_2412.10221.pdf`: local copy of arXiv:2412.10221.
- `supporting_paper_2412.11510.pdf`: local copy of arXiv:2412.11510.
- `figures/open_problem_crop.png`: source-paper crop of Problem 3.4.
- `solution_packet.pdf`: compiled proof packet.
- `code/crop_open_problem.py`: reproducible PDF crop script.

## Search Bounds

Before packaging, the cheap run indexes were searched for `2510.01873`,
`Asplund spaces C_k(X) beyond Banach spaces`, `C_k(X) product Asplund lcs`,
`Sigma-product Asplund Banach`, `product Banach Asplund C_k`, `quojection`,
`bound covering`, and related phrases. No exact packet or duplicate was found.
The local parsed sources for arXiv:2510.01873, arXiv:2412.10221, and
arXiv:2412.11510 were inspected. A targeted web/arXiv search on 2026-06-29
found the weak-Asplund one-dimensional preprint arXiv:2510.26827 and the two
Kakol--Leiderman papers above, but no separate full solution of the arbitrary
Asplund lcs product problem.

## Scope Limitations

This proves only structured-factor subcases: `E` must have open
bound-covering Banach quotient levels which are Asplund. It does not address
arbitrary Asplund lcs factors. In particular, the one-dimensional stability
question `E x R` for arbitrary Asplund lcs remains outside the theorem.

## Human Review Notes

Recommended review focus:

- Check that the compact-restriction/quotient factorization is justified from
  one locally bounded basic neighborhood, as in the source paper's proof of
  Theorem 3.2.
- Check the use of openness of `q_p` to make the quotient image of the domain
  an open Banach-space domain.
- Check whether this exact product/Sigma-product subcase is already explicit
  elsewhere; if so, reclassify as literature-implied partial status.
