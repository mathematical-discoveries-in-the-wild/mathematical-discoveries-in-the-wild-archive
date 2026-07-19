# Sigma-Unital Coronas Fail BCP

Status: `partial_result_likely_valid`.

Source target: Jinghao Huang, Karimbergen Kudaybergenov, Rui Liu, *The
ball-covering property of von Neumann algebras and noncommutative symmetric
spaces*, arXiv:2311.14257, Question 3.

Packet path:
`runs/fa_banach_001/solutions/partial/2311.14257_sigma_unital_coronas_fail_bcp/`

## Result

Let `A` be a nonunital sigma-unital C*-algebra. Then its multiplier corona

`M(A) / A`

fails the ball-covering property.

Consequently, if `D` is any nonzero sigma-unital C*-algebra and `H` is an
infinite-dimensional separable Hilbert space, then

`M(K(H) tensor_min D) / (K(H) tensor_min D)`

fails BCP. This includes the earlier stabilized unital corona theorem and also
covers the standard stable multiplier coronas with nonunital sigma-unital
coefficients.

## Why This Matters

This removes the main obstruction left by the previous Hilbert-module block
packet. The earlier finite-coordinate proof stalled because nonunital
coordinate projections are multiplier projections rather than compact
projections. The new proof avoids coordinate projections entirely: it cuts a
sequential approximate unit of the ideal into disjoint annuli and builds the
escaping multiplier as a strict sum over those annuli.

## Proof Intuition

For `T in M(A)`, the quotient norm `||Q(T)||` is the limit of
`||T(1-e_n)||` along any contractive approximate unit. If the approximate unit
is chosen with `e_{n+1}e_n=e_n`, then finite annuli `e_m-e_n` recover that
norm. Given countably many proposed centers, choose infinitely many annuli for
each center where its quotient norm is almost visible. On each annulus choose
a scalar phase that is Hahn-Banach far from the corresponding local piece of
the center. The strict sum of the phased, slightly larger annuli is a norm-one
multiplier whose corona class stays outside every ball `B(x, ||x||)`.

## Scope

This is not a full characterization of all C*-algebras with BCP. It is a broad
negative theorem for sigma-unital corona algebras. It leaves open what happens
for non-sigma-unital multiplier coronas and for arbitrary C*-algebras not
presented as coronas.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv:2311.14257 source paper.
- `figures/open_problem_crop.png`: crop of Corollary 3.9 and Question 3.

## Human Review Recommendation

Review as a major partial theorem for Question 3. The key checks are:

- the finite-annulus recovery lemma for quotient norms in `M(A)/A`;
- the strict convergence of the orthogonal annulus sum;
- the Hahn-Banach phase choice on each annulus;
- the final diagonal estimate against arbitrary compact/ideal perturbations.
