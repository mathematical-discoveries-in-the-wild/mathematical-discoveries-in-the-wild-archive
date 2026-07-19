# Conditional reduction: UMD case to symmetric de-Poissonization

Status: `conditional_reduction_likely_valid`.

Source problem: Ivan S. Yaroslavtsev, *Local characteristics and tangency of
vector-valued martingales*, arXiv:1907.11588, Remark 12.10.

Context from this lane:

- The broad Banach-space aggregate-domination statement is false in `c0`.
- Hilbert spaces are solved for all finite `p`.
- `L^q(S)` spaces are solved for all `1<q<infinity` and all `p>=1`.

Conditional result: fix a Banach space `X` and `1<=p<infinity`. Suppose `X`
has the symmetric `p` de-Poissonization property: for every finite independent
symmetric `X`-valued family `Z_i`, if `Pi_Z` is the compound-Poisson sum with
intensity `sum_i law(Z_i)|_{X\{0}}`, then

```text
||Pi_Z||_{L^p(X)} <= D_{p,X} ||sum_i Z_i||_{L^p(X)}.
```

Then the symmetric discrete aggregate-domination problem in Remark 12.10 holds
in `X` at exponent `p`. Consequently, by the standard symmetrization reduction
quoted in the source remark, this is the exact remaining route to the broad
UMD case.

Why this matters: aggregate domination is perfectly monotone after
Poissonization, because compound-Poisson sums superpose. The original family
is always controlled by its Poissonized version in the symmetric case. Thus the
only missing ingredient for arbitrary UMD spaces is the reverse comparison
from the Poissonized dominating family back to the original dominating family.

Interpretation: the `c0` counterexample is precisely a failure of this
de-Poissonization property. The Hilbert and `L^q` packets prove the property
through square-function/lattice structure. The open frontier is whether UMD
geometry alone implies it, or whether a UMD space without the property can be
constructed.

Files:

- `main.tex`: conditional reduction proof.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source paper arXiv:1907.11588.
- `figures/open_problem_crop.png`: crop of Remark 12.10.
- `figures/open_problem_continuation_crop.png`: crop of the discrete
  aggregate-domination formulation.

Human review recommendation: high priority as a routing packet. The main
thing to audit is Proposition 2.1, especially the universal lower
Poissonization step for symmetric families.
