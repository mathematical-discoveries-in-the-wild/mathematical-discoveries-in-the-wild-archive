# Counterexample Packet: Schreier Compactum for the c0 Vector-Measure Range Problem

Run: `fa_banach_001`

Result type: `counterexample`

## Source Problem

- Jose Rodriguez, *Open problems in Banach spaces and measure theory*,
  arXiv:1607.07787.
- Local PDF: `source_paper.pdf`.
- Location: Problem 4.2, PDF page 12; parsed source
  `data/parsed/arxiv_sources/1607.07787/source.tex`, lines 661--663.

The packet answers negatively the Anantharaman-Diestel question:

> Let `K` be a weakly compact subset of `c_0`. Is `K` contained in the range
> of a `c_0`-valued vector measure?

## Counterexample

Let

`S = {F subset N finite : |F| <= min F} union {emptyset}`

be the Schreier family, and put

`K_S = {1_F in c_0 : F in S}`.

Then `K_S` is weakly compact in `c_0`, but it is not contained in the range of
any countably additive `c_0`-valued vector measure.

The contradiction is that range containment would produce a bounded weakly
null sequence `(g_n)` in some `L_1(lambda)` such that Schreier averages are
uniformly bounded below by `1/2`. Szlenk's weak Banach-Saks theorem for `L_1`
gives a subsequence with Cesaro means converging to zero in `L_1`, impossible.

## Files

- `main.tex`: counterexample packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source/open-problem paper.
- `figures/open_problem_crop.png`: crop of Problem 4.2.

## Human Review Recommendation

Check the necessary-condition step from a hypothetical `c_0`-valued vector
measure to weakly null `L_1` densities. The rest is a standard Schreier-family
Cesaro lower bound plus Szlenk's weak Banach-Saks theorem for `L_1`.
