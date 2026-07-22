# Verification report

## Claimed result

Under only the decay hypothesis (1.2a) from arXiv:1409.2143, there is a
two-dimensional orthonormal wavelet system for which the nominal
`(1,0)`-directional projection cannot satisfy any interpolatory estimate whose
right-hand side tends to zero with `||R_1u||_2/||u||_2`. This is a candidate
full negative answer to the source's literal decay-only open problem.

## Proof audit

1. **Valid decay-only wavelet system.** Start with the standard tensor Haar
   basis and swap the orientation labels `(1,0)` and `(0,1)` at every dyadic
   square. Relabeling preserves orthonormality and completeness. Every Haar
   wavelet has absolute value at most `1_Q`, so it satisfies (1.2a) with
   `C=1` for every positive decay exponent.

2. **Projection identity.** For the relabeled system,
   `W^(1,0)=P^(0,1)`, the ordinary Haar projection onto wavelets constant in
   `x_1` and cancellative in `x_2`.

3. **Exact range vectors.** The unit dyadic squares
   `Q_k=[k,k+1) x [0,1)`, `0<=k<N`, carry `(0,1)` Haar wavelets whose sum is
   the long-strip function `u_N`. Hence `W^(1,0)u_N=u_N` exactly.

4. **Riesz-transform limit.** Write
   `u_N(x_1,x_2)=a(x_1/N)b(x_2)`, with `a=1_[0,1)` and `b` the unit Haar
   function. Plancherel and the multiplier
   `xi_1/sqrt(xi_1^2+xi_2^2)` show that the squared norm ratio equals

   `integral [(zeta/N)^2/((zeta/N)^2+xi_2^2)] |a_hat(zeta)|^2 |b_hat(xi_2)|^2`.

   The multiplier tends to zero for almost every `(zeta,xi_2)` and is bounded
   by one. The remaining product is integrable by Plancherel, so dominated
   convergence proves the ratio tends to zero.

5. **Contradiction to interpolation.** Any estimate with a control function
   `Psi(t)->0`, applied to `u_N` and divided by `||u_N||_2`, gives
   `1 <= C Psi(r_N)` with `r_N->0`, an impossibility. Power controls
   `Psi(t)=t^beta` and logarithmic control
   `Psi(t)=t(1+log(1/t))` are included.

## Stress tests

- The construction needs dimension at least two; dimension two suffices to
  refute the universal decay-only claim.
- Every `u_N` is a finite sum of basis vectors, so no closure or convergence
  issue enters the projection identity.
- The proof uses only `p=2`. Since the requested family of estimates includes
  the Hilbertian case, failure there is decisive.
- The example deliberately fails the source's direction-specific sectional
  oscillation condition (1.2c) after relabeling. This is the mechanism, not a
  hidden defect: the open problem says “decay estimates only.”
- If the intended question silently retains (1.2c) and removes only Holder
  regularity, this packet is a sharp obstruction/partial boundary result, not
  a resolution of that narrower interpretation.

## Literature and novelty check

- Cheap local indexes: no hit for arXiv:1409.2143 or the exact open problem.
  Nearby Riesz-transform results were unrelated.
- Exact web search: searched the full sentence beginning “It remains an open
  problem to prove interpolatory estimates” and close variants.
- Author/title/arXiv search: searched the exact title, authors, directional
  wavelet projection, Riesz transform, and decay-only terms, restricted to
  arXiv for the technical variants.
- Results found: the arXiv source and 2016 EMS published version. No later
  primary source answering this question was located.
- Novelty confidence: **moderate**, because citation search was bounded and a
  differently phrased later result may exist.

## Artifact verification

- The screenshot crop contains the complete item 4 problem statement and its
  immediate comparison with the Haar estimate on source PDF p. 4.
- The proof is symbolic; no computation is used as evidence.
- Final LaTeX compilation completed without warnings, overfull boxes, or
  undefined references. All four pages of the latest PDF were rendered at
  150 dpi and visually inspected; no clipping, overlap, illegible text, or
  broken references were found.

## Human review requested

Check:

1. the semantics of “decay estimates only” versus an implicit retention of
   sectional oscillation (1.2c);
2. the legitimacy of orientation relabeling under the literal hypotheses;
3. the dominated-convergence calculation; and
4. literature priority under alternative terminology.
