# Counterexample Packet: Literal Smoothing FIO Schatten Obstruction

- status: candidate counterexample, likely valid for the literal class-membership wording
- run: `fa_banach_001`
- source arXiv id: `2408.06833`
- source paper: D. Cardona, J. Delgado, M. Ruzhansky, *Nuclearity, Schatten-von Neumann classes, distribution of eigenvalues and L^p-L^q-boundedness of Fourier integral operators on compact manifolds*
- target passage: Open problem in the Main Results section, PDF page 5

## Claim

Open Problem 1 is false if `T in I^\mu_{1,0}(X;\Lambda)` is read in the
standard class-membership sense.

For every compact smooth manifold `X` of positive dimension `n`, every
`r>0`, and every real `mu >= -n/r`, there is a nonzero non-elliptic Fourier
integral operator `T in I^\mu_{1,0}(X;\Delta)` such that
`T in S_r(L^2(X))`. Thus the conclusion `mu < -n/r` fails throughout the
range of the source open problem, e.g. take `mu=0`.

## Construction

Choose nonzero `u,v in C^\infty(X)` and define

```text
Tf = <f,v>_{L^2(X)} u.
```

The kernel `K(x,y)=u(x) overline{v(y)}` is smooth. Hence `T` is a smoothing
pseudodifferential operator, so it belongs to `Psi^{-\infty}(X)` and therefore
to `Psi^\mu_{1,0}(X)=I^\mu_{1,0}(X;\Delta)` for every real `mu`.

The operator has rank one, with its only nonzero singular value equal to
`||u||_2 ||v||_2`, so it is in every Schatten class `S_r`, including
`0<r<1`. Its principal symbol in every finite-order class is zero, so it is
not elliptic. Choosing `mu>=-n/r` contradicts the displayed conclusion in the
source open problem.

## Scope

This packet only refutes the literal wording using membership in an order
class. It does not refute the corrected or intended variant where `T` is
required to have exact order `mu`, or equivalently a nonzero principal symbol
at that order. The source's own proofs later use language such as `T having
order mu` and use nonvanishing principal symbols, so this is best read as a
wording-level counterexample and a precise repair suggestion.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2408.06833.
- `figures/open_problem_crop.png`: crop of the source open problem.
- `code/crop_open_problem.py`: reproducible crop script using PyMuPDF.
- `code/rank_one_schatten_check.py`: finite-rank singular-value sanity check.

## Novelty Check

The run indexes were searched for `2408.06833`, the paper title, `non-elliptic
Fourier integral`, `mu < -n/r`, `smoothing Fourier integral Schatten`, and
`rank-one smoothing`. No prior packet or attempt for this target was found.

A bounded web search on 2026-06-28 for `2408.06833`, the paper title, and the
exact open-problem phrase surfaced the source arXiv page but no later answer
or discussion of this smoothing counterexample.

## Human Review Recommendation

Review the convention for `T in I^\mu`: if the source intended exact order,
the counterexample should be recorded as a wording repair, not as a disproof
of that stronger intended problem. Under ordinary class-membership notation,
the rank-one smoothing example is decisive.
