# Kernel Triviality for Every Admissible Heterogeneous Horizon

Source paper: Carolin Kreisbeck and Hidde Schönberger, "Local boundary
conditions in nonlocal hyperelasticity via heterogeneous horizons",
arXiv:2509.03468v1.

Status: likely valid full solution of Remark 4.18.

## Result

For every space dimension, every bounded connected Lipschitz domain, every
admissible horizon, and every kernel satisfying the source paper's
hypotheses,

```text
kernel of the heterogeneous nonlocal gradient = constant functions.
```

The source paper proves this only when the horizon amplitude is sufficiently
small and asks whether that restriction can be removed. This packet removes
it completely.

## Proof mechanism

The source proof already constructs a smooth compactly supported vector field
`w` such that

```text
Q_delta w = 0,     w|_Omega = grad u.
```

For dimensions at least two, take a Newtonian potential `F_j` of each scalar
component `w_j`. Radial integration by parts gives

```text
Q_delta Delta F_j
  = positive weight applied to
    (spherical mean of F_j - F_j at the center).
```

This operator satisfies a weak maximum principle. The potentials decay at
infinity; in dimension two the possible logarithmic term cancels because
each `w_j` has integral zero. Consequently every `F_j`, hence every `w_j`,
vanishes. The dimension-one case follows from the centered-second-difference
maximum principle proved in the previous packet version.

## Files

- `main.tex`: complete all-dimensional proof.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:2509.03468v1.
- `figures/open_problem_crop.png`: source Remark 4.18.
- `code/verify_spherical_mean_identity.py`: exact symbolic check of the new
  multidimensional identity.
- `code/verify_second_difference_identity.py`: exact check of the
  one-dimensional identity.
- `code/scan_1d_spectrum.py` and `code/search_1d_negative_spectrum.py`:
  exploratory checks that motivated the proof; they are not proof.
- `tmp/`: LaTeX and rendered-page intermediates.

## Human review recommendation

Review as a claimed full solution. The highest-value checks are:

1. the two radial integration-by-parts boundary terms at the singular origin;
2. the weak maximum principle for the global operator that equals the
   Laplacian outside the domain;
3. the zero-mean argument for the source auxiliary field in dimension two;
4. the use of the source theorem's no-smallness regularity and compact-support
   conclusions.

The symbolic checks pass, but the proof does not depend on computation.
