# Infinite-sum converse fails for statistically maximizing sequences

Status: `counterexample_likely_valid`.

Source paper: Susmita Seal, Sumit Som, Sudeshna Basu, and Lakshmi Kanta
Dey, *Characterization of M-compact sets via statistically convergent
sequences*, arXiv:2008.08491v1 (2020), 11 pages.

## Result

Remark 3.7 asks whether the converse of Corollary 3.6 is true: if every
coordinate sequence is statistically maximizing in `M_i`, must the sequence
be statistically maximizing in the infinite `ell_p`-sum of the `M_i`?

The answer is no for every `1 <= p < infinity`, even when every coordinate
space is the Euclidean plane, every `M_i` has only three points, the full
sum set is bounded, and every coordinate sequence is maximizing in the
ordinary (stronger) sense.

For `alpha_i = 2^{-i}`, take

```text
A_i = (-alpha_i/2, 0),
B_i = ( alpha_i/2, 0),
C_i = ( alpha_i, alpha_i^2),
M_i = {A_i, B_i, C_i} subset R^2.
```

In the `ell_p`-sum, alternate the two product points `A=(A_i)` and
`B=(B_i)`. In coordinate `i`, both alternating points are farthest from
`(0,1)`, so the coordinate sequence is maximizing. Globally, statistical
maximality would force both product points to be farthest from one common
center `z=(z_i)`. The geometry of the three-point set forces every such
`z_i` to have norm at least `3/8`, contradicting `z in ell_p`.

## Proof mechanism

The third point is an anisotropic obstruction. The first two points are
separated horizontally at scale `alpha_i`, while the third is displaced
vertically only at scale `alpha_i^2`. If both horizontal points are farthest
from a center `(s,t)`, equidistance gives `s=0`, and comparison with the third
point gives

```text
t >= 3/8 + alpha_i^2/2.
```

Thus coordinatewise witnesses exist but cannot be assembled into an
`ell_p` witness. This is exactly the compactness failure hidden by passage
from finitely many coordinates (where the converse is true) to infinitely
many coordinates.

## Files

- `main.tex`: complete formal proof, verification notes, and novelty audit.
- `solution_packet.pdf`: rendered reviewer packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_problem_crop.png`: full-width source-page crop containing
  Corollary 3.6 and Remark 3.7.
- `code/check_geometry.py`: exact checks of the coordinate identities and a
  finite-dimensional illustration of the witness-norm divergence.
- `code/crop_source.py`: reproducible source-page crop.

## Novelty check

On 2026-07-19, exact-phrase, exact-title/citation, and close-variant searches
were run for the Remark 3.7 converse, statistically maximizing sequences in
infinite direct sums, and M-compactness. The searches found the source paper
and source-adjacent earlier farthest-point/statistical-convergence work, but
no later primary source answering this infinite-sum converse. The audit is
bounded rather than exhaustive.

## Reviewer focus

The key checkpoint is the implication from global statistical maximality to
coordinatewise simultaneous farthest-point equalities. It uses that the two
global distances alternate on sets of natural density `1/2`, followed by the
coordinatewise formula for the farthest distance in the bounded product set.
