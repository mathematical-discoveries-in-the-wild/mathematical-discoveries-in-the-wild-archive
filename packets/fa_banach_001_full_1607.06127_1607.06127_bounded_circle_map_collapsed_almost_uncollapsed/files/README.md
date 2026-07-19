# Full Solution Packet: arXiv:1607.06127 Bounded Circle Map

## Classification

`full`

## Source

- arXiv:1607.06127
- Title: "On weaker notions of nonlinear embeddings between Banach spaces"
- Author: B. M. Braga
- Source PDF: `source_paper.pdf`
- Open-question screenshot: `figures/open_problem_crop.png`

## Targeted Question

Problem 2.6 asks whether there is a map `X -> Y` between Banach spaces which
is collapsed, almost uncollapsed, and bounded.

## Result

Yes. Let `X = R`, let `Y = R^2` with the Euclidean norm, and set
`f(x) = (cos x, sin x)`.

- `f` is bounded because its image is the unit circle.
- `f` is almost uncollapsed because every pair at distance `pi` maps to
  antipodal points, so `rhobar_f(pi)=2`.
- `f` is collapsed because for every threshold `t>0`, some period
  `2*pi*k >= t` gives `f(0)=f(2*pi*k)`, hence `rho_f(t)=0`.
- `f` is not solvent because its image diameter is at most `2`.

If an infinite-dimensional domain is desired, the packet also gives an
unrestricted-map variant. For any infinite-dimensional Banach space `X`, pick
`u in X` with `||u||=1`, set `A=2*pi*Z*u`, let `I=X/A`, take
`Y=ell_2(I)`, and define `F(x)=e_{x+A}`. Exact distance `pi` pairs cannot lie
in the same coset, but `0` and `2*pi*k*u` do lie in the same coset at
arbitrarily large distances.

## Proof Idea

Almost uncollapsedness only asks for one exact distance at which all pairs are
separated. Collapsedness asks whether some lower bound survives across all
larger distances. A periodic circle map separates exact distance `pi` but
repeats exactly at arbitrarily large multiples of `2*pi`. The
infinite-dimensional variant replaces the circle period by cosets of the
cyclic subgroup `2*pi*Z*u`.

## Files

- `main.tex`: LaTeX source for the packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: original arXiv PDF.
- `figures/open_problem_crop.png`: real screenshot crop of Problem 2.6.
- `code/make_open_problem_crop.py`: reproduces the source screenshot crop.
- `code/check_circle_map.py`: numerical smoke check for the circle-map
  identities used in the proof.

## Verification

`conda run --no-capture-output -n sandbox python code/check_circle_map.py`
passes. The proof itself is analytic and uses only the definitions in the
source paper plus the identities `f(x+pi)=-f(x)` and
`f(x+2*pi*k)=f(x)`.

## Literature Check

Local lightweight indexes were searched for `1607.06127`, title keywords,
`collapsed`, `almost uncollapsed`, and `bounded`; no duplicate packet or
attempt was found. Web searches on 2026-06-14 for exact and close phrases
found the source paper but no later paper explicitly answering Problem 2.6.
Novelty confidence is moderate because the construction is elementary.

## Human Review Recommendation

Send to human as a likely valid full answer under the printed statement. The
only main semantic risk is whether the author intended an unstated restriction
to cocycles, continuity, or another structured class of maps. The
finite-dimensional example is Lipschitz; the infinite-dimensional addendum is
only an unrestricted-map construction.
