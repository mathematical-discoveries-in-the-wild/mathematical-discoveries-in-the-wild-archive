# Partial solution packet: `B_{p,q}` non-embedding when one exponent exceeds `2`

Status: candidate partial result for Ray's `B_{p,q}` isometric-embedding
conjecture.

Source paper: Samya Kumar Ray, "On Isometric Embedding `ell_p^m -> S_infty^n`
and Unique operator space structure", arXiv:1911.00241.

## Extracted target

Ray defines `B_{p,q}={(z_1,z_2): |z_1|^p+|z_2|^q<1}` and denotes by
`||.||_{B_{p,q}}` the associated Minkowski norm on `C^2`. Remark 4.2 proves
non-embedding into `S_infty` for `2<p,q<infty`, records the positive embedding
for `B_{1,2}`, and conjectures that `(C^2,||.||_{B_{p,q}})` embeds
isometrically into `S_infty` if and only if `(p,q)=(2,2),(1,2),(2,1)`.

Evidence crop: `figures/open_problem_crop.png` from page 8 of the source PDF.

## Candidate theorem

Let `1 <= p,q < infinity`. If `max(p,q)>2`, then
`(C^2,||.||_{B_{p,q}})` does not embed linearly isometrically into `S_infty`.

This strictly extends the source paper's printed consequence for `2<p,q<infty`
to all cases where at least one exponent is greater than `2`, including the
edge cases `(1,q)`, `(2,q)`, `(p,1)`, and `(p,2)` with the other exponent
greater than `2`.

## Proof idea

Ray's proof of Theorem 1.2 gives a criterion for any two-dimensional complex
norm satisfying five elementary properties. The only property used in the
source to restrict to `p,q>2` is the statement that `(z_1,z_2) -> (z_1,c z_2)`
is not a contraction from the normed space to `ell_2^2` for every `0<c<=1`.
For `B_{p,q}`, that property already holds whenever `q>2`, regardless of
`p`.

Indeed, for small `y>0`, set `x=(1-y^q)^{1/p}`. Then `(x,y)` is on the
`B_{p,q}` unit sphere, while

`x^2+c^2 y^2 = (1-y^q)^{2/p}+c^2 y^2 > 1`

for all sufficiently small `y`, because `q>2`. Thus the map to `ell_2^2` is
not contractive. The remaining four properties are immediate from the
Reinhardt form of the unit ball. Ray's descent argument therefore excludes an
isometric embedding when `q>2`. If `p>2`, swap the two coordinates and apply
the same argument.

## Verification

- Local duplicate check: searched the run registry, solution packets, and
  attempt notes for `1911.00241`, `S_infty`, and the `B_{p,q}` conjecture; no
  existing packet or attempt was found.
- Computational sanity check: `code/check_Bpq_obstruction.py` searches small
  witnesses to the non-contraction property for representative `q>2` values
  and checks the known triangular positive case `B_{1,2}` numerically.
- Novelty status: local-run novelty only. No broad external literature search
  was performed for this partial result.

## Limitations

The packet does not settle the full conjecture. In particular, it does not
exclude the remaining region where `1<=p,q<=2` except for cases already
handled in the source paper, nor does it give a new positive embedding.

Human review should focus on the use of Ray's Remark 4.2 as a general
criterion and on the small-`y` non-contraction argument for `q>2`.
