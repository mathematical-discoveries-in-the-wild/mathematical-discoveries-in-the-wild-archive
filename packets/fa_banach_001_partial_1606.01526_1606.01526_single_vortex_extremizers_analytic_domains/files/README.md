# Single-vortex extremizers on analytic planar domains

Status: `candidate_partial_solution_likely_valid_needs_human_review` for
Open Problem 1 of arXiv:1606.01526.

## Result

Let `Omega` be a bounded simply connected planar domain with connected
real-analytic boundary, let `a` be in `Omega`, and let `d` be a nonzero
integer.  Put

```text
w_(a,d)(x) = ((x-a)/|x-a|)^d
```

and consider its equivalence class

```text
E_(a,d) = {w_(a,d) exp(i phi) : phi in W^{1,1}(Omega;R)}.
```

The source's geometric formula gives

```text
inf_{u in E_(a,d)} integral_Omega |grad u|
    = 2 pi |d| dist(a,boundary Omega).
```

The packet proves a complete attainment classification:

> The infimum is attained if and only if `Omega` is the disk centered at
> `a`.

Consequently, on the interior of a noncircular ellipse, no equivalence class
with exactly one isolated vortex (of any nonzero multiplicity and at any
interior point) can realize property `(P1)`.

## Proof mechanism

Let `r=dist(a,boundary Omega)`.  Every competitor has degree `d` on almost
every circle centered at `a` of radius less than `r`. Polar slicing gives

```text
integral_Omega |grad u| >= 2 pi |d| r.
```

If equality holds, every inequality in this estimate is an equality. Hence
`u` has zero radial derivative in the inscribed disk and zero full gradient
outside it. Thus `u(rho,theta)=q(theta)` in the disk. At every point where the
inscribed circle lies strictly inside `Omega`, the constant exterior trace
forces `q` to be locally constant. Since `q` has nonzero degree, the contact
set between the inscribed circle and `boundary Omega` must have positive arc
length. For a connected real-analytic boundary, positive-length contact with
a circle forces the entire boundary to be that circle by the real-analytic
identity principle.

## Scope

This is a full classification of minimizer attainment for all single-vortex
classes on real-analytic simply connected planar domains. It is a substantial
partial result for Open Problem 1, not a full solution: an ellipse could in
principle satisfy `(P1)` through a class with several vortices or a more
general non-atomic singularity distribution.

## Packet contents

- `solution_packet.pdf`: theorem, proof, verification notes, scope, and
  bounded novelty check.
- `source_paper.pdf`: arXiv:1606.01526.
- `figures/open_problem_crop.png`: Open Problems 1 and 2 on source PDF page
  22, including the noncircular-ellipse conjecture.
- `VERIFICATION.md`: separate proof audit.
- `tmp/`: LaTeX build and render intermediates.

Bounded arXiv/web searches by title, DOI, authors, the exact ellipse sentence,
`P1`, `single vortex`, and attainment terminology found the source paper and
its short announcement but no later result proving this classification or
resolving the ellipse question. This is evidence, not an exhaustive novelty
guarantee; expert mathematical and literature review is recommended.
