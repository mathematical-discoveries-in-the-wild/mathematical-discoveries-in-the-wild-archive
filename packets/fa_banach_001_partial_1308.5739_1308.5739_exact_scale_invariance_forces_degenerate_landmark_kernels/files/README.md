# Scale, completeness, and full two-landmark geometry

Status: strong_partial_result_likely_valid; exact scale covariance, all-N
directional-Osgood adaptive completeness, universal matrix two-landmark
completeness, the exact arbitrary-matrix normalized-shape criterion, the
exact scalar and matrix-TRI monotone-gap criteria and power-exponential phase
diagrams, and the full scalar two-landmark ambient geometry are complete in
the stated classes.

Source: Mario Micheli and Joan Alexis Glaunès, *Matrix-valued Kernels for
Shape Deformation Analysis*, arXiv:1308.5739.

## Main results

1. Exact covariance classification. A positive-definite landmark cometric has
   exactly dilation-covariant geodesic flow if and only if

       G(lambda q) = lambda^alpha G(q).

   The induced metric scales by lambda^(2-alpha), and alpha=2 makes dilation
   an isometry.

2. Fixed and global-scale kernels. A fixed stationary kernel can satisfy this
   law only by being constant and multi-landmark degenerate. Nondegenerate
   global-scale Hamiltonians are classified exactly by

       kappa_s(x) = s^alpha phi(x/s),    b(s) = beta s^alpha.

3. Sharp radial completeness. A homogeneous cometric with alpha<2 has finite
   distance to total collapse; with alpha>2 it has finite distance to spatial
   infinity. Completeness therefore forces alpha=2.

4. Complete adaptive metrics for every admissible profile. Let Phi be a
   strictly positive-definite matrix profile satisfying

       0 <= 2 Phi(0)-Phi(z)-Phi(-z) <= L^2 |z|^2 I.

   This condition follows whenever the stationary RKHS of Phi embeds
   continuously in bounded C1 vector fields. For

       rho(q)^2 = N^(-1) sum_a |q^a-qbar|^2,
       G_alpha(q)_ab
         = rho(q)^alpha Phi((q^a-q^b)/rho(q)),

   the metric is geodesically complete for every N,d exactly when alpha=2.
   The proof gives logarithmic barriers for scale escape and every pair
   collision.

5. Osgood-modulus completeness. The quadratic feature estimate can be
   replaced by

       0 <= 2 Phi(0)-Phi(z)-Phi(-z) <= omega(|z|)^2 I,
       integral_0^1 dt/omega(t) = infinity.

   The Osgood integral prevents every pair collision, while the scale and
   Euclidean-escape bounds are unchanged. Thus the adaptive metric is
   complete for every N exactly at alpha=2 under this strictly broader
   modulus hypothesis.

6. Directional Osgood and universal matrix N=2 completeness. For a pair
   separation z=t e, it is enough to bound only

       e^T[2 Phi(0)-Phi(t e)-Phi(-t e)]e <= omega(t)^2.

   Thus transverse feature roughness does not by itself cause a collision.
   Moreover, for every continuous strict stationary matrix profile, the
   entire N=2 adaptive metric at alpha=2 is uniformly equivalent to

       (|dc|^2+dr^2)/r^2 + |de|^2,

   and is therefore complete. No radial or scalar assumption is needed for
   this two-landmark theorem.

7. Exact scalar completeness criterion. For a scalar radial profile, put

       delta(r)=phi(0)-phi(r),

   and assume delta is nondecreasing near zero. For N=2, alpha=2 is always
   complete, regardless of the small-scale gap. For every N>=3, the adaptive
   metric is complete exactly when

       alpha=2 and integral_0 dr/sqrt(delta(r)) = infinity.

   When the integral is finite, monotonicity forces
   delta(r)/r^2 to tend to infinity. A symmetric binary collision then has
   Schur complement asymptotic to delta(2 epsilon/rho), and finite length.
   This is an exact criterion, not only a sufficient regularity condition.

8. Exact scalar rough-kernel phase diagram. For the strict power-exponential
   profiles

       Phi_beta(z)=exp(-|z|^beta) I,    0<beta<=2,

   the adaptive metric is complete precisely as follows:

       N=2:   alpha=2, every 0<beta<=2;
       N>=3:  alpha=2 and beta=2.

   For N>=3 and beta<2, a symmetric binary collision has Gram Schur
   complement S(epsilon) asymptotic to C epsilon^beta, so its metric speed
   is asymptotic to C epsilon^(-beta/2) and the collision has finite length.

9. Exact matrix-TRI completeness criterion. Write

       Phi(r e)=k_parallel(r) P_e+k_perp(r) P_e^perp,
       Phi(0)=a I,   delta_parallel(r)=a-k_parallel(r).

   If delta_parallel is nondecreasing near zero, then for every N>=3 the
   adaptive metric is complete exactly when

       alpha=2 and
       integral_0 dr/sqrt(delta_parallel(r)) = infinity.

   Collinear configurations decouple the full Gram matrix into longitudinal
   and transverse sectors, giving a matching finite-length Schur collision
   whenever the integral is finite. The tangential gap does not enter.

10. Genuinely matrix-valued phase diagram. For eta>0,

       Phi_{beta,eta}(z)
         = exp(-|z|^beta) I + eta[-D^2 exp(-|z|^2)]

   is a strict non-scalar TRI kernel. It is complete at alpha=2 for every
   beta in the two-landmark case, while for N>=3 it is complete exactly when
   beta=2.

11. Exact arbitrary-matrix completeness criterion. Let

       Sigma_N = {
         x : sum_a x^a=0,
             N^(-1) sum_a |x^a|^2=1,
             x^a != x^b
       },

    put `K(x)_ab=Phi(x^a-x^b)`, `A=K^(-1)`, and define

       h_x(v,v)
         = min_{u,lambda}
             (v+1 tensor u+lambda x)^T
             A
             (v+1 tensor u+lambda x).

    This is the explicit Riemannian quotient by translations and positive
    dilations. For every arbitrary continuous strict stationary matrix
    profile, C2 off the origin, and every N, the adaptive metric is complete
    exactly when alpha=2 and `(Sigma_N,h)` is complete. Since the closure of
    `Sigma_N` is compact, this is precisely the condition that every
    collision diagonal has infinite quotient distance. It is the full
    irregular non-TRI criterion; the Osgood and matrix-TRI integrals are
    computable certificates for this exact collision-end metric.

12. Full arbitrary-matrix N=2 block and magnetic laws. Put

       A=Phi(0), B=Phi(2e),
       B_s=(B+B^T)/2, C=(B-B^T)/2.

    In center-relative canonical variables the normalized cometric is

       J(e) = [[(A+B_s)/2,-C],[C,2(A-B_s)]],

    and the metric is `4 r^(-2) J(e)^(-1)`. The odd skew part `C` produces
    the exact zero-total-momentum center drift `-rho^2 C pi`. For even
    profiles, `C=0` and the fixed-center relative metric is an exact
    Kaluza--Klein metric over the direction sphere. Fixing logarithmic-scale
    momentum reduces the relative geodesic and Jacobi equations to magnetic
    mechanics on `S^(d-1)`. The matrix-TRI line-sphere product is the
    zero-connection constant-coefficient specialization.

13. Full scalar two-landmark geometry. For any strictly positive-definite
   scalar radial profile, put a=phi(0), b=phi(2), B=2/(a-b), and

       x = 2 sqrt((a-b)/(a+b)) (q^1+q^2)/2,
       q^1-q^2 = r omega.

   The entire alpha=2 two-landmark metric is

       B [ (dr^2+|dx|^2)/r^2 + g_S ],

   hence is exactly the product B(H^(d+1) x S^(d-1)). This supplies the
   complete distance formula, sectional curvatures -1/B, 0, and 1/B,
   injectivity radius pi sqrt(B), cut locus, and ambient conjugate locus.
   For d>=3, a pure angular geodesic first becomes ambient-conjugate at
   length pi sqrt(B), with multiplicity d-2. For d=2 there are cut points but
   no conjugate points; for d=1 each order component is a hyperbolic plane.

14. Matrix-TRI adaptive sector. For every strict matrix-valued TRI profile, the
   alpha=2 fixed-center sector is the exact product

       [2/delta_parallel] ds^2
         + [2/delta_perp] g_S.

   Its distance, cut locus, and conjugate locus follow in closed form.

15. Fixed-kernel matrix-TRI reduction. For an ordinary stationary matrix TRI
   kernel, the two-landmark fixed-center metric is

       dr^2/[2 delta_parallel(r)]
         + r^2 g_S/[2 delta_perp(r)].

   This gives the exact collision-completeness integral and the radial and
   tangential sectional-curvature formulas.

16. Tail-controlled decoupling. If kappa and Dkappa are small beyond distance
   R, the full landmark flow differs from the flow with cross-cluster terms
   deleted by O(eta(R)) on finite time intervals, with an explicit Grönwall
   factor.

## Literature boundary

- Niethammer--Vialard (MFCA 2013) substantially anticipates the negative
  fixed-LDDMM scale-invariance conclusion.
- Bauer--Bruveris--Michor (arXiv:1305.1150, Theorem 9.8) prove completeness
  for admissible C1 fixed kernels.
- Habermann--Preston--Sommer (arXiv:2503.10611; DCDS 2026) give the complete
  scalar stationary landmark completeness criterion for every N,d.
- Micheli--Michor--Mumford (arXiv:1009.2637; SIAM J. Imaging Sci. 2012)
  develop scalar fixed-kernel landmark curvature and conjugate points.

Those are cited as prior work, not claimed as discoveries. Bounded run-index,
arXiv, exact-phrase, and web searches through 2026-07-23 found no exact
statement of the configuration-normalized admissible-profile theorem, the
directional-Osgood theorem, the universal matrix N=2 theorem, the exact
arbitrary-matrix normalized-shape classification, the general N=2 block and
magnetic reductions, the scalar or matrix-TRI adaptive integral criteria,
either power-exponential N-dependent phase diagram, the
hyperbolic-times-sphere identification, the full two-landmark loci, the
adaptive matrix-TRI product, or the other surviving structural results.
Novelty remains subject to expert review.

## Scope

The source conclusion is a broad research agenda, not one formal conjecture.
The packet completes the exact-scale, admissible/directional-Osgood
adaptive-completeness, universal matrix two-landmark, scalar and matrix-TRI
monotone-gap, power-exponential phase-diagram, arbitrary-matrix
normalized-shape, and scalar two-landmark geometry subprograms. The general
N>=3 conjugate locus has no profile-independent closed formula here, and the
arbitrary even-matrix N=2 Jacobi problem is reduced to, rather than solved
past, its exact compact magnetic equation. The packet also does not select
an application-optimal scale functional. Although its profile may come from
an RKHS, the adaptive metric is configuration-dependent and is not induced
by one fixed ambient kernel.

## Verification and files

- `main.tex` and `solution_packet.pdf`: final 26-page expert-facing proof
  packet.
- `source_paper.pdf`: arXiv:1308.5739.
- `supporting_scale_invariance_Niethammer_Vialard_2013.pdf`: prior scale
  obstruction.
- `supporting_landmark_completeness_Habermann_Preston_Sommer_2025.pdf`: sharp
  fixed scalar completeness theorem.
- `supporting_landmark_curvature_Micheli_Michor_Mumford_2012.pdf`: fixed
  scalar curvature and conjugate-point prior work.
- `code/verify_multiscale_covariance.py`: 30 Hamiltonian covariance cases.
- `code/verify_full_geometry.py`: Gaussian operator, pair-distance, product,
  curvature, Jacobi, and exponent checks.
- `code/verify_admissible_profile_geometry.py`: matrix-profile completeness
  bounds, full scalar product, and adaptive matrix-TRI product checks.
- `code/verify_osgood_phase_diagram.py`: 80-decimal Schur asymptotics,
  collision exponents, inverse identities, and integral thresholds.
- `code/verify_matrix_tri_phase_diagram.py`: 180-decimal longitudinal Schur
  tests, a strict non-scalar TRI phase family, and 240 non-TRI N=2 tangent
  comparisons.
- `code/verify_shape_quotient_and_general_n2.py`: normalized-shape
  Schur/horizontal-lift identities, full skew-profile N=2 blocks, and the
  even-profile Kaluza--Klein reduction.
- `verification.md`: commands, results, literature corrections, PDF QA, and
  review focus.
