# Verification record

## Analytic checks

The core proof was checked line by line against the source Hamiltonian:

1. With two landmarks, positions (x,0), and momenta (0,v), the first
   Hamilton equation gives qdot^1(0)=kappa(x)v.
2. Differentiating the proposed covariance transform gives
   Qdot^1(0)=lambda C_lambda kappa(x)v.
3. Applying the same first Hamilton equation to the transformed initial
   data gives Qdot^1(0)=A_lambda kappa(lambda x)v.
4. Arbitrary v forces matrix equality
   kappa(lambda x)=h_lambda kappa(x).
5. Positive definiteness and nonzeroness force kappa(0) nonzero;
   evaluation at zero forces h_lambda=1.
6. Continuity and lambda tending to zero force kappa to be constant.
7. The N-landmark block Gram matrix is
   (1_N 1_N^T) tensor kappa(0), with rank at most d < Nd for N>=2.
8. Conversely, for constant kappa=B the equations are
   qdot^a=B sum_b p_b and pdot_a=0; the choice C_lambda=1 and
   A_lambda=lambda gives exact dilation covariance.

## Deterministic script

Run from the repository root:

    conda run --no-capture-output -n sandbox python runs/fa_banach_001/solutions/partial/1308.5739_exact_scale_invariance_forces_degenerate_landmark_kernels/code/verify_scale_obstruction.py

Captured output (exit code 0):

    N=2: constant block Gram rank 2 < ambient dimension 4
    N=3: constant block Gram rank 2 < ambient dimension 6
    N=4: constant block Gram rank 2 < ambient dimension 8
    Gaussian test: kappa(2x)/kappa(x) equals 1.000000 at x=0 but 0.049787 at |x|=1
    Zero diagonal/nonzero cross test: quadratic values +2 and -2
    ALL SCALE-INVARIANCE OBSTRUCTION CHECKS PASSED

## Source and PDF QA

- source_paper.pdf is the arXiv PDF for 1308.5739.
- figures/open_problem_crop.png is cropped from PDF page 41.
- The crop was visually checked for legibility and inclusion of the
  conclusion's scale-invariance direction.
- All five pages of solution_packet.pdf were rendered to PNG at 150 dpi
  and visually inspected. No clipping, overlap, or illegible content was
  found.

## Literature check

The run's cheap indexes were searched before continuing. Bounded searches
on 2026-07-22 for the exact title and combinations of LDDMM, landmark
Hamiltonian, scale invariant, dilation covariance, and homogeneous
positive-definite kernel found no prior exact statement of the theorem in
this packet. This is a bounded novelty check, not an exhaustive review.

## Human review focus

Check the covariance quantifiers, the use of arbitrary two-landmark
initial data, the matrix-valued kernel Cauchy--Schwarz step, and the
fixed-kernel versus scale-family distinction.
