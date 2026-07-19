# Literature-Implied Partial Subcase: Stochastic Weiss Under Property (alpha)

Status: `literature_implied_answer (partial subcase / reformulated resolvent condition)`

Source problem paper: B. H. Haak and J. van Neerven,
*Uniformly gamma-radonifying families of operators and the stochastic Weiss
conjecture*, arXiv:math/0611724.

Supporting paper: J. Abreu, B. Haak, and J. van Neerven,
*The stochastic Weiss conjecture for bounded analytic semigroups*,
arXiv:1206.3656.

## Target

In the final section of arXiv:math/0611724, Haak--van Neerven formulate the
stochastic Weiss conjecture. Under finite cotype, injectivity, sectoriality of
angle `< pi/2`, and bounded `H^infty` calculus for `-A`, they ask for
equivalence of:

- existence of an invariant measure for the stochastic Cauchy problem;
- `(-A)^(-1/2) B` being gamma-radonifying;
- uniform gamma-radonification of the sector resolvent family
  `{ sqrt(lambda) R(lambda,A) B }`.

The source paper proves the necessary implication from invariant measure to
the uniform gamma-radonifying family, and notes the remaining hard implication.

## Supporting Literature Result

Abreu--Haak--van Neerven prove the central equivalence for Banach spaces with
Pisier property `(alpha)` and bounded `H^infty` calculus of angle `< pi/2`.
Their Theorem 1.1 states that, for such spaces, invariant measure,
`(-A)^(-1/2)B in gamma(H,E)`, a gamma-`L^2(dlambda/lambda)` resolvent condition,
and an equivalent dyadic Gaussian resolvent condition are all equivalent.

The supporting authors explicitly identify this as solving the stochastic
Weiss conjecture proposed by Haak--van Neerven. The identification is scoped
here as a partial subcase/reformulation because the 2006 displayed conjecture
uses finite cotype and a uniform gamma-radonifying sector-family condition,
whereas the 2012 theorem assumes property `(alpha)` and uses the dyadic/Gaussian
resolvent formulation.

## Scope

This packet records the following literature-implied subcase:

If `E` has property `(alpha)`, `-A` is injective, sectorial of angle `< pi/2`,
has dense range, and admits a bounded `H^infty` calculus of angle `< pi/2`,
then the existence of an invariant measure for the stochastic Cauchy problem
is equivalent to `(-A)^(-1/2)B in gamma(H,E)`.

This covers Hilbert spaces and, by Pisier's theorem quoted in the supporting
paper, Banach lattices of finite cotype. It does not claim a full answer for
all finite-cotype Banach spaces in the exact 2006 uniform-family formulation.

## Evidence

- `source_paper.pdf`: local copy of arXiv:math/0611724.
- `supporting_paper_1206.3656.pdf`: local copy of arXiv:1206.3656.
- `main.tex` and `solution_packet.pdf`: compact status note with the exact
  theorem-to-question identification and limitations.

## Search Bounds

Before packaging, the cheap run indexes were searched for `0611724`,
`gamma-radonifying`, `stochastic Weiss`, `Weiss conjecture`, `admissibility`,
and `analytic semigroup`; no prior packet or attempt for this target was found.
Local source comparison identified arXiv:1206.3656. Web/arXiv searches on
2026-06-15 for `"stochastic Weiss conjecture" "finite cotype" "property
(alpha)"`, `"stochastic Weiss conjecture" "gamma-radonifying" "finite cotype"`,
and `site:arxiv.org/abs "stochastic Weiss conjecture"` found the same two
primary arXiv sources and no later broader finite-cotype resolution.

## Human Review Notes

Recommended review focus:

- Confirm that the packet is counted only as a literature-implied partial
  subcase/reformulation, not as a full answer to the exact 2006 finite-cotype
  uniform-family conjecture.
- Check whether a later paper after arXiv:1206.3656 removes property `(alpha)`
  or proves the exact uniform gamma-radonifying implication in full finite
  cotype generality.
- Check the theorem-number mapping in the published version of arXiv:1206.3656.

