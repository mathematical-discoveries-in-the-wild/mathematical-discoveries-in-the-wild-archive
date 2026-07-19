# Verification Report

Status: passed internal adversarial audit; independent human review requested.

## Claim audited

For arbitrary von Neumann algebras `M,N`, the class of tensors whose left
slice map `M_* -> N` is weakly compact is a bimodule over
`M tensor_min N`.  The Hopf consequence says that `WAP(M_*)` is a bimodule
over `A_Gamma = Gamma^{-1}(M tensor_min M)`.

## Checks

1. **Predual maps are legitimate.**  For `a in M`, left and right
   multiplication on `M` are normal bounded maps.  Therefore
   `f -> f o L_a` and `f -> f o R_a` map `M_*` boundedly into itself.

2. **Slice orientations are correct.**  On an algebraic tensor
   `u=sum m_j tensor n_j`,
   `T_{u(a tensor b)}(f)=sum f(m_j a)n_j b`
   equals `R_b T_u(f o R_a)`, while
   `T_{(a tensor b)u}(f)=sum f(a m_j)b n_j`
   equals `L_b T_u(f o L_a)`.  Normality extends the identities to every
   `u in M bar-tensor N`.

3. **Weak compactness survives.**  Weakly compact bounded operators form an
   operator ideal, so bounded pre- and post-composition preserve weak
   compactness.  They also form a norm-closed subspace: if `T_k -> T` in
   operator norm, then `T_k** -> T**`; the standard bidual criterion and the
   norm-closed canonical copy of `N` in `N**` give `T**(M^*) subset N`.

4. **The tensor approximation uses the right norm.**  The spatial minimal
   tensor product is the operator-norm closure of `M tensor N` in the same
   faithful spatial representation used for `M bar-tensor N`.  Thus, if
   `z_k -> z` in `M tensor_min N`, then `u z_k -> u z` and
   `z_k u -> z u` in operator norm.  Since
   `||T_v|| <= ||v||`, the corresponding slice maps converge in operator norm.

5. **Hopf transfer is exact.**  `Gamma` is a unital *-homomorphism, so
   `Gamma(xy)=Gamma(x)Gamma(y)` and similarly for `yx`.  Its inverse image of
   the norm-closed C*-subalgebra `M tensor_min M` is a unital C*-subalgebra.
   Proposition 3.2 of the source identifies weak compactness of the slice map
   of `Gamma(x)` with `x in WAP(M_*)`.

## Failure modes checked

- No injectivity or approximation property is used in the proof.
- The theorem does not assert that `A_Gamma = CAP(M_*)` for noninjective `M`.
- The plus sign in the displayed bimodule inclusion denotes the sum of the
  two contained subspaces; each left and right product is proved separately.
- The generic non-algebra example for weak-slice tensors in Daws
  (arXiv:1409.7302) is compatible with this theorem because both factors there
  need not lie in the minimal tensor product.

## Remaining scope

The original question remains open at the step where both factors are only
known to be WAP.  No claim of a full solution or counterexample is made.

## Recommended human focus

Compare the two elementary slice identities directly against the conventions
in source equation (1), then verify that the source's injectivity assumption
enters Corollary 2.3 only through its use of Theorem 2.1.  If both checks agree,
the partial theorem is ready to cite as a hypothesis removal.

