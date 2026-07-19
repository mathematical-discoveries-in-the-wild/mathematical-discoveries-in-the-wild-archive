# Counterexample: weak free Cramer fails for strictly convex free Gibbs laws

Status: `counterexample_likely_valid`.

Source target: Charles-Philippe Diez, *Free Stein kernels and moment maps*, arXiv:2410.02470.

The source states Conjecture 1, the "Weak free Cramer's conjecture": if `mu=nu_phi` and `nu=nu_psi` are one-dimensional free Gibbs measures associated with strictly `C^2` convex potentials, and `mu boxplus nu` is semicircular, then both `mu` and `nu` should be semicircular.

This packet gives a likely counterexample. For sufficiently small nonzero real `a`, take the compactly supported laws whose `R`-transforms are
[
  R_a(z)=z/2+a z^2,
  R_{-a}(z)=z/2-a z^2.
]
They are small one-cut perturbations of the variance-`1/2` semicircle. Their boundary Hilbert transforms are `C^1`-close to the semicircular one, so each law is the equilibrium/free Gibbs law of a strictly `C^2` convex potential. But the `R`-transforms add:
[
  R_a(z)+R_{-a}(z)=z,
]
which is the `R`-transform of the centered variance-`1` semicircle. Neither factor is semicircular, because their third free cumulants are `+a` and `-a`.

Files:

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: crop containing the conjecture.
- `code/verify_cubic_perturbation.py`: numerical sanity check for the one-cut perturbation and convexity margin.

Human-review recommendation:

Check the standard one-cut perturbation lemma used in the packet: for small `a`, the algebraic inverse
`z=1/G+G/2+aG^2` is the Cauchy transform of a one-interval compactly supported law with positive analytic density, and the associated Hilbert-transform potential can be extended to a strictly `C^2` convex potential. This is the only substantive analytic point; the free-convolution contradiction is then immediate from cumulant additivity.

Bounded novelty check:

- Cheap run indexes were searched for `2410.02470`, `Free Stein kernel`, `free Cramer`, `free Gibbs`, and `semicircular`.
- Source-corpus searches found no existing packet for this arXiv id or the weak free Cramer conjecture.
- Web searches for the exact phrase `Weak free Cramer's conjecture`, and for `free Gibbs Cramer's theorem free convolution semicircular`, found the source and the classical Bercovici-Voiculescu failure of free Cramer, but no public answer to the strictly convex free-Gibbs variant in this bounded search.
