# Counterexample Packet: Almost Delta-Points Need Not Be Detected on the Sphere

- status: candidate counterexample, likely valid
- run: `fa_banach_001`
- source arXiv id: `2307.10647`
- source paper: Geunsu Choi and Mingu Jung, *The Daugavet and Delta-constants of points in Banach spaces*
- target passage: PDF page 9 / source lines 485--518, where the authors state that it is unclear whether the almost-Delta analogue of Proposition 2.12 holds in general.

## Claim

There is a Banach space `X` which admits almost Delta-points but satisfies
`delta c(x)=0` for every `x` in the unit sphere.

Thus the proposed analogue

```text
X admits almost Delta-points iff sup_{x in S_X} delta c(x)=2
```

is false in general.

## Construction

Let `E_m = ell_{p_m}^m` with `p_m=m^2` for `m>=3`, and set
`X = (direct sum E_m)_2`.

The space `X` is locally uniformly rotund, hence every point of `S_X` is a
denting point of `B_X`, so every sphere point has Delta-constant zero.

On the other hand, in each block the rescaled cube point
`x_m = m^{-1/p_m}(1-2/m,...,1-2/m)` is the average of `m` unit vectors whose
distances from `x_m` are at least `(2-2/m)/m^{1/p_m}`. These lower bounds tend
to `2`, so the embedded block points witness almost Delta-points in `X`.

## Files

- `main.tex`: full proof packet
- `solution_packet.pdf`: rendered packet
- `source_paper.pdf`: local copy of arXiv:2307.10647
- `figures/open_problem_crop.png`: crop of the source passage
- `code/verify_constants.py`: tiny numeric check for the constants

## Novelty Check

Before promotion, the agent checked the run indexes for `2307.10647`,
`Daugavet and Delta constants`, `almost Delta-points`, and related Delta-point
phrases. Only adjacent Delta-point literature packets appeared, not this
question. A web search for exact phrases around `almost Delta-points`,
`Delta-constant`, and the source passage found the source paper but no later
answer.

Human review should focus on the LUR argument for the Hilbertian sum and the
use of Proposition 2.3(b) from the source paper to pass from explicit convex
combinations to lower bounds on the Delta-constant.
