# Counterexample Packet: Kazhdan Projection Not Approximable by Positive Measures

- status: candidate counterexample, likely valid
- run: `fa_banach_001`
- source arXiv id: `1604.01616`
- source paper: Mikael de la Salle, *A local characterization of Kazhdan projections and applications*
- target passage: PDF page 16, Section 3.5, where the paper asks whether every Kazhdan projection belongs to the closure of nonnegative probability densities/functions.

## Claim

The general positive-Kazhdan-projection question has a negative answer for
arbitrary Banach-space representation families.

There is a compactly generated infinite group `G`, a uniformly generator-bounded
Banach-space representation family `F`, and a Kazhdan projection in
`C_F(G)` which is not in the closure of the nonnegative finitely supported
probability measures.

## Construction

Let `G = Z` and let the generator act on `E = C^3` by

```text
T = diag(1, 2, 1/2).
```

Let `F` contain only this representation. In the resulting completion of the
group algebra, the signed mass-one polynomial

```text
p(u) = -2 u^2 + 5 u - 2
```

acts as `diag(1,0,0)`, the projection onto the invariant vectors. Thus it is a
Kazhdan projection.

If a nonnegative probability measure `mu` on `Z` approached this projection,
then

```text
sum_n mu(n) 2^n -> 0
sum_n mu(n) 2^{-n} -> 0.
```

But for every integer `n`, `2^n + 2^{-n} >= 2`, so the two quantities cannot
both tend to zero. Hence the Kazhdan projection is not positive in the sense of
Section 3.5 of the source paper.

## Scope

This is a literal counterexample to the general question for arbitrary
Banach-space representations. It does not contradict the source paper's
positive result for central Kazhdan projections attached to isometric
representation families. The example is finite-dimensional and non-isometric.

## Files

- `main.tex`: full counterexample packet
- `solution_packet.pdf`: rendered packet
- `source_paper.pdf`: local copy of arXiv:1604.01616
- `figures/open_problem_crop.png`: crop of the source question
- `code/make_open_problem_crop.py`: script used to regenerate the crop
- `code/verify_counterexample.py`: exact-arithmetic sanity check

## Novelty Check

The run indexes were searched for `1604.01616`, the paper title, Kazhdan
projection, positive Kazhdan projection, nonnegative functions, Banach property
T, fixed point spectrum, Laplacian, cohomology, and expander keywords. No exact
packet for arXiv:1604.01616 or this positive-projection question was present.
Adjacent packets concern BFGM/higher-rank fixed point properties, fixed point
spectra, and expander/superexpander questions, not this finite-dimensional
representation-algebra obstruction.

External phrase searches on June 28, 2026 for `"positive Kazhdan projections"
"nonnegative functions"`, `"Kazhdan projection" "closure of the nonnegative
functions"`, and the exact source sentence did not reveal a published answer.
The novelty confidence is bounded by that phrase search; the construction is
short enough that human review should focus more on interpretation of the
source scope than on technical complexity.

## Human Review Recommendation

Check that the source's phrase "in general" is intended to include arbitrary
families of Banach-space representations as in Definition 3.1 and Theorem 1.2.
Under that literal reading, the counterexample is complete.
