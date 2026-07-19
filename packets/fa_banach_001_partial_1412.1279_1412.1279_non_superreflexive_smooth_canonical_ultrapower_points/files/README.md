# arXiv:1412.1279 - non-superreflexive space with smooth canonical ultrapower points

Status: `partial_result_likely_valid`

Source paper:

- Jarno Talponen, "Uniform-to-proper duality of geometric properties of Banach spaces and their ultrapowers", arXiv:1412.1279.
- On PDF page 4, after Theorem 2.5, the paper says it is not known what geometric properties are implied by the Frechet smoothness of `j(x)` for all `x in S_X`.

Partial result:

The ultrapower-smooth canonical-sphere property does not force superreflexivity.

Let `p_n=max(2, log n)` for `n>=2` and `p_1=2`, and set

`X = (direct sum_n ell_{p_n}^n)_2`.

Then:

- `X` is reflexive, as an `ell_2`-sum of finite-dimensional spaces.
- `X` is not superreflexive, since the coordinate summands are uniformly isomorphic to `ell_infty^n`.
- The norm of `X` is Frechet smooth away from zero.
- For every free ultrafilter `U` on `N`, the weak-ultralimit projection gives an isometric splitting
  `X^U = j(X) direct-sum_2 ker(P)`.
- Therefore every canonical point `j(x)`, `x in S_X`, is Frechet smooth in `X^U`.

Scope:

This does not classify the property from the source paper. It rules out the natural possible implication "all canonical ultrapower points Frechet smooth => superreflexive". The construction is still reflexive, so whether the property forces reflexivity is not addressed here.

Files:

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_problem_crop.png`: crop of the source paragraph.
- Ledger: `runs/fa_banach_001/ledger/results/1412.1279_non_superreflexive_smooth_canonical_ultrapower_points.json`.
