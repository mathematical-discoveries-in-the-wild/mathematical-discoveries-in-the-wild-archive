# Banach universality for the weighted-composition question

Status: `full_solution_likely_valid`

Source paper: L. Abadias, F. J. Gonzalez-Dona, and J. Oliva-Maza,
*Universality arising from invertible weighted composition operators*,
arXiv:2406.02330.

## Result

The source asks whether, for
`\mathcal B = H^p` or `\mathcal A^p_\sigma`, the eigenspace
`ker(uC_\psi-\lambda I)` is complemented and contains a subspace isomorphic to
`\mathcal B`.

This packet proves both requirements under the hypotheses of the printed
question. The earlier complemented-kernel partial packet is kept under
`history/partial_kernel_complemented_2026_07_03/`.

## Proof Mechanism

Complementability follows because the source surjectivity proof on the range
spaces `B_{\mu,0}` and `B_{0,\nu}` admits a bounded linear splitting, hence
`\lambda I-uC_\psi` has a bounded right inverse.

For the copy-of-space half, the hyperbolic automorphism quotient
`\mathbb D / <\psi>` is an annulus. Multiplying a fixed eigenvector by
functions lifted from this quotient annulus stays inside the kernel. In the
Hardy case this gives a weighted Hardy space on the annulus, and standard
annulus factorization identifies it with `H^p`. In the Bergman case, the
kernel is an infinite-dimensional complemented subspace of
`A^p_\sigma \cong \ell^p`; by primeness of `\ell^p`, the kernel itself is
isomorphic to `A^p_\sigma`.

## Verification

- Source PDF and open-question crop are included.
- `solution_packet.pdf` renders from `main.tex`.
- The proof uses standard external facts: the annulus quotient of a hyperbolic
  automorphism, weighted Hardy factorization on annuli, atomic decomposition
  of weighted Bergman spaces, and primeness of `\ell^p`.

Human review should focus on the weighted Hardy annulus identification in
Lemma 3.2 of the packet; it is the nontrivial step that upgrades infinite
dimensionality to a copy of `H^p`.
