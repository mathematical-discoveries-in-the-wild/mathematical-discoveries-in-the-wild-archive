# Counterexample: A Uniformly Convex Set with an Extreme Point That Is Not Strongly Exposed

Status: `counterexample`

Source problem paper: L. Garcia-Lirola, G. Grelier, and A. Rueda Zoca,
*Extremal structure in ultrapowers of Banach spaces*, arXiv:2109.01393.

## Target

Remark 4.15 asks whether every extreme point of a uniformly convex set `K` is
strongly exposed.

## Result

No. In the real Hilbert space `X = ell_2`, let

```text
K = { x in ell_2 : sum_{n>=1} n^2 x_n^2 <= 1 }.
```

Then `K` is a symmetric bounded closed convex uniformly convex subset of
`ell_2`. The point

```text
x0 = c (1/n^2)_{n>=1},  c = (sum_{n>=1} 1/n^2)^(-1/2),
```

is an extreme point of `K`, but it is not exposed by any ambient continuous
functional in `X* = ell_2`. Therefore it is not strongly exposed.

## Proof Mechanism

The set `K` is the unit ball of the stronger Hilbert norm
`|x|_K = (sum n^2 x_n^2)^{1/2}` embedded compactly in ambient `ell_2`.
Uniform convexity is inherited from the Hilbert ball because ambient distance
is dominated by `|.|_K`.

The obstruction is exactly the one anticipated in the source remark. The
Minkowski-functional norming functional at `x0` is
`y -> sum n^2 x0_n y_n`, but the representing coefficient sequence
`(n^2 x0_n)` is constant and hence not in ambient `ell_2`. Thus the intrinsic
strongly exposing functional exists, but it is not ambient-norm continuous.

## Evidence

- `figures/open_problem_crop.png`: Remark 4.15 from the source paper, PDF
  page 26.
- `source_paper.pdf`: local copy of arXiv:2109.01393.
- `solution_packet.pdf`: full proof packet.

## Novelty / Literature Check

Before packaging, the cheap run indexes were searched for arXiv:2109.01393,
`uniformly convex set`, `strongly exposed point`, `extreme point`, and close
phrases. The local parsed arXiv corpus was searched for close variants such as
`uniformly convex set strongly exposed`, `extreme point not strongly exposed`,
`compact ellipsoid`, and `Minkowski functional strongly exposed`. A web search
on 2026-06-14 for the exact phrase and close variants only surfaced the source
paper itself among relevant hits. No prior packet or direct literature answer
for this counterexample was found.

## Human Review Notes

Recommended review focus:

- Verify that the source definition of uniformly convex set is the symmetric
  bounded closed convex-set definition used here.
- Check the no-exposure step: any ambient `ell_2` functional exposing `x0`
  would have to represent the Hilbert norming functional, forcing a constant
  coefficient sequence, which is not in `ell_2`.
- Confirm that `not exposed` is sufficient to refute `strongly exposed`.
