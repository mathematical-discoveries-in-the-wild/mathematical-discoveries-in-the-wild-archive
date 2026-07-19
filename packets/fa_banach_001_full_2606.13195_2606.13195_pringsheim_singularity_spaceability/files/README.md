# Candidate Solution: Spaceability of Pringsheim-Singular Smooth Disk-Algebra Functions

Status: human reviewed; rejected as a solution to the original question.

## Source Question

- Source paper: Andreas Debrouwere, *Some results about spaceability in function spaces*, arXiv:2606.13195.
- Location: Remark 3.15.
- Question: whether the set of functions in `A^\infty(D)` whose boundary restriction is Pringsheim singular at every point is spaceable in `A^\infty(D)`.
- Screenshot: `figures/open_problem_crop.png`.
- Source PDF retained as `source_paper.pdf`.

## Result

The claimed affirmative answer is not established by the packet.

The packet constructs a closed infinite-dimensional subspace `X` of
`A^\infty(D)` such that every nonzero element of `X` has the unit circle as a
natural boundary. This appears to prove a weaker natural-boundary statement,
but it does not by itself imply that the boundary restriction is Pringsheim
singular in the sense of the original reference.

In Bernal-Gonzalez--Bonilla--Lopez-Salazar--Seoane-Sepulveda, Pringsheim
singularity is defined for the boundary function `f_0(t)=f(e^{it})`: at each
point, the Taylor series of `f_0` must have radius of convergence zero. The
packet does not prove the corresponding pointwise derivative-growth condition.

## Construction

Use the master Hadamard gap sequence `2^k`, partition the index set `N` into
infinitely many infinite blocks, and define one smooth lacunary series per
block:

```text
g_m(z) = sum_j exp(-sqrt(n_{m,j})) z^{n_{m,j}}.
```

The coefficients decay faster than any inverse power, so each `g_m` belongs
to `A^\infty(D)`. Because all blocks lie inside the same master lacunary
support, every nonzero element of the closed span still has lacunary Taylor
support. At least one block appears with a nonzero scalar, forcing the radius
of convergence to be exactly `1`. Hadamard's gap theorem then gives the unit
circle as a natural boundary.

## Verification

- `code/crop_open_question.py` regenerates the screenshot crop.
- `code/check_lacunary_construction.py` performs finite sanity checks on the
  block partition, lacunarity, and coefficient decay.
- The computational script is not the proof; the proof is the lacunary-series
  argument in `solution_packet.pdf`.

## Novelty Status

This should not be filed as a correct full solution to the Pringsheim-singular
spaceability problem. It may still be useful as a candidate proof of a weaker
statement about natural boundaries or nowhere real analytic boundary behavior.

## Files

- `solution_packet.pdf`: rendered human-facing packet.
- `main.tex`: LaTeX source.
- `human_review.tex`: human verification note source.
- `human_review.pdf`: rendered human verification note.
- `bundle_with_review.pdf`: solution packet followed by the human verification
  note.
- `source_paper.pdf`: original source paper.
- `figures/open_problem_crop.png`: screenshot of Remark 3.15.
- `code/crop_open_question.py`: recreates the screenshot crop.
- `code/check_lacunary_construction.py`: finite sanity checks for the construction.

## Human Review

The proof is rejected as a solution to the original question. Hadamard's gap
theorem gives a natural boundary, but the original notion of Pringsheim
singularity requires zero Taylor radius of the boundary parametrization at
every point. The packet does not establish the necessary derivative-growth
lower bounds and does not rule out cancellations in the derivative sums.
