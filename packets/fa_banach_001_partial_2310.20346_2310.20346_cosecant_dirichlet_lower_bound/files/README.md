# Cosecant certificate for the bidisc weak-product constant

Status: `candidate_partial_likely_valid`

Source: Konstantinos Bampouras and Ole Fredrik Brevig, *Norm attaining
vectors and Hilbert points*, arXiv:2310.20346, open problem on page 3.

## Result

Let

`K_2 = sup ||f||_W / ||f||_H1`,

where `W(T^2) = H^2(T^2) odot H^2(T^2)`.  The packet proves

`K_2 >= pi/2`.

Equivalently, if the constant `C_2 > 0` asked for in the source paper exists,
then necessarily

`C_2 <= 2/pi`.

This improves the finite obstruction cited in the source paper.  It does **not**
prove that `C_2` exists and therefore does not settle whether `H^1(T^2)` and
`W(T^2)` are equal as sets.

## Construction

For `N >= 2`, use the homogeneous Dirichlet polynomial

`f_N = sum_(k=0)^(N-1) z1^k z2^(N-1-k)`

and the dual symbol with coefficients

`a_k = 1 / (N sin(pi(k+1/2)/N))`.

Every homogeneous Hankel block of this symbol is a rectangular submatrix of
the orthogonal matrix

`C_(r,s) = 1 / (N sin(pi(r+s+1/2)/N))`.

Hence the dual norm is at most one and

`||f_N||_W >= (1/N) sum_k csc(pi(k+1/2)/N)`.

The right side is `(2/pi) log N + O(1)`, while the classical Dirichlet-kernel
calculation gives `||f_N||_H1 = (4/pi^2) log N + O(1)`.  Their ratio tends to
`pi/2`.

## Verification

Run:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2310.20346_cosecant_dirichlet_lower_bound/code/verify_cosecant_certificate.py
```

The script checks the full cosecant matrix orthogonality, every homogeneous
Hankel-block norm, the certificate sum, and numerical `H^1` ratios for several
values of `N`.  These checks audit the formulas; the proof in `main.tex` is
analytic and does not depend on floating-point computation.

## Novelty check and limitations

A bounded arXiv/web search on 2026-07-21 used the phrases `polydisc Nehari
cosecant matrix`, `polydisc Nehari Dirichlet kernel`, `C_2 Nehari polydisc
pi/2`, and `weak factorization bidisc Dirichlet kernel`.  We also inspected
arXiv:2107.01680 (Brevig's earlier lower bound), arXiv:2101.00763, and the
source paper.  No occurrence of this cosecant/Dirichlet family or the
`pi/2` lower bound was found.  The `N=3` member recovers the certificate behind
the earlier quadratic bound, so the present result is best viewed as an exact
asymptotic extension of that construction.  Novelty confidence is moderate,
not definitive.

The failed amplification route is retained in the attempt history: digit-
separated products produce extra Hankel interactions whose norm growth erased
the gain in the tested cases.

## Human review recommendation

Review the indexing that identifies the homogeneous Hankel blocks with
submatrices of `C`, then the two elementary logarithmic asymptotics.  If those
pass, this is suitable as a substantial partial result; a broader literature
search should precede any external novelty claim.

