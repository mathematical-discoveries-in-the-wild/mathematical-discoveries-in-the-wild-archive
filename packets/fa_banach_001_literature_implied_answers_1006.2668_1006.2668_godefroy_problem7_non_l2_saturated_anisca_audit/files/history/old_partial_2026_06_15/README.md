# Partial packet: Godefroy Problem 7 outside the ell_2-saturated case

status: partial_result

source: Pandelis Dodos, Jordi Lopez-Abad, and Stevo Todorcevic,
*Banach spaces and Ramsey Theory: some open problems*, arXiv:1006.2668v1.

target: Problem 7 asks whether every separable non-Hilbertian Banach space
contains a sequence of closed infinite-dimensional pairwise non-isomorphic
subspaces.

packet: `runs/fa_banach_001/solutions/partial/1006.2668_godefroy_non_l2_saturated_subspaces/`

## Result

The packet proves the following reduction.

If `X` is separable, non-Hilbertian, and not `ell_2`-saturated, then `X`
contains a sequence of closed infinite-dimensional pairwise non-isomorphic
subspaces.

Equivalently, any counterexample to Problem 7 must be `ell_2`-saturated:
every closed infinite-dimensional subspace must contain a further subspace
isomorphic to `ell_2`.

## Scope

This is not a full solution to Problem 7. It reduces the remaining open case to
`ell_2`-saturated separable non-Hilbertian spaces. It does not address whether
such spaces can satisfy the conclusion of Problem 7, nor does it prove the
stronger continuum-many version from Problem 8.

## Verification

- Cheap run indexes were searched for `1006.2668`, the title, Ramsey/open
  problem terms, and Godefroy/pairwise non-isomorphic subspace terms.
- A prior attempt touching the Rosenthal/unique-spreading-model part of this
  survey was read and avoided.
- Web searches for the exact `ell_2`-saturated/pairwise non-isomorphic
  reduction did not locate an existing packet or obvious later exact answer
  during this pass.

## Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: original arXiv source paper.
- `figures/open_problem_crop.png`: crop of Problem 7 and neighboring context.
