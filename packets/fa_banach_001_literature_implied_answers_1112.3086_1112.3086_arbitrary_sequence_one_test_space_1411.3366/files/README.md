# Literature-Implied Answer: Arbitrary Sequences Have One Test-Space

Status: `literature_implied_answer (full arbitrary-sequence one-test-space, bounded-degree graph)`

Source/open-problem paper: M. I. Ostrovskii, *Test-space characterizations of
some classes of Banach spaces*, arXiv:1112.3086.

Supporting paper: M. I. Ostrovskii, *Metric characterizations of some classes
of Banach spaces*, arXiv:1411.3366.

## Target

In Section 3 of arXiv:1112.3086, Ostrovskii writes that the paper seeks
one-test-space characterizations for classes defined by excluded
finite-dimensional subspaces, but that "at this moment" the construction is
known only for increasing sequences of finite-dimensional subspaces, not for an
arbitrary sequence.

The source paper also proves, in Theorem `T:Ost11+`, that for every sequence
`(X_m)` of finite-dimensional Banach spaces there is a sequence `(H_n)` of
finite connected unweighted graphs of maximum degree `3` such that a Banach
space `Y` uniformly contains the spaces `(X_m)` iff the graphs `(H_n)` admit
uniformly bilipschitz embeddings into `Y`.

## Identification

The later paper arXiv:1411.3366 records an elementary proposition, citing
Ostrovskii's 2014 finite-graph work, which says:

- if `(S_n)` is a sequence of finite test-spaces for a class `P` of Banach
  spaces containing all finite-dimensional Banach spaces, then there is one
  metric space `S` which is a test-space for `P`;
- if the `(S_n)` are unweighted graphs, trees, or graphs with uniformly
  bounded degrees, the one test-space can be required to have the same
  corresponding graph property.

Apply this proposition to the class
`P = {Y : (X_m) do not admit uniformly isomorphic embeddings into Y}`.
Under the source paper's nontrivial standing convention `sup_m dim X_m = infinity`,
every finite-dimensional Banach space belongs to `P`. The finite graph sequence
`(H_n)` from arXiv:1112.3086 is therefore a sequence of finite test-spaces for
`P`, so arXiv:1411.3366 turns it into a single test-space.

## Result

For every arbitrary sequence `(X_m)` of finite-dimensional Banach spaces with
`sup_m dim X_m = infinity`, there is a single metric space `S` such that, for
every Banach space `Y`,

`S` bilipschitz embeds into `Y`
iff
the spaces `(X_m)` admit uniformly isomorphic embeddings into `Y`.

Moreover, `S` can be taken to be an unweighted graph with uniformly bounded
degree, since the finite test graphs `(H_n)` in arXiv:1112.3086 have maximum
degree `3`.

## Evidence

- `source_paper.pdf`: local copy of arXiv:1112.3086. The open-problem signal is
  in Section 3, lines 778-783 of the parsed TeX; Theorem `T:Ost11+` is at
  lines 275-285; the nontrivial unbounded-dimension convention is in Remark
  `R:InfDim`, lines 298-300.
- `supporting_paper_1411.3366.pdf`: local copy of arXiv:1411.3366. The
  finite-test-space-to-one-test-space proposition is in lines 1600-1617 of the
  parsed TeX, with the graph-chain proof sketch in lines 1625-1647.
- `solution_packet.pdf`: compact human-readable status note built from
  `main.tex`.

## Search Bounds

Before packaging, the cheap run indexes were searched for `1112.3086`,
`Test-space characterizations`, `one-test-space`, `arbitrary sequence`,
`finite-dimensional Banach test`, `locally finite`, `coarse disjoint`, and
`Ostrovskii`. No prior packet for this exact arbitrary-sequence one-test-space
identification was found.

External web queries on June 19, 2026 for exact phrases including
`"1112.3086" "one-test-space" "arbitrary sequence"`,
`"Test-space characterizations of some classes of Banach spaces" "arbitrary sequence"`,
and `"one test-space" "finite-dimensional subspaces" Ostrovskii` surfaced the
source paper and no separate explicit-answer paper. The supporting relation was
found by local corpus search in arXiv:1411.3366.

## Scope Limitations

This packet records a literature-implied full answer to the one-test-space
existence problem for arbitrary unbounded-dimension sequences. It does not
claim that arXiv:1411.3366 explicitly identifies the sentence in arXiv:1112.3086
as the question being answered.

The supporting proposition gives a single unweighted graph with uniformly
bounded degree. This packet does not separately prove or record a maximum-degree
`3` refinement for the arbitrary-sequence one-graph construction.

## Human Review Notes

Recommended review focus:

- Check that the source's target class is exactly
  `Y` not uniformly containing the arbitrary sequence `(X_m)`.
- Confirm that `sup_m dim X_m = infinity` is the intended nontrivial scope and
  makes the class contain all finite-dimensional Banach spaces.
- Verify that the finite graph theorem `T:Ost11+` supplies finite test-spaces
  for this class, so the arXiv:1411.3366 proposition applies directly.
