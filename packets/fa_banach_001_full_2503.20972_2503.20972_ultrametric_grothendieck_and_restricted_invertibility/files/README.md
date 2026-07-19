# Two ultrametric answers in arXiv:2503.20972

Status: `candidate_full_likely_valid`

Source: K. Mahesh Krishna, *p-adic Grothendieck Inequality, p-adic
Johnson-Lindenstrauss Flattening and p-adic Bourgain-Tzafriri Restricted
Invertibility Problems*, arXiv:2503.20972v3.

## Results

This packet fully answers two of the paper's problems over every
non-Archimedean valued field `K`.

1. **Problem 1.4 has the sharp constant `K_K=1`.** The scalar hypothesis
   implies `|a_jk| <= 1` by testing coordinate vectors. The ultrametric
   triangle inequality and the defining estimate
   `|<u,v>| <= ||u|| ||v||` then give

   ```text
   |sum_jk a_jk <u_j,v_k>|
     <= (max_j ||u_j||)(max_k ||v_k||).
   ```

   The one-dimensional choice `a_11=u_1=v_1=1` proves sharpness.

2. **Problem 3.2 is false over every such field.** For each `d`, set

   ```text
   T(x_1,...,x_d) = (sum_j x_j)e_1.
   ```

   In the standard sup norm, `||T||=1` and every column `Te_j=e_1` has norm
   one. Any subset containing two columns is linearly dependent: coefficients
   `1` and `-1` cancel. Thus no positive constants `A,c` can guarantee both
   the proposed cardinality and lower estimate for all `d`.

## Why the classical analogy collapses

The strong triangle inequality replaces accumulation by a maximum. This
makes the normalized Grothendieck estimate immediate with no dimensional
loss. The same feature lets arbitrarily many identical normalized columns
form an operator of norm one, destroying the stable-rank mechanism behind
classical restricted invertibility.

## Scope

- The affirmative result answers **Problem 1.4**, whose scalar tests range
  over all field elements, including zero.
- It does not claim an answer to the distinct unit-sphere formulation in
  Problem 1.5.
- The Johnson-Lindenstrauss display in Problem 2.5 uses `1-epsilon` on both
  sides, apparently a typographical error. This packet neither corrects nor
  exploits that wording.

See `main.tex` and `solution_packet.pdf` for the proof and `verification.md`
for the adversarial audit.

The run's cheap indexes and a bounded primary arXiv search using the exact
title and problem phrases found the source paper but no later resolution.
This is not an exhaustive novelty certification.

Human review recommendation: **send to a non-Archimedean functional
analyst**. The mathematical arguments are elementary; the most valuable
review is exact matching to the source's quantifiers and conventions.
