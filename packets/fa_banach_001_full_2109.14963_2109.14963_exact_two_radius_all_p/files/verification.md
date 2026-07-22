# Verification report

## Claim checked

The horizontal two-radius problem on an H-type group is exactly classified
on every `L^p`, including `L^infinity`. The high finite-p obstruction is the
same-level Laguerre root-ratio set `E_n`; the endpoint has the additional
Bessel root-ratio set `B_n`.

## Source verification

1. Source Remark 4.1 on physical arXiv PDF page 19 asks the exact two-radius
   question above `2m/(m-1)`, including infinity.
2. Source Theorem 1.1 supplies one-radius injectivity below and at the
   threshold.
3. The source proof gives the Laguerre-zero support containment for each
   spectral level before invoking its low-p Fourier-support theorem.
4. The source Abel reconstruction is valid for every finite `p>=2`, which
   yields the positive high finite-p implication when the two support sets
   are disjoint.
5. The source constructs the Laguerre-branch eigenfunctions and verifies
   their exact integrability threshold, including boundedness.

## Endpoint theorem verification

1. M. Sundari, arXiv:0803.2088, physical pages 5-6 describes the Gelfand
   spectrum of the biradial algebra `R=L^1(G)^natural`. In the notation of
   this packet its characters are the Laguerre branch `(lambda,k)` for
   `lambda>0`, and the Bessel branch `(0,tau)` for `tau>=0`.
2. Sundari Proposition 4.3, physical pages 10-12, says that every proper
   closed right ideal `I` in `L^1(G)` has a character annihilating all of
   `I intersect R`.
3. Sundari Proposition 4.4 proves that a biradial Poisson kernel `P_a` has
   nowhere-zero Gelfand transform on the entire spectrum.
4. For bounded `f`, Young's inequality makes
   `I_f={g in L^1(G):f*g=0}` a closed right ideal. Associativity makes it a
   right ideal.
5. If `f*mu_u=0`, then `g_u=mu_u*P_a` belongs to `I_f`. Convolution of a
   biradial finite measure with a biradial `L^1` function belongs to `R`,
   and its Gelfand transform is the product of the two transforms.
6. On `(lambda,k)`, the zero set of `hat(mu_u)` is exactly
   `L_k^(n-1)(lambda u^2/2)=0`; the exponential and normalization factors
   never vanish. Two radii have a common zero exactly at a ratio in `E_n`.
7. On `(0,tau)`, the multiplier is the normalized Bessel function
   `j_(n-1)(tau u)`. Two radii have a common zero exactly at a ratio in
   `B_n`. At `tau=0` the multiplier equals one.
8. Outside `E_n union B_n`, for every character at least one of `g_r,g_s`
   has nonzero transform. Proposition 4.3 rules out a proper `I_f`, so
   `I_f=L^1(G)`. Applying an `L^1` approximate identity gives `f=0`.

## Sharpness and edge cases

- `L_0^(n-1)=1`, so level zero has no Laguerre zeros.
- Every positive Laguerre root is simple and the ratio set uses two roots
  from the same level; cross-level ratios do not create a common character.
- The generalized Bessel function has the same positive zeros as ordinary
  `J_(n-1)`.
- A Laguerre exceptional ratio gives the bounded source eigenfunction.
- A Bessel exceptional ratio gives the bounded function
  `j_(n-1)(tau|z|)`, independent of the center variable.
- Bessel exceptional ratios do not obstruct finite `L^p`, because this
  center-independent branch has no nonzero finite-p vectors; the finite-p
  spectral argument removes it.
- Both exceptional sets are countable and reciprocal-invariant, and both
  contain one.

## Literature and novelty check

- The run indexes contained only the earlier finite-p partial result for
  this arXiv id.
- Two bounded exact-result searches used the title/question and variants of
  `H-type`, `two radius`, `L infinity`, `Wiener-Tauberian`, `Laguerre`, and
  `Bessel`.
- They located the source, its 2024 publication, Sundari's 2008 H-type
  Tauberian theorem, and adjacent Heisenberg/Gelfand-pair and X-ray results,
  but no primary source stating this exact horizontal spherical-mean
  classification.
- Novelty confidence is moderate pending a specialist citation search.

## Artifact verification

- `source_paper.pdf` is the original 20-page arXiv source.
- `tauberian_source.pdf` is arXiv:0803.2088; the spectral formulas and
  Proposition 4.3 were textually and visually checked on physical pages
  5-6 and 10-12.
- The source-problem crop contains all of Remark 4.1.
- `solution_packet.pdf` compiled without warnings. All four pages were
  rendered at 150 dpi and visually inspected; the source crop, equations,
  margins, page breaks, and references are clean and readable.

## Verdict

Likely valid candidate full result. Highest-priority audit: the biradial
measure-multiplier step and the exact applicability of Sundari Proposition
4.3. Second priority: the inherited finite-p support-containment audit and
literature priority.
