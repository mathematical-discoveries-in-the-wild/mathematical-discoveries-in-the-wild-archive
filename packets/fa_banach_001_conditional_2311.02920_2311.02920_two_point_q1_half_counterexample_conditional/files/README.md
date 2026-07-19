# Conditional half-exponent two-point counterexample

Status: `conditional`; would give a counterexample to Question 3 in Cuth-Raunig
if the scalar tripod inequality stated in the packet is verified.

Source paper: Marek Cuth and Tomas Raunig, *Canonical embedding of
Lipschitz-free p-spaces*, arXiv:2311.02920.

## Conditional claim

Question 3 asks whether \(\mathrm{aa}_{p}^{1}(2)>1\) for every
\(p\in(0,1)\).  The packet proves that, assuming one explicit scalar
inequality for Euclidean tripods, every two-leaf metric tripod is
isometrically \(1/2\)-amenable.  By the source paper's tree reduction this
would imply
\[
\mathrm{aa}_{1/2}^{1}(2)=1,
\]
and therefore a negative answer to Question 3.

## Files

- `main.tex` / `solution_packet.pdf`: conditional proof packet.
- `source_paper.pdf`: original source paper.
- `figures/open_problem_crop.png`: source crop containing Questions 1-3.
- `code/check_half_tripod_certificate.py`: deterministic numerical checks for
  the scalar certificate and the normalized Euclidean form.

## Remaining dependency

The only unproved dependency is Scalar Lemma E in `main.tex`.  Numerics strongly
support it, and the packet reduces it to a two-variable Euclidean inequality,
but it has not been converted into a clean analytic proof in this loop.

## Novelty check

Local run indexes contained no packet for arXiv:2311.02920 or for
\(\mathrm{aa}_{p}^{1}(2)\).  Web searches for exact phrases including
`aa_p^1(2)`, `absamen_p^1(2)`, `p-amenability Lipschitz-free aa_p(2)`, and the
paper title found the source paper and the later broad embedding paper
arXiv:2603.28193, but no literature answer to the sharp two-point
\(q=1\) constant question.

## Human review recommendation

Focus review on Scalar Lemma E.  If it is proved, this packet should be promoted
to `solutions/counterexamples/` as a counterexample to Question 3.  If the
inequality fails, the coefficient certificate still gives a precise obstruction
map for the next search.
