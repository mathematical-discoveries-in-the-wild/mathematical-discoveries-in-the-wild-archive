# Verification report

Status: candidate full solution, likely valid.

## Formal audit

1. **Exact source match.** Page 6 of arXiv:1805.02115v2 asks whether the
   coordinatewise bilinear product from `ell_1 x ell_1` to `ell_1` is
   Lipschitz `p`-summing. The theorem covers this map for every finite `p`.
2. **Difference tensor.** For every tested pair, the coefficient array is the
   difference of two decomposable tensors. Flattening the first index against
   the remaining indices therefore produces an operator of rank at most two.
3. **Diagonal estimate.** Pairing the flattening with the phase-adjusted
   diagonal partial isometry gives the `ell_1` norm of the diagonal. Trace
   duality and Cauchy-Schwarz on at most two singular values give
   `||Delta z||_1 <= sqrt(2)||z||_2`.
4. **Admissible test forms.** Every sign array defines a bounded `m`-linear
   form on `ell_1^m` of norm exactly one, since its coefficients have modulus
   one.
5. **Khintchine step.** The lower scalar Khintchine inequality applies to the
   absolutely summable, hence square-summable, coefficient array. It is valid
   over both the real and complex scalar fields.
6. **One common supremum.** After raising the pointwise bound to the `p`th
   power, the inequalities are summed before expectation. The expectation of
   the finite sum is bounded by its supremum over sign arrays, exactly matching
   the denominator in the source definition.
7. **Infinite-dimensional passage.** No truncation limit is needed: each
   coefficient array lies in `ell_1(N^m)`, so the sign series converges
   absolutely and the flattening is Hilbert-Schmidt and finite rank.

No circular use of Lipschitz summability occurs, and the proof does not use the
non-p-summability of the associated linearization.

The final `solution_packet.pdf` has four pages. It compiled with no unresolved
references, overfull boxes, or LaTeX warnings; all four rendered pages and the
source crop were visually inspected for clipping and legibility.

## Computational check

Command:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/1805.02115_coordinatewise_product_lipschitz_p_summing/code/finite_rank_sign_check.py
```

The script uses a fixed random seed and tests real and complex decomposable
differences for arities 2 and 3 in dimensions 2 and 3. It checks rank at most
two, the deterministic diagonal/Hilbert-Schmidt inequality, and the exact
finite sign supremum for small families. This is a sanity check only; the proof
is the analytic argument in `main.tex`.

Observed output:

```text
seed=180502115
deterministic rank/diagonal cases=960
exact finite sign-family cases=120
largest observed p=2 ratio=0.8671086950
all checks passed
```

## Literature check

The cheap run indexes, bounded exact-phrase arXiv web search, and local
full-source corpus of later citing papers found no prior answer to this exact
coordinatewise-product question. arXiv:2204.01775 explicitly answers a
different question from Section 7 of the source and is excluded from the new
claim.
