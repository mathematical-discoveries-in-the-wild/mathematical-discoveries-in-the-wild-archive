# Counterexample: weak*-to-weak continuous `ell^1` operator with uncomplemented kernel

Status: candidate counterexample, likely valid; human review recommended.

Source target: Jens Flemming and Bernd Hofmann, *New aspects of
ill-posedness classification in Banach spaces*, arXiv:2511.06690. The target
question appears on source PDF pages 11-12, after Theorem 3.4: in `ell^1`,
does weak*-to-weak continuity of a bounded operator imply complementedness of
the null-space?

## Result

The answer is negative. There is a bounded linear operator

```text
A: ell^1 -> c0
```

which is weak*-to-weak continuous, but whose kernel is not complemented in
`ell^1`.

## Construction

Let

```text
E0 = ( direct sum_n ell_2^n )_{c0}.
```

Embed `E0` isomorphically into `c0` by finite-dimensional block embeddings,
and call the image `E`. Choose a dense sequence `(v_k)` in the unit ball of
`E`. Define

```text
A x = ( 2^{-k} <x, v_k> )_k,       x in ell^1 = c0^*.
```

For every `a in ell^1 = c0^*`, one has

```text
A^* a = sum_k a_k 2^{-k} v_k in E subset c0,
```

so `A` is weak*-to-weak continuous. Its kernel is exactly

```text
E^\perp = { x in ell^1 : <x,e> = 0 for all e in E }.
```

If this kernel were complemented, then the quotient `ell^1/E^\perp`,
which is naturally isomorphic to `E^*`, would be isomorphic to a complemented
subspace of `ell^1`, hence to `ell^1` by the classical Pelczynski theorem on
complemented subspaces of `ell^1`. But

```text
E^* ~= ( direct sum_n ell_2^n )_{ell^1}
```

is not isomorphic to `ell^1`; otherwise its dual would be isomorphic to
`ell^\infty`, forcing uniformly bounded injectivity/projection constants for
the 1-complemented Hilbert blocks `ell_2^n`, contrary to the classical
unboundedness of the projection constants of finite-dimensional Hilbert spaces.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: locally rendered source paper from arXiv source.
- `figures/open_problem_crop.png`: stitched crop of the source question.
- `code/crop_open_problem.py`: PyMuPDF/Pillow crop script.

## Verification

No computational search is involved. The packet checks the operator formula,
the weak*-to-weak continuity criterion via the adjoint, the kernel identity,
and the classical complemented-subspace obstruction.

Novelty check: lightweight run indexes had no `2511.06690` result. Web searches
for the exact source question and close variants such as
`weak*-to-weak continuity complemented ell^1 null-space`,
`weak* closed subspace ell^1 complemented`, and
`weak*-closed subspace l_1 uncomplemented` found no direct later answer.
