# Verification and adversarial audit

## Logical checks

1. **Well-defined projections.**  An edge of a `k`-branch diamond is sent to
   an edge of the binary diamond with the same length.  When several source
   arms have the same bit, they may collapse onto the same binary arm; this
   causes no inconsistency because the arms meet only at their common
   endpoints and the construction is repeated identically inside every
   child edge.

2. **Endpoint distances.**  The proof first establishes, inductively, that
   every projection preserves distance to the top and bottom of every
   recursive cell.  This is essential: merely being edgewise 1-Lipschitz
   would not suffice for the pairwise argument.

3. **Pairs in different arms.**  Such a distance is the minimum of the route
   through the bottom and the route through the top.  A bit that separates
   the two arm labels leaves both endpoint distances unchanged and puts the
   images in distinct binary arms, so the same minimum is obtained.

4. **Pairs in one arm.**  If both points are in the same half-diamond, the
   claim recurses.  If they are in the two halves joined in series, their
   shortest path goes through the common midpoint and every projection
   preserves it.  The alternative route exits through both outer endpoints
   and is no shorter.

5. **One separating bit is enough.**  The recursive proof associates at most
   one pair of unequal arm labels to a vertex pair.  It does not require one
   bit to distinguish a sequence of unrelated branch choices.  Injectivity
   of the binary labels therefore supplies the needed bit.

6. **Concatenation loss.**  If a coordinate block has internal partial sums
   with maximum absolute value `s`, the corresponding global partial sums
   include an initial offset `A` and values `A+P_r`.  For an `r` with
   `|P_r|=s`, at least one of `|A|` and `|A+P_r|` is at least `s/2`.  Hence
   concatenation loses at most a factor two, independent of the number of
   blocks.

7. **Scaling and strict inequality.**  Scaling the concatenation by `1/m`
   makes its `ell_1` distance at most the source metric.  The strict binary
   estimate `d < C_2 ||.||_s` then yields the strict estimate with
   `2mC_2`; no limiting or equality issue is hidden.

8. **Metric normalization.**  The argument is invariant under the convention
   that final edges have length one or `2^{-n}`.  The projections preserve
   edge lengths and the binary maps can be scaled with the metric.

## Exhaustive finite-depth check

`code/verify_binary_projections.py` constructs the diamonds recursively,
constructs all bit projections from vertex addresses, computes all-pairs
shortest-path distances, and checks

```text
d(pi_j(x),pi_j(y)) <= d(x,y),
max_j d(pi_j(x),pi_j(y)) = d(x,y)
```

for every vertex pair.  It also builds the standard binary Hamming labels,
concatenates their pullbacks, and checks the `ell_1` upper bound and records
the smallest observed summing-norm ratio.

Run from the repository root with:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/1609.06618_multibranching_diamonds_summing_factorization/code/verify_binary_projections.py \
  --k 3 --max-n 4
```

The computation is supporting evidence only; the recursive lemma in
`main.tex` is the proof for all depths.

Recorded run: `k=3`, depths `n=1,2,3,4`.  All pairs passed; at depth four
the graph had 779 vertices, the smallest observed `ell_1/d` ratio was `1/2`,
and the smallest observed summing-norm ratio was `1/8`.  Additional runs for
`k=2,4,5,6` through depth three also passed every pairwise assertion.

## Remaining human-review focus

The most useful independent review is to formalize the recursive-cell
decomposition in the reviewer’s preferred definition of `D_{n,k}` and check
the same-arm/different-half case of the distance lemma.  No numerical or
external classification theorem is used in the new part of the proof.
