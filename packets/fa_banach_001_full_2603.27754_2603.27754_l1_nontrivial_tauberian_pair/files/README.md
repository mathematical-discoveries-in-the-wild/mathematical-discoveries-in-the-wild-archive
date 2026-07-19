# Nontrivial Tauberian Pairs In L1

status: full_solution_likely_valid

source_arxiv: 2603.27754

source_paper: Manuel Gonzalez and Antonio Martinez-Abejon, *Tauberian pairs
of closed subspaces of a Banach space*

## Result

The source asks for non-trivial examples, in `Z=L1(0,1)`, of tauberian pairs
`(M,N)` that are not in `K_+`.  The packet gives an explicit example with both
`M` and `N` nonreflexive:

```text
L1(0,1) = L1(A) +_1 L1(B) +_1 L1(C),
M = E +_1 F,
N = E +_1 G,
```

where `E` is a closed reflexive infinite-dimensional subspace of `L1(A)`,
for instance a Rademacher `ell_2` copy, and `F,G` are closed `ell_1` copies
in the disjoint bands `L1(B)` and `L1(C)`.

Then `(M,N)` is tauberian because `M^co cap N^co = 0`, using the band
projections and the reflexivity of `E`.  But `(M,N)` is not in `K_+`, since
the kernel of `Q_N J_M` is `M cap N = E`, which is infinite-dimensional.

## Evidence

- `main.tex` contains the proof packet.
- `solution_packet.pdf` is the rendered packet.

## Human Review Recommendation

Review as a literal full answer to the final `L1(0,1)` example question.  The
main point to check is the bidual quotient calculation
`M^co cap N^co = 0`, which follows from the three disjoint band projections
and `E^co=0`.
