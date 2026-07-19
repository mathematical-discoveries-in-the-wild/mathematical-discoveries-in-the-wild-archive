# Full Solution Packet: Torus and Real-Line Decompositions Are Equivalent

- status: candidate full solution, likely valid
- run: `fa_banach_001`
- source arXiv id: `2311.01436`
- source paper: Chenxi Deng, Emiel Lorist, and Mark Veraar, *Strongly Kreiss Bounded Operators in UMD Banach Spaces*
- target passage: PDF page 22 / source lines 1064--1069, Problem 5.2.

## Claim

In the standard range `1<p<infty`, the Fourier decomposition properties on
the torus `T` are equivalent to the corresponding properties on the real line
`R`.

More precisely, for every Banach space `X` and `1<=q<=infty`, the lower
`ell^q(L^p)`-decomposition property holds on `T` if and only if it holds on
`R`, with the same best constant. The same equivalence holds for upper
`ell^q(L^p)`-decompositions.

## Method

For a finite interval family, the decomposition map

```text
f -> (D_I f)_I
```

is a finite mixed-norm Fourier multiplier, with target norm
`ell^q` of `L^p` norms. The usual de Leeuw periodization and restriction
arguments apply componentwise to this finite family. They transfer both the
operator norm estimate for the analysis map and the lower-bound estimate
which defines upper decompositions.

The main point is that one does not need a naive single Banach-valued
`L^p(G;Y)` multiplier formulation; the finite mixed norm survives the
periodization limit because each component converges in `L^p` and the number
of components is finite.

## Files

- `main.tex`: proof packet
- `solution_packet.pdf`: rendered packet
- `source_paper.pdf`: local copy of arXiv:2311.01436
- `figures/open_problem_crop.png`: crop of Problem 5.2

## Novelty Check

The run indexes were searched for `2311.01436`, `Strongly Kreiss`, `UMD`,
`Fourier decomposition`, `decomposition properties on R`, and related
transference phrases. No existing packet or attempt addresses this problem.

External web searches for exact phrases around the paper title, Problem 5.2,
`ell^q(L^p)-decompositions`, and torus/real-line decomposition transference
found the source paper and adjacent multiplier literature, but no later paper
explicitly resolving this problem.

Human review should focus on the mixed-norm de Leeuw lemma: the proof invokes
the standard periodization/restriction proof componentwise for finite interval
families and then passes through the finite `ell^q` norm.
