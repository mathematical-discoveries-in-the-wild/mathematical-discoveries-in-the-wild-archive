# Verification audit

Status after audit: `still_likely_valid`, with the finite-vs-countable bridge
made explicit in `main.tex` and `README.md`.

Audit date: 2026-06-16.

## Source joins checked

- Maurey--Pisier input: local parsed source
  `data/parsed/arxiv_sources/2003.06345/source.tex:803--858` states exactly
  the contraction principle used in the thinning lemma, with exponent
  `1/max(p,q)` and dimension-free constant depending on `p`, `q`, and the
  cotype constant of `X`.
- UMD finite cotype: local parsed source
  `data/parsed/arxiv_sources/0703012/source.tex:367--372` recalls that every
  UMD space has finite cotype.
- Yaroslavtsev reduction: local parsed source
  `data/parsed/arxiv_sources/1907.11588/source.tex:4085--4095` states the open
  independent-increment aggregate-domination problem, and
  `source.tex:4188--4199` gives the finite predictable-jump approximation used
  for accessible martingales.

## Internal proof checks

- The deterministic iid thinning step is a direct substitution
  `theta_i = R_i eps_i` into Maurey--Pisier; the tail integral equals
  `a^(1/max(p,q))`.
- The non-identical selector step was rewritten explicitly: a Bernoulli-`a`
  signed selector is the smaller signed selector plus an independent centered
  remainder, so Jensen gives monotonicity from smaller thinning to common
  thinning.
- The random symmetric case is obtained by conditioning on the values and
  inserting independent signs; independence and symmetry are preserved.
- The Poisson layer step was rewritten explicitly: layer `k` has selector
  parameter
  `P(Pois(p_i) >= k) / p_i <= 1/k!`, so the thinning lemma applies layerwise,
  and the factorial powers are summable.
- Lower Poissonization and Poisson monotonicity use only symmetry plus Jensen:
  adding independent or conditionally mean-zero symmetric remainders cannot
  decrease the `L^p` norm of a convex norm power.
- The nonsymmetric mean-zero discrete result follows by standard
  symmetrization; aggregate domination is preserved under sign symmetrization.

## Caveat resolved in packet text

The packet proves the finite independent-increment comparison.  Remark 12.10
phrases the standalone discrete problem with countable sequences, but the
general-local martingale theorem needs the finite form at the level of
Yaroslavtsev's accessible-jump truncations.  The source then passes to the
limit in `L^p` using the accessible-jump approximation proposition.  This bridge
is now stated explicitly in the packet.

## Remaining human audit focus

The two highest-value referee checks are:

- the Jensen/sub-thinning argument in the finite-cotype thinning lemma;
- the final use of Yaroslavtsev's accessible-jump approximation to pass from
  finite predictable-jump estimates to the general accessible part.
