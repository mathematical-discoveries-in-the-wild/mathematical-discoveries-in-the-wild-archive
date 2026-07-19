# Verification report

Verdict: `candidate_counterexample_likely_valid`

## Source audit

The source defines `H(phi)` by the uniform marginal bound

```text
P(|<X,a>|>=t) <= tau/phi(t).
```

On page 6 it says that it does not know whether its covariance estimate holds
at `p=4`.  On page 20 it asks whether the exponent for `4<p<=8` can be
improved to `1/2`, and displays the usual maximum-column correction.  This
packet tests the natural combination: the square-root covariance remainder at
the weak-`L4` endpoint.

## Distribution audit

Let `L=sqrt(N)` and define a nonnegative `Z` by

```text
P(Z>=u)=1          (0<=u<=1),
         u^(-2)    (1<u<=L),
         0         (u>L).
```

Equivalently, `Z` has density `2u^(-3)` on `[1,L)` and an atom `L^(-2)`
at `L`.  Set `mu=EZ`, take an independent Rademacher sign `epsilon`, and let
`X=epsilon sqrt(Z/mu)`.

- `EX=0` by symmetry.
- `EX^2=1` by normalization.
- If `mu t^2<=1`, then `t<1` and `P(|X|>=t)<=1<=t^(-4)`.
- If `1<mu t^2<=L`, then
  `P(|X|>=t)=(mu t^2)^(-2)<=t^(-4)`.
- If `mu t^2>L`, the probability is zero.

Thus the source hypothesis holds with `n=1`, `phi(t)=t^4`, and `tau=1`.

## Moment audit

Tail integration gives exactly

```text
mu=EZ=2-L^(-1),
EZ^2=1+2 log L=1+log N,
EZ^4=1+4 integral_1^L u du=2N-1.
```

For `W=Z-mu` and `sigma^2=EW^2`,

```text
sigma^2=1+log N-mu^2 >= log N-3.
```

Hence, if `log N>=6`, then `sigma^2>=(1/2)log N` and `sigma^4>=9`.
Also, using `(a-b)^4<=8(a^4+b^4)` and `mu<=2`,

```text
EW^4 <= 8(EZ^4+mu^4) <= 16N+120 <=136N.
```

## Paley--Zygmund audit

For independent copies and `R=sum_i W_i`, independence and centering give

```text
ER^2=N sigma^2,
ER^4=N EW^4+3N(N-1)sigma^4.
```

Since `sigma^4>=9`, the first term is less than
`16N^2 sigma^4`; the second is at most `3N^2 sigma^4`.  Therefore

```text
ER^4 <=19(ER^2)^2.
```

Applying Paley--Zygmund to `R^2` at level one half gives

```text
P(|R|>=sqrt(N sigma^2/2)) >=1/(4*19)=1/76.
```

Since `mu<=2`, this event implies

```text
|N^(-1) sum_i (X_i^2-1)|
  =|R|/(mu N)
  >=(1/4)sqrt(log N/N).
```

## Violation audit

Because `Z<=L` and `mu>=1`, deterministically

```text
max_i X_i^2/N <=L/N=N^(-1/2).
```

Thus a proposed right side
`C(max_i X_i^2/N+N^(-1/2))` is at most `2C/sqrt(N)`.  If
`log N>64C^2`, it is strictly smaller than the counterexample's fluctuation
on an event of probability at least `1/76`.  A success probability tending to
one is therefore impossible.  Integration of the same event gives the
expectation lower bound

```text
E|N^(-1)sum_i(X_i^2-1)| >=(1/304)sqrt(log N/N).
```

## Scope and literature audit

- The example addresses weak `L4`, not a uniformly bounded fourth moment.
- It rules out the square-root endpoint remainder, not every slower rate.
- Dependence of the law on `N` is legitimate against a universal
  nonasymptotic theorem; each row consists of iid variables.
- Searches covered the run registry and exact phrases involving
  `1509.02322`, `weak L4`, `p=4`, sample covariance, and square-root rates.
- arXiv:1606.03557 and arXiv:2205.08494 settle or sharpen finite-`p>4`
  variants; the latter still records a finite-`p=4` Bai--Yin problem as open.
  Neither gives this weak-tail endpoint counterexample.  Search date:
  2026-07-19.  This is not an exhaustive novelty guarantee.

## Packet render audit

`main.tex` compiled without warnings to a four-page PDF.  All four pages were
rendered at 150 dpi and visually inspected.  Both source crops are readable,
and no clipping, overlap, broken glyphs, or malformed references were found.

## Human verifier focus

Check the intended scope of the source's phrase "if it holds in the case
`p=4`."  The packet makes the exact disproof deliberately narrower: the
square-root endpoint bound displayed by the neighboring rate question.  No
claim is made about a logarithmically weakened endpoint theorem.
