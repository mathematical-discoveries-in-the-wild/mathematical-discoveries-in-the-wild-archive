# Full Solution Packet: `Pi(7,15)=7/3`

## Status

Claimed full solution to the final question in:

- Giuliano Basso, *Computation of maximal projection constants*, arXiv:1901.07866.
- Source location: Remark 4.6, PDF page 24.

The source asks:

> Are there integers `n <= d` such that `Pi(n,d)=7/3`?

The answer is yes:

```text
Pi(7,15) = 7/3.
```

## Idea of the Proof

Basso recalls the Koenig--Lewis--Lin bound

```text
Pi(n,d) <= n/d + sqrt((d-1)(n/d)(1-n/d)),
```

with equality exactly when `R^n` admits `d` distinct equiangular lines. For
`(n,d)=(7,15)`, the right-hand side is

```text
7/15 + sqrt(14 * 7/15 * 8/15) = 7/15 + 28/15 = 7/3.
```

It remains only to exhibit 15 equiangular lines spanning a 7-dimensional real
space. In the hyperplane `H={x in R^8 : sum x_i=0}`, the vectors

```text
v_ij = e_i + e_j - (1/4)(1,1,1,1,1,1,1,1),  1 <= i < j <= 8,
```

give the standard 28-line equiangular system. Selecting the 15 lines indexed by

```text
(1,j), 2 <= j <= 8;   (2,j), 3 <= j <= 8;   (3,4), (3,5)
```

still spans `H`, so it gives a 15-line equiangular system in `R^7`.

## Packet Contents

- `main.tex`: full solution note.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv source paper PDF.
- `figures/source_definition_kll_page4.png`: source crop with `Pi(n,d)` and the KLL criterion.
- `figures/source_open_question_page24.png`: source crop with Remark 4.6 and the open question.
- `code/verify_equiangular_7_15.py`: exact-arithmetic verifier.

## Verification

The verifier checks:

- there are 15 selected vectors;
- their span has rank 7;
- every selected vector has squared norm `3/2`;
- every off-diagonal inner product has absolute value `1/2`;
- the normalized absolute inner product is `1/3`;
- the KLL value for `(7,15)` is exactly `7/3`.

Command:

```bash
conda run --no-capture-output -n sandbox python runs/fa_banach_001/solutions/full/1901.07866_pi_7_3_equiangular_lines/code/verify_equiangular_7_15.py
```

Output:

```text
selected lines: 15
span rank: 7
norm squared: 3/2
absolute off-diagonal inner product: 1/2
normalized absolute inner product: 1/3
KLL bound for (n,d)=(7,15): 7/3
```

## Novelty and Search Bounds

Cheap index searches for `1901.07866`, `Pi(n,d)=7/3`, maximal projection
constants, and equiangular-line keywords found no existing run packet or
attempt. Bounded web searches on 2026-06-14 for exact phrases including
`"Pi(n,d)" "7/3" "projection" "equiangular"`,
`"maximal projection constants" "7/3" "15"`, and
`"Are there integers" "Pi(n,d)" "7/3"` returned no exact answer hits.

The result is a short observation using the source paper's quoted
Koenig--Lewis--Lin equality criterion plus an explicit classical equiangular
line configuration. It should be reviewed as a likely-valid full answer to
the source question, not as a claim of broad historical novelty.

## Human Review Recommendation

Check that the quoted Koenig--Lewis--Lin equality criterion is being applied in
the same real setting as Basso's `Pi(n,d)`, and confirm that the 15 selected
vectors span the 7-dimensional hyperplane. The exact verifier covers the second
point.
