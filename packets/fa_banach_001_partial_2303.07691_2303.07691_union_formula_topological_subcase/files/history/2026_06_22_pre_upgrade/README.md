# Candidate Partial Result: Union Formula In The Topological Subcase

Source paper: Ondrej F. K. Kalenda and Matias Raja, *Topologies related to
(I)-envelopes*, arXiv:2303.07691.

Result type: `partial`

Status: candidate partial result, likely valid, pending human review.

## Open Question

Question 5.1 asks whether, for convex sets `A,B subset X^*` with `A union B`
also convex, one always has

```text
(I)-env(A union B) = (I)-env(A) union (I)-env(B).
```

The packet does not answer this in full generality.

## Candidate Contribution

The equality holds whenever `(I)-env(S)` is represented for every set
`S subset X^*` as topological closure of `co S` in a fixed topology on `X^*`.
In particular, by Theorem 3.3 of the source paper, the equality holds for
every Banach space `X` containing no isomorphic copy of `ell^1`.

The proof is just the finite-union law for topological closure:

```text
cl_tau(A union B) = cl_tau(A) union cl_tau(B).
```

Since `A`, `B`, and `A union B` are convex, the convex hulls disappear.

## Files

- `main.tex`: self-contained LaTeX packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of the original arXiv PDF.
- `figures/open_problem_crop.png`: crop of Question 5.1 from page 22 of the
  source paper.
- `tmp/`: LaTeX build intermediates.

## Literature Check

The run indexes were searched for `2303.07691`, the paper title,
`(I)-envelope`, `Ienv(A union B)`, `Ienv(A) union Ienv(B)`, and related
topology keywords; no prior packet or attempt was found. A bounded web search
on June 14, 2026 for exact union-formula phrases found only the source paper
and no later explicit answer.

## Human Review

Recommended check: verify that the source theorem indeed gives the required
representation for all subsets `S subset X^*` when `X` contains no copy of
`ell^1`, and that Question 5.1 assumes convexity of `A`, `B`, and their union.
The general case remains open.
