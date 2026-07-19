# Partial packet: almost-Hilbertian obstruction for Question 3

status: partial_result

source: Marek Cuth, Martin Dolezal, Michal Doucha, and Ondrej Kurka,
*Polish spaces of Banach spaces. Complexity of isometry and isomorphism
classes*, arXiv:2204.06834v1.

target: Question 3 in Section 6 asks whether a separable infinite-dimensional
Banach space that is linearly isometric to all of its closed
infinite-dimensional subspaces must be linearly isometric to `ell_2`.

packet: `runs/fa_banach_001/solutions/partial/2204.06834_isometric_homogeneous_almost_hilbertian_obstruction/`

## Result

This packet proves a partial obstruction. Let `X` satisfy the hypothesis of
Question 3. By the homogeneous Banach space theorem cited in the source paper,
`X` is isomorphic to `ell_2`. Suppose, for one equivalent Hilbert norm `h` on
`X`, that the given Banach norm has arbitrarily Hilbertian restrictions: for
every `epsilon > 0`, some closed infinite-dimensional subspace `Y` and scalar
`a > 0` satisfy

```text
a h(y) <= ||y|| <= (1+epsilon) a h(y),  y in Y.
```

Then `X` is linearly isometric to `ell_2`.

Equivalently, any non-Hilbert counterexample to Question 3 must be uniformly
distortive relative to every equivalent Hilbert norm: for each such Hilbert
norm, there is a positive distortion gap which persists on every closed
infinite-dimensional subspace.

## Scope

This is not a full answer to Question 3. The missing case is precisely the
distortive Hilbert-renorming case. The tempting shortcut using Hilbert
non-distortion is invalid in general, since Hilbert space admits distortive
equivalent norms.

## Verification

- Cheap run indexes were searched for `2204.06834`, the paper title, and core
  question keywords; no prior packet or attempt for this target was found.
- Local source text and de Rancourt's paper were inspected.
- Web searches for the exact isometrically homogeneous Banach-space question
  did not locate a later full resolution during this pass.

## Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: original arXiv source paper.
- `figures/open_problem_crop.png`: crop of Section 6, Question 3.
