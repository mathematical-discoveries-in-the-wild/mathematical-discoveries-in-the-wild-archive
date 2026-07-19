# Complemented BCAP Subspace Obstruction for Ostrovskii's Problem

Result type: `partial`

Status: candidate partial result, likely valid pending human review.

Source paper:

- Sheldon Dantas, Mingu Jung, Gonzalo Martinez-Cervantes,
  "On the existence of non-norm-attaining operators", arXiv:2102.06452.
- Local source PDF: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

## Claimed Contribution

This packet proves:

```text
If an infinite-dimensional Banach space X contains a complemented
infinite-dimensional subspace Y with the bounded compact approximation
property, then some operator on X does not attain its norm.
```

Equivalently, any positive solution to Ostrovskii's problem must have no
complemented infinite-dimensional BCAP subspace. In particular, it cannot
contain a complemented infinite-dimensional subspace with a Schauder basis.

## Mechanism

Let `P:X -> Y` be a bounded projection. BCAP on `Y` gives uniformly bounded
compact operators `K_alpha:Y -> Y` with `K_alpha -> Id_Y` strongly. Then
`J K_alpha P`, where `J:Y -> X` is inclusion, are compact and hence strictly
singular operators on `X`, uniformly bounded and SOT-converging to `P`.

Since `P` is not strictly singular on its infinite-dimensional range, the
strictly singular unit ball is not SOT closed. The Dantas--Jung--Martinez-
Cervantes James-property criterion, applied to the strictly singular ideal,
then yields a non-norm-attaining operator.

## Scope

This is not a full solution of Ostrovskii's problem. It rules out a broad
complemented-subspace configuration, but a hypothetical positive example could
still be hereditarily indecomposable or otherwise have no complemented
infinite-dimensional subspaces with BCAP.

## Novelty Caution

The source paper's TeX comments already mention that the strictly singular
ideal fits the SOT-closure method. This packet extracts and records a concrete
structural consequence of that route. Treat it as a modest but useful partial
obstruction.

## Files

- `main.tex`: self-contained LaTeX packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source paper PDF.
- `figures/open_problem_crop.png`: source crop around Ostrovskii's problem.
- `tmp/`: build intermediates.

## Human Review Notes

Verifier focus:

- Check that the compact approximants on `Y` remain uniformly bounded after
  transport through the projection `P`.
- Check that the SOT limit is the non-strictly-singular projection `P`.
- Check that the strictly singular ideal invocation is valid under the
  reflexivity forced by rank-one norm-attainment.

