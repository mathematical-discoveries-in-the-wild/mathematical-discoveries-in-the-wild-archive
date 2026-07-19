# Partial Result: Real Forms For Subcases Of The Complex CSP Remark

status: likely_valid_partial_result

## Source Target

- Source paper: D. de Hevia, G. Martinez-Cervantes,
  A. Salguero-Alarcon, P. Tradacete,
  *A counterexample to the complemented subspace problem in Banach lattices*,
  arXiv:2310.02196v2.
- Target location: Remark 5.5, page 22 of the source PDF.
- Source question: whether every complemented subspace of a complex Banach
  lattice is linearly isomorphic to the complexification of some real Banach
  space.

## Result

This packet gives several positive subcases and normalization criteria for the
source question.

1. Every finite-codimensional complex subspace of a complex Banach lattice is
   linearly isomorphic to the complexification of a real Banach space.
2. Every complex Banach space with an unconditional Schauder basis is linearly
   isomorphic to the complexification of a real Banach space.  Hence any
   complemented subspace of a complex Banach lattice with such a basis satisfies
   the source question.
3. If a complex Banach space admits a bounded anti-linear automorphism `A` and
   the spectrum of `A^2` avoids the non-positive real axis, then the space has a
   real form.  Equivalently, `A` can be normalized by holomorphic functional
   calculus into an anti-linear involution.
4. The same conclusion still holds when the bad spectral set
   `spectrum(A^2) cap (-infty,0]` is finite and consists of isolated spectral
   values with finite-dimensional Riesz spectral subspaces: split off the
   finite-dimensional bad part and normalize the complement.
5. In particular, the conclusion holds under the compact-perturbation
   hypothesis
   `A^2 = lambda I + K`, where `K` is compact and
   `lambda` avoids the non-positive real axis; the finite-dimensional bad
   spectral part is split off.
6. In particular, if `Z` is a complex Banach space with a bounded conjugation
   `J`, `P` is a projection, `Y=PZ`, and
   `||P|| ||P - J P J|| < 1`, then `Y` is linearly isomorphic to the
   complexification of a real Banach space.

The perturbative projection statement includes the exact real-compatible case
`P=JPJ`, where the range is invariant under the ambient conjugation.

## Scope

This does not solve Remark 5.5.  It leaves open the case of arbitrary
infinite-codimensional complemented subspaces whose available projections may
be far from their conjugates and whose anti-linear self-isomorphisms, if any,
cannot be spectrally normalized.  The result is a partial positive answer and
a useful obstruction profile.

## Files

- [main.tex](main.tex): proof packet source.
- [solution_packet.pdf](solution_packet.pdf): rendered packet.
- [source_paper.pdf](source_paper.pdf): arXiv:2310.02196v2.
- [figures/open_problem_crop.png](figures/open_problem_crop.png): crop of
  Remark 5.5.
- [code/crop_open_problem.py](code/crop_open_problem.py): reproducible crop
  script.

## Checks

Cheap run indexes were searched for `2310.02196`, the source title,
`complexification`, `complex conjugate`, `GL-lust`, and complex Banach lattice
real-form phrases.  Web searches on 2026-06-16 found the source paper and the
2025 survey arXiv:2505.24084, but no exact prior packet or later answer to
Remark 5.5.  Novelty confidence is modest because the arguments are elementary;
the mathematical claim should be reviewed as a scoped partial result.

## Human Review Recommendation

Review as a likely valid partial positive result for Remark 5.5.  The main
checks are the finite-codimensional construction of a conjugation-invariant
complement, the unconditional-basis coefficient-conjugation argument, the
anti-linear spectral-normalization lemma, the finite-bad-spectrum and
compact-perturbation spectral splitting arguments, and the square-root
normalization in the perturbative projection criterion.
