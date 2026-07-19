# Audit note: 2026-06-18

This audit rechecked the active `8/7` partial packet for arXiv:1809.10616.

## Verdict

The partial result remains worth recording as a likely valid strong partial result:

```text
rho(X,Y) >= 8/7
```

for all real Banach spaces `X,Y` of dimension at least `2`.

The audit checked the geometric reduction, the CHSH duality argument, the polytope vertices, and the exact rational verifier. The local committed verifier was rerun from the repository root on 2026-06-18:

```text
checks=130
failures=0
max_depth_used=2
certificate verified
```

The supplied audit reported a verifier variant needing only depth `1`; the committed verifier still reports depth `2`. This is harmless, since both are exact rational Bernstein-certificate checks and neither relies on floating-point optimization.

## Literature status

The audit found no archival paper or preprint, through 2026-06-18 searches, resolving the full `sqrt(2)` problem or giving an archival proof of the `8/7` improvement.

However, the `8/7` improvement should not be advertised as entirely new without qualification. The supplied audit reports a December 2025 Case Western Reserve University abstract by Lucas Maciel Bueno da Silva, supervised by Stanislaw Szarek, stating that the `8/7` configuration was numerically investigated and confirmed analytically, with Mathematica code intended to be provided. No corresponding archival proof was found in this audit.

## Obstruction recorded

The audit also records a useful negative pressure point. At the balanced outer body

```text
H = {(s,t): |s|,|t| <= 1, |s+t|,|s-t| <= 3/2},
```

the best possible bound obtainable using only this two-coordinate outer body and dual witnesses controlled by the coordinate square is exactly `8/7`. Equality is attained by the CHSH matrix proportional to

```text
[[1,  1],
 [1, -1]].
```

Thus the full `sqrt(2)` conjecture cannot be reached merely by optimizing the tensor inside the same coarse `H_m` reduction. Any full proof must use information discarded by that reduction, such as the full determinant-maximal Auerbach geometry, relations between selected vectors and functionals, additional coordinates, or a different dual witness.
