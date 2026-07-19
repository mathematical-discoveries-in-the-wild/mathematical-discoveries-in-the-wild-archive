# Full-cycle geodesic repair has no defect-only distance bound

Status: **counterexample likely valid; full disproof of the printed question**

Source: Cécilia Lancien, *High dimension and symmetries in quantum
information theory*, arXiv:1607.06843, Section 9.16.3, page 148.

The packet constructs, for every integer `m >= 1`, a permutation on `4m`
points whose geodesic defect relative to the canonical long cycle is exactly
`delta = 1`, but whose Cayley distance from every geodesic permutation is at
least `ceil(m/2)`.  Consequently no constants `theta,kappa` can satisfy the
mapping statement in the source question, even before the fibre bound is
considered.

The construction is a chord matching with two nested families of `m` chords,
where every chord in one family crosses every chord in the other.  A
permutation at Cayley distance `r` can change at most `2r` endpoints.  It
therefore retains at least `2m-2r` original transposition cycles, while a
noncrossing permutation can retain chords from at most one family.  Hence
`r >= m/2`.

Files:

- `solution_packet.pdf`: human-readable proof packet.
- `main.tex`: packet source.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source question on page 148.
- `code/verify_family.py`: exact finite checks of the cycle formulas,
  crossing pattern, defect, and the smallest cases.
- `verification.md`: verification and novelty-search record.

Ledger record:
`runs/fa_banach_001/ledger/results/1607.06843_full_cycle_unbounded_geodesic_repair.json`.

