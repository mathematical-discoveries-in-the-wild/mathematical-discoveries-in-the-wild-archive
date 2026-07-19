# Further push notes, 2026-06-20

After packaging the `c0 \oplus_infty Y` product extension, lane 17 checked
whether the result could plausibly be promoted to a full answer to the source
question.

## Literature check

Web searches on 2026-06-20 for close phrases around `2305.18976`, `CPCP`,
`strong regularity`, `tau-CPCP`, `tau-SR`, `c0`, and locally convex topologies
found the source paper but no later exact extension or full solution. The
source itself says that a positive answer for every Banach space failing
classical CPCP would feed into the RNP/KMP strategy, so that broad form should
be treated as major-open-problem scale rather than a bounded lane target.

## Natural upgrade route tested

The tempting next family is `X = c0 \oplus_p Y`, `1 <= p < infinity`, with the
same product topology: the source topology on the `c0` coordinate and the norm
topology on `Y`.

The failure of topological CPCP would still be witnessed by the face
`B_c0 x {0}`. The difficulty is proving strong regularity for open subsets of
the whole ball. A basic product-neighborhood in the relative topology has the
form

```text
(U x V) cap B_{c0 \oplus_p Y}.
```

For finite `p`, the allowed `c0` fiber radius depends on `y in V`. The source
small-convex-combination theorem can be scaled on a fixed `c0` ball, but the
resulting relatively open pieces in a scaled ball are not automatically
ambient-open pieces whose entire intersections with `(U x V) cap B_X` remain
inside the controlled fiber. This is exactly where the clean `ell_infty`
argument uses the product identity `B_X = B_c0 x B_Y`.

Thus the finite-`p`/absolute-sum route remains a possible future direction, but
the present proof does not promote safely.

## Complemented-copy route

Replacing the literal `ell_infty` product by an arbitrary complemented or
isomorphic copy of `c0` runs into an even stronger version of the same issue:
the unit ball need not contain uniform full `c0` fibers over the complementary
coordinate. The current argument is therefore best stated as an `M`-summand,
or equivalently literal `ell_infty`-sum, theorem.

## Conclusion

No full-result promotion was found. The existing packet should remain a single
cohesive partial result for the natural `c0` `ell_infty`-summand family.
