# Code Notes

No computational verification was used for this packet.

The proof is analytic. The useful check is the operator-theoretic criterion:

- `sup_n ||A^n|| < infinity`;
- `A` has no eigenvector with positive real eigenvalue;
- there are unit vectors `z_k` with `||Az_k-z_k|| -> 0`;
- therefore `U(x)=Ax/||Ax||` has no fixed point, has approximate fixed
  points, and has uniformly bounded Lipschitz iterates on the sphere.

For complex unconditional bases this is witnessed by unimodular coordinate
multipliers. For real spaces it is witnessed by the stated uniformly bounded
two-dimensional block rotations.
