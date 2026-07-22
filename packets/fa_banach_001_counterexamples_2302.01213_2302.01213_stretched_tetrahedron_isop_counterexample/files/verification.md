# Verification report

Verdict: `candidate_counterexample_likely_valid`.

## Exact audit

The chosen vertices have all six pairwise distances equal to one. After the
map `diag(3,1,1)`:

- the volume is `sqrt(2)/4`;
- two facets have sides `(3,sqrt(3),sqrt(3))` and area `3sqrt(3)/4`;
- two facets have sides `(1,sqrt(3),sqrt(3))` and area `sqrt(11)/4`;
- the tetrahedral inradius is
  `3sqrt(2)/(2(3sqrt(3)+sqrt(11)))`;
- the two facet inradii are
  `3sqrt(3)/(2(3+2sqrt(3)))` and
  `sqrt(11)/(2(1+2sqrt(3)))`.

The identity `Isop(S)=1/r(S)` is valid for every simplex by decomposing it
into pyramids from its incenter. Hence the two ratios in the packet are exact.

For type A, comparison with `1/sqrt(2)` reduces to
`4 < sqrt(3)+sqrt(11)`. For type B it reduces to
`12sqrt(3)-5 < 3sqrt(33)`; after checking positivity and squaring, this is
`4/3 < sqrt(3)`. No numerical approximation is used in the proof.

## Reproduction

Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2302.01213_stretched_tetrahedron_isop_counterexample/code/verify.py
```

The script uses exact SymPy radicals to recompute all distances, areas,
volumes, inradii, and positivity certificates. Decimal output is diagnostic
only.

## Adversarial checks

- Uniform rescaling does not change a facet/body `Isop` ratio, so the map can
  be normalized to determinant one if the affine class is represented by
  volume-preserving maps.
- Translation is irrelevant.
- All four facets are covered by the two symmetry classes.
- The regular comparison value is `1/sqrt(2)` from the exact inradii
  `sqrt(6)/12` and `sqrt(3)/6`.
- The result targets the explicit page-7 conjecture, not page-8 Question 1.
- The source's occasional `O(n)` notation is inconsistent with its own
  non-orthogonal examples. The packet states that it uses the intended affine
  interpretation; for orthogonal maps the objective is invariant.

## Novelty bounds

Cheap run indexes were searched for the arXiv id and the terms `regular
simplex`, `John's position`, `facet isoperimetric ratio`, and `affine simplex`.
A bounded web search on 2026-07-21 used exact and near-exact versions of those
phrases. No separate later resolution of this precise conjecture was found.
This is not an exhaustive novelty certification.

Recommended reviewer: a convex geometer. Primary review focus: source-scope
interpretation and the elementary facet classification.
