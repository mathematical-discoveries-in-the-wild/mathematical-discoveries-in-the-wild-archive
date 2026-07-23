# Verification record

## Analytic audit

The following implications were independently rederived.

1. Exact covariance of qdot=G(q)p for arbitrary p forces
   G(lambda q)=lambda^alpha G(q); differentiated homogeneity supplies the
   momentum equation.
2. Metric inversion gives D_lambda^*g=lambda^(2-alpha)g. Along q=ru, length
   is a constant times integral r^(-alpha/2)dr, so completeness forces
   alpha=2.
3. For a matrix-valued stationary profile Phi, the feature-map identity is

       ||F_x u-F_y u||_V^2
         = u^T[2 Phi(0)-Phi(x-y)-Phi(y-x)]u.

   If V embeds in C_b^1 with constant L, duality bounds this by
   L^2|u|^2|x-y|^2.
4. In the adaptive alpha=2 metric, positivity and the block trace give

       ||G||_op <= N tr(Phi(0)) rho^2,
       ||d rho||_G^2 <= tr(Phi(0)) rho^2.

   For every pair map L_ab,

       L_ab G L_ab^T <= L^2 |q^a-q^b|^2 I.

   Dual Cauchy--Schwarz gives logarithmic lower bounds for both rho and every
   pair separation. A finite-length curve is Euclidean Cauchy and has a
   pairwise-distinct limit. This proves all-N completeness for every
   admissible profile.
5. The logarithmic pair barrier is the linear-modulus case of an Osgood
   argument. If

       2 Phi(0)-Phi(z)-Phi(-z) <= omega(|z|)^2 I

   and integral_0^1 dt/omega(t) diverges, then on a finite-length curve,
   where m<=rho<=M,

       |dot r_ab| <= M omega(r_ab/m) |dot q|_g.

   The Osgood coordinate integral dr/omega(r/m) cannot diverge in finite
   metric length. This proves completeness for every profile with an
   Osgood feature modulus.
6. For a scalar monotone kernel gap
   delta(r)=phi(0)-phi(r), finiteness of
   integral dr/sqrt(delta(r)) forces delta(r)/r^2 to tend to infinity:
   otherwise disjoint half-dyadic intervals each contribute a fixed positive
   amount. A symmetric binary collision in an N>=3 configuration has
   antisymmetric Gram block

       a_epsilon = delta(2 epsilon/rho(epsilon)).

   The complementary limiting block is positive definite, and its coupling
   to the antisymmetric direction is O(epsilon). Hence the Schur complement
   satisfies

       S_epsilon
         = a_epsilon-b_epsilon^T C_epsilon^(-1)b_epsilon
         ~ a_epsilon

   whenever the integral is finite. The exact path speed squared is
   2/(rho^2 S_epsilon), so the binary collision has finite length precisely
   when the scalar gap integral is finite. Together with the Osgood theorem,
   this is an exact criterion for monotone scalar gaps when N>=3. For
   exp(-|z|^beta), delta(r) is asymptotic to r^beta, giving the stated phase
   diagram.
7. For N=2 and a scalar radial profile, rho=r/2 freezes the normalized
   off-diagonal value at b=phi(2). The center/relative Hamiltonian has
   cometric eigenvalues rho^2(a+b)/2 and 2rho^2(a-b). With

       x=2 sqrt((a-b)/(a+b)) c,
       B=2/(a-b),

   the full metric becomes

       B [ (dr^2+|dx|^2)/r^2 + g_S ],

   the exact product B(H^(d+1) x S^(d-1)).
8. Hyperbolic space has no cut or conjugate points. The round sphere has cut
   point -omega and singular exponential vectors of standard-sphere length
   m pi with multiplicity d-2. Product geometry therefore yields the stated
   full ambient distance, curvature, injectivity radius, cut locus, and
   conjugate loci.
9. For an adaptive matrix-TRI profile, the fixed-center relative cometric at
   normalized radius two has radial and tangential eigenvalues
   r^2 delta_parallel/2 and r^2 delta_perp/2. Inversion gives the exact
   line--sphere product.
10. For an ordinary fixed matrix-TRI kernel, center/relative variables give
   the warped metric governed separately by delta_parallel(r) and
   delta_perp(r), including its collision integral and curvature formulas.
11. Deleting intercluster Hamiltonian terms changes qdot by kernel-tail terms
   and pdot by derivative-tail terms. A vector-field estimate followed by
   Grönwall gives the trajectory bound.
12. For `z=q^a-q^b=r e`, the pair-distance covector has exact squared
    cometric norm

        rho^2 e^T[2 Phi(0)-Phi((r/rho)e)-Phi(-(r/rho)e)]e.

    Hence an Osgood bound is needed only in the instantaneous separation
    direction, not in operator norm. The same Osgood-coordinate proof gives
    all-N completeness.
13. For N=2, `rho=r/2` and the normalized two-point matrix Gram `K(e)` is
    uniformly positive on the compact direction sphere. The full metric is
    uniformly equivalent to

        (|dc|^2+dr^2)/r^2 + |de|^2,

    so every continuous strict matrix profile is complete at alpha two.
14. For a matrix-TRI profile, collinear configurations preserve the
    longitudinal/transverse output splitting. The collision velocity is
    longitudinal, and its scalar Gram kernel is `k_parallel`. If the locally
    monotone longitudinal gap integral is finite, the dyadic argument and
    scalar Schur proof apply in that invariant sector. Together with the
    directional Osgood theorem this proves the exact matrix-TRI criterion;
    the tangential gap is irrelevant.
15. At alpha two, translations and positive dilations act isometrically.
    Every orbit has one centered RMS-one representative `x` in the
    normalized pre-shape manifold `Sigma_N`. If `A=K(x)^(-1)` and `V_x`
    contains the translation and dilation directions, horizontal
    minimization gives the quotient metric

        h_x(v,v)
          = v^T[
              A-A V_x(V_x^T A V_x)^(-1)V_x^T A
            ]v.

    A finite-length landmark escape has bounded positive rho and is
    Euclidean Cauchy, so it projects to a finite-length quotient path ending
    at a collision diagonal. Conversely, a finite quotient path to a
    diagonal has a same-length horizontal lift; the same estimates prevent
    escape in its translation/dilation fiber. This proves the exact
    arbitrary-matrix completeness equivalence.
16. For N=2, canonical center/relative variables transform the normalized
    Gram matrix into

        J(e) = [[(A+B_s)/2,-C],[C,2(A-B_s)]],

    where `B=Phi(2e)`, `B_s=(B+B^T)/2`, and `C=(B-B^T)/2`. Congruence proves
    positivity and metric inversion gives the full `4 r^(-2) J(e)^(-1)`
    law. The zero-total-momentum center drift is `-rho^2 C pi`. For even
    profiles `C=0`; completing the square in `s=log r` gives the exact
    Kaluza--Klein sphere metric and cyclic reduction gives the stated
    magnetic Routhian.

## Scale-covariance script

Command:

    conda run --no-capture-output -n sandbox python runs/fa_banach_001/solutions/partial/1308.5739_exact_scale_invariance_forces_degenerate_landmark_kernels/code/verify_multiscale_covariance.py

Exit code: 0. The 15 augmented and 15 adaptive Gaussian cases check five
exponents, three dilations, all relevant Hamilton equations, and positive
Gram eigenvalues at relative/absolute tolerance 2e-13. Final output:

    ALL AUGMENTED AND ADAPTIVE SCALE-COVARIANCE CHECKS PASSED

## Gaussian full-geometry script

Command:

    conda run --no-capture-output -n sandbox python runs/fa_banach_001/solutions/partial/1308.5739_exact_scale_invariance_forces_degenerate_landmark_kernels/code/verify_full_geometry.py

Exit code: 0. It checks:

- 12 deterministic configurations with N in {2,3,5,8}, d in {1,2,3};
- positive adaptive Gram eigenvalues and ||G||_op<=N rho^2;
- all 126 pair-cometric inequalities;
- the d rho bound and degree-two homogeneity;
- the Gaussian two-landmark product constant and Jacobi zero;
- negative fixed-kernel relative Gaussian curvature at 80 radii;
- both radial-end exponent thresholds.

Tolerance is 3e-12. Final output:

    ALL FULL-GEOMETRY IDENTITY CHECKS PASSED

## Admissible-profile geometry script

Command:

    conda run --no-capture-output -n sandbox python runs/fa_banach_001/solutions/partial/1308.5739_exact_scale_invariance_forces_degenerate_landmark_kernels/code/verify_admissible_profile_geometry.py

Exit code: 0. It checks:

- a strict non-TRI matrix-valued Gaussian mixture for all 16 combinations
  N in {2,3,5,8}, d in {1,2,3,4};
- positive Gram eigenvalues, the block trace and d rho bounds, degree-two
  homogeneity, and all 168 pair-feature inequalities;
- 80 random tangent identities for the full scalar
  H^(d+1)-times-S^(d-1) metric;
- 60 tangent identities for the fixed-center product of a strict matrix-TRI
  mixture containing a curl-free Gaussian component;
- the hyperbolic and spherical curvature scales and first sector conjugate
  constants.

Tolerance is 2e-11. Final output:

    ALL ADMISSIBLE-PROFILE GEOMETRY CHECKS PASSED

## Osgood phase-diagram script

Command:

    conda run --no-capture-output -n sandbox python runs/fa_banach_001/solutions/partial/1308.5739_exact_scale_invariance_forces_degenerate_landmark_kernels/code/verify_osgood_phase_diagram.py

Exit code: 0. Using 80-decimal arithmetic, it checks:

- all 16 combinations of (N,d) in {(3,1),(4,2),(6,3),(8,4)} and
  beta in {0.5,1,1.5,1.9};
- the exact full-inverse versus Schur-complement identity at collision
  scales 1e-12 and 1e-18;
- positivity and S_epsilon/a_epsilon tending to one;
- logarithmic Schur slopes agreeing with beta to 2e-3;
- finite positive scaled speeds;
- the finite beta<2 model integrals and logarithmic beta=2 threshold.

Final output:

    ALL OSGOOD PHASE-DIAGRAM CHECKS PASSED

The first four scripts test finite-dimensional formulas and inequalities.
Completeness, incompleteness, and conjugacy are established analytically.

## Matrix-TRI phase-diagram script

Command:

    conda run --no-capture-output -n sandbox python runs/fa_banach_001/solutions/partial/1308.5739_exact_scale_invariance_forces_degenerate_landmark_kernels/code/verify_matrix_tri_phase_diagram.py

Exit code: 0. Using 180-decimal arithmetic, it checks:

- a strict genuinely matrix-valued TRI family on all 16 combinations
  `(N,d)` in `{(3,2),(4,3),(6,4),(8,5)}` and beta in
  `{0.5,1,1.5,1.9}`;
- the full matrix inverse against the longitudinal Schur formula at
  collision scales `1e-20` and `1e-50`;
- the exact longitudinal antisymmetric-block/gap identity;
- positivity, `S/delta_parallel` tending to one, and logarithmic exponent
  beta;
- finite scaled collision speeds and the beta-two logarithmic threshold;
- 240 tangent comparisons for the universal N=2 theorem using a strict
  non-TRI stationary Gaussian matrix mixture.

Final output:

    ALL MATRIX-TRI PHASE-DIAGRAM CHECKS PASSED

## Shape-quotient and general N=2 script

Command:

    conda run --no-capture-output -n sandbox python runs/fa_banach_001/solutions/partial/1308.5739_exact_scale_invariance_forces_degenerate_landmark_kernels/code/verify_shape_quotient_and_general_n2.py

Exit code: 0. It checks:

- 100 normalized-shape Schur, horizontal-orthogonality, horizontal-lift, and
  quotient-isometry identities for strict non-TRI Gaussian matrix mixtures
  on `(N,d)` in `{(3,2),(4,2),(5,3),(7,3)}`;
- 160 full center-relative cotangent/tangent block identities for a strict
  real stationary spectral Gaussian kernel with a nonzero odd skew part;
- the exact zero-total-momentum skew center drift;
- 180 Kaluza--Klein completions for strict even non-TRI profiles.

Final output:

    ALL SHAPE-QUOTIENT AND GENERAL N=2 CHECKS PASSED

All six scripts are computational checks of formulas and asymptotics, not
substitutes for the analytic proofs.

## Literature corrections and novelty bounds

The bounded search used:

- Niethammer--Vialard (MFCA 2013): prior smooth right-invariant scale
  nonexistence theorem;
- Bauer--Bruveris--Michor, arXiv:1305.1150, Theorem 9.8: prior admissible
  fixed-kernel completeness theorem;
- Habermann--Preston--Sommer, arXiv:2503.10611, Theorem 2: complete fixed
  scalar landmark completeness criterion for every N,d, including the same
  exponent-two threshold for a fixed scalar kernel gap;
- Micheli--Michor--Mumford, arXiv:1009.2637: fixed scalar landmark curvature
  formulas and conjugate-point examples;
- Sommer--Lauze--Nielsen--Pennec and Liu--Younes, arXiv:2501.04031:
  established discrete and continuous multiscale LDDMM.

The searches on 2026-07-22 and 2026-07-23 used run indexes, arXiv ids,
author/title searches, and the phrases `configuration-dependent bandwidth`,
`adaptive landmark kernel`, `scale-invariant landmark metric`, `landmark
hyperbolic sphere product`, `two-landmark hyperbolic geometry`, `adaptive
cometric landmark`, `landmark cut locus`, and `matrix-TRI completeness`.
The final pass added `Osgood landmark completeness`, `RMS-normalized landmark
kernel`, `power-exponential landmark metric`, `rough adaptive landmark
kernel`, `variable bandwidth LDDMM completeness`, and exact-phrase variants.
The matrix pass added `TRI kernel completeness`, `longitudinal landmark
kernel completeness`, `radial tangential matrix kernel landmark
completeness`, `adaptive matrix-valued landmark metric`, and
`two-landmark matrix-valued kernel completeness`.
The arbitrary-matrix pass added `normalized pre-shape sphere`, `shape
quotient landmark completeness`, `matrix-valued landmark Kaluza--Klein`,
and `magnetic geodesic matrix kernel`.
It found the fixed-kernel integrability theorem of
Habermann--Preston--Sommer, which is cited as prior mechanism, but no exact
statement for the configuration-normalized directional-Osgood theorem, the
universal matrix N=2 theorem, the arbitrary-matrix normalized-shape
classification, the general N=2 block/magnetic reductions, the N-dependent
scalar or matrix-TRI adaptive integral criteria, either power-exponential
phase diagram, the full hyperbolic-times-sphere identification and loci, or
the adaptive matrix-TRI line--sphere product. This is a bounded novelty
assessment and requires expert review.

Local decisive supporting PDFs:

- `supporting_scale_invariance_Niethammer_Vialard_2013.pdf`;
- `supporting_landmark_completeness_Habermann_Preston_Sommer_2025.pdf`;
- `supporting_landmark_curvature_Micheli_Michor_Mumford_2012.pdf`.

## PDF QA

The final clean build is a 26-page US-Letter PDF of 827091 bytes. The final
LaTeX log contains no warnings, overfull or underfull boxes, undefined
references, or suppressed diagnostics. `tmp/main.pdf` and
`solution_packet.pdf` are byte-identical. The packet was rendered at 150 dpi,
and all 26 pages were individually inspected; no clipping, overlap, malformed
equations, broken references, or other visual defects were found.

## Human review focus

Prioritize:

- the RKHS feature-map implication and the finite-length escape criterion;
- the Osgood reparametrization and its use of the finite-length rho bounds;
- the radial-covector calculation in the directional-Osgood theorem;
- the uniform compact-sphere comparison proving universal N=2 matrix
  completeness;
- the dyadic proof that a finite monotone-gap integral forces
  delta(r)/r^2 to infinity;
- positivity of the limiting complementary Gram block, the O(epsilon)
  coupling estimate, and the Schur-complement asymptotic;
- the N=2 versus N>=3 quantifiers in the power-exponential phase diagram;
- invariance of the longitudinal sector for collinear TRI configurations
  and the claim that the tangential gap drops out;
- the quotient-metric Schur formula and both directions of the horizontal
  lift completeness equivalence;
- the center-relative skew signs for a non-even matrix profile;
- the Kaluza--Klein completion and the sign of the magnetic Routhian;
- the center/relative cometric constants and the hyperbolic coordinate
  rescaling;
- the distinction between first and all conjugate endpoints;
- the circle case, where cut points occur without conjugate points;
- the radial/tangential constants in the adaptive and fixed matrix-TRI
  reductions;
- the bounded, nonexhaustive novelty conclusion.
