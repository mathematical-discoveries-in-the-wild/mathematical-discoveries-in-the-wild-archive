# Verification Report

Status: `candidate_partial_likely_valid`

## Analytic checks

The proof was checked against the following possible failure points.

1. The upper-right block of `TT*` is
   `Z = sum_i a_i b_i U_i V_i*`; both diagonal blocks are scalar multiples of
   the identity because every block is a scaled unitary.
2. A singular-value decomposition of `Z` gives a unitary equivalence to `d`
   two-by-two positive matrices. No simultaneous diagonalization of the
   relative unitaries is assumed.
3. The operator-norm triangle inequality gives every singular value of `Z`
   at most `c = sum_i a_i b_i`.
4. The derivative of the two-eigenvalue power sum has the sign of `q-1`,
   with `q=p/2`. Continuity covers zero eigenvalues and endpoints.
5. The compression includes the factor `d^(1/p)`, so its `p`th power norm is
   exactly `d F_q(c)`.

## Reproducible numerical check

Command:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/0702186_scaled_unitary_block_norm_compression/code/verify_scaled_unitary.py \
  --trials 5000 --seed 20260719
```

The script samples dimensions `1 <= d <= 6`, block counts `2 <= N <= 7`,
random complex Haar unitaries, lognormal nonnegative coefficients, and values
of `p` on both sides of 2. It compares direct singular-value calculations
with both spectral formulas and checks the asserted inequality direction.

Output:

```text
seed=20260719
trials=5000
max_relative_full_formula_error=4.178e-15
max_relative_compression_formula_error=8.040e-15
max_relative_direction_violation=1.414e-15
minimum_normalized_slack=-1.414e-15
PASS
```

These finite computations do not prove the theorem. They check the algebra,
normalization, inequality direction, and implementation against independently
computed Schatten norms.

## Novelty bounds

The run's cheap indexes were searched by arXiv id, title, `norm compression`,
`Schatten`, and `Hanner`. A bounded web/arXiv search used the source title and
the combinations `norm compression unitary blocks`, `scaled unitaries
Schatten`, and `Audenaert unitary blocks`. It recovered the source and nearby
PSD/diagonal norm-compression literature, but no exact scaled-unitary subcase.
This is a bounded check, not a claim of exhaustive novelty.

## Human review recommendation

Recommended focus: verify the unitary equivalence after the singular-value
decomposition of `Z`, the sign of `F_q'`, and the factor `d` in the compressed
norm formula. The packet should remain `candidate_partial_likely_valid` until
human mathematical review.

## Packet build and visual QA

`main.tex` compiled without warnings to a five-page PDF. All five pages were
rendered to PNG at 145 dpi and inspected individually. The source crop is
readable at normal review zoom and includes the definition, full conjecture
statement, and both inequality directions. No clipped text, overflow, broken
glyphs, missing references, or page-layout defects were found.
