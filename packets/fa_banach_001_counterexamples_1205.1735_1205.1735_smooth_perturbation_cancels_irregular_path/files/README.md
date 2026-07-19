# Counterexample packet: a smooth perturbation can cancel an irregular path

Status: candidate full counterexample, likely valid

## Source problem

Rémi Catellier and Massimiliano Gubinelli, *Averaging along irregular curves
and regularisation of ODEs*, arXiv:1205.1735, PDF page 6. The paper conjectures
that if `w` is `(rho,gamma)`-irregular, then `w+phi` remains
`(rho,gamma)`-irregular for every smooth `phi`.

## Counterexample

Work on `[0,1]` in dimension one. For any `0<rho<1/2`, put

`gamma=1-rho`, `w(t)=t`, and `phi(t)=-t`.

For `h=t-s`,

`|integral_s^t exp(i xi r) dr| <= min(h,2/|xi|)`.

Interpolation between the two bounds shows that the defining
`(rho,gamma)`-irregularity norm of `w` is finite. Indeed it is at most
`4^rho`. But `phi` is smooth and `w+phi` is the constant zero path. Its
occupation Fourier increment equals `h` for every frequency, so its defining
norm diverges as `|xi|` tends to infinity.

Thus the conjecture is false as literally stated.

## Scope

This counterexample uses `rho<1/2`. It does not refute stronger stability
statements for highly irregular or strongly irregular paths. Galeati and
Gubinelli, arXiv:2004.00872v2, treat the smooth-additive claim as open in
general, assume `rho>1/2` in their additive-perturbation section, and prove a
positive theorem after strengthening the hypothesis to strong
`rho`-irregularity.

## Files

- `solution_packet.pdf`: review-ready proof and scope analysis.
- `main.tex`: packet source.
- `source_paper.pdf`: original arXiv paper.
- `supporting_paper_2004.00872.pdf`: later primary literature checked.
- `figures/open_problem_crop.png`: exact conjecture from source PDF page 6.
- `tmp/`: build and rendering intermediates.

## Human review focus

Check that the source quantifier really is meant literally for all positive
`rho`, with no tacit requirement `rho>1/2` and no independence restriction on
the deterministic smooth perturbation. Under the printed definition and
conjecture, the counterexample is elementary and complete.
