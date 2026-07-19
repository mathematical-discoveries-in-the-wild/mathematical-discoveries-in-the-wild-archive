# Rotund Ball Tilings Have Only Singular, Locally Diameter-Two Boundary Points

Status: `partial_result`

Source paper: Carlo Alberto De Bernardi, Tommaso Russo, Jacopo Somaglia,
*Lattice tilings of Hilbert spaces*, arXiv:2505.04267.

Targeted source problem: Problem 7.5 asks whether there exists a rotund and/or
smooth normed space that admits a tiling by balls.

## Result

Let \(X\) be a normed space of dimension at least two, and suppose that
translates of its closed unit ball form a tiling of \(X\). If the norm is
rotund, then every boundary point of every tile is singular for the tiling.

Equivalently, any rotund ball-tiling example answering Problem 7.5 must be
maximally non-locally-finite at the boundary: no boundary point can have a
neighbourhood meeting only finitely many tiles.

A later strengthening in the same packet shows more: every unit vector must
fail the locally non-D2 condition. Explicitly, for every \(x\in S_X\) and every
\(\delta>0\),
\[
  \operatorname{diam}\{y\in S_X:\|(x+y)/2\|\ge 1-\delta\}=2.
\]
Thus a positive rotund example would need a unit sphere that is rotund but
locally diameter-two at every point.

The same argument gives a smooth variant: if a boundary point is regular, then
it is quasi-polyhedral; if the norm is Gateaux smooth there, then it is a flat
point. Thus a smooth no-flat ball tiling has the same boundary-singularity
obstruction.

## Why This Is Partial

This does not decide whether a rotund or smooth normed space with a ball tiling
exists. It proves a necessary condition for any positive example. The source
paper's own construction fails to be rotund/smooth because it has many regular
quasi-polyhedral boundary points; this packet shows that this failure is not an
artifact of that construction but an unavoidable feature of every rotund
example unless all boundary points are singular.

## Verification

The proof uses two elementary/local facts already recalled in the source paper:

- a regular boundary point in a convex tiling is a \(\Delta\)-QP point;
- in dimension at least two, a convex body with a QP boundary point is not
  rotund, and a Gateaux smooth QP point is flat.
- a standard three-balls estimate of De Bernardi--Somaglia--Vesely and
  De Bernardi--Vesely converts singularity into local diameter-two behaviour.

The proof has no computational dependency.

## Novelty Check

Checked the run indexes for arXiv:2505.04267 and core phrases
`lattice tilings`, `rotund`, `smooth`, and `ball tiling`; no duplicate packet
was present. Web search found the source arXiv page and no later exact answer
to Problem 7.5.

## Files

- `main.tex` - proof note.
- `solution_packet.pdf` - compiled packet.
- `source_paper.pdf` - source paper PDF.

Human-review recommendation: verify whether this corollary is already explicit
in the older Klee--Maluta--Zanco/Klee--Tricot tiling literature. Even if known,
it is a useful local obstruction to keep attached to this target. The LND2
strengthening should also be compared with the De Bernardi--Vesely tiling and
star-finite covering results.
