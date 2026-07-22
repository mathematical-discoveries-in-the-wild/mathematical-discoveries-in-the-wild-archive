# Verification notes

- The open question was checked in the source PDF on page 18, immediately
  after Theorem 5.3; the rendered crop is in `figures/open_problem_crop.png`.
- The endpoint estimate used in the proof was checked in the alternative
  complete-boundedness proof in Section 8: grouping the first factor against
  the complementary tensor product gives
  `C(e_beta T_1) <= C(tensor_k T_k)` when `beta` is the growth bound of the
  complement and is finite.
- Sign check: the complementary normalized semigroup is `e_{-beta}S`, so the
  two group-level shifts are `beta` and `-beta`.  Expanding the complement
  yields shifts `d_k=-omega_0(T_k)` for `k>=2` and
  `d_1=sum_{k>=2}omega_0(T_k)`, whose sum is zero.
- The original contractivity hypothesis was strengthened to the exact bound
  `C(e_{-beta_k}T_k) <= C(product)`.  The proof needs only this inequality;
  it never uses that the endpoint constant equals one.
- If `T_k(t)` is normal, then its norm equals its spectral radius.  Hence
  `||e^{-omega_0(T_k)t}T_k(t)||=1`, which verifies the normal-semigroup
  corollary.
- Matrix endpoint check: compressing `I <= P <= C^2 I` to the invariant slice
  `H_A tensor span(v)` preserves both order bounds.  If `Bv=lambda v`, the two
  `B` terms compress to `2 Re(lambda) P_v`, proving the displayed matrix
  theorem without a numerical assumption.
- Convex Lyapunov feasibility bisection tested more than 2,300 random real
  matrix pairs in factor dimensions 2, 3, and 4, plus structured Jordan
  families, over multiple values of `C`.  Every strictly active gap was
  positive.  Apparent negative gaps occurred only at the spectral boundary
  and disappeared under refinement or were ruled out by the endpoint theorem.
  This evidence is explicitly non-probative and is not used in either proof.
- The PDF was compiled with all build intermediates under `tmp/`, and every
  rendered page was visually inspected.
