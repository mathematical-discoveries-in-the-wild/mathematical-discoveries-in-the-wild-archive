# Adversarial verification

Status: `candidate_full_likely_valid`

## Claim audited

If `conv_2(X)=0`, there is a Lipschitz-open, second-order Lipschitz map from
the unit ball of `X` into `X` which is not locally convex at zero. This is
the contrapositive needed for Problem 6.1 of arXiv:1205.3412.

## Audit checklist

### 1. Exhaustiveness of the support dichotomy

For a flat triple `(x,y,sigma)`, let its ratio be

```text
(1-||(x+y)/2||) / ||(x-y)/2||^2.
```

Case I says that some fixed unit vector `v` and `c>0` are detected in
absolute value by triples of arbitrarily small ratio. Its negation is
exactly: for every fixed `v,c`, below some ratio threshold all norming
supports satisfy `|sigma(v)|<c`. Taking the minimum of finitely many such
thresholds gives the simultaneous finite-set statement used in Case II.
There is no compactness or separability assumption hidden here.

In Case I, a subsequence has one sign, so `v` can be replaced by `-v` and
`sigma_n(v)>=c` arranged. In Case II, setting
`v_n=z_n/||z_n||` gives `sigma_n(v_n)=1` while the previous weighted
directions contribute at most `alpha_n/4`. With `alpha_n=16^{-n}`, the
future tail is exactly `alpha_n/15`. Therefore the `n`th diagonal term
dominates by at least `1-1/4-1/15 > 1/2`.

Verdict: passes.

### 2. Order of choices

The weights `alpha_n`, uniform bilinear norm bound `kappa=1/15`, and lower
coefficient `beta_n` are known before the `n`th triple is chosen. Hence one
can first choose `epsilon_n` small enough for the inverse-error estimate and
then choose the triple with flatness ratio below
`epsilon_n beta_n/4`. In Case II, that flatness threshold can be intersected
with all finite-set disappearance thresholds. The final bilinear series is
then formed from the already chosen triples.

Verdict: passes; no circular selection remains.

### 3. Map hypotheses

On the unit ball, `Q(x)=B(x,x)` has Lipschitz constant at most
`2||B|| <= 2/15 < 1`. Thus `f=Id+Q` is co-Lipschitz and injective. For every
ball compactly contained in the domain, the fixed-point map `z -> w-Q(z)`
is a contraction whenever `w` lies in the claimed output ball. This proves
the exact uniform Lipschitz-open condition from the source, not merely
topological openness. The centered second difference is `2B(h,h)`, so
`Lip_2(f)<=2/15`.

Verdict: passes.

### 4. Inverse displacement constants

Let `r=epsilon z+u` be the unique preimage of the image midpoint. The
co-Lipschitz estimate gives

```text
||u|| <= C kappa epsilon^2 ||h||^2,
C=(1-2kappa)^(-1).
```

Expansion yields

```text
u + 2 epsilon B(z,u) + B(u,u) = epsilon^2 B(h,h).
```

Using `||z||,||h||<=1`, the error after replacing `u` by
`epsilon^2 B(h,h)` is at most

```text
epsilon^2 ||h||^2
  (2 C kappa^2 epsilon + C^2 kappa^3 epsilon^2).
```

The stipulated choice of `epsilon_n` bounds this by half the detected
support displacement. No division by `||h_n||` occurs, so configurations
with very small chords cause no problem.

Verdict: passes.

### 5. Nonconvexity and uniqueness

Both endpoints have norm at most `epsilon_n`, strictly below `rho_n`. The
support functional puts the unique midpoint preimage strictly outside the
closed `rho_n`-ball. Injectivity on the whole unit-ball domain rules out a
second preimage inside. Hence the midpoint is absent from the image of the
small ball. Since `rho_n -> 0`, local convexity at zero fails.

Verdict: passes.

### 6. Scalar field and consequence

For complex `X`, the construction is performed on the underlying real
space. The problem's Lipschitz, openness, second-difference and convexity
conditions are metric/real conditions, so a real-bilinear quadratic map is
admissible. Positivity of `conv_2(X)` makes the given norm uniformly convex;
standard renorming characterizations then imply superreflexivity.

Verdict: passes.

## Remaining review risk

No mathematical gap was found in the audit. The result is nevertheless new
relative to the bounded search, so the packet is labeled `likely_valid`, not
`verified`. A specialist should independently reconstruct the logical
negation leading to Case II and confirm that the source intended arbitrary
metric maps rather than a narrower complex-analytic category.
