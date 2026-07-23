# Counterexample packet: no unrestricted Mahler product for polar-volume valuations

Status: candidate counterexample likely valid. This is a complete negative
answer to the unrestricted two-sided product interpretation of the source
question for the nonnegative valuation-class weights classified in the source.
It is not a claim that every normalized or restricted variant is impossible.

Source paper: Fabian Mussnig, “SL(n) Invariant Valuations on Super-Coercive
Convex Functions,” arXiv:1903.04225, Canadian Journal of Mathematics 73
(2021), 108–130.

Targeted question: the unnumbered remark following Theorem 1.3* on PDF page 4
asks whether inequalities analogous to the functional
Bourgain–Milman/Blaschke–Santaló bounds can be obtained from

`A_zeta(u) = integral zeta(grad u*(y) dot y - u*(y)) dy`

and/or

`B_zeta(u) = integral zeta(grad u(x) dot x - u(x)) dx`.

Result: let `n >= 2`, and let `zeta, eta : R -> [0,infinity)` be continuous
and vanish on upper half-lines, exactly as the source’s polar-volume
valuation weights do. On the full space of finite super-coercive convex
functions,

`inf_u A_zeta(u) B_eta(u) = 0`.

Indeed, for `u_c(x)=|x|^2/2+c`, the first factor is exactly zero once `c` is
above the support threshold of `zeta`. Thus no positive lower product bound,
and hence no two-sided Mahler/Santaló analogue, can hold on the unrestricted
class for any such weights.

There is a complementary upper obstruction. If each weight is nonzero at a
positive argument, then even on the normalized class of even, radial, finite,
strictly convex, `C^1`, super-coercive functions satisfying
`u(0)=min u=0`,

`sup_u A_zeta(u) B_eta(u) = infinity`.

The witnesses are `u_p(x)=|x|^p/p` as `p` decreases to `1`. The proof gives
closed formulas for both factors.

Files:

- `main.tex`: complete proof and scope analysis.
- `solution_packet.pdf`: rendered proof packet.
- `verifier_report.md`: independent logical, computational, source, and
  scope audit.
- `source_paper.pdf`: local copy of arXiv:1903.04225.
- `figures/open_problem_crop.png`: source-page crop containing Theorem 1.3*
  and the full open-question remark.
- `code/make_open_problem_crop.py`: reproduces the source crop from the
  rendered fourth page.
- `code/verify_radial_families.py`: checks the radial integral formulas and
  illustrates divergence for a sample weight; it is not used as proof.

Novelty check: the run’s registry, solutions, attempts, and proof-gap indexes
were searched for the arXiv id, title, “polar volume valuation,” “Mahler
product,” and the displayed integrands. Bounded arXiv/web searches on
2026-07-23 used the exact source question, the integrands, “Hessian valuation
volume product,” and related author/title terms. They found the source paper,
the adjacent arXiv:1806.11084, and the later arXiv:2412.05001 on different
Brunn–Minkowski and isoperimetric questions for functional intrinsic volumes.
Inspection of the latter’s full text found neither “polar volume” nor the
target arXiv id. No direct answer to this exact product question was found.

Human-review focus: verify that the intended reading of “similar inequality”
is a positive-lower/finite-upper product inequality for the two displayed
Legendre-dual quantities. The mathematical calculation is elementary; the
important judgment is scope. The packet does not rule out a one-sided bound,
a different combination of the quantities, weights outside the
upper-supported valuation class, or a narrower normalization designed to
exclude both witness families.
