# Derivative Norm Transfer for the CLMS Jacobian Problem

Result type: `partial`

Status: candidate partial result, likely valid pending human review.

Source paper:

- Sauli Lindberg, "A note on the Jacobian problem of Coifman, Lions, Meyer and
  Semmes", arXiv:2208.13576.
- Local source PDF: `source_paper.pdf`.
- Evidence crops:
  - `figures/open_problem_crop.png`
  - `figures/self_adjoint_modification_crop.png`

## Source Problem Context

After proving that the dual space `X_Q^*` associated with the planar Jacobian
quadratic operator

`Q omega = |S omega|^2 - |omega|^2`

is not strictly convex, the source paper says it is unclear whether the
analogous statement holds for the Gateaux derivative

`(omega, gamma) -> Q'_omega gamma`.

## Claimed Contribution

This packet proves that the answer is yes, in the exact dual-ball geometry
sense of the source corollary.

For any quadratic operator in the source framework, the self-adjoint block
operator associated with the Gateaux derivative induces the same `X_Q` norm on
the coefficient space:

`||b||_{X_tildeQ} = ||tilde T_b|| = ||T_b|| = ||b||_{X_Q}`.

Therefore `X_tildeQ` and `X_Q` are isometric by the identity map, their dual
unit balls have the same extreme points, and strict convexity is identical for
the two dual norms.

Applying the source paper's Corollary 1.11 to the planar Jacobian gives

`ext(B_{X_tildeQ^*}) subsetneq S_{X_tildeQ^*}`.

## Novelty Caution

The proof uses the source paper's own self-adjoint modification lemma and norm
identity. The contribution is the explicit observation that this identity
settles the later derivative strict-convexity remark. It does not address the
main Jacobian surjectivity problem or Question 1.6.

Cheap index checks found no prior packet for arXiv:2208.13576. Web exact-phrase
checks found the source paper but no direct later answer to the derivative
strict-convexity remark.

## Files

- `main.tex`: self-contained LaTeX packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source paper PDF.
- `figures/open_problem_crop.png`: crop around Corollary 1.11 and the unclear
  derivative remark.
- `figures/self_adjoint_modification_crop.png`: crop around the block
  modification lemma and derivative formula.
- `code/make_evidence_crops.py`: reproducible crop script.
- `tmp/`: build and render intermediates.

## Human Review Notes

Verifier focus:

- Check that the derivative operator is interpreted with the same Hilbert
  direct-sum norm as the source's modified operator.
- Check that the `X_Q` norm definition for the modified operator is exactly
  the operator norm of `tilde T_b`; this uses self-adjointness/numerical-radius
  equality built into Assumption 1.3.
- Check that the statement transferred is only the dual norm geometry
  `ext(B) subsetneq S`, not surjectivity of the derivative map.
