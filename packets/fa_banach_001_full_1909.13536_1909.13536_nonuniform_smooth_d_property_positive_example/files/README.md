# Full Result: A Non-Uniformly Smooth Example With Property `D(s,c_1)`

Status: `full`

Source paper: S. Dilworth, G. Garrigos, E. Hernandez, D. Kutzarova, and V. Temlyakov, *Lebesgue-type inequalities in greedy approximation*, arXiv:1909.13536.

## Answered Question

Remark 2.11 asks whether property `D(s,c_1)` can hold for some non-uniformly smooth Banach space and some dictionary.

This packet gives a positive answer.

## Construction

For `0 < eps < 1/2`, put on `R^2`

```tex
N_eps(x,y) = (x^2+y^2)^{1/2} + eps |x+y|.
```

This norm is not Gateaux differentiable on the nonzero line `x+y=0`, hence it is not uniformly smooth. Let `E_eps=(R^2,N_eps)` and let `H=ell_2`. On

```tex
X = E_eps \oplus_2 H
```

take the dictionary consisting of the two normalized coordinate atoms in `E_eps` and the canonical Hilbert basis in `H`.

## Result

There is a constant `c>0` such that `(X,D)` has property `D(2,c)`. Thus property `D(s,c_1)` can indeed hold in an infinite-dimensional non-uniformly smooth Banach space.

## History: Obstruction Route

The first push produced an obstruction: no nontrivial `ell_1` direct sum `E \oplus_1 F` can satisfy property `D(s,c)` for any nonempty dictionary. That route is now included inside this full packet as historical context and as a warning against the most tempting nonsmooth-corner construction.

Archived historical packet:
`history/1909.13536_l1_sum_D_property_obstruction/`

The full positive example shows that the obstruction is specific to `ell_1`-sum corners, not to all nonsmooth norms.

## Verification Notes

- The proof is analytic. The only compactness step is a one-variable quotient for the finite-dimensional block.
- The historical `ell_1`-sum obstruction is included in the packet PDF, but the live registry result is this full positive answer.
- `code/sample_block_ratio.py` numerically samples the finite block for `eps=1/4`; it is a sanity check, not a proof.
- Source-question crop: `figures/open_problem_crop.png`.
- Bounded novelty check: local run indexes and web search were checked for `1909.13536`, `Remark 2.11`, `D(s,c_1)`, `property D`, and `non-uniformly smooth`; no exact later answer was found.

## Human Review Recommendation

Review the one-variable lemma in the finite block and the `ell_2`-sum stability step. If those pass, the packet gives a literal positive answer to Remark 2.11.
