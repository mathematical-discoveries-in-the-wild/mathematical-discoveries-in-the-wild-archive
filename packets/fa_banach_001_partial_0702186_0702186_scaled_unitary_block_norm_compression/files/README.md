# Partial Result: Norm Compression for Scaled-Unitary Blocks

Run: `fa_banach_001`

Agent: `agent_lane_00`

Status: `candidate_partial_likely_valid`

## Source problem

Koenraad M. R. Audenaert, *On a Norm Compression Inequality for 2 x N
Partitioned Block Matrices*, arXiv:math/0702186, Conjecture 1 on PDF page 2.

The conjecture compares the Schatten `p`-norm of a matrix with two block rows
to the Schatten `p`-norm of the `2 x N` scalar matrix formed from the norms of
its blocks. The asserted direction reverses at `p=2`.

## Result

The conjecture holds for every finite `p >= 1` when all blocks are square of a
common size and each is a nonnegative scalar multiple of a unitary:

```text
A_i = a_i U_i,   B_i = b_i V_i.
```

The unitaries may vary arbitrarily with `i`; in particular, the blocks need
not be proportional or commuting. This gives a full-rank subcase distinct
from the rank-one and proportional-block families proved in the source.

## Mechanism

The Gram matrix `TT*` has scalar diagonal blocks and one cross term
`Z = sum_i a_i b_i U_i V_i*`. Its spectrum is the union of the spectra of `d`
two-by-two matrices indexed by the singular values `s_j(Z)`. Each satisfies
`s_j(Z) <= sum_i a_i b_i`. The trace of the relevant power of the two-by-two
matrix is decreasing for `1 <= p <= 2` and increasing for `p >= 2`, producing
exactly the required reversal.

## Verification

`code/verify_scaled_unitary.py` independently checks the spectral reduction,
the compressed-norm formula, and the inequality direction on 5,000 seeded
random complex instances. See `verification.md` for the command and output.
The computation is a regression check; the proof is analytic.

## Scope

This is a partial result. It does not settle arbitrary rectangular or
non-unitarily-flat blocks, and it does not settle the full matrix Hanner
inequality implied by the source conjecture.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered and visually inspected proof packet.
- `source_paper.pdf`: local copy of arXiv:math/0702186.
- `figures/open_problem_crop.png`: source Conjecture 1, rendered from PDF page 2.
- `code/verify_scaled_unitary.py`: reusable randomized verifier.
- `verification.md`: verification and review notes.
