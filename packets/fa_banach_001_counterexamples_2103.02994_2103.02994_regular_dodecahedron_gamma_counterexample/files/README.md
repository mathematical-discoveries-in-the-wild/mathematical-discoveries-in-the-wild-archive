# Regular-dodecahedron counterexample to the Gamma characterization

Status: `candidate_counterexample_likely_valid`

Model: `GPT5.6`

## Source problem

- Emanuel Milman, *A sharp centro-affine isospectral inequality of
  Szegö--Weinberger type and the L^p-Minkowski problem*, arXiv:2103.02994.
- Exact location: Remark 4.2, PDF page 20, after Theorem 4.1(3).
- Local source: `source_paper.pdf`.

The paper asks whether an origin-symmetric tangential body of a Euclidean ball
whose `Gamma_{-2}` and `Gamma_{-4}` bodies are Euclidean must itself be an
ellipsoid.

## Counterexample

Let `U` be the 12 unit vertices of a regular icosahedron and let

```text
K = {x in R^3 : <x,u> <= 1 for every u in U}.
```

Then `K` is the regular dodecahedron circumscribed about the unit ball. It is
origin symmetric and tangential, but it is not an ellipsoid. Its equal-area
facet normals satisfy the exact identities

```text
sum_u <x,u>^2 = 4 |x|^2,
sum_u <x,u>^4 = (12/5) |x|^4.
```

Writing `a` for the common facet area, the inradius-one pyramid formula gives
`V(K)=4a`. Consequently,

```text
Gamma_{-2} K = B_2^3,
Gamma_{-4} K = (5/3)^(1/4) B_2^3.
```

This is exactly the equality constant `((n+2)/3)^(1/4)` from Theorem 4.1(3)
when `n=3`. Thus the asserted property does not characterize ellipsoids.

## Verification

From this packet directory run:

```bash
conda run --no-capture-output -n sandbox python \
  code/verify_icosahedral_moments.py
```

The verifier uses exact SymPy arithmetic over `Q(sqrt(5))`; it confirms all 12
normals and the two polynomial moment identities.

## Novelty and review

A bounded search on 19 July 2026 covered the run's lightweight indexes and
local source corpus plus exact web combinations of arXiv:2103.02994,
`Gamma_{-4}`, `tangential body`, `dodecahedron`, and `spherical 4-design`. It
found the source paper and classical spherical-design material but no later
answer or this counterexample. Novelty confidence is moderate-high, not a
substitute for a full bibliographic review.

Human review should focus on the source's normalization of `Gamma_{-p}` and
the conversion from equal-area tangential facets to the discrete `S_p K`
measure. Those steps are written explicitly in the packet.

## Files

- `solution_packet.pdf`: rendered proof packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: rendered source evidence.
- `code/verify_icosahedral_moments.py`: exact certificate.

