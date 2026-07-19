# Partial Result: Subtree L-Summands Give Super Daugavet Points

Run: `fa_banach_001`

Source paper: Trond A. Abrahamsen, Ramon J. Aliaga, Vegard Lima, Andre
Martiny, Yoel Perreau, Antonin Prochazka, and Triinu Veeorg, "A relative
version of Daugavet-points and the Daugavet property", arXiv:2306.05536.

Status: partial result likely valid. This does not solve the arbitrary
R-tree-subset question in full.

## Main Claim

Let `M` be a subset of a complete R-tree and let `A subset M` be a
non-degenerate closed metric-convex subtree. Then `F(A)` is an L-summand in
`F(M)`. Consequently every unit vector of `F(A)` is a super Daugavet-point of
the ambient space `F(M)`.

In particular, if `M` itself is a non-degenerate complete metric-convex subset
of an R-tree, then every unit vector of `F(M)` is a super Daugavet-point.

## Proof Mechanism

The nearest-point retraction `pi_A:M -> A` linearizes to a norm-one projection
on free spaces. The same Lipschitz pasting argument used in the source for a
single segment shows this projection is an L-projection. Since `A` is an
R-tree, Godard identifies `F(A)` with an atomless `L_1` space. The known MPRZ
`L_1` characterization makes all unit vectors of `F(A)` super Daugavet, and
the property transfers through the resulting `ell_1` sum.

## Remaining Gap

The packet does not prove that every Daugavet-point or Delta-point in an
arbitrary `F(M)` lies in such a convex subtree summand. Missing branch points
and non-convex length-measure pieces remain the obstruction to a full answer.

## Packet Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source paper arXiv:2306.05536.
- `supporting_paper_0904.3178.pdf`: Godard's tree/free-space computation.
- `supporting_paper_2301.04433.pdf`: MPRZ diametral point facts.
- `figures/open_problem_crop.png`: crop of the source open-question sentence.

## Human Review Recommendation

Check the L-projection proof for arbitrary closed metric-convex subtrees,
especially the nearest-point projection identity in the R-tree. Also verify
that the transfer from `F(A)` to `F(M)=F(A) op_1 ker P` is exactly the standard
super-Daugavet stability under `ell_1` sums.
