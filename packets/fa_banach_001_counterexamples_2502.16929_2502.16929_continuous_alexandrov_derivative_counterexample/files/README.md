# Continuous perturbations need not have a two-sided functional Alexandrov derivative

Status: `candidate full counterexample, likely valid pending expert review`

Source: Tomer Falah and Liran Rotem, *On the functional Minkowski problem*,
arXiv:2502.16929.  The target passage is in Section 2, equation (2.1), PDF
page 9.

## Result

The literal extension of equation (2.1) to every continuous perturbation
`xi:R^n -> R` is false, even in dimension one and even when the perturbation
has at most linear growth and the perturbed dual potentials remain coercive
for all sufficiently small positive and negative parameters.

Let `phi` be zero on `[-1,1]` and `+infinity` outside, so `phi*(y)=|y|`, and
set

`xi(y)=|y| sin(log(1+|y|))`.

For `|t|<1`, the conjugate of `phi*+t xi` is zero on
`[-(1-|t|),1-|t|]` and `+infinity` outside.  Consequently,

`integral_R exp(-(phi*+t xi)*) = 2(1-|t|)`.

The right derivative at zero is `-2` and the left derivative is `+2`.

## Scope

This is a full negative answer only to the paper's unrestricted phrase
“for all continuous functions.”  It does not contradict Proposition 2.1 for
bounded continuous perturbations, Theorem 2.3 for support functions, or the
paper's completed functional Minkowski theorem.  It shows that a viable
general Alexandrov lemma must impose asymptotic/recession regularity in
addition to continuity.

## Files

- `solution_packet.pdf`: rendered counterexample packet.
- `main.tex`: self-contained proof source.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source passage on PDF page 9.
- `verification_report.md`: line-by-line proof audit.
- `tmp/`: LaTeX and PDF-rendering intermediates.

## Novelty check

The run's lightweight indexes were searched for the arXiv id, functional
Minkowski problem, functional Alexandrov lemma, continuous perturbations, and
Legendre-transform derivative variants; no duplicate was found.  Bounded web
searches on July 23, 2026 used the exact title and author names together with
“functional Alexandrov lemma,” “all continuous functions,” “two-sided
derivative,” and close Legendre-perturbation variants.  They found the source
and background functional-convexity papers, but no later answer or matching
counterexample.  Novelty confidence is moderate pending specialist review.

## Human review focus

Check the exact domain computation of the conjugate.  The decisive point is
that the oscillating coefficient attains its lower asymptotic value
`1-|t|` along an unbounded sequence for each sign of `t`.
