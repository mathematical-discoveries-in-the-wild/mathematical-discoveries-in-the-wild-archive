# Verification report

Verdict: `candidate_full_solution_likely_valid`, pending expert review.

## Exact scope

The packet proves that every Donoho--Stark minimizer in every canonical
finite-dimensional fusion bialgebra is a bishift of a biprojection. The
statement is invariant under product-one gauges, precisely the gauges that
preserve the sharp constant-one uncertainty inequality. No dual Young or
dual Schur property is used.

## Proof audit

1. **Equality normalization.** The source's equality theorem identifies a
   minimizer with an extremal bi-partial isometry. In the abelian algebra
   `A`, normalization therefore gives unit phases on the minimal support
   projections. Extremality gives `||F(w)||_infty=||w||_1=D`, while
   Plancherel gives trace `1/D` for both partial-isometry support projections.

2. **Saturated triangle.** For every unit vector in the initial projection,
   both inequalities

   ```text
   ||sum eps_j d_j x_j xi|| <= sum d_j ||x_j xi||
                              <= sum d_j^2
   ```

   are equalities. Because the fusion coefficients used later are
   nonnegative, equality forces each constituent to attain its norm and have
   the common phase. This is valid for arbitrary noncommutative `B`.

3. **Stabilizer closure.** Both `x_s Q=d_s alpha_s Q` and
   `x_s* Q=d_s conjugate(alpha_s) Q` are imposed. Applying the saturation
   lemma to a product and separately to its adjoint proves star and fusion
   closure without commuting basis elements.

4. **Exact stabilizer support.** Products `x_j x_k*` are supported in the
   stabilizer `H`. Conversely, coefficient extraction from
   `F(w)F(w)*=D^2 Q` shows every member of `H` occurs with nonzero coefficient.
   The phased regular element squares both to `D_H` times itself (fusion
   calculation) and to `D` times itself (projection calculation), so
   `D_H=D`.

5. **Coset closure.** Saturation applied to `x_s x_j` and its adjoint puts
   every constituent back in `J`. Conversely, the two cross-relations give
   Fourier coefficient `d_r eps_r`, so no extra basis index can satisfy them.

6. **Right shift.** Frobenius reciprocity
   `N_{s,j}^r=N_{s*,r}^j` and `H*J subset J` give coefficient `D d_r` on
   `J` and zero outside. Therefore `B_H*P_J=D P_J` and the trace weights agree.

7. **Dual shift.** The source convention is
   `X *_B Y=(F(F^{-1}(Y*) diamond F^{-1}(X*))) *`. With `X=Q` and `Y=R_H`,
   coordinatewise multiplication gives `(1/D)F^{-1}(Q)` before applying
   `F` and the final adjoint. Hence `Q *_B R_H=(1/D)Q=tau(R_H)Q`.

8. **Bishift identity.** `P_J` supports `w` and `Q` supports `F(w)`, so
   `F^{-1}(Q)*(w diamond P_J)=w` exactly.

## Computational sanity checks

Run from the repository root:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/1910.12059_donoho_stark_minimizers_are_bishifts/code/verify_stabilizer_group_cases.py

conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/1910.12059_donoho_stark_minimizers_are_bishifts/code/verify_rank_three_identities.py
```

The first script checks the partial-isometry, phased stabilizer, coset, and
right-shift identities for multiple subgroups, cosets, and one-dimensional
characters in `S_3` and `D_4`; these include noncommutative group algebras.
The second retains the exact symbolic checks from the earlier independent
rank-three classification proof. Neither script replaces the general proof.

## Source and novelty evidence

- `source_paper.pdf` is present.
- `figures/open_problem_crop.png` is a real render of source PDF page 22 and
  shows the entire Question 6.15 plus Theorem 6.16.
- Cheap indexes and bounded arXiv searches on 2026-07-22 found no separate
  later answer to the exact question.

## Human reviewer focus

The most consequential checks are the equality case in the saturated
triangle lemma, the adjoint order in the noncommutative products, the
`D_H=D` coefficient computation, and the final dual convolution convention.

