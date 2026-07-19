# Partial packet: Hilbert reductions for the isometrically homogeneous problem

status: partial_result

source: Marek Cuth, Martin Dolezal, Michal Doucha, and Ondrej Kurka,
*Polish spaces of Banach spaces. Complexity of isometry and isomorphism
classes*, arXiv:2204.06834v1.

target: Question 3 in Section 6 asks whether a separable infinite-dimensional
Banach space that is linearly isometric to all of its closed
infinite-dimensional subspaces must be linearly isometric to `ell_2`.

packet: `runs/fa_banach_001/solutions/partial/2204.06834_isometric_homogeneous_hilbert_reductions/`

## Classification

This is a strengthened partial result, not a full solution and not a
counterexample. The attached report explicitly leaves the source question open.
It verifies the previous almost-Hilbertian stabilization theorem, corrects the
square-root normalization in the symmetric-distortion corollary, and adds
structural reductions for any possible non-Hilbert counterexample.

## Result

If an isometrically homogeneous space has arbitrarily almost-Hilbertian
infinite-dimensional restrictions, then it is isometric to `ell_2`. More
intrinsically, if the infimum of `d(Y, ell_2)` over closed infinite-dimensional
subspaces `Y` is `1`, then the space is isometric to `ell_2`.

For a hypothetical non-Hilbert counterexample, the packet records necessary
structure:

- the Banach-Mazur distance to Hilbert space is attained by an optimal Hilbert
  norm;
- every infinite-dimensional subspace realizes the full optimal distortion
  interval `[1,D]`;
- optimal Hilbert structures are unique modulo compact positive perturbations;
- every linear isometric embedding is a compact perturbation of a Hilbert
  isometric embedding;
- after passing to an isometric subspace, the space has a model on `ell_2`
  where the unilateral shift is both a Banach-space isometry and a Hilbert
  isometry.

The remaining bottleneck is to rule out a renorming of `ell_2` with this full
profile when `D>1`.

## Upgrade History

- `2026-06-22`: upgraded from the earlier almost-Hilbertian obstruction packet
  using the supplied report `isometric_homogeneity_report`.
- Previous active packet preserved at
  `history/2026-06-22_previous_almost_hilbertian_partial/`.
- Supplied TeX/PDF report preserved at
  `evidence/2026-06-22_isometric_homogeneity_report/`.

## Files

- `main.tex`: upgraded partial packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: original arXiv source paper.
- `figures/open_problem_crop.png`: crop of Section 6, Question 3.
