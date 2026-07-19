# Full solution packet: Ray's `B_{p,q}` embedding conjecture

Status: human reviewed; proof appears correct, with author follow-up
recommended.

Source paper: Samya Kumar Ray, "On Isometric Embedding `ell_p^m -> S_infty^n`
and Unique operator space structure", arXiv:1911.00241.

## Extracted target

For `1 <= p,q < infinity`, let

`B_{p,q} = {(z_1,z_2) in C^2 : |z_1|^p + |z_2|^q < 1}`.

Ray conjectures in Remark 4.2 that `(C^2, ||.||_{B_{p,q}})` embeds linearly
isometrically into `S_infty` if and only if

`(p,q) = (2,2), (1,2), or (2,1)`.

Evidence crop: `figures/open_problem_crop.png` from page 8 of the source PDF.

The same conjecture is present in the journal version, Bull. London Math. Soc.
52 (2020), 437--447, on printed page 445.

## Candidate theorem

Ray's conjecture is true.

More explicitly, `(C^2, ||.||_{B_{p,q}})` embeds linearly isometrically into
`S_infty` exactly for `(p,q)=(2,2),(1,2),(2,1)`.

## Proof summary

- The positive cases are explicit finite-rank matrix embeddings.
- Ray's Theorem 1.1 excludes `(p,q)=(1,1)` because this is complex `ell_1^2`.
- The previous partial packet proves non-embedding whenever `max(p,q)>2`.
- The new point here excludes the remaining fractional strip. If
  `1<q<2`, then near the first coordinate axis
  `||(1,t)||_{B_{p,q}} = 1 + (1/p)t^q + o(t^q)`.
  But for compact operators, any curve `||T+tS||` near a norm-attaining
  compact operator has top singular value squared given locally by the maximum
  of finitely many real analytic eigenvalue branches. Its first nonzero
  leading power is therefore an integer. The fractional exponent `q` is
  impossible. The same argument at the other axis excludes `1<p<2`.

## Verification

- The packet includes a self-contained proof of the analytic axis-curve lemma,
  using only the standard finite-dimensional Rellich theorem for the isolated
  top spectral cluster of `(T+tS)^*(T+tS)`.
- `code/check_axis_and_embeddings.py` verifies the axis asymptotics and the
  triangular matrix positive embedding numerically.
- The packet PDF was built with `latexmk`.
- Bounded novelty check on 2026-06-13: exact web searches for
  `"B_{p,q}" "S_infty" "embeds isometrically"`,
  `"Ray" "B_{p,q}" "S_infty"`,
  `"On Isometric Embedding" "B_{p,q}" conjecture`,
  `"unique operator space structure" "B_{p,q}" "Ray"`,
  and close variants surfaced Ray's original arXiv page but no later
  resolution.
- Later related Schatten-class embeddability papers should be cited and
  compared, especially Chattopadhyay--Hong--Pal--Pradhan--Ray, but the
  full off-diagonal `B_{p,q}` conjecture did not appear to be answered in
  the checked literature.

## Human review

- `human_review.tex`: human verification note.
- `human_review.pdf`: rendered human verification note.
- `bundle_with_review.pdf`: rendered packet followed by the human review.

## Human-review focus

Review should focus on the compact-operator axis-curve lemma: the top
singular value of a compact analytic perturbation is controlled by finitely
many analytic eigenvalue branches because the norm-one spectral cluster of
`T^*T` is isolated and finite-dimensional.
