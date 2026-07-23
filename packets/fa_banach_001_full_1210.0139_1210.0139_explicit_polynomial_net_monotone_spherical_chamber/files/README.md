# Explicit polynomial net for the monotone spherical chamber

Status: `full_result_likely_valid_fixed_accuracy_dimension_asymptotic`  
Source: M. Fickus, J. Jasper, D. G. Mixon, and J. Peterson,
*Group-theoretic constructions of erasure-robust frames*, arXiv:1210.0139,
Conclusions and future work, page 16.

Let

`T_M = {x in R^M : 0 <= x_1 <= ... <= x_M, ||x||_2 = 1}`

with chordal distance `rho(x,y) = sqrt(1-<x,y>^2)`, and let
`N_M(epsilon)` be its optimal covering number.  The packet proves

`M^c <= N_M(epsilon) <= (1+4/epsilon)^(32 epsilon^(-2)(1+log M))`

for all sufficiently large `M` and every `0<epsilon<=1/5`, with the lower
constant allowed to depend only through the fixed accuracy range.  In
particular, for each fixed `epsilon<=1/5`,

`log N_M(epsilon) = Theta_epsilon(log M)`.

Thus the correct dimension dependence is polynomial.  The source paper's
explicit level-quantization net has size `exp(O_epsilon((log M)^2))`.

The upgrade supplies a deterministic chamber-valued net, not merely the
abstract maximal net used to prove the sharper numerical upper bound.  For the
same geometric block partition, with

`d <= 32 epsilon^(-2) (1 + log M)`,

it explicitly constructs a chordal epsilon-net of size at most

`(42/epsilon)^d`.

The construction enumerates integer lattice points in a Euclidean ball, maps
each one to the weighted isotonic cone by metric projection, and normalizes.
Weighted pool-adjacent-violators computes every projection in `O(d)` time.
Consequently the net and its output-sensitive enumeration time are polynomial
in `M` for every fixed accuracy.

## Mechanism

After reversing coordinates, partition the indices into initial singletons and
then geometric blocks whose length is at most `eta` times their left endpoint.
Every decreasing unit vector is within squared `l_2` error `eta` of the
block-constant subspace.  Taking `eta=epsilon^2/8` reduces the covering problem
to a sphere of dimension at most `32 epsilon^(-2)(1+log M)`.

For the lower bound, use geometrically decreasing block sizes and perturb the
block energies according to a constant-weight binary code.  Monotonicity is
preserved, while distinct codewords have chordal distance greater than `2/5`.
Thus polynomial growth is unavoidable at every fixed `epsilon <= 1/5`.

## Files

- `main.tex` / `solution_packet.pdf`: complete statement and proof.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: the source question on page 16.
- `code/verify_entropy_bounds.py`: finite-dimensional checks of the partition
  estimate and packing construction.
- `code/verify_explicit_net.py`: checks lattice rounding, weighted isotonic
  projection, normalization, chamber preservation, and the constructive
  covering estimate.
- `history/partial_packet/`: the earlier nonconstructive partial packet.

The verifier passed at `(M,epsilon,d)=(4096,0.2,8)` with 300 random trials and
at `(7777,0.125,10)` with 200 trials.  In the first run the minimum enumerated
packing distance was exactly `sqrt(19)/10`, the constant used in the proof.
The explicit-net checker also passed 303 test vectors at `(4096,0.2)` and 203
test vectors at `(7777,0.125)`.

## Scope

This is classified as a scoped full answer to the source's natural
fixed-accuracy ambient-dimension problem: it determines the optimal complexity
class in `M` and provides an explicit structure-preserving polynomial-size net.
It does not determine the sharp joint dependence of the exponent on `epsilon`,
and it does not claim that the output-sensitive enumeration is practically
optimal in constants.
