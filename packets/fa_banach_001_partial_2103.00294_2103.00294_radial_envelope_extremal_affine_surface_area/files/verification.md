# Verification Report

Candidate: `2103.00294_radial_envelope_extremal_affine_surface_area`

## Claim checked

Under the finite tail-limsup and strict tail-gap hypotheses on
`h_phi(t)=phi(t)/sqrt(t)`, the inner maximal functional is finite, attained,
Hausdorff-continuous, and bounded sharply by its radial envelope. The class
strictly contains the source decreasing-ratio class.

## Verdict

`likely valid`

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Radial upper bound | valid | Hoehner's affine isoperimetric inequality gives `as_phi(C) <= n|B_n| h_phi(vrad(C)^(-2n))`; volume inclusion gives the envelope domain. |
| Finiteness | valid | Finite tail limsup plus continuity of `h_phi` makes every `H_phi(a)` finite. |
| Non-collapse | valid | A degenerate maximizing subsequence has limsup at most `n|B_n|L_phi`, while the tail-gap condition supplies a smaller centered ball with strictly larger value. |
| Attainment | valid | Blaschke selection, centroid continuity, and upper semicontinuity of `as_phi` finish the compactness argument once degeneration is excluded. |
| Sharpness on balls | valid | Every `t >= R^(-2n)` is realized by the centered ball of radius `t^(-1/(2n))` inside `RB_n`. |
| Hausdorff continuity | valid | Inclusion monotonicity plus `IS_phi(cK) <= c^n IS_phi(K)` for `c >= 1` yields the two-sided squeeze. |
| Strict class extension | valid | Strictly decreasing positive `h_phi` has a finite tail limit and a strict tail gap. For `log(1+t)`, the derivative changes sign once, so its ratio is nonmonotone but its tail limit is zero. |

## Counterexample and edge-case audit

- `phi(t)=sqrt(t)+t^(1/4)` shows why replacing the source's asserted zero tail
  limit by a strict tail gap is necessary. It belongs to the source
  decreasing-ratio class but has tail limit `1`.
- If `limsup h_phi(t)=infinity`, arbitrarily small centered balls make
  `IS_phi(K)=infinity`; thus some tail boundedness is genuinely needed.
- If the strict tail gap is removed, the presented compactness proof can no
  longer exclude degeneration. No necessity claim is made.
- The logarithmic example invalidates any attempted verbatim extension of the
  source identity `IS_phi(B_n)=as_phi(B_n)`, because its maximizing radius is
  strictly less than one.

## Computational check

`python code/check_log_example.py` locates the positive root of
`2t/(1+t)-log(1+t)` and samples the derivative signs on both sides. This only
checks the reported decimal value; the uniqueness proof in `main.tex` is
analytic.

## External dependencies

- The general affine isoperimetric inequality and upper semicontinuity quoted
  in Hoehner's Sections 2.1 and 7.1.
- Blaschke's selection theorem and standard continuity of volume and centroid
  under nondegenerate Hausdorff convergence.

## Remaining scope gap

The source asks broadly for a richer function class supporting the results of
the article. This packet proves a coherent group of inner-maximal results but
does not extend the full Blaschke-Santalo theorem or its equality cases.

Confidence: **88/100**.

Human recommendation: **send to human review**.

