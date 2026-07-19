# Verification report

## Claim checked

For all integers `n >= 1` and `1 <= r <= n`, a balanced join of `r` regular
simplices is an `n`-polytope with exactly `n+r` vertices and isoperimetric
quotient comparable to `n/sqrt(r)` with universal constants.

## Verdict

likely valid

## Step checks

| Step | Status | Notes |
| --- | --- | --- |
| Choose balanced positive `b_i` summing to `n` | valid | Euclidean division gives `b_i` in `{floor(n/r), ceil(n/r)}`. |
| Apply source Lemma 12 to regular simplices | valid | Equations (24)--(26) require only an inscribed ball tangent to every facet; origin symmetry is introduced only for equation (27). |
| Count vertices | valid | The lemma gives `sum_i(b_i+1)=n+r`; no vertices collapse because each simplex contains the origin in its interior. |
| Regular-simplex volume formula | valid | Substituting side length `a=h sqrt(2b(b+1))` into `a^b sqrt(b+1)/(b! sqrt(2^b))` gives the displayed formula. |
| Surface/volume simplification | valid | With `h_i^{-2}=b_i`, the square-root factor in (26) is `sqrt(n)` and `(n!)/(n-1)!=n`. |
| Balanced product estimate | valid | `m=n/r <= b_i+1 <= m+2 <= 3m` and `sum_i(b_i+1)=n+r=n(1+1/m)`. |
| Uniform endpoint behavior | valid | `r=1` is the regular simplex; `r=n` is the cross-polytope. Both match equation (11) of the source. |
| Answer scope | valid as partial only | The construction is an upper bound on the extremal infimum; it does not prove the desired universal lower bound. |

## Counterexample search

The main risks were off-by-one vertex counts, accidental use of the
origin-symmetric clause of Lemma 12, and loss of a universal constant when
`r/n` is not small.  None occurs.  The formula audit checked every
`1 <= r <= n <= 500`; the normalized ratio stayed bounded and the two endpoint
specializations converged to the expected constants.

## External dependencies

- Ball--Böröczky--Naor, Lemma 12, equations (24)--(26): verified directly in
  the source PDF and TeX.
- Standard volume and inradius formulas for a regular simplex: algebraically
  re-derived in the packet.
- Stirling's formula: used only up to universal multiplicative constants.

## Confidence

Score: 94/100.

The computation and scope are clear.  Remaining uncertainty concerns novelty,
not mathematical correctness: a broader historical search could reveal that
the same join construction was previously recorded elsewhere.

## Human review recommendation

Send as a candidate partial result.  Do not describe it as resolving Remark 2
unless a matching lower bound is added.
