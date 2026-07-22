# Polynomial metric entropy of the monotone spherical chamber

Status: `partial_result_likely_valid`  
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

## Mechanism

After reversing coordinates, partition the indices into initial singletons and
then geometric blocks whose length is at most `eta` times their left endpoint.
Every decreasing unit vector is within squared `l_2` error `eta` of the
block-constant subspace.  Taking `eta=epsilon^2/8` reduces the covering problem
to a sphere of dimension at most `32 epsilon^(-2)(1+log M)`.

For the lower bound, use geometrically decreasing block sizes and perturb the
block energies according to a constant-weight binary code.  Monotonicity is
preserved, while distinct codewords have chordal distance greater than `2/5`.

## Files

- `main.tex` / `solution_packet.pdf`: complete statement and proof.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: the source question on page 16.
- `code/verify_entropy_bounds.py`: finite-dimensional checks of the partition
  estimate and packing construction.

The verifier passed at `(M,epsilon,d)=(4096,0.2,8)` with 300 random trials and
at `(7777,0.125,10)` with 200 trials.  In the first run the minimum enumerated
packing distance was exactly `sqrt(19)/10`, the constant used in the proof.

## Scope

This settles the order of the logarithmic covering number as the dimension
grows at every fixed accuracy `epsilon<=1/5`.  It does not determine the sharp
dependence of the polynomial exponent on `epsilon`, nor does it give a
practically optimized enumeration of the low-dimensional net.  It is therefore
packaged as a substantial partial answer rather than a complete resolution of
all formulations of the source's broad question.
