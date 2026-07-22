# 0206108 -- a nonreflexive space with singleton ell-p spectrum

Status: literature-implied positive answer to Problem 2. Problem 1 remains open.

## Source questions

Eugene Tokarev, *An example of a Banach Space with a Subsymmetric Basis,
which has the Hereditarily Approximation Property*, arXiv:math/0206108,
asks:

1. whether a non-superreflexive Banach space can have the hereditary
   approximation property (HAP); and
2. the stated weaker question whether there is a non-superreflexive Banach
   space whose ell-p spectrum is exactly `{2}`.

Here the ell-p spectrum is the set of exponents `p` for which `ell_p` is
finitely representable in the space.

## Literature-implied answer

Johnson and Szankowski, *Hereditary approximation property*, Annals of
Mathematics 176 (2012), 1987--2001, state immediately after their open
Question 3 that there exist nonreflexive Banach spaces having type
`2-epsilon` and cotype `2+epsilon` for every positive `epsilon`; they cite
Pisier and Xu (1987) for these spaces.

Any such space `X` has ell-p spectrum exactly `{2}`. Indeed:

- Dvoretzky's theorem gives finite representability of `ell_2` in every
  infinite-dimensional Banach space.
- If `p<2`, choose `r` with `p<r<2`. Type `r` passes under finite
  representability, whereas `ell_p` does not have type `r`.
- If `2<p<infinity`, choose `s` with `2<s<p`. Cotype `s` passes under finite
  representability, whereas `ell_p` does not have cotype `s`.
- Finite cotype also excludes `ell_infinity`.

The space is nonreflexive, hence cannot be superreflexive. This is a positive
answer to Tokarev's Problem 2.

## Scope limitation

This does not solve Problem 1. Johnson--Szankowski formulate the stronger
question "Is every HAPpy space reflexive?" and explicitly leave it open.
Bounded exact-phrase and topic searches found no later primary-source
resolution.

## Files

- `main.tex`: proof and literature identification.
- `solution_packet.pdf`: compiled packet.
- `source_paper.pdf`: Tokarev's source paper.
- `supporting_johnson_szankowski_2012.pdf`: official Annals paper.
- Ledger: `runs/fa_banach_001/ledger/results/0206108_nonreflexive_singleton_lp_spectrum.json`.

