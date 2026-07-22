# Exact quadratic-chaos reduction and a sign-paired subcase of Question 1.1

Status: `likely_valid partial_result`  
Source: Steven Heilman, *Low Correlation Noise Stability of Symmetric Sets*,
arXiv:1511.00382, Question 1.1 (Introduction, page 8 in the arXiv PDF).

## Result

For a measurable symmetric set `A subset R^n`, define the centered second
moment matrix

```text
C_A = integral_A (I - x x^T) d gamma_n(x).
```

After an orthogonal change of coordinates, the paper's functional is
`F(A)=||C_A||_F^2`.  The packet proves the exact variational identity

```text
sup_{A=-A} ||C_A||_F
  = (1/2) sup_{U=U^T, ||U||_F=1} E|X^T U X - tr(U)|.
```

Thus Question 1.1 is equivalent to the sharp second-Gaussian-chaos
inequality

```text
E|X^T U X - tr(U)| <= 2/sqrt(pi),   ||U||_F=1.
```

For each fixed `U`, an extremizing set in the inner set optimization is a
quadratic threshold `{x : x^T U x - tr(U) > 0}` (or its complement).

The packet then proves the desired bound when the eigenvalue multiset of `U`
is invariant under sign, i.e. it is

```text
(a_1,-a_1,...,a_m,-a_m,0,...,0).
```

Consequently, `F(A) <= 1/pi` whenever the nonzero eigenvalues of `C_A` occur
in opposite pairs.  The inequality is strict for nonzero finite-dimensional
`C_A` in this class.  In particular, it applies in dimension two whenever
`tr(C_A)=0`.

## Proof idea

Duality for the Frobenius norm converts the set problem into a scalar
quadratic-form problem.  Since every centered quadratic form is even, its
positive and negative regions are admissible symmetric sets, and the best
set captures exactly half of its `L^1` norm.

For a sign-paired spectrum, the quadratic form is a sum of independent
differences of squares.  Its characteristic function is real and positive:

```text
phi(t) = product_j (1 + 4 a_j^2 t^2)^(-1/2).
```

The normalization gives `2 sum_j a_j^2=1`, and `log(1+s) <= s` yields
`phi(t) >= exp(-t^2)`.  The Fourier representation of the first absolute
moment then compares the form directly with a centered Gaussian of variance
two and gives `E|Q| <= 2/sqrt(pi)`.

## Scope and unresolved point

This does **not** solve Question 1.1 for a general spectrum.  For arbitrary
eigenvalues the characteristic function has a nontrivial phase, so the
pointwise comparison with `exp(-t^2)` fails.  Numerical optimization found no
counterexample and instead approached the claimed constant through increasingly
diffuse positive spectra, but that is not a proof.

The symmetric infinitely divisible moment comparison in Klebanov--Kakosyan--
Volchenkova, arXiv:1904.07604, Theorem 3.1, independently subsumes the
sign-paired *moment inequality*.  The exact set/quadratic-chaos variational
identity and its application to Heilman's matrix functional were not found in
the bounded searches.  Accordingly, novelty should be treated as limited and
subject to expert review.

## Verification

- The matrix reduction is coordinate invariant and uses only finite-dimensional
  Frobenius duality.
- The characteristic function calculation and normalization are symbolic.
- The Gaussian comparison is strict at every `t != 0` for a nonzero finite
  sign-paired spectrum.
- `code/quadratic_l1_search.py` is exploratory only; it is not used in the
  proof.

Human-review recommendation: **review the reduction and classification as a
useful partial result; do not interpret it as resolving the asymmetric-spectrum
case.**

## Files

- `main.tex`, `solution_packet.pdf`: proof note.
- `source_paper.pdf`: arXiv:1511.00382.
- `code/quadratic_l1_search.py`: non-proof numerical search.
- Ledger: `ledger/results/1511.00382_sign_paired_second_moment_bound.json`.

