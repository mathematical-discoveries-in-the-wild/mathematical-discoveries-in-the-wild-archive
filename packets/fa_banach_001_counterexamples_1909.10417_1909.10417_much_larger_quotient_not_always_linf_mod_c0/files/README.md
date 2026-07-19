# Counterexample: a much-larger ideal quotient need not be `ell_infty/c0`

Status: candidate counterexample, likely valid.

Source: Miek Messerschmidt, arXiv:1909.10417, *A family of quotient maps of `ell^infty` that do not admit uniformly continuous right inverses*.

## Result

The source observes that if ideals `i` and `j` on `N` satisfy `i \Subset j`, then the quotient map

```text
j c0 -> j c0 / i c0
```

has no uniformly continuous right inverse. It then remarks that, since much-larger inclusions seem abundant and non-special, one could conjecture that `j c0 / i c0` is always isomorphic to `ell_infty/c0`.

This packet gives a counterexample to that conjectural remark.

There is an ideal `J` on `N` such that `Fin \Subset J`, but

```text
J c0 / c0
```

is not isomorphic to `ell_infty/c0`.

## Construction

Partition `N` into pairwise disjoint infinite sets

```text
D, A_1, A_2, ...
```

Let

```text
J = { S subset N : S \ D is contained in A_1 union ... union A_n for some n }.
```

Then `J` is a proper ideal, `Fin subset J`, and `Fin \Subset J`: take singleton witnesses inside `D`; every infinite union of them is an infinite subset of `D`, hence lies in `J \ Fin`.

## Obstruction

The quotient `J c0 / c0` contains a complemented subspace isomorphic, in fact isometric, to `c0`. Choose a free ultrafilter limit functional on each block `A_m`, and project a class `[x]` to the block-constant class whose `A_m`-value is that ultrafilter limit of `x|A_m`. The defining property of `J c0` forces these block values to tend to zero, so the projection is well-defined on the quotient.

By contrast, `ell_infty/c0` is Grothendieck: `ell_infty` is Grothendieck, and quotients of Grothendieck spaces are Grothendieck. Complemented subspaces of Grothendieck spaces are Grothendieck, while `c0` is not Grothendieck. Hence `ell_infty/c0` cannot contain a complemented copy of `c0`.

## Novelty Check

Bounded checks performed on 2026-06-20:

- local run indexes for `1909.10417`, `quotient maps`, and `uniformly continuous right inverses`;
- local source/corpus search around `much larger inclusion`, `J c0 / I c0`, and `ell_infty/c0`;
- web searches for the exact conjectural phrase and close variants:
  `we could conjecture J c0 I c0 ell_infty/c0`, `much larger inclusion ideals ell_infty/c0 quotient space always isomorphic`, and `A family of quotient maps much larger inclusion isomorphic`.

These searches found the source arXiv page and no prior answer to this specific conjectural remark.

## Files

- `main.tex` contains the self-contained proof.
- `solution_packet.pdf` is the rendered packet.
- `source_paper.pdf` is the source paper.
- `figures/open_problem_crop.png` shows the source conjectural remark on page 3.

## Human Review

Recommended review focus: verify the ideal definition, the descended ultrafilter-block projection, and the Grothendieck invariant step. The argument is otherwise short and robust.

