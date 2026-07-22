# All upper-critical radial quadratic coefficients are nonzero

Status: `partial_result_likely_valid`

Source: Fatima Aboud and Didier Robert, *Asymptotic expansion for nonlinear
eigenvalue problems*, arXiv:0903.0919.

## Result

For `P(x)=|x|^2`, the entire upper-critical half of the source's coefficient
conjecture holds. For every integer `j>=1`, in dimension `d=4j-1`,

```text
C_(2j)^(4j-1)(f) = A_j integral_0^infinity a^(3j-5/2) f(a) da,
```

where

```text
A_j = (-1)^j * 6(2j-1)sqrt(pi)
      / (2^(2j+1) Gamma(2j-1/2))
      * 2(1-2^(2j-1))B_(2j)/(2j)!  > 0.
```

Thus every positive source-admissible test function gives a nonzero
coefficient. In particular `f(z)=(z+1)^(-(6j-1))` is admissible. The pencil

```text
-Delta + (|x|^2-lambda)^2
```

has infinitely many nonlinear eigenvalues in every dimension `d=4j-1`, with
the source's counting lower bound

```text
N(R) >= c_epsilon R^(3j-3/2-epsilon).
```

## Mechanism

The invariant Weyl recurrence closes at every order. Its two highest powers
of `a=|x|^2` reduce to a two-dimensional harmonic-oscillator resolvent in the
variables `w=a-z` and the component of `xi` parallel to `x`. Mehler's formula
and the change `y=tanh(x)` reduce the decisive constant to

```text
[y^(2j)] (y/artanh(y))^(2j-1) / sqrt(1-y^2)
 = -(2j-1)[x^(2j)] x/sinh(x).
```

The latter coefficient is a nonzero Bernoulli number with a known sign.

## Scope

This is an all-order theorem, but still a partial answer to Conjecture (4.25):
it treats the radial quadratic polynomial and the dimensions `4j-1`. The
second critical family `4j-3` and general positive elliptic polynomials remain
open. Exact calculations also give positive `4j-3` coefficients through
`j=6`, but the packet does not promote that finite pattern to an all-order
claim.

## Verification

Run:

```bash
conda run --no-capture-output -n sandbox python code/verify_all_order_top.py --through 7
```

The checker reconstructs the complete four-invariant recurrence, including
all angular moments, and verifies the arbitrary-order closed formula at the
first seven orders in exact arithmetic. These finite checks audit the proof;
the proof itself uses coefficient extraction for arbitrary `j`.

Ledger:
`runs/fa_banach_001/ledger/results/0903.0919_radial_quadratic_all_upper_critical_dimensions.json`
