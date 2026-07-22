# Counterexample packet: coordinate dependence of the implicit-function growth bound

Status: `candidate_counterexample_likely_valid`

Source: Thomas Berger and Frédéric Haller, *On an extension of a global
implicit function theorem*, arXiv:2004.04427; *Comptes Rendus Mathématique*
360 (2022), 439-450, DOI 10.5802/crmath.309.

## Result

Remark 2.3 of the source asks whether the growth bound in Theorem 2.1(iii) is
independent of the diffeomorphisms used to identify the two zero-set
projections with Banach spaces. The packet gives a negative answer, already
for

`F(x,y)=x-y` on `R x R`.

With the identity coordinates, the growth expression is identically `1` and
the constant weight `omega=1` is admissible. The packet constructs an explicit
smooth diffeomorphism `h:R->R` such that replacing the output coordinate by
`h` makes the growth expression admit no continuous nondecreasing Osgood
weight majorant.

## Construction

Choose a smooth bump `beta` supported in `(-1/4,1/4)` with `beta(0)=1` and set

`H(t)=1+sum_{n>=1} 4^n beta(4^n(t-n))`.

The bumps have summable total width, so `integral_0^infinity 1/H = infinity`.
Hence

`Q(t)=integral_0^t 1/H(s) ds`

is a global smooth diffeomorphism, and `h=Q^{-1}` satisfies
`h'(y)=H(h(y))`. But `H(n)>=4^n`. Any nondecreasing majorant must remain at
least `4^n` throughout `[n,n+1]`, making its reciprocal integrable. It cannot
be a weight in the source's sense.

## Packet contents

- `main.tex`: self-contained counterexample with proof intuition, formal
  verification, scope, and novelty bounds.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_problem_crop.png`: source PDF page-7 crop containing Remark
  2.3 in full.
- `tmp/`: LaTeX intermediates and rendered-page QA images.

No computation is used in the proof.

## Verification focus

1. Check that the bump supports have finite total measure and the infinite
   series is locally finite.
2. Check that the reciprocal-speed integral diverges, making `Q` onto all of
   `R`.
3. Check the inverse derivative `h'=H composed with h` and its substitution
   into Theorem 2.1(iii).
4. Check the use of monotonicity in ruling out every admissible weight.

Current verdict: full counterexample likely valid. Human review is recommended,
particularly for the quantifier match with Remark 2.3.

## Novelty check

The cheap run indexes contained no overlap. A bounded web/arXiv search on
2026-07-21 used the arXiv id, title, authors, DOI, exact open-question wording,
and coordinate-independence/counterexample variants. It found the source and
papers merely citing it, but no later settlement. The current arXiv text dated
March 2026 still labels the question open. This supports, but does not prove,
novelty.
