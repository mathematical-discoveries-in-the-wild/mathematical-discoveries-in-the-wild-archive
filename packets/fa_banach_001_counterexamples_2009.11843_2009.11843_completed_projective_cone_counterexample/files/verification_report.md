# Verification report

Candidate: arXiv:2009.11843, Question `q:completed-semisimple` / PDF Question 5.16.

## Claim audited

The packet gives a negative answer by constructing closed proper generating cones whose completed projective cone has nonzero lineality.

## Line-by-line checks

1. **Kernel pair.** The source itself records that (X\widehat\otimes_\pi Y\to X\widehat\otimes_\varepsilon Y) need not be injective. Passing to the closed spans in an absolutely convergent representation preserves nonzeroness in the projective tensor (the original tensor is its image) and preserves the zero injective image because the injective tensor norm is injective on subspaces.
2. **Hilbert gauges.** A countable separating subset of (B_{X^*}) exists for separable (X). The weighted coordinate map into (ell_2) is bounded and injective, so (p(x)=\|Jx\|_2) is a continuous norm. Likewise for (Y).
3. **Base cones.** The epigraph cones (t\ge p(x)), (s\ge q(y)) are closed. Applying the inequalities to an element and its negative proves properness. The displayed two-term decomposition proves they are generating.
4. **Four-sign lemma.** Expanding positivity on ((p(x),\sigma x)) and ((q(y),\tau y)) gives four inequalities. Pairwise addition cancels both linear cross terms and yields (-ap(x)q(y)\le A(x,y)\le ap(x)q(y)).
5. **Hilbert factorization.** The preceding domination extends (A) to the Hilbert completions. Functoriality gives a commutative projective/injective diagram. Since Hilbert spaces have the approximation property, the right vertical map is injective, forcing the projective Hilbert image of the kernel tensor to vanish.
6. **Nonzero embedded tensor.** The coordinate inclusions have bounded coordinate projections as left inverses, so their projective tensor inclusion cannot kill (z).
7. **Bipolar conclusion.** The dual of the closed projective cone is precisely the cone of continuous bilinear forms positive on the two base cones. Every such functional vanishes on (w), so both (w) and (-w) satisfy every dual inequality and belong to the closed cone. Thus its lineality is nonzero.

## Scope and caveats

- The proof answers the source's general yes/no question; it does not claim an explicit familiar Enflo-type model for the two Banach spaces.
- The only imported existence fact is the classical existence of a noninjective projective-to-injective tensor map.
- Novelty checking was bounded, not exhaustive.

## Recommended human-review order

First check the commuting tensor diagram and the reduction to separable subspaces. Then check the four-sign cancellation and the last bipolar step. These are the only points where a hidden tensor-topology or cone-duality error could affect the conclusion.
