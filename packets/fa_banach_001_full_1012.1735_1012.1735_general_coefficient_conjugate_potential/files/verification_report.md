# Verification report

Result: general-coefficient existence of the vector-valued potential asked for after Proposition 3.5 of arXiv:1012.1735.

Status: proof internally verified; independent expert verification still required by the run protocol.

## Audit

1. **Source match:** The source asks whether the converse of Proposition 3.5 holds for general coefficients. The theorem constructs exactly a `v` in `L2_loc(R_+; dom D)`, with the required `BD` equation, exact normal component, and the stated integral bound on `Dv`.
2. **Scaling:** With `sigma=(n-1)/2`, the conormal identities give `f_parallel = grad_S(r^sigma u_r)` and `(Bf)_perp=r^(sigma+1) partial_r u_r`. Hence the normal `v` equation has the claimed signs.
3. **Initial slice:** Because `f_t` lies in `ran D` almost everywhere, `f_perp(t_*)` lies in `ran div_S`; a tangential `w_*` with `-div_S w_*=f_perp(t_*)` exists.
4. **Evolution:** The Bochner formula for `w` is well-defined from local `L2` integrability of `Bf` and solves the tangential equation in `L2`.
5. **Constraint propagation:** The normal component of the conormal equation is exactly the variation-of-constants formula obtained by applying `-div_S` to `w`. This proves `-div_S w=f_perp` in `W^{-1,2}`, and therefore in `L2` almost everywhere.
6. **Graph domain:** The preceding identity and `grad_S U=f_parallel` put `v_t` in `dom D` almost everywhere. Local graph-norm integrability follows from the construction and `f in L2_loc`.
7. **Global condition:** `Dv=f`; the required integral from `1` to infinity is Corollary 3.4 of the source paper.
8. **Hidden assumptions checked:** The proof uses neither pointwise ellipticity nor a Carleson discrepancy estimate. It uses only the coefficient hypotheses already needed to form `B` and obtain the conormal system.

## Main reviewer focus

Confirm that the phrase “such `v`” in the source refers exactly to the explicit hypotheses of Proposition 3.5 and does not tacitly demand the later perturbative uniform-in-time estimates. Under the literal proposition-level formulation, the proof closes.

