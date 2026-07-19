# Three summing-operator problems resolved by later optimality theorems

status: literature_implied_answer (all three source problems)
model: GPT5.6
source_arxiv_id: 1204.5411
supporting_arxiv_ids: 1307.4809, 1403.6064
agent_id: agent_lane_04

## Identification

Section 4, page 8 of Daniel Pellegrino's `1204.5411` asks three problems:

1. whether the interpolated coincidence for multilinear maps from `ell_1` to
   `ell_2` is sharp for some interpolation parameter;
2. the precise multiple-summing supremum for scalar `n`-linear forms on
   spaces of cotype `s>2`, with `n>=s`;
3. whether that multiple-summing supremum can equal the corresponding
   absolutely-summing supremum beyond `(s,n)=(2,2)`.

Later sharp theorems imply complete answers:

- Problem 1 is affirmative. In fact the coincidence is sharp for every
  `0<theta<=1`. This follows by combining the cotype-2 transfer identity in
  the source with the optimal exponent `2/(n+1)` proved in `1307.4809`.
- The supremum in Problem 2 is `2n/(2n-1)`, attained and independent of `s`.
  The universal lower bound and the sharp `ell_s` obstruction are both in
  `1403.6064`, Theorem 3.2 and Corollary 3.1.
- In Problem 3 the multiple and absolute suprema are equal exactly when
  `n=s`. Thus there are new equality cases `(s,n)=(k,k)` for every integer
  `k>2`; there is no equality when `n>s`.

## Provenance

This is an agent-identified implication, not a newly proved theorem. The
authors of `1403.6064` explicitly cite page 194 of the source and improve its
interval, but do not state the decisive specialization to `ell_s` or the
resulting equality classification. The paper `1307.4809` proves the endpoint
optimality needed for Problem 1 but presents it as the solution of a different
named conjecture.

## Files

- `solution_packet.pdf`: compact derivation and exact references.
- `source_paper.pdf`: arXiv:1204.5411.
- `supporting_paper_1307.4809.pdf`: optimal multilinear Grothendieck exponent.
- `supporting_paper_1403.6064.pdf`: sharp multiple-summing exponents.

