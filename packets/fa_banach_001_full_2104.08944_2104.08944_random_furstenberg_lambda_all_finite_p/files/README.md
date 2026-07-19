# Random Furstenberg set is Lambda(q) for every finite q

Status: `full_solution_likely_valid` (candidate full solution; human review required)

Model: `GPT5.6`

Source: Aihua Fan, Herve Queffelec, and Martine Queffelec,
*The Furstenberg set and its random version*, arXiv:2104.08944v2.

## Result

Let `T` be the independent Bernoulli random set with selector means
`delta_n = log(n)/n`. The source asks whether `T`, like the deterministic
Furstenberg set, is a `Lambda(q)`-set for every finite `q>2`.

The packet proves an affirmative answer: almost surely, simultaneously for
every finite `q>2`, there is a random finite constant `C_(q,T)` such that

`||sum_(n in T) a_n e_n||_q <= C_(q,T) (sum |a_n|^2)^(1/2)`

for every finitely supported coefficient family.

## Proof mechanism

For each fixed nonzero integer coefficient vector, the expected number of
injective relations of that type inside `T` is finite. A relation with maximum
entry `M` has a second entry comparable to `M`; after fixing the other entries,
that second large entry is determined. The expected count is therefore bounded
by a convergent series of size

`sum_M (log M)^(2r-2) / M^2`.

Hence every fixed reduced additive-relation type occurs only finitely often,
almost surely. In a `2m`-th Fourier moment, cancel the common multiplicities on
the two sides. Only finitely many reduced cores remain; arbitrary canceled
pairs contribute a power of the coefficient `ell^2` norm. This proves
`Lambda(2m)` for every integer `m>=2`, and the general finite exponent follows
from monotonicity of `L^p` norms on the circle.

## Verification and novelty

- The proof explicitly separates injective reduced cores from repeated-index
  diagonal padding; independence is used only for the injective cores.
- The moment estimate allows infinitely many padded full relations and bounds
  them by the coefficient `ell^2` norm, rather than incorrectly asserting that
  the full relation set is finite.
- The run indexes were searched for the arXiv id, random Furstenberg sets,
  `Lambda(q)`, `p`-Rider, and selector means `log(n)/n`; no duplicate was found.
- The authors' follow-up, arXiv:2303.06850v1, still says that they do not know
  whether `T` itself has the `Lambda(q)` property proved for a large subset.
- Bounded arXiv-focused and general web searches on 2026-07-19 used the exact
  titles, authors, question wording, and selector sequence. They found the 2021
  source and 2023 follow-up, but no later resolution. This is not an exhaustive
  novelty guarantee.

Human review should focus on the fixed-relation expectation bound and the
reconstruction of an arbitrary moment tuple from its reduced core plus common
diagonal pairs. See `verification.md` and `solution_packet.pdf`.

Ledger: `runs/fa_banach_001/ledger/results/2104.08944_random_furstenberg_lambda_all_finite_p.json`
