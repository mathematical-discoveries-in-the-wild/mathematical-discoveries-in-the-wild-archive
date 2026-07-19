# Full solution: arbitrary Banach wild-dynamics operators

Status: `claimed_full_solution`, pending human review.

Source: Jean-Matthieu Auge, *Linear operators with wild dynamics*, arXiv:1204.2044.

Question addressed: Remark 3.8 conjectures that operators with the properties
of Theorem 1.1 can be constructed in arbitrary Banach spaces, beyond the
separable case proved in the paper.

Result: Every infinite-dimensional real or complex Banach space admits an
operator `R = I + N`, with `N` nuclear, such that

- `A_R = {x : ||R^t x|| -> infinity}` has non-empty interior;
- `B_R = {x : liminf_t ||R^t x - x|| = 0}` has non-empty interior;
- `A_R` and `B_R` form a partition of the whole space.

Proof mechanism: replace the separable Ovsepian-Pelczynski biorthogonal
sequence by a normalized basic sequence in the arbitrary Banach space.  The
coordinate functionals extend by Hahn-Banach and remain uniformly bounded.
Choosing the root periods much faster than in the source paper makes the
periodic diagonal or rotation part return to the identity in operator norm,
which removes the separability/density requirement.

Novelty check: local run indexes had no prior `1204.2044` packet.  Web searches
on 2026-06-20 for the exact title, arXiv id, Remark 3.8 wording, Prajitura
conjecture variants, and `A_R`/`I+K`/nuclear perturbation phrases found the
source paper and the earlier Hajek--Smith symmetric-basis paper, but no later
exact answer to the arbitrary-Banach-space conjecture.  This is bounded, not
exhaustive.

Reviewer focus: verify the operator-norm estimate `S^(2m_n) -> I`, and in the
real case check that the rotation-block lower bound gives the same divergence
estimate as the complex diagonal proof.
