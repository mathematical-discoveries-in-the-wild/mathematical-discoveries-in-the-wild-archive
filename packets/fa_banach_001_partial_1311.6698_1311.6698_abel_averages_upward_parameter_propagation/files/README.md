# Upward propagation of nonlinear Abel averages

Status: `candidate_partial_result_likely_valid`

Update: the remaining downward direction has now been settled negatively by
the full counterexample in
`solutions/counterexamples/1311.6698_radial_abel_average_nonuniqueness/`.
The upward theorem in this packet remains valid and explains why the
counterexample necessarily fails below its known parameter.

Source: F. Bracci, Y. Kozitsky, and D. Shoikhet, *Abel averages and
holomorphically pseudo-contractive maps in Banach spaces*, arXiv:1311.6698;
J. Math. Anal. Appl. 423 (2015), no. 2, 1580-1593,
DOI 10.1016/j.jmaa.2014.10.079.

## Result

Let `B` be the open unit ball of a complex Banach space, let `D` be any
subset of `B`, and let `h:D -> X`. Suppose that for one `mu>0` the inverse

`Phi_mu = (I-mu h)^{-1}: B -> D`

is well defined and holomorphic. Then, for every `alpha >= mu`, the Abel
average `Phi_alpha=(I-alpha h)^{-1}:B -> D` is also well defined and
holomorphic.

Thus the source question has an affirmative answer on the entire upward ray
`[alpha_0,infinity)`. The proof does not use balancedness or density of `D`,
weak closedness of `h`, or 0-dissipativity.

For `t=mu/alpha`, define

`K_x(z)=t x+(1-t)Phi_mu(z)`.

Its image lies strictly inside `B`, so the Earle-Hamilton theorem gives a
unique fixed point `Z_t(x)`, depending holomorphically on `x`. Then

`Phi_alpha(x)=Phi_mu(Z_t(x))`.

The proof also gives the convergent iteration

`z_(n+1)=t x+(1-t)Phi_mu(z_n)`.

## Scope

The interval `0<alpha<mu` remains open. In that direction the corresponding
resolvent identity requires an affine extrapolation with a negative
coefficient, which need not preserve the unit ball, so the fixed-point
argument genuinely stops at `mu`.

## Evidence and files

- `main.tex`: complete expert-facing proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:1311.6698.
- `figures/open_problem_crop.png`: full-width crop of the printed open
  question on source PDF page 13.
- `verification_report.md`: explicit proof and artifact audit.

## Literature status

A bounded search found no later paper explicitly answering the full question
or recording this exact upward-ray statement. Section 5.5 of M. Elin,
S. Reich, and D. Shoikhet, *Numerical Range of Holomorphic Mappings and
Applications* (Birkhauser, 2019), reproduces the question as open. Searches
also covered the exact question text, the source title and authors, nonlinear
resolvent identities, and later holomorphic-resolvent work through the March
2026 version of arXiv:2406.02758. Those later results assume a holomorphic
generator or an already existing full resolvent family. Novelty confidence is
moderate, not definitive: the proof is a short application of the classical
Earle-Hamilton theorem and may be folklore.

## Human review recommendation

Review as a likely valid substantial partial result. The two decisive checks
are (1) the strict-inside estimate for `K_x(B)` and (2) the uniqueness step,
where a competing solution `y` yields
`z=(mu/alpha)x+(1-mu/alpha)y in B` by convexity.
