# Counterexample Packet: The \(Q_A^{(t)}\) Riesz Product Need Not Be a Measure

- status: candidate counterexample, likely valid
- run: `fa_banach_001`
- source arXiv id: `1812.05412`
- source paper: Ron Blei, *From Parseval to Grothendieck and a little beyond, part I*
- target passage: PDF page 49 / source `part1.tex`, Remark 5.13 and Question 5.14

## Claim

For `2 < t <= infinity`, the formal object `Q_A^{(t)}(y)` from Question 5.14
represents a finite complex measure on the Rademacher compact group if and only
if `y` is square summable.

Consequently, the answer to the source question "does `Q_A^{(t)}(y)` represent
a measure?" is negative in general: on any infinite index set, choose a
countably supported vector `y_n = n^{-1/2}`. Then `y in l^t` for every
`t > 2` and for `t = infinity`, but `Q_A^{(t)}(y)` is not a measure.

## Mechanism

If `y in l^2`, the usual complex Riesz products have uniformly bounded total
variation, so their weak-* limit gives the desired measure. If `y notin l^2`,
finite-coordinate restrictions force the variation norm of any representing
measure to dominate an odd Riesz-product test polynomial. The lower bound grows
like a positive multiple of

```text
prod_{alpha in B} (1 + |y_alpha|^2 / ||y||_t^2)^{1/2}
```

along finite sets `B`, which is unbounded exactly when `y notin l^2`.

## Files

- `main.tex`: full proof packet
- `solution_packet.pdf`: rendered packet
- `source_paper.pdf`: local copy of arXiv:1812.05412
- `figures/open_problem_crop.png`: crop of Remark 5.13 and Question 5.14
- `code/check_lower_bounds.py`: numerical sanity check for the finite lower bounds

## Novelty Check

Before promotion, the run indexes were searched for `1812.05412`,
`Q_A^{(t)}`, `represent a measure`, `bona fide integrals`, and nearby
`S(p)`/`L(p)` terminology. No duplicate packet or attempt was found. External
exact-phrase searches for `Does q-Sidon S(q*)`, `q-Sidon S(p) Blei`,
`Does Lambda(2) L(p) Blei`, `Lambda(2)-uniformizable`, and close variants did
not surface a later answer to Question 5.14.

Human review should focus on the finite-dimensional duality estimate in the
negative direction and on the weak-* compactness argument in the positive
direction.
