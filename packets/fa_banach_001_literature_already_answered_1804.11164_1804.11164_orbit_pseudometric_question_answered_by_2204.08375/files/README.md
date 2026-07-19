# Literature-Already-Answered Packet: canonical orbit pseudometric for GH distance

Run: `fa_banach_001`

Result type: `literature_already_answered`

Status: a later paper gives a positive answer to the specific continuous
orbit-pseudometric question asked in the concluding problems of arXiv:1804.11164.
This packet records literature status only; it is not an original proof from
the run.

## Original Problem Source

- M. Cuth, M. Doucha, and O. Kurka, *Complexity of distances: Theory of
  generalized analytic equivalence relations*, arXiv:1804.11164.
- Local source inspected: `data/parsed/arxiv_sources/1804.11164/gh_part1.tex`,
  lines 958--972.
- Local PDF: `source_paper.pdf`.

The source asks whether there is a continuous analogue of the Clemens--Gao--
Kechris universality theorem: if `d` is the Hausdorff distance on `F(U)`,
`Iso(U)` acts canonically on `F(U)`, and `rho` is the corresponding orbit
pseudometric, is the Gromov--Hausdorff pseudometric `rho_GH` Borel-uniformly
continuously bi-reducible with `rho`? The source also asks whether at least one
of the two reductions holds.

## Supporting Answer Source

- O. Kurka, *Orbit pseudometrics and a universality property of the
  Gromov-Hausdorff distance*, arXiv:2204.08375; Topology Appl. 364 (2025),
  109095.
- Local supporting source inspected from arXiv e-print:
  `tmp/supporting_source_2204.08375.tex.gz`, source lines around Theorem 1.2
  and Theorem 1.3.
- Local PDF: `supporting_paper_2204.08375.pdf`.

## Status Match

Kurka's Theorem 1.2 states that the Gromov--Hausdorff distance `rho_GH` is
Borel-u.c. bireducible with the orbit pseudometric
`rho_{Iso(U), rho_H}` on `F(U) \ {empty}`. This is exactly the orbit
pseudometric in the question from arXiv:1804.11164, with the standard nonempty
closed-set coding of Polish metric spaces.

Moreover, Kurka's Theorem 1.3 gives a quantitative comparison for the
constructed reductions:

```text
rho_GH(Y_p,Y_q) <= rho_{Iso(U),rho_H}(Y_p,Y_q)
 <= rho_{G,d}(p,q) <= 2 rho_GH(Y_p,Y_q).
```

Thus both directions requested in the original question are answered
positively, and the paper records that the reductions can be chosen
Borel-Lipschitz on small distances.

## Scope Limitations

This packet clears the specific canonical Urysohn/Hausdorff orbit pseudometric
question from arXiv:1804.11164. It does not solve all concluding problems from
that paper. Kurka explicitly leaves open a broader question about dropping the
auxiliary system of pseudometrics in the general orbit-pseudometric theorem.

## Verification Notes

- Same-paper check: arXiv:1804.11164 states this as a question in its
  concluding open problems, not as a theorem.
- Separate-source check: arXiv:2204.08375 is a later paper and cites
  arXiv:1804.11164 as `cdk1`.
- Exact-match check: the notation `rho_{Iso(U),rho_H}` in Kurka's Theorem 1.2
  matches the Hausdorff-distance orbit pseudometric for the canonical action of
  `Iso(U)` on `F(U)`.
- Local duplicate check: the cheap run indexes had no exact packet for
  arXiv:1804.11164 or Kurka's arXiv:2204.08375 answer before creation.

## Files

- `README.md`: this packet summary.
- `main.tex`: compact human-readable status note.
- `solution_packet.pdf`: rendered status note, if LaTeX rendering succeeds.
- `source_paper.pdf`: original/open-problem source.
- `supporting_paper_2204.08375.pdf`: decisive supporting answer source.
- `tmp/supporting_source_2204.08375.tex.gz`: downloaded arXiv e-print payload
  used to inspect theorem statements.

## Human Review Recommendation

Verify the exact source chain:

1. arXiv:1804.11164 asks whether `rho_GH` is Borel-u.c. bi-reducible with the
   canonical `Iso(U)`/Hausdorff orbit pseudometric.
2. arXiv:2204.08375, Theorem 1.2 answers yes for
   `rho_{Iso(U),rho_H}` on `F(U) \ {empty}`.
3. arXiv:2204.08375, Theorem 1.3 supplies the quantitative comparison behind
   the two reductions.
