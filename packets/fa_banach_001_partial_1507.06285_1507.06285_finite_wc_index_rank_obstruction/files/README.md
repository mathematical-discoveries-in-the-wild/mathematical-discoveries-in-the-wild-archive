# Partial Packet: Finite Levels of the WC Index Are Rank Bounds

Run: `fa_banach_001`

Result type: `partial`

## Source Problem

- Kevin Beanland, Ryan Causey, Daniel Freeman, Ben Wallis, *Classes of
  operators determined by ordinal indices*, arXiv:1507.06285.
- Local PDF: `source_paper.pdf`.
- Source location: Section 9.2, Question 9.3, page 43.
- Evidence crops:
  - `figures/open_problem_crop.png`: definition of `WC(A,X,Y,K)` and
    `WC(A,X,Y)`.
  - `figures/question_crop.png`: Question 9.3.

Question 9.3 asks:

```text
For which ordinals xi is the class of operators A:X -> Y such that
WC(A,X,Y) <= xi an ideal?
```

## Result

This packet settles the finite ordinal cutoffs.

For every bounded operator `A:X -> Y`,

```text
WC(A,X,Y) <= n    iff    rank(A) <= n-1
```

for each finite `n >= 1`. Equivalently:

```text
rank(A) = r < infinity  =>  WC(A,X,Y) = r+1,
rank(A) = infinity      =>  WC(A,X,Y) >= omega.
```

Consequently, for every finite `n >= 2`, the class
`{A : WC(A,X,Y) <= n}` is not closed under sums. For example, on an
`n`-dimensional space, a rank `n-1` projection and a rank-one complementary
projection both have `WC <= n`, but their sum is the identity of rank `n` and
has `WC = n+1`.

The `n=1` cutoff is the zero-operator class. It is closed under sums and
composition, but it is not an operator ideal if the convention requires
containing all finite-rank operators.

## Proof Intuition

The finite part of the `WC` tree only sees linear dimension. A node of length
`m` in `WC(A,K)` forces the vectors `Ax_1,...,Ax_m` to dominate the first
`m` summing-basis vectors, hence these images must be linearly independent.
So finite-rank range dimension `r` forbids nodes of length `r+1`.

Conversely, if the range has dimension at least `m`, pick `m` independent
vectors in `A(B_X)`. Any two bases of an `m`-dimensional space are equivalent,
so for some constant `K` these images dominate the first `m` summing-basis
vectors. Thus `WC(A,K)` has a branch of length `m`.

## Verification Notes

- The proof uses only the source definition of `WC(A,X,Y,K)` and elementary
  finite-dimensional basis equivalence.
- The lower estimate for infinite-rank operators allows `K` to depend on the
  chosen length `m`, which is legitimate because `WC(A,X,Y)` is the supremum
  over all `K >= 1`.
- The finite-rank formula is exact because a tree with maximum node length
  `r` and a branch of length `r` has order `r+1`.

## Search Bounds

- Checked local `registry_index.tsv`, `solutions/index.tsv`,
  `attempts/index.tsv`, and `proof_gaps/index.tsv` for `1507.06285`,
  weak compactness index, `WC(A,X,Y)`, finite rank, and related operator-index
  terms.
- Web search was run for the source title/arXiv id together with
  `WC(A,X,Y)`, weak compactness, summing basis, finite rank, and ideal
  terminology. No direct later answer to this finite-cutoff observation was
  found.

## Limitations

- This is a finite-ordinal partial answer only.
- The packet does not classify infinite countable ordinal cutoffs.
- The source paper already proves that the `WC <= omega` class is the ideal of
  super weakly compact operators and that `WC < omega_1` is an ideal; this
  packet fills in the finite levels below `omega`.

## Files

- `README.md`: this summary.
- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered packet, if LaTeX rendering succeeds.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: definition of the `WC` index.
- `figures/question_crop.png`: Question 9.3.
- `tmp/`: render intermediates.

## Human Review Recommendation

Check the exact convention for "operator ideal" used in the source. The
rank-characterization theorem is independent of that convention; only the
wording of the `n=1` cutoff depends on whether operator ideals are required to
contain all finite-rank operators.
