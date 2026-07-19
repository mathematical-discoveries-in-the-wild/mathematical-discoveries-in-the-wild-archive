# Literature-Implied Partial Subcase: Pisier Analyticity Conjecture

Status: `literature_implied_answer (partial subcase)`

Source problem paper: C. Arhancet, *On a conjecture of Pisier on the
analyticity of semigroups*, arXiv:1403.6737.

Supporting paper: C. Arhancet, *On analyticity of semigroups on Bochner spaces
and on vector-valued noncommutative Lp-spaces*, arXiv:1807.00875.

## Target

The source paper records Pisier's conjecture that, for a K-convex Banach space
`X`, analyticity of a weak-star continuous semigroup `(T_t)` of selfadjoint
contractive operators on scalar `L^p` should be preserved by tensoring with
`Id_X` on the Bochner space `L^p(Omega, X)`.

The 2014 source paper itself proves only partial Fourier-multiplier cases. This
packet records a later, stronger literature-implied subcase from arXiv:1807.00875.

## Result

For every second-countable abelian locally compact group `G`, every
weak-star continuous semigroup `(T_t)` of selfadjoint contractive Fourier
multipliers on `L^\infty(G)`, every `1<p<infty`, and every `K'`-convex
Banach space `X`, the tensorized semigroup `(T_t \otimes Id_X)` is a strongly
continuous bounded analytic semigroup of contractions on `L^p(G,X)`.

Here `K'`-convex is the supporting paper's condition that `X` is isomorphic to
a Banach space carrying an OK-convex operator space structure. The supporting
paper notes that `K'`-convex spaces are K-convex and conjectures equality with
the K-convex class.

## Proof Summary

Arhancet arXiv:1807.00875, Corollary 14, states exactly the result above.
Definition 12 and the paragraph following it identify `K'`-convex spaces as
K-convex Banach spaces with the needed OK-convex operator-space realization.
Thus the corollary verifies Pisier's analyticity conclusion for this
Fourier-multiplier/locally-compact-abelian subcase. It is even stronger inside
that subcase because positivity and unitality are not assumed.

## Evidence

- `figures/open_problem_crop.png`: source-paper paragraph recording Pisier's
  conjecture.
- `figures/supporting_theorem_crop.png`: Definition 12 and Corollary 14 from
  arXiv:1807.00875.
- `source_paper.pdf`: local copy of arXiv:1403.6737.
- `supporting_paper_1807.00875.pdf`: local copy of arXiv:1807.00875.

## Search Bounds

Before packaging, the cheap run indexes were searched for `1403.6737`,
`1807.00875`, `Pisier`, `analyticity of semigroups`, `K-convex`,
`OK-convex`, `Fourier multipliers`, `Ritt`, and related semigroup terms. No
prior packet or attempt for this exact 1403.6737/1807.00875 subcase was found.
A nearby indexed packet for arXiv:1407.1142 concerns a different
positive/contractive UMD-Banach-lattice regularity cluster.

External arXiv/web search on 2026-06-14 found arXiv:1807.00875 as the relevant
later strengthening. No full solution of Pisier's general measure-space and
all-K-convex conjecture was identified during this bounded check.

## Human Review Notes

Recommended review focus:

- Confirm that the source conjecture is being restricted to Fourier-multiplier
  semigroups on `L^\infty(G)` for second-countable locally compact abelian
  `G`.
- Confirm that `K'`-convexity is strictly recorded as an extra hypothesis and
  not silently replaced by K-convexity.
- Count this only as a literature-implied partial subcase. The arbitrary
  measure-space case and the removal of the `K'`/OK-convex hypothesis remain
  open here.

