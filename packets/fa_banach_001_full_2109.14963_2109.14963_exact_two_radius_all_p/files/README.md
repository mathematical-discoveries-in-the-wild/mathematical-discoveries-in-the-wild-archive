# Exact two-radius classification on every L^p for H-type groups

Status: candidate full result, likely valid; specialist review recommended.

Source: E. K. Narayanan, P. K. Sanjay, and K. T. Yasser, *Injectivity of
spherical means on H-type groups*, arXiv:2109.14963; JFAA 30 (2024), article
33.

Source question: Remark 4.1 asks whether a two-radius theorem holds for
horizontal spherical means above the one-radius threshold
`2m/(m-1)`, including `p=infinity`.

## Full classification

Let the horizontal dimension be `2n` and the center dimension be `m>=2`.
Let

`E_n={sqrt(zeta_(k,i)/zeta_(k,j))}`

where the two positive zeros belong to the same generalized Laguerre
polynomial `L_k^(n-1)`. Let

`B_n={beta_i/beta_j}`

where `beta_i,beta_j` are positive zeros of the ordinary Bessel function
`J_(n-1)`.

- For `1<=p<=2m/(m-1)`, one radius is injective by the source theorem.
- For `2m/(m-1)<p<infinity`, the pair at radii `r,s` is injective exactly
  when `r/s` is not in `E_n`.
- For `p=infinity`, the pair is injective exactly when `r/s` is not in
  `E_n union B_n`.

Thus the first question in source Remark 4.1 is completely answered, with
sharp exceptional sets.

## Endpoint mechanism

M. Sundari's H-type Wiener-Tauberian theorem (arXiv:0803.2088,
Proposition 4.3) applies to the commutative biradial algebra
`R=L^1(G)^natural`. Its Gelfand spectrum has two branches:

- nonzero central frequency, with Laguerre spherical multipliers;
- zero central frequency, with Euclidean Bessel spherical multipliers.

For bounded `f`, let `I_f={g in L^1(G):f*g=0}`. This is a closed right
ideal. If both spherical means vanish, convolving each spherical measure
with Sundari's biradial Poisson kernel gives two members of `I_f intersect R`.
The Poisson kernel has nowhere-zero Gelfand transform. Outside
`E_n union B_n`, the two spherical-measure transforms have no common zero
on either spectral branch. Sundari's theorem therefore forces
`I_f=L^1(G)`, and an approximate identity gives `f=0`.

At a Laguerre exceptional ratio, the source's explicit spherical
eigenfunctions are bounded common-kernel vectors. At a Bessel exceptional
ratio, a center-independent Euclidean spherical function is a bounded
common-kernel vector.

## Files

- `solution_packet.pdf`: full proof packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: source problem paper.
- `tauberian_source.pdf`: Sundari's H-type Wiener-Tauberian paper.
- `figures/open_problem_crop.png`: complete source Remark 4.1.
- `verification.md`: proof, source, edge-case, and novelty audit.

## Human review focus

1. Confirm the standard multiplier extension placing
   `mu_r*P_a` in the biradial algebra and multiplying Gelfand transforms.
2. Check the translation of Sundari's spectrum notation to horizontal
   dimension `2n` and center dimension `m`.
3. Re-audit the finite-p support-containment step inherited from the earlier
   partial packet.
