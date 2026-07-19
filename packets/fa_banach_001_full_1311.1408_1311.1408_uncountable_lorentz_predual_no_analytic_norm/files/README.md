# Candidate full solution: no analytic norm on uncountable Lorentz preduals

Source paper: Victor Bible, *Using boundaries to find smooth norms*,
arXiv:1311.1408.

Status: candidate full negative answer, likely valid, pending expert review.

## Source question

Remark 3.10 asks whether, for uncountable `A`, the Lorentz predual
`X = d_*(w,1,A)` has an analytic renorming. Bible had just shown that these
spaces have `C^\infty` smooth equivalent renormings.

## Result

For every standard decreasing Lorentz weight `w` and every uncountable set
`A`, the space `d_*(w,1,A)` has no equivalent analytic norm.

Equivalently, the answer to Remark 3.10 is negative under the usual Lorentz
weight convention.

## Proof mechanism

The earlier partial packet handled slow weights by proving that all continuous
homogeneous polynomials are countably supported. This full packet handles the
remaining finite-`ell_q` weights by a different obstruction.

For `|F| = m`, set

```text
u_F = (W_m / m) sum_{a in F} e_a.
```

Then `||u_F||_* = 1`. The core lemma proves that every fixed finite family of
continuous homogeneous polynomials becomes arbitrarily small on some far-out
flat average `u_F`. Diagonal finite-`ell_q` terms vanish because
`w in ell_q` implies `W_m^q / m^{q-1} -> 0`; all other equality patterns are
handled by Ramsey thinning and sign averaging.

Thus no polynomial separates the origin from the unit sphere. An analytic norm
would produce an analytic separating function whose Taylor series at the
origin converges on a ball containing a small separating sphere; truncating
that series and applying the flattening lemma gives the contradiction.

## Files

- `main.tex`: full proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of the source paper.
- `figures/open_problem_crop.png`: crop of Example 3.9 and Remark 3.10.
- `code/crop_open_problem.py`: crop-generation script inherited from the
  earlier partial packet.
- `history/slow_weight_partial_packet/`: earlier lane-7 partial packet, kept
  as provenance after supersession.

## Novelty check

Cheap run indexes were searched for `1311.1408`, the source title,
`d_*(w,1,A)`, `Lorentz predual`, and `analytic renorming`. The only exact
hit was the earlier slow-weight partial packet.

Web searches on 2026-06-20 for the exact Lorentz-predual analytic-renorming
question and close variants did not locate a later full answer. The
Dantas-Hajek-Russo paper gives the analytic-separation template for
`c0(omega_1)`, but does not answer this Lorentz-predual question.

## Review focus

Review Lemma 2, especially:

- the Ramsey thinning of polynomial coordinate coefficients by equality
  pattern;
- the sign-averaging argument forcing a nonzero spreading coefficient with
  block sizes `(r_1,...,r_s)` to imply `w in ell_{r_i}` for every block size;
- the flattening estimate
  `m^s (W_m/m)^(r_1+...+r_s) -> 0` once those finite-`ell_r_i` conditions hold.
