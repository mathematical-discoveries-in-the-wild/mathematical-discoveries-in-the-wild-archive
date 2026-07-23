# Verification report

Verdict: `candidate_full_solution_likely_valid_needs_human_review`

## Formal proof audit

The proof was checked at the following pressure points.

1. Differentiating

   `q(t) + beta int_[0,L] 1_{|t-s|<=1} q(s) ds = 1`

   gives

   `q'(t) = -beta q(t+1) + beta q(t-1)`

   whenever the indicated translated points remain in `[0,L]`. This fixes
   the superdiagonal sign `-beta` and subdiagonal sign `+beta`.

2. For `L=N+r`, `0<r<1`, translation by one preserves the two cell chains
   `R_k=[k,k+r]` and `S_k=[k+r,k+1]`. Their endpoint equations are exactly
   the two matrix-exponential matching equations in the packet.

3. The last scalar equation is the undifferentiated Fredholm equation at
   `t=0`; it restores the constant lost on differentiation.

4. A homogeneous coefficient vector reconstructs a homogeneous Fredholm
   solution. The strict bound `||T_L||<2` rules out such a solution for
   `beta=+/-1/2`, proving that every finite coefficient matrix is
   nonsingular.

5. The SO(odd) kernel differs from the Sp kernel by the positive rank-one
   term `Pq=(int q)1`. Therefore, if `q_-=(I-T_L/2)^(-1)1` and
   `Q_-=int q_-`, the SO(odd) solution is exactly `q_-/(1+Q_-)`.

6. The variational conclusion follows from Cauchy-Schwarz in the positive
   operator inner product. Equality fixes the optimizer up to scalar, and
   the equation `B_G g=1` fixes its normalization.

7. On each interval `N<L<N+1`, the square system is real-analytic in
   `r=L-N` and its determinant never vanishes. Across integer `L`, the
   zero-extended kernels converge in Hilbert-Schmidt norm, so the resolvent
   and the relevant integrals are continuous.

No unresolved lemma is used in the result.

## Numerical pressure test

Command:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/\
1507.03598_all_support_optimal_test_function_algorithm/code/verify_algorithm.py
```

Main tested lengths:

```text
0.4, 1, 1.4, 2, 2.4, 3, 3.7, 5.25, 8.1
```

For both `beta=1/2` and `beta=-1/2`, the script:

- builds the breakpoint translation orbits;
- solves the square matrix system;
- checks continuity at every cell boundary;
- evaluates the Fredholm residual on 401 points;
- checks the SO(odd) rank-one rescaling.

The maximum residual in the main suite was below `4.3e-14`. Additional runs
at `L=1+/-1e-6`, `2+/-1e-6`, and `3+/-1e-6` showed convergence of the
computed integrals from both sides of each integer. These computations are
not part of the proof.

## Bounded novelty check

Checked on 2026-07-23:

- local run registry, solution, attempt, and proof-gap indexes;
- arXiv ids `1507.03598`, `1708.01588`, and `2011.10140`;
- author/title searches for Freeman, Miller, optimal test functions, all
  support, finite-dimensional optimization, coefficients, matrix
  exponentials, and Conjecture 12.1;
- the exact phrase concerning real-analyticity at integers and
  half-integers.

Found:

- arXiv:1708.01588 reduces the all-support problem to a finite-dimensional
  family, solves only two support ranges by matrices, asks for a general
  coefficient solution, and states Conjecture 12.1;
- arXiv:2011.10140 concerns a restricted two-level problem and does not
  supply the one-level all-support coefficient system.

Not found:

- a square all-support coefficient system equivalent to the one in this
  packet;
- a later proof of Conjecture 12.1.

This is a bounded search, not a guarantee of novelty.

## Recommended human checks

- Confirm the interval shift and kernel normalizations against
  arXiv:1507.03598.
- Check the endpoint ordering in the two noninteger cell chains.
- Confirm the admissibility/factorization step for the resulting optimal
  test function at arbitrary support.
- Search citations to arXiv:1708.01588 for differently phrased later work.
