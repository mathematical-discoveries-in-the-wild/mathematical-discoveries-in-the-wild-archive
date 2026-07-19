# Exact infinite-dimensional stability for affine sections of Hilbert balls

Status: `candidate_full_likely_valid`

Source: Daniel Reem, Simeon Reich, and Alvaro De Pierro, *Stability of the
optimal values under small perturbations of the constraint set*,
arXiv:1902.02363v4, Pure and Applied Functional Analysis 5 (2020), 705-731.

Source location: Remark 5.12(i), page 19. The authors ask whether the
compactness and finite-dimensionality assumptions in Example 5.11 can be
removed, at least in interesting cases.

## Full affirmative Hilbert-ball extension

Let `H,Y` be arbitrary real Hilbert spaces, let `L:H->Y` be bounded with
closed range, and let `C` be a closed ball. With

```text
N = ker L,  M = N^perp,  G = (L|_M)^(-1),
z_t = G(t-Lc),  rho_t = sqrt(r^2-||z_t||^2),
```

the affine section has the exact form

```text
A_t = C intersect L^(-1)(t) = c + z_t + rho_t B_N.
```

If `N` is nonzero, its Hausdorff distance is

```text
D_H(A_s,A_t)^2 = ||z_s-z_t||^2 + |rho_s-rho_t|^2.
```

For a zero kernel the sections are singletons and only the first term remains.
The section map is locally Lipschitz over interior parameters and globally
1/2-Hölder up to the boundary.

Consequences for optimal values:

- Every uniformly continuous objective on `C` gives continuous infimal and
  supremal value functions, for an arbitrary kernel. Lipschitz objectives
  inherit the exact Hausdorff modulus.
- If `ker L` is finite-dimensional, every continuous objective works. The
  fibers along any convergent parameter sequence lie in a single compact set.

This removes both ambient finite dimensionality and compactness of the
constraint ball.

## Sharpness

For `H = R direct-sum ell^2`, `L(a,x)=a`, and the unit ball, the fibers are

```text
A_t = {(t,x): ||x|| <= sqrt(1-t^2)}.
```

Localized depth-one wells around boundary points
`y_n=(t_n,sqrt(1-t_n^2)e_n)`, with `t_n->0`, produce a bounded continuous
objective `f` satisfying

```text
inf(A_0) f = 0,       inf(A_tn) f = -1.
```

The well centers escape along orthogonal kernel directions, so the supports
are locally finite. This proves that mere continuity cannot replace uniform
continuity for arbitrary infinite-dimensional kernels.

## Scope and novelty

The packet fully supplies the kind of infinite-dimensional, noncompact case
requested by the source and includes the sharp obstruction for continuous
objectives. It does not cover arbitrary convex bodies or arbitrary Banach
spaces.

Cheap run indexes were searched using the arXiv id, source title, Hilbert
balls, affine fibers, Hausdorff continuity, and finite-dimensional kernels. A
bounded arXiv/web search used the exact source sentence and close terms. It
found the source and general noncompact Berge-theorem literature, but no exact
matching Hilbert-ball fiber and sharpness theorem. This is not an exhaustive
novelty certification.

## Packet contents

- `main.tex`: exact geometry, optimal-value theorem, sharp counterexample,
  proof, scope, and references.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: official arXiv PDF.
- `figures/open_problem_crop.png`: full-width source crop from page 19.
- `code/check_hilbert_ball_fibers.py`: deterministic numerical audit.
- `verification.md`: adversarial proof verification.

Human review recommendation: **send to a functional analyst or variational
analyst**. The key checks are the exact Hausdorff formula, the compact-union
argument, and local finiteness of the escaping wells.
