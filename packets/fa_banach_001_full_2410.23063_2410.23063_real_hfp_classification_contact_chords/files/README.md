# Full packet: real HFP classification via contact chords

status: full_solution_likely_valid

source: Guillaume Aubrun and Alexander Muller-Hermes, *Limit formulas for norms
of tensor power operators*, arXiv:2410.23063.

target: Conjecture 5.2 asks whether a pair `(X,Y)` of real Banach spaces has the
Hilbert space factorization property (HFP) if and only if `X` or `Y` is a
Hilbert space. The source paper gives the equivalent two-dimensional
convex-body ellipse-sandwich formulation as Conjecture 5.5.

packet: `runs/fa_banach_001/solutions/full/2410.23063_real_hfp_classification_contact_chords/`

## Classification

This is a candidate full solution, marked `full_solution_likely_valid`. The
attached report says the proof is new and unrefereed, and no published proof or
counterexample was found in its literature search through 2026-06-22. The
packet therefore records a full proof candidate, not an externally verified
literature answer.

## Result

The packet proves the planar ellipse-sandwich theorem: for centrally symmetric
planar convex bodies `K,L`, if every linear contraction `T(K) subset L` admits
an intermediate ellipse, then `K` or `L` is an ellipse. The proof normalizes by
the Loewner ellipse of `K` and the John ellipse of `L`, sends contact directions
through the quadratic double-angle map, rotates exposed contact chords until
they cross, and uses equal second-moment measures plus a separating quadratic
form to construct a small contraction with no intermediate ellipse.

Using the source paper's equivalence between the planar statement and real HFP,
this proves that a real pair `(X,Y)` has HFP exactly when `X` or `Y` is Hilbert.

## Upgrade History

- `2026-06-22`: upgraded from the previous common quotient-subspace partial
  packet using the supplied report `hfp_full_solution`.
- Previous active packet preserved at
  `history/2026-06-22_previous_common_quotient_subspace_partial/`.
- Supplied TeX/PDF report preserved at
  `evidence/2026-06-22_hfp_full_solution/`.

## Files

- `main.tex`: upgraded full proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:2410.23063.
- `figures/hfp_conjecture_crop.png`: source Conjecture 5.2.
- `figures/open_problem_crop.png`: source Conjecture 5.5.
