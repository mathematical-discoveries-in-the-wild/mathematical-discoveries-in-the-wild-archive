# Verification report

## Mathematical checks

For

`alpha_m = prod_i (i,3m+1-i) prod_j (m+j,4m+1-j)`

on `4m` points, the proof uses the explicit disjoint-cycle decomposition

`alpha_m gamma = prod_{i<m}(i,3m-i) (m,4m,3m,2m)
prod_{j<m}(m+j,4m-j)`.

Thus `#alpha_m=2m`, `#(gamma^{-1}alpha_m)=2m-1`, and the defect is exactly
one.  The two chord families are separately nested, and every chord from the
first family crosses every chord from the second.

If `r=d(alpha_m,pi)` and `tau=alpha_m^{-1}pi`, then the support of `tau` has
size at most `2r`.  Hence at least `2m-2r` transposition cycles of `alpha_m`
remain cycles of `pi`.  A geodesic `pi` is noncrossing and cannot retain a
cycle from both crossing families, so it retains at most `m` of them.  This
gives `r >= ceil(m/2)`.

## Computational check

Command:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/1607.06843_full_cycle_unbounded_geodesic_repair/code/verify_family.py
```

The script checks the formulas and all pairwise crossing assertions for
`1 <= m <= 50`.  It also exhaustively checks all permutations for `m=1,2`:

```text
m=1: geodesic_count=14, nearest_distance=1
m=2: geodesic_count=1430, nearest_distance=2
```

The computation is a guard against indexing errors; the unbounded lower bound
is proved symbolically and does not depend on finite enumeration.

## Bounded novelty search

Searched on 2026-07-19 using the exact source wording and the phrases
`distance to noncrossing permutations`, `genus one permutation Cayley
distance noncrossing`, `nearest noncrossing permutation`, and `geodesic
permutations Cayley distance non-geodesic defect`.  Also inspected the source
paper, Cori--Hetyei's genus-one permutation representation
(arXiv:1306.4628), Chen--Reidys on plane permutations (arXiv:1502.07674), and
Cori--Hetyei on spanning hypertrees (arXiv:2110.00176).  No later source was
found that explicitly answers Lancien's question or states this unbounded
distance family.  Novelty therefore remains provisional pending expert and
bibliographic review.

## Human-review recommendation

High priority.  Check the convention-independent identity
`#(gamma^{-1}alpha_m)=#(alpha_m gamma)` and the support-to-retained-cycle
argument.  These are the only substantive proof steps; both are elementary.

