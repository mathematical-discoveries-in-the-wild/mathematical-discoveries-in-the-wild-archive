# Verification report

## Claim checked

For horizontal spherical means on an H-type group with center dimension
`m>=2`, the two-radius problem is completely classified on every finite
`L^p`: in the high-p range the pair is injective exactly outside a countable
explicit set of same-level Laguerre root ratios. Only the nonexceptional
`p=infinity` endpoint of the source question remains open.

## Step check

1. **Spectral ingredients.** The source proves that every spectral projection
   `A_k` is bounded on `L^p` for `1<p<infinity` and that the Abel sum of the
   projections converges to `f` for `2<=p<infinity`.
2. **Support containment.** In the proof of source Theorem 1.1, the equation
   `f*mu_r=0` implies that the central Fourier transform of `A_k f` is
   supported in the zero set of
   `L_k^(n-1)(|a|r^2/2)`. Up to this point the proof uses only the preceding
   spectral results. The restriction `p<=2m/(m-1)` is used only in the next
   step, where source Theorem 2.4 kills an `L^p` function whose Fourier
   transform is supported on a sphere.
3. **Two supports.** Applying the same statement at radii `r` and `s` puts the
   Fourier transform in the intersection of the two zero sets.
4. **Root-ratio calculation.** For `k>=1`, a common point of radius
   `lambda=|a|>0` gives
   `lambda r^2/2=zeta_(k,i)` and
   `lambda s^2/2=zeta_(k,j)`, hence
   `r/s=sqrt(zeta_(k,i)/zeta_(k,j))`. Conversely, every such equality gives a
   common zero. For `k=0`, `L_0^(n-1)=1`, so there is no zero. At `a=0`, every
   `L_k^(n-1)(0)` is nonzero.
5. **Reconstruction.** Outside the exceptional set the support intersection
   is empty, so `A_k f=0` for every `k`. Abel summability yields `f=0` for the
   high range, where automatically `p>2`.
6. **Low range.** Source Theorem 1.1 already proves one-radius injectivity for
   `1<=p<=2m/(m-1)`.
7. **Sharpness.** At an exceptional ratio, choose the common level `k` and
   frequency `lambda`. The source eigenfunction `F_(k,lambda)` satisfies
   `F*mu_u=c_(k,n) phi_k^lambda(u)F` and lies in `L^p` exactly when
   `p>2m/(m-1)`. It is therefore a common nonzero kernel vector for both
   radii throughout the high-p range, including `p=infinity`.

## Stress tests

- The exceptional condition uses two roots from the **same** Laguerre level;
  cross-level root ratios are irrelevant because the support argument is
  applied separately to each `A_k`.
- The set is countable and contains `1`; admissible radii are automatically
  distinct.
- No support theorem on positive-codimension manifolds is used in the new
  high-p implication; empty distributional support is enough.
- The proof does not assert Abel reconstruction in `L^infinity`.
- No numerical computation is used as evidence.

## Literature and novelty check

- Cheap run indexes contained no exact entry for arXiv:2109.14963.
- Two bounded web-search rounds used the exact title and question, authors,
  `H-type`, `two radius/two radii`, `spherical means`, and `Laguerre zeros`,
  with arXiv-focused variants.
- Located the source arXiv record and its 2024 JFAA publication. A later
  thesis result concerns narrower tempered/periodic or Metivier-group
  settings, not the all-finite-`L^p` classification here. No primary source
  stating this exact theorem was found.
- Novelty confidence: **moderate**; a differently phrased harmonic-analysis
  result may exist and specialist citation review is required.

## Artifact verification

- `source_paper.pdf` is the original 20-page arXiv PDF.
- The screenshot crop contains all of source Remark 4.1 on physical PDF p. 19.
- `solution_packet.pdf` compiled without warnings. All four pages were
  rendered at 150 dpi and visually inspected; equations, the source crop,
  references, margins, and page breaks are clean and readable.

## Verdict

Likely valid substantial partial result. Send to a specialist in harmonic
analysis on nilpotent Lie groups, focusing on the precise hypothesis usage in
the source support-containment argument and on literature priority.
