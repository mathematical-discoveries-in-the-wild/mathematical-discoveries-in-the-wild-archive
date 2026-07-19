# Infinite-dimensional Hilbert codomains in Theorem 4.7 of arXiv:2209.01767

Status: `partial_result_likely_valid`

Source target: Sheldon Dantas, Mingu Jung, Martin Mazzitelli, and Jorge Tomas Rodriguez, *On the strong subdifferentiability of the homogeneous polynomials and (symmetric) tensor products*, arXiv:2209.01767.

## Result

The source proves that, in the complex case, `(c0, H)` has the `2`-homogeneous polynomial `L_{p,p}` when `H` is finite-dimensional Hilbert. It then notes that finite dimensionality is only used to know that `(ell_infty^A, H)` has the same polynomial point property.

This packet removes that restriction:

- for every finite-dimensional Banach space `E`, every Hilbert space `H`, and every `N`, the pair `(E,H)` has the `N`-homogeneous polynomial `L_{p,p}`;
- consequently, for every complex Hilbert space `H`, the pair `(c0,H)` has the `2`-homogeneous polynomial `L_{p,p}`;
- consequently, `(hat tensor_{pi_s}^2 c0) hat tensor_pi H` is SSD on elementary tensors for every complex Hilbert space `H`, extending the source corollary from finite-dimensional Hilbert spaces.

## Mechanism

An `H`-valued homogeneous polynomial on a finite-dimensional domain has range contained in the span of finitely many Hilbert-valued coefficients. That coefficient span has dimension bounded only by `N` and `dim E`. Reducing to that finite-dimensional Hilbert subspace recovers the compactness proof used in the source paper, uniformly over the finitely many possible dimensions.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_problem_crop.png`: crop of Theorem 4.7 and the finite-dimensional Hilbert notice.

## Scope

This is not a full solution of all questions in arXiv:2209.01767. It addresses the finite-dimensional Hilbert restriction around Theorem 4.7 and the following tensor-product SSD corollary. It does not settle the source question about replacing uniform convexity of `Y` by `Y*` being SSD in Theorem A, nor the open problem on non-Hilbert micro-transitive norms.
