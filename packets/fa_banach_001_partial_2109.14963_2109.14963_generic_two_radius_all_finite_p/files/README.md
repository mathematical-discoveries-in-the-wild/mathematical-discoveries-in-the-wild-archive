# Exact finite-p two-radius classification on H-type groups

Status: candidate substantial partial result, likely valid; human review
recommended.

Source: E. K. Narayanan, P. K. Sanjay, and K. T. Yasser, *Injectivity of
spherical means on H-type groups*, arXiv:2109.14963; published in *Journal of
Fourier Analysis and Applications* 30 (2024), article 33.

Source question: Remark 4.1 on arXiv PDF p. 19 asks whether a two-radius
theorem holds for `L^p(G)` above the one-radius threshold
`2m/(m-1)`, including `p=infinity`.

## Candidate result

Let `G` be an H-type group with horizontal dimension `2n` and center
dimension `m>=2`. For `k>=1`, let

`0<zeta_(k,1)<...<zeta_(k,k)`

be the positive zeros of the generalized Laguerre polynomial
`L_k^(n-1)`, and define the countable set

`E_n={sqrt(zeta_(k,i)/zeta_(k,j)): k>=1, 1<=i,j<=k}`.

For every `1<=p<infinity`, the pair of horizontal spherical means at radii
`r,s>0` is injective on `L^p(G)` as follows:

- below and at `2m/(m-1)`, one radius already suffices by the source theorem;
- above `2m/(m-1)`, the pair is injective exactly when `r/s` is not in `E_n`.

At every exceptional ratio, the source's spherical eigenfunction construction
gives a common nonzero kernel vector in every `L^p` above the threshold,
including `L^infinity`. For a nonexceptional ratio, the remaining unresolved
case is precisely `p=infinity`.

## Proof mechanism

For a fixed spectral level `k`, the source proof shows that
`f*mu_r=0` forces the central Fourier transform of the spectral projection
`A_k f` to be supported where

`L_k^(n-1)(|a|r^2/2)=0`.

Imposing the equation at a second radius `s` puts the same distribution in
the intersection of two such zero sets. That intersection is empty exactly
when `r/s` avoids the same-level Laguerre root ratios. Thus every `A_k f`
vanishes. The source's Abel summability theorem then reconstructs `f=0` for
all finite `p` in the previously open range. The original low-p theorem and
the source eigenfunction examples complete the finite-p classification.

## Files

- `solution_packet.pdf`: review packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source Remark 4.1.
- `verification.md`: proof and novelty audit.

## Human review focus

Check that the support-containment part of the source proof of Theorem 1.1
uses only its `L^p` spectral projection and Abel theorems, not the upper bound
`p<=2m/(m-1)`. The upper bound enters only in the subsequent theorem that
kills a distribution supported on one sphere; the two-radius argument avoids
that step by making the support empty.
