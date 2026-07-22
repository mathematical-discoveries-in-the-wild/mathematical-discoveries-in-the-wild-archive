# Verification report

Status: `candidate_partial_result_likely_valid`

## Mathematical checks

- Checked the exact transcription of Questions 3.9 and 3.10 against arXiv PDF
  page 13.
- Checked the sign step in the concentration lemma: if
  (x^*(a)y^*(b)>1-\delta), the two scalar factors have the same sign and both
  have modulus (>1-\delta); replacing ((a,b)) by
  ((\sigma a,\sigma b)) leaves (a\otimes b) unchanged.
- Checked the convex-combination estimate: mass outside the good elementary
  tensors tends to zero when the tensor functional tends to one.
- Checked the bidual step: Goldstine approximation plus norm distance to
  (x\otimes B_Y) places the entire norm-one face in
  (M_x^{**}(B_{Y^{**}})).
- Checked that (M_x^{**}) is isometric and injective because
  (M_x(y)=x\otimes y) is an isometry for (x\in S_X).
- Checked that the midpoint identity then reduces exactly to extremality of
  (y) in (B_{Y^{**}}), which is the definition of preserved extreme.
- Checked the norm-attainment argument for countably infinite
  representations by isolating one positive coefficient and grouping the
  remaining convex series into a point of the unit ball.

No computational verification is needed; both arguments are qualitative.

## Literature check

Searched arXiv by the exact source questions and close phrases. The relevant
later source located was arXiv:2510.21234, whose tensor theorem assumes every
bounded operator (X\to Y^*) is compact together with an approximation
property. It explicitly describes that as a partial answer. No exact match for
the two present subcases was found.

## Rendering check

The packet was compiled with `latexmk -pdf -interaction=nonstopmode
-halt-on-error -outdir=tmp main.tex`. All pages were rendered at 150 DPI and
visually inspected for clipping, overflow, broken formulas, crop readability,
and page transitions.

## Human-review recommendation

Review as a likely valid partial result. The highest-value check is the face
concentration lemma; the remainder is a direct bidual extremality argument.
