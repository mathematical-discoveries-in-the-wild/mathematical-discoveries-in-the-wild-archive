# Verification Report

Candidate: arXiv:1902.02363, Remark 5.12(i), removal of compactness and
finite-dimensionality from Example 5.11

## Claim Checked

Affine sections of a closed ball by fibers of a closed-range Hilbert-space
operator have an exact center-radius representation and exact Hausdorff
distance. This yields optimal-value continuity for uniformly continuous
objectives with arbitrary kernels, and for continuous objectives with
finite-dimensional kernels. A bounded continuous counterexample shows the
uniform-continuity issue is real for infinite-dimensional kernels.

## Verdict

`likely valid`

Confidence: 96/100.

The geometry and counterexample are exact. Residual uncertainty concerns
novelty and whether the source authors would label this broad Hilbert-ball
theorem a full answer to their intentionally open-ended research direction.

## Step Check

| Step | Status | Notes |
| --- | --- | --- |
| Bounded inverse `G` exists | valid | `L|_(ker L)^perp` is a bounded bijection onto the assumed closed range. |
| Fiber formula | valid | The range coordinate is fixed by `G`; Pythagoras leaves a kernel ball. |
| Exact Hausdorff formula | valid | Orthogonality separates center distance from distance to the kernel ball. The zero-kernel exception is stated separately. |
| Local Lipschitz bound | valid | Rationalize the square-root radii on `||z||<=b<r`. |
| Boundary Hölder bound | valid | Uses `(sqrt(u)-sqrt(v))^2<=|u-v|` and `||z_s-z_t||<=2r`. |
| Uniformly continuous objective is bounded | valid | Chain any two points along the line segment in the bounded convex ball. |
| Value stability without minimizers | valid | Hausdorff approximation plus a uniform modulus controls infima and suprema in both directions. |
| Mere continuity for finite-dimensional kernel | valid | A convergent sequence of center-radius pairs times the compact kernel ball has compact image. |
| Escaping-well supports avoid `A_0` | valid | Their radii are `t_n/3`, while center distance to `A_0` is exactly `t_n`. |
| Escaping-well function is continuous | valid | Orthogonal directions make centers uniformly separated; the support family is locally finite and each tent vanishes at its boundary. |
| Discontinuity conclusion | valid | `f=0` on `A_0`, `f(y_n)=-1` on `A_tn`, and `t_n->0`. |

## Adversarial Checks

- `ker L = {0}`: the radius term does not affect a singleton section; the
  theorem explicitly separates this case.
- Boundary parameters: local Lipschitz continuity is claimed only in the
  interior; the global statement is only `1/2`-Hölder.
- Nonattainment for infinite-dimensional fibers: the uniformly continuous
  argument uses infima and suprema, not minimizers.
- Continuous objectives may be unbounded on the full noncompact ball: the
  finite-kernel argument only needs boundedness on a compact sequential tube.
- Support accumulation in the counterexample: impossible because the centers
  have a uniform positive separation.
- Complex Hilbert-space conventions: the theorem is explicitly stated for
  real Hilbert spaces, matching the source optimization setting.

The deterministic checker samples the exact distance identity in finite
dimensional proxies, audits both quantitative bounds, and checks the escaping
well separation constants.

Command:

```text
conda run --no-capture-output -n sandbox python code/check_hilbert_ball_fibers.py
```

Expected final line: `all Hilbert-ball fiber checks passed`.

## Literature Check

The cheap run indexes contain no packet for arXiv:1902.02363 or the exact
Hilbert-ball theorem. Bounded arXiv/web searches used the source sentence,
`affine sections Hilbert ball Hausdorff distance`, `Hilbert ball optimal value
function affine constraint`, and noncompact Berge-theorem terms. They found
the source and broad noncompact-image maximum-theorem papers, but no exact
match. This is not an exhaustive novelty certification.

## Human Review Recommendation

`send to human`

Mathematically, review the asymmetric Hausdorff calculation and the compact
sequential tube. For positioning, decide whether to present the packet as a
full answer to the source's existential extension request or as a strong
solved class.
