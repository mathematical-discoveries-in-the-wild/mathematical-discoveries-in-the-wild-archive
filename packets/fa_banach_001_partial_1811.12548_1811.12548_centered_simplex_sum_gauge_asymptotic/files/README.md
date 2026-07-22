# Finite-facet bound and centered-simplex asymptotic for the Minkowski-sum gauge question

Status: `candidate partial result - likely valid`

Source: Han Huang, Boaz A. Slomka, Tomasz Tkocz, and
Beatrice-Helen Vritsiou, *Improved bounds for Hadwiger's covering problem via
thin-shell estimates*, arXiv:1811.12548.

## Source question

Section 6, page 15 asks whether, for independent uniform random vectors
`X,Y` on an arbitrary centered convex body `K` in `R^n`, one has

`E ||X+Y||_K <= 2 - Omega(n^{-alpha})`

for some universal `alpha<1`, and in particular whether the worst deficit is
of order `n^{-1/2}`.  The source gives the cube benchmark

`E ||X+Y||_K = 2 - sqrt(pi/n) + o(n^{-1/2})`.

The exact source passage is in `figures/open_problem_crop.png`.

## Candidate partial theorems

For every centered polytope `K` with `N` facets,

`E ||X+Y||_K <= 2 - 3/(16 sqrt(N))`.

Thus the proposed `n^{-1/2}` deficit holds for every family of centered
polytopes having `O(n)` facets, including all simplices and parallelotopes.

For every centered `n`-dimensional simplex `K_n`,

`E ||X+Y||_{K_n} = 2 - sqrt(pi/(2n)) + o(n^{-1/2})`.

Consequently, the simplex deficit is asymptotically `1/sqrt(2)` times the
cube deficit.  In particular, the simplex has a larger expectation than the
cube in all sufficiently large dimensions.  The finite-facet theorem is much
broader and the simplex theorem gives its sharp leading constant in a natural
nonsymmetric case.  Neither proves the universal bound for arbitrary bodies.

## Proof idea

For the finite-facet result, write the gauge as the maximum of normalized
facet functionals.  Each facet deficit `U=1-phi(X)` is a nonnegative
log-concave variable of mean one, and `P(U<=t)<=2t` for `t<=1/2`.  Two
independent points can have total gauge within `t` of two only if both are
within `t` of the same facet; a union bound gives the `N^{-1/2}` deficit.

For the exact simplex asymptotic, by affine invariance use the centered simplex

`K_n = {x in R^{n+1}: sum x_i=0 and x_i>=-1}`.

Uniform points have the form `X=(n+1)P-1`, where `P` is flat Dirichlet.
The simplex gauge is `||z||_K=-min_i z_i`, hence

`||X+Y||_K = 2-(n+1) min_i(P_i+Q_i)`.

Write `P_i=E_i/sum E_j` and `Q_i=F_i/sum F_j` with independent unit
exponentials.  The denominators concentrate around `n+1`, while
`E_i+F_i` are independent `Gamma(2,1)` variables.  The minimum of `n+1`
such variables, multiplied by `sqrt(n+1)`, converges in distribution and in
mean to a Rayleigh variable with survival function `exp(-t^2/2)`.  Its mean
is `sqrt(pi/2)`, which gives the stated constant.

## Verification

- The formal proof includes the uniform-integrability tail estimate needed
  to pass from distributional convergence to convergence of expectations.
- The finite-facet proof separately audits the log-concave boundary
  small-ball lemma and the exact facet-deficit identity.
- `code/verify_simplex_asymptotic.py` numerically integrates the exact
  `Gamma(2,1)` minimum and Monte Carlo checks the normalized Dirichlet model.
- `verification_report.md` records the command, numerical output, and the
  separate analytic proof audit.
- The computation is a sanity check only; the theorem is analytic.
- Bounded novelty search: the run indexes, parsed arXiv corpus, arXiv search,
  and exact web phrases combining the simplex, the Minkowski functional of
  `X+Y`, and the Dirichlet minimum were searched.  No prior exact computation
  was found.  This is not an exhaustive bibliographic claim.

## Human review recommendation

Review as a likely valid substantial partial result.  The highest-value checks
are the small-ball lemma, both gauge identities, the scaling
`m^(3/2) min(P_i+Q_i)`, and the bad-event estimate used for convergence in
mean.
