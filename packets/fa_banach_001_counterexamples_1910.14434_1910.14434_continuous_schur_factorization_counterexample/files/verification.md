# Verification report

Verdict: likely valid candidate full counterexample, pending expert review.

## Mathematical checks

1. **Topology and measure.** `N union {infinity}` is a compact metrizable
   convergent-sequence space. The masses `2^{-n}` sum to one. Every finite
   point is a positive-mass open atom, and every neighborhood of infinity
   contains a positive-mass tail, so the Radon probability measure has full
   support.
2. **Continuity.** Finite points are isolated. Near `(infinity,j)` the kernel
   is eventually zero because `j` belongs to one finite block. Near
   `(infinity,infinity)`, same-block entries have modulus `2^{-k/2}` and
   cross-block entries vanish.
3. **Atomic representation.** In the normalized atom basis
   `e_n = 1_{n}/sqrt(mu_n)`, an integral operator with kernel `K` has matrix
   entries `K(i,j)sqrt(mu_i mu_j)`. Replacing `K` by `phi K` therefore
   multiplies matrix entries by `phi(i,j)`, independently of the weights.
4. **Upper Schur bound.** Normalized Hadamard rows and standard basis columns
   have norm one and factor the kernel in an orthogonal direct sum. The formula
   `S_phi(T)=U^*(T tensor I)V` gives ordinary operator norm at most one.
5. **Sharp lower bound.** On a block of order `n`, multiplying the Hadamard
   matrix `H` by `H/sqrt(n)` entrywise produces `J/sqrt(n)`. Both input and
   output have operator norm `sqrt(n)`, so the block multiplier norm is one.
6. **No continuous factors.** The zero row and column at infinity allow both
   factors to be centered at their values at infinity without changing the
   kernel. Continuity makes the centered factor suprema on block `I_k` tend to
   zero. The finite factorization estimate would then make a norm-one block
   multiplier have norm tending to zero.

## Computational sanity check

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/1910.14434_continuous_schur_factorization_counterexample/code/verify_hadamard_blocks.py
```

The script builds Sylvester matrices through order 256 and checks the
orthogonality relation, the row-column factorization, and the exact norm-witness
ratio numerically. These calculations are not used in the proof.

## Literature check

The exact question appears in arXiv:1206.3889. The target paper
arXiv:1910.14434 proves the positive case and predicts a negative answer to
part (i). Searches for the exact question and for the block-Hadamard compactified
construction found no prior negative solution. This is a bounded search, not a
claim of exhaustive novelty.

## Review focus

The principal review point is the translation between the source paper's
measure-theoretic Schur multiplier convention and the atomic matrix model.
Because all finite points have positive mass and infinity has measure zero,
the normalized-basis calculation above makes that translation exact.
