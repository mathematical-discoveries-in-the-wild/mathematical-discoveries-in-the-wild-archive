# Full Solution: Question 2 via dual-ball parametrization

Status: `candidate_full_solution_to_question_2`

Run: `fa_banach_001`

Source paper: arXiv:1912.03994, Marek Cuth, Martin Dolezal, Michal Doucha,
and Ondrej Kurka, "Polish spaces of Banach spaces."

Supporting source: arXiv:2204.06834, "Polish spaces of Banach spaces.
Complexity of isometry and isomorphism classes."

## Claim Recorded

Question 2 of arXiv:1912.03994 asks whether, for every isometrically universal
separable Banach space `X` and every admissible topology `tau` on `SB(X)`,
there is a `Sigma^0_2`-measurable map

```text
Phi : P_infty -> (SB(X), tau)
```

such that `X_mu` is linearly isometric to `Phi(mu)` for every
`mu in P_infty`.

This packet proves an affirmative answer.

## Main Theorem

There are a separable Banach space `U` and continuous maps

```text
chi_k : P -> U
```

such that for every pseudonorm `mu in P` and every finite scalar family
`(a_k)`,

```text
|| sum_k a_k chi_k(mu) ||_U = mu(sum_k a_k e_k).
```

Embedding `U` isometrically into any isometrically universal separable Banach
space `X` and setting

```text
Phi(mu) = closed span { chi_k(mu) : k in N }
```

gives the required `Sigma^0_2`-measurable reduction to admissible `SB(X)`.

## Proof Mechanism

The sequel arXiv:2204.06834 constructs a continuous map assigning to each
pseudonorm `mu` its dual unit ball `Omega(mu)` as a compact convex subset of
the Hilbert cube.

For compact convex subsets of a Hilbert space, projecting a fixed dense
sequence onto the moving compact convex set yields continuous dense selections.
Applying this to `Omega(mu)` gives a dense sequence of dual functionals
depending continuously on `mu`. Their coordinate evaluations define the
continuous maps `chi_k`.

The source paper's Lemma 2.10 then upgrades continuous realizing maps
`chi_k` to a `Sigma^0_2`-measurable map into any admissible `SB(X)` topology.

## What This Does Not Claim

This does not solve Question 1 of arXiv:1912.03994. The construction realizes
`X_mu` as a closed subspace of a fixed universal Banach space, but it does not
produce a continuous norm code in `B` or a continuous global independent
coordinate representative sequence.

## Verification

The proof is purely analytic/descriptive-set-theoretic. The delicate continuity
point is uniform continuity of Hilbert-space metric projection on the compact
parameter space of compact convex subsets of the Hilbert cube.

The packet PDF was compiled from `main.tex`. The open-question crops are copied
from the prior 1912.03994 packet and show the source pages containing Questions
1 and 2.

## Search Notes

Cheap local index searches found only the prior fixed-representative partial
packet for Question 1. Web searches on 2026-06-16 for exact phrases from
Question 2 and for author/title combinations found arXiv:1912.03994 and
arXiv:2204.06834, but no explicit answer to Question 2. The present proof uses
the continuous dual-ball lemma from arXiv:2204.06834 and adds the
projection-parametrization argument.
