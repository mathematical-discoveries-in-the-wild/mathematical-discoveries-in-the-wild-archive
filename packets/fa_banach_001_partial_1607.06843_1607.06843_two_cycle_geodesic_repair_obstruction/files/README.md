# Partial result: a two-cycle obstruction to bounded geodesic repair

Status: `partial_result_likely_valid`

This packet concerns the geodesic-repair question on page 148 of Cécilia
Lancien's thesis, arXiv:1607.06843.  The displayed question there is stated
for the canonical full cycle.  The preceding application, however, needs the
analogous statement for `gamma_f`, the product of canonical cycles on the
level sets of a function `f`.

## Result

The needed multi-cycle extension is false already when `gamma_f` has two
cycles of the same size.  For every `n >= 2` there are permutations on `2n`
points such that:

- `gamma_f` is the product of two `n`-cycles;
- `alpha` has geodesic defect `delta = 1` relative to `gamma_f`;
- the Cayley distance from `alpha` to the whole geodesic interval
  `[id, gamma_f]` is exactly `n`.

Thus there is no universal constant `theta` for which every defect-`delta`
permutation can be repaired to that interval within `2 theta delta`
transpositions in the multi-cycle setting.  Since even the distance condition
fails, no bounded-fibre choice map can satisfy the stronger proposal.

## Scope

This packet by itself does **not** answer the exact full-cycle question printed
on page 148.  That question was subsequently disproved by the defect-one
family in
`solutions/counterexamples/1607.06843_full_cycle_unbounded_geodesic_repair`.
The present packet retains the sharper exact-distance obstruction for the
multi-cycle `gamma_f` setting needed in the preceding counting application.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:1607.06843.
- `figures/open_problem_crop.png`: crop of page 148 containing the open
  question and its multi-cycle motivation.
- `code/crop_open_problem.py`: reproducible crop script.
- `code/verify_obstruction.py`: independent exhaustive check for `2 <= n <= 4`.
- `tmp/`: source-page render and LaTeX build intermediates.

## Human review note

The key convention check is that the source's multi-cycle defect equation is

`#(gamma_f^{-1} alpha) + #(alpha) = p + #Im(f) - 2 delta`.

For the construction here, both cycle counts on the left equal `n`, while
`p = 2n` and `#Im(f) = 2`, hence `delta = 1`.  The interval lemma then forces
every geodesic permutation to preserve the two level sets, whereas `alpha`
interchanges them.
