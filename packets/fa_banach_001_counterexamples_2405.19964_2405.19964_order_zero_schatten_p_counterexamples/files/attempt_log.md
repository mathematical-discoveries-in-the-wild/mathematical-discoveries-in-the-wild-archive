# Attempt Log

Candidate: arXiv:2405.19964 p-Schatten boundedness question.

## Attempt 1: sum the almost-diagonal frame matrix

Idea: use the rapid decay of the source's four-index frame coefficients to
write the super operator as an absolutely summable series of left/right
shifts, uniformly bounded on every Schatten class.

Result: fails as a positive route. After the shifts are fixed, the remaining
coefficient array acts as a Schur multiplier. Bounded scalar entries suffice
on S2 but not on general Sp, so the frame estimate alone does not control the
needed multiplier norm.

## Attempt 2: endpoint triangular obstruction

Idea: take a smooth step function `phi(x-y)` so finite matrix compressions are
triangular projections. Their operator norms grow logarithmically, giving
failure on S-infinity and, by duality, S1.

Result: works, but only addresses the endpoints directly.

## Attempt 3: one sign multiplier bad for every p != 2

Idea: build a sign sequence in disjoint blocks. For each rational q>2, choose
Khintchine-small signs on infinitely many blocks. Multiplication by the same
signs turns those inputs into Dirichlet kernels, whose Lq norms grow faster.
Diagonalize over rational q, then use interpolation and duality. Smoothly
interpolate the sign sequence and compress the resulting kernel multiplier to
the associated Toeplitz Schur multiplier.

Result: works and strictly upgrades Attempt 2. Promoted as a candidate
counterexample likely valid pending human review.

