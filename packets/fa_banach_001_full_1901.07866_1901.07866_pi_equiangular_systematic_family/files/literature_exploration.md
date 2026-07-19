# Literature exploration and strengthening notes

Checked on 2026-06-15 while revising the human-requested follow-up packet.

## Sources checked

- Basso, *Computation of maximal projection constants*, arXiv:1901.07866:
  source of the `Pi(n,d)` question and the quoted Koenig--Lewis--Lin bound.
  https://arxiv.org/abs/1901.07866
- Basso, *Erratum to "Computation of maximal projection constants"*,
  arXiv:2402.06672: flags an error in Lemma 3.1 and a separate theorem
  strategy, but explicitly records that the other main-body results are not
  affected. The current packet uses the Section 1.4 KLL criterion/equiangular
  line route, not the affected lemma.
  https://arxiv.org/abs/2402.06672
- Lin--Yu, *Equiangular lines and the Lemmens-Seidel conjecture*,
  arXiv:1807.06249: useful for the modern equiangular-line context,
  Gerzon-sharp dimensions, the 276-line system in `R^23`, and fixed-angle
  restrictions.
  https://arxiv.org/abs/1807.06249
- Greaves--Koolen--Munemasa--Szollosi, *Equiangular lines in Euclidean
  spaces*, arXiv:1403.2155: useful for Seidel-matrix and low-dimensional
  equiangular-line tables/tools.
  https://arxiv.org/abs/1403.2155
- Jiang--Tidor--Yao--Zhang--Zhao, *Equiangular lines with a fixed angle*,
  arXiv:1907.12466 / Annals of Mathematics 194 (2021): useful for the
  asymptotic fixed-angle viewpoint and possible future lower-bound-to-`Pi`
  transfers.
  https://arxiv.org/abs/1907.12466
- Fickus--Jasper--Mixon--Peterson, *Tremain equiangular tight frames*,
  arXiv:1602.03490: points to Steiner triple systems plus Hadamard matrices as
  another source of infinite real ETF families.
  https://arxiv.org/abs/1602.03490
- Renes, *Equiangular Tight Frames from Paley Tournaments*,
  arXiv:math/0408287: adjacent Paley/quadratic-residue ETF construction, more
  complex-valued in its stated form but useful as a cross-checking reference.
  https://arxiv.org/abs/math/0408287

## Main improvement found after audit

The right abstraction is the spanning equiangular interval principle:

If `R^n` admits `M` distinct equiangular lines spanning `R^n`, then for every
`n <= d <= M`,

```text
Pi(n,d) = n/d + sqrt((d-1)(n/d)(1-n/d)).
```

An attempted stronger "ambient admission" version was rejected during audit:
lower-dimensional embeddings are not enough. The sanity check is Basso's own
`Pi(4,6)=5/3`; embedding the six equiangular lines in `R^3` into `R^4` would
otherwise incorrectly force the larger KLL value `B(4,6)`.

## Strongest new `7/3` conclusion

Solving the equation that the KLL upper bound itself equals `7/3` gives only
two integer candidates:

```text
(n,d) = (7,15), (49,51).
```

Both are sharp:

- `(7,15)` comes from the `E_7` 28-line system.
- `(49,51)` comes from the Paley symmetric conference matrix for `q=97`,
  which gives 98 equiangular lines spanning `R^49`; selecting a spanning
  51-line subsystem realizes the value.

This does not classify all possible pairs with `Pi(n,d)=7/3`, because a pair
with a larger KLL upper bound could conceivably have exact value `7/3` by some
other mechanism. It does classify the KLL-equality route to `7/3`.

## Classification push

The safe classification statement is only for the KLL-bound route:
`B(n,d)=7/3` has exactly two integer pairs, `(7,15)` and `(49,51)`, and both
are KLL-sharp. A full classification of `Pi(n,d)=7/3` would require ruling out
possible non-KLL mechanisms at pairs where `B(n,d)>7/3`.

## Further routes worth pursuing later

- Build a machine-readable table of known real equiangular-line systems
  `(n,M)` and automatically emit exact spanning intervals.
- Add explicit Seidel/Gram matrices for the `R^23` 276-line system if the
  reviewer wants fully constructive certificates rather than literature-backed
  existence.
- Explore Steiner/Hadamard/Tremain ETF families and harmonic ETF difference
  sets as additional infinite sources of exact intervals.
- Use fixed-angle results as a source of asymptotic lower bounds for families
  of `Pi(n,d)` values, while keeping exact KLL equality only where actual
  full-dimensional finite equiangular systems are known.
- Attack non-KLL possibilities directly using Basso's two-graph/eigenvalue
  framework or linear-programming formulations for relative projection
  constants. This is the route toward a true full `7/3` classification.
