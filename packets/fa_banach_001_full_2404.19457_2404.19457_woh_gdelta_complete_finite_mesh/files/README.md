# Exact complexity of weak octahedrality via finite scale meshes

Status: `full_solution_likely_valid`

Source: Ginés López-Pérez, Esteban Martínez Vañó, and Abraham Rueda Zoca,
*Computing Borel complexity of some geometrical properties in Banach spaces*,
arXiv:2404.19457. The open question is on source PDF pages 24–25, immediately
after Theorem 6.6.

## Claimed contribution

In each Polish coding space `P_infinity` and `B`, the isometry class of
weakly octahedral separable Banach spaces is `G_delta`-complete. This improves
the source paper's `F_sigma_delta` upper bound and answers its exact-complexity
question in both spaces.

The related question whether the full weak-octahedrality condition can be
tested only at `t=1` is not resolved here.

## Proof mechanism

1. For an accuracy `epsilon`, reverse-triangle estimates handle
   `t <= epsilon/4` and `t >= 2/epsilon`. On the middle interval, the norm is
   1-Lipschitz in `t`, so a fixed finite rational mesh suffices.
2. On finitely many rational directions, retain only the finite vector of
   dual evaluations. Its admissible values form a compact subset of
   `[-1,1]^n` with a closed graph, described by the Hahn–Banach inequalities
   for rational linear combinations.
3. The finite-mesh witness relation is open. Compact co-projection over the
   cube gives an open block; a countable intersection gives `G_delta`.
4. The source paper already proves that the class is not `F_sigma`, so the
   standard Hurewicz theorem gives `G_delta`-completeness.

## Verification

The argument has no computational dependency. `VERIFICATION.md` audits the
mesh constants, density transfers, varying-kernel dual trace, compact
co-projection, and completeness step.

The most important human-review point is the relative closedness of the
finite dual-evaluation graph over the open domain where the chosen rational
directions survive the quotient. The displayed rational Hahn–Banach
inequalities make this interface explicit.

## Novelty and scope

The bounded novelty check on 2026-07-22 covered the run's four cheap indexes;
the exact arXiv id and title; searches combining weak octahedrality with
`finite mesh`, `G_delta`, and `Borel complexity`; arXiv records and the current
source version; and the cited finite-set characterization. No later paper or
preprint stating this result was found.

Novelty confidence is moderate. The result settles the exact Borel complexity
in both coding spaces named in the source theorem, but it does not settle the
single-scale (`t=1`) characterization.

Files:

- `source_paper.pdf`: arXiv:2404.19457.
- `figures/open_problem_crop.png`: stitched source evidence from PDF pages
  24–25.
- `main.tex`, `solution_packet.pdf`: full proof packet.
- `VERIFICATION.md`: adversarial verification report.
- `code/crop_source_evidence.py`: reproducible evidence crop.

